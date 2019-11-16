"Main interface for cloudsearch type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientBuildSuggestersResponseTypeDef",
    "ClientCreateDomainResponseDomainStatusDocServiceTypeDef",
    "ClientCreateDomainResponseDomainStatusLimitsTypeDef",
    "ClientCreateDomainResponseDomainStatusSearchServiceTypeDef",
    "ClientCreateDomainResponseDomainStatusTypeDef",
    "ClientCreateDomainResponseTypeDef",
    "ClientDefineAnalysisSchemeAnalysisSchemeAnalysisOptionsTypeDef",
    "ClientDefineAnalysisSchemeAnalysisSchemeTypeDef",
    "ClientDefineAnalysisSchemeResponseAnalysisSchemeOptionsAnalysisOptionsTypeDef",
    "ClientDefineAnalysisSchemeResponseAnalysisSchemeOptionsTypeDef",
    "ClientDefineAnalysisSchemeResponseAnalysisSchemeStatusTypeDef",
    "ClientDefineAnalysisSchemeResponseAnalysisSchemeTypeDef",
    "ClientDefineAnalysisSchemeResponseTypeDef",
    "ClientDefineExpressionExpressionTypeDef",
    "ClientDefineExpressionResponseExpressionOptionsTypeDef",
    "ClientDefineExpressionResponseExpressionStatusTypeDef",
    "ClientDefineExpressionResponseExpressionTypeDef",
    "ClientDefineExpressionResponseTypeDef",
    "ClientDefineIndexFieldIndexFieldDateArrayOptionsTypeDef",
    "ClientDefineIndexFieldIndexFieldDateOptionsTypeDef",
    "ClientDefineIndexFieldIndexFieldDoubleArrayOptionsTypeDef",
    "ClientDefineIndexFieldIndexFieldDoubleOptionsTypeDef",
    "ClientDefineIndexFieldIndexFieldIntArrayOptionsTypeDef",
    "ClientDefineIndexFieldIndexFieldIntOptionsTypeDef",
    "ClientDefineIndexFieldIndexFieldLatLonOptionsTypeDef",
    "ClientDefineIndexFieldIndexFieldLiteralArrayOptionsTypeDef",
    "ClientDefineIndexFieldIndexFieldLiteralOptionsTypeDef",
    "ClientDefineIndexFieldIndexFieldTextArrayOptionsTypeDef",
    "ClientDefineIndexFieldIndexFieldTextOptionsTypeDef",
    "ClientDefineIndexFieldIndexFieldTypeDef",
    "ClientDefineIndexFieldResponseIndexFieldOptionsDateArrayOptionsTypeDef",
    "ClientDefineIndexFieldResponseIndexFieldOptionsDateOptionsTypeDef",
    "ClientDefineIndexFieldResponseIndexFieldOptionsDoubleArrayOptionsTypeDef",
    "ClientDefineIndexFieldResponseIndexFieldOptionsDoubleOptionsTypeDef",
    "ClientDefineIndexFieldResponseIndexFieldOptionsIntArrayOptionsTypeDef",
    "ClientDefineIndexFieldResponseIndexFieldOptionsIntOptionsTypeDef",
    "ClientDefineIndexFieldResponseIndexFieldOptionsLatLonOptionsTypeDef",
    "ClientDefineIndexFieldResponseIndexFieldOptionsLiteralArrayOptionsTypeDef",
    "ClientDefineIndexFieldResponseIndexFieldOptionsLiteralOptionsTypeDef",
    "ClientDefineIndexFieldResponseIndexFieldOptionsTextArrayOptionsTypeDef",
    "ClientDefineIndexFieldResponseIndexFieldOptionsTextOptionsTypeDef",
    "ClientDefineIndexFieldResponseIndexFieldOptionsTypeDef",
    "ClientDefineIndexFieldResponseIndexFieldStatusTypeDef",
    "ClientDefineIndexFieldResponseIndexFieldTypeDef",
    "ClientDefineIndexFieldResponseTypeDef",
    "ClientDefineSuggesterResponseSuggesterOptionsDocumentSuggesterOptionsTypeDef",
    "ClientDefineSuggesterResponseSuggesterOptionsTypeDef",
    "ClientDefineSuggesterResponseSuggesterStatusTypeDef",
    "ClientDefineSuggesterResponseSuggesterTypeDef",
    "ClientDefineSuggesterResponseTypeDef",
    "ClientDefineSuggesterSuggesterDocumentSuggesterOptionsTypeDef",
    "ClientDefineSuggesterSuggesterTypeDef",
    "ClientDeleteAnalysisSchemeResponseAnalysisSchemeOptionsAnalysisOptionsTypeDef",
    "ClientDeleteAnalysisSchemeResponseAnalysisSchemeOptionsTypeDef",
    "ClientDeleteAnalysisSchemeResponseAnalysisSchemeStatusTypeDef",
    "ClientDeleteAnalysisSchemeResponseAnalysisSchemeTypeDef",
    "ClientDeleteAnalysisSchemeResponseTypeDef",
    "ClientDeleteDomainResponseDomainStatusDocServiceTypeDef",
    "ClientDeleteDomainResponseDomainStatusLimitsTypeDef",
    "ClientDeleteDomainResponseDomainStatusSearchServiceTypeDef",
    "ClientDeleteDomainResponseDomainStatusTypeDef",
    "ClientDeleteDomainResponseTypeDef",
    "ClientDeleteExpressionResponseExpressionOptionsTypeDef",
    "ClientDeleteExpressionResponseExpressionStatusTypeDef",
    "ClientDeleteExpressionResponseExpressionTypeDef",
    "ClientDeleteExpressionResponseTypeDef",
    "ClientDeleteIndexFieldResponseIndexFieldOptionsDateArrayOptionsTypeDef",
    "ClientDeleteIndexFieldResponseIndexFieldOptionsDateOptionsTypeDef",
    "ClientDeleteIndexFieldResponseIndexFieldOptionsDoubleArrayOptionsTypeDef",
    "ClientDeleteIndexFieldResponseIndexFieldOptionsDoubleOptionsTypeDef",
    "ClientDeleteIndexFieldResponseIndexFieldOptionsIntArrayOptionsTypeDef",
    "ClientDeleteIndexFieldResponseIndexFieldOptionsIntOptionsTypeDef",
    "ClientDeleteIndexFieldResponseIndexFieldOptionsLatLonOptionsTypeDef",
    "ClientDeleteIndexFieldResponseIndexFieldOptionsLiteralArrayOptionsTypeDef",
    "ClientDeleteIndexFieldResponseIndexFieldOptionsLiteralOptionsTypeDef",
    "ClientDeleteIndexFieldResponseIndexFieldOptionsTextArrayOptionsTypeDef",
    "ClientDeleteIndexFieldResponseIndexFieldOptionsTextOptionsTypeDef",
    "ClientDeleteIndexFieldResponseIndexFieldOptionsTypeDef",
    "ClientDeleteIndexFieldResponseIndexFieldStatusTypeDef",
    "ClientDeleteIndexFieldResponseIndexFieldTypeDef",
    "ClientDeleteIndexFieldResponseTypeDef",
    "ClientDeleteSuggesterResponseSuggesterOptionsDocumentSuggesterOptionsTypeDef",
    "ClientDeleteSuggesterResponseSuggesterOptionsTypeDef",
    "ClientDeleteSuggesterResponseSuggesterStatusTypeDef",
    "ClientDeleteSuggesterResponseSuggesterTypeDef",
    "ClientDeleteSuggesterResponseTypeDef",
    "ClientDescribeAnalysisSchemesResponseAnalysisSchemesOptionsAnalysisOptionsTypeDef",
    "ClientDescribeAnalysisSchemesResponseAnalysisSchemesOptionsTypeDef",
    "ClientDescribeAnalysisSchemesResponseAnalysisSchemesStatusTypeDef",
    "ClientDescribeAnalysisSchemesResponseAnalysisSchemesTypeDef",
    "ClientDescribeAnalysisSchemesResponseTypeDef",
    "ClientDescribeAvailabilityOptionsResponseAvailabilityOptionsStatusTypeDef",
    "ClientDescribeAvailabilityOptionsResponseAvailabilityOptionsTypeDef",
    "ClientDescribeAvailabilityOptionsResponseTypeDef",
    "ClientDescribeDomainEndpointOptionsResponseDomainEndpointOptionsOptionsTypeDef",
    "ClientDescribeDomainEndpointOptionsResponseDomainEndpointOptionsStatusTypeDef",
    "ClientDescribeDomainEndpointOptionsResponseDomainEndpointOptionsTypeDef",
    "ClientDescribeDomainEndpointOptionsResponseTypeDef",
    "ClientDescribeDomainsResponseDomainStatusListDocServiceTypeDef",
    "ClientDescribeDomainsResponseDomainStatusListLimitsTypeDef",
    "ClientDescribeDomainsResponseDomainStatusListSearchServiceTypeDef",
    "ClientDescribeDomainsResponseDomainStatusListTypeDef",
    "ClientDescribeDomainsResponseTypeDef",
    "ClientDescribeExpressionsResponseExpressionsOptionsTypeDef",
    "ClientDescribeExpressionsResponseExpressionsStatusTypeDef",
    "ClientDescribeExpressionsResponseExpressionsTypeDef",
    "ClientDescribeExpressionsResponseTypeDef",
    "ClientDescribeIndexFieldsResponseIndexFieldsOptionsDateArrayOptionsTypeDef",
    "ClientDescribeIndexFieldsResponseIndexFieldsOptionsDateOptionsTypeDef",
    "ClientDescribeIndexFieldsResponseIndexFieldsOptionsDoubleArrayOptionsTypeDef",
    "ClientDescribeIndexFieldsResponseIndexFieldsOptionsDoubleOptionsTypeDef",
    "ClientDescribeIndexFieldsResponseIndexFieldsOptionsIntArrayOptionsTypeDef",
    "ClientDescribeIndexFieldsResponseIndexFieldsOptionsIntOptionsTypeDef",
    "ClientDescribeIndexFieldsResponseIndexFieldsOptionsLatLonOptionsTypeDef",
    "ClientDescribeIndexFieldsResponseIndexFieldsOptionsLiteralArrayOptionsTypeDef",
    "ClientDescribeIndexFieldsResponseIndexFieldsOptionsLiteralOptionsTypeDef",
    "ClientDescribeIndexFieldsResponseIndexFieldsOptionsTextArrayOptionsTypeDef",
    "ClientDescribeIndexFieldsResponseIndexFieldsOptionsTextOptionsTypeDef",
    "ClientDescribeIndexFieldsResponseIndexFieldsOptionsTypeDef",
    "ClientDescribeIndexFieldsResponseIndexFieldsStatusTypeDef",
    "ClientDescribeIndexFieldsResponseIndexFieldsTypeDef",
    "ClientDescribeIndexFieldsResponseTypeDef",
    "ClientDescribeScalingParametersResponseScalingParametersOptionsTypeDef",
    "ClientDescribeScalingParametersResponseScalingParametersStatusTypeDef",
    "ClientDescribeScalingParametersResponseScalingParametersTypeDef",
    "ClientDescribeScalingParametersResponseTypeDef",
    "ClientDescribeServiceAccessPoliciesResponseAccessPoliciesStatusTypeDef",
    "ClientDescribeServiceAccessPoliciesResponseAccessPoliciesTypeDef",
    "ClientDescribeServiceAccessPoliciesResponseTypeDef",
    "ClientDescribeSuggestersResponseSuggestersOptionsDocumentSuggesterOptionsTypeDef",
    "ClientDescribeSuggestersResponseSuggestersOptionsTypeDef",
    "ClientDescribeSuggestersResponseSuggestersStatusTypeDef",
    "ClientDescribeSuggestersResponseSuggestersTypeDef",
    "ClientDescribeSuggestersResponseTypeDef",
    "ClientIndexDocumentsResponseTypeDef",
    "ClientListDomainNamesResponseTypeDef",
    "ClientUpdateAvailabilityOptionsResponseAvailabilityOptionsStatusTypeDef",
    "ClientUpdateAvailabilityOptionsResponseAvailabilityOptionsTypeDef",
    "ClientUpdateAvailabilityOptionsResponseTypeDef",
    "ClientUpdateDomainEndpointOptionsDomainEndpointOptionsTypeDef",
    "ClientUpdateDomainEndpointOptionsResponseDomainEndpointOptionsOptionsTypeDef",
    "ClientUpdateDomainEndpointOptionsResponseDomainEndpointOptionsStatusTypeDef",
    "ClientUpdateDomainEndpointOptionsResponseDomainEndpointOptionsTypeDef",
    "ClientUpdateDomainEndpointOptionsResponseTypeDef",
    "ClientUpdateScalingParametersResponseScalingParametersOptionsTypeDef",
    "ClientUpdateScalingParametersResponseScalingParametersStatusTypeDef",
    "ClientUpdateScalingParametersResponseScalingParametersTypeDef",
    "ClientUpdateScalingParametersResponseTypeDef",
    "ClientUpdateScalingParametersScalingParametersTypeDef",
    "ClientUpdateServiceAccessPoliciesResponseAccessPoliciesStatusTypeDef",
    "ClientUpdateServiceAccessPoliciesResponseAccessPoliciesTypeDef",
    "ClientUpdateServiceAccessPoliciesResponseTypeDef",
)


_ClientBuildSuggestersResponseTypeDef = TypedDict(
    "_ClientBuildSuggestersResponseTypeDef", {"FieldNames": List[str]}, total=False
)


class ClientBuildSuggestersResponseTypeDef(_ClientBuildSuggestersResponseTypeDef):
    """
    Type definition for `ClientBuildSuggesters` `Response`

    The result of a ``BuildSuggester`` request. Contains a list of the fields used for suggestions.

    - **FieldNames** *(list) --*

      A list of field names.

      - *(string) --*

        A string that represents the name of an index field. CloudSearch supports regular index
        fields as well as dynamic fields. A dynamic field's name defines a pattern that begins or
        ends with a wildcard. Any document fields that don't map to a regular index field but do
        match a dynamic field's pattern are configured with the dynamic field's indexing options.

        Regular field names begin with a letter and can contain the following characters: a-z
        (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a wildcard
        (*). The wildcard can also be the only character in a dynamic field name. Multiple
        wildcards, and wildcards embedded within a string are not supported.

        The name ``score`` is reserved and cannot be used as a field name. To reference a
        document's ID, you can use the name ``_id`` .
    """


_ClientCreateDomainResponseDomainStatusDocServiceTypeDef = TypedDict(
    "_ClientCreateDomainResponseDomainStatusDocServiceTypeDef",
    {"Endpoint": str},
    total=False,
)


class ClientCreateDomainResponseDomainStatusDocServiceTypeDef(
    _ClientCreateDomainResponseDomainStatusDocServiceTypeDef
):
    """
    Type definition for `ClientCreateDomainResponseDomainStatus` `DocService`

    The service endpoint for updating documents in a search domain.

    - **Endpoint** *(string) --*

      The endpoint to which service requests can be submitted. For example,
      ``search-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.cloudsearch.amazonaws.com`` or
      ``doc-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.cloudsearch.amazonaws.com`` .
    """


_ClientCreateDomainResponseDomainStatusLimitsTypeDef = TypedDict(
    "_ClientCreateDomainResponseDomainStatusLimitsTypeDef",
    {"MaximumReplicationCount": int, "MaximumPartitionCount": int},
    total=False,
)


class ClientCreateDomainResponseDomainStatusLimitsTypeDef(
    _ClientCreateDomainResponseDomainStatusLimitsTypeDef
):
    """
    Type definition for `ClientCreateDomainResponseDomainStatus` `Limits`

    - **MaximumReplicationCount** *(integer) --*

    - **MaximumPartitionCount** *(integer) --*
    """


_ClientCreateDomainResponseDomainStatusSearchServiceTypeDef = TypedDict(
    "_ClientCreateDomainResponseDomainStatusSearchServiceTypeDef",
    {"Endpoint": str},
    total=False,
)


class ClientCreateDomainResponseDomainStatusSearchServiceTypeDef(
    _ClientCreateDomainResponseDomainStatusSearchServiceTypeDef
):
    """
    Type definition for `ClientCreateDomainResponseDomainStatus` `SearchService`

    The service endpoint for requesting search results from a search domain.

    - **Endpoint** *(string) --*

      The endpoint to which service requests can be submitted. For example,
      ``search-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.cloudsearch.amazonaws.com`` or
      ``doc-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.cloudsearch.amazonaws.com`` .
    """


_ClientCreateDomainResponseDomainStatusTypeDef = TypedDict(
    "_ClientCreateDomainResponseDomainStatusTypeDef",
    {
        "DomainId": str,
        "DomainName": str,
        "ARN": str,
        "Created": bool,
        "Deleted": bool,
        "DocService": ClientCreateDomainResponseDomainStatusDocServiceTypeDef,
        "SearchService": ClientCreateDomainResponseDomainStatusSearchServiceTypeDef,
        "RequiresIndexDocuments": bool,
        "Processing": bool,
        "SearchInstanceType": str,
        "SearchPartitionCount": int,
        "SearchInstanceCount": int,
        "Limits": ClientCreateDomainResponseDomainStatusLimitsTypeDef,
    },
    total=False,
)


class ClientCreateDomainResponseDomainStatusTypeDef(
    _ClientCreateDomainResponseDomainStatusTypeDef
):
    """
    Type definition for `ClientCreateDomainResponse` `DomainStatus`

    The current status of the search domain.

    - **DomainId** *(string) --*

      An internally generated unique identifier for a domain.

    - **DomainName** *(string) --*

      A string that represents the name of a domain. Domain names are unique across the domains
      owned by an account within an AWS region. Domain names start with a letter or number and
      can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).

    - **ARN** *(string) --*

      The Amazon Resource Name (ARN) of the search domain. See `Identifiers for IAM Entities
      <http://docs.aws.amazon.com/IAM/latest/UserGuide/index.html?Using_Identifiers.html>`__ in
      *Using AWS Identity and Access Management* for more information.

    - **Created** *(boolean) --*

      True if the search domain is created. It can take several minutes to initialize a domain
      when  CreateDomain is called. Newly created search domains are returned from
      DescribeDomains with a false value for Created until domain creation is complete.

    - **Deleted** *(boolean) --*

      True if the search domain has been deleted. The system must clean up resources dedicated to
      the search domain when  DeleteDomain is called. Newly deleted search domains are returned
      from  DescribeDomains with a true value for IsDeleted for several minutes until resource
      cleanup is complete.

    - **DocService** *(dict) --*

      The service endpoint for updating documents in a search domain.

      - **Endpoint** *(string) --*

        The endpoint to which service requests can be submitted. For example,
        ``search-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.cloudsearch.amazonaws.com`` or
        ``doc-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.cloudsearch.amazonaws.com`` .

    - **SearchService** *(dict) --*

      The service endpoint for requesting search results from a search domain.

      - **Endpoint** *(string) --*

        The endpoint to which service requests can be submitted. For example,
        ``search-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.cloudsearch.amazonaws.com`` or
        ``doc-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.cloudsearch.amazonaws.com`` .

    - **RequiresIndexDocuments** *(boolean) --*

      True if  IndexDocuments needs to be called to activate the current domain configuration.

    - **Processing** *(boolean) --*

      True if processing is being done to activate the current domain configuration.

    - **SearchInstanceType** *(string) --*

      The instance type that is being used to process search requests.

    - **SearchPartitionCount** *(integer) --*

      The number of partitions across which the search index is spread.

    - **SearchInstanceCount** *(integer) --*

      The number of search instances that are available to process search requests.

    - **Limits** *(dict) --*

      - **MaximumReplicationCount** *(integer) --*

      - **MaximumPartitionCount** *(integer) --*
    """


_ClientCreateDomainResponseTypeDef = TypedDict(
    "_ClientCreateDomainResponseTypeDef",
    {"DomainStatus": ClientCreateDomainResponseDomainStatusTypeDef},
    total=False,
)


class ClientCreateDomainResponseTypeDef(_ClientCreateDomainResponseTypeDef):
    """
    Type definition for `ClientCreateDomain` `Response`

    The result of a ``CreateDomainRequest`` . Contains the status of a newly created domain.

    - **DomainStatus** *(dict) --*

      The current status of the search domain.

      - **DomainId** *(string) --*

        An internally generated unique identifier for a domain.

      - **DomainName** *(string) --*

        A string that represents the name of a domain. Domain names are unique across the domains
        owned by an account within an AWS region. Domain names start with a letter or number and
        can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).

      - **ARN** *(string) --*

        The Amazon Resource Name (ARN) of the search domain. See `Identifiers for IAM Entities
        <http://docs.aws.amazon.com/IAM/latest/UserGuide/index.html?Using_Identifiers.html>`__ in
        *Using AWS Identity and Access Management* for more information.

      - **Created** *(boolean) --*

        True if the search domain is created. It can take several minutes to initialize a domain
        when  CreateDomain is called. Newly created search domains are returned from
        DescribeDomains with a false value for Created until domain creation is complete.

      - **Deleted** *(boolean) --*

        True if the search domain has been deleted. The system must clean up resources dedicated to
        the search domain when  DeleteDomain is called. Newly deleted search domains are returned
        from  DescribeDomains with a true value for IsDeleted for several minutes until resource
        cleanup is complete.

      - **DocService** *(dict) --*

        The service endpoint for updating documents in a search domain.

        - **Endpoint** *(string) --*

          The endpoint to which service requests can be submitted. For example,
          ``search-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.cloudsearch.amazonaws.com`` or
          ``doc-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.cloudsearch.amazonaws.com`` .

      - **SearchService** *(dict) --*

        The service endpoint for requesting search results from a search domain.

        - **Endpoint** *(string) --*

          The endpoint to which service requests can be submitted. For example,
          ``search-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.cloudsearch.amazonaws.com`` or
          ``doc-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.cloudsearch.amazonaws.com`` .

      - **RequiresIndexDocuments** *(boolean) --*

        True if  IndexDocuments needs to be called to activate the current domain configuration.

      - **Processing** *(boolean) --*

        True if processing is being done to activate the current domain configuration.

      - **SearchInstanceType** *(string) --*

        The instance type that is being used to process search requests.

      - **SearchPartitionCount** *(integer) --*

        The number of partitions across which the search index is spread.

      - **SearchInstanceCount** *(integer) --*

        The number of search instances that are available to process search requests.

      - **Limits** *(dict) --*

        - **MaximumReplicationCount** *(integer) --*

        - **MaximumPartitionCount** *(integer) --*
    """


_ClientDefineAnalysisSchemeAnalysisSchemeAnalysisOptionsTypeDef = TypedDict(
    "_ClientDefineAnalysisSchemeAnalysisSchemeAnalysisOptionsTypeDef",
    {
        "Synonyms": str,
        "Stopwords": str,
        "StemmingDictionary": str,
        "JapaneseTokenizationDictionary": str,
        "AlgorithmicStemming": str,
    },
    total=False,
)


class ClientDefineAnalysisSchemeAnalysisSchemeAnalysisOptionsTypeDef(
    _ClientDefineAnalysisSchemeAnalysisSchemeAnalysisOptionsTypeDef
):
    """
    Type definition for `ClientDefineAnalysisSchemeAnalysisScheme` `AnalysisOptions`

    Synonyms, stopwords, and stemming options for an analysis scheme. Includes tokenization
    dictionary for Japanese.

    - **Synonyms** *(string) --*

      A JSON object that defines synonym groups and aliases. A synonym group is an array of arrays,
      where each sub-array is a group of terms where each term in the group is considered a synonym
      of every other term in the group. The aliases value is an object that contains a collection
      of string:value pairs where the string specifies a term and the array of values specifies
      each of the aliases for that term. An alias is considered a synonym of the specified term,
      but the term is not considered a synonym of the alias. For more information about specifying
      synonyms, see `Synonyms
      <http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-analysis-schemes.html#synonyms>`__
      in the *Amazon CloudSearch Developer Guide* .

    - **Stopwords** *(string) --*

      A JSON array of terms to ignore during indexing and searching. For example, ``["a", "an",
      "the", "of"]`` . The stopwords dictionary must explicitly list each word you want to ignore.
      Wildcards and regular expressions are not supported.

    - **StemmingDictionary** *(string) --*

      A JSON object that contains a collection of string:value pairs that each map a term to its
      stem. For example, ``{"term1": "stem1", "term2": "stem2", "term3": "stem3"}`` . The stemming
      dictionary is applied in addition to any algorithmic stemming. This enables you to override
      the results of the algorithmic stemming to correct specific cases of overstemming or
      understemming. The maximum size of a stemming dictionary is 500 KB.

    - **JapaneseTokenizationDictionary** *(string) --*

      A JSON array that contains a collection of terms, tokens, readings and part of speech for
      Japanese Tokenizaiton. The Japanese tokenization dictionary enables you to override the
      default tokenization for selected terms. This is only valid for Japanese language fields.

    - **AlgorithmicStemming** *(string) --*

      The level of algorithmic stemming to perform: ``none`` , ``minimal`` , ``light`` , or
      ``full`` . The available levels vary depending on the language. For more information, see
      `Language Specific Text Processing Settings
      <http://docs.aws.amazon.com/cloudsearch/latest/developerguide/text-processing.html#text-processing-settings>`__
      in the *Amazon CloudSearch Developer Guide*
    """


_RequiredClientDefineAnalysisSchemeAnalysisSchemeTypeDef = TypedDict(
    "_RequiredClientDefineAnalysisSchemeAnalysisSchemeTypeDef",
    {"AnalysisSchemeName": str, "AnalysisSchemeLanguage": str},
)
_OptionalClientDefineAnalysisSchemeAnalysisSchemeTypeDef = TypedDict(
    "_OptionalClientDefineAnalysisSchemeAnalysisSchemeTypeDef",
    {"AnalysisOptions": ClientDefineAnalysisSchemeAnalysisSchemeAnalysisOptionsTypeDef},
    total=False,
)


class ClientDefineAnalysisSchemeAnalysisSchemeTypeDef(
    _RequiredClientDefineAnalysisSchemeAnalysisSchemeTypeDef,
    _OptionalClientDefineAnalysisSchemeAnalysisSchemeTypeDef,
):
    """
    Type definition for `ClientDefineAnalysisScheme` `AnalysisScheme`

    Configuration information for an analysis scheme. Each analysis scheme has a unique name and
    specifies the language of the text to be processed. The following options can be configured for
    an analysis scheme: ``Synonyms`` , ``Stopwords`` , ``StemmingDictionary`` ,
    ``JapaneseTokenizationDictionary`` and ``AlgorithmicStemming`` .

    - **AnalysisSchemeName** *(string) --* **[REQUIRED]**

      Names must begin with a letter and can contain the following characters: a-z (lowercase), 0-9,
      and _ (underscore).

    - **AnalysisSchemeLanguage** *(string) --* **[REQUIRED]**

      An `IETF RFC 4646 <http://tools.ietf.org/html/rfc4646>`__ language code or ``mul`` for multiple
      languages.

    - **AnalysisOptions** *(dict) --*

      Synonyms, stopwords, and stemming options for an analysis scheme. Includes tokenization
      dictionary for Japanese.

      - **Synonyms** *(string) --*

        A JSON object that defines synonym groups and aliases. A synonym group is an array of arrays,
        where each sub-array is a group of terms where each term in the group is considered a synonym
        of every other term in the group. The aliases value is an object that contains a collection
        of string:value pairs where the string specifies a term and the array of values specifies
        each of the aliases for that term. An alias is considered a synonym of the specified term,
        but the term is not considered a synonym of the alias. For more information about specifying
        synonyms, see `Synonyms
        <http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-analysis-schemes.html#synonyms>`__
        in the *Amazon CloudSearch Developer Guide* .

      - **Stopwords** *(string) --*

        A JSON array of terms to ignore during indexing and searching. For example, ``["a", "an",
        "the", "of"]`` . The stopwords dictionary must explicitly list each word you want to ignore.
        Wildcards and regular expressions are not supported.

      - **StemmingDictionary** *(string) --*

        A JSON object that contains a collection of string:value pairs that each map a term to its
        stem. For example, ``{"term1": "stem1", "term2": "stem2", "term3": "stem3"}`` . The stemming
        dictionary is applied in addition to any algorithmic stemming. This enables you to override
        the results of the algorithmic stemming to correct specific cases of overstemming or
        understemming. The maximum size of a stemming dictionary is 500 KB.

      - **JapaneseTokenizationDictionary** *(string) --*

        A JSON array that contains a collection of terms, tokens, readings and part of speech for
        Japanese Tokenizaiton. The Japanese tokenization dictionary enables you to override the
        default tokenization for selected terms. This is only valid for Japanese language fields.

      - **AlgorithmicStemming** *(string) --*

        The level of algorithmic stemming to perform: ``none`` , ``minimal`` , ``light`` , or
        ``full`` . The available levels vary depending on the language. For more information, see
        `Language Specific Text Processing Settings
        <http://docs.aws.amazon.com/cloudsearch/latest/developerguide/text-processing.html#text-processing-settings>`__
        in the *Amazon CloudSearch Developer Guide*
    """


_ClientDefineAnalysisSchemeResponseAnalysisSchemeOptionsAnalysisOptionsTypeDef = TypedDict(
    "_ClientDefineAnalysisSchemeResponseAnalysisSchemeOptionsAnalysisOptionsTypeDef",
    {
        "Synonyms": str,
        "Stopwords": str,
        "StemmingDictionary": str,
        "JapaneseTokenizationDictionary": str,
        "AlgorithmicStemming": str,
    },
    total=False,
)


class ClientDefineAnalysisSchemeResponseAnalysisSchemeOptionsAnalysisOptionsTypeDef(
    _ClientDefineAnalysisSchemeResponseAnalysisSchemeOptionsAnalysisOptionsTypeDef
):
    """
    Type definition for `ClientDefineAnalysisSchemeResponseAnalysisSchemeOptions` `AnalysisOptions`

    Synonyms, stopwords, and stemming options for an analysis scheme. Includes tokenization
    dictionary for Japanese.

    - **Synonyms** *(string) --*

      A JSON object that defines synonym groups and aliases. A synonym group is an array of
      arrays, where each sub-array is a group of terms where each term in the group is
      considered a synonym of every other term in the group. The aliases value is an object
      that contains a collection of string:value pairs where the string specifies a term and
      the array of values specifies each of the aliases for that term. An alias is considered
      a synonym of the specified term, but the term is not considered a synonym of the alias.
      For more information about specifying synonyms, see `Synonyms
      <http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-analysis-schemes.html#synonyms>`__
      in the *Amazon CloudSearch Developer Guide* .

    - **Stopwords** *(string) --*

      A JSON array of terms to ignore during indexing and searching. For example, ``["a",
      "an", "the", "of"]`` . The stopwords dictionary must explicitly list each word you want
      to ignore. Wildcards and regular expressions are not supported.

    - **StemmingDictionary** *(string) --*

      A JSON object that contains a collection of string:value pairs that each map a term to
      its stem. For example, ``{"term1": "stem1", "term2": "stem2", "term3": "stem3"}`` . The
      stemming dictionary is applied in addition to any algorithmic stemming. This enables
      you to override the results of the algorithmic stemming to correct specific cases of
      overstemming or understemming. The maximum size of a stemming dictionary is 500 KB.

    - **JapaneseTokenizationDictionary** *(string) --*

      A JSON array that contains a collection of terms, tokens, readings and part of speech
      for Japanese Tokenizaiton. The Japanese tokenization dictionary enables you to override
      the default tokenization for selected terms. This is only valid for Japanese language
      fields.

    - **AlgorithmicStemming** *(string) --*

      The level of algorithmic stemming to perform: ``none`` , ``minimal`` , ``light`` , or
      ``full`` . The available levels vary depending on the language. For more information,
      see `Language Specific Text Processing Settings
      <http://docs.aws.amazon.com/cloudsearch/latest/developerguide/text-processing.html#text-processing-settings>`__
      in the *Amazon CloudSearch Developer Guide*
    """


_ClientDefineAnalysisSchemeResponseAnalysisSchemeOptionsTypeDef = TypedDict(
    "_ClientDefineAnalysisSchemeResponseAnalysisSchemeOptionsTypeDef",
    {
        "AnalysisSchemeName": str,
        "AnalysisSchemeLanguage": str,
        "AnalysisOptions": ClientDefineAnalysisSchemeResponseAnalysisSchemeOptionsAnalysisOptionsTypeDef,
    },
    total=False,
)


class ClientDefineAnalysisSchemeResponseAnalysisSchemeOptionsTypeDef(
    _ClientDefineAnalysisSchemeResponseAnalysisSchemeOptionsTypeDef
):
    """
    Type definition for `ClientDefineAnalysisSchemeResponseAnalysisScheme` `Options`

    Configuration information for an analysis scheme. Each analysis scheme has a unique name
    and specifies the language of the text to be processed. The following options can be
    configured for an analysis scheme: ``Synonyms`` , ``Stopwords`` , ``StemmingDictionary`` ,
    ``JapaneseTokenizationDictionary`` and ``AlgorithmicStemming`` .

    - **AnalysisSchemeName** *(string) --*

      Names must begin with a letter and can contain the following characters: a-z (lowercase),
      0-9, and _ (underscore).

    - **AnalysisSchemeLanguage** *(string) --*

      An `IETF RFC 4646 <http://tools.ietf.org/html/rfc4646>`__ language code or ``mul`` for
      multiple languages.

    - **AnalysisOptions** *(dict) --*

      Synonyms, stopwords, and stemming options for an analysis scheme. Includes tokenization
      dictionary for Japanese.

      - **Synonyms** *(string) --*

        A JSON object that defines synonym groups and aliases. A synonym group is an array of
        arrays, where each sub-array is a group of terms where each term in the group is
        considered a synonym of every other term in the group. The aliases value is an object
        that contains a collection of string:value pairs where the string specifies a term and
        the array of values specifies each of the aliases for that term. An alias is considered
        a synonym of the specified term, but the term is not considered a synonym of the alias.
        For more information about specifying synonyms, see `Synonyms
        <http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-analysis-schemes.html#synonyms>`__
        in the *Amazon CloudSearch Developer Guide* .

      - **Stopwords** *(string) --*

        A JSON array of terms to ignore during indexing and searching. For example, ``["a",
        "an", "the", "of"]`` . The stopwords dictionary must explicitly list each word you want
        to ignore. Wildcards and regular expressions are not supported.

      - **StemmingDictionary** *(string) --*

        A JSON object that contains a collection of string:value pairs that each map a term to
        its stem. For example, ``{"term1": "stem1", "term2": "stem2", "term3": "stem3"}`` . The
        stemming dictionary is applied in addition to any algorithmic stemming. This enables
        you to override the results of the algorithmic stemming to correct specific cases of
        overstemming or understemming. The maximum size of a stemming dictionary is 500 KB.

      - **JapaneseTokenizationDictionary** *(string) --*

        A JSON array that contains a collection of terms, tokens, readings and part of speech
        for Japanese Tokenizaiton. The Japanese tokenization dictionary enables you to override
        the default tokenization for selected terms. This is only valid for Japanese language
        fields.

      - **AlgorithmicStemming** *(string) --*

        The level of algorithmic stemming to perform: ``none`` , ``minimal`` , ``light`` , or
        ``full`` . The available levels vary depending on the language. For more information,
        see `Language Specific Text Processing Settings
        <http://docs.aws.amazon.com/cloudsearch/latest/developerguide/text-processing.html#text-processing-settings>`__
        in the *Amazon CloudSearch Developer Guide*
    """


_ClientDefineAnalysisSchemeResponseAnalysisSchemeStatusTypeDef = TypedDict(
    "_ClientDefineAnalysisSchemeResponseAnalysisSchemeStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": str,
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientDefineAnalysisSchemeResponseAnalysisSchemeStatusTypeDef(
    _ClientDefineAnalysisSchemeResponseAnalysisSchemeStatusTypeDef
):
    """
    Type definition for `ClientDefineAnalysisSchemeResponseAnalysisScheme` `Status`

    The status of domain configuration option.

    - **CreationDate** *(datetime) --*

      A timestamp for when this option was created.

    - **UpdateDate** *(datetime) --*

      A timestamp for when this option was last updated.

    - **UpdateVersion** *(integer) --*

      A unique integer that indicates when this option was last updated.

    - **State** *(string) --*

      The state of processing a change to an option. Possible values:

      * ``RequiresIndexDocuments`` : the option's latest value will not be deployed until
      IndexDocuments has been called and indexing is complete.

      * ``Processing`` : the option's latest value is in the process of being activated.

      * ``Active`` : the option's latest value is completely deployed.

      * ``FailedToValidate`` : the option value is not compatible with the domain's data and
      cannot be used to index the data. You must either modify the option value or update or
      remove the incompatible documents.

    - **PendingDeletion** *(boolean) --*

      Indicates that the option will be deleted once processing is complete.
    """


_ClientDefineAnalysisSchemeResponseAnalysisSchemeTypeDef = TypedDict(
    "_ClientDefineAnalysisSchemeResponseAnalysisSchemeTypeDef",
    {
        "Options": ClientDefineAnalysisSchemeResponseAnalysisSchemeOptionsTypeDef,
        "Status": ClientDefineAnalysisSchemeResponseAnalysisSchemeStatusTypeDef,
    },
    total=False,
)


class ClientDefineAnalysisSchemeResponseAnalysisSchemeTypeDef(
    _ClientDefineAnalysisSchemeResponseAnalysisSchemeTypeDef
):
    """
    Type definition for `ClientDefineAnalysisSchemeResponse` `AnalysisScheme`

    The status and configuration of an ``AnalysisScheme`` .

    - **Options** *(dict) --*

      Configuration information for an analysis scheme. Each analysis scheme has a unique name
      and specifies the language of the text to be processed. The following options can be
      configured for an analysis scheme: ``Synonyms`` , ``Stopwords`` , ``StemmingDictionary`` ,
      ``JapaneseTokenizationDictionary`` and ``AlgorithmicStemming`` .

      - **AnalysisSchemeName** *(string) --*

        Names must begin with a letter and can contain the following characters: a-z (lowercase),
        0-9, and _ (underscore).

      - **AnalysisSchemeLanguage** *(string) --*

        An `IETF RFC 4646 <http://tools.ietf.org/html/rfc4646>`__ language code or ``mul`` for
        multiple languages.

      - **AnalysisOptions** *(dict) --*

        Synonyms, stopwords, and stemming options for an analysis scheme. Includes tokenization
        dictionary for Japanese.

        - **Synonyms** *(string) --*

          A JSON object that defines synonym groups and aliases. A synonym group is an array of
          arrays, where each sub-array is a group of terms where each term in the group is
          considered a synonym of every other term in the group. The aliases value is an object
          that contains a collection of string:value pairs where the string specifies a term and
          the array of values specifies each of the aliases for that term. An alias is considered
          a synonym of the specified term, but the term is not considered a synonym of the alias.
          For more information about specifying synonyms, see `Synonyms
          <http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-analysis-schemes.html#synonyms>`__
          in the *Amazon CloudSearch Developer Guide* .

        - **Stopwords** *(string) --*

          A JSON array of terms to ignore during indexing and searching. For example, ``["a",
          "an", "the", "of"]`` . The stopwords dictionary must explicitly list each word you want
          to ignore. Wildcards and regular expressions are not supported.

        - **StemmingDictionary** *(string) --*

          A JSON object that contains a collection of string:value pairs that each map a term to
          its stem. For example, ``{"term1": "stem1", "term2": "stem2", "term3": "stem3"}`` . The
          stemming dictionary is applied in addition to any algorithmic stemming. This enables
          you to override the results of the algorithmic stemming to correct specific cases of
          overstemming or understemming. The maximum size of a stemming dictionary is 500 KB.

        - **JapaneseTokenizationDictionary** *(string) --*

          A JSON array that contains a collection of terms, tokens, readings and part of speech
          for Japanese Tokenizaiton. The Japanese tokenization dictionary enables you to override
          the default tokenization for selected terms. This is only valid for Japanese language
          fields.

        - **AlgorithmicStemming** *(string) --*

          The level of algorithmic stemming to perform: ``none`` , ``minimal`` , ``light`` , or
          ``full`` . The available levels vary depending on the language. For more information,
          see `Language Specific Text Processing Settings
          <http://docs.aws.amazon.com/cloudsearch/latest/developerguide/text-processing.html#text-processing-settings>`__
          in the *Amazon CloudSearch Developer Guide*

    - **Status** *(dict) --*

      The status of domain configuration option.

      - **CreationDate** *(datetime) --*

        A timestamp for when this option was created.

      - **UpdateDate** *(datetime) --*

        A timestamp for when this option was last updated.

      - **UpdateVersion** *(integer) --*

        A unique integer that indicates when this option was last updated.

      - **State** *(string) --*

        The state of processing a change to an option. Possible values:

        * ``RequiresIndexDocuments`` : the option's latest value will not be deployed until
        IndexDocuments has been called and indexing is complete.

        * ``Processing`` : the option's latest value is in the process of being activated.

        * ``Active`` : the option's latest value is completely deployed.

        * ``FailedToValidate`` : the option value is not compatible with the domain's data and
        cannot be used to index the data. You must either modify the option value or update or
        remove the incompatible documents.

      - **PendingDeletion** *(boolean) --*

        Indicates that the option will be deleted once processing is complete.
    """


_ClientDefineAnalysisSchemeResponseTypeDef = TypedDict(
    "_ClientDefineAnalysisSchemeResponseTypeDef",
    {"AnalysisScheme": ClientDefineAnalysisSchemeResponseAnalysisSchemeTypeDef},
    total=False,
)


class ClientDefineAnalysisSchemeResponseTypeDef(
    _ClientDefineAnalysisSchemeResponseTypeDef
):
    """
    Type definition for `ClientDefineAnalysisScheme` `Response`

    The result of a `` DefineAnalysisScheme`` request. Contains the status of the newly-configured
    analysis scheme.

    - **AnalysisScheme** *(dict) --*

      The status and configuration of an ``AnalysisScheme`` .

      - **Options** *(dict) --*

        Configuration information for an analysis scheme. Each analysis scheme has a unique name
        and specifies the language of the text to be processed. The following options can be
        configured for an analysis scheme: ``Synonyms`` , ``Stopwords`` , ``StemmingDictionary`` ,
        ``JapaneseTokenizationDictionary`` and ``AlgorithmicStemming`` .

        - **AnalysisSchemeName** *(string) --*

          Names must begin with a letter and can contain the following characters: a-z (lowercase),
          0-9, and _ (underscore).

        - **AnalysisSchemeLanguage** *(string) --*

          An `IETF RFC 4646 <http://tools.ietf.org/html/rfc4646>`__ language code or ``mul`` for
          multiple languages.

        - **AnalysisOptions** *(dict) --*

          Synonyms, stopwords, and stemming options for an analysis scheme. Includes tokenization
          dictionary for Japanese.

          - **Synonyms** *(string) --*

            A JSON object that defines synonym groups and aliases. A synonym group is an array of
            arrays, where each sub-array is a group of terms where each term in the group is
            considered a synonym of every other term in the group. The aliases value is an object
            that contains a collection of string:value pairs where the string specifies a term and
            the array of values specifies each of the aliases for that term. An alias is considered
            a synonym of the specified term, but the term is not considered a synonym of the alias.
            For more information about specifying synonyms, see `Synonyms
            <http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-analysis-schemes.html#synonyms>`__
            in the *Amazon CloudSearch Developer Guide* .

          - **Stopwords** *(string) --*

            A JSON array of terms to ignore during indexing and searching. For example, ``["a",
            "an", "the", "of"]`` . The stopwords dictionary must explicitly list each word you want
            to ignore. Wildcards and regular expressions are not supported.

          - **StemmingDictionary** *(string) --*

            A JSON object that contains a collection of string:value pairs that each map a term to
            its stem. For example, ``{"term1": "stem1", "term2": "stem2", "term3": "stem3"}`` . The
            stemming dictionary is applied in addition to any algorithmic stemming. This enables
            you to override the results of the algorithmic stemming to correct specific cases of
            overstemming or understemming. The maximum size of a stemming dictionary is 500 KB.

          - **JapaneseTokenizationDictionary** *(string) --*

            A JSON array that contains a collection of terms, tokens, readings and part of speech
            for Japanese Tokenizaiton. The Japanese tokenization dictionary enables you to override
            the default tokenization for selected terms. This is only valid for Japanese language
            fields.

          - **AlgorithmicStemming** *(string) --*

            The level of algorithmic stemming to perform: ``none`` , ``minimal`` , ``light`` , or
            ``full`` . The available levels vary depending on the language. For more information,
            see `Language Specific Text Processing Settings
            <http://docs.aws.amazon.com/cloudsearch/latest/developerguide/text-processing.html#text-processing-settings>`__
            in the *Amazon CloudSearch Developer Guide*

      - **Status** *(dict) --*

        The status of domain configuration option.

        - **CreationDate** *(datetime) --*

          A timestamp for when this option was created.

        - **UpdateDate** *(datetime) --*

          A timestamp for when this option was last updated.

        - **UpdateVersion** *(integer) --*

          A unique integer that indicates when this option was last updated.

        - **State** *(string) --*

          The state of processing a change to an option. Possible values:

          * ``RequiresIndexDocuments`` : the option's latest value will not be deployed until
          IndexDocuments has been called and indexing is complete.

          * ``Processing`` : the option's latest value is in the process of being activated.

          * ``Active`` : the option's latest value is completely deployed.

          * ``FailedToValidate`` : the option value is not compatible with the domain's data and
          cannot be used to index the data. You must either modify the option value or update or
          remove the incompatible documents.

        - **PendingDeletion** *(boolean) --*

          Indicates that the option will be deleted once processing is complete.
    """


_ClientDefineExpressionExpressionTypeDef = TypedDict(
    "_ClientDefineExpressionExpressionTypeDef",
    {"ExpressionName": str, "ExpressionValue": str},
)


class ClientDefineExpressionExpressionTypeDef(_ClientDefineExpressionExpressionTypeDef):
    """
    Type definition for `ClientDefineExpression` `Expression`

    A named expression that can be evaluated at search time. Can be used to sort the search results,
    define other expressions, or return computed information in the search results.

    - **ExpressionName** *(string) --* **[REQUIRED]**

      Names must begin with a letter and can contain the following characters: a-z (lowercase), 0-9,
      and _ (underscore).

    - **ExpressionValue** *(string) --* **[REQUIRED]**

      The expression to evaluate for sorting while processing a search request. The ``Expression``
      syntax is based on JavaScript expressions. For more information, see `Configuring Expressions
      <http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-expressions.html>`__
      in the *Amazon CloudSearch Developer Guide* .
    """


_ClientDefineExpressionResponseExpressionOptionsTypeDef = TypedDict(
    "_ClientDefineExpressionResponseExpressionOptionsTypeDef",
    {"ExpressionName": str, "ExpressionValue": str},
    total=False,
)


class ClientDefineExpressionResponseExpressionOptionsTypeDef(
    _ClientDefineExpressionResponseExpressionOptionsTypeDef
):
    """
    Type definition for `ClientDefineExpressionResponseExpression` `Options`

    The expression that is evaluated for sorting while processing a search request.

    - **ExpressionName** *(string) --*

      Names must begin with a letter and can contain the following characters: a-z (lowercase),
      0-9, and _ (underscore).

    - **ExpressionValue** *(string) --*

      The expression to evaluate for sorting while processing a search request. The
      ``Expression`` syntax is based on JavaScript expressions. For more information, see
      `Configuring Expressions
      <http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-expressions.html>`__
      in the *Amazon CloudSearch Developer Guide* .
    """


_ClientDefineExpressionResponseExpressionStatusTypeDef = TypedDict(
    "_ClientDefineExpressionResponseExpressionStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": str,
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientDefineExpressionResponseExpressionStatusTypeDef(
    _ClientDefineExpressionResponseExpressionStatusTypeDef
):
    """
    Type definition for `ClientDefineExpressionResponseExpression` `Status`

    The status of domain configuration option.

    - **CreationDate** *(datetime) --*

      A timestamp for when this option was created.

    - **UpdateDate** *(datetime) --*

      A timestamp for when this option was last updated.

    - **UpdateVersion** *(integer) --*

      A unique integer that indicates when this option was last updated.

    - **State** *(string) --*

      The state of processing a change to an option. Possible values:

      * ``RequiresIndexDocuments`` : the option's latest value will not be deployed until
      IndexDocuments has been called and indexing is complete.

      * ``Processing`` : the option's latest value is in the process of being activated.

      * ``Active`` : the option's latest value is completely deployed.

      * ``FailedToValidate`` : the option value is not compatible with the domain's data and
      cannot be used to index the data. You must either modify the option value or update or
      remove the incompatible documents.

    - **PendingDeletion** *(boolean) --*

      Indicates that the option will be deleted once processing is complete.
    """


_ClientDefineExpressionResponseExpressionTypeDef = TypedDict(
    "_ClientDefineExpressionResponseExpressionTypeDef",
    {
        "Options": ClientDefineExpressionResponseExpressionOptionsTypeDef,
        "Status": ClientDefineExpressionResponseExpressionStatusTypeDef,
    },
    total=False,
)


class ClientDefineExpressionResponseExpressionTypeDef(
    _ClientDefineExpressionResponseExpressionTypeDef
):
    """
    Type definition for `ClientDefineExpressionResponse` `Expression`

    The value of an ``Expression`` and its current status.

    - **Options** *(dict) --*

      The expression that is evaluated for sorting while processing a search request.

      - **ExpressionName** *(string) --*

        Names must begin with a letter and can contain the following characters: a-z (lowercase),
        0-9, and _ (underscore).

      - **ExpressionValue** *(string) --*

        The expression to evaluate for sorting while processing a search request. The
        ``Expression`` syntax is based on JavaScript expressions. For more information, see
        `Configuring Expressions
        <http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-expressions.html>`__
        in the *Amazon CloudSearch Developer Guide* .

    - **Status** *(dict) --*

      The status of domain configuration option.

      - **CreationDate** *(datetime) --*

        A timestamp for when this option was created.

      - **UpdateDate** *(datetime) --*

        A timestamp for when this option was last updated.

      - **UpdateVersion** *(integer) --*

        A unique integer that indicates when this option was last updated.

      - **State** *(string) --*

        The state of processing a change to an option. Possible values:

        * ``RequiresIndexDocuments`` : the option's latest value will not be deployed until
        IndexDocuments has been called and indexing is complete.

        * ``Processing`` : the option's latest value is in the process of being activated.

        * ``Active`` : the option's latest value is completely deployed.

        * ``FailedToValidate`` : the option value is not compatible with the domain's data and
        cannot be used to index the data. You must either modify the option value or update or
        remove the incompatible documents.

      - **PendingDeletion** *(boolean) --*

        Indicates that the option will be deleted once processing is complete.
    """


_ClientDefineExpressionResponseTypeDef = TypedDict(
    "_ClientDefineExpressionResponseTypeDef",
    {"Expression": ClientDefineExpressionResponseExpressionTypeDef},
    total=False,
)


class ClientDefineExpressionResponseTypeDef(_ClientDefineExpressionResponseTypeDef):
    """
    Type definition for `ClientDefineExpression` `Response`

    The result of a ``DefineExpression`` request. Contains the status of the newly-configured
    expression.

    - **Expression** *(dict) --*

      The value of an ``Expression`` and its current status.

      - **Options** *(dict) --*

        The expression that is evaluated for sorting while processing a search request.

        - **ExpressionName** *(string) --*

          Names must begin with a letter and can contain the following characters: a-z (lowercase),
          0-9, and _ (underscore).

        - **ExpressionValue** *(string) --*

          The expression to evaluate for sorting while processing a search request. The
          ``Expression`` syntax is based on JavaScript expressions. For more information, see
          `Configuring Expressions
          <http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-expressions.html>`__
          in the *Amazon CloudSearch Developer Guide* .

      - **Status** *(dict) --*

        The status of domain configuration option.

        - **CreationDate** *(datetime) --*

          A timestamp for when this option was created.

        - **UpdateDate** *(datetime) --*

          A timestamp for when this option was last updated.

        - **UpdateVersion** *(integer) --*

          A unique integer that indicates when this option was last updated.

        - **State** *(string) --*

          The state of processing a change to an option. Possible values:

          * ``RequiresIndexDocuments`` : the option's latest value will not be deployed until
          IndexDocuments has been called and indexing is complete.

          * ``Processing`` : the option's latest value is in the process of being activated.

          * ``Active`` : the option's latest value is completely deployed.

          * ``FailedToValidate`` : the option value is not compatible with the domain's data and
          cannot be used to index the data. You must either modify the option value or update or
          remove the incompatible documents.

        - **PendingDeletion** *(boolean) --*

          Indicates that the option will be deleted once processing is complete.
    """


_ClientDefineIndexFieldIndexFieldDateArrayOptionsTypeDef = TypedDict(
    "_ClientDefineIndexFieldIndexFieldDateArrayOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceFields": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
    },
    total=False,
)


class ClientDefineIndexFieldIndexFieldDateArrayOptionsTypeDef(
    _ClientDefineIndexFieldIndexFieldDateArrayOptionsTypeDef
):
    """
    Type definition for `ClientDefineIndexFieldIndexField` `DateArrayOptions`

    Options for a field that contains an array of dates. Present if ``IndexFieldType`` specifies
    the field is of type ``date-array`` . All options are enabled by default.

    - **DefaultValue** *(string) --* A value to use for the field if the field isn't specified for
    a document.

    - **SourceFields** *(string) --*

      A list of source fields to map to the field.

    - **FacetEnabled** *(boolean) --*

      Whether facet information can be returned for the field.

    - **SearchEnabled** *(boolean) --*

      Whether the contents of the field are searchable.

    - **ReturnEnabled** *(boolean) --*

      Whether the contents of the field can be returned in the search results.
    """


_ClientDefineIndexFieldIndexFieldDateOptionsTypeDef = TypedDict(
    "_ClientDefineIndexFieldIndexFieldDateOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)


class ClientDefineIndexFieldIndexFieldDateOptionsTypeDef(
    _ClientDefineIndexFieldIndexFieldDateOptionsTypeDef
):
    """
    Type definition for `ClientDefineIndexFieldIndexField` `DateOptions`

    Options for a date field. Dates and times are specified in UTC (Coordinated Universal Time)
    according to IETF RFC3339: yyyy-mm-ddT00:00:00Z. Present if ``IndexFieldType`` specifies the
    field is of type ``date`` . All options are enabled by default.

    - **DefaultValue** *(string) --* A value to use for the field if the field isn't specified for
    a document.

    - **SourceField** *(string) --*

      A string that represents the name of an index field. CloudSearch supports regular index
      fields as well as dynamic fields. A dynamic field's name defines a pattern that begins or
      ends with a wildcard. Any document fields that don't map to a regular index field but do
      match a dynamic field's pattern are configured with the dynamic field's indexing options.

      Regular field names begin with a letter and can contain the following characters: a-z
      (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a wildcard
      (*). The wildcard can also be the only character in a dynamic field name. Multiple wildcards,
      and wildcards embedded within a string are not supported.

      The name ``score`` is reserved and cannot be used as a field name. To reference a document's
      ID, you can use the name ``_id`` .

    - **FacetEnabled** *(boolean) --*

      Whether facet information can be returned for the field.

    - **SearchEnabled** *(boolean) --*

      Whether the contents of the field are searchable.

    - **ReturnEnabled** *(boolean) --*

      Whether the contents of the field can be returned in the search results.

    - **SortEnabled** *(boolean) --*

      Whether the field can be used to sort the search results.
    """


_ClientDefineIndexFieldIndexFieldDoubleArrayOptionsTypeDef = TypedDict(
    "_ClientDefineIndexFieldIndexFieldDoubleArrayOptionsTypeDef",
    {
        "DefaultValue": float,
        "SourceFields": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
    },
    total=False,
)


class ClientDefineIndexFieldIndexFieldDoubleArrayOptionsTypeDef(
    _ClientDefineIndexFieldIndexFieldDoubleArrayOptionsTypeDef
):
    """
    Type definition for `ClientDefineIndexFieldIndexField` `DoubleArrayOptions`

    Options for a field that contains an array of double-precision 64-bit floating point values.
    Present if ``IndexFieldType`` specifies the field is of type ``double-array`` . All options are
    enabled by default.

    - **DefaultValue** *(float) --* A value to use for the field if the field isn't specified for a
    document.

    - **SourceFields** *(string) --*

      A list of source fields to map to the field.

    - **FacetEnabled** *(boolean) --*

      Whether facet information can be returned for the field.

    - **SearchEnabled** *(boolean) --*

      Whether the contents of the field are searchable.

    - **ReturnEnabled** *(boolean) --*

      Whether the contents of the field can be returned in the search results.
    """


_ClientDefineIndexFieldIndexFieldDoubleOptionsTypeDef = TypedDict(
    "_ClientDefineIndexFieldIndexFieldDoubleOptionsTypeDef",
    {
        "DefaultValue": float,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)


class ClientDefineIndexFieldIndexFieldDoubleOptionsTypeDef(
    _ClientDefineIndexFieldIndexFieldDoubleOptionsTypeDef
):
    """
    Type definition for `ClientDefineIndexFieldIndexField` `DoubleOptions`

    Options for a double-precision 64-bit floating point field. Present if ``IndexFieldType``
    specifies the field is of type ``double`` . All options are enabled by default.

    - **DefaultValue** *(float) --*

      A value to use for the field if the field isn't specified for a document. This can be
      important if you are using the field in an expression and that field is not present in every
      document.

    - **SourceField** *(string) --*

      The name of the source field to map to the field.

    - **FacetEnabled** *(boolean) --*

      Whether facet information can be returned for the field.

    - **SearchEnabled** *(boolean) --*

      Whether the contents of the field are searchable.

    - **ReturnEnabled** *(boolean) --*

      Whether the contents of the field can be returned in the search results.

    - **SortEnabled** *(boolean) --*

      Whether the field can be used to sort the search results.
    """


_ClientDefineIndexFieldIndexFieldIntArrayOptionsTypeDef = TypedDict(
    "_ClientDefineIndexFieldIndexFieldIntArrayOptionsTypeDef",
    {
        "DefaultValue": int,
        "SourceFields": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
    },
    total=False,
)


class ClientDefineIndexFieldIndexFieldIntArrayOptionsTypeDef(
    _ClientDefineIndexFieldIndexFieldIntArrayOptionsTypeDef
):
    """
    Type definition for `ClientDefineIndexFieldIndexField` `IntArrayOptions`

    Options for a field that contains an array of 64-bit signed integers. Present if
    ``IndexFieldType`` specifies the field is of type ``int-array`` . All options are enabled by
    default.

    - **DefaultValue** *(integer) --* A value to use for the field if the field isn't specified for
    a document.

    - **SourceFields** *(string) --*

      A list of source fields to map to the field.

    - **FacetEnabled** *(boolean) --*

      Whether facet information can be returned for the field.

    - **SearchEnabled** *(boolean) --*

      Whether the contents of the field are searchable.

    - **ReturnEnabled** *(boolean) --*

      Whether the contents of the field can be returned in the search results.
    """


_ClientDefineIndexFieldIndexFieldIntOptionsTypeDef = TypedDict(
    "_ClientDefineIndexFieldIndexFieldIntOptionsTypeDef",
    {
        "DefaultValue": int,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)


class ClientDefineIndexFieldIndexFieldIntOptionsTypeDef(
    _ClientDefineIndexFieldIndexFieldIntOptionsTypeDef
):
    """
    Type definition for `ClientDefineIndexFieldIndexField` `IntOptions`

    Options for a 64-bit signed integer field. Present if ``IndexFieldType`` specifies the field is
    of type ``int`` . All options are enabled by default.

    - **DefaultValue** *(integer) --* A value to use for the field if the field isn't specified for
    a document. This can be important if you are using the field in an expression and that field is
    not present in every document.

    - **SourceField** *(string) --*

      The name of the source field to map to the field.

    - **FacetEnabled** *(boolean) --*

      Whether facet information can be returned for the field.

    - **SearchEnabled** *(boolean) --*

      Whether the contents of the field are searchable.

    - **ReturnEnabled** *(boolean) --*

      Whether the contents of the field can be returned in the search results.

    - **SortEnabled** *(boolean) --*

      Whether the field can be used to sort the search results.
    """


_ClientDefineIndexFieldIndexFieldLatLonOptionsTypeDef = TypedDict(
    "_ClientDefineIndexFieldIndexFieldLatLonOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)


class ClientDefineIndexFieldIndexFieldLatLonOptionsTypeDef(
    _ClientDefineIndexFieldIndexFieldLatLonOptionsTypeDef
):
    """
    Type definition for `ClientDefineIndexFieldIndexField` `LatLonOptions`

    Options for a latlon field. A latlon field contains a location stored as a latitude and
    longitude value pair. Present if ``IndexFieldType`` specifies the field is of type ``latlon`` .
    All options are enabled by default.

    - **DefaultValue** *(string) --* A value to use for the field if the field isn't specified for
    a document.

    - **SourceField** *(string) --*

      A string that represents the name of an index field. CloudSearch supports regular index
      fields as well as dynamic fields. A dynamic field's name defines a pattern that begins or
      ends with a wildcard. Any document fields that don't map to a regular index field but do
      match a dynamic field's pattern are configured with the dynamic field's indexing options.

      Regular field names begin with a letter and can contain the following characters: a-z
      (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a wildcard
      (*). The wildcard can also be the only character in a dynamic field name. Multiple wildcards,
      and wildcards embedded within a string are not supported.

      The name ``score`` is reserved and cannot be used as a field name. To reference a document's
      ID, you can use the name ``_id`` .

    - **FacetEnabled** *(boolean) --*

      Whether facet information can be returned for the field.

    - **SearchEnabled** *(boolean) --*

      Whether the contents of the field are searchable.

    - **ReturnEnabled** *(boolean) --*

      Whether the contents of the field can be returned in the search results.

    - **SortEnabled** *(boolean) --*

      Whether the field can be used to sort the search results.
    """


_ClientDefineIndexFieldIndexFieldLiteralArrayOptionsTypeDef = TypedDict(
    "_ClientDefineIndexFieldIndexFieldLiteralArrayOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceFields": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
    },
    total=False,
)


class ClientDefineIndexFieldIndexFieldLiteralArrayOptionsTypeDef(
    _ClientDefineIndexFieldIndexFieldLiteralArrayOptionsTypeDef
):
    """
    Type definition for `ClientDefineIndexFieldIndexField` `LiteralArrayOptions`

    Options for a field that contains an array of literal strings. Present if ``IndexFieldType``
    specifies the field is of type ``literal-array`` . All options are enabled by default.

    - **DefaultValue** *(string) --* A value to use for the field if the field isn't specified for
    a document.

    - **SourceFields** *(string) --*

      A list of source fields to map to the field.

    - **FacetEnabled** *(boolean) --*

      Whether facet information can be returned for the field.

    - **SearchEnabled** *(boolean) --*

      Whether the contents of the field are searchable.

    - **ReturnEnabled** *(boolean) --*

      Whether the contents of the field can be returned in the search results.
    """


_ClientDefineIndexFieldIndexFieldLiteralOptionsTypeDef = TypedDict(
    "_ClientDefineIndexFieldIndexFieldLiteralOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)


class ClientDefineIndexFieldIndexFieldLiteralOptionsTypeDef(
    _ClientDefineIndexFieldIndexFieldLiteralOptionsTypeDef
):
    """
    Type definition for `ClientDefineIndexFieldIndexField` `LiteralOptions`

    Options for literal field. Present if ``IndexFieldType`` specifies the field is of type
    ``literal`` . All options are enabled by default.

    - **DefaultValue** *(string) --* A value to use for the field if the field isn't specified for
    a document.

    - **SourceField** *(string) --*

      A string that represents the name of an index field. CloudSearch supports regular index
      fields as well as dynamic fields. A dynamic field's name defines a pattern that begins or
      ends with a wildcard. Any document fields that don't map to a regular index field but do
      match a dynamic field's pattern are configured with the dynamic field's indexing options.

      Regular field names begin with a letter and can contain the following characters: a-z
      (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a wildcard
      (*). The wildcard can also be the only character in a dynamic field name. Multiple wildcards,
      and wildcards embedded within a string are not supported.

      The name ``score`` is reserved and cannot be used as a field name. To reference a document's
      ID, you can use the name ``_id`` .

    - **FacetEnabled** *(boolean) --*

      Whether facet information can be returned for the field.

    - **SearchEnabled** *(boolean) --*

      Whether the contents of the field are searchable.

    - **ReturnEnabled** *(boolean) --*

      Whether the contents of the field can be returned in the search results.

    - **SortEnabled** *(boolean) --*

      Whether the field can be used to sort the search results.
    """


_ClientDefineIndexFieldIndexFieldTextArrayOptionsTypeDef = TypedDict(
    "_ClientDefineIndexFieldIndexFieldTextArrayOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceFields": str,
        "ReturnEnabled": bool,
        "HighlightEnabled": bool,
        "AnalysisScheme": str,
    },
    total=False,
)


class ClientDefineIndexFieldIndexFieldTextArrayOptionsTypeDef(
    _ClientDefineIndexFieldIndexFieldTextArrayOptionsTypeDef
):
    """
    Type definition for `ClientDefineIndexFieldIndexField` `TextArrayOptions`

    Options for a field that contains an array of text strings. Present if ``IndexFieldType``
    specifies the field is of type ``text-array`` . A ``text-array`` field is always searchable.
    All options are enabled by default.

    - **DefaultValue** *(string) --* A value to use for the field if the field isn't specified for
    a document.

    - **SourceFields** *(string) --*

      A list of source fields to map to the field.

    - **ReturnEnabled** *(boolean) --*

      Whether the contents of the field can be returned in the search results.

    - **HighlightEnabled** *(boolean) --*

      Whether highlights can be returned for the field.

    - **AnalysisScheme** *(string) --*

      The name of an analysis scheme for a ``text-array`` field.
    """


_ClientDefineIndexFieldIndexFieldTextOptionsTypeDef = TypedDict(
    "_ClientDefineIndexFieldIndexFieldTextOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceField": str,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
        "HighlightEnabled": bool,
        "AnalysisScheme": str,
    },
    total=False,
)


class ClientDefineIndexFieldIndexFieldTextOptionsTypeDef(
    _ClientDefineIndexFieldIndexFieldTextOptionsTypeDef
):
    """
    Type definition for `ClientDefineIndexFieldIndexField` `TextOptions`

    Options for text field. Present if ``IndexFieldType`` specifies the field is of type ``text`` .
    A ``text`` field is always searchable. All options are enabled by default.

    - **DefaultValue** *(string) --* A value to use for the field if the field isn't specified for
    a document.

    - **SourceField** *(string) --*

      A string that represents the name of an index field. CloudSearch supports regular index
      fields as well as dynamic fields. A dynamic field's name defines a pattern that begins or
      ends with a wildcard. Any document fields that don't map to a regular index field but do
      match a dynamic field's pattern are configured with the dynamic field's indexing options.

      Regular field names begin with a letter and can contain the following characters: a-z
      (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a wildcard
      (*). The wildcard can also be the only character in a dynamic field name. Multiple wildcards,
      and wildcards embedded within a string are not supported.

      The name ``score`` is reserved and cannot be used as a field name. To reference a document's
      ID, you can use the name ``_id`` .

    - **ReturnEnabled** *(boolean) --*

      Whether the contents of the field can be returned in the search results.

    - **SortEnabled** *(boolean) --*

      Whether the field can be used to sort the search results.

    - **HighlightEnabled** *(boolean) --*

      Whether highlights can be returned for the field.

    - **AnalysisScheme** *(string) --*

      The name of an analysis scheme for a ``text`` field.
    """


_RequiredClientDefineIndexFieldIndexFieldTypeDef = TypedDict(
    "_RequiredClientDefineIndexFieldIndexFieldTypeDef",
    {"IndexFieldName": str, "IndexFieldType": str},
)
_OptionalClientDefineIndexFieldIndexFieldTypeDef = TypedDict(
    "_OptionalClientDefineIndexFieldIndexFieldTypeDef",
    {
        "IntOptions": ClientDefineIndexFieldIndexFieldIntOptionsTypeDef,
        "DoubleOptions": ClientDefineIndexFieldIndexFieldDoubleOptionsTypeDef,
        "LiteralOptions": ClientDefineIndexFieldIndexFieldLiteralOptionsTypeDef,
        "TextOptions": ClientDefineIndexFieldIndexFieldTextOptionsTypeDef,
        "DateOptions": ClientDefineIndexFieldIndexFieldDateOptionsTypeDef,
        "LatLonOptions": ClientDefineIndexFieldIndexFieldLatLonOptionsTypeDef,
        "IntArrayOptions": ClientDefineIndexFieldIndexFieldIntArrayOptionsTypeDef,
        "DoubleArrayOptions": ClientDefineIndexFieldIndexFieldDoubleArrayOptionsTypeDef,
        "LiteralArrayOptions": ClientDefineIndexFieldIndexFieldLiteralArrayOptionsTypeDef,
        "TextArrayOptions": ClientDefineIndexFieldIndexFieldTextArrayOptionsTypeDef,
        "DateArrayOptions": ClientDefineIndexFieldIndexFieldDateArrayOptionsTypeDef,
    },
    total=False,
)


class ClientDefineIndexFieldIndexFieldTypeDef(
    _RequiredClientDefineIndexFieldIndexFieldTypeDef,
    _OptionalClientDefineIndexFieldIndexFieldTypeDef,
):
    """
    Type definition for `ClientDefineIndexField` `IndexField`

    The index field and field options you want to configure.

    - **IndexFieldName** *(string) --* **[REQUIRED]**

      A string that represents the name of an index field. CloudSearch supports regular index fields
      as well as dynamic fields. A dynamic field's name defines a pattern that begins or ends with a
      wildcard. Any document fields that don't map to a regular index field but do match a dynamic
      field's pattern are configured with the dynamic field's indexing options.

      Regular field names begin with a letter and can contain the following characters: a-z
      (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a wildcard
      (*). The wildcard can also be the only character in a dynamic field name. Multiple wildcards,
      and wildcards embedded within a string are not supported.

      The name ``score`` is reserved and cannot be used as a field name. To reference a document's
      ID, you can use the name ``_id`` .

    - **IndexFieldType** *(string) --* **[REQUIRED]**

      The type of field. The valid options for a field depend on the field type. For more information
      about the supported field types, see `Configuring Index Fields
      <http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-index-fields.html>`__
      in the *Amazon CloudSearch Developer Guide* .

    - **IntOptions** *(dict) --*

      Options for a 64-bit signed integer field. Present if ``IndexFieldType`` specifies the field is
      of type ``int`` . All options are enabled by default.

      - **DefaultValue** *(integer) --* A value to use for the field if the field isn't specified for
      a document. This can be important if you are using the field in an expression and that field is
      not present in every document.

      - **SourceField** *(string) --*

        The name of the source field to map to the field.

      - **FacetEnabled** *(boolean) --*

        Whether facet information can be returned for the field.

      - **SearchEnabled** *(boolean) --*

        Whether the contents of the field are searchable.

      - **ReturnEnabled** *(boolean) --*

        Whether the contents of the field can be returned in the search results.

      - **SortEnabled** *(boolean) --*

        Whether the field can be used to sort the search results.

    - **DoubleOptions** *(dict) --*

      Options for a double-precision 64-bit floating point field. Present if ``IndexFieldType``
      specifies the field is of type ``double`` . All options are enabled by default.

      - **DefaultValue** *(float) --*

        A value to use for the field if the field isn't specified for a document. This can be
        important if you are using the field in an expression and that field is not present in every
        document.

      - **SourceField** *(string) --*

        The name of the source field to map to the field.

      - **FacetEnabled** *(boolean) --*

        Whether facet information can be returned for the field.

      - **SearchEnabled** *(boolean) --*

        Whether the contents of the field are searchable.

      - **ReturnEnabled** *(boolean) --*

        Whether the contents of the field can be returned in the search results.

      - **SortEnabled** *(boolean) --*

        Whether the field can be used to sort the search results.

    - **LiteralOptions** *(dict) --*

      Options for literal field. Present if ``IndexFieldType`` specifies the field is of type
      ``literal`` . All options are enabled by default.

      - **DefaultValue** *(string) --* A value to use for the field if the field isn't specified for
      a document.

      - **SourceField** *(string) --*

        A string that represents the name of an index field. CloudSearch supports regular index
        fields as well as dynamic fields. A dynamic field's name defines a pattern that begins or
        ends with a wildcard. Any document fields that don't map to a regular index field but do
        match a dynamic field's pattern are configured with the dynamic field's indexing options.

        Regular field names begin with a letter and can contain the following characters: a-z
        (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a wildcard
        (*). The wildcard can also be the only character in a dynamic field name. Multiple wildcards,
        and wildcards embedded within a string are not supported.

        The name ``score`` is reserved and cannot be used as a field name. To reference a document's
        ID, you can use the name ``_id`` .

      - **FacetEnabled** *(boolean) --*

        Whether facet information can be returned for the field.

      - **SearchEnabled** *(boolean) --*

        Whether the contents of the field are searchable.

      - **ReturnEnabled** *(boolean) --*

        Whether the contents of the field can be returned in the search results.

      - **SortEnabled** *(boolean) --*

        Whether the field can be used to sort the search results.

    - **TextOptions** *(dict) --*

      Options for text field. Present if ``IndexFieldType`` specifies the field is of type ``text`` .
      A ``text`` field is always searchable. All options are enabled by default.

      - **DefaultValue** *(string) --* A value to use for the field if the field isn't specified for
      a document.

      - **SourceField** *(string) --*

        A string that represents the name of an index field. CloudSearch supports regular index
        fields as well as dynamic fields. A dynamic field's name defines a pattern that begins or
        ends with a wildcard. Any document fields that don't map to a regular index field but do
        match a dynamic field's pattern are configured with the dynamic field's indexing options.

        Regular field names begin with a letter and can contain the following characters: a-z
        (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a wildcard
        (*). The wildcard can also be the only character in a dynamic field name. Multiple wildcards,
        and wildcards embedded within a string are not supported.

        The name ``score`` is reserved and cannot be used as a field name. To reference a document's
        ID, you can use the name ``_id`` .

      - **ReturnEnabled** *(boolean) --*

        Whether the contents of the field can be returned in the search results.

      - **SortEnabled** *(boolean) --*

        Whether the field can be used to sort the search results.

      - **HighlightEnabled** *(boolean) --*

        Whether highlights can be returned for the field.

      - **AnalysisScheme** *(string) --*

        The name of an analysis scheme for a ``text`` field.

    - **DateOptions** *(dict) --*

      Options for a date field. Dates and times are specified in UTC (Coordinated Universal Time)
      according to IETF RFC3339: yyyy-mm-ddT00:00:00Z. Present if ``IndexFieldType`` specifies the
      field is of type ``date`` . All options are enabled by default.

      - **DefaultValue** *(string) --* A value to use for the field if the field isn't specified for
      a document.

      - **SourceField** *(string) --*

        A string that represents the name of an index field. CloudSearch supports regular index
        fields as well as dynamic fields. A dynamic field's name defines a pattern that begins or
        ends with a wildcard. Any document fields that don't map to a regular index field but do
        match a dynamic field's pattern are configured with the dynamic field's indexing options.

        Regular field names begin with a letter and can contain the following characters: a-z
        (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a wildcard
        (*). The wildcard can also be the only character in a dynamic field name. Multiple wildcards,
        and wildcards embedded within a string are not supported.

        The name ``score`` is reserved and cannot be used as a field name. To reference a document's
        ID, you can use the name ``_id`` .

      - **FacetEnabled** *(boolean) --*

        Whether facet information can be returned for the field.

      - **SearchEnabled** *(boolean) --*

        Whether the contents of the field are searchable.

      - **ReturnEnabled** *(boolean) --*

        Whether the contents of the field can be returned in the search results.

      - **SortEnabled** *(boolean) --*

        Whether the field can be used to sort the search results.

    - **LatLonOptions** *(dict) --*

      Options for a latlon field. A latlon field contains a location stored as a latitude and
      longitude value pair. Present if ``IndexFieldType`` specifies the field is of type ``latlon`` .
      All options are enabled by default.

      - **DefaultValue** *(string) --* A value to use for the field if the field isn't specified for
      a document.

      - **SourceField** *(string) --*

        A string that represents the name of an index field. CloudSearch supports regular index
        fields as well as dynamic fields. A dynamic field's name defines a pattern that begins or
        ends with a wildcard. Any document fields that don't map to a regular index field but do
        match a dynamic field's pattern are configured with the dynamic field's indexing options.

        Regular field names begin with a letter and can contain the following characters: a-z
        (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a wildcard
        (*). The wildcard can also be the only character in a dynamic field name. Multiple wildcards,
        and wildcards embedded within a string are not supported.

        The name ``score`` is reserved and cannot be used as a field name. To reference a document's
        ID, you can use the name ``_id`` .

      - **FacetEnabled** *(boolean) --*

        Whether facet information can be returned for the field.

      - **SearchEnabled** *(boolean) --*

        Whether the contents of the field are searchable.

      - **ReturnEnabled** *(boolean) --*

        Whether the contents of the field can be returned in the search results.

      - **SortEnabled** *(boolean) --*

        Whether the field can be used to sort the search results.

    - **IntArrayOptions** *(dict) --*

      Options for a field that contains an array of 64-bit signed integers. Present if
      ``IndexFieldType`` specifies the field is of type ``int-array`` . All options are enabled by
      default.

      - **DefaultValue** *(integer) --* A value to use for the field if the field isn't specified for
      a document.

      - **SourceFields** *(string) --*

        A list of source fields to map to the field.

      - **FacetEnabled** *(boolean) --*

        Whether facet information can be returned for the field.

      - **SearchEnabled** *(boolean) --*

        Whether the contents of the field are searchable.

      - **ReturnEnabled** *(boolean) --*

        Whether the contents of the field can be returned in the search results.

    - **DoubleArrayOptions** *(dict) --*

      Options for a field that contains an array of double-precision 64-bit floating point values.
      Present if ``IndexFieldType`` specifies the field is of type ``double-array`` . All options are
      enabled by default.

      - **DefaultValue** *(float) --* A value to use for the field if the field isn't specified for a
      document.

      - **SourceFields** *(string) --*

        A list of source fields to map to the field.

      - **FacetEnabled** *(boolean) --*

        Whether facet information can be returned for the field.

      - **SearchEnabled** *(boolean) --*

        Whether the contents of the field are searchable.

      - **ReturnEnabled** *(boolean) --*

        Whether the contents of the field can be returned in the search results.

    - **LiteralArrayOptions** *(dict) --*

      Options for a field that contains an array of literal strings. Present if ``IndexFieldType``
      specifies the field is of type ``literal-array`` . All options are enabled by default.

      - **DefaultValue** *(string) --* A value to use for the field if the field isn't specified for
      a document.

      - **SourceFields** *(string) --*

        A list of source fields to map to the field.

      - **FacetEnabled** *(boolean) --*

        Whether facet information can be returned for the field.

      - **SearchEnabled** *(boolean) --*

        Whether the contents of the field are searchable.

      - **ReturnEnabled** *(boolean) --*

        Whether the contents of the field can be returned in the search results.

    - **TextArrayOptions** *(dict) --*

      Options for a field that contains an array of text strings. Present if ``IndexFieldType``
      specifies the field is of type ``text-array`` . A ``text-array`` field is always searchable.
      All options are enabled by default.

      - **DefaultValue** *(string) --* A value to use for the field if the field isn't specified for
      a document.

      - **SourceFields** *(string) --*

        A list of source fields to map to the field.

      - **ReturnEnabled** *(boolean) --*

        Whether the contents of the field can be returned in the search results.

      - **HighlightEnabled** *(boolean) --*

        Whether highlights can be returned for the field.

      - **AnalysisScheme** *(string) --*

        The name of an analysis scheme for a ``text-array`` field.

    - **DateArrayOptions** *(dict) --*

      Options for a field that contains an array of dates. Present if ``IndexFieldType`` specifies
      the field is of type ``date-array`` . All options are enabled by default.

      - **DefaultValue** *(string) --* A value to use for the field if the field isn't specified for
      a document.

      - **SourceFields** *(string) --*

        A list of source fields to map to the field.

      - **FacetEnabled** *(boolean) --*

        Whether facet information can be returned for the field.

      - **SearchEnabled** *(boolean) --*

        Whether the contents of the field are searchable.

      - **ReturnEnabled** *(boolean) --*

        Whether the contents of the field can be returned in the search results.
    """


_ClientDefineIndexFieldResponseIndexFieldOptionsDateArrayOptionsTypeDef = TypedDict(
    "_ClientDefineIndexFieldResponseIndexFieldOptionsDateArrayOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceFields": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
    },
    total=False,
)


class ClientDefineIndexFieldResponseIndexFieldOptionsDateArrayOptionsTypeDef(
    _ClientDefineIndexFieldResponseIndexFieldOptionsDateArrayOptionsTypeDef
):
    """
    Type definition for `ClientDefineIndexFieldResponseIndexFieldOptions` `DateArrayOptions`

    Options for a field that contains an array of dates. Present if ``IndexFieldType``
    specifies the field is of type ``date-array`` . All options are enabled by default.

    - **DefaultValue** *(string) --* A value to use for the field if the field isn't
    specified for a document.

    - **SourceFields** *(string) --*

      A list of source fields to map to the field.

    - **FacetEnabled** *(boolean) --*

      Whether facet information can be returned for the field.

    - **SearchEnabled** *(boolean) --*

      Whether the contents of the field are searchable.

    - **ReturnEnabled** *(boolean) --*

      Whether the contents of the field can be returned in the search results.
    """


_ClientDefineIndexFieldResponseIndexFieldOptionsDateOptionsTypeDef = TypedDict(
    "_ClientDefineIndexFieldResponseIndexFieldOptionsDateOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)


class ClientDefineIndexFieldResponseIndexFieldOptionsDateOptionsTypeDef(
    _ClientDefineIndexFieldResponseIndexFieldOptionsDateOptionsTypeDef
):
    """
    Type definition for `ClientDefineIndexFieldResponseIndexFieldOptions` `DateOptions`

    Options for a date field. Dates and times are specified in UTC (Coordinated Universal
    Time) according to IETF RFC3339: yyyy-mm-ddT00:00:00Z. Present if ``IndexFieldType``
    specifies the field is of type ``date`` . All options are enabled by default.

    - **DefaultValue** *(string) --* A value to use for the field if the field isn't
    specified for a document.

    - **SourceField** *(string) --*

      A string that represents the name of an index field. CloudSearch supports regular index
      fields as well as dynamic fields. A dynamic field's name defines a pattern that begins
      or ends with a wildcard. Any document fields that don't map to a regular index field
      but do match a dynamic field's pattern are configured with the dynamic field's indexing
      options.

      Regular field names begin with a letter and can contain the following characters: a-z
      (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a
      wildcard (*). The wildcard can also be the only character in a dynamic field name.
      Multiple wildcards, and wildcards embedded within a string are not supported.

      The name ``score`` is reserved and cannot be used as a field name. To reference a
      document's ID, you can use the name ``_id`` .

    - **FacetEnabled** *(boolean) --*

      Whether facet information can be returned for the field.

    - **SearchEnabled** *(boolean) --*

      Whether the contents of the field are searchable.

    - **ReturnEnabled** *(boolean) --*

      Whether the contents of the field can be returned in the search results.

    - **SortEnabled** *(boolean) --*

      Whether the field can be used to sort the search results.
    """


_ClientDefineIndexFieldResponseIndexFieldOptionsDoubleArrayOptionsTypeDef = TypedDict(
    "_ClientDefineIndexFieldResponseIndexFieldOptionsDoubleArrayOptionsTypeDef",
    {
        "DefaultValue": float,
        "SourceFields": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
    },
    total=False,
)


class ClientDefineIndexFieldResponseIndexFieldOptionsDoubleArrayOptionsTypeDef(
    _ClientDefineIndexFieldResponseIndexFieldOptionsDoubleArrayOptionsTypeDef
):
    """
    Type definition for `ClientDefineIndexFieldResponseIndexFieldOptions` `DoubleArrayOptions`

    Options for a field that contains an array of double-precision 64-bit floating point
    values. Present if ``IndexFieldType`` specifies the field is of type ``double-array`` .
    All options are enabled by default.

    - **DefaultValue** *(float) --* A value to use for the field if the field isn't specified
    for a document.

    - **SourceFields** *(string) --*

      A list of source fields to map to the field.

    - **FacetEnabled** *(boolean) --*

      Whether facet information can be returned for the field.

    - **SearchEnabled** *(boolean) --*

      Whether the contents of the field are searchable.

    - **ReturnEnabled** *(boolean) --*

      Whether the contents of the field can be returned in the search results.
    """


_ClientDefineIndexFieldResponseIndexFieldOptionsDoubleOptionsTypeDef = TypedDict(
    "_ClientDefineIndexFieldResponseIndexFieldOptionsDoubleOptionsTypeDef",
    {
        "DefaultValue": float,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)


class ClientDefineIndexFieldResponseIndexFieldOptionsDoubleOptionsTypeDef(
    _ClientDefineIndexFieldResponseIndexFieldOptionsDoubleOptionsTypeDef
):
    """
    Type definition for `ClientDefineIndexFieldResponseIndexFieldOptions` `DoubleOptions`

    Options for a double-precision 64-bit floating point field. Present if ``IndexFieldType``
    specifies the field is of type ``double`` . All options are enabled by default.

    - **DefaultValue** *(float) --*

      A value to use for the field if the field isn't specified for a document. This can be
      important if you are using the field in an expression and that field is not present in
      every document.

    - **SourceField** *(string) --*

      The name of the source field to map to the field.

    - **FacetEnabled** *(boolean) --*

      Whether facet information can be returned for the field.

    - **SearchEnabled** *(boolean) --*

      Whether the contents of the field are searchable.

    - **ReturnEnabled** *(boolean) --*

      Whether the contents of the field can be returned in the search results.

    - **SortEnabled** *(boolean) --*

      Whether the field can be used to sort the search results.
    """


_ClientDefineIndexFieldResponseIndexFieldOptionsIntArrayOptionsTypeDef = TypedDict(
    "_ClientDefineIndexFieldResponseIndexFieldOptionsIntArrayOptionsTypeDef",
    {
        "DefaultValue": int,
        "SourceFields": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
    },
    total=False,
)


class ClientDefineIndexFieldResponseIndexFieldOptionsIntArrayOptionsTypeDef(
    _ClientDefineIndexFieldResponseIndexFieldOptionsIntArrayOptionsTypeDef
):
    """
    Type definition for `ClientDefineIndexFieldResponseIndexFieldOptions` `IntArrayOptions`

    Options for a field that contains an array of 64-bit signed integers. Present if
    ``IndexFieldType`` specifies the field is of type ``int-array`` . All options are enabled
    by default.

    - **DefaultValue** *(integer) --* A value to use for the field if the field isn't
    specified for a document.

    - **SourceFields** *(string) --*

      A list of source fields to map to the field.

    - **FacetEnabled** *(boolean) --*

      Whether facet information can be returned for the field.

    - **SearchEnabled** *(boolean) --*

      Whether the contents of the field are searchable.

    - **ReturnEnabled** *(boolean) --*

      Whether the contents of the field can be returned in the search results.
    """


_ClientDefineIndexFieldResponseIndexFieldOptionsIntOptionsTypeDef = TypedDict(
    "_ClientDefineIndexFieldResponseIndexFieldOptionsIntOptionsTypeDef",
    {
        "DefaultValue": int,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)


class ClientDefineIndexFieldResponseIndexFieldOptionsIntOptionsTypeDef(
    _ClientDefineIndexFieldResponseIndexFieldOptionsIntOptionsTypeDef
):
    """
    Type definition for `ClientDefineIndexFieldResponseIndexFieldOptions` `IntOptions`

    Options for a 64-bit signed integer field. Present if ``IndexFieldType`` specifies the
    field is of type ``int`` . All options are enabled by default.

    - **DefaultValue** *(integer) --* A value to use for the field if the field isn't
    specified for a document. This can be important if you are using the field in an
    expression and that field is not present in every document.

    - **SourceField** *(string) --*

      The name of the source field to map to the field.

    - **FacetEnabled** *(boolean) --*

      Whether facet information can be returned for the field.

    - **SearchEnabled** *(boolean) --*

      Whether the contents of the field are searchable.

    - **ReturnEnabled** *(boolean) --*

      Whether the contents of the field can be returned in the search results.

    - **SortEnabled** *(boolean) --*

      Whether the field can be used to sort the search results.
    """


_ClientDefineIndexFieldResponseIndexFieldOptionsLatLonOptionsTypeDef = TypedDict(
    "_ClientDefineIndexFieldResponseIndexFieldOptionsLatLonOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)


class ClientDefineIndexFieldResponseIndexFieldOptionsLatLonOptionsTypeDef(
    _ClientDefineIndexFieldResponseIndexFieldOptionsLatLonOptionsTypeDef
):
    """
    Type definition for `ClientDefineIndexFieldResponseIndexFieldOptions` `LatLonOptions`

    Options for a latlon field. A latlon field contains a location stored as a latitude and
    longitude value pair. Present if ``IndexFieldType`` specifies the field is of type
    ``latlon`` . All options are enabled by default.

    - **DefaultValue** *(string) --* A value to use for the field if the field isn't
    specified for a document.

    - **SourceField** *(string) --*

      A string that represents the name of an index field. CloudSearch supports regular index
      fields as well as dynamic fields. A dynamic field's name defines a pattern that begins
      or ends with a wildcard. Any document fields that don't map to a regular index field
      but do match a dynamic field's pattern are configured with the dynamic field's indexing
      options.

      Regular field names begin with a letter and can contain the following characters: a-z
      (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a
      wildcard (*). The wildcard can also be the only character in a dynamic field name.
      Multiple wildcards, and wildcards embedded within a string are not supported.

      The name ``score`` is reserved and cannot be used as a field name. To reference a
      document's ID, you can use the name ``_id`` .

    - **FacetEnabled** *(boolean) --*

      Whether facet information can be returned for the field.

    - **SearchEnabled** *(boolean) --*

      Whether the contents of the field are searchable.

    - **ReturnEnabled** *(boolean) --*

      Whether the contents of the field can be returned in the search results.

    - **SortEnabled** *(boolean) --*

      Whether the field can be used to sort the search results.
    """


_ClientDefineIndexFieldResponseIndexFieldOptionsLiteralArrayOptionsTypeDef = TypedDict(
    "_ClientDefineIndexFieldResponseIndexFieldOptionsLiteralArrayOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceFields": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
    },
    total=False,
)


class ClientDefineIndexFieldResponseIndexFieldOptionsLiteralArrayOptionsTypeDef(
    _ClientDefineIndexFieldResponseIndexFieldOptionsLiteralArrayOptionsTypeDef
):
    """
    Type definition for `ClientDefineIndexFieldResponseIndexFieldOptions` `LiteralArrayOptions`

    Options for a field that contains an array of literal strings. Present if
    ``IndexFieldType`` specifies the field is of type ``literal-array`` . All options are
    enabled by default.

    - **DefaultValue** *(string) --* A value to use for the field if the field isn't
    specified for a document.

    - **SourceFields** *(string) --*

      A list of source fields to map to the field.

    - **FacetEnabled** *(boolean) --*

      Whether facet information can be returned for the field.

    - **SearchEnabled** *(boolean) --*

      Whether the contents of the field are searchable.

    - **ReturnEnabled** *(boolean) --*

      Whether the contents of the field can be returned in the search results.
    """


_ClientDefineIndexFieldResponseIndexFieldOptionsLiteralOptionsTypeDef = TypedDict(
    "_ClientDefineIndexFieldResponseIndexFieldOptionsLiteralOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)


class ClientDefineIndexFieldResponseIndexFieldOptionsLiteralOptionsTypeDef(
    _ClientDefineIndexFieldResponseIndexFieldOptionsLiteralOptionsTypeDef
):
    """
    Type definition for `ClientDefineIndexFieldResponseIndexFieldOptions` `LiteralOptions`

    Options for literal field. Present if ``IndexFieldType`` specifies the field is of type
    ``literal`` . All options are enabled by default.

    - **DefaultValue** *(string) --* A value to use for the field if the field isn't
    specified for a document.

    - **SourceField** *(string) --*

      A string that represents the name of an index field. CloudSearch supports regular index
      fields as well as dynamic fields. A dynamic field's name defines a pattern that begins
      or ends with a wildcard. Any document fields that don't map to a regular index field
      but do match a dynamic field's pattern are configured with the dynamic field's indexing
      options.

      Regular field names begin with a letter and can contain the following characters: a-z
      (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a
      wildcard (*). The wildcard can also be the only character in a dynamic field name.
      Multiple wildcards, and wildcards embedded within a string are not supported.

      The name ``score`` is reserved and cannot be used as a field name. To reference a
      document's ID, you can use the name ``_id`` .

    - **FacetEnabled** *(boolean) --*

      Whether facet information can be returned for the field.

    - **SearchEnabled** *(boolean) --*

      Whether the contents of the field are searchable.

    - **ReturnEnabled** *(boolean) --*

      Whether the contents of the field can be returned in the search results.

    - **SortEnabled** *(boolean) --*

      Whether the field can be used to sort the search results.
    """


_ClientDefineIndexFieldResponseIndexFieldOptionsTextArrayOptionsTypeDef = TypedDict(
    "_ClientDefineIndexFieldResponseIndexFieldOptionsTextArrayOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceFields": str,
        "ReturnEnabled": bool,
        "HighlightEnabled": bool,
        "AnalysisScheme": str,
    },
    total=False,
)


class ClientDefineIndexFieldResponseIndexFieldOptionsTextArrayOptionsTypeDef(
    _ClientDefineIndexFieldResponseIndexFieldOptionsTextArrayOptionsTypeDef
):
    """
    Type definition for `ClientDefineIndexFieldResponseIndexFieldOptions` `TextArrayOptions`

    Options for a field that contains an array of text strings. Present if ``IndexFieldType``
    specifies the field is of type ``text-array`` . A ``text-array`` field is always
    searchable. All options are enabled by default.

    - **DefaultValue** *(string) --* A value to use for the field if the field isn't
    specified for a document.

    - **SourceFields** *(string) --*

      A list of source fields to map to the field.

    - **ReturnEnabled** *(boolean) --*

      Whether the contents of the field can be returned in the search results.

    - **HighlightEnabled** *(boolean) --*

      Whether highlights can be returned for the field.

    - **AnalysisScheme** *(string) --*

      The name of an analysis scheme for a ``text-array`` field.
    """


_ClientDefineIndexFieldResponseIndexFieldOptionsTextOptionsTypeDef = TypedDict(
    "_ClientDefineIndexFieldResponseIndexFieldOptionsTextOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceField": str,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
        "HighlightEnabled": bool,
        "AnalysisScheme": str,
    },
    total=False,
)


class ClientDefineIndexFieldResponseIndexFieldOptionsTextOptionsTypeDef(
    _ClientDefineIndexFieldResponseIndexFieldOptionsTextOptionsTypeDef
):
    """
    Type definition for `ClientDefineIndexFieldResponseIndexFieldOptions` `TextOptions`

    Options for text field. Present if ``IndexFieldType`` specifies the field is of type
    ``text`` . A ``text`` field is always searchable. All options are enabled by default.

    - **DefaultValue** *(string) --* A value to use for the field if the field isn't
    specified for a document.

    - **SourceField** *(string) --*

      A string that represents the name of an index field. CloudSearch supports regular index
      fields as well as dynamic fields. A dynamic field's name defines a pattern that begins
      or ends with a wildcard. Any document fields that don't map to a regular index field
      but do match a dynamic field's pattern are configured with the dynamic field's indexing
      options.

      Regular field names begin with a letter and can contain the following characters: a-z
      (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a
      wildcard (*). The wildcard can also be the only character in a dynamic field name.
      Multiple wildcards, and wildcards embedded within a string are not supported.

      The name ``score`` is reserved and cannot be used as a field name. To reference a
      document's ID, you can use the name ``_id`` .

    - **ReturnEnabled** *(boolean) --*

      Whether the contents of the field can be returned in the search results.

    - **SortEnabled** *(boolean) --*

      Whether the field can be used to sort the search results.

    - **HighlightEnabled** *(boolean) --*

      Whether highlights can be returned for the field.

    - **AnalysisScheme** *(string) --*

      The name of an analysis scheme for a ``text`` field.
    """


_ClientDefineIndexFieldResponseIndexFieldOptionsTypeDef = TypedDict(
    "_ClientDefineIndexFieldResponseIndexFieldOptionsTypeDef",
    {
        "IndexFieldName": str,
        "IndexFieldType": str,
        "IntOptions": ClientDefineIndexFieldResponseIndexFieldOptionsIntOptionsTypeDef,
        "DoubleOptions": ClientDefineIndexFieldResponseIndexFieldOptionsDoubleOptionsTypeDef,
        "LiteralOptions": ClientDefineIndexFieldResponseIndexFieldOptionsLiteralOptionsTypeDef,
        "TextOptions": ClientDefineIndexFieldResponseIndexFieldOptionsTextOptionsTypeDef,
        "DateOptions": ClientDefineIndexFieldResponseIndexFieldOptionsDateOptionsTypeDef,
        "LatLonOptions": ClientDefineIndexFieldResponseIndexFieldOptionsLatLonOptionsTypeDef,
        "IntArrayOptions": ClientDefineIndexFieldResponseIndexFieldOptionsIntArrayOptionsTypeDef,
        "DoubleArrayOptions": ClientDefineIndexFieldResponseIndexFieldOptionsDoubleArrayOptionsTypeDef,
        "LiteralArrayOptions": ClientDefineIndexFieldResponseIndexFieldOptionsLiteralArrayOptionsTypeDef,
        "TextArrayOptions": ClientDefineIndexFieldResponseIndexFieldOptionsTextArrayOptionsTypeDef,
        "DateArrayOptions": ClientDefineIndexFieldResponseIndexFieldOptionsDateArrayOptionsTypeDef,
    },
    total=False,
)


class ClientDefineIndexFieldResponseIndexFieldOptionsTypeDef(
    _ClientDefineIndexFieldResponseIndexFieldOptionsTypeDef
):
    """
    Type definition for `ClientDefineIndexFieldResponseIndexField` `Options`

    Configuration information for a field in the index, including its name, type, and options.
    The supported options depend on the `` IndexFieldType`` .

    - **IndexFieldName** *(string) --*

      A string that represents the name of an index field. CloudSearch supports regular index
      fields as well as dynamic fields. A dynamic field's name defines a pattern that begins or
      ends with a wildcard. Any document fields that don't map to a regular index field but do
      match a dynamic field's pattern are configured with the dynamic field's indexing options.

      Regular field names begin with a letter and can contain the following characters: a-z
      (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a
      wildcard (*). The wildcard can also be the only character in a dynamic field name.
      Multiple wildcards, and wildcards embedded within a string are not supported.

      The name ``score`` is reserved and cannot be used as a field name. To reference a
      document's ID, you can use the name ``_id`` .

    - **IndexFieldType** *(string) --*

      The type of field. The valid options for a field depend on the field type. For more
      information about the supported field types, see `Configuring Index Fields
      <http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-index-fields.html>`__
      in the *Amazon CloudSearch Developer Guide* .

    - **IntOptions** *(dict) --*

      Options for a 64-bit signed integer field. Present if ``IndexFieldType`` specifies the
      field is of type ``int`` . All options are enabled by default.

      - **DefaultValue** *(integer) --* A value to use for the field if the field isn't
      specified for a document. This can be important if you are using the field in an
      expression and that field is not present in every document.

      - **SourceField** *(string) --*

        The name of the source field to map to the field.

      - **FacetEnabled** *(boolean) --*

        Whether facet information can be returned for the field.

      - **SearchEnabled** *(boolean) --*

        Whether the contents of the field are searchable.

      - **ReturnEnabled** *(boolean) --*

        Whether the contents of the field can be returned in the search results.

      - **SortEnabled** *(boolean) --*

        Whether the field can be used to sort the search results.

    - **DoubleOptions** *(dict) --*

      Options for a double-precision 64-bit floating point field. Present if ``IndexFieldType``
      specifies the field is of type ``double`` . All options are enabled by default.

      - **DefaultValue** *(float) --*

        A value to use for the field if the field isn't specified for a document. This can be
        important if you are using the field in an expression and that field is not present in
        every document.

      - **SourceField** *(string) --*

        The name of the source field to map to the field.

      - **FacetEnabled** *(boolean) --*

        Whether facet information can be returned for the field.

      - **SearchEnabled** *(boolean) --*

        Whether the contents of the field are searchable.

      - **ReturnEnabled** *(boolean) --*

        Whether the contents of the field can be returned in the search results.

      - **SortEnabled** *(boolean) --*

        Whether the field can be used to sort the search results.

    - **LiteralOptions** *(dict) --*

      Options for literal field. Present if ``IndexFieldType`` specifies the field is of type
      ``literal`` . All options are enabled by default.

      - **DefaultValue** *(string) --* A value to use for the field if the field isn't
      specified for a document.

      - **SourceField** *(string) --*

        A string that represents the name of an index field. CloudSearch supports regular index
        fields as well as dynamic fields. A dynamic field's name defines a pattern that begins
        or ends with a wildcard. Any document fields that don't map to a regular index field
        but do match a dynamic field's pattern are configured with the dynamic field's indexing
        options.

        Regular field names begin with a letter and can contain the following characters: a-z
        (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a
        wildcard (*). The wildcard can also be the only character in a dynamic field name.
        Multiple wildcards, and wildcards embedded within a string are not supported.

        The name ``score`` is reserved and cannot be used as a field name. To reference a
        document's ID, you can use the name ``_id`` .

      - **FacetEnabled** *(boolean) --*

        Whether facet information can be returned for the field.

      - **SearchEnabled** *(boolean) --*

        Whether the contents of the field are searchable.

      - **ReturnEnabled** *(boolean) --*

        Whether the contents of the field can be returned in the search results.

      - **SortEnabled** *(boolean) --*

        Whether the field can be used to sort the search results.

    - **TextOptions** *(dict) --*

      Options for text field. Present if ``IndexFieldType`` specifies the field is of type
      ``text`` . A ``text`` field is always searchable. All options are enabled by default.

      - **DefaultValue** *(string) --* A value to use for the field if the field isn't
      specified for a document.

      - **SourceField** *(string) --*

        A string that represents the name of an index field. CloudSearch supports regular index
        fields as well as dynamic fields. A dynamic field's name defines a pattern that begins
        or ends with a wildcard. Any document fields that don't map to a regular index field
        but do match a dynamic field's pattern are configured with the dynamic field's indexing
        options.

        Regular field names begin with a letter and can contain the following characters: a-z
        (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a
        wildcard (*). The wildcard can also be the only character in a dynamic field name.
        Multiple wildcards, and wildcards embedded within a string are not supported.

        The name ``score`` is reserved and cannot be used as a field name. To reference a
        document's ID, you can use the name ``_id`` .

      - **ReturnEnabled** *(boolean) --*

        Whether the contents of the field can be returned in the search results.

      - **SortEnabled** *(boolean) --*

        Whether the field can be used to sort the search results.

      - **HighlightEnabled** *(boolean) --*

        Whether highlights can be returned for the field.

      - **AnalysisScheme** *(string) --*

        The name of an analysis scheme for a ``text`` field.

    - **DateOptions** *(dict) --*

      Options for a date field. Dates and times are specified in UTC (Coordinated Universal
      Time) according to IETF RFC3339: yyyy-mm-ddT00:00:00Z. Present if ``IndexFieldType``
      specifies the field is of type ``date`` . All options are enabled by default.

      - **DefaultValue** *(string) --* A value to use for the field if the field isn't
      specified for a document.

      - **SourceField** *(string) --*

        A string that represents the name of an index field. CloudSearch supports regular index
        fields as well as dynamic fields. A dynamic field's name defines a pattern that begins
        or ends with a wildcard. Any document fields that don't map to a regular index field
        but do match a dynamic field's pattern are configured with the dynamic field's indexing
        options.

        Regular field names begin with a letter and can contain the following characters: a-z
        (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a
        wildcard (*). The wildcard can also be the only character in a dynamic field name.
        Multiple wildcards, and wildcards embedded within a string are not supported.

        The name ``score`` is reserved and cannot be used as a field name. To reference a
        document's ID, you can use the name ``_id`` .

      - **FacetEnabled** *(boolean) --*

        Whether facet information can be returned for the field.

      - **SearchEnabled** *(boolean) --*

        Whether the contents of the field are searchable.

      - **ReturnEnabled** *(boolean) --*

        Whether the contents of the field can be returned in the search results.

      - **SortEnabled** *(boolean) --*

        Whether the field can be used to sort the search results.

    - **LatLonOptions** *(dict) --*

      Options for a latlon field. A latlon field contains a location stored as a latitude and
      longitude value pair. Present if ``IndexFieldType`` specifies the field is of type
      ``latlon`` . All options are enabled by default.

      - **DefaultValue** *(string) --* A value to use for the field if the field isn't
      specified for a document.

      - **SourceField** *(string) --*

        A string that represents the name of an index field. CloudSearch supports regular index
        fields as well as dynamic fields. A dynamic field's name defines a pattern that begins
        or ends with a wildcard. Any document fields that don't map to a regular index field
        but do match a dynamic field's pattern are configured with the dynamic field's indexing
        options.

        Regular field names begin with a letter and can contain the following characters: a-z
        (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a
        wildcard (*). The wildcard can also be the only character in a dynamic field name.
        Multiple wildcards, and wildcards embedded within a string are not supported.

        The name ``score`` is reserved and cannot be used as a field name. To reference a
        document's ID, you can use the name ``_id`` .

      - **FacetEnabled** *(boolean) --*

        Whether facet information can be returned for the field.

      - **SearchEnabled** *(boolean) --*

        Whether the contents of the field are searchable.

      - **ReturnEnabled** *(boolean) --*

        Whether the contents of the field can be returned in the search results.

      - **SortEnabled** *(boolean) --*

        Whether the field can be used to sort the search results.

    - **IntArrayOptions** *(dict) --*

      Options for a field that contains an array of 64-bit signed integers. Present if
      ``IndexFieldType`` specifies the field is of type ``int-array`` . All options are enabled
      by default.

      - **DefaultValue** *(integer) --* A value to use for the field if the field isn't
      specified for a document.

      - **SourceFields** *(string) --*

        A list of source fields to map to the field.

      - **FacetEnabled** *(boolean) --*

        Whether facet information can be returned for the field.

      - **SearchEnabled** *(boolean) --*

        Whether the contents of the field are searchable.

      - **ReturnEnabled** *(boolean) --*

        Whether the contents of the field can be returned in the search results.

    - **DoubleArrayOptions** *(dict) --*

      Options for a field that contains an array of double-precision 64-bit floating point
      values. Present if ``IndexFieldType`` specifies the field is of type ``double-array`` .
      All options are enabled by default.

      - **DefaultValue** *(float) --* A value to use for the field if the field isn't specified
      for a document.

      - **SourceFields** *(string) --*

        A list of source fields to map to the field.

      - **FacetEnabled** *(boolean) --*

        Whether facet information can be returned for the field.

      - **SearchEnabled** *(boolean) --*

        Whether the contents of the field are searchable.

      - **ReturnEnabled** *(boolean) --*

        Whether the contents of the field can be returned in the search results.

    - **LiteralArrayOptions** *(dict) --*

      Options for a field that contains an array of literal strings. Present if
      ``IndexFieldType`` specifies the field is of type ``literal-array`` . All options are
      enabled by default.

      - **DefaultValue** *(string) --* A value to use for the field if the field isn't
      specified for a document.

      - **SourceFields** *(string) --*

        A list of source fields to map to the field.

      - **FacetEnabled** *(boolean) --*

        Whether facet information can be returned for the field.

      - **SearchEnabled** *(boolean) --*

        Whether the contents of the field are searchable.

      - **ReturnEnabled** *(boolean) --*

        Whether the contents of the field can be returned in the search results.

    - **TextArrayOptions** *(dict) --*

      Options for a field that contains an array of text strings. Present if ``IndexFieldType``
      specifies the field is of type ``text-array`` . A ``text-array`` field is always
      searchable. All options are enabled by default.

      - **DefaultValue** *(string) --* A value to use for the field if the field isn't
      specified for a document.

      - **SourceFields** *(string) --*

        A list of source fields to map to the field.

      - **ReturnEnabled** *(boolean) --*

        Whether the contents of the field can be returned in the search results.

      - **HighlightEnabled** *(boolean) --*

        Whether highlights can be returned for the field.

      - **AnalysisScheme** *(string) --*

        The name of an analysis scheme for a ``text-array`` field.

    - **DateArrayOptions** *(dict) --*

      Options for a field that contains an array of dates. Present if ``IndexFieldType``
      specifies the field is of type ``date-array`` . All options are enabled by default.

      - **DefaultValue** *(string) --* A value to use for the field if the field isn't
      specified for a document.

      - **SourceFields** *(string) --*

        A list of source fields to map to the field.

      - **FacetEnabled** *(boolean) --*

        Whether facet information can be returned for the field.

      - **SearchEnabled** *(boolean) --*

        Whether the contents of the field are searchable.

      - **ReturnEnabled** *(boolean) --*

        Whether the contents of the field can be returned in the search results.
    """


_ClientDefineIndexFieldResponseIndexFieldStatusTypeDef = TypedDict(
    "_ClientDefineIndexFieldResponseIndexFieldStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": str,
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientDefineIndexFieldResponseIndexFieldStatusTypeDef(
    _ClientDefineIndexFieldResponseIndexFieldStatusTypeDef
):
    """
    Type definition for `ClientDefineIndexFieldResponseIndexField` `Status`

    The status of domain configuration option.

    - **CreationDate** *(datetime) --*

      A timestamp for when this option was created.

    - **UpdateDate** *(datetime) --*

      A timestamp for when this option was last updated.

    - **UpdateVersion** *(integer) --*

      A unique integer that indicates when this option was last updated.

    - **State** *(string) --*

      The state of processing a change to an option. Possible values:

      * ``RequiresIndexDocuments`` : the option's latest value will not be deployed until
      IndexDocuments has been called and indexing is complete.

      * ``Processing`` : the option's latest value is in the process of being activated.

      * ``Active`` : the option's latest value is completely deployed.

      * ``FailedToValidate`` : the option value is not compatible with the domain's data and
      cannot be used to index the data. You must either modify the option value or update or
      remove the incompatible documents.

    - **PendingDeletion** *(boolean) --*

      Indicates that the option will be deleted once processing is complete.
    """


_ClientDefineIndexFieldResponseIndexFieldTypeDef = TypedDict(
    "_ClientDefineIndexFieldResponseIndexFieldTypeDef",
    {
        "Options": ClientDefineIndexFieldResponseIndexFieldOptionsTypeDef,
        "Status": ClientDefineIndexFieldResponseIndexFieldStatusTypeDef,
    },
    total=False,
)


class ClientDefineIndexFieldResponseIndexFieldTypeDef(
    _ClientDefineIndexFieldResponseIndexFieldTypeDef
):
    """
    Type definition for `ClientDefineIndexFieldResponse` `IndexField`

    The value of an ``IndexField`` and its current status.

    - **Options** *(dict) --*

      Configuration information for a field in the index, including its name, type, and options.
      The supported options depend on the `` IndexFieldType`` .

      - **IndexFieldName** *(string) --*

        A string that represents the name of an index field. CloudSearch supports regular index
        fields as well as dynamic fields. A dynamic field's name defines a pattern that begins or
        ends with a wildcard. Any document fields that don't map to a regular index field but do
        match a dynamic field's pattern are configured with the dynamic field's indexing options.

        Regular field names begin with a letter and can contain the following characters: a-z
        (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a
        wildcard (*). The wildcard can also be the only character in a dynamic field name.
        Multiple wildcards, and wildcards embedded within a string are not supported.

        The name ``score`` is reserved and cannot be used as a field name. To reference a
        document's ID, you can use the name ``_id`` .

      - **IndexFieldType** *(string) --*

        The type of field. The valid options for a field depend on the field type. For more
        information about the supported field types, see `Configuring Index Fields
        <http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-index-fields.html>`__
        in the *Amazon CloudSearch Developer Guide* .

      - **IntOptions** *(dict) --*

        Options for a 64-bit signed integer field. Present if ``IndexFieldType`` specifies the
        field is of type ``int`` . All options are enabled by default.

        - **DefaultValue** *(integer) --* A value to use for the field if the field isn't
        specified for a document. This can be important if you are using the field in an
        expression and that field is not present in every document.

        - **SourceField** *(string) --*

          The name of the source field to map to the field.

        - **FacetEnabled** *(boolean) --*

          Whether facet information can be returned for the field.

        - **SearchEnabled** *(boolean) --*

          Whether the contents of the field are searchable.

        - **ReturnEnabled** *(boolean) --*

          Whether the contents of the field can be returned in the search results.

        - **SortEnabled** *(boolean) --*

          Whether the field can be used to sort the search results.

      - **DoubleOptions** *(dict) --*

        Options for a double-precision 64-bit floating point field. Present if ``IndexFieldType``
        specifies the field is of type ``double`` . All options are enabled by default.

        - **DefaultValue** *(float) --*

          A value to use for the field if the field isn't specified for a document. This can be
          important if you are using the field in an expression and that field is not present in
          every document.

        - **SourceField** *(string) --*

          The name of the source field to map to the field.

        - **FacetEnabled** *(boolean) --*

          Whether facet information can be returned for the field.

        - **SearchEnabled** *(boolean) --*

          Whether the contents of the field are searchable.

        - **ReturnEnabled** *(boolean) --*

          Whether the contents of the field can be returned in the search results.

        - **SortEnabled** *(boolean) --*

          Whether the field can be used to sort the search results.

      - **LiteralOptions** *(dict) --*

        Options for literal field. Present if ``IndexFieldType`` specifies the field is of type
        ``literal`` . All options are enabled by default.

        - **DefaultValue** *(string) --* A value to use for the field if the field isn't
        specified for a document.

        - **SourceField** *(string) --*

          A string that represents the name of an index field. CloudSearch supports regular index
          fields as well as dynamic fields. A dynamic field's name defines a pattern that begins
          or ends with a wildcard. Any document fields that don't map to a regular index field
          but do match a dynamic field's pattern are configured with the dynamic field's indexing
          options.

          Regular field names begin with a letter and can contain the following characters: a-z
          (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a
          wildcard (*). The wildcard can also be the only character in a dynamic field name.
          Multiple wildcards, and wildcards embedded within a string are not supported.

          The name ``score`` is reserved and cannot be used as a field name. To reference a
          document's ID, you can use the name ``_id`` .

        - **FacetEnabled** *(boolean) --*

          Whether facet information can be returned for the field.

        - **SearchEnabled** *(boolean) --*

          Whether the contents of the field are searchable.

        - **ReturnEnabled** *(boolean) --*

          Whether the contents of the field can be returned in the search results.

        - **SortEnabled** *(boolean) --*

          Whether the field can be used to sort the search results.

      - **TextOptions** *(dict) --*

        Options for text field. Present if ``IndexFieldType`` specifies the field is of type
        ``text`` . A ``text`` field is always searchable. All options are enabled by default.

        - **DefaultValue** *(string) --* A value to use for the field if the field isn't
        specified for a document.

        - **SourceField** *(string) --*

          A string that represents the name of an index field. CloudSearch supports regular index
          fields as well as dynamic fields. A dynamic field's name defines a pattern that begins
          or ends with a wildcard. Any document fields that don't map to a regular index field
          but do match a dynamic field's pattern are configured with the dynamic field's indexing
          options.

          Regular field names begin with a letter and can contain the following characters: a-z
          (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a
          wildcard (*). The wildcard can also be the only character in a dynamic field name.
          Multiple wildcards, and wildcards embedded within a string are not supported.

          The name ``score`` is reserved and cannot be used as a field name. To reference a
          document's ID, you can use the name ``_id`` .

        - **ReturnEnabled** *(boolean) --*

          Whether the contents of the field can be returned in the search results.

        - **SortEnabled** *(boolean) --*

          Whether the field can be used to sort the search results.

        - **HighlightEnabled** *(boolean) --*

          Whether highlights can be returned for the field.

        - **AnalysisScheme** *(string) --*

          The name of an analysis scheme for a ``text`` field.

      - **DateOptions** *(dict) --*

        Options for a date field. Dates and times are specified in UTC (Coordinated Universal
        Time) according to IETF RFC3339: yyyy-mm-ddT00:00:00Z. Present if ``IndexFieldType``
        specifies the field is of type ``date`` . All options are enabled by default.

        - **DefaultValue** *(string) --* A value to use for the field if the field isn't
        specified for a document.

        - **SourceField** *(string) --*

          A string that represents the name of an index field. CloudSearch supports regular index
          fields as well as dynamic fields. A dynamic field's name defines a pattern that begins
          or ends with a wildcard. Any document fields that don't map to a regular index field
          but do match a dynamic field's pattern are configured with the dynamic field's indexing
          options.

          Regular field names begin with a letter and can contain the following characters: a-z
          (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a
          wildcard (*). The wildcard can also be the only character in a dynamic field name.
          Multiple wildcards, and wildcards embedded within a string are not supported.

          The name ``score`` is reserved and cannot be used as a field name. To reference a
          document's ID, you can use the name ``_id`` .

        - **FacetEnabled** *(boolean) --*

          Whether facet information can be returned for the field.

        - **SearchEnabled** *(boolean) --*

          Whether the contents of the field are searchable.

        - **ReturnEnabled** *(boolean) --*

          Whether the contents of the field can be returned in the search results.

        - **SortEnabled** *(boolean) --*

          Whether the field can be used to sort the search results.

      - **LatLonOptions** *(dict) --*

        Options for a latlon field. A latlon field contains a location stored as a latitude and
        longitude value pair. Present if ``IndexFieldType`` specifies the field is of type
        ``latlon`` . All options are enabled by default.

        - **DefaultValue** *(string) --* A value to use for the field if the field isn't
        specified for a document.

        - **SourceField** *(string) --*

          A string that represents the name of an index field. CloudSearch supports regular index
          fields as well as dynamic fields. A dynamic field's name defines a pattern that begins
          or ends with a wildcard. Any document fields that don't map to a regular index field
          but do match a dynamic field's pattern are configured with the dynamic field's indexing
          options.

          Regular field names begin with a letter and can contain the following characters: a-z
          (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a
          wildcard (*). The wildcard can also be the only character in a dynamic field name.
          Multiple wildcards, and wildcards embedded within a string are not supported.

          The name ``score`` is reserved and cannot be used as a field name. To reference a
          document's ID, you can use the name ``_id`` .

        - **FacetEnabled** *(boolean) --*

          Whether facet information can be returned for the field.

        - **SearchEnabled** *(boolean) --*

          Whether the contents of the field are searchable.

        - **ReturnEnabled** *(boolean) --*

          Whether the contents of the field can be returned in the search results.

        - **SortEnabled** *(boolean) --*

          Whether the field can be used to sort the search results.

      - **IntArrayOptions** *(dict) --*

        Options for a field that contains an array of 64-bit signed integers. Present if
        ``IndexFieldType`` specifies the field is of type ``int-array`` . All options are enabled
        by default.

        - **DefaultValue** *(integer) --* A value to use for the field if the field isn't
        specified for a document.

        - **SourceFields** *(string) --*

          A list of source fields to map to the field.

        - **FacetEnabled** *(boolean) --*

          Whether facet information can be returned for the field.

        - **SearchEnabled** *(boolean) --*

          Whether the contents of the field are searchable.

        - **ReturnEnabled** *(boolean) --*

          Whether the contents of the field can be returned in the search results.

      - **DoubleArrayOptions** *(dict) --*

        Options for a field that contains an array of double-precision 64-bit floating point
        values. Present if ``IndexFieldType`` specifies the field is of type ``double-array`` .
        All options are enabled by default.

        - **DefaultValue** *(float) --* A value to use for the field if the field isn't specified
        for a document.

        - **SourceFields** *(string) --*

          A list of source fields to map to the field.

        - **FacetEnabled** *(boolean) --*

          Whether facet information can be returned for the field.

        - **SearchEnabled** *(boolean) --*

          Whether the contents of the field are searchable.

        - **ReturnEnabled** *(boolean) --*

          Whether the contents of the field can be returned in the search results.

      - **LiteralArrayOptions** *(dict) --*

        Options for a field that contains an array of literal strings. Present if
        ``IndexFieldType`` specifies the field is of type ``literal-array`` . All options are
        enabled by default.

        - **DefaultValue** *(string) --* A value to use for the field if the field isn't
        specified for a document.

        - **SourceFields** *(string) --*

          A list of source fields to map to the field.

        - **FacetEnabled** *(boolean) --*

          Whether facet information can be returned for the field.

        - **SearchEnabled** *(boolean) --*

          Whether the contents of the field are searchable.

        - **ReturnEnabled** *(boolean) --*

          Whether the contents of the field can be returned in the search results.

      - **TextArrayOptions** *(dict) --*

        Options for a field that contains an array of text strings. Present if ``IndexFieldType``
        specifies the field is of type ``text-array`` . A ``text-array`` field is always
        searchable. All options are enabled by default.

        - **DefaultValue** *(string) --* A value to use for the field if the field isn't
        specified for a document.

        - **SourceFields** *(string) --*

          A list of source fields to map to the field.

        - **ReturnEnabled** *(boolean) --*

          Whether the contents of the field can be returned in the search results.

        - **HighlightEnabled** *(boolean) --*

          Whether highlights can be returned for the field.

        - **AnalysisScheme** *(string) --*

          The name of an analysis scheme for a ``text-array`` field.

      - **DateArrayOptions** *(dict) --*

        Options for a field that contains an array of dates. Present if ``IndexFieldType``
        specifies the field is of type ``date-array`` . All options are enabled by default.

        - **DefaultValue** *(string) --* A value to use for the field if the field isn't
        specified for a document.

        - **SourceFields** *(string) --*

          A list of source fields to map to the field.

        - **FacetEnabled** *(boolean) --*

          Whether facet information can be returned for the field.

        - **SearchEnabled** *(boolean) --*

          Whether the contents of the field are searchable.

        - **ReturnEnabled** *(boolean) --*

          Whether the contents of the field can be returned in the search results.

    - **Status** *(dict) --*

      The status of domain configuration option.

      - **CreationDate** *(datetime) --*

        A timestamp for when this option was created.

      - **UpdateDate** *(datetime) --*

        A timestamp for when this option was last updated.

      - **UpdateVersion** *(integer) --*

        A unique integer that indicates when this option was last updated.

      - **State** *(string) --*

        The state of processing a change to an option. Possible values:

        * ``RequiresIndexDocuments`` : the option's latest value will not be deployed until
        IndexDocuments has been called and indexing is complete.

        * ``Processing`` : the option's latest value is in the process of being activated.

        * ``Active`` : the option's latest value is completely deployed.

        * ``FailedToValidate`` : the option value is not compatible with the domain's data and
        cannot be used to index the data. You must either modify the option value or update or
        remove the incompatible documents.

      - **PendingDeletion** *(boolean) --*

        Indicates that the option will be deleted once processing is complete.
    """


_ClientDefineIndexFieldResponseTypeDef = TypedDict(
    "_ClientDefineIndexFieldResponseTypeDef",
    {"IndexField": ClientDefineIndexFieldResponseIndexFieldTypeDef},
    total=False,
)


class ClientDefineIndexFieldResponseTypeDef(_ClientDefineIndexFieldResponseTypeDef):
    """
    Type definition for `ClientDefineIndexField` `Response`

    The result of a `` DefineIndexField`` request. Contains the status of the newly-configured
    index field.

    - **IndexField** *(dict) --*

      The value of an ``IndexField`` and its current status.

      - **Options** *(dict) --*

        Configuration information for a field in the index, including its name, type, and options.
        The supported options depend on the `` IndexFieldType`` .

        - **IndexFieldName** *(string) --*

          A string that represents the name of an index field. CloudSearch supports regular index
          fields as well as dynamic fields. A dynamic field's name defines a pattern that begins or
          ends with a wildcard. Any document fields that don't map to a regular index field but do
          match a dynamic field's pattern are configured with the dynamic field's indexing options.

          Regular field names begin with a letter and can contain the following characters: a-z
          (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a
          wildcard (*). The wildcard can also be the only character in a dynamic field name.
          Multiple wildcards, and wildcards embedded within a string are not supported.

          The name ``score`` is reserved and cannot be used as a field name. To reference a
          document's ID, you can use the name ``_id`` .

        - **IndexFieldType** *(string) --*

          The type of field. The valid options for a field depend on the field type. For more
          information about the supported field types, see `Configuring Index Fields
          <http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-index-fields.html>`__
          in the *Amazon CloudSearch Developer Guide* .

        - **IntOptions** *(dict) --*

          Options for a 64-bit signed integer field. Present if ``IndexFieldType`` specifies the
          field is of type ``int`` . All options are enabled by default.

          - **DefaultValue** *(integer) --* A value to use for the field if the field isn't
          specified for a document. This can be important if you are using the field in an
          expression and that field is not present in every document.

          - **SourceField** *(string) --*

            The name of the source field to map to the field.

          - **FacetEnabled** *(boolean) --*

            Whether facet information can be returned for the field.

          - **SearchEnabled** *(boolean) --*

            Whether the contents of the field are searchable.

          - **ReturnEnabled** *(boolean) --*

            Whether the contents of the field can be returned in the search results.

          - **SortEnabled** *(boolean) --*

            Whether the field can be used to sort the search results.

        - **DoubleOptions** *(dict) --*

          Options for a double-precision 64-bit floating point field. Present if ``IndexFieldType``
          specifies the field is of type ``double`` . All options are enabled by default.

          - **DefaultValue** *(float) --*

            A value to use for the field if the field isn't specified for a document. This can be
            important if you are using the field in an expression and that field is not present in
            every document.

          - **SourceField** *(string) --*

            The name of the source field to map to the field.

          - **FacetEnabled** *(boolean) --*

            Whether facet information can be returned for the field.

          - **SearchEnabled** *(boolean) --*

            Whether the contents of the field are searchable.

          - **ReturnEnabled** *(boolean) --*

            Whether the contents of the field can be returned in the search results.

          - **SortEnabled** *(boolean) --*

            Whether the field can be used to sort the search results.

        - **LiteralOptions** *(dict) --*

          Options for literal field. Present if ``IndexFieldType`` specifies the field is of type
          ``literal`` . All options are enabled by default.

          - **DefaultValue** *(string) --* A value to use for the field if the field isn't
          specified for a document.

          - **SourceField** *(string) --*

            A string that represents the name of an index field. CloudSearch supports regular index
            fields as well as dynamic fields. A dynamic field's name defines a pattern that begins
            or ends with a wildcard. Any document fields that don't map to a regular index field
            but do match a dynamic field's pattern are configured with the dynamic field's indexing
            options.

            Regular field names begin with a letter and can contain the following characters: a-z
            (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a
            wildcard (*). The wildcard can also be the only character in a dynamic field name.
            Multiple wildcards, and wildcards embedded within a string are not supported.

            The name ``score`` is reserved and cannot be used as a field name. To reference a
            document's ID, you can use the name ``_id`` .

          - **FacetEnabled** *(boolean) --*

            Whether facet information can be returned for the field.

          - **SearchEnabled** *(boolean) --*

            Whether the contents of the field are searchable.

          - **ReturnEnabled** *(boolean) --*

            Whether the contents of the field can be returned in the search results.

          - **SortEnabled** *(boolean) --*

            Whether the field can be used to sort the search results.

        - **TextOptions** *(dict) --*

          Options for text field. Present if ``IndexFieldType`` specifies the field is of type
          ``text`` . A ``text`` field is always searchable. All options are enabled by default.

          - **DefaultValue** *(string) --* A value to use for the field if the field isn't
          specified for a document.

          - **SourceField** *(string) --*

            A string that represents the name of an index field. CloudSearch supports regular index
            fields as well as dynamic fields. A dynamic field's name defines a pattern that begins
            or ends with a wildcard. Any document fields that don't map to a regular index field
            but do match a dynamic field's pattern are configured with the dynamic field's indexing
            options.

            Regular field names begin with a letter and can contain the following characters: a-z
            (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a
            wildcard (*). The wildcard can also be the only character in a dynamic field name.
            Multiple wildcards, and wildcards embedded within a string are not supported.

            The name ``score`` is reserved and cannot be used as a field name. To reference a
            document's ID, you can use the name ``_id`` .

          - **ReturnEnabled** *(boolean) --*

            Whether the contents of the field can be returned in the search results.

          - **SortEnabled** *(boolean) --*

            Whether the field can be used to sort the search results.

          - **HighlightEnabled** *(boolean) --*

            Whether highlights can be returned for the field.

          - **AnalysisScheme** *(string) --*

            The name of an analysis scheme for a ``text`` field.

        - **DateOptions** *(dict) --*

          Options for a date field. Dates and times are specified in UTC (Coordinated Universal
          Time) according to IETF RFC3339: yyyy-mm-ddT00:00:00Z. Present if ``IndexFieldType``
          specifies the field is of type ``date`` . All options are enabled by default.

          - **DefaultValue** *(string) --* A value to use for the field if the field isn't
          specified for a document.

          - **SourceField** *(string) --*

            A string that represents the name of an index field. CloudSearch supports regular index
            fields as well as dynamic fields. A dynamic field's name defines a pattern that begins
            or ends with a wildcard. Any document fields that don't map to a regular index field
            but do match a dynamic field's pattern are configured with the dynamic field's indexing
            options.

            Regular field names begin with a letter and can contain the following characters: a-z
            (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a
            wildcard (*). The wildcard can also be the only character in a dynamic field name.
            Multiple wildcards, and wildcards embedded within a string are not supported.

            The name ``score`` is reserved and cannot be used as a field name. To reference a
            document's ID, you can use the name ``_id`` .

          - **FacetEnabled** *(boolean) --*

            Whether facet information can be returned for the field.

          - **SearchEnabled** *(boolean) --*

            Whether the contents of the field are searchable.

          - **ReturnEnabled** *(boolean) --*

            Whether the contents of the field can be returned in the search results.

          - **SortEnabled** *(boolean) --*

            Whether the field can be used to sort the search results.

        - **LatLonOptions** *(dict) --*

          Options for a latlon field. A latlon field contains a location stored as a latitude and
          longitude value pair. Present if ``IndexFieldType`` specifies the field is of type
          ``latlon`` . All options are enabled by default.

          - **DefaultValue** *(string) --* A value to use for the field if the field isn't
          specified for a document.

          - **SourceField** *(string) --*

            A string that represents the name of an index field. CloudSearch supports regular index
            fields as well as dynamic fields. A dynamic field's name defines a pattern that begins
            or ends with a wildcard. Any document fields that don't map to a regular index field
            but do match a dynamic field's pattern are configured with the dynamic field's indexing
            options.

            Regular field names begin with a letter and can contain the following characters: a-z
            (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a
            wildcard (*). The wildcard can also be the only character in a dynamic field name.
            Multiple wildcards, and wildcards embedded within a string are not supported.

            The name ``score`` is reserved and cannot be used as a field name. To reference a
            document's ID, you can use the name ``_id`` .

          - **FacetEnabled** *(boolean) --*

            Whether facet information can be returned for the field.

          - **SearchEnabled** *(boolean) --*

            Whether the contents of the field are searchable.

          - **ReturnEnabled** *(boolean) --*

            Whether the contents of the field can be returned in the search results.

          - **SortEnabled** *(boolean) --*

            Whether the field can be used to sort the search results.

        - **IntArrayOptions** *(dict) --*

          Options for a field that contains an array of 64-bit signed integers. Present if
          ``IndexFieldType`` specifies the field is of type ``int-array`` . All options are enabled
          by default.

          - **DefaultValue** *(integer) --* A value to use for the field if the field isn't
          specified for a document.

          - **SourceFields** *(string) --*

            A list of source fields to map to the field.

          - **FacetEnabled** *(boolean) --*

            Whether facet information can be returned for the field.

          - **SearchEnabled** *(boolean) --*

            Whether the contents of the field are searchable.

          - **ReturnEnabled** *(boolean) --*

            Whether the contents of the field can be returned in the search results.

        - **DoubleArrayOptions** *(dict) --*

          Options for a field that contains an array of double-precision 64-bit floating point
          values. Present if ``IndexFieldType`` specifies the field is of type ``double-array`` .
          All options are enabled by default.

          - **DefaultValue** *(float) --* A value to use for the field if the field isn't specified
          for a document.

          - **SourceFields** *(string) --*

            A list of source fields to map to the field.

          - **FacetEnabled** *(boolean) --*

            Whether facet information can be returned for the field.

          - **SearchEnabled** *(boolean) --*

            Whether the contents of the field are searchable.

          - **ReturnEnabled** *(boolean) --*

            Whether the contents of the field can be returned in the search results.

        - **LiteralArrayOptions** *(dict) --*

          Options for a field that contains an array of literal strings. Present if
          ``IndexFieldType`` specifies the field is of type ``literal-array`` . All options are
          enabled by default.

          - **DefaultValue** *(string) --* A value to use for the field if the field isn't
          specified for a document.

          - **SourceFields** *(string) --*

            A list of source fields to map to the field.

          - **FacetEnabled** *(boolean) --*

            Whether facet information can be returned for the field.

          - **SearchEnabled** *(boolean) --*

            Whether the contents of the field are searchable.

          - **ReturnEnabled** *(boolean) --*

            Whether the contents of the field can be returned in the search results.

        - **TextArrayOptions** *(dict) --*

          Options for a field that contains an array of text strings. Present if ``IndexFieldType``
          specifies the field is of type ``text-array`` . A ``text-array`` field is always
          searchable. All options are enabled by default.

          - **DefaultValue** *(string) --* A value to use for the field if the field isn't
          specified for a document.

          - **SourceFields** *(string) --*

            A list of source fields to map to the field.

          - **ReturnEnabled** *(boolean) --*

            Whether the contents of the field can be returned in the search results.

          - **HighlightEnabled** *(boolean) --*

            Whether highlights can be returned for the field.

          - **AnalysisScheme** *(string) --*

            The name of an analysis scheme for a ``text-array`` field.

        - **DateArrayOptions** *(dict) --*

          Options for a field that contains an array of dates. Present if ``IndexFieldType``
          specifies the field is of type ``date-array`` . All options are enabled by default.

          - **DefaultValue** *(string) --* A value to use for the field if the field isn't
          specified for a document.

          - **SourceFields** *(string) --*

            A list of source fields to map to the field.

          - **FacetEnabled** *(boolean) --*

            Whether facet information can be returned for the field.

          - **SearchEnabled** *(boolean) --*

            Whether the contents of the field are searchable.

          - **ReturnEnabled** *(boolean) --*

            Whether the contents of the field can be returned in the search results.

      - **Status** *(dict) --*

        The status of domain configuration option.

        - **CreationDate** *(datetime) --*

          A timestamp for when this option was created.

        - **UpdateDate** *(datetime) --*

          A timestamp for when this option was last updated.

        - **UpdateVersion** *(integer) --*

          A unique integer that indicates when this option was last updated.

        - **State** *(string) --*

          The state of processing a change to an option. Possible values:

          * ``RequiresIndexDocuments`` : the option's latest value will not be deployed until
          IndexDocuments has been called and indexing is complete.

          * ``Processing`` : the option's latest value is in the process of being activated.

          * ``Active`` : the option's latest value is completely deployed.

          * ``FailedToValidate`` : the option value is not compatible with the domain's data and
          cannot be used to index the data. You must either modify the option value or update or
          remove the incompatible documents.

        - **PendingDeletion** *(boolean) --*

          Indicates that the option will be deleted once processing is complete.
    """


_ClientDefineSuggesterResponseSuggesterOptionsDocumentSuggesterOptionsTypeDef = TypedDict(
    "_ClientDefineSuggesterResponseSuggesterOptionsDocumentSuggesterOptionsTypeDef",
    {"SourceField": str, "FuzzyMatching": str, "SortExpression": str},
    total=False,
)


class ClientDefineSuggesterResponseSuggesterOptionsDocumentSuggesterOptionsTypeDef(
    _ClientDefineSuggesterResponseSuggesterOptionsDocumentSuggesterOptionsTypeDef
):
    """
    Type definition for `ClientDefineSuggesterResponseSuggesterOptions` `DocumentSuggesterOptions`

    Options for a search suggester.

    - **SourceField** *(string) --*

      The name of the index field you want to use for suggestions.

    - **FuzzyMatching** *(string) --*

      The level of fuzziness allowed when suggesting matches for a string: ``none`` , ``low``
      , or ``high`` . With none, the specified string is treated as an exact prefix. With
      low, suggestions must differ from the specified string by no more than one character.
      With high, suggestions can differ by up to two characters. The default is none.

    - **SortExpression** *(string) --*

      An expression that computes a score for each suggestion to control how they are sorted.
      The scores are rounded to the nearest integer, with a floor of 0 and a ceiling of
      2^31-1. A document's relevance score is not computed for suggestions, so sort
      expressions cannot reference the ``_score`` value. To sort suggestions using a numeric
      field or existing expression, simply specify the name of the field or expression. If no
      expression is configured for the suggester, the suggestions are sorted with the closest
      matches listed first.
    """


_ClientDefineSuggesterResponseSuggesterOptionsTypeDef = TypedDict(
    "_ClientDefineSuggesterResponseSuggesterOptionsTypeDef",
    {
        "SuggesterName": str,
        "DocumentSuggesterOptions": ClientDefineSuggesterResponseSuggesterOptionsDocumentSuggesterOptionsTypeDef,
    },
    total=False,
)


class ClientDefineSuggesterResponseSuggesterOptionsTypeDef(
    _ClientDefineSuggesterResponseSuggesterOptionsTypeDef
):
    """
    Type definition for `ClientDefineSuggesterResponseSuggester` `Options`

    Configuration information for a search suggester. Each suggester has a unique name and
    specifies the text field you want to use for suggestions. The following options can be
    configured for a suggester: ``FuzzyMatching`` , ``SortExpression`` .

    - **SuggesterName** *(string) --*

      Names must begin with a letter and can contain the following characters: a-z (lowercase),
      0-9, and _ (underscore).

    - **DocumentSuggesterOptions** *(dict) --*

      Options for a search suggester.

      - **SourceField** *(string) --*

        The name of the index field you want to use for suggestions.

      - **FuzzyMatching** *(string) --*

        The level of fuzziness allowed when suggesting matches for a string: ``none`` , ``low``
        , or ``high`` . With none, the specified string is treated as an exact prefix. With
        low, suggestions must differ from the specified string by no more than one character.
        With high, suggestions can differ by up to two characters. The default is none.

      - **SortExpression** *(string) --*

        An expression that computes a score for each suggestion to control how they are sorted.
        The scores are rounded to the nearest integer, with a floor of 0 and a ceiling of
        2^31-1. A document's relevance score is not computed for suggestions, so sort
        expressions cannot reference the ``_score`` value. To sort suggestions using a numeric
        field or existing expression, simply specify the name of the field or expression. If no
        expression is configured for the suggester, the suggestions are sorted with the closest
        matches listed first.
    """


_ClientDefineSuggesterResponseSuggesterStatusTypeDef = TypedDict(
    "_ClientDefineSuggesterResponseSuggesterStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": str,
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientDefineSuggesterResponseSuggesterStatusTypeDef(
    _ClientDefineSuggesterResponseSuggesterStatusTypeDef
):
    """
    Type definition for `ClientDefineSuggesterResponseSuggester` `Status`

    The status of domain configuration option.

    - **CreationDate** *(datetime) --*

      A timestamp for when this option was created.

    - **UpdateDate** *(datetime) --*

      A timestamp for when this option was last updated.

    - **UpdateVersion** *(integer) --*

      A unique integer that indicates when this option was last updated.

    - **State** *(string) --*

      The state of processing a change to an option. Possible values:

      * ``RequiresIndexDocuments`` : the option's latest value will not be deployed until
      IndexDocuments has been called and indexing is complete.

      * ``Processing`` : the option's latest value is in the process of being activated.

      * ``Active`` : the option's latest value is completely deployed.

      * ``FailedToValidate`` : the option value is not compatible with the domain's data and
      cannot be used to index the data. You must either modify the option value or update or
      remove the incompatible documents.

    - **PendingDeletion** *(boolean) --*

      Indicates that the option will be deleted once processing is complete.
    """


_ClientDefineSuggesterResponseSuggesterTypeDef = TypedDict(
    "_ClientDefineSuggesterResponseSuggesterTypeDef",
    {
        "Options": ClientDefineSuggesterResponseSuggesterOptionsTypeDef,
        "Status": ClientDefineSuggesterResponseSuggesterStatusTypeDef,
    },
    total=False,
)


class ClientDefineSuggesterResponseSuggesterTypeDef(
    _ClientDefineSuggesterResponseSuggesterTypeDef
):
    """
    Type definition for `ClientDefineSuggesterResponse` `Suggester`

    The value of a ``Suggester`` and its current status.

    - **Options** *(dict) --*

      Configuration information for a search suggester. Each suggester has a unique name and
      specifies the text field you want to use for suggestions. The following options can be
      configured for a suggester: ``FuzzyMatching`` , ``SortExpression`` .

      - **SuggesterName** *(string) --*

        Names must begin with a letter and can contain the following characters: a-z (lowercase),
        0-9, and _ (underscore).

      - **DocumentSuggesterOptions** *(dict) --*

        Options for a search suggester.

        - **SourceField** *(string) --*

          The name of the index field you want to use for suggestions.

        - **FuzzyMatching** *(string) --*

          The level of fuzziness allowed when suggesting matches for a string: ``none`` , ``low``
          , or ``high`` . With none, the specified string is treated as an exact prefix. With
          low, suggestions must differ from the specified string by no more than one character.
          With high, suggestions can differ by up to two characters. The default is none.

        - **SortExpression** *(string) --*

          An expression that computes a score for each suggestion to control how they are sorted.
          The scores are rounded to the nearest integer, with a floor of 0 and a ceiling of
          2^31-1. A document's relevance score is not computed for suggestions, so sort
          expressions cannot reference the ``_score`` value. To sort suggestions using a numeric
          field or existing expression, simply specify the name of the field or expression. If no
          expression is configured for the suggester, the suggestions are sorted with the closest
          matches listed first.

    - **Status** *(dict) --*

      The status of domain configuration option.

      - **CreationDate** *(datetime) --*

        A timestamp for when this option was created.

      - **UpdateDate** *(datetime) --*

        A timestamp for when this option was last updated.

      - **UpdateVersion** *(integer) --*

        A unique integer that indicates when this option was last updated.

      - **State** *(string) --*

        The state of processing a change to an option. Possible values:

        * ``RequiresIndexDocuments`` : the option's latest value will not be deployed until
        IndexDocuments has been called and indexing is complete.

        * ``Processing`` : the option's latest value is in the process of being activated.

        * ``Active`` : the option's latest value is completely deployed.

        * ``FailedToValidate`` : the option value is not compatible with the domain's data and
        cannot be used to index the data. You must either modify the option value or update or
        remove the incompatible documents.

      - **PendingDeletion** *(boolean) --*

        Indicates that the option will be deleted once processing is complete.
    """


_ClientDefineSuggesterResponseTypeDef = TypedDict(
    "_ClientDefineSuggesterResponseTypeDef",
    {"Suggester": ClientDefineSuggesterResponseSuggesterTypeDef},
    total=False,
)


class ClientDefineSuggesterResponseTypeDef(_ClientDefineSuggesterResponseTypeDef):
    """
    Type definition for `ClientDefineSuggester` `Response`

    The result of a ``DefineSuggester`` request. Contains the status of the newly-configured
    suggester.

    - **Suggester** *(dict) --*

      The value of a ``Suggester`` and its current status.

      - **Options** *(dict) --*

        Configuration information for a search suggester. Each suggester has a unique name and
        specifies the text field you want to use for suggestions. The following options can be
        configured for a suggester: ``FuzzyMatching`` , ``SortExpression`` .

        - **SuggesterName** *(string) --*

          Names must begin with a letter and can contain the following characters: a-z (lowercase),
          0-9, and _ (underscore).

        - **DocumentSuggesterOptions** *(dict) --*

          Options for a search suggester.

          - **SourceField** *(string) --*

            The name of the index field you want to use for suggestions.

          - **FuzzyMatching** *(string) --*

            The level of fuzziness allowed when suggesting matches for a string: ``none`` , ``low``
            , or ``high`` . With none, the specified string is treated as an exact prefix. With
            low, suggestions must differ from the specified string by no more than one character.
            With high, suggestions can differ by up to two characters. The default is none.

          - **SortExpression** *(string) --*

            An expression that computes a score for each suggestion to control how they are sorted.
            The scores are rounded to the nearest integer, with a floor of 0 and a ceiling of
            2^31-1. A document's relevance score is not computed for suggestions, so sort
            expressions cannot reference the ``_score`` value. To sort suggestions using a numeric
            field or existing expression, simply specify the name of the field or expression. If no
            expression is configured for the suggester, the suggestions are sorted with the closest
            matches listed first.

      - **Status** *(dict) --*

        The status of domain configuration option.

        - **CreationDate** *(datetime) --*

          A timestamp for when this option was created.

        - **UpdateDate** *(datetime) --*

          A timestamp for when this option was last updated.

        - **UpdateVersion** *(integer) --*

          A unique integer that indicates when this option was last updated.

        - **State** *(string) --*

          The state of processing a change to an option. Possible values:

          * ``RequiresIndexDocuments`` : the option's latest value will not be deployed until
          IndexDocuments has been called and indexing is complete.

          * ``Processing`` : the option's latest value is in the process of being activated.

          * ``Active`` : the option's latest value is completely deployed.

          * ``FailedToValidate`` : the option value is not compatible with the domain's data and
          cannot be used to index the data. You must either modify the option value or update or
          remove the incompatible documents.

        - **PendingDeletion** *(boolean) --*

          Indicates that the option will be deleted once processing is complete.
    """


_RequiredClientDefineSuggesterSuggesterDocumentSuggesterOptionsTypeDef = TypedDict(
    "_RequiredClientDefineSuggesterSuggesterDocumentSuggesterOptionsTypeDef",
    {"SourceField": str},
)
_OptionalClientDefineSuggesterSuggesterDocumentSuggesterOptionsTypeDef = TypedDict(
    "_OptionalClientDefineSuggesterSuggesterDocumentSuggesterOptionsTypeDef",
    {"FuzzyMatching": str, "SortExpression": str},
    total=False,
)


class ClientDefineSuggesterSuggesterDocumentSuggesterOptionsTypeDef(
    _RequiredClientDefineSuggesterSuggesterDocumentSuggesterOptionsTypeDef,
    _OptionalClientDefineSuggesterSuggesterDocumentSuggesterOptionsTypeDef,
):
    """
    Type definition for `ClientDefineSuggesterSuggester` `DocumentSuggesterOptions`

    Options for a search suggester.

    - **SourceField** *(string) --* **[REQUIRED]**

      The name of the index field you want to use for suggestions.

    - **FuzzyMatching** *(string) --*

      The level of fuzziness allowed when suggesting matches for a string: ``none`` , ``low`` , or
      ``high`` . With none, the specified string is treated as an exact prefix. With low,
      suggestions must differ from the specified string by no more than one character. With high,
      suggestions can differ by up to two characters. The default is none.

    - **SortExpression** *(string) --*

      An expression that computes a score for each suggestion to control how they are sorted. The
      scores are rounded to the nearest integer, with a floor of 0 and a ceiling of 2^31-1. A
      document's relevance score is not computed for suggestions, so sort expressions cannot
      reference the ``_score`` value. To sort suggestions using a numeric field or existing
      expression, simply specify the name of the field or expression. If no expression is
      configured for the suggester, the suggestions are sorted with the closest matches listed
      first.
    """


_ClientDefineSuggesterSuggesterTypeDef = TypedDict(
    "_ClientDefineSuggesterSuggesterTypeDef",
    {
        "SuggesterName": str,
        "DocumentSuggesterOptions": ClientDefineSuggesterSuggesterDocumentSuggesterOptionsTypeDef,
    },
)


class ClientDefineSuggesterSuggesterTypeDef(_ClientDefineSuggesterSuggesterTypeDef):
    """
    Type definition for `ClientDefineSuggester` `Suggester`

    Configuration information for a search suggester. Each suggester has a unique name and specifies
    the text field you want to use for suggestions. The following options can be configured for a
    suggester: ``FuzzyMatching`` , ``SortExpression`` .

    - **SuggesterName** *(string) --* **[REQUIRED]**

      Names must begin with a letter and can contain the following characters: a-z (lowercase), 0-9,
      and _ (underscore).

    - **DocumentSuggesterOptions** *(dict) --* **[REQUIRED]**

      Options for a search suggester.

      - **SourceField** *(string) --* **[REQUIRED]**

        The name of the index field you want to use for suggestions.

      - **FuzzyMatching** *(string) --*

        The level of fuzziness allowed when suggesting matches for a string: ``none`` , ``low`` , or
        ``high`` . With none, the specified string is treated as an exact prefix. With low,
        suggestions must differ from the specified string by no more than one character. With high,
        suggestions can differ by up to two characters. The default is none.

      - **SortExpression** *(string) --*

        An expression that computes a score for each suggestion to control how they are sorted. The
        scores are rounded to the nearest integer, with a floor of 0 and a ceiling of 2^31-1. A
        document's relevance score is not computed for suggestions, so sort expressions cannot
        reference the ``_score`` value. To sort suggestions using a numeric field or existing
        expression, simply specify the name of the field or expression. If no expression is
        configured for the suggester, the suggestions are sorted with the closest matches listed
        first.
    """


_ClientDeleteAnalysisSchemeResponseAnalysisSchemeOptionsAnalysisOptionsTypeDef = TypedDict(
    "_ClientDeleteAnalysisSchemeResponseAnalysisSchemeOptionsAnalysisOptionsTypeDef",
    {
        "Synonyms": str,
        "Stopwords": str,
        "StemmingDictionary": str,
        "JapaneseTokenizationDictionary": str,
        "AlgorithmicStemming": str,
    },
    total=False,
)


class ClientDeleteAnalysisSchemeResponseAnalysisSchemeOptionsAnalysisOptionsTypeDef(
    _ClientDeleteAnalysisSchemeResponseAnalysisSchemeOptionsAnalysisOptionsTypeDef
):
    """
    Type definition for `ClientDeleteAnalysisSchemeResponseAnalysisSchemeOptions` `AnalysisOptions`

    Synonyms, stopwords, and stemming options for an analysis scheme. Includes tokenization
    dictionary for Japanese.

    - **Synonyms** *(string) --*

      A JSON object that defines synonym groups and aliases. A synonym group is an array of
      arrays, where each sub-array is a group of terms where each term in the group is
      considered a synonym of every other term in the group. The aliases value is an object
      that contains a collection of string:value pairs where the string specifies a term and
      the array of values specifies each of the aliases for that term. An alias is considered
      a synonym of the specified term, but the term is not considered a synonym of the alias.
      For more information about specifying synonyms, see `Synonyms
      <http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-analysis-schemes.html#synonyms>`__
      in the *Amazon CloudSearch Developer Guide* .

    - **Stopwords** *(string) --*

      A JSON array of terms to ignore during indexing and searching. For example, ``["a",
      "an", "the", "of"]`` . The stopwords dictionary must explicitly list each word you want
      to ignore. Wildcards and regular expressions are not supported.

    - **StemmingDictionary** *(string) --*

      A JSON object that contains a collection of string:value pairs that each map a term to
      its stem. For example, ``{"term1": "stem1", "term2": "stem2", "term3": "stem3"}`` . The
      stemming dictionary is applied in addition to any algorithmic stemming. This enables
      you to override the results of the algorithmic stemming to correct specific cases of
      overstemming or understemming. The maximum size of a stemming dictionary is 500 KB.

    - **JapaneseTokenizationDictionary** *(string) --*

      A JSON array that contains a collection of terms, tokens, readings and part of speech
      for Japanese Tokenizaiton. The Japanese tokenization dictionary enables you to override
      the default tokenization for selected terms. This is only valid for Japanese language
      fields.

    - **AlgorithmicStemming** *(string) --*

      The level of algorithmic stemming to perform: ``none`` , ``minimal`` , ``light`` , or
      ``full`` . The available levels vary depending on the language. For more information,
      see `Language Specific Text Processing Settings
      <http://docs.aws.amazon.com/cloudsearch/latest/developerguide/text-processing.html#text-processing-settings>`__
      in the *Amazon CloudSearch Developer Guide*
    """


_ClientDeleteAnalysisSchemeResponseAnalysisSchemeOptionsTypeDef = TypedDict(
    "_ClientDeleteAnalysisSchemeResponseAnalysisSchemeOptionsTypeDef",
    {
        "AnalysisSchemeName": str,
        "AnalysisSchemeLanguage": str,
        "AnalysisOptions": ClientDeleteAnalysisSchemeResponseAnalysisSchemeOptionsAnalysisOptionsTypeDef,
    },
    total=False,
)


class ClientDeleteAnalysisSchemeResponseAnalysisSchemeOptionsTypeDef(
    _ClientDeleteAnalysisSchemeResponseAnalysisSchemeOptionsTypeDef
):
    """
    Type definition for `ClientDeleteAnalysisSchemeResponseAnalysisScheme` `Options`

    Configuration information for an analysis scheme. Each analysis scheme has a unique name
    and specifies the language of the text to be processed. The following options can be
    configured for an analysis scheme: ``Synonyms`` , ``Stopwords`` , ``StemmingDictionary`` ,
    ``JapaneseTokenizationDictionary`` and ``AlgorithmicStemming`` .

    - **AnalysisSchemeName** *(string) --*

      Names must begin with a letter and can contain the following characters: a-z (lowercase),
      0-9, and _ (underscore).

    - **AnalysisSchemeLanguage** *(string) --*

      An `IETF RFC 4646 <http://tools.ietf.org/html/rfc4646>`__ language code or ``mul`` for
      multiple languages.

    - **AnalysisOptions** *(dict) --*

      Synonyms, stopwords, and stemming options for an analysis scheme. Includes tokenization
      dictionary for Japanese.

      - **Synonyms** *(string) --*

        A JSON object that defines synonym groups and aliases. A synonym group is an array of
        arrays, where each sub-array is a group of terms where each term in the group is
        considered a synonym of every other term in the group. The aliases value is an object
        that contains a collection of string:value pairs where the string specifies a term and
        the array of values specifies each of the aliases for that term. An alias is considered
        a synonym of the specified term, but the term is not considered a synonym of the alias.
        For more information about specifying synonyms, see `Synonyms
        <http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-analysis-schemes.html#synonyms>`__
        in the *Amazon CloudSearch Developer Guide* .

      - **Stopwords** *(string) --*

        A JSON array of terms to ignore during indexing and searching. For example, ``["a",
        "an", "the", "of"]`` . The stopwords dictionary must explicitly list each word you want
        to ignore. Wildcards and regular expressions are not supported.

      - **StemmingDictionary** *(string) --*

        A JSON object that contains a collection of string:value pairs that each map a term to
        its stem. For example, ``{"term1": "stem1", "term2": "stem2", "term3": "stem3"}`` . The
        stemming dictionary is applied in addition to any algorithmic stemming. This enables
        you to override the results of the algorithmic stemming to correct specific cases of
        overstemming or understemming. The maximum size of a stemming dictionary is 500 KB.

      - **JapaneseTokenizationDictionary** *(string) --*

        A JSON array that contains a collection of terms, tokens, readings and part of speech
        for Japanese Tokenizaiton. The Japanese tokenization dictionary enables you to override
        the default tokenization for selected terms. This is only valid for Japanese language
        fields.

      - **AlgorithmicStemming** *(string) --*

        The level of algorithmic stemming to perform: ``none`` , ``minimal`` , ``light`` , or
        ``full`` . The available levels vary depending on the language. For more information,
        see `Language Specific Text Processing Settings
        <http://docs.aws.amazon.com/cloudsearch/latest/developerguide/text-processing.html#text-processing-settings>`__
        in the *Amazon CloudSearch Developer Guide*
    """


_ClientDeleteAnalysisSchemeResponseAnalysisSchemeStatusTypeDef = TypedDict(
    "_ClientDeleteAnalysisSchemeResponseAnalysisSchemeStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": str,
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientDeleteAnalysisSchemeResponseAnalysisSchemeStatusTypeDef(
    _ClientDeleteAnalysisSchemeResponseAnalysisSchemeStatusTypeDef
):
    """
    Type definition for `ClientDeleteAnalysisSchemeResponseAnalysisScheme` `Status`

    The status of domain configuration option.

    - **CreationDate** *(datetime) --*

      A timestamp for when this option was created.

    - **UpdateDate** *(datetime) --*

      A timestamp for when this option was last updated.

    - **UpdateVersion** *(integer) --*

      A unique integer that indicates when this option was last updated.

    - **State** *(string) --*

      The state of processing a change to an option. Possible values:

      * ``RequiresIndexDocuments`` : the option's latest value will not be deployed until
      IndexDocuments has been called and indexing is complete.

      * ``Processing`` : the option's latest value is in the process of being activated.

      * ``Active`` : the option's latest value is completely deployed.

      * ``FailedToValidate`` : the option value is not compatible with the domain's data and
      cannot be used to index the data. You must either modify the option value or update or
      remove the incompatible documents.

    - **PendingDeletion** *(boolean) --*

      Indicates that the option will be deleted once processing is complete.
    """


_ClientDeleteAnalysisSchemeResponseAnalysisSchemeTypeDef = TypedDict(
    "_ClientDeleteAnalysisSchemeResponseAnalysisSchemeTypeDef",
    {
        "Options": ClientDeleteAnalysisSchemeResponseAnalysisSchemeOptionsTypeDef,
        "Status": ClientDeleteAnalysisSchemeResponseAnalysisSchemeStatusTypeDef,
    },
    total=False,
)


class ClientDeleteAnalysisSchemeResponseAnalysisSchemeTypeDef(
    _ClientDeleteAnalysisSchemeResponseAnalysisSchemeTypeDef
):
    """
    Type definition for `ClientDeleteAnalysisSchemeResponse` `AnalysisScheme`

    The status of the analysis scheme being deleted.

    - **Options** *(dict) --*

      Configuration information for an analysis scheme. Each analysis scheme has a unique name
      and specifies the language of the text to be processed. The following options can be
      configured for an analysis scheme: ``Synonyms`` , ``Stopwords`` , ``StemmingDictionary`` ,
      ``JapaneseTokenizationDictionary`` and ``AlgorithmicStemming`` .

      - **AnalysisSchemeName** *(string) --*

        Names must begin with a letter and can contain the following characters: a-z (lowercase),
        0-9, and _ (underscore).

      - **AnalysisSchemeLanguage** *(string) --*

        An `IETF RFC 4646 <http://tools.ietf.org/html/rfc4646>`__ language code or ``mul`` for
        multiple languages.

      - **AnalysisOptions** *(dict) --*

        Synonyms, stopwords, and stemming options for an analysis scheme. Includes tokenization
        dictionary for Japanese.

        - **Synonyms** *(string) --*

          A JSON object that defines synonym groups and aliases. A synonym group is an array of
          arrays, where each sub-array is a group of terms where each term in the group is
          considered a synonym of every other term in the group. The aliases value is an object
          that contains a collection of string:value pairs where the string specifies a term and
          the array of values specifies each of the aliases for that term. An alias is considered
          a synonym of the specified term, but the term is not considered a synonym of the alias.
          For more information about specifying synonyms, see `Synonyms
          <http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-analysis-schemes.html#synonyms>`__
          in the *Amazon CloudSearch Developer Guide* .

        - **Stopwords** *(string) --*

          A JSON array of terms to ignore during indexing and searching. For example, ``["a",
          "an", "the", "of"]`` . The stopwords dictionary must explicitly list each word you want
          to ignore. Wildcards and regular expressions are not supported.

        - **StemmingDictionary** *(string) --*

          A JSON object that contains a collection of string:value pairs that each map a term to
          its stem. For example, ``{"term1": "stem1", "term2": "stem2", "term3": "stem3"}`` . The
          stemming dictionary is applied in addition to any algorithmic stemming. This enables
          you to override the results of the algorithmic stemming to correct specific cases of
          overstemming or understemming. The maximum size of a stemming dictionary is 500 KB.

        - **JapaneseTokenizationDictionary** *(string) --*

          A JSON array that contains a collection of terms, tokens, readings and part of speech
          for Japanese Tokenizaiton. The Japanese tokenization dictionary enables you to override
          the default tokenization for selected terms. This is only valid for Japanese language
          fields.

        - **AlgorithmicStemming** *(string) --*

          The level of algorithmic stemming to perform: ``none`` , ``minimal`` , ``light`` , or
          ``full`` . The available levels vary depending on the language. For more information,
          see `Language Specific Text Processing Settings
          <http://docs.aws.amazon.com/cloudsearch/latest/developerguide/text-processing.html#text-processing-settings>`__
          in the *Amazon CloudSearch Developer Guide*

    - **Status** *(dict) --*

      The status of domain configuration option.

      - **CreationDate** *(datetime) --*

        A timestamp for when this option was created.

      - **UpdateDate** *(datetime) --*

        A timestamp for when this option was last updated.

      - **UpdateVersion** *(integer) --*

        A unique integer that indicates when this option was last updated.

      - **State** *(string) --*

        The state of processing a change to an option. Possible values:

        * ``RequiresIndexDocuments`` : the option's latest value will not be deployed until
        IndexDocuments has been called and indexing is complete.

        * ``Processing`` : the option's latest value is in the process of being activated.

        * ``Active`` : the option's latest value is completely deployed.

        * ``FailedToValidate`` : the option value is not compatible with the domain's data and
        cannot be used to index the data. You must either modify the option value or update or
        remove the incompatible documents.

      - **PendingDeletion** *(boolean) --*

        Indicates that the option will be deleted once processing is complete.
    """


_ClientDeleteAnalysisSchemeResponseTypeDef = TypedDict(
    "_ClientDeleteAnalysisSchemeResponseTypeDef",
    {"AnalysisScheme": ClientDeleteAnalysisSchemeResponseAnalysisSchemeTypeDef},
    total=False,
)


class ClientDeleteAnalysisSchemeResponseTypeDef(
    _ClientDeleteAnalysisSchemeResponseTypeDef
):
    """
    Type definition for `ClientDeleteAnalysisScheme` `Response`

    The result of a ``DeleteAnalysisScheme`` request. Contains the status of the deleted analysis
    scheme.

    - **AnalysisScheme** *(dict) --*

      The status of the analysis scheme being deleted.

      - **Options** *(dict) --*

        Configuration information for an analysis scheme. Each analysis scheme has a unique name
        and specifies the language of the text to be processed. The following options can be
        configured for an analysis scheme: ``Synonyms`` , ``Stopwords`` , ``StemmingDictionary`` ,
        ``JapaneseTokenizationDictionary`` and ``AlgorithmicStemming`` .

        - **AnalysisSchemeName** *(string) --*

          Names must begin with a letter and can contain the following characters: a-z (lowercase),
          0-9, and _ (underscore).

        - **AnalysisSchemeLanguage** *(string) --*

          An `IETF RFC 4646 <http://tools.ietf.org/html/rfc4646>`__ language code or ``mul`` for
          multiple languages.

        - **AnalysisOptions** *(dict) --*

          Synonyms, stopwords, and stemming options for an analysis scheme. Includes tokenization
          dictionary for Japanese.

          - **Synonyms** *(string) --*

            A JSON object that defines synonym groups and aliases. A synonym group is an array of
            arrays, where each sub-array is a group of terms where each term in the group is
            considered a synonym of every other term in the group. The aliases value is an object
            that contains a collection of string:value pairs where the string specifies a term and
            the array of values specifies each of the aliases for that term. An alias is considered
            a synonym of the specified term, but the term is not considered a synonym of the alias.
            For more information about specifying synonyms, see `Synonyms
            <http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-analysis-schemes.html#synonyms>`__
            in the *Amazon CloudSearch Developer Guide* .

          - **Stopwords** *(string) --*

            A JSON array of terms to ignore during indexing and searching. For example, ``["a",
            "an", "the", "of"]`` . The stopwords dictionary must explicitly list each word you want
            to ignore. Wildcards and regular expressions are not supported.

          - **StemmingDictionary** *(string) --*

            A JSON object that contains a collection of string:value pairs that each map a term to
            its stem. For example, ``{"term1": "stem1", "term2": "stem2", "term3": "stem3"}`` . The
            stemming dictionary is applied in addition to any algorithmic stemming. This enables
            you to override the results of the algorithmic stemming to correct specific cases of
            overstemming or understemming. The maximum size of a stemming dictionary is 500 KB.

          - **JapaneseTokenizationDictionary** *(string) --*

            A JSON array that contains a collection of terms, tokens, readings and part of speech
            for Japanese Tokenizaiton. The Japanese tokenization dictionary enables you to override
            the default tokenization for selected terms. This is only valid for Japanese language
            fields.

          - **AlgorithmicStemming** *(string) --*

            The level of algorithmic stemming to perform: ``none`` , ``minimal`` , ``light`` , or
            ``full`` . The available levels vary depending on the language. For more information,
            see `Language Specific Text Processing Settings
            <http://docs.aws.amazon.com/cloudsearch/latest/developerguide/text-processing.html#text-processing-settings>`__
            in the *Amazon CloudSearch Developer Guide*

      - **Status** *(dict) --*

        The status of domain configuration option.

        - **CreationDate** *(datetime) --*

          A timestamp for when this option was created.

        - **UpdateDate** *(datetime) --*

          A timestamp for when this option was last updated.

        - **UpdateVersion** *(integer) --*

          A unique integer that indicates when this option was last updated.

        - **State** *(string) --*

          The state of processing a change to an option. Possible values:

          * ``RequiresIndexDocuments`` : the option's latest value will not be deployed until
          IndexDocuments has been called and indexing is complete.

          * ``Processing`` : the option's latest value is in the process of being activated.

          * ``Active`` : the option's latest value is completely deployed.

          * ``FailedToValidate`` : the option value is not compatible with the domain's data and
          cannot be used to index the data. You must either modify the option value or update or
          remove the incompatible documents.

        - **PendingDeletion** *(boolean) --*

          Indicates that the option will be deleted once processing is complete.
    """


_ClientDeleteDomainResponseDomainStatusDocServiceTypeDef = TypedDict(
    "_ClientDeleteDomainResponseDomainStatusDocServiceTypeDef",
    {"Endpoint": str},
    total=False,
)


class ClientDeleteDomainResponseDomainStatusDocServiceTypeDef(
    _ClientDeleteDomainResponseDomainStatusDocServiceTypeDef
):
    """
    Type definition for `ClientDeleteDomainResponseDomainStatus` `DocService`

    The service endpoint for updating documents in a search domain.

    - **Endpoint** *(string) --*

      The endpoint to which service requests can be submitted. For example,
      ``search-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.cloudsearch.amazonaws.com`` or
      ``doc-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.cloudsearch.amazonaws.com`` .
    """


_ClientDeleteDomainResponseDomainStatusLimitsTypeDef = TypedDict(
    "_ClientDeleteDomainResponseDomainStatusLimitsTypeDef",
    {"MaximumReplicationCount": int, "MaximumPartitionCount": int},
    total=False,
)


class ClientDeleteDomainResponseDomainStatusLimitsTypeDef(
    _ClientDeleteDomainResponseDomainStatusLimitsTypeDef
):
    """
    Type definition for `ClientDeleteDomainResponseDomainStatus` `Limits`

    - **MaximumReplicationCount** *(integer) --*

    - **MaximumPartitionCount** *(integer) --*
    """


_ClientDeleteDomainResponseDomainStatusSearchServiceTypeDef = TypedDict(
    "_ClientDeleteDomainResponseDomainStatusSearchServiceTypeDef",
    {"Endpoint": str},
    total=False,
)


class ClientDeleteDomainResponseDomainStatusSearchServiceTypeDef(
    _ClientDeleteDomainResponseDomainStatusSearchServiceTypeDef
):
    """
    Type definition for `ClientDeleteDomainResponseDomainStatus` `SearchService`

    The service endpoint for requesting search results from a search domain.

    - **Endpoint** *(string) --*

      The endpoint to which service requests can be submitted. For example,
      ``search-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.cloudsearch.amazonaws.com`` or
      ``doc-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.cloudsearch.amazonaws.com`` .
    """


_ClientDeleteDomainResponseDomainStatusTypeDef = TypedDict(
    "_ClientDeleteDomainResponseDomainStatusTypeDef",
    {
        "DomainId": str,
        "DomainName": str,
        "ARN": str,
        "Created": bool,
        "Deleted": bool,
        "DocService": ClientDeleteDomainResponseDomainStatusDocServiceTypeDef,
        "SearchService": ClientDeleteDomainResponseDomainStatusSearchServiceTypeDef,
        "RequiresIndexDocuments": bool,
        "Processing": bool,
        "SearchInstanceType": str,
        "SearchPartitionCount": int,
        "SearchInstanceCount": int,
        "Limits": ClientDeleteDomainResponseDomainStatusLimitsTypeDef,
    },
    total=False,
)


class ClientDeleteDomainResponseDomainStatusTypeDef(
    _ClientDeleteDomainResponseDomainStatusTypeDef
):
    """
    Type definition for `ClientDeleteDomainResponse` `DomainStatus`

    The current status of the search domain.

    - **DomainId** *(string) --*

      An internally generated unique identifier for a domain.

    - **DomainName** *(string) --*

      A string that represents the name of a domain. Domain names are unique across the domains
      owned by an account within an AWS region. Domain names start with a letter or number and
      can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).

    - **ARN** *(string) --*

      The Amazon Resource Name (ARN) of the search domain. See `Identifiers for IAM Entities
      <http://docs.aws.amazon.com/IAM/latest/UserGuide/index.html?Using_Identifiers.html>`__ in
      *Using AWS Identity and Access Management* for more information.

    - **Created** *(boolean) --*

      True if the search domain is created. It can take several minutes to initialize a domain
      when  CreateDomain is called. Newly created search domains are returned from
      DescribeDomains with a false value for Created until domain creation is complete.

    - **Deleted** *(boolean) --*

      True if the search domain has been deleted. The system must clean up resources dedicated to
      the search domain when  DeleteDomain is called. Newly deleted search domains are returned
      from  DescribeDomains with a true value for IsDeleted for several minutes until resource
      cleanup is complete.

    - **DocService** *(dict) --*

      The service endpoint for updating documents in a search domain.

      - **Endpoint** *(string) --*

        The endpoint to which service requests can be submitted. For example,
        ``search-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.cloudsearch.amazonaws.com`` or
        ``doc-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.cloudsearch.amazonaws.com`` .

    - **SearchService** *(dict) --*

      The service endpoint for requesting search results from a search domain.

      - **Endpoint** *(string) --*

        The endpoint to which service requests can be submitted. For example,
        ``search-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.cloudsearch.amazonaws.com`` or
        ``doc-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.cloudsearch.amazonaws.com`` .

    - **RequiresIndexDocuments** *(boolean) --*

      True if  IndexDocuments needs to be called to activate the current domain configuration.

    - **Processing** *(boolean) --*

      True if processing is being done to activate the current domain configuration.

    - **SearchInstanceType** *(string) --*

      The instance type that is being used to process search requests.

    - **SearchPartitionCount** *(integer) --*

      The number of partitions across which the search index is spread.

    - **SearchInstanceCount** *(integer) --*

      The number of search instances that are available to process search requests.

    - **Limits** *(dict) --*

      - **MaximumReplicationCount** *(integer) --*

      - **MaximumPartitionCount** *(integer) --*
    """


_ClientDeleteDomainResponseTypeDef = TypedDict(
    "_ClientDeleteDomainResponseTypeDef",
    {"DomainStatus": ClientDeleteDomainResponseDomainStatusTypeDef},
    total=False,
)


class ClientDeleteDomainResponseTypeDef(_ClientDeleteDomainResponseTypeDef):
    """
    Type definition for `ClientDeleteDomain` `Response`

    The result of a ``DeleteDomain`` request. Contains the status of a newly deleted domain, or no
    status if the domain has already been completely deleted.

    - **DomainStatus** *(dict) --*

      The current status of the search domain.

      - **DomainId** *(string) --*

        An internally generated unique identifier for a domain.

      - **DomainName** *(string) --*

        A string that represents the name of a domain. Domain names are unique across the domains
        owned by an account within an AWS region. Domain names start with a letter or number and
        can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).

      - **ARN** *(string) --*

        The Amazon Resource Name (ARN) of the search domain. See `Identifiers for IAM Entities
        <http://docs.aws.amazon.com/IAM/latest/UserGuide/index.html?Using_Identifiers.html>`__ in
        *Using AWS Identity and Access Management* for more information.

      - **Created** *(boolean) --*

        True if the search domain is created. It can take several minutes to initialize a domain
        when  CreateDomain is called. Newly created search domains are returned from
        DescribeDomains with a false value for Created until domain creation is complete.

      - **Deleted** *(boolean) --*

        True if the search domain has been deleted. The system must clean up resources dedicated to
        the search domain when  DeleteDomain is called. Newly deleted search domains are returned
        from  DescribeDomains with a true value for IsDeleted for several minutes until resource
        cleanup is complete.

      - **DocService** *(dict) --*

        The service endpoint for updating documents in a search domain.

        - **Endpoint** *(string) --*

          The endpoint to which service requests can be submitted. For example,
          ``search-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.cloudsearch.amazonaws.com`` or
          ``doc-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.cloudsearch.amazonaws.com`` .

      - **SearchService** *(dict) --*

        The service endpoint for requesting search results from a search domain.

        - **Endpoint** *(string) --*

          The endpoint to which service requests can be submitted. For example,
          ``search-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.cloudsearch.amazonaws.com`` or
          ``doc-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.cloudsearch.amazonaws.com`` .

      - **RequiresIndexDocuments** *(boolean) --*

        True if  IndexDocuments needs to be called to activate the current domain configuration.

      - **Processing** *(boolean) --*

        True if processing is being done to activate the current domain configuration.

      - **SearchInstanceType** *(string) --*

        The instance type that is being used to process search requests.

      - **SearchPartitionCount** *(integer) --*

        The number of partitions across which the search index is spread.

      - **SearchInstanceCount** *(integer) --*

        The number of search instances that are available to process search requests.

      - **Limits** *(dict) --*

        - **MaximumReplicationCount** *(integer) --*

        - **MaximumPartitionCount** *(integer) --*
    """


_ClientDeleteExpressionResponseExpressionOptionsTypeDef = TypedDict(
    "_ClientDeleteExpressionResponseExpressionOptionsTypeDef",
    {"ExpressionName": str, "ExpressionValue": str},
    total=False,
)


class ClientDeleteExpressionResponseExpressionOptionsTypeDef(
    _ClientDeleteExpressionResponseExpressionOptionsTypeDef
):
    """
    Type definition for `ClientDeleteExpressionResponseExpression` `Options`

    The expression that is evaluated for sorting while processing a search request.

    - **ExpressionName** *(string) --*

      Names must begin with a letter and can contain the following characters: a-z (lowercase),
      0-9, and _ (underscore).

    - **ExpressionValue** *(string) --*

      The expression to evaluate for sorting while processing a search request. The
      ``Expression`` syntax is based on JavaScript expressions. For more information, see
      `Configuring Expressions
      <http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-expressions.html>`__
      in the *Amazon CloudSearch Developer Guide* .
    """


_ClientDeleteExpressionResponseExpressionStatusTypeDef = TypedDict(
    "_ClientDeleteExpressionResponseExpressionStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": str,
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientDeleteExpressionResponseExpressionStatusTypeDef(
    _ClientDeleteExpressionResponseExpressionStatusTypeDef
):
    """
    Type definition for `ClientDeleteExpressionResponseExpression` `Status`

    The status of domain configuration option.

    - **CreationDate** *(datetime) --*

      A timestamp for when this option was created.

    - **UpdateDate** *(datetime) --*

      A timestamp for when this option was last updated.

    - **UpdateVersion** *(integer) --*

      A unique integer that indicates when this option was last updated.

    - **State** *(string) --*

      The state of processing a change to an option. Possible values:

      * ``RequiresIndexDocuments`` : the option's latest value will not be deployed until
      IndexDocuments has been called and indexing is complete.

      * ``Processing`` : the option's latest value is in the process of being activated.

      * ``Active`` : the option's latest value is completely deployed.

      * ``FailedToValidate`` : the option value is not compatible with the domain's data and
      cannot be used to index the data. You must either modify the option value or update or
      remove the incompatible documents.

    - **PendingDeletion** *(boolean) --*

      Indicates that the option will be deleted once processing is complete.
    """


_ClientDeleteExpressionResponseExpressionTypeDef = TypedDict(
    "_ClientDeleteExpressionResponseExpressionTypeDef",
    {
        "Options": ClientDeleteExpressionResponseExpressionOptionsTypeDef,
        "Status": ClientDeleteExpressionResponseExpressionStatusTypeDef,
    },
    total=False,
)


class ClientDeleteExpressionResponseExpressionTypeDef(
    _ClientDeleteExpressionResponseExpressionTypeDef
):
    """
    Type definition for `ClientDeleteExpressionResponse` `Expression`

    The status of the expression being deleted.

    - **Options** *(dict) --*

      The expression that is evaluated for sorting while processing a search request.

      - **ExpressionName** *(string) --*

        Names must begin with a letter and can contain the following characters: a-z (lowercase),
        0-9, and _ (underscore).

      - **ExpressionValue** *(string) --*

        The expression to evaluate for sorting while processing a search request. The
        ``Expression`` syntax is based on JavaScript expressions. For more information, see
        `Configuring Expressions
        <http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-expressions.html>`__
        in the *Amazon CloudSearch Developer Guide* .

    - **Status** *(dict) --*

      The status of domain configuration option.

      - **CreationDate** *(datetime) --*

        A timestamp for when this option was created.

      - **UpdateDate** *(datetime) --*

        A timestamp for when this option was last updated.

      - **UpdateVersion** *(integer) --*

        A unique integer that indicates when this option was last updated.

      - **State** *(string) --*

        The state of processing a change to an option. Possible values:

        * ``RequiresIndexDocuments`` : the option's latest value will not be deployed until
        IndexDocuments has been called and indexing is complete.

        * ``Processing`` : the option's latest value is in the process of being activated.

        * ``Active`` : the option's latest value is completely deployed.

        * ``FailedToValidate`` : the option value is not compatible with the domain's data and
        cannot be used to index the data. You must either modify the option value or update or
        remove the incompatible documents.

      - **PendingDeletion** *(boolean) --*

        Indicates that the option will be deleted once processing is complete.
    """


_ClientDeleteExpressionResponseTypeDef = TypedDict(
    "_ClientDeleteExpressionResponseTypeDef",
    {"Expression": ClientDeleteExpressionResponseExpressionTypeDef},
    total=False,
)


class ClientDeleteExpressionResponseTypeDef(_ClientDeleteExpressionResponseTypeDef):
    """
    Type definition for `ClientDeleteExpression` `Response`

    The result of a `` DeleteExpression`` request. Specifies the expression being deleted.

    - **Expression** *(dict) --*

      The status of the expression being deleted.

      - **Options** *(dict) --*

        The expression that is evaluated for sorting while processing a search request.

        - **ExpressionName** *(string) --*

          Names must begin with a letter and can contain the following characters: a-z (lowercase),
          0-9, and _ (underscore).

        - **ExpressionValue** *(string) --*

          The expression to evaluate for sorting while processing a search request. The
          ``Expression`` syntax is based on JavaScript expressions. For more information, see
          `Configuring Expressions
          <http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-expressions.html>`__
          in the *Amazon CloudSearch Developer Guide* .

      - **Status** *(dict) --*

        The status of domain configuration option.

        - **CreationDate** *(datetime) --*

          A timestamp for when this option was created.

        - **UpdateDate** *(datetime) --*

          A timestamp for when this option was last updated.

        - **UpdateVersion** *(integer) --*

          A unique integer that indicates when this option was last updated.

        - **State** *(string) --*

          The state of processing a change to an option. Possible values:

          * ``RequiresIndexDocuments`` : the option's latest value will not be deployed until
          IndexDocuments has been called and indexing is complete.

          * ``Processing`` : the option's latest value is in the process of being activated.

          * ``Active`` : the option's latest value is completely deployed.

          * ``FailedToValidate`` : the option value is not compatible with the domain's data and
          cannot be used to index the data. You must either modify the option value or update or
          remove the incompatible documents.

        - **PendingDeletion** *(boolean) --*

          Indicates that the option will be deleted once processing is complete.
    """


_ClientDeleteIndexFieldResponseIndexFieldOptionsDateArrayOptionsTypeDef = TypedDict(
    "_ClientDeleteIndexFieldResponseIndexFieldOptionsDateArrayOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceFields": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
    },
    total=False,
)


class ClientDeleteIndexFieldResponseIndexFieldOptionsDateArrayOptionsTypeDef(
    _ClientDeleteIndexFieldResponseIndexFieldOptionsDateArrayOptionsTypeDef
):
    """
    Type definition for `ClientDeleteIndexFieldResponseIndexFieldOptions` `DateArrayOptions`

    Options for a field that contains an array of dates. Present if ``IndexFieldType``
    specifies the field is of type ``date-array`` . All options are enabled by default.

    - **DefaultValue** *(string) --* A value to use for the field if the field isn't
    specified for a document.

    - **SourceFields** *(string) --*

      A list of source fields to map to the field.

    - **FacetEnabled** *(boolean) --*

      Whether facet information can be returned for the field.

    - **SearchEnabled** *(boolean) --*

      Whether the contents of the field are searchable.

    - **ReturnEnabled** *(boolean) --*

      Whether the contents of the field can be returned in the search results.
    """


_ClientDeleteIndexFieldResponseIndexFieldOptionsDateOptionsTypeDef = TypedDict(
    "_ClientDeleteIndexFieldResponseIndexFieldOptionsDateOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)


class ClientDeleteIndexFieldResponseIndexFieldOptionsDateOptionsTypeDef(
    _ClientDeleteIndexFieldResponseIndexFieldOptionsDateOptionsTypeDef
):
    """
    Type definition for `ClientDeleteIndexFieldResponseIndexFieldOptions` `DateOptions`

    Options for a date field. Dates and times are specified in UTC (Coordinated Universal
    Time) according to IETF RFC3339: yyyy-mm-ddT00:00:00Z. Present if ``IndexFieldType``
    specifies the field is of type ``date`` . All options are enabled by default.

    - **DefaultValue** *(string) --* A value to use for the field if the field isn't
    specified for a document.

    - **SourceField** *(string) --*

      A string that represents the name of an index field. CloudSearch supports regular index
      fields as well as dynamic fields. A dynamic field's name defines a pattern that begins
      or ends with a wildcard. Any document fields that don't map to a regular index field
      but do match a dynamic field's pattern are configured with the dynamic field's indexing
      options.

      Regular field names begin with a letter and can contain the following characters: a-z
      (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a
      wildcard (*). The wildcard can also be the only character in a dynamic field name.
      Multiple wildcards, and wildcards embedded within a string are not supported.

      The name ``score`` is reserved and cannot be used as a field name. To reference a
      document's ID, you can use the name ``_id`` .

    - **FacetEnabled** *(boolean) --*

      Whether facet information can be returned for the field.

    - **SearchEnabled** *(boolean) --*

      Whether the contents of the field are searchable.

    - **ReturnEnabled** *(boolean) --*

      Whether the contents of the field can be returned in the search results.

    - **SortEnabled** *(boolean) --*

      Whether the field can be used to sort the search results.
    """


_ClientDeleteIndexFieldResponseIndexFieldOptionsDoubleArrayOptionsTypeDef = TypedDict(
    "_ClientDeleteIndexFieldResponseIndexFieldOptionsDoubleArrayOptionsTypeDef",
    {
        "DefaultValue": float,
        "SourceFields": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
    },
    total=False,
)


class ClientDeleteIndexFieldResponseIndexFieldOptionsDoubleArrayOptionsTypeDef(
    _ClientDeleteIndexFieldResponseIndexFieldOptionsDoubleArrayOptionsTypeDef
):
    """
    Type definition for `ClientDeleteIndexFieldResponseIndexFieldOptions` `DoubleArrayOptions`

    Options for a field that contains an array of double-precision 64-bit floating point
    values. Present if ``IndexFieldType`` specifies the field is of type ``double-array`` .
    All options are enabled by default.

    - **DefaultValue** *(float) --* A value to use for the field if the field isn't specified
    for a document.

    - **SourceFields** *(string) --*

      A list of source fields to map to the field.

    - **FacetEnabled** *(boolean) --*

      Whether facet information can be returned for the field.

    - **SearchEnabled** *(boolean) --*

      Whether the contents of the field are searchable.

    - **ReturnEnabled** *(boolean) --*

      Whether the contents of the field can be returned in the search results.
    """


_ClientDeleteIndexFieldResponseIndexFieldOptionsDoubleOptionsTypeDef = TypedDict(
    "_ClientDeleteIndexFieldResponseIndexFieldOptionsDoubleOptionsTypeDef",
    {
        "DefaultValue": float,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)


class ClientDeleteIndexFieldResponseIndexFieldOptionsDoubleOptionsTypeDef(
    _ClientDeleteIndexFieldResponseIndexFieldOptionsDoubleOptionsTypeDef
):
    """
    Type definition for `ClientDeleteIndexFieldResponseIndexFieldOptions` `DoubleOptions`

    Options for a double-precision 64-bit floating point field. Present if ``IndexFieldType``
    specifies the field is of type ``double`` . All options are enabled by default.

    - **DefaultValue** *(float) --*

      A value to use for the field if the field isn't specified for a document. This can be
      important if you are using the field in an expression and that field is not present in
      every document.

    - **SourceField** *(string) --*

      The name of the source field to map to the field.

    - **FacetEnabled** *(boolean) --*

      Whether facet information can be returned for the field.

    - **SearchEnabled** *(boolean) --*

      Whether the contents of the field are searchable.

    - **ReturnEnabled** *(boolean) --*

      Whether the contents of the field can be returned in the search results.

    - **SortEnabled** *(boolean) --*

      Whether the field can be used to sort the search results.
    """


_ClientDeleteIndexFieldResponseIndexFieldOptionsIntArrayOptionsTypeDef = TypedDict(
    "_ClientDeleteIndexFieldResponseIndexFieldOptionsIntArrayOptionsTypeDef",
    {
        "DefaultValue": int,
        "SourceFields": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
    },
    total=False,
)


class ClientDeleteIndexFieldResponseIndexFieldOptionsIntArrayOptionsTypeDef(
    _ClientDeleteIndexFieldResponseIndexFieldOptionsIntArrayOptionsTypeDef
):
    """
    Type definition for `ClientDeleteIndexFieldResponseIndexFieldOptions` `IntArrayOptions`

    Options for a field that contains an array of 64-bit signed integers. Present if
    ``IndexFieldType`` specifies the field is of type ``int-array`` . All options are enabled
    by default.

    - **DefaultValue** *(integer) --* A value to use for the field if the field isn't
    specified for a document.

    - **SourceFields** *(string) --*

      A list of source fields to map to the field.

    - **FacetEnabled** *(boolean) --*

      Whether facet information can be returned for the field.

    - **SearchEnabled** *(boolean) --*

      Whether the contents of the field are searchable.

    - **ReturnEnabled** *(boolean) --*

      Whether the contents of the field can be returned in the search results.
    """


_ClientDeleteIndexFieldResponseIndexFieldOptionsIntOptionsTypeDef = TypedDict(
    "_ClientDeleteIndexFieldResponseIndexFieldOptionsIntOptionsTypeDef",
    {
        "DefaultValue": int,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)


class ClientDeleteIndexFieldResponseIndexFieldOptionsIntOptionsTypeDef(
    _ClientDeleteIndexFieldResponseIndexFieldOptionsIntOptionsTypeDef
):
    """
    Type definition for `ClientDeleteIndexFieldResponseIndexFieldOptions` `IntOptions`

    Options for a 64-bit signed integer field. Present if ``IndexFieldType`` specifies the
    field is of type ``int`` . All options are enabled by default.

    - **DefaultValue** *(integer) --* A value to use for the field if the field isn't
    specified for a document. This can be important if you are using the field in an
    expression and that field is not present in every document.

    - **SourceField** *(string) --*

      The name of the source field to map to the field.

    - **FacetEnabled** *(boolean) --*

      Whether facet information can be returned for the field.

    - **SearchEnabled** *(boolean) --*

      Whether the contents of the field are searchable.

    - **ReturnEnabled** *(boolean) --*

      Whether the contents of the field can be returned in the search results.

    - **SortEnabled** *(boolean) --*

      Whether the field can be used to sort the search results.
    """


_ClientDeleteIndexFieldResponseIndexFieldOptionsLatLonOptionsTypeDef = TypedDict(
    "_ClientDeleteIndexFieldResponseIndexFieldOptionsLatLonOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)


class ClientDeleteIndexFieldResponseIndexFieldOptionsLatLonOptionsTypeDef(
    _ClientDeleteIndexFieldResponseIndexFieldOptionsLatLonOptionsTypeDef
):
    """
    Type definition for `ClientDeleteIndexFieldResponseIndexFieldOptions` `LatLonOptions`

    Options for a latlon field. A latlon field contains a location stored as a latitude and
    longitude value pair. Present if ``IndexFieldType`` specifies the field is of type
    ``latlon`` . All options are enabled by default.

    - **DefaultValue** *(string) --* A value to use for the field if the field isn't
    specified for a document.

    - **SourceField** *(string) --*

      A string that represents the name of an index field. CloudSearch supports regular index
      fields as well as dynamic fields. A dynamic field's name defines a pattern that begins
      or ends with a wildcard. Any document fields that don't map to a regular index field
      but do match a dynamic field's pattern are configured with the dynamic field's indexing
      options.

      Regular field names begin with a letter and can contain the following characters: a-z
      (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a
      wildcard (*). The wildcard can also be the only character in a dynamic field name.
      Multiple wildcards, and wildcards embedded within a string are not supported.

      The name ``score`` is reserved and cannot be used as a field name. To reference a
      document's ID, you can use the name ``_id`` .

    - **FacetEnabled** *(boolean) --*

      Whether facet information can be returned for the field.

    - **SearchEnabled** *(boolean) --*

      Whether the contents of the field are searchable.

    - **ReturnEnabled** *(boolean) --*

      Whether the contents of the field can be returned in the search results.

    - **SortEnabled** *(boolean) --*

      Whether the field can be used to sort the search results.
    """


_ClientDeleteIndexFieldResponseIndexFieldOptionsLiteralArrayOptionsTypeDef = TypedDict(
    "_ClientDeleteIndexFieldResponseIndexFieldOptionsLiteralArrayOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceFields": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
    },
    total=False,
)


class ClientDeleteIndexFieldResponseIndexFieldOptionsLiteralArrayOptionsTypeDef(
    _ClientDeleteIndexFieldResponseIndexFieldOptionsLiteralArrayOptionsTypeDef
):
    """
    Type definition for `ClientDeleteIndexFieldResponseIndexFieldOptions` `LiteralArrayOptions`

    Options for a field that contains an array of literal strings. Present if
    ``IndexFieldType`` specifies the field is of type ``literal-array`` . All options are
    enabled by default.

    - **DefaultValue** *(string) --* A value to use for the field if the field isn't
    specified for a document.

    - **SourceFields** *(string) --*

      A list of source fields to map to the field.

    - **FacetEnabled** *(boolean) --*

      Whether facet information can be returned for the field.

    - **SearchEnabled** *(boolean) --*

      Whether the contents of the field are searchable.

    - **ReturnEnabled** *(boolean) --*

      Whether the contents of the field can be returned in the search results.
    """


_ClientDeleteIndexFieldResponseIndexFieldOptionsLiteralOptionsTypeDef = TypedDict(
    "_ClientDeleteIndexFieldResponseIndexFieldOptionsLiteralOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)


class ClientDeleteIndexFieldResponseIndexFieldOptionsLiteralOptionsTypeDef(
    _ClientDeleteIndexFieldResponseIndexFieldOptionsLiteralOptionsTypeDef
):
    """
    Type definition for `ClientDeleteIndexFieldResponseIndexFieldOptions` `LiteralOptions`

    Options for literal field. Present if ``IndexFieldType`` specifies the field is of type
    ``literal`` . All options are enabled by default.

    - **DefaultValue** *(string) --* A value to use for the field if the field isn't
    specified for a document.

    - **SourceField** *(string) --*

      A string that represents the name of an index field. CloudSearch supports regular index
      fields as well as dynamic fields. A dynamic field's name defines a pattern that begins
      or ends with a wildcard. Any document fields that don't map to a regular index field
      but do match a dynamic field's pattern are configured with the dynamic field's indexing
      options.

      Regular field names begin with a letter and can contain the following characters: a-z
      (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a
      wildcard (*). The wildcard can also be the only character in a dynamic field name.
      Multiple wildcards, and wildcards embedded within a string are not supported.

      The name ``score`` is reserved and cannot be used as a field name. To reference a
      document's ID, you can use the name ``_id`` .

    - **FacetEnabled** *(boolean) --*

      Whether facet information can be returned for the field.

    - **SearchEnabled** *(boolean) --*

      Whether the contents of the field are searchable.

    - **ReturnEnabled** *(boolean) --*

      Whether the contents of the field can be returned in the search results.

    - **SortEnabled** *(boolean) --*

      Whether the field can be used to sort the search results.
    """


_ClientDeleteIndexFieldResponseIndexFieldOptionsTextArrayOptionsTypeDef = TypedDict(
    "_ClientDeleteIndexFieldResponseIndexFieldOptionsTextArrayOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceFields": str,
        "ReturnEnabled": bool,
        "HighlightEnabled": bool,
        "AnalysisScheme": str,
    },
    total=False,
)


class ClientDeleteIndexFieldResponseIndexFieldOptionsTextArrayOptionsTypeDef(
    _ClientDeleteIndexFieldResponseIndexFieldOptionsTextArrayOptionsTypeDef
):
    """
    Type definition for `ClientDeleteIndexFieldResponseIndexFieldOptions` `TextArrayOptions`

    Options for a field that contains an array of text strings. Present if ``IndexFieldType``
    specifies the field is of type ``text-array`` . A ``text-array`` field is always
    searchable. All options are enabled by default.

    - **DefaultValue** *(string) --* A value to use for the field if the field isn't
    specified for a document.

    - **SourceFields** *(string) --*

      A list of source fields to map to the field.

    - **ReturnEnabled** *(boolean) --*

      Whether the contents of the field can be returned in the search results.

    - **HighlightEnabled** *(boolean) --*

      Whether highlights can be returned for the field.

    - **AnalysisScheme** *(string) --*

      The name of an analysis scheme for a ``text-array`` field.
    """


_ClientDeleteIndexFieldResponseIndexFieldOptionsTextOptionsTypeDef = TypedDict(
    "_ClientDeleteIndexFieldResponseIndexFieldOptionsTextOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceField": str,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
        "HighlightEnabled": bool,
        "AnalysisScheme": str,
    },
    total=False,
)


class ClientDeleteIndexFieldResponseIndexFieldOptionsTextOptionsTypeDef(
    _ClientDeleteIndexFieldResponseIndexFieldOptionsTextOptionsTypeDef
):
    """
    Type definition for `ClientDeleteIndexFieldResponseIndexFieldOptions` `TextOptions`

    Options for text field. Present if ``IndexFieldType`` specifies the field is of type
    ``text`` . A ``text`` field is always searchable. All options are enabled by default.

    - **DefaultValue** *(string) --* A value to use for the field if the field isn't
    specified for a document.

    - **SourceField** *(string) --*

      A string that represents the name of an index field. CloudSearch supports regular index
      fields as well as dynamic fields. A dynamic field's name defines a pattern that begins
      or ends with a wildcard. Any document fields that don't map to a regular index field
      but do match a dynamic field's pattern are configured with the dynamic field's indexing
      options.

      Regular field names begin with a letter and can contain the following characters: a-z
      (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a
      wildcard (*). The wildcard can also be the only character in a dynamic field name.
      Multiple wildcards, and wildcards embedded within a string are not supported.

      The name ``score`` is reserved and cannot be used as a field name. To reference a
      document's ID, you can use the name ``_id`` .

    - **ReturnEnabled** *(boolean) --*

      Whether the contents of the field can be returned in the search results.

    - **SortEnabled** *(boolean) --*

      Whether the field can be used to sort the search results.

    - **HighlightEnabled** *(boolean) --*

      Whether highlights can be returned for the field.

    - **AnalysisScheme** *(string) --*

      The name of an analysis scheme for a ``text`` field.
    """


_ClientDeleteIndexFieldResponseIndexFieldOptionsTypeDef = TypedDict(
    "_ClientDeleteIndexFieldResponseIndexFieldOptionsTypeDef",
    {
        "IndexFieldName": str,
        "IndexFieldType": str,
        "IntOptions": ClientDeleteIndexFieldResponseIndexFieldOptionsIntOptionsTypeDef,
        "DoubleOptions": ClientDeleteIndexFieldResponseIndexFieldOptionsDoubleOptionsTypeDef,
        "LiteralOptions": ClientDeleteIndexFieldResponseIndexFieldOptionsLiteralOptionsTypeDef,
        "TextOptions": ClientDeleteIndexFieldResponseIndexFieldOptionsTextOptionsTypeDef,
        "DateOptions": ClientDeleteIndexFieldResponseIndexFieldOptionsDateOptionsTypeDef,
        "LatLonOptions": ClientDeleteIndexFieldResponseIndexFieldOptionsLatLonOptionsTypeDef,
        "IntArrayOptions": ClientDeleteIndexFieldResponseIndexFieldOptionsIntArrayOptionsTypeDef,
        "DoubleArrayOptions": ClientDeleteIndexFieldResponseIndexFieldOptionsDoubleArrayOptionsTypeDef,
        "LiteralArrayOptions": ClientDeleteIndexFieldResponseIndexFieldOptionsLiteralArrayOptionsTypeDef,
        "TextArrayOptions": ClientDeleteIndexFieldResponseIndexFieldOptionsTextArrayOptionsTypeDef,
        "DateArrayOptions": ClientDeleteIndexFieldResponseIndexFieldOptionsDateArrayOptionsTypeDef,
    },
    total=False,
)


class ClientDeleteIndexFieldResponseIndexFieldOptionsTypeDef(
    _ClientDeleteIndexFieldResponseIndexFieldOptionsTypeDef
):
    """
    Type definition for `ClientDeleteIndexFieldResponseIndexField` `Options`

    Configuration information for a field in the index, including its name, type, and options.
    The supported options depend on the `` IndexFieldType`` .

    - **IndexFieldName** *(string) --*

      A string that represents the name of an index field. CloudSearch supports regular index
      fields as well as dynamic fields. A dynamic field's name defines a pattern that begins or
      ends with a wildcard. Any document fields that don't map to a regular index field but do
      match a dynamic field's pattern are configured with the dynamic field's indexing options.

      Regular field names begin with a letter and can contain the following characters: a-z
      (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a
      wildcard (*). The wildcard can also be the only character in a dynamic field name.
      Multiple wildcards, and wildcards embedded within a string are not supported.

      The name ``score`` is reserved and cannot be used as a field name. To reference a
      document's ID, you can use the name ``_id`` .

    - **IndexFieldType** *(string) --*

      The type of field. The valid options for a field depend on the field type. For more
      information about the supported field types, see `Configuring Index Fields
      <http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-index-fields.html>`__
      in the *Amazon CloudSearch Developer Guide* .

    - **IntOptions** *(dict) --*

      Options for a 64-bit signed integer field. Present if ``IndexFieldType`` specifies the
      field is of type ``int`` . All options are enabled by default.

      - **DefaultValue** *(integer) --* A value to use for the field if the field isn't
      specified for a document. This can be important if you are using the field in an
      expression and that field is not present in every document.

      - **SourceField** *(string) --*

        The name of the source field to map to the field.

      - **FacetEnabled** *(boolean) --*

        Whether facet information can be returned for the field.

      - **SearchEnabled** *(boolean) --*

        Whether the contents of the field are searchable.

      - **ReturnEnabled** *(boolean) --*

        Whether the contents of the field can be returned in the search results.

      - **SortEnabled** *(boolean) --*

        Whether the field can be used to sort the search results.

    - **DoubleOptions** *(dict) --*

      Options for a double-precision 64-bit floating point field. Present if ``IndexFieldType``
      specifies the field is of type ``double`` . All options are enabled by default.

      - **DefaultValue** *(float) --*

        A value to use for the field if the field isn't specified for a document. This can be
        important if you are using the field in an expression and that field is not present in
        every document.

      - **SourceField** *(string) --*

        The name of the source field to map to the field.

      - **FacetEnabled** *(boolean) --*

        Whether facet information can be returned for the field.

      - **SearchEnabled** *(boolean) --*

        Whether the contents of the field are searchable.

      - **ReturnEnabled** *(boolean) --*

        Whether the contents of the field can be returned in the search results.

      - **SortEnabled** *(boolean) --*

        Whether the field can be used to sort the search results.

    - **LiteralOptions** *(dict) --*

      Options for literal field. Present if ``IndexFieldType`` specifies the field is of type
      ``literal`` . All options are enabled by default.

      - **DefaultValue** *(string) --* A value to use for the field if the field isn't
      specified for a document.

      - **SourceField** *(string) --*

        A string that represents the name of an index field. CloudSearch supports regular index
        fields as well as dynamic fields. A dynamic field's name defines a pattern that begins
        or ends with a wildcard. Any document fields that don't map to a regular index field
        but do match a dynamic field's pattern are configured with the dynamic field's indexing
        options.

        Regular field names begin with a letter and can contain the following characters: a-z
        (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a
        wildcard (*). The wildcard can also be the only character in a dynamic field name.
        Multiple wildcards, and wildcards embedded within a string are not supported.

        The name ``score`` is reserved and cannot be used as a field name. To reference a
        document's ID, you can use the name ``_id`` .

      - **FacetEnabled** *(boolean) --*

        Whether facet information can be returned for the field.

      - **SearchEnabled** *(boolean) --*

        Whether the contents of the field are searchable.

      - **ReturnEnabled** *(boolean) --*

        Whether the contents of the field can be returned in the search results.

      - **SortEnabled** *(boolean) --*

        Whether the field can be used to sort the search results.

    - **TextOptions** *(dict) --*

      Options for text field. Present if ``IndexFieldType`` specifies the field is of type
      ``text`` . A ``text`` field is always searchable. All options are enabled by default.

      - **DefaultValue** *(string) --* A value to use for the field if the field isn't
      specified for a document.

      - **SourceField** *(string) --*

        A string that represents the name of an index field. CloudSearch supports regular index
        fields as well as dynamic fields. A dynamic field's name defines a pattern that begins
        or ends with a wildcard. Any document fields that don't map to a regular index field
        but do match a dynamic field's pattern are configured with the dynamic field's indexing
        options.

        Regular field names begin with a letter and can contain the following characters: a-z
        (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a
        wildcard (*). The wildcard can also be the only character in a dynamic field name.
        Multiple wildcards, and wildcards embedded within a string are not supported.

        The name ``score`` is reserved and cannot be used as a field name. To reference a
        document's ID, you can use the name ``_id`` .

      - **ReturnEnabled** *(boolean) --*

        Whether the contents of the field can be returned in the search results.

      - **SortEnabled** *(boolean) --*

        Whether the field can be used to sort the search results.

      - **HighlightEnabled** *(boolean) --*

        Whether highlights can be returned for the field.

      - **AnalysisScheme** *(string) --*

        The name of an analysis scheme for a ``text`` field.

    - **DateOptions** *(dict) --*

      Options for a date field. Dates and times are specified in UTC (Coordinated Universal
      Time) according to IETF RFC3339: yyyy-mm-ddT00:00:00Z. Present if ``IndexFieldType``
      specifies the field is of type ``date`` . All options are enabled by default.

      - **DefaultValue** *(string) --* A value to use for the field if the field isn't
      specified for a document.

      - **SourceField** *(string) --*

        A string that represents the name of an index field. CloudSearch supports regular index
        fields as well as dynamic fields. A dynamic field's name defines a pattern that begins
        or ends with a wildcard. Any document fields that don't map to a regular index field
        but do match a dynamic field's pattern are configured with the dynamic field's indexing
        options.

        Regular field names begin with a letter and can contain the following characters: a-z
        (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a
        wildcard (*). The wildcard can also be the only character in a dynamic field name.
        Multiple wildcards, and wildcards embedded within a string are not supported.

        The name ``score`` is reserved and cannot be used as a field name. To reference a
        document's ID, you can use the name ``_id`` .

      - **FacetEnabled** *(boolean) --*

        Whether facet information can be returned for the field.

      - **SearchEnabled** *(boolean) --*

        Whether the contents of the field are searchable.

      - **ReturnEnabled** *(boolean) --*

        Whether the contents of the field can be returned in the search results.

      - **SortEnabled** *(boolean) --*

        Whether the field can be used to sort the search results.

    - **LatLonOptions** *(dict) --*

      Options for a latlon field. A latlon field contains a location stored as a latitude and
      longitude value pair. Present if ``IndexFieldType`` specifies the field is of type
      ``latlon`` . All options are enabled by default.

      - **DefaultValue** *(string) --* A value to use for the field if the field isn't
      specified for a document.

      - **SourceField** *(string) --*

        A string that represents the name of an index field. CloudSearch supports regular index
        fields as well as dynamic fields. A dynamic field's name defines a pattern that begins
        or ends with a wildcard. Any document fields that don't map to a regular index field
        but do match a dynamic field's pattern are configured with the dynamic field's indexing
        options.

        Regular field names begin with a letter and can contain the following characters: a-z
        (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a
        wildcard (*). The wildcard can also be the only character in a dynamic field name.
        Multiple wildcards, and wildcards embedded within a string are not supported.

        The name ``score`` is reserved and cannot be used as a field name. To reference a
        document's ID, you can use the name ``_id`` .

      - **FacetEnabled** *(boolean) --*

        Whether facet information can be returned for the field.

      - **SearchEnabled** *(boolean) --*

        Whether the contents of the field are searchable.

      - **ReturnEnabled** *(boolean) --*

        Whether the contents of the field can be returned in the search results.

      - **SortEnabled** *(boolean) --*

        Whether the field can be used to sort the search results.

    - **IntArrayOptions** *(dict) --*

      Options for a field that contains an array of 64-bit signed integers. Present if
      ``IndexFieldType`` specifies the field is of type ``int-array`` . All options are enabled
      by default.

      - **DefaultValue** *(integer) --* A value to use for the field if the field isn't
      specified for a document.

      - **SourceFields** *(string) --*

        A list of source fields to map to the field.

      - **FacetEnabled** *(boolean) --*

        Whether facet information can be returned for the field.

      - **SearchEnabled** *(boolean) --*

        Whether the contents of the field are searchable.

      - **ReturnEnabled** *(boolean) --*

        Whether the contents of the field can be returned in the search results.

    - **DoubleArrayOptions** *(dict) --*

      Options for a field that contains an array of double-precision 64-bit floating point
      values. Present if ``IndexFieldType`` specifies the field is of type ``double-array`` .
      All options are enabled by default.

      - **DefaultValue** *(float) --* A value to use for the field if the field isn't specified
      for a document.

      - **SourceFields** *(string) --*

        A list of source fields to map to the field.

      - **FacetEnabled** *(boolean) --*

        Whether facet information can be returned for the field.

      - **SearchEnabled** *(boolean) --*

        Whether the contents of the field are searchable.

      - **ReturnEnabled** *(boolean) --*

        Whether the contents of the field can be returned in the search results.

    - **LiteralArrayOptions** *(dict) --*

      Options for a field that contains an array of literal strings. Present if
      ``IndexFieldType`` specifies the field is of type ``literal-array`` . All options are
      enabled by default.

      - **DefaultValue** *(string) --* A value to use for the field if the field isn't
      specified for a document.

      - **SourceFields** *(string) --*

        A list of source fields to map to the field.

      - **FacetEnabled** *(boolean) --*

        Whether facet information can be returned for the field.

      - **SearchEnabled** *(boolean) --*

        Whether the contents of the field are searchable.

      - **ReturnEnabled** *(boolean) --*

        Whether the contents of the field can be returned in the search results.

    - **TextArrayOptions** *(dict) --*

      Options for a field that contains an array of text strings. Present if ``IndexFieldType``
      specifies the field is of type ``text-array`` . A ``text-array`` field is always
      searchable. All options are enabled by default.

      - **DefaultValue** *(string) --* A value to use for the field if the field isn't
      specified for a document.

      - **SourceFields** *(string) --*

        A list of source fields to map to the field.

      - **ReturnEnabled** *(boolean) --*

        Whether the contents of the field can be returned in the search results.

      - **HighlightEnabled** *(boolean) --*

        Whether highlights can be returned for the field.

      - **AnalysisScheme** *(string) --*

        The name of an analysis scheme for a ``text-array`` field.

    - **DateArrayOptions** *(dict) --*

      Options for a field that contains an array of dates. Present if ``IndexFieldType``
      specifies the field is of type ``date-array`` . All options are enabled by default.

      - **DefaultValue** *(string) --* A value to use for the field if the field isn't
      specified for a document.

      - **SourceFields** *(string) --*

        A list of source fields to map to the field.

      - **FacetEnabled** *(boolean) --*

        Whether facet information can be returned for the field.

      - **SearchEnabled** *(boolean) --*

        Whether the contents of the field are searchable.

      - **ReturnEnabled** *(boolean) --*

        Whether the contents of the field can be returned in the search results.
    """


_ClientDeleteIndexFieldResponseIndexFieldStatusTypeDef = TypedDict(
    "_ClientDeleteIndexFieldResponseIndexFieldStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": str,
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientDeleteIndexFieldResponseIndexFieldStatusTypeDef(
    _ClientDeleteIndexFieldResponseIndexFieldStatusTypeDef
):
    """
    Type definition for `ClientDeleteIndexFieldResponseIndexField` `Status`

    The status of domain configuration option.

    - **CreationDate** *(datetime) --*

      A timestamp for when this option was created.

    - **UpdateDate** *(datetime) --*

      A timestamp for when this option was last updated.

    - **UpdateVersion** *(integer) --*

      A unique integer that indicates when this option was last updated.

    - **State** *(string) --*

      The state of processing a change to an option. Possible values:

      * ``RequiresIndexDocuments`` : the option's latest value will not be deployed until
      IndexDocuments has been called and indexing is complete.

      * ``Processing`` : the option's latest value is in the process of being activated.

      * ``Active`` : the option's latest value is completely deployed.

      * ``FailedToValidate`` : the option value is not compatible with the domain's data and
      cannot be used to index the data. You must either modify the option value or update or
      remove the incompatible documents.

    - **PendingDeletion** *(boolean) --*

      Indicates that the option will be deleted once processing is complete.
    """


_ClientDeleteIndexFieldResponseIndexFieldTypeDef = TypedDict(
    "_ClientDeleteIndexFieldResponseIndexFieldTypeDef",
    {
        "Options": ClientDeleteIndexFieldResponseIndexFieldOptionsTypeDef,
        "Status": ClientDeleteIndexFieldResponseIndexFieldStatusTypeDef,
    },
    total=False,
)


class ClientDeleteIndexFieldResponseIndexFieldTypeDef(
    _ClientDeleteIndexFieldResponseIndexFieldTypeDef
):
    """
    Type definition for `ClientDeleteIndexFieldResponse` `IndexField`

    The status of the index field being deleted.

    - **Options** *(dict) --*

      Configuration information for a field in the index, including its name, type, and options.
      The supported options depend on the `` IndexFieldType`` .

      - **IndexFieldName** *(string) --*

        A string that represents the name of an index field. CloudSearch supports regular index
        fields as well as dynamic fields. A dynamic field's name defines a pattern that begins or
        ends with a wildcard. Any document fields that don't map to a regular index field but do
        match a dynamic field's pattern are configured with the dynamic field's indexing options.

        Regular field names begin with a letter and can contain the following characters: a-z
        (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a
        wildcard (*). The wildcard can also be the only character in a dynamic field name.
        Multiple wildcards, and wildcards embedded within a string are not supported.

        The name ``score`` is reserved and cannot be used as a field name. To reference a
        document's ID, you can use the name ``_id`` .

      - **IndexFieldType** *(string) --*

        The type of field. The valid options for a field depend on the field type. For more
        information about the supported field types, see `Configuring Index Fields
        <http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-index-fields.html>`__
        in the *Amazon CloudSearch Developer Guide* .

      - **IntOptions** *(dict) --*

        Options for a 64-bit signed integer field. Present if ``IndexFieldType`` specifies the
        field is of type ``int`` . All options are enabled by default.

        - **DefaultValue** *(integer) --* A value to use for the field if the field isn't
        specified for a document. This can be important if you are using the field in an
        expression and that field is not present in every document.

        - **SourceField** *(string) --*

          The name of the source field to map to the field.

        - **FacetEnabled** *(boolean) --*

          Whether facet information can be returned for the field.

        - **SearchEnabled** *(boolean) --*

          Whether the contents of the field are searchable.

        - **ReturnEnabled** *(boolean) --*

          Whether the contents of the field can be returned in the search results.

        - **SortEnabled** *(boolean) --*

          Whether the field can be used to sort the search results.

      - **DoubleOptions** *(dict) --*

        Options for a double-precision 64-bit floating point field. Present if ``IndexFieldType``
        specifies the field is of type ``double`` . All options are enabled by default.

        - **DefaultValue** *(float) --*

          A value to use for the field if the field isn't specified for a document. This can be
          important if you are using the field in an expression and that field is not present in
          every document.

        - **SourceField** *(string) --*

          The name of the source field to map to the field.

        - **FacetEnabled** *(boolean) --*

          Whether facet information can be returned for the field.

        - **SearchEnabled** *(boolean) --*

          Whether the contents of the field are searchable.

        - **ReturnEnabled** *(boolean) --*

          Whether the contents of the field can be returned in the search results.

        - **SortEnabled** *(boolean) --*

          Whether the field can be used to sort the search results.

      - **LiteralOptions** *(dict) --*

        Options for literal field. Present if ``IndexFieldType`` specifies the field is of type
        ``literal`` . All options are enabled by default.

        - **DefaultValue** *(string) --* A value to use for the field if the field isn't
        specified for a document.

        - **SourceField** *(string) --*

          A string that represents the name of an index field. CloudSearch supports regular index
          fields as well as dynamic fields. A dynamic field's name defines a pattern that begins
          or ends with a wildcard. Any document fields that don't map to a regular index field
          but do match a dynamic field's pattern are configured with the dynamic field's indexing
          options.

          Regular field names begin with a letter and can contain the following characters: a-z
          (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a
          wildcard (*). The wildcard can also be the only character in a dynamic field name.
          Multiple wildcards, and wildcards embedded within a string are not supported.

          The name ``score`` is reserved and cannot be used as a field name. To reference a
          document's ID, you can use the name ``_id`` .

        - **FacetEnabled** *(boolean) --*

          Whether facet information can be returned for the field.

        - **SearchEnabled** *(boolean) --*

          Whether the contents of the field are searchable.

        - **ReturnEnabled** *(boolean) --*

          Whether the contents of the field can be returned in the search results.

        - **SortEnabled** *(boolean) --*

          Whether the field can be used to sort the search results.

      - **TextOptions** *(dict) --*

        Options for text field. Present if ``IndexFieldType`` specifies the field is of type
        ``text`` . A ``text`` field is always searchable. All options are enabled by default.

        - **DefaultValue** *(string) --* A value to use for the field if the field isn't
        specified for a document.

        - **SourceField** *(string) --*

          A string that represents the name of an index field. CloudSearch supports regular index
          fields as well as dynamic fields. A dynamic field's name defines a pattern that begins
          or ends with a wildcard. Any document fields that don't map to a regular index field
          but do match a dynamic field's pattern are configured with the dynamic field's indexing
          options.

          Regular field names begin with a letter and can contain the following characters: a-z
          (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a
          wildcard (*). The wildcard can also be the only character in a dynamic field name.
          Multiple wildcards, and wildcards embedded within a string are not supported.

          The name ``score`` is reserved and cannot be used as a field name. To reference a
          document's ID, you can use the name ``_id`` .

        - **ReturnEnabled** *(boolean) --*

          Whether the contents of the field can be returned in the search results.

        - **SortEnabled** *(boolean) --*

          Whether the field can be used to sort the search results.

        - **HighlightEnabled** *(boolean) --*

          Whether highlights can be returned for the field.

        - **AnalysisScheme** *(string) --*

          The name of an analysis scheme for a ``text`` field.

      - **DateOptions** *(dict) --*

        Options for a date field. Dates and times are specified in UTC (Coordinated Universal
        Time) according to IETF RFC3339: yyyy-mm-ddT00:00:00Z. Present if ``IndexFieldType``
        specifies the field is of type ``date`` . All options are enabled by default.

        - **DefaultValue** *(string) --* A value to use for the field if the field isn't
        specified for a document.

        - **SourceField** *(string) --*

          A string that represents the name of an index field. CloudSearch supports regular index
          fields as well as dynamic fields. A dynamic field's name defines a pattern that begins
          or ends with a wildcard. Any document fields that don't map to a regular index field
          but do match a dynamic field's pattern are configured with the dynamic field's indexing
          options.

          Regular field names begin with a letter and can contain the following characters: a-z
          (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a
          wildcard (*). The wildcard can also be the only character in a dynamic field name.
          Multiple wildcards, and wildcards embedded within a string are not supported.

          The name ``score`` is reserved and cannot be used as a field name. To reference a
          document's ID, you can use the name ``_id`` .

        - **FacetEnabled** *(boolean) --*

          Whether facet information can be returned for the field.

        - **SearchEnabled** *(boolean) --*

          Whether the contents of the field are searchable.

        - **ReturnEnabled** *(boolean) --*

          Whether the contents of the field can be returned in the search results.

        - **SortEnabled** *(boolean) --*

          Whether the field can be used to sort the search results.

      - **LatLonOptions** *(dict) --*

        Options for a latlon field. A latlon field contains a location stored as a latitude and
        longitude value pair. Present if ``IndexFieldType`` specifies the field is of type
        ``latlon`` . All options are enabled by default.

        - **DefaultValue** *(string) --* A value to use for the field if the field isn't
        specified for a document.

        - **SourceField** *(string) --*

          A string that represents the name of an index field. CloudSearch supports regular index
          fields as well as dynamic fields. A dynamic field's name defines a pattern that begins
          or ends with a wildcard. Any document fields that don't map to a regular index field
          but do match a dynamic field's pattern are configured with the dynamic field's indexing
          options.

          Regular field names begin with a letter and can contain the following characters: a-z
          (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a
          wildcard (*). The wildcard can also be the only character in a dynamic field name.
          Multiple wildcards, and wildcards embedded within a string are not supported.

          The name ``score`` is reserved and cannot be used as a field name. To reference a
          document's ID, you can use the name ``_id`` .

        - **FacetEnabled** *(boolean) --*

          Whether facet information can be returned for the field.

        - **SearchEnabled** *(boolean) --*

          Whether the contents of the field are searchable.

        - **ReturnEnabled** *(boolean) --*

          Whether the contents of the field can be returned in the search results.

        - **SortEnabled** *(boolean) --*

          Whether the field can be used to sort the search results.

      - **IntArrayOptions** *(dict) --*

        Options for a field that contains an array of 64-bit signed integers. Present if
        ``IndexFieldType`` specifies the field is of type ``int-array`` . All options are enabled
        by default.

        - **DefaultValue** *(integer) --* A value to use for the field if the field isn't
        specified for a document.

        - **SourceFields** *(string) --*

          A list of source fields to map to the field.

        - **FacetEnabled** *(boolean) --*

          Whether facet information can be returned for the field.

        - **SearchEnabled** *(boolean) --*

          Whether the contents of the field are searchable.

        - **ReturnEnabled** *(boolean) --*

          Whether the contents of the field can be returned in the search results.

      - **DoubleArrayOptions** *(dict) --*

        Options for a field that contains an array of double-precision 64-bit floating point
        values. Present if ``IndexFieldType`` specifies the field is of type ``double-array`` .
        All options are enabled by default.

        - **DefaultValue** *(float) --* A value to use for the field if the field isn't specified
        for a document.

        - **SourceFields** *(string) --*

          A list of source fields to map to the field.

        - **FacetEnabled** *(boolean) --*

          Whether facet information can be returned for the field.

        - **SearchEnabled** *(boolean) --*

          Whether the contents of the field are searchable.

        - **ReturnEnabled** *(boolean) --*

          Whether the contents of the field can be returned in the search results.

      - **LiteralArrayOptions** *(dict) --*

        Options for a field that contains an array of literal strings. Present if
        ``IndexFieldType`` specifies the field is of type ``literal-array`` . All options are
        enabled by default.

        - **DefaultValue** *(string) --* A value to use for the field if the field isn't
        specified for a document.

        - **SourceFields** *(string) --*

          A list of source fields to map to the field.

        - **FacetEnabled** *(boolean) --*

          Whether facet information can be returned for the field.

        - **SearchEnabled** *(boolean) --*

          Whether the contents of the field are searchable.

        - **ReturnEnabled** *(boolean) --*

          Whether the contents of the field can be returned in the search results.

      - **TextArrayOptions** *(dict) --*

        Options for a field that contains an array of text strings. Present if ``IndexFieldType``
        specifies the field is of type ``text-array`` . A ``text-array`` field is always
        searchable. All options are enabled by default.

        - **DefaultValue** *(string) --* A value to use for the field if the field isn't
        specified for a document.

        - **SourceFields** *(string) --*

          A list of source fields to map to the field.

        - **ReturnEnabled** *(boolean) --*

          Whether the contents of the field can be returned in the search results.

        - **HighlightEnabled** *(boolean) --*

          Whether highlights can be returned for the field.

        - **AnalysisScheme** *(string) --*

          The name of an analysis scheme for a ``text-array`` field.

      - **DateArrayOptions** *(dict) --*

        Options for a field that contains an array of dates. Present if ``IndexFieldType``
        specifies the field is of type ``date-array`` . All options are enabled by default.

        - **DefaultValue** *(string) --* A value to use for the field if the field isn't
        specified for a document.

        - **SourceFields** *(string) --*

          A list of source fields to map to the field.

        - **FacetEnabled** *(boolean) --*

          Whether facet information can be returned for the field.

        - **SearchEnabled** *(boolean) --*

          Whether the contents of the field are searchable.

        - **ReturnEnabled** *(boolean) --*

          Whether the contents of the field can be returned in the search results.

    - **Status** *(dict) --*

      The status of domain configuration option.

      - **CreationDate** *(datetime) --*

        A timestamp for when this option was created.

      - **UpdateDate** *(datetime) --*

        A timestamp for when this option was last updated.

      - **UpdateVersion** *(integer) --*

        A unique integer that indicates when this option was last updated.

      - **State** *(string) --*

        The state of processing a change to an option. Possible values:

        * ``RequiresIndexDocuments`` : the option's latest value will not be deployed until
        IndexDocuments has been called and indexing is complete.

        * ``Processing`` : the option's latest value is in the process of being activated.

        * ``Active`` : the option's latest value is completely deployed.

        * ``FailedToValidate`` : the option value is not compatible with the domain's data and
        cannot be used to index the data. You must either modify the option value or update or
        remove the incompatible documents.

      - **PendingDeletion** *(boolean) --*

        Indicates that the option will be deleted once processing is complete.
    """


_ClientDeleteIndexFieldResponseTypeDef = TypedDict(
    "_ClientDeleteIndexFieldResponseTypeDef",
    {"IndexField": ClientDeleteIndexFieldResponseIndexFieldTypeDef},
    total=False,
)


class ClientDeleteIndexFieldResponseTypeDef(_ClientDeleteIndexFieldResponseTypeDef):
    """
    Type definition for `ClientDeleteIndexField` `Response`

    The result of a `` DeleteIndexField`` request.

    - **IndexField** *(dict) --*

      The status of the index field being deleted.

      - **Options** *(dict) --*

        Configuration information for a field in the index, including its name, type, and options.
        The supported options depend on the `` IndexFieldType`` .

        - **IndexFieldName** *(string) --*

          A string that represents the name of an index field. CloudSearch supports regular index
          fields as well as dynamic fields. A dynamic field's name defines a pattern that begins or
          ends with a wildcard. Any document fields that don't map to a regular index field but do
          match a dynamic field's pattern are configured with the dynamic field's indexing options.

          Regular field names begin with a letter and can contain the following characters: a-z
          (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a
          wildcard (*). The wildcard can also be the only character in a dynamic field name.
          Multiple wildcards, and wildcards embedded within a string are not supported.

          The name ``score`` is reserved and cannot be used as a field name. To reference a
          document's ID, you can use the name ``_id`` .

        - **IndexFieldType** *(string) --*

          The type of field. The valid options for a field depend on the field type. For more
          information about the supported field types, see `Configuring Index Fields
          <http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-index-fields.html>`__
          in the *Amazon CloudSearch Developer Guide* .

        - **IntOptions** *(dict) --*

          Options for a 64-bit signed integer field. Present if ``IndexFieldType`` specifies the
          field is of type ``int`` . All options are enabled by default.

          - **DefaultValue** *(integer) --* A value to use for the field if the field isn't
          specified for a document. This can be important if you are using the field in an
          expression and that field is not present in every document.

          - **SourceField** *(string) --*

            The name of the source field to map to the field.

          - **FacetEnabled** *(boolean) --*

            Whether facet information can be returned for the field.

          - **SearchEnabled** *(boolean) --*

            Whether the contents of the field are searchable.

          - **ReturnEnabled** *(boolean) --*

            Whether the contents of the field can be returned in the search results.

          - **SortEnabled** *(boolean) --*

            Whether the field can be used to sort the search results.

        - **DoubleOptions** *(dict) --*

          Options for a double-precision 64-bit floating point field. Present if ``IndexFieldType``
          specifies the field is of type ``double`` . All options are enabled by default.

          - **DefaultValue** *(float) --*

            A value to use for the field if the field isn't specified for a document. This can be
            important if you are using the field in an expression and that field is not present in
            every document.

          - **SourceField** *(string) --*

            The name of the source field to map to the field.

          - **FacetEnabled** *(boolean) --*

            Whether facet information can be returned for the field.

          - **SearchEnabled** *(boolean) --*

            Whether the contents of the field are searchable.

          - **ReturnEnabled** *(boolean) --*

            Whether the contents of the field can be returned in the search results.

          - **SortEnabled** *(boolean) --*

            Whether the field can be used to sort the search results.

        - **LiteralOptions** *(dict) --*

          Options for literal field. Present if ``IndexFieldType`` specifies the field is of type
          ``literal`` . All options are enabled by default.

          - **DefaultValue** *(string) --* A value to use for the field if the field isn't
          specified for a document.

          - **SourceField** *(string) --*

            A string that represents the name of an index field. CloudSearch supports regular index
            fields as well as dynamic fields. A dynamic field's name defines a pattern that begins
            or ends with a wildcard. Any document fields that don't map to a regular index field
            but do match a dynamic field's pattern are configured with the dynamic field's indexing
            options.

            Regular field names begin with a letter and can contain the following characters: a-z
            (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a
            wildcard (*). The wildcard can also be the only character in a dynamic field name.
            Multiple wildcards, and wildcards embedded within a string are not supported.

            The name ``score`` is reserved and cannot be used as a field name. To reference a
            document's ID, you can use the name ``_id`` .

          - **FacetEnabled** *(boolean) --*

            Whether facet information can be returned for the field.

          - **SearchEnabled** *(boolean) --*

            Whether the contents of the field are searchable.

          - **ReturnEnabled** *(boolean) --*

            Whether the contents of the field can be returned in the search results.

          - **SortEnabled** *(boolean) --*

            Whether the field can be used to sort the search results.

        - **TextOptions** *(dict) --*

          Options for text field. Present if ``IndexFieldType`` specifies the field is of type
          ``text`` . A ``text`` field is always searchable. All options are enabled by default.

          - **DefaultValue** *(string) --* A value to use for the field if the field isn't
          specified for a document.

          - **SourceField** *(string) --*

            A string that represents the name of an index field. CloudSearch supports regular index
            fields as well as dynamic fields. A dynamic field's name defines a pattern that begins
            or ends with a wildcard. Any document fields that don't map to a regular index field
            but do match a dynamic field's pattern are configured with the dynamic field's indexing
            options.

            Regular field names begin with a letter and can contain the following characters: a-z
            (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a
            wildcard (*). The wildcard can also be the only character in a dynamic field name.
            Multiple wildcards, and wildcards embedded within a string are not supported.

            The name ``score`` is reserved and cannot be used as a field name. To reference a
            document's ID, you can use the name ``_id`` .

          - **ReturnEnabled** *(boolean) --*

            Whether the contents of the field can be returned in the search results.

          - **SortEnabled** *(boolean) --*

            Whether the field can be used to sort the search results.

          - **HighlightEnabled** *(boolean) --*

            Whether highlights can be returned for the field.

          - **AnalysisScheme** *(string) --*

            The name of an analysis scheme for a ``text`` field.

        - **DateOptions** *(dict) --*

          Options for a date field. Dates and times are specified in UTC (Coordinated Universal
          Time) according to IETF RFC3339: yyyy-mm-ddT00:00:00Z. Present if ``IndexFieldType``
          specifies the field is of type ``date`` . All options are enabled by default.

          - **DefaultValue** *(string) --* A value to use for the field if the field isn't
          specified for a document.

          - **SourceField** *(string) --*

            A string that represents the name of an index field. CloudSearch supports regular index
            fields as well as dynamic fields. A dynamic field's name defines a pattern that begins
            or ends with a wildcard. Any document fields that don't map to a regular index field
            but do match a dynamic field's pattern are configured with the dynamic field's indexing
            options.

            Regular field names begin with a letter and can contain the following characters: a-z
            (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a
            wildcard (*). The wildcard can also be the only character in a dynamic field name.
            Multiple wildcards, and wildcards embedded within a string are not supported.

            The name ``score`` is reserved and cannot be used as a field name. To reference a
            document's ID, you can use the name ``_id`` .

          - **FacetEnabled** *(boolean) --*

            Whether facet information can be returned for the field.

          - **SearchEnabled** *(boolean) --*

            Whether the contents of the field are searchable.

          - **ReturnEnabled** *(boolean) --*

            Whether the contents of the field can be returned in the search results.

          - **SortEnabled** *(boolean) --*

            Whether the field can be used to sort the search results.

        - **LatLonOptions** *(dict) --*

          Options for a latlon field. A latlon field contains a location stored as a latitude and
          longitude value pair. Present if ``IndexFieldType`` specifies the field is of type
          ``latlon`` . All options are enabled by default.

          - **DefaultValue** *(string) --* A value to use for the field if the field isn't
          specified for a document.

          - **SourceField** *(string) --*

            A string that represents the name of an index field. CloudSearch supports regular index
            fields as well as dynamic fields. A dynamic field's name defines a pattern that begins
            or ends with a wildcard. Any document fields that don't map to a regular index field
            but do match a dynamic field's pattern are configured with the dynamic field's indexing
            options.

            Regular field names begin with a letter and can contain the following characters: a-z
            (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a
            wildcard (*). The wildcard can also be the only character in a dynamic field name.
            Multiple wildcards, and wildcards embedded within a string are not supported.

            The name ``score`` is reserved and cannot be used as a field name. To reference a
            document's ID, you can use the name ``_id`` .

          - **FacetEnabled** *(boolean) --*

            Whether facet information can be returned for the field.

          - **SearchEnabled** *(boolean) --*

            Whether the contents of the field are searchable.

          - **ReturnEnabled** *(boolean) --*

            Whether the contents of the field can be returned in the search results.

          - **SortEnabled** *(boolean) --*

            Whether the field can be used to sort the search results.

        - **IntArrayOptions** *(dict) --*

          Options for a field that contains an array of 64-bit signed integers. Present if
          ``IndexFieldType`` specifies the field is of type ``int-array`` . All options are enabled
          by default.

          - **DefaultValue** *(integer) --* A value to use for the field if the field isn't
          specified for a document.

          - **SourceFields** *(string) --*

            A list of source fields to map to the field.

          - **FacetEnabled** *(boolean) --*

            Whether facet information can be returned for the field.

          - **SearchEnabled** *(boolean) --*

            Whether the contents of the field are searchable.

          - **ReturnEnabled** *(boolean) --*

            Whether the contents of the field can be returned in the search results.

        - **DoubleArrayOptions** *(dict) --*

          Options for a field that contains an array of double-precision 64-bit floating point
          values. Present if ``IndexFieldType`` specifies the field is of type ``double-array`` .
          All options are enabled by default.

          - **DefaultValue** *(float) --* A value to use for the field if the field isn't specified
          for a document.

          - **SourceFields** *(string) --*

            A list of source fields to map to the field.

          - **FacetEnabled** *(boolean) --*

            Whether facet information can be returned for the field.

          - **SearchEnabled** *(boolean) --*

            Whether the contents of the field are searchable.

          - **ReturnEnabled** *(boolean) --*

            Whether the contents of the field can be returned in the search results.

        - **LiteralArrayOptions** *(dict) --*

          Options for a field that contains an array of literal strings. Present if
          ``IndexFieldType`` specifies the field is of type ``literal-array`` . All options are
          enabled by default.

          - **DefaultValue** *(string) --* A value to use for the field if the field isn't
          specified for a document.

          - **SourceFields** *(string) --*

            A list of source fields to map to the field.

          - **FacetEnabled** *(boolean) --*

            Whether facet information can be returned for the field.

          - **SearchEnabled** *(boolean) --*

            Whether the contents of the field are searchable.

          - **ReturnEnabled** *(boolean) --*

            Whether the contents of the field can be returned in the search results.

        - **TextArrayOptions** *(dict) --*

          Options for a field that contains an array of text strings. Present if ``IndexFieldType``
          specifies the field is of type ``text-array`` . A ``text-array`` field is always
          searchable. All options are enabled by default.

          - **DefaultValue** *(string) --* A value to use for the field if the field isn't
          specified for a document.

          - **SourceFields** *(string) --*

            A list of source fields to map to the field.

          - **ReturnEnabled** *(boolean) --*

            Whether the contents of the field can be returned in the search results.

          - **HighlightEnabled** *(boolean) --*

            Whether highlights can be returned for the field.

          - **AnalysisScheme** *(string) --*

            The name of an analysis scheme for a ``text-array`` field.

        - **DateArrayOptions** *(dict) --*

          Options for a field that contains an array of dates. Present if ``IndexFieldType``
          specifies the field is of type ``date-array`` . All options are enabled by default.

          - **DefaultValue** *(string) --* A value to use for the field if the field isn't
          specified for a document.

          - **SourceFields** *(string) --*

            A list of source fields to map to the field.

          - **FacetEnabled** *(boolean) --*

            Whether facet information can be returned for the field.

          - **SearchEnabled** *(boolean) --*

            Whether the contents of the field are searchable.

          - **ReturnEnabled** *(boolean) --*

            Whether the contents of the field can be returned in the search results.

      - **Status** *(dict) --*

        The status of domain configuration option.

        - **CreationDate** *(datetime) --*

          A timestamp for when this option was created.

        - **UpdateDate** *(datetime) --*

          A timestamp for when this option was last updated.

        - **UpdateVersion** *(integer) --*

          A unique integer that indicates when this option was last updated.

        - **State** *(string) --*

          The state of processing a change to an option. Possible values:

          * ``RequiresIndexDocuments`` : the option's latest value will not be deployed until
          IndexDocuments has been called and indexing is complete.

          * ``Processing`` : the option's latest value is in the process of being activated.

          * ``Active`` : the option's latest value is completely deployed.

          * ``FailedToValidate`` : the option value is not compatible with the domain's data and
          cannot be used to index the data. You must either modify the option value or update or
          remove the incompatible documents.

        - **PendingDeletion** *(boolean) --*

          Indicates that the option will be deleted once processing is complete.
    """


_ClientDeleteSuggesterResponseSuggesterOptionsDocumentSuggesterOptionsTypeDef = TypedDict(
    "_ClientDeleteSuggesterResponseSuggesterOptionsDocumentSuggesterOptionsTypeDef",
    {"SourceField": str, "FuzzyMatching": str, "SortExpression": str},
    total=False,
)


class ClientDeleteSuggesterResponseSuggesterOptionsDocumentSuggesterOptionsTypeDef(
    _ClientDeleteSuggesterResponseSuggesterOptionsDocumentSuggesterOptionsTypeDef
):
    """
    Type definition for `ClientDeleteSuggesterResponseSuggesterOptions` `DocumentSuggesterOptions`

    Options for a search suggester.

    - **SourceField** *(string) --*

      The name of the index field you want to use for suggestions.

    - **FuzzyMatching** *(string) --*

      The level of fuzziness allowed when suggesting matches for a string: ``none`` , ``low``
      , or ``high`` . With none, the specified string is treated as an exact prefix. With
      low, suggestions must differ from the specified string by no more than one character.
      With high, suggestions can differ by up to two characters. The default is none.

    - **SortExpression** *(string) --*

      An expression that computes a score for each suggestion to control how they are sorted.
      The scores are rounded to the nearest integer, with a floor of 0 and a ceiling of
      2^31-1. A document's relevance score is not computed for suggestions, so sort
      expressions cannot reference the ``_score`` value. To sort suggestions using a numeric
      field or existing expression, simply specify the name of the field or expression. If no
      expression is configured for the suggester, the suggestions are sorted with the closest
      matches listed first.
    """


_ClientDeleteSuggesterResponseSuggesterOptionsTypeDef = TypedDict(
    "_ClientDeleteSuggesterResponseSuggesterOptionsTypeDef",
    {
        "SuggesterName": str,
        "DocumentSuggesterOptions": ClientDeleteSuggesterResponseSuggesterOptionsDocumentSuggesterOptionsTypeDef,
    },
    total=False,
)


class ClientDeleteSuggesterResponseSuggesterOptionsTypeDef(
    _ClientDeleteSuggesterResponseSuggesterOptionsTypeDef
):
    """
    Type definition for `ClientDeleteSuggesterResponseSuggester` `Options`

    Configuration information for a search suggester. Each suggester has a unique name and
    specifies the text field you want to use for suggestions. The following options can be
    configured for a suggester: ``FuzzyMatching`` , ``SortExpression`` .

    - **SuggesterName** *(string) --*

      Names must begin with a letter and can contain the following characters: a-z (lowercase),
      0-9, and _ (underscore).

    - **DocumentSuggesterOptions** *(dict) --*

      Options for a search suggester.

      - **SourceField** *(string) --*

        The name of the index field you want to use for suggestions.

      - **FuzzyMatching** *(string) --*

        The level of fuzziness allowed when suggesting matches for a string: ``none`` , ``low``
        , or ``high`` . With none, the specified string is treated as an exact prefix. With
        low, suggestions must differ from the specified string by no more than one character.
        With high, suggestions can differ by up to two characters. The default is none.

      - **SortExpression** *(string) --*

        An expression that computes a score for each suggestion to control how they are sorted.
        The scores are rounded to the nearest integer, with a floor of 0 and a ceiling of
        2^31-1. A document's relevance score is not computed for suggestions, so sort
        expressions cannot reference the ``_score`` value. To sort suggestions using a numeric
        field or existing expression, simply specify the name of the field or expression. If no
        expression is configured for the suggester, the suggestions are sorted with the closest
        matches listed first.
    """


_ClientDeleteSuggesterResponseSuggesterStatusTypeDef = TypedDict(
    "_ClientDeleteSuggesterResponseSuggesterStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": str,
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientDeleteSuggesterResponseSuggesterStatusTypeDef(
    _ClientDeleteSuggesterResponseSuggesterStatusTypeDef
):
    """
    Type definition for `ClientDeleteSuggesterResponseSuggester` `Status`

    The status of domain configuration option.

    - **CreationDate** *(datetime) --*

      A timestamp for when this option was created.

    - **UpdateDate** *(datetime) --*

      A timestamp for when this option was last updated.

    - **UpdateVersion** *(integer) --*

      A unique integer that indicates when this option was last updated.

    - **State** *(string) --*

      The state of processing a change to an option. Possible values:

      * ``RequiresIndexDocuments`` : the option's latest value will not be deployed until
      IndexDocuments has been called and indexing is complete.

      * ``Processing`` : the option's latest value is in the process of being activated.

      * ``Active`` : the option's latest value is completely deployed.

      * ``FailedToValidate`` : the option value is not compatible with the domain's data and
      cannot be used to index the data. You must either modify the option value or update or
      remove the incompatible documents.

    - **PendingDeletion** *(boolean) --*

      Indicates that the option will be deleted once processing is complete.
    """


_ClientDeleteSuggesterResponseSuggesterTypeDef = TypedDict(
    "_ClientDeleteSuggesterResponseSuggesterTypeDef",
    {
        "Options": ClientDeleteSuggesterResponseSuggesterOptionsTypeDef,
        "Status": ClientDeleteSuggesterResponseSuggesterStatusTypeDef,
    },
    total=False,
)


class ClientDeleteSuggesterResponseSuggesterTypeDef(
    _ClientDeleteSuggesterResponseSuggesterTypeDef
):
    """
    Type definition for `ClientDeleteSuggesterResponse` `Suggester`

    The status of the suggester being deleted.

    - **Options** *(dict) --*

      Configuration information for a search suggester. Each suggester has a unique name and
      specifies the text field you want to use for suggestions. The following options can be
      configured for a suggester: ``FuzzyMatching`` , ``SortExpression`` .

      - **SuggesterName** *(string) --*

        Names must begin with a letter and can contain the following characters: a-z (lowercase),
        0-9, and _ (underscore).

      - **DocumentSuggesterOptions** *(dict) --*

        Options for a search suggester.

        - **SourceField** *(string) --*

          The name of the index field you want to use for suggestions.

        - **FuzzyMatching** *(string) --*

          The level of fuzziness allowed when suggesting matches for a string: ``none`` , ``low``
          , or ``high`` . With none, the specified string is treated as an exact prefix. With
          low, suggestions must differ from the specified string by no more than one character.
          With high, suggestions can differ by up to two characters. The default is none.

        - **SortExpression** *(string) --*

          An expression that computes a score for each suggestion to control how they are sorted.
          The scores are rounded to the nearest integer, with a floor of 0 and a ceiling of
          2^31-1. A document's relevance score is not computed for suggestions, so sort
          expressions cannot reference the ``_score`` value. To sort suggestions using a numeric
          field or existing expression, simply specify the name of the field or expression. If no
          expression is configured for the suggester, the suggestions are sorted with the closest
          matches listed first.

    - **Status** *(dict) --*

      The status of domain configuration option.

      - **CreationDate** *(datetime) --*

        A timestamp for when this option was created.

      - **UpdateDate** *(datetime) --*

        A timestamp for when this option was last updated.

      - **UpdateVersion** *(integer) --*

        A unique integer that indicates when this option was last updated.

      - **State** *(string) --*

        The state of processing a change to an option. Possible values:

        * ``RequiresIndexDocuments`` : the option's latest value will not be deployed until
        IndexDocuments has been called and indexing is complete.

        * ``Processing`` : the option's latest value is in the process of being activated.

        * ``Active`` : the option's latest value is completely deployed.

        * ``FailedToValidate`` : the option value is not compatible with the domain's data and
        cannot be used to index the data. You must either modify the option value or update or
        remove the incompatible documents.

      - **PendingDeletion** *(boolean) --*

        Indicates that the option will be deleted once processing is complete.
    """


_ClientDeleteSuggesterResponseTypeDef = TypedDict(
    "_ClientDeleteSuggesterResponseTypeDef",
    {"Suggester": ClientDeleteSuggesterResponseSuggesterTypeDef},
    total=False,
)


class ClientDeleteSuggesterResponseTypeDef(_ClientDeleteSuggesterResponseTypeDef):
    """
    Type definition for `ClientDeleteSuggester` `Response`

    The result of a ``DeleteSuggester`` request. Contains the status of the deleted suggester.

    - **Suggester** *(dict) --*

      The status of the suggester being deleted.

      - **Options** *(dict) --*

        Configuration information for a search suggester. Each suggester has a unique name and
        specifies the text field you want to use for suggestions. The following options can be
        configured for a suggester: ``FuzzyMatching`` , ``SortExpression`` .

        - **SuggesterName** *(string) --*

          Names must begin with a letter and can contain the following characters: a-z (lowercase),
          0-9, and _ (underscore).

        - **DocumentSuggesterOptions** *(dict) --*

          Options for a search suggester.

          - **SourceField** *(string) --*

            The name of the index field you want to use for suggestions.

          - **FuzzyMatching** *(string) --*

            The level of fuzziness allowed when suggesting matches for a string: ``none`` , ``low``
            , or ``high`` . With none, the specified string is treated as an exact prefix. With
            low, suggestions must differ from the specified string by no more than one character.
            With high, suggestions can differ by up to two characters. The default is none.

          - **SortExpression** *(string) --*

            An expression that computes a score for each suggestion to control how they are sorted.
            The scores are rounded to the nearest integer, with a floor of 0 and a ceiling of
            2^31-1. A document's relevance score is not computed for suggestions, so sort
            expressions cannot reference the ``_score`` value. To sort suggestions using a numeric
            field or existing expression, simply specify the name of the field or expression. If no
            expression is configured for the suggester, the suggestions are sorted with the closest
            matches listed first.

      - **Status** *(dict) --*

        The status of domain configuration option.

        - **CreationDate** *(datetime) --*

          A timestamp for when this option was created.

        - **UpdateDate** *(datetime) --*

          A timestamp for when this option was last updated.

        - **UpdateVersion** *(integer) --*

          A unique integer that indicates when this option was last updated.

        - **State** *(string) --*

          The state of processing a change to an option. Possible values:

          * ``RequiresIndexDocuments`` : the option's latest value will not be deployed until
          IndexDocuments has been called and indexing is complete.

          * ``Processing`` : the option's latest value is in the process of being activated.

          * ``Active`` : the option's latest value is completely deployed.

          * ``FailedToValidate`` : the option value is not compatible with the domain's data and
          cannot be used to index the data. You must either modify the option value or update or
          remove the incompatible documents.

        - **PendingDeletion** *(boolean) --*

          Indicates that the option will be deleted once processing is complete.
    """


_ClientDescribeAnalysisSchemesResponseAnalysisSchemesOptionsAnalysisOptionsTypeDef = TypedDict(
    "_ClientDescribeAnalysisSchemesResponseAnalysisSchemesOptionsAnalysisOptionsTypeDef",
    {
        "Synonyms": str,
        "Stopwords": str,
        "StemmingDictionary": str,
        "JapaneseTokenizationDictionary": str,
        "AlgorithmicStemming": str,
    },
    total=False,
)


class ClientDescribeAnalysisSchemesResponseAnalysisSchemesOptionsAnalysisOptionsTypeDef(
    _ClientDescribeAnalysisSchemesResponseAnalysisSchemesOptionsAnalysisOptionsTypeDef
):
    """
    Type definition for `ClientDescribeAnalysisSchemesResponseAnalysisSchemesOptions` `AnalysisOptions`

    Synonyms, stopwords, and stemming options for an analysis scheme. Includes tokenization
    dictionary for Japanese.

    - **Synonyms** *(string) --*

      A JSON object that defines synonym groups and aliases. A synonym group is an array of
      arrays, where each sub-array is a group of terms where each term in the group is
      considered a synonym of every other term in the group. The aliases value is an object
      that contains a collection of string:value pairs where the string specifies a term
      and the array of values specifies each of the aliases for that term. An alias is
      considered a synonym of the specified term, but the term is not considered a synonym
      of the alias. For more information about specifying synonyms, see `Synonyms
      <http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-analysis-schemes.html#synonyms>`__
      in the *Amazon CloudSearch Developer Guide* .

    - **Stopwords** *(string) --*

      A JSON array of terms to ignore during indexing and searching. For example, ``["a",
      "an", "the", "of"]`` . The stopwords dictionary must explicitly list each word you
      want to ignore. Wildcards and regular expressions are not supported.

    - **StemmingDictionary** *(string) --*

      A JSON object that contains a collection of string:value pairs that each map a term
      to its stem. For example, ``{"term1": "stem1", "term2": "stem2", "term3": "stem3"}``
      . The stemming dictionary is applied in addition to any algorithmic stemming. This
      enables you to override the results of the algorithmic stemming to correct specific
      cases of overstemming or understemming. The maximum size of a stemming dictionary is
      500 KB.

    - **JapaneseTokenizationDictionary** *(string) --*

      A JSON array that contains a collection of terms, tokens, readings and part of speech
      for Japanese Tokenizaiton. The Japanese tokenization dictionary enables you to
      override the default tokenization for selected terms. This is only valid for Japanese
      language fields.

    - **AlgorithmicStemming** *(string) --*

      The level of algorithmic stemming to perform: ``none`` , ``minimal`` , ``light`` , or
      ``full`` . The available levels vary depending on the language. For more information,
      see `Language Specific Text Processing Settings
      <http://docs.aws.amazon.com/cloudsearch/latest/developerguide/text-processing.html#text-processing-settings>`__
      in the *Amazon CloudSearch Developer Guide*
    """


_ClientDescribeAnalysisSchemesResponseAnalysisSchemesOptionsTypeDef = TypedDict(
    "_ClientDescribeAnalysisSchemesResponseAnalysisSchemesOptionsTypeDef",
    {
        "AnalysisSchemeName": str,
        "AnalysisSchemeLanguage": str,
        "AnalysisOptions": ClientDescribeAnalysisSchemesResponseAnalysisSchemesOptionsAnalysisOptionsTypeDef,
    },
    total=False,
)


class ClientDescribeAnalysisSchemesResponseAnalysisSchemesOptionsTypeDef(
    _ClientDescribeAnalysisSchemesResponseAnalysisSchemesOptionsTypeDef
):
    """
    Type definition for `ClientDescribeAnalysisSchemesResponseAnalysisSchemes` `Options`

    Configuration information for an analysis scheme. Each analysis scheme has a unique name
    and specifies the language of the text to be processed. The following options can be
    configured for an analysis scheme: ``Synonyms`` , ``Stopwords`` , ``StemmingDictionary``
    , ``JapaneseTokenizationDictionary`` and ``AlgorithmicStemming`` .

    - **AnalysisSchemeName** *(string) --*

      Names must begin with a letter and can contain the following characters: a-z
      (lowercase), 0-9, and _ (underscore).

    - **AnalysisSchemeLanguage** *(string) --*

      An `IETF RFC 4646 <http://tools.ietf.org/html/rfc4646>`__ language code or ``mul`` for
      multiple languages.

    - **AnalysisOptions** *(dict) --*

      Synonyms, stopwords, and stemming options for an analysis scheme. Includes tokenization
      dictionary for Japanese.

      - **Synonyms** *(string) --*

        A JSON object that defines synonym groups and aliases. A synonym group is an array of
        arrays, where each sub-array is a group of terms where each term in the group is
        considered a synonym of every other term in the group. The aliases value is an object
        that contains a collection of string:value pairs where the string specifies a term
        and the array of values specifies each of the aliases for that term. An alias is
        considered a synonym of the specified term, but the term is not considered a synonym
        of the alias. For more information about specifying synonyms, see `Synonyms
        <http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-analysis-schemes.html#synonyms>`__
        in the *Amazon CloudSearch Developer Guide* .

      - **Stopwords** *(string) --*

        A JSON array of terms to ignore during indexing and searching. For example, ``["a",
        "an", "the", "of"]`` . The stopwords dictionary must explicitly list each word you
        want to ignore. Wildcards and regular expressions are not supported.

      - **StemmingDictionary** *(string) --*

        A JSON object that contains a collection of string:value pairs that each map a term
        to its stem. For example, ``{"term1": "stem1", "term2": "stem2", "term3": "stem3"}``
        . The stemming dictionary is applied in addition to any algorithmic stemming. This
        enables you to override the results of the algorithmic stemming to correct specific
        cases of overstemming or understemming. The maximum size of a stemming dictionary is
        500 KB.

      - **JapaneseTokenizationDictionary** *(string) --*

        A JSON array that contains a collection of terms, tokens, readings and part of speech
        for Japanese Tokenizaiton. The Japanese tokenization dictionary enables you to
        override the default tokenization for selected terms. This is only valid for Japanese
        language fields.

      - **AlgorithmicStemming** *(string) --*

        The level of algorithmic stemming to perform: ``none`` , ``minimal`` , ``light`` , or
        ``full`` . The available levels vary depending on the language. For more information,
        see `Language Specific Text Processing Settings
        <http://docs.aws.amazon.com/cloudsearch/latest/developerguide/text-processing.html#text-processing-settings>`__
        in the *Amazon CloudSearch Developer Guide*
    """


_ClientDescribeAnalysisSchemesResponseAnalysisSchemesStatusTypeDef = TypedDict(
    "_ClientDescribeAnalysisSchemesResponseAnalysisSchemesStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": str,
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientDescribeAnalysisSchemesResponseAnalysisSchemesStatusTypeDef(
    _ClientDescribeAnalysisSchemesResponseAnalysisSchemesStatusTypeDef
):
    """
    Type definition for `ClientDescribeAnalysisSchemesResponseAnalysisSchemes` `Status`

    The status of domain configuration option.

    - **CreationDate** *(datetime) --*

      A timestamp for when this option was created.

    - **UpdateDate** *(datetime) --*

      A timestamp for when this option was last updated.

    - **UpdateVersion** *(integer) --*

      A unique integer that indicates when this option was last updated.

    - **State** *(string) --*

      The state of processing a change to an option. Possible values:

      * ``RequiresIndexDocuments`` : the option's latest value will not be deployed until
      IndexDocuments has been called and indexing is complete.

      * ``Processing`` : the option's latest value is in the process of being activated.

      * ``Active`` : the option's latest value is completely deployed.

      * ``FailedToValidate`` : the option value is not compatible with the domain's data and
      cannot be used to index the data. You must either modify the option value or update or
      remove the incompatible documents.

    - **PendingDeletion** *(boolean) --*

      Indicates that the option will be deleted once processing is complete.
    """


_ClientDescribeAnalysisSchemesResponseAnalysisSchemesTypeDef = TypedDict(
    "_ClientDescribeAnalysisSchemesResponseAnalysisSchemesTypeDef",
    {
        "Options": ClientDescribeAnalysisSchemesResponseAnalysisSchemesOptionsTypeDef,
        "Status": ClientDescribeAnalysisSchemesResponseAnalysisSchemesStatusTypeDef,
    },
    total=False,
)


class ClientDescribeAnalysisSchemesResponseAnalysisSchemesTypeDef(
    _ClientDescribeAnalysisSchemesResponseAnalysisSchemesTypeDef
):
    """
    Type definition for `ClientDescribeAnalysisSchemesResponse` `AnalysisSchemes`

    The status and configuration of an ``AnalysisScheme`` .

    - **Options** *(dict) --*

      Configuration information for an analysis scheme. Each analysis scheme has a unique name
      and specifies the language of the text to be processed. The following options can be
      configured for an analysis scheme: ``Synonyms`` , ``Stopwords`` , ``StemmingDictionary``
      , ``JapaneseTokenizationDictionary`` and ``AlgorithmicStemming`` .

      - **AnalysisSchemeName** *(string) --*

        Names must begin with a letter and can contain the following characters: a-z
        (lowercase), 0-9, and _ (underscore).

      - **AnalysisSchemeLanguage** *(string) --*

        An `IETF RFC 4646 <http://tools.ietf.org/html/rfc4646>`__ language code or ``mul`` for
        multiple languages.

      - **AnalysisOptions** *(dict) --*

        Synonyms, stopwords, and stemming options for an analysis scheme. Includes tokenization
        dictionary for Japanese.

        - **Synonyms** *(string) --*

          A JSON object that defines synonym groups and aliases. A synonym group is an array of
          arrays, where each sub-array is a group of terms where each term in the group is
          considered a synonym of every other term in the group. The aliases value is an object
          that contains a collection of string:value pairs where the string specifies a term
          and the array of values specifies each of the aliases for that term. An alias is
          considered a synonym of the specified term, but the term is not considered a synonym
          of the alias. For more information about specifying synonyms, see `Synonyms
          <http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-analysis-schemes.html#synonyms>`__
          in the *Amazon CloudSearch Developer Guide* .

        - **Stopwords** *(string) --*

          A JSON array of terms to ignore during indexing and searching. For example, ``["a",
          "an", "the", "of"]`` . The stopwords dictionary must explicitly list each word you
          want to ignore. Wildcards and regular expressions are not supported.

        - **StemmingDictionary** *(string) --*

          A JSON object that contains a collection of string:value pairs that each map a term
          to its stem. For example, ``{"term1": "stem1", "term2": "stem2", "term3": "stem3"}``
          . The stemming dictionary is applied in addition to any algorithmic stemming. This
          enables you to override the results of the algorithmic stemming to correct specific
          cases of overstemming or understemming. The maximum size of a stemming dictionary is
          500 KB.

        - **JapaneseTokenizationDictionary** *(string) --*

          A JSON array that contains a collection of terms, tokens, readings and part of speech
          for Japanese Tokenizaiton. The Japanese tokenization dictionary enables you to
          override the default tokenization for selected terms. This is only valid for Japanese
          language fields.

        - **AlgorithmicStemming** *(string) --*

          The level of algorithmic stemming to perform: ``none`` , ``minimal`` , ``light`` , or
          ``full`` . The available levels vary depending on the language. For more information,
          see `Language Specific Text Processing Settings
          <http://docs.aws.amazon.com/cloudsearch/latest/developerguide/text-processing.html#text-processing-settings>`__
          in the *Amazon CloudSearch Developer Guide*

    - **Status** *(dict) --*

      The status of domain configuration option.

      - **CreationDate** *(datetime) --*

        A timestamp for when this option was created.

      - **UpdateDate** *(datetime) --*

        A timestamp for when this option was last updated.

      - **UpdateVersion** *(integer) --*

        A unique integer that indicates when this option was last updated.

      - **State** *(string) --*

        The state of processing a change to an option. Possible values:

        * ``RequiresIndexDocuments`` : the option's latest value will not be deployed until
        IndexDocuments has been called and indexing is complete.

        * ``Processing`` : the option's latest value is in the process of being activated.

        * ``Active`` : the option's latest value is completely deployed.

        * ``FailedToValidate`` : the option value is not compatible with the domain's data and
        cannot be used to index the data. You must either modify the option value or update or
        remove the incompatible documents.

      - **PendingDeletion** *(boolean) --*

        Indicates that the option will be deleted once processing is complete.
    """


_ClientDescribeAnalysisSchemesResponseTypeDef = TypedDict(
    "_ClientDescribeAnalysisSchemesResponseTypeDef",
    {
        "AnalysisSchemes": List[
            ClientDescribeAnalysisSchemesResponseAnalysisSchemesTypeDef
        ]
    },
    total=False,
)


class ClientDescribeAnalysisSchemesResponseTypeDef(
    _ClientDescribeAnalysisSchemesResponseTypeDef
):
    """
    Type definition for `ClientDescribeAnalysisSchemes` `Response`

    The result of a ``DescribeAnalysisSchemes`` request. Contains the analysis schemes configured
    for the domain specified in the request.

    - **AnalysisSchemes** *(list) --*

      The analysis scheme descriptions.

      - *(dict) --*

        The status and configuration of an ``AnalysisScheme`` .

        - **Options** *(dict) --*

          Configuration information for an analysis scheme. Each analysis scheme has a unique name
          and specifies the language of the text to be processed. The following options can be
          configured for an analysis scheme: ``Synonyms`` , ``Stopwords`` , ``StemmingDictionary``
          , ``JapaneseTokenizationDictionary`` and ``AlgorithmicStemming`` .

          - **AnalysisSchemeName** *(string) --*

            Names must begin with a letter and can contain the following characters: a-z
            (lowercase), 0-9, and _ (underscore).

          - **AnalysisSchemeLanguage** *(string) --*

            An `IETF RFC 4646 <http://tools.ietf.org/html/rfc4646>`__ language code or ``mul`` for
            multiple languages.

          - **AnalysisOptions** *(dict) --*

            Synonyms, stopwords, and stemming options for an analysis scheme. Includes tokenization
            dictionary for Japanese.

            - **Synonyms** *(string) --*

              A JSON object that defines synonym groups and aliases. A synonym group is an array of
              arrays, where each sub-array is a group of terms where each term in the group is
              considered a synonym of every other term in the group. The aliases value is an object
              that contains a collection of string:value pairs where the string specifies a term
              and the array of values specifies each of the aliases for that term. An alias is
              considered a synonym of the specified term, but the term is not considered a synonym
              of the alias. For more information about specifying synonyms, see `Synonyms
              <http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-analysis-schemes.html#synonyms>`__
              in the *Amazon CloudSearch Developer Guide* .

            - **Stopwords** *(string) --*

              A JSON array of terms to ignore during indexing and searching. For example, ``["a",
              "an", "the", "of"]`` . The stopwords dictionary must explicitly list each word you
              want to ignore. Wildcards and regular expressions are not supported.

            - **StemmingDictionary** *(string) --*

              A JSON object that contains a collection of string:value pairs that each map a term
              to its stem. For example, ``{"term1": "stem1", "term2": "stem2", "term3": "stem3"}``
              . The stemming dictionary is applied in addition to any algorithmic stemming. This
              enables you to override the results of the algorithmic stemming to correct specific
              cases of overstemming or understemming. The maximum size of a stemming dictionary is
              500 KB.

            - **JapaneseTokenizationDictionary** *(string) --*

              A JSON array that contains a collection of terms, tokens, readings and part of speech
              for Japanese Tokenizaiton. The Japanese tokenization dictionary enables you to
              override the default tokenization for selected terms. This is only valid for Japanese
              language fields.

            - **AlgorithmicStemming** *(string) --*

              The level of algorithmic stemming to perform: ``none`` , ``minimal`` , ``light`` , or
              ``full`` . The available levels vary depending on the language. For more information,
              see `Language Specific Text Processing Settings
              <http://docs.aws.amazon.com/cloudsearch/latest/developerguide/text-processing.html#text-processing-settings>`__
              in the *Amazon CloudSearch Developer Guide*

        - **Status** *(dict) --*

          The status of domain configuration option.

          - **CreationDate** *(datetime) --*

            A timestamp for when this option was created.

          - **UpdateDate** *(datetime) --*

            A timestamp for when this option was last updated.

          - **UpdateVersion** *(integer) --*

            A unique integer that indicates when this option was last updated.

          - **State** *(string) --*

            The state of processing a change to an option. Possible values:

            * ``RequiresIndexDocuments`` : the option's latest value will not be deployed until
            IndexDocuments has been called and indexing is complete.

            * ``Processing`` : the option's latest value is in the process of being activated.

            * ``Active`` : the option's latest value is completely deployed.

            * ``FailedToValidate`` : the option value is not compatible with the domain's data and
            cannot be used to index the data. You must either modify the option value or update or
            remove the incompatible documents.

          - **PendingDeletion** *(boolean) --*

            Indicates that the option will be deleted once processing is complete.
    """


_ClientDescribeAvailabilityOptionsResponseAvailabilityOptionsStatusTypeDef = TypedDict(
    "_ClientDescribeAvailabilityOptionsResponseAvailabilityOptionsStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": str,
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientDescribeAvailabilityOptionsResponseAvailabilityOptionsStatusTypeDef(
    _ClientDescribeAvailabilityOptionsResponseAvailabilityOptionsStatusTypeDef
):
    """
    Type definition for `ClientDescribeAvailabilityOptionsResponseAvailabilityOptions` `Status`

    The status of domain configuration option.

    - **CreationDate** *(datetime) --*

      A timestamp for when this option was created.

    - **UpdateDate** *(datetime) --*

      A timestamp for when this option was last updated.

    - **UpdateVersion** *(integer) --*

      A unique integer that indicates when this option was last updated.

    - **State** *(string) --*

      The state of processing a change to an option. Possible values:

      * ``RequiresIndexDocuments`` : the option's latest value will not be deployed until
      IndexDocuments has been called and indexing is complete.

      * ``Processing`` : the option's latest value is in the process of being activated.

      * ``Active`` : the option's latest value is completely deployed.

      * ``FailedToValidate`` : the option value is not compatible with the domain's data and
      cannot be used to index the data. You must either modify the option value or update or
      remove the incompatible documents.

    - **PendingDeletion** *(boolean) --*

      Indicates that the option will be deleted once processing is complete.
    """


_ClientDescribeAvailabilityOptionsResponseAvailabilityOptionsTypeDef = TypedDict(
    "_ClientDescribeAvailabilityOptionsResponseAvailabilityOptionsTypeDef",
    {
        "Options": bool,
        "Status": ClientDescribeAvailabilityOptionsResponseAvailabilityOptionsStatusTypeDef,
    },
    total=False,
)


class ClientDescribeAvailabilityOptionsResponseAvailabilityOptionsTypeDef(
    _ClientDescribeAvailabilityOptionsResponseAvailabilityOptionsTypeDef
):
    """
    Type definition for `ClientDescribeAvailabilityOptionsResponse` `AvailabilityOptions`

    The availability options configured for the domain. Indicates whether Multi-AZ is enabled for
    the domain.

    - **Options** *(boolean) --*

      The availability options configured for the domain.

    - **Status** *(dict) --*

      The status of domain configuration option.

      - **CreationDate** *(datetime) --*

        A timestamp for when this option was created.

      - **UpdateDate** *(datetime) --*

        A timestamp for when this option was last updated.

      - **UpdateVersion** *(integer) --*

        A unique integer that indicates when this option was last updated.

      - **State** *(string) --*

        The state of processing a change to an option. Possible values:

        * ``RequiresIndexDocuments`` : the option's latest value will not be deployed until
        IndexDocuments has been called and indexing is complete.

        * ``Processing`` : the option's latest value is in the process of being activated.

        * ``Active`` : the option's latest value is completely deployed.

        * ``FailedToValidate`` : the option value is not compatible with the domain's data and
        cannot be used to index the data. You must either modify the option value or update or
        remove the incompatible documents.

      - **PendingDeletion** *(boolean) --*

        Indicates that the option will be deleted once processing is complete.
    """


_ClientDescribeAvailabilityOptionsResponseTypeDef = TypedDict(
    "_ClientDescribeAvailabilityOptionsResponseTypeDef",
    {
        "AvailabilityOptions": ClientDescribeAvailabilityOptionsResponseAvailabilityOptionsTypeDef
    },
    total=False,
)


class ClientDescribeAvailabilityOptionsResponseTypeDef(
    _ClientDescribeAvailabilityOptionsResponseTypeDef
):
    """
    Type definition for `ClientDescribeAvailabilityOptions` `Response`

    The result of a ``DescribeAvailabilityOptions`` request. Indicates whether or not the Multi-AZ
    option is enabled for the domain specified in the request.

    - **AvailabilityOptions** *(dict) --*

      The availability options configured for the domain. Indicates whether Multi-AZ is enabled for
      the domain.

      - **Options** *(boolean) --*

        The availability options configured for the domain.

      - **Status** *(dict) --*

        The status of domain configuration option.

        - **CreationDate** *(datetime) --*

          A timestamp for when this option was created.

        - **UpdateDate** *(datetime) --*

          A timestamp for when this option was last updated.

        - **UpdateVersion** *(integer) --*

          A unique integer that indicates when this option was last updated.

        - **State** *(string) --*

          The state of processing a change to an option. Possible values:

          * ``RequiresIndexDocuments`` : the option's latest value will not be deployed until
          IndexDocuments has been called and indexing is complete.

          * ``Processing`` : the option's latest value is in the process of being activated.

          * ``Active`` : the option's latest value is completely deployed.

          * ``FailedToValidate`` : the option value is not compatible with the domain's data and
          cannot be used to index the data. You must either modify the option value or update or
          remove the incompatible documents.

        - **PendingDeletion** *(boolean) --*

          Indicates that the option will be deleted once processing is complete.
    """


_ClientDescribeDomainEndpointOptionsResponseDomainEndpointOptionsOptionsTypeDef = TypedDict(
    "_ClientDescribeDomainEndpointOptionsResponseDomainEndpointOptionsOptionsTypeDef",
    {"EnforceHTTPS": bool, "TLSSecurityPolicy": str},
    total=False,
)


class ClientDescribeDomainEndpointOptionsResponseDomainEndpointOptionsOptionsTypeDef(
    _ClientDescribeDomainEndpointOptionsResponseDomainEndpointOptionsOptionsTypeDef
):
    """
    Type definition for `ClientDescribeDomainEndpointOptionsResponseDomainEndpointOptions` `Options`

    The domain endpoint options configured for the domain.

    - **EnforceHTTPS** *(boolean) --*

      Whether the domain is HTTPS only enabled.

    - **TLSSecurityPolicy** *(string) --*

      The minimum required TLS version
    """


_ClientDescribeDomainEndpointOptionsResponseDomainEndpointOptionsStatusTypeDef = TypedDict(
    "_ClientDescribeDomainEndpointOptionsResponseDomainEndpointOptionsStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": str,
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientDescribeDomainEndpointOptionsResponseDomainEndpointOptionsStatusTypeDef(
    _ClientDescribeDomainEndpointOptionsResponseDomainEndpointOptionsStatusTypeDef
):
    """
    Type definition for `ClientDescribeDomainEndpointOptionsResponseDomainEndpointOptions` `Status`

    The status of the configured domain endpoint options.

    - **CreationDate** *(datetime) --*

      A timestamp for when this option was created.

    - **UpdateDate** *(datetime) --*

      A timestamp for when this option was last updated.

    - **UpdateVersion** *(integer) --*

      A unique integer that indicates when this option was last updated.

    - **State** *(string) --*

      The state of processing a change to an option. Possible values:

      * ``RequiresIndexDocuments`` : the option's latest value will not be deployed until
      IndexDocuments has been called and indexing is complete.

      * ``Processing`` : the option's latest value is in the process of being activated.

      * ``Active`` : the option's latest value is completely deployed.

      * ``FailedToValidate`` : the option value is not compatible with the domain's data and
      cannot be used to index the data. You must either modify the option value or update or
      remove the incompatible documents.

    - **PendingDeletion** *(boolean) --*

      Indicates that the option will be deleted once processing is complete.
    """


_ClientDescribeDomainEndpointOptionsResponseDomainEndpointOptionsTypeDef = TypedDict(
    "_ClientDescribeDomainEndpointOptionsResponseDomainEndpointOptionsTypeDef",
    {
        "Options": ClientDescribeDomainEndpointOptionsResponseDomainEndpointOptionsOptionsTypeDef,
        "Status": ClientDescribeDomainEndpointOptionsResponseDomainEndpointOptionsStatusTypeDef,
    },
    total=False,
)


class ClientDescribeDomainEndpointOptionsResponseDomainEndpointOptionsTypeDef(
    _ClientDescribeDomainEndpointOptionsResponseDomainEndpointOptionsTypeDef
):
    """
    Type definition for `ClientDescribeDomainEndpointOptionsResponse` `DomainEndpointOptions`

    The status and configuration of a search domain's endpoint options.

    - **Options** *(dict) --*

      The domain endpoint options configured for the domain.

      - **EnforceHTTPS** *(boolean) --*

        Whether the domain is HTTPS only enabled.

      - **TLSSecurityPolicy** *(string) --*

        The minimum required TLS version

    - **Status** *(dict) --*

      The status of the configured domain endpoint options.

      - **CreationDate** *(datetime) --*

        A timestamp for when this option was created.

      - **UpdateDate** *(datetime) --*

        A timestamp for when this option was last updated.

      - **UpdateVersion** *(integer) --*

        A unique integer that indicates when this option was last updated.

      - **State** *(string) --*

        The state of processing a change to an option. Possible values:

        * ``RequiresIndexDocuments`` : the option's latest value will not be deployed until
        IndexDocuments has been called and indexing is complete.

        * ``Processing`` : the option's latest value is in the process of being activated.

        * ``Active`` : the option's latest value is completely deployed.

        * ``FailedToValidate`` : the option value is not compatible with the domain's data and
        cannot be used to index the data. You must either modify the option value or update or
        remove the incompatible documents.

      - **PendingDeletion** *(boolean) --*

        Indicates that the option will be deleted once processing is complete.
    """


_ClientDescribeDomainEndpointOptionsResponseTypeDef = TypedDict(
    "_ClientDescribeDomainEndpointOptionsResponseTypeDef",
    {
        "DomainEndpointOptions": ClientDescribeDomainEndpointOptionsResponseDomainEndpointOptionsTypeDef
    },
    total=False,
)


class ClientDescribeDomainEndpointOptionsResponseTypeDef(
    _ClientDescribeDomainEndpointOptionsResponseTypeDef
):
    """
    Type definition for `ClientDescribeDomainEndpointOptions` `Response`

    The result of a ``DescribeDomainEndpointOptions`` request. Contains the status and
    configuration of a search domain's endpoint options.

    - **DomainEndpointOptions** *(dict) --*

      The status and configuration of a search domain's endpoint options.

      - **Options** *(dict) --*

        The domain endpoint options configured for the domain.

        - **EnforceHTTPS** *(boolean) --*

          Whether the domain is HTTPS only enabled.

        - **TLSSecurityPolicy** *(string) --*

          The minimum required TLS version

      - **Status** *(dict) --*

        The status of the configured domain endpoint options.

        - **CreationDate** *(datetime) --*

          A timestamp for when this option was created.

        - **UpdateDate** *(datetime) --*

          A timestamp for when this option was last updated.

        - **UpdateVersion** *(integer) --*

          A unique integer that indicates when this option was last updated.

        - **State** *(string) --*

          The state of processing a change to an option. Possible values:

          * ``RequiresIndexDocuments`` : the option's latest value will not be deployed until
          IndexDocuments has been called and indexing is complete.

          * ``Processing`` : the option's latest value is in the process of being activated.

          * ``Active`` : the option's latest value is completely deployed.

          * ``FailedToValidate`` : the option value is not compatible with the domain's data and
          cannot be used to index the data. You must either modify the option value or update or
          remove the incompatible documents.

        - **PendingDeletion** *(boolean) --*

          Indicates that the option will be deleted once processing is complete.
    """


_ClientDescribeDomainsResponseDomainStatusListDocServiceTypeDef = TypedDict(
    "_ClientDescribeDomainsResponseDomainStatusListDocServiceTypeDef",
    {"Endpoint": str},
    total=False,
)


class ClientDescribeDomainsResponseDomainStatusListDocServiceTypeDef(
    _ClientDescribeDomainsResponseDomainStatusListDocServiceTypeDef
):
    """
    Type definition for `ClientDescribeDomainsResponseDomainStatusList` `DocService`

    The service endpoint for updating documents in a search domain.

    - **Endpoint** *(string) --*

      The endpoint to which service requests can be submitted. For example,
      ``search-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.cloudsearch.amazonaws.com``
      or ``doc-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.cloudsearch.amazonaws.com`` .
    """


_ClientDescribeDomainsResponseDomainStatusListLimitsTypeDef = TypedDict(
    "_ClientDescribeDomainsResponseDomainStatusListLimitsTypeDef",
    {"MaximumReplicationCount": int, "MaximumPartitionCount": int},
    total=False,
)


class ClientDescribeDomainsResponseDomainStatusListLimitsTypeDef(
    _ClientDescribeDomainsResponseDomainStatusListLimitsTypeDef
):
    """
    Type definition for `ClientDescribeDomainsResponseDomainStatusList` `Limits`

    - **MaximumReplicationCount** *(integer) --*

    - **MaximumPartitionCount** *(integer) --*
    """


_ClientDescribeDomainsResponseDomainStatusListSearchServiceTypeDef = TypedDict(
    "_ClientDescribeDomainsResponseDomainStatusListSearchServiceTypeDef",
    {"Endpoint": str},
    total=False,
)


class ClientDescribeDomainsResponseDomainStatusListSearchServiceTypeDef(
    _ClientDescribeDomainsResponseDomainStatusListSearchServiceTypeDef
):
    """
    Type definition for `ClientDescribeDomainsResponseDomainStatusList` `SearchService`

    The service endpoint for requesting search results from a search domain.

    - **Endpoint** *(string) --*

      The endpoint to which service requests can be submitted. For example,
      ``search-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.cloudsearch.amazonaws.com``
      or ``doc-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.cloudsearch.amazonaws.com`` .
    """


_ClientDescribeDomainsResponseDomainStatusListTypeDef = TypedDict(
    "_ClientDescribeDomainsResponseDomainStatusListTypeDef",
    {
        "DomainId": str,
        "DomainName": str,
        "ARN": str,
        "Created": bool,
        "Deleted": bool,
        "DocService": ClientDescribeDomainsResponseDomainStatusListDocServiceTypeDef,
        "SearchService": ClientDescribeDomainsResponseDomainStatusListSearchServiceTypeDef,
        "RequiresIndexDocuments": bool,
        "Processing": bool,
        "SearchInstanceType": str,
        "SearchPartitionCount": int,
        "SearchInstanceCount": int,
        "Limits": ClientDescribeDomainsResponseDomainStatusListLimitsTypeDef,
    },
    total=False,
)


class ClientDescribeDomainsResponseDomainStatusListTypeDef(
    _ClientDescribeDomainsResponseDomainStatusListTypeDef
):
    """
    Type definition for `ClientDescribeDomainsResponse` `DomainStatusList`

    The current status of the search domain.

    - **DomainId** *(string) --*

      An internally generated unique identifier for a domain.

    - **DomainName** *(string) --*

      A string that represents the name of a domain. Domain names are unique across the domains
      owned by an account within an AWS region. Domain names start with a letter or number and
      can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).

    - **ARN** *(string) --*

      The Amazon Resource Name (ARN) of the search domain. See `Identifiers for IAM Entities
      <http://docs.aws.amazon.com/IAM/latest/UserGuide/index.html?Using_Identifiers.html>`__ in
      *Using AWS Identity and Access Management* for more information.

    - **Created** *(boolean) --*

      True if the search domain is created. It can take several minutes to initialize a domain
      when  CreateDomain is called. Newly created search domains are returned from
      DescribeDomains with a false value for Created until domain creation is complete.

    - **Deleted** *(boolean) --*

      True if the search domain has been deleted. The system must clean up resources dedicated
      to the search domain when  DeleteDomain is called. Newly deleted search domains are
      returned from  DescribeDomains with a true value for IsDeleted for several minutes until
      resource cleanup is complete.

    - **DocService** *(dict) --*

      The service endpoint for updating documents in a search domain.

      - **Endpoint** *(string) --*

        The endpoint to which service requests can be submitted. For example,
        ``search-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.cloudsearch.amazonaws.com``
        or ``doc-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.cloudsearch.amazonaws.com`` .

    - **SearchService** *(dict) --*

      The service endpoint for requesting search results from a search domain.

      - **Endpoint** *(string) --*

        The endpoint to which service requests can be submitted. For example,
        ``search-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.cloudsearch.amazonaws.com``
        or ``doc-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.cloudsearch.amazonaws.com`` .

    - **RequiresIndexDocuments** *(boolean) --*

      True if  IndexDocuments needs to be called to activate the current domain configuration.

    - **Processing** *(boolean) --*

      True if processing is being done to activate the current domain configuration.

    - **SearchInstanceType** *(string) --*

      The instance type that is being used to process search requests.

    - **SearchPartitionCount** *(integer) --*

      The number of partitions across which the search index is spread.

    - **SearchInstanceCount** *(integer) --*

      The number of search instances that are available to process search requests.

    - **Limits** *(dict) --*

      - **MaximumReplicationCount** *(integer) --*

      - **MaximumPartitionCount** *(integer) --*
    """


_ClientDescribeDomainsResponseTypeDef = TypedDict(
    "_ClientDescribeDomainsResponseTypeDef",
    {"DomainStatusList": List[ClientDescribeDomainsResponseDomainStatusListTypeDef]},
    total=False,
)


class ClientDescribeDomainsResponseTypeDef(_ClientDescribeDomainsResponseTypeDef):
    """
    Type definition for `ClientDescribeDomains` `Response`

    The result of a ``DescribeDomains`` request. Contains the status of the domains specified in
    the request or all domains owned by the account.

    - **DomainStatusList** *(list) --*

      A list that contains the status of each requested domain.

      - *(dict) --*

        The current status of the search domain.

        - **DomainId** *(string) --*

          An internally generated unique identifier for a domain.

        - **DomainName** *(string) --*

          A string that represents the name of a domain. Domain names are unique across the domains
          owned by an account within an AWS region. Domain names start with a letter or number and
          can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).

        - **ARN** *(string) --*

          The Amazon Resource Name (ARN) of the search domain. See `Identifiers for IAM Entities
          <http://docs.aws.amazon.com/IAM/latest/UserGuide/index.html?Using_Identifiers.html>`__ in
          *Using AWS Identity and Access Management* for more information.

        - **Created** *(boolean) --*

          True if the search domain is created. It can take several minutes to initialize a domain
          when  CreateDomain is called. Newly created search domains are returned from
          DescribeDomains with a false value for Created until domain creation is complete.

        - **Deleted** *(boolean) --*

          True if the search domain has been deleted. The system must clean up resources dedicated
          to the search domain when  DeleteDomain is called. Newly deleted search domains are
          returned from  DescribeDomains with a true value for IsDeleted for several minutes until
          resource cleanup is complete.

        - **DocService** *(dict) --*

          The service endpoint for updating documents in a search domain.

          - **Endpoint** *(string) --*

            The endpoint to which service requests can be submitted. For example,
            ``search-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.cloudsearch.amazonaws.com``
            or ``doc-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.cloudsearch.amazonaws.com`` .

        - **SearchService** *(dict) --*

          The service endpoint for requesting search results from a search domain.

          - **Endpoint** *(string) --*

            The endpoint to which service requests can be submitted. For example,
            ``search-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.cloudsearch.amazonaws.com``
            or ``doc-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.cloudsearch.amazonaws.com`` .

        - **RequiresIndexDocuments** *(boolean) --*

          True if  IndexDocuments needs to be called to activate the current domain configuration.

        - **Processing** *(boolean) --*

          True if processing is being done to activate the current domain configuration.

        - **SearchInstanceType** *(string) --*

          The instance type that is being used to process search requests.

        - **SearchPartitionCount** *(integer) --*

          The number of partitions across which the search index is spread.

        - **SearchInstanceCount** *(integer) --*

          The number of search instances that are available to process search requests.

        - **Limits** *(dict) --*

          - **MaximumReplicationCount** *(integer) --*

          - **MaximumPartitionCount** *(integer) --*
    """


_ClientDescribeExpressionsResponseExpressionsOptionsTypeDef = TypedDict(
    "_ClientDescribeExpressionsResponseExpressionsOptionsTypeDef",
    {"ExpressionName": str, "ExpressionValue": str},
    total=False,
)


class ClientDescribeExpressionsResponseExpressionsOptionsTypeDef(
    _ClientDescribeExpressionsResponseExpressionsOptionsTypeDef
):
    """
    Type definition for `ClientDescribeExpressionsResponseExpressions` `Options`

    The expression that is evaluated for sorting while processing a search request.

    - **ExpressionName** *(string) --*

      Names must begin with a letter and can contain the following characters: a-z
      (lowercase), 0-9, and _ (underscore).

    - **ExpressionValue** *(string) --*

      The expression to evaluate for sorting while processing a search request. The
      ``Expression`` syntax is based on JavaScript expressions. For more information, see
      `Configuring Expressions
      <http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-expressions.html>`__
      in the *Amazon CloudSearch Developer Guide* .
    """


_ClientDescribeExpressionsResponseExpressionsStatusTypeDef = TypedDict(
    "_ClientDescribeExpressionsResponseExpressionsStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": str,
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientDescribeExpressionsResponseExpressionsStatusTypeDef(
    _ClientDescribeExpressionsResponseExpressionsStatusTypeDef
):
    """
    Type definition for `ClientDescribeExpressionsResponseExpressions` `Status`

    The status of domain configuration option.

    - **CreationDate** *(datetime) --*

      A timestamp for when this option was created.

    - **UpdateDate** *(datetime) --*

      A timestamp for when this option was last updated.

    - **UpdateVersion** *(integer) --*

      A unique integer that indicates when this option was last updated.

    - **State** *(string) --*

      The state of processing a change to an option. Possible values:

      * ``RequiresIndexDocuments`` : the option's latest value will not be deployed until
      IndexDocuments has been called and indexing is complete.

      * ``Processing`` : the option's latest value is in the process of being activated.

      * ``Active`` : the option's latest value is completely deployed.

      * ``FailedToValidate`` : the option value is not compatible with the domain's data and
      cannot be used to index the data. You must either modify the option value or update or
      remove the incompatible documents.

    - **PendingDeletion** *(boolean) --*

      Indicates that the option will be deleted once processing is complete.
    """


_ClientDescribeExpressionsResponseExpressionsTypeDef = TypedDict(
    "_ClientDescribeExpressionsResponseExpressionsTypeDef",
    {
        "Options": ClientDescribeExpressionsResponseExpressionsOptionsTypeDef,
        "Status": ClientDescribeExpressionsResponseExpressionsStatusTypeDef,
    },
    total=False,
)


class ClientDescribeExpressionsResponseExpressionsTypeDef(
    _ClientDescribeExpressionsResponseExpressionsTypeDef
):
    """
    Type definition for `ClientDescribeExpressionsResponse` `Expressions`

    The value of an ``Expression`` and its current status.

    - **Options** *(dict) --*

      The expression that is evaluated for sorting while processing a search request.

      - **ExpressionName** *(string) --*

        Names must begin with a letter and can contain the following characters: a-z
        (lowercase), 0-9, and _ (underscore).

      - **ExpressionValue** *(string) --*

        The expression to evaluate for sorting while processing a search request. The
        ``Expression`` syntax is based on JavaScript expressions. For more information, see
        `Configuring Expressions
        <http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-expressions.html>`__
        in the *Amazon CloudSearch Developer Guide* .

    - **Status** *(dict) --*

      The status of domain configuration option.

      - **CreationDate** *(datetime) --*

        A timestamp for when this option was created.

      - **UpdateDate** *(datetime) --*

        A timestamp for when this option was last updated.

      - **UpdateVersion** *(integer) --*

        A unique integer that indicates when this option was last updated.

      - **State** *(string) --*

        The state of processing a change to an option. Possible values:

        * ``RequiresIndexDocuments`` : the option's latest value will not be deployed until
        IndexDocuments has been called and indexing is complete.

        * ``Processing`` : the option's latest value is in the process of being activated.

        * ``Active`` : the option's latest value is completely deployed.

        * ``FailedToValidate`` : the option value is not compatible with the domain's data and
        cannot be used to index the data. You must either modify the option value or update or
        remove the incompatible documents.

      - **PendingDeletion** *(boolean) --*

        Indicates that the option will be deleted once processing is complete.
    """


_ClientDescribeExpressionsResponseTypeDef = TypedDict(
    "_ClientDescribeExpressionsResponseTypeDef",
    {"Expressions": List[ClientDescribeExpressionsResponseExpressionsTypeDef]},
    total=False,
)


class ClientDescribeExpressionsResponseTypeDef(
    _ClientDescribeExpressionsResponseTypeDef
):
    """
    Type definition for `ClientDescribeExpressions` `Response`

    The result of a ``DescribeExpressions`` request. Contains the expressions configured for the
    domain specified in the request.

    - **Expressions** *(list) --*

      The expressions configured for the domain.

      - *(dict) --*

        The value of an ``Expression`` and its current status.

        - **Options** *(dict) --*

          The expression that is evaluated for sorting while processing a search request.

          - **ExpressionName** *(string) --*

            Names must begin with a letter and can contain the following characters: a-z
            (lowercase), 0-9, and _ (underscore).

          - **ExpressionValue** *(string) --*

            The expression to evaluate for sorting while processing a search request. The
            ``Expression`` syntax is based on JavaScript expressions. For more information, see
            `Configuring Expressions
            <http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-expressions.html>`__
            in the *Amazon CloudSearch Developer Guide* .

        - **Status** *(dict) --*

          The status of domain configuration option.

          - **CreationDate** *(datetime) --*

            A timestamp for when this option was created.

          - **UpdateDate** *(datetime) --*

            A timestamp for when this option was last updated.

          - **UpdateVersion** *(integer) --*

            A unique integer that indicates when this option was last updated.

          - **State** *(string) --*

            The state of processing a change to an option. Possible values:

            * ``RequiresIndexDocuments`` : the option's latest value will not be deployed until
            IndexDocuments has been called and indexing is complete.

            * ``Processing`` : the option's latest value is in the process of being activated.

            * ``Active`` : the option's latest value is completely deployed.

            * ``FailedToValidate`` : the option value is not compatible with the domain's data and
            cannot be used to index the data. You must either modify the option value or update or
            remove the incompatible documents.

          - **PendingDeletion** *(boolean) --*

            Indicates that the option will be deleted once processing is complete.
    """


_ClientDescribeIndexFieldsResponseIndexFieldsOptionsDateArrayOptionsTypeDef = TypedDict(
    "_ClientDescribeIndexFieldsResponseIndexFieldsOptionsDateArrayOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceFields": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
    },
    total=False,
)


class ClientDescribeIndexFieldsResponseIndexFieldsOptionsDateArrayOptionsTypeDef(
    _ClientDescribeIndexFieldsResponseIndexFieldsOptionsDateArrayOptionsTypeDef
):
    """
    Type definition for `ClientDescribeIndexFieldsResponseIndexFieldsOptions` `DateArrayOptions`

    Options for a field that contains an array of dates. Present if ``IndexFieldType``
    specifies the field is of type ``date-array`` . All options are enabled by default.

    - **DefaultValue** *(string) --* A value to use for the field if the field isn't
    specified for a document.

    - **SourceFields** *(string) --*

      A list of source fields to map to the field.

    - **FacetEnabled** *(boolean) --*

      Whether facet information can be returned for the field.

    - **SearchEnabled** *(boolean) --*

      Whether the contents of the field are searchable.

    - **ReturnEnabled** *(boolean) --*

      Whether the contents of the field can be returned in the search results.
    """


_ClientDescribeIndexFieldsResponseIndexFieldsOptionsDateOptionsTypeDef = TypedDict(
    "_ClientDescribeIndexFieldsResponseIndexFieldsOptionsDateOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)


class ClientDescribeIndexFieldsResponseIndexFieldsOptionsDateOptionsTypeDef(
    _ClientDescribeIndexFieldsResponseIndexFieldsOptionsDateOptionsTypeDef
):
    """
    Type definition for `ClientDescribeIndexFieldsResponseIndexFieldsOptions` `DateOptions`

    Options for a date field. Dates and times are specified in UTC (Coordinated Universal
    Time) according to IETF RFC3339: yyyy-mm-ddT00:00:00Z. Present if ``IndexFieldType``
    specifies the field is of type ``date`` . All options are enabled by default.

    - **DefaultValue** *(string) --* A value to use for the field if the field isn't
    specified for a document.

    - **SourceField** *(string) --*

      A string that represents the name of an index field. CloudSearch supports regular
      index fields as well as dynamic fields. A dynamic field's name defines a pattern that
      begins or ends with a wildcard. Any document fields that don't map to a regular index
      field but do match a dynamic field's pattern are configured with the dynamic field's
      indexing options.

      Regular field names begin with a letter and can contain the following characters: a-z
      (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a
      wildcard (*). The wildcard can also be the only character in a dynamic field name.
      Multiple wildcards, and wildcards embedded within a string are not supported.

      The name ``score`` is reserved and cannot be used as a field name. To reference a
      document's ID, you can use the name ``_id`` .

    - **FacetEnabled** *(boolean) --*

      Whether facet information can be returned for the field.

    - **SearchEnabled** *(boolean) --*

      Whether the contents of the field are searchable.

    - **ReturnEnabled** *(boolean) --*

      Whether the contents of the field can be returned in the search results.

    - **SortEnabled** *(boolean) --*

      Whether the field can be used to sort the search results.
    """


_ClientDescribeIndexFieldsResponseIndexFieldsOptionsDoubleArrayOptionsTypeDef = TypedDict(
    "_ClientDescribeIndexFieldsResponseIndexFieldsOptionsDoubleArrayOptionsTypeDef",
    {
        "DefaultValue": float,
        "SourceFields": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
    },
    total=False,
)


class ClientDescribeIndexFieldsResponseIndexFieldsOptionsDoubleArrayOptionsTypeDef(
    _ClientDescribeIndexFieldsResponseIndexFieldsOptionsDoubleArrayOptionsTypeDef
):
    """
    Type definition for `ClientDescribeIndexFieldsResponseIndexFieldsOptions` `DoubleArrayOptions`

    Options for a field that contains an array of double-precision 64-bit floating point
    values. Present if ``IndexFieldType`` specifies the field is of type ``double-array`` .
    All options are enabled by default.

    - **DefaultValue** *(float) --* A value to use for the field if the field isn't
    specified for a document.

    - **SourceFields** *(string) --*

      A list of source fields to map to the field.

    - **FacetEnabled** *(boolean) --*

      Whether facet information can be returned for the field.

    - **SearchEnabled** *(boolean) --*

      Whether the contents of the field are searchable.

    - **ReturnEnabled** *(boolean) --*

      Whether the contents of the field can be returned in the search results.
    """


_ClientDescribeIndexFieldsResponseIndexFieldsOptionsDoubleOptionsTypeDef = TypedDict(
    "_ClientDescribeIndexFieldsResponseIndexFieldsOptionsDoubleOptionsTypeDef",
    {
        "DefaultValue": float,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)


class ClientDescribeIndexFieldsResponseIndexFieldsOptionsDoubleOptionsTypeDef(
    _ClientDescribeIndexFieldsResponseIndexFieldsOptionsDoubleOptionsTypeDef
):
    """
    Type definition for `ClientDescribeIndexFieldsResponseIndexFieldsOptions` `DoubleOptions`

    Options for a double-precision 64-bit floating point field. Present if
    ``IndexFieldType`` specifies the field is of type ``double`` . All options are enabled
    by default.

    - **DefaultValue** *(float) --*

      A value to use for the field if the field isn't specified for a document. This can be
      important if you are using the field in an expression and that field is not present
      in every document.

    - **SourceField** *(string) --*

      The name of the source field to map to the field.

    - **FacetEnabled** *(boolean) --*

      Whether facet information can be returned for the field.

    - **SearchEnabled** *(boolean) --*

      Whether the contents of the field are searchable.

    - **ReturnEnabled** *(boolean) --*

      Whether the contents of the field can be returned in the search results.

    - **SortEnabled** *(boolean) --*

      Whether the field can be used to sort the search results.
    """


_ClientDescribeIndexFieldsResponseIndexFieldsOptionsIntArrayOptionsTypeDef = TypedDict(
    "_ClientDescribeIndexFieldsResponseIndexFieldsOptionsIntArrayOptionsTypeDef",
    {
        "DefaultValue": int,
        "SourceFields": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
    },
    total=False,
)


class ClientDescribeIndexFieldsResponseIndexFieldsOptionsIntArrayOptionsTypeDef(
    _ClientDescribeIndexFieldsResponseIndexFieldsOptionsIntArrayOptionsTypeDef
):
    """
    Type definition for `ClientDescribeIndexFieldsResponseIndexFieldsOptions` `IntArrayOptions`

    Options for a field that contains an array of 64-bit signed integers. Present if
    ``IndexFieldType`` specifies the field is of type ``int-array`` . All options are
    enabled by default.

    - **DefaultValue** *(integer) --* A value to use for the field if the field isn't
    specified for a document.

    - **SourceFields** *(string) --*

      A list of source fields to map to the field.

    - **FacetEnabled** *(boolean) --*

      Whether facet information can be returned for the field.

    - **SearchEnabled** *(boolean) --*

      Whether the contents of the field are searchable.

    - **ReturnEnabled** *(boolean) --*

      Whether the contents of the field can be returned in the search results.
    """


_ClientDescribeIndexFieldsResponseIndexFieldsOptionsIntOptionsTypeDef = TypedDict(
    "_ClientDescribeIndexFieldsResponseIndexFieldsOptionsIntOptionsTypeDef",
    {
        "DefaultValue": int,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)


class ClientDescribeIndexFieldsResponseIndexFieldsOptionsIntOptionsTypeDef(
    _ClientDescribeIndexFieldsResponseIndexFieldsOptionsIntOptionsTypeDef
):
    """
    Type definition for `ClientDescribeIndexFieldsResponseIndexFieldsOptions` `IntOptions`

    Options for a 64-bit signed integer field. Present if ``IndexFieldType`` specifies the
    field is of type ``int`` . All options are enabled by default.

    - **DefaultValue** *(integer) --* A value to use for the field if the field isn't
    specified for a document. This can be important if you are using the field in an
    expression and that field is not present in every document.

    - **SourceField** *(string) --*

      The name of the source field to map to the field.

    - **FacetEnabled** *(boolean) --*

      Whether facet information can be returned for the field.

    - **SearchEnabled** *(boolean) --*

      Whether the contents of the field are searchable.

    - **ReturnEnabled** *(boolean) --*

      Whether the contents of the field can be returned in the search results.

    - **SortEnabled** *(boolean) --*

      Whether the field can be used to sort the search results.
    """


_ClientDescribeIndexFieldsResponseIndexFieldsOptionsLatLonOptionsTypeDef = TypedDict(
    "_ClientDescribeIndexFieldsResponseIndexFieldsOptionsLatLonOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)


class ClientDescribeIndexFieldsResponseIndexFieldsOptionsLatLonOptionsTypeDef(
    _ClientDescribeIndexFieldsResponseIndexFieldsOptionsLatLonOptionsTypeDef
):
    """
    Type definition for `ClientDescribeIndexFieldsResponseIndexFieldsOptions` `LatLonOptions`

    Options for a latlon field. A latlon field contains a location stored as a latitude and
    longitude value pair. Present if ``IndexFieldType`` specifies the field is of type
    ``latlon`` . All options are enabled by default.

    - **DefaultValue** *(string) --* A value to use for the field if the field isn't
    specified for a document.

    - **SourceField** *(string) --*

      A string that represents the name of an index field. CloudSearch supports regular
      index fields as well as dynamic fields. A dynamic field's name defines a pattern that
      begins or ends with a wildcard. Any document fields that don't map to a regular index
      field but do match a dynamic field's pattern are configured with the dynamic field's
      indexing options.

      Regular field names begin with a letter and can contain the following characters: a-z
      (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a
      wildcard (*). The wildcard can also be the only character in a dynamic field name.
      Multiple wildcards, and wildcards embedded within a string are not supported.

      The name ``score`` is reserved and cannot be used as a field name. To reference a
      document's ID, you can use the name ``_id`` .

    - **FacetEnabled** *(boolean) --*

      Whether facet information can be returned for the field.

    - **SearchEnabled** *(boolean) --*

      Whether the contents of the field are searchable.

    - **ReturnEnabled** *(boolean) --*

      Whether the contents of the field can be returned in the search results.

    - **SortEnabled** *(boolean) --*

      Whether the field can be used to sort the search results.
    """


_ClientDescribeIndexFieldsResponseIndexFieldsOptionsLiteralArrayOptionsTypeDef = TypedDict(
    "_ClientDescribeIndexFieldsResponseIndexFieldsOptionsLiteralArrayOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceFields": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
    },
    total=False,
)


class ClientDescribeIndexFieldsResponseIndexFieldsOptionsLiteralArrayOptionsTypeDef(
    _ClientDescribeIndexFieldsResponseIndexFieldsOptionsLiteralArrayOptionsTypeDef
):
    """
    Type definition for `ClientDescribeIndexFieldsResponseIndexFieldsOptions` `LiteralArrayOptions`

    Options for a field that contains an array of literal strings. Present if
    ``IndexFieldType`` specifies the field is of type ``literal-array`` . All options are
    enabled by default.

    - **DefaultValue** *(string) --* A value to use for the field if the field isn't
    specified for a document.

    - **SourceFields** *(string) --*

      A list of source fields to map to the field.

    - **FacetEnabled** *(boolean) --*

      Whether facet information can be returned for the field.

    - **SearchEnabled** *(boolean) --*

      Whether the contents of the field are searchable.

    - **ReturnEnabled** *(boolean) --*

      Whether the contents of the field can be returned in the search results.
    """


_ClientDescribeIndexFieldsResponseIndexFieldsOptionsLiteralOptionsTypeDef = TypedDict(
    "_ClientDescribeIndexFieldsResponseIndexFieldsOptionsLiteralOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)


class ClientDescribeIndexFieldsResponseIndexFieldsOptionsLiteralOptionsTypeDef(
    _ClientDescribeIndexFieldsResponseIndexFieldsOptionsLiteralOptionsTypeDef
):
    """
    Type definition for `ClientDescribeIndexFieldsResponseIndexFieldsOptions` `LiteralOptions`

    Options for literal field. Present if ``IndexFieldType`` specifies the field is of type
    ``literal`` . All options are enabled by default.

    - **DefaultValue** *(string) --* A value to use for the field if the field isn't
    specified for a document.

    - **SourceField** *(string) --*

      A string that represents the name of an index field. CloudSearch supports regular
      index fields as well as dynamic fields. A dynamic field's name defines a pattern that
      begins or ends with a wildcard. Any document fields that don't map to a regular index
      field but do match a dynamic field's pattern are configured with the dynamic field's
      indexing options.

      Regular field names begin with a letter and can contain the following characters: a-z
      (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a
      wildcard (*). The wildcard can also be the only character in a dynamic field name.
      Multiple wildcards, and wildcards embedded within a string are not supported.

      The name ``score`` is reserved and cannot be used as a field name. To reference a
      document's ID, you can use the name ``_id`` .

    - **FacetEnabled** *(boolean) --*

      Whether facet information can be returned for the field.

    - **SearchEnabled** *(boolean) --*

      Whether the contents of the field are searchable.

    - **ReturnEnabled** *(boolean) --*

      Whether the contents of the field can be returned in the search results.

    - **SortEnabled** *(boolean) --*

      Whether the field can be used to sort the search results.
    """


_ClientDescribeIndexFieldsResponseIndexFieldsOptionsTextArrayOptionsTypeDef = TypedDict(
    "_ClientDescribeIndexFieldsResponseIndexFieldsOptionsTextArrayOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceFields": str,
        "ReturnEnabled": bool,
        "HighlightEnabled": bool,
        "AnalysisScheme": str,
    },
    total=False,
)


class ClientDescribeIndexFieldsResponseIndexFieldsOptionsTextArrayOptionsTypeDef(
    _ClientDescribeIndexFieldsResponseIndexFieldsOptionsTextArrayOptionsTypeDef
):
    """
    Type definition for `ClientDescribeIndexFieldsResponseIndexFieldsOptions` `TextArrayOptions`

    Options for a field that contains an array of text strings. Present if
    ``IndexFieldType`` specifies the field is of type ``text-array`` . A ``text-array``
    field is always searchable. All options are enabled by default.

    - **DefaultValue** *(string) --* A value to use for the field if the field isn't
    specified for a document.

    - **SourceFields** *(string) --*

      A list of source fields to map to the field.

    - **ReturnEnabled** *(boolean) --*

      Whether the contents of the field can be returned in the search results.

    - **HighlightEnabled** *(boolean) --*

      Whether highlights can be returned for the field.

    - **AnalysisScheme** *(string) --*

      The name of an analysis scheme for a ``text-array`` field.
    """


_ClientDescribeIndexFieldsResponseIndexFieldsOptionsTextOptionsTypeDef = TypedDict(
    "_ClientDescribeIndexFieldsResponseIndexFieldsOptionsTextOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceField": str,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
        "HighlightEnabled": bool,
        "AnalysisScheme": str,
    },
    total=False,
)


class ClientDescribeIndexFieldsResponseIndexFieldsOptionsTextOptionsTypeDef(
    _ClientDescribeIndexFieldsResponseIndexFieldsOptionsTextOptionsTypeDef
):
    """
    Type definition for `ClientDescribeIndexFieldsResponseIndexFieldsOptions` `TextOptions`

    Options for text field. Present if ``IndexFieldType`` specifies the field is of type
    ``text`` . A ``text`` field is always searchable. All options are enabled by default.

    - **DefaultValue** *(string) --* A value to use for the field if the field isn't
    specified for a document.

    - **SourceField** *(string) --*

      A string that represents the name of an index field. CloudSearch supports regular
      index fields as well as dynamic fields. A dynamic field's name defines a pattern that
      begins or ends with a wildcard. Any document fields that don't map to a regular index
      field but do match a dynamic field's pattern are configured with the dynamic field's
      indexing options.

      Regular field names begin with a letter and can contain the following characters: a-z
      (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a
      wildcard (*). The wildcard can also be the only character in a dynamic field name.
      Multiple wildcards, and wildcards embedded within a string are not supported.

      The name ``score`` is reserved and cannot be used as a field name. To reference a
      document's ID, you can use the name ``_id`` .

    - **ReturnEnabled** *(boolean) --*

      Whether the contents of the field can be returned in the search results.

    - **SortEnabled** *(boolean) --*

      Whether the field can be used to sort the search results.

    - **HighlightEnabled** *(boolean) --*

      Whether highlights can be returned for the field.

    - **AnalysisScheme** *(string) --*

      The name of an analysis scheme for a ``text`` field.
    """


_ClientDescribeIndexFieldsResponseIndexFieldsOptionsTypeDef = TypedDict(
    "_ClientDescribeIndexFieldsResponseIndexFieldsOptionsTypeDef",
    {
        "IndexFieldName": str,
        "IndexFieldType": str,
        "IntOptions": ClientDescribeIndexFieldsResponseIndexFieldsOptionsIntOptionsTypeDef,
        "DoubleOptions": ClientDescribeIndexFieldsResponseIndexFieldsOptionsDoubleOptionsTypeDef,
        "LiteralOptions": ClientDescribeIndexFieldsResponseIndexFieldsOptionsLiteralOptionsTypeDef,
        "TextOptions": ClientDescribeIndexFieldsResponseIndexFieldsOptionsTextOptionsTypeDef,
        "DateOptions": ClientDescribeIndexFieldsResponseIndexFieldsOptionsDateOptionsTypeDef,
        "LatLonOptions": ClientDescribeIndexFieldsResponseIndexFieldsOptionsLatLonOptionsTypeDef,
        "IntArrayOptions": ClientDescribeIndexFieldsResponseIndexFieldsOptionsIntArrayOptionsTypeDef,
        "DoubleArrayOptions": ClientDescribeIndexFieldsResponseIndexFieldsOptionsDoubleArrayOptionsTypeDef,
        "LiteralArrayOptions": ClientDescribeIndexFieldsResponseIndexFieldsOptionsLiteralArrayOptionsTypeDef,
        "TextArrayOptions": ClientDescribeIndexFieldsResponseIndexFieldsOptionsTextArrayOptionsTypeDef,
        "DateArrayOptions": ClientDescribeIndexFieldsResponseIndexFieldsOptionsDateArrayOptionsTypeDef,
    },
    total=False,
)


class ClientDescribeIndexFieldsResponseIndexFieldsOptionsTypeDef(
    _ClientDescribeIndexFieldsResponseIndexFieldsOptionsTypeDef
):
    """
    Type definition for `ClientDescribeIndexFieldsResponseIndexFields` `Options`

    Configuration information for a field in the index, including its name, type, and
    options. The supported options depend on the `` IndexFieldType`` .

    - **IndexFieldName** *(string) --*

      A string that represents the name of an index field. CloudSearch supports regular index
      fields as well as dynamic fields. A dynamic field's name defines a pattern that begins
      or ends with a wildcard. Any document fields that don't map to a regular index field
      but do match a dynamic field's pattern are configured with the dynamic field's indexing
      options.

      Regular field names begin with a letter and can contain the following characters: a-z
      (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a
      wildcard (*). The wildcard can also be the only character in a dynamic field name.
      Multiple wildcards, and wildcards embedded within a string are not supported.

      The name ``score`` is reserved and cannot be used as a field name. To reference a
      document's ID, you can use the name ``_id`` .

    - **IndexFieldType** *(string) --*

      The type of field. The valid options for a field depend on the field type. For more
      information about the supported field types, see `Configuring Index Fields
      <http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-index-fields.html>`__
      in the *Amazon CloudSearch Developer Guide* .

    - **IntOptions** *(dict) --*

      Options for a 64-bit signed integer field. Present if ``IndexFieldType`` specifies the
      field is of type ``int`` . All options are enabled by default.

      - **DefaultValue** *(integer) --* A value to use for the field if the field isn't
      specified for a document. This can be important if you are using the field in an
      expression and that field is not present in every document.

      - **SourceField** *(string) --*

        The name of the source field to map to the field.

      - **FacetEnabled** *(boolean) --*

        Whether facet information can be returned for the field.

      - **SearchEnabled** *(boolean) --*

        Whether the contents of the field are searchable.

      - **ReturnEnabled** *(boolean) --*

        Whether the contents of the field can be returned in the search results.

      - **SortEnabled** *(boolean) --*

        Whether the field can be used to sort the search results.

    - **DoubleOptions** *(dict) --*

      Options for a double-precision 64-bit floating point field. Present if
      ``IndexFieldType`` specifies the field is of type ``double`` . All options are enabled
      by default.

      - **DefaultValue** *(float) --*

        A value to use for the field if the field isn't specified for a document. This can be
        important if you are using the field in an expression and that field is not present
        in every document.

      - **SourceField** *(string) --*

        The name of the source field to map to the field.

      - **FacetEnabled** *(boolean) --*

        Whether facet information can be returned for the field.

      - **SearchEnabled** *(boolean) --*

        Whether the contents of the field are searchable.

      - **ReturnEnabled** *(boolean) --*

        Whether the contents of the field can be returned in the search results.

      - **SortEnabled** *(boolean) --*

        Whether the field can be used to sort the search results.

    - **LiteralOptions** *(dict) --*

      Options for literal field. Present if ``IndexFieldType`` specifies the field is of type
      ``literal`` . All options are enabled by default.

      - **DefaultValue** *(string) --* A value to use for the field if the field isn't
      specified for a document.

      - **SourceField** *(string) --*

        A string that represents the name of an index field. CloudSearch supports regular
        index fields as well as dynamic fields. A dynamic field's name defines a pattern that
        begins or ends with a wildcard. Any document fields that don't map to a regular index
        field but do match a dynamic field's pattern are configured with the dynamic field's
        indexing options.

        Regular field names begin with a letter and can contain the following characters: a-z
        (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a
        wildcard (*). The wildcard can also be the only character in a dynamic field name.
        Multiple wildcards, and wildcards embedded within a string are not supported.

        The name ``score`` is reserved and cannot be used as a field name. To reference a
        document's ID, you can use the name ``_id`` .

      - **FacetEnabled** *(boolean) --*

        Whether facet information can be returned for the field.

      - **SearchEnabled** *(boolean) --*

        Whether the contents of the field are searchable.

      - **ReturnEnabled** *(boolean) --*

        Whether the contents of the field can be returned in the search results.

      - **SortEnabled** *(boolean) --*

        Whether the field can be used to sort the search results.

    - **TextOptions** *(dict) --*

      Options for text field. Present if ``IndexFieldType`` specifies the field is of type
      ``text`` . A ``text`` field is always searchable. All options are enabled by default.

      - **DefaultValue** *(string) --* A value to use for the field if the field isn't
      specified for a document.

      - **SourceField** *(string) --*

        A string that represents the name of an index field. CloudSearch supports regular
        index fields as well as dynamic fields. A dynamic field's name defines a pattern that
        begins or ends with a wildcard. Any document fields that don't map to a regular index
        field but do match a dynamic field's pattern are configured with the dynamic field's
        indexing options.

        Regular field names begin with a letter and can contain the following characters: a-z
        (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a
        wildcard (*). The wildcard can also be the only character in a dynamic field name.
        Multiple wildcards, and wildcards embedded within a string are not supported.

        The name ``score`` is reserved and cannot be used as a field name. To reference a
        document's ID, you can use the name ``_id`` .

      - **ReturnEnabled** *(boolean) --*

        Whether the contents of the field can be returned in the search results.

      - **SortEnabled** *(boolean) --*

        Whether the field can be used to sort the search results.

      - **HighlightEnabled** *(boolean) --*

        Whether highlights can be returned for the field.

      - **AnalysisScheme** *(string) --*

        The name of an analysis scheme for a ``text`` field.

    - **DateOptions** *(dict) --*

      Options for a date field. Dates and times are specified in UTC (Coordinated Universal
      Time) according to IETF RFC3339: yyyy-mm-ddT00:00:00Z. Present if ``IndexFieldType``
      specifies the field is of type ``date`` . All options are enabled by default.

      - **DefaultValue** *(string) --* A value to use for the field if the field isn't
      specified for a document.

      - **SourceField** *(string) --*

        A string that represents the name of an index field. CloudSearch supports regular
        index fields as well as dynamic fields. A dynamic field's name defines a pattern that
        begins or ends with a wildcard. Any document fields that don't map to a regular index
        field but do match a dynamic field's pattern are configured with the dynamic field's
        indexing options.

        Regular field names begin with a letter and can contain the following characters: a-z
        (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a
        wildcard (*). The wildcard can also be the only character in a dynamic field name.
        Multiple wildcards, and wildcards embedded within a string are not supported.

        The name ``score`` is reserved and cannot be used as a field name. To reference a
        document's ID, you can use the name ``_id`` .

      - **FacetEnabled** *(boolean) --*

        Whether facet information can be returned for the field.

      - **SearchEnabled** *(boolean) --*

        Whether the contents of the field are searchable.

      - **ReturnEnabled** *(boolean) --*

        Whether the contents of the field can be returned in the search results.

      - **SortEnabled** *(boolean) --*

        Whether the field can be used to sort the search results.

    - **LatLonOptions** *(dict) --*

      Options for a latlon field. A latlon field contains a location stored as a latitude and
      longitude value pair. Present if ``IndexFieldType`` specifies the field is of type
      ``latlon`` . All options are enabled by default.

      - **DefaultValue** *(string) --* A value to use for the field if the field isn't
      specified for a document.

      - **SourceField** *(string) --*

        A string that represents the name of an index field. CloudSearch supports regular
        index fields as well as dynamic fields. A dynamic field's name defines a pattern that
        begins or ends with a wildcard. Any document fields that don't map to a regular index
        field but do match a dynamic field's pattern are configured with the dynamic field's
        indexing options.

        Regular field names begin with a letter and can contain the following characters: a-z
        (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a
        wildcard (*). The wildcard can also be the only character in a dynamic field name.
        Multiple wildcards, and wildcards embedded within a string are not supported.

        The name ``score`` is reserved and cannot be used as a field name. To reference a
        document's ID, you can use the name ``_id`` .

      - **FacetEnabled** *(boolean) --*

        Whether facet information can be returned for the field.

      - **SearchEnabled** *(boolean) --*

        Whether the contents of the field are searchable.

      - **ReturnEnabled** *(boolean) --*

        Whether the contents of the field can be returned in the search results.

      - **SortEnabled** *(boolean) --*

        Whether the field can be used to sort the search results.

    - **IntArrayOptions** *(dict) --*

      Options for a field that contains an array of 64-bit signed integers. Present if
      ``IndexFieldType`` specifies the field is of type ``int-array`` . All options are
      enabled by default.

      - **DefaultValue** *(integer) --* A value to use for the field if the field isn't
      specified for a document.

      - **SourceFields** *(string) --*

        A list of source fields to map to the field.

      - **FacetEnabled** *(boolean) --*

        Whether facet information can be returned for the field.

      - **SearchEnabled** *(boolean) --*

        Whether the contents of the field are searchable.

      - **ReturnEnabled** *(boolean) --*

        Whether the contents of the field can be returned in the search results.

    - **DoubleArrayOptions** *(dict) --*

      Options for a field that contains an array of double-precision 64-bit floating point
      values. Present if ``IndexFieldType`` specifies the field is of type ``double-array`` .
      All options are enabled by default.

      - **DefaultValue** *(float) --* A value to use for the field if the field isn't
      specified for a document.

      - **SourceFields** *(string) --*

        A list of source fields to map to the field.

      - **FacetEnabled** *(boolean) --*

        Whether facet information can be returned for the field.

      - **SearchEnabled** *(boolean) --*

        Whether the contents of the field are searchable.

      - **ReturnEnabled** *(boolean) --*

        Whether the contents of the field can be returned in the search results.

    - **LiteralArrayOptions** *(dict) --*

      Options for a field that contains an array of literal strings. Present if
      ``IndexFieldType`` specifies the field is of type ``literal-array`` . All options are
      enabled by default.

      - **DefaultValue** *(string) --* A value to use for the field if the field isn't
      specified for a document.

      - **SourceFields** *(string) --*

        A list of source fields to map to the field.

      - **FacetEnabled** *(boolean) --*

        Whether facet information can be returned for the field.

      - **SearchEnabled** *(boolean) --*

        Whether the contents of the field are searchable.

      - **ReturnEnabled** *(boolean) --*

        Whether the contents of the field can be returned in the search results.

    - **TextArrayOptions** *(dict) --*

      Options for a field that contains an array of text strings. Present if
      ``IndexFieldType`` specifies the field is of type ``text-array`` . A ``text-array``
      field is always searchable. All options are enabled by default.

      - **DefaultValue** *(string) --* A value to use for the field if the field isn't
      specified for a document.

      - **SourceFields** *(string) --*

        A list of source fields to map to the field.

      - **ReturnEnabled** *(boolean) --*

        Whether the contents of the field can be returned in the search results.

      - **HighlightEnabled** *(boolean) --*

        Whether highlights can be returned for the field.

      - **AnalysisScheme** *(string) --*

        The name of an analysis scheme for a ``text-array`` field.

    - **DateArrayOptions** *(dict) --*

      Options for a field that contains an array of dates. Present if ``IndexFieldType``
      specifies the field is of type ``date-array`` . All options are enabled by default.

      - **DefaultValue** *(string) --* A value to use for the field if the field isn't
      specified for a document.

      - **SourceFields** *(string) --*

        A list of source fields to map to the field.

      - **FacetEnabled** *(boolean) --*

        Whether facet information can be returned for the field.

      - **SearchEnabled** *(boolean) --*

        Whether the contents of the field are searchable.

      - **ReturnEnabled** *(boolean) --*

        Whether the contents of the field can be returned in the search results.
    """


_ClientDescribeIndexFieldsResponseIndexFieldsStatusTypeDef = TypedDict(
    "_ClientDescribeIndexFieldsResponseIndexFieldsStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": str,
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientDescribeIndexFieldsResponseIndexFieldsStatusTypeDef(
    _ClientDescribeIndexFieldsResponseIndexFieldsStatusTypeDef
):
    """
    Type definition for `ClientDescribeIndexFieldsResponseIndexFields` `Status`

    The status of domain configuration option.

    - **CreationDate** *(datetime) --*

      A timestamp for when this option was created.

    - **UpdateDate** *(datetime) --*

      A timestamp for when this option was last updated.

    - **UpdateVersion** *(integer) --*

      A unique integer that indicates when this option was last updated.

    - **State** *(string) --*

      The state of processing a change to an option. Possible values:

      * ``RequiresIndexDocuments`` : the option's latest value will not be deployed until
      IndexDocuments has been called and indexing is complete.

      * ``Processing`` : the option's latest value is in the process of being activated.

      * ``Active`` : the option's latest value is completely deployed.

      * ``FailedToValidate`` : the option value is not compatible with the domain's data and
      cannot be used to index the data. You must either modify the option value or update or
      remove the incompatible documents.

    - **PendingDeletion** *(boolean) --*

      Indicates that the option will be deleted once processing is complete.
    """


_ClientDescribeIndexFieldsResponseIndexFieldsTypeDef = TypedDict(
    "_ClientDescribeIndexFieldsResponseIndexFieldsTypeDef",
    {
        "Options": ClientDescribeIndexFieldsResponseIndexFieldsOptionsTypeDef,
        "Status": ClientDescribeIndexFieldsResponseIndexFieldsStatusTypeDef,
    },
    total=False,
)


class ClientDescribeIndexFieldsResponseIndexFieldsTypeDef(
    _ClientDescribeIndexFieldsResponseIndexFieldsTypeDef
):
    """
    Type definition for `ClientDescribeIndexFieldsResponse` `IndexFields`

    The value of an ``IndexField`` and its current status.

    - **Options** *(dict) --*

      Configuration information for a field in the index, including its name, type, and
      options. The supported options depend on the `` IndexFieldType`` .

      - **IndexFieldName** *(string) --*

        A string that represents the name of an index field. CloudSearch supports regular index
        fields as well as dynamic fields. A dynamic field's name defines a pattern that begins
        or ends with a wildcard. Any document fields that don't map to a regular index field
        but do match a dynamic field's pattern are configured with the dynamic field's indexing
        options.

        Regular field names begin with a letter and can contain the following characters: a-z
        (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a
        wildcard (*). The wildcard can also be the only character in a dynamic field name.
        Multiple wildcards, and wildcards embedded within a string are not supported.

        The name ``score`` is reserved and cannot be used as a field name. To reference a
        document's ID, you can use the name ``_id`` .

      - **IndexFieldType** *(string) --*

        The type of field. The valid options for a field depend on the field type. For more
        information about the supported field types, see `Configuring Index Fields
        <http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-index-fields.html>`__
        in the *Amazon CloudSearch Developer Guide* .

      - **IntOptions** *(dict) --*

        Options for a 64-bit signed integer field. Present if ``IndexFieldType`` specifies the
        field is of type ``int`` . All options are enabled by default.

        - **DefaultValue** *(integer) --* A value to use for the field if the field isn't
        specified for a document. This can be important if you are using the field in an
        expression and that field is not present in every document.

        - **SourceField** *(string) --*

          The name of the source field to map to the field.

        - **FacetEnabled** *(boolean) --*

          Whether facet information can be returned for the field.

        - **SearchEnabled** *(boolean) --*

          Whether the contents of the field are searchable.

        - **ReturnEnabled** *(boolean) --*

          Whether the contents of the field can be returned in the search results.

        - **SortEnabled** *(boolean) --*

          Whether the field can be used to sort the search results.

      - **DoubleOptions** *(dict) --*

        Options for a double-precision 64-bit floating point field. Present if
        ``IndexFieldType`` specifies the field is of type ``double`` . All options are enabled
        by default.

        - **DefaultValue** *(float) --*

          A value to use for the field if the field isn't specified for a document. This can be
          important if you are using the field in an expression and that field is not present
          in every document.

        - **SourceField** *(string) --*

          The name of the source field to map to the field.

        - **FacetEnabled** *(boolean) --*

          Whether facet information can be returned for the field.

        - **SearchEnabled** *(boolean) --*

          Whether the contents of the field are searchable.

        - **ReturnEnabled** *(boolean) --*

          Whether the contents of the field can be returned in the search results.

        - **SortEnabled** *(boolean) --*

          Whether the field can be used to sort the search results.

      - **LiteralOptions** *(dict) --*

        Options for literal field. Present if ``IndexFieldType`` specifies the field is of type
        ``literal`` . All options are enabled by default.

        - **DefaultValue** *(string) --* A value to use for the field if the field isn't
        specified for a document.

        - **SourceField** *(string) --*

          A string that represents the name of an index field. CloudSearch supports regular
          index fields as well as dynamic fields. A dynamic field's name defines a pattern that
          begins or ends with a wildcard. Any document fields that don't map to a regular index
          field but do match a dynamic field's pattern are configured with the dynamic field's
          indexing options.

          Regular field names begin with a letter and can contain the following characters: a-z
          (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a
          wildcard (*). The wildcard can also be the only character in a dynamic field name.
          Multiple wildcards, and wildcards embedded within a string are not supported.

          The name ``score`` is reserved and cannot be used as a field name. To reference a
          document's ID, you can use the name ``_id`` .

        - **FacetEnabled** *(boolean) --*

          Whether facet information can be returned for the field.

        - **SearchEnabled** *(boolean) --*

          Whether the contents of the field are searchable.

        - **ReturnEnabled** *(boolean) --*

          Whether the contents of the field can be returned in the search results.

        - **SortEnabled** *(boolean) --*

          Whether the field can be used to sort the search results.

      - **TextOptions** *(dict) --*

        Options for text field. Present if ``IndexFieldType`` specifies the field is of type
        ``text`` . A ``text`` field is always searchable. All options are enabled by default.

        - **DefaultValue** *(string) --* A value to use for the field if the field isn't
        specified for a document.

        - **SourceField** *(string) --*

          A string that represents the name of an index field. CloudSearch supports regular
          index fields as well as dynamic fields. A dynamic field's name defines a pattern that
          begins or ends with a wildcard. Any document fields that don't map to a regular index
          field but do match a dynamic field's pattern are configured with the dynamic field's
          indexing options.

          Regular field names begin with a letter and can contain the following characters: a-z
          (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a
          wildcard (*). The wildcard can also be the only character in a dynamic field name.
          Multiple wildcards, and wildcards embedded within a string are not supported.

          The name ``score`` is reserved and cannot be used as a field name. To reference a
          document's ID, you can use the name ``_id`` .

        - **ReturnEnabled** *(boolean) --*

          Whether the contents of the field can be returned in the search results.

        - **SortEnabled** *(boolean) --*

          Whether the field can be used to sort the search results.

        - **HighlightEnabled** *(boolean) --*

          Whether highlights can be returned for the field.

        - **AnalysisScheme** *(string) --*

          The name of an analysis scheme for a ``text`` field.

      - **DateOptions** *(dict) --*

        Options for a date field. Dates and times are specified in UTC (Coordinated Universal
        Time) according to IETF RFC3339: yyyy-mm-ddT00:00:00Z. Present if ``IndexFieldType``
        specifies the field is of type ``date`` . All options are enabled by default.

        - **DefaultValue** *(string) --* A value to use for the field if the field isn't
        specified for a document.

        - **SourceField** *(string) --*

          A string that represents the name of an index field. CloudSearch supports regular
          index fields as well as dynamic fields. A dynamic field's name defines a pattern that
          begins or ends with a wildcard. Any document fields that don't map to a regular index
          field but do match a dynamic field's pattern are configured with the dynamic field's
          indexing options.

          Regular field names begin with a letter and can contain the following characters: a-z
          (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a
          wildcard (*). The wildcard can also be the only character in a dynamic field name.
          Multiple wildcards, and wildcards embedded within a string are not supported.

          The name ``score`` is reserved and cannot be used as a field name. To reference a
          document's ID, you can use the name ``_id`` .

        - **FacetEnabled** *(boolean) --*

          Whether facet information can be returned for the field.

        - **SearchEnabled** *(boolean) --*

          Whether the contents of the field are searchable.

        - **ReturnEnabled** *(boolean) --*

          Whether the contents of the field can be returned in the search results.

        - **SortEnabled** *(boolean) --*

          Whether the field can be used to sort the search results.

      - **LatLonOptions** *(dict) --*

        Options for a latlon field. A latlon field contains a location stored as a latitude and
        longitude value pair. Present if ``IndexFieldType`` specifies the field is of type
        ``latlon`` . All options are enabled by default.

        - **DefaultValue** *(string) --* A value to use for the field if the field isn't
        specified for a document.

        - **SourceField** *(string) --*

          A string that represents the name of an index field. CloudSearch supports regular
          index fields as well as dynamic fields. A dynamic field's name defines a pattern that
          begins or ends with a wildcard. Any document fields that don't map to a regular index
          field but do match a dynamic field's pattern are configured with the dynamic field's
          indexing options.

          Regular field names begin with a letter and can contain the following characters: a-z
          (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a
          wildcard (*). The wildcard can also be the only character in a dynamic field name.
          Multiple wildcards, and wildcards embedded within a string are not supported.

          The name ``score`` is reserved and cannot be used as a field name. To reference a
          document's ID, you can use the name ``_id`` .

        - **FacetEnabled** *(boolean) --*

          Whether facet information can be returned for the field.

        - **SearchEnabled** *(boolean) --*

          Whether the contents of the field are searchable.

        - **ReturnEnabled** *(boolean) --*

          Whether the contents of the field can be returned in the search results.

        - **SortEnabled** *(boolean) --*

          Whether the field can be used to sort the search results.

      - **IntArrayOptions** *(dict) --*

        Options for a field that contains an array of 64-bit signed integers. Present if
        ``IndexFieldType`` specifies the field is of type ``int-array`` . All options are
        enabled by default.

        - **DefaultValue** *(integer) --* A value to use for the field if the field isn't
        specified for a document.

        - **SourceFields** *(string) --*

          A list of source fields to map to the field.

        - **FacetEnabled** *(boolean) --*

          Whether facet information can be returned for the field.

        - **SearchEnabled** *(boolean) --*

          Whether the contents of the field are searchable.

        - **ReturnEnabled** *(boolean) --*

          Whether the contents of the field can be returned in the search results.

      - **DoubleArrayOptions** *(dict) --*

        Options for a field that contains an array of double-precision 64-bit floating point
        values. Present if ``IndexFieldType`` specifies the field is of type ``double-array`` .
        All options are enabled by default.

        - **DefaultValue** *(float) --* A value to use for the field if the field isn't
        specified for a document.

        - **SourceFields** *(string) --*

          A list of source fields to map to the field.

        - **FacetEnabled** *(boolean) --*

          Whether facet information can be returned for the field.

        - **SearchEnabled** *(boolean) --*

          Whether the contents of the field are searchable.

        - **ReturnEnabled** *(boolean) --*

          Whether the contents of the field can be returned in the search results.

      - **LiteralArrayOptions** *(dict) --*

        Options for a field that contains an array of literal strings. Present if
        ``IndexFieldType`` specifies the field is of type ``literal-array`` . All options are
        enabled by default.

        - **DefaultValue** *(string) --* A value to use for the field if the field isn't
        specified for a document.

        - **SourceFields** *(string) --*

          A list of source fields to map to the field.

        - **FacetEnabled** *(boolean) --*

          Whether facet information can be returned for the field.

        - **SearchEnabled** *(boolean) --*

          Whether the contents of the field are searchable.

        - **ReturnEnabled** *(boolean) --*

          Whether the contents of the field can be returned in the search results.

      - **TextArrayOptions** *(dict) --*

        Options for a field that contains an array of text strings. Present if
        ``IndexFieldType`` specifies the field is of type ``text-array`` . A ``text-array``
        field is always searchable. All options are enabled by default.

        - **DefaultValue** *(string) --* A value to use for the field if the field isn't
        specified for a document.

        - **SourceFields** *(string) --*

          A list of source fields to map to the field.

        - **ReturnEnabled** *(boolean) --*

          Whether the contents of the field can be returned in the search results.

        - **HighlightEnabled** *(boolean) --*

          Whether highlights can be returned for the field.

        - **AnalysisScheme** *(string) --*

          The name of an analysis scheme for a ``text-array`` field.

      - **DateArrayOptions** *(dict) --*

        Options for a field that contains an array of dates. Present if ``IndexFieldType``
        specifies the field is of type ``date-array`` . All options are enabled by default.

        - **DefaultValue** *(string) --* A value to use for the field if the field isn't
        specified for a document.

        - **SourceFields** *(string) --*

          A list of source fields to map to the field.

        - **FacetEnabled** *(boolean) --*

          Whether facet information can be returned for the field.

        - **SearchEnabled** *(boolean) --*

          Whether the contents of the field are searchable.

        - **ReturnEnabled** *(boolean) --*

          Whether the contents of the field can be returned in the search results.

    - **Status** *(dict) --*

      The status of domain configuration option.

      - **CreationDate** *(datetime) --*

        A timestamp for when this option was created.

      - **UpdateDate** *(datetime) --*

        A timestamp for when this option was last updated.

      - **UpdateVersion** *(integer) --*

        A unique integer that indicates when this option was last updated.

      - **State** *(string) --*

        The state of processing a change to an option. Possible values:

        * ``RequiresIndexDocuments`` : the option's latest value will not be deployed until
        IndexDocuments has been called and indexing is complete.

        * ``Processing`` : the option's latest value is in the process of being activated.

        * ``Active`` : the option's latest value is completely deployed.

        * ``FailedToValidate`` : the option value is not compatible with the domain's data and
        cannot be used to index the data. You must either modify the option value or update or
        remove the incompatible documents.

      - **PendingDeletion** *(boolean) --*

        Indicates that the option will be deleted once processing is complete.
    """


_ClientDescribeIndexFieldsResponseTypeDef = TypedDict(
    "_ClientDescribeIndexFieldsResponseTypeDef",
    {"IndexFields": List[ClientDescribeIndexFieldsResponseIndexFieldsTypeDef]},
    total=False,
)


class ClientDescribeIndexFieldsResponseTypeDef(
    _ClientDescribeIndexFieldsResponseTypeDef
):
    """
    Type definition for `ClientDescribeIndexFields` `Response`

    The result of a ``DescribeIndexFields`` request. Contains the index fields configured for the
    domain specified in the request.

    - **IndexFields** *(list) --*

      The index fields configured for the domain.

      - *(dict) --*

        The value of an ``IndexField`` and its current status.

        - **Options** *(dict) --*

          Configuration information for a field in the index, including its name, type, and
          options. The supported options depend on the `` IndexFieldType`` .

          - **IndexFieldName** *(string) --*

            A string that represents the name of an index field. CloudSearch supports regular index
            fields as well as dynamic fields. A dynamic field's name defines a pattern that begins
            or ends with a wildcard. Any document fields that don't map to a regular index field
            but do match a dynamic field's pattern are configured with the dynamic field's indexing
            options.

            Regular field names begin with a letter and can contain the following characters: a-z
            (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a
            wildcard (*). The wildcard can also be the only character in a dynamic field name.
            Multiple wildcards, and wildcards embedded within a string are not supported.

            The name ``score`` is reserved and cannot be used as a field name. To reference a
            document's ID, you can use the name ``_id`` .

          - **IndexFieldType** *(string) --*

            The type of field. The valid options for a field depend on the field type. For more
            information about the supported field types, see `Configuring Index Fields
            <http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-index-fields.html>`__
            in the *Amazon CloudSearch Developer Guide* .

          - **IntOptions** *(dict) --*

            Options for a 64-bit signed integer field. Present if ``IndexFieldType`` specifies the
            field is of type ``int`` . All options are enabled by default.

            - **DefaultValue** *(integer) --* A value to use for the field if the field isn't
            specified for a document. This can be important if you are using the field in an
            expression and that field is not present in every document.

            - **SourceField** *(string) --*

              The name of the source field to map to the field.

            - **FacetEnabled** *(boolean) --*

              Whether facet information can be returned for the field.

            - **SearchEnabled** *(boolean) --*

              Whether the contents of the field are searchable.

            - **ReturnEnabled** *(boolean) --*

              Whether the contents of the field can be returned in the search results.

            - **SortEnabled** *(boolean) --*

              Whether the field can be used to sort the search results.

          - **DoubleOptions** *(dict) --*

            Options for a double-precision 64-bit floating point field. Present if
            ``IndexFieldType`` specifies the field is of type ``double`` . All options are enabled
            by default.

            - **DefaultValue** *(float) --*

              A value to use for the field if the field isn't specified for a document. This can be
              important if you are using the field in an expression and that field is not present
              in every document.

            - **SourceField** *(string) --*

              The name of the source field to map to the field.

            - **FacetEnabled** *(boolean) --*

              Whether facet information can be returned for the field.

            - **SearchEnabled** *(boolean) --*

              Whether the contents of the field are searchable.

            - **ReturnEnabled** *(boolean) --*

              Whether the contents of the field can be returned in the search results.

            - **SortEnabled** *(boolean) --*

              Whether the field can be used to sort the search results.

          - **LiteralOptions** *(dict) --*

            Options for literal field. Present if ``IndexFieldType`` specifies the field is of type
            ``literal`` . All options are enabled by default.

            - **DefaultValue** *(string) --* A value to use for the field if the field isn't
            specified for a document.

            - **SourceField** *(string) --*

              A string that represents the name of an index field. CloudSearch supports regular
              index fields as well as dynamic fields. A dynamic field's name defines a pattern that
              begins or ends with a wildcard. Any document fields that don't map to a regular index
              field but do match a dynamic field's pattern are configured with the dynamic field's
              indexing options.

              Regular field names begin with a letter and can contain the following characters: a-z
              (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a
              wildcard (*). The wildcard can also be the only character in a dynamic field name.
              Multiple wildcards, and wildcards embedded within a string are not supported.

              The name ``score`` is reserved and cannot be used as a field name. To reference a
              document's ID, you can use the name ``_id`` .

            - **FacetEnabled** *(boolean) --*

              Whether facet information can be returned for the field.

            - **SearchEnabled** *(boolean) --*

              Whether the contents of the field are searchable.

            - **ReturnEnabled** *(boolean) --*

              Whether the contents of the field can be returned in the search results.

            - **SortEnabled** *(boolean) --*

              Whether the field can be used to sort the search results.

          - **TextOptions** *(dict) --*

            Options for text field. Present if ``IndexFieldType`` specifies the field is of type
            ``text`` . A ``text`` field is always searchable. All options are enabled by default.

            - **DefaultValue** *(string) --* A value to use for the field if the field isn't
            specified for a document.

            - **SourceField** *(string) --*

              A string that represents the name of an index field. CloudSearch supports regular
              index fields as well as dynamic fields. A dynamic field's name defines a pattern that
              begins or ends with a wildcard. Any document fields that don't map to a regular index
              field but do match a dynamic field's pattern are configured with the dynamic field's
              indexing options.

              Regular field names begin with a letter and can contain the following characters: a-z
              (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a
              wildcard (*). The wildcard can also be the only character in a dynamic field name.
              Multiple wildcards, and wildcards embedded within a string are not supported.

              The name ``score`` is reserved and cannot be used as a field name. To reference a
              document's ID, you can use the name ``_id`` .

            - **ReturnEnabled** *(boolean) --*

              Whether the contents of the field can be returned in the search results.

            - **SortEnabled** *(boolean) --*

              Whether the field can be used to sort the search results.

            - **HighlightEnabled** *(boolean) --*

              Whether highlights can be returned for the field.

            - **AnalysisScheme** *(string) --*

              The name of an analysis scheme for a ``text`` field.

          - **DateOptions** *(dict) --*

            Options for a date field. Dates and times are specified in UTC (Coordinated Universal
            Time) according to IETF RFC3339: yyyy-mm-ddT00:00:00Z. Present if ``IndexFieldType``
            specifies the field is of type ``date`` . All options are enabled by default.

            - **DefaultValue** *(string) --* A value to use for the field if the field isn't
            specified for a document.

            - **SourceField** *(string) --*

              A string that represents the name of an index field. CloudSearch supports regular
              index fields as well as dynamic fields. A dynamic field's name defines a pattern that
              begins or ends with a wildcard. Any document fields that don't map to a regular index
              field but do match a dynamic field's pattern are configured with the dynamic field's
              indexing options.

              Regular field names begin with a letter and can contain the following characters: a-z
              (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a
              wildcard (*). The wildcard can also be the only character in a dynamic field name.
              Multiple wildcards, and wildcards embedded within a string are not supported.

              The name ``score`` is reserved and cannot be used as a field name. To reference a
              document's ID, you can use the name ``_id`` .

            - **FacetEnabled** *(boolean) --*

              Whether facet information can be returned for the field.

            - **SearchEnabled** *(boolean) --*

              Whether the contents of the field are searchable.

            - **ReturnEnabled** *(boolean) --*

              Whether the contents of the field can be returned in the search results.

            - **SortEnabled** *(boolean) --*

              Whether the field can be used to sort the search results.

          - **LatLonOptions** *(dict) --*

            Options for a latlon field. A latlon field contains a location stored as a latitude and
            longitude value pair. Present if ``IndexFieldType`` specifies the field is of type
            ``latlon`` . All options are enabled by default.

            - **DefaultValue** *(string) --* A value to use for the field if the field isn't
            specified for a document.

            - **SourceField** *(string) --*

              A string that represents the name of an index field. CloudSearch supports regular
              index fields as well as dynamic fields. A dynamic field's name defines a pattern that
              begins or ends with a wildcard. Any document fields that don't map to a regular index
              field but do match a dynamic field's pattern are configured with the dynamic field's
              indexing options.

              Regular field names begin with a letter and can contain the following characters: a-z
              (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a
              wildcard (*). The wildcard can also be the only character in a dynamic field name.
              Multiple wildcards, and wildcards embedded within a string are not supported.

              The name ``score`` is reserved and cannot be used as a field name. To reference a
              document's ID, you can use the name ``_id`` .

            - **FacetEnabled** *(boolean) --*

              Whether facet information can be returned for the field.

            - **SearchEnabled** *(boolean) --*

              Whether the contents of the field are searchable.

            - **ReturnEnabled** *(boolean) --*

              Whether the contents of the field can be returned in the search results.

            - **SortEnabled** *(boolean) --*

              Whether the field can be used to sort the search results.

          - **IntArrayOptions** *(dict) --*

            Options for a field that contains an array of 64-bit signed integers. Present if
            ``IndexFieldType`` specifies the field is of type ``int-array`` . All options are
            enabled by default.

            - **DefaultValue** *(integer) --* A value to use for the field if the field isn't
            specified for a document.

            - **SourceFields** *(string) --*

              A list of source fields to map to the field.

            - **FacetEnabled** *(boolean) --*

              Whether facet information can be returned for the field.

            - **SearchEnabled** *(boolean) --*

              Whether the contents of the field are searchable.

            - **ReturnEnabled** *(boolean) --*

              Whether the contents of the field can be returned in the search results.

          - **DoubleArrayOptions** *(dict) --*

            Options for a field that contains an array of double-precision 64-bit floating point
            values. Present if ``IndexFieldType`` specifies the field is of type ``double-array`` .
            All options are enabled by default.

            - **DefaultValue** *(float) --* A value to use for the field if the field isn't
            specified for a document.

            - **SourceFields** *(string) --*

              A list of source fields to map to the field.

            - **FacetEnabled** *(boolean) --*

              Whether facet information can be returned for the field.

            - **SearchEnabled** *(boolean) --*

              Whether the contents of the field are searchable.

            - **ReturnEnabled** *(boolean) --*

              Whether the contents of the field can be returned in the search results.

          - **LiteralArrayOptions** *(dict) --*

            Options for a field that contains an array of literal strings. Present if
            ``IndexFieldType`` specifies the field is of type ``literal-array`` . All options are
            enabled by default.

            - **DefaultValue** *(string) --* A value to use for the field if the field isn't
            specified for a document.

            - **SourceFields** *(string) --*

              A list of source fields to map to the field.

            - **FacetEnabled** *(boolean) --*

              Whether facet information can be returned for the field.

            - **SearchEnabled** *(boolean) --*

              Whether the contents of the field are searchable.

            - **ReturnEnabled** *(boolean) --*

              Whether the contents of the field can be returned in the search results.

          - **TextArrayOptions** *(dict) --*

            Options for a field that contains an array of text strings. Present if
            ``IndexFieldType`` specifies the field is of type ``text-array`` . A ``text-array``
            field is always searchable. All options are enabled by default.

            - **DefaultValue** *(string) --* A value to use for the field if the field isn't
            specified for a document.

            - **SourceFields** *(string) --*

              A list of source fields to map to the field.

            - **ReturnEnabled** *(boolean) --*

              Whether the contents of the field can be returned in the search results.

            - **HighlightEnabled** *(boolean) --*

              Whether highlights can be returned for the field.

            - **AnalysisScheme** *(string) --*

              The name of an analysis scheme for a ``text-array`` field.

          - **DateArrayOptions** *(dict) --*

            Options for a field that contains an array of dates. Present if ``IndexFieldType``
            specifies the field is of type ``date-array`` . All options are enabled by default.

            - **DefaultValue** *(string) --* A value to use for the field if the field isn't
            specified for a document.

            - **SourceFields** *(string) --*

              A list of source fields to map to the field.

            - **FacetEnabled** *(boolean) --*

              Whether facet information can be returned for the field.

            - **SearchEnabled** *(boolean) --*

              Whether the contents of the field are searchable.

            - **ReturnEnabled** *(boolean) --*

              Whether the contents of the field can be returned in the search results.

        - **Status** *(dict) --*

          The status of domain configuration option.

          - **CreationDate** *(datetime) --*

            A timestamp for when this option was created.

          - **UpdateDate** *(datetime) --*

            A timestamp for when this option was last updated.

          - **UpdateVersion** *(integer) --*

            A unique integer that indicates when this option was last updated.

          - **State** *(string) --*

            The state of processing a change to an option. Possible values:

            * ``RequiresIndexDocuments`` : the option's latest value will not be deployed until
            IndexDocuments has been called and indexing is complete.

            * ``Processing`` : the option's latest value is in the process of being activated.

            * ``Active`` : the option's latest value is completely deployed.

            * ``FailedToValidate`` : the option value is not compatible with the domain's data and
            cannot be used to index the data. You must either modify the option value or update or
            remove the incompatible documents.

          - **PendingDeletion** *(boolean) --*

            Indicates that the option will be deleted once processing is complete.
    """


_ClientDescribeScalingParametersResponseScalingParametersOptionsTypeDef = TypedDict(
    "_ClientDescribeScalingParametersResponseScalingParametersOptionsTypeDef",
    {
        "DesiredInstanceType": str,
        "DesiredReplicationCount": int,
        "DesiredPartitionCount": int,
    },
    total=False,
)


class ClientDescribeScalingParametersResponseScalingParametersOptionsTypeDef(
    _ClientDescribeScalingParametersResponseScalingParametersOptionsTypeDef
):
    """
    Type definition for `ClientDescribeScalingParametersResponseScalingParameters` `Options`

    The desired instance type and desired number of replicas of each index partition.

    - **DesiredInstanceType** *(string) --*

      The instance type that you want to preconfigure for your domain. For example,
      ``search.m1.small`` .

    - **DesiredReplicationCount** *(integer) --*

      The number of replicas you want to preconfigure for each index partition.

    - **DesiredPartitionCount** *(integer) --*

      The number of partitions you want to preconfigure for your domain. Only valid when you
      select ``m2.2xlarge`` as the desired instance type.
    """


_ClientDescribeScalingParametersResponseScalingParametersStatusTypeDef = TypedDict(
    "_ClientDescribeScalingParametersResponseScalingParametersStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": str,
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientDescribeScalingParametersResponseScalingParametersStatusTypeDef(
    _ClientDescribeScalingParametersResponseScalingParametersStatusTypeDef
):
    """
    Type definition for `ClientDescribeScalingParametersResponseScalingParameters` `Status`

    The status of domain configuration option.

    - **CreationDate** *(datetime) --*

      A timestamp for when this option was created.

    - **UpdateDate** *(datetime) --*

      A timestamp for when this option was last updated.

    - **UpdateVersion** *(integer) --*

      A unique integer that indicates when this option was last updated.

    - **State** *(string) --*

      The state of processing a change to an option. Possible values:

      * ``RequiresIndexDocuments`` : the option's latest value will not be deployed until
      IndexDocuments has been called and indexing is complete.

      * ``Processing`` : the option's latest value is in the process of being activated.

      * ``Active`` : the option's latest value is completely deployed.

      * ``FailedToValidate`` : the option value is not compatible with the domain's data and
      cannot be used to index the data. You must either modify the option value or update or
      remove the incompatible documents.

    - **PendingDeletion** *(boolean) --*

      Indicates that the option will be deleted once processing is complete.
    """


_ClientDescribeScalingParametersResponseScalingParametersTypeDef = TypedDict(
    "_ClientDescribeScalingParametersResponseScalingParametersTypeDef",
    {
        "Options": ClientDescribeScalingParametersResponseScalingParametersOptionsTypeDef,
        "Status": ClientDescribeScalingParametersResponseScalingParametersStatusTypeDef,
    },
    total=False,
)


class ClientDescribeScalingParametersResponseScalingParametersTypeDef(
    _ClientDescribeScalingParametersResponseScalingParametersTypeDef
):
    """
    Type definition for `ClientDescribeScalingParametersResponse` `ScalingParameters`

    The status and configuration of a search domain's scaling parameters.

    - **Options** *(dict) --*

      The desired instance type and desired number of replicas of each index partition.

      - **DesiredInstanceType** *(string) --*

        The instance type that you want to preconfigure for your domain. For example,
        ``search.m1.small`` .

      - **DesiredReplicationCount** *(integer) --*

        The number of replicas you want to preconfigure for each index partition.

      - **DesiredPartitionCount** *(integer) --*

        The number of partitions you want to preconfigure for your domain. Only valid when you
        select ``m2.2xlarge`` as the desired instance type.

    - **Status** *(dict) --*

      The status of domain configuration option.

      - **CreationDate** *(datetime) --*

        A timestamp for when this option was created.

      - **UpdateDate** *(datetime) --*

        A timestamp for when this option was last updated.

      - **UpdateVersion** *(integer) --*

        A unique integer that indicates when this option was last updated.

      - **State** *(string) --*

        The state of processing a change to an option. Possible values:

        * ``RequiresIndexDocuments`` : the option's latest value will not be deployed until
        IndexDocuments has been called and indexing is complete.

        * ``Processing`` : the option's latest value is in the process of being activated.

        * ``Active`` : the option's latest value is completely deployed.

        * ``FailedToValidate`` : the option value is not compatible with the domain's data and
        cannot be used to index the data. You must either modify the option value or update or
        remove the incompatible documents.

      - **PendingDeletion** *(boolean) --*

        Indicates that the option will be deleted once processing is complete.
    """


_ClientDescribeScalingParametersResponseTypeDef = TypedDict(
    "_ClientDescribeScalingParametersResponseTypeDef",
    {
        "ScalingParameters": ClientDescribeScalingParametersResponseScalingParametersTypeDef
    },
    total=False,
)


class ClientDescribeScalingParametersResponseTypeDef(
    _ClientDescribeScalingParametersResponseTypeDef
):
    """
    Type definition for `ClientDescribeScalingParameters` `Response`

    The result of a ``DescribeScalingParameters`` request. Contains the scaling parameters
    configured for the domain specified in the request.

    - **ScalingParameters** *(dict) --*

      The status and configuration of a search domain's scaling parameters.

      - **Options** *(dict) --*

        The desired instance type and desired number of replicas of each index partition.

        - **DesiredInstanceType** *(string) --*

          The instance type that you want to preconfigure for your domain. For example,
          ``search.m1.small`` .

        - **DesiredReplicationCount** *(integer) --*

          The number of replicas you want to preconfigure for each index partition.

        - **DesiredPartitionCount** *(integer) --*

          The number of partitions you want to preconfigure for your domain. Only valid when you
          select ``m2.2xlarge`` as the desired instance type.

      - **Status** *(dict) --*

        The status of domain configuration option.

        - **CreationDate** *(datetime) --*

          A timestamp for when this option was created.

        - **UpdateDate** *(datetime) --*

          A timestamp for when this option was last updated.

        - **UpdateVersion** *(integer) --*

          A unique integer that indicates when this option was last updated.

        - **State** *(string) --*

          The state of processing a change to an option. Possible values:

          * ``RequiresIndexDocuments`` : the option's latest value will not be deployed until
          IndexDocuments has been called and indexing is complete.

          * ``Processing`` : the option's latest value is in the process of being activated.

          * ``Active`` : the option's latest value is completely deployed.

          * ``FailedToValidate`` : the option value is not compatible with the domain's data and
          cannot be used to index the data. You must either modify the option value or update or
          remove the incompatible documents.

        - **PendingDeletion** *(boolean) --*

          Indicates that the option will be deleted once processing is complete.
    """


_ClientDescribeServiceAccessPoliciesResponseAccessPoliciesStatusTypeDef = TypedDict(
    "_ClientDescribeServiceAccessPoliciesResponseAccessPoliciesStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": str,
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientDescribeServiceAccessPoliciesResponseAccessPoliciesStatusTypeDef(
    _ClientDescribeServiceAccessPoliciesResponseAccessPoliciesStatusTypeDef
):
    """
    Type definition for `ClientDescribeServiceAccessPoliciesResponseAccessPolicies` `Status`

    The status of domain configuration option.

    - **CreationDate** *(datetime) --*

      A timestamp for when this option was created.

    - **UpdateDate** *(datetime) --*

      A timestamp for when this option was last updated.

    - **UpdateVersion** *(integer) --*

      A unique integer that indicates when this option was last updated.

    - **State** *(string) --*

      The state of processing a change to an option. Possible values:

      * ``RequiresIndexDocuments`` : the option's latest value will not be deployed until
      IndexDocuments has been called and indexing is complete.

      * ``Processing`` : the option's latest value is in the process of being activated.

      * ``Active`` : the option's latest value is completely deployed.

      * ``FailedToValidate`` : the option value is not compatible with the domain's data and
      cannot be used to index the data. You must either modify the option value or update or
      remove the incompatible documents.

    - **PendingDeletion** *(boolean) --*

      Indicates that the option will be deleted once processing is complete.
    """


_ClientDescribeServiceAccessPoliciesResponseAccessPoliciesTypeDef = TypedDict(
    "_ClientDescribeServiceAccessPoliciesResponseAccessPoliciesTypeDef",
    {
        "Options": str,
        "Status": ClientDescribeServiceAccessPoliciesResponseAccessPoliciesStatusTypeDef,
    },
    total=False,
)


class ClientDescribeServiceAccessPoliciesResponseAccessPoliciesTypeDef(
    _ClientDescribeServiceAccessPoliciesResponseAccessPoliciesTypeDef
):
    """
    Type definition for `ClientDescribeServiceAccessPoliciesResponse` `AccessPolicies`

    The access rules configured for the domain specified in the request.

    - **Options** *(string) --*

      Access rules for a domain's document or search service endpoints. For more information, see
      `Configuring Access for a Search Domain
      <http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-access.html>`__
      in the *Amazon CloudSearch Developer Guide* . The maximum size of a policy document is 100
      KB.

    - **Status** *(dict) --*

      The status of domain configuration option.

      - **CreationDate** *(datetime) --*

        A timestamp for when this option was created.

      - **UpdateDate** *(datetime) --*

        A timestamp for when this option was last updated.

      - **UpdateVersion** *(integer) --*

        A unique integer that indicates when this option was last updated.

      - **State** *(string) --*

        The state of processing a change to an option. Possible values:

        * ``RequiresIndexDocuments`` : the option's latest value will not be deployed until
        IndexDocuments has been called and indexing is complete.

        * ``Processing`` : the option's latest value is in the process of being activated.

        * ``Active`` : the option's latest value is completely deployed.

        * ``FailedToValidate`` : the option value is not compatible with the domain's data and
        cannot be used to index the data. You must either modify the option value or update or
        remove the incompatible documents.

      - **PendingDeletion** *(boolean) --*

        Indicates that the option will be deleted once processing is complete.
    """


_ClientDescribeServiceAccessPoliciesResponseTypeDef = TypedDict(
    "_ClientDescribeServiceAccessPoliciesResponseTypeDef",
    {
        "AccessPolicies": ClientDescribeServiceAccessPoliciesResponseAccessPoliciesTypeDef
    },
    total=False,
)


class ClientDescribeServiceAccessPoliciesResponseTypeDef(
    _ClientDescribeServiceAccessPoliciesResponseTypeDef
):
    """
    Type definition for `ClientDescribeServiceAccessPolicies` `Response`

    The result of a ``DescribeServiceAccessPolicies`` request.

    - **AccessPolicies** *(dict) --*

      The access rules configured for the domain specified in the request.

      - **Options** *(string) --*

        Access rules for a domain's document or search service endpoints. For more information, see
        `Configuring Access for a Search Domain
        <http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-access.html>`__
        in the *Amazon CloudSearch Developer Guide* . The maximum size of a policy document is 100
        KB.

      - **Status** *(dict) --*

        The status of domain configuration option.

        - **CreationDate** *(datetime) --*

          A timestamp for when this option was created.

        - **UpdateDate** *(datetime) --*

          A timestamp for when this option was last updated.

        - **UpdateVersion** *(integer) --*

          A unique integer that indicates when this option was last updated.

        - **State** *(string) --*

          The state of processing a change to an option. Possible values:

          * ``RequiresIndexDocuments`` : the option's latest value will not be deployed until
          IndexDocuments has been called and indexing is complete.

          * ``Processing`` : the option's latest value is in the process of being activated.

          * ``Active`` : the option's latest value is completely deployed.

          * ``FailedToValidate`` : the option value is not compatible with the domain's data and
          cannot be used to index the data. You must either modify the option value or update or
          remove the incompatible documents.

        - **PendingDeletion** *(boolean) --*

          Indicates that the option will be deleted once processing is complete.
    """


_ClientDescribeSuggestersResponseSuggestersOptionsDocumentSuggesterOptionsTypeDef = TypedDict(
    "_ClientDescribeSuggestersResponseSuggestersOptionsDocumentSuggesterOptionsTypeDef",
    {"SourceField": str, "FuzzyMatching": str, "SortExpression": str},
    total=False,
)


class ClientDescribeSuggestersResponseSuggestersOptionsDocumentSuggesterOptionsTypeDef(
    _ClientDescribeSuggestersResponseSuggestersOptionsDocumentSuggesterOptionsTypeDef
):
    """
    Type definition for `ClientDescribeSuggestersResponseSuggestersOptions` `DocumentSuggesterOptions`

    Options for a search suggester.

    - **SourceField** *(string) --*

      The name of the index field you want to use for suggestions.

    - **FuzzyMatching** *(string) --*

      The level of fuzziness allowed when suggesting matches for a string: ``none`` ,
      ``low`` , or ``high`` . With none, the specified string is treated as an exact
      prefix. With low, suggestions must differ from the specified string by no more than
      one character. With high, suggestions can differ by up to two characters. The default
      is none.

    - **SortExpression** *(string) --*

      An expression that computes a score for each suggestion to control how they are
      sorted. The scores are rounded to the nearest integer, with a floor of 0 and a
      ceiling of 2^31-1. A document's relevance score is not computed for suggestions, so
      sort expressions cannot reference the ``_score`` value. To sort suggestions using a
      numeric field or existing expression, simply specify the name of the field or
      expression. If no expression is configured for the suggester, the suggestions are
      sorted with the closest matches listed first.
    """


_ClientDescribeSuggestersResponseSuggestersOptionsTypeDef = TypedDict(
    "_ClientDescribeSuggestersResponseSuggestersOptionsTypeDef",
    {
        "SuggesterName": str,
        "DocumentSuggesterOptions": ClientDescribeSuggestersResponseSuggestersOptionsDocumentSuggesterOptionsTypeDef,
    },
    total=False,
)


class ClientDescribeSuggestersResponseSuggestersOptionsTypeDef(
    _ClientDescribeSuggestersResponseSuggestersOptionsTypeDef
):
    """
    Type definition for `ClientDescribeSuggestersResponseSuggesters` `Options`

    Configuration information for a search suggester. Each suggester has a unique name and
    specifies the text field you want to use for suggestions. The following options can be
    configured for a suggester: ``FuzzyMatching`` , ``SortExpression`` .

    - **SuggesterName** *(string) --*

      Names must begin with a letter and can contain the following characters: a-z
      (lowercase), 0-9, and _ (underscore).

    - **DocumentSuggesterOptions** *(dict) --*

      Options for a search suggester.

      - **SourceField** *(string) --*

        The name of the index field you want to use for suggestions.

      - **FuzzyMatching** *(string) --*

        The level of fuzziness allowed when suggesting matches for a string: ``none`` ,
        ``low`` , or ``high`` . With none, the specified string is treated as an exact
        prefix. With low, suggestions must differ from the specified string by no more than
        one character. With high, suggestions can differ by up to two characters. The default
        is none.

      - **SortExpression** *(string) --*

        An expression that computes a score for each suggestion to control how they are
        sorted. The scores are rounded to the nearest integer, with a floor of 0 and a
        ceiling of 2^31-1. A document's relevance score is not computed for suggestions, so
        sort expressions cannot reference the ``_score`` value. To sort suggestions using a
        numeric field or existing expression, simply specify the name of the field or
        expression. If no expression is configured for the suggester, the suggestions are
        sorted with the closest matches listed first.
    """


_ClientDescribeSuggestersResponseSuggestersStatusTypeDef = TypedDict(
    "_ClientDescribeSuggestersResponseSuggestersStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": str,
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientDescribeSuggestersResponseSuggestersStatusTypeDef(
    _ClientDescribeSuggestersResponseSuggestersStatusTypeDef
):
    """
    Type definition for `ClientDescribeSuggestersResponseSuggesters` `Status`

    The status of domain configuration option.

    - **CreationDate** *(datetime) --*

      A timestamp for when this option was created.

    - **UpdateDate** *(datetime) --*

      A timestamp for when this option was last updated.

    - **UpdateVersion** *(integer) --*

      A unique integer that indicates when this option was last updated.

    - **State** *(string) --*

      The state of processing a change to an option. Possible values:

      * ``RequiresIndexDocuments`` : the option's latest value will not be deployed until
      IndexDocuments has been called and indexing is complete.

      * ``Processing`` : the option's latest value is in the process of being activated.

      * ``Active`` : the option's latest value is completely deployed.

      * ``FailedToValidate`` : the option value is not compatible with the domain's data and
      cannot be used to index the data. You must either modify the option value or update or
      remove the incompatible documents.

    - **PendingDeletion** *(boolean) --*

      Indicates that the option will be deleted once processing is complete.
    """


_ClientDescribeSuggestersResponseSuggestersTypeDef = TypedDict(
    "_ClientDescribeSuggestersResponseSuggestersTypeDef",
    {
        "Options": ClientDescribeSuggestersResponseSuggestersOptionsTypeDef,
        "Status": ClientDescribeSuggestersResponseSuggestersStatusTypeDef,
    },
    total=False,
)


class ClientDescribeSuggestersResponseSuggestersTypeDef(
    _ClientDescribeSuggestersResponseSuggestersTypeDef
):
    """
    Type definition for `ClientDescribeSuggestersResponse` `Suggesters`

    The value of a ``Suggester`` and its current status.

    - **Options** *(dict) --*

      Configuration information for a search suggester. Each suggester has a unique name and
      specifies the text field you want to use for suggestions. The following options can be
      configured for a suggester: ``FuzzyMatching`` , ``SortExpression`` .

      - **SuggesterName** *(string) --*

        Names must begin with a letter and can contain the following characters: a-z
        (lowercase), 0-9, and _ (underscore).

      - **DocumentSuggesterOptions** *(dict) --*

        Options for a search suggester.

        - **SourceField** *(string) --*

          The name of the index field you want to use for suggestions.

        - **FuzzyMatching** *(string) --*

          The level of fuzziness allowed when suggesting matches for a string: ``none`` ,
          ``low`` , or ``high`` . With none, the specified string is treated as an exact
          prefix. With low, suggestions must differ from the specified string by no more than
          one character. With high, suggestions can differ by up to two characters. The default
          is none.

        - **SortExpression** *(string) --*

          An expression that computes a score for each suggestion to control how they are
          sorted. The scores are rounded to the nearest integer, with a floor of 0 and a
          ceiling of 2^31-1. A document's relevance score is not computed for suggestions, so
          sort expressions cannot reference the ``_score`` value. To sort suggestions using a
          numeric field or existing expression, simply specify the name of the field or
          expression. If no expression is configured for the suggester, the suggestions are
          sorted with the closest matches listed first.

    - **Status** *(dict) --*

      The status of domain configuration option.

      - **CreationDate** *(datetime) --*

        A timestamp for when this option was created.

      - **UpdateDate** *(datetime) --*

        A timestamp for when this option was last updated.

      - **UpdateVersion** *(integer) --*

        A unique integer that indicates when this option was last updated.

      - **State** *(string) --*

        The state of processing a change to an option. Possible values:

        * ``RequiresIndexDocuments`` : the option's latest value will not be deployed until
        IndexDocuments has been called and indexing is complete.

        * ``Processing`` : the option's latest value is in the process of being activated.

        * ``Active`` : the option's latest value is completely deployed.

        * ``FailedToValidate`` : the option value is not compatible with the domain's data and
        cannot be used to index the data. You must either modify the option value or update or
        remove the incompatible documents.

      - **PendingDeletion** *(boolean) --*

        Indicates that the option will be deleted once processing is complete.
    """


_ClientDescribeSuggestersResponseTypeDef = TypedDict(
    "_ClientDescribeSuggestersResponseTypeDef",
    {"Suggesters": List[ClientDescribeSuggestersResponseSuggestersTypeDef]},
    total=False,
)


class ClientDescribeSuggestersResponseTypeDef(_ClientDescribeSuggestersResponseTypeDef):
    """
    Type definition for `ClientDescribeSuggesters` `Response`

    The result of a ``DescribeSuggesters`` request.

    - **Suggesters** *(list) --*

      The suggesters configured for the domain specified in the request.

      - *(dict) --*

        The value of a ``Suggester`` and its current status.

        - **Options** *(dict) --*

          Configuration information for a search suggester. Each suggester has a unique name and
          specifies the text field you want to use for suggestions. The following options can be
          configured for a suggester: ``FuzzyMatching`` , ``SortExpression`` .

          - **SuggesterName** *(string) --*

            Names must begin with a letter and can contain the following characters: a-z
            (lowercase), 0-9, and _ (underscore).

          - **DocumentSuggesterOptions** *(dict) --*

            Options for a search suggester.

            - **SourceField** *(string) --*

              The name of the index field you want to use for suggestions.

            - **FuzzyMatching** *(string) --*

              The level of fuzziness allowed when suggesting matches for a string: ``none`` ,
              ``low`` , or ``high`` . With none, the specified string is treated as an exact
              prefix. With low, suggestions must differ from the specified string by no more than
              one character. With high, suggestions can differ by up to two characters. The default
              is none.

            - **SortExpression** *(string) --*

              An expression that computes a score for each suggestion to control how they are
              sorted. The scores are rounded to the nearest integer, with a floor of 0 and a
              ceiling of 2^31-1. A document's relevance score is not computed for suggestions, so
              sort expressions cannot reference the ``_score`` value. To sort suggestions using a
              numeric field or existing expression, simply specify the name of the field or
              expression. If no expression is configured for the suggester, the suggestions are
              sorted with the closest matches listed first.

        - **Status** *(dict) --*

          The status of domain configuration option.

          - **CreationDate** *(datetime) --*

            A timestamp for when this option was created.

          - **UpdateDate** *(datetime) --*

            A timestamp for when this option was last updated.

          - **UpdateVersion** *(integer) --*

            A unique integer that indicates when this option was last updated.

          - **State** *(string) --*

            The state of processing a change to an option. Possible values:

            * ``RequiresIndexDocuments`` : the option's latest value will not be deployed until
            IndexDocuments has been called and indexing is complete.

            * ``Processing`` : the option's latest value is in the process of being activated.

            * ``Active`` : the option's latest value is completely deployed.

            * ``FailedToValidate`` : the option value is not compatible with the domain's data and
            cannot be used to index the data. You must either modify the option value or update or
            remove the incompatible documents.

          - **PendingDeletion** *(boolean) --*

            Indicates that the option will be deleted once processing is complete.
    """


_ClientIndexDocumentsResponseTypeDef = TypedDict(
    "_ClientIndexDocumentsResponseTypeDef", {"FieldNames": List[str]}, total=False
)


class ClientIndexDocumentsResponseTypeDef(_ClientIndexDocumentsResponseTypeDef):
    """
    Type definition for `ClientIndexDocuments` `Response`

    The result of an ``IndexDocuments`` request. Contains the status of the indexing operation,
    including the fields being indexed.

    - **FieldNames** *(list) --*

      The names of the fields that are currently being indexed.

      - *(string) --*

        A string that represents the name of an index field. CloudSearch supports regular index
        fields as well as dynamic fields. A dynamic field's name defines a pattern that begins or
        ends with a wildcard. Any document fields that don't map to a regular index field but do
        match a dynamic field's pattern are configured with the dynamic field's indexing options.

        Regular field names begin with a letter and can contain the following characters: a-z
        (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a wildcard
        (*). The wildcard can also be the only character in a dynamic field name. Multiple
        wildcards, and wildcards embedded within a string are not supported.

        The name ``score`` is reserved and cannot be used as a field name. To reference a
        document's ID, you can use the name ``_id`` .
    """


_ClientListDomainNamesResponseTypeDef = TypedDict(
    "_ClientListDomainNamesResponseTypeDef",
    {"DomainNames": Dict[str, str]},
    total=False,
)


class ClientListDomainNamesResponseTypeDef(_ClientListDomainNamesResponseTypeDef):
    """
    Type definition for `ClientListDomainNames` `Response`

    The result of a ``ListDomainNames`` request. Contains a list of the domains owned by an account.

    - **DomainNames** *(dict) --*

      The names of the search domains owned by an account.

      - *(string) --*

        A string that represents the name of a domain. Domain names are unique across the domains
        owned by an account within an AWS region. Domain names start with a letter or number and
        can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).

        - *(string) --*

          The Amazon CloudSearch API version for a domain: 2011-02-01 or 2013-01-01.
    """


_ClientUpdateAvailabilityOptionsResponseAvailabilityOptionsStatusTypeDef = TypedDict(
    "_ClientUpdateAvailabilityOptionsResponseAvailabilityOptionsStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": str,
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientUpdateAvailabilityOptionsResponseAvailabilityOptionsStatusTypeDef(
    _ClientUpdateAvailabilityOptionsResponseAvailabilityOptionsStatusTypeDef
):
    """
    Type definition for `ClientUpdateAvailabilityOptionsResponseAvailabilityOptions` `Status`

    The status of domain configuration option.

    - **CreationDate** *(datetime) --*

      A timestamp for when this option was created.

    - **UpdateDate** *(datetime) --*

      A timestamp for when this option was last updated.

    - **UpdateVersion** *(integer) --*

      A unique integer that indicates when this option was last updated.

    - **State** *(string) --*

      The state of processing a change to an option. Possible values:

      * ``RequiresIndexDocuments`` : the option's latest value will not be deployed until
      IndexDocuments has been called and indexing is complete.

      * ``Processing`` : the option's latest value is in the process of being activated.

      * ``Active`` : the option's latest value is completely deployed.

      * ``FailedToValidate`` : the option value is not compatible with the domain's data and
      cannot be used to index the data. You must either modify the option value or update or
      remove the incompatible documents.

    - **PendingDeletion** *(boolean) --*

      Indicates that the option will be deleted once processing is complete.
    """


_ClientUpdateAvailabilityOptionsResponseAvailabilityOptionsTypeDef = TypedDict(
    "_ClientUpdateAvailabilityOptionsResponseAvailabilityOptionsTypeDef",
    {
        "Options": bool,
        "Status": ClientUpdateAvailabilityOptionsResponseAvailabilityOptionsStatusTypeDef,
    },
    total=False,
)


class ClientUpdateAvailabilityOptionsResponseAvailabilityOptionsTypeDef(
    _ClientUpdateAvailabilityOptionsResponseAvailabilityOptionsTypeDef
):
    """
    Type definition for `ClientUpdateAvailabilityOptionsResponse` `AvailabilityOptions`

    The newly-configured availability options. Indicates whether Multi-AZ is enabled for the
    domain.

    - **Options** *(boolean) --*

      The availability options configured for the domain.

    - **Status** *(dict) --*

      The status of domain configuration option.

      - **CreationDate** *(datetime) --*

        A timestamp for when this option was created.

      - **UpdateDate** *(datetime) --*

        A timestamp for when this option was last updated.

      - **UpdateVersion** *(integer) --*

        A unique integer that indicates when this option was last updated.

      - **State** *(string) --*

        The state of processing a change to an option. Possible values:

        * ``RequiresIndexDocuments`` : the option's latest value will not be deployed until
        IndexDocuments has been called and indexing is complete.

        * ``Processing`` : the option's latest value is in the process of being activated.

        * ``Active`` : the option's latest value is completely deployed.

        * ``FailedToValidate`` : the option value is not compatible with the domain's data and
        cannot be used to index the data. You must either modify the option value or update or
        remove the incompatible documents.

      - **PendingDeletion** *(boolean) --*

        Indicates that the option will be deleted once processing is complete.
    """


_ClientUpdateAvailabilityOptionsResponseTypeDef = TypedDict(
    "_ClientUpdateAvailabilityOptionsResponseTypeDef",
    {
        "AvailabilityOptions": ClientUpdateAvailabilityOptionsResponseAvailabilityOptionsTypeDef
    },
    total=False,
)


class ClientUpdateAvailabilityOptionsResponseTypeDef(
    _ClientUpdateAvailabilityOptionsResponseTypeDef
):
    """
    Type definition for `ClientUpdateAvailabilityOptions` `Response`

    The result of a ``UpdateAvailabilityOptions`` request. Contains the status of the domain's
    availability options.

    - **AvailabilityOptions** *(dict) --*

      The newly-configured availability options. Indicates whether Multi-AZ is enabled for the
      domain.

      - **Options** *(boolean) --*

        The availability options configured for the domain.

      - **Status** *(dict) --*

        The status of domain configuration option.

        - **CreationDate** *(datetime) --*

          A timestamp for when this option was created.

        - **UpdateDate** *(datetime) --*

          A timestamp for when this option was last updated.

        - **UpdateVersion** *(integer) --*

          A unique integer that indicates when this option was last updated.

        - **State** *(string) --*

          The state of processing a change to an option. Possible values:

          * ``RequiresIndexDocuments`` : the option's latest value will not be deployed until
          IndexDocuments has been called and indexing is complete.

          * ``Processing`` : the option's latest value is in the process of being activated.

          * ``Active`` : the option's latest value is completely deployed.

          * ``FailedToValidate`` : the option value is not compatible with the domain's data and
          cannot be used to index the data. You must either modify the option value or update or
          remove the incompatible documents.

        - **PendingDeletion** *(boolean) --*

          Indicates that the option will be deleted once processing is complete.
    """


_ClientUpdateDomainEndpointOptionsDomainEndpointOptionsTypeDef = TypedDict(
    "_ClientUpdateDomainEndpointOptionsDomainEndpointOptionsTypeDef",
    {"EnforceHTTPS": bool, "TLSSecurityPolicy": str},
    total=False,
)


class ClientUpdateDomainEndpointOptionsDomainEndpointOptionsTypeDef(
    _ClientUpdateDomainEndpointOptionsDomainEndpointOptionsTypeDef
):
    """
    Type definition for `ClientUpdateDomainEndpointOptions` `DomainEndpointOptions`

    Whether to require that all requests to the domain arrive over HTTPS. We recommend
    Policy-Min-TLS-1-2-2019-07 for TLSSecurityPolicy. For compatibility with older clients, the
    default is Policy-Min-TLS-1-0-2019-07.

    - **EnforceHTTPS** *(boolean) --*

      Whether the domain is HTTPS only enabled.

    - **TLSSecurityPolicy** *(string) --*

      The minimum required TLS version
    """


_ClientUpdateDomainEndpointOptionsResponseDomainEndpointOptionsOptionsTypeDef = TypedDict(
    "_ClientUpdateDomainEndpointOptionsResponseDomainEndpointOptionsOptionsTypeDef",
    {"EnforceHTTPS": bool, "TLSSecurityPolicy": str},
    total=False,
)


class ClientUpdateDomainEndpointOptionsResponseDomainEndpointOptionsOptionsTypeDef(
    _ClientUpdateDomainEndpointOptionsResponseDomainEndpointOptionsOptionsTypeDef
):
    """
    Type definition for `ClientUpdateDomainEndpointOptionsResponseDomainEndpointOptions` `Options`

    The domain endpoint options configured for the domain.

    - **EnforceHTTPS** *(boolean) --*

      Whether the domain is HTTPS only enabled.

    - **TLSSecurityPolicy** *(string) --*

      The minimum required TLS version
    """


_ClientUpdateDomainEndpointOptionsResponseDomainEndpointOptionsStatusTypeDef = TypedDict(
    "_ClientUpdateDomainEndpointOptionsResponseDomainEndpointOptionsStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": str,
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientUpdateDomainEndpointOptionsResponseDomainEndpointOptionsStatusTypeDef(
    _ClientUpdateDomainEndpointOptionsResponseDomainEndpointOptionsStatusTypeDef
):
    """
    Type definition for `ClientUpdateDomainEndpointOptionsResponseDomainEndpointOptions` `Status`

    The status of the configured domain endpoint options.

    - **CreationDate** *(datetime) --*

      A timestamp for when this option was created.

    - **UpdateDate** *(datetime) --*

      A timestamp for when this option was last updated.

    - **UpdateVersion** *(integer) --*

      A unique integer that indicates when this option was last updated.

    - **State** *(string) --*

      The state of processing a change to an option. Possible values:

      * ``RequiresIndexDocuments`` : the option's latest value will not be deployed until
      IndexDocuments has been called and indexing is complete.

      * ``Processing`` : the option's latest value is in the process of being activated.

      * ``Active`` : the option's latest value is completely deployed.

      * ``FailedToValidate`` : the option value is not compatible with the domain's data and
      cannot be used to index the data. You must either modify the option value or update or
      remove the incompatible documents.

    - **PendingDeletion** *(boolean) --*

      Indicates that the option will be deleted once processing is complete.
    """


_ClientUpdateDomainEndpointOptionsResponseDomainEndpointOptionsTypeDef = TypedDict(
    "_ClientUpdateDomainEndpointOptionsResponseDomainEndpointOptionsTypeDef",
    {
        "Options": ClientUpdateDomainEndpointOptionsResponseDomainEndpointOptionsOptionsTypeDef,
        "Status": ClientUpdateDomainEndpointOptionsResponseDomainEndpointOptionsStatusTypeDef,
    },
    total=False,
)


class ClientUpdateDomainEndpointOptionsResponseDomainEndpointOptionsTypeDef(
    _ClientUpdateDomainEndpointOptionsResponseDomainEndpointOptionsTypeDef
):
    """
    Type definition for `ClientUpdateDomainEndpointOptionsResponse` `DomainEndpointOptions`

    The newly-configured domain endpoint options.

    - **Options** *(dict) --*

      The domain endpoint options configured for the domain.

      - **EnforceHTTPS** *(boolean) --*

        Whether the domain is HTTPS only enabled.

      - **TLSSecurityPolicy** *(string) --*

        The minimum required TLS version

    - **Status** *(dict) --*

      The status of the configured domain endpoint options.

      - **CreationDate** *(datetime) --*

        A timestamp for when this option was created.

      - **UpdateDate** *(datetime) --*

        A timestamp for when this option was last updated.

      - **UpdateVersion** *(integer) --*

        A unique integer that indicates when this option was last updated.

      - **State** *(string) --*

        The state of processing a change to an option. Possible values:

        * ``RequiresIndexDocuments`` : the option's latest value will not be deployed until
        IndexDocuments has been called and indexing is complete.

        * ``Processing`` : the option's latest value is in the process of being activated.

        * ``Active`` : the option's latest value is completely deployed.

        * ``FailedToValidate`` : the option value is not compatible with the domain's data and
        cannot be used to index the data. You must either modify the option value or update or
        remove the incompatible documents.

      - **PendingDeletion** *(boolean) --*

        Indicates that the option will be deleted once processing is complete.
    """


_ClientUpdateDomainEndpointOptionsResponseTypeDef = TypedDict(
    "_ClientUpdateDomainEndpointOptionsResponseTypeDef",
    {
        "DomainEndpointOptions": ClientUpdateDomainEndpointOptionsResponseDomainEndpointOptionsTypeDef
    },
    total=False,
)


class ClientUpdateDomainEndpointOptionsResponseTypeDef(
    _ClientUpdateDomainEndpointOptionsResponseTypeDef
):
    """
    Type definition for `ClientUpdateDomainEndpointOptions` `Response`

    The result of a ``UpdateDomainEndpointOptions`` request. Contains the configuration and status
    of the domain's endpoint options.

    - **DomainEndpointOptions** *(dict) --*

      The newly-configured domain endpoint options.

      - **Options** *(dict) --*

        The domain endpoint options configured for the domain.

        - **EnforceHTTPS** *(boolean) --*

          Whether the domain is HTTPS only enabled.

        - **TLSSecurityPolicy** *(string) --*

          The minimum required TLS version

      - **Status** *(dict) --*

        The status of the configured domain endpoint options.

        - **CreationDate** *(datetime) --*

          A timestamp for when this option was created.

        - **UpdateDate** *(datetime) --*

          A timestamp for when this option was last updated.

        - **UpdateVersion** *(integer) --*

          A unique integer that indicates when this option was last updated.

        - **State** *(string) --*

          The state of processing a change to an option. Possible values:

          * ``RequiresIndexDocuments`` : the option's latest value will not be deployed until
          IndexDocuments has been called and indexing is complete.

          * ``Processing`` : the option's latest value is in the process of being activated.

          * ``Active`` : the option's latest value is completely deployed.

          * ``FailedToValidate`` : the option value is not compatible with the domain's data and
          cannot be used to index the data. You must either modify the option value or update or
          remove the incompatible documents.

        - **PendingDeletion** *(boolean) --*

          Indicates that the option will be deleted once processing is complete.
    """


_ClientUpdateScalingParametersResponseScalingParametersOptionsTypeDef = TypedDict(
    "_ClientUpdateScalingParametersResponseScalingParametersOptionsTypeDef",
    {
        "DesiredInstanceType": str,
        "DesiredReplicationCount": int,
        "DesiredPartitionCount": int,
    },
    total=False,
)


class ClientUpdateScalingParametersResponseScalingParametersOptionsTypeDef(
    _ClientUpdateScalingParametersResponseScalingParametersOptionsTypeDef
):
    """
    Type definition for `ClientUpdateScalingParametersResponseScalingParameters` `Options`

    The desired instance type and desired number of replicas of each index partition.

    - **DesiredInstanceType** *(string) --*

      The instance type that you want to preconfigure for your domain. For example,
      ``search.m1.small`` .

    - **DesiredReplicationCount** *(integer) --*

      The number of replicas you want to preconfigure for each index partition.

    - **DesiredPartitionCount** *(integer) --*

      The number of partitions you want to preconfigure for your domain. Only valid when you
      select ``m2.2xlarge`` as the desired instance type.
    """


_ClientUpdateScalingParametersResponseScalingParametersStatusTypeDef = TypedDict(
    "_ClientUpdateScalingParametersResponseScalingParametersStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": str,
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientUpdateScalingParametersResponseScalingParametersStatusTypeDef(
    _ClientUpdateScalingParametersResponseScalingParametersStatusTypeDef
):
    """
    Type definition for `ClientUpdateScalingParametersResponseScalingParameters` `Status`

    The status of domain configuration option.

    - **CreationDate** *(datetime) --*

      A timestamp for when this option was created.

    - **UpdateDate** *(datetime) --*

      A timestamp for when this option was last updated.

    - **UpdateVersion** *(integer) --*

      A unique integer that indicates when this option was last updated.

    - **State** *(string) --*

      The state of processing a change to an option. Possible values:

      * ``RequiresIndexDocuments`` : the option's latest value will not be deployed until
      IndexDocuments has been called and indexing is complete.

      * ``Processing`` : the option's latest value is in the process of being activated.

      * ``Active`` : the option's latest value is completely deployed.

      * ``FailedToValidate`` : the option value is not compatible with the domain's data and
      cannot be used to index the data. You must either modify the option value or update or
      remove the incompatible documents.

    - **PendingDeletion** *(boolean) --*

      Indicates that the option will be deleted once processing is complete.
    """


_ClientUpdateScalingParametersResponseScalingParametersTypeDef = TypedDict(
    "_ClientUpdateScalingParametersResponseScalingParametersTypeDef",
    {
        "Options": ClientUpdateScalingParametersResponseScalingParametersOptionsTypeDef,
        "Status": ClientUpdateScalingParametersResponseScalingParametersStatusTypeDef,
    },
    total=False,
)


class ClientUpdateScalingParametersResponseScalingParametersTypeDef(
    _ClientUpdateScalingParametersResponseScalingParametersTypeDef
):
    """
    Type definition for `ClientUpdateScalingParametersResponse` `ScalingParameters`

    The status and configuration of a search domain's scaling parameters.

    - **Options** *(dict) --*

      The desired instance type and desired number of replicas of each index partition.

      - **DesiredInstanceType** *(string) --*

        The instance type that you want to preconfigure for your domain. For example,
        ``search.m1.small`` .

      - **DesiredReplicationCount** *(integer) --*

        The number of replicas you want to preconfigure for each index partition.

      - **DesiredPartitionCount** *(integer) --*

        The number of partitions you want to preconfigure for your domain. Only valid when you
        select ``m2.2xlarge`` as the desired instance type.

    - **Status** *(dict) --*

      The status of domain configuration option.

      - **CreationDate** *(datetime) --*

        A timestamp for when this option was created.

      - **UpdateDate** *(datetime) --*

        A timestamp for when this option was last updated.

      - **UpdateVersion** *(integer) --*

        A unique integer that indicates when this option was last updated.

      - **State** *(string) --*

        The state of processing a change to an option. Possible values:

        * ``RequiresIndexDocuments`` : the option's latest value will not be deployed until
        IndexDocuments has been called and indexing is complete.

        * ``Processing`` : the option's latest value is in the process of being activated.

        * ``Active`` : the option's latest value is completely deployed.

        * ``FailedToValidate`` : the option value is not compatible with the domain's data and
        cannot be used to index the data. You must either modify the option value or update or
        remove the incompatible documents.

      - **PendingDeletion** *(boolean) --*

        Indicates that the option will be deleted once processing is complete.
    """


_ClientUpdateScalingParametersResponseTypeDef = TypedDict(
    "_ClientUpdateScalingParametersResponseTypeDef",
    {
        "ScalingParameters": ClientUpdateScalingParametersResponseScalingParametersTypeDef
    },
    total=False,
)


class ClientUpdateScalingParametersResponseTypeDef(
    _ClientUpdateScalingParametersResponseTypeDef
):
    """
    Type definition for `ClientUpdateScalingParameters` `Response`

    The result of a ``UpdateScalingParameters`` request. Contains the status of the
    newly-configured scaling parameters.

    - **ScalingParameters** *(dict) --*

      The status and configuration of a search domain's scaling parameters.

      - **Options** *(dict) --*

        The desired instance type and desired number of replicas of each index partition.

        - **DesiredInstanceType** *(string) --*

          The instance type that you want to preconfigure for your domain. For example,
          ``search.m1.small`` .

        - **DesiredReplicationCount** *(integer) --*

          The number of replicas you want to preconfigure for each index partition.

        - **DesiredPartitionCount** *(integer) --*

          The number of partitions you want to preconfigure for your domain. Only valid when you
          select ``m2.2xlarge`` as the desired instance type.

      - **Status** *(dict) --*

        The status of domain configuration option.

        - **CreationDate** *(datetime) --*

          A timestamp for when this option was created.

        - **UpdateDate** *(datetime) --*

          A timestamp for when this option was last updated.

        - **UpdateVersion** *(integer) --*

          A unique integer that indicates when this option was last updated.

        - **State** *(string) --*

          The state of processing a change to an option. Possible values:

          * ``RequiresIndexDocuments`` : the option's latest value will not be deployed until
          IndexDocuments has been called and indexing is complete.

          * ``Processing`` : the option's latest value is in the process of being activated.

          * ``Active`` : the option's latest value is completely deployed.

          * ``FailedToValidate`` : the option value is not compatible with the domain's data and
          cannot be used to index the data. You must either modify the option value or update or
          remove the incompatible documents.

        - **PendingDeletion** *(boolean) --*

          Indicates that the option will be deleted once processing is complete.
    """


_ClientUpdateScalingParametersScalingParametersTypeDef = TypedDict(
    "_ClientUpdateScalingParametersScalingParametersTypeDef",
    {
        "DesiredInstanceType": str,
        "DesiredReplicationCount": int,
        "DesiredPartitionCount": int,
    },
    total=False,
)


class ClientUpdateScalingParametersScalingParametersTypeDef(
    _ClientUpdateScalingParametersScalingParametersTypeDef
):
    """
    Type definition for `ClientUpdateScalingParameters` `ScalingParameters`

    The desired instance type and desired number of replicas of each index partition.

    - **DesiredInstanceType** *(string) --*

      The instance type that you want to preconfigure for your domain. For example,
      ``search.m1.small`` .

    - **DesiredReplicationCount** *(integer) --*

      The number of replicas you want to preconfigure for each index partition.

    - **DesiredPartitionCount** *(integer) --*

      The number of partitions you want to preconfigure for your domain. Only valid when you select
      ``m2.2xlarge`` as the desired instance type.
    """


_ClientUpdateServiceAccessPoliciesResponseAccessPoliciesStatusTypeDef = TypedDict(
    "_ClientUpdateServiceAccessPoliciesResponseAccessPoliciesStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": str,
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientUpdateServiceAccessPoliciesResponseAccessPoliciesStatusTypeDef(
    _ClientUpdateServiceAccessPoliciesResponseAccessPoliciesStatusTypeDef
):
    """
    Type definition for `ClientUpdateServiceAccessPoliciesResponseAccessPolicies` `Status`

    The status of domain configuration option.

    - **CreationDate** *(datetime) --*

      A timestamp for when this option was created.

    - **UpdateDate** *(datetime) --*

      A timestamp for when this option was last updated.

    - **UpdateVersion** *(integer) --*

      A unique integer that indicates when this option was last updated.

    - **State** *(string) --*

      The state of processing a change to an option. Possible values:

      * ``RequiresIndexDocuments`` : the option's latest value will not be deployed until
      IndexDocuments has been called and indexing is complete.

      * ``Processing`` : the option's latest value is in the process of being activated.

      * ``Active`` : the option's latest value is completely deployed.

      * ``FailedToValidate`` : the option value is not compatible with the domain's data and
      cannot be used to index the data. You must either modify the option value or update or
      remove the incompatible documents.

    - **PendingDeletion** *(boolean) --*

      Indicates that the option will be deleted once processing is complete.
    """


_ClientUpdateServiceAccessPoliciesResponseAccessPoliciesTypeDef = TypedDict(
    "_ClientUpdateServiceAccessPoliciesResponseAccessPoliciesTypeDef",
    {
        "Options": str,
        "Status": ClientUpdateServiceAccessPoliciesResponseAccessPoliciesStatusTypeDef,
    },
    total=False,
)


class ClientUpdateServiceAccessPoliciesResponseAccessPoliciesTypeDef(
    _ClientUpdateServiceAccessPoliciesResponseAccessPoliciesTypeDef
):
    """
    Type definition for `ClientUpdateServiceAccessPoliciesResponse` `AccessPolicies`

    The access rules configured for the domain.

    - **Options** *(string) --*

      Access rules for a domain's document or search service endpoints. For more information, see
      `Configuring Access for a Search Domain
      <http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-access.html>`__
      in the *Amazon CloudSearch Developer Guide* . The maximum size of a policy document is 100
      KB.

    - **Status** *(dict) --*

      The status of domain configuration option.

      - **CreationDate** *(datetime) --*

        A timestamp for when this option was created.

      - **UpdateDate** *(datetime) --*

        A timestamp for when this option was last updated.

      - **UpdateVersion** *(integer) --*

        A unique integer that indicates when this option was last updated.

      - **State** *(string) --*

        The state of processing a change to an option. Possible values:

        * ``RequiresIndexDocuments`` : the option's latest value will not be deployed until
        IndexDocuments has been called and indexing is complete.

        * ``Processing`` : the option's latest value is in the process of being activated.

        * ``Active`` : the option's latest value is completely deployed.

        * ``FailedToValidate`` : the option value is not compatible with the domain's data and
        cannot be used to index the data. You must either modify the option value or update or
        remove the incompatible documents.

      - **PendingDeletion** *(boolean) --*

        Indicates that the option will be deleted once processing is complete.
    """


_ClientUpdateServiceAccessPoliciesResponseTypeDef = TypedDict(
    "_ClientUpdateServiceAccessPoliciesResponseTypeDef",
    {"AccessPolicies": ClientUpdateServiceAccessPoliciesResponseAccessPoliciesTypeDef},
    total=False,
)


class ClientUpdateServiceAccessPoliciesResponseTypeDef(
    _ClientUpdateServiceAccessPoliciesResponseTypeDef
):
    """
    Type definition for `ClientUpdateServiceAccessPolicies` `Response`

    The result of an ``UpdateServiceAccessPolicies`` request. Contains the new access policies.

    - **AccessPolicies** *(dict) --*

      The access rules configured for the domain.

      - **Options** *(string) --*

        Access rules for a domain's document or search service endpoints. For more information, see
        `Configuring Access for a Search Domain
        <http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-access.html>`__
        in the *Amazon CloudSearch Developer Guide* . The maximum size of a policy document is 100
        KB.

      - **Status** *(dict) --*

        The status of domain configuration option.

        - **CreationDate** *(datetime) --*

          A timestamp for when this option was created.

        - **UpdateDate** *(datetime) --*

          A timestamp for when this option was last updated.

        - **UpdateVersion** *(integer) --*

          A unique integer that indicates when this option was last updated.

        - **State** *(string) --*

          The state of processing a change to an option. Possible values:

          * ``RequiresIndexDocuments`` : the option's latest value will not be deployed until
          IndexDocuments has been called and indexing is complete.

          * ``Processing`` : the option's latest value is in the process of being activated.

          * ``Active`` : the option's latest value is completely deployed.

          * ``FailedToValidate`` : the option value is not compatible with the domain's data and
          cannot be used to index the data. You must either modify the option value or update or
          remove the incompatible documents.

        - **PendingDeletion** *(boolean) --*

          Indicates that the option will be deleted once processing is complete.
    """
