"Main interface for kinesisanalytics type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from typing_extensions import TypedDict


__all__ = (
    "ClientAddApplicationCloudWatchLoggingOptionCloudWatchLoggingOptionTypeDef",
    "ClientAddApplicationInputInputInputParallelismTypeDef",
    "ClientAddApplicationInputInputInputProcessingConfigurationInputLambdaProcessorTypeDef",
    "ClientAddApplicationInputInputInputProcessingConfigurationTypeDef",
    "ClientAddApplicationInputInputInputSchemaRecordColumnsTypeDef",
    "ClientAddApplicationInputInputInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef",
    "ClientAddApplicationInputInputInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef",
    "ClientAddApplicationInputInputInputSchemaRecordFormatMappingParametersTypeDef",
    "ClientAddApplicationInputInputInputSchemaRecordFormatTypeDef",
    "ClientAddApplicationInputInputInputSchemaTypeDef",
    "ClientAddApplicationInputInputKinesisFirehoseInputTypeDef",
    "ClientAddApplicationInputInputKinesisStreamsInputTypeDef",
    "ClientAddApplicationInputInputTypeDef",
    "ClientAddApplicationInputProcessingConfigurationInputProcessingConfigurationInputLambdaProcessorTypeDef",
    "ClientAddApplicationInputProcessingConfigurationInputProcessingConfigurationTypeDef",
    "ClientAddApplicationOutputOutputDestinationSchemaTypeDef",
    "ClientAddApplicationOutputOutputKinesisFirehoseOutputTypeDef",
    "ClientAddApplicationOutputOutputKinesisStreamsOutputTypeDef",
    "ClientAddApplicationOutputOutputLambdaOutputTypeDef",
    "ClientAddApplicationOutputOutputTypeDef",
    "ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordColumnsTypeDef",
    "ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef",
    "ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef",
    "ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordFormatMappingParametersTypeDef",
    "ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordFormatTypeDef",
    "ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaTypeDef",
    "ClientAddApplicationReferenceDataSourceReferenceDataSourceS3ReferenceDataSourceTypeDef",
    "ClientAddApplicationReferenceDataSourceReferenceDataSourceTypeDef",
    "ClientCreateApplicationCloudWatchLoggingOptionsTypeDef",
    "ClientCreateApplicationInputsInputParallelismTypeDef",
    "ClientCreateApplicationInputsInputProcessingConfigurationInputLambdaProcessorTypeDef",
    "ClientCreateApplicationInputsInputProcessingConfigurationTypeDef",
    "ClientCreateApplicationInputsInputSchemaRecordColumnsTypeDef",
    "ClientCreateApplicationInputsInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef",
    "ClientCreateApplicationInputsInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef",
    "ClientCreateApplicationInputsInputSchemaRecordFormatMappingParametersTypeDef",
    "ClientCreateApplicationInputsInputSchemaRecordFormatTypeDef",
    "ClientCreateApplicationInputsInputSchemaTypeDef",
    "ClientCreateApplicationInputsKinesisFirehoseInputTypeDef",
    "ClientCreateApplicationInputsKinesisStreamsInputTypeDef",
    "ClientCreateApplicationInputsTypeDef",
    "ClientCreateApplicationOutputsDestinationSchemaTypeDef",
    "ClientCreateApplicationOutputsKinesisFirehoseOutputTypeDef",
    "ClientCreateApplicationOutputsKinesisStreamsOutputTypeDef",
    "ClientCreateApplicationOutputsLambdaOutputTypeDef",
    "ClientCreateApplicationOutputsTypeDef",
    "ClientCreateApplicationResponseApplicationSummaryTypeDef",
    "ClientCreateApplicationResponseTypeDef",
    "ClientCreateApplicationTagsTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailCloudWatchLoggingOptionDescriptionsTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputParallelismTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputProcessingConfigurationDescriptionInputLambdaProcessorDescriptionTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputProcessingConfigurationDescriptionTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordColumnsTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordFormatMappingParametersTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordFormatTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputStartingPositionConfigurationTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailInputDescriptionsKinesisFirehoseInputDescriptionTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailInputDescriptionsKinesisStreamsInputDescriptionTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailInputDescriptionsTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsDestinationSchemaTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsKinesisFirehoseOutputDescriptionTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsKinesisStreamsOutputDescriptionTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsLambdaOutputDescriptionTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordColumnsTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordFormatTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsS3ReferenceDataSourceDescriptionTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailTypeDef",
    "ClientDescribeApplicationResponseTypeDef",
    "ClientDiscoverInputSchemaInputProcessingConfigurationInputLambdaProcessorTypeDef",
    "ClientDiscoverInputSchemaInputProcessingConfigurationTypeDef",
    "ClientDiscoverInputSchemaInputStartingPositionConfigurationTypeDef",
    "ClientDiscoverInputSchemaResponseInputSchemaRecordColumnsTypeDef",
    "ClientDiscoverInputSchemaResponseInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef",
    "ClientDiscoverInputSchemaResponseInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef",
    "ClientDiscoverInputSchemaResponseInputSchemaRecordFormatMappingParametersTypeDef",
    "ClientDiscoverInputSchemaResponseInputSchemaRecordFormatTypeDef",
    "ClientDiscoverInputSchemaResponseInputSchemaTypeDef",
    "ClientDiscoverInputSchemaResponseTypeDef",
    "ClientDiscoverInputSchemaS3ConfigurationTypeDef",
    "ClientListApplicationsResponseApplicationSummariesTypeDef",
    "ClientListApplicationsResponseTypeDef",
    "ClientListTagsForResourceResponseTagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientStartApplicationInputConfigurationsInputStartingPositionConfigurationTypeDef",
    "ClientStartApplicationInputConfigurationsTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientUpdateApplicationApplicationUpdateCloudWatchLoggingOptionUpdatesTypeDef",
    "ClientUpdateApplicationApplicationUpdateInputUpdatesInputParallelismUpdateTypeDef",
    "ClientUpdateApplicationApplicationUpdateInputUpdatesInputProcessingConfigurationUpdateInputLambdaProcessorUpdateTypeDef",
    "ClientUpdateApplicationApplicationUpdateInputUpdatesInputProcessingConfigurationUpdateTypeDef",
    "ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordColumnUpdatesTypeDef",
    "ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateMappingParametersCSVMappingParametersTypeDef",
    "ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateMappingParametersJSONMappingParametersTypeDef",
    "ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateMappingParametersTypeDef",
    "ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateTypeDef",
    "ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateTypeDef",
    "ClientUpdateApplicationApplicationUpdateInputUpdatesKinesisFirehoseInputUpdateTypeDef",
    "ClientUpdateApplicationApplicationUpdateInputUpdatesKinesisStreamsInputUpdateTypeDef",
    "ClientUpdateApplicationApplicationUpdateInputUpdatesTypeDef",
    "ClientUpdateApplicationApplicationUpdateOutputUpdatesDestinationSchemaUpdateTypeDef",
    "ClientUpdateApplicationApplicationUpdateOutputUpdatesKinesisFirehoseOutputUpdateTypeDef",
    "ClientUpdateApplicationApplicationUpdateOutputUpdatesKinesisStreamsOutputUpdateTypeDef",
    "ClientUpdateApplicationApplicationUpdateOutputUpdatesLambdaOutputUpdateTypeDef",
    "ClientUpdateApplicationApplicationUpdateOutputUpdatesTypeDef",
    "ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordColumnsTypeDef",
    "ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatMappingParametersCSVMappingParametersTypeDef",
    "ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatMappingParametersJSONMappingParametersTypeDef",
    "ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatMappingParametersTypeDef",
    "ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatTypeDef",
    "ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateTypeDef",
    "ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesS3ReferenceDataSourceUpdateTypeDef",
    "ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesTypeDef",
    "ClientUpdateApplicationApplicationUpdateTypeDef",
)


_ClientAddApplicationCloudWatchLoggingOptionCloudWatchLoggingOptionTypeDef = TypedDict(
    "_ClientAddApplicationCloudWatchLoggingOptionCloudWatchLoggingOptionTypeDef",
    {"LogStreamARN": str, "RoleARN": str},
)


class ClientAddApplicationCloudWatchLoggingOptionCloudWatchLoggingOptionTypeDef(
    _ClientAddApplicationCloudWatchLoggingOptionCloudWatchLoggingOptionTypeDef
):
    """
    Type definition for `ClientAddApplicationCloudWatchLoggingOption` `CloudWatchLoggingOption`

    Provides the CloudWatch log stream Amazon Resource Name (ARN) and the IAM role ARN. Note: To
    write application messages to CloudWatch, the IAM role that is used must have the
    ``PutLogEvents`` policy action enabled.

    - **LogStreamARN** *(string) --* **[REQUIRED]**

      ARN of the CloudWatch log to receive application messages.

    - **RoleARN** *(string) --* **[REQUIRED]**

      IAM ARN of the role to use to send application messages. Note: To write application messages to
      CloudWatch, the IAM role that is used must have the ``PutLogEvents`` policy action enabled.
    """


_ClientAddApplicationInputInputInputParallelismTypeDef = TypedDict(
    "_ClientAddApplicationInputInputInputParallelismTypeDef",
    {"Count": int},
    total=False,
)


class ClientAddApplicationInputInputInputParallelismTypeDef(
    _ClientAddApplicationInputInputInputParallelismTypeDef
):
    """
    Type definition for `ClientAddApplicationInputInput` `InputParallelism`

    Describes the number of in-application streams to create.

    Data from your source is routed to these in-application input streams.

    (see `Configuring Application Input
    <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-input.html>`__ .

    - **Count** *(integer) --*

      Number of in-application streams to create. For more information, see `Limits
      <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/limits.html>`__ .
    """


_ClientAddApplicationInputInputInputProcessingConfigurationInputLambdaProcessorTypeDef = TypedDict(
    "_ClientAddApplicationInputInputInputProcessingConfigurationInputLambdaProcessorTypeDef",
    {"ResourceARN": str, "RoleARN": str},
)


class ClientAddApplicationInputInputInputProcessingConfigurationInputLambdaProcessorTypeDef(
    _ClientAddApplicationInputInputInputProcessingConfigurationInputLambdaProcessorTypeDef
):
    """
    Type definition for `ClientAddApplicationInputInputInputProcessingConfiguration` `InputLambdaProcessor`

    The `InputLambdaProcessor
    <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_InputLambdaProcessor.html>`__
    that is used to preprocess the records in the stream before being processed by your
    application code.

    - **ResourceARN** *(string) --* **[REQUIRED]**

      The ARN of the `AWS Lambda <https://docs.aws.amazon.com/lambda/>`__ function that operates
      on records in the stream.

      .. note::

        To specify an earlier version of the Lambda function than the latest, include the Lambda
        function version in the Lambda function ARN. For more information about Lambda ARNs, see
        `Example ARNs\\: AWS Lambda
        </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__

    - **RoleARN** *(string) --* **[REQUIRED]**

      The ARN of the IAM role that is used to access the AWS Lambda function.
    """


_ClientAddApplicationInputInputInputProcessingConfigurationTypeDef = TypedDict(
    "_ClientAddApplicationInputInputInputProcessingConfigurationTypeDef",
    {
        "InputLambdaProcessor": ClientAddApplicationInputInputInputProcessingConfigurationInputLambdaProcessorTypeDef
    },
)


class ClientAddApplicationInputInputInputProcessingConfigurationTypeDef(
    _ClientAddApplicationInputInputInputProcessingConfigurationTypeDef
):
    """
    Type definition for `ClientAddApplicationInputInput` `InputProcessingConfiguration`

    The `InputProcessingConfiguration
    <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_InputProcessingConfiguration.html>`__
    for the input. An input processor transforms records as they are received from the stream,
    before the application's SQL code executes. Currently, the only input processing configuration
    available is `InputLambdaProcessor
    <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_InputLambdaProcessor.html>`__ .

    - **InputLambdaProcessor** *(dict) --* **[REQUIRED]**

      The `InputLambdaProcessor
      <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_InputLambdaProcessor.html>`__
      that is used to preprocess the records in the stream before being processed by your
      application code.

      - **ResourceARN** *(string) --* **[REQUIRED]**

        The ARN of the `AWS Lambda <https://docs.aws.amazon.com/lambda/>`__ function that operates
        on records in the stream.

        .. note::

          To specify an earlier version of the Lambda function than the latest, include the Lambda
          function version in the Lambda function ARN. For more information about Lambda ARNs, see
          `Example ARNs\\: AWS Lambda
          </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__

      - **RoleARN** *(string) --* **[REQUIRED]**

        The ARN of the IAM role that is used to access the AWS Lambda function.
    """


_RequiredClientAddApplicationInputInputInputSchemaRecordColumnsTypeDef = TypedDict(
    "_RequiredClientAddApplicationInputInputInputSchemaRecordColumnsTypeDef",
    {"Name": str, "SqlType": str},
)
_OptionalClientAddApplicationInputInputInputSchemaRecordColumnsTypeDef = TypedDict(
    "_OptionalClientAddApplicationInputInputInputSchemaRecordColumnsTypeDef",
    {"Mapping": str},
    total=False,
)


class ClientAddApplicationInputInputInputSchemaRecordColumnsTypeDef(
    _RequiredClientAddApplicationInputInputInputSchemaRecordColumnsTypeDef,
    _OptionalClientAddApplicationInputInputInputSchemaRecordColumnsTypeDef,
):
    """
    Type definition for `ClientAddApplicationInputInputInputSchema` `RecordColumns`

    Describes the mapping of each data element in the streaming source to the corresponding
    column in the in-application stream.

    Also used to describe the format of the reference data source.

    - **Name** *(string) --* **[REQUIRED]**

      Name of the column created in the in-application input stream or reference table.

    - **Mapping** *(string) --*

      Reference to the data element in the streaming input or the reference data source. This
      element is required if the `RecordFormatType
      <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_RecordFormat.html#analytics-Type-RecordFormat-RecordFormatTypel>`__
      is ``JSON`` .

    - **SqlType** *(string) --* **[REQUIRED]**

      Type of column created in the in-application input stream or reference table.
    """


_ClientAddApplicationInputInputInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef = TypedDict(
    "_ClientAddApplicationInputInputInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef",
    {"RecordRowDelimiter": str, "RecordColumnDelimiter": str},
)


class ClientAddApplicationInputInputInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef(
    _ClientAddApplicationInputInputInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef
):
    """
    Type definition for `ClientAddApplicationInputInputInputSchemaRecordFormatMappingParameters` `CSVMappingParameters`

    Provides additional mapping information when the record format uses delimiters (for
    example, CSV).

    - **RecordRowDelimiter** *(string) --* **[REQUIRED]**

      Row delimiter. For example, in a CSV format, *'\\n'* is the typical row delimiter.

    - **RecordColumnDelimiter** *(string) --* **[REQUIRED]**

      Column delimiter. For example, in a CSV format, a comma (",") is the typical column
      delimiter.
    """


_ClientAddApplicationInputInputInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef = TypedDict(
    "_ClientAddApplicationInputInputInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef",
    {"RecordRowPath": str},
)


class ClientAddApplicationInputInputInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef(
    _ClientAddApplicationInputInputInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef
):
    """
    Type definition for `ClientAddApplicationInputInputInputSchemaRecordFormatMappingParameters` `JSONMappingParameters`

    Provides additional mapping information when JSON is the record format on the streaming
    source.

    - **RecordRowPath** *(string) --* **[REQUIRED]**

      Path to the top-level parent that contains the records.
    """


_ClientAddApplicationInputInputInputSchemaRecordFormatMappingParametersTypeDef = TypedDict(
    "_ClientAddApplicationInputInputInputSchemaRecordFormatMappingParametersTypeDef",
    {
        "JSONMappingParameters": ClientAddApplicationInputInputInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef,
        "CSVMappingParameters": ClientAddApplicationInputInputInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef,
    },
    total=False,
)


class ClientAddApplicationInputInputInputSchemaRecordFormatMappingParametersTypeDef(
    _ClientAddApplicationInputInputInputSchemaRecordFormatMappingParametersTypeDef
):
    """
    Type definition for `ClientAddApplicationInputInputInputSchemaRecordFormat` `MappingParameters`

    When configuring application input at the time of creating or updating an application,
    provides additional mapping information specific to the record format (such as JSON, CSV,
    or record fields delimited by some delimiter) on the streaming source.

    - **JSONMappingParameters** *(dict) --*

      Provides additional mapping information when JSON is the record format on the streaming
      source.

      - **RecordRowPath** *(string) --* **[REQUIRED]**

        Path to the top-level parent that contains the records.

    - **CSVMappingParameters** *(dict) --*

      Provides additional mapping information when the record format uses delimiters (for
      example, CSV).

      - **RecordRowDelimiter** *(string) --* **[REQUIRED]**

        Row delimiter. For example, in a CSV format, *'\\n'* is the typical row delimiter.

      - **RecordColumnDelimiter** *(string) --* **[REQUIRED]**

        Column delimiter. For example, in a CSV format, a comma (",") is the typical column
        delimiter.
    """


_RequiredClientAddApplicationInputInputInputSchemaRecordFormatTypeDef = TypedDict(
    "_RequiredClientAddApplicationInputInputInputSchemaRecordFormatTypeDef",
    {"RecordFormatType": str},
)
_OptionalClientAddApplicationInputInputInputSchemaRecordFormatTypeDef = TypedDict(
    "_OptionalClientAddApplicationInputInputInputSchemaRecordFormatTypeDef",
    {
        "MappingParameters": ClientAddApplicationInputInputInputSchemaRecordFormatMappingParametersTypeDef
    },
    total=False,
)


class ClientAddApplicationInputInputInputSchemaRecordFormatTypeDef(
    _RequiredClientAddApplicationInputInputInputSchemaRecordFormatTypeDef,
    _OptionalClientAddApplicationInputInputInputSchemaRecordFormatTypeDef,
):
    """
    Type definition for `ClientAddApplicationInputInputInputSchema` `RecordFormat`

    Specifies the format of the records on the streaming source.

    - **RecordFormatType** *(string) --* **[REQUIRED]**

      The type of record format.

    - **MappingParameters** *(dict) --*

      When configuring application input at the time of creating or updating an application,
      provides additional mapping information specific to the record format (such as JSON, CSV,
      or record fields delimited by some delimiter) on the streaming source.

      - **JSONMappingParameters** *(dict) --*

        Provides additional mapping information when JSON is the record format on the streaming
        source.

        - **RecordRowPath** *(string) --* **[REQUIRED]**

          Path to the top-level parent that contains the records.

      - **CSVMappingParameters** *(dict) --*

        Provides additional mapping information when the record format uses delimiters (for
        example, CSV).

        - **RecordRowDelimiter** *(string) --* **[REQUIRED]**

          Row delimiter. For example, in a CSV format, *'\\n'* is the typical row delimiter.

        - **RecordColumnDelimiter** *(string) --* **[REQUIRED]**

          Column delimiter. For example, in a CSV format, a comma (",") is the typical column
          delimiter.
    """


_RequiredClientAddApplicationInputInputInputSchemaTypeDef = TypedDict(
    "_RequiredClientAddApplicationInputInputInputSchemaTypeDef",
    {
        "RecordFormat": ClientAddApplicationInputInputInputSchemaRecordFormatTypeDef,
        "RecordColumns": List[
            ClientAddApplicationInputInputInputSchemaRecordColumnsTypeDef
        ],
    },
)
_OptionalClientAddApplicationInputInputInputSchemaTypeDef = TypedDict(
    "_OptionalClientAddApplicationInputInputInputSchemaTypeDef",
    {"RecordEncoding": str},
    total=False,
)


class ClientAddApplicationInputInputInputSchemaTypeDef(
    _RequiredClientAddApplicationInputInputInputSchemaTypeDef,
    _OptionalClientAddApplicationInputInputInputSchemaTypeDef,
):
    """
    Type definition for `ClientAddApplicationInputInput` `InputSchema`

    Describes the format of the data in the streaming source, and how each data element maps to
    corresponding columns in the in-application stream that is being created.

    Also used to describe the format of the reference data source.

    - **RecordFormat** *(dict) --* **[REQUIRED]**

      Specifies the format of the records on the streaming source.

      - **RecordFormatType** *(string) --* **[REQUIRED]**

        The type of record format.

      - **MappingParameters** *(dict) --*

        When configuring application input at the time of creating or updating an application,
        provides additional mapping information specific to the record format (such as JSON, CSV,
        or record fields delimited by some delimiter) on the streaming source.

        - **JSONMappingParameters** *(dict) --*

          Provides additional mapping information when JSON is the record format on the streaming
          source.

          - **RecordRowPath** *(string) --* **[REQUIRED]**

            Path to the top-level parent that contains the records.

        - **CSVMappingParameters** *(dict) --*

          Provides additional mapping information when the record format uses delimiters (for
          example, CSV).

          - **RecordRowDelimiter** *(string) --* **[REQUIRED]**

            Row delimiter. For example, in a CSV format, *'\\n'* is the typical row delimiter.

          - **RecordColumnDelimiter** *(string) --* **[REQUIRED]**

            Column delimiter. For example, in a CSV format, a comma (",") is the typical column
            delimiter.

    - **RecordEncoding** *(string) --*

      Specifies the encoding of the records in the streaming source. For example, UTF-8.

    - **RecordColumns** *(list) --* **[REQUIRED]**

      A list of ``RecordColumn`` objects.

      - *(dict) --*

        Describes the mapping of each data element in the streaming source to the corresponding
        column in the in-application stream.

        Also used to describe the format of the reference data source.

        - **Name** *(string) --* **[REQUIRED]**

          Name of the column created in the in-application input stream or reference table.

        - **Mapping** *(string) --*

          Reference to the data element in the streaming input or the reference data source. This
          element is required if the `RecordFormatType
          <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_RecordFormat.html#analytics-Type-RecordFormat-RecordFormatTypel>`__
          is ``JSON`` .

        - **SqlType** *(string) --* **[REQUIRED]**

          Type of column created in the in-application input stream or reference table.
    """


_ClientAddApplicationInputInputKinesisFirehoseInputTypeDef = TypedDict(
    "_ClientAddApplicationInputInputKinesisFirehoseInputTypeDef",
    {"ResourceARN": str, "RoleARN": str},
)


class ClientAddApplicationInputInputKinesisFirehoseInputTypeDef(
    _ClientAddApplicationInputInputKinesisFirehoseInputTypeDef
):
    """
    Type definition for `ClientAddApplicationInputInput` `KinesisFirehoseInput`

    If the streaming source is an Amazon Kinesis Firehose delivery stream, identifies the delivery
    stream's ARN and an IAM role that enables Amazon Kinesis Analytics to access the stream on your
    behalf.

    Note: Either ``KinesisStreamsInput`` or ``KinesisFirehoseInput`` is required.

    - **ResourceARN** *(string) --* **[REQUIRED]**

      ARN of the input delivery stream.

    - **RoleARN** *(string) --* **[REQUIRED]**

      ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream on your
      behalf. You need to make sure that the role has the necessary permissions to access the
      stream.
    """


_ClientAddApplicationInputInputKinesisStreamsInputTypeDef = TypedDict(
    "_ClientAddApplicationInputInputKinesisStreamsInputTypeDef",
    {"ResourceARN": str, "RoleARN": str},
)


class ClientAddApplicationInputInputKinesisStreamsInputTypeDef(
    _ClientAddApplicationInputInputKinesisStreamsInputTypeDef
):
    """
    Type definition for `ClientAddApplicationInputInput` `KinesisStreamsInput`

    If the streaming source is an Amazon Kinesis stream, identifies the stream's Amazon Resource
    Name (ARN) and an IAM role that enables Amazon Kinesis Analytics to access the stream on your
    behalf.

    Note: Either ``KinesisStreamsInput`` or ``KinesisFirehoseInput`` is required.

    - **ResourceARN** *(string) --* **[REQUIRED]**

      ARN of the input Amazon Kinesis stream to read.

    - **RoleARN** *(string) --* **[REQUIRED]**

      ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream on your
      behalf. You need to grant the necessary permissions to this role.
    """


_RequiredClientAddApplicationInputInputTypeDef = TypedDict(
    "_RequiredClientAddApplicationInputInputTypeDef",
    {
        "NamePrefix": str,
        "InputSchema": ClientAddApplicationInputInputInputSchemaTypeDef,
    },
)
_OptionalClientAddApplicationInputInputTypeDef = TypedDict(
    "_OptionalClientAddApplicationInputInputTypeDef",
    {
        "InputProcessingConfiguration": ClientAddApplicationInputInputInputProcessingConfigurationTypeDef,
        "KinesisStreamsInput": ClientAddApplicationInputInputKinesisStreamsInputTypeDef,
        "KinesisFirehoseInput": ClientAddApplicationInputInputKinesisFirehoseInputTypeDef,
        "InputParallelism": ClientAddApplicationInputInputInputParallelismTypeDef,
    },
    total=False,
)


