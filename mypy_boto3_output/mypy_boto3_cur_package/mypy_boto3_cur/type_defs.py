"Main interface for cur type defs"
from __future__ import annotations

from typing import List
from typing_extensions import TypedDict


__all__ = (
    "ClientDeleteReportDefinitionResponseTypeDef",
    "ClientDescribeReportDefinitionsResponseReportDefinitionsTypeDef",
    "ClientDescribeReportDefinitionsResponseTypeDef",
    "ClientModifyReportDefinitionReportDefinitionTypeDef",
    "ClientPutReportDefinitionReportDefinitionTypeDef",
    "DescribeReportDefinitionsPaginatePaginationConfigTypeDef",
    "DescribeReportDefinitionsPaginateResponseReportDefinitionsTypeDef",
    "DescribeReportDefinitionsPaginateResponseTypeDef",
)


_ClientDeleteReportDefinitionResponseTypeDef = TypedDict(
    "_ClientDeleteReportDefinitionResponseTypeDef",
    {"ResponseMessage": str},
    total=False,
)


class ClientDeleteReportDefinitionResponseTypeDef(
    _ClientDeleteReportDefinitionResponseTypeDef
):
    """
    Type definition for `ClientDeleteReportDefinition` `Response`

    If the action is successful, the service sends back an HTTP 200 response.

    - **ResponseMessage** *(string) --*

      Whether the deletion was successful or not.
    """


_ClientDescribeReportDefinitionsResponseReportDefinitionsTypeDef = TypedDict(
    "_ClientDescribeReportDefinitionsResponseReportDefinitionsTypeDef",
    {
        "ReportName": str,
        "TimeUnit": str,
        "Format": str,
        "Compression": str,
        "AdditionalSchemaElements": List[str],
        "S3Bucket": str,
        "S3Prefix": str,
        "S3Region": str,
        "AdditionalArtifacts": List[str],
        "RefreshClosedReports": bool,
        "ReportVersioning": str,
    },
    total=False,
)


class ClientDescribeReportDefinitionsResponseReportDefinitionsTypeDef(
    _ClientDescribeReportDefinitionsResponseReportDefinitionsTypeDef
):
    """
    Type definition for `ClientDescribeReportDefinitionsResponse` `ReportDefinitions`

    The definition of AWS Cost and Usage Report. You can specify the report name, time unit,
    report format, compression format, S3 bucket, additional artifacts, and schema elements in
    the definition.

    - **ReportName** *(string) --*

      The name of the report that you want to create. The name must be unique, is case
      sensitive, and can't include spaces.

    - **TimeUnit** *(string) --*

      The length of time covered by the report.

    - **Format** *(string) --*

      The format that AWS saves the report in.

    - **Compression** *(string) --*

      The compression format that AWS uses for the report.

    - **AdditionalSchemaElements** *(list) --*

      A list of strings that indicate additional content that Amazon Web Services includes in
      the report, such as individual resource IDs.

      - *(string) --*

        Whether or not AWS includes resource IDs in the report.

    - **S3Bucket** *(string) --*

      The S3 bucket where AWS delivers the report.

    - **S3Prefix** *(string) --*

      The prefix that AWS adds to the report name when AWS delivers the report. Your prefix
      can't include spaces.

    - **S3Region** *(string) --*

      The region of the S3 bucket that AWS delivers the report into.

    - **AdditionalArtifacts** *(list) --*

      A list of manifests that you want Amazon Web Services to create for this report.

      - *(string) --*

        The types of manifest that you want AWS to create for this report.

    - **RefreshClosedReports** *(boolean) --*

      Whether you want Amazon Web Services to update your reports after they have been
      finalized if Amazon Web Services detects charges related to previous months. These
      charges can include refunds, credits, or support fees.

    - **ReportVersioning** *(string) --*

      Whether you want Amazon Web Services to overwrite the previous version of each report or
      to deliver the report in addition to the previous versions.
    """