class ClientAddApplicationInputInputTypeDef(
    _RequiredClientAddApplicationInputInputTypeDef,
    _OptionalClientAddApplicationInputInputTypeDef,
):
    """
    Type definition for `ClientAddApplicationInput` `Input`

    The `Input <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_Input.html>`__ to add.

    - **NamePrefix** *(string) --* **[REQUIRED]**

      Name prefix to use when creating an in-application stream. Suppose that you specify a prefix
      "MyInApplicationStream." Amazon Kinesis Analytics then creates one or more (as per the
      ``InputParallelism`` count you specified) in-application streams with names
      "MyInApplicationStream_001," "MyInApplicationStream_002," and so on.

    - **InputProcessingConfiguration** *(dict) --*

      The `InputProcessingConfiguration
      <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_InputProcessingConfiguration.html>`__
      for the input. An input processor transforms records as they are received from the stream,
      before the application's SQL code executes. Currently, the only input processing configuration
      available is `InputLambdaProcessor
      <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_InputLambdaProcessor.html>`__ .

      - **InputLambdaProcessor** *(dict) --* **[REQUIRED]**

        The `InputLambdaProcessor
        <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_InputLambdaProcessor.html>`__
        that is used to preprocess the records in the stream before being processed by your
        application code.

        - **ResourceARN** *(string) --* **[REQUIRED]**

          The ARN of the `AWS Lambda <https://docs.aws.amazon.com/lambda/>`__ function that operates
          on records in the stream.

          .. note::

            To specify an earlier version of the Lambda function than the latest, include the Lambda
            function version in the Lambda function ARN. For more information about Lambda ARNs, see
            `Example ARNs\\: AWS Lambda
            </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__

        - **RoleARN** *(string) --* **[REQUIRED]**

          The ARN of the IAM role that is used to access the AWS Lambda function.

    - **KinesisStreamsInput** *(dict) --*

      If the streaming source is an Amazon Kinesis stream, identifies the stream's Amazon Resource
      Name (ARN) and an IAM role that enables Amazon Kinesis Analytics to access the stream on your
      behalf.

      Note: Either ``KinesisStreamsInput`` or ``KinesisFirehoseInput`` is required.

      - **ResourceARN** *(string) --* **[REQUIRED]**

        ARN of the input Amazon Kinesis stream to read.

      - **RoleARN** *(string) --* **[REQUIRED]**

        ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream on your
        behalf. You need to grant the necessary permissions to this role.

    - **KinesisFirehoseInput** *(dict) --*

      If the streaming source is an Amazon Kinesis Firehose delivery stream, identifies the delivery
      stream's ARN and an IAM role that enables Amazon Kinesis Analytics to access the stream on your
      behalf.

      Note: Either ``KinesisStreamsInput`` or ``KinesisFirehoseInput`` is required.

      - **ResourceARN** *(string) --* **[REQUIRED]**

        ARN of the input delivery stream.

      - **RoleARN** *(string) --* **[REQUIRED]**

        ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream on your
        behalf. You need to make sure that the role has the necessary permissions to access the
        stream.

    - **InputParallelism** *(dict) --*

      Describes the number of in-application streams to create.

      Data from your source is routed to these in-application input streams.

      (see `Configuring Application Input
      <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-input.html>`__ .

      - **Count** *(integer) --*

        Number of in-application streams to create. For more information, see `Limits
        <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/limits.html>`__ .

    - **InputSchema** *(dict) --* **[REQUIRED]**

      Describes the format of the data in the streaming source, and how each data element maps to
      corresponding columns in the in-application stream that is being created.

      Also used to describe the format of the reference data source.

      - **RecordFormat** *(dict) --* **[REQUIRED]**

        Specifies the format of the records on the streaming source.

        - **RecordFormatType** *(string) --* **[REQUIRED]**

          The type of record format.

        - **MappingParameters** *(dict) --*

          When configuring application input at the time of creating or updating an application,
          provides additional mapping information specific to the record format (such as JSON, CSV,
          or record fields delimited by some delimiter) on the streaming source.

          - **JSONMappingParameters** *(dict) --*

            Provides additional mapping information when JSON is the record format on the streaming
            source.

            - **RecordRowPath** *(string) --* **[REQUIRED]**

              Path to the top-level parent that contains the records.

          - **CSVMappingParameters** *(dict) --*

            Provides additional mapping information when the record format uses delimiters (for
            example, CSV).

            - **RecordRowDelimiter** *(string) --* **[REQUIRED]**

              Row delimiter. For example, in a CSV format, *'\\n'* is the typical row delimiter.

            - **RecordColumnDelimiter** *(string) --* **[REQUIRED]**

              Column delimiter. For example, in a CSV format, a comma (",") is the typical column
              delimiter.

      - **RecordEncoding** *(string) --*

        Specifies the encoding of the records in the streaming source. For example, UTF-8.

      - **RecordColumns** *(list) --* **[REQUIRED]**

        A list of ``RecordColumn`` objects.

        - *(dict) --*

          Describes the mapping of each data element in the streaming source to the corresponding
          column in the in-application stream.

          Also used to describe the format of the reference data source.

          - **Name** *(string) --* **[REQUIRED]**

            Name of the column created in the in-application input stream or reference table.

          - **Mapping** *(string) --*

            Reference to the data element in the streaming input or the reference data source. This
            element is required if the `RecordFormatType
            <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_RecordFormat.html#analytics-Type-RecordFormat-RecordFormatTypel>`__
            is ``JSON`` .

          - **SqlType** *(string) --* **[REQUIRED]**

            Type of column created in the in-application input stream or reference table.
    """


_ClientAddApplicationInputProcessingConfigurationInputProcessingConfigurationInputLambdaProcessorTypeDef = TypedDict(
    "_ClientAddApplicationInputProcessingConfigurationInputProcessingConfigurationInputLambdaProcessorTypeDef",
    {"ResourceARN": str, "RoleARN": str},
)


class ClientAddApplicationInputProcessingConfigurationInputProcessingConfigurationInputLambdaProcessorTypeDef(
    _ClientAddApplicationInputProcessingConfigurationInputProcessingConfigurationInputLambdaProcessorTypeDef
):
    """
    Type definition for `ClientAddApplicationInputProcessingConfigurationInputProcessingConfiguration` `InputLambdaProcessor`

    The `InputLambdaProcessor
    <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_InputLambdaProcessor.html>`__ that
    is used to preprocess the records in the stream before being processed by your application code.

    - **ResourceARN** *(string) --* **[REQUIRED]**

      The ARN of the `AWS Lambda <https://docs.aws.amazon.com/lambda/>`__ function that operates on
      records in the stream.

      .. note::

        To specify an earlier version of the Lambda function than the latest, include the Lambda
        function version in the Lambda function ARN. For more information about Lambda ARNs, see
        `Example ARNs\\: AWS Lambda
        </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__

    - **RoleARN** *(string) --* **[REQUIRED]**

      The ARN of the IAM role that is used to access the AWS Lambda function.
    """


_ClientAddApplicationInputProcessingConfigurationInputProcessingConfigurationTypeDef = TypedDict(
    "_ClientAddApplicationInputProcessingConfigurationInputProcessingConfigurationTypeDef",
    {
        "InputLambdaProcessor": ClientAddApplicationInputProcessingConfigurationInputProcessingConfigurationInputLambdaProcessorTypeDef
    },
)


class ClientAddApplicationInputProcessingConfigurationInputProcessingConfigurationTypeDef(
    _ClientAddApplicationInputProcessingConfigurationInputProcessingConfigurationTypeDef
):
    """
    Type definition for `ClientAddApplicationInputProcessingConfiguration` `InputProcessingConfiguration`

    The `InputProcessingConfiguration
    <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_InputProcessingConfiguration.html>`__
    to add to the application.

    - **InputLambdaProcessor** *(dict) --* **[REQUIRED]**

      The `InputLambdaProcessor
      <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_InputLambdaProcessor.html>`__ that
      is used to preprocess the records in the stream before being processed by your application code.

      - **ResourceARN** *(string) --* **[REQUIRED]**

        The ARN of the `AWS Lambda <https://docs.aws.amazon.com/lambda/>`__ function that operates on
        records in the stream.

        .. note::

          To specify an earlier version of the Lambda function than the latest, include the Lambda
          function version in the Lambda function ARN. For more information about Lambda ARNs, see
          `Example ARNs\\: AWS Lambda
          </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__

      - **RoleARN** *(string) --* **[REQUIRED]**

        The ARN of the IAM role that is used to access the AWS Lambda function.
    """


_ClientAddApplicationOutputOutputDestinationSchemaTypeDef = TypedDict(
    "_ClientAddApplicationOutputOutputDestinationSchemaTypeDef",
    {"RecordFormatType": str},
)


class ClientAddApplicationOutputOutputDestinationSchemaTypeDef(
    _ClientAddApplicationOutputOutputDestinationSchemaTypeDef
):
    """
    Type definition for `ClientAddApplicationOutputOutput` `DestinationSchema`

    Describes the data format when records are written to the destination. For more information,
    see `Configuring Application Output
    <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-output.html>`__ .

    - **RecordFormatType** *(string) --* **[REQUIRED]**

      Specifies the format of the records on the output stream.
    """


_ClientAddApplicationOutputOutputKinesisFirehoseOutputTypeDef = TypedDict(
    "_ClientAddApplicationOutputOutputKinesisFirehoseOutputTypeDef",
    {"ResourceARN": str, "RoleARN": str},
)


class ClientAddApplicationOutputOutputKinesisFirehoseOutputTypeDef(
    _ClientAddApplicationOutputOutputKinesisFirehoseOutputTypeDef
):
    """
    Type definition for `ClientAddApplicationOutputOutput` `KinesisFirehoseOutput`

    Identifies an Amazon Kinesis Firehose delivery stream as the destination.

    - **ResourceARN** *(string) --* **[REQUIRED]**

      ARN of the destination Amazon Kinesis Firehose delivery stream to write to.

    - **RoleARN** *(string) --* **[REQUIRED]**

      ARN of the IAM role that Amazon Kinesis Analytics can assume to write to the destination
      stream on your behalf. You need to grant the necessary permissions to this role.
    """


_ClientAddApplicationOutputOutputKinesisStreamsOutputTypeDef = TypedDict(
    "_ClientAddApplicationOutputOutputKinesisStreamsOutputTypeDef",
    {"ResourceARN": str, "RoleARN": str},
)


class ClientAddApplicationOutputOutputKinesisStreamsOutputTypeDef(
    _ClientAddApplicationOutputOutputKinesisStreamsOutputTypeDef
):
    """
    Type definition for `ClientAddApplicationOutputOutput` `KinesisStreamsOutput`

    Identifies an Amazon Kinesis stream as the destination.

    - **ResourceARN** *(string) --* **[REQUIRED]**

      ARN of the destination Amazon Kinesis stream to write to.

    - **RoleARN** *(string) --* **[REQUIRED]**

      ARN of the IAM role that Amazon Kinesis Analytics can assume to write to the destination
      stream on your behalf. You need to grant the necessary permissions to this role.
    """


_ClientAddApplicationOutputOutputLambdaOutputTypeDef = TypedDict(
    "_ClientAddApplicationOutputOutputLambdaOutputTypeDef",
    {"ResourceARN": str, "RoleARN": str},
)


class ClientAddApplicationOutputOutputLambdaOutputTypeDef(
    _ClientAddApplicationOutputOutputLambdaOutputTypeDef
):
    """
    Type definition for `ClientAddApplicationOutputOutput` `LambdaOutput`

    Identifies an AWS Lambda function as the destination.

    - **ResourceARN** *(string) --* **[REQUIRED]**

      Amazon Resource Name (ARN) of the destination Lambda function to write to.

      .. note::

        To specify an earlier version of the Lambda function than the latest, include the Lambda
        function version in the Lambda function ARN. For more information about Lambda ARNs, see
        `Example ARNs\\: AWS Lambda
        </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__

    - **RoleARN** *(string) --* **[REQUIRED]**

      ARN of the IAM role that Amazon Kinesis Analytics can assume to write to the destination
      function on your behalf. You need to grant the necessary permissions to this role.
    """


_RequiredClientAddApplicationOutputOutputTypeDef = TypedDict(
    "_RequiredClientAddApplicationOutputOutputTypeDef",
    {
        "Name": str,
        "DestinationSchema": ClientAddApplicationOutputOutputDestinationSchemaTypeDef,
    },
)
_OptionalClientAddApplicationOutputOutputTypeDef = TypedDict(
    "_OptionalClientAddApplicationOutputOutputTypeDef",
    {
        "KinesisStreamsOutput": ClientAddApplicationOutputOutputKinesisStreamsOutputTypeDef,
        "KinesisFirehoseOutput": ClientAddApplicationOutputOutputKinesisFirehoseOutputTypeDef,
        "LambdaOutput": ClientAddApplicationOutputOutputLambdaOutputTypeDef,
    },
    total=False,
)


class ClientAddApplicationOutputOutputTypeDef(
    _RequiredClientAddApplicationOutputOutputTypeDef,
    _OptionalClientAddApplicationOutputOutputTypeDef,
):
    """
    Type definition for `ClientAddApplicationOutput` `Output`

    An array of objects, each describing one output configuration. In the output configuration, you
    specify the name of an in-application stream, a destination (that is, an Amazon Kinesis stream,
    an Amazon Kinesis Firehose delivery stream, or an AWS Lambda function), and record the formation
    to use when writing to the destination.

    - **Name** *(string) --* **[REQUIRED]**

      Name of the in-application stream.

    - **KinesisStreamsOutput** *(dict) --*

      Identifies an Amazon Kinesis stream as the destination.

      - **ResourceARN** *(string) --* **[REQUIRED]**

        ARN of the destination Amazon Kinesis stream to write to.

      - **RoleARN** *(string) --* **[REQUIRED]**

        ARN of the IAM role that Amazon Kinesis Analytics can assume to write to the destination
        stream on your behalf. You need to grant the necessary permissions to this role.

    - **KinesisFirehoseOutput** *(dict) --*

      Identifies an Amazon Kinesis Firehose delivery stream as the destination.

      - **ResourceARN** *(string) --* **[REQUIRED]**

        ARN of the destination Amazon Kinesis Firehose delivery stream to write to.

      - **RoleARN** *(string) --* **[REQUIRED]**

        ARN of the IAM role that Amazon Kinesis Analytics can assume to write to the destination
        stream on your behalf. You need to grant the necessary permissions to this role.

    - **LambdaOutput** *(dict) --*

      Identifies an AWS Lambda function as the destination.

      - **ResourceARN** *(string) --* **[REQUIRED]**

        Amazon Resource Name (ARN) of the destination Lambda function to write to.

        .. note::

          To specify an earlier version of the Lambda function than the latest, include the Lambda
          function version in the Lambda function ARN. For more information about Lambda ARNs, see
          `Example ARNs\\: AWS Lambda
          </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__

      - **RoleARN** *(string) --* **[REQUIRED]**

        ARN of the IAM role that Amazon Kinesis Analytics can assume to write to the destination
        function on your behalf. You need to grant the necessary permissions to this role.

    - **DestinationSchema** *(dict) --* **[REQUIRED]**

      Describes the data format when records are written to the destination. For more information,
      see `Configuring Application Output
      <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-output.html>`__ .

      - **RecordFormatType** *(string) --* **[REQUIRED]**

        Specifies the format of the records on the output stream.
    """


_RequiredClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordColumnsTypeDef = TypedDict(
    "_RequiredClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordColumnsTypeDef",
    {"Name": str, "SqlType": str},
)
_OptionalClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordColumnsTypeDef = TypedDict(
    "_OptionalClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordColumnsTypeDef",
    {"Mapping": str},
    total=False,
)


class ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordColumnsTypeDef(
    _RequiredClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordColumnsTypeDef,
    _OptionalClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordColumnsTypeDef,
):
    """
    Type definition for `ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchema` `RecordColumns`

    Describes the mapping of each data element in the streaming source to the corresponding
    column in the in-application stream.

    Also used to describe the format of the reference data source.

    - **Name** *(string) --* **[REQUIRED]**

      Name of the column created in the in-application input stream or reference table.

    - **Mapping** *(string) --*

      Reference to the data element in the streaming input or the reference data source. This
      element is required if the `RecordFormatType
      <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_RecordFormat.html#analytics-Type-RecordFormat-RecordFormatTypel>`__
      is ``JSON`` .

    - **SqlType** *(string) --* **[REQUIRED]**

      Type of column created in the in-application input stream or reference table.
    """


_ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef = TypedDict(
    "_ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef",
    {"RecordRowDelimiter": str, "RecordColumnDelimiter": str},
)


class ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef(
    _ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef
):
    """
    Type definition for `ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordFormatMappingParameters` `CSVMappingParameters`

    Provides additional mapping information when the record format uses delimiters (for
    example, CSV).

    - **RecordRowDelimiter** *(string) --* **[REQUIRED]**

      Row delimiter. For example, in a CSV format, *'\\n'* is the typical row delimiter.

    - **RecordColumnDelimiter** *(string) --* **[REQUIRED]**

      Column delimiter. For example, in a CSV format, a comma (",") is the typical column
      delimiter.
    """


_ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef = TypedDict(
    "_ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef",
    {"RecordRowPath": str},
)


class ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef(
    _ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef
):
    """
    Type definition for `ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordFormatMappingParameters` `JSONMappingParameters`

    Provides additional mapping information when JSON is the record format on the streaming
    source.

    - **RecordRowPath** *(string) --* **[REQUIRED]**

      Path to the top-level parent that contains the records.
    """


_ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordFormatMappingParametersTypeDef = TypedDict(
    "_ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordFormatMappingParametersTypeDef",
    {
        "JSONMappingParameters": ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef,
        "CSVMappingParameters": ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef,
    },
    total=False,
)


class ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordFormatMappingParametersTypeDef(
    _ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordFormatMappingParametersTypeDef
):
    """
    Type definition for `ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordFormat` `MappingParameters`

    When configuring application input at the time of creating or updating an application,
    provides additional mapping information specific to the record format (such as JSON, CSV,
    or record fields delimited by some delimiter) on the streaming source.

    - **JSONMappingParameters** *(dict) --*

      Provides additional mapping information when JSON is the record format on the streaming
      source.

      - **RecordRowPath** *(string) --* **[REQUIRED]**

        Path to the top-level parent that contains the records.

    - **CSVMappingParameters** *(dict) --*

      Provides additional mapping information when the record format uses delimiters (for
      example, CSV).

      - **RecordRowDelimiter** *(string) --* **[REQUIRED]**

        Row delimiter. For example, in a CSV format, *'\\n'* is the typical row delimiter.

      - **RecordColumnDelimiter** *(string) --* **[REQUIRED]**

        Column delimiter. For example, in a CSV format, a comma (",") is the typical column
        delimiter.
    """


_RequiredClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordFormatTypeDef = TypedDict(
    "_RequiredClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordFormatTypeDef",
    {"RecordFormatType": str},
)
_OptionalClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordFormatTypeDef = TypedDict(
    "_OptionalClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordFormatTypeDef",
    {
        "MappingParameters": ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordFormatMappingParametersTypeDef
    },
    total=False,
)


class ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordFormatTypeDef(
    _RequiredClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordFormatTypeDef,
    _OptionalClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordFormatTypeDef,
):
    """
    Type definition for `ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchema` `RecordFormat`

    Specifies the format of the records on the streaming source.

    - **RecordFormatType** *(string) --* **[REQUIRED]**

      The type of record format.

    - **MappingParameters** *(dict) --*

      When configuring application input at the time of creating or updating an application,
      provides additional mapping information specific to the record format (such as JSON, CSV,
      or record fields delimited by some delimiter) on the streaming source.

      - **JSONMappingParameters** *(dict) --*

        Provides additional mapping information when JSON is the record format on the streaming
        source.

        - **RecordRowPath** *(string) --* **[REQUIRED]**

          Path to the top-level parent that contains the records.

      - **CSVMappingParameters** *(dict) --*

        Provides additional mapping information when the record format uses delimiters (for
        example, CSV).

        - **RecordRowDelimiter** *(string) --* **[REQUIRED]**

          Row delimiter. For example, in a CSV format, *'\\n'* is the typical row delimiter.

        - **RecordColumnDelimiter** *(string) --* **[REQUIRED]**

          Column delimiter. For example, in a CSV format, a comma (",") is the typical column
          delimiter.
    """


_RequiredClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaTypeDef = TypedDict(
    "_RequiredClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaTypeDef",
    {
        "RecordFormat": ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordFormatTypeDef,
        "RecordColumns": List[
            ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordColumnsTypeDef
        ],
    },
)
_OptionalClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaTypeDef = TypedDict(
    "_OptionalClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaTypeDef",
    {"RecordEncoding": str},
    total=False,
)


class ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaTypeDef(
    _RequiredClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaTypeDef,
    _OptionalClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaTypeDef,
):
    """
    Type definition for `ClientAddApplicationReferenceDataSourceReferenceDataSource` `ReferenceSchema`

    Describes the format of the data in the streaming source, and how each data element maps to
    corresponding columns created in the in-application stream.

    - **RecordFormat** *(dict) --* **[REQUIRED]**

      Specifies the format of the records on the streaming source.

      - **RecordFormatType** *(string) --* **[REQUIRED]**

        The type of record format.

      - **MappingParameters** *(dict) --*

        When configuring application input at the time of creating or updating an application,
        provides additional mapping information specific to the record format (such as JSON, CSV,
        or record fields delimited by some delimiter) on the streaming source.

        - **JSONMappingParameters** *(dict) --*

          Provides additional mapping information when JSON is the record format on the streaming
          source.

          - **RecordRowPath** *(string) --* **[REQUIRED]**

            Path to the top-level parent that contains the records.

        - **CSVMappingParameters** *(dict) --*

          Provides additional mapping information when the record format uses delimiters (for
          example, CSV).

          - **RecordRowDelimiter** *(string) --* **[REQUIRED]**

            Row delimiter. For example, in a CSV format, *'\\n'* is the typical row delimiter.

          - **RecordColumnDelimiter** *(string) --* **[REQUIRED]**

            Column delimiter. For example, in a CSV format, a comma (",") is the typical column
            delimiter.

    - **RecordEncoding** *(string) --*

      Specifies the encoding of the records in the streaming source. For example, UTF-8.

    - **RecordColumns** *(list) --* **[REQUIRED]**

      A list of ``RecordColumn`` objects.

      - *(dict) --*

        Describes the mapping of each data element in the streaming source to the corresponding
        column in the in-application stream.

        Also used to describe the format of the reference data source.

        - **Name** *(string) --* **[REQUIRED]**

          Name of the column created in the in-application input stream or reference table.

        - **Mapping** *(string) --*

          Reference to the data element in the streaming input or the reference data source. This
          element is required if the `RecordFormatType
          <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_RecordFormat.html#analytics-Type-RecordFormat-RecordFormatTypel>`__
          is ``JSON`` .

        - **SqlType** *(string) --* **[REQUIRED]**

          Type of column created in the in-application input stream or reference table.
    """


_ClientAddApplicationReferenceDataSourceReferenceDataSourceS3ReferenceDataSourceTypeDef = TypedDict(
    "_ClientAddApplicationReferenceDataSourceReferenceDataSourceS3ReferenceDataSourceTypeDef",
    {"BucketARN": str, "FileKey": str, "ReferenceRoleARN": str},
)


class ClientAddApplicationReferenceDataSourceReferenceDataSourceS3ReferenceDataSourceTypeDef(
    _ClientAddApplicationReferenceDataSourceReferenceDataSourceS3ReferenceDataSourceTypeDef
):
    """
    Type definition for `ClientAddApplicationReferenceDataSourceReferenceDataSource` `S3ReferenceDataSource`

    Identifies the S3 bucket and object that contains the reference data. Also identifies the IAM
    role Amazon Kinesis Analytics can assume to read this object on your behalf. An Amazon Kinesis
    Analytics application loads reference data only once. If the data changes, you call the
    ``UpdateApplication`` operation to trigger reloading of data into your application.

    - **BucketARN** *(string) --* **[REQUIRED]**

      Amazon Resource Name (ARN) of the S3 bucket.

    - **FileKey** *(string) --* **[REQUIRED]**

      Object key name containing reference data.

    - **ReferenceRoleARN** *(string) --* **[REQUIRED]**

      ARN of the IAM role that the service can assume to read data on your behalf. This role must
      have permission for the ``s3:GetObject`` action on the object and trust policy that allows
      Amazon Kinesis Analytics service principal to assume this role.
    """


_RequiredClientAddApplicationReferenceDataSourceReferenceDataSourceTypeDef = TypedDict(
    "_RequiredClientAddApplicationReferenceDataSourceReferenceDataSourceTypeDef",
    {
        "TableName": str,
        "ReferenceSchema": ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaTypeDef,
    },
)
_OptionalClientAddApplicationReferenceDataSourceReferenceDataSourceTypeDef = TypedDict(
    "_OptionalClientAddApplicationReferenceDataSourceReferenceDataSourceTypeDef",
    {
        "S3ReferenceDataSource": ClientAddApplicationReferenceDataSourceReferenceDataSourceS3ReferenceDataSourceTypeDef
    },
    total=False,
)


class ClientAddApplicationReferenceDataSourceReferenceDataSourceTypeDef(
    _RequiredClientAddApplicationReferenceDataSourceReferenceDataSourceTypeDef,
    _OptionalClientAddApplicationReferenceDataSourceReferenceDataSourceTypeDef,
):
    """
    Type definition for `ClientAddApplicationReferenceDataSource` `ReferenceDataSource`

    The reference data source can be an object in your Amazon S3 bucket. Amazon Kinesis Analytics
    reads the object and copies the data into the in-application table that is created. You provide
    an S3 bucket, object key name, and the resulting in-application table that is created. You must
    also provide an IAM role with the necessary permissions that Amazon Kinesis Analytics can assume
    to read the object from your S3 bucket on your behalf.

    - **TableName** *(string) --* **[REQUIRED]**

      Name of the in-application table to create.

    - **S3ReferenceDataSource** *(dict) --*

      Identifies the S3 bucket and object that contains the reference data. Also identifies the IAM
      role Amazon Kinesis Analytics can assume to read this object on your behalf. An Amazon Kinesis
      Analytics application loads reference data only once. If the data changes, you call the
      ``UpdateApplication`` operation to trigger reloading of data into your application.

      - **BucketARN** *(string) --* **[REQUIRED]**

        Amazon Resource Name (ARN) of the S3 bucket.

      - **FileKey** *(string) --* **[REQUIRED]**

        Object key name containing reference data.

      - **ReferenceRoleARN** *(string) --* **[REQUIRED]**

        ARN of the IAM role that the service can assume to read data on your behalf. This role must
        have permission for the ``s3:GetObject`` action on the object and trust policy that allows
        Amazon Kinesis Analytics service principal to assume this role.

    - **ReferenceSchema** *(dict) --* **[REQUIRED]**

      Describes the format of the data in the streaming source, and how each data element maps to
      corresponding columns created in the in-application stream.

      - **RecordFormat** *(dict) --* **[REQUIRED]**

        Specifies the format of the records on the streaming source.

        - **RecordFormatType** *(string) --* **[REQUIRED]**

          The type of record format.

        - **MappingParameters** *(dict) --*

          When configuring application input at the time of creating or updating an application,
          provides additional mapping information specific to the record format (such as JSON, CSV,
          or record fields delimited by some delimiter) on the streaming source.

          - **JSONMappingParameters** *(dict) --*

            Provides additional mapping information when JSON is the record format on the streaming
            source.

            - **RecordRowPath** *(string) --* **[REQUIRED]**

              Path to the top-level parent that contains the records.

          - **CSVMappingParameters** *(dict) --*

            Provides additional mapping information when the record format uses delimiters (for
            example, CSV).

            - **RecordRowDelimiter** *(string) --* **[REQUIRED]**

              Row delimiter. For example, in a CSV format, *'\\n'* is the typical row delimiter.

            - **RecordColumnDelimiter** *(string) --* **[REQUIRED]**

              Column delimiter. For example, in a CSV format, a comma (",") is the typical column
              delimiter.

      - **RecordEncoding** *(string) --*

        Specifies the encoding of the records in the streaming source. For example, UTF-8.

      - **RecordColumns** *(list) --* **[REQUIRED]**

        A list of ``RecordColumn`` objects.

        - *(dict) --*

          Describes the mapping of each data element in the streaming source to the corresponding
          column in the in-application stream.

          Also used to describe the format of the reference data source.

          - **Name** *(string) --* **[REQUIRED]**

            Name of the column created in the in-application input stream or reference table.

          - **Mapping** *(string) --*

            Reference to the data element in the streaming input or the reference data source. This
            element is required if the `RecordFormatType
            <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_RecordFormat.html#analytics-Type-RecordFormat-RecordFormatTypel>`__
            is ``JSON`` .

          - **SqlType** *(string) --* **[REQUIRED]**

            Type of column created in the in-application input stream or reference table.
    """


_ClientCreateApplicationCloudWatchLoggingOptionsTypeDef = TypedDict(
    "_ClientCreateApplicationCloudWatchLoggingOptionsTypeDef",
    {"LogStreamARN": str, "RoleARN": str},
)


class ClientCreateApplicationCloudWatchLoggingOptionsTypeDef(
    _ClientCreateApplicationCloudWatchLoggingOptionsTypeDef
):
    """
    Type definition for `ClientCreateApplication` `CloudWatchLoggingOptions`

    Provides a description of CloudWatch logging options, including the log stream Amazon Resource
    Name (ARN) and the role ARN.

    - **LogStreamARN** *(string) --* **[REQUIRED]**

      ARN of the CloudWatch log to receive application messages.

    - **RoleARN** *(string) --* **[REQUIRED]**

      IAM ARN of the role to use to send application messages. Note: To write application messages
      to CloudWatch, the IAM role that is used must have the ``PutLogEvents`` policy action enabled.
    """


_ClientCreateApplicationInputsInputParallelismTypeDef = TypedDict(
    "_ClientCreateApplicationInputsInputParallelismTypeDef", {"Count": int}, total=False
)


class ClientCreateApplicationInputsInputParallelismTypeDef(
    _ClientCreateApplicationInputsInputParallelismTypeDef
):
    """
    Type definition for `ClientCreateApplicationInputs` `InputParallelism`

    Describes the number of in-application streams to create.

    Data from your source is routed to these in-application input streams.

    (see `Configuring Application Input
    <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-input.html>`__ .

    - **Count** *(integer) --*

      Number of in-application streams to create. For more information, see `Limits
      <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/limits.html>`__ .
    """


_ClientCreateApplicationInputsInputProcessingConfigurationInputLambdaProcessorTypeDef = TypedDict(
    "_ClientCreateApplicationInputsInputProcessingConfigurationInputLambdaProcessorTypeDef",
    {"ResourceARN": str, "RoleARN": str},
)


class ClientCreateApplicationInputsInputProcessingConfigurationInputLambdaProcessorTypeDef(
    _ClientCreateApplicationInputsInputProcessingConfigurationInputLambdaProcessorTypeDef
):
    """
    Type definition for `ClientCreateApplicationInputsInputProcessingConfiguration` `InputLambdaProcessor`

    The `InputLambdaProcessor
    <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_InputLambdaProcessor.html>`__
    that is used to preprocess the records in the stream before being processed by your
    application code.

    - **ResourceARN** *(string) --* **[REQUIRED]**

      The ARN of the `AWS Lambda <https://docs.aws.amazon.com/lambda/>`__ function that
      operates on records in the stream.

      .. note::

        To specify an earlier version of the Lambda function than the latest, include the
        Lambda function version in the Lambda function ARN. For more information about Lambda
        ARNs, see `Example ARNs\\: AWS Lambda
        </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__

    - **RoleARN** *(string) --* **[REQUIRED]**

      The ARN of the IAM role that is used to access the AWS Lambda function.
    """


_ClientCreateApplicationInputsInputProcessingConfigurationTypeDef = TypedDict(
    "_ClientCreateApplicationInputsInputProcessingConfigurationTypeDef",
    {
        "InputLambdaProcessor": ClientCreateApplicationInputsInputProcessingConfigurationInputLambdaProcessorTypeDef
    },
)


class ClientCreateApplicationInputsInputProcessingConfigurationTypeDef(
    _ClientCreateApplicationInputsInputProcessingConfigurationTypeDef
):
    """
    Type definition for `ClientCreateApplicationInputs` `InputProcessingConfiguration`

    The `InputProcessingConfiguration
    <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_InputProcessingConfiguration.html>`__
    for the input. An input processor transforms records as they are received from the stream,
    before the application's SQL code executes. Currently, the only input processing
    configuration available is `InputLambdaProcessor
    <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_InputLambdaProcessor.html>`__ .

    - **InputLambdaProcessor** *(dict) --* **[REQUIRED]**

      The `InputLambdaProcessor
      <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_InputLambdaProcessor.html>`__
      that is used to preprocess the records in the stream before being processed by your
      application code.

      - **ResourceARN** *(string) --* **[REQUIRED]**

        The ARN of the `AWS Lambda <https://docs.aws.amazon.com/lambda/>`__ function that
        operates on records in the stream.

        .. note::

          To specify an earlier version of the Lambda function than the latest, include the
          Lambda function version in the Lambda function ARN. For more information about Lambda
          ARNs, see `Example ARNs\\: AWS Lambda
          </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__

      - **RoleARN** *(string) --* **[REQUIRED]**

        The ARN of the IAM role that is used to access the AWS Lambda function.
    """


_RequiredClientCreateApplicationInputsInputSchemaRecordColumnsTypeDef = TypedDict(
    "_RequiredClientCreateApplicationInputsInputSchemaRecordColumnsTypeDef",
    {"Name": str, "SqlType": str},
)
_OptionalClientCreateApplicationInputsInputSchemaRecordColumnsTypeDef = TypedDict(
    "_OptionalClientCreateApplicationInputsInputSchemaRecordColumnsTypeDef",
    {"Mapping": str},
    total=False,
)


class ClientCreateApplicationInputsInputSchemaRecordColumnsTypeDef(
    _RequiredClientCreateApplicationInputsInputSchemaRecordColumnsTypeDef,
    _OptionalClientCreateApplicationInputsInputSchemaRecordColumnsTypeDef,
):
    """
    Type definition for `ClientCreateApplicationInputsInputSchema` `RecordColumns`

    Describes the mapping of each data element in the streaming source to the corresponding
    column in the in-application stream.

    Also used to describe the format of the reference data source.

    - **Name** *(string) --* **[REQUIRED]**

      Name of the column created in the in-application input stream or reference table.

    - **Mapping** *(string) --*

      Reference to the data element in the streaming input or the reference data source. This
      element is required if the `RecordFormatType
      <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_RecordFormat.html#analytics-Type-RecordFormat-RecordFormatTypel>`__
      is ``JSON`` .

    - **SqlType** *(string) --* **[REQUIRED]**

      Type of column created in the in-application input stream or reference table.
    """


_ClientCreateApplicationInputsInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef = TypedDict(
    "_ClientCreateApplicationInputsInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef",
    {"RecordRowDelimiter": str, "RecordColumnDelimiter": str},
)


class ClientCreateApplicationInputsInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef(
    _ClientCreateApplicationInputsInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef
):
    """
    Type definition for `ClientCreateApplicationInputsInputSchemaRecordFormatMappingParameters` `CSVMappingParameters`

    Provides additional mapping information when the record format uses delimiters (for
    example, CSV).

    - **RecordRowDelimiter** *(string) --* **[REQUIRED]**

      Row delimiter. For example, in a CSV format, *'\\n'* is the typical row delimiter.

    - **RecordColumnDelimiter** *(string) --* **[REQUIRED]**

      Column delimiter. For example, in a CSV format, a comma (",") is the typical column
      delimiter.
    """


_ClientCreateApplicationInputsInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef = TypedDict(
    "_ClientCreateApplicationInputsInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef",
    {"RecordRowPath": str},
)


class ClientCreateApplicationInputsInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef(
    _ClientCreateApplicationInputsInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef
):
    """
    Type definition for `ClientCreateApplicationInputsInputSchemaRecordFormatMappingParameters` `JSONMappingParameters`

    Provides additional mapping information when JSON is the record format on the streaming
    source.

    - **RecordRowPath** *(string) --* **[REQUIRED]**

      Path to the top-level parent that contains the records.
    """


_ClientCreateApplicationInputsInputSchemaRecordFormatMappingParametersTypeDef = TypedDict(
    "_ClientCreateApplicationInputsInputSchemaRecordFormatMappingParametersTypeDef",
    {
        "JSONMappingParameters": ClientCreateApplicationInputsInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef,
        "CSVMappingParameters": ClientCreateApplicationInputsInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef,
    },
    total=False,
)


class ClientCreateApplicationInputsInputSchemaRecordFormatMappingParametersTypeDef(
    _ClientCreateApplicationInputsInputSchemaRecordFormatMappingParametersTypeDef
):
    """
    Type definition for `ClientCreateApplicationInputsInputSchemaRecordFormat` `MappingParameters`

    When configuring application input at the time of creating or updating an application,
    provides additional mapping information specific to the record format (such as JSON, CSV,
    or record fields delimited by some delimiter) on the streaming source.

    - **JSONMappingParameters** *(dict) --*

      Provides additional mapping information when JSON is the record format on the streaming
      source.

      - **RecordRowPath** *(string) --* **[REQUIRED]**

        Path to the top-level parent that contains the records.

    - **CSVMappingParameters** *(dict) --*

      Provides additional mapping information when the record format uses delimiters (for
      example, CSV).

      - **RecordRowDelimiter** *(string) --* **[REQUIRED]**

        Row delimiter. For example, in a CSV format, *'\\n'* is the typical row delimiter.

      - **RecordColumnDelimiter** *(string) --* **[REQUIRED]**

        Column delimiter. For example, in a CSV format, a comma (",") is the typical column
        delimiter.
    """


_RequiredClientCreateApplicationInputsInputSchemaRecordFormatTypeDef = TypedDict(
    "_RequiredClientCreateApplicationInputsInputSchemaRecordFormatTypeDef",
    {"RecordFormatType": str},
)
_OptionalClientCreateApplicationInputsInputSchemaRecordFormatTypeDef = TypedDict(
    "_OptionalClientCreateApplicationInputsInputSchemaRecordFormatTypeDef",
    {
        "MappingParameters": ClientCreateApplicationInputsInputSchemaRecordFormatMappingParametersTypeDef
    },
    total=False,
)


class ClientCreateApplicationInputsInputSchemaRecordFormatTypeDef(
    _RequiredClientCreateApplicationInputsInputSchemaRecordFormatTypeDef,
    _OptionalClientCreateApplicationInputsInputSchemaRecordFormatTypeDef,
):
    """
    Type definition for `ClientCreateApplicationInputsInputSchema` `RecordFormat`

    Specifies the format of the records on the streaming source.

    - **RecordFormatType** *(string) --* **[REQUIRED]**

      The type of record format.

    - **MappingParameters** *(dict) --*

      When configuring application input at the time of creating or updating an application,
      provides additional mapping information specific to the record format (such as JSON, CSV,
      or record fields delimited by some delimiter) on the streaming source.

      - **JSONMappingParameters** *(dict) --*

        Provides additional mapping information when JSON is the record format on the streaming
        source.

        - **RecordRowPath** *(string) --* **[REQUIRED]**

          Path to the top-level parent that contains the records.

      - **CSVMappingParameters** *(dict) --*

        Provides additional mapping information when the record format uses delimiters (for
        example, CSV).

        - **RecordRowDelimiter** *(string) --* **[REQUIRED]**

          Row delimiter. For example, in a CSV format, *'\\n'* is the typical row delimiter.

        - **RecordColumnDelimiter** *(string) --* **[REQUIRED]**

          Column delimiter. For example, in a CSV format, a comma (",") is the typical column
          delimiter.
    """


_RequiredClientCreateApplicationInputsInputSchemaTypeDef = TypedDict(
    "_RequiredClientCreateApplicationInputsInputSchemaTypeDef",
    {
        "RecordFormat": ClientCreateApplicationInputsInputSchemaRecordFormatTypeDef,
        "RecordColumns": List[
            ClientCreateApplicationInputsInputSchemaRecordColumnsTypeDef
        ],
    },
)
_OptionalClientCreateApplicationInputsInputSchemaTypeDef = TypedDict(
    "_OptionalClientCreateApplicationInputsInputSchemaTypeDef",
    {"RecordEncoding": str},
    total=False,
)


class ClientCreateApplicationInputsInputSchemaTypeDef(
    _RequiredClientCreateApplicationInputsInputSchemaTypeDef,
    _OptionalClientCreateApplicationInputsInputSchemaTypeDef,
):
    """
    Type definition for `ClientCreateApplicationInputs` `InputSchema`

    Describes the format of the data in the streaming source, and how each data element maps to
    corresponding columns in the in-application stream that is being created.

    Also used to describe the format of the reference data source.

    - **RecordFormat** *(dict) --* **[REQUIRED]**

      Specifies the format of the records on the streaming source.

      - **RecordFormatType** *(string) --* **[REQUIRED]**

        The type of record format.

      - **MappingParameters** *(dict) --*

        When configuring application input at the time of creating or updating an application,
        provides additional mapping information specific to the record format (such as JSON, CSV,
        or record fields delimited by some delimiter) on the streaming source.

        - **JSONMappingParameters** *(dict) --*

          Provides additional mapping information when JSON is the record format on the streaming
          source.

          - **RecordRowPath** *(string) --* **[REQUIRED]**

            Path to the top-level parent that contains the records.

        - **CSVMappingParameters** *(dict) --*

          Provides additional mapping information when the record format uses delimiters (for
          example, CSV).

          - **RecordRowDelimiter** *(string) --* **[REQUIRED]**

            Row delimiter. For example, in a CSV format, *'\\n'* is the typical row delimiter.

          - **RecordColumnDelimiter** *(string) --* **[REQUIRED]**

            Column delimiter. For example, in a CSV format, a comma (",") is the typical column
            delimiter.

    - **RecordEncoding** *(string) --*

      Specifies the encoding of the records in the streaming source. For example, UTF-8.

    - **RecordColumns** *(list) --* **[REQUIRED]**

      A list of ``RecordColumn`` objects.

      - *(dict) --*

        Describes the mapping of each data element in the streaming source to the corresponding
        column in the in-application stream.

        Also used to describe the format of the reference data source.

        - **Name** *(string) --* **[REQUIRED]**

          Name of the column created in the in-application input stream or reference table.

        - **Mapping** *(string) --*

          Reference to the data element in the streaming input or the reference data source. This
          element is required if the `RecordFormatType
          <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_RecordFormat.html#analytics-Type-RecordFormat-RecordFormatTypel>`__
          is ``JSON`` .

        - **SqlType** *(string) --* **[REQUIRED]**

          Type of column created in the in-application input stream or reference table.
    """


_ClientCreateApplicationInputsKinesisFirehoseInputTypeDef = TypedDict(
    "_ClientCreateApplicationInputsKinesisFirehoseInputTypeDef",
    {"ResourceARN": str, "RoleARN": str},
)


class ClientCreateApplicationInputsKinesisFirehoseInputTypeDef(
    _ClientCreateApplicationInputsKinesisFirehoseInputTypeDef
):
    """
    Type definition for `ClientCreateApplicationInputs` `KinesisFirehoseInput`

    If the streaming source is an Amazon Kinesis Firehose delivery stream, identifies the
    delivery stream's ARN and an IAM role that enables Amazon Kinesis Analytics to access the
    stream on your behalf.

    Note: Either ``KinesisStreamsInput`` or ``KinesisFirehoseInput`` is required.

    - **ResourceARN** *(string) --* **[REQUIRED]**

      ARN of the input delivery stream.

    - **RoleARN** *(string) --* **[REQUIRED]**

      ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream on your
      behalf. You need to make sure that the role has the necessary permissions to access the
      stream.
    """


_ClientCreateApplicationInputsKinesisStreamsInputTypeDef = TypedDict(
    "_ClientCreateApplicationInputsKinesisStreamsInputTypeDef",
    {"ResourceARN": str, "RoleARN": str},
)


class ClientCreateApplicationInputsKinesisStreamsInputTypeDef(
    _ClientCreateApplicationInputsKinesisStreamsInputTypeDef
):
    """
    Type definition for `ClientCreateApplicationInputs` `KinesisStreamsInput`

    If the streaming source is an Amazon Kinesis stream, identifies the stream's Amazon Resource
    Name (ARN) and an IAM role that enables Amazon Kinesis Analytics to access the stream on your
    behalf.

    Note: Either ``KinesisStreamsInput`` or ``KinesisFirehoseInput`` is required.

    - **ResourceARN** *(string) --* **[REQUIRED]**

      ARN of the input Amazon Kinesis stream to read.

    - **RoleARN** *(string) --* **[REQUIRED]**

      ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream on your
      behalf. You need to grant the necessary permissions to this role.
    """


_RequiredClientCreateApplicationInputsTypeDef = TypedDict(
    "_RequiredClientCreateApplicationInputsTypeDef",
    {"NamePrefix": str, "InputSchema": ClientCreateApplicationInputsInputSchemaTypeDef},
)
_OptionalClientCreateApplicationInputsTypeDef = TypedDict(
    "_OptionalClientCreateApplicationInputsTypeDef",
    {
        "InputProcessingConfiguration": ClientCreateApplicationInputsInputProcessingConfigurationTypeDef,
        "KinesisStreamsInput": ClientCreateApplicationInputsKinesisStreamsInputTypeDef,
        "KinesisFirehoseInput": ClientCreateApplicationInputsKinesisFirehoseInputTypeDef,
        "InputParallelism": ClientCreateApplicationInputsInputParallelismTypeDef,
    },
    total=False,
)


class ClientCreateApplicationInputsTypeDef(
    _RequiredClientCreateApplicationInputsTypeDef,
    _OptionalClientCreateApplicationInputsTypeDef,
):
    """
    Type definition for `ClientCreateApplication` `Inputs`

    When you configure the application input, you specify the streaming source, the in-application
    stream name that is created, and the mapping between the two. For more information, see
    `Configuring Application Input
    <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-input.html>`__ .

    - **NamePrefix** *(string) --* **[REQUIRED]**

      Name prefix to use when creating an in-application stream. Suppose that you specify a prefix
      "MyInApplicationStream." Amazon Kinesis Analytics then creates one or more (as per the
      ``InputParallelism`` count you specified) in-application streams with names
      "MyInApplicationStream_001," "MyInApplicationStream_002," and so on.

    - **InputProcessingConfiguration** *(dict) --*

      The `InputProcessingConfiguration
      <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_InputProcessingConfiguration.html>`__
      for the input. An input processor transforms records as they are received from the stream,
      before the application's SQL code executes. Currently, the only input processing
      configuration available is `InputLambdaProcessor
      <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_InputLambdaProcessor.html>`__ .

      - **InputLambdaProcessor** *(dict) --* **[REQUIRED]**

        The `InputLambdaProcessor
        <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_InputLambdaProcessor.html>`__
        that is used to preprocess the records in the stream before being processed by your
        application code.

        - **ResourceARN** *(string) --* **[REQUIRED]**

          The ARN of the `AWS Lambda <https://docs.aws.amazon.com/lambda/>`__ function that
          operates on records in the stream.

          .. note::

            To specify an earlier version of the Lambda function than the latest, include the
            Lambda function version in the Lambda function ARN. For more information about Lambda
            ARNs, see `Example ARNs\\: AWS Lambda
            </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__

        - **RoleARN** *(string) --* **[REQUIRED]**

          The ARN of the IAM role that is used to access the AWS Lambda function.

    - **KinesisStreamsInput** *(dict) --*

      If the streaming source is an Amazon Kinesis stream, identifies the stream's Amazon Resource
      Name (ARN) and an IAM role that enables Amazon Kinesis Analytics to access the stream on your
      behalf.

      Note: Either ``KinesisStreamsInput`` or ``KinesisFirehoseInput`` is required.

      - **ResourceARN** *(string) --* **[REQUIRED]**

        ARN of the input Amazon Kinesis stream to read.

      - **RoleARN** *(string) --* **[REQUIRED]**

        ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream on your
        behalf. You need to grant the necessary permissions to this role.

    - **KinesisFirehoseInput** *(dict) --*

      If the streaming source is an Amazon Kinesis Firehose delivery stream, identifies the
      delivery stream's ARN and an IAM role that enables Amazon Kinesis Analytics to access the
      stream on your behalf.

      Note: Either ``KinesisStreamsInput`` or ``KinesisFirehoseInput`` is required.

      - **ResourceARN** *(string) --* **[REQUIRED]**

        ARN of the input delivery stream.

      - **RoleARN** *(string) --* **[REQUIRED]**

        ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream on your
        behalf. You need to make sure that the role has the necessary permissions to access the
        stream.

    - **InputParallelism** *(dict) --*

      Describes the number of in-application streams to create.

      Data from your source is routed to these in-application input streams.

      (see `Configuring Application Input
      <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-input.html>`__ .

      - **Count** *(integer) --*

        Number of in-application streams to create. For more information, see `Limits
        <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/limits.html>`__ .

    - **InputSchema** *(dict) --* **[REQUIRED]**

      Describes the format of the data in the streaming source, and how each data element maps to
      corresponding columns in the in-application stream that is being created.

      Also used to describe the format of the reference data source.

      - **RecordFormat** *(dict) --* **[REQUIRED]**

        Specifies the format of the records on the streaming source.

        - **RecordFormatType** *(string) --* **[REQUIRED]**

          The type of record format.

        - **MappingParameters** *(dict) --*

          When configuring application input at the time of creating or updating an application,
          provides additional mapping information specific to the record format (such as JSON, CSV,
          or record fields delimited by some delimiter) on the streaming source.

          - **JSONMappingParameters** *(dict) --*

            Provides additional mapping information when JSON is the record format on the streaming
            source.

            - **RecordRowPath** *(string) --* **[REQUIRED]**

              Path to the top-level parent that contains the records.

          - **CSVMappingParameters** *(dict) --*

            Provides additional mapping information when the record format uses delimiters (for
            example, CSV).

            - **RecordRowDelimiter** *(string) --* **[REQUIRED]**

              Row delimiter. For example, in a CSV format, *'\\n'* is the typical row delimiter.

            - **RecordColumnDelimiter** *(string) --* **[REQUIRED]**

              Column delimiter. For example, in a CSV format, a comma (",") is the typical column
              delimiter.

      - **RecordEncoding** *(string) --*

        Specifies the encoding of the records in the streaming source. For example, UTF-8.

      - **RecordColumns** *(list) --* **[REQUIRED]**

        A list of ``RecordColumn`` objects.

        - *(dict) --*

          Describes the mapping of each data element in the streaming source to the corresponding
          column in the in-application stream.

          Also used to describe the format of the reference data source.

          - **Name** *(string) --* **[REQUIRED]**

            Name of the column created in the in-application input stream or reference table.

          - **Mapping** *(string) --*

            Reference to the data element in the streaming input or the reference data source. This
            element is required if the `RecordFormatType
            <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_RecordFormat.html#analytics-Type-RecordFormat-RecordFormatTypel>`__
            is ``JSON`` .

          - **SqlType** *(string) --* **[REQUIRED]**

            Type of column created in the in-application input stream or reference table.
    """


_ClientCreateApplicationOutputsDestinationSchemaTypeDef = TypedDict(
    "_ClientCreateApplicationOutputsDestinationSchemaTypeDef", {"RecordFormatType": str}
)


class ClientCreateApplicationOutputsDestinationSchemaTypeDef(
    _ClientCreateApplicationOutputsDestinationSchemaTypeDef
):
    """
    Type definition for `ClientCreateApplicationOutputs` `DestinationSchema`

    Describes the data format when records are written to the destination. For more information,
    see `Configuring Application Output
    <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-output.html>`__ .

    - **RecordFormatType** *(string) --* **[REQUIRED]**

      Specifies the format of the records on the output stream.
    """


_ClientCreateApplicationOutputsKinesisFirehoseOutputTypeDef = TypedDict(
    "_ClientCreateApplicationOutputsKinesisFirehoseOutputTypeDef",
    {"ResourceARN": str, "RoleARN": str},
)


class ClientCreateApplicationOutputsKinesisFirehoseOutputTypeDef(
    _ClientCreateApplicationOutputsKinesisFirehoseOutputTypeDef
):
    """
    Type definition for `ClientCreateApplicationOutputs` `KinesisFirehoseOutput`

    Identifies an Amazon Kinesis Firehose delivery stream as the destination.

    - **ResourceARN** *(string) --* **[REQUIRED]**

      ARN of the destination Amazon Kinesis Firehose delivery stream to write to.

    - **RoleARN** *(string) --* **[REQUIRED]**

      ARN of the IAM role that Amazon Kinesis Analytics can assume to write to the destination
      stream on your behalf. You need to grant the necessary permissions to this role.
    """


_ClientCreateApplicationOutputsKinesisStreamsOutputTypeDef = TypedDict(
    "_ClientCreateApplicationOutputsKinesisStreamsOutputTypeDef",
    {"ResourceARN": str, "RoleARN": str},
)


class ClientCreateApplicationOutputsKinesisStreamsOutputTypeDef(
    _ClientCreateApplicationOutputsKinesisStreamsOutputTypeDef
):
    """
    Type definition for `ClientCreateApplicationOutputs` `KinesisStreamsOutput`

    Identifies an Amazon Kinesis stream as the destination.

    - **ResourceARN** *(string) --* **[REQUIRED]**

      ARN of the destination Amazon Kinesis stream to write to.

    - **RoleARN** *(string) --* **[REQUIRED]**

      ARN of the IAM role that Amazon Kinesis Analytics can assume to write to the destination
      stream on your behalf. You need to grant the necessary permissions to this role.
    """


_ClientCreateApplicationOutputsLambdaOutputTypeDef = TypedDict(
    "_ClientCreateApplicationOutputsLambdaOutputTypeDef",
    {"ResourceARN": str, "RoleARN": str},
)


class ClientCreateApplicationOutputsLambdaOutputTypeDef(
    _ClientCreateApplicationOutputsLambdaOutputTypeDef
):
    """
    Type definition for `ClientCreateApplicationOutputs` `LambdaOutput`

    Identifies an AWS Lambda function as the destination.

    - **ResourceARN** *(string) --* **[REQUIRED]**

      Amazon Resource Name (ARN) of the destination Lambda function to write to.

      .. note::

        To specify an earlier version of the Lambda function than the latest, include the Lambda
        function version in the Lambda function ARN. For more information about Lambda ARNs, see
        `Example ARNs\\: AWS Lambda
        </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__

    - **RoleARN** *(string) --* **[REQUIRED]**

      ARN of the IAM role that Amazon Kinesis Analytics can assume to write to the destination
      function on your behalf. You need to grant the necessary permissions to this role.
    """


_RequiredClientCreateApplicationOutputsTypeDef = TypedDict(
    "_RequiredClientCreateApplicationOutputsTypeDef",
    {
        "Name": str,
        "DestinationSchema": ClientCreateApplicationOutputsDestinationSchemaTypeDef,
    },
)
_OptionalClientCreateApplicationOutputsTypeDef = TypedDict(
    "_OptionalClientCreateApplicationOutputsTypeDef",
    {
        "KinesisStreamsOutput": ClientCreateApplicationOutputsKinesisStreamsOutputTypeDef,
        "KinesisFirehoseOutput": ClientCreateApplicationOutputsKinesisFirehoseOutputTypeDef,
        "LambdaOutput": ClientCreateApplicationOutputsLambdaOutputTypeDef,
    },
    total=False,
)


class ClientCreateApplicationOutputsTypeDef(
    _RequiredClientCreateApplicationOutputsTypeDef,
    _OptionalClientCreateApplicationOutputsTypeDef,
):
    """
    Type definition for `ClientCreateApplication` `Outputs`

    Describes application output configuration in which you identify an in-application stream and a
    destination where you want the in-application stream data to be written. The destination can be
    an Amazon Kinesis stream or an Amazon Kinesis Firehose delivery stream.

    For limits on how many destinations an application can write and other limitations, see `Limits
    <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/limits.html>`__ .

    - **Name** *(string) --* **[REQUIRED]**

      Name of the in-application stream.

    - **KinesisStreamsOutput** *(dict) --*

      Identifies an Amazon Kinesis stream as the destination.

      - **ResourceARN** *(string) --* **[REQUIRED]**

        ARN of the destination Amazon Kinesis stream to write to.

      - **RoleARN** *(string) --* **[REQUIRED]**

        ARN of the IAM role that Amazon Kinesis Analytics can assume to write to the destination
        stream on your behalf. You need to grant the necessary permissions to this role.

    - **KinesisFirehoseOutput** *(dict) --*

      Identifies an Amazon Kinesis Firehose delivery stream as the destination.

      - **ResourceARN** *(string) --* **[REQUIRED]**

        ARN of the destination Amazon Kinesis Firehose delivery stream to write to.

      - **RoleARN** *(string) --* **[REQUIRED]**

        ARN of the IAM role that Amazon Kinesis Analytics can assume to write to the destination
        stream on your behalf. You need to grant the necessary permissions to this role.

    - **LambdaOutput** *(dict) --*

      Identifies an AWS Lambda function as the destination.

      - **ResourceARN** *(string) --* **[REQUIRED]**

        Amazon Resource Name (ARN) of the destination Lambda function to write to.

        .. note::

          To specify an earlier version of the Lambda function than the latest, include the Lambda
          function version in the Lambda function ARN. For more information about Lambda ARNs, see
          `Example ARNs\\: AWS Lambda
          </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__

      - **RoleARN** *(string) --* **[REQUIRED]**

        ARN of the IAM role that Amazon Kinesis Analytics can assume to write to the destination
        function on your behalf. You need to grant the necessary permissions to this role.

    - **DestinationSchema** *(dict) --* **[REQUIRED]**

      Describes the data format when records are written to the destination. For more information,
      see `Configuring Application Output
      <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-output.html>`__ .

      - **RecordFormatType** *(string) --* **[REQUIRED]**

        Specifies the format of the records on the output stream.
    """