_ClientDescribeReportDefinitionsResponseTypeDef = TypedDict(
    "_ClientDescribeReportDefinitionsResponseTypeDef",
    {
        "ReportDefinitions": List[
            ClientDescribeReportDefinitionsResponseReportDefinitionsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeReportDefinitionsResponseTypeDef(
    _ClientDescribeReportDefinitionsResponseTypeDef
):
    """
    Type definition for `ClientDescribeReportDefinitions` `Response`

    If the action is successful, the service sends back an HTTP 200 response.

    - **ReportDefinitions** *(list) --*

      A list of AWS Cost and Usage reports owned by the account.

      - *(dict) --*

        The definition of AWS Cost and Usage Report. You can specify the report name, time unit,
        report format, compression format, S3 bucket, additional artifacts, and schema elements in
        the definition.

        - **ReportName** *(string) --*

          The name of the report that you want to create. The name must be unique, is case
          sensitive, and can't include spaces.

        - **TimeUnit** *(string) --*

          The length of time covered by the report.

        - **Format** *(string) --*

          The format that AWS saves the report in.

        - **Compression** *(string) --*

          The compression format that AWS uses for the report.

        - **AdditionalSchemaElements** *(list) --*

          A list of strings that indicate additional content that Amazon Web Services includes in
          the report, such as individual resource IDs.

          - *(string) --*

            Whether or not AWS includes resource IDs in the report.

        - **S3Bucket** *(string) --*

          The S3 bucket where AWS delivers the report.

        - **S3Prefix** *(string) --*

          The prefix that AWS adds to the report name when AWS delivers the report. Your prefix
          can't include spaces.

        - **S3Region** *(string) --*

          The region of the S3 bucket that AWS delivers the report into.

        - **AdditionalArtifacts** *(list) --*

          A list of manifests that you want Amazon Web Services to create for this report.

          - *(string) --*

            The types of manifest that you want AWS to create for this report.

        - **RefreshClosedReports** *(boolean) --*

          Whether you want Amazon Web Services to update your reports after they have been
          finalized if Amazon Web Services detects charges related to previous months. These
          charges can include refunds, credits, or support fees.

        - **ReportVersioning** *(string) --*

          Whether you want Amazon Web Services to overwrite the previous version of each report or
          to deliver the report in addition to the previous versions.

    - **NextToken** *(string) --*

      A generic string.
    """


_RequiredClientModifyReportDefinitionReportDefinitionTypeDef = TypedDict(
    "_RequiredClientModifyReportDefinitionReportDefinitionTypeDef",
    {
        "ReportName": str,
        "TimeUnit": str,
        "Format": str,
        "Compression": str,
        "AdditionalSchemaElements": List[str],
        "S3Bucket": str,
        "S3Prefix": str,
        "S3Region": str,
    },
)
_OptionalClientModifyReportDefinitionReportDefinitionTypeDef = TypedDict(
    "_OptionalClientModifyReportDefinitionReportDefinitionTypeDef",
    {
        "AdditionalArtifacts": List[str],
        "RefreshClosedReports": bool,
        "ReportVersioning": str,
    },
    total=False,
)


class ClientModifyReportDefinitionReportDefinitionTypeDef(
    _RequiredClientModifyReportDefinitionReportDefinitionTypeDef,
    _OptionalClientModifyReportDefinitionReportDefinitionTypeDef,
):
    """
    Type definition for `ClientModifyReportDefinition` `ReportDefinition`

    The definition of AWS Cost and Usage Report. You can specify the report name, time unit, report
    format, compression format, S3 bucket, additional artifacts, and schema elements in the
    definition.

    - **ReportName** *(string) --* **[REQUIRED]**

      The name of the report that you want to create. The name must be unique, is case sensitive, and
      can't include spaces.

    - **TimeUnit** *(string) --* **[REQUIRED]**

      The length of time covered by the report.

    - **Format** *(string) --* **[REQUIRED]**

      The format that AWS saves the report in.

    - **Compression** *(string) --* **[REQUIRED]**

      The compression format that AWS uses for the report.

    - **AdditionalSchemaElements** *(list) --* **[REQUIRED]**

      A list of strings that indicate additional content that Amazon Web Services includes in the
      report, such as individual resource IDs.

      - *(string) --*

        Whether or not AWS includes resource IDs in the report.

    - **S3Bucket** *(string) --* **[REQUIRED]**

      The S3 bucket where AWS delivers the report.

    - **S3Prefix** *(string) --* **[REQUIRED]**

      The prefix that AWS adds to the report name when AWS delivers the report. Your prefix can't
      include spaces.

    - **S3Region** *(string) --* **[REQUIRED]**

      The region of the S3 bucket that AWS delivers the report into.

    - **AdditionalArtifacts** *(list) --*

      A list of manifests that you want Amazon Web Services to create for this report.

      - *(string) --*

        The types of manifest that you want AWS to create for this report.

    - **RefreshClosedReports** *(boolean) --*

      Whether you want Amazon Web Services to update your reports after they have been finalized if
      Amazon Web Services detects charges related to previous months. These charges can include
      refunds, credits, or support fees.

    - **ReportVersioning** *(string) --*

      Whether you want Amazon Web Services to overwrite the previous version of each report or to
      deliver the report in addition to the previous versions.
    """


_RequiredClientPutReportDefinitionReportDefinitionTypeDef = TypedDict(
    "_RequiredClientPutReportDefinitionReportDefinitionTypeDef",
    {
        "ReportName": str,
        "TimeUnit": str,
        "Format": str,
        "Compression": str,
        "AdditionalSchemaElements": List[str],
        "S3Bucket": str,
        "S3Prefix": str,
        "S3Region": str,
    },
)
_OptionalClientPutReportDefinitionReportDefinitionTypeDef = TypedDict(
    "_OptionalClientPutReportDefinitionReportDefinitionTypeDef",
    {
        "AdditionalArtifacts": List[str],
        "RefreshClosedReports": bool,
        "ReportVersioning": str,
    },
    total=False,
)


class ClientPutReportDefinitionReportDefinitionTypeDef(
    _RequiredClientPutReportDefinitionReportDefinitionTypeDef,
    _OptionalClientPutReportDefinitionReportDefinitionTypeDef,
):
    """
    Type definition for `ClientPutReportDefinition` `ReportDefinition`

    Represents the output of the PutReportDefinition operation. The content consists of the detailed
    metadata and data file information.

    - **ReportName** *(string) --* **[REQUIRED]**

      The name of the report that you want to create. The name must be unique, is case sensitive, and
      can't include spaces.

    - **TimeUnit** *(string) --* **[REQUIRED]**

      The length of time covered by the report.

    - **Format** *(string) --* **[REQUIRED]**

      The format that AWS saves the report in.

    - **Compression** *(string) --* **[REQUIRED]**

      The compression format that AWS uses for the report.

    - **AdditionalSchemaElements** *(list) --* **[REQUIRED]**

      A list of strings that indicate additional content that Amazon Web Services includes in the
      report, such as individual resource IDs.

      - *(string) --*

        Whether or not AWS includes resource IDs in the report.

    - **S3Bucket** *(string) --* **[REQUIRED]**

      The S3 bucket where AWS delivers the report.

    - **S3Prefix** *(string) --* **[REQUIRED]**

      The prefix that AWS adds to the report name when AWS delivers the report. Your prefix can't
      include spaces.

    - **S3Region** *(string) --* **[REQUIRED]**

      The region of the S3 bucket that AWS delivers the report into.

    - **AdditionalArtifacts** *(list) --*

      A list of manifests that you want Amazon Web Services to create for this report.

      - *(string) --*

        The types of manifest that you want AWS to create for this report.

    - **RefreshClosedReports** *(boolean) --*

      Whether you want Amazon Web Services to update your reports after they have been finalized if
      Amazon Web Services detects charges related to previous months. These charges can include
      refunds, credits, or support fees.

    - **ReportVersioning** *(string) --*

      Whether you want Amazon Web Services to overwrite the previous version of each report or to
      deliver the report in addition to the previous versions.
    """


_DescribeReportDefinitionsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeReportDefinitionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeReportDefinitionsPaginatePaginationConfigTypeDef(
    _DescribeReportDefinitionsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeReportDefinitionsPaginate` `PaginationConfig`

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


_DescribeReportDefinitionsPaginateResponseReportDefinitionsTypeDef = TypedDict(
    "_DescribeReportDefinitionsPaginateResponseReportDefinitionsTypeDef",
    {
        "ReportName": str,
        "TimeUnit": str,
        "Format": str,
        "Compression": str,
        "AdditionalSchemaElements": List[str],
        "S3Bucket": str,
        "S3Prefix": str,
        "S3Region": str,
        "AdditionalArtifacts": List[str],
        "RefreshClosedReports": bool,
        "ReportVersioning": str,
    },
    total=False,
)


class DescribeReportDefinitionsPaginateResponseReportDefinitionsTypeDef(
    _DescribeReportDefinitionsPaginateResponseReportDefinitionsTypeDef
):
    """
    Type definition for `DescribeReportDefinitionsPaginateResponse` `ReportDefinitions`

    The definition of AWS Cost and Usage Report. You can specify the report name, time unit,
    report format, compression format, S3 bucket, additional artifacts, and schema elements in
    the definition.

    - **ReportName** *(string) --*

      The name of the report that you want to create. The name must be unique, is case
      sensitive, and can't include spaces.

    - **TimeUnit** *(string) --*

      The length of time covered by the report.

    - **Format** *(string) --*

      The format that AWS saves the report in.

    - **Compression** *(string) --*

      The compression format that AWS uses for the report.

    - **AdditionalSchemaElements** *(list) --*

      A list of strings that indicate additional content that Amazon Web Services includes in
      the report, such as individual resource IDs.

      - *(string) --*

        Whether or not AWS includes resource IDs in the report.

    - **S3Bucket** *(string) --*

      The S3 bucket where AWS delivers the report.

    - **S3Prefix** *(string) --*

      The prefix that AWS adds to the report name when AWS delivers the report. Your prefix
      can't include spaces.

    - **S3Region** *(string) --*

      The region of the S3 bucket that AWS delivers the report into.

    - **AdditionalArtifacts** *(list) --*

      A list of manifests that you want Amazon Web Services to create for this report.

      - *(string) --*

        The types of manifest that you want AWS to create for this report.

    - **RefreshClosedReports** *(boolean) --*

      Whether you want Amazon Web Services to update your reports after they have been
      finalized if Amazon Web Services detects charges related to previous months. These
      charges can include refunds, credits, or support fees.

    - **ReportVersioning** *(string) --*

      Whether you want Amazon Web Services to overwrite the previous version of each report or
      to deliver the report in addition to the previous versions.
    """


_DescribeReportDefinitionsPaginateResponseTypeDef = TypedDict(
    "_DescribeReportDefinitionsPaginateResponseTypeDef",
    {
        "ReportDefinitions": List[
            DescribeReportDefinitionsPaginateResponseReportDefinitionsTypeDef
        ]
    },
    total=False,
)


class DescribeReportDefinitionsPaginateResponseTypeDef(
    _DescribeReportDefinitionsPaginateResponseTypeDef
):
    """
    Type definition for `DescribeReportDefinitionsPaginate` `Response`

    If the action is successful, the service sends back an HTTP 200 response.

    - **ReportDefinitions** *(list) --*

      A list of AWS Cost and Usage reports owned by the account.

      - *(dict) --*

        The definition of AWS Cost and Usage Report. You can specify the report name, time unit,
        report format, compression format, S3 bucket, additional artifacts, and schema elements in
        the definition.

        - **ReportName** *(string) --*

          The name of the report that you want to create. The name must be unique, is case
          sensitive, and can't include spaces.

        - **TimeUnit** *(string) --*

          The length of time covered by the report.

        - **Format** *(string) --*

          The format that AWS saves the report in.

        - **Compression** *(string) --*

          The compression format that AWS uses for the report.

        - **AdditionalSchemaElements** *(list) --*

          A list of strings that indicate additional content that Amazon Web Services includes in
          the report, such as individual resource IDs.

          - *(string) --*

            Whether or not AWS includes resource IDs in the report.

        - **S3Bucket** *(string) --*

          The S3 bucket where AWS delivers the report.

        - **S3Prefix** *(string) --*

          The prefix that AWS adds to the report name when AWS delivers the report. Your prefix
          can't include spaces.

        - **S3Region** *(string) --*

          The region of the S3 bucket that AWS delivers the report into.

        - **AdditionalArtifacts** *(list) --*

          A list of manifests that you want Amazon Web Services to create for this report.

          - *(string) --*

            The types of manifest that you want AWS to create for this report.

        - **RefreshClosedReports** *(boolean) --*

          Whether you want Amazon Web Services to update your reports after they have been
          finalized if Amazon Web Services detects charges related to previous months. These
          charges can include refunds, credits, or support fees.

        - **ReportVersioning** *(string) --*

          Whether you want Amazon Web Services to overwrite the previous version of each report or
          to deliver the report in addition to the previous versions.
    """