_ClientCreateApplicationResponseApplicationSummaryTypeDef = TypedDict(
    "_ClientCreateApplicationResponseApplicationSummaryTypeDef",
    {"ApplicationName": str, "ApplicationARN": str, "ApplicationStatus": str},
    total=False,
)


class ClientCreateApplicationResponseApplicationSummaryTypeDef(
    _ClientCreateApplicationResponseApplicationSummaryTypeDef
):
    """
    Type definition for `ClientCreateApplicationResponse` `ApplicationSummary`

    In response to your ``CreateApplication`` request, Amazon Kinesis Analytics returns a
    response with a summary of the application it created, including the application Amazon
    Resource Name (ARN), name, and status.

    - **ApplicationName** *(string) --*

      Name of the application.

    - **ApplicationARN** *(string) --*

      ARN of the application.

    - **ApplicationStatus** *(string) --*

      Status of the application.
    """


_ClientCreateApplicationResponseTypeDef = TypedDict(
    "_ClientCreateApplicationResponseTypeDef",
    {"ApplicationSummary": ClientCreateApplicationResponseApplicationSummaryTypeDef},
    total=False,
)


class ClientCreateApplicationResponseTypeDef(_ClientCreateApplicationResponseTypeDef):
    """
    Type definition for `ClientCreateApplication` `Response`

    TBD

    - **ApplicationSummary** *(dict) --*

      In response to your ``CreateApplication`` request, Amazon Kinesis Analytics returns a
      response with a summary of the application it created, including the application Amazon
      Resource Name (ARN), name, and status.

      - **ApplicationName** *(string) --*

        Name of the application.

      - **ApplicationARN** *(string) --*

        ARN of the application.

      - **ApplicationStatus** *(string) --*

        Status of the application.
    """


_RequiredClientCreateApplicationTagsTypeDef = TypedDict(
    "_RequiredClientCreateApplicationTagsTypeDef", {"Key": str}
)
_OptionalClientCreateApplicationTagsTypeDef = TypedDict(
    "_OptionalClientCreateApplicationTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateApplicationTagsTypeDef(
    _RequiredClientCreateApplicationTagsTypeDef,
    _OptionalClientCreateApplicationTagsTypeDef,
):
    """
    Type definition for `ClientCreateApplication` `Tags`

    A key-value pair (the value is optional) that you can define and assign to AWS resources. If
    you specify a tag that already exists, the tag value is replaced with the value that you
    specify in the request. Note that the maximum number of application tags includes system tags.
    The maximum number of user-defined application tags is 50. For more information, see `Using
    Tagging <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-tagging.html>`__ .

    - **Key** *(string) --* **[REQUIRED]**

      The key of the key-value tag.

    - **Value** *(string) --*

      The value of the key-value tag. The value is optional.
    """


_ClientDescribeApplicationResponseApplicationDetailCloudWatchLoggingOptionDescriptionsTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailCloudWatchLoggingOptionDescriptionsTypeDef",
    {"CloudWatchLoggingOptionId": str, "LogStreamARN": str, "RoleARN": str},
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailCloudWatchLoggingOptionDescriptionsTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailCloudWatchLoggingOptionDescriptionsTypeDef
):
    """
    Type definition for `ClientDescribeApplicationResponseApplicationDetail` `CloudWatchLoggingOptionDescriptions`

    Description of the CloudWatch logging option.

    - **CloudWatchLoggingOptionId** *(string) --*

      ID of the CloudWatch logging option description.

    - **LogStreamARN** *(string) --*

      ARN of the CloudWatch log to receive application messages.

    - **RoleARN** *(string) --*

      IAM ARN of the role to use to send application messages. Note: To write application
      messages to CloudWatch, the IAM role used must have the ``PutLogEvents`` policy action
      enabled.
    """


_ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputParallelismTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputParallelismTypeDef",
    {"Count": int},
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputParallelismTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputParallelismTypeDef
):
    """
    Type definition for `ClientDescribeApplicationResponseApplicationDetailInputDescriptions` `InputParallelism`

    Describes the configured parallelism (number of in-application streams mapped to the
    streaming source).

    - **Count** *(integer) --*

      Number of in-application streams to create. For more information, see `Limits
      <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/limits.html>`__ .
    """


_ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputProcessingConfigurationDescriptionInputLambdaProcessorDescriptionTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputProcessingConfigurationDescriptionInputLambdaProcessorDescriptionTypeDef",
    {"ResourceARN": str, "RoleARN": str},
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputProcessingConfigurationDescriptionInputLambdaProcessorDescriptionTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputProcessingConfigurationDescriptionInputLambdaProcessorDescriptionTypeDef
):
    """
    Type definition for `ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputProcessingConfigurationDescription` `InputLambdaProcessorDescription`

    Provides configuration information about the associated
    `InputLambdaProcessorDescription
    <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_InputLambdaProcessorDescription.html>`__
    .

    - **ResourceARN** *(string) --*

      The ARN of the `AWS Lambda <https://docs.aws.amazon.com/lambda/>`__ function that
      is used to preprocess the records in the stream.

    - **RoleARN** *(string) --*

      The ARN of the IAM role that is used to access the AWS Lambda function.
    """


_ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputProcessingConfigurationDescriptionTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputProcessingConfigurationDescriptionTypeDef",
    {
        "InputLambdaProcessorDescription": ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputProcessingConfigurationDescriptionInputLambdaProcessorDescriptionTypeDef
    },
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputProcessingConfigurationDescriptionTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputProcessingConfigurationDescriptionTypeDef
):
    """
    Type definition for `ClientDescribeApplicationResponseApplicationDetailInputDescriptions` `InputProcessingConfigurationDescription`

    The description of the preprocessor that executes on records in this input before the
    application's code is run.

    - **InputLambdaProcessorDescription** *(dict) --*

      Provides configuration information about the associated
      `InputLambdaProcessorDescription
      <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_InputLambdaProcessorDescription.html>`__
      .

      - **ResourceARN** *(string) --*

        The ARN of the `AWS Lambda <https://docs.aws.amazon.com/lambda/>`__ function that
        is used to preprocess the records in the stream.

      - **RoleARN** *(string) --*

        The ARN of the IAM role that is used to access the AWS Lambda function.
    """


_ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordColumnsTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordColumnsTypeDef",
    {"Name": str, "Mapping": str, "SqlType": str},
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordColumnsTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordColumnsTypeDef
):
    """
    Type definition for `ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchema` `RecordColumns`

    Describes the mapping of each data element in the streaming source to the
    corresponding column in the in-application stream.

    Also used to describe the format of the reference data source.

    - **Name** *(string) --*

      Name of the column created in the in-application input stream or reference table.

    - **Mapping** *(string) --*

      Reference to the data element in the streaming input or the reference data
      source. This element is required if the `RecordFormatType
      <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_RecordFormat.html#analytics-Type-RecordFormat-RecordFormatTypel>`__
      is ``JSON`` .

    - **SqlType** *(string) --*

      Type of column created in the in-application input stream or reference table.
    """


_ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef",
    {"RecordRowDelimiter": str, "RecordColumnDelimiter": str},
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef
):
    """
    Type definition for `ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordFormatMappingParameters` `CSVMappingParameters`

    Provides additional mapping information when the record format uses delimiters
    (for example, CSV).

    - **RecordRowDelimiter** *(string) --*

      Row delimiter. For example, in a CSV format, *'\\n'* is the typical row
      delimiter.

    - **RecordColumnDelimiter** *(string) --*

      Column delimiter. For example, in a CSV format, a comma (",") is the typical
      column delimiter.
    """


_ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef",
    {"RecordRowPath": str},
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef
):
    """
    Type definition for `ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordFormatMappingParameters` `JSONMappingParameters`

    Provides additional mapping information when JSON is the record format on the
    streaming source.

    - **RecordRowPath** *(string) --*

      Path to the top-level parent that contains the records.
    """


_ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordFormatMappingParametersTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordFormatMappingParametersTypeDef",
    {
        "JSONMappingParameters": ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef,
        "CSVMappingParameters": ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef,
    },
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordFormatMappingParametersTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordFormatMappingParametersTypeDef
):
    """
    Type definition for `ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordFormat` `MappingParameters`

    When configuring application input at the time of creating or updating an
    application, provides additional mapping information specific to the record format
    (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming
    source.

    - **JSONMappingParameters** *(dict) --*

      Provides additional mapping information when JSON is the record format on the
      streaming source.

      - **RecordRowPath** *(string) --*

        Path to the top-level parent that contains the records.

    - **CSVMappingParameters** *(dict) --*

      Provides additional mapping information when the record format uses delimiters
      (for example, CSV).

      - **RecordRowDelimiter** *(string) --*

        Row delimiter. For example, in a CSV format, *'\\n'* is the typical row
        delimiter.

      - **RecordColumnDelimiter** *(string) --*

        Column delimiter. For example, in a CSV format, a comma (",") is the typical
        column delimiter.
    """


_ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordFormatTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordFormatTypeDef",
    {
        "RecordFormatType": str,
        "MappingParameters": ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordFormatMappingParametersTypeDef,
    },
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordFormatTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordFormatTypeDef
):
    """
    Type definition for `ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchema` `RecordFormat`

    Specifies the format of the records on the streaming source.

    - **RecordFormatType** *(string) --*

      The type of record format.

    - **MappingParameters** *(dict) --*

      When configuring application input at the time of creating or updating an
      application, provides additional mapping information specific to the record format
      (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming
      source.

      - **JSONMappingParameters** *(dict) --*

        Provides additional mapping information when JSON is the record format on the
        streaming source.

        - **RecordRowPath** *(string) --*

          Path to the top-level parent that contains the records.

      - **CSVMappingParameters** *(dict) --*

        Provides additional mapping information when the record format uses delimiters
        (for example, CSV).

        - **RecordRowDelimiter** *(string) --*

          Row delimiter. For example, in a CSV format, *'\\n'* is the typical row
          delimiter.

        - **RecordColumnDelimiter** *(string) --*

          Column delimiter. For example, in a CSV format, a comma (",") is the typical
          column delimiter.
    """


_ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaTypeDef",
    {
        "RecordFormat": ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordFormatTypeDef,
        "RecordEncoding": str,
        "RecordColumns": List[
            ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordColumnsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaTypeDef
):
    """
    Type definition for `ClientDescribeApplicationResponseApplicationDetailInputDescriptions` `InputSchema`

    Describes the format of the data in the streaming source, and how each data element
    maps to corresponding columns in the in-application stream that is being created.

    - **RecordFormat** *(dict) --*

      Specifies the format of the records on the streaming source.

      - **RecordFormatType** *(string) --*

        The type of record format.

      - **MappingParameters** *(dict) --*

        When configuring application input at the time of creating or updating an
        application, provides additional mapping information specific to the record format
        (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming
        source.

        - **JSONMappingParameters** *(dict) --*

          Provides additional mapping information when JSON is the record format on the
          streaming source.

          - **RecordRowPath** *(string) --*

            Path to the top-level parent that contains the records.

        - **CSVMappingParameters** *(dict) --*

          Provides additional mapping information when the record format uses delimiters
          (for example, CSV).

          - **RecordRowDelimiter** *(string) --*

            Row delimiter. For example, in a CSV format, *'\\n'* is the typical row
            delimiter.

          - **RecordColumnDelimiter** *(string) --*

            Column delimiter. For example, in a CSV format, a comma (",") is the typical
            column delimiter.

    - **RecordEncoding** *(string) --*

      Specifies the encoding of the records in the streaming source. For example, UTF-8.

    - **RecordColumns** *(list) --*

      A list of ``RecordColumn`` objects.

      - *(dict) --*

        Describes the mapping of each data element in the streaming source to the
        corresponding column in the in-application stream.

        Also used to describe the format of the reference data source.

        - **Name** *(string) --*

          Name of the column created in the in-application input stream or reference table.

        - **Mapping** *(string) --*

          Reference to the data element in the streaming input or the reference data
          source. This element is required if the `RecordFormatType
          <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_RecordFormat.html#analytics-Type-RecordFormat-RecordFormatTypel>`__
          is ``JSON`` .

        - **SqlType** *(string) --*

          Type of column created in the in-application input stream or reference table.
    """


_ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputStartingPositionConfigurationTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputStartingPositionConfigurationTypeDef",
    {"InputStartingPosition": str},
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputStartingPositionConfigurationTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputStartingPositionConfigurationTypeDef
):
    """
    Type definition for `ClientDescribeApplicationResponseApplicationDetailInputDescriptions` `InputStartingPositionConfiguration`

    Point at which the application is configured to read from the input stream.

    - **InputStartingPosition** *(string) --*

      The starting position on the stream.

      * ``NOW`` - Start reading just after the most recent record in the stream, start at
      the request time stamp that the customer issued.

      * ``TRIM_HORIZON`` - Start reading at the last untrimmed record in the stream, which
      is the oldest record available in the stream. This option is not available for an
      Amazon Kinesis Firehose delivery stream.

      * ``LAST_STOPPED_POINT`` - Resume reading from where the application last stopped
      reading.
    """


_ClientDescribeApplicationResponseApplicationDetailInputDescriptionsKinesisFirehoseInputDescriptionTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailInputDescriptionsKinesisFirehoseInputDescriptionTypeDef",
    {"ResourceARN": str, "RoleARN": str},
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailInputDescriptionsKinesisFirehoseInputDescriptionTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailInputDescriptionsKinesisFirehoseInputDescriptionTypeDef
):
    """
    Type definition for `ClientDescribeApplicationResponseApplicationDetailInputDescriptions` `KinesisFirehoseInputDescription`

    If an Amazon Kinesis Firehose delivery stream is configured as a streaming source,
    provides the delivery stream's ARN and an IAM role that enables Amazon Kinesis
    Analytics to access the stream on your behalf.

    - **ResourceARN** *(string) --*

      Amazon Resource Name (ARN) of the Amazon Kinesis Firehose delivery stream.

    - **RoleARN** *(string) --*

      ARN of the IAM role that Amazon Kinesis Analytics assumes to access the stream.
    """


_ClientDescribeApplicationResponseApplicationDetailInputDescriptionsKinesisStreamsInputDescriptionTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailInputDescriptionsKinesisStreamsInputDescriptionTypeDef",
    {"ResourceARN": str, "RoleARN": str},
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailInputDescriptionsKinesisStreamsInputDescriptionTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailInputDescriptionsKinesisStreamsInputDescriptionTypeDef
):
    """
    Type definition for `ClientDescribeApplicationResponseApplicationDetailInputDescriptions` `KinesisStreamsInputDescription`

    If an Amazon Kinesis stream is configured as streaming source, provides Amazon Kinesis
    stream's Amazon Resource Name (ARN) and an IAM role that enables Amazon Kinesis
    Analytics to access the stream on your behalf.

    - **ResourceARN** *(string) --*

      Amazon Resource Name (ARN) of the Amazon Kinesis stream.

    - **RoleARN** *(string) --*

      ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream.
    """


_ClientDescribeApplicationResponseApplicationDetailInputDescriptionsTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailInputDescriptionsTypeDef",
    {
        "InputId": str,
        "NamePrefix": str,
        "InAppStreamNames": List[str],
        "InputProcessingConfigurationDescription": ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputProcessingConfigurationDescriptionTypeDef,
        "KinesisStreamsInputDescription": ClientDescribeApplicationResponseApplicationDetailInputDescriptionsKinesisStreamsInputDescriptionTypeDef,
        "KinesisFirehoseInputDescription": ClientDescribeApplicationResponseApplicationDetailInputDescriptionsKinesisFirehoseInputDescriptionTypeDef,
        "InputSchema": ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaTypeDef,
        "InputParallelism": ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputParallelismTypeDef,
        "InputStartingPositionConfiguration": ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputStartingPositionConfigurationTypeDef,
    },
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailInputDescriptionsTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailInputDescriptionsTypeDef
):
    """
    Type definition for `ClientDescribeApplicationResponseApplicationDetail` `InputDescriptions`

    Describes the application input configuration. For more information, see `Configuring
    Application Input
    <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-input.html>`__ .

    - **InputId** *(string) --*

      Input ID associated with the application input. This is the ID that Amazon Kinesis
      Analytics assigns to each input configuration you add to your application.

    - **NamePrefix** *(string) --*

      In-application name prefix.

    - **InAppStreamNames** *(list) --*

      Returns the in-application stream names that are mapped to the stream source.

      - *(string) --*

    - **InputProcessingConfigurationDescription** *(dict) --*

      The description of the preprocessor that executes on records in this input before the
      application's code is run.

      - **InputLambdaProcessorDescription** *(dict) --*

        Provides configuration information about the associated
        `InputLambdaProcessorDescription
        <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_InputLambdaProcessorDescription.html>`__
        .

        - **ResourceARN** *(string) --*

          The ARN of the `AWS Lambda <https://docs.aws.amazon.com/lambda/>`__ function that
          is used to preprocess the records in the stream.

        - **RoleARN** *(string) --*

          The ARN of the IAM role that is used to access the AWS Lambda function.

    - **KinesisStreamsInputDescription** *(dict) --*

      If an Amazon Kinesis stream is configured as streaming source, provides Amazon Kinesis
      stream's Amazon Resource Name (ARN) and an IAM role that enables Amazon Kinesis
      Analytics to access the stream on your behalf.

      - **ResourceARN** *(string) --*

        Amazon Resource Name (ARN) of the Amazon Kinesis stream.

      - **RoleARN** *(string) --*

        ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream.

    - **KinesisFirehoseInputDescription** *(dict) --*

      If an Amazon Kinesis Firehose delivery stream is configured as a streaming source,
      provides the delivery stream's ARN and an IAM role that enables Amazon Kinesis
      Analytics to access the stream on your behalf.

      - **ResourceARN** *(string) --*

        Amazon Resource Name (ARN) of the Amazon Kinesis Firehose delivery stream.

      - **RoleARN** *(string) --*

        ARN of the IAM role that Amazon Kinesis Analytics assumes to access the stream.

    - **InputSchema** *(dict) --*

      Describes the format of the data in the streaming source, and how each data element
      maps to corresponding columns in the in-application stream that is being created.

      - **RecordFormat** *(dict) --*

        Specifies the format of the records on the streaming source.

        - **RecordFormatType** *(string) --*

          The type of record format.

        - **MappingParameters** *(dict) --*

          When configuring application input at the time of creating or updating an
          application, provides additional mapping information specific to the record format
          (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming
          source.

          - **JSONMappingParameters** *(dict) --*

            Provides additional mapping information when JSON is the record format on the
            streaming source.

            - **RecordRowPath** *(string) --*

              Path to the top-level parent that contains the records.

          - **CSVMappingParameters** *(dict) --*

            Provides additional mapping information when the record format uses delimiters
            (for example, CSV).

            - **RecordRowDelimiter** *(string) --*

              Row delimiter. For example, in a CSV format, *'\\n'* is the typical row
              delimiter.

            - **RecordColumnDelimiter** *(string) --*

              Column delimiter. For example, in a CSV format, a comma (",") is the typical
              column delimiter.

      - **RecordEncoding** *(string) --*

        Specifies the encoding of the records in the streaming source. For example, UTF-8.

      - **RecordColumns** *(list) --*

        A list of ``RecordColumn`` objects.

        - *(dict) --*

          Describes the mapping of each data element in the streaming source to the
          corresponding column in the in-application stream.

          Also used to describe the format of the reference data source.

          - **Name** *(string) --*

            Name of the column created in the in-application input stream or reference table.

          - **Mapping** *(string) --*

            Reference to the data element in the streaming input or the reference data
            source. This element is required if the `RecordFormatType
            <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_RecordFormat.html#analytics-Type-RecordFormat-RecordFormatTypel>`__
            is ``JSON`` .

          - **SqlType** *(string) --*

            Type of column created in the in-application input stream or reference table.

    - **InputParallelism** *(dict) --*

      Describes the configured parallelism (number of in-application streams mapped to the
      streaming source).

      - **Count** *(integer) --*

        Number of in-application streams to create. For more information, see `Limits
        <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/limits.html>`__ .

    - **InputStartingPositionConfiguration** *(dict) --*

      Point at which the application is configured to read from the input stream.

      - **InputStartingPosition** *(string) --*

        The starting position on the stream.

        * ``NOW`` - Start reading just after the most recent record in the stream, start at
        the request time stamp that the customer issued.

        * ``TRIM_HORIZON`` - Start reading at the last untrimmed record in the stream, which
        is the oldest record available in the stream. This option is not available for an
        Amazon Kinesis Firehose delivery stream.

        * ``LAST_STOPPED_POINT`` - Resume reading from where the application last stopped
        reading.
    """


_ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsDestinationSchemaTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsDestinationSchemaTypeDef",
    {"RecordFormatType": str},
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsDestinationSchemaTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsDestinationSchemaTypeDef
):
    """
    Type definition for `ClientDescribeApplicationResponseApplicationDetailOutputDescriptions` `DestinationSchema`

    Data format used for writing data to the destination.

    - **RecordFormatType** *(string) --*

      Specifies the format of the records on the output stream.
    """


_ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsKinesisFirehoseOutputDescriptionTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsKinesisFirehoseOutputDescriptionTypeDef",
    {"ResourceARN": str, "RoleARN": str},
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsKinesisFirehoseOutputDescriptionTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsKinesisFirehoseOutputDescriptionTypeDef
):
    """
    Type definition for `ClientDescribeApplicationResponseApplicationDetailOutputDescriptions` `KinesisFirehoseOutputDescription`

    Describes the Amazon Kinesis Firehose delivery stream configured as the destination
    where output is written.

    - **ResourceARN** *(string) --*

      Amazon Resource Name (ARN) of the Amazon Kinesis Firehose delivery stream.

    - **RoleARN** *(string) --*

      ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream.
    """


_ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsKinesisStreamsOutputDescriptionTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsKinesisStreamsOutputDescriptionTypeDef",
    {"ResourceARN": str, "RoleARN": str},
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsKinesisStreamsOutputDescriptionTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsKinesisStreamsOutputDescriptionTypeDef
):
    """
    Type definition for `ClientDescribeApplicationResponseApplicationDetailOutputDescriptions` `KinesisStreamsOutputDescription`

    Describes Amazon Kinesis stream configured as the destination where output is written.

    - **ResourceARN** *(string) --*

      Amazon Resource Name (ARN) of the Amazon Kinesis stream.

    - **RoleARN** *(string) --*

      ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream.
    """


_ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsLambdaOutputDescriptionTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsLambdaOutputDescriptionTypeDef",
    {"ResourceARN": str, "RoleARN": str},
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsLambdaOutputDescriptionTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsLambdaOutputDescriptionTypeDef
):
    """
    Type definition for `ClientDescribeApplicationResponseApplicationDetailOutputDescriptions` `LambdaOutputDescription`

    Describes the AWS Lambda function configured as the destination where output is written.

    - **ResourceARN** *(string) --*

      Amazon Resource Name (ARN) of the destination Lambda function.

    - **RoleARN** *(string) --*

      ARN of the IAM role that Amazon Kinesis Analytics can assume to write to the
      destination function.
    """


_ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsTypeDef",
    {
        "OutputId": str,
        "Name": str,
        "KinesisStreamsOutputDescription": ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsKinesisStreamsOutputDescriptionTypeDef,
        "KinesisFirehoseOutputDescription": ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsKinesisFirehoseOutputDescriptionTypeDef,
        "LambdaOutputDescription": ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsLambdaOutputDescriptionTypeDef,
        "DestinationSchema": ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsDestinationSchemaTypeDef,
    },
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsTypeDef
):
    """
    Type definition for `ClientDescribeApplicationResponseApplicationDetail` `OutputDescriptions`

    Describes the application output configuration, which includes the in-application stream
    name and the destination where the stream data is written. The destination can be an
    Amazon Kinesis stream or an Amazon Kinesis Firehose delivery stream.

    - **OutputId** *(string) --*

      A unique identifier for the output configuration.

    - **Name** *(string) --*

      Name of the in-application stream configured as output.

    - **KinesisStreamsOutputDescription** *(dict) --*

      Describes Amazon Kinesis stream configured as the destination where output is written.

      - **ResourceARN** *(string) --*

        Amazon Resource Name (ARN) of the Amazon Kinesis stream.

      - **RoleARN** *(string) --*

        ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream.

    - **KinesisFirehoseOutputDescription** *(dict) --*

      Describes the Amazon Kinesis Firehose delivery stream configured as the destination
      where output is written.

      - **ResourceARN** *(string) --*

        Amazon Resource Name (ARN) of the Amazon Kinesis Firehose delivery stream.

      - **RoleARN** *(string) --*

        ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream.

    - **LambdaOutputDescription** *(dict) --*

      Describes the AWS Lambda function configured as the destination where output is written.

      - **ResourceARN** *(string) --*

        Amazon Resource Name (ARN) of the destination Lambda function.

      - **RoleARN** *(string) --*

        ARN of the IAM role that Amazon Kinesis Analytics can assume to write to the
        destination function.

    - **DestinationSchema** *(dict) --*

      Data format used for writing data to the destination.

      - **RecordFormatType** *(string) --*

        Specifies the format of the records on the output stream.
    """


_ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordColumnsTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordColumnsTypeDef",
    {"Name": str, "Mapping": str, "SqlType": str},
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordColumnsTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordColumnsTypeDef
):
    """
    Type definition for `ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchema` `RecordColumns`

    Describes the mapping of each data element in the streaming source to the
    corresponding column in the in-application stream.

    Also used to describe the format of the reference data source.

    - **Name** *(string) --*

      Name of the column created in the in-application input stream or reference table.

    - **Mapping** *(string) --*

      Reference to the data element in the streaming input or the reference data
      source. This element is required if the `RecordFormatType
      <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_RecordFormat.html#analytics-Type-RecordFormat-RecordFormatTypel>`__
      is ``JSON`` .

    - **SqlType** *(string) --*

      Type of column created in the in-application input stream or reference table.
    """


_ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef",
    {"RecordRowDelimiter": str, "RecordColumnDelimiter": str},
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef
):
    """
    Type definition for `ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParameters` `CSVMappingParameters`

    Provides additional mapping information when the record format uses delimiters
    (for example, CSV).

    - **RecordRowDelimiter** *(string) --*

      Row delimiter. For example, in a CSV format, *'\\n'* is the typical row
      delimiter.

    - **RecordColumnDelimiter** *(string) --*

      Column delimiter. For example, in a CSV format, a comma (",") is the typical
      column delimiter.
    """


_ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef",
    {"RecordRowPath": str},
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef
):
    """
    Type definition for `ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParameters` `JSONMappingParameters`

    Provides additional mapping information when JSON is the record format on the
    streaming source.

    - **RecordRowPath** *(string) --*

      Path to the top-level parent that contains the records.
    """


_ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersTypeDef",
    {
        "JSONMappingParameters": ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef,
        "CSVMappingParameters": ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef,
    },
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersTypeDef
):
    """
    Type definition for `ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordFormat` `MappingParameters`

    When configuring application input at the time of creating or updating an
    application, provides additional mapping information specific to the record format
    (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming
    source.

    - **JSONMappingParameters** *(dict) --*

      Provides additional mapping information when JSON is the record format on the
      streaming source.

      - **RecordRowPath** *(string) --*

        Path to the top-level parent that contains the records.

    - **CSVMappingParameters** *(dict) --*

      Provides additional mapping information when the record format uses delimiters
      (for example, CSV).

      - **RecordRowDelimiter** *(string) --*

        Row delimiter. For example, in a CSV format, *'\\n'* is the typical row
        delimiter.

      - **RecordColumnDelimiter** *(string) --*

        Column delimiter. For example, in a CSV format, a comma (",") is the typical
        column delimiter.
    """


_ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordFormatTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordFormatTypeDef",
    {
        "RecordFormatType": str,
        "MappingParameters": ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersTypeDef,
    },
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordFormatTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordFormatTypeDef
):
    """
    Type definition for `ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchema` `RecordFormat`

    Specifies the format of the records on the streaming source.

    - **RecordFormatType** *(string) --*

      The type of record format.

    - **MappingParameters** *(dict) --*

      When configuring application input at the time of creating or updating an
      application, provides additional mapping information specific to the record format
      (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming
      source.

      - **JSONMappingParameters** *(dict) --*

        Provides additional mapping information when JSON is the record format on the
        streaming source.

        - **RecordRowPath** *(string) --*

          Path to the top-level parent that contains the records.

      - **CSVMappingParameters** *(dict) --*

        Provides additional mapping information when the record format uses delimiters
        (for example, CSV).

        - **RecordRowDelimiter** *(string) --*

          Row delimiter. For example, in a CSV format, *'\\n'* is the typical row
          delimiter.

        - **RecordColumnDelimiter** *(string) --*

          Column delimiter. For example, in a CSV format, a comma (",") is the typical
          column delimiter.
    """


_ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaTypeDef",
    {
        "RecordFormat": ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordFormatTypeDef,
        "RecordEncoding": str,
        "RecordColumns": List[
            ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordColumnsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaTypeDef
):
    """
    Type definition for `ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptions` `ReferenceSchema`

    Describes the format of the data in the streaming source, and how each data element
    maps to corresponding columns created in the in-application stream.

    - **RecordFormat** *(dict) --*

      Specifies the format of the records on the streaming source.

      - **RecordFormatType** *(string) --*

        The type of record format.

      - **MappingParameters** *(dict) --*

        When configuring application input at the time of creating or updating an
        application, provides additional mapping information specific to the record format
        (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming
        source.

        - **JSONMappingParameters** *(dict) --*

          Provides additional mapping information when JSON is the record format on the
          streaming source.

          - **RecordRowPath** *(string) --*

            Path to the top-level parent that contains the records.

        - **CSVMappingParameters** *(dict) --*

          Provides additional mapping information when the record format uses delimiters
          (for example, CSV).

          - **RecordRowDelimiter** *(string) --*

            Row delimiter. For example, in a CSV format, *'\\n'* is the typical row
            delimiter.

          - **RecordColumnDelimiter** *(string) --*

            Column delimiter. For example, in a CSV format, a comma (",") is the typical
            column delimiter.

    - **RecordEncoding** *(string) --*

      Specifies the encoding of the records in the streaming source. For example, UTF-8.

    - **RecordColumns** *(list) --*

      A list of ``RecordColumn`` objects.

      - *(dict) --*

        Describes the mapping of each data element in the streaming source to the
        corresponding column in the in-application stream.

        Also used to describe the format of the reference data source.

        - **Name** *(string) --*

          Name of the column created in the in-application input stream or reference table.

        - **Mapping** *(string) --*

          Reference to the data element in the streaming input or the reference data
          source. This element is required if the `RecordFormatType
          <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_RecordFormat.html#analytics-Type-RecordFormat-RecordFormatTypel>`__
          is ``JSON`` .

        - **SqlType** *(string) --*

          Type of column created in the in-application input stream or reference table.
    """


_ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsS3ReferenceDataSourceDescriptionTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsS3ReferenceDataSourceDescriptionTypeDef",
    {"BucketARN": str, "FileKey": str, "ReferenceRoleARN": str},
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsS3ReferenceDataSourceDescriptionTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsS3ReferenceDataSourceDescriptionTypeDef
):
    """
    Type definition for `ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptions` `S3ReferenceDataSourceDescription`

    Provides the S3 bucket name, the object key name that contains the reference data. It
    also provides the Amazon Resource Name (ARN) of the IAM role that Amazon Kinesis
    Analytics can assume to read the Amazon S3 object and populate the in-application
    reference table.

    - **BucketARN** *(string) --*

      Amazon Resource Name (ARN) of the S3 bucket.

    - **FileKey** *(string) --*

      Amazon S3 object key name.

    - **ReferenceRoleARN** *(string) --*

      ARN of the IAM role that Amazon Kinesis Analytics can assume to read the Amazon S3
      object on your behalf to populate the in-application reference table.
    """


_ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsTypeDef",
    {
        "ReferenceId": str,
        "TableName": str,
        "S3ReferenceDataSourceDescription": ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsS3ReferenceDataSourceDescriptionTypeDef,
        "ReferenceSchema": ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaTypeDef,
    },
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsTypeDef
):
    """
    Type definition for `ClientDescribeApplicationResponseApplicationDetail` `ReferenceDataSourceDescriptions`

    Describes the reference data source configured for an application.

    - **ReferenceId** *(string) --*

      ID of the reference data source. This is the ID that Amazon Kinesis Analytics assigns
      when you add the reference data source to your application using the
      `AddApplicationReferenceDataSource
      <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_AddApplicationReferenceDataSource.html>`__
      operation.

    - **TableName** *(string) --*

      The in-application table name created by the specific reference data source
      configuration.

    - **S3ReferenceDataSourceDescription** *(dict) --*

      Provides the S3 bucket name, the object key name that contains the reference data. It
      also provides the Amazon Resource Name (ARN) of the IAM role that Amazon Kinesis
      Analytics can assume to read the Amazon S3 object and populate the in-application
      reference table.

      - **BucketARN** *(string) --*

        Amazon Resource Name (ARN) of the S3 bucket.

      - **FileKey** *(string) --*

        Amazon S3 object key name.

      - **ReferenceRoleARN** *(string) --*

        ARN of the IAM role that Amazon Kinesis Analytics can assume to read the Amazon S3
        object on your behalf to populate the in-application reference table.

    - **ReferenceSchema** *(dict) --*

      Describes the format of the data in the streaming source, and how each data element
      maps to corresponding columns created in the in-application stream.

      - **RecordFormat** *(dict) --*

        Specifies the format of the records on the streaming source.

        - **RecordFormatType** *(string) --*

          The type of record format.

        - **MappingParameters** *(dict) --*

          When configuring application input at the time of creating or updating an
          application, provides additional mapping information specific to the record format
          (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming
          source.

          - **JSONMappingParameters** *(dict) --*

            Provides additional mapping information when JSON is the record format on the
            streaming source.

            - **RecordRowPath** *(string) --*

              Path to the top-level parent that contains the records.

          - **CSVMappingParameters** *(dict) --*

            Provides additional mapping information when the record format uses delimiters
            (for example, CSV).

            - **RecordRowDelimiter** *(string) --*

              Row delimiter. For example, in a CSV format, *'\\n'* is the typical row
              delimiter.

            - **RecordColumnDelimiter** *(string) --*

              Column delimiter. For example, in a CSV format, a comma (",") is the typical
              column delimiter.

      - **RecordEncoding** *(string) --*

        Specifies the encoding of the records in the streaming source. For example, UTF-8.

      - **RecordColumns** *(list) --*

        A list of ``RecordColumn`` objects.

        - *(dict) --*

          Describes the mapping of each data element in the streaming source to the
          corresponding column in the in-application stream.

          Also used to describe the format of the reference data source.

          - **Name** *(string) --*

            Name of the column created in the in-application input stream or reference table.

          - **Mapping** *(string) --*

            Reference to the data element in the streaming input or the reference data
            source. This element is required if the `RecordFormatType
            <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_RecordFormat.html#analytics-Type-RecordFormat-RecordFormatTypel>`__
            is ``JSON`` .

          - **SqlType** *(string) --*

            Type of column created in the in-application input stream or reference table.
    """


_ClientDescribeApplicationResponseApplicationDetailTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailTypeDef",
    {
        "ApplicationName": str,
        "ApplicationDescription": str,
        "ApplicationARN": str,
        "ApplicationStatus": str,
        "CreateTimestamp": datetime,
        "LastUpdateTimestamp": datetime,
        "InputDescriptions": List[
            ClientDescribeApplicationResponseApplicationDetailInputDescriptionsTypeDef
        ],
        "OutputDescriptions": List[
            ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsTypeDef
        ],
        "ReferenceDataSourceDescriptions": List[
            ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsTypeDef
        ],
        "CloudWatchLoggingOptionDescriptions": List[
            ClientDescribeApplicationResponseApplicationDetailCloudWatchLoggingOptionDescriptionsTypeDef
        ],
        "ApplicationCode": str,
        "ApplicationVersionId": int,
    },
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailTypeDef
):
    """
    Type definition for `ClientDescribeApplicationResponse` `ApplicationDetail`

    Provides a description of the application, such as the application Amazon Resource Name
    (ARN), status, latest version, and input and output configuration details.

    - **ApplicationName** *(string) --*

      Name of the application.

    - **ApplicationDescription** *(string) --*

      Description of the application.

    - **ApplicationARN** *(string) --*

      ARN of the application.

    - **ApplicationStatus** *(string) --*

      Status of the application.

    - **CreateTimestamp** *(datetime) --*

      Time stamp when the application version was created.

    - **LastUpdateTimestamp** *(datetime) --*

      Time stamp when the application was last updated.

    - **InputDescriptions** *(list) --*

      Describes the application input configuration. For more information, see `Configuring
      Application Input
      <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-input.html>`__ .

      - *(dict) --*

        Describes the application input configuration. For more information, see `Configuring
        Application Input
        <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-input.html>`__ .

        - **InputId** *(string) --*

          Input ID associated with the application input. This is the ID that Amazon Kinesis
          Analytics assigns to each input configuration you add to your application.

        - **NamePrefix** *(string) --*

          In-application name prefix.

        - **InAppStreamNames** *(list) --*

          Returns the in-application stream names that are mapped to the stream source.

          - *(string) --*

        - **InputProcessingConfigurationDescription** *(dict) --*

          The description of the preprocessor that executes on records in this input before the
          application's code is run.

          - **InputLambdaProcessorDescription** *(dict) --*

            Provides configuration information about the associated
            `InputLambdaProcessorDescription
            <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_InputLambdaProcessorDescription.html>`__
            .

            - **ResourceARN** *(string) --*

              The ARN of the `AWS Lambda <https://docs.aws.amazon.com/lambda/>`__ function that
              is used to preprocess the records in the stream.

            - **RoleARN** *(string) --*

              The ARN of the IAM role that is used to access the AWS Lambda function.

        - **KinesisStreamsInputDescription** *(dict) --*

          If an Amazon Kinesis stream is configured as streaming source, provides Amazon Kinesis
          stream's Amazon Resource Name (ARN) and an IAM role that enables Amazon Kinesis
          Analytics to access the stream on your behalf.

          - **ResourceARN** *(string) --*

            Amazon Resource Name (ARN) of the Amazon Kinesis stream.

          - **RoleARN** *(string) --*

            ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream.

        - **KinesisFirehoseInputDescription** *(dict) --*

          If an Amazon Kinesis Firehose delivery stream is configured as a streaming source,
          provides the delivery stream's ARN and an IAM role that enables Amazon Kinesis
          Analytics to access the stream on your behalf.

          - **ResourceARN** *(string) --*

            Amazon Resource Name (ARN) of the Amazon Kinesis Firehose delivery stream.

          - **RoleARN** *(string) --*

            ARN of the IAM role that Amazon Kinesis Analytics assumes to access the stream.

        - **InputSchema** *(dict) --*

          Describes the format of the data in the streaming source, and how each data element
          maps to corresponding columns in the in-application stream that is being created.

          - **RecordFormat** *(dict) --*

            Specifies the format of the records on the streaming source.

            - **RecordFormatType** *(string) --*

              The type of record format.

            - **MappingParameters** *(dict) --*

              When configuring application input at the time of creating or updating an
              application, provides additional mapping information specific to the record format
              (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming
              source.

              - **JSONMappingParameters** *(dict) --*

                Provides additional mapping information when JSON is the record format on the
                streaming source.

                - **RecordRowPath** *(string) --*

                  Path to the top-level parent that contains the records.

              - **CSVMappingParameters** *(dict) --*

                Provides additional mapping information when the record format uses delimiters
                (for example, CSV).

                - **RecordRowDelimiter** *(string) --*

                  Row delimiter. For example, in a CSV format, *'\\n'* is the typical row
                  delimiter.

                - **RecordColumnDelimiter** *(string) --*

                  Column delimiter. For example, in a CSV format, a comma (",") is the typical
                  column delimiter.

          - **RecordEncoding** *(string) --*

            Specifies the encoding of the records in the streaming source. For example, UTF-8.

          - **RecordColumns** *(list) --*

            A list of ``RecordColumn`` objects.

            - *(dict) --*

              Describes the mapping of each data element in the streaming source to the
              corresponding column in the in-application stream.

              Also used to describe the format of the reference data source.

              - **Name** *(string) --*

                Name of the column created in the in-application input stream or reference table.

              - **Mapping** *(string) --*

                Reference to the data element in the streaming input or the reference data
                source. This element is required if the `RecordFormatType
                <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_RecordFormat.html#analytics-Type-RecordFormat-RecordFormatTypel>`__
                is ``JSON`` .

              - **SqlType** *(string) --*

                Type of column created in the in-application input stream or reference table.

        - **InputParallelism** *(dict) --*

          Describes the configured parallelism (number of in-application streams mapped to the
          streaming source).

          - **Count** *(integer) --*

            Number of in-application streams to create. For more information, see `Limits
            <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/limits.html>`__ .

        - **InputStartingPositionConfiguration** *(dict) --*

          Point at which the application is configured to read from the input stream.

          - **InputStartingPosition** *(string) --*

            The starting position on the stream.

            * ``NOW`` - Start reading just after the most recent record in the stream, start at
            the request time stamp that the customer issued.

            * ``TRIM_HORIZON`` - Start reading at the last untrimmed record in the stream, which
            is the oldest record available in the stream. This option is not available for an
            Amazon Kinesis Firehose delivery stream.

            * ``LAST_STOPPED_POINT`` - Resume reading from where the application last stopped
            reading.

    - **OutputDescriptions** *(list) --*

      Describes the application output configuration. For more information, see `Configuring
      Application Output
      <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-output.html>`__ .

      - *(dict) --*

        Describes the application output configuration, which includes the in-application stream
        name and the destination where the stream data is written. The destination can be an
        Amazon Kinesis stream or an Amazon Kinesis Firehose delivery stream.

        - **OutputId** *(string) --*

          A unique identifier for the output configuration.

        - **Name** *(string) --*

          Name of the in-application stream configured as output.

        - **KinesisStreamsOutputDescription** *(dict) --*

          Describes Amazon Kinesis stream configured as the destination where output is written.

          - **ResourceARN** *(string) --*

            Amazon Resource Name (ARN) of the Amazon Kinesis stream.

          - **RoleARN** *(string) --*

            ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream.

        - **KinesisFirehoseOutputDescription** *(dict) --*

          Describes the Amazon Kinesis Firehose delivery stream configured as the destination
          where output is written.

          - **ResourceARN** *(string) --*

            Amazon Resource Name (ARN) of the Amazon Kinesis Firehose delivery stream.

          - **RoleARN** *(string) --*

            ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream.

        - **LambdaOutputDescription** *(dict) --*

          Describes the AWS Lambda function configured as the destination where output is written.

          - **ResourceARN** *(string) --*

            Amazon Resource Name (ARN) of the destination Lambda function.

          - **RoleARN** *(string) --*

            ARN of the IAM role that Amazon Kinesis Analytics can assume to write to the
            destination function.

        - **DestinationSchema** *(dict) --*

          Data format used for writing data to the destination.

          - **RecordFormatType** *(string) --*

            Specifies the format of the records on the output stream.

    - **ReferenceDataSourceDescriptions** *(list) --*

      Describes reference data sources configured for the application. For more information, see
      `Configuring Application Input
      <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-input.html>`__ .

      - *(dict) --*

        Describes the reference data source configured for an application.

        - **ReferenceId** *(string) --*

          ID of the reference data source. This is the ID that Amazon Kinesis Analytics assigns
          when you add the reference data source to your application using the
          `AddApplicationReferenceDataSource
          <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_AddApplicationReferenceDataSource.html>`__
          operation.

        - **TableName** *(string) --*

          The in-application table name created by the specific reference data source
          configuration.

        - **S3ReferenceDataSourceDescription** *(dict) --*

          Provides the S3 bucket name, the object key name that contains the reference data. It
          also provides the Amazon Resource Name (ARN) of the IAM role that Amazon Kinesis
          Analytics can assume to read the Amazon S3 object and populate the in-application
          reference table.

          - **BucketARN** *(string) --*

            Amazon Resource Name (ARN) of the S3 bucket.

          - **FileKey** *(string) --*

            Amazon S3 object key name.

          - **ReferenceRoleARN** *(string) --*

            ARN of the IAM role that Amazon Kinesis Analytics can assume to read the Amazon S3
            object on your behalf to populate the in-application reference table.

        - **ReferenceSchema** *(dict) --*

          Describes the format of the data in the streaming source, and how each data element
          maps to corresponding columns created in the in-application stream.

          - **RecordFormat** *(dict) --*

            Specifies the format of the records on the streaming source.

            - **RecordFormatType** *(string) --*

              The type of record format.

            - **MappingParameters** *(dict) --*

              When configuring application input at the time of creating or updating an
              application, provides additional mapping information specific to the record format
              (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming
              source.

              - **JSONMappingParameters** *(dict) --*

                Provides additional mapping information when JSON is the record format on the
                streaming source.

                - **RecordRowPath** *(string) --*

                  Path to the top-level parent that contains the records.

              - **CSVMappingParameters** *(dict) --*

                Provides additional mapping information when the record format uses delimiters
                (for example, CSV).

                - **RecordRowDelimiter** *(string) --*

                  Row delimiter. For example, in a CSV format, *'\\n'* is the typical row
                  delimiter.

                - **RecordColumnDelimiter** *(string) --*

                  Column delimiter. For example, in a CSV format, a comma (",") is the typical
                  column delimiter.

          - **RecordEncoding** *(string) --*

            Specifies the encoding of the records in the streaming source. For example, UTF-8.

          - **RecordColumns** *(list) --*

            A list of ``RecordColumn`` objects.

            - *(dict) --*

              Describes the mapping of each data element in the streaming source to the
              corresponding column in the in-application stream.

              Also used to describe the format of the reference data source.

              - **Name** *(string) --*

                Name of the column created in the in-application input stream or reference table.

              - **Mapping** *(string) --*

                Reference to the data element in the streaming input or the reference data
                source. This element is required if the `RecordFormatType
                <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_RecordFormat.html#analytics-Type-RecordFormat-RecordFormatTypel>`__
                is ``JSON`` .

              - **SqlType** *(string) --*

                Type of column created in the in-application input stream or reference table.

    - **CloudWatchLoggingOptionDescriptions** *(list) --*

      Describes the CloudWatch log streams that are configured to receive application messages.
      For more information about using CloudWatch log streams with Amazon Kinesis Analytics
      applications, see `Working with Amazon CloudWatch Logs
      <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/cloudwatch-logs.html>`__ .

      - *(dict) --*

        Description of the CloudWatch logging option.

        - **CloudWatchLoggingOptionId** *(string) --*

          ID of the CloudWatch logging option description.

        - **LogStreamARN** *(string) --*

          ARN of the CloudWatch log to receive application messages.

        - **RoleARN** *(string) --*

          IAM ARN of the role to use to send application messages. Note: To write application
          messages to CloudWatch, the IAM role used must have the ``PutLogEvents`` policy action
          enabled.

    - **ApplicationCode** *(string) --*

      Returns the application code that you provided to perform data analysis on any of the
      in-application streams in your application.

    - **ApplicationVersionId** *(integer) --*

      Provides the current application version.
    """


_ClientDescribeApplicationResponseTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseTypeDef",
    {"ApplicationDetail": ClientDescribeApplicationResponseApplicationDetailTypeDef},
    total=False,
)


class ClientDescribeApplicationResponseTypeDef(
    _ClientDescribeApplicationResponseTypeDef
):
    """
    Type definition for `ClientDescribeApplication` `Response`

    - **ApplicationDetail** *(dict) --*

      Provides a description of the application, such as the application Amazon Resource Name
      (ARN), status, latest version, and input and output configuration details.

      - **ApplicationName** *(string) --*

        Name of the application.

      - **ApplicationDescription** *(string) --*

        Description of the application.

      - **ApplicationARN** *(string) --*

        ARN of the application.

      - **ApplicationStatus** *(string) --*

        Status of the application.

      - **CreateTimestamp** *(datetime) --*

        Time stamp when the application version was created.

      - **LastUpdateTimestamp** *(datetime) --*

        Time stamp when the application was last updated.

      - **InputDescriptions** *(list) --*

        Describes the application input configuration. For more information, see `Configuring
        Application Input
        <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-input.html>`__ .

        - *(dict) --*

          Describes the application input configuration. For more information, see `Configuring
          Application Input
          <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-input.html>`__ .

          - **InputId** *(string) --*

            Input ID associated with the application input. This is the ID that Amazon Kinesis
            Analytics assigns to each input configuration you add to your application.

          - **NamePrefix** *(string) --*

            In-application name prefix.

          - **InAppStreamNames** *(list) --*

            Returns the in-application stream names that are mapped to the stream source.

            - *(string) --*

          - **InputProcessingConfigurationDescription** *(dict) --*

            The description of the preprocessor that executes on records in this input before the
            application's code is run.

            - **InputLambdaProcessorDescription** *(dict) --*

              Provides configuration information about the associated
              `InputLambdaProcessorDescription
              <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_InputLambdaProcessorDescription.html>`__
              .

              - **ResourceARN** *(string) --*

                The ARN of the `AWS Lambda <https://docs.aws.amazon.com/lambda/>`__ function that
                is used to preprocess the records in the stream.

              - **RoleARN** *(string) --*

                The ARN of the IAM role that is used to access the AWS Lambda function.

          - **KinesisStreamsInputDescription** *(dict) --*

            If an Amazon Kinesis stream is configured as streaming source, provides Amazon Kinesis
            stream's Amazon Resource Name (ARN) and an IAM role that enables Amazon Kinesis
            Analytics to access the stream on your behalf.

            - **ResourceARN** *(string) --*

              Amazon Resource Name (ARN) of the Amazon Kinesis stream.

            - **RoleARN** *(string) --*

              ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream.

          - **KinesisFirehoseInputDescription** *(dict) --*

            If an Amazon Kinesis Firehose delivery stream is configured as a streaming source,
            provides the delivery stream's ARN and an IAM role that enables Amazon Kinesis
            Analytics to access the stream on your behalf.

            - **ResourceARN** *(string) --*

              Amazon Resource Name (ARN) of the Amazon Kinesis Firehose delivery stream.

            - **RoleARN** *(string) --*

              ARN of the IAM role that Amazon Kinesis Analytics assumes to access the stream.

          - **InputSchema** *(dict) --*

            Describes the format of the data in the streaming source, and how each data element
            maps to corresponding columns in the in-application stream that is being created.

            - **RecordFormat** *(dict) --*

              Specifies the format of the records on the streaming source.

              - **RecordFormatType** *(string) --*

                The type of record format.

              - **MappingParameters** *(dict) --*

                When configuring application input at the time of creating or updating an
                application, provides additional mapping information specific to the record format
                (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming
                source.

                - **JSONMappingParameters** *(dict) --*

                  Provides additional mapping information when JSON is the record format on the
                  streaming source.

                  - **RecordRowPath** *(string) --*

                    Path to the top-level parent that contains the records.

                - **CSVMappingParameters** *(dict) --*

                  Provides additional mapping information when the record format uses delimiters
                  (for example, CSV).

                  - **RecordRowDelimiter** *(string) --*

                    Row delimiter. For example, in a CSV format, *'\\n'* is the typical row
                    delimiter.

                  - **RecordColumnDelimiter** *(string) --*

                    Column delimiter. For example, in a CSV format, a comma (",") is the typical
                    column delimiter.

            - **RecordEncoding** *(string) --*

              Specifies the encoding of the records in the streaming source. For example, UTF-8.

            - **RecordColumns** *(list) --*

              A list of ``RecordColumn`` objects.

              - *(dict) --*

                Describes the mapping of each data element in the streaming source to the
                corresponding column in the in-application stream.

                Also used to describe the format of the reference data source.

                - **Name** *(string) --*

                  Name of the column created in the in-application input stream or reference table.

                - **Mapping** *(string) --*

                  Reference to the data element in the streaming input or the reference data
                  source. This element is required if the `RecordFormatType
                  <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_RecordFormat.html#analytics-Type-RecordFormat-RecordFormatTypel>`__
                  is ``JSON`` .

                - **SqlType** *(string) --*

                  Type of column created in the in-application input stream or reference table.

          - **InputParallelism** *(dict) --*

            Describes the configured parallelism (number of in-application streams mapped to the
            streaming source).

            - **Count** *(integer) --*

              Number of in-application streams to create. For more information, see `Limits
              <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/limits.html>`__ .

          - **InputStartingPositionConfiguration** *(dict) --*

            Point at which the application is configured to read from the input stream.

            - **InputStartingPosition** *(string) --*

              The starting position on the stream.

              * ``NOW`` - Start reading just after the most recent record in the stream, start at
              the request time stamp that the customer issued.

              * ``TRIM_HORIZON`` - Start reading at the last untrimmed record in the stream, which
              is the oldest record available in the stream. This option is not available for an
              Amazon Kinesis Firehose delivery stream.

              * ``LAST_STOPPED_POINT`` - Resume reading from where the application last stopped
              reading.

      - **OutputDescriptions** *(list) --*

        Describes the application output configuration. For more information, see `Configuring
        Application Output
        <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-output.html>`__ .

        - *(dict) --*

          Describes the application output configuration, which includes the in-application stream
          name and the destination where the stream data is written. The destination can be an
          Amazon Kinesis stream or an Amazon Kinesis Firehose delivery stream.

          - **OutputId** *(string) --*

            A unique identifier for the output configuration.

          - **Name** *(string) --*

            Name of the in-application stream configured as output.

          - **KinesisStreamsOutputDescription** *(dict) --*

            Describes Amazon Kinesis stream configured as the destination where output is written.

            - **ResourceARN** *(string) --*

              Amazon Resource Name (ARN) of the Amazon Kinesis stream.

            - **RoleARN** *(string) --*

              ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream.

          - **KinesisFirehoseOutputDescription** *(dict) --*

            Describes the Amazon Kinesis Firehose delivery stream configured as the destination
            where output is written.

            - **ResourceARN** *(string) --*

              Amazon Resource Name (ARN) of the Amazon Kinesis Firehose delivery stream.

            - **RoleARN** *(string) --*

              ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream.

          - **LambdaOutputDescription** *(dict) --*

            Describes the AWS Lambda function configured as the destination where output is written.

            - **ResourceARN** *(string) --*

              Amazon Resource Name (ARN) of the destination Lambda function.

            - **RoleARN** *(string) --*

              ARN of the IAM role that Amazon Kinesis Analytics can assume to write to the
              destination function.

          - **DestinationSchema** *(dict) --*

            Data format used for writing data to the destination.

            - **RecordFormatType** *(string) --*

              Specifies the format of the records on the output stream.

      - **ReferenceDataSourceDescriptions** *(list) --*

        Describes reference data sources configured for the application. For more information, see
        `Configuring Application Input
        <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-input.html>`__ .

        - *(dict) --*

          Describes the reference data source configured for an application.

          - **ReferenceId** *(string) --*

            ID of the reference data source. This is the ID that Amazon Kinesis Analytics assigns
            when you add the reference data source to your application using the
            `AddApplicationReferenceDataSource
            <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_AddApplicationReferenceDataSource.html>`__
            operation.

          - **TableName** *(string) --*

            The in-application table name created by the specific reference data source
            configuration.

          - **S3ReferenceDataSourceDescription** *(dict) --*

            Provides the S3 bucket name, the object key name that contains the reference data. It
            also provides the Amazon Resource Name (ARN) of the IAM role that Amazon Kinesis
            Analytics can assume to read the Amazon S3 object and populate the in-application
            reference table.

            - **BucketARN** *(string) --*

              Amazon Resource Name (ARN) of the S3 bucket.

            - **FileKey** *(string) --*

              Amazon S3 object key name.

            - **ReferenceRoleARN** *(string) --*

              ARN of the IAM role that Amazon Kinesis Analytics can assume to read the Amazon S3
              object on your behalf to populate the in-application reference table.

          - **ReferenceSchema** *(dict) --*

            Describes the format of the data in the streaming source, and how each data element
            maps to corresponding columns created in the in-application stream.

            - **RecordFormat** *(dict) --*

              Specifies the format of the records on the streaming source.

              - **RecordFormatType** *(string) --*

                The type of record format.

              - **MappingParameters** *(dict) --*

                When configuring application input at the time of creating or updating an
                application, provides additional mapping information specific to the record format
                (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming
                source.

                - **JSONMappingParameters** *(dict) --*

                  Provides additional mapping information when JSON is the record format on the
                  streaming source.

                  - **RecordRowPath** *(string) --*

                    Path to the top-level parent that contains the records.

                - **CSVMappingParameters** *(dict) --*

                  Provides additional mapping information when the record format uses delimiters
                  (for example, CSV).

                  - **RecordRowDelimiter** *(string) --*

                    Row delimiter. For example, in a CSV format, *'\\n'* is the typical row
                    delimiter.

                  - **RecordColumnDelimiter** *(string) --*

                    Column delimiter. For example, in a CSV format, a comma (",") is the typical
                    column delimiter.

            - **RecordEncoding** *(string) --*

              Specifies the encoding of the records in the streaming source. For example, UTF-8.

            - **RecordColumns** *(list) --*

              A list of ``RecordColumn`` objects.

              - *(dict) --*

                Describes the mapping of each data element in the streaming source to the
                corresponding column in the in-application stream.

                Also used to describe the format of the reference data source.

                - **Name** *(string) --*

                  Name of the column created in the in-application input stream or reference table.

                - **Mapping** *(string) --*

                  Reference to the data element in the streaming input or the reference data
                  source. This element is required if the `RecordFormatType
                  <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_RecordFormat.html#analytics-Type-RecordFormat-RecordFormatTypel>`__
                  is ``JSON`` .

                - **SqlType** *(string) --*

                  Type of column created in the in-application input stream or reference table.

      - **CloudWatchLoggingOptionDescriptions** *(list) --*

        Describes the CloudWatch log streams that are configured to receive application messages.
        For more information about using CloudWatch log streams with Amazon Kinesis Analytics
        applications, see `Working with Amazon CloudWatch Logs
        <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/cloudwatch-logs.html>`__ .

        - *(dict) --*

          Description of the CloudWatch logging option.

          - **CloudWatchLoggingOptionId** *(string) --*

            ID of the CloudWatch logging option description.

          - **LogStreamARN** *(string) --*

            ARN of the CloudWatch log to receive application messages.

          - **RoleARN** *(string) --*

            IAM ARN of the role to use to send application messages. Note: To write application
            messages to CloudWatch, the IAM role used must have the ``PutLogEvents`` policy action
            enabled.

      - **ApplicationCode** *(string) --*

        Returns the application code that you provided to perform data analysis on any of the
        in-application streams in your application.

      - **ApplicationVersionId** *(integer) --*

        Provides the current application version.
    """


_ClientDiscoverInputSchemaInputProcessingConfigurationInputLambdaProcessorTypeDef = TypedDict(
    "_ClientDiscoverInputSchemaInputProcessingConfigurationInputLambdaProcessorTypeDef",
    {"ResourceARN": str, "RoleARN": str},
)


class ClientDiscoverInputSchemaInputProcessingConfigurationInputLambdaProcessorTypeDef(
    _ClientDiscoverInputSchemaInputProcessingConfigurationInputLambdaProcessorTypeDef
):
    """
    Type definition for `ClientDiscoverInputSchemaInputProcessingConfiguration` `InputLambdaProcessor`

    The `InputLambdaProcessor
    <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_InputLambdaProcessor.html>`__ that
    is used to preprocess the records in the stream before being processed by your application code.

    - **ResourceARN** *(string) --* **[REQUIRED]**

      The ARN of the `AWS Lambda <https://docs.aws.amazon.com/lambda/>`__ function that operates on
      records in the stream.

      .. note::

        To specify an earlier version of the Lambda function than the latest, include the Lambda
        function version in the Lambda function ARN. For more information about Lambda ARNs, see
        `Example ARNs\\: AWS Lambda
        </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__

    - **RoleARN** *(string) --* **[REQUIRED]**

      The ARN of the IAM role that is used to access the AWS Lambda function.
    """


_ClientDiscoverInputSchemaInputProcessingConfigurationTypeDef = TypedDict(
    "_ClientDiscoverInputSchemaInputProcessingConfigurationTypeDef",
    {
        "InputLambdaProcessor": ClientDiscoverInputSchemaInputProcessingConfigurationInputLambdaProcessorTypeDef
    },
)


class ClientDiscoverInputSchemaInputProcessingConfigurationTypeDef(
    _ClientDiscoverInputSchemaInputProcessingConfigurationTypeDef
):
    """
    Type definition for `ClientDiscoverInputSchema` `InputProcessingConfiguration`

    The `InputProcessingConfiguration
    <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_InputProcessingConfiguration.html>`__
    to use to preprocess the records before discovering the schema of the records.

    - **InputLambdaProcessor** *(dict) --* **[REQUIRED]**

      The `InputLambdaProcessor
      <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_InputLambdaProcessor.html>`__ that
      is used to preprocess the records in the stream before being processed by your application code.

      - **ResourceARN** *(string) --* **[REQUIRED]**

        The ARN of the `AWS Lambda <https://docs.aws.amazon.com/lambda/>`__ function that operates on
        records in the stream.

        .. note::

          To specify an earlier version of the Lambda function than the latest, include the Lambda
          function version in the Lambda function ARN. For more information about Lambda ARNs, see
          `Example ARNs\\: AWS Lambda
          </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__

      - **RoleARN** *(string) --* **[REQUIRED]**

        The ARN of the IAM role that is used to access the AWS Lambda function.
    """


_ClientDiscoverInputSchemaInputStartingPositionConfigurationTypeDef = TypedDict(
    "_ClientDiscoverInputSchemaInputStartingPositionConfigurationTypeDef",
    {"InputStartingPosition": str},
    total=False,
)


class ClientDiscoverInputSchemaInputStartingPositionConfigurationTypeDef(
    _ClientDiscoverInputSchemaInputStartingPositionConfigurationTypeDef
):
    """
    Type definition for `ClientDiscoverInputSchema` `InputStartingPositionConfiguration`

    Point at which you want Amazon Kinesis Analytics to start reading records from the specified
    streaming source discovery purposes.

    - **InputStartingPosition** *(string) --*

      The starting position on the stream.

      * ``NOW`` - Start reading just after the most recent record in the stream, start at the request
      time stamp that the customer issued.

      * ``TRIM_HORIZON`` - Start reading at the last untrimmed record in the stream, which is the
      oldest record available in the stream. This option is not available for an Amazon Kinesis
      Firehose delivery stream.

      * ``LAST_STOPPED_POINT`` - Resume reading from where the application last stopped reading.
    """


_ClientDiscoverInputSchemaResponseInputSchemaRecordColumnsTypeDef = TypedDict(
    "_ClientDiscoverInputSchemaResponseInputSchemaRecordColumnsTypeDef",
    {"Name": str, "Mapping": str, "SqlType": str},
    total=False,
)


class ClientDiscoverInputSchemaResponseInputSchemaRecordColumnsTypeDef(
    _ClientDiscoverInputSchemaResponseInputSchemaRecordColumnsTypeDef
):
    """
    Type definition for `ClientDiscoverInputSchemaResponseInputSchema` `RecordColumns`

    Describes the mapping of each data element in the streaming source to the corresponding
    column in the in-application stream.

    Also used to describe the format of the reference data source.

    - **Name** *(string) --*

      Name of the column created in the in-application input stream or reference table.

    - **Mapping** *(string) --*

      Reference to the data element in the streaming input or the reference data source. This
      element is required if the `RecordFormatType
      <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_RecordFormat.html#analytics-Type-RecordFormat-RecordFormatTypel>`__
      is ``JSON`` .

    - **SqlType** *(string) --*

      Type of column created in the in-application input stream or reference table.
    """


_ClientDiscoverInputSchemaResponseInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef = TypedDict(
    "_ClientDiscoverInputSchemaResponseInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef",
    {"RecordRowDelimiter": str, "RecordColumnDelimiter": str},
    total=False,
)


class ClientDiscoverInputSchemaResponseInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef(
    _ClientDiscoverInputSchemaResponseInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef
):
    """
    Type definition for `ClientDiscoverInputSchemaResponseInputSchemaRecordFormatMappingParameters` `CSVMappingParameters`

    Provides additional mapping information when the record format uses delimiters (for
    example, CSV).

    - **RecordRowDelimiter** *(string) --*

      Row delimiter. For example, in a CSV format, *'\\n'* is the typical row delimiter.

    - **RecordColumnDelimiter** *(string) --*

      Column delimiter. For example, in a CSV format, a comma (",") is the typical column
      delimiter.
    """


_ClientDiscoverInputSchemaResponseInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef = TypedDict(
    "_ClientDiscoverInputSchemaResponseInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef",
    {"RecordRowPath": str},
    total=False,
)


class ClientDiscoverInputSchemaResponseInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef(
    _ClientDiscoverInputSchemaResponseInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef
):
    """
    Type definition for `ClientDiscoverInputSchemaResponseInputSchemaRecordFormatMappingParameters` `JSONMappingParameters`

    Provides additional mapping information when JSON is the record format on the streaming
    source.

    - **RecordRowPath** *(string) --*

      Path to the top-level parent that contains the records.
    """


_ClientDiscoverInputSchemaResponseInputSchemaRecordFormatMappingParametersTypeDef = TypedDict(
    "_ClientDiscoverInputSchemaResponseInputSchemaRecordFormatMappingParametersTypeDef",
    {
        "JSONMappingParameters": ClientDiscoverInputSchemaResponseInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef,
        "CSVMappingParameters": ClientDiscoverInputSchemaResponseInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef,
    },
    total=False,
)


class ClientDiscoverInputSchemaResponseInputSchemaRecordFormatMappingParametersTypeDef(
    _ClientDiscoverInputSchemaResponseInputSchemaRecordFormatMappingParametersTypeDef
):
    """
    Type definition for `ClientDiscoverInputSchemaResponseInputSchemaRecordFormat` `MappingParameters`

    When configuring application input at the time of creating or updating an application,
    provides additional mapping information specific to the record format (such as JSON, CSV,
    or record fields delimited by some delimiter) on the streaming source.

    - **JSONMappingParameters** *(dict) --*

      Provides additional mapping information when JSON is the record format on the streaming
      source.

      - **RecordRowPath** *(string) --*

        Path to the top-level parent that contains the records.

    - **CSVMappingParameters** *(dict) --*

      Provides additional mapping information when the record format uses delimiters (for
      example, CSV).

      - **RecordRowDelimiter** *(string) --*

        Row delimiter. For example, in a CSV format, *'\\n'* is the typical row delimiter.

      - **RecordColumnDelimiter** *(string) --*

        Column delimiter. For example, in a CSV format, a comma (",") is the typical column
        delimiter.
    """


_ClientDiscoverInputSchemaResponseInputSchemaRecordFormatTypeDef = TypedDict(
    "_ClientDiscoverInputSchemaResponseInputSchemaRecordFormatTypeDef",
    {
        "RecordFormatType": str,
        "MappingParameters": ClientDiscoverInputSchemaResponseInputSchemaRecordFormatMappingParametersTypeDef,
    },
    total=False,
)


class ClientDiscoverInputSchemaResponseInputSchemaRecordFormatTypeDef(
    _ClientDiscoverInputSchemaResponseInputSchemaRecordFormatTypeDef
):
    """
    Type definition for `ClientDiscoverInputSchemaResponseInputSchema` `RecordFormat`

    Specifies the format of the records on the streaming source.

    - **RecordFormatType** *(string) --*

      The type of record format.

    - **MappingParameters** *(dict) --*

      When configuring application input at the time of creating or updating an application,
      provides additional mapping information specific to the record format (such as JSON, CSV,
      or record fields delimited by some delimiter) on the streaming source.

      - **JSONMappingParameters** *(dict) --*

        Provides additional mapping information when JSON is the record format on the streaming
        source.

        - **RecordRowPath** *(string) --*

          Path to the top-level parent that contains the records.

      - **CSVMappingParameters** *(dict) --*

        Provides additional mapping information when the record format uses delimiters (for
        example, CSV).

        - **RecordRowDelimiter** *(string) --*

          Row delimiter. For example, in a CSV format, *'\\n'* is the typical row delimiter.

        - **RecordColumnDelimiter** *(string) --*

          Column delimiter. For example, in a CSV format, a comma (",") is the typical column
          delimiter.
    """


_ClientDiscoverInputSchemaResponseInputSchemaTypeDef = TypedDict(
    "_ClientDiscoverInputSchemaResponseInputSchemaTypeDef",
    {
        "RecordFormat": ClientDiscoverInputSchemaResponseInputSchemaRecordFormatTypeDef,
        "RecordEncoding": str,
        "RecordColumns": List[
            ClientDiscoverInputSchemaResponseInputSchemaRecordColumnsTypeDef
        ],
    },
    total=False,
)


class ClientDiscoverInputSchemaResponseInputSchemaTypeDef(
    _ClientDiscoverInputSchemaResponseInputSchemaTypeDef
):
    """
    Type definition for `ClientDiscoverInputSchemaResponse` `InputSchema`

    Schema inferred from the streaming source. It identifies the format of the data in the
    streaming source and how each data element maps to corresponding columns in the
    in-application stream that you can create.

    - **RecordFormat** *(dict) --*

      Specifies the format of the records on the streaming source.

      - **RecordFormatType** *(string) --*

        The type of record format.

      - **MappingParameters** *(dict) --*

        When configuring application input at the time of creating or updating an application,
        provides additional mapping information specific to the record format (such as JSON, CSV,
        or record fields delimited by some delimiter) on the streaming source.

        - **JSONMappingParameters** *(dict) --*

          Provides additional mapping information when JSON is the record format on the streaming
          source.

          - **RecordRowPath** *(string) --*

            Path to the top-level parent that contains the records.

        - **CSVMappingParameters** *(dict) --*

          Provides additional mapping information when the record format uses delimiters (for
          example, CSV).

          - **RecordRowDelimiter** *(string) --*

            Row delimiter. For example, in a CSV format, *'\\n'* is the typical row delimiter.

          - **RecordColumnDelimiter** *(string) --*

            Column delimiter. For example, in a CSV format, a comma (",") is the typical column
            delimiter.

    - **RecordEncoding** *(string) --*

      Specifies the encoding of the records in the streaming source. For example, UTF-8.

    - **RecordColumns** *(list) --*

      A list of ``RecordColumn`` objects.

      - *(dict) --*

        Describes the mapping of each data element in the streaming source to the corresponding
        column in the in-application stream.

        Also used to describe the format of the reference data source.

        - **Name** *(string) --*

          Name of the column created in the in-application input stream or reference table.

        - **Mapping** *(string) --*

          Reference to the data element in the streaming input or the reference data source. This
          element is required if the `RecordFormatType
          <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_RecordFormat.html#analytics-Type-RecordFormat-RecordFormatTypel>`__
          is ``JSON`` .

        - **SqlType** *(string) --*

          Type of column created in the in-application input stream or reference table.
    """


_ClientDiscoverInputSchemaResponseTypeDef = TypedDict(
    "_ClientDiscoverInputSchemaResponseTypeDef",
    {
        "InputSchema": ClientDiscoverInputSchemaResponseInputSchemaTypeDef,
        "ParsedInputRecords": List[List[str]],
        "ProcessedInputRecords": List[str],
        "RawInputRecords": List[str],
    },
    total=False,
)


class ClientDiscoverInputSchemaResponseTypeDef(
    _ClientDiscoverInputSchemaResponseTypeDef
):
    """
    Type definition for `ClientDiscoverInputSchema` `Response`

    - **InputSchema** *(dict) --*

      Schema inferred from the streaming source. It identifies the format of the data in the
      streaming source and how each data element maps to corresponding columns in the
      in-application stream that you can create.

      - **RecordFormat** *(dict) --*

        Specifies the format of the records on the streaming source.

        - **RecordFormatType** *(string) --*

          The type of record format.

        - **MappingParameters** *(dict) --*

          When configuring application input at the time of creating or updating an application,
          provides additional mapping information specific to the record format (such as JSON, CSV,
          or record fields delimited by some delimiter) on the streaming source.

          - **JSONMappingParameters** *(dict) --*

            Provides additional mapping information when JSON is the record format on the streaming
            source.

            - **RecordRowPath** *(string) --*

              Path to the top-level parent that contains the records.

          - **CSVMappingParameters** *(dict) --*

            Provides additional mapping information when the record format uses delimiters (for
            example, CSV).

            - **RecordRowDelimiter** *(string) --*

              Row delimiter. For example, in a CSV format, *'\\n'* is the typical row delimiter.

            - **RecordColumnDelimiter** *(string) --*

              Column delimiter. For example, in a CSV format, a comma (",") is the typical column
              delimiter.

      - **RecordEncoding** *(string) --*

        Specifies the encoding of the records in the streaming source. For example, UTF-8.

      - **RecordColumns** *(list) --*

        A list of ``RecordColumn`` objects.

        - *(dict) --*

          Describes the mapping of each data element in the streaming source to the corresponding
          column in the in-application stream.

          Also used to describe the format of the reference data source.

          - **Name** *(string) --*

            Name of the column created in the in-application input stream or reference table.

          - **Mapping** *(string) --*

            Reference to the data element in the streaming input or the reference data source. This
            element is required if the `RecordFormatType
            <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_RecordFormat.html#analytics-Type-RecordFormat-RecordFormatTypel>`__
            is ``JSON`` .

          - **SqlType** *(string) --*

            Type of column created in the in-application input stream or reference table.

    - **ParsedInputRecords** *(list) --*

      An array of elements, where each element corresponds to a row in a stream record (a stream
      record can have more than one row).

      - *(list) --*

        - *(string) --*

    - **ProcessedInputRecords** *(list) --*

      Stream data that was modified by the processor specified in the
      ``InputProcessingConfiguration`` parameter.

      - *(string) --*

    - **RawInputRecords** *(list) --*

      Raw stream data that was sampled to infer the schema.

      - *(string) --*
    """


_ClientDiscoverInputSchemaS3ConfigurationTypeDef = TypedDict(
    "_ClientDiscoverInputSchemaS3ConfigurationTypeDef",
    {"RoleARN": str, "BucketARN": str, "FileKey": str},
)


class ClientDiscoverInputSchemaS3ConfigurationTypeDef(
    _ClientDiscoverInputSchemaS3ConfigurationTypeDef
):
    """
    Type definition for `ClientDiscoverInputSchema` `S3Configuration`

    Specify this parameter to discover a schema from data in an Amazon S3 object.

    - **RoleARN** *(string) --* **[REQUIRED]**

      IAM ARN of the role used to access the data.

    - **BucketARN** *(string) --* **[REQUIRED]**

      ARN of the S3 bucket that contains the data.

    - **FileKey** *(string) --* **[REQUIRED]**

      The name of the object that contains the data.
    """


_ClientListApplicationsResponseApplicationSummariesTypeDef = TypedDict(
    "_ClientListApplicationsResponseApplicationSummariesTypeDef",
    {"ApplicationName": str, "ApplicationARN": str, "ApplicationStatus": str},
    total=False,
)


class ClientListApplicationsResponseApplicationSummariesTypeDef(
    _ClientListApplicationsResponseApplicationSummariesTypeDef
):
    """
    Type definition for `ClientListApplicationsResponse` `ApplicationSummaries`

    .. note::

      This documentation is for version 1 of the Amazon Kinesis Data Analytics API, which only
      supports SQL applications. Version 2 of the API supports SQL and Java applications. For
      more information about version 2, see `Amazon Kinesis Data Analytics API V2 Documentation
      </kinesisanalytics/latest/apiv2/Welcome.html>`__ .

    Provides application summary information, including the application Amazon Resource Name
    (ARN), name, and status.

    - **ApplicationName** *(string) --*

      Name of the application.

    - **ApplicationARN** *(string) --*

      ARN of the application.

    - **ApplicationStatus** *(string) --*

      Status of the application.
    """


_ClientListApplicationsResponseTypeDef = TypedDict(
    "_ClientListApplicationsResponseTypeDef",
    {
        "ApplicationSummaries": List[
            ClientListApplicationsResponseApplicationSummariesTypeDef
        ],
        "HasMoreApplications": bool,
    },
    total=False,
)


class ClientListApplicationsResponseTypeDef(_ClientListApplicationsResponseTypeDef):
    """
    Type definition for `ClientListApplications` `Response`

    - **ApplicationSummaries** *(list) --*

      List of ``ApplicationSummary`` objects.

      - *(dict) --*

        .. note::

          This documentation is for version 1 of the Amazon Kinesis Data Analytics API, which only
          supports SQL applications. Version 2 of the API supports SQL and Java applications. For
          more information about version 2, see `Amazon Kinesis Data Analytics API V2 Documentation
          </kinesisanalytics/latest/apiv2/Welcome.html>`__ .

        Provides application summary information, including the application Amazon Resource Name
        (ARN), name, and status.

        - **ApplicationName** *(string) --*

          Name of the application.

        - **ApplicationARN** *(string) --*

          ARN of the application.

        - **ApplicationStatus** *(string) --*

          Status of the application.

    - **HasMoreApplications** *(boolean) --*

      Returns true if there are more applications to retrieve.
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

    A key-value pair (the value is optional) that you can define and assign to AWS resources.
    If you specify a tag that already exists, the tag value is replaced with the value that you
    specify in the request. Note that the maximum number of application tags includes system
    tags. The maximum number of user-defined application tags is 50. For more information, see
    `Using Tagging
    <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-tagging.html>`__ .

    - **Key** *(string) --*

      The key of the key-value tag.

    - **Value** *(string) --*

      The value of the key-value tag. The value is optional.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef",
    {"Tags": List[ClientListTagsForResourceResponseTagsTypeDef]},
    total=False,
)


class ClientListTagsForResourceResponseTypeDef(
    _ClientListTagsForResourceResponseTypeDef
):
    """
    Type definition for `ClientListTagsForResource` `Response`

    - **Tags** *(list) --*

      The key-value tags assigned to the application.

      - *(dict) --*

        A key-value pair (the value is optional) that you can define and assign to AWS resources.
        If you specify a tag that already exists, the tag value is replaced with the value that you
        specify in the request. Note that the maximum number of application tags includes system
        tags. The maximum number of user-defined application tags is 50. For more information, see
        `Using Tagging
        <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-tagging.html>`__ .

        - **Key** *(string) --*

          The key of the key-value tag.

        - **Value** *(string) --*

          The value of the key-value tag. The value is optional.
    """


_ClientStartApplicationInputConfigurationsInputStartingPositionConfigurationTypeDef = TypedDict(
    "_ClientStartApplicationInputConfigurationsInputStartingPositionConfigurationTypeDef",
    {"InputStartingPosition": str},
    total=False,
)


class ClientStartApplicationInputConfigurationsInputStartingPositionConfigurationTypeDef(
    _ClientStartApplicationInputConfigurationsInputStartingPositionConfigurationTypeDef
):
    """
    Type definition for `ClientStartApplicationInputConfigurations` `InputStartingPositionConfiguration`

    Point at which you want the application to start processing records from the streaming source.

    - **InputStartingPosition** *(string) --*

      The starting position on the stream.

      * ``NOW`` - Start reading just after the most recent record in the stream, start at the
      request time stamp that the customer issued.

      * ``TRIM_HORIZON`` - Start reading at the last untrimmed record in the stream, which is the
      oldest record available in the stream. This option is not available for an Amazon Kinesis
      Firehose delivery stream.

      * ``LAST_STOPPED_POINT`` - Resume reading from where the application last stopped reading.
    """


_ClientStartApplicationInputConfigurationsTypeDef = TypedDict(
    "_ClientStartApplicationInputConfigurationsTypeDef",
    {
        "Id": str,
        "InputStartingPositionConfiguration": ClientStartApplicationInputConfigurationsInputStartingPositionConfigurationTypeDef,
    },
)


class ClientStartApplicationInputConfigurationsTypeDef(
    _ClientStartApplicationInputConfigurationsTypeDef
):
    """
    Type definition for `ClientStartApplication` `InputConfigurations`

    When you start your application, you provide this configuration, which identifies the input
    source and the point in the input source at which you want the application to start processing
    records.

    - **Id** *(string) --* **[REQUIRED]**

      Input source ID. You can get this ID by calling the `DescribeApplication
      <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_DescribeApplication.html>`__
      operation.

    - **InputStartingPositionConfiguration** *(dict) --* **[REQUIRED]**

      Point at which you want the application to start processing records from the streaming source.

      - **InputStartingPosition** *(string) --*

        The starting position on the stream.

        * ``NOW`` - Start reading just after the most recent record in the stream, start at the
        request time stamp that the customer issued.

        * ``TRIM_HORIZON`` - Start reading at the last untrimmed record in the stream, which is the
        oldest record available in the stream. This option is not available for an Amazon Kinesis
        Firehose delivery stream.

        * ``LAST_STOPPED_POINT`` - Resume reading from where the application last stopped reading.
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

    A key-value pair (the value is optional) that you can define and assign to AWS resources. If
    you specify a tag that already exists, the tag value is replaced with the value that you
    specify in the request. Note that the maximum number of application tags includes system tags.
    The maximum number of user-defined application tags is 50. For more information, see `Using
    Tagging <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-tagging.html>`__ .

    - **Key** *(string) --* **[REQUIRED]**

      The key of the key-value tag.

    - **Value** *(string) --*

      The value of the key-value tag. The value is optional.
    """


_RequiredClientUpdateApplicationApplicationUpdateCloudWatchLoggingOptionUpdatesTypeDef = TypedDict(
    "_RequiredClientUpdateApplicationApplicationUpdateCloudWatchLoggingOptionUpdatesTypeDef",
    {"CloudWatchLoggingOptionId": str},
)
_OptionalClientUpdateApplicationApplicationUpdateCloudWatchLoggingOptionUpdatesTypeDef = TypedDict(
    "_OptionalClientUpdateApplicationApplicationUpdateCloudWatchLoggingOptionUpdatesTypeDef",
    {"LogStreamARNUpdate": str, "RoleARNUpdate": str},
    total=False,
)


class ClientUpdateApplicationApplicationUpdateCloudWatchLoggingOptionUpdatesTypeDef(
    _RequiredClientUpdateApplicationApplicationUpdateCloudWatchLoggingOptionUpdatesTypeDef,
    _OptionalClientUpdateApplicationApplicationUpdateCloudWatchLoggingOptionUpdatesTypeDef,
):
    """
    Type definition for `ClientUpdateApplicationApplicationUpdate` `CloudWatchLoggingOptionUpdates`

    Describes CloudWatch logging option updates.

    - **CloudWatchLoggingOptionId** *(string) --* **[REQUIRED]**

      ID of the CloudWatch logging option to update

    - **LogStreamARNUpdate** *(string) --*

      ARN of the CloudWatch log to receive application messages.

    - **RoleARNUpdate** *(string) --*

      IAM ARN of the role to use to send application messages. Note: To write application
      messages to CloudWatch, the IAM role used must have the ``PutLogEvents`` policy action
      enabled.
    """


_ClientUpdateApplicationApplicationUpdateInputUpdatesInputParallelismUpdateTypeDef = TypedDict(
    "_ClientUpdateApplicationApplicationUpdateInputUpdatesInputParallelismUpdateTypeDef",
    {"CountUpdate": int},
    total=False,
)


class ClientUpdateApplicationApplicationUpdateInputUpdatesInputParallelismUpdateTypeDef(
    _ClientUpdateApplicationApplicationUpdateInputUpdatesInputParallelismUpdateTypeDef
):
    """
    Type definition for `ClientUpdateApplicationApplicationUpdateInputUpdates` `InputParallelismUpdate`

    Describes the parallelism updates (the number in-application streams Amazon Kinesis
    Analytics creates for the specific streaming source).

    - **CountUpdate** *(integer) --*

      Number of in-application streams to create for the specified streaming source.
    """


_ClientUpdateApplicationApplicationUpdateInputUpdatesInputProcessingConfigurationUpdateInputLambdaProcessorUpdateTypeDef = TypedDict(
    "_ClientUpdateApplicationApplicationUpdateInputUpdatesInputProcessingConfigurationUpdateInputLambdaProcessorUpdateTypeDef",
    {"ResourceARNUpdate": str, "RoleARNUpdate": str},
    total=False,
)


class ClientUpdateApplicationApplicationUpdateInputUpdatesInputProcessingConfigurationUpdateInputLambdaProcessorUpdateTypeDef(
    _ClientUpdateApplicationApplicationUpdateInputUpdatesInputProcessingConfigurationUpdateInputLambdaProcessorUpdateTypeDef
):
    """
    Type definition for `ClientUpdateApplicationApplicationUpdateInputUpdatesInputProcessingConfigurationUpdate` `InputLambdaProcessorUpdate`

    Provides update information for an `InputLambdaProcessor
    <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_InputLambdaProcessor.html>`__
    .

    - **ResourceARNUpdate** *(string) --*

      The Amazon Resource Name (ARN) of the new `AWS Lambda
      <https://docs.aws.amazon.com/lambda/>`__ function that is used to preprocess the
      records in the stream.

      .. note::

        To specify an earlier version of the Lambda function than the latest, include the
        Lambda function version in the Lambda function ARN. For more information about Lambda
        ARNs, see `Example ARNs\\: AWS Lambda
        </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__

    - **RoleARNUpdate** *(string) --*

      The ARN of the new IAM role that is used to access the AWS Lambda function.
    """


_ClientUpdateApplicationApplicationUpdateInputUpdatesInputProcessingConfigurationUpdateTypeDef = TypedDict(
    "_ClientUpdateApplicationApplicationUpdateInputUpdatesInputProcessingConfigurationUpdateTypeDef",
    {
        "InputLambdaProcessorUpdate": ClientUpdateApplicationApplicationUpdateInputUpdatesInputProcessingConfigurationUpdateInputLambdaProcessorUpdateTypeDef
    },
)


class ClientUpdateApplicationApplicationUpdateInputUpdatesInputProcessingConfigurationUpdateTypeDef(
    _ClientUpdateApplicationApplicationUpdateInputUpdatesInputProcessingConfigurationUpdateTypeDef
):
    """
    Type definition for `ClientUpdateApplicationApplicationUpdateInputUpdates` `InputProcessingConfigurationUpdate`

    Describes updates for an input processing configuration.

    - **InputLambdaProcessorUpdate** *(dict) --* **[REQUIRED]**

      Provides update information for an `InputLambdaProcessor
      <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_InputLambdaProcessor.html>`__
      .

      - **ResourceARNUpdate** *(string) --*

        The Amazon Resource Name (ARN) of the new `AWS Lambda
        <https://docs.aws.amazon.com/lambda/>`__ function that is used to preprocess the
        records in the stream.

        .. note::

          To specify an earlier version of the Lambda function than the latest, include the
          Lambda function version in the Lambda function ARN. For more information about Lambda
          ARNs, see `Example ARNs\\: AWS Lambda
          </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__

      - **RoleARNUpdate** *(string) --*

        The ARN of the new IAM role that is used to access the AWS Lambda function.
    """


_RequiredClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordColumnUpdatesTypeDef = TypedDict(
    "_RequiredClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordColumnUpdatesTypeDef",
    {"Name": str, "SqlType": str},
)
_OptionalClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordColumnUpdatesTypeDef = TypedDict(
    "_OptionalClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordColumnUpdatesTypeDef",
    {"Mapping": str},
    total=False,
)


class ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordColumnUpdatesTypeDef(
    _RequiredClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordColumnUpdatesTypeDef,
    _OptionalClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordColumnUpdatesTypeDef,
):
    """
    Type definition for `ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdate` `RecordColumnUpdates`

    Describes the mapping of each data element in the streaming source to the corresponding
    column in the in-application stream.

    Also used to describe the format of the reference data source.

    - **Name** *(string) --* **[REQUIRED]**

      Name of the column created in the in-application input stream or reference table.

    - **Mapping** *(string) --*

      Reference to the data element in the streaming input or the reference data source.
      This element is required if the `RecordFormatType
      <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_RecordFormat.html#analytics-Type-RecordFormat-RecordFormatTypel>`__
      is ``JSON`` .

    - **SqlType** *(string) --* **[REQUIRED]**

      Type of column created in the in-application input stream or reference table.
    """


_ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateMappingParametersCSVMappingParametersTypeDef = TypedDict(
    "_ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateMappingParametersCSVMappingParametersTypeDef",
    {"RecordRowDelimiter": str, "RecordColumnDelimiter": str},
)


class ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateMappingParametersCSVMappingParametersTypeDef(
    _ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateMappingParametersCSVMappingParametersTypeDef
):
    """
    Type definition for `ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateMappingParameters` `CSVMappingParameters`

    Provides additional mapping information when the record format uses delimiters (for
    example, CSV).

    - **RecordRowDelimiter** *(string) --* **[REQUIRED]**

      Row delimiter. For example, in a CSV format, *'\\n'* is the typical row delimiter.

    - **RecordColumnDelimiter** *(string) --* **[REQUIRED]**

      Column delimiter. For example, in a CSV format, a comma (",") is the typical column
      delimiter.
    """


_ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateMappingParametersJSONMappingParametersTypeDef = TypedDict(
    "_ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateMappingParametersJSONMappingParametersTypeDef",
    {"RecordRowPath": str},
)


class ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateMappingParametersJSONMappingParametersTypeDef(
    _ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateMappingParametersJSONMappingParametersTypeDef
):
    """
    Type definition for `ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateMappingParameters` `JSONMappingParameters`

    Provides additional mapping information when JSON is the record format on the
    streaming source.

    - **RecordRowPath** *(string) --* **[REQUIRED]**

      Path to the top-level parent that contains the records.
    """


_ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateMappingParametersTypeDef = TypedDict(
    "_ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateMappingParametersTypeDef",
    {
        "JSONMappingParameters": ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateMappingParametersJSONMappingParametersTypeDef,
        "CSVMappingParameters": ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateMappingParametersCSVMappingParametersTypeDef,
    },
    total=False,
)


class ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateMappingParametersTypeDef(
    _ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateMappingParametersTypeDef
):
    """
    Type definition for `ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdate` `MappingParameters`

    When configuring application input at the time of creating or updating an application,
    provides additional mapping information specific to the record format (such as JSON,
    CSV, or record fields delimited by some delimiter) on the streaming source.

    - **JSONMappingParameters** *(dict) --*

      Provides additional mapping information when JSON is the record format on the
      streaming source.

      - **RecordRowPath** *(string) --* **[REQUIRED]**

        Path to the top-level parent that contains the records.

    - **CSVMappingParameters** *(dict) --*

      Provides additional mapping information when the record format uses delimiters (for
      example, CSV).

      - **RecordRowDelimiter** *(string) --* **[REQUIRED]**

        Row delimiter. For example, in a CSV format, *'\\n'* is the typical row delimiter.

      - **RecordColumnDelimiter** *(string) --* **[REQUIRED]**

        Column delimiter. For example, in a CSV format, a comma (",") is the typical column
        delimiter.
    """


_RequiredClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateTypeDef = TypedDict(
    "_RequiredClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateTypeDef",
    {"RecordFormatType": str},
)
_OptionalClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateTypeDef = TypedDict(
    "_OptionalClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateTypeDef",
    {
        "MappingParameters": ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateMappingParametersTypeDef
    },
    total=False,
)


class ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateTypeDef(
    _RequiredClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateTypeDef,
    _OptionalClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateTypeDef,
):
    """
    Type definition for `ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdate` `RecordFormatUpdate`

    Specifies the format of the records on the streaming source.

    - **RecordFormatType** *(string) --* **[REQUIRED]**

      The type of record format.

    - **MappingParameters** *(dict) --*

      When configuring application input at the time of creating or updating an application,
      provides additional mapping information specific to the record format (such as JSON,
      CSV, or record fields delimited by some delimiter) on the streaming source.

      - **JSONMappingParameters** *(dict) --*

        Provides additional mapping information when JSON is the record format on the
        streaming source.

        - **RecordRowPath** *(string) --* **[REQUIRED]**

          Path to the top-level parent that contains the records.

      - **CSVMappingParameters** *(dict) --*

        Provides additional mapping information when the record format uses delimiters (for
        example, CSV).

        - **RecordRowDelimiter** *(string) --* **[REQUIRED]**

          Row delimiter. For example, in a CSV format, *'\\n'* is the typical row delimiter.

        - **RecordColumnDelimiter** *(string) --* **[REQUIRED]**

          Column delimiter. For example, in a CSV format, a comma (",") is the typical column
          delimiter.
    """


_ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateTypeDef = TypedDict(
    "_ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateTypeDef",
    {
        "RecordFormatUpdate": ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateTypeDef,
        "RecordEncodingUpdate": str,
        "RecordColumnUpdates": List[
            ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordColumnUpdatesTypeDef
        ],
    },
    total=False,
)


class ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateTypeDef(
    _ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateTypeDef
):
    """
    Type definition for `ClientUpdateApplicationApplicationUpdateInputUpdates` `InputSchemaUpdate`

    Describes the data format on the streaming source, and how record elements on the streaming
    source map to columns of the in-application stream that is created.

    - **RecordFormatUpdate** *(dict) --*

      Specifies the format of the records on the streaming source.

      - **RecordFormatType** *(string) --* **[REQUIRED]**

        The type of record format.

      - **MappingParameters** *(dict) --*

        When configuring application input at the time of creating or updating an application,
        provides additional mapping information specific to the record format (such as JSON,
        CSV, or record fields delimited by some delimiter) on the streaming source.

        - **JSONMappingParameters** *(dict) --*

          Provides additional mapping information when JSON is the record format on the
          streaming source.

          - **RecordRowPath** *(string) --* **[REQUIRED]**

            Path to the top-level parent that contains the records.

        - **CSVMappingParameters** *(dict) --*

          Provides additional mapping information when the record format uses delimiters (for
          example, CSV).

          - **RecordRowDelimiter** *(string) --* **[REQUIRED]**

            Row delimiter. For example, in a CSV format, *'\\n'* is the typical row delimiter.

          - **RecordColumnDelimiter** *(string) --* **[REQUIRED]**

            Column delimiter. For example, in a CSV format, a comma (",") is the typical column
            delimiter.

    - **RecordEncodingUpdate** *(string) --*

      Specifies the encoding of the records in the streaming source. For example, UTF-8.

    - **RecordColumnUpdates** *(list) --*

      A list of ``RecordColumn`` objects. Each object describes the mapping of the streaming
      source element to the corresponding column in the in-application stream.

      - *(dict) --*

        Describes the mapping of each data element in the streaming source to the corresponding
        column in the in-application stream.

        Also used to describe the format of the reference data source.

        - **Name** *(string) --* **[REQUIRED]**

          Name of the column created in the in-application input stream or reference table.

        - **Mapping** *(string) --*

          Reference to the data element in the streaming input or the reference data source.
          This element is required if the `RecordFormatType
          <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_RecordFormat.html#analytics-Type-RecordFormat-RecordFormatTypel>`__
          is ``JSON`` .

        - **SqlType** *(string) --* **[REQUIRED]**

          Type of column created in the in-application input stream or reference table.
    """


_ClientUpdateApplicationApplicationUpdateInputUpdatesKinesisFirehoseInputUpdateTypeDef = TypedDict(
    "_ClientUpdateApplicationApplicationUpdateInputUpdatesKinesisFirehoseInputUpdateTypeDef",
    {"ResourceARNUpdate": str, "RoleARNUpdate": str},
    total=False,
)


class ClientUpdateApplicationApplicationUpdateInputUpdatesKinesisFirehoseInputUpdateTypeDef(
    _ClientUpdateApplicationApplicationUpdateInputUpdatesKinesisFirehoseInputUpdateTypeDef
):
    """
    Type definition for `ClientUpdateApplicationApplicationUpdateInputUpdates` `KinesisFirehoseInputUpdate`

    If an Amazon Kinesis Firehose delivery stream is the streaming source to be updated,
    provides an updated stream ARN and IAM role ARN.

    - **ResourceARNUpdate** *(string) --*

      Amazon Resource Name (ARN) of the input Amazon Kinesis Firehose delivery stream to read.

    - **RoleARNUpdate** *(string) --*

      ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream on your
      behalf. You need to grant the necessary permissions to this role.
    """


_ClientUpdateApplicationApplicationUpdateInputUpdatesKinesisStreamsInputUpdateTypeDef = TypedDict(
    "_ClientUpdateApplicationApplicationUpdateInputUpdatesKinesisStreamsInputUpdateTypeDef",
    {"ResourceARNUpdate": str, "RoleARNUpdate": str},
    total=False,
)


class ClientUpdateApplicationApplicationUpdateInputUpdatesKinesisStreamsInputUpdateTypeDef(
    _ClientUpdateApplicationApplicationUpdateInputUpdatesKinesisStreamsInputUpdateTypeDef
):
    """
    Type definition for `ClientUpdateApplicationApplicationUpdateInputUpdates` `KinesisStreamsInputUpdate`

    If an Amazon Kinesis stream is the streaming source to be updated, provides an updated
    stream Amazon Resource Name (ARN) and IAM role ARN.

    - **ResourceARNUpdate** *(string) --*

      Amazon Resource Name (ARN) of the input Amazon Kinesis stream to read.

    - **RoleARNUpdate** *(string) --*

      ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream on your
      behalf. You need to grant the necessary permissions to this role.
    """


_RequiredClientUpdateApplicationApplicationUpdateInputUpdatesTypeDef = TypedDict(
    "_RequiredClientUpdateApplicationApplicationUpdateInputUpdatesTypeDef",
    {"InputId": str},
)
_OptionalClientUpdateApplicationApplicationUpdateInputUpdatesTypeDef = TypedDict(
    "_OptionalClientUpdateApplicationApplicationUpdateInputUpdatesTypeDef",
    {
        "NamePrefixUpdate": str,
        "InputProcessingConfigurationUpdate": ClientUpdateApplicationApplicationUpdateInputUpdatesInputProcessingConfigurationUpdateTypeDef,
        "KinesisStreamsInputUpdate": ClientUpdateApplicationApplicationUpdateInputUpdatesKinesisStreamsInputUpdateTypeDef,
        "KinesisFirehoseInputUpdate": ClientUpdateApplicationApplicationUpdateInputUpdatesKinesisFirehoseInputUpdateTypeDef,
        "InputSchemaUpdate": ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateTypeDef,
        "InputParallelismUpdate": ClientUpdateApplicationApplicationUpdateInputUpdatesInputParallelismUpdateTypeDef,
    },
    total=False,
)


class ClientUpdateApplicationApplicationUpdateInputUpdatesTypeDef(
    _RequiredClientUpdateApplicationApplicationUpdateInputUpdatesTypeDef,
    _OptionalClientUpdateApplicationApplicationUpdateInputUpdatesTypeDef,
):
    """
    Type definition for `ClientUpdateApplicationApplicationUpdate` `InputUpdates`

    Describes updates to a specific input configuration (identified by the ``InputId`` of an
    application).

    - **InputId** *(string) --* **[REQUIRED]**

      Input ID of the application input to be updated.

    - **NamePrefixUpdate** *(string) --*

      Name prefix for in-application streams that Amazon Kinesis Analytics creates for the
      specific streaming source.

    - **InputProcessingConfigurationUpdate** *(dict) --*

      Describes updates for an input processing configuration.

      - **InputLambdaProcessorUpdate** *(dict) --* **[REQUIRED]**

        Provides update information for an `InputLambdaProcessor
        <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_InputLambdaProcessor.html>`__
        .

        - **ResourceARNUpdate** *(string) --*

          The Amazon Resource Name (ARN) of the new `AWS Lambda
          <https://docs.aws.amazon.com/lambda/>`__ function that is used to preprocess the
          records in the stream.

          .. note::

            To specify an earlier version of the Lambda function than the latest, include the
            Lambda function version in the Lambda function ARN. For more information about Lambda
            ARNs, see `Example ARNs\\: AWS Lambda
            </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__

        - **RoleARNUpdate** *(string) --*

          The ARN of the new IAM role that is used to access the AWS Lambda function.

    - **KinesisStreamsInputUpdate** *(dict) --*

      If an Amazon Kinesis stream is the streaming source to be updated, provides an updated
      stream Amazon Resource Name (ARN) and IAM role ARN.

      - **ResourceARNUpdate** *(string) --*

        Amazon Resource Name (ARN) of the input Amazon Kinesis stream to read.

      - **RoleARNUpdate** *(string) --*

        ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream on your
        behalf. You need to grant the necessary permissions to this role.

    - **KinesisFirehoseInputUpdate** *(dict) --*

      If an Amazon Kinesis Firehose delivery stream is the streaming source to be updated,
      provides an updated stream ARN and IAM role ARN.

      - **ResourceARNUpdate** *(string) --*

        Amazon Resource Name (ARN) of the input Amazon Kinesis Firehose delivery stream to read.

      - **RoleARNUpdate** *(string) --*

        ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream on your
        behalf. You need to grant the necessary permissions to this role.

    - **InputSchemaUpdate** *(dict) --*

      Describes the data format on the streaming source, and how record elements on the streaming
      source map to columns of the in-application stream that is created.

      - **RecordFormatUpdate** *(dict) --*

        Specifies the format of the records on the streaming source.

        - **RecordFormatType** *(string) --* **[REQUIRED]**

          The type of record format.

        - **MappingParameters** *(dict) --*

          When configuring application input at the time of creating or updating an application,
          provides additional mapping information specific to the record format (such as JSON,
          CSV, or record fields delimited by some delimiter) on the streaming source.

          - **JSONMappingParameters** *(dict) --*

            Provides additional mapping information when JSON is the record format on the
            streaming source.

            - **RecordRowPath** *(string) --* **[REQUIRED]**

              Path to the top-level parent that contains the records.

          - **CSVMappingParameters** *(dict) --*

            Provides additional mapping information when the record format uses delimiters (for
            example, CSV).

            - **RecordRowDelimiter** *(string) --* **[REQUIRED]**

              Row delimiter. For example, in a CSV format, *'\\n'* is the typical row delimiter.

            - **RecordColumnDelimiter** *(string) --* **[REQUIRED]**

              Column delimiter. For example, in a CSV format, a comma (",") is the typical column
              delimiter.

      - **RecordEncodingUpdate** *(string) --*

        Specifies the encoding of the records in the streaming source. For example, UTF-8.

      - **RecordColumnUpdates** *(list) --*

        A list of ``RecordColumn`` objects. Each object describes the mapping of the streaming
        source element to the corresponding column in the in-application stream.

        - *(dict) --*

          Describes the mapping of each data element in the streaming source to the corresponding
          column in the in-application stream.

          Also used to describe the format of the reference data source.

          - **Name** *(string) --* **[REQUIRED]**

            Name of the column created in the in-application input stream or reference table.

          - **Mapping** *(string) --*

            Reference to the data element in the streaming input or the reference data source.
            This element is required if the `RecordFormatType
            <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_RecordFormat.html#analytics-Type-RecordFormat-RecordFormatTypel>`__
            is ``JSON`` .

          - **SqlType** *(string) --* **[REQUIRED]**

            Type of column created in the in-application input stream or reference table.

    - **InputParallelismUpdate** *(dict) --*

      Describes the parallelism updates (the number in-application streams Amazon Kinesis
      Analytics creates for the specific streaming source).

      - **CountUpdate** *(integer) --*

        Number of in-application streams to create for the specified streaming source.
    """


_ClientUpdateApplicationApplicationUpdateOutputUpdatesDestinationSchemaUpdateTypeDef = TypedDict(
    "_ClientUpdateApplicationApplicationUpdateOutputUpdatesDestinationSchemaUpdateTypeDef",
    {"RecordFormatType": str},
)


class ClientUpdateApplicationApplicationUpdateOutputUpdatesDestinationSchemaUpdateTypeDef(
    _ClientUpdateApplicationApplicationUpdateOutputUpdatesDestinationSchemaUpdateTypeDef
):
    """
    Type definition for `ClientUpdateApplicationApplicationUpdateOutputUpdates` `DestinationSchemaUpdate`

    Describes the data format when records are written to the destination. For more
    information, see `Configuring Application Output
    <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-output.html>`__ .

    - **RecordFormatType** *(string) --* **[REQUIRED]**

      Specifies the format of the records on the output stream.
    """


_ClientUpdateApplicationApplicationUpdateOutputUpdatesKinesisFirehoseOutputUpdateTypeDef = TypedDict(
    "_ClientUpdateApplicationApplicationUpdateOutputUpdatesKinesisFirehoseOutputUpdateTypeDef",
    {"ResourceARNUpdate": str, "RoleARNUpdate": str},
    total=False,
)


class ClientUpdateApplicationApplicationUpdateOutputUpdatesKinesisFirehoseOutputUpdateTypeDef(
    _ClientUpdateApplicationApplicationUpdateOutputUpdatesKinesisFirehoseOutputUpdateTypeDef
):
    """
    Type definition for `ClientUpdateApplicationApplicationUpdateOutputUpdates` `KinesisFirehoseOutputUpdate`

    Describes an Amazon Kinesis Firehose delivery stream as the destination for the output.

    - **ResourceARNUpdate** *(string) --*

      Amazon Resource Name (ARN) of the Amazon Kinesis Firehose delivery stream to write to.

    - **RoleARNUpdate** *(string) --*

      ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream on your
      behalf. You need to grant the necessary permissions to this role.
    """


_ClientUpdateApplicationApplicationUpdateOutputUpdatesKinesisStreamsOutputUpdateTypeDef = TypedDict(
    "_ClientUpdateApplicationApplicationUpdateOutputUpdatesKinesisStreamsOutputUpdateTypeDef",
    {"ResourceARNUpdate": str, "RoleARNUpdate": str},
    total=False,
)


class ClientUpdateApplicationApplicationUpdateOutputUpdatesKinesisStreamsOutputUpdateTypeDef(
    _ClientUpdateApplicationApplicationUpdateOutputUpdatesKinesisStreamsOutputUpdateTypeDef
):
    """
    Type definition for `ClientUpdateApplicationApplicationUpdateOutputUpdates` `KinesisStreamsOutputUpdate`

    Describes an Amazon Kinesis stream as the destination for the output.

    - **ResourceARNUpdate** *(string) --*

      Amazon Resource Name (ARN) of the Amazon Kinesis stream where you want to write the
      output.

    - **RoleARNUpdate** *(string) --*

      ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream on your
      behalf. You need to grant the necessary permissions to this role.
    """


_ClientUpdateApplicationApplicationUpdateOutputUpdatesLambdaOutputUpdateTypeDef = TypedDict(
    "_ClientUpdateApplicationApplicationUpdateOutputUpdatesLambdaOutputUpdateTypeDef",
    {"ResourceARNUpdate": str, "RoleARNUpdate": str},
    total=False,
)


class ClientUpdateApplicationApplicationUpdateOutputUpdatesLambdaOutputUpdateTypeDef(
    _ClientUpdateApplicationApplicationUpdateOutputUpdatesLambdaOutputUpdateTypeDef
):
    """
    Type definition for `ClientUpdateApplicationApplicationUpdateOutputUpdates` `LambdaOutputUpdate`

    Describes an AWS Lambda function as the destination for the output.

    - **ResourceARNUpdate** *(string) --*

      Amazon Resource Name (ARN) of the destination Lambda function.

      .. note::

        To specify an earlier version of the Lambda function than the latest, include the
        Lambda function version in the Lambda function ARN. For more information about Lambda
        ARNs, see `Example ARNs\\: AWS Lambda
        </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__

    - **RoleARNUpdate** *(string) --*

      ARN of the IAM role that Amazon Kinesis Analytics can assume to write to the destination
      function on your behalf. You need to grant the necessary permissions to this role.
    """


_RequiredClientUpdateApplicationApplicationUpdateOutputUpdatesTypeDef = TypedDict(
    "_RequiredClientUpdateApplicationApplicationUpdateOutputUpdatesTypeDef",
    {"OutputId": str},
)
_OptionalClientUpdateApplicationApplicationUpdateOutputUpdatesTypeDef = TypedDict(
    "_OptionalClientUpdateApplicationApplicationUpdateOutputUpdatesTypeDef",
    {
        "NameUpdate": str,
        "KinesisStreamsOutputUpdate": ClientUpdateApplicationApplicationUpdateOutputUpdatesKinesisStreamsOutputUpdateTypeDef,
        "KinesisFirehoseOutputUpdate": ClientUpdateApplicationApplicationUpdateOutputUpdatesKinesisFirehoseOutputUpdateTypeDef,
        "LambdaOutputUpdate": ClientUpdateApplicationApplicationUpdateOutputUpdatesLambdaOutputUpdateTypeDef,
        "DestinationSchemaUpdate": ClientUpdateApplicationApplicationUpdateOutputUpdatesDestinationSchemaUpdateTypeDef,
    },
    total=False,
)


class ClientUpdateApplicationApplicationUpdateOutputUpdatesTypeDef(
    _RequiredClientUpdateApplicationApplicationUpdateOutputUpdatesTypeDef,
    _OptionalClientUpdateApplicationApplicationUpdateOutputUpdatesTypeDef,
):
    """
    Type definition for `ClientUpdateApplicationApplicationUpdate` `OutputUpdates`

    Describes updates to the output configuration identified by the ``OutputId`` .

    - **OutputId** *(string) --* **[REQUIRED]**

      Identifies the specific output configuration that you want to update.

    - **NameUpdate** *(string) --*

      If you want to specify a different in-application stream for this output configuration, use
      this field to specify the new in-application stream name.

    - **KinesisStreamsOutputUpdate** *(dict) --*

      Describes an Amazon Kinesis stream as the destination for the output.

      - **ResourceARNUpdate** *(string) --*

        Amazon Resource Name (ARN) of the Amazon Kinesis stream where you want to write the
        output.

      - **RoleARNUpdate** *(string) --*

        ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream on your
        behalf. You need to grant the necessary permissions to this role.

    - **KinesisFirehoseOutputUpdate** *(dict) --*

      Describes an Amazon Kinesis Firehose delivery stream as the destination for the output.

      - **ResourceARNUpdate** *(string) --*

        Amazon Resource Name (ARN) of the Amazon Kinesis Firehose delivery stream to write to.

      - **RoleARNUpdate** *(string) --*

        ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream on your
        behalf. You need to grant the necessary permissions to this role.

    - **LambdaOutputUpdate** *(dict) --*

      Describes an AWS Lambda function as the destination for the output.

      - **ResourceARNUpdate** *(string) --*

        Amazon Resource Name (ARN) of the destination Lambda function.

        .. note::

          To specify an earlier version of the Lambda function than the latest, include the
          Lambda function version in the Lambda function ARN. For more information about Lambda
          ARNs, see `Example ARNs\\: AWS Lambda
          </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__

      - **RoleARNUpdate** *(string) --*

        ARN of the IAM role that Amazon Kinesis Analytics can assume to write to the destination
        function on your behalf. You need to grant the necessary permissions to this role.

    - **DestinationSchemaUpdate** *(dict) --*

      Describes the data format when records are written to the destination. For more
      information, see `Configuring Application Output
      <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-output.html>`__ .

      - **RecordFormatType** *(string) --* **[REQUIRED]**

        Specifies the format of the records on the output stream.
    """


_RequiredClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordColumnsTypeDef = TypedDict(
    "_RequiredClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordColumnsTypeDef",
    {"Name": str, "SqlType": str},
)
_OptionalClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordColumnsTypeDef = TypedDict(
    "_OptionalClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordColumnsTypeDef",
    {"Mapping": str},
    total=False,
)


class ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordColumnsTypeDef(
    _RequiredClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordColumnsTypeDef,
    _OptionalClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordColumnsTypeDef,
):
    """
    Type definition for `ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdate` `RecordColumns`

    Describes the mapping of each data element in the streaming source to the corresponding
    column in the in-application stream.

    Also used to describe the format of the reference data source.

    - **Name** *(string) --* **[REQUIRED]**

      Name of the column created in the in-application input stream or reference table.

    - **Mapping** *(string) --*

      Reference to the data element in the streaming input or the reference data source.
      This element is required if the `RecordFormatType
      <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_RecordFormat.html#analytics-Type-RecordFormat-RecordFormatTypel>`__
      is ``JSON`` .

    - **SqlType** *(string) --* **[REQUIRED]**

      Type of column created in the in-application input stream or reference table.
    """


_ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatMappingParametersCSVMappingParametersTypeDef = TypedDict(
    "_ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatMappingParametersCSVMappingParametersTypeDef",
    {"RecordRowDelimiter": str, "RecordColumnDelimiter": str},
)


class ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatMappingParametersCSVMappingParametersTypeDef(
    _ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatMappingParametersCSVMappingParametersTypeDef
):
    """
    Type definition for `ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatMappingParameters` `CSVMappingParameters`

    Provides additional mapping information when the record format uses delimiters (for
    example, CSV).

    - **RecordRowDelimiter** *(string) --* **[REQUIRED]**

      Row delimiter. For example, in a CSV format, *'\\n'* is the typical row delimiter.

    - **RecordColumnDelimiter** *(string) --* **[REQUIRED]**

      Column delimiter. For example, in a CSV format, a comma (",") is the typical column
      delimiter.
    """


_ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatMappingParametersJSONMappingParametersTypeDef = TypedDict(
    "_ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatMappingParametersJSONMappingParametersTypeDef",
    {"RecordRowPath": str},
)


class ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatMappingParametersJSONMappingParametersTypeDef(
    _ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatMappingParametersJSONMappingParametersTypeDef
):
    """
    Type definition for `ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatMappingParameters` `JSONMappingParameters`

    Provides additional mapping information when JSON is the record format on the
    streaming source.

    - **RecordRowPath** *(string) --* **[REQUIRED]**

      Path to the top-level parent that contains the records.
    """


_ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatMappingParametersTypeDef = TypedDict(
    "_ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatMappingParametersTypeDef",
    {
        "JSONMappingParameters": ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatMappingParametersJSONMappingParametersTypeDef,
        "CSVMappingParameters": ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatMappingParametersCSVMappingParametersTypeDef,
    },
    total=False,
)


class ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatMappingParametersTypeDef(
    _ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatMappingParametersTypeDef
):
    """
    Type definition for `ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormat` `MappingParameters`

    When configuring application input at the time of creating or updating an application,
    provides additional mapping information specific to the record format (such as JSON,
    CSV, or record fields delimited by some delimiter) on the streaming source.

    - **JSONMappingParameters** *(dict) --*

      Provides additional mapping information when JSON is the record format on the
      streaming source.

      - **RecordRowPath** *(string) --* **[REQUIRED]**

        Path to the top-level parent that contains the records.

    - **CSVMappingParameters** *(dict) --*

      Provides additional mapping information when the record format uses delimiters (for
      example, CSV).

      - **RecordRowDelimiter** *(string) --* **[REQUIRED]**

        Row delimiter. For example, in a CSV format, *'\\n'* is the typical row delimiter.

      - **RecordColumnDelimiter** *(string) --* **[REQUIRED]**

        Column delimiter. For example, in a CSV format, a comma (",") is the typical column
        delimiter.
    """


_RequiredClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatTypeDef = TypedDict(
    "_RequiredClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatTypeDef",
    {"RecordFormatType": str},
)
_OptionalClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatTypeDef = TypedDict(
    "_OptionalClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatTypeDef",
    {
        "MappingParameters": ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatMappingParametersTypeDef
    },
    total=False,
)


class ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatTypeDef(
    _RequiredClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatTypeDef,
    _OptionalClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatTypeDef,
):
    """
    Type definition for `ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdate` `RecordFormat`

    Specifies the format of the records on the streaming source.

    - **RecordFormatType** *(string) --* **[REQUIRED]**

      The type of record format.

    - **MappingParameters** *(dict) --*

      When configuring application input at the time of creating or updating an application,
      provides additional mapping information specific to the record format (such as JSON,
      CSV, or record fields delimited by some delimiter) on the streaming source.

      - **JSONMappingParameters** *(dict) --*

        Provides additional mapping information when JSON is the record format on the
        streaming source.

        - **RecordRowPath** *(string) --* **[REQUIRED]**

          Path to the top-level parent that contains the records.

      - **CSVMappingParameters** *(dict) --*

        Provides additional mapping information when the record format uses delimiters (for
        example, CSV).

        - **RecordRowDelimiter** *(string) --* **[REQUIRED]**

          Row delimiter. For example, in a CSV format, *'\\n'* is the typical row delimiter.

        - **RecordColumnDelimiter** *(string) --* **[REQUIRED]**

          Column delimiter. For example, in a CSV format, a comma (",") is the typical column
          delimiter.
    """


_RequiredClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateTypeDef = TypedDict(
    "_RequiredClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateTypeDef",
    {
        "RecordFormat": ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatTypeDef,
        "RecordColumns": List[
            ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordColumnsTypeDef
        ],
    },
)
_OptionalClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateTypeDef = TypedDict(
    "_OptionalClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateTypeDef",
    {"RecordEncoding": str},
    total=False,
)


class ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateTypeDef(
    _RequiredClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateTypeDef,
    _OptionalClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateTypeDef,
):
    """
    Type definition for `ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdates` `ReferenceSchemaUpdate`

    Describes the format of the data in the streaming source, and how each data element maps to
    corresponding columns created in the in-application stream.

    - **RecordFormat** *(dict) --* **[REQUIRED]**

      Specifies the format of the records on the streaming source.

      - **RecordFormatType** *(string) --* **[REQUIRED]**

        The type of record format.

      - **MappingParameters** *(dict) --*

        When configuring application input at the time of creating or updating an application,
        provides additional mapping information specific to the record format (such as JSON,
        CSV, or record fields delimited by some delimiter) on the streaming source.

        - **JSONMappingParameters** *(dict) --*

          Provides additional mapping information when JSON is the record format on the
          streaming source.

          - **RecordRowPath** *(string) --* **[REQUIRED]**

            Path to the top-level parent that contains the records.

        - **CSVMappingParameters** *(dict) --*

          Provides additional mapping information when the record format uses delimiters (for
          example, CSV).

          - **RecordRowDelimiter** *(string) --* **[REQUIRED]**

            Row delimiter. For example, in a CSV format, *'\\n'* is the typical row delimiter.

          - **RecordColumnDelimiter** *(string) --* **[REQUIRED]**

            Column delimiter. For example, in a CSV format, a comma (",") is the typical column
            delimiter.

    - **RecordEncoding** *(string) --*

      Specifies the encoding of the records in the streaming source. For example, UTF-8.

    - **RecordColumns** *(list) --* **[REQUIRED]**

      A list of ``RecordColumn`` objects.

      - *(dict) --*

        Describes the mapping of each data element in the streaming source to the corresponding
        column in the in-application stream.

        Also used to describe the format of the reference data source.

        - **Name** *(string) --* **[REQUIRED]**

          Name of the column created in the in-application input stream or reference table.

        - **Mapping** *(string) --*

          Reference to the data element in the streaming input or the reference data source.
          This element is required if the `RecordFormatType
          <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_RecordFormat.html#analytics-Type-RecordFormat-RecordFormatTypel>`__
          is ``JSON`` .

        - **SqlType** *(string) --* **[REQUIRED]**

          Type of column created in the in-application input stream or reference table.
    """


_ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesS3ReferenceDataSourceUpdateTypeDef = TypedDict(
    "_ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesS3ReferenceDataSourceUpdateTypeDef",
    {"BucketARNUpdate": str, "FileKeyUpdate": str, "ReferenceRoleARNUpdate": str},
    total=False,
)


class ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesS3ReferenceDataSourceUpdateTypeDef(
    _ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesS3ReferenceDataSourceUpdateTypeDef
):
    """
    Type definition for `ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdates` `S3ReferenceDataSourceUpdate`

    Describes the S3 bucket name, object key name, and IAM role that Amazon Kinesis Analytics
    can assume to read the Amazon S3 object on your behalf and populate the in-application
    reference table.

    - **BucketARNUpdate** *(string) --*

      Amazon Resource Name (ARN) of the S3 bucket.

    - **FileKeyUpdate** *(string) --*

      Object key name.

    - **ReferenceRoleARNUpdate** *(string) --*

      ARN of the IAM role that Amazon Kinesis Analytics can assume to read the Amazon S3 object
      and populate the in-application.
    """


_RequiredClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesTypeDef = TypedDict(
    "_RequiredClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesTypeDef",
    {"ReferenceId": str},
)
_OptionalClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesTypeDef = TypedDict(
    "_OptionalClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesTypeDef",
    {
        "TableNameUpdate": str,
        "S3ReferenceDataSourceUpdate": ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesS3ReferenceDataSourceUpdateTypeDef,
        "ReferenceSchemaUpdate": ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateTypeDef,
    },
    total=False,
)


class ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesTypeDef(
    _RequiredClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesTypeDef,
    _OptionalClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesTypeDef,
):
    """
    Type definition for `ClientUpdateApplicationApplicationUpdate` `ReferenceDataSourceUpdates`

    When you update a reference data source configuration for an application, this object
    provides all the updated values (such as the source bucket name and object key name), the
    in-application table name that is created, and updated mapping information that maps the data
    in the Amazon S3 object to the in-application reference table that is created.

    - **ReferenceId** *(string) --* **[REQUIRED]**

      ID of the reference data source being updated. You can use the `DescribeApplication
      <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_DescribeApplication.html>`__
      operation to get this value.

    - **TableNameUpdate** *(string) --*

      In-application table name that is created by this update.

    - **S3ReferenceDataSourceUpdate** *(dict) --*

      Describes the S3 bucket name, object key name, and IAM role that Amazon Kinesis Analytics
      can assume to read the Amazon S3 object on your behalf and populate the in-application
      reference table.

      - **BucketARNUpdate** *(string) --*

        Amazon Resource Name (ARN) of the S3 bucket.

      - **FileKeyUpdate** *(string) --*

        Object key name.

      - **ReferenceRoleARNUpdate** *(string) --*

        ARN of the IAM role that Amazon Kinesis Analytics can assume to read the Amazon S3 object
        and populate the in-application.

    - **ReferenceSchemaUpdate** *(dict) --*

      Describes the format of the data in the streaming source, and how each data element maps to
      corresponding columns created in the in-application stream.

      - **RecordFormat** *(dict) --* **[REQUIRED]**

        Specifies the format of the records on the streaming source.

        - **RecordFormatType** *(string) --* **[REQUIRED]**

          The type of record format.

        - **MappingParameters** *(dict) --*

          When configuring application input at the time of creating or updating an application,
          provides additional mapping information specific to the record format (such as JSON,
          CSV, or record fields delimited by some delimiter) on the streaming source.

          - **JSONMappingParameters** *(dict) --*

            Provides additional mapping information when JSON is the record format on the
            streaming source.

            - **RecordRowPath** *(string) --* **[REQUIRED]**

              Path to the top-level parent that contains the records.

          - **CSVMappingParameters** *(dict) --*

            Provides additional mapping information when the record format uses delimiters (for
            example, CSV).

            - **RecordRowDelimiter** *(string) --* **[REQUIRED]**

              Row delimiter. For example, in a CSV format, *'\\n'* is the typical row delimiter.

            - **RecordColumnDelimiter** *(string) --* **[REQUIRED]**

              Column delimiter. For example, in a CSV format, a comma (",") is the typical column
              delimiter.

      - **RecordEncoding** *(string) --*

        Specifies the encoding of the records in the streaming source. For example, UTF-8.

      - **RecordColumns** *(list) --* **[REQUIRED]**

        A list of ``RecordColumn`` objects.

        - *(dict) --*

          Describes the mapping of each data element in the streaming source to the corresponding
          column in the in-application stream.

          Also used to describe the format of the reference data source.

          - **Name** *(string) --* **[REQUIRED]**

            Name of the column created in the in-application input stream or reference table.

          - **Mapping** *(string) --*

            Reference to the data element in the streaming input or the reference data source.
            This element is required if the `RecordFormatType
            <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_RecordFormat.html#analytics-Type-RecordFormat-RecordFormatTypel>`__
            is ``JSON`` .

          - **SqlType** *(string) --* **[REQUIRED]**

            Type of column created in the in-application input stream or reference table.
    """


_ClientUpdateApplicationApplicationUpdateTypeDef = TypedDict(
    "_ClientUpdateApplicationApplicationUpdateTypeDef",
    {
        "InputUpdates": List[
            ClientUpdateApplicationApplicationUpdateInputUpdatesTypeDef
        ],
        "ApplicationCodeUpdate": str,
        "OutputUpdates": List[
            ClientUpdateApplicationApplicationUpdateOutputUpdatesTypeDef
        ],
        "ReferenceDataSourceUpdates": List[
            ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesTypeDef
        ],
        "CloudWatchLoggingOptionUpdates": List[
            ClientUpdateApplicationApplicationUpdateCloudWatchLoggingOptionUpdatesTypeDef
        ],
    },
    total=False,
)


class ClientUpdateApplicationApplicationUpdateTypeDef(
    _ClientUpdateApplicationApplicationUpdateTypeDef
):
    """
    Type definition for `ClientUpdateApplication` `ApplicationUpdate`

    Describes application updates.

    - **InputUpdates** *(list) --*

      Describes application input configuration updates.

      - *(dict) --*

        Describes updates to a specific input configuration (identified by the ``InputId`` of an
        application).

        - **InputId** *(string) --* **[REQUIRED]**

          Input ID of the application input to be updated.

        - **NamePrefixUpdate** *(string) --*

          Name prefix for in-application streams that Amazon Kinesis Analytics creates for the
          specific streaming source.

        - **InputProcessingConfigurationUpdate** *(dict) --*

          Describes updates for an input processing configuration.

          - **InputLambdaProcessorUpdate** *(dict) --* **[REQUIRED]**

            Provides update information for an `InputLambdaProcessor
            <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_InputLambdaProcessor.html>`__
            .

            - **ResourceARNUpdate** *(string) --*

              The Amazon Resource Name (ARN) of the new `AWS Lambda
              <https://docs.aws.amazon.com/lambda/>`__ function that is used to preprocess the
              records in the stream.

              .. note::

                To specify an earlier version of the Lambda function than the latest, include the
                Lambda function version in the Lambda function ARN. For more information about Lambda
                ARNs, see `Example ARNs\\: AWS Lambda
                </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__

            - **RoleARNUpdate** *(string) --*

              The ARN of the new IAM role that is used to access the AWS Lambda function.

        - **KinesisStreamsInputUpdate** *(dict) --*

          If an Amazon Kinesis stream is the streaming source to be updated, provides an updated
          stream Amazon Resource Name (ARN) and IAM role ARN.

          - **ResourceARNUpdate** *(string) --*

            Amazon Resource Name (ARN) of the input Amazon Kinesis stream to read.

          - **RoleARNUpdate** *(string) --*

            ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream on your
            behalf. You need to grant the necessary permissions to this role.

        - **KinesisFirehoseInputUpdate** *(dict) --*

          If an Amazon Kinesis Firehose delivery stream is the streaming source to be updated,
          provides an updated stream ARN and IAM role ARN.

          - **ResourceARNUpdate** *(string) --*

            Amazon Resource Name (ARN) of the input Amazon Kinesis Firehose delivery stream to read.

          - **RoleARNUpdate** *(string) --*

            ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream on your
            behalf. You need to grant the necessary permissions to this role.

        - **InputSchemaUpdate** *(dict) --*

          Describes the data format on the streaming source, and how record elements on the streaming
          source map to columns of the in-application stream that is created.

          - **RecordFormatUpdate** *(dict) --*

            Specifies the format of the records on the streaming source.

            - **RecordFormatType** *(string) --* **[REQUIRED]**

              The type of record format.

            - **MappingParameters** *(dict) --*

              When configuring application input at the time of creating or updating an application,
              provides additional mapping information specific to the record format (such as JSON,
              CSV, or record fields delimited by some delimiter) on the streaming source.

              - **JSONMappingParameters** *(dict) --*

                Provides additional mapping information when JSON is the record format on the
                streaming source.

                - **RecordRowPath** *(string) --* **[REQUIRED]**

                  Path to the top-level parent that contains the records.

              - **CSVMappingParameters** *(dict) --*

                Provides additional mapping information when the record format uses delimiters (for
                example, CSV).

                - **RecordRowDelimiter** *(string) --* **[REQUIRED]**

                  Row delimiter. For example, in a CSV format, *'\\n'* is the typical row delimiter.

                - **RecordColumnDelimiter** *(string) --* **[REQUIRED]**

                  Column delimiter. For example, in a CSV format, a comma (",") is the typical column
                  delimiter.

          - **RecordEncodingUpdate** *(string) --*

            Specifies the encoding of the records in the streaming source. For example, UTF-8.

          - **RecordColumnUpdates** *(list) --*

            A list of ``RecordColumn`` objects. Each object describes the mapping of the streaming
            source element to the corresponding column in the in-application stream.

            - *(dict) --*

              Describes the mapping of each data element in the streaming source to the corresponding
              column in the in-application stream.

              Also used to describe the format of the reference data source.

              - **Name** *(string) --* **[REQUIRED]**

                Name of the column created in the in-application input stream or reference table.

              - **Mapping** *(string) --*

                Reference to the data element in the streaming input or the reference data source.
                This element is required if the `RecordFormatType
                <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_RecordFormat.html#analytics-Type-RecordFormat-RecordFormatTypel>`__
                is ``JSON`` .

              - **SqlType** *(string) --* **[REQUIRED]**

                Type of column created in the in-application input stream or reference table.

        - **InputParallelismUpdate** *(dict) --*

          Describes the parallelism updates (the number in-application streams Amazon Kinesis
          Analytics creates for the specific streaming source).

          - **CountUpdate** *(integer) --*

            Number of in-application streams to create for the specified streaming source.

    - **ApplicationCodeUpdate** *(string) --*

      Describes application code updates.

    - **OutputUpdates** *(list) --*

      Describes application output configuration updates.

      - *(dict) --*

        Describes updates to the output configuration identified by the ``OutputId`` .

        - **OutputId** *(string) --* **[REQUIRED]**

          Identifies the specific output configuration that you want to update.

        - **NameUpdate** *(string) --*

          If you want to specify a different in-application stream for this output configuration, use
          this field to specify the new in-application stream name.

        - **KinesisStreamsOutputUpdate** *(dict) --*

          Describes an Amazon Kinesis stream as the destination for the output.

          - **ResourceARNUpdate** *(string) --*

            Amazon Resource Name (ARN) of the Amazon Kinesis stream where you want to write the
            output.

          - **RoleARNUpdate** *(string) --*

            ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream on your
            behalf. You need to grant the necessary permissions to this role.

        - **KinesisFirehoseOutputUpdate** *(dict) --*

          Describes an Amazon Kinesis Firehose delivery stream as the destination for the output.

          - **ResourceARNUpdate** *(string) --*

            Amazon Resource Name (ARN) of the Amazon Kinesis Firehose delivery stream to write to.

          - **RoleARNUpdate** *(string) --*

            ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream on your
            behalf. You need to grant the necessary permissions to this role.

        - **LambdaOutputUpdate** *(dict) --*

          Describes an AWS Lambda function as the destination for the output.

          - **ResourceARNUpdate** *(string) --*

            Amazon Resource Name (ARN) of the destination Lambda function.

            .. note::

              To specify an earlier version of the Lambda function than the latest, include the
              Lambda function version in the Lambda function ARN. For more information about Lambda
              ARNs, see `Example ARNs\\: AWS Lambda
              </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__

          - **RoleARNUpdate** *(string) --*

            ARN of the IAM role that Amazon Kinesis Analytics can assume to write to the destination
            function on your behalf. You need to grant the necessary permissions to this role.

        - **DestinationSchemaUpdate** *(dict) --*

          Describes the data format when records are written to the destination. For more
          information, see `Configuring Application Output
          <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-output.html>`__ .

          - **RecordFormatType** *(string) --* **[REQUIRED]**

            Specifies the format of the records on the output stream.

    - **ReferenceDataSourceUpdates** *(list) --*

      Describes application reference data source updates.

      - *(dict) --*

        When you update a reference data source configuration for an application, this object
        provides all the updated values (such as the source bucket name and object key name), the
        in-application table name that is created, and updated mapping information that maps the data
        in the Amazon S3 object to the in-application reference table that is created.

        - **ReferenceId** *(string) --* **[REQUIRED]**

          ID of the reference data source being updated. You can use the `DescribeApplication
          <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_DescribeApplication.html>`__
          operation to get this value.

        - **TableNameUpdate** *(string) --*

          In-application table name that is created by this update.

        - **S3ReferenceDataSourceUpdate** *(dict) --*

          Describes the S3 bucket name, object key name, and IAM role that Amazon Kinesis Analytics
          can assume to read the Amazon S3 object on your behalf and populate the in-application
          reference table.

          - **BucketARNUpdate** *(string) --*

            Amazon Resource Name (ARN) of the S3 bucket.

          - **FileKeyUpdate** *(string) --*

            Object key name.

          - **ReferenceRoleARNUpdate** *(string) --*

            ARN of the IAM role that Amazon Kinesis Analytics can assume to read the Amazon S3 object
            and populate the in-application.

        - **ReferenceSchemaUpdate** *(dict) --*

          Describes the format of the data in the streaming source, and how each data element maps to
          corresponding columns created in the in-application stream.

          - **RecordFormat** *(dict) --* **[REQUIRED]**

            Specifies the format of the records on the streaming source.

            - **RecordFormatType** *(string) --* **[REQUIRED]**

              The type of record format.

            - **MappingParameters** *(dict) --*

              When configuring application input at the time of creating or updating an application,
              provides additional mapping information specific to the record format (such as JSON,
              CSV, or record fields delimited by some delimiter) on the streaming source.

              - **JSONMappingParameters** *(dict) --*

                Provides additional mapping information when JSON is the record format on the
                streaming source.

                - **RecordRowPath** *(string) --* **[REQUIRED]**

                  Path to the top-level parent that contains the records.

              - **CSVMappingParameters** *(dict) --*

                Provides additional mapping information when the record format uses delimiters (for
                example, CSV).

                - **RecordRowDelimiter** *(string) --* **[REQUIRED]**

                  Row delimiter. For example, in a CSV format, *'\\n'* is the typical row delimiter.

                - **RecordColumnDelimiter** *(string) --* **[REQUIRED]**

                  Column delimiter. For example, in a CSV format, a comma (",") is the typical column
                  delimiter.

          - **RecordEncoding** *(string) --*

            Specifies the encoding of the records in the streaming source. For example, UTF-8.

          - **RecordColumns** *(list) --* **[REQUIRED]**

            A list of ``RecordColumn`` objects.

            - *(dict) --*

              Describes the mapping of each data element in the streaming source to the corresponding
              column in the in-application stream.

              Also used to describe the format of the reference data source.

              - **Name** *(string) --* **[REQUIRED]**

                Name of the column created in the in-application input stream or reference table.

              - **Mapping** *(string) --*

                Reference to the data element in the streaming input or the reference data source.
                This element is required if the `RecordFormatType
                <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_RecordFormat.html#analytics-Type-RecordFormat-RecordFormatTypel>`__
                is ``JSON`` .

              - **SqlType** *(string) --* **[REQUIRED]**

                Type of column created in the in-application input stream or reference table.

    - **CloudWatchLoggingOptionUpdates** *(list) --*

      Describes application CloudWatch logging option updates.

      - *(dict) --*

        Describes CloudWatch logging option updates.

        - **CloudWatchLoggingOptionId** *(string) --* **[REQUIRED]**

          ID of the CloudWatch logging option to update

        - **LogStreamARNUpdate** *(string) --*

          ARN of the CloudWatch log to receive application messages.

        - **RoleARNUpdate** *(string) --*

          IAM ARN of the role to use to send application messages. Note: To write application
          messages to CloudWatch, the IAM role used must have the ``PutLogEvents`` policy action
          enabled.
    """
