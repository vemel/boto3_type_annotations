"Main interface for kinesisanalyticsv2 type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from typing_extensions import TypedDict


_ClientAddApplicationCloudWatchLoggingOptionCloudWatchLoggingOptionTypeDef = TypedDict(
    "_ClientAddApplicationCloudWatchLoggingOptionCloudWatchLoggingOptionTypeDef",
    {"LogStreamARN": str},
)


class ClientAddApplicationCloudWatchLoggingOptionCloudWatchLoggingOptionTypeDef(
    _ClientAddApplicationCloudWatchLoggingOptionCloudWatchLoggingOptionTypeDef
):
    """
    Type definition for `ClientAddApplicationCloudWatchLoggingOption` `CloudWatchLoggingOption`

    Provides the Amazon CloudWatch log stream Amazon Resource Name (ARN).

    - **LogStreamARN** *(string) --* **[REQUIRED]**

      The ARN of the CloudWatch log to receive application messages.
    """


_ClientAddApplicationCloudWatchLoggingOptionResponseCloudWatchLoggingOptionDescriptionsTypeDef = TypedDict(
    "_ClientAddApplicationCloudWatchLoggingOptionResponseCloudWatchLoggingOptionDescriptionsTypeDef",
    {"CloudWatchLoggingOptionId": str, "LogStreamARN": str, "RoleARN": str},
    total=False,
)


class ClientAddApplicationCloudWatchLoggingOptionResponseCloudWatchLoggingOptionDescriptionsTypeDef(
    _ClientAddApplicationCloudWatchLoggingOptionResponseCloudWatchLoggingOptionDescriptionsTypeDef
):
    """
    Type definition for `ClientAddApplicationCloudWatchLoggingOptionResponse` `CloudWatchLoggingOptionDescriptions`

    Describes the Amazon CloudWatch logging option.

    - **CloudWatchLoggingOptionId** *(string) --*

      The ID of the CloudWatch logging option description.

    - **LogStreamARN** *(string) --*

      The Amazon Resource Name (ARN) of the CloudWatch log to receive application messages.

    - **RoleARN** *(string) --*

      The IAM ARN of the role to use to send application messages.

      .. note::

        Provided for backward compatibility. Applications created with the current API version
        have an application-level service execution role rather than a resource-level role.
    """


_ClientAddApplicationCloudWatchLoggingOptionResponseTypeDef = TypedDict(
    "_ClientAddApplicationCloudWatchLoggingOptionResponseTypeDef",
    {
        "ApplicationARN": str,
        "ApplicationVersionId": int,
        "CloudWatchLoggingOptionDescriptions": List[
            ClientAddApplicationCloudWatchLoggingOptionResponseCloudWatchLoggingOptionDescriptionsTypeDef
        ],
    },
    total=False,
)


class ClientAddApplicationCloudWatchLoggingOptionResponseTypeDef(
    _ClientAddApplicationCloudWatchLoggingOptionResponseTypeDef
):
    """
    Type definition for `ClientAddApplicationCloudWatchLoggingOption` `Response`

    - **ApplicationARN** *(string) --*

      The application's ARN.

    - **ApplicationVersionId** *(integer) --*

      The new version ID of the Kinesis Data Analytics application. Kinesis Data Analytics updates
      the ``ApplicationVersionId`` each time you change the CloudWatch logging options.

    - **CloudWatchLoggingOptionDescriptions** *(list) --*

      The descriptions of the current CloudWatch logging options for the Kinesis Data Analytics
      application.

      - *(dict) --*

        Describes the Amazon CloudWatch logging option.

        - **CloudWatchLoggingOptionId** *(string) --*

          The ID of the CloudWatch logging option description.

        - **LogStreamARN** *(string) --*

          The Amazon Resource Name (ARN) of the CloudWatch log to receive application messages.

        - **RoleARN** *(string) --*

          The IAM ARN of the role to use to send application messages.

          .. note::

            Provided for backward compatibility. Applications created with the current API version
            have an application-level service execution role rather than a resource-level role.
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

    - **Count** *(integer) --*

      The number of in-application streams to create.
    """


_ClientAddApplicationInputInputInputProcessingConfigurationInputLambdaProcessorTypeDef = TypedDict(
    "_ClientAddApplicationInputInputInputProcessingConfigurationInputLambdaProcessorTypeDef",
    {"ResourceARN": str},
)


class ClientAddApplicationInputInputInputProcessingConfigurationInputLambdaProcessorTypeDef(
    _ClientAddApplicationInputInputInputProcessingConfigurationInputLambdaProcessorTypeDef
):
    """
    Type definition for `ClientAddApplicationInputInputInputProcessingConfiguration` `InputLambdaProcessor`

    The  InputLambdaProcessor that is used to preprocess the records in the stream before being
    processed by your application code.

    - **ResourceARN** *(string) --* **[REQUIRED]**

      The ARN of the AWS Lambda function that operates on records in the stream.

      .. note::

        To specify an earlier version of the Lambda function than the latest, include the Lambda
        function version in the Lambda function ARN. For more information about Lambda ARNs, see
        `Example ARNs\\: AWS Lambda
        </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__
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

    The  InputProcessingConfiguration for the input. An input processor transforms records as they
    are received from the stream, before the application's SQL code executes. Currently, the only
    input processing configuration available is  InputLambdaProcessor .

    - **InputLambdaProcessor** *(dict) --* **[REQUIRED]**

      The  InputLambdaProcessor that is used to preprocess the records in the stream before being
      processed by your application code.

      - **ResourceARN** *(string) --* **[REQUIRED]**

        The ARN of the AWS Lambda function that operates on records in the stream.

        .. note::

          To specify an earlier version of the Lambda function than the latest, include the Lambda
          function version in the Lambda function ARN. For more information about Lambda ARNs, see
          `Example ARNs\\: AWS Lambda
          </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__
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

    For an SQL-based Amazon Kinesis Data Analytics application, describes the mapping of each
    data element in the streaming source to the corresponding column in the in-application
    stream.

    Also used to describe the format of the reference data source.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the column that is created in the in-application input stream or reference
      table.

    - **Mapping** *(string) --*

      A reference to the data element in the streaming input or the reference data source.

    - **SqlType** *(string) --* **[REQUIRED]**

      The type of column created in the in-application input stream or reference table.
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

      The row delimiter. For example, in a CSV format, *'\\n'* is the typical row delimiter.

    - **RecordColumnDelimiter** *(string) --* **[REQUIRED]**

      The column delimiter. For example, in a CSV format, a comma (",") is the typical column
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

      The path to the top-level parent that contains the records.
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

    When you configure application input at the time of creating or updating an application,
    provides additional mapping information specific to the record format (such as JSON, CSV,
    or record fields delimited by some delimiter) on the streaming source.

    - **JSONMappingParameters** *(dict) --*

      Provides additional mapping information when JSON is the record format on the streaming
      source.

      - **RecordRowPath** *(string) --* **[REQUIRED]**

        The path to the top-level parent that contains the records.

    - **CSVMappingParameters** *(dict) --*

      Provides additional mapping information when the record format uses delimiters (for
      example, CSV).

      - **RecordRowDelimiter** *(string) --* **[REQUIRED]**

        The row delimiter. For example, in a CSV format, *'\\n'* is the typical row delimiter.

      - **RecordColumnDelimiter** *(string) --* **[REQUIRED]**

        The column delimiter. For example, in a CSV format, a comma (",") is the typical column
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

      When you configure application input at the time of creating or updating an application,
      provides additional mapping information specific to the record format (such as JSON, CSV,
      or record fields delimited by some delimiter) on the streaming source.

      - **JSONMappingParameters** *(dict) --*

        Provides additional mapping information when JSON is the record format on the streaming
        source.

        - **RecordRowPath** *(string) --* **[REQUIRED]**

          The path to the top-level parent that contains the records.

      - **CSVMappingParameters** *(dict) --*

        Provides additional mapping information when the record format uses delimiters (for
        example, CSV).

        - **RecordRowDelimiter** *(string) --* **[REQUIRED]**

          The row delimiter. For example, in a CSV format, *'\\n'* is the typical row delimiter.

        - **RecordColumnDelimiter** *(string) --* **[REQUIRED]**

          The column delimiter. For example, in a CSV format, a comma (",") is the typical column
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

        When you configure application input at the time of creating or updating an application,
        provides additional mapping information specific to the record format (such as JSON, CSV,
        or record fields delimited by some delimiter) on the streaming source.

        - **JSONMappingParameters** *(dict) --*

          Provides additional mapping information when JSON is the record format on the streaming
          source.

          - **RecordRowPath** *(string) --* **[REQUIRED]**

            The path to the top-level parent that contains the records.

        - **CSVMappingParameters** *(dict) --*

          Provides additional mapping information when the record format uses delimiters (for
          example, CSV).

          - **RecordRowDelimiter** *(string) --* **[REQUIRED]**

            The row delimiter. For example, in a CSV format, *'\\n'* is the typical row delimiter.

          - **RecordColumnDelimiter** *(string) --* **[REQUIRED]**

            The column delimiter. For example, in a CSV format, a comma (",") is the typical column
            delimiter.

    - **RecordEncoding** *(string) --*

      Specifies the encoding of the records in the streaming source. For example, UTF-8.

    - **RecordColumns** *(list) --* **[REQUIRED]**

      A list of ``RecordColumn`` objects.

      - *(dict) --*

        For an SQL-based Amazon Kinesis Data Analytics application, describes the mapping of each
        data element in the streaming source to the corresponding column in the in-application
        stream.

        Also used to describe the format of the reference data source.

        - **Name** *(string) --* **[REQUIRED]**

          The name of the column that is created in the in-application input stream or reference
          table.

        - **Mapping** *(string) --*

          A reference to the data element in the streaming input or the reference data source.

        - **SqlType** *(string) --* **[REQUIRED]**

          The type of column created in the in-application input stream or reference table.
    """


_ClientAddApplicationInputInputKinesisFirehoseInputTypeDef = TypedDict(
    "_ClientAddApplicationInputInputKinesisFirehoseInputTypeDef", {"ResourceARN": str}
)


class ClientAddApplicationInputInputKinesisFirehoseInputTypeDef(
    _ClientAddApplicationInputInputKinesisFirehoseInputTypeDef
):
    """
    Type definition for `ClientAddApplicationInputInput` `KinesisFirehoseInput`

    If the streaming source is an Amazon Kinesis Data Firehose delivery stream, identifies the
    delivery stream's ARN.

    - **ResourceARN** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the delivery stream.
    """


_ClientAddApplicationInputInputKinesisStreamsInputTypeDef = TypedDict(
    "_ClientAddApplicationInputInputKinesisStreamsInputTypeDef", {"ResourceARN": str}
)


class ClientAddApplicationInputInputKinesisStreamsInputTypeDef(
    _ClientAddApplicationInputInputKinesisStreamsInputTypeDef
):
    """
    Type definition for `ClientAddApplicationInputInput` `KinesisStreamsInput`

    If the streaming source is an Amazon Kinesis data stream, identifies the stream's Amazon
    Resource Name (ARN).

    - **ResourceARN** *(string) --* **[REQUIRED]**

      The ARN of the input Kinesis data stream to read.
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

    The  Input to add.

    - **NamePrefix** *(string) --* **[REQUIRED]**

      The name prefix to use when creating an in-application stream. Suppose that you specify a
      prefix "``MyInApplicationStream`` ." Kinesis Data Analytics then creates one or more (as per
      the ``InputParallelism`` count you specified) in-application streams with the names
      "``MyInApplicationStream_001`` ," "``MyInApplicationStream_002`` ," and so on.

    - **InputProcessingConfiguration** *(dict) --*

      The  InputProcessingConfiguration for the input. An input processor transforms records as they
      are received from the stream, before the application's SQL code executes. Currently, the only
      input processing configuration available is  InputLambdaProcessor .

      - **InputLambdaProcessor** *(dict) --* **[REQUIRED]**

        The  InputLambdaProcessor that is used to preprocess the records in the stream before being
        processed by your application code.

        - **ResourceARN** *(string) --* **[REQUIRED]**

          The ARN of the AWS Lambda function that operates on records in the stream.

          .. note::

            To specify an earlier version of the Lambda function than the latest, include the Lambda
            function version in the Lambda function ARN. For more information about Lambda ARNs, see
            `Example ARNs\\: AWS Lambda
            </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__

    - **KinesisStreamsInput** *(dict) --*

      If the streaming source is an Amazon Kinesis data stream, identifies the stream's Amazon
      Resource Name (ARN).

      - **ResourceARN** *(string) --* **[REQUIRED]**

        The ARN of the input Kinesis data stream to read.

    - **KinesisFirehoseInput** *(dict) --*

      If the streaming source is an Amazon Kinesis Data Firehose delivery stream, identifies the
      delivery stream's ARN.

      - **ResourceARN** *(string) --* **[REQUIRED]**

        The Amazon Resource Name (ARN) of the delivery stream.

    - **InputParallelism** *(dict) --*

      Describes the number of in-application streams to create.

      - **Count** *(integer) --*

        The number of in-application streams to create.

    - **InputSchema** *(dict) --* **[REQUIRED]**

      Describes the format of the data in the streaming source, and how each data element maps to
      corresponding columns in the in-application stream that is being created.

      Also used to describe the format of the reference data source.

      - **RecordFormat** *(dict) --* **[REQUIRED]**

        Specifies the format of the records on the streaming source.

        - **RecordFormatType** *(string) --* **[REQUIRED]**

          The type of record format.

        - **MappingParameters** *(dict) --*

          When you configure application input at the time of creating or updating an application,
          provides additional mapping information specific to the record format (such as JSON, CSV,
          or record fields delimited by some delimiter) on the streaming source.

          - **JSONMappingParameters** *(dict) --*

            Provides additional mapping information when JSON is the record format on the streaming
            source.

            - **RecordRowPath** *(string) --* **[REQUIRED]**

              The path to the top-level parent that contains the records.

          - **CSVMappingParameters** *(dict) --*

            Provides additional mapping information when the record format uses delimiters (for
            example, CSV).

            - **RecordRowDelimiter** *(string) --* **[REQUIRED]**

              The row delimiter. For example, in a CSV format, *'\\n'* is the typical row delimiter.

            - **RecordColumnDelimiter** *(string) --* **[REQUIRED]**

              The column delimiter. For example, in a CSV format, a comma (",") is the typical column
              delimiter.

      - **RecordEncoding** *(string) --*

        Specifies the encoding of the records in the streaming source. For example, UTF-8.

      - **RecordColumns** *(list) --* **[REQUIRED]**

        A list of ``RecordColumn`` objects.

        - *(dict) --*

          For an SQL-based Amazon Kinesis Data Analytics application, describes the mapping of each
          data element in the streaming source to the corresponding column in the in-application
          stream.

          Also used to describe the format of the reference data source.

          - **Name** *(string) --* **[REQUIRED]**

            The name of the column that is created in the in-application input stream or reference
            table.

          - **Mapping** *(string) --*

            A reference to the data element in the streaming input or the reference data source.

          - **SqlType** *(string) --* **[REQUIRED]**

            The type of column created in the in-application input stream or reference table.
    """


_ClientAddApplicationInputProcessingConfigurationInputProcessingConfigurationInputLambdaProcessorTypeDef = TypedDict(
    "_ClientAddApplicationInputProcessingConfigurationInputProcessingConfigurationInputLambdaProcessorTypeDef",
    {"ResourceARN": str},
)


class ClientAddApplicationInputProcessingConfigurationInputProcessingConfigurationInputLambdaProcessorTypeDef(
    _ClientAddApplicationInputProcessingConfigurationInputProcessingConfigurationInputLambdaProcessorTypeDef
):
    """
    Type definition for `ClientAddApplicationInputProcessingConfigurationInputProcessingConfiguration` `InputLambdaProcessor`

    The  InputLambdaProcessor that is used to preprocess the records in the stream before being
    processed by your application code.

    - **ResourceARN** *(string) --* **[REQUIRED]**

      The ARN of the AWS Lambda function that operates on records in the stream.

      .. note::

        To specify an earlier version of the Lambda function than the latest, include the Lambda
        function version in the Lambda function ARN. For more information about Lambda ARNs, see
        `Example ARNs\\: AWS Lambda
        </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__
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

    The  InputProcessingConfiguration to add to the application.

    - **InputLambdaProcessor** *(dict) --* **[REQUIRED]**

      The  InputLambdaProcessor that is used to preprocess the records in the stream before being
      processed by your application code.

      - **ResourceARN** *(string) --* **[REQUIRED]**

        The ARN of the AWS Lambda function that operates on records in the stream.

        .. note::

          To specify an earlier version of the Lambda function than the latest, include the Lambda
          function version in the Lambda function ARN. For more information about Lambda ARNs, see
          `Example ARNs\\: AWS Lambda
          </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__
    """


_ClientAddApplicationInputProcessingConfigurationResponseInputProcessingConfigurationDescriptionInputLambdaProcessorDescriptionTypeDef = TypedDict(
    "_ClientAddApplicationInputProcessingConfigurationResponseInputProcessingConfigurationDescriptionInputLambdaProcessorDescriptionTypeDef",
    {"ResourceARN": str, "RoleARN": str},
    total=False,
)


class ClientAddApplicationInputProcessingConfigurationResponseInputProcessingConfigurationDescriptionInputLambdaProcessorDescriptionTypeDef(
    _ClientAddApplicationInputProcessingConfigurationResponseInputProcessingConfigurationDescriptionInputLambdaProcessorDescriptionTypeDef
):
    """
    Type definition for `ClientAddApplicationInputProcessingConfigurationResponseInputProcessingConfigurationDescription` `InputLambdaProcessorDescription`

    Provides configuration information about the associated  InputLambdaProcessorDescription

    - **ResourceARN** *(string) --*

      The ARN of the AWS Lambda function that is used to preprocess the records in the stream.

      .. note::

        To specify an earlier version of the Lambda function than the latest, include the
        Lambda function version in the Lambda function ARN. For more information about Lambda
        ARNs, see `Example ARNs\\: AWS Lambda
        </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__

    - **RoleARN** *(string) --*

      The ARN of the IAM role that is used to access the AWS Lambda function.

      .. note::

        Provided for backward compatibility. Applications that are created with the current API
        version have an application-level service execution role rather than a resource-level
        role.
    """


_ClientAddApplicationInputProcessingConfigurationResponseInputProcessingConfigurationDescriptionTypeDef = TypedDict(
    "_ClientAddApplicationInputProcessingConfigurationResponseInputProcessingConfigurationDescriptionTypeDef",
    {
        "InputLambdaProcessorDescription": ClientAddApplicationInputProcessingConfigurationResponseInputProcessingConfigurationDescriptionInputLambdaProcessorDescriptionTypeDef
    },
    total=False,
)


class ClientAddApplicationInputProcessingConfigurationResponseInputProcessingConfigurationDescriptionTypeDef(
    _ClientAddApplicationInputProcessingConfigurationResponseInputProcessingConfigurationDescriptionTypeDef
):
    """
    Type definition for `ClientAddApplicationInputProcessingConfigurationResponse` `InputProcessingConfigurationDescription`

    The description of the preprocessor that executes on records in this input before the
    application's code is run.

    - **InputLambdaProcessorDescription** *(dict) --*

      Provides configuration information about the associated  InputLambdaProcessorDescription

      - **ResourceARN** *(string) --*

        The ARN of the AWS Lambda function that is used to preprocess the records in the stream.

        .. note::

          To specify an earlier version of the Lambda function than the latest, include the
          Lambda function version in the Lambda function ARN. For more information about Lambda
          ARNs, see `Example ARNs\\: AWS Lambda
          </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__

      - **RoleARN** *(string) --*

        The ARN of the IAM role that is used to access the AWS Lambda function.

        .. note::

          Provided for backward compatibility. Applications that are created with the current API
          version have an application-level service execution role rather than a resource-level
          role.
    """


_ClientAddApplicationInputProcessingConfigurationResponseTypeDef = TypedDict(
    "_ClientAddApplicationInputProcessingConfigurationResponseTypeDef",
    {
        "ApplicationARN": str,
        "ApplicationVersionId": int,
        "InputId": str,
        "InputProcessingConfigurationDescription": ClientAddApplicationInputProcessingConfigurationResponseInputProcessingConfigurationDescriptionTypeDef,
    },
    total=False,
)


class ClientAddApplicationInputProcessingConfigurationResponseTypeDef(
    _ClientAddApplicationInputProcessingConfigurationResponseTypeDef
):
    """
    Type definition for `ClientAddApplicationInputProcessingConfiguration` `Response`

    - **ApplicationARN** *(string) --*

      The Amazon Resource Name (ARN) of the application.

    - **ApplicationVersionId** *(integer) --*

      Provides the current application version.

    - **InputId** *(string) --*

      The input ID that is associated with the application input. This is the ID that Amazon
      Kinesis Data Analytics assigns to each input configuration that you add to your application.

    - **InputProcessingConfigurationDescription** *(dict) --*

      The description of the preprocessor that executes on records in this input before the
      application's code is run.

      - **InputLambdaProcessorDescription** *(dict) --*

        Provides configuration information about the associated  InputLambdaProcessorDescription

        - **ResourceARN** *(string) --*

          The ARN of the AWS Lambda function that is used to preprocess the records in the stream.

          .. note::

            To specify an earlier version of the Lambda function than the latest, include the
            Lambda function version in the Lambda function ARN. For more information about Lambda
            ARNs, see `Example ARNs\\: AWS Lambda
            </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__

        - **RoleARN** *(string) --*

          The ARN of the IAM role that is used to access the AWS Lambda function.

          .. note::

            Provided for backward compatibility. Applications that are created with the current API
            version have an application-level service execution role rather than a resource-level
            role.
    """


_ClientAddApplicationInputResponseInputDescriptionsInputParallelismTypeDef = TypedDict(
    "_ClientAddApplicationInputResponseInputDescriptionsInputParallelismTypeDef",
    {"Count": int},
    total=False,
)


class ClientAddApplicationInputResponseInputDescriptionsInputParallelismTypeDef(
    _ClientAddApplicationInputResponseInputDescriptionsInputParallelismTypeDef
):
    """
    Type definition for `ClientAddApplicationInputResponseInputDescriptions` `InputParallelism`

    Describes the configured parallelism (number of in-application streams mapped to the
    streaming source).

    - **Count** *(integer) --*

      The number of in-application streams to create.
    """


_ClientAddApplicationInputResponseInputDescriptionsInputProcessingConfigurationDescriptionInputLambdaProcessorDescriptionTypeDef = TypedDict(
    "_ClientAddApplicationInputResponseInputDescriptionsInputProcessingConfigurationDescriptionInputLambdaProcessorDescriptionTypeDef",
    {"ResourceARN": str, "RoleARN": str},
    total=False,
)


class ClientAddApplicationInputResponseInputDescriptionsInputProcessingConfigurationDescriptionInputLambdaProcessorDescriptionTypeDef(
    _ClientAddApplicationInputResponseInputDescriptionsInputProcessingConfigurationDescriptionInputLambdaProcessorDescriptionTypeDef
):
    """
    Type definition for `ClientAddApplicationInputResponseInputDescriptionsInputProcessingConfigurationDescription` `InputLambdaProcessorDescription`

    Provides configuration information about the associated  InputLambdaProcessorDescription

    - **ResourceARN** *(string) --*

      The ARN of the AWS Lambda function that is used to preprocess the records in the
      stream.

      .. note::

        To specify an earlier version of the Lambda function than the latest, include the
        Lambda function version in the Lambda function ARN. For more information about
        Lambda ARNs, see `Example ARNs\\: AWS Lambda
        </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__

    - **RoleARN** *(string) --*

      The ARN of the IAM role that is used to access the AWS Lambda function.

      .. note::

        Provided for backward compatibility. Applications that are created with the current
        API version have an application-level service execution role rather than a
        resource-level role.
    """


_ClientAddApplicationInputResponseInputDescriptionsInputProcessingConfigurationDescriptionTypeDef = TypedDict(
    "_ClientAddApplicationInputResponseInputDescriptionsInputProcessingConfigurationDescriptionTypeDef",
    {
        "InputLambdaProcessorDescription": ClientAddApplicationInputResponseInputDescriptionsInputProcessingConfigurationDescriptionInputLambdaProcessorDescriptionTypeDef
    },
    total=False,
)


class ClientAddApplicationInputResponseInputDescriptionsInputProcessingConfigurationDescriptionTypeDef(
    _ClientAddApplicationInputResponseInputDescriptionsInputProcessingConfigurationDescriptionTypeDef
):
    """
    Type definition for `ClientAddApplicationInputResponseInputDescriptions` `InputProcessingConfigurationDescription`

    The description of the preprocessor that executes on records in this input before the
    application's code is run.

    - **InputLambdaProcessorDescription** *(dict) --*

      Provides configuration information about the associated  InputLambdaProcessorDescription

      - **ResourceARN** *(string) --*

        The ARN of the AWS Lambda function that is used to preprocess the records in the
        stream.

        .. note::

          To specify an earlier version of the Lambda function than the latest, include the
          Lambda function version in the Lambda function ARN. For more information about
          Lambda ARNs, see `Example ARNs\\: AWS Lambda
          </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__

      - **RoleARN** *(string) --*

        The ARN of the IAM role that is used to access the AWS Lambda function.

        .. note::

          Provided for backward compatibility. Applications that are created with the current
          API version have an application-level service execution role rather than a
          resource-level role.
    """


_ClientAddApplicationInputResponseInputDescriptionsInputSchemaRecordColumnsTypeDef = TypedDict(
    "_ClientAddApplicationInputResponseInputDescriptionsInputSchemaRecordColumnsTypeDef",
    {"Name": str, "Mapping": str, "SqlType": str},
    total=False,
)


class ClientAddApplicationInputResponseInputDescriptionsInputSchemaRecordColumnsTypeDef(
    _ClientAddApplicationInputResponseInputDescriptionsInputSchemaRecordColumnsTypeDef
):
    """
    Type definition for `ClientAddApplicationInputResponseInputDescriptionsInputSchema` `RecordColumns`

    For an SQL-based Amazon Kinesis Data Analytics application, describes the mapping of
    each data element in the streaming source to the corresponding column in the
    in-application stream.

    Also used to describe the format of the reference data source.

    - **Name** *(string) --*

      The name of the column that is created in the in-application input stream or
      reference table.

    - **Mapping** *(string) --*

      A reference to the data element in the streaming input or the reference data source.

    - **SqlType** *(string) --*

      The type of column created in the in-application input stream or reference table.
    """


_ClientAddApplicationInputResponseInputDescriptionsInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef = TypedDict(
    "_ClientAddApplicationInputResponseInputDescriptionsInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef",
    {"RecordRowDelimiter": str, "RecordColumnDelimiter": str},
    total=False,
)


class ClientAddApplicationInputResponseInputDescriptionsInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef(
    _ClientAddApplicationInputResponseInputDescriptionsInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef
):
    """
    Type definition for `ClientAddApplicationInputResponseInputDescriptionsInputSchemaRecordFormatMappingParameters` `CSVMappingParameters`

    Provides additional mapping information when the record format uses delimiters (for
    example, CSV).

    - **RecordRowDelimiter** *(string) --*

      The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
      delimiter.

    - **RecordColumnDelimiter** *(string) --*

      The column delimiter. For example, in a CSV format, a comma (",") is the typical
      column delimiter.
    """


_ClientAddApplicationInputResponseInputDescriptionsInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef = TypedDict(
    "_ClientAddApplicationInputResponseInputDescriptionsInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef",
    {"RecordRowPath": str},
    total=False,
)


class ClientAddApplicationInputResponseInputDescriptionsInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef(
    _ClientAddApplicationInputResponseInputDescriptionsInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef
):
    """
    Type definition for `ClientAddApplicationInputResponseInputDescriptionsInputSchemaRecordFormatMappingParameters` `JSONMappingParameters`

    Provides additional mapping information when JSON is the record format on the
    streaming source.

    - **RecordRowPath** *(string) --*

      The path to the top-level parent that contains the records.
    """


_ClientAddApplicationInputResponseInputDescriptionsInputSchemaRecordFormatMappingParametersTypeDef = TypedDict(
    "_ClientAddApplicationInputResponseInputDescriptionsInputSchemaRecordFormatMappingParametersTypeDef",
    {
        "JSONMappingParameters": ClientAddApplicationInputResponseInputDescriptionsInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef,
        "CSVMappingParameters": ClientAddApplicationInputResponseInputDescriptionsInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef,
    },
    total=False,
)


class ClientAddApplicationInputResponseInputDescriptionsInputSchemaRecordFormatMappingParametersTypeDef(
    _ClientAddApplicationInputResponseInputDescriptionsInputSchemaRecordFormatMappingParametersTypeDef
):
    """
    Type definition for `ClientAddApplicationInputResponseInputDescriptionsInputSchemaRecordFormat` `MappingParameters`

    When you configure application input at the time of creating or updating an
    application, provides additional mapping information specific to the record format
    (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming
    source.

    - **JSONMappingParameters** *(dict) --*

      Provides additional mapping information when JSON is the record format on the
      streaming source.

      - **RecordRowPath** *(string) --*

        The path to the top-level parent that contains the records.

    - **CSVMappingParameters** *(dict) --*

      Provides additional mapping information when the record format uses delimiters (for
      example, CSV).

      - **RecordRowDelimiter** *(string) --*

        The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
        delimiter.

      - **RecordColumnDelimiter** *(string) --*

        The column delimiter. For example, in a CSV format, a comma (",") is the typical
        column delimiter.
    """


_ClientAddApplicationInputResponseInputDescriptionsInputSchemaRecordFormatTypeDef = TypedDict(
    "_ClientAddApplicationInputResponseInputDescriptionsInputSchemaRecordFormatTypeDef",
    {
        "RecordFormatType": str,
        "MappingParameters": ClientAddApplicationInputResponseInputDescriptionsInputSchemaRecordFormatMappingParametersTypeDef,
    },
    total=False,
)


class ClientAddApplicationInputResponseInputDescriptionsInputSchemaRecordFormatTypeDef(
    _ClientAddApplicationInputResponseInputDescriptionsInputSchemaRecordFormatTypeDef
):
    """
    Type definition for `ClientAddApplicationInputResponseInputDescriptionsInputSchema` `RecordFormat`

    Specifies the format of the records on the streaming source.

    - **RecordFormatType** *(string) --*

      The type of record format.

    - **MappingParameters** *(dict) --*

      When you configure application input at the time of creating or updating an
      application, provides additional mapping information specific to the record format
      (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming
      source.

      - **JSONMappingParameters** *(dict) --*

        Provides additional mapping information when JSON is the record format on the
        streaming source.

        - **RecordRowPath** *(string) --*

          The path to the top-level parent that contains the records.

      - **CSVMappingParameters** *(dict) --*

        Provides additional mapping information when the record format uses delimiters (for
        example, CSV).

        - **RecordRowDelimiter** *(string) --*

          The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
          delimiter.

        - **RecordColumnDelimiter** *(string) --*

          The column delimiter. For example, in a CSV format, a comma (",") is the typical
          column delimiter.
    """


_ClientAddApplicationInputResponseInputDescriptionsInputSchemaTypeDef = TypedDict(
    "_ClientAddApplicationInputResponseInputDescriptionsInputSchemaTypeDef",
    {
        "RecordFormat": ClientAddApplicationInputResponseInputDescriptionsInputSchemaRecordFormatTypeDef,
        "RecordEncoding": str,
        "RecordColumns": List[
            ClientAddApplicationInputResponseInputDescriptionsInputSchemaRecordColumnsTypeDef
        ],
    },
    total=False,
)


class ClientAddApplicationInputResponseInputDescriptionsInputSchemaTypeDef(
    _ClientAddApplicationInputResponseInputDescriptionsInputSchemaTypeDef
):
    """
    Type definition for `ClientAddApplicationInputResponseInputDescriptions` `InputSchema`

    Describes the format of the data in the streaming source, and how each data element maps
    to corresponding columns in the in-application stream that is being created.

    - **RecordFormat** *(dict) --*

      Specifies the format of the records on the streaming source.

      - **RecordFormatType** *(string) --*

        The type of record format.

      - **MappingParameters** *(dict) --*

        When you configure application input at the time of creating or updating an
        application, provides additional mapping information specific to the record format
        (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming
        source.

        - **JSONMappingParameters** *(dict) --*

          Provides additional mapping information when JSON is the record format on the
          streaming source.

          - **RecordRowPath** *(string) --*

            The path to the top-level parent that contains the records.

        - **CSVMappingParameters** *(dict) --*

          Provides additional mapping information when the record format uses delimiters (for
          example, CSV).

          - **RecordRowDelimiter** *(string) --*

            The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
            delimiter.

          - **RecordColumnDelimiter** *(string) --*

            The column delimiter. For example, in a CSV format, a comma (",") is the typical
            column delimiter.

    - **RecordEncoding** *(string) --*

      Specifies the encoding of the records in the streaming source. For example, UTF-8.

    - **RecordColumns** *(list) --*

      A list of ``RecordColumn`` objects.

      - *(dict) --*

        For an SQL-based Amazon Kinesis Data Analytics application, describes the mapping of
        each data element in the streaming source to the corresponding column in the
        in-application stream.

        Also used to describe the format of the reference data source.

        - **Name** *(string) --*

          The name of the column that is created in the in-application input stream or
          reference table.

        - **Mapping** *(string) --*

          A reference to the data element in the streaming input or the reference data source.

        - **SqlType** *(string) --*

          The type of column created in the in-application input stream or reference table.
    """


_ClientAddApplicationInputResponseInputDescriptionsInputStartingPositionConfigurationTypeDef = TypedDict(
    "_ClientAddApplicationInputResponseInputDescriptionsInputStartingPositionConfigurationTypeDef",
    {"InputStartingPosition": str},
    total=False,
)


class ClientAddApplicationInputResponseInputDescriptionsInputStartingPositionConfigurationTypeDef(
    _ClientAddApplicationInputResponseInputDescriptionsInputStartingPositionConfigurationTypeDef
):
    """
    Type definition for `ClientAddApplicationInputResponseInputDescriptions` `InputStartingPositionConfiguration`

    The point at which the application is configured to read from the input stream.

    - **InputStartingPosition** *(string) --*

      The starting position on the stream.

      * ``NOW`` - Start reading just after the most recent record in the stream, and start at
      the request timestamp that the customer issued.

      * ``TRIM_HORIZON`` - Start reading at the last untrimmed record in the stream, which is
      the oldest record available in the stream. This option is not available for an Amazon
      Kinesis Data Firehose delivery stream.

      * ``LAST_STOPPED_POINT`` - Resume reading from where the application last stopped
      reading.
    """


_ClientAddApplicationInputResponseInputDescriptionsKinesisFirehoseInputDescriptionTypeDef = TypedDict(
    "_ClientAddApplicationInputResponseInputDescriptionsKinesisFirehoseInputDescriptionTypeDef",
    {"ResourceARN": str, "RoleARN": str},
    total=False,
)


class ClientAddApplicationInputResponseInputDescriptionsKinesisFirehoseInputDescriptionTypeDef(
    _ClientAddApplicationInputResponseInputDescriptionsKinesisFirehoseInputDescriptionTypeDef
):
    """
    Type definition for `ClientAddApplicationInputResponseInputDescriptions` `KinesisFirehoseInputDescription`

    If a Kinesis Data Firehose delivery stream is configured as a streaming source, provides
    the delivery stream's ARN.

    - **ResourceARN** *(string) --*

      The Amazon Resource Name (ARN) of the delivery stream.

    - **RoleARN** *(string) --*

      The ARN of the IAM role that Kinesis Data Analytics assumes to access the stream.

      .. note::

        Provided for backward compatibility. Applications that are created with the current
        API version have an application-level service execution role rather than a
        resource-level role.
    """


_ClientAddApplicationInputResponseInputDescriptionsKinesisStreamsInputDescriptionTypeDef = TypedDict(
    "_ClientAddApplicationInputResponseInputDescriptionsKinesisStreamsInputDescriptionTypeDef",
    {"ResourceARN": str, "RoleARN": str},
    total=False,
)


class ClientAddApplicationInputResponseInputDescriptionsKinesisStreamsInputDescriptionTypeDef(
    _ClientAddApplicationInputResponseInputDescriptionsKinesisStreamsInputDescriptionTypeDef
):
    """
    Type definition for `ClientAddApplicationInputResponseInputDescriptions` `KinesisStreamsInputDescription`

    If a Kinesis data stream is configured as a streaming source, provides the Kinesis data
    stream's Amazon Resource Name (ARN).

    - **ResourceARN** *(string) --*

      The Amazon Resource Name (ARN) of the Kinesis data stream.

    - **RoleARN** *(string) --*

      The ARN of the IAM role that Kinesis Data Analytics can assume to access the stream.

      .. note::

        Provided for backward compatibility. Applications that are created with the current
        API version have an application-level service execution role rather than a
        resource-level role.
    """


_ClientAddApplicationInputResponseInputDescriptionsTypeDef = TypedDict(
    "_ClientAddApplicationInputResponseInputDescriptionsTypeDef",
    {
        "InputId": str,
        "NamePrefix": str,
        "InAppStreamNames": List[str],
        "InputProcessingConfigurationDescription": ClientAddApplicationInputResponseInputDescriptionsInputProcessingConfigurationDescriptionTypeDef,
        "KinesisStreamsInputDescription": ClientAddApplicationInputResponseInputDescriptionsKinesisStreamsInputDescriptionTypeDef,
        "KinesisFirehoseInputDescription": ClientAddApplicationInputResponseInputDescriptionsKinesisFirehoseInputDescriptionTypeDef,
        "InputSchema": ClientAddApplicationInputResponseInputDescriptionsInputSchemaTypeDef,
        "InputParallelism": ClientAddApplicationInputResponseInputDescriptionsInputParallelismTypeDef,
        "InputStartingPositionConfiguration": ClientAddApplicationInputResponseInputDescriptionsInputStartingPositionConfigurationTypeDef,
    },
    total=False,
)


class ClientAddApplicationInputResponseInputDescriptionsTypeDef(
    _ClientAddApplicationInputResponseInputDescriptionsTypeDef
):
    """
    Type definition for `ClientAddApplicationInputResponse` `InputDescriptions`

    Describes the application input configuration for an SQL-based Amazon Kinesis Data
    Analytics application.

    - **InputId** *(string) --*

      The input ID that is associated with the application input. This is the ID that Kinesis
      Data Analytics assigns to each input configuration that you add to your application.

    - **NamePrefix** *(string) --*

      The in-application name prefix.

    - **InAppStreamNames** *(list) --*

      Returns the in-application stream names that are mapped to the stream source.

      - *(string) --*

    - **InputProcessingConfigurationDescription** *(dict) --*

      The description of the preprocessor that executes on records in this input before the
      application's code is run.

      - **InputLambdaProcessorDescription** *(dict) --*

        Provides configuration information about the associated  InputLambdaProcessorDescription

        - **ResourceARN** *(string) --*

          The ARN of the AWS Lambda function that is used to preprocess the records in the
          stream.

          .. note::

            To specify an earlier version of the Lambda function than the latest, include the
            Lambda function version in the Lambda function ARN. For more information about
            Lambda ARNs, see `Example ARNs\\: AWS Lambda
            </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__

        - **RoleARN** *(string) --*

          The ARN of the IAM role that is used to access the AWS Lambda function.

          .. note::

            Provided for backward compatibility. Applications that are created with the current
            API version have an application-level service execution role rather than a
            resource-level role.

    - **KinesisStreamsInputDescription** *(dict) --*

      If a Kinesis data stream is configured as a streaming source, provides the Kinesis data
      stream's Amazon Resource Name (ARN).

      - **ResourceARN** *(string) --*

        The Amazon Resource Name (ARN) of the Kinesis data stream.

      - **RoleARN** *(string) --*

        The ARN of the IAM role that Kinesis Data Analytics can assume to access the stream.

        .. note::

          Provided for backward compatibility. Applications that are created with the current
          API version have an application-level service execution role rather than a
          resource-level role.

    - **KinesisFirehoseInputDescription** *(dict) --*

      If a Kinesis Data Firehose delivery stream is configured as a streaming source, provides
      the delivery stream's ARN.

      - **ResourceARN** *(string) --*

        The Amazon Resource Name (ARN) of the delivery stream.

      - **RoleARN** *(string) --*

        The ARN of the IAM role that Kinesis Data Analytics assumes to access the stream.

        .. note::

          Provided for backward compatibility. Applications that are created with the current
          API version have an application-level service execution role rather than a
          resource-level role.

    - **InputSchema** *(dict) --*

      Describes the format of the data in the streaming source, and how each data element maps
      to corresponding columns in the in-application stream that is being created.

      - **RecordFormat** *(dict) --*

        Specifies the format of the records on the streaming source.

        - **RecordFormatType** *(string) --*

          The type of record format.

        - **MappingParameters** *(dict) --*

          When you configure application input at the time of creating or updating an
          application, provides additional mapping information specific to the record format
          (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming
          source.

          - **JSONMappingParameters** *(dict) --*

            Provides additional mapping information when JSON is the record format on the
            streaming source.

            - **RecordRowPath** *(string) --*

              The path to the top-level parent that contains the records.

          - **CSVMappingParameters** *(dict) --*

            Provides additional mapping information when the record format uses delimiters (for
            example, CSV).

            - **RecordRowDelimiter** *(string) --*

              The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
              delimiter.

            - **RecordColumnDelimiter** *(string) --*

              The column delimiter. For example, in a CSV format, a comma (",") is the typical
              column delimiter.

      - **RecordEncoding** *(string) --*

        Specifies the encoding of the records in the streaming source. For example, UTF-8.

      - **RecordColumns** *(list) --*

        A list of ``RecordColumn`` objects.

        - *(dict) --*

          For an SQL-based Amazon Kinesis Data Analytics application, describes the mapping of
          each data element in the streaming source to the corresponding column in the
          in-application stream.

          Also used to describe the format of the reference data source.

          - **Name** *(string) --*

            The name of the column that is created in the in-application input stream or
            reference table.

          - **Mapping** *(string) --*

            A reference to the data element in the streaming input or the reference data source.

          - **SqlType** *(string) --*

            The type of column created in the in-application input stream or reference table.

    - **InputParallelism** *(dict) --*

      Describes the configured parallelism (number of in-application streams mapped to the
      streaming source).

      - **Count** *(integer) --*

        The number of in-application streams to create.

    - **InputStartingPositionConfiguration** *(dict) --*

      The point at which the application is configured to read from the input stream.

      - **InputStartingPosition** *(string) --*

        The starting position on the stream.

        * ``NOW`` - Start reading just after the most recent record in the stream, and start at
        the request timestamp that the customer issued.

        * ``TRIM_HORIZON`` - Start reading at the last untrimmed record in the stream, which is
        the oldest record available in the stream. This option is not available for an Amazon
        Kinesis Data Firehose delivery stream.

        * ``LAST_STOPPED_POINT`` - Resume reading from where the application last stopped
        reading.
    """


_ClientAddApplicationInputResponseTypeDef = TypedDict(
    "_ClientAddApplicationInputResponseTypeDef",
    {
        "ApplicationARN": str,
        "ApplicationVersionId": int,
        "InputDescriptions": List[
            ClientAddApplicationInputResponseInputDescriptionsTypeDef
        ],
    },
    total=False,
)


class ClientAddApplicationInputResponseTypeDef(
    _ClientAddApplicationInputResponseTypeDef
):
    """
    Type definition for `ClientAddApplicationInput` `Response`

    - **ApplicationARN** *(string) --*

      The Amazon Resource Name (ARN) of the application.

    - **ApplicationVersionId** *(integer) --*

      Provides the current application version.

    - **InputDescriptions** *(list) --*

      Describes the application input configuration.

      - *(dict) --*

        Describes the application input configuration for an SQL-based Amazon Kinesis Data
        Analytics application.

        - **InputId** *(string) --*

          The input ID that is associated with the application input. This is the ID that Kinesis
          Data Analytics assigns to each input configuration that you add to your application.

        - **NamePrefix** *(string) --*

          The in-application name prefix.

        - **InAppStreamNames** *(list) --*

          Returns the in-application stream names that are mapped to the stream source.

          - *(string) --*

        - **InputProcessingConfigurationDescription** *(dict) --*

          The description of the preprocessor that executes on records in this input before the
          application's code is run.

          - **InputLambdaProcessorDescription** *(dict) --*

            Provides configuration information about the associated  InputLambdaProcessorDescription

            - **ResourceARN** *(string) --*

              The ARN of the AWS Lambda function that is used to preprocess the records in the
              stream.

              .. note::

                To specify an earlier version of the Lambda function than the latest, include the
                Lambda function version in the Lambda function ARN. For more information about
                Lambda ARNs, see `Example ARNs\\: AWS Lambda
                </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__

            - **RoleARN** *(string) --*

              The ARN of the IAM role that is used to access the AWS Lambda function.

              .. note::

                Provided for backward compatibility. Applications that are created with the current
                API version have an application-level service execution role rather than a
                resource-level role.

        - **KinesisStreamsInputDescription** *(dict) --*

          If a Kinesis data stream is configured as a streaming source, provides the Kinesis data
          stream's Amazon Resource Name (ARN).

          - **ResourceARN** *(string) --*

            The Amazon Resource Name (ARN) of the Kinesis data stream.

          - **RoleARN** *(string) --*

            The ARN of the IAM role that Kinesis Data Analytics can assume to access the stream.

            .. note::

              Provided for backward compatibility. Applications that are created with the current
              API version have an application-level service execution role rather than a
              resource-level role.

        - **KinesisFirehoseInputDescription** *(dict) --*

          If a Kinesis Data Firehose delivery stream is configured as a streaming source, provides
          the delivery stream's ARN.

          - **ResourceARN** *(string) --*

            The Amazon Resource Name (ARN) of the delivery stream.

          - **RoleARN** *(string) --*

            The ARN of the IAM role that Kinesis Data Analytics assumes to access the stream.

            .. note::

              Provided for backward compatibility. Applications that are created with the current
              API version have an application-level service execution role rather than a
              resource-level role.

        - **InputSchema** *(dict) --*

          Describes the format of the data in the streaming source, and how each data element maps
          to corresponding columns in the in-application stream that is being created.

          - **RecordFormat** *(dict) --*

            Specifies the format of the records on the streaming source.

            - **RecordFormatType** *(string) --*

              The type of record format.

            - **MappingParameters** *(dict) --*

              When you configure application input at the time of creating or updating an
              application, provides additional mapping information specific to the record format
              (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming
              source.

              - **JSONMappingParameters** *(dict) --*

                Provides additional mapping information when JSON is the record format on the
                streaming source.

                - **RecordRowPath** *(string) --*

                  The path to the top-level parent that contains the records.

              - **CSVMappingParameters** *(dict) --*

                Provides additional mapping information when the record format uses delimiters (for
                example, CSV).

                - **RecordRowDelimiter** *(string) --*

                  The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
                  delimiter.

                - **RecordColumnDelimiter** *(string) --*

                  The column delimiter. For example, in a CSV format, a comma (",") is the typical
                  column delimiter.

          - **RecordEncoding** *(string) --*

            Specifies the encoding of the records in the streaming source. For example, UTF-8.

          - **RecordColumns** *(list) --*

            A list of ``RecordColumn`` objects.

            - *(dict) --*

              For an SQL-based Amazon Kinesis Data Analytics application, describes the mapping of
              each data element in the streaming source to the corresponding column in the
              in-application stream.

              Also used to describe the format of the reference data source.

              - **Name** *(string) --*

                The name of the column that is created in the in-application input stream or
                reference table.

              - **Mapping** *(string) --*

                A reference to the data element in the streaming input or the reference data source.

              - **SqlType** *(string) --*

                The type of column created in the in-application input stream or reference table.

        - **InputParallelism** *(dict) --*

          Describes the configured parallelism (number of in-application streams mapped to the
          streaming source).

          - **Count** *(integer) --*

            The number of in-application streams to create.

        - **InputStartingPositionConfiguration** *(dict) --*

          The point at which the application is configured to read from the input stream.

          - **InputStartingPosition** *(string) --*

            The starting position on the stream.

            * ``NOW`` - Start reading just after the most recent record in the stream, and start at
            the request timestamp that the customer issued.

            * ``TRIM_HORIZON`` - Start reading at the last untrimmed record in the stream, which is
            the oldest record available in the stream. This option is not available for an Amazon
            Kinesis Data Firehose delivery stream.

            * ``LAST_STOPPED_POINT`` - Resume reading from where the application last stopped
            reading.
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

    Describes the data format when records are written to the destination.

    - **RecordFormatType** *(string) --* **[REQUIRED]**

      Specifies the format of the records on the output stream.
    """


_ClientAddApplicationOutputOutputKinesisFirehoseOutputTypeDef = TypedDict(
    "_ClientAddApplicationOutputOutputKinesisFirehoseOutputTypeDef",
    {"ResourceARN": str},
)


class ClientAddApplicationOutputOutputKinesisFirehoseOutputTypeDef(
    _ClientAddApplicationOutputOutputKinesisFirehoseOutputTypeDef
):
    """
    Type definition for `ClientAddApplicationOutputOutput` `KinesisFirehoseOutput`

    Identifies an Amazon Kinesis Data Firehose delivery stream as the destination.

    - **ResourceARN** *(string) --* **[REQUIRED]**

      The ARN of the destination delivery stream to write to.
    """


_ClientAddApplicationOutputOutputKinesisStreamsOutputTypeDef = TypedDict(
    "_ClientAddApplicationOutputOutputKinesisStreamsOutputTypeDef", {"ResourceARN": str}
)


class ClientAddApplicationOutputOutputKinesisStreamsOutputTypeDef(
    _ClientAddApplicationOutputOutputKinesisStreamsOutputTypeDef
):
    """
    Type definition for `ClientAddApplicationOutputOutput` `KinesisStreamsOutput`

    Identifies an Amazon Kinesis data stream as the destination.

    - **ResourceARN** *(string) --* **[REQUIRED]**

      The ARN of the destination Kinesis data stream to write to.
    """


_ClientAddApplicationOutputOutputLambdaOutputTypeDef = TypedDict(
    "_ClientAddApplicationOutputOutputLambdaOutputTypeDef", {"ResourceARN": str}
)


class ClientAddApplicationOutputOutputLambdaOutputTypeDef(
    _ClientAddApplicationOutputOutputLambdaOutputTypeDef
):
    """
    Type definition for `ClientAddApplicationOutputOutput` `LambdaOutput`

    Identifies an AWS Lambda function as the destination.

    - **ResourceARN** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the destination Lambda function to write to.

      .. note::

        To specify an earlier version of the Lambda function than the latest, include the Lambda
        function version in the Lambda function ARN. For more information about Lambda ARNs, see
        `Example ARNs\\: AWS Lambda
        </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__
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
    specify the name of an in-application stream, a destination (that is, a Kinesis data stream, a
    Kinesis Data Firehose delivery stream, or an AWS Lambda function), and record the formation to
    use when writing to the destination.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the in-application stream.

    - **KinesisStreamsOutput** *(dict) --*

      Identifies an Amazon Kinesis data stream as the destination.

      - **ResourceARN** *(string) --* **[REQUIRED]**

        The ARN of the destination Kinesis data stream to write to.

    - **KinesisFirehoseOutput** *(dict) --*

      Identifies an Amazon Kinesis Data Firehose delivery stream as the destination.

      - **ResourceARN** *(string) --* **[REQUIRED]**

        The ARN of the destination delivery stream to write to.

    - **LambdaOutput** *(dict) --*

      Identifies an AWS Lambda function as the destination.

      - **ResourceARN** *(string) --* **[REQUIRED]**

        The Amazon Resource Name (ARN) of the destination Lambda function to write to.

        .. note::

          To specify an earlier version of the Lambda function than the latest, include the Lambda
          function version in the Lambda function ARN. For more information about Lambda ARNs, see
          `Example ARNs\\: AWS Lambda
          </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__

    - **DestinationSchema** *(dict) --* **[REQUIRED]**

      Describes the data format when records are written to the destination.

      - **RecordFormatType** *(string) --* **[REQUIRED]**

        Specifies the format of the records on the output stream.
    """


_ClientAddApplicationOutputResponseOutputDescriptionsDestinationSchemaTypeDef = TypedDict(
    "_ClientAddApplicationOutputResponseOutputDescriptionsDestinationSchemaTypeDef",
    {"RecordFormatType": str},
    total=False,
)


class ClientAddApplicationOutputResponseOutputDescriptionsDestinationSchemaTypeDef(
    _ClientAddApplicationOutputResponseOutputDescriptionsDestinationSchemaTypeDef
):
    """
    Type definition for `ClientAddApplicationOutputResponseOutputDescriptions` `DestinationSchema`

    The data format used for writing data to the destination.

    - **RecordFormatType** *(string) --*

      Specifies the format of the records on the output stream.
    """


_ClientAddApplicationOutputResponseOutputDescriptionsKinesisFirehoseOutputDescriptionTypeDef = TypedDict(
    "_ClientAddApplicationOutputResponseOutputDescriptionsKinesisFirehoseOutputDescriptionTypeDef",
    {"ResourceARN": str, "RoleARN": str},
    total=False,
)


class ClientAddApplicationOutputResponseOutputDescriptionsKinesisFirehoseOutputDescriptionTypeDef(
    _ClientAddApplicationOutputResponseOutputDescriptionsKinesisFirehoseOutputDescriptionTypeDef
):
    """
    Type definition for `ClientAddApplicationOutputResponseOutputDescriptions` `KinesisFirehoseOutputDescription`

    Describes the Kinesis Data Firehose delivery stream that is configured as the destination
    where output is written.

    - **ResourceARN** *(string) --*

      The Amazon Resource Name (ARN) of the delivery stream.

    - **RoleARN** *(string) --*

      The ARN of the IAM role that Kinesis Data Analytics can assume to access the stream.

      .. note::

        Provided for backward compatibility. Applications that are created with the current
        API version have an application-level service execution role rather than a
        resource-level role.
    """


_ClientAddApplicationOutputResponseOutputDescriptionsKinesisStreamsOutputDescriptionTypeDef = TypedDict(
    "_ClientAddApplicationOutputResponseOutputDescriptionsKinesisStreamsOutputDescriptionTypeDef",
    {"ResourceARN": str, "RoleARN": str},
    total=False,
)


class ClientAddApplicationOutputResponseOutputDescriptionsKinesisStreamsOutputDescriptionTypeDef(
    _ClientAddApplicationOutputResponseOutputDescriptionsKinesisStreamsOutputDescriptionTypeDef
):
    """
    Type definition for `ClientAddApplicationOutputResponseOutputDescriptions` `KinesisStreamsOutputDescription`

    Describes the Kinesis data stream that is configured as the destination where output is
    written.

    - **ResourceARN** *(string) --*

      The Amazon Resource Name (ARN) of the Kinesis data stream.

    - **RoleARN** *(string) --*

      The ARN of the IAM role that Kinesis Data Analytics can assume to access the stream.

      .. note::

        Provided for backward compatibility. Applications that are created with the current
        API version have an application-level service execution role rather than a
        resource-level role.
    """


_ClientAddApplicationOutputResponseOutputDescriptionsLambdaOutputDescriptionTypeDef = TypedDict(
    "_ClientAddApplicationOutputResponseOutputDescriptionsLambdaOutputDescriptionTypeDef",
    {"ResourceARN": str, "RoleARN": str},
    total=False,
)


class ClientAddApplicationOutputResponseOutputDescriptionsLambdaOutputDescriptionTypeDef(
    _ClientAddApplicationOutputResponseOutputDescriptionsLambdaOutputDescriptionTypeDef
):
    """
    Type definition for `ClientAddApplicationOutputResponseOutputDescriptions` `LambdaOutputDescription`

    Describes the Lambda function that is configured as the destination where output is
    written.

    - **ResourceARN** *(string) --*

      The Amazon Resource Name (ARN) of the destination Lambda function.

    - **RoleARN** *(string) --*

      The ARN of the IAM role that Kinesis Data Analytics can assume to write to the
      destination function.

      .. note::

        Provided for backward compatibility. Applications that are created with the current
        API version have an application-level service execution role rather than a
        resource-level role.
    """


_ClientAddApplicationOutputResponseOutputDescriptionsTypeDef = TypedDict(
    "_ClientAddApplicationOutputResponseOutputDescriptionsTypeDef",
    {
        "OutputId": str,
        "Name": str,
        "KinesisStreamsOutputDescription": ClientAddApplicationOutputResponseOutputDescriptionsKinesisStreamsOutputDescriptionTypeDef,
        "KinesisFirehoseOutputDescription": ClientAddApplicationOutputResponseOutputDescriptionsKinesisFirehoseOutputDescriptionTypeDef,
        "LambdaOutputDescription": ClientAddApplicationOutputResponseOutputDescriptionsLambdaOutputDescriptionTypeDef,
        "DestinationSchema": ClientAddApplicationOutputResponseOutputDescriptionsDestinationSchemaTypeDef,
    },
    total=False,
)


class ClientAddApplicationOutputResponseOutputDescriptionsTypeDef(
    _ClientAddApplicationOutputResponseOutputDescriptionsTypeDef
):
    """
    Type definition for `ClientAddApplicationOutputResponse` `OutputDescriptions`

    For an SQL-based Amazon Kinesis Data Analytics application, describes the application
    output configuration, which includes the in-application stream name and the destination
    where the stream data is written. The destination can be a Kinesis data stream or a Kinesis
    Data Firehose delivery stream.

    - **OutputId** *(string) --*

      A unique identifier for the output configuration.

    - **Name** *(string) --*

      The name of the in-application stream that is configured as output.

    - **KinesisStreamsOutputDescription** *(dict) --*

      Describes the Kinesis data stream that is configured as the destination where output is
      written.

      - **ResourceARN** *(string) --*

        The Amazon Resource Name (ARN) of the Kinesis data stream.

      - **RoleARN** *(string) --*

        The ARN of the IAM role that Kinesis Data Analytics can assume to access the stream.

        .. note::

          Provided for backward compatibility. Applications that are created with the current
          API version have an application-level service execution role rather than a
          resource-level role.

    - **KinesisFirehoseOutputDescription** *(dict) --*

      Describes the Kinesis Data Firehose delivery stream that is configured as the destination
      where output is written.

      - **ResourceARN** *(string) --*

        The Amazon Resource Name (ARN) of the delivery stream.

      - **RoleARN** *(string) --*

        The ARN of the IAM role that Kinesis Data Analytics can assume to access the stream.

        .. note::

          Provided for backward compatibility. Applications that are created with the current
          API version have an application-level service execution role rather than a
          resource-level role.

    - **LambdaOutputDescription** *(dict) --*

      Describes the Lambda function that is configured as the destination where output is
      written.

      - **ResourceARN** *(string) --*

        The Amazon Resource Name (ARN) of the destination Lambda function.

      - **RoleARN** *(string) --*

        The ARN of the IAM role that Kinesis Data Analytics can assume to write to the
        destination function.

        .. note::

          Provided for backward compatibility. Applications that are created with the current
          API version have an application-level service execution role rather than a
          resource-level role.

    - **DestinationSchema** *(dict) --*

      The data format used for writing data to the destination.

      - **RecordFormatType** *(string) --*

        Specifies the format of the records on the output stream.
    """


_ClientAddApplicationOutputResponseTypeDef = TypedDict(
    "_ClientAddApplicationOutputResponseTypeDef",
    {
        "ApplicationARN": str,
        "ApplicationVersionId": int,
        "OutputDescriptions": List[
            ClientAddApplicationOutputResponseOutputDescriptionsTypeDef
        ],
    },
    total=False,
)


class ClientAddApplicationOutputResponseTypeDef(
    _ClientAddApplicationOutputResponseTypeDef
):
    """
    Type definition for `ClientAddApplicationOutput` `Response`

    - **ApplicationARN** *(string) --*

      The application Amazon Resource Name (ARN).

    - **ApplicationVersionId** *(integer) --*

      The updated application version ID. Kinesis Data Analytics increments this ID when the
      application is updated.

    - **OutputDescriptions** *(list) --*

      Describes the application output configuration. For more information, see `Configuring
      Application Output
      <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-output.html>`__ .

      - *(dict) --*

        For an SQL-based Amazon Kinesis Data Analytics application, describes the application
        output configuration, which includes the in-application stream name and the destination
        where the stream data is written. The destination can be a Kinesis data stream or a Kinesis
        Data Firehose delivery stream.

        - **OutputId** *(string) --*

          A unique identifier for the output configuration.

        - **Name** *(string) --*

          The name of the in-application stream that is configured as output.

        - **KinesisStreamsOutputDescription** *(dict) --*

          Describes the Kinesis data stream that is configured as the destination where output is
          written.

          - **ResourceARN** *(string) --*

            The Amazon Resource Name (ARN) of the Kinesis data stream.

          - **RoleARN** *(string) --*

            The ARN of the IAM role that Kinesis Data Analytics can assume to access the stream.

            .. note::

              Provided for backward compatibility. Applications that are created with the current
              API version have an application-level service execution role rather than a
              resource-level role.

        - **KinesisFirehoseOutputDescription** *(dict) --*

          Describes the Kinesis Data Firehose delivery stream that is configured as the destination
          where output is written.

          - **ResourceARN** *(string) --*

            The Amazon Resource Name (ARN) of the delivery stream.

          - **RoleARN** *(string) --*

            The ARN of the IAM role that Kinesis Data Analytics can assume to access the stream.

            .. note::

              Provided for backward compatibility. Applications that are created with the current
              API version have an application-level service execution role rather than a
              resource-level role.

        - **LambdaOutputDescription** *(dict) --*

          Describes the Lambda function that is configured as the destination where output is
          written.

          - **ResourceARN** *(string) --*

            The Amazon Resource Name (ARN) of the destination Lambda function.

          - **RoleARN** *(string) --*

            The ARN of the IAM role that Kinesis Data Analytics can assume to write to the
            destination function.

            .. note::

              Provided for backward compatibility. Applications that are created with the current
              API version have an application-level service execution role rather than a
              resource-level role.

        - **DestinationSchema** *(dict) --*

          The data format used for writing data to the destination.

          - **RecordFormatType** *(string) --*

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

    For an SQL-based Amazon Kinesis Data Analytics application, describes the mapping of each
    data element in the streaming source to the corresponding column in the in-application
    stream.

    Also used to describe the format of the reference data source.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the column that is created in the in-application input stream or reference
      table.

    - **Mapping** *(string) --*

      A reference to the data element in the streaming input or the reference data source.

    - **SqlType** *(string) --* **[REQUIRED]**

      The type of column created in the in-application input stream or reference table.
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

      The row delimiter. For example, in a CSV format, *'\\n'* is the typical row delimiter.

    - **RecordColumnDelimiter** *(string) --* **[REQUIRED]**

      The column delimiter. For example, in a CSV format, a comma (",") is the typical column
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

      The path to the top-level parent that contains the records.
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

    When you configure application input at the time of creating or updating an application,
    provides additional mapping information specific to the record format (such as JSON, CSV,
    or record fields delimited by some delimiter) on the streaming source.

    - **JSONMappingParameters** *(dict) --*

      Provides additional mapping information when JSON is the record format on the streaming
      source.

      - **RecordRowPath** *(string) --* **[REQUIRED]**

        The path to the top-level parent that contains the records.

    - **CSVMappingParameters** *(dict) --*

      Provides additional mapping information when the record format uses delimiters (for
      example, CSV).

      - **RecordRowDelimiter** *(string) --* **[REQUIRED]**

        The row delimiter. For example, in a CSV format, *'\\n'* is the typical row delimiter.

      - **RecordColumnDelimiter** *(string) --* **[REQUIRED]**

        The column delimiter. For example, in a CSV format, a comma (",") is the typical column
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

      When you configure application input at the time of creating or updating an application,
      provides additional mapping information specific to the record format (such as JSON, CSV,
      or record fields delimited by some delimiter) on the streaming source.

      - **JSONMappingParameters** *(dict) --*

        Provides additional mapping information when JSON is the record format on the streaming
        source.

        - **RecordRowPath** *(string) --* **[REQUIRED]**

          The path to the top-level parent that contains the records.

      - **CSVMappingParameters** *(dict) --*

        Provides additional mapping information when the record format uses delimiters (for
        example, CSV).

        - **RecordRowDelimiter** *(string) --* **[REQUIRED]**

          The row delimiter. For example, in a CSV format, *'\\n'* is the typical row delimiter.

        - **RecordColumnDelimiter** *(string) --* **[REQUIRED]**

          The column delimiter. For example, in a CSV format, a comma (",") is the typical column
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

        When you configure application input at the time of creating or updating an application,
        provides additional mapping information specific to the record format (such as JSON, CSV,
        or record fields delimited by some delimiter) on the streaming source.

        - **JSONMappingParameters** *(dict) --*

          Provides additional mapping information when JSON is the record format on the streaming
          source.

          - **RecordRowPath** *(string) --* **[REQUIRED]**

            The path to the top-level parent that contains the records.

        - **CSVMappingParameters** *(dict) --*

          Provides additional mapping information when the record format uses delimiters (for
          example, CSV).

          - **RecordRowDelimiter** *(string) --* **[REQUIRED]**

            The row delimiter. For example, in a CSV format, *'\\n'* is the typical row delimiter.

          - **RecordColumnDelimiter** *(string) --* **[REQUIRED]**

            The column delimiter. For example, in a CSV format, a comma (",") is the typical column
            delimiter.

    - **RecordEncoding** *(string) --*

      Specifies the encoding of the records in the streaming source. For example, UTF-8.

    - **RecordColumns** *(list) --* **[REQUIRED]**

      A list of ``RecordColumn`` objects.

      - *(dict) --*

        For an SQL-based Amazon Kinesis Data Analytics application, describes the mapping of each
        data element in the streaming source to the corresponding column in the in-application
        stream.

        Also used to describe the format of the reference data source.

        - **Name** *(string) --* **[REQUIRED]**

          The name of the column that is created in the in-application input stream or reference
          table.

        - **Mapping** *(string) --*

          A reference to the data element in the streaming input or the reference data source.

        - **SqlType** *(string) --* **[REQUIRED]**

          The type of column created in the in-application input stream or reference table.
    """


_ClientAddApplicationReferenceDataSourceReferenceDataSourceS3ReferenceDataSourceTypeDef = TypedDict(
    "_ClientAddApplicationReferenceDataSourceReferenceDataSourceS3ReferenceDataSourceTypeDef",
    {"BucketARN": str, "FileKey": str},
    total=False,
)


class ClientAddApplicationReferenceDataSourceReferenceDataSourceS3ReferenceDataSourceTypeDef(
    _ClientAddApplicationReferenceDataSourceReferenceDataSourceS3ReferenceDataSourceTypeDef
):
    """
    Type definition for `ClientAddApplicationReferenceDataSourceReferenceDataSource` `S3ReferenceDataSource`

    Identifies the S3 bucket and object that contains the reference data. A Kinesis Data Analytics
    application loads reference data only once. If the data changes, you call the
    UpdateApplication operation to trigger reloading of data into your application.

    - **BucketARN** *(string) --*

      The Amazon Resource Name (ARN) of the S3 bucket.

    - **FileKey** *(string) --*

      The object key name containing the reference data.
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

    The reference data source can be an object in your Amazon S3 bucket. Kinesis Data Analytics reads
    the object and copies the data into the in-application table that is created. You provide an S3
    bucket, object key name, and the resulting in-application table that is created.

    - **TableName** *(string) --* **[REQUIRED]**

      The name of the in-application table to create.

    - **S3ReferenceDataSource** *(dict) --*

      Identifies the S3 bucket and object that contains the reference data. A Kinesis Data Analytics
      application loads reference data only once. If the data changes, you call the
      UpdateApplication operation to trigger reloading of data into your application.

      - **BucketARN** *(string) --*

        The Amazon Resource Name (ARN) of the S3 bucket.

      - **FileKey** *(string) --*

        The object key name containing the reference data.

    - **ReferenceSchema** *(dict) --* **[REQUIRED]**

      Describes the format of the data in the streaming source, and how each data element maps to
      corresponding columns created in the in-application stream.

      - **RecordFormat** *(dict) --* **[REQUIRED]**

        Specifies the format of the records on the streaming source.

        - **RecordFormatType** *(string) --* **[REQUIRED]**

          The type of record format.

        - **MappingParameters** *(dict) --*

          When you configure application input at the time of creating or updating an application,
          provides additional mapping information specific to the record format (such as JSON, CSV,
          or record fields delimited by some delimiter) on the streaming source.

          - **JSONMappingParameters** *(dict) --*

            Provides additional mapping information when JSON is the record format on the streaming
            source.

            - **RecordRowPath** *(string) --* **[REQUIRED]**

              The path to the top-level parent that contains the records.

          - **CSVMappingParameters** *(dict) --*

            Provides additional mapping information when the record format uses delimiters (for
            example, CSV).

            - **RecordRowDelimiter** *(string) --* **[REQUIRED]**

              The row delimiter. For example, in a CSV format, *'\\n'* is the typical row delimiter.

            - **RecordColumnDelimiter** *(string) --* **[REQUIRED]**

              The column delimiter. For example, in a CSV format, a comma (",") is the typical column
              delimiter.

      - **RecordEncoding** *(string) --*

        Specifies the encoding of the records in the streaming source. For example, UTF-8.

      - **RecordColumns** *(list) --* **[REQUIRED]**

        A list of ``RecordColumn`` objects.

        - *(dict) --*

          For an SQL-based Amazon Kinesis Data Analytics application, describes the mapping of each
          data element in the streaming source to the corresponding column in the in-application
          stream.

          Also used to describe the format of the reference data source.

          - **Name** *(string) --* **[REQUIRED]**

            The name of the column that is created in the in-application input stream or reference
            table.

          - **Mapping** *(string) --*

            A reference to the data element in the streaming input or the reference data source.

          - **SqlType** *(string) --* **[REQUIRED]**

            The type of column created in the in-application input stream or reference table.
    """


_ClientAddApplicationReferenceDataSourceResponseReferenceDataSourceDescriptionsReferenceSchemaRecordColumnsTypeDef = TypedDict(
    "_ClientAddApplicationReferenceDataSourceResponseReferenceDataSourceDescriptionsReferenceSchemaRecordColumnsTypeDef",
    {"Name": str, "Mapping": str, "SqlType": str},
    total=False,
)


class ClientAddApplicationReferenceDataSourceResponseReferenceDataSourceDescriptionsReferenceSchemaRecordColumnsTypeDef(
    _ClientAddApplicationReferenceDataSourceResponseReferenceDataSourceDescriptionsReferenceSchemaRecordColumnsTypeDef
):
    """
    Type definition for `ClientAddApplicationReferenceDataSourceResponseReferenceDataSourceDescriptionsReferenceSchema` `RecordColumns`

    For an SQL-based Amazon Kinesis Data Analytics application, describes the mapping of
    each data element in the streaming source to the corresponding column in the
    in-application stream.

    Also used to describe the format of the reference data source.

    - **Name** *(string) --*

      The name of the column that is created in the in-application input stream or
      reference table.

    - **Mapping** *(string) --*

      A reference to the data element in the streaming input or the reference data source.

    - **SqlType** *(string) --*

      The type of column created in the in-application input stream or reference table.
    """


_ClientAddApplicationReferenceDataSourceResponseReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef = TypedDict(
    "_ClientAddApplicationReferenceDataSourceResponseReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef",
    {"RecordRowDelimiter": str, "RecordColumnDelimiter": str},
    total=False,
)


class ClientAddApplicationReferenceDataSourceResponseReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef(
    _ClientAddApplicationReferenceDataSourceResponseReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef
):
    """
    Type definition for `ClientAddApplicationReferenceDataSourceResponseReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParameters` `CSVMappingParameters`

    Provides additional mapping information when the record format uses delimiters (for
    example, CSV).

    - **RecordRowDelimiter** *(string) --*

      The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
      delimiter.

    - **RecordColumnDelimiter** *(string) --*

      The column delimiter. For example, in a CSV format, a comma (",") is the typical
      column delimiter.
    """


_ClientAddApplicationReferenceDataSourceResponseReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef = TypedDict(
    "_ClientAddApplicationReferenceDataSourceResponseReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef",
    {"RecordRowPath": str},
    total=False,
)


class ClientAddApplicationReferenceDataSourceResponseReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef(
    _ClientAddApplicationReferenceDataSourceResponseReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef
):
    """
    Type definition for `ClientAddApplicationReferenceDataSourceResponseReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParameters` `JSONMappingParameters`

    Provides additional mapping information when JSON is the record format on the
    streaming source.

    - **RecordRowPath** *(string) --*

      The path to the top-level parent that contains the records.
    """


_ClientAddApplicationReferenceDataSourceResponseReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersTypeDef = TypedDict(
    "_ClientAddApplicationReferenceDataSourceResponseReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersTypeDef",
    {
        "JSONMappingParameters": ClientAddApplicationReferenceDataSourceResponseReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef,
        "CSVMappingParameters": ClientAddApplicationReferenceDataSourceResponseReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef,
    },
    total=False,
)


class ClientAddApplicationReferenceDataSourceResponseReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersTypeDef(
    _ClientAddApplicationReferenceDataSourceResponseReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersTypeDef
):
    """
    Type definition for `ClientAddApplicationReferenceDataSourceResponseReferenceDataSourceDescriptionsReferenceSchemaRecordFormat` `MappingParameters`

    When you configure application input at the time of creating or updating an
    application, provides additional mapping information specific to the record format
    (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming
    source.

    - **JSONMappingParameters** *(dict) --*

      Provides additional mapping information when JSON is the record format on the
      streaming source.

      - **RecordRowPath** *(string) --*

        The path to the top-level parent that contains the records.

    - **CSVMappingParameters** *(dict) --*

      Provides additional mapping information when the record format uses delimiters (for
      example, CSV).

      - **RecordRowDelimiter** *(string) --*

        The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
        delimiter.

      - **RecordColumnDelimiter** *(string) --*

        The column delimiter. For example, in a CSV format, a comma (",") is the typical
        column delimiter.
    """


_ClientAddApplicationReferenceDataSourceResponseReferenceDataSourceDescriptionsReferenceSchemaRecordFormatTypeDef = TypedDict(
    "_ClientAddApplicationReferenceDataSourceResponseReferenceDataSourceDescriptionsReferenceSchemaRecordFormatTypeDef",
    {
        "RecordFormatType": str,
        "MappingParameters": ClientAddApplicationReferenceDataSourceResponseReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersTypeDef,
    },
    total=False,
)


class ClientAddApplicationReferenceDataSourceResponseReferenceDataSourceDescriptionsReferenceSchemaRecordFormatTypeDef(
    _ClientAddApplicationReferenceDataSourceResponseReferenceDataSourceDescriptionsReferenceSchemaRecordFormatTypeDef
):
    """
    Type definition for `ClientAddApplicationReferenceDataSourceResponseReferenceDataSourceDescriptionsReferenceSchema` `RecordFormat`

    Specifies the format of the records on the streaming source.

    - **RecordFormatType** *(string) --*

      The type of record format.

    - **MappingParameters** *(dict) --*

      When you configure application input at the time of creating or updating an
      application, provides additional mapping information specific to the record format
      (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming
      source.

      - **JSONMappingParameters** *(dict) --*

        Provides additional mapping information when JSON is the record format on the
        streaming source.

        - **RecordRowPath** *(string) --*

          The path to the top-level parent that contains the records.

      - **CSVMappingParameters** *(dict) --*

        Provides additional mapping information when the record format uses delimiters (for
        example, CSV).

        - **RecordRowDelimiter** *(string) --*

          The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
          delimiter.

        - **RecordColumnDelimiter** *(string) --*

          The column delimiter. For example, in a CSV format, a comma (",") is the typical
          column delimiter.
    """


_ClientAddApplicationReferenceDataSourceResponseReferenceDataSourceDescriptionsReferenceSchemaTypeDef = TypedDict(
    "_ClientAddApplicationReferenceDataSourceResponseReferenceDataSourceDescriptionsReferenceSchemaTypeDef",
    {
        "RecordFormat": ClientAddApplicationReferenceDataSourceResponseReferenceDataSourceDescriptionsReferenceSchemaRecordFormatTypeDef,
        "RecordEncoding": str,
        "RecordColumns": List[
            ClientAddApplicationReferenceDataSourceResponseReferenceDataSourceDescriptionsReferenceSchemaRecordColumnsTypeDef
        ],
    },
    total=False,
)


class ClientAddApplicationReferenceDataSourceResponseReferenceDataSourceDescriptionsReferenceSchemaTypeDef(
    _ClientAddApplicationReferenceDataSourceResponseReferenceDataSourceDescriptionsReferenceSchemaTypeDef
):
    """
    Type definition for `ClientAddApplicationReferenceDataSourceResponseReferenceDataSourceDescriptions` `ReferenceSchema`

    Describes the format of the data in the streaming source, and how each data element maps
    to corresponding columns created in the in-application stream.

    - **RecordFormat** *(dict) --*

      Specifies the format of the records on the streaming source.

      - **RecordFormatType** *(string) --*

        The type of record format.

      - **MappingParameters** *(dict) --*

        When you configure application input at the time of creating or updating an
        application, provides additional mapping information specific to the record format
        (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming
        source.

        - **JSONMappingParameters** *(dict) --*

          Provides additional mapping information when JSON is the record format on the
          streaming source.

          - **RecordRowPath** *(string) --*

            The path to the top-level parent that contains the records.

        - **CSVMappingParameters** *(dict) --*

          Provides additional mapping information when the record format uses delimiters (for
          example, CSV).

          - **RecordRowDelimiter** *(string) --*

            The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
            delimiter.

          - **RecordColumnDelimiter** *(string) --*

            The column delimiter. For example, in a CSV format, a comma (",") is the typical
            column delimiter.

    - **RecordEncoding** *(string) --*

      Specifies the encoding of the records in the streaming source. For example, UTF-8.

    - **RecordColumns** *(list) --*

      A list of ``RecordColumn`` objects.

      - *(dict) --*

        For an SQL-based Amazon Kinesis Data Analytics application, describes the mapping of
        each data element in the streaming source to the corresponding column in the
        in-application stream.

        Also used to describe the format of the reference data source.

        - **Name** *(string) --*

          The name of the column that is created in the in-application input stream or
          reference table.

        - **Mapping** *(string) --*

          A reference to the data element in the streaming input or the reference data source.

        - **SqlType** *(string) --*

          The type of column created in the in-application input stream or reference table.
    """


_ClientAddApplicationReferenceDataSourceResponseReferenceDataSourceDescriptionsS3ReferenceDataSourceDescriptionTypeDef = TypedDict(
    "_ClientAddApplicationReferenceDataSourceResponseReferenceDataSourceDescriptionsS3ReferenceDataSourceDescriptionTypeDef",
    {"BucketARN": str, "FileKey": str, "ReferenceRoleARN": str},
    total=False,
)


class ClientAddApplicationReferenceDataSourceResponseReferenceDataSourceDescriptionsS3ReferenceDataSourceDescriptionTypeDef(
    _ClientAddApplicationReferenceDataSourceResponseReferenceDataSourceDescriptionsS3ReferenceDataSourceDescriptionTypeDef
):
    """
    Type definition for `ClientAddApplicationReferenceDataSourceResponseReferenceDataSourceDescriptions` `S3ReferenceDataSourceDescription`

    Provides the Amazon S3 bucket name, the object key name that contains the reference data.

    - **BucketARN** *(string) --*

      The Amazon Resource Name (ARN) of the S3 bucket.

    - **FileKey** *(string) --*

      Amazon S3 object key name.

    - **ReferenceRoleARN** *(string) --*

      The ARN of the IAM role that Kinesis Data Analytics can assume to read the Amazon S3
      object on your behalf to populate the in-application reference table.

      .. note::

        Provided for backward compatibility. Applications that are created with the current
        API version have an application-level service execution role rather than a
        resource-level role.
    """


_ClientAddApplicationReferenceDataSourceResponseReferenceDataSourceDescriptionsTypeDef = TypedDict(
    "_ClientAddApplicationReferenceDataSourceResponseReferenceDataSourceDescriptionsTypeDef",
    {
        "ReferenceId": str,
        "TableName": str,
        "S3ReferenceDataSourceDescription": ClientAddApplicationReferenceDataSourceResponseReferenceDataSourceDescriptionsS3ReferenceDataSourceDescriptionTypeDef,
        "ReferenceSchema": ClientAddApplicationReferenceDataSourceResponseReferenceDataSourceDescriptionsReferenceSchemaTypeDef,
    },
    total=False,
)


class ClientAddApplicationReferenceDataSourceResponseReferenceDataSourceDescriptionsTypeDef(
    _ClientAddApplicationReferenceDataSourceResponseReferenceDataSourceDescriptionsTypeDef
):
    """
    Type definition for `ClientAddApplicationReferenceDataSourceResponse` `ReferenceDataSourceDescriptions`

    For an SQL-based Amazon Kinesis Data Analytics application, describes the reference data
    source configured for an application.

    - **ReferenceId** *(string) --*

      The ID of the reference data source. This is the ID that Kinesis Data Analytics assigns
      when you add the reference data source to your application using the  CreateApplication
      or  UpdateApplication operation.

    - **TableName** *(string) --*

      The in-application table name created by the specific reference data source configuration.

    - **S3ReferenceDataSourceDescription** *(dict) --*

      Provides the Amazon S3 bucket name, the object key name that contains the reference data.

      - **BucketARN** *(string) --*

        The Amazon Resource Name (ARN) of the S3 bucket.

      - **FileKey** *(string) --*

        Amazon S3 object key name.

      - **ReferenceRoleARN** *(string) --*

        The ARN of the IAM role that Kinesis Data Analytics can assume to read the Amazon S3
        object on your behalf to populate the in-application reference table.

        .. note::

          Provided for backward compatibility. Applications that are created with the current
          API version have an application-level service execution role rather than a
          resource-level role.

    - **ReferenceSchema** *(dict) --*

      Describes the format of the data in the streaming source, and how each data element maps
      to corresponding columns created in the in-application stream.

      - **RecordFormat** *(dict) --*

        Specifies the format of the records on the streaming source.

        - **RecordFormatType** *(string) --*

          The type of record format.

        - **MappingParameters** *(dict) --*

          When you configure application input at the time of creating or updating an
          application, provides additional mapping information specific to the record format
          (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming
          source.

          - **JSONMappingParameters** *(dict) --*

            Provides additional mapping information when JSON is the record format on the
            streaming source.

            - **RecordRowPath** *(string) --*

              The path to the top-level parent that contains the records.

          - **CSVMappingParameters** *(dict) --*

            Provides additional mapping information when the record format uses delimiters (for
            example, CSV).

            - **RecordRowDelimiter** *(string) --*

              The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
              delimiter.

            - **RecordColumnDelimiter** *(string) --*

              The column delimiter. For example, in a CSV format, a comma (",") is the typical
              column delimiter.

      - **RecordEncoding** *(string) --*

        Specifies the encoding of the records in the streaming source. For example, UTF-8.

      - **RecordColumns** *(list) --*

        A list of ``RecordColumn`` objects.

        - *(dict) --*

          For an SQL-based Amazon Kinesis Data Analytics application, describes the mapping of
          each data element in the streaming source to the corresponding column in the
          in-application stream.

          Also used to describe the format of the reference data source.

          - **Name** *(string) --*

            The name of the column that is created in the in-application input stream or
            reference table.

          - **Mapping** *(string) --*

            A reference to the data element in the streaming input or the reference data source.

          - **SqlType** *(string) --*

            The type of column created in the in-application input stream or reference table.
    """


_ClientAddApplicationReferenceDataSourceResponseTypeDef = TypedDict(
    "_ClientAddApplicationReferenceDataSourceResponseTypeDef",
    {
        "ApplicationARN": str,
        "ApplicationVersionId": int,
        "ReferenceDataSourceDescriptions": List[
            ClientAddApplicationReferenceDataSourceResponseReferenceDataSourceDescriptionsTypeDef
        ],
    },
    total=False,
)


class ClientAddApplicationReferenceDataSourceResponseTypeDef(
    _ClientAddApplicationReferenceDataSourceResponseTypeDef
):
    """
    Type definition for `ClientAddApplicationReferenceDataSource` `Response`

    - **ApplicationARN** *(string) --*

      The application Amazon Resource Name (ARN).

    - **ApplicationVersionId** *(integer) --*

      The updated application version ID. Amazon Kinesis Data Analytics increments this ID when the
      application is updated.

    - **ReferenceDataSourceDescriptions** *(list) --*

      Describes reference data sources configured for the application.

      - *(dict) --*

        For an SQL-based Amazon Kinesis Data Analytics application, describes the reference data
        source configured for an application.

        - **ReferenceId** *(string) --*

          The ID of the reference data source. This is the ID that Kinesis Data Analytics assigns
          when you add the reference data source to your application using the  CreateApplication
          or  UpdateApplication operation.

        - **TableName** *(string) --*

          The in-application table name created by the specific reference data source configuration.

        - **S3ReferenceDataSourceDescription** *(dict) --*

          Provides the Amazon S3 bucket name, the object key name that contains the reference data.

          - **BucketARN** *(string) --*

            The Amazon Resource Name (ARN) of the S3 bucket.

          - **FileKey** *(string) --*

            Amazon S3 object key name.

          - **ReferenceRoleARN** *(string) --*

            The ARN of the IAM role that Kinesis Data Analytics can assume to read the Amazon S3
            object on your behalf to populate the in-application reference table.

            .. note::

              Provided for backward compatibility. Applications that are created with the current
              API version have an application-level service execution role rather than a
              resource-level role.

        - **ReferenceSchema** *(dict) --*

          Describes the format of the data in the streaming source, and how each data element maps
          to corresponding columns created in the in-application stream.

          - **RecordFormat** *(dict) --*

            Specifies the format of the records on the streaming source.

            - **RecordFormatType** *(string) --*

              The type of record format.

            - **MappingParameters** *(dict) --*

              When you configure application input at the time of creating or updating an
              application, provides additional mapping information specific to the record format
              (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming
              source.

              - **JSONMappingParameters** *(dict) --*

                Provides additional mapping information when JSON is the record format on the
                streaming source.

                - **RecordRowPath** *(string) --*

                  The path to the top-level parent that contains the records.

              - **CSVMappingParameters** *(dict) --*

                Provides additional mapping information when the record format uses delimiters (for
                example, CSV).

                - **RecordRowDelimiter** *(string) --*

                  The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
                  delimiter.

                - **RecordColumnDelimiter** *(string) --*

                  The column delimiter. For example, in a CSV format, a comma (",") is the typical
                  column delimiter.

          - **RecordEncoding** *(string) --*

            Specifies the encoding of the records in the streaming source. For example, UTF-8.

          - **RecordColumns** *(list) --*

            A list of ``RecordColumn`` objects.

            - *(dict) --*

              For an SQL-based Amazon Kinesis Data Analytics application, describes the mapping of
              each data element in the streaming source to the corresponding column in the
              in-application stream.

              Also used to describe the format of the reference data source.

              - **Name** *(string) --*

                The name of the column that is created in the in-application input stream or
                reference table.

              - **Mapping** *(string) --*

                A reference to the data element in the streaming input or the reference data source.

              - **SqlType** *(string) --*

                The type of column created in the in-application input stream or reference table.
    """


_RequiredClientCreateApplicationApplicationConfigurationApplicationCodeConfigurationCodeContentS3ContentLocationTypeDef = TypedDict(
    "_RequiredClientCreateApplicationApplicationConfigurationApplicationCodeConfigurationCodeContentS3ContentLocationTypeDef",
    {"BucketARN": str, "FileKey": str},
)
_OptionalClientCreateApplicationApplicationConfigurationApplicationCodeConfigurationCodeContentS3ContentLocationTypeDef = TypedDict(
    "_OptionalClientCreateApplicationApplicationConfigurationApplicationCodeConfigurationCodeContentS3ContentLocationTypeDef",
    {"ObjectVersion": str},
    total=False,
)


class ClientCreateApplicationApplicationConfigurationApplicationCodeConfigurationCodeContentS3ContentLocationTypeDef(
    _RequiredClientCreateApplicationApplicationConfigurationApplicationCodeConfigurationCodeContentS3ContentLocationTypeDef,
    _OptionalClientCreateApplicationApplicationConfigurationApplicationCodeConfigurationCodeContentS3ContentLocationTypeDef,
):
    """
    Type definition for `ClientCreateApplicationApplicationConfigurationApplicationCodeConfigurationCodeContent` `S3ContentLocation`

    Information about the Amazon S3 bucket containing the application code.

    - **BucketARN** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) for the S3 bucket containing the application code.

    - **FileKey** *(string) --* **[REQUIRED]**

      The file key for the object containing the application code.

    - **ObjectVersion** *(string) --*

      The version of the object containing the application code.
    """


_ClientCreateApplicationApplicationConfigurationApplicationCodeConfigurationCodeContentTypeDef = TypedDict(
    "_ClientCreateApplicationApplicationConfigurationApplicationCodeConfigurationCodeContentTypeDef",
    {
        "TextContent": str,
        "ZipFileContent": bytes,
        "S3ContentLocation": ClientCreateApplicationApplicationConfigurationApplicationCodeConfigurationCodeContentS3ContentLocationTypeDef,
    },
    total=False,
)


class ClientCreateApplicationApplicationConfigurationApplicationCodeConfigurationCodeContentTypeDef(
    _ClientCreateApplicationApplicationConfigurationApplicationCodeConfigurationCodeContentTypeDef
):
    """
    Type definition for `ClientCreateApplicationApplicationConfigurationApplicationCodeConfiguration` `CodeContent`

    The location and type of the application code.

    - **TextContent** *(string) --*

      The text-format code for a Java-based Kinesis Data Analytics application.

    - **ZipFileContent** *(bytes) --*

      The zip-format code for a Java-based Kinesis Data Analytics application.

    - **S3ContentLocation** *(dict) --*

      Information about the Amazon S3 bucket containing the application code.

      - **BucketARN** *(string) --* **[REQUIRED]**

        The Amazon Resource Name (ARN) for the S3 bucket containing the application code.

      - **FileKey** *(string) --* **[REQUIRED]**

        The file key for the object containing the application code.

      - **ObjectVersion** *(string) --*

        The version of the object containing the application code.
    """


_RequiredClientCreateApplicationApplicationConfigurationApplicationCodeConfigurationTypeDef = TypedDict(
    "_RequiredClientCreateApplicationApplicationConfigurationApplicationCodeConfigurationTypeDef",
    {"CodeContentType": str},
)
_OptionalClientCreateApplicationApplicationConfigurationApplicationCodeConfigurationTypeDef = TypedDict(
    "_OptionalClientCreateApplicationApplicationConfigurationApplicationCodeConfigurationTypeDef",
    {
        "CodeContent": ClientCreateApplicationApplicationConfigurationApplicationCodeConfigurationCodeContentTypeDef
    },
    total=False,
)


class ClientCreateApplicationApplicationConfigurationApplicationCodeConfigurationTypeDef(
    _RequiredClientCreateApplicationApplicationConfigurationApplicationCodeConfigurationTypeDef,
    _OptionalClientCreateApplicationApplicationConfigurationApplicationCodeConfigurationTypeDef,
):
    """
    Type definition for `ClientCreateApplicationApplicationConfiguration` `ApplicationCodeConfiguration`

    The code location and type parameters for a Java-based Kinesis Data Analytics application.

    - **CodeContent** *(dict) --*

      The location and type of the application code.

      - **TextContent** *(string) --*

        The text-format code for a Java-based Kinesis Data Analytics application.

      - **ZipFileContent** *(bytes) --*

        The zip-format code for a Java-based Kinesis Data Analytics application.

      - **S3ContentLocation** *(dict) --*

        Information about the Amazon S3 bucket containing the application code.

        - **BucketARN** *(string) --* **[REQUIRED]**

          The Amazon Resource Name (ARN) for the S3 bucket containing the application code.

        - **FileKey** *(string) --* **[REQUIRED]**

          The file key for the object containing the application code.

        - **ObjectVersion** *(string) --*

          The version of the object containing the application code.

    - **CodeContentType** *(string) --* **[REQUIRED]**

      Specifies whether the code content is in text or zip format.
    """


_ClientCreateApplicationApplicationConfigurationApplicationSnapshotConfigurationTypeDef = TypedDict(
    "_ClientCreateApplicationApplicationConfigurationApplicationSnapshotConfigurationTypeDef",
    {"SnapshotsEnabled": bool},
)


class ClientCreateApplicationApplicationConfigurationApplicationSnapshotConfigurationTypeDef(
    _ClientCreateApplicationApplicationConfigurationApplicationSnapshotConfigurationTypeDef
):
    """
    Type definition for `ClientCreateApplicationApplicationConfiguration` `ApplicationSnapshotConfiguration`

    Describes whether snapshots are enabled for a Java-based Kinesis Data Analytics application.

    - **SnapshotsEnabled** *(boolean) --* **[REQUIRED]**

      Describes whether snapshots are enabled for a Java-based Kinesis Data Analytics application.
    """


_ClientCreateApplicationApplicationConfigurationEnvironmentPropertiesPropertyGroupsTypeDef = TypedDict(
    "_ClientCreateApplicationApplicationConfigurationEnvironmentPropertiesPropertyGroupsTypeDef",
    {"PropertyGroupId": str, "PropertyMap": Dict[str, str]},
)


class ClientCreateApplicationApplicationConfigurationEnvironmentPropertiesPropertyGroupsTypeDef(
    _ClientCreateApplicationApplicationConfigurationEnvironmentPropertiesPropertyGroupsTypeDef
):
    """
    Type definition for `ClientCreateApplicationApplicationConfigurationEnvironmentProperties` `PropertyGroups`

    Property key-value pairs passed into a Java-based Kinesis Data Analytics application.

    - **PropertyGroupId** *(string) --* **[REQUIRED]**

      Describes the key of an application execution property key-value pair.

    - **PropertyMap** *(dict) --* **[REQUIRED]**

      Describes the value of an application execution property key-value pair.

      - *(string) --*

        - *(string) --*
    """


_ClientCreateApplicationApplicationConfigurationEnvironmentPropertiesTypeDef = TypedDict(
    "_ClientCreateApplicationApplicationConfigurationEnvironmentPropertiesTypeDef",
    {
        "PropertyGroups": List[
            ClientCreateApplicationApplicationConfigurationEnvironmentPropertiesPropertyGroupsTypeDef
        ]
    },
)


class ClientCreateApplicationApplicationConfigurationEnvironmentPropertiesTypeDef(
    _ClientCreateApplicationApplicationConfigurationEnvironmentPropertiesTypeDef
):
    """
    Type definition for `ClientCreateApplicationApplicationConfiguration` `EnvironmentProperties`

    Describes execution properties for a Java-based Kinesis Data Analytics application.

    - **PropertyGroups** *(list) --* **[REQUIRED]**

      Describes the execution property groups.

      - *(dict) --*

        Property key-value pairs passed into a Java-based Kinesis Data Analytics application.

        - **PropertyGroupId** *(string) --* **[REQUIRED]**

          Describes the key of an application execution property key-value pair.

        - **PropertyMap** *(dict) --* **[REQUIRED]**

          Describes the value of an application execution property key-value pair.

          - *(string) --*

            - *(string) --*
    """


_RequiredClientCreateApplicationApplicationConfigurationFlinkApplicationConfigurationCheckpointConfigurationTypeDef = TypedDict(
    "_RequiredClientCreateApplicationApplicationConfigurationFlinkApplicationConfigurationCheckpointConfigurationTypeDef",
    {"ConfigurationType": str},
)
_OptionalClientCreateApplicationApplicationConfigurationFlinkApplicationConfigurationCheckpointConfigurationTypeDef = TypedDict(
    "_OptionalClientCreateApplicationApplicationConfigurationFlinkApplicationConfigurationCheckpointConfigurationTypeDef",
    {
        "CheckpointingEnabled": bool,
        "CheckpointInterval": int,
        "MinPauseBetweenCheckpoints": int,
    },
    total=False,
)


class ClientCreateApplicationApplicationConfigurationFlinkApplicationConfigurationCheckpointConfigurationTypeDef(
    _RequiredClientCreateApplicationApplicationConfigurationFlinkApplicationConfigurationCheckpointConfigurationTypeDef,
    _OptionalClientCreateApplicationApplicationConfigurationFlinkApplicationConfigurationCheckpointConfigurationTypeDef,
):
    """
    Type definition for `ClientCreateApplicationApplicationConfigurationFlinkApplicationConfiguration` `CheckpointConfiguration`

    Describes an application's checkpointing configuration. Checkpointing is the process of
    persisting application state for fault tolerance. For more information, see `Checkpoints for
    Fault Tolerance
    <https://ci.apache.org/projects/flink/flink-docs-release-1.6/concepts/programming-model.html#checkpoints-for-fault-tolerance>`__
    in the `Apache Flink Documentation
    <https://ci.apache.org/projects/flink/flink-docs-release-1.6/>`__ .

    - **ConfigurationType** *(string) --* **[REQUIRED]**

      Describes whether the application uses Amazon Kinesis Data Analytics' default checkpointing
      behavior.

    - **CheckpointingEnabled** *(boolean) --*

      Describes whether checkpointing is enabled for a Java-based Kinesis Data Analytics
      application.

    - **CheckpointInterval** *(integer) --*

      Describes the interval in milliseconds between checkpoint operations.

    - **MinPauseBetweenCheckpoints** *(integer) --*

      Describes the minimum time in milliseconds after a checkpoint operation completes that a
      new checkpoint operation can start. If a checkpoint operation takes longer than the
      ``CheckpointInterval`` , the application otherwise performs continual checkpoint
      operations. For more information, see `Tuning Checkpointing
      <https://ci.apache.org/projects/flink/flink-docs-stable/ops/state/large_state_tuning.html#tuning-checkpointing>`__
      in the `Apache Flink Documentation
      <https://ci.apache.org/projects/flink/flink-docs-release-1.6/>`__ .
    """


_RequiredClientCreateApplicationApplicationConfigurationFlinkApplicationConfigurationMonitoringConfigurationTypeDef = TypedDict(
    "_RequiredClientCreateApplicationApplicationConfigurationFlinkApplicationConfigurationMonitoringConfigurationTypeDef",
    {"ConfigurationType": str},
)
_OptionalClientCreateApplicationApplicationConfigurationFlinkApplicationConfigurationMonitoringConfigurationTypeDef = TypedDict(
    "_OptionalClientCreateApplicationApplicationConfigurationFlinkApplicationConfigurationMonitoringConfigurationTypeDef",
    {"MetricsLevel": str, "LogLevel": str},
    total=False,
)


class ClientCreateApplicationApplicationConfigurationFlinkApplicationConfigurationMonitoringConfigurationTypeDef(
    _RequiredClientCreateApplicationApplicationConfigurationFlinkApplicationConfigurationMonitoringConfigurationTypeDef,
    _OptionalClientCreateApplicationApplicationConfigurationFlinkApplicationConfigurationMonitoringConfigurationTypeDef,
):
    """
    Type definition for `ClientCreateApplicationApplicationConfigurationFlinkApplicationConfiguration` `MonitoringConfiguration`

    Describes configuration parameters for Amazon CloudWatch logging for an application.

    - **ConfigurationType** *(string) --* **[REQUIRED]**

      Describes whether to use the default CloudWatch logging configuration for an application.

    - **MetricsLevel** *(string) --*

      Describes the granularity of the CloudWatch Logs for an application.

    - **LogLevel** *(string) --*

      Describes the verbosity of the CloudWatch Logs for an application.
    """


_RequiredClientCreateApplicationApplicationConfigurationFlinkApplicationConfigurationParallelismConfigurationTypeDef = TypedDict(
    "_RequiredClientCreateApplicationApplicationConfigurationFlinkApplicationConfigurationParallelismConfigurationTypeDef",
    {"ConfigurationType": str},
)
_OptionalClientCreateApplicationApplicationConfigurationFlinkApplicationConfigurationParallelismConfigurationTypeDef = TypedDict(
    "_OptionalClientCreateApplicationApplicationConfigurationFlinkApplicationConfigurationParallelismConfigurationTypeDef",
    {"Parallelism": int, "ParallelismPerKPU": int, "AutoScalingEnabled": bool},
    total=False,
)


class ClientCreateApplicationApplicationConfigurationFlinkApplicationConfigurationParallelismConfigurationTypeDef(
    _RequiredClientCreateApplicationApplicationConfigurationFlinkApplicationConfigurationParallelismConfigurationTypeDef,
    _OptionalClientCreateApplicationApplicationConfigurationFlinkApplicationConfigurationParallelismConfigurationTypeDef,
):
    """
    Type definition for `ClientCreateApplicationApplicationConfigurationFlinkApplicationConfiguration` `ParallelismConfiguration`

    Describes parameters for how an application executes multiple tasks simultaneously.

    - **ConfigurationType** *(string) --* **[REQUIRED]**

      Describes whether the application uses the default parallelism for the Kinesis Data
      Analytics service.

    - **Parallelism** *(integer) --*

      Describes the initial number of parallel tasks that a Java-based Kinesis Data Analytics
      application can perform. The Kinesis Data Analytics service can increase this number
      automatically if  ParallelismConfiguration$AutoScalingEnabled is set to ``true`` .

    - **ParallelismPerKPU** *(integer) --*

      Describes the number of parallel tasks that a Java-based Kinesis Data Analytics application
      can perform per Kinesis Processing Unit (KPU) used by the application. For more information
      about KPUs, see `Amazon Kinesis Data Analytics Pricing
      <http://aws.amazon.com/kinesis/data-analytics/pricing/>`__ .

    - **AutoScalingEnabled** *(boolean) --*

      Describes whether the Kinesis Data Analytics service can increase the parallelism of the
      application in response to increased throughput.
    """


_ClientCreateApplicationApplicationConfigurationFlinkApplicationConfigurationTypeDef = TypedDict(
    "_ClientCreateApplicationApplicationConfigurationFlinkApplicationConfigurationTypeDef",
    {
        "CheckpointConfiguration": ClientCreateApplicationApplicationConfigurationFlinkApplicationConfigurationCheckpointConfigurationTypeDef,
        "MonitoringConfiguration": ClientCreateApplicationApplicationConfigurationFlinkApplicationConfigurationMonitoringConfigurationTypeDef,
        "ParallelismConfiguration": ClientCreateApplicationApplicationConfigurationFlinkApplicationConfigurationParallelismConfigurationTypeDef,
    },
    total=False,
)


class ClientCreateApplicationApplicationConfigurationFlinkApplicationConfigurationTypeDef(
    _ClientCreateApplicationApplicationConfigurationFlinkApplicationConfigurationTypeDef
):
    """
    Type definition for `ClientCreateApplicationApplicationConfiguration` `FlinkApplicationConfiguration`

    The creation and update parameters for a Java-based Kinesis Data Analytics application.

    - **CheckpointConfiguration** *(dict) --*

      Describes an application's checkpointing configuration. Checkpointing is the process of
      persisting application state for fault tolerance. For more information, see `Checkpoints for
      Fault Tolerance
      <https://ci.apache.org/projects/flink/flink-docs-release-1.6/concepts/programming-model.html#checkpoints-for-fault-tolerance>`__
      in the `Apache Flink Documentation
      <https://ci.apache.org/projects/flink/flink-docs-release-1.6/>`__ .

      - **ConfigurationType** *(string) --* **[REQUIRED]**

        Describes whether the application uses Amazon Kinesis Data Analytics' default checkpointing
        behavior.

      - **CheckpointingEnabled** *(boolean) --*

        Describes whether checkpointing is enabled for a Java-based Kinesis Data Analytics
        application.

      - **CheckpointInterval** *(integer) --*

        Describes the interval in milliseconds between checkpoint operations.

      - **MinPauseBetweenCheckpoints** *(integer) --*

        Describes the minimum time in milliseconds after a checkpoint operation completes that a
        new checkpoint operation can start. If a checkpoint operation takes longer than the
        ``CheckpointInterval`` , the application otherwise performs continual checkpoint
        operations. For more information, see `Tuning Checkpointing
        <https://ci.apache.org/projects/flink/flink-docs-stable/ops/state/large_state_tuning.html#tuning-checkpointing>`__
        in the `Apache Flink Documentation
        <https://ci.apache.org/projects/flink/flink-docs-release-1.6/>`__ .

    - **MonitoringConfiguration** *(dict) --*

      Describes configuration parameters for Amazon CloudWatch logging for an application.

      - **ConfigurationType** *(string) --* **[REQUIRED]**

        Describes whether to use the default CloudWatch logging configuration for an application.

      - **MetricsLevel** *(string) --*

        Describes the granularity of the CloudWatch Logs for an application.

      - **LogLevel** *(string) --*

        Describes the verbosity of the CloudWatch Logs for an application.

    - **ParallelismConfiguration** *(dict) --*

      Describes parameters for how an application executes multiple tasks simultaneously.

      - **ConfigurationType** *(string) --* **[REQUIRED]**

        Describes whether the application uses the default parallelism for the Kinesis Data
        Analytics service.

      - **Parallelism** *(integer) --*

        Describes the initial number of parallel tasks that a Java-based Kinesis Data Analytics
        application can perform. The Kinesis Data Analytics service can increase this number
        automatically if  ParallelismConfiguration$AutoScalingEnabled is set to ``true`` .

      - **ParallelismPerKPU** *(integer) --*

        Describes the number of parallel tasks that a Java-based Kinesis Data Analytics application
        can perform per Kinesis Processing Unit (KPU) used by the application. For more information
        about KPUs, see `Amazon Kinesis Data Analytics Pricing
        <http://aws.amazon.com/kinesis/data-analytics/pricing/>`__ .

      - **AutoScalingEnabled** *(boolean) --*

        Describes whether the Kinesis Data Analytics service can increase the parallelism of the
        application in response to increased throughput.
    """


_ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsInputParallelismTypeDef = TypedDict(
    "_ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsInputParallelismTypeDef",
    {"Count": int},
    total=False,
)


class ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsInputParallelismTypeDef(
    _ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsInputParallelismTypeDef
):
    """
    Type definition for `ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputs` `InputParallelism`

    Describes the number of in-application streams to create.

    - **Count** *(integer) --*

      The number of in-application streams to create.
    """


_ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsInputProcessingConfigurationInputLambdaProcessorTypeDef = TypedDict(
    "_ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsInputProcessingConfigurationInputLambdaProcessorTypeDef",
    {"ResourceARN": str},
)


class ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsInputProcessingConfigurationInputLambdaProcessorTypeDef(
    _ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsInputProcessingConfigurationInputLambdaProcessorTypeDef
):
    """
    Type definition for `ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsInputProcessingConfiguration` `InputLambdaProcessor`

    The  InputLambdaProcessor that is used to preprocess the records in the stream before
    being processed by your application code.

    - **ResourceARN** *(string) --* **[REQUIRED]**

      The ARN of the AWS Lambda function that operates on records in the stream.

      .. note::

        To specify an earlier version of the Lambda function than the latest, include the
        Lambda function version in the Lambda function ARN. For more information about
        Lambda ARNs, see `Example ARNs\\: AWS Lambda
        </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__
    """


_ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsInputProcessingConfigurationTypeDef = TypedDict(
    "_ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsInputProcessingConfigurationTypeDef",
    {
        "InputLambdaProcessor": ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsInputProcessingConfigurationInputLambdaProcessorTypeDef
    },
)


class ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsInputProcessingConfigurationTypeDef(
    _ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsInputProcessingConfigurationTypeDef
):
    """
    Type definition for `ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputs` `InputProcessingConfiguration`

    The  InputProcessingConfiguration for the input. An input processor transforms records as
    they are received from the stream, before the application's SQL code executes. Currently,
    the only input processing configuration available is  InputLambdaProcessor .

    - **InputLambdaProcessor** *(dict) --* **[REQUIRED]**

      The  InputLambdaProcessor that is used to preprocess the records in the stream before
      being processed by your application code.

      - **ResourceARN** *(string) --* **[REQUIRED]**

        The ARN of the AWS Lambda function that operates on records in the stream.

        .. note::

          To specify an earlier version of the Lambda function than the latest, include the
          Lambda function version in the Lambda function ARN. For more information about
          Lambda ARNs, see `Example ARNs\\: AWS Lambda
          </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__
    """


_RequiredClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsInputSchemaRecordColumnsTypeDef = TypedDict(
    "_RequiredClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsInputSchemaRecordColumnsTypeDef",
    {"Name": str, "SqlType": str},
)
_OptionalClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsInputSchemaRecordColumnsTypeDef = TypedDict(
    "_OptionalClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsInputSchemaRecordColumnsTypeDef",
    {"Mapping": str},
    total=False,
)


class ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsInputSchemaRecordColumnsTypeDef(
    _RequiredClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsInputSchemaRecordColumnsTypeDef,
    _OptionalClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsInputSchemaRecordColumnsTypeDef,
):
    """
    Type definition for `ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsInputSchema` `RecordColumns`

    For an SQL-based Amazon Kinesis Data Analytics application, describes the mapping of
    each data element in the streaming source to the corresponding column in the
    in-application stream.

    Also used to describe the format of the reference data source.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the column that is created in the in-application input stream or
      reference table.

    - **Mapping** *(string) --*

      A reference to the data element in the streaming input or the reference data source.

    - **SqlType** *(string) --* **[REQUIRED]**

      The type of column created in the in-application input stream or reference table.
    """


_ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef = TypedDict(
    "_ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef",
    {"RecordRowDelimiter": str, "RecordColumnDelimiter": str},
)


class ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef(
    _ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef
):
    """
    Type definition for `ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsInputSchemaRecordFormatMappingParameters` `CSVMappingParameters`

    Provides additional mapping information when the record format uses delimiters (for
    example, CSV).

    - **RecordRowDelimiter** *(string) --* **[REQUIRED]**

      The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
      delimiter.

    - **RecordColumnDelimiter** *(string) --* **[REQUIRED]**

      The column delimiter. For example, in a CSV format, a comma (",") is the typical
      column delimiter.
    """


_ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef = TypedDict(
    "_ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef",
    {"RecordRowPath": str},
)


class ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef(
    _ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef
):
    """
    Type definition for `ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsInputSchemaRecordFormatMappingParameters` `JSONMappingParameters`

    Provides additional mapping information when JSON is the record format on the
    streaming source.

    - **RecordRowPath** *(string) --* **[REQUIRED]**

      The path to the top-level parent that contains the records.
    """


_ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsInputSchemaRecordFormatMappingParametersTypeDef = TypedDict(
    "_ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsInputSchemaRecordFormatMappingParametersTypeDef",
    {
        "JSONMappingParameters": ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef,
        "CSVMappingParameters": ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef,
    },
    total=False,
)


class ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsInputSchemaRecordFormatMappingParametersTypeDef(
    _ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsInputSchemaRecordFormatMappingParametersTypeDef
):
    """
    Type definition for `ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsInputSchemaRecordFormat` `MappingParameters`

    When you configure application input at the time of creating or updating an
    application, provides additional mapping information specific to the record format
    (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming
    source.

    - **JSONMappingParameters** *(dict) --*

      Provides additional mapping information when JSON is the record format on the
      streaming source.

      - **RecordRowPath** *(string) --* **[REQUIRED]**

        The path to the top-level parent that contains the records.

    - **CSVMappingParameters** *(dict) --*

      Provides additional mapping information when the record format uses delimiters (for
      example, CSV).

      - **RecordRowDelimiter** *(string) --* **[REQUIRED]**

        The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
        delimiter.

      - **RecordColumnDelimiter** *(string) --* **[REQUIRED]**

        The column delimiter. For example, in a CSV format, a comma (",") is the typical
        column delimiter.
    """


_RequiredClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsInputSchemaRecordFormatTypeDef = TypedDict(
    "_RequiredClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsInputSchemaRecordFormatTypeDef",
    {"RecordFormatType": str},
)
_OptionalClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsInputSchemaRecordFormatTypeDef = TypedDict(
    "_OptionalClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsInputSchemaRecordFormatTypeDef",
    {
        "MappingParameters": ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsInputSchemaRecordFormatMappingParametersTypeDef
    },
    total=False,
)


class ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsInputSchemaRecordFormatTypeDef(
    _RequiredClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsInputSchemaRecordFormatTypeDef,
    _OptionalClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsInputSchemaRecordFormatTypeDef,
):
    """
    Type definition for `ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsInputSchema` `RecordFormat`

    Specifies the format of the records on the streaming source.

    - **RecordFormatType** *(string) --* **[REQUIRED]**

      The type of record format.

    - **MappingParameters** *(dict) --*

      When you configure application input at the time of creating or updating an
      application, provides additional mapping information specific to the record format
      (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming
      source.

      - **JSONMappingParameters** *(dict) --*

        Provides additional mapping information when JSON is the record format on the
        streaming source.

        - **RecordRowPath** *(string) --* **[REQUIRED]**

          The path to the top-level parent that contains the records.

      - **CSVMappingParameters** *(dict) --*

        Provides additional mapping information when the record format uses delimiters (for
        example, CSV).

        - **RecordRowDelimiter** *(string) --* **[REQUIRED]**

          The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
          delimiter.

        - **RecordColumnDelimiter** *(string) --* **[REQUIRED]**

          The column delimiter. For example, in a CSV format, a comma (",") is the typical
          column delimiter.
    """


_RequiredClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsInputSchemaTypeDef = TypedDict(
    "_RequiredClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsInputSchemaTypeDef",
    {
        "RecordFormat": ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsInputSchemaRecordFormatTypeDef,
        "RecordColumns": List[
            ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsInputSchemaRecordColumnsTypeDef
        ],
    },
)
_OptionalClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsInputSchemaTypeDef = TypedDict(
    "_OptionalClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsInputSchemaTypeDef",
    {"RecordEncoding": str},
    total=False,
)


class ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsInputSchemaTypeDef(
    _RequiredClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsInputSchemaTypeDef,
    _OptionalClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsInputSchemaTypeDef,
):
    """
    Type definition for `ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputs` `InputSchema`

    Describes the format of the data in the streaming source, and how each data element maps
    to corresponding columns in the in-application stream that is being created.

    Also used to describe the format of the reference data source.

    - **RecordFormat** *(dict) --* **[REQUIRED]**

      Specifies the format of the records on the streaming source.

      - **RecordFormatType** *(string) --* **[REQUIRED]**

        The type of record format.

      - **MappingParameters** *(dict) --*

        When you configure application input at the time of creating or updating an
        application, provides additional mapping information specific to the record format
        (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming
        source.

        - **JSONMappingParameters** *(dict) --*

          Provides additional mapping information when JSON is the record format on the
          streaming source.

          - **RecordRowPath** *(string) --* **[REQUIRED]**

            The path to the top-level parent that contains the records.

        - **CSVMappingParameters** *(dict) --*

          Provides additional mapping information when the record format uses delimiters (for
          example, CSV).

          - **RecordRowDelimiter** *(string) --* **[REQUIRED]**

            The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
            delimiter.

          - **RecordColumnDelimiter** *(string) --* **[REQUIRED]**

            The column delimiter. For example, in a CSV format, a comma (",") is the typical
            column delimiter.

    - **RecordEncoding** *(string) --*

      Specifies the encoding of the records in the streaming source. For example, UTF-8.

    - **RecordColumns** *(list) --* **[REQUIRED]**

      A list of ``RecordColumn`` objects.

      - *(dict) --*

        For an SQL-based Amazon Kinesis Data Analytics application, describes the mapping of
        each data element in the streaming source to the corresponding column in the
        in-application stream.

        Also used to describe the format of the reference data source.

        - **Name** *(string) --* **[REQUIRED]**

          The name of the column that is created in the in-application input stream or
          reference table.

        - **Mapping** *(string) --*

          A reference to the data element in the streaming input or the reference data source.

        - **SqlType** *(string) --* **[REQUIRED]**

          The type of column created in the in-application input stream or reference table.
    """


_ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsKinesisFirehoseInputTypeDef = TypedDict(
    "_ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsKinesisFirehoseInputTypeDef",
    {"ResourceARN": str},
)


class ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsKinesisFirehoseInputTypeDef(
    _ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsKinesisFirehoseInputTypeDef
):
    """
    Type definition for `ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputs` `KinesisFirehoseInput`

    If the streaming source is an Amazon Kinesis Data Firehose delivery stream, identifies
    the delivery stream's ARN.

    - **ResourceARN** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the delivery stream.
    """


_ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsKinesisStreamsInputTypeDef = TypedDict(
    "_ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsKinesisStreamsInputTypeDef",
    {"ResourceARN": str},
)


class ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsKinesisStreamsInputTypeDef(
    _ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsKinesisStreamsInputTypeDef
):
    """
    Type definition for `ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputs` `KinesisStreamsInput`

    If the streaming source is an Amazon Kinesis data stream, identifies the stream's Amazon
    Resource Name (ARN).

    - **ResourceARN** *(string) --* **[REQUIRED]**

      The ARN of the input Kinesis data stream to read.
    """


_RequiredClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsTypeDef = TypedDict(
    "_RequiredClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsTypeDef",
    {
        "NamePrefix": str,
        "InputSchema": ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsInputSchemaTypeDef,
    },
)
_OptionalClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsTypeDef = TypedDict(
    "_OptionalClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsTypeDef",
    {
        "InputProcessingConfiguration": ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsInputProcessingConfigurationTypeDef,
        "KinesisStreamsInput": ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsKinesisStreamsInputTypeDef,
        "KinesisFirehoseInput": ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsKinesisFirehoseInputTypeDef,
        "InputParallelism": ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsInputParallelismTypeDef,
    },
    total=False,
)


class ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsTypeDef(
    _RequiredClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsTypeDef,
    _OptionalClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsTypeDef,
):
    """
    Type definition for `ClientCreateApplicationApplicationConfigurationSqlApplicationConfiguration` `Inputs`

    When you configure the application input for an SQL-based Amazon Kinesis Data Analytics
    application, you specify the streaming source, the in-application stream name that is
    created, and the mapping between the two.

    - **NamePrefix** *(string) --* **[REQUIRED]**

      The name prefix to use when creating an in-application stream. Suppose that you specify a
      prefix "``MyInApplicationStream`` ." Kinesis Data Analytics then creates one or more (as
      per the ``InputParallelism`` count you specified) in-application streams with the names
      "``MyInApplicationStream_001`` ," "``MyInApplicationStream_002`` ," and so on.

    - **InputProcessingConfiguration** *(dict) --*

      The  InputProcessingConfiguration for the input. An input processor transforms records as
      they are received from the stream, before the application's SQL code executes. Currently,
      the only input processing configuration available is  InputLambdaProcessor .

      - **InputLambdaProcessor** *(dict) --* **[REQUIRED]**

        The  InputLambdaProcessor that is used to preprocess the records in the stream before
        being processed by your application code.

        - **ResourceARN** *(string) --* **[REQUIRED]**

          The ARN of the AWS Lambda function that operates on records in the stream.

          .. note::

            To specify an earlier version of the Lambda function than the latest, include the
            Lambda function version in the Lambda function ARN. For more information about
            Lambda ARNs, see `Example ARNs\\: AWS Lambda
            </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__

    - **KinesisStreamsInput** *(dict) --*

      If the streaming source is an Amazon Kinesis data stream, identifies the stream's Amazon
      Resource Name (ARN).

      - **ResourceARN** *(string) --* **[REQUIRED]**

        The ARN of the input Kinesis data stream to read.

    - **KinesisFirehoseInput** *(dict) --*

      If the streaming source is an Amazon Kinesis Data Firehose delivery stream, identifies
      the delivery stream's ARN.

      - **ResourceARN** *(string) --* **[REQUIRED]**

        The Amazon Resource Name (ARN) of the delivery stream.

    - **InputParallelism** *(dict) --*

      Describes the number of in-application streams to create.

      - **Count** *(integer) --*

        The number of in-application streams to create.

    - **InputSchema** *(dict) --* **[REQUIRED]**

      Describes the format of the data in the streaming source, and how each data element maps
      to corresponding columns in the in-application stream that is being created.

      Also used to describe the format of the reference data source.

      - **RecordFormat** *(dict) --* **[REQUIRED]**

        Specifies the format of the records on the streaming source.

        - **RecordFormatType** *(string) --* **[REQUIRED]**

          The type of record format.

        - **MappingParameters** *(dict) --*

          When you configure application input at the time of creating or updating an
          application, provides additional mapping information specific to the record format
          (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming
          source.

          - **JSONMappingParameters** *(dict) --*

            Provides additional mapping information when JSON is the record format on the
            streaming source.

            - **RecordRowPath** *(string) --* **[REQUIRED]**

              The path to the top-level parent that contains the records.

          - **CSVMappingParameters** *(dict) --*

            Provides additional mapping information when the record format uses delimiters (for
            example, CSV).

            - **RecordRowDelimiter** *(string) --* **[REQUIRED]**

              The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
              delimiter.

            - **RecordColumnDelimiter** *(string) --* **[REQUIRED]**

              The column delimiter. For example, in a CSV format, a comma (",") is the typical
              column delimiter.

      - **RecordEncoding** *(string) --*

        Specifies the encoding of the records in the streaming source. For example, UTF-8.

      - **RecordColumns** *(list) --* **[REQUIRED]**

        A list of ``RecordColumn`` objects.

        - *(dict) --*

          For an SQL-based Amazon Kinesis Data Analytics application, describes the mapping of
          each data element in the streaming source to the corresponding column in the
          in-application stream.

          Also used to describe the format of the reference data source.

          - **Name** *(string) --* **[REQUIRED]**

            The name of the column that is created in the in-application input stream or
            reference table.

          - **Mapping** *(string) --*

            A reference to the data element in the streaming input or the reference data source.

          - **SqlType** *(string) --* **[REQUIRED]**

            The type of column created in the in-application input stream or reference table.
    """


_ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationOutputsDestinationSchemaTypeDef = TypedDict(
    "_ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationOutputsDestinationSchemaTypeDef",
    {"RecordFormatType": str},
)


class ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationOutputsDestinationSchemaTypeDef(
    _ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationOutputsDestinationSchemaTypeDef
):
    """
    Type definition for `ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationOutputs` `DestinationSchema`

    Describes the data format when records are written to the destination.

    - **RecordFormatType** *(string) --* **[REQUIRED]**

      Specifies the format of the records on the output stream.
    """


_ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationOutputsKinesisFirehoseOutputTypeDef = TypedDict(
    "_ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationOutputsKinesisFirehoseOutputTypeDef",
    {"ResourceARN": str},
)


class ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationOutputsKinesisFirehoseOutputTypeDef(
    _ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationOutputsKinesisFirehoseOutputTypeDef
):
    """
    Type definition for `ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationOutputs` `KinesisFirehoseOutput`

    Identifies an Amazon Kinesis Data Firehose delivery stream as the destination.

    - **ResourceARN** *(string) --* **[REQUIRED]**

      The ARN of the destination delivery stream to write to.
    """


_ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationOutputsKinesisStreamsOutputTypeDef = TypedDict(
    "_ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationOutputsKinesisStreamsOutputTypeDef",
    {"ResourceARN": str},
)


class ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationOutputsKinesisStreamsOutputTypeDef(
    _ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationOutputsKinesisStreamsOutputTypeDef
):
    """
    Type definition for `ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationOutputs` `KinesisStreamsOutput`

    Identifies an Amazon Kinesis data stream as the destination.

    - **ResourceARN** *(string) --* **[REQUIRED]**

      The ARN of the destination Kinesis data stream to write to.
    """


_ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationOutputsLambdaOutputTypeDef = TypedDict(
    "_ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationOutputsLambdaOutputTypeDef",
    {"ResourceARN": str},
)


class ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationOutputsLambdaOutputTypeDef(
    _ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationOutputsLambdaOutputTypeDef
):
    """
    Type definition for `ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationOutputs` `LambdaOutput`

    Identifies an AWS Lambda function as the destination.

    - **ResourceARN** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the destination Lambda function to write to.

      .. note::

        To specify an earlier version of the Lambda function than the latest, include the
        Lambda function version in the Lambda function ARN. For more information about Lambda
        ARNs, see `Example ARNs\\: AWS Lambda
        </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__
    """


_RequiredClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationOutputsTypeDef = TypedDict(
    "_RequiredClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationOutputsTypeDef",
    {
        "Name": str,
        "DestinationSchema": ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationOutputsDestinationSchemaTypeDef,
    },
)
_OptionalClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationOutputsTypeDef = TypedDict(
    "_OptionalClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationOutputsTypeDef",
    {
        "KinesisStreamsOutput": ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationOutputsKinesisStreamsOutputTypeDef,
        "KinesisFirehoseOutput": ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationOutputsKinesisFirehoseOutputTypeDef,
        "LambdaOutput": ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationOutputsLambdaOutputTypeDef,
    },
    total=False,
)


class ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationOutputsTypeDef(
    _RequiredClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationOutputsTypeDef,
    _OptionalClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationOutputsTypeDef,
):
    """
    Type definition for `ClientCreateApplicationApplicationConfigurationSqlApplicationConfiguration` `Outputs`

    Describes an SQL-based Amazon Kinesis Data Analytics application's output configuration, in
    which you identify an in-application stream and a destination where you want the
    in-application stream data to be written. The destination can be a Kinesis data stream or a
    Kinesis Data Firehose delivery stream.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the in-application stream.

    - **KinesisStreamsOutput** *(dict) --*

      Identifies an Amazon Kinesis data stream as the destination.

      - **ResourceARN** *(string) --* **[REQUIRED]**

        The ARN of the destination Kinesis data stream to write to.

    - **KinesisFirehoseOutput** *(dict) --*

      Identifies an Amazon Kinesis Data Firehose delivery stream as the destination.

      - **ResourceARN** *(string) --* **[REQUIRED]**

        The ARN of the destination delivery stream to write to.

    - **LambdaOutput** *(dict) --*

      Identifies an AWS Lambda function as the destination.

      - **ResourceARN** *(string) --* **[REQUIRED]**

        The Amazon Resource Name (ARN) of the destination Lambda function to write to.

        .. note::

          To specify an earlier version of the Lambda function than the latest, include the
          Lambda function version in the Lambda function ARN. For more information about Lambda
          ARNs, see `Example ARNs\\: AWS Lambda
          </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__

    - **DestinationSchema** *(dict) --* **[REQUIRED]**

      Describes the data format when records are written to the destination.

      - **RecordFormatType** *(string) --* **[REQUIRED]**

        Specifies the format of the records on the output stream.
    """


_RequiredClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourcesReferenceSchemaRecordColumnsTypeDef = TypedDict(
    "_RequiredClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourcesReferenceSchemaRecordColumnsTypeDef",
    {"Name": str, "SqlType": str},
)
_OptionalClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourcesReferenceSchemaRecordColumnsTypeDef = TypedDict(
    "_OptionalClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourcesReferenceSchemaRecordColumnsTypeDef",
    {"Mapping": str},
    total=False,
)


class ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourcesReferenceSchemaRecordColumnsTypeDef(
    _RequiredClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourcesReferenceSchemaRecordColumnsTypeDef,
    _OptionalClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourcesReferenceSchemaRecordColumnsTypeDef,
):
    """
    Type definition for `ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourcesReferenceSchema` `RecordColumns`

    For an SQL-based Amazon Kinesis Data Analytics application, describes the mapping of
    each data element in the streaming source to the corresponding column in the
    in-application stream.

    Also used to describe the format of the reference data source.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the column that is created in the in-application input stream or
      reference table.

    - **Mapping** *(string) --*

      A reference to the data element in the streaming input or the reference data source.

    - **SqlType** *(string) --* **[REQUIRED]**

      The type of column created in the in-application input stream or reference table.
    """


_ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourcesReferenceSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef = TypedDict(
    "_ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourcesReferenceSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef",
    {"RecordRowDelimiter": str, "RecordColumnDelimiter": str},
)


class ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourcesReferenceSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef(
    _ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourcesReferenceSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef
):
    """
    Type definition for `ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourcesReferenceSchemaRecordFormatMappingParameters` `CSVMappingParameters`

    Provides additional mapping information when the record format uses delimiters (for
    example, CSV).

    - **RecordRowDelimiter** *(string) --* **[REQUIRED]**

      The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
      delimiter.

    - **RecordColumnDelimiter** *(string) --* **[REQUIRED]**

      The column delimiter. For example, in a CSV format, a comma (",") is the typical
      column delimiter.
    """


_ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourcesReferenceSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef = TypedDict(
    "_ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourcesReferenceSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef",
    {"RecordRowPath": str},
)


class ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourcesReferenceSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef(
    _ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourcesReferenceSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef
):
    """
    Type definition for `ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourcesReferenceSchemaRecordFormatMappingParameters` `JSONMappingParameters`

    Provides additional mapping information when JSON is the record format on the
    streaming source.

    - **RecordRowPath** *(string) --* **[REQUIRED]**

      The path to the top-level parent that contains the records.
    """


_ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourcesReferenceSchemaRecordFormatMappingParametersTypeDef = TypedDict(
    "_ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourcesReferenceSchemaRecordFormatMappingParametersTypeDef",
    {
        "JSONMappingParameters": ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourcesReferenceSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef,
        "CSVMappingParameters": ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourcesReferenceSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef,
    },
    total=False,
)


class ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourcesReferenceSchemaRecordFormatMappingParametersTypeDef(
    _ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourcesReferenceSchemaRecordFormatMappingParametersTypeDef
):
    """
    Type definition for `ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourcesReferenceSchemaRecordFormat` `MappingParameters`

    When you configure application input at the time of creating or updating an
    application, provides additional mapping information specific to the record format
    (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming
    source.

    - **JSONMappingParameters** *(dict) --*

      Provides additional mapping information when JSON is the record format on the
      streaming source.

      - **RecordRowPath** *(string) --* **[REQUIRED]**

        The path to the top-level parent that contains the records.

    - **CSVMappingParameters** *(dict) --*

      Provides additional mapping information when the record format uses delimiters (for
      example, CSV).

      - **RecordRowDelimiter** *(string) --* **[REQUIRED]**

        The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
        delimiter.

      - **RecordColumnDelimiter** *(string) --* **[REQUIRED]**

        The column delimiter. For example, in a CSV format, a comma (",") is the typical
        column delimiter.
    """


_RequiredClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourcesReferenceSchemaRecordFormatTypeDef = TypedDict(
    "_RequiredClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourcesReferenceSchemaRecordFormatTypeDef",
    {"RecordFormatType": str},
)
_OptionalClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourcesReferenceSchemaRecordFormatTypeDef = TypedDict(
    "_OptionalClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourcesReferenceSchemaRecordFormatTypeDef",
    {
        "MappingParameters": ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourcesReferenceSchemaRecordFormatMappingParametersTypeDef
    },
    total=False,
)


class ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourcesReferenceSchemaRecordFormatTypeDef(
    _RequiredClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourcesReferenceSchemaRecordFormatTypeDef,
    _OptionalClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourcesReferenceSchemaRecordFormatTypeDef,
):
    """
    Type definition for `ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourcesReferenceSchema` `RecordFormat`

    Specifies the format of the records on the streaming source.

    - **RecordFormatType** *(string) --* **[REQUIRED]**

      The type of record format.

    - **MappingParameters** *(dict) --*

      When you configure application input at the time of creating or updating an
      application, provides additional mapping information specific to the record format
      (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming
      source.

      - **JSONMappingParameters** *(dict) --*

        Provides additional mapping information when JSON is the record format on the
        streaming source.

        - **RecordRowPath** *(string) --* **[REQUIRED]**

          The path to the top-level parent that contains the records.

      - **CSVMappingParameters** *(dict) --*

        Provides additional mapping information when the record format uses delimiters (for
        example, CSV).

        - **RecordRowDelimiter** *(string) --* **[REQUIRED]**

          The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
          delimiter.

        - **RecordColumnDelimiter** *(string) --* **[REQUIRED]**

          The column delimiter. For example, in a CSV format, a comma (",") is the typical
          column delimiter.
    """


_RequiredClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourcesReferenceSchemaTypeDef = TypedDict(
    "_RequiredClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourcesReferenceSchemaTypeDef",
    {
        "RecordFormat": ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourcesReferenceSchemaRecordFormatTypeDef,
        "RecordColumns": List[
            ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourcesReferenceSchemaRecordColumnsTypeDef
        ],
    },
)
_OptionalClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourcesReferenceSchemaTypeDef = TypedDict(
    "_OptionalClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourcesReferenceSchemaTypeDef",
    {"RecordEncoding": str},
    total=False,
)


class ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourcesReferenceSchemaTypeDef(
    _RequiredClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourcesReferenceSchemaTypeDef,
    _OptionalClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourcesReferenceSchemaTypeDef,
):
    """
    Type definition for `ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSources` `ReferenceSchema`

    Describes the format of the data in the streaming source, and how each data element maps
    to corresponding columns created in the in-application stream.

    - **RecordFormat** *(dict) --* **[REQUIRED]**

      Specifies the format of the records on the streaming source.

      - **RecordFormatType** *(string) --* **[REQUIRED]**

        The type of record format.

      - **MappingParameters** *(dict) --*

        When you configure application input at the time of creating or updating an
        application, provides additional mapping information specific to the record format
        (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming
        source.

        - **JSONMappingParameters** *(dict) --*

          Provides additional mapping information when JSON is the record format on the
          streaming source.

          - **RecordRowPath** *(string) --* **[REQUIRED]**

            The path to the top-level parent that contains the records.

        - **CSVMappingParameters** *(dict) --*

          Provides additional mapping information when the record format uses delimiters (for
          example, CSV).

          - **RecordRowDelimiter** *(string) --* **[REQUIRED]**

            The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
            delimiter.

          - **RecordColumnDelimiter** *(string) --* **[REQUIRED]**

            The column delimiter. For example, in a CSV format, a comma (",") is the typical
            column delimiter.

    - **RecordEncoding** *(string) --*

      Specifies the encoding of the records in the streaming source. For example, UTF-8.

    - **RecordColumns** *(list) --* **[REQUIRED]**

      A list of ``RecordColumn`` objects.

      - *(dict) --*

        For an SQL-based Amazon Kinesis Data Analytics application, describes the mapping of
        each data element in the streaming source to the corresponding column in the
        in-application stream.

        Also used to describe the format of the reference data source.

        - **Name** *(string) --* **[REQUIRED]**

          The name of the column that is created in the in-application input stream or
          reference table.

        - **Mapping** *(string) --*

          A reference to the data element in the streaming input or the reference data source.

        - **SqlType** *(string) --* **[REQUIRED]**

          The type of column created in the in-application input stream or reference table.
    """


_ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourcesS3ReferenceDataSourceTypeDef = TypedDict(
    "_ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourcesS3ReferenceDataSourceTypeDef",
    {"BucketARN": str, "FileKey": str},
    total=False,
)


class ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourcesS3ReferenceDataSourceTypeDef(
    _ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourcesS3ReferenceDataSourceTypeDef
):
    """
    Type definition for `ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSources` `S3ReferenceDataSource`

    Identifies the S3 bucket and object that contains the reference data. A Kinesis Data
    Analytics application loads reference data only once. If the data changes, you call the
    UpdateApplication operation to trigger reloading of data into your application.

    - **BucketARN** *(string) --*

      The Amazon Resource Name (ARN) of the S3 bucket.

    - **FileKey** *(string) --*

      The object key name containing the reference data.
    """


_RequiredClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourcesTypeDef = TypedDict(
    "_RequiredClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourcesTypeDef",
    {
        "TableName": str,
        "ReferenceSchema": ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourcesReferenceSchemaTypeDef,
    },
)
_OptionalClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourcesTypeDef = TypedDict(
    "_OptionalClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourcesTypeDef",
    {
        "S3ReferenceDataSource": ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourcesS3ReferenceDataSourceTypeDef
    },
    total=False,
)


class ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourcesTypeDef(
    _RequiredClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourcesTypeDef,
    _OptionalClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourcesTypeDef,
):
    """
    Type definition for `ClientCreateApplicationApplicationConfigurationSqlApplicationConfiguration` `ReferenceDataSources`

    For an SQL-based Amazon Kinesis Data Analytics application, describes the reference data
    source by providing the source information (Amazon S3 bucket name and object key name), the
    resulting in-application table name that is created, and the necessary schema to map the
    data elements in the Amazon S3 object to the in-application table.

    - **TableName** *(string) --* **[REQUIRED]**

      The name of the in-application table to create.

    - **S3ReferenceDataSource** *(dict) --*

      Identifies the S3 bucket and object that contains the reference data. A Kinesis Data
      Analytics application loads reference data only once. If the data changes, you call the
      UpdateApplication operation to trigger reloading of data into your application.

      - **BucketARN** *(string) --*

        The Amazon Resource Name (ARN) of the S3 bucket.

      - **FileKey** *(string) --*

        The object key name containing the reference data.

    - **ReferenceSchema** *(dict) --* **[REQUIRED]**

      Describes the format of the data in the streaming source, and how each data element maps
      to corresponding columns created in the in-application stream.

      - **RecordFormat** *(dict) --* **[REQUIRED]**

        Specifies the format of the records on the streaming source.

        - **RecordFormatType** *(string) --* **[REQUIRED]**

          The type of record format.

        - **MappingParameters** *(dict) --*

          When you configure application input at the time of creating or updating an
          application, provides additional mapping information specific to the record format
          (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming
          source.

          - **JSONMappingParameters** *(dict) --*

            Provides additional mapping information when JSON is the record format on the
            streaming source.

            - **RecordRowPath** *(string) --* **[REQUIRED]**

              The path to the top-level parent that contains the records.

          - **CSVMappingParameters** *(dict) --*

            Provides additional mapping information when the record format uses delimiters (for
            example, CSV).

            - **RecordRowDelimiter** *(string) --* **[REQUIRED]**

              The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
              delimiter.

            - **RecordColumnDelimiter** *(string) --* **[REQUIRED]**

              The column delimiter. For example, in a CSV format, a comma (",") is the typical
              column delimiter.

      - **RecordEncoding** *(string) --*

        Specifies the encoding of the records in the streaming source. For example, UTF-8.

      - **RecordColumns** *(list) --* **[REQUIRED]**

        A list of ``RecordColumn`` objects.

        - *(dict) --*

          For an SQL-based Amazon Kinesis Data Analytics application, describes the mapping of
          each data element in the streaming source to the corresponding column in the
          in-application stream.

          Also used to describe the format of the reference data source.

          - **Name** *(string) --* **[REQUIRED]**

            The name of the column that is created in the in-application input stream or
            reference table.

          - **Mapping** *(string) --*

            A reference to the data element in the streaming input or the reference data source.

          - **SqlType** *(string) --* **[REQUIRED]**

            The type of column created in the in-application input stream or reference table.
    """


_ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationTypeDef = TypedDict(
    "_ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationTypeDef",
    {
        "Inputs": List[
            ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationInputsTypeDef
        ],
        "Outputs": List[
            ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationOutputsTypeDef
        ],
        "ReferenceDataSources": List[
            ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourcesTypeDef
        ],
    },
    total=False,
)


class ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationTypeDef(
    _ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationTypeDef
):
    """
    Type definition for `ClientCreateApplicationApplicationConfiguration` `SqlApplicationConfiguration`

    The creation and update parameters for an SQL-based Kinesis Data Analytics application.

    - **Inputs** *(list) --*

      The array of  Input objects describing the input streams used by the application.

      - *(dict) --*

        When you configure the application input for an SQL-based Amazon Kinesis Data Analytics
        application, you specify the streaming source, the in-application stream name that is
        created, and the mapping between the two.

        - **NamePrefix** *(string) --* **[REQUIRED]**

          The name prefix to use when creating an in-application stream. Suppose that you specify a
          prefix "``MyInApplicationStream`` ." Kinesis Data Analytics then creates one or more (as
          per the ``InputParallelism`` count you specified) in-application streams with the names
          "``MyInApplicationStream_001`` ," "``MyInApplicationStream_002`` ," and so on.

        - **InputProcessingConfiguration** *(dict) --*

          The  InputProcessingConfiguration for the input. An input processor transforms records as
          they are received from the stream, before the application's SQL code executes. Currently,
          the only input processing configuration available is  InputLambdaProcessor .

          - **InputLambdaProcessor** *(dict) --* **[REQUIRED]**

            The  InputLambdaProcessor that is used to preprocess the records in the stream before
            being processed by your application code.

            - **ResourceARN** *(string) --* **[REQUIRED]**

              The ARN of the AWS Lambda function that operates on records in the stream.

              .. note::

                To specify an earlier version of the Lambda function than the latest, include the
                Lambda function version in the Lambda function ARN. For more information about
                Lambda ARNs, see `Example ARNs\\: AWS Lambda
                </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__

        - **KinesisStreamsInput** *(dict) --*

          If the streaming source is an Amazon Kinesis data stream, identifies the stream's Amazon
          Resource Name (ARN).

          - **ResourceARN** *(string) --* **[REQUIRED]**

            The ARN of the input Kinesis data stream to read.

        - **KinesisFirehoseInput** *(dict) --*

          If the streaming source is an Amazon Kinesis Data Firehose delivery stream, identifies
          the delivery stream's ARN.

          - **ResourceARN** *(string) --* **[REQUIRED]**

            The Amazon Resource Name (ARN) of the delivery stream.

        - **InputParallelism** *(dict) --*

          Describes the number of in-application streams to create.

          - **Count** *(integer) --*

            The number of in-application streams to create.

        - **InputSchema** *(dict) --* **[REQUIRED]**

          Describes the format of the data in the streaming source, and how each data element maps
          to corresponding columns in the in-application stream that is being created.

          Also used to describe the format of the reference data source.

          - **RecordFormat** *(dict) --* **[REQUIRED]**

            Specifies the format of the records on the streaming source.

            - **RecordFormatType** *(string) --* **[REQUIRED]**

              The type of record format.

            - **MappingParameters** *(dict) --*

              When you configure application input at the time of creating or updating an
              application, provides additional mapping information specific to the record format
              (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming
              source.

              - **JSONMappingParameters** *(dict) --*

                Provides additional mapping information when JSON is the record format on the
                streaming source.

                - **RecordRowPath** *(string) --* **[REQUIRED]**

                  The path to the top-level parent that contains the records.

              - **CSVMappingParameters** *(dict) --*

                Provides additional mapping information when the record format uses delimiters (for
                example, CSV).

                - **RecordRowDelimiter** *(string) --* **[REQUIRED]**

                  The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
                  delimiter.

                - **RecordColumnDelimiter** *(string) --* **[REQUIRED]**

                  The column delimiter. For example, in a CSV format, a comma (",") is the typical
                  column delimiter.

          - **RecordEncoding** *(string) --*

            Specifies the encoding of the records in the streaming source. For example, UTF-8.

          - **RecordColumns** *(list) --* **[REQUIRED]**

            A list of ``RecordColumn`` objects.

            - *(dict) --*

              For an SQL-based Amazon Kinesis Data Analytics application, describes the mapping of
              each data element in the streaming source to the corresponding column in the
              in-application stream.

              Also used to describe the format of the reference data source.

              - **Name** *(string) --* **[REQUIRED]**

                The name of the column that is created in the in-application input stream or
                reference table.

              - **Mapping** *(string) --*

                A reference to the data element in the streaming input or the reference data source.

              - **SqlType** *(string) --* **[REQUIRED]**

                The type of column created in the in-application input stream or reference table.

    - **Outputs** *(list) --*

      The array of  Output objects describing the destination streams used by the application.

      - *(dict) --*

        Describes an SQL-based Amazon Kinesis Data Analytics application's output configuration, in
        which you identify an in-application stream and a destination where you want the
        in-application stream data to be written. The destination can be a Kinesis data stream or a
        Kinesis Data Firehose delivery stream.

        - **Name** *(string) --* **[REQUIRED]**

          The name of the in-application stream.

        - **KinesisStreamsOutput** *(dict) --*

          Identifies an Amazon Kinesis data stream as the destination.

          - **ResourceARN** *(string) --* **[REQUIRED]**

            The ARN of the destination Kinesis data stream to write to.

        - **KinesisFirehoseOutput** *(dict) --*

          Identifies an Amazon Kinesis Data Firehose delivery stream as the destination.

          - **ResourceARN** *(string) --* **[REQUIRED]**

            The ARN of the destination delivery stream to write to.

        - **LambdaOutput** *(dict) --*

          Identifies an AWS Lambda function as the destination.

          - **ResourceARN** *(string) --* **[REQUIRED]**

            The Amazon Resource Name (ARN) of the destination Lambda function to write to.

            .. note::

              To specify an earlier version of the Lambda function than the latest, include the
              Lambda function version in the Lambda function ARN. For more information about Lambda
              ARNs, see `Example ARNs\\: AWS Lambda
              </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__

        - **DestinationSchema** *(dict) --* **[REQUIRED]**

          Describes the data format when records are written to the destination.

          - **RecordFormatType** *(string) --* **[REQUIRED]**

            Specifies the format of the records on the output stream.

    - **ReferenceDataSources** *(list) --*

      The array of  ReferenceDataSource objects describing the reference data sources used by the
      application.

      - *(dict) --*

        For an SQL-based Amazon Kinesis Data Analytics application, describes the reference data
        source by providing the source information (Amazon S3 bucket name and object key name), the
        resulting in-application table name that is created, and the necessary schema to map the
        data elements in the Amazon S3 object to the in-application table.

        - **TableName** *(string) --* **[REQUIRED]**

          The name of the in-application table to create.

        - **S3ReferenceDataSource** *(dict) --*

          Identifies the S3 bucket and object that contains the reference data. A Kinesis Data
          Analytics application loads reference data only once. If the data changes, you call the
          UpdateApplication operation to trigger reloading of data into your application.

          - **BucketARN** *(string) --*

            The Amazon Resource Name (ARN) of the S3 bucket.

          - **FileKey** *(string) --*

            The object key name containing the reference data.

        - **ReferenceSchema** *(dict) --* **[REQUIRED]**

          Describes the format of the data in the streaming source, and how each data element maps
          to corresponding columns created in the in-application stream.

          - **RecordFormat** *(dict) --* **[REQUIRED]**

            Specifies the format of the records on the streaming source.

            - **RecordFormatType** *(string) --* **[REQUIRED]**

              The type of record format.

            - **MappingParameters** *(dict) --*

              When you configure application input at the time of creating or updating an
              application, provides additional mapping information specific to the record format
              (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming
              source.

              - **JSONMappingParameters** *(dict) --*

                Provides additional mapping information when JSON is the record format on the
                streaming source.

                - **RecordRowPath** *(string) --* **[REQUIRED]**

                  The path to the top-level parent that contains the records.

              - **CSVMappingParameters** *(dict) --*

                Provides additional mapping information when the record format uses delimiters (for
                example, CSV).

                - **RecordRowDelimiter** *(string) --* **[REQUIRED]**

                  The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
                  delimiter.

                - **RecordColumnDelimiter** *(string) --* **[REQUIRED]**

                  The column delimiter. For example, in a CSV format, a comma (",") is the typical
                  column delimiter.

          - **RecordEncoding** *(string) --*

            Specifies the encoding of the records in the streaming source. For example, UTF-8.

          - **RecordColumns** *(list) --* **[REQUIRED]**

            A list of ``RecordColumn`` objects.

            - *(dict) --*

              For an SQL-based Amazon Kinesis Data Analytics application, describes the mapping of
              each data element in the streaming source to the corresponding column in the
              in-application stream.

              Also used to describe the format of the reference data source.

              - **Name** *(string) --* **[REQUIRED]**

                The name of the column that is created in the in-application input stream or
                reference table.

              - **Mapping** *(string) --*

                A reference to the data element in the streaming input or the reference data source.

              - **SqlType** *(string) --* **[REQUIRED]**

                The type of column created in the in-application input stream or reference table.
    """


_RequiredClientCreateApplicationApplicationConfigurationTypeDef = TypedDict(
    "_RequiredClientCreateApplicationApplicationConfigurationTypeDef",
    {
        "ApplicationCodeConfiguration": ClientCreateApplicationApplicationConfigurationApplicationCodeConfigurationTypeDef
    },
)
_OptionalClientCreateApplicationApplicationConfigurationTypeDef = TypedDict(
    "_OptionalClientCreateApplicationApplicationConfigurationTypeDef",
    {
        "SqlApplicationConfiguration": ClientCreateApplicationApplicationConfigurationSqlApplicationConfigurationTypeDef,
        "FlinkApplicationConfiguration": ClientCreateApplicationApplicationConfigurationFlinkApplicationConfigurationTypeDef,
        "EnvironmentProperties": ClientCreateApplicationApplicationConfigurationEnvironmentPropertiesTypeDef,
        "ApplicationSnapshotConfiguration": ClientCreateApplicationApplicationConfigurationApplicationSnapshotConfigurationTypeDef,
    },
    total=False,
)


class ClientCreateApplicationApplicationConfigurationTypeDef(
    _RequiredClientCreateApplicationApplicationConfigurationTypeDef,
    _OptionalClientCreateApplicationApplicationConfigurationTypeDef,
):
    """
    Type definition for `ClientCreateApplication` `ApplicationConfiguration`

    Use this parameter to configure the application.

    - **SqlApplicationConfiguration** *(dict) --*

      The creation and update parameters for an SQL-based Kinesis Data Analytics application.

      - **Inputs** *(list) --*

        The array of  Input objects describing the input streams used by the application.

        - *(dict) --*

          When you configure the application input for an SQL-based Amazon Kinesis Data Analytics
          application, you specify the streaming source, the in-application stream name that is
          created, and the mapping between the two.

          - **NamePrefix** *(string) --* **[REQUIRED]**

            The name prefix to use when creating an in-application stream. Suppose that you specify a
            prefix "``MyInApplicationStream`` ." Kinesis Data Analytics then creates one or more (as
            per the ``InputParallelism`` count you specified) in-application streams with the names
            "``MyInApplicationStream_001`` ," "``MyInApplicationStream_002`` ," and so on.

          - **InputProcessingConfiguration** *(dict) --*

            The  InputProcessingConfiguration for the input. An input processor transforms records as
            they are received from the stream, before the application's SQL code executes. Currently,
            the only input processing configuration available is  InputLambdaProcessor .

            - **InputLambdaProcessor** *(dict) --* **[REQUIRED]**

              The  InputLambdaProcessor that is used to preprocess the records in the stream before
              being processed by your application code.

              - **ResourceARN** *(string) --* **[REQUIRED]**

                The ARN of the AWS Lambda function that operates on records in the stream.

                .. note::

                  To specify an earlier version of the Lambda function than the latest, include the
                  Lambda function version in the Lambda function ARN. For more information about
                  Lambda ARNs, see `Example ARNs\\: AWS Lambda
                  </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__

          - **KinesisStreamsInput** *(dict) --*

            If the streaming source is an Amazon Kinesis data stream, identifies the stream's Amazon
            Resource Name (ARN).

            - **ResourceARN** *(string) --* **[REQUIRED]**

              The ARN of the input Kinesis data stream to read.

          - **KinesisFirehoseInput** *(dict) --*

            If the streaming source is an Amazon Kinesis Data Firehose delivery stream, identifies
            the delivery stream's ARN.

            - **ResourceARN** *(string) --* **[REQUIRED]**

              The Amazon Resource Name (ARN) of the delivery stream.

          - **InputParallelism** *(dict) --*

            Describes the number of in-application streams to create.

            - **Count** *(integer) --*

              The number of in-application streams to create.

          - **InputSchema** *(dict) --* **[REQUIRED]**

            Describes the format of the data in the streaming source, and how each data element maps
            to corresponding columns in the in-application stream that is being created.

            Also used to describe the format of the reference data source.

            - **RecordFormat** *(dict) --* **[REQUIRED]**

              Specifies the format of the records on the streaming source.

              - **RecordFormatType** *(string) --* **[REQUIRED]**

                The type of record format.

              - **MappingParameters** *(dict) --*

                When you configure application input at the time of creating or updating an
                application, provides additional mapping information specific to the record format
                (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming
                source.

                - **JSONMappingParameters** *(dict) --*

                  Provides additional mapping information when JSON is the record format on the
                  streaming source.

                  - **RecordRowPath** *(string) --* **[REQUIRED]**

                    The path to the top-level parent that contains the records.

                - **CSVMappingParameters** *(dict) --*

                  Provides additional mapping information when the record format uses delimiters (for
                  example, CSV).

                  - **RecordRowDelimiter** *(string) --* **[REQUIRED]**

                    The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
                    delimiter.

                  - **RecordColumnDelimiter** *(string) --* **[REQUIRED]**

                    The column delimiter. For example, in a CSV format, a comma (",") is the typical
                    column delimiter.

            - **RecordEncoding** *(string) --*

              Specifies the encoding of the records in the streaming source. For example, UTF-8.

            - **RecordColumns** *(list) --* **[REQUIRED]**

              A list of ``RecordColumn`` objects.

              - *(dict) --*

                For an SQL-based Amazon Kinesis Data Analytics application, describes the mapping of
                each data element in the streaming source to the corresponding column in the
                in-application stream.

                Also used to describe the format of the reference data source.

                - **Name** *(string) --* **[REQUIRED]**

                  The name of the column that is created in the in-application input stream or
                  reference table.

                - **Mapping** *(string) --*

                  A reference to the data element in the streaming input or the reference data source.

                - **SqlType** *(string) --* **[REQUIRED]**

                  The type of column created in the in-application input stream or reference table.

      - **Outputs** *(list) --*

        The array of  Output objects describing the destination streams used by the application.

        - *(dict) --*

          Describes an SQL-based Amazon Kinesis Data Analytics application's output configuration, in
          which you identify an in-application stream and a destination where you want the
          in-application stream data to be written. The destination can be a Kinesis data stream or a
          Kinesis Data Firehose delivery stream.

          - **Name** *(string) --* **[REQUIRED]**

            The name of the in-application stream.

          - **KinesisStreamsOutput** *(dict) --*

            Identifies an Amazon Kinesis data stream as the destination.

            - **ResourceARN** *(string) --* **[REQUIRED]**

              The ARN of the destination Kinesis data stream to write to.

          - **KinesisFirehoseOutput** *(dict) --*

            Identifies an Amazon Kinesis Data Firehose delivery stream as the destination.

            - **ResourceARN** *(string) --* **[REQUIRED]**

              The ARN of the destination delivery stream to write to.

          - **LambdaOutput** *(dict) --*

            Identifies an AWS Lambda function as the destination.

            - **ResourceARN** *(string) --* **[REQUIRED]**

              The Amazon Resource Name (ARN) of the destination Lambda function to write to.

              .. note::

                To specify an earlier version of the Lambda function than the latest, include the
                Lambda function version in the Lambda function ARN. For more information about Lambda
                ARNs, see `Example ARNs\\: AWS Lambda
                </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__

          - **DestinationSchema** *(dict) --* **[REQUIRED]**

            Describes the data format when records are written to the destination.

            - **RecordFormatType** *(string) --* **[REQUIRED]**

              Specifies the format of the records on the output stream.

      - **ReferenceDataSources** *(list) --*

        The array of  ReferenceDataSource objects describing the reference data sources used by the
        application.

        - *(dict) --*

          For an SQL-based Amazon Kinesis Data Analytics application, describes the reference data
          source by providing the source information (Amazon S3 bucket name and object key name), the
          resulting in-application table name that is created, and the necessary schema to map the
          data elements in the Amazon S3 object to the in-application table.

          - **TableName** *(string) --* **[REQUIRED]**

            The name of the in-application table to create.

          - **S3ReferenceDataSource** *(dict) --*

            Identifies the S3 bucket and object that contains the reference data. A Kinesis Data
            Analytics application loads reference data only once. If the data changes, you call the
            UpdateApplication operation to trigger reloading of data into your application.

            - **BucketARN** *(string) --*

              The Amazon Resource Name (ARN) of the S3 bucket.

            - **FileKey** *(string) --*

              The object key name containing the reference data.

          - **ReferenceSchema** *(dict) --* **[REQUIRED]**

            Describes the format of the data in the streaming source, and how each data element maps
            to corresponding columns created in the in-application stream.

            - **RecordFormat** *(dict) --* **[REQUIRED]**

              Specifies the format of the records on the streaming source.

              - **RecordFormatType** *(string) --* **[REQUIRED]**

                The type of record format.

              - **MappingParameters** *(dict) --*

                When you configure application input at the time of creating or updating an
                application, provides additional mapping information specific to the record format
                (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming
                source.

                - **JSONMappingParameters** *(dict) --*

                  Provides additional mapping information when JSON is the record format on the
                  streaming source.

                  - **RecordRowPath** *(string) --* **[REQUIRED]**

                    The path to the top-level parent that contains the records.

                - **CSVMappingParameters** *(dict) --*

                  Provides additional mapping information when the record format uses delimiters (for
                  example, CSV).

                  - **RecordRowDelimiter** *(string) --* **[REQUIRED]**

                    The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
                    delimiter.

                  - **RecordColumnDelimiter** *(string) --* **[REQUIRED]**

                    The column delimiter. For example, in a CSV format, a comma (",") is the typical
                    column delimiter.

            - **RecordEncoding** *(string) --*

              Specifies the encoding of the records in the streaming source. For example, UTF-8.

            - **RecordColumns** *(list) --* **[REQUIRED]**

              A list of ``RecordColumn`` objects.

              - *(dict) --*

                For an SQL-based Amazon Kinesis Data Analytics application, describes the mapping of
                each data element in the streaming source to the corresponding column in the
                in-application stream.

                Also used to describe the format of the reference data source.

                - **Name** *(string) --* **[REQUIRED]**

                  The name of the column that is created in the in-application input stream or
                  reference table.

                - **Mapping** *(string) --*

                  A reference to the data element in the streaming input or the reference data source.

                - **SqlType** *(string) --* **[REQUIRED]**

                  The type of column created in the in-application input stream or reference table.

    - **FlinkApplicationConfiguration** *(dict) --*

      The creation and update parameters for a Java-based Kinesis Data Analytics application.

      - **CheckpointConfiguration** *(dict) --*

        Describes an application's checkpointing configuration. Checkpointing is the process of
        persisting application state for fault tolerance. For more information, see `Checkpoints for
        Fault Tolerance
        <https://ci.apache.org/projects/flink/flink-docs-release-1.6/concepts/programming-model.html#checkpoints-for-fault-tolerance>`__
        in the `Apache Flink Documentation
        <https://ci.apache.org/projects/flink/flink-docs-release-1.6/>`__ .

        - **ConfigurationType** *(string) --* **[REQUIRED]**

          Describes whether the application uses Amazon Kinesis Data Analytics' default checkpointing
          behavior.

        - **CheckpointingEnabled** *(boolean) --*

          Describes whether checkpointing is enabled for a Java-based Kinesis Data Analytics
          application.

        - **CheckpointInterval** *(integer) --*

          Describes the interval in milliseconds between checkpoint operations.

        - **MinPauseBetweenCheckpoints** *(integer) --*

          Describes the minimum time in milliseconds after a checkpoint operation completes that a
          new checkpoint operation can start. If a checkpoint operation takes longer than the
          ``CheckpointInterval`` , the application otherwise performs continual checkpoint
          operations. For more information, see `Tuning Checkpointing
          <https://ci.apache.org/projects/flink/flink-docs-stable/ops/state/large_state_tuning.html#tuning-checkpointing>`__
          in the `Apache Flink Documentation
          <https://ci.apache.org/projects/flink/flink-docs-release-1.6/>`__ .

      - **MonitoringConfiguration** *(dict) --*

        Describes configuration parameters for Amazon CloudWatch logging for an application.

        - **ConfigurationType** *(string) --* **[REQUIRED]**

          Describes whether to use the default CloudWatch logging configuration for an application.

        - **MetricsLevel** *(string) --*

          Describes the granularity of the CloudWatch Logs for an application.

        - **LogLevel** *(string) --*

          Describes the verbosity of the CloudWatch Logs for an application.

      - **ParallelismConfiguration** *(dict) --*

        Describes parameters for how an application executes multiple tasks simultaneously.

        - **ConfigurationType** *(string) --* **[REQUIRED]**

          Describes whether the application uses the default parallelism for the Kinesis Data
          Analytics service.

        - **Parallelism** *(integer) --*

          Describes the initial number of parallel tasks that a Java-based Kinesis Data Analytics
          application can perform. The Kinesis Data Analytics service can increase this number
          automatically if  ParallelismConfiguration$AutoScalingEnabled is set to ``true`` .

        - **ParallelismPerKPU** *(integer) --*

          Describes the number of parallel tasks that a Java-based Kinesis Data Analytics application
          can perform per Kinesis Processing Unit (KPU) used by the application. For more information
          about KPUs, see `Amazon Kinesis Data Analytics Pricing
          <http://aws.amazon.com/kinesis/data-analytics/pricing/>`__ .

        - **AutoScalingEnabled** *(boolean) --*

          Describes whether the Kinesis Data Analytics service can increase the parallelism of the
          application in response to increased throughput.

    - **EnvironmentProperties** *(dict) --*

      Describes execution properties for a Java-based Kinesis Data Analytics application.

      - **PropertyGroups** *(list) --* **[REQUIRED]**

        Describes the execution property groups.

        - *(dict) --*

          Property key-value pairs passed into a Java-based Kinesis Data Analytics application.

          - **PropertyGroupId** *(string) --* **[REQUIRED]**

            Describes the key of an application execution property key-value pair.

          - **PropertyMap** *(dict) --* **[REQUIRED]**

            Describes the value of an application execution property key-value pair.

            - *(string) --*

              - *(string) --*

    - **ApplicationCodeConfiguration** *(dict) --* **[REQUIRED]**

      The code location and type parameters for a Java-based Kinesis Data Analytics application.

      - **CodeContent** *(dict) --*

        The location and type of the application code.

        - **TextContent** *(string) --*

          The text-format code for a Java-based Kinesis Data Analytics application.

        - **ZipFileContent** *(bytes) --*

          The zip-format code for a Java-based Kinesis Data Analytics application.

        - **S3ContentLocation** *(dict) --*

          Information about the Amazon S3 bucket containing the application code.

          - **BucketARN** *(string) --* **[REQUIRED]**

            The Amazon Resource Name (ARN) for the S3 bucket containing the application code.

          - **FileKey** *(string) --* **[REQUIRED]**

            The file key for the object containing the application code.

          - **ObjectVersion** *(string) --*

            The version of the object containing the application code.

      - **CodeContentType** *(string) --* **[REQUIRED]**

        Specifies whether the code content is in text or zip format.

    - **ApplicationSnapshotConfiguration** *(dict) --*

      Describes whether snapshots are enabled for a Java-based Kinesis Data Analytics application.

      - **SnapshotsEnabled** *(boolean) --* **[REQUIRED]**

        Describes whether snapshots are enabled for a Java-based Kinesis Data Analytics application.
    """


_ClientCreateApplicationCloudWatchLoggingOptionsTypeDef = TypedDict(
    "_ClientCreateApplicationCloudWatchLoggingOptionsTypeDef", {"LogStreamARN": str}
)


class ClientCreateApplicationCloudWatchLoggingOptionsTypeDef(
    _ClientCreateApplicationCloudWatchLoggingOptionsTypeDef
):
    """
    Type definition for `ClientCreateApplication` `CloudWatchLoggingOptions`

    Provides a description of Amazon CloudWatch logging options, including the log stream Amazon
    Resource Name (ARN).

    - **LogStreamARN** *(string) --* **[REQUIRED]**

      The ARN of the CloudWatch log to receive application messages.
    """


_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionApplicationCodeConfigurationDescriptionCodeContentDescriptionS3ApplicationCodeLocationDescriptionTypeDef = TypedDict(
    "_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionApplicationCodeConfigurationDescriptionCodeContentDescriptionS3ApplicationCodeLocationDescriptionTypeDef",
    {"BucketARN": str, "FileKey": str, "ObjectVersion": str},
    total=False,
)


class ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionApplicationCodeConfigurationDescriptionCodeContentDescriptionS3ApplicationCodeLocationDescriptionTypeDef(
    _ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionApplicationCodeConfigurationDescriptionCodeContentDescriptionS3ApplicationCodeLocationDescriptionTypeDef
):
    """
    Type definition for `ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionApplicationCodeConfigurationDescriptionCodeContentDescription` `S3ApplicationCodeLocationDescription`

    The S3 bucket Amazon Resource Name (ARN), file key, and object version of the
    application code stored in Amazon S3.

    - **BucketARN** *(string) --*

      The Amazon Resource Name (ARN) for the S3 bucket containing the application code.

    - **FileKey** *(string) --*

      The file key for the object containing the application code.

    - **ObjectVersion** *(string) --*

      The version of the object containing the application code.
    """


_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionApplicationCodeConfigurationDescriptionCodeContentDescriptionTypeDef = TypedDict(
    "_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionApplicationCodeConfigurationDescriptionCodeContentDescriptionTypeDef",
    {
        "TextContent": str,
        "CodeMD5": str,
        "CodeSize": int,
        "S3ApplicationCodeLocationDescription": ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionApplicationCodeConfigurationDescriptionCodeContentDescriptionS3ApplicationCodeLocationDescriptionTypeDef,
    },
    total=False,
)


class ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionApplicationCodeConfigurationDescriptionCodeContentDescriptionTypeDef(
    _ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionApplicationCodeConfigurationDescriptionCodeContentDescriptionTypeDef
):
    """
    Type definition for `ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionApplicationCodeConfigurationDescription` `CodeContentDescription`

    Describes details about the location and format of the application code.

    - **TextContent** *(string) --*

      The text-format code

    - **CodeMD5** *(string) --*

      The checksum that can be used to validate zip-format code.

    - **CodeSize** *(integer) --*

      The size in bytes of the application code. Can be used to validate zip-format code.

    - **S3ApplicationCodeLocationDescription** *(dict) --*

      The S3 bucket Amazon Resource Name (ARN), file key, and object version of the
      application code stored in Amazon S3.

      - **BucketARN** *(string) --*

        The Amazon Resource Name (ARN) for the S3 bucket containing the application code.

      - **FileKey** *(string) --*

        The file key for the object containing the application code.

      - **ObjectVersion** *(string) --*

        The version of the object containing the application code.
    """


_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionApplicationCodeConfigurationDescriptionTypeDef = TypedDict(
    "_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionApplicationCodeConfigurationDescriptionTypeDef",
    {
        "CodeContentType": str,
        "CodeContentDescription": ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionApplicationCodeConfigurationDescriptionCodeContentDescriptionTypeDef,
    },
    total=False,
)


class ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionApplicationCodeConfigurationDescriptionTypeDef(
    _ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionApplicationCodeConfigurationDescriptionTypeDef
):
    """
    Type definition for `ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescription` `ApplicationCodeConfigurationDescription`

    The details about the application code for a Java-based Kinesis Data Analytics
    application.

    - **CodeContentType** *(string) --*

      Specifies whether the code content is in text or zip format.

    - **CodeContentDescription** *(dict) --*

      Describes details about the location and format of the application code.

      - **TextContent** *(string) --*

        The text-format code

      - **CodeMD5** *(string) --*

        The checksum that can be used to validate zip-format code.

      - **CodeSize** *(integer) --*

        The size in bytes of the application code. Can be used to validate zip-format code.

      - **S3ApplicationCodeLocationDescription** *(dict) --*

        The S3 bucket Amazon Resource Name (ARN), file key, and object version of the
        application code stored in Amazon S3.

        - **BucketARN** *(string) --*

          The Amazon Resource Name (ARN) for the S3 bucket containing the application code.

        - **FileKey** *(string) --*

          The file key for the object containing the application code.

        - **ObjectVersion** *(string) --*

          The version of the object containing the application code.
    """


_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionApplicationSnapshotConfigurationDescriptionTypeDef = TypedDict(
    "_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionApplicationSnapshotConfigurationDescriptionTypeDef",
    {"SnapshotsEnabled": bool},
    total=False,
)


class ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionApplicationSnapshotConfigurationDescriptionTypeDef(
    _ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionApplicationSnapshotConfigurationDescriptionTypeDef
):
    """
    Type definition for `ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescription` `ApplicationSnapshotConfigurationDescription`

    Describes whether snapshots are enabled for a Java-based Kinesis Data Analytics
    application.

    - **SnapshotsEnabled** *(boolean) --*

      Describes whether snapshots are enabled for a Java-based Kinesis Data Analytics
      application.
    """


_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionEnvironmentPropertyDescriptionsPropertyGroupDescriptionsTypeDef = TypedDict(
    "_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionEnvironmentPropertyDescriptionsPropertyGroupDescriptionsTypeDef",
    {"PropertyGroupId": str, "PropertyMap": Dict[str, str]},
    total=False,
)


class ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionEnvironmentPropertyDescriptionsPropertyGroupDescriptionsTypeDef(
    _ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionEnvironmentPropertyDescriptionsPropertyGroupDescriptionsTypeDef
):
    """
    Type definition for `ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionEnvironmentPropertyDescriptions` `PropertyGroupDescriptions`

    Property key-value pairs passed into a Java-based Kinesis Data Analytics application.

    - **PropertyGroupId** *(string) --*

      Describes the key of an application execution property key-value pair.

    - **PropertyMap** *(dict) --*

      Describes the value of an application execution property key-value pair.

      - *(string) --*

        - *(string) --*
    """


_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionEnvironmentPropertyDescriptionsTypeDef = TypedDict(
    "_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionEnvironmentPropertyDescriptionsTypeDef",
    {
        "PropertyGroupDescriptions": List[
            ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionEnvironmentPropertyDescriptionsPropertyGroupDescriptionsTypeDef
        ]
    },
    total=False,
)


class ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionEnvironmentPropertyDescriptionsTypeDef(
    _ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionEnvironmentPropertyDescriptionsTypeDef
):
    """
    Type definition for `ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescription` `EnvironmentPropertyDescriptions`

    Describes execution properties for a Java-based Kinesis Data Analytics application.

    - **PropertyGroupDescriptions** *(list) --*

      Describes the execution property groups.

      - *(dict) --*

        Property key-value pairs passed into a Java-based Kinesis Data Analytics application.

        - **PropertyGroupId** *(string) --*

          Describes the key of an application execution property key-value pair.

        - **PropertyMap** *(dict) --*

          Describes the value of an application execution property key-value pair.

          - *(string) --*

            - *(string) --*
    """


_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionFlinkApplicationConfigurationDescriptionCheckpointConfigurationDescriptionTypeDef = TypedDict(
    "_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionFlinkApplicationConfigurationDescriptionCheckpointConfigurationDescriptionTypeDef",
    {
        "ConfigurationType": str,
        "CheckpointingEnabled": bool,
        "CheckpointInterval": int,
        "MinPauseBetweenCheckpoints": int,
    },
    total=False,
)


class ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionFlinkApplicationConfigurationDescriptionCheckpointConfigurationDescriptionTypeDef(
    _ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionFlinkApplicationConfigurationDescriptionCheckpointConfigurationDescriptionTypeDef
):
    """
    Type definition for `ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionFlinkApplicationConfigurationDescription` `CheckpointConfigurationDescription`

    Describes an application's checkpointing configuration. Checkpointing is the process of
    persisting application state for fault tolerance.

    - **ConfigurationType** *(string) --*

      Describes whether the application uses the default checkpointing behavior in Kinesis
      Data Analytics.

    - **CheckpointingEnabled** *(boolean) --*

      Describes whether checkpointing is enabled for a Java-based Kinesis Data Analytics
      application.

    - **CheckpointInterval** *(integer) --*

      Describes the interval in milliseconds between checkpoint operations.

    - **MinPauseBetweenCheckpoints** *(integer) --*

      Describes the minimum time in milliseconds after a checkpoint operation completes
      that a new checkpoint operation can start.
    """


_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionFlinkApplicationConfigurationDescriptionMonitoringConfigurationDescriptionTypeDef = TypedDict(
    "_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionFlinkApplicationConfigurationDescriptionMonitoringConfigurationDescriptionTypeDef",
    {"ConfigurationType": str, "MetricsLevel": str, "LogLevel": str},
    total=False,
)


class ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionFlinkApplicationConfigurationDescriptionMonitoringConfigurationDescriptionTypeDef(
    _ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionFlinkApplicationConfigurationDescriptionMonitoringConfigurationDescriptionTypeDef
):
    """
    Type definition for `ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionFlinkApplicationConfigurationDescription` `MonitoringConfigurationDescription`

    Describes configuration parameters for Amazon CloudWatch logging for an application.

    - **ConfigurationType** *(string) --*

      Describes whether to use the default CloudWatch logging configuration for an
      application.

    - **MetricsLevel** *(string) --*

      Describes the granularity of the CloudWatch Logs for an application.

    - **LogLevel** *(string) --*

      Describes the verbosity of the CloudWatch Logs for an application.
    """


_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionFlinkApplicationConfigurationDescriptionParallelismConfigurationDescriptionTypeDef = TypedDict(
    "_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionFlinkApplicationConfigurationDescriptionParallelismConfigurationDescriptionTypeDef",
    {
        "ConfigurationType": str,
        "Parallelism": int,
        "ParallelismPerKPU": int,
        "CurrentParallelism": int,
        "AutoScalingEnabled": bool,
    },
    total=False,
)


class ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionFlinkApplicationConfigurationDescriptionParallelismConfigurationDescriptionTypeDef(
    _ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionFlinkApplicationConfigurationDescriptionParallelismConfigurationDescriptionTypeDef
):
    """
    Type definition for `ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionFlinkApplicationConfigurationDescription` `ParallelismConfigurationDescription`

    Describes parameters for how an application executes multiple tasks simultaneously.

    - **ConfigurationType** *(string) --*

      Describes whether the application uses the default parallelism for the Kinesis Data
      Analytics service.

    - **Parallelism** *(integer) --*

      Describes the initial number of parallel tasks that a Java-based Kinesis Data
      Analytics application can perform.

    - **ParallelismPerKPU** *(integer) --*

      Describes the number of parallel tasks that a Java-based Kinesis Data Analytics
      application can perform per Kinesis Processing Unit (KPU) used by the application.

    - **CurrentParallelism** *(integer) --*

      Describes the current number of parallel tasks that a Java-based Kinesis Data
      Analytics application can perform.

    - **AutoScalingEnabled** *(boolean) --*

      Describes whether the Kinesis Data Analytics service can increase the parallelism of
      the application in response to increased throughput.
    """


_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionFlinkApplicationConfigurationDescriptionTypeDef = TypedDict(
    "_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionFlinkApplicationConfigurationDescriptionTypeDef",
    {
        "CheckpointConfigurationDescription": ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionFlinkApplicationConfigurationDescriptionCheckpointConfigurationDescriptionTypeDef,
        "MonitoringConfigurationDescription": ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionFlinkApplicationConfigurationDescriptionMonitoringConfigurationDescriptionTypeDef,
        "ParallelismConfigurationDescription": ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionFlinkApplicationConfigurationDescriptionParallelismConfigurationDescriptionTypeDef,
        "JobPlanDescription": str,
    },
    total=False,
)


class ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionFlinkApplicationConfigurationDescriptionTypeDef(
    _ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionFlinkApplicationConfigurationDescriptionTypeDef
):
    """
    Type definition for `ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescription` `FlinkApplicationConfigurationDescription`

    The details about a Java-based Kinesis Data Analytics application.

    - **CheckpointConfigurationDescription** *(dict) --*

      Describes an application's checkpointing configuration. Checkpointing is the process of
      persisting application state for fault tolerance.

      - **ConfigurationType** *(string) --*

        Describes whether the application uses the default checkpointing behavior in Kinesis
        Data Analytics.

      - **CheckpointingEnabled** *(boolean) --*

        Describes whether checkpointing is enabled for a Java-based Kinesis Data Analytics
        application.

      - **CheckpointInterval** *(integer) --*

        Describes the interval in milliseconds between checkpoint operations.

      - **MinPauseBetweenCheckpoints** *(integer) --*

        Describes the minimum time in milliseconds after a checkpoint operation completes
        that a new checkpoint operation can start.

    - **MonitoringConfigurationDescription** *(dict) --*

      Describes configuration parameters for Amazon CloudWatch logging for an application.

      - **ConfigurationType** *(string) --*

        Describes whether to use the default CloudWatch logging configuration for an
        application.

      - **MetricsLevel** *(string) --*

        Describes the granularity of the CloudWatch Logs for an application.

      - **LogLevel** *(string) --*

        Describes the verbosity of the CloudWatch Logs for an application.

    - **ParallelismConfigurationDescription** *(dict) --*

      Describes parameters for how an application executes multiple tasks simultaneously.

      - **ConfigurationType** *(string) --*

        Describes whether the application uses the default parallelism for the Kinesis Data
        Analytics service.

      - **Parallelism** *(integer) --*

        Describes the initial number of parallel tasks that a Java-based Kinesis Data
        Analytics application can perform.

      - **ParallelismPerKPU** *(integer) --*

        Describes the number of parallel tasks that a Java-based Kinesis Data Analytics
        application can perform per Kinesis Processing Unit (KPU) used by the application.

      - **CurrentParallelism** *(integer) --*

        Describes the current number of parallel tasks that a Java-based Kinesis Data
        Analytics application can perform.

      - **AutoScalingEnabled** *(boolean) --*

        Describes whether the Kinesis Data Analytics service can increase the parallelism of
        the application in response to increased throughput.

    - **JobPlanDescription** *(string) --*

      The job plan for an application. For more information about the job plan, see `Jobs and
      Scheduling
      <https://ci.apache.org/projects/flink/flink-docs-stable/internals/job_scheduling.html>`__
      in the `Apache Flink Documentation
      <https://ci.apache.org/projects/flink/flink-docs-release-1.6/>`__ . To retrieve the job
      plan for the application, use the  DescribeApplicationRequest$IncludeAdditionalDetails
      parameter of the  DescribeApplication operation.
    """


_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionRunConfigurationDescriptionApplicationRestoreConfigurationDescriptionTypeDef = TypedDict(
    "_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionRunConfigurationDescriptionApplicationRestoreConfigurationDescriptionTypeDef",
    {"ApplicationRestoreType": str, "SnapshotName": str},
    total=False,
)


class ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionRunConfigurationDescriptionApplicationRestoreConfigurationDescriptionTypeDef(
    _ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionRunConfigurationDescriptionApplicationRestoreConfigurationDescriptionTypeDef
):
    """
    Type definition for `ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionRunConfigurationDescription` `ApplicationRestoreConfigurationDescription`

    Describes the restore behavior of a restarting application.

    - **ApplicationRestoreType** *(string) --*

      Specifies how the application should be restored.

    - **SnapshotName** *(string) --*

      The identifier of an existing snapshot of application state to use to restart an
      application. The application uses this value if ``RESTORE_FROM_CUSTOM_SNAPSHOT`` is
      specified for the ``ApplicationRestoreType`` .
    """


_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionRunConfigurationDescriptionTypeDef = TypedDict(
    "_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionRunConfigurationDescriptionTypeDef",
    {
        "ApplicationRestoreConfigurationDescription": ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionRunConfigurationDescriptionApplicationRestoreConfigurationDescriptionTypeDef
    },
    total=False,
)


class ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionRunConfigurationDescriptionTypeDef(
    _ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionRunConfigurationDescriptionTypeDef
):
    """
    Type definition for `ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescription` `RunConfigurationDescription`

    The details about the starting properties for a Kinesis Data Analytics application.

    - **ApplicationRestoreConfigurationDescription** *(dict) --*

      Describes the restore behavior of a restarting application.

      - **ApplicationRestoreType** *(string) --*

        Specifies how the application should be restored.

      - **SnapshotName** *(string) --*

        The identifier of an existing snapshot of application state to use to restart an
        application. The application uses this value if ``RESTORE_FROM_CUSTOM_SNAPSHOT`` is
        specified for the ``ApplicationRestoreType`` .
    """


_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputParallelismTypeDef = TypedDict(
    "_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputParallelismTypeDef",
    {"Count": int},
    total=False,
)


class ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputParallelismTypeDef(
    _ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputParallelismTypeDef
):
    """
    Type definition for `ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptions` `InputParallelism`

    Describes the configured parallelism (number of in-application streams mapped to
    the streaming source).

    - **Count** *(integer) --*

      The number of in-application streams to create.
    """


_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputProcessingConfigurationDescriptionInputLambdaProcessorDescriptionTypeDef = TypedDict(
    "_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputProcessingConfigurationDescriptionInputLambdaProcessorDescriptionTypeDef",
    {"ResourceARN": str, "RoleARN": str},
    total=False,
)


class ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputProcessingConfigurationDescriptionInputLambdaProcessorDescriptionTypeDef(
    _ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputProcessingConfigurationDescriptionInputLambdaProcessorDescriptionTypeDef
):
    """
    Type definition for `ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputProcessingConfigurationDescription` `InputLambdaProcessorDescription`

    Provides configuration information about the associated
    InputLambdaProcessorDescription

    - **ResourceARN** *(string) --*

      The ARN of the AWS Lambda function that is used to preprocess the records in
      the stream.

      .. note::

        To specify an earlier version of the Lambda function than the latest, include
        the Lambda function version in the Lambda function ARN. For more information
        about Lambda ARNs, see `Example ARNs\\: AWS Lambda
        </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__

    - **RoleARN** *(string) --*

      The ARN of the IAM role that is used to access the AWS Lambda function.

      .. note::

        Provided for backward compatibility. Applications that are created with the
        current API version have an application-level service execution role rather
        than a resource-level role.
    """


_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputProcessingConfigurationDescriptionTypeDef = TypedDict(
    "_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputProcessingConfigurationDescriptionTypeDef",
    {
        "InputLambdaProcessorDescription": ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputProcessingConfigurationDescriptionInputLambdaProcessorDescriptionTypeDef
    },
    total=False,
)


class ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputProcessingConfigurationDescriptionTypeDef(
    _ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputProcessingConfigurationDescriptionTypeDef
):
    """
    Type definition for `ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptions` `InputProcessingConfigurationDescription`

    The description of the preprocessor that executes on records in this input before
    the application's code is run.

    - **InputLambdaProcessorDescription** *(dict) --*

      Provides configuration information about the associated
      InputLambdaProcessorDescription

      - **ResourceARN** *(string) --*

        The ARN of the AWS Lambda function that is used to preprocess the records in
        the stream.

        .. note::

          To specify an earlier version of the Lambda function than the latest, include
          the Lambda function version in the Lambda function ARN. For more information
          about Lambda ARNs, see `Example ARNs\\: AWS Lambda
          </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__

      - **RoleARN** *(string) --*

        The ARN of the IAM role that is used to access the AWS Lambda function.

        .. note::

          Provided for backward compatibility. Applications that are created with the
          current API version have an application-level service execution role rather
          than a resource-level role.
    """


_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordColumnsTypeDef = TypedDict(
    "_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordColumnsTypeDef",
    {"Name": str, "Mapping": str, "SqlType": str},
    total=False,
)


class ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordColumnsTypeDef(
    _ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordColumnsTypeDef
):
    """
    Type definition for `ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchema` `RecordColumns`

    For an SQL-based Amazon Kinesis Data Analytics application, describes the
    mapping of each data element in the streaming source to the corresponding
    column in the in-application stream.

    Also used to describe the format of the reference data source.

    - **Name** *(string) --*

      The name of the column that is created in the in-application input stream or
      reference table.

    - **Mapping** *(string) --*

      A reference to the data element in the streaming input or the reference data
      source.

    - **SqlType** *(string) --*

      The type of column created in the in-application input stream or reference
      table.
    """


_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef = TypedDict(
    "_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef",
    {"RecordRowDelimiter": str, "RecordColumnDelimiter": str},
    total=False,
)


class ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef(
    _ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef
):
    """
    Type definition for `ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordFormatMappingParameters` `CSVMappingParameters`

    Provides additional mapping information when the record format uses
    delimiters (for example, CSV).

    - **RecordRowDelimiter** *(string) --*

      The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
      delimiter.

    - **RecordColumnDelimiter** *(string) --*

      The column delimiter. For example, in a CSV format, a comma (",") is the
      typical column delimiter.
    """


_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef = TypedDict(
    "_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef",
    {"RecordRowPath": str},
    total=False,
)


class ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef(
    _ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef
):
    """
    Type definition for `ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordFormatMappingParameters` `JSONMappingParameters`

    Provides additional mapping information when JSON is the record format on the
    streaming source.

    - **RecordRowPath** *(string) --*

      The path to the top-level parent that contains the records.
    """


_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordFormatMappingParametersTypeDef = TypedDict(
    "_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordFormatMappingParametersTypeDef",
    {
        "JSONMappingParameters": ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef,
        "CSVMappingParameters": ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef,
    },
    total=False,
)


class ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordFormatMappingParametersTypeDef(
    _ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordFormatMappingParametersTypeDef
):
    """
    Type definition for `ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordFormat` `MappingParameters`

    When you configure application input at the time of creating or updating an
    application, provides additional mapping information specific to the record
    format (such as JSON, CSV, or record fields delimited by some delimiter) on the
    streaming source.

    - **JSONMappingParameters** *(dict) --*

      Provides additional mapping information when JSON is the record format on the
      streaming source.

      - **RecordRowPath** *(string) --*

        The path to the top-level parent that contains the records.

    - **CSVMappingParameters** *(dict) --*

      Provides additional mapping information when the record format uses
      delimiters (for example, CSV).

      - **RecordRowDelimiter** *(string) --*

        The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
        delimiter.

      - **RecordColumnDelimiter** *(string) --*

        The column delimiter. For example, in a CSV format, a comma (",") is the
        typical column delimiter.
    """


_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordFormatTypeDef = TypedDict(
    "_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordFormatTypeDef",
    {
        "RecordFormatType": str,
        "MappingParameters": ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordFormatMappingParametersTypeDef,
    },
    total=False,
)


class ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordFormatTypeDef(
    _ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordFormatTypeDef
):
    """
    Type definition for `ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchema` `RecordFormat`

    Specifies the format of the records on the streaming source.

    - **RecordFormatType** *(string) --*

      The type of record format.

    - **MappingParameters** *(dict) --*

      When you configure application input at the time of creating or updating an
      application, provides additional mapping information specific to the record
      format (such as JSON, CSV, or record fields delimited by some delimiter) on the
      streaming source.

      - **JSONMappingParameters** *(dict) --*

        Provides additional mapping information when JSON is the record format on the
        streaming source.

        - **RecordRowPath** *(string) --*

          The path to the top-level parent that contains the records.

      - **CSVMappingParameters** *(dict) --*

        Provides additional mapping information when the record format uses
        delimiters (for example, CSV).

        - **RecordRowDelimiter** *(string) --*

          The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
          delimiter.

        - **RecordColumnDelimiter** *(string) --*

          The column delimiter. For example, in a CSV format, a comma (",") is the
          typical column delimiter.
    """


_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaTypeDef = TypedDict(
    "_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaTypeDef",
    {
        "RecordFormat": ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordFormatTypeDef,
        "RecordEncoding": str,
        "RecordColumns": List[
            ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordColumnsTypeDef
        ],
    },
    total=False,
)


class ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaTypeDef(
    _ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaTypeDef
):
    """
    Type definition for `ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptions` `InputSchema`

    Describes the format of the data in the streaming source, and how each data element
    maps to corresponding columns in the in-application stream that is being created.

    - **RecordFormat** *(dict) --*

      Specifies the format of the records on the streaming source.

      - **RecordFormatType** *(string) --*

        The type of record format.

      - **MappingParameters** *(dict) --*

        When you configure application input at the time of creating or updating an
        application, provides additional mapping information specific to the record
        format (such as JSON, CSV, or record fields delimited by some delimiter) on the
        streaming source.

        - **JSONMappingParameters** *(dict) --*

          Provides additional mapping information when JSON is the record format on the
          streaming source.

          - **RecordRowPath** *(string) --*

            The path to the top-level parent that contains the records.

        - **CSVMappingParameters** *(dict) --*

          Provides additional mapping information when the record format uses
          delimiters (for example, CSV).

          - **RecordRowDelimiter** *(string) --*

            The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
            delimiter.

          - **RecordColumnDelimiter** *(string) --*

            The column delimiter. For example, in a CSV format, a comma (",") is the
            typical column delimiter.

    - **RecordEncoding** *(string) --*

      Specifies the encoding of the records in the streaming source. For example, UTF-8.

    - **RecordColumns** *(list) --*

      A list of ``RecordColumn`` objects.

      - *(dict) --*

        For an SQL-based Amazon Kinesis Data Analytics application, describes the
        mapping of each data element in the streaming source to the corresponding
        column in the in-application stream.

        Also used to describe the format of the reference data source.

        - **Name** *(string) --*

          The name of the column that is created in the in-application input stream or
          reference table.

        - **Mapping** *(string) --*

          A reference to the data element in the streaming input or the reference data
          source.

        - **SqlType** *(string) --*

          The type of column created in the in-application input stream or reference
          table.
    """


_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputStartingPositionConfigurationTypeDef = TypedDict(
    "_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputStartingPositionConfigurationTypeDef",
    {"InputStartingPosition": str},
    total=False,
)


class ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputStartingPositionConfigurationTypeDef(
    _ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputStartingPositionConfigurationTypeDef
):
    """
    Type definition for `ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptions` `InputStartingPositionConfiguration`

    The point at which the application is configured to read from the input stream.

    - **InputStartingPosition** *(string) --*

      The starting position on the stream.

      * ``NOW`` - Start reading just after the most recent record in the stream, and
      start at the request timestamp that the customer issued.

      * ``TRIM_HORIZON`` - Start reading at the last untrimmed record in the stream,
      which is the oldest record available in the stream. This option is not available
      for an Amazon Kinesis Data Firehose delivery stream.

      * ``LAST_STOPPED_POINT`` - Resume reading from where the application last stopped
      reading.
    """


_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsKinesisFirehoseInputDescriptionTypeDef = TypedDict(
    "_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsKinesisFirehoseInputDescriptionTypeDef",
    {"ResourceARN": str, "RoleARN": str},
    total=False,
)


class ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsKinesisFirehoseInputDescriptionTypeDef(
    _ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsKinesisFirehoseInputDescriptionTypeDef
):
    """
    Type definition for `ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptions` `KinesisFirehoseInputDescription`

    If a Kinesis Data Firehose delivery stream is configured as a streaming source,
    provides the delivery stream's ARN.

    - **ResourceARN** *(string) --*

      The Amazon Resource Name (ARN) of the delivery stream.

    - **RoleARN** *(string) --*

      The ARN of the IAM role that Kinesis Data Analytics assumes to access the stream.

      .. note::

        Provided for backward compatibility. Applications that are created with the
        current API version have an application-level service execution role rather
        than a resource-level role.
    """


_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsKinesisStreamsInputDescriptionTypeDef = TypedDict(
    "_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsKinesisStreamsInputDescriptionTypeDef",
    {"ResourceARN": str, "RoleARN": str},
    total=False,
)


class ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsKinesisStreamsInputDescriptionTypeDef(
    _ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsKinesisStreamsInputDescriptionTypeDef
):
    """
    Type definition for `ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptions` `KinesisStreamsInputDescription`

    If a Kinesis data stream is configured as a streaming source, provides the Kinesis
    data stream's Amazon Resource Name (ARN).

    - **ResourceARN** *(string) --*

      The Amazon Resource Name (ARN) of the Kinesis data stream.

    - **RoleARN** *(string) --*

      The ARN of the IAM role that Kinesis Data Analytics can assume to access the
      stream.

      .. note::

        Provided for backward compatibility. Applications that are created with the
        current API version have an application-level service execution role rather
        than a resource-level role.
    """


_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsTypeDef = TypedDict(
    "_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsTypeDef",
    {
        "InputId": str,
        "NamePrefix": str,
        "InAppStreamNames": List[str],
        "InputProcessingConfigurationDescription": ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputProcessingConfigurationDescriptionTypeDef,
        "KinesisStreamsInputDescription": ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsKinesisStreamsInputDescriptionTypeDef,
        "KinesisFirehoseInputDescription": ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsKinesisFirehoseInputDescriptionTypeDef,
        "InputSchema": ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaTypeDef,
        "InputParallelism": ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputParallelismTypeDef,
        "InputStartingPositionConfiguration": ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputStartingPositionConfigurationTypeDef,
    },
    total=False,
)


class ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsTypeDef(
    _ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsTypeDef
):
    """
    Type definition for `ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescription` `InputDescriptions`

    Describes the application input configuration for an SQL-based Amazon Kinesis Data
    Analytics application.

    - **InputId** *(string) --*

      The input ID that is associated with the application input. This is the ID that
      Kinesis Data Analytics assigns to each input configuration that you add to your
      application.

    - **NamePrefix** *(string) --*

      The in-application name prefix.

    - **InAppStreamNames** *(list) --*

      Returns the in-application stream names that are mapped to the stream source.

      - *(string) --*

    - **InputProcessingConfigurationDescription** *(dict) --*

      The description of the preprocessor that executes on records in this input before
      the application's code is run.

      - **InputLambdaProcessorDescription** *(dict) --*

        Provides configuration information about the associated
        InputLambdaProcessorDescription

        - **ResourceARN** *(string) --*

          The ARN of the AWS Lambda function that is used to preprocess the records in
          the stream.

          .. note::

            To specify an earlier version of the Lambda function than the latest, include
            the Lambda function version in the Lambda function ARN. For more information
            about Lambda ARNs, see `Example ARNs\\: AWS Lambda
            </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__

        - **RoleARN** *(string) --*

          The ARN of the IAM role that is used to access the AWS Lambda function.

          .. note::

            Provided for backward compatibility. Applications that are created with the
            current API version have an application-level service execution role rather
            than a resource-level role.

    - **KinesisStreamsInputDescription** *(dict) --*

      If a Kinesis data stream is configured as a streaming source, provides the Kinesis
      data stream's Amazon Resource Name (ARN).

      - **ResourceARN** *(string) --*

        The Amazon Resource Name (ARN) of the Kinesis data stream.

      - **RoleARN** *(string) --*

        The ARN of the IAM role that Kinesis Data Analytics can assume to access the
        stream.

        .. note::

          Provided for backward compatibility. Applications that are created with the
          current API version have an application-level service execution role rather
          than a resource-level role.

    - **KinesisFirehoseInputDescription** *(dict) --*

      If a Kinesis Data Firehose delivery stream is configured as a streaming source,
      provides the delivery stream's ARN.

      - **ResourceARN** *(string) --*

        The Amazon Resource Name (ARN) of the delivery stream.

      - **RoleARN** *(string) --*

        The ARN of the IAM role that Kinesis Data Analytics assumes to access the stream.

        .. note::

          Provided for backward compatibility. Applications that are created with the
          current API version have an application-level service execution role rather
          than a resource-level role.

    - **InputSchema** *(dict) --*

      Describes the format of the data in the streaming source, and how each data element
      maps to corresponding columns in the in-application stream that is being created.

      - **RecordFormat** *(dict) --*

        Specifies the format of the records on the streaming source.

        - **RecordFormatType** *(string) --*

          The type of record format.

        - **MappingParameters** *(dict) --*

          When you configure application input at the time of creating or updating an
          application, provides additional mapping information specific to the record
          format (such as JSON, CSV, or record fields delimited by some delimiter) on the
          streaming source.

          - **JSONMappingParameters** *(dict) --*

            Provides additional mapping information when JSON is the record format on the
            streaming source.

            - **RecordRowPath** *(string) --*

              The path to the top-level parent that contains the records.

          - **CSVMappingParameters** *(dict) --*

            Provides additional mapping information when the record format uses
            delimiters (for example, CSV).

            - **RecordRowDelimiter** *(string) --*

              The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
              delimiter.

            - **RecordColumnDelimiter** *(string) --*

              The column delimiter. For example, in a CSV format, a comma (",") is the
              typical column delimiter.

      - **RecordEncoding** *(string) --*

        Specifies the encoding of the records in the streaming source. For example, UTF-8.

      - **RecordColumns** *(list) --*

        A list of ``RecordColumn`` objects.

        - *(dict) --*

          For an SQL-based Amazon Kinesis Data Analytics application, describes the
          mapping of each data element in the streaming source to the corresponding
          column in the in-application stream.

          Also used to describe the format of the reference data source.

          - **Name** *(string) --*

            The name of the column that is created in the in-application input stream or
            reference table.

          - **Mapping** *(string) --*

            A reference to the data element in the streaming input or the reference data
            source.

          - **SqlType** *(string) --*

            The type of column created in the in-application input stream or reference
            table.

    - **InputParallelism** *(dict) --*

      Describes the configured parallelism (number of in-application streams mapped to
      the streaming source).

      - **Count** *(integer) --*

        The number of in-application streams to create.

    - **InputStartingPositionConfiguration** *(dict) --*

      The point at which the application is configured to read from the input stream.

      - **InputStartingPosition** *(string) --*

        The starting position on the stream.

        * ``NOW`` - Start reading just after the most recent record in the stream, and
        start at the request timestamp that the customer issued.

        * ``TRIM_HORIZON`` - Start reading at the last untrimmed record in the stream,
        which is the oldest record available in the stream. This option is not available
        for an Amazon Kinesis Data Firehose delivery stream.

        * ``LAST_STOPPED_POINT`` - Resume reading from where the application last stopped
        reading.
    """


_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptionsDestinationSchemaTypeDef = TypedDict(
    "_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptionsDestinationSchemaTypeDef",
    {"RecordFormatType": str},
    total=False,
)


class ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptionsDestinationSchemaTypeDef(
    _ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptionsDestinationSchemaTypeDef
):
    """
    Type definition for `ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptions` `DestinationSchema`

    The data format used for writing data to the destination.

    - **RecordFormatType** *(string) --*

      Specifies the format of the records on the output stream.
    """


_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptionsKinesisFirehoseOutputDescriptionTypeDef = TypedDict(
    "_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptionsKinesisFirehoseOutputDescriptionTypeDef",
    {"ResourceARN": str, "RoleARN": str},
    total=False,
)


class ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptionsKinesisFirehoseOutputDescriptionTypeDef(
    _ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptionsKinesisFirehoseOutputDescriptionTypeDef
):
    """
    Type definition for `ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptions` `KinesisFirehoseOutputDescription`

    Describes the Kinesis Data Firehose delivery stream that is configured as the
    destination where output is written.

    - **ResourceARN** *(string) --*

      The Amazon Resource Name (ARN) of the delivery stream.

    - **RoleARN** *(string) --*

      The ARN of the IAM role that Kinesis Data Analytics can assume to access the
      stream.

      .. note::

        Provided for backward compatibility. Applications that are created with the
        current API version have an application-level service execution role rather
        than a resource-level role.
    """


_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptionsKinesisStreamsOutputDescriptionTypeDef = TypedDict(
    "_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptionsKinesisStreamsOutputDescriptionTypeDef",
    {"ResourceARN": str, "RoleARN": str},
    total=False,
)


class ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptionsKinesisStreamsOutputDescriptionTypeDef(
    _ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptionsKinesisStreamsOutputDescriptionTypeDef
):
    """
    Type definition for `ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptions` `KinesisStreamsOutputDescription`

    Describes the Kinesis data stream that is configured as the destination where
    output is written.

    - **ResourceARN** *(string) --*

      The Amazon Resource Name (ARN) of the Kinesis data stream.

    - **RoleARN** *(string) --*

      The ARN of the IAM role that Kinesis Data Analytics can assume to access the
      stream.

      .. note::

        Provided for backward compatibility. Applications that are created with the
        current API version have an application-level service execution role rather
        than a resource-level role.
    """


_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptionsLambdaOutputDescriptionTypeDef = TypedDict(
    "_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptionsLambdaOutputDescriptionTypeDef",
    {"ResourceARN": str, "RoleARN": str},
    total=False,
)


class ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptionsLambdaOutputDescriptionTypeDef(
    _ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptionsLambdaOutputDescriptionTypeDef
):
    """
    Type definition for `ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptions` `LambdaOutputDescription`

    Describes the Lambda function that is configured as the destination where output is
    written.

    - **ResourceARN** *(string) --*

      The Amazon Resource Name (ARN) of the destination Lambda function.

    - **RoleARN** *(string) --*

      The ARN of the IAM role that Kinesis Data Analytics can assume to write to the
      destination function.

      .. note::

        Provided for backward compatibility. Applications that are created with the
        current API version have an application-level service execution role rather
        than a resource-level role.
    """


_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptionsTypeDef = TypedDict(
    "_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptionsTypeDef",
    {
        "OutputId": str,
        "Name": str,
        "KinesisStreamsOutputDescription": ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptionsKinesisStreamsOutputDescriptionTypeDef,
        "KinesisFirehoseOutputDescription": ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptionsKinesisFirehoseOutputDescriptionTypeDef,
        "LambdaOutputDescription": ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptionsLambdaOutputDescriptionTypeDef,
        "DestinationSchema": ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptionsDestinationSchemaTypeDef,
    },
    total=False,
)


class ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptionsTypeDef(
    _ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptionsTypeDef
):
    """
    Type definition for `ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescription` `OutputDescriptions`

    For an SQL-based Amazon Kinesis Data Analytics application, describes the application
    output configuration, which includes the in-application stream name and the
    destination where the stream data is written. The destination can be a Kinesis data
    stream or a Kinesis Data Firehose delivery stream.

    - **OutputId** *(string) --*

      A unique identifier for the output configuration.

    - **Name** *(string) --*

      The name of the in-application stream that is configured as output.

    - **KinesisStreamsOutputDescription** *(dict) --*

      Describes the Kinesis data stream that is configured as the destination where
      output is written.

      - **ResourceARN** *(string) --*

        The Amazon Resource Name (ARN) of the Kinesis data stream.

      - **RoleARN** *(string) --*

        The ARN of the IAM role that Kinesis Data Analytics can assume to access the
        stream.

        .. note::

          Provided for backward compatibility. Applications that are created with the
          current API version have an application-level service execution role rather
          than a resource-level role.

    - **KinesisFirehoseOutputDescription** *(dict) --*

      Describes the Kinesis Data Firehose delivery stream that is configured as the
      destination where output is written.

      - **ResourceARN** *(string) --*

        The Amazon Resource Name (ARN) of the delivery stream.

      - **RoleARN** *(string) --*

        The ARN of the IAM role that Kinesis Data Analytics can assume to access the
        stream.

        .. note::

          Provided for backward compatibility. Applications that are created with the
          current API version have an application-level service execution role rather
          than a resource-level role.

    - **LambdaOutputDescription** *(dict) --*

      Describes the Lambda function that is configured as the destination where output is
      written.

      - **ResourceARN** *(string) --*

        The Amazon Resource Name (ARN) of the destination Lambda function.

      - **RoleARN** *(string) --*

        The ARN of the IAM role that Kinesis Data Analytics can assume to write to the
        destination function.

        .. note::

          Provided for backward compatibility. Applications that are created with the
          current API version have an application-level service execution role rather
          than a resource-level role.

    - **DestinationSchema** *(dict) --*

      The data format used for writing data to the destination.

      - **RecordFormatType** *(string) --*

        Specifies the format of the records on the output stream.
    """


_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordColumnsTypeDef = TypedDict(
    "_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordColumnsTypeDef",
    {"Name": str, "Mapping": str, "SqlType": str},
    total=False,
)


class ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordColumnsTypeDef(
    _ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordColumnsTypeDef
):
    """
    Type definition for `ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchema` `RecordColumns`

    For an SQL-based Amazon Kinesis Data Analytics application, describes the
    mapping of each data element in the streaming source to the corresponding
    column in the in-application stream.

    Also used to describe the format of the reference data source.

    - **Name** *(string) --*

      The name of the column that is created in the in-application input stream or
      reference table.

    - **Mapping** *(string) --*

      A reference to the data element in the streaming input or the reference data
      source.

    - **SqlType** *(string) --*

      The type of column created in the in-application input stream or reference
      table.
    """


_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef = TypedDict(
    "_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef",
    {"RecordRowDelimiter": str, "RecordColumnDelimiter": str},
    total=False,
)


class ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef(
    _ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef
):
    """
    Type definition for `ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParameters` `CSVMappingParameters`

    Provides additional mapping information when the record format uses
    delimiters (for example, CSV).

    - **RecordRowDelimiter** *(string) --*

      The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
      delimiter.

    - **RecordColumnDelimiter** *(string) --*

      The column delimiter. For example, in a CSV format, a comma (",") is the
      typical column delimiter.
    """


_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef = TypedDict(
    "_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef",
    {"RecordRowPath": str},
    total=False,
)


class ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef(
    _ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef
):
    """
    Type definition for `ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParameters` `JSONMappingParameters`

    Provides additional mapping information when JSON is the record format on the
    streaming source.

    - **RecordRowPath** *(string) --*

      The path to the top-level parent that contains the records.
    """


_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersTypeDef = TypedDict(
    "_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersTypeDef",
    {
        "JSONMappingParameters": ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef,
        "CSVMappingParameters": ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef,
    },
    total=False,
)


class ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersTypeDef(
    _ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersTypeDef
):
    """
    Type definition for `ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordFormat` `MappingParameters`

    When you configure application input at the time of creating or updating an
    application, provides additional mapping information specific to the record
    format (such as JSON, CSV, or record fields delimited by some delimiter) on the
    streaming source.

    - **JSONMappingParameters** *(dict) --*

      Provides additional mapping information when JSON is the record format on the
      streaming source.

      - **RecordRowPath** *(string) --*

        The path to the top-level parent that contains the records.

    - **CSVMappingParameters** *(dict) --*

      Provides additional mapping information when the record format uses
      delimiters (for example, CSV).

      - **RecordRowDelimiter** *(string) --*

        The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
        delimiter.

      - **RecordColumnDelimiter** *(string) --*

        The column delimiter. For example, in a CSV format, a comma (",") is the
        typical column delimiter.
    """


_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordFormatTypeDef = TypedDict(
    "_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordFormatTypeDef",
    {
        "RecordFormatType": str,
        "MappingParameters": ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersTypeDef,
    },
    total=False,
)


class ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordFormatTypeDef(
    _ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordFormatTypeDef
):
    """
    Type definition for `ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchema` `RecordFormat`

    Specifies the format of the records on the streaming source.

    - **RecordFormatType** *(string) --*

      The type of record format.

    - **MappingParameters** *(dict) --*

      When you configure application input at the time of creating or updating an
      application, provides additional mapping information specific to the record
      format (such as JSON, CSV, or record fields delimited by some delimiter) on the
      streaming source.

      - **JSONMappingParameters** *(dict) --*

        Provides additional mapping information when JSON is the record format on the
        streaming source.

        - **RecordRowPath** *(string) --*

          The path to the top-level parent that contains the records.

      - **CSVMappingParameters** *(dict) --*

        Provides additional mapping information when the record format uses
        delimiters (for example, CSV).

        - **RecordRowDelimiter** *(string) --*

          The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
          delimiter.

        - **RecordColumnDelimiter** *(string) --*

          The column delimiter. For example, in a CSV format, a comma (",") is the
          typical column delimiter.
    """


_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaTypeDef = TypedDict(
    "_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaTypeDef",
    {
        "RecordFormat": ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordFormatTypeDef,
        "RecordEncoding": str,
        "RecordColumns": List[
            ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordColumnsTypeDef
        ],
    },
    total=False,
)


class ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaTypeDef(
    _ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaTypeDef
):
    """
    Type definition for `ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptions` `ReferenceSchema`

    Describes the format of the data in the streaming source, and how each data element
    maps to corresponding columns created in the in-application stream.

    - **RecordFormat** *(dict) --*

      Specifies the format of the records on the streaming source.

      - **RecordFormatType** *(string) --*

        The type of record format.

      - **MappingParameters** *(dict) --*

        When you configure application input at the time of creating or updating an
        application, provides additional mapping information specific to the record
        format (such as JSON, CSV, or record fields delimited by some delimiter) on the
        streaming source.

        - **JSONMappingParameters** *(dict) --*

          Provides additional mapping information when JSON is the record format on the
          streaming source.

          - **RecordRowPath** *(string) --*

            The path to the top-level parent that contains the records.

        - **CSVMappingParameters** *(dict) --*

          Provides additional mapping information when the record format uses
          delimiters (for example, CSV).

          - **RecordRowDelimiter** *(string) --*

            The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
            delimiter.

          - **RecordColumnDelimiter** *(string) --*

            The column delimiter. For example, in a CSV format, a comma (",") is the
            typical column delimiter.

    - **RecordEncoding** *(string) --*

      Specifies the encoding of the records in the streaming source. For example, UTF-8.

    - **RecordColumns** *(list) --*

      A list of ``RecordColumn`` objects.

      - *(dict) --*

        For an SQL-based Amazon Kinesis Data Analytics application, describes the
        mapping of each data element in the streaming source to the corresponding
        column in the in-application stream.

        Also used to describe the format of the reference data source.

        - **Name** *(string) --*

          The name of the column that is created in the in-application input stream or
          reference table.

        - **Mapping** *(string) --*

          A reference to the data element in the streaming input or the reference data
          source.

        - **SqlType** *(string) --*

          The type of column created in the in-application input stream or reference
          table.
    """


_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsS3ReferenceDataSourceDescriptionTypeDef = TypedDict(
    "_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsS3ReferenceDataSourceDescriptionTypeDef",
    {"BucketARN": str, "FileKey": str, "ReferenceRoleARN": str},
    total=False,
)


class ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsS3ReferenceDataSourceDescriptionTypeDef(
    _ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsS3ReferenceDataSourceDescriptionTypeDef
):
    """
    Type definition for `ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptions` `S3ReferenceDataSourceDescription`

    Provides the Amazon S3 bucket name, the object key name that contains the reference
    data.

    - **BucketARN** *(string) --*

      The Amazon Resource Name (ARN) of the S3 bucket.

    - **FileKey** *(string) --*

      Amazon S3 object key name.

    - **ReferenceRoleARN** *(string) --*

      The ARN of the IAM role that Kinesis Data Analytics can assume to read the Amazon
      S3 object on your behalf to populate the in-application reference table.

      .. note::

        Provided for backward compatibility. Applications that are created with the
        current API version have an application-level service execution role rather
        than a resource-level role.
    """


_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsTypeDef = TypedDict(
    "_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsTypeDef",
    {
        "ReferenceId": str,
        "TableName": str,
        "S3ReferenceDataSourceDescription": ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsS3ReferenceDataSourceDescriptionTypeDef,
        "ReferenceSchema": ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaTypeDef,
    },
    total=False,
)


class ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsTypeDef(
    _ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsTypeDef
):
    """
    Type definition for `ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescription` `ReferenceDataSourceDescriptions`

    For an SQL-based Amazon Kinesis Data Analytics application, describes the reference
    data source configured for an application.

    - **ReferenceId** *(string) --*

      The ID of the reference data source. This is the ID that Kinesis Data Analytics
      assigns when you add the reference data source to your application using the
      CreateApplication or  UpdateApplication operation.

    - **TableName** *(string) --*

      The in-application table name created by the specific reference data source
      configuration.

    - **S3ReferenceDataSourceDescription** *(dict) --*

      Provides the Amazon S3 bucket name, the object key name that contains the reference
      data.

      - **BucketARN** *(string) --*

        The Amazon Resource Name (ARN) of the S3 bucket.

      - **FileKey** *(string) --*

        Amazon S3 object key name.

      - **ReferenceRoleARN** *(string) --*

        The ARN of the IAM role that Kinesis Data Analytics can assume to read the Amazon
        S3 object on your behalf to populate the in-application reference table.

        .. note::

          Provided for backward compatibility. Applications that are created with the
          current API version have an application-level service execution role rather
          than a resource-level role.

    - **ReferenceSchema** *(dict) --*

      Describes the format of the data in the streaming source, and how each data element
      maps to corresponding columns created in the in-application stream.

      - **RecordFormat** *(dict) --*

        Specifies the format of the records on the streaming source.

        - **RecordFormatType** *(string) --*

          The type of record format.

        - **MappingParameters** *(dict) --*

          When you configure application input at the time of creating or updating an
          application, provides additional mapping information specific to the record
          format (such as JSON, CSV, or record fields delimited by some delimiter) on the
          streaming source.

          - **JSONMappingParameters** *(dict) --*

            Provides additional mapping information when JSON is the record format on the
            streaming source.

            - **RecordRowPath** *(string) --*

              The path to the top-level parent that contains the records.

          - **CSVMappingParameters** *(dict) --*

            Provides additional mapping information when the record format uses
            delimiters (for example, CSV).

            - **RecordRowDelimiter** *(string) --*

              The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
              delimiter.

            - **RecordColumnDelimiter** *(string) --*

              The column delimiter. For example, in a CSV format, a comma (",") is the
              typical column delimiter.

      - **RecordEncoding** *(string) --*

        Specifies the encoding of the records in the streaming source. For example, UTF-8.

      - **RecordColumns** *(list) --*

        A list of ``RecordColumn`` objects.

        - *(dict) --*

          For an SQL-based Amazon Kinesis Data Analytics application, describes the
          mapping of each data element in the streaming source to the corresponding
          column in the in-application stream.

          Also used to describe the format of the reference data source.

          - **Name** *(string) --*

            The name of the column that is created in the in-application input stream or
            reference table.

          - **Mapping** *(string) --*

            A reference to the data element in the streaming input or the reference data
            source.

          - **SqlType** *(string) --*

            The type of column created in the in-application input stream or reference
            table.
    """


_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionTypeDef = TypedDict(
    "_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionTypeDef",
    {
        "InputDescriptions": List[
            ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsTypeDef
        ],
        "OutputDescriptions": List[
            ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptionsTypeDef
        ],
        "ReferenceDataSourceDescriptions": List[
            ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsTypeDef
        ],
    },
    total=False,
)


class ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionTypeDef(
    _ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionTypeDef
):
    """
    Type definition for `ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescription` `SqlApplicationConfigurationDescription`

    The details about inputs, outputs, and reference data sources for an SQL-based Kinesis
    Data Analytics application.

    - **InputDescriptions** *(list) --*

      The array of  InputDescription objects describing the input streams used by the
      application.

      - *(dict) --*

        Describes the application input configuration for an SQL-based Amazon Kinesis Data
        Analytics application.

        - **InputId** *(string) --*

          The input ID that is associated with the application input. This is the ID that
          Kinesis Data Analytics assigns to each input configuration that you add to your
          application.

        - **NamePrefix** *(string) --*

          The in-application name prefix.

        - **InAppStreamNames** *(list) --*

          Returns the in-application stream names that are mapped to the stream source.

          - *(string) --*

        - **InputProcessingConfigurationDescription** *(dict) --*

          The description of the preprocessor that executes on records in this input before
          the application's code is run.

          - **InputLambdaProcessorDescription** *(dict) --*

            Provides configuration information about the associated
            InputLambdaProcessorDescription

            - **ResourceARN** *(string) --*

              The ARN of the AWS Lambda function that is used to preprocess the records in
              the stream.

              .. note::

                To specify an earlier version of the Lambda function than the latest, include
                the Lambda function version in the Lambda function ARN. For more information
                about Lambda ARNs, see `Example ARNs\\: AWS Lambda
                </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__

            - **RoleARN** *(string) --*

              The ARN of the IAM role that is used to access the AWS Lambda function.

              .. note::

                Provided for backward compatibility. Applications that are created with the
                current API version have an application-level service execution role rather
                than a resource-level role.

        - **KinesisStreamsInputDescription** *(dict) --*

          If a Kinesis data stream is configured as a streaming source, provides the Kinesis
          data stream's Amazon Resource Name (ARN).

          - **ResourceARN** *(string) --*

            The Amazon Resource Name (ARN) of the Kinesis data stream.

          - **RoleARN** *(string) --*

            The ARN of the IAM role that Kinesis Data Analytics can assume to access the
            stream.

            .. note::

              Provided for backward compatibility. Applications that are created with the
              current API version have an application-level service execution role rather
              than a resource-level role.

        - **KinesisFirehoseInputDescription** *(dict) --*

          If a Kinesis Data Firehose delivery stream is configured as a streaming source,
          provides the delivery stream's ARN.

          - **ResourceARN** *(string) --*

            The Amazon Resource Name (ARN) of the delivery stream.

          - **RoleARN** *(string) --*

            The ARN of the IAM role that Kinesis Data Analytics assumes to access the stream.

            .. note::

              Provided for backward compatibility. Applications that are created with the
              current API version have an application-level service execution role rather
              than a resource-level role.

        - **InputSchema** *(dict) --*

          Describes the format of the data in the streaming source, and how each data element
          maps to corresponding columns in the in-application stream that is being created.

          - **RecordFormat** *(dict) --*

            Specifies the format of the records on the streaming source.

            - **RecordFormatType** *(string) --*

              The type of record format.

            - **MappingParameters** *(dict) --*

              When you configure application input at the time of creating or updating an
              application, provides additional mapping information specific to the record
              format (such as JSON, CSV, or record fields delimited by some delimiter) on the
              streaming source.

              - **JSONMappingParameters** *(dict) --*

                Provides additional mapping information when JSON is the record format on the
                streaming source.

                - **RecordRowPath** *(string) --*

                  The path to the top-level parent that contains the records.

              - **CSVMappingParameters** *(dict) --*

                Provides additional mapping information when the record format uses
                delimiters (for example, CSV).

                - **RecordRowDelimiter** *(string) --*

                  The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
                  delimiter.

                - **RecordColumnDelimiter** *(string) --*

                  The column delimiter. For example, in a CSV format, a comma (",") is the
                  typical column delimiter.

          - **RecordEncoding** *(string) --*

            Specifies the encoding of the records in the streaming source. For example, UTF-8.

          - **RecordColumns** *(list) --*

            A list of ``RecordColumn`` objects.

            - *(dict) --*

              For an SQL-based Amazon Kinesis Data Analytics application, describes the
              mapping of each data element in the streaming source to the corresponding
              column in the in-application stream.

              Also used to describe the format of the reference data source.

              - **Name** *(string) --*

                The name of the column that is created in the in-application input stream or
                reference table.

              - **Mapping** *(string) --*

                A reference to the data element in the streaming input or the reference data
                source.

              - **SqlType** *(string) --*

                The type of column created in the in-application input stream or reference
                table.

        - **InputParallelism** *(dict) --*

          Describes the configured parallelism (number of in-application streams mapped to
          the streaming source).

          - **Count** *(integer) --*

            The number of in-application streams to create.

        - **InputStartingPositionConfiguration** *(dict) --*

          The point at which the application is configured to read from the input stream.

          - **InputStartingPosition** *(string) --*

            The starting position on the stream.

            * ``NOW`` - Start reading just after the most recent record in the stream, and
            start at the request timestamp that the customer issued.

            * ``TRIM_HORIZON`` - Start reading at the last untrimmed record in the stream,
            which is the oldest record available in the stream. This option is not available
            for an Amazon Kinesis Data Firehose delivery stream.

            * ``LAST_STOPPED_POINT`` - Resume reading from where the application last stopped
            reading.

    - **OutputDescriptions** *(list) --*

      The array of  OutputDescription objects describing the destination streams used by the
      application.

      - *(dict) --*

        For an SQL-based Amazon Kinesis Data Analytics application, describes the application
        output configuration, which includes the in-application stream name and the
        destination where the stream data is written. The destination can be a Kinesis data
        stream or a Kinesis Data Firehose delivery stream.

        - **OutputId** *(string) --*

          A unique identifier for the output configuration.

        - **Name** *(string) --*

          The name of the in-application stream that is configured as output.

        - **KinesisStreamsOutputDescription** *(dict) --*

          Describes the Kinesis data stream that is configured as the destination where
          output is written.

          - **ResourceARN** *(string) --*

            The Amazon Resource Name (ARN) of the Kinesis data stream.

          - **RoleARN** *(string) --*

            The ARN of the IAM role that Kinesis Data Analytics can assume to access the
            stream.

            .. note::

              Provided for backward compatibility. Applications that are created with the
              current API version have an application-level service execution role rather
              than a resource-level role.

        - **KinesisFirehoseOutputDescription** *(dict) --*

          Describes the Kinesis Data Firehose delivery stream that is configured as the
          destination where output is written.

          - **ResourceARN** *(string) --*

            The Amazon Resource Name (ARN) of the delivery stream.

          - **RoleARN** *(string) --*

            The ARN of the IAM role that Kinesis Data Analytics can assume to access the
            stream.

            .. note::

              Provided for backward compatibility. Applications that are created with the
              current API version have an application-level service execution role rather
              than a resource-level role.

        - **LambdaOutputDescription** *(dict) --*

          Describes the Lambda function that is configured as the destination where output is
          written.

          - **ResourceARN** *(string) --*

            The Amazon Resource Name (ARN) of the destination Lambda function.

          - **RoleARN** *(string) --*

            The ARN of the IAM role that Kinesis Data Analytics can assume to write to the
            destination function.

            .. note::

              Provided for backward compatibility. Applications that are created with the
              current API version have an application-level service execution role rather
              than a resource-level role.

        - **DestinationSchema** *(dict) --*

          The data format used for writing data to the destination.

          - **RecordFormatType** *(string) --*

            Specifies the format of the records on the output stream.

    - **ReferenceDataSourceDescriptions** *(list) --*

      The array of  ReferenceDataSourceDescription objects describing the reference data
      sources used by the application.

      - *(dict) --*

        For an SQL-based Amazon Kinesis Data Analytics application, describes the reference
        data source configured for an application.

        - **ReferenceId** *(string) --*

          The ID of the reference data source. This is the ID that Kinesis Data Analytics
          assigns when you add the reference data source to your application using the
          CreateApplication or  UpdateApplication operation.

        - **TableName** *(string) --*

          The in-application table name created by the specific reference data source
          configuration.

        - **S3ReferenceDataSourceDescription** *(dict) --*

          Provides the Amazon S3 bucket name, the object key name that contains the reference
          data.

          - **BucketARN** *(string) --*

            The Amazon Resource Name (ARN) of the S3 bucket.

          - **FileKey** *(string) --*

            Amazon S3 object key name.

          - **ReferenceRoleARN** *(string) --*

            The ARN of the IAM role that Kinesis Data Analytics can assume to read the Amazon
            S3 object on your behalf to populate the in-application reference table.

            .. note::

              Provided for backward compatibility. Applications that are created with the
              current API version have an application-level service execution role rather
              than a resource-level role.

        - **ReferenceSchema** *(dict) --*

          Describes the format of the data in the streaming source, and how each data element
          maps to corresponding columns created in the in-application stream.

          - **RecordFormat** *(dict) --*

            Specifies the format of the records on the streaming source.

            - **RecordFormatType** *(string) --*

              The type of record format.

            - **MappingParameters** *(dict) --*

              When you configure application input at the time of creating or updating an
              application, provides additional mapping information specific to the record
              format (such as JSON, CSV, or record fields delimited by some delimiter) on the
              streaming source.

              - **JSONMappingParameters** *(dict) --*

                Provides additional mapping information when JSON is the record format on the
                streaming source.

                - **RecordRowPath** *(string) --*

                  The path to the top-level parent that contains the records.

              - **CSVMappingParameters** *(dict) --*

                Provides additional mapping information when the record format uses
                delimiters (for example, CSV).

                - **RecordRowDelimiter** *(string) --*

                  The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
                  delimiter.

                - **RecordColumnDelimiter** *(string) --*

                  The column delimiter. For example, in a CSV format, a comma (",") is the
                  typical column delimiter.

          - **RecordEncoding** *(string) --*

            Specifies the encoding of the records in the streaming source. For example, UTF-8.

          - **RecordColumns** *(list) --*

            A list of ``RecordColumn`` objects.

            - *(dict) --*

              For an SQL-based Amazon Kinesis Data Analytics application, describes the
              mapping of each data element in the streaming source to the corresponding
              column in the in-application stream.

              Also used to describe the format of the reference data source.

              - **Name** *(string) --*

                The name of the column that is created in the in-application input stream or
                reference table.

              - **Mapping** *(string) --*

                A reference to the data element in the streaming input or the reference data
                source.

              - **SqlType** *(string) --*

                The type of column created in the in-application input stream or reference
                table.
    """


_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionTypeDef = TypedDict(
    "_ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionTypeDef",
    {
        "SqlApplicationConfigurationDescription": ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionTypeDef,
        "ApplicationCodeConfigurationDescription": ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionApplicationCodeConfigurationDescriptionTypeDef,
        "RunConfigurationDescription": ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionRunConfigurationDescriptionTypeDef,
        "FlinkApplicationConfigurationDescription": ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionFlinkApplicationConfigurationDescriptionTypeDef,
        "EnvironmentPropertyDescriptions": ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionEnvironmentPropertyDescriptionsTypeDef,
        "ApplicationSnapshotConfigurationDescription": ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionApplicationSnapshotConfigurationDescriptionTypeDef,
    },
    total=False,
)


class ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionTypeDef(
    _ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionTypeDef
):
    """
    Type definition for `ClientCreateApplicationResponseApplicationDetail` `ApplicationConfigurationDescription`

    Provides details about the application's SQL or Java code and starting parameters.

    - **SqlApplicationConfigurationDescription** *(dict) --*

      The details about inputs, outputs, and reference data sources for an SQL-based Kinesis
      Data Analytics application.

      - **InputDescriptions** *(list) --*

        The array of  InputDescription objects describing the input streams used by the
        application.

        - *(dict) --*

          Describes the application input configuration for an SQL-based Amazon Kinesis Data
          Analytics application.

          - **InputId** *(string) --*

            The input ID that is associated with the application input. This is the ID that
            Kinesis Data Analytics assigns to each input configuration that you add to your
            application.

          - **NamePrefix** *(string) --*

            The in-application name prefix.

          - **InAppStreamNames** *(list) --*

            Returns the in-application stream names that are mapped to the stream source.

            - *(string) --*

          - **InputProcessingConfigurationDescription** *(dict) --*

            The description of the preprocessor that executes on records in this input before
            the application's code is run.

            - **InputLambdaProcessorDescription** *(dict) --*

              Provides configuration information about the associated
              InputLambdaProcessorDescription

              - **ResourceARN** *(string) --*

                The ARN of the AWS Lambda function that is used to preprocess the records in
                the stream.

                .. note::

                  To specify an earlier version of the Lambda function than the latest, include
                  the Lambda function version in the Lambda function ARN. For more information
                  about Lambda ARNs, see `Example ARNs\\: AWS Lambda
                  </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__

              - **RoleARN** *(string) --*

                The ARN of the IAM role that is used to access the AWS Lambda function.

                .. note::

                  Provided for backward compatibility. Applications that are created with the
                  current API version have an application-level service execution role rather
                  than a resource-level role.

          - **KinesisStreamsInputDescription** *(dict) --*

            If a Kinesis data stream is configured as a streaming source, provides the Kinesis
            data stream's Amazon Resource Name (ARN).

            - **ResourceARN** *(string) --*

              The Amazon Resource Name (ARN) of the Kinesis data stream.

            - **RoleARN** *(string) --*

              The ARN of the IAM role that Kinesis Data Analytics can assume to access the
              stream.

              .. note::

                Provided for backward compatibility. Applications that are created with the
                current API version have an application-level service execution role rather
                than a resource-level role.

          - **KinesisFirehoseInputDescription** *(dict) --*

            If a Kinesis Data Firehose delivery stream is configured as a streaming source,
            provides the delivery stream's ARN.

            - **ResourceARN** *(string) --*

              The Amazon Resource Name (ARN) of the delivery stream.

            - **RoleARN** *(string) --*

              The ARN of the IAM role that Kinesis Data Analytics assumes to access the stream.

              .. note::

                Provided for backward compatibility. Applications that are created with the
                current API version have an application-level service execution role rather
                than a resource-level role.

          - **InputSchema** *(dict) --*

            Describes the format of the data in the streaming source, and how each data element
            maps to corresponding columns in the in-application stream that is being created.

            - **RecordFormat** *(dict) --*

              Specifies the format of the records on the streaming source.

              - **RecordFormatType** *(string) --*

                The type of record format.

              - **MappingParameters** *(dict) --*

                When you configure application input at the time of creating or updating an
                application, provides additional mapping information specific to the record
                format (such as JSON, CSV, or record fields delimited by some delimiter) on the
                streaming source.

                - **JSONMappingParameters** *(dict) --*

                  Provides additional mapping information when JSON is the record format on the
                  streaming source.

                  - **RecordRowPath** *(string) --*

                    The path to the top-level parent that contains the records.

                - **CSVMappingParameters** *(dict) --*

                  Provides additional mapping information when the record format uses
                  delimiters (for example, CSV).

                  - **RecordRowDelimiter** *(string) --*

                    The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
                    delimiter.

                  - **RecordColumnDelimiter** *(string) --*

                    The column delimiter. For example, in a CSV format, a comma (",") is the
                    typical column delimiter.

            - **RecordEncoding** *(string) --*

              Specifies the encoding of the records in the streaming source. For example, UTF-8.

            - **RecordColumns** *(list) --*

              A list of ``RecordColumn`` objects.

              - *(dict) --*

                For an SQL-based Amazon Kinesis Data Analytics application, describes the
                mapping of each data element in the streaming source to the corresponding
                column in the in-application stream.

                Also used to describe the format of the reference data source.

                - **Name** *(string) --*

                  The name of the column that is created in the in-application input stream or
                  reference table.

                - **Mapping** *(string) --*

                  A reference to the data element in the streaming input or the reference data
                  source.

                - **SqlType** *(string) --*

                  The type of column created in the in-application input stream or reference
                  table.

          - **InputParallelism** *(dict) --*

            Describes the configured parallelism (number of in-application streams mapped to
            the streaming source).

            - **Count** *(integer) --*

              The number of in-application streams to create.

          - **InputStartingPositionConfiguration** *(dict) --*

            The point at which the application is configured to read from the input stream.

            - **InputStartingPosition** *(string) --*

              The starting position on the stream.

              * ``NOW`` - Start reading just after the most recent record in the stream, and
              start at the request timestamp that the customer issued.

              * ``TRIM_HORIZON`` - Start reading at the last untrimmed record in the stream,
              which is the oldest record available in the stream. This option is not available
              for an Amazon Kinesis Data Firehose delivery stream.

              * ``LAST_STOPPED_POINT`` - Resume reading from where the application last stopped
              reading.

      - **OutputDescriptions** *(list) --*

        The array of  OutputDescription objects describing the destination streams used by the
        application.

        - *(dict) --*

          For an SQL-based Amazon Kinesis Data Analytics application, describes the application
          output configuration, which includes the in-application stream name and the
          destination where the stream data is written. The destination can be a Kinesis data
          stream or a Kinesis Data Firehose delivery stream.

          - **OutputId** *(string) --*

            A unique identifier for the output configuration.

          - **Name** *(string) --*

            The name of the in-application stream that is configured as output.

          - **KinesisStreamsOutputDescription** *(dict) --*

            Describes the Kinesis data stream that is configured as the destination where
            output is written.

            - **ResourceARN** *(string) --*

              The Amazon Resource Name (ARN) of the Kinesis data stream.

            - **RoleARN** *(string) --*

              The ARN of the IAM role that Kinesis Data Analytics can assume to access the
              stream.

              .. note::

                Provided for backward compatibility. Applications that are created with the
                current API version have an application-level service execution role rather
                than a resource-level role.

          - **KinesisFirehoseOutputDescription** *(dict) --*

            Describes the Kinesis Data Firehose delivery stream that is configured as the
            destination where output is written.

            - **ResourceARN** *(string) --*

              The Amazon Resource Name (ARN) of the delivery stream.

            - **RoleARN** *(string) --*

              The ARN of the IAM role that Kinesis Data Analytics can assume to access the
              stream.

              .. note::

                Provided for backward compatibility. Applications that are created with the
                current API version have an application-level service execution role rather
                than a resource-level role.

          - **LambdaOutputDescription** *(dict) --*

            Describes the Lambda function that is configured as the destination where output is
            written.

            - **ResourceARN** *(string) --*

              The Amazon Resource Name (ARN) of the destination Lambda function.

            - **RoleARN** *(string) --*

              The ARN of the IAM role that Kinesis Data Analytics can assume to write to the
              destination function.

              .. note::

                Provided for backward compatibility. Applications that are created with the
                current API version have an application-level service execution role rather
                than a resource-level role.

          - **DestinationSchema** *(dict) --*

            The data format used for writing data to the destination.

            - **RecordFormatType** *(string) --*

              Specifies the format of the records on the output stream.

      - **ReferenceDataSourceDescriptions** *(list) --*

        The array of  ReferenceDataSourceDescription objects describing the reference data
        sources used by the application.

        - *(dict) --*

          For an SQL-based Amazon Kinesis Data Analytics application, describes the reference
          data source configured for an application.

          - **ReferenceId** *(string) --*

            The ID of the reference data source. This is the ID that Kinesis Data Analytics
            assigns when you add the reference data source to your application using the
            CreateApplication or  UpdateApplication operation.

          - **TableName** *(string) --*

            The in-application table name created by the specific reference data source
            configuration.

          - **S3ReferenceDataSourceDescription** *(dict) --*

            Provides the Amazon S3 bucket name, the object key name that contains the reference
            data.

            - **BucketARN** *(string) --*

              The Amazon Resource Name (ARN) of the S3 bucket.

            - **FileKey** *(string) --*

              Amazon S3 object key name.

            - **ReferenceRoleARN** *(string) --*

              The ARN of the IAM role that Kinesis Data Analytics can assume to read the Amazon
              S3 object on your behalf to populate the in-application reference table.

              .. note::

                Provided for backward compatibility. Applications that are created with the
                current API version have an application-level service execution role rather
                than a resource-level role.

          - **ReferenceSchema** *(dict) --*

            Describes the format of the data in the streaming source, and how each data element
            maps to corresponding columns created in the in-application stream.

            - **RecordFormat** *(dict) --*

              Specifies the format of the records on the streaming source.

              - **RecordFormatType** *(string) --*

                The type of record format.

              - **MappingParameters** *(dict) --*

                When you configure application input at the time of creating or updating an
                application, provides additional mapping information specific to the record
                format (such as JSON, CSV, or record fields delimited by some delimiter) on the
                streaming source.

                - **JSONMappingParameters** *(dict) --*

                  Provides additional mapping information when JSON is the record format on the
                  streaming source.

                  - **RecordRowPath** *(string) --*

                    The path to the top-level parent that contains the records.

                - **CSVMappingParameters** *(dict) --*

                  Provides additional mapping information when the record format uses
                  delimiters (for example, CSV).

                  - **RecordRowDelimiter** *(string) --*

                    The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
                    delimiter.

                  - **RecordColumnDelimiter** *(string) --*

                    The column delimiter. For example, in a CSV format, a comma (",") is the
                    typical column delimiter.

            - **RecordEncoding** *(string) --*

              Specifies the encoding of the records in the streaming source. For example, UTF-8.

            - **RecordColumns** *(list) --*

              A list of ``RecordColumn`` objects.

              - *(dict) --*

                For an SQL-based Amazon Kinesis Data Analytics application, describes the
                mapping of each data element in the streaming source to the corresponding
                column in the in-application stream.

                Also used to describe the format of the reference data source.

                - **Name** *(string) --*

                  The name of the column that is created in the in-application input stream or
                  reference table.

                - **Mapping** *(string) --*

                  A reference to the data element in the streaming input or the reference data
                  source.

                - **SqlType** *(string) --*

                  The type of column created in the in-application input stream or reference
                  table.

    - **ApplicationCodeConfigurationDescription** *(dict) --*

      The details about the application code for a Java-based Kinesis Data Analytics
      application.

      - **CodeContentType** *(string) --*

        Specifies whether the code content is in text or zip format.

      - **CodeContentDescription** *(dict) --*

        Describes details about the location and format of the application code.

        - **TextContent** *(string) --*

          The text-format code

        - **CodeMD5** *(string) --*

          The checksum that can be used to validate zip-format code.

        - **CodeSize** *(integer) --*

          The size in bytes of the application code. Can be used to validate zip-format code.

        - **S3ApplicationCodeLocationDescription** *(dict) --*

          The S3 bucket Amazon Resource Name (ARN), file key, and object version of the
          application code stored in Amazon S3.

          - **BucketARN** *(string) --*

            The Amazon Resource Name (ARN) for the S3 bucket containing the application code.

          - **FileKey** *(string) --*

            The file key for the object containing the application code.

          - **ObjectVersion** *(string) --*

            The version of the object containing the application code.

    - **RunConfigurationDescription** *(dict) --*

      The details about the starting properties for a Kinesis Data Analytics application.

      - **ApplicationRestoreConfigurationDescription** *(dict) --*

        Describes the restore behavior of a restarting application.

        - **ApplicationRestoreType** *(string) --*

          Specifies how the application should be restored.

        - **SnapshotName** *(string) --*

          The identifier of an existing snapshot of application state to use to restart an
          application. The application uses this value if ``RESTORE_FROM_CUSTOM_SNAPSHOT`` is
          specified for the ``ApplicationRestoreType`` .

    - **FlinkApplicationConfigurationDescription** *(dict) --*

      The details about a Java-based Kinesis Data Analytics application.

      - **CheckpointConfigurationDescription** *(dict) --*

        Describes an application's checkpointing configuration. Checkpointing is the process of
        persisting application state for fault tolerance.

        - **ConfigurationType** *(string) --*

          Describes whether the application uses the default checkpointing behavior in Kinesis
          Data Analytics.

        - **CheckpointingEnabled** *(boolean) --*

          Describes whether checkpointing is enabled for a Java-based Kinesis Data Analytics
          application.

        - **CheckpointInterval** *(integer) --*

          Describes the interval in milliseconds between checkpoint operations.

        - **MinPauseBetweenCheckpoints** *(integer) --*

          Describes the minimum time in milliseconds after a checkpoint operation completes
          that a new checkpoint operation can start.

      - **MonitoringConfigurationDescription** *(dict) --*

        Describes configuration parameters for Amazon CloudWatch logging for an application.

        - **ConfigurationType** *(string) --*

          Describes whether to use the default CloudWatch logging configuration for an
          application.

        - **MetricsLevel** *(string) --*

          Describes the granularity of the CloudWatch Logs for an application.

        - **LogLevel** *(string) --*

          Describes the verbosity of the CloudWatch Logs for an application.

      - **ParallelismConfigurationDescription** *(dict) --*

        Describes parameters for how an application executes multiple tasks simultaneously.

        - **ConfigurationType** *(string) --*

          Describes whether the application uses the default parallelism for the Kinesis Data
          Analytics service.

        - **Parallelism** *(integer) --*

          Describes the initial number of parallel tasks that a Java-based Kinesis Data
          Analytics application can perform.

        - **ParallelismPerKPU** *(integer) --*

          Describes the number of parallel tasks that a Java-based Kinesis Data Analytics
          application can perform per Kinesis Processing Unit (KPU) used by the application.

        - **CurrentParallelism** *(integer) --*

          Describes the current number of parallel tasks that a Java-based Kinesis Data
          Analytics application can perform.

        - **AutoScalingEnabled** *(boolean) --*

          Describes whether the Kinesis Data Analytics service can increase the parallelism of
          the application in response to increased throughput.

      - **JobPlanDescription** *(string) --*

        The job plan for an application. For more information about the job plan, see `Jobs and
        Scheduling
        <https://ci.apache.org/projects/flink/flink-docs-stable/internals/job_scheduling.html>`__
        in the `Apache Flink Documentation
        <https://ci.apache.org/projects/flink/flink-docs-release-1.6/>`__ . To retrieve the job
        plan for the application, use the  DescribeApplicationRequest$IncludeAdditionalDetails
        parameter of the  DescribeApplication operation.

    - **EnvironmentPropertyDescriptions** *(dict) --*

      Describes execution properties for a Java-based Kinesis Data Analytics application.

      - **PropertyGroupDescriptions** *(list) --*

        Describes the execution property groups.

        - *(dict) --*

          Property key-value pairs passed into a Java-based Kinesis Data Analytics application.

          - **PropertyGroupId** *(string) --*

            Describes the key of an application execution property key-value pair.

          - **PropertyMap** *(dict) --*

            Describes the value of an application execution property key-value pair.

            - *(string) --*

              - *(string) --*

    - **ApplicationSnapshotConfigurationDescription** *(dict) --*

      Describes whether snapshots are enabled for a Java-based Kinesis Data Analytics
      application.

      - **SnapshotsEnabled** *(boolean) --*

        Describes whether snapshots are enabled for a Java-based Kinesis Data Analytics
        application.
    """


_ClientCreateApplicationResponseApplicationDetailCloudWatchLoggingOptionDescriptionsTypeDef = TypedDict(
    "_ClientCreateApplicationResponseApplicationDetailCloudWatchLoggingOptionDescriptionsTypeDef",
    {"CloudWatchLoggingOptionId": str, "LogStreamARN": str, "RoleARN": str},
    total=False,
)


class ClientCreateApplicationResponseApplicationDetailCloudWatchLoggingOptionDescriptionsTypeDef(
    _ClientCreateApplicationResponseApplicationDetailCloudWatchLoggingOptionDescriptionsTypeDef
):
    """
    Type definition for `ClientCreateApplicationResponseApplicationDetail` `CloudWatchLoggingOptionDescriptions`

    Describes the Amazon CloudWatch logging option.

    - **CloudWatchLoggingOptionId** *(string) --*

      The ID of the CloudWatch logging option description.

    - **LogStreamARN** *(string) --*

      The Amazon Resource Name (ARN) of the CloudWatch log to receive application messages.

    - **RoleARN** *(string) --*

      The IAM ARN of the role to use to send application messages.

      .. note::

        Provided for backward compatibility. Applications created with the current API
        version have an application-level service execution role rather than a resource-level
        role.
    """


_ClientCreateApplicationResponseApplicationDetailTypeDef = TypedDict(
    "_ClientCreateApplicationResponseApplicationDetailTypeDef",
    {
        "ApplicationARN": str,
        "ApplicationDescription": str,
        "ApplicationName": str,
        "RuntimeEnvironment": str,
        "ServiceExecutionRole": str,
        "ApplicationStatus": str,
        "ApplicationVersionId": int,
        "CreateTimestamp": datetime,
        "LastUpdateTimestamp": datetime,
        "ApplicationConfigurationDescription": ClientCreateApplicationResponseApplicationDetailApplicationConfigurationDescriptionTypeDef,
        "CloudWatchLoggingOptionDescriptions": List[
            ClientCreateApplicationResponseApplicationDetailCloudWatchLoggingOptionDescriptionsTypeDef
        ],
    },
    total=False,
)


class ClientCreateApplicationResponseApplicationDetailTypeDef(
    _ClientCreateApplicationResponseApplicationDetailTypeDef
):
    """
    Type definition for `ClientCreateApplicationResponse` `ApplicationDetail`

    In response to your ``CreateApplication`` request, Kinesis Data Analytics returns a response
    with details of the application it created.

    - **ApplicationARN** *(string) --*

      The ARN of the application.

    - **ApplicationDescription** *(string) --*

      The description of the application.

    - **ApplicationName** *(string) --*

      The name of the application.

    - **RuntimeEnvironment** *(string) --*

      The runtime environment for the application (``SQL-1.0`` or ``FLINK-1_6`` ).

    - **ServiceExecutionRole** *(string) --*

      Specifies the IAM role that the application uses to access external resources.

    - **ApplicationStatus** *(string) --*

      The status of the application.

    - **ApplicationVersionId** *(integer) --*

      Provides the current application version. Kinesis Data Analytics updates the
      ``ApplicationVersionId`` each time you update the application.

    - **CreateTimestamp** *(datetime) --*

      The current timestamp when the application was created.

    - **LastUpdateTimestamp** *(datetime) --*

      The current timestamp when the application was last updated.

    - **ApplicationConfigurationDescription** *(dict) --*

      Provides details about the application's SQL or Java code and starting parameters.

      - **SqlApplicationConfigurationDescription** *(dict) --*

        The details about inputs, outputs, and reference data sources for an SQL-based Kinesis
        Data Analytics application.

        - **InputDescriptions** *(list) --*

          The array of  InputDescription objects describing the input streams used by the
          application.

          - *(dict) --*

            Describes the application input configuration for an SQL-based Amazon Kinesis Data
            Analytics application.

            - **InputId** *(string) --*

              The input ID that is associated with the application input. This is the ID that
              Kinesis Data Analytics assigns to each input configuration that you add to your
              application.

            - **NamePrefix** *(string) --*

              The in-application name prefix.

            - **InAppStreamNames** *(list) --*

              Returns the in-application stream names that are mapped to the stream source.

              - *(string) --*

            - **InputProcessingConfigurationDescription** *(dict) --*

              The description of the preprocessor that executes on records in this input before
              the application's code is run.

              - **InputLambdaProcessorDescription** *(dict) --*

                Provides configuration information about the associated
                InputLambdaProcessorDescription

                - **ResourceARN** *(string) --*

                  The ARN of the AWS Lambda function that is used to preprocess the records in
                  the stream.

                  .. note::

                    To specify an earlier version of the Lambda function than the latest, include
                    the Lambda function version in the Lambda function ARN. For more information
                    about Lambda ARNs, see `Example ARNs\\: AWS Lambda
                    </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__

                - **RoleARN** *(string) --*

                  The ARN of the IAM role that is used to access the AWS Lambda function.

                  .. note::

                    Provided for backward compatibility. Applications that are created with the
                    current API version have an application-level service execution role rather
                    than a resource-level role.

            - **KinesisStreamsInputDescription** *(dict) --*

              If a Kinesis data stream is configured as a streaming source, provides the Kinesis
              data stream's Amazon Resource Name (ARN).

              - **ResourceARN** *(string) --*

                The Amazon Resource Name (ARN) of the Kinesis data stream.

              - **RoleARN** *(string) --*

                The ARN of the IAM role that Kinesis Data Analytics can assume to access the
                stream.

                .. note::

                  Provided for backward compatibility. Applications that are created with the
                  current API version have an application-level service execution role rather
                  than a resource-level role.

            - **KinesisFirehoseInputDescription** *(dict) --*

              If a Kinesis Data Firehose delivery stream is configured as a streaming source,
              provides the delivery stream's ARN.

              - **ResourceARN** *(string) --*

                The Amazon Resource Name (ARN) of the delivery stream.

              - **RoleARN** *(string) --*

                The ARN of the IAM role that Kinesis Data Analytics assumes to access the stream.

                .. note::

                  Provided for backward compatibility. Applications that are created with the
                  current API version have an application-level service execution role rather
                  than a resource-level role.

            - **InputSchema** *(dict) --*

              Describes the format of the data in the streaming source, and how each data element
              maps to corresponding columns in the in-application stream that is being created.

              - **RecordFormat** *(dict) --*

                Specifies the format of the records on the streaming source.

                - **RecordFormatType** *(string) --*

                  The type of record format.

                - **MappingParameters** *(dict) --*

                  When you configure application input at the time of creating or updating an
                  application, provides additional mapping information specific to the record
                  format (such as JSON, CSV, or record fields delimited by some delimiter) on the
                  streaming source.

                  - **JSONMappingParameters** *(dict) --*

                    Provides additional mapping information when JSON is the record format on the
                    streaming source.

                    - **RecordRowPath** *(string) --*

                      The path to the top-level parent that contains the records.

                  - **CSVMappingParameters** *(dict) --*

                    Provides additional mapping information when the record format uses
                    delimiters (for example, CSV).

                    - **RecordRowDelimiter** *(string) --*

                      The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
                      delimiter.

                    - **RecordColumnDelimiter** *(string) --*

                      The column delimiter. For example, in a CSV format, a comma (",") is the
                      typical column delimiter.

              - **RecordEncoding** *(string) --*

                Specifies the encoding of the records in the streaming source. For example, UTF-8.

              - **RecordColumns** *(list) --*

                A list of ``RecordColumn`` objects.

                - *(dict) --*

                  For an SQL-based Amazon Kinesis Data Analytics application, describes the
                  mapping of each data element in the streaming source to the corresponding
                  column in the in-application stream.

                  Also used to describe the format of the reference data source.

                  - **Name** *(string) --*

                    The name of the column that is created in the in-application input stream or
                    reference table.

                  - **Mapping** *(string) --*

                    A reference to the data element in the streaming input or the reference data
                    source.

                  - **SqlType** *(string) --*

                    The type of column created in the in-application input stream or reference
                    table.

            - **InputParallelism** *(dict) --*

              Describes the configured parallelism (number of in-application streams mapped to
              the streaming source).

              - **Count** *(integer) --*

                The number of in-application streams to create.

            - **InputStartingPositionConfiguration** *(dict) --*

              The point at which the application is configured to read from the input stream.

              - **InputStartingPosition** *(string) --*

                The starting position on the stream.

                * ``NOW`` - Start reading just after the most recent record in the stream, and
                start at the request timestamp that the customer issued.

                * ``TRIM_HORIZON`` - Start reading at the last untrimmed record in the stream,
                which is the oldest record available in the stream. This option is not available
                for an Amazon Kinesis Data Firehose delivery stream.

                * ``LAST_STOPPED_POINT`` - Resume reading from where the application last stopped
                reading.

        - **OutputDescriptions** *(list) --*

          The array of  OutputDescription objects describing the destination streams used by the
          application.

          - *(dict) --*

            For an SQL-based Amazon Kinesis Data Analytics application, describes the application
            output configuration, which includes the in-application stream name and the
            destination where the stream data is written. The destination can be a Kinesis data
            stream or a Kinesis Data Firehose delivery stream.

            - **OutputId** *(string) --*

              A unique identifier for the output configuration.

            - **Name** *(string) --*

              The name of the in-application stream that is configured as output.

            - **KinesisStreamsOutputDescription** *(dict) --*

              Describes the Kinesis data stream that is configured as the destination where
              output is written.

              - **ResourceARN** *(string) --*

                The Amazon Resource Name (ARN) of the Kinesis data stream.

              - **RoleARN** *(string) --*

                The ARN of the IAM role that Kinesis Data Analytics can assume to access the
                stream.

                .. note::

                  Provided for backward compatibility. Applications that are created with the
                  current API version have an application-level service execution role rather
                  than a resource-level role.

            - **KinesisFirehoseOutputDescription** *(dict) --*

              Describes the Kinesis Data Firehose delivery stream that is configured as the
              destination where output is written.

              - **ResourceARN** *(string) --*

                The Amazon Resource Name (ARN) of the delivery stream.

              - **RoleARN** *(string) --*

                The ARN of the IAM role that Kinesis Data Analytics can assume to access the
                stream.

                .. note::

                  Provided for backward compatibility. Applications that are created with the
                  current API version have an application-level service execution role rather
                  than a resource-level role.

            - **LambdaOutputDescription** *(dict) --*

              Describes the Lambda function that is configured as the destination where output is
              written.

              - **ResourceARN** *(string) --*

                The Amazon Resource Name (ARN) of the destination Lambda function.

              - **RoleARN** *(string) --*

                The ARN of the IAM role that Kinesis Data Analytics can assume to write to the
                destination function.

                .. note::

                  Provided for backward compatibility. Applications that are created with the
                  current API version have an application-level service execution role rather
                  than a resource-level role.

            - **DestinationSchema** *(dict) --*

              The data format used for writing data to the destination.

              - **RecordFormatType** *(string) --*

                Specifies the format of the records on the output stream.

        - **ReferenceDataSourceDescriptions** *(list) --*

          The array of  ReferenceDataSourceDescription objects describing the reference data
          sources used by the application.

          - *(dict) --*

            For an SQL-based Amazon Kinesis Data Analytics application, describes the reference
            data source configured for an application.

            - **ReferenceId** *(string) --*

              The ID of the reference data source. This is the ID that Kinesis Data Analytics
              assigns when you add the reference data source to your application using the
              CreateApplication or  UpdateApplication operation.

            - **TableName** *(string) --*

              The in-application table name created by the specific reference data source
              configuration.

            - **S3ReferenceDataSourceDescription** *(dict) --*

              Provides the Amazon S3 bucket name, the object key name that contains the reference
              data.

              - **BucketARN** *(string) --*

                The Amazon Resource Name (ARN) of the S3 bucket.

              - **FileKey** *(string) --*

                Amazon S3 object key name.

              - **ReferenceRoleARN** *(string) --*

                The ARN of the IAM role that Kinesis Data Analytics can assume to read the Amazon
                S3 object on your behalf to populate the in-application reference table.

                .. note::

                  Provided for backward compatibility. Applications that are created with the
                  current API version have an application-level service execution role rather
                  than a resource-level role.

            - **ReferenceSchema** *(dict) --*

              Describes the format of the data in the streaming source, and how each data element
              maps to corresponding columns created in the in-application stream.

              - **RecordFormat** *(dict) --*

                Specifies the format of the records on the streaming source.

                - **RecordFormatType** *(string) --*

                  The type of record format.

                - **MappingParameters** *(dict) --*

                  When you configure application input at the time of creating or updating an
                  application, provides additional mapping information specific to the record
                  format (such as JSON, CSV, or record fields delimited by some delimiter) on the
                  streaming source.

                  - **JSONMappingParameters** *(dict) --*

                    Provides additional mapping information when JSON is the record format on the
                    streaming source.

                    - **RecordRowPath** *(string) --*

                      The path to the top-level parent that contains the records.

                  - **CSVMappingParameters** *(dict) --*

                    Provides additional mapping information when the record format uses
                    delimiters (for example, CSV).

                    - **RecordRowDelimiter** *(string) --*

                      The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
                      delimiter.

                    - **RecordColumnDelimiter** *(string) --*

                      The column delimiter. For example, in a CSV format, a comma (",") is the
                      typical column delimiter.

              - **RecordEncoding** *(string) --*

                Specifies the encoding of the records in the streaming source. For example, UTF-8.

              - **RecordColumns** *(list) --*

                A list of ``RecordColumn`` objects.

                - *(dict) --*

                  For an SQL-based Amazon Kinesis Data Analytics application, describes the
                  mapping of each data element in the streaming source to the corresponding
                  column in the in-application stream.

                  Also used to describe the format of the reference data source.

                  - **Name** *(string) --*

                    The name of the column that is created in the in-application input stream or
                    reference table.

                  - **Mapping** *(string) --*

                    A reference to the data element in the streaming input or the reference data
                    source.

                  - **SqlType** *(string) --*

                    The type of column created in the in-application input stream or reference
                    table.

      - **ApplicationCodeConfigurationDescription** *(dict) --*

        The details about the application code for a Java-based Kinesis Data Analytics
        application.

        - **CodeContentType** *(string) --*

          Specifies whether the code content is in text or zip format.

        - **CodeContentDescription** *(dict) --*

          Describes details about the location and format of the application code.

          - **TextContent** *(string) --*

            The text-format code

          - **CodeMD5** *(string) --*

            The checksum that can be used to validate zip-format code.

          - **CodeSize** *(integer) --*

            The size in bytes of the application code. Can be used to validate zip-format code.

          - **S3ApplicationCodeLocationDescription** *(dict) --*

            The S3 bucket Amazon Resource Name (ARN), file key, and object version of the
            application code stored in Amazon S3.

            - **BucketARN** *(string) --*

              The Amazon Resource Name (ARN) for the S3 bucket containing the application code.

            - **FileKey** *(string) --*

              The file key for the object containing the application code.

            - **ObjectVersion** *(string) --*

              The version of the object containing the application code.

      - **RunConfigurationDescription** *(dict) --*

        The details about the starting properties for a Kinesis Data Analytics application.

        - **ApplicationRestoreConfigurationDescription** *(dict) --*

          Describes the restore behavior of a restarting application.

          - **ApplicationRestoreType** *(string) --*

            Specifies how the application should be restored.

          - **SnapshotName** *(string) --*

            The identifier of an existing snapshot of application state to use to restart an
            application. The application uses this value if ``RESTORE_FROM_CUSTOM_SNAPSHOT`` is
            specified for the ``ApplicationRestoreType`` .

      - **FlinkApplicationConfigurationDescription** *(dict) --*

        The details about a Java-based Kinesis Data Analytics application.

        - **CheckpointConfigurationDescription** *(dict) --*

          Describes an application's checkpointing configuration. Checkpointing is the process of
          persisting application state for fault tolerance.

          - **ConfigurationType** *(string) --*

            Describes whether the application uses the default checkpointing behavior in Kinesis
            Data Analytics.

          - **CheckpointingEnabled** *(boolean) --*

            Describes whether checkpointing is enabled for a Java-based Kinesis Data Analytics
            application.

          - **CheckpointInterval** *(integer) --*

            Describes the interval in milliseconds between checkpoint operations.

          - **MinPauseBetweenCheckpoints** *(integer) --*

            Describes the minimum time in milliseconds after a checkpoint operation completes
            that a new checkpoint operation can start.

        - **MonitoringConfigurationDescription** *(dict) --*

          Describes configuration parameters for Amazon CloudWatch logging for an application.

          - **ConfigurationType** *(string) --*

            Describes whether to use the default CloudWatch logging configuration for an
            application.

          - **MetricsLevel** *(string) --*

            Describes the granularity of the CloudWatch Logs for an application.

          - **LogLevel** *(string) --*

            Describes the verbosity of the CloudWatch Logs for an application.

        - **ParallelismConfigurationDescription** *(dict) --*

          Describes parameters for how an application executes multiple tasks simultaneously.

          - **ConfigurationType** *(string) --*

            Describes whether the application uses the default parallelism for the Kinesis Data
            Analytics service.

          - **Parallelism** *(integer) --*

            Describes the initial number of parallel tasks that a Java-based Kinesis Data
            Analytics application can perform.

          - **ParallelismPerKPU** *(integer) --*

            Describes the number of parallel tasks that a Java-based Kinesis Data Analytics
            application can perform per Kinesis Processing Unit (KPU) used by the application.

          - **CurrentParallelism** *(integer) --*

            Describes the current number of parallel tasks that a Java-based Kinesis Data
            Analytics application can perform.

          - **AutoScalingEnabled** *(boolean) --*

            Describes whether the Kinesis Data Analytics service can increase the parallelism of
            the application in response to increased throughput.

        - **JobPlanDescription** *(string) --*

          The job plan for an application. For more information about the job plan, see `Jobs and
          Scheduling
          <https://ci.apache.org/projects/flink/flink-docs-stable/internals/job_scheduling.html>`__
          in the `Apache Flink Documentation
          <https://ci.apache.org/projects/flink/flink-docs-release-1.6/>`__ . To retrieve the job
          plan for the application, use the  DescribeApplicationRequest$IncludeAdditionalDetails
          parameter of the  DescribeApplication operation.

      - **EnvironmentPropertyDescriptions** *(dict) --*

        Describes execution properties for a Java-based Kinesis Data Analytics application.

        - **PropertyGroupDescriptions** *(list) --*

          Describes the execution property groups.

          - *(dict) --*

            Property key-value pairs passed into a Java-based Kinesis Data Analytics application.

            - **PropertyGroupId** *(string) --*

              Describes the key of an application execution property key-value pair.

            - **PropertyMap** *(dict) --*

              Describes the value of an application execution property key-value pair.

              - *(string) --*

                - *(string) --*

      - **ApplicationSnapshotConfigurationDescription** *(dict) --*

        Describes whether snapshots are enabled for a Java-based Kinesis Data Analytics
        application.

        - **SnapshotsEnabled** *(boolean) --*

          Describes whether snapshots are enabled for a Java-based Kinesis Data Analytics
          application.

    - **CloudWatchLoggingOptionDescriptions** *(list) --*

      Describes the application Amazon CloudWatch logging options.

      - *(dict) --*

        Describes the Amazon CloudWatch logging option.

        - **CloudWatchLoggingOptionId** *(string) --*

          The ID of the CloudWatch logging option description.

        - **LogStreamARN** *(string) --*

          The Amazon Resource Name (ARN) of the CloudWatch log to receive application messages.

        - **RoleARN** *(string) --*

          The IAM ARN of the role to use to send application messages.

          .. note::

            Provided for backward compatibility. Applications created with the current API
            version have an application-level service execution role rather than a resource-level
            role.
    """


_ClientCreateApplicationResponseTypeDef = TypedDict(
    "_ClientCreateApplicationResponseTypeDef",
    {"ApplicationDetail": ClientCreateApplicationResponseApplicationDetailTypeDef},
    total=False,
)


class ClientCreateApplicationResponseTypeDef(_ClientCreateApplicationResponseTypeDef):
    """
    Type definition for `ClientCreateApplication` `Response`

    - **ApplicationDetail** *(dict) --*

      In response to your ``CreateApplication`` request, Kinesis Data Analytics returns a response
      with details of the application it created.

      - **ApplicationARN** *(string) --*

        The ARN of the application.

      - **ApplicationDescription** *(string) --*

        The description of the application.

      - **ApplicationName** *(string) --*

        The name of the application.

      - **RuntimeEnvironment** *(string) --*

        The runtime environment for the application (``SQL-1.0`` or ``FLINK-1_6`` ).

      - **ServiceExecutionRole** *(string) --*

        Specifies the IAM role that the application uses to access external resources.

      - **ApplicationStatus** *(string) --*

        The status of the application.

      - **ApplicationVersionId** *(integer) --*

        Provides the current application version. Kinesis Data Analytics updates the
        ``ApplicationVersionId`` each time you update the application.

      - **CreateTimestamp** *(datetime) --*

        The current timestamp when the application was created.

      - **LastUpdateTimestamp** *(datetime) --*

        The current timestamp when the application was last updated.

      - **ApplicationConfigurationDescription** *(dict) --*

        Provides details about the application's SQL or Java code and starting parameters.

        - **SqlApplicationConfigurationDescription** *(dict) --*

          The details about inputs, outputs, and reference data sources for an SQL-based Kinesis
          Data Analytics application.

          - **InputDescriptions** *(list) --*

            The array of  InputDescription objects describing the input streams used by the
            application.

            - *(dict) --*

              Describes the application input configuration for an SQL-based Amazon Kinesis Data
              Analytics application.

              - **InputId** *(string) --*

                The input ID that is associated with the application input. This is the ID that
                Kinesis Data Analytics assigns to each input configuration that you add to your
                application.

              - **NamePrefix** *(string) --*

                The in-application name prefix.

              - **InAppStreamNames** *(list) --*

                Returns the in-application stream names that are mapped to the stream source.

                - *(string) --*

              - **InputProcessingConfigurationDescription** *(dict) --*

                The description of the preprocessor that executes on records in this input before
                the application's code is run.

                - **InputLambdaProcessorDescription** *(dict) --*

                  Provides configuration information about the associated
                  InputLambdaProcessorDescription

                  - **ResourceARN** *(string) --*

                    The ARN of the AWS Lambda function that is used to preprocess the records in
                    the stream.

                    .. note::

                      To specify an earlier version of the Lambda function than the latest, include
                      the Lambda function version in the Lambda function ARN. For more information
                      about Lambda ARNs, see `Example ARNs\\: AWS Lambda
                      </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__

                  - **RoleARN** *(string) --*

                    The ARN of the IAM role that is used to access the AWS Lambda function.

                    .. note::

                      Provided for backward compatibility. Applications that are created with the
                      current API version have an application-level service execution role rather
                      than a resource-level role.

              - **KinesisStreamsInputDescription** *(dict) --*

                If a Kinesis data stream is configured as a streaming source, provides the Kinesis
                data stream's Amazon Resource Name (ARN).

                - **ResourceARN** *(string) --*

                  The Amazon Resource Name (ARN) of the Kinesis data stream.

                - **RoleARN** *(string) --*

                  The ARN of the IAM role that Kinesis Data Analytics can assume to access the
                  stream.

                  .. note::

                    Provided for backward compatibility. Applications that are created with the
                    current API version have an application-level service execution role rather
                    than a resource-level role.

              - **KinesisFirehoseInputDescription** *(dict) --*

                If a Kinesis Data Firehose delivery stream is configured as a streaming source,
                provides the delivery stream's ARN.

                - **ResourceARN** *(string) --*

                  The Amazon Resource Name (ARN) of the delivery stream.

                - **RoleARN** *(string) --*

                  The ARN of the IAM role that Kinesis Data Analytics assumes to access the stream.

                  .. note::

                    Provided for backward compatibility. Applications that are created with the
                    current API version have an application-level service execution role rather
                    than a resource-level role.

              - **InputSchema** *(dict) --*

                Describes the format of the data in the streaming source, and how each data element
                maps to corresponding columns in the in-application stream that is being created.

                - **RecordFormat** *(dict) --*

                  Specifies the format of the records on the streaming source.

                  - **RecordFormatType** *(string) --*

                    The type of record format.

                  - **MappingParameters** *(dict) --*

                    When you configure application input at the time of creating or updating an
                    application, provides additional mapping information specific to the record
                    format (such as JSON, CSV, or record fields delimited by some delimiter) on the
                    streaming source.

                    - **JSONMappingParameters** *(dict) --*

                      Provides additional mapping information when JSON is the record format on the
                      streaming source.

                      - **RecordRowPath** *(string) --*

                        The path to the top-level parent that contains the records.

                    - **CSVMappingParameters** *(dict) --*

                      Provides additional mapping information when the record format uses
                      delimiters (for example, CSV).

                      - **RecordRowDelimiter** *(string) --*

                        The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
                        delimiter.

                      - **RecordColumnDelimiter** *(string) --*

                        The column delimiter. For example, in a CSV format, a comma (",") is the
                        typical column delimiter.

                - **RecordEncoding** *(string) --*

                  Specifies the encoding of the records in the streaming source. For example, UTF-8.

                - **RecordColumns** *(list) --*

                  A list of ``RecordColumn`` objects.

                  - *(dict) --*

                    For an SQL-based Amazon Kinesis Data Analytics application, describes the
                    mapping of each data element in the streaming source to the corresponding
                    column in the in-application stream.

                    Also used to describe the format of the reference data source.

                    - **Name** *(string) --*

                      The name of the column that is created in the in-application input stream or
                      reference table.

                    - **Mapping** *(string) --*

                      A reference to the data element in the streaming input or the reference data
                      source.

                    - **SqlType** *(string) --*

                      The type of column created in the in-application input stream or reference
                      table.

              - **InputParallelism** *(dict) --*

                Describes the configured parallelism (number of in-application streams mapped to
                the streaming source).

                - **Count** *(integer) --*

                  The number of in-application streams to create.

              - **InputStartingPositionConfiguration** *(dict) --*

                The point at which the application is configured to read from the input stream.

                - **InputStartingPosition** *(string) --*

                  The starting position on the stream.

                  * ``NOW`` - Start reading just after the most recent record in the stream, and
                  start at the request timestamp that the customer issued.

                  * ``TRIM_HORIZON`` - Start reading at the last untrimmed record in the stream,
                  which is the oldest record available in the stream. This option is not available
                  for an Amazon Kinesis Data Firehose delivery stream.

                  * ``LAST_STOPPED_POINT`` - Resume reading from where the application last stopped
                  reading.

          - **OutputDescriptions** *(list) --*

            The array of  OutputDescription objects describing the destination streams used by the
            application.

            - *(dict) --*

              For an SQL-based Amazon Kinesis Data Analytics application, describes the application
              output configuration, which includes the in-application stream name and the
              destination where the stream data is written. The destination can be a Kinesis data
              stream or a Kinesis Data Firehose delivery stream.

              - **OutputId** *(string) --*

                A unique identifier for the output configuration.

              - **Name** *(string) --*

                The name of the in-application stream that is configured as output.

              - **KinesisStreamsOutputDescription** *(dict) --*

                Describes the Kinesis data stream that is configured as the destination where
                output is written.

                - **ResourceARN** *(string) --*

                  The Amazon Resource Name (ARN) of the Kinesis data stream.

                - **RoleARN** *(string) --*

                  The ARN of the IAM role that Kinesis Data Analytics can assume to access the
                  stream.

                  .. note::

                    Provided for backward compatibility. Applications that are created with the
                    current API version have an application-level service execution role rather
                    than a resource-level role.

              - **KinesisFirehoseOutputDescription** *(dict) --*

                Describes the Kinesis Data Firehose delivery stream that is configured as the
                destination where output is written.

                - **ResourceARN** *(string) --*

                  The Amazon Resource Name (ARN) of the delivery stream.

                - **RoleARN** *(string) --*

                  The ARN of the IAM role that Kinesis Data Analytics can assume to access the
                  stream.

                  .. note::

                    Provided for backward compatibility. Applications that are created with the
                    current API version have an application-level service execution role rather
                    than a resource-level role.

              - **LambdaOutputDescription** *(dict) --*

                Describes the Lambda function that is configured as the destination where output is
                written.

                - **ResourceARN** *(string) --*

                  The Amazon Resource Name (ARN) of the destination Lambda function.

                - **RoleARN** *(string) --*

                  The ARN of the IAM role that Kinesis Data Analytics can assume to write to the
                  destination function.

                  .. note::

                    Provided for backward compatibility. Applications that are created with the
                    current API version have an application-level service execution role rather
                    than a resource-level role.

              - **DestinationSchema** *(dict) --*

                The data format used for writing data to the destination.

                - **RecordFormatType** *(string) --*

                  Specifies the format of the records on the output stream.

          - **ReferenceDataSourceDescriptions** *(list) --*

            The array of  ReferenceDataSourceDescription objects describing the reference data
            sources used by the application.

            - *(dict) --*

              For an SQL-based Amazon Kinesis Data Analytics application, describes the reference
              data source configured for an application.

              - **ReferenceId** *(string) --*

                The ID of the reference data source. This is the ID that Kinesis Data Analytics
                assigns when you add the reference data source to your application using the
                CreateApplication or  UpdateApplication operation.

              - **TableName** *(string) --*

                The in-application table name created by the specific reference data source
                configuration.

              - **S3ReferenceDataSourceDescription** *(dict) --*

                Provides the Amazon S3 bucket name, the object key name that contains the reference
                data.

                - **BucketARN** *(string) --*

                  The Amazon Resource Name (ARN) of the S3 bucket.

                - **FileKey** *(string) --*

                  Amazon S3 object key name.

                - **ReferenceRoleARN** *(string) --*

                  The ARN of the IAM role that Kinesis Data Analytics can assume to read the Amazon
                  S3 object on your behalf to populate the in-application reference table.

                  .. note::

                    Provided for backward compatibility. Applications that are created with the
                    current API version have an application-level service execution role rather
                    than a resource-level role.

              - **ReferenceSchema** *(dict) --*

                Describes the format of the data in the streaming source, and how each data element
                maps to corresponding columns created in the in-application stream.

                - **RecordFormat** *(dict) --*

                  Specifies the format of the records on the streaming source.

                  - **RecordFormatType** *(string) --*

                    The type of record format.

                  - **MappingParameters** *(dict) --*

                    When you configure application input at the time of creating or updating an
                    application, provides additional mapping information specific to the record
                    format (such as JSON, CSV, or record fields delimited by some delimiter) on the
                    streaming source.

                    - **JSONMappingParameters** *(dict) --*

                      Provides additional mapping information when JSON is the record format on the
                      streaming source.

                      - **RecordRowPath** *(string) --*

                        The path to the top-level parent that contains the records.

                    - **CSVMappingParameters** *(dict) --*

                      Provides additional mapping information when the record format uses
                      delimiters (for example, CSV).

                      - **RecordRowDelimiter** *(string) --*

                        The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
                        delimiter.

                      - **RecordColumnDelimiter** *(string) --*

                        The column delimiter. For example, in a CSV format, a comma (",") is the
                        typical column delimiter.

                - **RecordEncoding** *(string) --*

                  Specifies the encoding of the records in the streaming source. For example, UTF-8.

                - **RecordColumns** *(list) --*

                  A list of ``RecordColumn`` objects.

                  - *(dict) --*

                    For an SQL-based Amazon Kinesis Data Analytics application, describes the
                    mapping of each data element in the streaming source to the corresponding
                    column in the in-application stream.

                    Also used to describe the format of the reference data source.

                    - **Name** *(string) --*

                      The name of the column that is created in the in-application input stream or
                      reference table.

                    - **Mapping** *(string) --*

                      A reference to the data element in the streaming input or the reference data
                      source.

                    - **SqlType** *(string) --*

                      The type of column created in the in-application input stream or reference
                      table.

        - **ApplicationCodeConfigurationDescription** *(dict) --*

          The details about the application code for a Java-based Kinesis Data Analytics
          application.

          - **CodeContentType** *(string) --*

            Specifies whether the code content is in text or zip format.

          - **CodeContentDescription** *(dict) --*

            Describes details about the location and format of the application code.

            - **TextContent** *(string) --*

              The text-format code

            - **CodeMD5** *(string) --*

              The checksum that can be used to validate zip-format code.

            - **CodeSize** *(integer) --*

              The size in bytes of the application code. Can be used to validate zip-format code.

            - **S3ApplicationCodeLocationDescription** *(dict) --*

              The S3 bucket Amazon Resource Name (ARN), file key, and object version of the
              application code stored in Amazon S3.

              - **BucketARN** *(string) --*

                The Amazon Resource Name (ARN) for the S3 bucket containing the application code.

              - **FileKey** *(string) --*

                The file key for the object containing the application code.

              - **ObjectVersion** *(string) --*

                The version of the object containing the application code.

        - **RunConfigurationDescription** *(dict) --*

          The details about the starting properties for a Kinesis Data Analytics application.

          - **ApplicationRestoreConfigurationDescription** *(dict) --*

            Describes the restore behavior of a restarting application.

            - **ApplicationRestoreType** *(string) --*

              Specifies how the application should be restored.

            - **SnapshotName** *(string) --*

              The identifier of an existing snapshot of application state to use to restart an
              application. The application uses this value if ``RESTORE_FROM_CUSTOM_SNAPSHOT`` is
              specified for the ``ApplicationRestoreType`` .

        - **FlinkApplicationConfigurationDescription** *(dict) --*

          The details about a Java-based Kinesis Data Analytics application.

          - **CheckpointConfigurationDescription** *(dict) --*

            Describes an application's checkpointing configuration. Checkpointing is the process of
            persisting application state for fault tolerance.

            - **ConfigurationType** *(string) --*

              Describes whether the application uses the default checkpointing behavior in Kinesis
              Data Analytics.

            - **CheckpointingEnabled** *(boolean) --*

              Describes whether checkpointing is enabled for a Java-based Kinesis Data Analytics
              application.

            - **CheckpointInterval** *(integer) --*

              Describes the interval in milliseconds between checkpoint operations.

            - **MinPauseBetweenCheckpoints** *(integer) --*

              Describes the minimum time in milliseconds after a checkpoint operation completes
              that a new checkpoint operation can start.

          - **MonitoringConfigurationDescription** *(dict) --*

            Describes configuration parameters for Amazon CloudWatch logging for an application.

            - **ConfigurationType** *(string) --*

              Describes whether to use the default CloudWatch logging configuration for an
              application.

            - **MetricsLevel** *(string) --*

              Describes the granularity of the CloudWatch Logs for an application.

            - **LogLevel** *(string) --*

              Describes the verbosity of the CloudWatch Logs for an application.

          - **ParallelismConfigurationDescription** *(dict) --*

            Describes parameters for how an application executes multiple tasks simultaneously.

            - **ConfigurationType** *(string) --*

              Describes whether the application uses the default parallelism for the Kinesis Data
              Analytics service.

            - **Parallelism** *(integer) --*

              Describes the initial number of parallel tasks that a Java-based Kinesis Data
              Analytics application can perform.

            - **ParallelismPerKPU** *(integer) --*

              Describes the number of parallel tasks that a Java-based Kinesis Data Analytics
              application can perform per Kinesis Processing Unit (KPU) used by the application.

            - **CurrentParallelism** *(integer) --*

              Describes the current number of parallel tasks that a Java-based Kinesis Data
              Analytics application can perform.

            - **AutoScalingEnabled** *(boolean) --*

              Describes whether the Kinesis Data Analytics service can increase the parallelism of
              the application in response to increased throughput.

          - **JobPlanDescription** *(string) --*

            The job plan for an application. For more information about the job plan, see `Jobs and
            Scheduling
            <https://ci.apache.org/projects/flink/flink-docs-stable/internals/job_scheduling.html>`__
            in the `Apache Flink Documentation
            <https://ci.apache.org/projects/flink/flink-docs-release-1.6/>`__ . To retrieve the job
            plan for the application, use the  DescribeApplicationRequest$IncludeAdditionalDetails
            parameter of the  DescribeApplication operation.

        - **EnvironmentPropertyDescriptions** *(dict) --*

          Describes execution properties for a Java-based Kinesis Data Analytics application.

          - **PropertyGroupDescriptions** *(list) --*

            Describes the execution property groups.

            - *(dict) --*

              Property key-value pairs passed into a Java-based Kinesis Data Analytics application.

              - **PropertyGroupId** *(string) --*

                Describes the key of an application execution property key-value pair.

              - **PropertyMap** *(dict) --*

                Describes the value of an application execution property key-value pair.

                - *(string) --*

                  - *(string) --*

        - **ApplicationSnapshotConfigurationDescription** *(dict) --*

          Describes whether snapshots are enabled for a Java-based Kinesis Data Analytics
          application.

          - **SnapshotsEnabled** *(boolean) --*

            Describes whether snapshots are enabled for a Java-based Kinesis Data Analytics
            application.

      - **CloudWatchLoggingOptionDescriptions** *(list) --*

        Describes the application Amazon CloudWatch logging options.

        - *(dict) --*

          Describes the Amazon CloudWatch logging option.

          - **CloudWatchLoggingOptionId** *(string) --*

            The ID of the CloudWatch logging option description.

          - **LogStreamARN** *(string) --*

            The Amazon Resource Name (ARN) of the CloudWatch log to receive application messages.

          - **RoleARN** *(string) --*

            The IAM ARN of the role to use to send application messages.

            .. note::

              Provided for backward compatibility. Applications created with the current API
              version have an application-level service execution role rather than a resource-level
              role.
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
    Cost Allocation Tags
    <https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html>`__ in the
    *AWS Billing and Cost Management Guide* .

    - **Key** *(string) --* **[REQUIRED]**

      The key of the key-value tag.

    - **Value** *(string) --*

      The value of the key-value tag. The value is optional.
    """


_ClientDeleteApplicationCloudWatchLoggingOptionResponseCloudWatchLoggingOptionDescriptionsTypeDef = TypedDict(
    "_ClientDeleteApplicationCloudWatchLoggingOptionResponseCloudWatchLoggingOptionDescriptionsTypeDef",
    {"CloudWatchLoggingOptionId": str, "LogStreamARN": str, "RoleARN": str},
    total=False,
)


class ClientDeleteApplicationCloudWatchLoggingOptionResponseCloudWatchLoggingOptionDescriptionsTypeDef(
    _ClientDeleteApplicationCloudWatchLoggingOptionResponseCloudWatchLoggingOptionDescriptionsTypeDef
):
    """
    Type definition for `ClientDeleteApplicationCloudWatchLoggingOptionResponse` `CloudWatchLoggingOptionDescriptions`

    Describes the Amazon CloudWatch logging option.

    - **CloudWatchLoggingOptionId** *(string) --*

      The ID of the CloudWatch logging option description.

    - **LogStreamARN** *(string) --*

      The Amazon Resource Name (ARN) of the CloudWatch log to receive application messages.

    - **RoleARN** *(string) --*

      The IAM ARN of the role to use to send application messages.

      .. note::

        Provided for backward compatibility. Applications created with the current API version
        have an application-level service execution role rather than a resource-level role.
    """


_ClientDeleteApplicationCloudWatchLoggingOptionResponseTypeDef = TypedDict(
    "_ClientDeleteApplicationCloudWatchLoggingOptionResponseTypeDef",
    {
        "ApplicationARN": str,
        "ApplicationVersionId": int,
        "CloudWatchLoggingOptionDescriptions": List[
            ClientDeleteApplicationCloudWatchLoggingOptionResponseCloudWatchLoggingOptionDescriptionsTypeDef
        ],
    },
    total=False,
)


class ClientDeleteApplicationCloudWatchLoggingOptionResponseTypeDef(
    _ClientDeleteApplicationCloudWatchLoggingOptionResponseTypeDef
):
    """
    Type definition for `ClientDeleteApplicationCloudWatchLoggingOption` `Response`

    - **ApplicationARN** *(string) --*

      The application's Amazon Resource Name (ARN).

    - **ApplicationVersionId** *(integer) --*

      The version ID of the application. Kinesis Data Analytics updates the
      ``ApplicationVersionId`` each time you change the CloudWatch logging options.

    - **CloudWatchLoggingOptionDescriptions** *(list) --*

      The descriptions of the remaining CloudWatch logging options for the application.

      - *(dict) --*

        Describes the Amazon CloudWatch logging option.

        - **CloudWatchLoggingOptionId** *(string) --*

          The ID of the CloudWatch logging option description.

        - **LogStreamARN** *(string) --*

          The Amazon Resource Name (ARN) of the CloudWatch log to receive application messages.

        - **RoleARN** *(string) --*

          The IAM ARN of the role to use to send application messages.

          .. note::

            Provided for backward compatibility. Applications created with the current API version
            have an application-level service execution role rather than a resource-level role.
    """


_ClientDeleteApplicationInputProcessingConfigurationResponseTypeDef = TypedDict(
    "_ClientDeleteApplicationInputProcessingConfigurationResponseTypeDef",
    {"ApplicationARN": str, "ApplicationVersionId": int},
    total=False,
)


class ClientDeleteApplicationInputProcessingConfigurationResponseTypeDef(
    _ClientDeleteApplicationInputProcessingConfigurationResponseTypeDef
):
    """
    Type definition for `ClientDeleteApplicationInputProcessingConfiguration` `Response`

    - **ApplicationARN** *(string) --*

      The Amazon Resource Name (ARN) of the application.

    - **ApplicationVersionId** *(integer) --*

      The current application version ID.
    """


_ClientDeleteApplicationOutputResponseTypeDef = TypedDict(
    "_ClientDeleteApplicationOutputResponseTypeDef",
    {"ApplicationARN": str, "ApplicationVersionId": int},
    total=False,
)


class ClientDeleteApplicationOutputResponseTypeDef(
    _ClientDeleteApplicationOutputResponseTypeDef
):
    """
    Type definition for `ClientDeleteApplicationOutput` `Response`

    - **ApplicationARN** *(string) --*

      The application Amazon Resource Name (ARN).

    - **ApplicationVersionId** *(integer) --*

      The current application version ID.
    """


_ClientDeleteApplicationReferenceDataSourceResponseTypeDef = TypedDict(
    "_ClientDeleteApplicationReferenceDataSourceResponseTypeDef",
    {"ApplicationARN": str, "ApplicationVersionId": int},
    total=False,
)


class ClientDeleteApplicationReferenceDataSourceResponseTypeDef(
    _ClientDeleteApplicationReferenceDataSourceResponseTypeDef
):
    """
    Type definition for `ClientDeleteApplicationReferenceDataSource` `Response`

    - **ApplicationARN** *(string) --*

      The application Amazon Resource Name (ARN).

    - **ApplicationVersionId** *(integer) --*

      The updated version ID of the application.
    """


_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionApplicationCodeConfigurationDescriptionCodeContentDescriptionS3ApplicationCodeLocationDescriptionTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionApplicationCodeConfigurationDescriptionCodeContentDescriptionS3ApplicationCodeLocationDescriptionTypeDef",
    {"BucketARN": str, "FileKey": str, "ObjectVersion": str},
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionApplicationCodeConfigurationDescriptionCodeContentDescriptionS3ApplicationCodeLocationDescriptionTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionApplicationCodeConfigurationDescriptionCodeContentDescriptionS3ApplicationCodeLocationDescriptionTypeDef
):
    """
    Type definition for `ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionApplicationCodeConfigurationDescriptionCodeContentDescription` `S3ApplicationCodeLocationDescription`

    The S3 bucket Amazon Resource Name (ARN), file key, and object version of the
    application code stored in Amazon S3.

    - **BucketARN** *(string) --*

      The Amazon Resource Name (ARN) for the S3 bucket containing the application code.

    - **FileKey** *(string) --*

      The file key for the object containing the application code.

    - **ObjectVersion** *(string) --*

      The version of the object containing the application code.
    """


_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionApplicationCodeConfigurationDescriptionCodeContentDescriptionTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionApplicationCodeConfigurationDescriptionCodeContentDescriptionTypeDef",
    {
        "TextContent": str,
        "CodeMD5": str,
        "CodeSize": int,
        "S3ApplicationCodeLocationDescription": ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionApplicationCodeConfigurationDescriptionCodeContentDescriptionS3ApplicationCodeLocationDescriptionTypeDef,
    },
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionApplicationCodeConfigurationDescriptionCodeContentDescriptionTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionApplicationCodeConfigurationDescriptionCodeContentDescriptionTypeDef
):
    """
    Type definition for `ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionApplicationCodeConfigurationDescription` `CodeContentDescription`

    Describes details about the location and format of the application code.

    - **TextContent** *(string) --*

      The text-format code

    - **CodeMD5** *(string) --*

      The checksum that can be used to validate zip-format code.

    - **CodeSize** *(integer) --*

      The size in bytes of the application code. Can be used to validate zip-format code.

    - **S3ApplicationCodeLocationDescription** *(dict) --*

      The S3 bucket Amazon Resource Name (ARN), file key, and object version of the
      application code stored in Amazon S3.

      - **BucketARN** *(string) --*

        The Amazon Resource Name (ARN) for the S3 bucket containing the application code.

      - **FileKey** *(string) --*

        The file key for the object containing the application code.

      - **ObjectVersion** *(string) --*

        The version of the object containing the application code.
    """


_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionApplicationCodeConfigurationDescriptionTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionApplicationCodeConfigurationDescriptionTypeDef",
    {
        "CodeContentType": str,
        "CodeContentDescription": ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionApplicationCodeConfigurationDescriptionCodeContentDescriptionTypeDef,
    },
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionApplicationCodeConfigurationDescriptionTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionApplicationCodeConfigurationDescriptionTypeDef
):
    """
    Type definition for `ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescription` `ApplicationCodeConfigurationDescription`

    The details about the application code for a Java-based Kinesis Data Analytics
    application.

    - **CodeContentType** *(string) --*

      Specifies whether the code content is in text or zip format.

    - **CodeContentDescription** *(dict) --*

      Describes details about the location and format of the application code.

      - **TextContent** *(string) --*

        The text-format code

      - **CodeMD5** *(string) --*

        The checksum that can be used to validate zip-format code.

      - **CodeSize** *(integer) --*

        The size in bytes of the application code. Can be used to validate zip-format code.

      - **S3ApplicationCodeLocationDescription** *(dict) --*

        The S3 bucket Amazon Resource Name (ARN), file key, and object version of the
        application code stored in Amazon S3.

        - **BucketARN** *(string) --*

          The Amazon Resource Name (ARN) for the S3 bucket containing the application code.

        - **FileKey** *(string) --*

          The file key for the object containing the application code.

        - **ObjectVersion** *(string) --*

          The version of the object containing the application code.
    """


_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionApplicationSnapshotConfigurationDescriptionTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionApplicationSnapshotConfigurationDescriptionTypeDef",
    {"SnapshotsEnabled": bool},
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionApplicationSnapshotConfigurationDescriptionTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionApplicationSnapshotConfigurationDescriptionTypeDef
):
    """
    Type definition for `ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescription` `ApplicationSnapshotConfigurationDescription`

    Describes whether snapshots are enabled for a Java-based Kinesis Data Analytics
    application.

    - **SnapshotsEnabled** *(boolean) --*

      Describes whether snapshots are enabled for a Java-based Kinesis Data Analytics
      application.
    """


_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionEnvironmentPropertyDescriptionsPropertyGroupDescriptionsTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionEnvironmentPropertyDescriptionsPropertyGroupDescriptionsTypeDef",
    {"PropertyGroupId": str, "PropertyMap": Dict[str, str]},
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionEnvironmentPropertyDescriptionsPropertyGroupDescriptionsTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionEnvironmentPropertyDescriptionsPropertyGroupDescriptionsTypeDef
):
    """
    Type definition for `ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionEnvironmentPropertyDescriptions` `PropertyGroupDescriptions`

    Property key-value pairs passed into a Java-based Kinesis Data Analytics application.

    - **PropertyGroupId** *(string) --*

      Describes the key of an application execution property key-value pair.

    - **PropertyMap** *(dict) --*

      Describes the value of an application execution property key-value pair.

      - *(string) --*

        - *(string) --*
    """


_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionEnvironmentPropertyDescriptionsTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionEnvironmentPropertyDescriptionsTypeDef",
    {
        "PropertyGroupDescriptions": List[
            ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionEnvironmentPropertyDescriptionsPropertyGroupDescriptionsTypeDef
        ]
    },
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionEnvironmentPropertyDescriptionsTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionEnvironmentPropertyDescriptionsTypeDef
):
    """
    Type definition for `ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescription` `EnvironmentPropertyDescriptions`

    Describes execution properties for a Java-based Kinesis Data Analytics application.

    - **PropertyGroupDescriptions** *(list) --*

      Describes the execution property groups.

      - *(dict) --*

        Property key-value pairs passed into a Java-based Kinesis Data Analytics application.

        - **PropertyGroupId** *(string) --*

          Describes the key of an application execution property key-value pair.

        - **PropertyMap** *(dict) --*

          Describes the value of an application execution property key-value pair.

          - *(string) --*

            - *(string) --*
    """


_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionFlinkApplicationConfigurationDescriptionCheckpointConfigurationDescriptionTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionFlinkApplicationConfigurationDescriptionCheckpointConfigurationDescriptionTypeDef",
    {
        "ConfigurationType": str,
        "CheckpointingEnabled": bool,
        "CheckpointInterval": int,
        "MinPauseBetweenCheckpoints": int,
    },
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionFlinkApplicationConfigurationDescriptionCheckpointConfigurationDescriptionTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionFlinkApplicationConfigurationDescriptionCheckpointConfigurationDescriptionTypeDef
):
    """
    Type definition for `ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionFlinkApplicationConfigurationDescription` `CheckpointConfigurationDescription`

    Describes an application's checkpointing configuration. Checkpointing is the process of
    persisting application state for fault tolerance.

    - **ConfigurationType** *(string) --*

      Describes whether the application uses the default checkpointing behavior in Kinesis
      Data Analytics.

    - **CheckpointingEnabled** *(boolean) --*

      Describes whether checkpointing is enabled for a Java-based Kinesis Data Analytics
      application.

    - **CheckpointInterval** *(integer) --*

      Describes the interval in milliseconds between checkpoint operations.

    - **MinPauseBetweenCheckpoints** *(integer) --*

      Describes the minimum time in milliseconds after a checkpoint operation completes
      that a new checkpoint operation can start.
    """


_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionFlinkApplicationConfigurationDescriptionMonitoringConfigurationDescriptionTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionFlinkApplicationConfigurationDescriptionMonitoringConfigurationDescriptionTypeDef",
    {"ConfigurationType": str, "MetricsLevel": str, "LogLevel": str},
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionFlinkApplicationConfigurationDescriptionMonitoringConfigurationDescriptionTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionFlinkApplicationConfigurationDescriptionMonitoringConfigurationDescriptionTypeDef
):
    """
    Type definition for `ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionFlinkApplicationConfigurationDescription` `MonitoringConfigurationDescription`

    Describes configuration parameters for Amazon CloudWatch logging for an application.

    - **ConfigurationType** *(string) --*

      Describes whether to use the default CloudWatch logging configuration for an
      application.

    - **MetricsLevel** *(string) --*

      Describes the granularity of the CloudWatch Logs for an application.

    - **LogLevel** *(string) --*

      Describes the verbosity of the CloudWatch Logs for an application.
    """


_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionFlinkApplicationConfigurationDescriptionParallelismConfigurationDescriptionTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionFlinkApplicationConfigurationDescriptionParallelismConfigurationDescriptionTypeDef",
    {
        "ConfigurationType": str,
        "Parallelism": int,
        "ParallelismPerKPU": int,
        "CurrentParallelism": int,
        "AutoScalingEnabled": bool,
    },
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionFlinkApplicationConfigurationDescriptionParallelismConfigurationDescriptionTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionFlinkApplicationConfigurationDescriptionParallelismConfigurationDescriptionTypeDef
):
    """
    Type definition for `ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionFlinkApplicationConfigurationDescription` `ParallelismConfigurationDescription`

    Describes parameters for how an application executes multiple tasks simultaneously.

    - **ConfigurationType** *(string) --*

      Describes whether the application uses the default parallelism for the Kinesis Data
      Analytics service.

    - **Parallelism** *(integer) --*

      Describes the initial number of parallel tasks that a Java-based Kinesis Data
      Analytics application can perform.

    - **ParallelismPerKPU** *(integer) --*

      Describes the number of parallel tasks that a Java-based Kinesis Data Analytics
      application can perform per Kinesis Processing Unit (KPU) used by the application.

    - **CurrentParallelism** *(integer) --*

      Describes the current number of parallel tasks that a Java-based Kinesis Data
      Analytics application can perform.

    - **AutoScalingEnabled** *(boolean) --*

      Describes whether the Kinesis Data Analytics service can increase the parallelism of
      the application in response to increased throughput.
    """


_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionFlinkApplicationConfigurationDescriptionTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionFlinkApplicationConfigurationDescriptionTypeDef",
    {
        "CheckpointConfigurationDescription": ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionFlinkApplicationConfigurationDescriptionCheckpointConfigurationDescriptionTypeDef,
        "MonitoringConfigurationDescription": ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionFlinkApplicationConfigurationDescriptionMonitoringConfigurationDescriptionTypeDef,
        "ParallelismConfigurationDescription": ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionFlinkApplicationConfigurationDescriptionParallelismConfigurationDescriptionTypeDef,
        "JobPlanDescription": str,
    },
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionFlinkApplicationConfigurationDescriptionTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionFlinkApplicationConfigurationDescriptionTypeDef
):
    """
    Type definition for `ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescription` `FlinkApplicationConfigurationDescription`

    The details about a Java-based Kinesis Data Analytics application.

    - **CheckpointConfigurationDescription** *(dict) --*

      Describes an application's checkpointing configuration. Checkpointing is the process of
      persisting application state for fault tolerance.

      - **ConfigurationType** *(string) --*

        Describes whether the application uses the default checkpointing behavior in Kinesis
        Data Analytics.

      - **CheckpointingEnabled** *(boolean) --*

        Describes whether checkpointing is enabled for a Java-based Kinesis Data Analytics
        application.

      - **CheckpointInterval** *(integer) --*

        Describes the interval in milliseconds between checkpoint operations.

      - **MinPauseBetweenCheckpoints** *(integer) --*

        Describes the minimum time in milliseconds after a checkpoint operation completes
        that a new checkpoint operation can start.

    - **MonitoringConfigurationDescription** *(dict) --*

      Describes configuration parameters for Amazon CloudWatch logging for an application.

      - **ConfigurationType** *(string) --*

        Describes whether to use the default CloudWatch logging configuration for an
        application.

      - **MetricsLevel** *(string) --*

        Describes the granularity of the CloudWatch Logs for an application.

      - **LogLevel** *(string) --*

        Describes the verbosity of the CloudWatch Logs for an application.

    - **ParallelismConfigurationDescription** *(dict) --*

      Describes parameters for how an application executes multiple tasks simultaneously.

      - **ConfigurationType** *(string) --*

        Describes whether the application uses the default parallelism for the Kinesis Data
        Analytics service.

      - **Parallelism** *(integer) --*

        Describes the initial number of parallel tasks that a Java-based Kinesis Data
        Analytics application can perform.

      - **ParallelismPerKPU** *(integer) --*

        Describes the number of parallel tasks that a Java-based Kinesis Data Analytics
        application can perform per Kinesis Processing Unit (KPU) used by the application.

      - **CurrentParallelism** *(integer) --*

        Describes the current number of parallel tasks that a Java-based Kinesis Data
        Analytics application can perform.

      - **AutoScalingEnabled** *(boolean) --*

        Describes whether the Kinesis Data Analytics service can increase the parallelism of
        the application in response to increased throughput.

    - **JobPlanDescription** *(string) --*

      The job plan for an application. For more information about the job plan, see `Jobs and
      Scheduling
      <https://ci.apache.org/projects/flink/flink-docs-stable/internals/job_scheduling.html>`__
      in the `Apache Flink Documentation
      <https://ci.apache.org/projects/flink/flink-docs-release-1.6/>`__ . To retrieve the job
      plan for the application, use the  DescribeApplicationRequest$IncludeAdditionalDetails
      parameter of the  DescribeApplication operation.
    """


_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionRunConfigurationDescriptionApplicationRestoreConfigurationDescriptionTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionRunConfigurationDescriptionApplicationRestoreConfigurationDescriptionTypeDef",
    {"ApplicationRestoreType": str, "SnapshotName": str},
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionRunConfigurationDescriptionApplicationRestoreConfigurationDescriptionTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionRunConfigurationDescriptionApplicationRestoreConfigurationDescriptionTypeDef
):
    """
    Type definition for `ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionRunConfigurationDescription` `ApplicationRestoreConfigurationDescription`

    Describes the restore behavior of a restarting application.

    - **ApplicationRestoreType** *(string) --*

      Specifies how the application should be restored.

    - **SnapshotName** *(string) --*

      The identifier of an existing snapshot of application state to use to restart an
      application. The application uses this value if ``RESTORE_FROM_CUSTOM_SNAPSHOT`` is
      specified for the ``ApplicationRestoreType`` .
    """


_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionRunConfigurationDescriptionTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionRunConfigurationDescriptionTypeDef",
    {
        "ApplicationRestoreConfigurationDescription": ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionRunConfigurationDescriptionApplicationRestoreConfigurationDescriptionTypeDef
    },
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionRunConfigurationDescriptionTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionRunConfigurationDescriptionTypeDef
):
    """
    Type definition for `ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescription` `RunConfigurationDescription`

    The details about the starting properties for a Kinesis Data Analytics application.

    - **ApplicationRestoreConfigurationDescription** *(dict) --*

      Describes the restore behavior of a restarting application.

      - **ApplicationRestoreType** *(string) --*

        Specifies how the application should be restored.

      - **SnapshotName** *(string) --*

        The identifier of an existing snapshot of application state to use to restart an
        application. The application uses this value if ``RESTORE_FROM_CUSTOM_SNAPSHOT`` is
        specified for the ``ApplicationRestoreType`` .
    """


_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputParallelismTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputParallelismTypeDef",
    {"Count": int},
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputParallelismTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputParallelismTypeDef
):
    """
    Type definition for `ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptions` `InputParallelism`

    Describes the configured parallelism (number of in-application streams mapped to
    the streaming source).

    - **Count** *(integer) --*

      The number of in-application streams to create.
    """


_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputProcessingConfigurationDescriptionInputLambdaProcessorDescriptionTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputProcessingConfigurationDescriptionInputLambdaProcessorDescriptionTypeDef",
    {"ResourceARN": str, "RoleARN": str},
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputProcessingConfigurationDescriptionInputLambdaProcessorDescriptionTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputProcessingConfigurationDescriptionInputLambdaProcessorDescriptionTypeDef
):
    """
    Type definition for `ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputProcessingConfigurationDescription` `InputLambdaProcessorDescription`

    Provides configuration information about the associated
    InputLambdaProcessorDescription

    - **ResourceARN** *(string) --*

      The ARN of the AWS Lambda function that is used to preprocess the records in
      the stream.

      .. note::

        To specify an earlier version of the Lambda function than the latest, include
        the Lambda function version in the Lambda function ARN. For more information
        about Lambda ARNs, see `Example ARNs\\: AWS Lambda
        </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__

    - **RoleARN** *(string) --*

      The ARN of the IAM role that is used to access the AWS Lambda function.

      .. note::

        Provided for backward compatibility. Applications that are created with the
        current API version have an application-level service execution role rather
        than a resource-level role.
    """


_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputProcessingConfigurationDescriptionTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputProcessingConfigurationDescriptionTypeDef",
    {
        "InputLambdaProcessorDescription": ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputProcessingConfigurationDescriptionInputLambdaProcessorDescriptionTypeDef
    },
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputProcessingConfigurationDescriptionTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputProcessingConfigurationDescriptionTypeDef
):
    """
    Type definition for `ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptions` `InputProcessingConfigurationDescription`

    The description of the preprocessor that executes on records in this input before
    the application's code is run.

    - **InputLambdaProcessorDescription** *(dict) --*

      Provides configuration information about the associated
      InputLambdaProcessorDescription

      - **ResourceARN** *(string) --*

        The ARN of the AWS Lambda function that is used to preprocess the records in
        the stream.

        .. note::

          To specify an earlier version of the Lambda function than the latest, include
          the Lambda function version in the Lambda function ARN. For more information
          about Lambda ARNs, see `Example ARNs\\: AWS Lambda
          </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__

      - **RoleARN** *(string) --*

        The ARN of the IAM role that is used to access the AWS Lambda function.

        .. note::

          Provided for backward compatibility. Applications that are created with the
          current API version have an application-level service execution role rather
          than a resource-level role.
    """


_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordColumnsTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordColumnsTypeDef",
    {"Name": str, "Mapping": str, "SqlType": str},
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordColumnsTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordColumnsTypeDef
):
    """
    Type definition for `ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchema` `RecordColumns`

    For an SQL-based Amazon Kinesis Data Analytics application, describes the
    mapping of each data element in the streaming source to the corresponding
    column in the in-application stream.

    Also used to describe the format of the reference data source.

    - **Name** *(string) --*

      The name of the column that is created in the in-application input stream or
      reference table.

    - **Mapping** *(string) --*

      A reference to the data element in the streaming input or the reference data
      source.

    - **SqlType** *(string) --*

      The type of column created in the in-application input stream or reference
      table.
    """


_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef",
    {"RecordRowDelimiter": str, "RecordColumnDelimiter": str},
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef
):
    """
    Type definition for `ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordFormatMappingParameters` `CSVMappingParameters`

    Provides additional mapping information when the record format uses
    delimiters (for example, CSV).

    - **RecordRowDelimiter** *(string) --*

      The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
      delimiter.

    - **RecordColumnDelimiter** *(string) --*

      The column delimiter. For example, in a CSV format, a comma (",") is the
      typical column delimiter.
    """


_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef",
    {"RecordRowPath": str},
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef
):
    """
    Type definition for `ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordFormatMappingParameters` `JSONMappingParameters`

    Provides additional mapping information when JSON is the record format on the
    streaming source.

    - **RecordRowPath** *(string) --*

      The path to the top-level parent that contains the records.
    """


_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordFormatMappingParametersTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordFormatMappingParametersTypeDef",
    {
        "JSONMappingParameters": ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef,
        "CSVMappingParameters": ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef,
    },
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordFormatMappingParametersTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordFormatMappingParametersTypeDef
):
    """
    Type definition for `ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordFormat` `MappingParameters`

    When you configure application input at the time of creating or updating an
    application, provides additional mapping information specific to the record
    format (such as JSON, CSV, or record fields delimited by some delimiter) on the
    streaming source.

    - **JSONMappingParameters** *(dict) --*

      Provides additional mapping information when JSON is the record format on the
      streaming source.

      - **RecordRowPath** *(string) --*

        The path to the top-level parent that contains the records.

    - **CSVMappingParameters** *(dict) --*

      Provides additional mapping information when the record format uses
      delimiters (for example, CSV).

      - **RecordRowDelimiter** *(string) --*

        The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
        delimiter.

      - **RecordColumnDelimiter** *(string) --*

        The column delimiter. For example, in a CSV format, a comma (",") is the
        typical column delimiter.
    """


_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordFormatTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordFormatTypeDef",
    {
        "RecordFormatType": str,
        "MappingParameters": ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordFormatMappingParametersTypeDef,
    },
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordFormatTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordFormatTypeDef
):
    """
    Type definition for `ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchema` `RecordFormat`

    Specifies the format of the records on the streaming source.

    - **RecordFormatType** *(string) --*

      The type of record format.

    - **MappingParameters** *(dict) --*

      When you configure application input at the time of creating or updating an
      application, provides additional mapping information specific to the record
      format (such as JSON, CSV, or record fields delimited by some delimiter) on the
      streaming source.

      - **JSONMappingParameters** *(dict) --*

        Provides additional mapping information when JSON is the record format on the
        streaming source.

        - **RecordRowPath** *(string) --*

          The path to the top-level parent that contains the records.

      - **CSVMappingParameters** *(dict) --*

        Provides additional mapping information when the record format uses
        delimiters (for example, CSV).

        - **RecordRowDelimiter** *(string) --*

          The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
          delimiter.

        - **RecordColumnDelimiter** *(string) --*

          The column delimiter. For example, in a CSV format, a comma (",") is the
          typical column delimiter.
    """


_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaTypeDef",
    {
        "RecordFormat": ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordFormatTypeDef,
        "RecordEncoding": str,
        "RecordColumns": List[
            ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordColumnsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaTypeDef
):
    """
    Type definition for `ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptions` `InputSchema`

    Describes the format of the data in the streaming source, and how each data element
    maps to corresponding columns in the in-application stream that is being created.

    - **RecordFormat** *(dict) --*

      Specifies the format of the records on the streaming source.

      - **RecordFormatType** *(string) --*

        The type of record format.

      - **MappingParameters** *(dict) --*

        When you configure application input at the time of creating or updating an
        application, provides additional mapping information specific to the record
        format (such as JSON, CSV, or record fields delimited by some delimiter) on the
        streaming source.

        - **JSONMappingParameters** *(dict) --*

          Provides additional mapping information when JSON is the record format on the
          streaming source.

          - **RecordRowPath** *(string) --*

            The path to the top-level parent that contains the records.

        - **CSVMappingParameters** *(dict) --*

          Provides additional mapping information when the record format uses
          delimiters (for example, CSV).

          - **RecordRowDelimiter** *(string) --*

            The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
            delimiter.

          - **RecordColumnDelimiter** *(string) --*

            The column delimiter. For example, in a CSV format, a comma (",") is the
            typical column delimiter.

    - **RecordEncoding** *(string) --*

      Specifies the encoding of the records in the streaming source. For example, UTF-8.

    - **RecordColumns** *(list) --*

      A list of ``RecordColumn`` objects.

      - *(dict) --*

        For an SQL-based Amazon Kinesis Data Analytics application, describes the
        mapping of each data element in the streaming source to the corresponding
        column in the in-application stream.

        Also used to describe the format of the reference data source.

        - **Name** *(string) --*

          The name of the column that is created in the in-application input stream or
          reference table.

        - **Mapping** *(string) --*

          A reference to the data element in the streaming input or the reference data
          source.

        - **SqlType** *(string) --*

          The type of column created in the in-application input stream or reference
          table.
    """


_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputStartingPositionConfigurationTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputStartingPositionConfigurationTypeDef",
    {"InputStartingPosition": str},
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputStartingPositionConfigurationTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputStartingPositionConfigurationTypeDef
):
    """
    Type definition for `ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptions` `InputStartingPositionConfiguration`

    The point at which the application is configured to read from the input stream.

    - **InputStartingPosition** *(string) --*

      The starting position on the stream.

      * ``NOW`` - Start reading just after the most recent record in the stream, and
      start at the request timestamp that the customer issued.

      * ``TRIM_HORIZON`` - Start reading at the last untrimmed record in the stream,
      which is the oldest record available in the stream. This option is not available
      for an Amazon Kinesis Data Firehose delivery stream.

      * ``LAST_STOPPED_POINT`` - Resume reading from where the application last stopped
      reading.
    """


_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsKinesisFirehoseInputDescriptionTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsKinesisFirehoseInputDescriptionTypeDef",
    {"ResourceARN": str, "RoleARN": str},
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsKinesisFirehoseInputDescriptionTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsKinesisFirehoseInputDescriptionTypeDef
):
    """
    Type definition for `ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptions` `KinesisFirehoseInputDescription`

    If a Kinesis Data Firehose delivery stream is configured as a streaming source,
    provides the delivery stream's ARN.

    - **ResourceARN** *(string) --*

      The Amazon Resource Name (ARN) of the delivery stream.

    - **RoleARN** *(string) --*

      The ARN of the IAM role that Kinesis Data Analytics assumes to access the stream.

      .. note::

        Provided for backward compatibility. Applications that are created with the
        current API version have an application-level service execution role rather
        than a resource-level role.
    """


_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsKinesisStreamsInputDescriptionTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsKinesisStreamsInputDescriptionTypeDef",
    {"ResourceARN": str, "RoleARN": str},
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsKinesisStreamsInputDescriptionTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsKinesisStreamsInputDescriptionTypeDef
):
    """
    Type definition for `ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptions` `KinesisStreamsInputDescription`

    If a Kinesis data stream is configured as a streaming source, provides the Kinesis
    data stream's Amazon Resource Name (ARN).

    - **ResourceARN** *(string) --*

      The Amazon Resource Name (ARN) of the Kinesis data stream.

    - **RoleARN** *(string) --*

      The ARN of the IAM role that Kinesis Data Analytics can assume to access the
      stream.

      .. note::

        Provided for backward compatibility. Applications that are created with the
        current API version have an application-level service execution role rather
        than a resource-level role.
    """


_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsTypeDef",
    {
        "InputId": str,
        "NamePrefix": str,
        "InAppStreamNames": List[str],
        "InputProcessingConfigurationDescription": ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputProcessingConfigurationDescriptionTypeDef,
        "KinesisStreamsInputDescription": ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsKinesisStreamsInputDescriptionTypeDef,
        "KinesisFirehoseInputDescription": ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsKinesisFirehoseInputDescriptionTypeDef,
        "InputSchema": ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaTypeDef,
        "InputParallelism": ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputParallelismTypeDef,
        "InputStartingPositionConfiguration": ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputStartingPositionConfigurationTypeDef,
    },
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsTypeDef
):
    """
    Type definition for `ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescription` `InputDescriptions`

    Describes the application input configuration for an SQL-based Amazon Kinesis Data
    Analytics application.

    - **InputId** *(string) --*

      The input ID that is associated with the application input. This is the ID that
      Kinesis Data Analytics assigns to each input configuration that you add to your
      application.

    - **NamePrefix** *(string) --*

      The in-application name prefix.

    - **InAppStreamNames** *(list) --*

      Returns the in-application stream names that are mapped to the stream source.

      - *(string) --*

    - **InputProcessingConfigurationDescription** *(dict) --*

      The description of the preprocessor that executes on records in this input before
      the application's code is run.

      - **InputLambdaProcessorDescription** *(dict) --*

        Provides configuration information about the associated
        InputLambdaProcessorDescription

        - **ResourceARN** *(string) --*

          The ARN of the AWS Lambda function that is used to preprocess the records in
          the stream.

          .. note::

            To specify an earlier version of the Lambda function than the latest, include
            the Lambda function version in the Lambda function ARN. For more information
            about Lambda ARNs, see `Example ARNs\\: AWS Lambda
            </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__

        - **RoleARN** *(string) --*

          The ARN of the IAM role that is used to access the AWS Lambda function.

          .. note::

            Provided for backward compatibility. Applications that are created with the
            current API version have an application-level service execution role rather
            than a resource-level role.

    - **KinesisStreamsInputDescription** *(dict) --*

      If a Kinesis data stream is configured as a streaming source, provides the Kinesis
      data stream's Amazon Resource Name (ARN).

      - **ResourceARN** *(string) --*

        The Amazon Resource Name (ARN) of the Kinesis data stream.

      - **RoleARN** *(string) --*

        The ARN of the IAM role that Kinesis Data Analytics can assume to access the
        stream.

        .. note::

          Provided for backward compatibility. Applications that are created with the
          current API version have an application-level service execution role rather
          than a resource-level role.

    - **KinesisFirehoseInputDescription** *(dict) --*

      If a Kinesis Data Firehose delivery stream is configured as a streaming source,
      provides the delivery stream's ARN.

      - **ResourceARN** *(string) --*

        The Amazon Resource Name (ARN) of the delivery stream.

      - **RoleARN** *(string) --*

        The ARN of the IAM role that Kinesis Data Analytics assumes to access the stream.

        .. note::

          Provided for backward compatibility. Applications that are created with the
          current API version have an application-level service execution role rather
          than a resource-level role.

    - **InputSchema** *(dict) --*

      Describes the format of the data in the streaming source, and how each data element
      maps to corresponding columns in the in-application stream that is being created.

      - **RecordFormat** *(dict) --*

        Specifies the format of the records on the streaming source.

        - **RecordFormatType** *(string) --*

          The type of record format.

        - **MappingParameters** *(dict) --*

          When you configure application input at the time of creating or updating an
          application, provides additional mapping information specific to the record
          format (such as JSON, CSV, or record fields delimited by some delimiter) on the
          streaming source.

          - **JSONMappingParameters** *(dict) --*

            Provides additional mapping information when JSON is the record format on the
            streaming source.

            - **RecordRowPath** *(string) --*

              The path to the top-level parent that contains the records.

          - **CSVMappingParameters** *(dict) --*

            Provides additional mapping information when the record format uses
            delimiters (for example, CSV).

            - **RecordRowDelimiter** *(string) --*

              The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
              delimiter.

            - **RecordColumnDelimiter** *(string) --*

              The column delimiter. For example, in a CSV format, a comma (",") is the
              typical column delimiter.

      - **RecordEncoding** *(string) --*

        Specifies the encoding of the records in the streaming source. For example, UTF-8.

      - **RecordColumns** *(list) --*

        A list of ``RecordColumn`` objects.

        - *(dict) --*

          For an SQL-based Amazon Kinesis Data Analytics application, describes the
          mapping of each data element in the streaming source to the corresponding
          column in the in-application stream.

          Also used to describe the format of the reference data source.

          - **Name** *(string) --*

            The name of the column that is created in the in-application input stream or
            reference table.

          - **Mapping** *(string) --*

            A reference to the data element in the streaming input or the reference data
            source.

          - **SqlType** *(string) --*

            The type of column created in the in-application input stream or reference
            table.

    - **InputParallelism** *(dict) --*

      Describes the configured parallelism (number of in-application streams mapped to
      the streaming source).

      - **Count** *(integer) --*

        The number of in-application streams to create.

    - **InputStartingPositionConfiguration** *(dict) --*

      The point at which the application is configured to read from the input stream.

      - **InputStartingPosition** *(string) --*

        The starting position on the stream.

        * ``NOW`` - Start reading just after the most recent record in the stream, and
        start at the request timestamp that the customer issued.

        * ``TRIM_HORIZON`` - Start reading at the last untrimmed record in the stream,
        which is the oldest record available in the stream. This option is not available
        for an Amazon Kinesis Data Firehose delivery stream.

        * ``LAST_STOPPED_POINT`` - Resume reading from where the application last stopped
        reading.
    """


_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptionsDestinationSchemaTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptionsDestinationSchemaTypeDef",
    {"RecordFormatType": str},
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptionsDestinationSchemaTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptionsDestinationSchemaTypeDef
):
    """
    Type definition for `ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptions` `DestinationSchema`

    The data format used for writing data to the destination.

    - **RecordFormatType** *(string) --*

      Specifies the format of the records on the output stream.
    """


_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptionsKinesisFirehoseOutputDescriptionTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptionsKinesisFirehoseOutputDescriptionTypeDef",
    {"ResourceARN": str, "RoleARN": str},
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptionsKinesisFirehoseOutputDescriptionTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptionsKinesisFirehoseOutputDescriptionTypeDef
):
    """
    Type definition for `ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptions` `KinesisFirehoseOutputDescription`

    Describes the Kinesis Data Firehose delivery stream that is configured as the
    destination where output is written.

    - **ResourceARN** *(string) --*

      The Amazon Resource Name (ARN) of the delivery stream.

    - **RoleARN** *(string) --*

      The ARN of the IAM role that Kinesis Data Analytics can assume to access the
      stream.

      .. note::

        Provided for backward compatibility. Applications that are created with the
        current API version have an application-level service execution role rather
        than a resource-level role.
    """


_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptionsKinesisStreamsOutputDescriptionTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptionsKinesisStreamsOutputDescriptionTypeDef",
    {"ResourceARN": str, "RoleARN": str},
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptionsKinesisStreamsOutputDescriptionTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptionsKinesisStreamsOutputDescriptionTypeDef
):
    """
    Type definition for `ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptions` `KinesisStreamsOutputDescription`

    Describes the Kinesis data stream that is configured as the destination where
    output is written.

    - **ResourceARN** *(string) --*

      The Amazon Resource Name (ARN) of the Kinesis data stream.

    - **RoleARN** *(string) --*

      The ARN of the IAM role that Kinesis Data Analytics can assume to access the
      stream.

      .. note::

        Provided for backward compatibility. Applications that are created with the
        current API version have an application-level service execution role rather
        than a resource-level role.
    """


_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptionsLambdaOutputDescriptionTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptionsLambdaOutputDescriptionTypeDef",
    {"ResourceARN": str, "RoleARN": str},
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptionsLambdaOutputDescriptionTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptionsLambdaOutputDescriptionTypeDef
):
    """
    Type definition for `ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptions` `LambdaOutputDescription`

    Describes the Lambda function that is configured as the destination where output is
    written.

    - **ResourceARN** *(string) --*

      The Amazon Resource Name (ARN) of the destination Lambda function.

    - **RoleARN** *(string) --*

      The ARN of the IAM role that Kinesis Data Analytics can assume to write to the
      destination function.

      .. note::

        Provided for backward compatibility. Applications that are created with the
        current API version have an application-level service execution role rather
        than a resource-level role.
    """


_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptionsTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptionsTypeDef",
    {
        "OutputId": str,
        "Name": str,
        "KinesisStreamsOutputDescription": ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptionsKinesisStreamsOutputDescriptionTypeDef,
        "KinesisFirehoseOutputDescription": ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptionsKinesisFirehoseOutputDescriptionTypeDef,
        "LambdaOutputDescription": ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptionsLambdaOutputDescriptionTypeDef,
        "DestinationSchema": ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptionsDestinationSchemaTypeDef,
    },
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptionsTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptionsTypeDef
):
    """
    Type definition for `ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescription` `OutputDescriptions`

    For an SQL-based Amazon Kinesis Data Analytics application, describes the application
    output configuration, which includes the in-application stream name and the
    destination where the stream data is written. The destination can be a Kinesis data
    stream or a Kinesis Data Firehose delivery stream.

    - **OutputId** *(string) --*

      A unique identifier for the output configuration.

    - **Name** *(string) --*

      The name of the in-application stream that is configured as output.

    - **KinesisStreamsOutputDescription** *(dict) --*

      Describes the Kinesis data stream that is configured as the destination where
      output is written.

      - **ResourceARN** *(string) --*

        The Amazon Resource Name (ARN) of the Kinesis data stream.

      - **RoleARN** *(string) --*

        The ARN of the IAM role that Kinesis Data Analytics can assume to access the
        stream.

        .. note::

          Provided for backward compatibility. Applications that are created with the
          current API version have an application-level service execution role rather
          than a resource-level role.

    - **KinesisFirehoseOutputDescription** *(dict) --*

      Describes the Kinesis Data Firehose delivery stream that is configured as the
      destination where output is written.

      - **ResourceARN** *(string) --*

        The Amazon Resource Name (ARN) of the delivery stream.

      - **RoleARN** *(string) --*

        The ARN of the IAM role that Kinesis Data Analytics can assume to access the
        stream.

        .. note::

          Provided for backward compatibility. Applications that are created with the
          current API version have an application-level service execution role rather
          than a resource-level role.

    - **LambdaOutputDescription** *(dict) --*

      Describes the Lambda function that is configured as the destination where output is
      written.

      - **ResourceARN** *(string) --*

        The Amazon Resource Name (ARN) of the destination Lambda function.

      - **RoleARN** *(string) --*

        The ARN of the IAM role that Kinesis Data Analytics can assume to write to the
        destination function.

        .. note::

          Provided for backward compatibility. Applications that are created with the
          current API version have an application-level service execution role rather
          than a resource-level role.

    - **DestinationSchema** *(dict) --*

      The data format used for writing data to the destination.

      - **RecordFormatType** *(string) --*

        Specifies the format of the records on the output stream.
    """


_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordColumnsTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordColumnsTypeDef",
    {"Name": str, "Mapping": str, "SqlType": str},
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordColumnsTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordColumnsTypeDef
):
    """
    Type definition for `ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchema` `RecordColumns`

    For an SQL-based Amazon Kinesis Data Analytics application, describes the
    mapping of each data element in the streaming source to the corresponding
    column in the in-application stream.

    Also used to describe the format of the reference data source.

    - **Name** *(string) --*

      The name of the column that is created in the in-application input stream or
      reference table.

    - **Mapping** *(string) --*

      A reference to the data element in the streaming input or the reference data
      source.

    - **SqlType** *(string) --*

      The type of column created in the in-application input stream or reference
      table.
    """


_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef",
    {"RecordRowDelimiter": str, "RecordColumnDelimiter": str},
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef
):
    """
    Type definition for `ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParameters` `CSVMappingParameters`

    Provides additional mapping information when the record format uses
    delimiters (for example, CSV).

    - **RecordRowDelimiter** *(string) --*

      The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
      delimiter.

    - **RecordColumnDelimiter** *(string) --*

      The column delimiter. For example, in a CSV format, a comma (",") is the
      typical column delimiter.
    """


_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef",
    {"RecordRowPath": str},
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef
):
    """
    Type definition for `ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParameters` `JSONMappingParameters`

    Provides additional mapping information when JSON is the record format on the
    streaming source.

    - **RecordRowPath** *(string) --*

      The path to the top-level parent that contains the records.
    """


_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersTypeDef",
    {
        "JSONMappingParameters": ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef,
        "CSVMappingParameters": ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef,
    },
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersTypeDef
):
    """
    Type definition for `ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordFormat` `MappingParameters`

    When you configure application input at the time of creating or updating an
    application, provides additional mapping information specific to the record
    format (such as JSON, CSV, or record fields delimited by some delimiter) on the
    streaming source.

    - **JSONMappingParameters** *(dict) --*

      Provides additional mapping information when JSON is the record format on the
      streaming source.

      - **RecordRowPath** *(string) --*

        The path to the top-level parent that contains the records.

    - **CSVMappingParameters** *(dict) --*

      Provides additional mapping information when the record format uses
      delimiters (for example, CSV).

      - **RecordRowDelimiter** *(string) --*

        The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
        delimiter.

      - **RecordColumnDelimiter** *(string) --*

        The column delimiter. For example, in a CSV format, a comma (",") is the
        typical column delimiter.
    """


_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordFormatTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordFormatTypeDef",
    {
        "RecordFormatType": str,
        "MappingParameters": ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersTypeDef,
    },
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordFormatTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordFormatTypeDef
):
    """
    Type definition for `ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchema` `RecordFormat`

    Specifies the format of the records on the streaming source.

    - **RecordFormatType** *(string) --*

      The type of record format.

    - **MappingParameters** *(dict) --*

      When you configure application input at the time of creating or updating an
      application, provides additional mapping information specific to the record
      format (such as JSON, CSV, or record fields delimited by some delimiter) on the
      streaming source.

      - **JSONMappingParameters** *(dict) --*

        Provides additional mapping information when JSON is the record format on the
        streaming source.

        - **RecordRowPath** *(string) --*

          The path to the top-level parent that contains the records.

      - **CSVMappingParameters** *(dict) --*

        Provides additional mapping information when the record format uses
        delimiters (for example, CSV).

        - **RecordRowDelimiter** *(string) --*

          The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
          delimiter.

        - **RecordColumnDelimiter** *(string) --*

          The column delimiter. For example, in a CSV format, a comma (",") is the
          typical column delimiter.
    """


_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaTypeDef",
    {
        "RecordFormat": ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordFormatTypeDef,
        "RecordEncoding": str,
        "RecordColumns": List[
            ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordColumnsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaTypeDef
):
    """
    Type definition for `ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptions` `ReferenceSchema`

    Describes the format of the data in the streaming source, and how each data element
    maps to corresponding columns created in the in-application stream.

    - **RecordFormat** *(dict) --*

      Specifies the format of the records on the streaming source.

      - **RecordFormatType** *(string) --*

        The type of record format.

      - **MappingParameters** *(dict) --*

        When you configure application input at the time of creating or updating an
        application, provides additional mapping information specific to the record
        format (such as JSON, CSV, or record fields delimited by some delimiter) on the
        streaming source.

        - **JSONMappingParameters** *(dict) --*

          Provides additional mapping information when JSON is the record format on the
          streaming source.

          - **RecordRowPath** *(string) --*

            The path to the top-level parent that contains the records.

        - **CSVMappingParameters** *(dict) --*

          Provides additional mapping information when the record format uses
          delimiters (for example, CSV).

          - **RecordRowDelimiter** *(string) --*

            The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
            delimiter.

          - **RecordColumnDelimiter** *(string) --*

            The column delimiter. For example, in a CSV format, a comma (",") is the
            typical column delimiter.

    - **RecordEncoding** *(string) --*

      Specifies the encoding of the records in the streaming source. For example, UTF-8.

    - **RecordColumns** *(list) --*

      A list of ``RecordColumn`` objects.

      - *(dict) --*

        For an SQL-based Amazon Kinesis Data Analytics application, describes the
        mapping of each data element in the streaming source to the corresponding
        column in the in-application stream.

        Also used to describe the format of the reference data source.

        - **Name** *(string) --*

          The name of the column that is created in the in-application input stream or
          reference table.

        - **Mapping** *(string) --*

          A reference to the data element in the streaming input or the reference data
          source.

        - **SqlType** *(string) --*

          The type of column created in the in-application input stream or reference
          table.
    """


_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsS3ReferenceDataSourceDescriptionTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsS3ReferenceDataSourceDescriptionTypeDef",
    {"BucketARN": str, "FileKey": str, "ReferenceRoleARN": str},
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsS3ReferenceDataSourceDescriptionTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsS3ReferenceDataSourceDescriptionTypeDef
):
    """
    Type definition for `ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptions` `S3ReferenceDataSourceDescription`

    Provides the Amazon S3 bucket name, the object key name that contains the reference
    data.

    - **BucketARN** *(string) --*

      The Amazon Resource Name (ARN) of the S3 bucket.

    - **FileKey** *(string) --*

      Amazon S3 object key name.

    - **ReferenceRoleARN** *(string) --*

      The ARN of the IAM role that Kinesis Data Analytics can assume to read the Amazon
      S3 object on your behalf to populate the in-application reference table.

      .. note::

        Provided for backward compatibility. Applications that are created with the
        current API version have an application-level service execution role rather
        than a resource-level role.
    """


_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsTypeDef",
    {
        "ReferenceId": str,
        "TableName": str,
        "S3ReferenceDataSourceDescription": ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsS3ReferenceDataSourceDescriptionTypeDef,
        "ReferenceSchema": ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaTypeDef,
    },
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsTypeDef
):
    """
    Type definition for `ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescription` `ReferenceDataSourceDescriptions`

    For an SQL-based Amazon Kinesis Data Analytics application, describes the reference
    data source configured for an application.

    - **ReferenceId** *(string) --*

      The ID of the reference data source. This is the ID that Kinesis Data Analytics
      assigns when you add the reference data source to your application using the
      CreateApplication or  UpdateApplication operation.

    - **TableName** *(string) --*

      The in-application table name created by the specific reference data source
      configuration.

    - **S3ReferenceDataSourceDescription** *(dict) --*

      Provides the Amazon S3 bucket name, the object key name that contains the reference
      data.

      - **BucketARN** *(string) --*

        The Amazon Resource Name (ARN) of the S3 bucket.

      - **FileKey** *(string) --*

        Amazon S3 object key name.

      - **ReferenceRoleARN** *(string) --*

        The ARN of the IAM role that Kinesis Data Analytics can assume to read the Amazon
        S3 object on your behalf to populate the in-application reference table.

        .. note::

          Provided for backward compatibility. Applications that are created with the
          current API version have an application-level service execution role rather
          than a resource-level role.

    - **ReferenceSchema** *(dict) --*

      Describes the format of the data in the streaming source, and how each data element
      maps to corresponding columns created in the in-application stream.

      - **RecordFormat** *(dict) --*

        Specifies the format of the records on the streaming source.

        - **RecordFormatType** *(string) --*

          The type of record format.

        - **MappingParameters** *(dict) --*

          When you configure application input at the time of creating or updating an
          application, provides additional mapping information specific to the record
          format (such as JSON, CSV, or record fields delimited by some delimiter) on the
          streaming source.

          - **JSONMappingParameters** *(dict) --*

            Provides additional mapping information when JSON is the record format on the
            streaming source.

            - **RecordRowPath** *(string) --*

              The path to the top-level parent that contains the records.

          - **CSVMappingParameters** *(dict) --*

            Provides additional mapping information when the record format uses
            delimiters (for example, CSV).

            - **RecordRowDelimiter** *(string) --*

              The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
              delimiter.

            - **RecordColumnDelimiter** *(string) --*

              The column delimiter. For example, in a CSV format, a comma (",") is the
              typical column delimiter.

      - **RecordEncoding** *(string) --*

        Specifies the encoding of the records in the streaming source. For example, UTF-8.

      - **RecordColumns** *(list) --*

        A list of ``RecordColumn`` objects.

        - *(dict) --*

          For an SQL-based Amazon Kinesis Data Analytics application, describes the
          mapping of each data element in the streaming source to the corresponding
          column in the in-application stream.

          Also used to describe the format of the reference data source.

          - **Name** *(string) --*

            The name of the column that is created in the in-application input stream or
            reference table.

          - **Mapping** *(string) --*

            A reference to the data element in the streaming input or the reference data
            source.

          - **SqlType** *(string) --*

            The type of column created in the in-application input stream or reference
            table.
    """


_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionTypeDef",
    {
        "InputDescriptions": List[
            ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsTypeDef
        ],
        "OutputDescriptions": List[
            ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptionsTypeDef
        ],
        "ReferenceDataSourceDescriptions": List[
            ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionTypeDef
):
    """
    Type definition for `ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescription` `SqlApplicationConfigurationDescription`

    The details about inputs, outputs, and reference data sources for an SQL-based Kinesis
    Data Analytics application.

    - **InputDescriptions** *(list) --*

      The array of  InputDescription objects describing the input streams used by the
      application.

      - *(dict) --*

        Describes the application input configuration for an SQL-based Amazon Kinesis Data
        Analytics application.

        - **InputId** *(string) --*

          The input ID that is associated with the application input. This is the ID that
          Kinesis Data Analytics assigns to each input configuration that you add to your
          application.

        - **NamePrefix** *(string) --*

          The in-application name prefix.

        - **InAppStreamNames** *(list) --*

          Returns the in-application stream names that are mapped to the stream source.

          - *(string) --*

        - **InputProcessingConfigurationDescription** *(dict) --*

          The description of the preprocessor that executes on records in this input before
          the application's code is run.

          - **InputLambdaProcessorDescription** *(dict) --*

            Provides configuration information about the associated
            InputLambdaProcessorDescription

            - **ResourceARN** *(string) --*

              The ARN of the AWS Lambda function that is used to preprocess the records in
              the stream.

              .. note::

                To specify an earlier version of the Lambda function than the latest, include
                the Lambda function version in the Lambda function ARN. For more information
                about Lambda ARNs, see `Example ARNs\\: AWS Lambda
                </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__

            - **RoleARN** *(string) --*

              The ARN of the IAM role that is used to access the AWS Lambda function.

              .. note::

                Provided for backward compatibility. Applications that are created with the
                current API version have an application-level service execution role rather
                than a resource-level role.

        - **KinesisStreamsInputDescription** *(dict) --*

          If a Kinesis data stream is configured as a streaming source, provides the Kinesis
          data stream's Amazon Resource Name (ARN).

          - **ResourceARN** *(string) --*

            The Amazon Resource Name (ARN) of the Kinesis data stream.

          - **RoleARN** *(string) --*

            The ARN of the IAM role that Kinesis Data Analytics can assume to access the
            stream.

            .. note::

              Provided for backward compatibility. Applications that are created with the
              current API version have an application-level service execution role rather
              than a resource-level role.

        - **KinesisFirehoseInputDescription** *(dict) --*

          If a Kinesis Data Firehose delivery stream is configured as a streaming source,
          provides the delivery stream's ARN.

          - **ResourceARN** *(string) --*

            The Amazon Resource Name (ARN) of the delivery stream.

          - **RoleARN** *(string) --*

            The ARN of the IAM role that Kinesis Data Analytics assumes to access the stream.

            .. note::

              Provided for backward compatibility. Applications that are created with the
              current API version have an application-level service execution role rather
              than a resource-level role.

        - **InputSchema** *(dict) --*

          Describes the format of the data in the streaming source, and how each data element
          maps to corresponding columns in the in-application stream that is being created.

          - **RecordFormat** *(dict) --*

            Specifies the format of the records on the streaming source.

            - **RecordFormatType** *(string) --*

              The type of record format.

            - **MappingParameters** *(dict) --*

              When you configure application input at the time of creating or updating an
              application, provides additional mapping information specific to the record
              format (such as JSON, CSV, or record fields delimited by some delimiter) on the
              streaming source.

              - **JSONMappingParameters** *(dict) --*

                Provides additional mapping information when JSON is the record format on the
                streaming source.

                - **RecordRowPath** *(string) --*

                  The path to the top-level parent that contains the records.

              - **CSVMappingParameters** *(dict) --*

                Provides additional mapping information when the record format uses
                delimiters (for example, CSV).

                - **RecordRowDelimiter** *(string) --*

                  The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
                  delimiter.

                - **RecordColumnDelimiter** *(string) --*

                  The column delimiter. For example, in a CSV format, a comma (",") is the
                  typical column delimiter.

          - **RecordEncoding** *(string) --*

            Specifies the encoding of the records in the streaming source. For example, UTF-8.

          - **RecordColumns** *(list) --*

            A list of ``RecordColumn`` objects.

            - *(dict) --*

              For an SQL-based Amazon Kinesis Data Analytics application, describes the
              mapping of each data element in the streaming source to the corresponding
              column in the in-application stream.

              Also used to describe the format of the reference data source.

              - **Name** *(string) --*

                The name of the column that is created in the in-application input stream or
                reference table.

              - **Mapping** *(string) --*

                A reference to the data element in the streaming input or the reference data
                source.

              - **SqlType** *(string) --*

                The type of column created in the in-application input stream or reference
                table.

        - **InputParallelism** *(dict) --*

          Describes the configured parallelism (number of in-application streams mapped to
          the streaming source).

          - **Count** *(integer) --*

            The number of in-application streams to create.

        - **InputStartingPositionConfiguration** *(dict) --*

          The point at which the application is configured to read from the input stream.

          - **InputStartingPosition** *(string) --*

            The starting position on the stream.

            * ``NOW`` - Start reading just after the most recent record in the stream, and
            start at the request timestamp that the customer issued.

            * ``TRIM_HORIZON`` - Start reading at the last untrimmed record in the stream,
            which is the oldest record available in the stream. This option is not available
            for an Amazon Kinesis Data Firehose delivery stream.

            * ``LAST_STOPPED_POINT`` - Resume reading from where the application last stopped
            reading.

    - **OutputDescriptions** *(list) --*

      The array of  OutputDescription objects describing the destination streams used by the
      application.

      - *(dict) --*

        For an SQL-based Amazon Kinesis Data Analytics application, describes the application
        output configuration, which includes the in-application stream name and the
        destination where the stream data is written. The destination can be a Kinesis data
        stream or a Kinesis Data Firehose delivery stream.

        - **OutputId** *(string) --*

          A unique identifier for the output configuration.

        - **Name** *(string) --*

          The name of the in-application stream that is configured as output.

        - **KinesisStreamsOutputDescription** *(dict) --*

          Describes the Kinesis data stream that is configured as the destination where
          output is written.

          - **ResourceARN** *(string) --*

            The Amazon Resource Name (ARN) of the Kinesis data stream.

          - **RoleARN** *(string) --*

            The ARN of the IAM role that Kinesis Data Analytics can assume to access the
            stream.

            .. note::

              Provided for backward compatibility. Applications that are created with the
              current API version have an application-level service execution role rather
              than a resource-level role.

        - **KinesisFirehoseOutputDescription** *(dict) --*

          Describes the Kinesis Data Firehose delivery stream that is configured as the
          destination where output is written.

          - **ResourceARN** *(string) --*

            The Amazon Resource Name (ARN) of the delivery stream.

          - **RoleARN** *(string) --*

            The ARN of the IAM role that Kinesis Data Analytics can assume to access the
            stream.

            .. note::

              Provided for backward compatibility. Applications that are created with the
              current API version have an application-level service execution role rather
              than a resource-level role.

        - **LambdaOutputDescription** *(dict) --*

          Describes the Lambda function that is configured as the destination where output is
          written.

          - **ResourceARN** *(string) --*

            The Amazon Resource Name (ARN) of the destination Lambda function.

          - **RoleARN** *(string) --*

            The ARN of the IAM role that Kinesis Data Analytics can assume to write to the
            destination function.

            .. note::

              Provided for backward compatibility. Applications that are created with the
              current API version have an application-level service execution role rather
              than a resource-level role.

        - **DestinationSchema** *(dict) --*

          The data format used for writing data to the destination.

          - **RecordFormatType** *(string) --*

            Specifies the format of the records on the output stream.

    - **ReferenceDataSourceDescriptions** *(list) --*

      The array of  ReferenceDataSourceDescription objects describing the reference data
      sources used by the application.

      - *(dict) --*

        For an SQL-based Amazon Kinesis Data Analytics application, describes the reference
        data source configured for an application.

        - **ReferenceId** *(string) --*

          The ID of the reference data source. This is the ID that Kinesis Data Analytics
          assigns when you add the reference data source to your application using the
          CreateApplication or  UpdateApplication operation.

        - **TableName** *(string) --*

          The in-application table name created by the specific reference data source
          configuration.

        - **S3ReferenceDataSourceDescription** *(dict) --*

          Provides the Amazon S3 bucket name, the object key name that contains the reference
          data.

          - **BucketARN** *(string) --*

            The Amazon Resource Name (ARN) of the S3 bucket.

          - **FileKey** *(string) --*

            Amazon S3 object key name.

          - **ReferenceRoleARN** *(string) --*

            The ARN of the IAM role that Kinesis Data Analytics can assume to read the Amazon
            S3 object on your behalf to populate the in-application reference table.

            .. note::

              Provided for backward compatibility. Applications that are created with the
              current API version have an application-level service execution role rather
              than a resource-level role.

        - **ReferenceSchema** *(dict) --*

          Describes the format of the data in the streaming source, and how each data element
          maps to corresponding columns created in the in-application stream.

          - **RecordFormat** *(dict) --*

            Specifies the format of the records on the streaming source.

            - **RecordFormatType** *(string) --*

              The type of record format.

            - **MappingParameters** *(dict) --*

              When you configure application input at the time of creating or updating an
              application, provides additional mapping information specific to the record
              format (such as JSON, CSV, or record fields delimited by some delimiter) on the
              streaming source.

              - **JSONMappingParameters** *(dict) --*

                Provides additional mapping information when JSON is the record format on the
                streaming source.

                - **RecordRowPath** *(string) --*

                  The path to the top-level parent that contains the records.

              - **CSVMappingParameters** *(dict) --*

                Provides additional mapping information when the record format uses
                delimiters (for example, CSV).

                - **RecordRowDelimiter** *(string) --*

                  The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
                  delimiter.

                - **RecordColumnDelimiter** *(string) --*

                  The column delimiter. For example, in a CSV format, a comma (",") is the
                  typical column delimiter.

          - **RecordEncoding** *(string) --*

            Specifies the encoding of the records in the streaming source. For example, UTF-8.

          - **RecordColumns** *(list) --*

            A list of ``RecordColumn`` objects.

            - *(dict) --*

              For an SQL-based Amazon Kinesis Data Analytics application, describes the
              mapping of each data element in the streaming source to the corresponding
              column in the in-application stream.

              Also used to describe the format of the reference data source.

              - **Name** *(string) --*

                The name of the column that is created in the in-application input stream or
                reference table.

              - **Mapping** *(string) --*

                A reference to the data element in the streaming input or the reference data
                source.

              - **SqlType** *(string) --*

                The type of column created in the in-application input stream or reference
                table.
    """


_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionTypeDef",
    {
        "SqlApplicationConfigurationDescription": ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionTypeDef,
        "ApplicationCodeConfigurationDescription": ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionApplicationCodeConfigurationDescriptionTypeDef,
        "RunConfigurationDescription": ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionRunConfigurationDescriptionTypeDef,
        "FlinkApplicationConfigurationDescription": ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionFlinkApplicationConfigurationDescriptionTypeDef,
        "EnvironmentPropertyDescriptions": ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionEnvironmentPropertyDescriptionsTypeDef,
        "ApplicationSnapshotConfigurationDescription": ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionApplicationSnapshotConfigurationDescriptionTypeDef,
    },
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionTypeDef
):
    """
    Type definition for `ClientDescribeApplicationResponseApplicationDetail` `ApplicationConfigurationDescription`

    Provides details about the application's SQL or Java code and starting parameters.

    - **SqlApplicationConfigurationDescription** *(dict) --*

      The details about inputs, outputs, and reference data sources for an SQL-based Kinesis
      Data Analytics application.

      - **InputDescriptions** *(list) --*

        The array of  InputDescription objects describing the input streams used by the
        application.

        - *(dict) --*

          Describes the application input configuration for an SQL-based Amazon Kinesis Data
          Analytics application.

          - **InputId** *(string) --*

            The input ID that is associated with the application input. This is the ID that
            Kinesis Data Analytics assigns to each input configuration that you add to your
            application.

          - **NamePrefix** *(string) --*

            The in-application name prefix.

          - **InAppStreamNames** *(list) --*

            Returns the in-application stream names that are mapped to the stream source.

            - *(string) --*

          - **InputProcessingConfigurationDescription** *(dict) --*

            The description of the preprocessor that executes on records in this input before
            the application's code is run.

            - **InputLambdaProcessorDescription** *(dict) --*

              Provides configuration information about the associated
              InputLambdaProcessorDescription

              - **ResourceARN** *(string) --*

                The ARN of the AWS Lambda function that is used to preprocess the records in
                the stream.

                .. note::

                  To specify an earlier version of the Lambda function than the latest, include
                  the Lambda function version in the Lambda function ARN. For more information
                  about Lambda ARNs, see `Example ARNs\\: AWS Lambda
                  </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__

              - **RoleARN** *(string) --*

                The ARN of the IAM role that is used to access the AWS Lambda function.

                .. note::

                  Provided for backward compatibility. Applications that are created with the
                  current API version have an application-level service execution role rather
                  than a resource-level role.

          - **KinesisStreamsInputDescription** *(dict) --*

            If a Kinesis data stream is configured as a streaming source, provides the Kinesis
            data stream's Amazon Resource Name (ARN).

            - **ResourceARN** *(string) --*

              The Amazon Resource Name (ARN) of the Kinesis data stream.

            - **RoleARN** *(string) --*

              The ARN of the IAM role that Kinesis Data Analytics can assume to access the
              stream.

              .. note::

                Provided for backward compatibility. Applications that are created with the
                current API version have an application-level service execution role rather
                than a resource-level role.

          - **KinesisFirehoseInputDescription** *(dict) --*

            If a Kinesis Data Firehose delivery stream is configured as a streaming source,
            provides the delivery stream's ARN.

            - **ResourceARN** *(string) --*

              The Amazon Resource Name (ARN) of the delivery stream.

            - **RoleARN** *(string) --*

              The ARN of the IAM role that Kinesis Data Analytics assumes to access the stream.

              .. note::

                Provided for backward compatibility. Applications that are created with the
                current API version have an application-level service execution role rather
                than a resource-level role.

          - **InputSchema** *(dict) --*

            Describes the format of the data in the streaming source, and how each data element
            maps to corresponding columns in the in-application stream that is being created.

            - **RecordFormat** *(dict) --*

              Specifies the format of the records on the streaming source.

              - **RecordFormatType** *(string) --*

                The type of record format.

              - **MappingParameters** *(dict) --*

                When you configure application input at the time of creating or updating an
                application, provides additional mapping information specific to the record
                format (such as JSON, CSV, or record fields delimited by some delimiter) on the
                streaming source.

                - **JSONMappingParameters** *(dict) --*

                  Provides additional mapping information when JSON is the record format on the
                  streaming source.

                  - **RecordRowPath** *(string) --*

                    The path to the top-level parent that contains the records.

                - **CSVMappingParameters** *(dict) --*

                  Provides additional mapping information when the record format uses
                  delimiters (for example, CSV).

                  - **RecordRowDelimiter** *(string) --*

                    The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
                    delimiter.

                  - **RecordColumnDelimiter** *(string) --*

                    The column delimiter. For example, in a CSV format, a comma (",") is the
                    typical column delimiter.

            - **RecordEncoding** *(string) --*

              Specifies the encoding of the records in the streaming source. For example, UTF-8.

            - **RecordColumns** *(list) --*

              A list of ``RecordColumn`` objects.

              - *(dict) --*

                For an SQL-based Amazon Kinesis Data Analytics application, describes the
                mapping of each data element in the streaming source to the corresponding
                column in the in-application stream.

                Also used to describe the format of the reference data source.

                - **Name** *(string) --*

                  The name of the column that is created in the in-application input stream or
                  reference table.

                - **Mapping** *(string) --*

                  A reference to the data element in the streaming input or the reference data
                  source.

                - **SqlType** *(string) --*

                  The type of column created in the in-application input stream or reference
                  table.

          - **InputParallelism** *(dict) --*

            Describes the configured parallelism (number of in-application streams mapped to
            the streaming source).

            - **Count** *(integer) --*

              The number of in-application streams to create.

          - **InputStartingPositionConfiguration** *(dict) --*

            The point at which the application is configured to read from the input stream.

            - **InputStartingPosition** *(string) --*

              The starting position on the stream.

              * ``NOW`` - Start reading just after the most recent record in the stream, and
              start at the request timestamp that the customer issued.

              * ``TRIM_HORIZON`` - Start reading at the last untrimmed record in the stream,
              which is the oldest record available in the stream. This option is not available
              for an Amazon Kinesis Data Firehose delivery stream.

              * ``LAST_STOPPED_POINT`` - Resume reading from where the application last stopped
              reading.

      - **OutputDescriptions** *(list) --*

        The array of  OutputDescription objects describing the destination streams used by the
        application.

        - *(dict) --*

          For an SQL-based Amazon Kinesis Data Analytics application, describes the application
          output configuration, which includes the in-application stream name and the
          destination where the stream data is written. The destination can be a Kinesis data
          stream or a Kinesis Data Firehose delivery stream.

          - **OutputId** *(string) --*

            A unique identifier for the output configuration.

          - **Name** *(string) --*

            The name of the in-application stream that is configured as output.

          - **KinesisStreamsOutputDescription** *(dict) --*

            Describes the Kinesis data stream that is configured as the destination where
            output is written.

            - **ResourceARN** *(string) --*

              The Amazon Resource Name (ARN) of the Kinesis data stream.

            - **RoleARN** *(string) --*

              The ARN of the IAM role that Kinesis Data Analytics can assume to access the
              stream.

              .. note::

                Provided for backward compatibility. Applications that are created with the
                current API version have an application-level service execution role rather
                than a resource-level role.

          - **KinesisFirehoseOutputDescription** *(dict) --*

            Describes the Kinesis Data Firehose delivery stream that is configured as the
            destination where output is written.

            - **ResourceARN** *(string) --*

              The Amazon Resource Name (ARN) of the delivery stream.

            - **RoleARN** *(string) --*

              The ARN of the IAM role that Kinesis Data Analytics can assume to access the
              stream.

              .. note::

                Provided for backward compatibility. Applications that are created with the
                current API version have an application-level service execution role rather
                than a resource-level role.

          - **LambdaOutputDescription** *(dict) --*

            Describes the Lambda function that is configured as the destination where output is
            written.

            - **ResourceARN** *(string) --*

              The Amazon Resource Name (ARN) of the destination Lambda function.

            - **RoleARN** *(string) --*

              The ARN of the IAM role that Kinesis Data Analytics can assume to write to the
              destination function.

              .. note::

                Provided for backward compatibility. Applications that are created with the
                current API version have an application-level service execution role rather
                than a resource-level role.

          - **DestinationSchema** *(dict) --*

            The data format used for writing data to the destination.

            - **RecordFormatType** *(string) --*

              Specifies the format of the records on the output stream.

      - **ReferenceDataSourceDescriptions** *(list) --*

        The array of  ReferenceDataSourceDescription objects describing the reference data
        sources used by the application.

        - *(dict) --*

          For an SQL-based Amazon Kinesis Data Analytics application, describes the reference
          data source configured for an application.

          - **ReferenceId** *(string) --*

            The ID of the reference data source. This is the ID that Kinesis Data Analytics
            assigns when you add the reference data source to your application using the
            CreateApplication or  UpdateApplication operation.

          - **TableName** *(string) --*

            The in-application table name created by the specific reference data source
            configuration.

          - **S3ReferenceDataSourceDescription** *(dict) --*

            Provides the Amazon S3 bucket name, the object key name that contains the reference
            data.

            - **BucketARN** *(string) --*

              The Amazon Resource Name (ARN) of the S3 bucket.

            - **FileKey** *(string) --*

              Amazon S3 object key name.

            - **ReferenceRoleARN** *(string) --*

              The ARN of the IAM role that Kinesis Data Analytics can assume to read the Amazon
              S3 object on your behalf to populate the in-application reference table.

              .. note::

                Provided for backward compatibility. Applications that are created with the
                current API version have an application-level service execution role rather
                than a resource-level role.

          - **ReferenceSchema** *(dict) --*

            Describes the format of the data in the streaming source, and how each data element
            maps to corresponding columns created in the in-application stream.

            - **RecordFormat** *(dict) --*

              Specifies the format of the records on the streaming source.

              - **RecordFormatType** *(string) --*

                The type of record format.

              - **MappingParameters** *(dict) --*

                When you configure application input at the time of creating or updating an
                application, provides additional mapping information specific to the record
                format (such as JSON, CSV, or record fields delimited by some delimiter) on the
                streaming source.

                - **JSONMappingParameters** *(dict) --*

                  Provides additional mapping information when JSON is the record format on the
                  streaming source.

                  - **RecordRowPath** *(string) --*

                    The path to the top-level parent that contains the records.

                - **CSVMappingParameters** *(dict) --*

                  Provides additional mapping information when the record format uses
                  delimiters (for example, CSV).

                  - **RecordRowDelimiter** *(string) --*

                    The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
                    delimiter.

                  - **RecordColumnDelimiter** *(string) --*

                    The column delimiter. For example, in a CSV format, a comma (",") is the
                    typical column delimiter.

            - **RecordEncoding** *(string) --*

              Specifies the encoding of the records in the streaming source. For example, UTF-8.

            - **RecordColumns** *(list) --*

              A list of ``RecordColumn`` objects.

              - *(dict) --*

                For an SQL-based Amazon Kinesis Data Analytics application, describes the
                mapping of each data element in the streaming source to the corresponding
                column in the in-application stream.

                Also used to describe the format of the reference data source.

                - **Name** *(string) --*

                  The name of the column that is created in the in-application input stream or
                  reference table.

                - **Mapping** *(string) --*

                  A reference to the data element in the streaming input or the reference data
                  source.

                - **SqlType** *(string) --*

                  The type of column created in the in-application input stream or reference
                  table.

    - **ApplicationCodeConfigurationDescription** *(dict) --*

      The details about the application code for a Java-based Kinesis Data Analytics
      application.

      - **CodeContentType** *(string) --*

        Specifies whether the code content is in text or zip format.

      - **CodeContentDescription** *(dict) --*

        Describes details about the location and format of the application code.

        - **TextContent** *(string) --*

          The text-format code

        - **CodeMD5** *(string) --*

          The checksum that can be used to validate zip-format code.

        - **CodeSize** *(integer) --*

          The size in bytes of the application code. Can be used to validate zip-format code.

        - **S3ApplicationCodeLocationDescription** *(dict) --*

          The S3 bucket Amazon Resource Name (ARN), file key, and object version of the
          application code stored in Amazon S3.

          - **BucketARN** *(string) --*

            The Amazon Resource Name (ARN) for the S3 bucket containing the application code.

          - **FileKey** *(string) --*

            The file key for the object containing the application code.

          - **ObjectVersion** *(string) --*

            The version of the object containing the application code.

    - **RunConfigurationDescription** *(dict) --*

      The details about the starting properties for a Kinesis Data Analytics application.

      - **ApplicationRestoreConfigurationDescription** *(dict) --*

        Describes the restore behavior of a restarting application.

        - **ApplicationRestoreType** *(string) --*

          Specifies how the application should be restored.

        - **SnapshotName** *(string) --*

          The identifier of an existing snapshot of application state to use to restart an
          application. The application uses this value if ``RESTORE_FROM_CUSTOM_SNAPSHOT`` is
          specified for the ``ApplicationRestoreType`` .

    - **FlinkApplicationConfigurationDescription** *(dict) --*

      The details about a Java-based Kinesis Data Analytics application.

      - **CheckpointConfigurationDescription** *(dict) --*

        Describes an application's checkpointing configuration. Checkpointing is the process of
        persisting application state for fault tolerance.

        - **ConfigurationType** *(string) --*

          Describes whether the application uses the default checkpointing behavior in Kinesis
          Data Analytics.

        - **CheckpointingEnabled** *(boolean) --*

          Describes whether checkpointing is enabled for a Java-based Kinesis Data Analytics
          application.

        - **CheckpointInterval** *(integer) --*

          Describes the interval in milliseconds between checkpoint operations.

        - **MinPauseBetweenCheckpoints** *(integer) --*

          Describes the minimum time in milliseconds after a checkpoint operation completes
          that a new checkpoint operation can start.

      - **MonitoringConfigurationDescription** *(dict) --*

        Describes configuration parameters for Amazon CloudWatch logging for an application.

        - **ConfigurationType** *(string) --*

          Describes whether to use the default CloudWatch logging configuration for an
          application.

        - **MetricsLevel** *(string) --*

          Describes the granularity of the CloudWatch Logs for an application.

        - **LogLevel** *(string) --*

          Describes the verbosity of the CloudWatch Logs for an application.

      - **ParallelismConfigurationDescription** *(dict) --*

        Describes parameters for how an application executes multiple tasks simultaneously.

        - **ConfigurationType** *(string) --*

          Describes whether the application uses the default parallelism for the Kinesis Data
          Analytics service.

        - **Parallelism** *(integer) --*

          Describes the initial number of parallel tasks that a Java-based Kinesis Data
          Analytics application can perform.

        - **ParallelismPerKPU** *(integer) --*

          Describes the number of parallel tasks that a Java-based Kinesis Data Analytics
          application can perform per Kinesis Processing Unit (KPU) used by the application.

        - **CurrentParallelism** *(integer) --*

          Describes the current number of parallel tasks that a Java-based Kinesis Data
          Analytics application can perform.

        - **AutoScalingEnabled** *(boolean) --*

          Describes whether the Kinesis Data Analytics service can increase the parallelism of
          the application in response to increased throughput.

      - **JobPlanDescription** *(string) --*

        The job plan for an application. For more information about the job plan, see `Jobs and
        Scheduling
        <https://ci.apache.org/projects/flink/flink-docs-stable/internals/job_scheduling.html>`__
        in the `Apache Flink Documentation
        <https://ci.apache.org/projects/flink/flink-docs-release-1.6/>`__ . To retrieve the job
        plan for the application, use the  DescribeApplicationRequest$IncludeAdditionalDetails
        parameter of the  DescribeApplication operation.

    - **EnvironmentPropertyDescriptions** *(dict) --*

      Describes execution properties for a Java-based Kinesis Data Analytics application.

      - **PropertyGroupDescriptions** *(list) --*

        Describes the execution property groups.

        - *(dict) --*

          Property key-value pairs passed into a Java-based Kinesis Data Analytics application.

          - **PropertyGroupId** *(string) --*

            Describes the key of an application execution property key-value pair.

          - **PropertyMap** *(dict) --*

            Describes the value of an application execution property key-value pair.

            - *(string) --*

              - *(string) --*

    - **ApplicationSnapshotConfigurationDescription** *(dict) --*

      Describes whether snapshots are enabled for a Java-based Kinesis Data Analytics
      application.

      - **SnapshotsEnabled** *(boolean) --*

        Describes whether snapshots are enabled for a Java-based Kinesis Data Analytics
        application.
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

    Describes the Amazon CloudWatch logging option.

    - **CloudWatchLoggingOptionId** *(string) --*

      The ID of the CloudWatch logging option description.

    - **LogStreamARN** *(string) --*

      The Amazon Resource Name (ARN) of the CloudWatch log to receive application messages.

    - **RoleARN** *(string) --*

      The IAM ARN of the role to use to send application messages.

      .. note::

        Provided for backward compatibility. Applications created with the current API
        version have an application-level service execution role rather than a resource-level
        role.
    """


_ClientDescribeApplicationResponseApplicationDetailTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailTypeDef",
    {
        "ApplicationARN": str,
        "ApplicationDescription": str,
        "ApplicationName": str,
        "RuntimeEnvironment": str,
        "ServiceExecutionRole": str,
        "ApplicationStatus": str,
        "ApplicationVersionId": int,
        "CreateTimestamp": datetime,
        "LastUpdateTimestamp": datetime,
        "ApplicationConfigurationDescription": ClientDescribeApplicationResponseApplicationDetailApplicationConfigurationDescriptionTypeDef,
        "CloudWatchLoggingOptionDescriptions": List[
            ClientDescribeApplicationResponseApplicationDetailCloudWatchLoggingOptionDescriptionsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailTypeDef
):
    """
    Type definition for `ClientDescribeApplicationResponse` `ApplicationDetail`

    Provides a description of the application, such as the application's Amazon Resource Name
    (ARN), status, and latest version.

    - **ApplicationARN** *(string) --*

      The ARN of the application.

    - **ApplicationDescription** *(string) --*

      The description of the application.

    - **ApplicationName** *(string) --*

      The name of the application.

    - **RuntimeEnvironment** *(string) --*

      The runtime environment for the application (``SQL-1.0`` or ``FLINK-1_6`` ).

    - **ServiceExecutionRole** *(string) --*

      Specifies the IAM role that the application uses to access external resources.

    - **ApplicationStatus** *(string) --*

      The status of the application.

    - **ApplicationVersionId** *(integer) --*

      Provides the current application version. Kinesis Data Analytics updates the
      ``ApplicationVersionId`` each time you update the application.

    - **CreateTimestamp** *(datetime) --*

      The current timestamp when the application was created.

    - **LastUpdateTimestamp** *(datetime) --*

      The current timestamp when the application was last updated.

    - **ApplicationConfigurationDescription** *(dict) --*

      Provides details about the application's SQL or Java code and starting parameters.

      - **SqlApplicationConfigurationDescription** *(dict) --*

        The details about inputs, outputs, and reference data sources for an SQL-based Kinesis
        Data Analytics application.

        - **InputDescriptions** *(list) --*

          The array of  InputDescription objects describing the input streams used by the
          application.

          - *(dict) --*

            Describes the application input configuration for an SQL-based Amazon Kinesis Data
            Analytics application.

            - **InputId** *(string) --*

              The input ID that is associated with the application input. This is the ID that
              Kinesis Data Analytics assigns to each input configuration that you add to your
              application.

            - **NamePrefix** *(string) --*

              The in-application name prefix.

            - **InAppStreamNames** *(list) --*

              Returns the in-application stream names that are mapped to the stream source.

              - *(string) --*

            - **InputProcessingConfigurationDescription** *(dict) --*

              The description of the preprocessor that executes on records in this input before
              the application's code is run.

              - **InputLambdaProcessorDescription** *(dict) --*

                Provides configuration information about the associated
                InputLambdaProcessorDescription

                - **ResourceARN** *(string) --*

                  The ARN of the AWS Lambda function that is used to preprocess the records in
                  the stream.

                  .. note::

                    To specify an earlier version of the Lambda function than the latest, include
                    the Lambda function version in the Lambda function ARN. For more information
                    about Lambda ARNs, see `Example ARNs\\: AWS Lambda
                    </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__

                - **RoleARN** *(string) --*

                  The ARN of the IAM role that is used to access the AWS Lambda function.

                  .. note::

                    Provided for backward compatibility. Applications that are created with the
                    current API version have an application-level service execution role rather
                    than a resource-level role.

            - **KinesisStreamsInputDescription** *(dict) --*

              If a Kinesis data stream is configured as a streaming source, provides the Kinesis
              data stream's Amazon Resource Name (ARN).

              - **ResourceARN** *(string) --*

                The Amazon Resource Name (ARN) of the Kinesis data stream.

              - **RoleARN** *(string) --*

                The ARN of the IAM role that Kinesis Data Analytics can assume to access the
                stream.

                .. note::

                  Provided for backward compatibility. Applications that are created with the
                  current API version have an application-level service execution role rather
                  than a resource-level role.

            - **KinesisFirehoseInputDescription** *(dict) --*

              If a Kinesis Data Firehose delivery stream is configured as a streaming source,
              provides the delivery stream's ARN.

              - **ResourceARN** *(string) --*

                The Amazon Resource Name (ARN) of the delivery stream.

              - **RoleARN** *(string) --*

                The ARN of the IAM role that Kinesis Data Analytics assumes to access the stream.

                .. note::

                  Provided for backward compatibility. Applications that are created with the
                  current API version have an application-level service execution role rather
                  than a resource-level role.

            - **InputSchema** *(dict) --*

              Describes the format of the data in the streaming source, and how each data element
              maps to corresponding columns in the in-application stream that is being created.

              - **RecordFormat** *(dict) --*

                Specifies the format of the records on the streaming source.

                - **RecordFormatType** *(string) --*

                  The type of record format.

                - **MappingParameters** *(dict) --*

                  When you configure application input at the time of creating or updating an
                  application, provides additional mapping information specific to the record
                  format (such as JSON, CSV, or record fields delimited by some delimiter) on the
                  streaming source.

                  - **JSONMappingParameters** *(dict) --*

                    Provides additional mapping information when JSON is the record format on the
                    streaming source.

                    - **RecordRowPath** *(string) --*

                      The path to the top-level parent that contains the records.

                  - **CSVMappingParameters** *(dict) --*

                    Provides additional mapping information when the record format uses
                    delimiters (for example, CSV).

                    - **RecordRowDelimiter** *(string) --*

                      The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
                      delimiter.

                    - **RecordColumnDelimiter** *(string) --*

                      The column delimiter. For example, in a CSV format, a comma (",") is the
                      typical column delimiter.

              - **RecordEncoding** *(string) --*

                Specifies the encoding of the records in the streaming source. For example, UTF-8.

              - **RecordColumns** *(list) --*

                A list of ``RecordColumn`` objects.

                - *(dict) --*

                  For an SQL-based Amazon Kinesis Data Analytics application, describes the
                  mapping of each data element in the streaming source to the corresponding
                  column in the in-application stream.

                  Also used to describe the format of the reference data source.

                  - **Name** *(string) --*

                    The name of the column that is created in the in-application input stream or
                    reference table.

                  - **Mapping** *(string) --*

                    A reference to the data element in the streaming input or the reference data
                    source.

                  - **SqlType** *(string) --*

                    The type of column created in the in-application input stream or reference
                    table.

            - **InputParallelism** *(dict) --*

              Describes the configured parallelism (number of in-application streams mapped to
              the streaming source).

              - **Count** *(integer) --*

                The number of in-application streams to create.

            - **InputStartingPositionConfiguration** *(dict) --*

              The point at which the application is configured to read from the input stream.

              - **InputStartingPosition** *(string) --*

                The starting position on the stream.

                * ``NOW`` - Start reading just after the most recent record in the stream, and
                start at the request timestamp that the customer issued.

                * ``TRIM_HORIZON`` - Start reading at the last untrimmed record in the stream,
                which is the oldest record available in the stream. This option is not available
                for an Amazon Kinesis Data Firehose delivery stream.

                * ``LAST_STOPPED_POINT`` - Resume reading from where the application last stopped
                reading.

        - **OutputDescriptions** *(list) --*

          The array of  OutputDescription objects describing the destination streams used by the
          application.

          - *(dict) --*

            For an SQL-based Amazon Kinesis Data Analytics application, describes the application
            output configuration, which includes the in-application stream name and the
            destination where the stream data is written. The destination can be a Kinesis data
            stream or a Kinesis Data Firehose delivery stream.

            - **OutputId** *(string) --*

              A unique identifier for the output configuration.

            - **Name** *(string) --*

              The name of the in-application stream that is configured as output.

            - **KinesisStreamsOutputDescription** *(dict) --*

              Describes the Kinesis data stream that is configured as the destination where
              output is written.

              - **ResourceARN** *(string) --*

                The Amazon Resource Name (ARN) of the Kinesis data stream.

              - **RoleARN** *(string) --*

                The ARN of the IAM role that Kinesis Data Analytics can assume to access the
                stream.

                .. note::

                  Provided for backward compatibility. Applications that are created with the
                  current API version have an application-level service execution role rather
                  than a resource-level role.

            - **KinesisFirehoseOutputDescription** *(dict) --*

              Describes the Kinesis Data Firehose delivery stream that is configured as the
              destination where output is written.

              - **ResourceARN** *(string) --*

                The Amazon Resource Name (ARN) of the delivery stream.

              - **RoleARN** *(string) --*

                The ARN of the IAM role that Kinesis Data Analytics can assume to access the
                stream.

                .. note::

                  Provided for backward compatibility. Applications that are created with the
                  current API version have an application-level service execution role rather
                  than a resource-level role.

            - **LambdaOutputDescription** *(dict) --*

              Describes the Lambda function that is configured as the destination where output is
              written.

              - **ResourceARN** *(string) --*

                The Amazon Resource Name (ARN) of the destination Lambda function.

              - **RoleARN** *(string) --*

                The ARN of the IAM role that Kinesis Data Analytics can assume to write to the
                destination function.

                .. note::

                  Provided for backward compatibility. Applications that are created with the
                  current API version have an application-level service execution role rather
                  than a resource-level role.

            - **DestinationSchema** *(dict) --*

              The data format used for writing data to the destination.

              - **RecordFormatType** *(string) --*

                Specifies the format of the records on the output stream.

        - **ReferenceDataSourceDescriptions** *(list) --*

          The array of  ReferenceDataSourceDescription objects describing the reference data
          sources used by the application.

          - *(dict) --*

            For an SQL-based Amazon Kinesis Data Analytics application, describes the reference
            data source configured for an application.

            - **ReferenceId** *(string) --*

              The ID of the reference data source. This is the ID that Kinesis Data Analytics
              assigns when you add the reference data source to your application using the
              CreateApplication or  UpdateApplication operation.

            - **TableName** *(string) --*

              The in-application table name created by the specific reference data source
              configuration.

            - **S3ReferenceDataSourceDescription** *(dict) --*

              Provides the Amazon S3 bucket name, the object key name that contains the reference
              data.

              - **BucketARN** *(string) --*

                The Amazon Resource Name (ARN) of the S3 bucket.

              - **FileKey** *(string) --*

                Amazon S3 object key name.

              - **ReferenceRoleARN** *(string) --*

                The ARN of the IAM role that Kinesis Data Analytics can assume to read the Amazon
                S3 object on your behalf to populate the in-application reference table.

                .. note::

                  Provided for backward compatibility. Applications that are created with the
                  current API version have an application-level service execution role rather
                  than a resource-level role.

            - **ReferenceSchema** *(dict) --*

              Describes the format of the data in the streaming source, and how each data element
              maps to corresponding columns created in the in-application stream.

              - **RecordFormat** *(dict) --*

                Specifies the format of the records on the streaming source.

                - **RecordFormatType** *(string) --*

                  The type of record format.

                - **MappingParameters** *(dict) --*

                  When you configure application input at the time of creating or updating an
                  application, provides additional mapping information specific to the record
                  format (such as JSON, CSV, or record fields delimited by some delimiter) on the
                  streaming source.

                  - **JSONMappingParameters** *(dict) --*

                    Provides additional mapping information when JSON is the record format on the
                    streaming source.

                    - **RecordRowPath** *(string) --*

                      The path to the top-level parent that contains the records.

                  - **CSVMappingParameters** *(dict) --*

                    Provides additional mapping information when the record format uses
                    delimiters (for example, CSV).

                    - **RecordRowDelimiter** *(string) --*

                      The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
                      delimiter.

                    - **RecordColumnDelimiter** *(string) --*

                      The column delimiter. For example, in a CSV format, a comma (",") is the
                      typical column delimiter.

              - **RecordEncoding** *(string) --*

                Specifies the encoding of the records in the streaming source. For example, UTF-8.

              - **RecordColumns** *(list) --*

                A list of ``RecordColumn`` objects.

                - *(dict) --*

                  For an SQL-based Amazon Kinesis Data Analytics application, describes the
                  mapping of each data element in the streaming source to the corresponding
                  column in the in-application stream.

                  Also used to describe the format of the reference data source.

                  - **Name** *(string) --*

                    The name of the column that is created in the in-application input stream or
                    reference table.

                  - **Mapping** *(string) --*

                    A reference to the data element in the streaming input or the reference data
                    source.

                  - **SqlType** *(string) --*

                    The type of column created in the in-application input stream or reference
                    table.

      - **ApplicationCodeConfigurationDescription** *(dict) --*

        The details about the application code for a Java-based Kinesis Data Analytics
        application.

        - **CodeContentType** *(string) --*

          Specifies whether the code content is in text or zip format.

        - **CodeContentDescription** *(dict) --*

          Describes details about the location and format of the application code.

          - **TextContent** *(string) --*

            The text-format code

          - **CodeMD5** *(string) --*

            The checksum that can be used to validate zip-format code.

          - **CodeSize** *(integer) --*

            The size in bytes of the application code. Can be used to validate zip-format code.

          - **S3ApplicationCodeLocationDescription** *(dict) --*

            The S3 bucket Amazon Resource Name (ARN), file key, and object version of the
            application code stored in Amazon S3.

            - **BucketARN** *(string) --*

              The Amazon Resource Name (ARN) for the S3 bucket containing the application code.

            - **FileKey** *(string) --*

              The file key for the object containing the application code.

            - **ObjectVersion** *(string) --*

              The version of the object containing the application code.

      - **RunConfigurationDescription** *(dict) --*

        The details about the starting properties for a Kinesis Data Analytics application.

        - **ApplicationRestoreConfigurationDescription** *(dict) --*

          Describes the restore behavior of a restarting application.

          - **ApplicationRestoreType** *(string) --*

            Specifies how the application should be restored.

          - **SnapshotName** *(string) --*

            The identifier of an existing snapshot of application state to use to restart an
            application. The application uses this value if ``RESTORE_FROM_CUSTOM_SNAPSHOT`` is
            specified for the ``ApplicationRestoreType`` .

      - **FlinkApplicationConfigurationDescription** *(dict) --*

        The details about a Java-based Kinesis Data Analytics application.

        - **CheckpointConfigurationDescription** *(dict) --*

          Describes an application's checkpointing configuration. Checkpointing is the process of
          persisting application state for fault tolerance.

          - **ConfigurationType** *(string) --*

            Describes whether the application uses the default checkpointing behavior in Kinesis
            Data Analytics.

          - **CheckpointingEnabled** *(boolean) --*

            Describes whether checkpointing is enabled for a Java-based Kinesis Data Analytics
            application.

          - **CheckpointInterval** *(integer) --*

            Describes the interval in milliseconds between checkpoint operations.

          - **MinPauseBetweenCheckpoints** *(integer) --*

            Describes the minimum time in milliseconds after a checkpoint operation completes
            that a new checkpoint operation can start.

        - **MonitoringConfigurationDescription** *(dict) --*

          Describes configuration parameters for Amazon CloudWatch logging for an application.

          - **ConfigurationType** *(string) --*

            Describes whether to use the default CloudWatch logging configuration for an
            application.

          - **MetricsLevel** *(string) --*

            Describes the granularity of the CloudWatch Logs for an application.

          - **LogLevel** *(string) --*

            Describes the verbosity of the CloudWatch Logs for an application.

        - **ParallelismConfigurationDescription** *(dict) --*

          Describes parameters for how an application executes multiple tasks simultaneously.

          - **ConfigurationType** *(string) --*

            Describes whether the application uses the default parallelism for the Kinesis Data
            Analytics service.

          - **Parallelism** *(integer) --*

            Describes the initial number of parallel tasks that a Java-based Kinesis Data
            Analytics application can perform.

          - **ParallelismPerKPU** *(integer) --*

            Describes the number of parallel tasks that a Java-based Kinesis Data Analytics
            application can perform per Kinesis Processing Unit (KPU) used by the application.

          - **CurrentParallelism** *(integer) --*

            Describes the current number of parallel tasks that a Java-based Kinesis Data
            Analytics application can perform.

          - **AutoScalingEnabled** *(boolean) --*

            Describes whether the Kinesis Data Analytics service can increase the parallelism of
            the application in response to increased throughput.

        - **JobPlanDescription** *(string) --*

          The job plan for an application. For more information about the job plan, see `Jobs and
          Scheduling
          <https://ci.apache.org/projects/flink/flink-docs-stable/internals/job_scheduling.html>`__
          in the `Apache Flink Documentation
          <https://ci.apache.org/projects/flink/flink-docs-release-1.6/>`__ . To retrieve the job
          plan for the application, use the  DescribeApplicationRequest$IncludeAdditionalDetails
          parameter of the  DescribeApplication operation.

      - **EnvironmentPropertyDescriptions** *(dict) --*

        Describes execution properties for a Java-based Kinesis Data Analytics application.

        - **PropertyGroupDescriptions** *(list) --*

          Describes the execution property groups.

          - *(dict) --*

            Property key-value pairs passed into a Java-based Kinesis Data Analytics application.

            - **PropertyGroupId** *(string) --*

              Describes the key of an application execution property key-value pair.

            - **PropertyMap** *(dict) --*

              Describes the value of an application execution property key-value pair.

              - *(string) --*

                - *(string) --*

      - **ApplicationSnapshotConfigurationDescription** *(dict) --*

        Describes whether snapshots are enabled for a Java-based Kinesis Data Analytics
        application.

        - **SnapshotsEnabled** *(boolean) --*

          Describes whether snapshots are enabled for a Java-based Kinesis Data Analytics
          application.

    - **CloudWatchLoggingOptionDescriptions** *(list) --*

      Describes the application Amazon CloudWatch logging options.

      - *(dict) --*

        Describes the Amazon CloudWatch logging option.

        - **CloudWatchLoggingOptionId** *(string) --*

          The ID of the CloudWatch logging option description.

        - **LogStreamARN** *(string) --*

          The Amazon Resource Name (ARN) of the CloudWatch log to receive application messages.

        - **RoleARN** *(string) --*

          The IAM ARN of the role to use to send application messages.

          .. note::

            Provided for backward compatibility. Applications created with the current API
            version have an application-level service execution role rather than a resource-level
            role.
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

      Provides a description of the application, such as the application's Amazon Resource Name
      (ARN), status, and latest version.

      - **ApplicationARN** *(string) --*

        The ARN of the application.

      - **ApplicationDescription** *(string) --*

        The description of the application.

      - **ApplicationName** *(string) --*

        The name of the application.

      - **RuntimeEnvironment** *(string) --*

        The runtime environment for the application (``SQL-1.0`` or ``FLINK-1_6`` ).

      - **ServiceExecutionRole** *(string) --*

        Specifies the IAM role that the application uses to access external resources.

      - **ApplicationStatus** *(string) --*

        The status of the application.

      - **ApplicationVersionId** *(integer) --*

        Provides the current application version. Kinesis Data Analytics updates the
        ``ApplicationVersionId`` each time you update the application.

      - **CreateTimestamp** *(datetime) --*

        The current timestamp when the application was created.

      - **LastUpdateTimestamp** *(datetime) --*

        The current timestamp when the application was last updated.

      - **ApplicationConfigurationDescription** *(dict) --*

        Provides details about the application's SQL or Java code and starting parameters.

        - **SqlApplicationConfigurationDescription** *(dict) --*

          The details about inputs, outputs, and reference data sources for an SQL-based Kinesis
          Data Analytics application.

          - **InputDescriptions** *(list) --*

            The array of  InputDescription objects describing the input streams used by the
            application.

            - *(dict) --*

              Describes the application input configuration for an SQL-based Amazon Kinesis Data
              Analytics application.

              - **InputId** *(string) --*

                The input ID that is associated with the application input. This is the ID that
                Kinesis Data Analytics assigns to each input configuration that you add to your
                application.

              - **NamePrefix** *(string) --*

                The in-application name prefix.

              - **InAppStreamNames** *(list) --*

                Returns the in-application stream names that are mapped to the stream source.

                - *(string) --*

              - **InputProcessingConfigurationDescription** *(dict) --*

                The description of the preprocessor that executes on records in this input before
                the application's code is run.

                - **InputLambdaProcessorDescription** *(dict) --*

                  Provides configuration information about the associated
                  InputLambdaProcessorDescription

                  - **ResourceARN** *(string) --*

                    The ARN of the AWS Lambda function that is used to preprocess the records in
                    the stream.

                    .. note::

                      To specify an earlier version of the Lambda function than the latest, include
                      the Lambda function version in the Lambda function ARN. For more information
                      about Lambda ARNs, see `Example ARNs\\: AWS Lambda
                      </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__

                  - **RoleARN** *(string) --*

                    The ARN of the IAM role that is used to access the AWS Lambda function.

                    .. note::

                      Provided for backward compatibility. Applications that are created with the
                      current API version have an application-level service execution role rather
                      than a resource-level role.

              - **KinesisStreamsInputDescription** *(dict) --*

                If a Kinesis data stream is configured as a streaming source, provides the Kinesis
                data stream's Amazon Resource Name (ARN).

                - **ResourceARN** *(string) --*

                  The Amazon Resource Name (ARN) of the Kinesis data stream.

                - **RoleARN** *(string) --*

                  The ARN of the IAM role that Kinesis Data Analytics can assume to access the
                  stream.

                  .. note::

                    Provided for backward compatibility. Applications that are created with the
                    current API version have an application-level service execution role rather
                    than a resource-level role.

              - **KinesisFirehoseInputDescription** *(dict) --*

                If a Kinesis Data Firehose delivery stream is configured as a streaming source,
                provides the delivery stream's ARN.

                - **ResourceARN** *(string) --*

                  The Amazon Resource Name (ARN) of the delivery stream.

                - **RoleARN** *(string) --*

                  The ARN of the IAM role that Kinesis Data Analytics assumes to access the stream.

                  .. note::

                    Provided for backward compatibility. Applications that are created with the
                    current API version have an application-level service execution role rather
                    than a resource-level role.

              - **InputSchema** *(dict) --*

                Describes the format of the data in the streaming source, and how each data element
                maps to corresponding columns in the in-application stream that is being created.

                - **RecordFormat** *(dict) --*

                  Specifies the format of the records on the streaming source.

                  - **RecordFormatType** *(string) --*

                    The type of record format.

                  - **MappingParameters** *(dict) --*

                    When you configure application input at the time of creating or updating an
                    application, provides additional mapping information specific to the record
                    format (such as JSON, CSV, or record fields delimited by some delimiter) on the
                    streaming source.

                    - **JSONMappingParameters** *(dict) --*

                      Provides additional mapping information when JSON is the record format on the
                      streaming source.

                      - **RecordRowPath** *(string) --*

                        The path to the top-level parent that contains the records.

                    - **CSVMappingParameters** *(dict) --*

                      Provides additional mapping information when the record format uses
                      delimiters (for example, CSV).

                      - **RecordRowDelimiter** *(string) --*

                        The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
                        delimiter.

                      - **RecordColumnDelimiter** *(string) --*

                        The column delimiter. For example, in a CSV format, a comma (",") is the
                        typical column delimiter.

                - **RecordEncoding** *(string) --*

                  Specifies the encoding of the records in the streaming source. For example, UTF-8.

                - **RecordColumns** *(list) --*

                  A list of ``RecordColumn`` objects.

                  - *(dict) --*

                    For an SQL-based Amazon Kinesis Data Analytics application, describes the
                    mapping of each data element in the streaming source to the corresponding
                    column in the in-application stream.

                    Also used to describe the format of the reference data source.

                    - **Name** *(string) --*

                      The name of the column that is created in the in-application input stream or
                      reference table.

                    - **Mapping** *(string) --*

                      A reference to the data element in the streaming input or the reference data
                      source.

                    - **SqlType** *(string) --*

                      The type of column created in the in-application input stream or reference
                      table.

              - **InputParallelism** *(dict) --*

                Describes the configured parallelism (number of in-application streams mapped to
                the streaming source).

                - **Count** *(integer) --*

                  The number of in-application streams to create.

              - **InputStartingPositionConfiguration** *(dict) --*

                The point at which the application is configured to read from the input stream.

                - **InputStartingPosition** *(string) --*

                  The starting position on the stream.

                  * ``NOW`` - Start reading just after the most recent record in the stream, and
                  start at the request timestamp that the customer issued.

                  * ``TRIM_HORIZON`` - Start reading at the last untrimmed record in the stream,
                  which is the oldest record available in the stream. This option is not available
                  for an Amazon Kinesis Data Firehose delivery stream.

                  * ``LAST_STOPPED_POINT`` - Resume reading from where the application last stopped
                  reading.

          - **OutputDescriptions** *(list) --*

            The array of  OutputDescription objects describing the destination streams used by the
            application.

            - *(dict) --*

              For an SQL-based Amazon Kinesis Data Analytics application, describes the application
              output configuration, which includes the in-application stream name and the
              destination where the stream data is written. The destination can be a Kinesis data
              stream or a Kinesis Data Firehose delivery stream.

              - **OutputId** *(string) --*

                A unique identifier for the output configuration.

              - **Name** *(string) --*

                The name of the in-application stream that is configured as output.

              - **KinesisStreamsOutputDescription** *(dict) --*

                Describes the Kinesis data stream that is configured as the destination where
                output is written.

                - **ResourceARN** *(string) --*

                  The Amazon Resource Name (ARN) of the Kinesis data stream.

                - **RoleARN** *(string) --*

                  The ARN of the IAM role that Kinesis Data Analytics can assume to access the
                  stream.

                  .. note::

                    Provided for backward compatibility. Applications that are created with the
                    current API version have an application-level service execution role rather
                    than a resource-level role.

              - **KinesisFirehoseOutputDescription** *(dict) --*

                Describes the Kinesis Data Firehose delivery stream that is configured as the
                destination where output is written.

                - **ResourceARN** *(string) --*

                  The Amazon Resource Name (ARN) of the delivery stream.

                - **RoleARN** *(string) --*

                  The ARN of the IAM role that Kinesis Data Analytics can assume to access the
                  stream.

                  .. note::

                    Provided for backward compatibility. Applications that are created with the
                    current API version have an application-level service execution role rather
                    than a resource-level role.

              - **LambdaOutputDescription** *(dict) --*

                Describes the Lambda function that is configured as the destination where output is
                written.

                - **ResourceARN** *(string) --*

                  The Amazon Resource Name (ARN) of the destination Lambda function.

                - **RoleARN** *(string) --*

                  The ARN of the IAM role that Kinesis Data Analytics can assume to write to the
                  destination function.

                  .. note::

                    Provided for backward compatibility. Applications that are created with the
                    current API version have an application-level service execution role rather
                    than a resource-level role.

              - **DestinationSchema** *(dict) --*

                The data format used for writing data to the destination.

                - **RecordFormatType** *(string) --*

                  Specifies the format of the records on the output stream.

          - **ReferenceDataSourceDescriptions** *(list) --*

            The array of  ReferenceDataSourceDescription objects describing the reference data
            sources used by the application.

            - *(dict) --*

              For an SQL-based Amazon Kinesis Data Analytics application, describes the reference
              data source configured for an application.

              - **ReferenceId** *(string) --*

                The ID of the reference data source. This is the ID that Kinesis Data Analytics
                assigns when you add the reference data source to your application using the
                CreateApplication or  UpdateApplication operation.

              - **TableName** *(string) --*

                The in-application table name created by the specific reference data source
                configuration.

              - **S3ReferenceDataSourceDescription** *(dict) --*

                Provides the Amazon S3 bucket name, the object key name that contains the reference
                data.

                - **BucketARN** *(string) --*

                  The Amazon Resource Name (ARN) of the S3 bucket.

                - **FileKey** *(string) --*

                  Amazon S3 object key name.

                - **ReferenceRoleARN** *(string) --*

                  The ARN of the IAM role that Kinesis Data Analytics can assume to read the Amazon
                  S3 object on your behalf to populate the in-application reference table.

                  .. note::

                    Provided for backward compatibility. Applications that are created with the
                    current API version have an application-level service execution role rather
                    than a resource-level role.

              - **ReferenceSchema** *(dict) --*

                Describes the format of the data in the streaming source, and how each data element
                maps to corresponding columns created in the in-application stream.

                - **RecordFormat** *(dict) --*

                  Specifies the format of the records on the streaming source.

                  - **RecordFormatType** *(string) --*

                    The type of record format.

                  - **MappingParameters** *(dict) --*

                    When you configure application input at the time of creating or updating an
                    application, provides additional mapping information specific to the record
                    format (such as JSON, CSV, or record fields delimited by some delimiter) on the
                    streaming source.

                    - **JSONMappingParameters** *(dict) --*

                      Provides additional mapping information when JSON is the record format on the
                      streaming source.

                      - **RecordRowPath** *(string) --*

                        The path to the top-level parent that contains the records.

                    - **CSVMappingParameters** *(dict) --*

                      Provides additional mapping information when the record format uses
                      delimiters (for example, CSV).

                      - **RecordRowDelimiter** *(string) --*

                        The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
                        delimiter.

                      - **RecordColumnDelimiter** *(string) --*

                        The column delimiter. For example, in a CSV format, a comma (",") is the
                        typical column delimiter.

                - **RecordEncoding** *(string) --*

                  Specifies the encoding of the records in the streaming source. For example, UTF-8.

                - **RecordColumns** *(list) --*

                  A list of ``RecordColumn`` objects.

                  - *(dict) --*

                    For an SQL-based Amazon Kinesis Data Analytics application, describes the
                    mapping of each data element in the streaming source to the corresponding
                    column in the in-application stream.

                    Also used to describe the format of the reference data source.

                    - **Name** *(string) --*

                      The name of the column that is created in the in-application input stream or
                      reference table.

                    - **Mapping** *(string) --*

                      A reference to the data element in the streaming input or the reference data
                      source.

                    - **SqlType** *(string) --*

                      The type of column created in the in-application input stream or reference
                      table.

        - **ApplicationCodeConfigurationDescription** *(dict) --*

          The details about the application code for a Java-based Kinesis Data Analytics
          application.

          - **CodeContentType** *(string) --*

            Specifies whether the code content is in text or zip format.

          - **CodeContentDescription** *(dict) --*

            Describes details about the location and format of the application code.

            - **TextContent** *(string) --*

              The text-format code

            - **CodeMD5** *(string) --*

              The checksum that can be used to validate zip-format code.

            - **CodeSize** *(integer) --*

              The size in bytes of the application code. Can be used to validate zip-format code.

            - **S3ApplicationCodeLocationDescription** *(dict) --*

              The S3 bucket Amazon Resource Name (ARN), file key, and object version of the
              application code stored in Amazon S3.

              - **BucketARN** *(string) --*

                The Amazon Resource Name (ARN) for the S3 bucket containing the application code.

              - **FileKey** *(string) --*

                The file key for the object containing the application code.

              - **ObjectVersion** *(string) --*

                The version of the object containing the application code.

        - **RunConfigurationDescription** *(dict) --*

          The details about the starting properties for a Kinesis Data Analytics application.

          - **ApplicationRestoreConfigurationDescription** *(dict) --*

            Describes the restore behavior of a restarting application.

            - **ApplicationRestoreType** *(string) --*

              Specifies how the application should be restored.

            - **SnapshotName** *(string) --*

              The identifier of an existing snapshot of application state to use to restart an
              application. The application uses this value if ``RESTORE_FROM_CUSTOM_SNAPSHOT`` is
              specified for the ``ApplicationRestoreType`` .

        - **FlinkApplicationConfigurationDescription** *(dict) --*

          The details about a Java-based Kinesis Data Analytics application.

          - **CheckpointConfigurationDescription** *(dict) --*

            Describes an application's checkpointing configuration. Checkpointing is the process of
            persisting application state for fault tolerance.

            - **ConfigurationType** *(string) --*

              Describes whether the application uses the default checkpointing behavior in Kinesis
              Data Analytics.

            - **CheckpointingEnabled** *(boolean) --*

              Describes whether checkpointing is enabled for a Java-based Kinesis Data Analytics
              application.

            - **CheckpointInterval** *(integer) --*

              Describes the interval in milliseconds between checkpoint operations.

            - **MinPauseBetweenCheckpoints** *(integer) --*

              Describes the minimum time in milliseconds after a checkpoint operation completes
              that a new checkpoint operation can start.

          - **MonitoringConfigurationDescription** *(dict) --*

            Describes configuration parameters for Amazon CloudWatch logging for an application.

            - **ConfigurationType** *(string) --*

              Describes whether to use the default CloudWatch logging configuration for an
              application.

            - **MetricsLevel** *(string) --*

              Describes the granularity of the CloudWatch Logs for an application.

            - **LogLevel** *(string) --*

              Describes the verbosity of the CloudWatch Logs for an application.

          - **ParallelismConfigurationDescription** *(dict) --*

            Describes parameters for how an application executes multiple tasks simultaneously.

            - **ConfigurationType** *(string) --*

              Describes whether the application uses the default parallelism for the Kinesis Data
              Analytics service.

            - **Parallelism** *(integer) --*

              Describes the initial number of parallel tasks that a Java-based Kinesis Data
              Analytics application can perform.

            - **ParallelismPerKPU** *(integer) --*

              Describes the number of parallel tasks that a Java-based Kinesis Data Analytics
              application can perform per Kinesis Processing Unit (KPU) used by the application.

            - **CurrentParallelism** *(integer) --*

              Describes the current number of parallel tasks that a Java-based Kinesis Data
              Analytics application can perform.

            - **AutoScalingEnabled** *(boolean) --*

              Describes whether the Kinesis Data Analytics service can increase the parallelism of
              the application in response to increased throughput.

          - **JobPlanDescription** *(string) --*

            The job plan for an application. For more information about the job plan, see `Jobs and
            Scheduling
            <https://ci.apache.org/projects/flink/flink-docs-stable/internals/job_scheduling.html>`__
            in the `Apache Flink Documentation
            <https://ci.apache.org/projects/flink/flink-docs-release-1.6/>`__ . To retrieve the job
            plan for the application, use the  DescribeApplicationRequest$IncludeAdditionalDetails
            parameter of the  DescribeApplication operation.

        - **EnvironmentPropertyDescriptions** *(dict) --*

          Describes execution properties for a Java-based Kinesis Data Analytics application.

          - **PropertyGroupDescriptions** *(list) --*

            Describes the execution property groups.

            - *(dict) --*

              Property key-value pairs passed into a Java-based Kinesis Data Analytics application.

              - **PropertyGroupId** *(string) --*

                Describes the key of an application execution property key-value pair.

              - **PropertyMap** *(dict) --*

                Describes the value of an application execution property key-value pair.

                - *(string) --*

                  - *(string) --*

        - **ApplicationSnapshotConfigurationDescription** *(dict) --*

          Describes whether snapshots are enabled for a Java-based Kinesis Data Analytics
          application.

          - **SnapshotsEnabled** *(boolean) --*

            Describes whether snapshots are enabled for a Java-based Kinesis Data Analytics
            application.

      - **CloudWatchLoggingOptionDescriptions** *(list) --*

        Describes the application Amazon CloudWatch logging options.

        - *(dict) --*

          Describes the Amazon CloudWatch logging option.

          - **CloudWatchLoggingOptionId** *(string) --*

            The ID of the CloudWatch logging option description.

          - **LogStreamARN** *(string) --*

            The Amazon Resource Name (ARN) of the CloudWatch log to receive application messages.

          - **RoleARN** *(string) --*

            The IAM ARN of the role to use to send application messages.

            .. note::

              Provided for backward compatibility. Applications created with the current API
              version have an application-level service execution role rather than a resource-level
              role.
    """


_ClientDescribeApplicationSnapshotResponseSnapshotDetailsTypeDef = TypedDict(
    "_ClientDescribeApplicationSnapshotResponseSnapshotDetailsTypeDef",
    {
        "SnapshotName": str,
        "SnapshotStatus": str,
        "ApplicationVersionId": int,
        "SnapshotCreationTimestamp": datetime,
    },
    total=False,
)


class ClientDescribeApplicationSnapshotResponseSnapshotDetailsTypeDef(
    _ClientDescribeApplicationSnapshotResponseSnapshotDetailsTypeDef
):
    """
    Type definition for `ClientDescribeApplicationSnapshotResponse` `SnapshotDetails`

    An object containing information about the application snapshot.

    - **SnapshotName** *(string) --*

      The identifier for the application snapshot.

    - **SnapshotStatus** *(string) --*

      The status of the application snapshot.

    - **ApplicationVersionId** *(integer) --*

      The current application version ID when the snapshot was created.

    - **SnapshotCreationTimestamp** *(datetime) --*

      The timestamp of the application snapshot.
    """


_ClientDescribeApplicationSnapshotResponseTypeDef = TypedDict(
    "_ClientDescribeApplicationSnapshotResponseTypeDef",
    {
        "SnapshotDetails": ClientDescribeApplicationSnapshotResponseSnapshotDetailsTypeDef
    },
    total=False,
)


class ClientDescribeApplicationSnapshotResponseTypeDef(
    _ClientDescribeApplicationSnapshotResponseTypeDef
):
    """
    Type definition for `ClientDescribeApplicationSnapshot` `Response`

    - **SnapshotDetails** *(dict) --*

      An object containing information about the application snapshot.

      - **SnapshotName** *(string) --*

        The identifier for the application snapshot.

      - **SnapshotStatus** *(string) --*

        The status of the application snapshot.

      - **ApplicationVersionId** *(integer) --*

        The current application version ID when the snapshot was created.

      - **SnapshotCreationTimestamp** *(datetime) --*

        The timestamp of the application snapshot.
    """


_ClientDiscoverInputSchemaInputProcessingConfigurationInputLambdaProcessorTypeDef = TypedDict(
    "_ClientDiscoverInputSchemaInputProcessingConfigurationInputLambdaProcessorTypeDef",
    {"ResourceARN": str},
)


class ClientDiscoverInputSchemaInputProcessingConfigurationInputLambdaProcessorTypeDef(
    _ClientDiscoverInputSchemaInputProcessingConfigurationInputLambdaProcessorTypeDef
):
    """
    Type definition for `ClientDiscoverInputSchemaInputProcessingConfiguration` `InputLambdaProcessor`

    The  InputLambdaProcessor that is used to preprocess the records in the stream before being
    processed by your application code.

    - **ResourceARN** *(string) --* **[REQUIRED]**

      The ARN of the AWS Lambda function that operates on records in the stream.

      .. note::

        To specify an earlier version of the Lambda function than the latest, include the Lambda
        function version in the Lambda function ARN. For more information about Lambda ARNs, see
        `Example ARNs\\: AWS Lambda
        </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__
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

    The  InputProcessingConfiguration to use to preprocess the records before discovering the schema
    of the records.

    - **InputLambdaProcessor** *(dict) --* **[REQUIRED]**

      The  InputLambdaProcessor that is used to preprocess the records in the stream before being
      processed by your application code.

      - **ResourceARN** *(string) --* **[REQUIRED]**

        The ARN of the AWS Lambda function that operates on records in the stream.

        .. note::

          To specify an earlier version of the Lambda function than the latest, include the Lambda
          function version in the Lambda function ARN. For more information about Lambda ARNs, see
          `Example ARNs\\: AWS Lambda
          </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__
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

    The point at which you want Kinesis Data Analytics to start reading records from the specified
    streaming source discovery purposes.

    - **InputStartingPosition** *(string) --*

      The starting position on the stream.

      * ``NOW`` - Start reading just after the most recent record in the stream, and start at the
      request timestamp that the customer issued.

      * ``TRIM_HORIZON`` - Start reading at the last untrimmed record in the stream, which is the
      oldest record available in the stream. This option is not available for an Amazon Kinesis Data
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

    For an SQL-based Amazon Kinesis Data Analytics application, describes the mapping of each
    data element in the streaming source to the corresponding column in the in-application
    stream.

    Also used to describe the format of the reference data source.

    - **Name** *(string) --*

      The name of the column that is created in the in-application input stream or reference
      table.

    - **Mapping** *(string) --*

      A reference to the data element in the streaming input or the reference data source.

    - **SqlType** *(string) --*

      The type of column created in the in-application input stream or reference table.
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

      The row delimiter. For example, in a CSV format, *'\\n'* is the typical row delimiter.

    - **RecordColumnDelimiter** *(string) --*

      The column delimiter. For example, in a CSV format, a comma (",") is the typical
      column delimiter.
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

      The path to the top-level parent that contains the records.
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

    When you configure application input at the time of creating or updating an application,
    provides additional mapping information specific to the record format (such as JSON, CSV,
    or record fields delimited by some delimiter) on the streaming source.

    - **JSONMappingParameters** *(dict) --*

      Provides additional mapping information when JSON is the record format on the streaming
      source.

      - **RecordRowPath** *(string) --*

        The path to the top-level parent that contains the records.

    - **CSVMappingParameters** *(dict) --*

      Provides additional mapping information when the record format uses delimiters (for
      example, CSV).

      - **RecordRowDelimiter** *(string) --*

        The row delimiter. For example, in a CSV format, *'\\n'* is the typical row delimiter.

      - **RecordColumnDelimiter** *(string) --*

        The column delimiter. For example, in a CSV format, a comma (",") is the typical
        column delimiter.
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

      When you configure application input at the time of creating or updating an application,
      provides additional mapping information specific to the record format (such as JSON, CSV,
      or record fields delimited by some delimiter) on the streaming source.

      - **JSONMappingParameters** *(dict) --*

        Provides additional mapping information when JSON is the record format on the streaming
        source.

        - **RecordRowPath** *(string) --*

          The path to the top-level parent that contains the records.

      - **CSVMappingParameters** *(dict) --*

        Provides additional mapping information when the record format uses delimiters (for
        example, CSV).

        - **RecordRowDelimiter** *(string) --*

          The row delimiter. For example, in a CSV format, *'\\n'* is the typical row delimiter.

        - **RecordColumnDelimiter** *(string) --*

          The column delimiter. For example, in a CSV format, a comma (",") is the typical
          column delimiter.
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

    The schema inferred from the streaming source. It identifies the format of the data in the
    streaming source and how each data element maps to corresponding columns in the
    in-application stream that you can create.

    - **RecordFormat** *(dict) --*

      Specifies the format of the records on the streaming source.

      - **RecordFormatType** *(string) --*

        The type of record format.

      - **MappingParameters** *(dict) --*

        When you configure application input at the time of creating or updating an application,
        provides additional mapping information specific to the record format (such as JSON, CSV,
        or record fields delimited by some delimiter) on the streaming source.

        - **JSONMappingParameters** *(dict) --*

          Provides additional mapping information when JSON is the record format on the streaming
          source.

          - **RecordRowPath** *(string) --*

            The path to the top-level parent that contains the records.

        - **CSVMappingParameters** *(dict) --*

          Provides additional mapping information when the record format uses delimiters (for
          example, CSV).

          - **RecordRowDelimiter** *(string) --*

            The row delimiter. For example, in a CSV format, *'\\n'* is the typical row delimiter.

          - **RecordColumnDelimiter** *(string) --*

            The column delimiter. For example, in a CSV format, a comma (",") is the typical
            column delimiter.

    - **RecordEncoding** *(string) --*

      Specifies the encoding of the records in the streaming source. For example, UTF-8.

    - **RecordColumns** *(list) --*

      A list of ``RecordColumn`` objects.

      - *(dict) --*

        For an SQL-based Amazon Kinesis Data Analytics application, describes the mapping of each
        data element in the streaming source to the corresponding column in the in-application
        stream.

        Also used to describe the format of the reference data source.

        - **Name** *(string) --*

          The name of the column that is created in the in-application input stream or reference
          table.

        - **Mapping** *(string) --*

          A reference to the data element in the streaming input or the reference data source.

        - **SqlType** *(string) --*

          The type of column created in the in-application input stream or reference table.
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

      The schema inferred from the streaming source. It identifies the format of the data in the
      streaming source and how each data element maps to corresponding columns in the
      in-application stream that you can create.

      - **RecordFormat** *(dict) --*

        Specifies the format of the records on the streaming source.

        - **RecordFormatType** *(string) --*

          The type of record format.

        - **MappingParameters** *(dict) --*

          When you configure application input at the time of creating or updating an application,
          provides additional mapping information specific to the record format (such as JSON, CSV,
          or record fields delimited by some delimiter) on the streaming source.

          - **JSONMappingParameters** *(dict) --*

            Provides additional mapping information when JSON is the record format on the streaming
            source.

            - **RecordRowPath** *(string) --*

              The path to the top-level parent that contains the records.

          - **CSVMappingParameters** *(dict) --*

            Provides additional mapping information when the record format uses delimiters (for
            example, CSV).

            - **RecordRowDelimiter** *(string) --*

              The row delimiter. For example, in a CSV format, *'\\n'* is the typical row delimiter.

            - **RecordColumnDelimiter** *(string) --*

              The column delimiter. For example, in a CSV format, a comma (",") is the typical
              column delimiter.

      - **RecordEncoding** *(string) --*

        Specifies the encoding of the records in the streaming source. For example, UTF-8.

      - **RecordColumns** *(list) --*

        A list of ``RecordColumn`` objects.

        - *(dict) --*

          For an SQL-based Amazon Kinesis Data Analytics application, describes the mapping of each
          data element in the streaming source to the corresponding column in the in-application
          stream.

          Also used to describe the format of the reference data source.

          - **Name** *(string) --*

            The name of the column that is created in the in-application input stream or reference
            table.

          - **Mapping** *(string) --*

            A reference to the data element in the streaming input or the reference data source.

          - **SqlType** *(string) --*

            The type of column created in the in-application input stream or reference table.

    - **ParsedInputRecords** *(list) --*

      An array of elements, where each element corresponds to a row in a stream record (a stream
      record can have more than one row).

      - *(list) --*

        - *(string) --*

    - **ProcessedInputRecords** *(list) --*

      The stream data that was modified by the processor specified in the
      ``InputProcessingConfiguration`` parameter.

      - *(string) --*

    - **RawInputRecords** *(list) --*

      The raw stream data that was sampled to infer the schema.

      - *(string) --*
    """


_ClientDiscoverInputSchemaS3ConfigurationTypeDef = TypedDict(
    "_ClientDiscoverInputSchemaS3ConfigurationTypeDef",
    {"BucketARN": str, "FileKey": str},
)


class ClientDiscoverInputSchemaS3ConfigurationTypeDef(
    _ClientDiscoverInputSchemaS3ConfigurationTypeDef
):
    """
    Type definition for `ClientDiscoverInputSchema` `S3Configuration`

    Specify this parameter to discover a schema from data in an Amazon S3 object.

    - **BucketARN** *(string) --* **[REQUIRED]**

      The ARN of the S3 bucket that contains the data.

    - **FileKey** *(string) --* **[REQUIRED]**

      The name of the object that contains the data.
    """


_ClientListApplicationSnapshotsResponseSnapshotSummariesTypeDef = TypedDict(
    "_ClientListApplicationSnapshotsResponseSnapshotSummariesTypeDef",
    {
        "SnapshotName": str,
        "SnapshotStatus": str,
        "ApplicationVersionId": int,
        "SnapshotCreationTimestamp": datetime,
    },
    total=False,
)


class ClientListApplicationSnapshotsResponseSnapshotSummariesTypeDef(
    _ClientListApplicationSnapshotsResponseSnapshotSummariesTypeDef
):
    """
    Type definition for `ClientListApplicationSnapshotsResponse` `SnapshotSummaries`

    Provides details about a snapshot of application state.

    - **SnapshotName** *(string) --*

      The identifier for the application snapshot.

    - **SnapshotStatus** *(string) --*

      The status of the application snapshot.

    - **ApplicationVersionId** *(integer) --*

      The current application version ID when the snapshot was created.

    - **SnapshotCreationTimestamp** *(datetime) --*

      The timestamp of the application snapshot.
    """


_ClientListApplicationSnapshotsResponseTypeDef = TypedDict(
    "_ClientListApplicationSnapshotsResponseTypeDef",
    {
        "SnapshotSummaries": List[
            ClientListApplicationSnapshotsResponseSnapshotSummariesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListApplicationSnapshotsResponseTypeDef(
    _ClientListApplicationSnapshotsResponseTypeDef
):
    """
    Type definition for `ClientListApplicationSnapshots` `Response`

    - **SnapshotSummaries** *(list) --*

      A collection of objects containing information about the application snapshots.

      - *(dict) --*

        Provides details about a snapshot of application state.

        - **SnapshotName** *(string) --*

          The identifier for the application snapshot.

        - **SnapshotStatus** *(string) --*

          The status of the application snapshot.

        - **ApplicationVersionId** *(integer) --*

          The current application version ID when the snapshot was created.

        - **SnapshotCreationTimestamp** *(datetime) --*

          The timestamp of the application snapshot.

    - **NextToken** *(string) --*

      The token for the next set of results, or ``null`` if there are no additional results.
    """


_ClientListApplicationsResponseApplicationSummariesTypeDef = TypedDict(
    "_ClientListApplicationsResponseApplicationSummariesTypeDef",
    {
        "ApplicationName": str,
        "ApplicationARN": str,
        "ApplicationStatus": str,
        "ApplicationVersionId": int,
        "RuntimeEnvironment": str,
    },
    total=False,
)


class ClientListApplicationsResponseApplicationSummariesTypeDef(
    _ClientListApplicationsResponseApplicationSummariesTypeDef
):
    """
    Type definition for `ClientListApplicationsResponse` `ApplicationSummaries`

    Provides application summary information, including the application Amazon Resource Name
    (ARN), name, and status.

    - **ApplicationName** *(string) --*

      The name of the application.

    - **ApplicationARN** *(string) --*

      The ARN of the application.

    - **ApplicationStatus** *(string) --*

      The status of the application.

    - **ApplicationVersionId** *(integer) --*

      Provides the current application version.

    - **RuntimeEnvironment** *(string) --*

      The runtime environment for the application (``SQL-1.0`` or ``FLINK-1_6`` ).
    """


_ClientListApplicationsResponseTypeDef = TypedDict(
    "_ClientListApplicationsResponseTypeDef",
    {
        "ApplicationSummaries": List[
            ClientListApplicationsResponseApplicationSummariesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListApplicationsResponseTypeDef(_ClientListApplicationsResponseTypeDef):
    """
    Type definition for `ClientListApplications` `Response`

    - **ApplicationSummaries** *(list) --*

      A list of ``ApplicationSummary`` objects.

      - *(dict) --*

        Provides application summary information, including the application Amazon Resource Name
        (ARN), name, and status.

        - **ApplicationName** *(string) --*

          The name of the application.

        - **ApplicationARN** *(string) --*

          The ARN of the application.

        - **ApplicationStatus** *(string) --*

          The status of the application.

        - **ApplicationVersionId** *(integer) --*

          Provides the current application version.

        - **RuntimeEnvironment** *(string) --*

          The runtime environment for the application (``SQL-1.0`` or ``FLINK-1_6`` ).

    - **NextToken** *(string) --*

      The pagination token for the next set of results, or ``null`` if there are no additional
      results. Pass this token into a subsequent command to retrieve the next set of items For more
      information about pagination, see `Using the AWS Command Line Interface's Pagination Options
      <https://docs.aws.amazon.com/cli/latest/userguide/pagination.html>`__ .
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
    `Using Cost Allocation Tags
    <https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html>`__ in
    the *AWS Billing and Cost Management Guide* .

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
        `Using Cost Allocation Tags
        <https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html>`__ in
        the *AWS Billing and Cost Management Guide* .

        - **Key** *(string) --*

          The key of the key-value tag.

        - **Value** *(string) --*

          The value of the key-value tag. The value is optional.
    """


_RequiredClientStartApplicationRunConfigurationApplicationRestoreConfigurationTypeDef = TypedDict(
    "_RequiredClientStartApplicationRunConfigurationApplicationRestoreConfigurationTypeDef",
    {"ApplicationRestoreType": str},
)
_OptionalClientStartApplicationRunConfigurationApplicationRestoreConfigurationTypeDef = TypedDict(
    "_OptionalClientStartApplicationRunConfigurationApplicationRestoreConfigurationTypeDef",
    {"SnapshotName": str},
    total=False,
)


class ClientStartApplicationRunConfigurationApplicationRestoreConfigurationTypeDef(
    _RequiredClientStartApplicationRunConfigurationApplicationRestoreConfigurationTypeDef,
    _OptionalClientStartApplicationRunConfigurationApplicationRestoreConfigurationTypeDef,
):
    """
    Type definition for `ClientStartApplicationRunConfiguration` `ApplicationRestoreConfiguration`

    Describes the restore behavior of a restarting application.

    - **ApplicationRestoreType** *(string) --* **[REQUIRED]**

      Specifies how the application should be restored.

    - **SnapshotName** *(string) --*

      The identifier of an existing snapshot of application state to use to restart an application.
      The application uses this value if ``RESTORE_FROM_CUSTOM_SNAPSHOT`` is specified for the
      ``ApplicationRestoreType`` .
    """


_ClientStartApplicationRunConfigurationSqlRunConfigurationsInputStartingPositionConfigurationTypeDef = TypedDict(
    "_ClientStartApplicationRunConfigurationSqlRunConfigurationsInputStartingPositionConfigurationTypeDef",
    {"InputStartingPosition": str},
    total=False,
)


class ClientStartApplicationRunConfigurationSqlRunConfigurationsInputStartingPositionConfigurationTypeDef(
    _ClientStartApplicationRunConfigurationSqlRunConfigurationsInputStartingPositionConfigurationTypeDef
):
    """
    Type definition for `ClientStartApplicationRunConfigurationSqlRunConfigurations` `InputStartingPositionConfiguration`

    The point at which you want the application to start processing records from the streaming
    source.

    - **InputStartingPosition** *(string) --*

      The starting position on the stream.

      * ``NOW`` - Start reading just after the most recent record in the stream, and start at
      the request timestamp that the customer issued.

      * ``TRIM_HORIZON`` - Start reading at the last untrimmed record in the stream, which is
      the oldest record available in the stream. This option is not available for an Amazon
      Kinesis Data Firehose delivery stream.

      * ``LAST_STOPPED_POINT`` - Resume reading from where the application last stopped reading.
    """


_ClientStartApplicationRunConfigurationSqlRunConfigurationsTypeDef = TypedDict(
    "_ClientStartApplicationRunConfigurationSqlRunConfigurationsTypeDef",
    {
        "InputId": str,
        "InputStartingPositionConfiguration": ClientStartApplicationRunConfigurationSqlRunConfigurationsInputStartingPositionConfigurationTypeDef,
    },
)


class ClientStartApplicationRunConfigurationSqlRunConfigurationsTypeDef(
    _ClientStartApplicationRunConfigurationSqlRunConfigurationsTypeDef
):
    """
    Type definition for `ClientStartApplicationRunConfiguration` `SqlRunConfigurations`

    Describes the starting parameters for an SQL-based Kinesis Data Analytics application.

    - **InputId** *(string) --* **[REQUIRED]**

      The input source ID. You can get this ID by calling the  DescribeApplication operation.

    - **InputStartingPositionConfiguration** *(dict) --* **[REQUIRED]**

      The point at which you want the application to start processing records from the streaming
      source.

      - **InputStartingPosition** *(string) --*

        The starting position on the stream.

        * ``NOW`` - Start reading just after the most recent record in the stream, and start at
        the request timestamp that the customer issued.

        * ``TRIM_HORIZON`` - Start reading at the last untrimmed record in the stream, which is
        the oldest record available in the stream. This option is not available for an Amazon
        Kinesis Data Firehose delivery stream.

        * ``LAST_STOPPED_POINT`` - Resume reading from where the application last stopped reading.
    """


_ClientStartApplicationRunConfigurationTypeDef = TypedDict(
    "_ClientStartApplicationRunConfigurationTypeDef",
    {
        "SqlRunConfigurations": List[
            ClientStartApplicationRunConfigurationSqlRunConfigurationsTypeDef
        ],
        "ApplicationRestoreConfiguration": ClientStartApplicationRunConfigurationApplicationRestoreConfigurationTypeDef,
    },
    total=False,
)


class ClientStartApplicationRunConfigurationTypeDef(
    _ClientStartApplicationRunConfigurationTypeDef
):
    """
    Type definition for `ClientStartApplication` `RunConfiguration`

    Identifies the run configuration (start parameters) of a Kinesis Data Analytics application.

    - **SqlRunConfigurations** *(list) --*

      Describes the starting parameters for an SQL-based Kinesis Data Analytics application.

      - *(dict) --*

        Describes the starting parameters for an SQL-based Kinesis Data Analytics application.

        - **InputId** *(string) --* **[REQUIRED]**

          The input source ID. You can get this ID by calling the  DescribeApplication operation.

        - **InputStartingPositionConfiguration** *(dict) --* **[REQUIRED]**

          The point at which you want the application to start processing records from the streaming
          source.

          - **InputStartingPosition** *(string) --*

            The starting position on the stream.

            * ``NOW`` - Start reading just after the most recent record in the stream, and start at
            the request timestamp that the customer issued.

            * ``TRIM_HORIZON`` - Start reading at the last untrimmed record in the stream, which is
            the oldest record available in the stream. This option is not available for an Amazon
            Kinesis Data Firehose delivery stream.

            * ``LAST_STOPPED_POINT`` - Resume reading from where the application last stopped reading.

    - **ApplicationRestoreConfiguration** *(dict) --*

      Describes the restore behavior of a restarting application.

      - **ApplicationRestoreType** *(string) --* **[REQUIRED]**

        Specifies how the application should be restored.

      - **SnapshotName** *(string) --*

        The identifier of an existing snapshot of application state to use to restart an application.
        The application uses this value if ``RESTORE_FROM_CUSTOM_SNAPSHOT`` is specified for the
        ``ApplicationRestoreType`` .
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
    Cost Allocation Tags
    <https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html>`__ in the
    *AWS Billing and Cost Management Guide* .

    - **Key** *(string) --* **[REQUIRED]**

      The key of the key-value tag.

    - **Value** *(string) --*

      The value of the key-value tag. The value is optional.
    """


_ClientUpdateApplicationApplicationConfigurationUpdateApplicationCodeConfigurationUpdateCodeContentUpdateS3ContentLocationUpdateTypeDef = TypedDict(
    "_ClientUpdateApplicationApplicationConfigurationUpdateApplicationCodeConfigurationUpdateCodeContentUpdateS3ContentLocationUpdateTypeDef",
    {"BucketARNUpdate": str, "FileKeyUpdate": str, "ObjectVersionUpdate": str},
    total=False,
)


class ClientUpdateApplicationApplicationConfigurationUpdateApplicationCodeConfigurationUpdateCodeContentUpdateS3ContentLocationUpdateTypeDef(
    _ClientUpdateApplicationApplicationConfigurationUpdateApplicationCodeConfigurationUpdateCodeContentUpdateS3ContentLocationUpdateTypeDef
):
    """
    Type definition for `ClientUpdateApplicationApplicationConfigurationUpdateApplicationCodeConfigurationUpdateCodeContentUpdate` `S3ContentLocationUpdate`

    Describes an update to the location of code for an application.

    - **BucketARNUpdate** *(string) --*

      The new Amazon Resource Name (ARN) for the S3 bucket containing the application code.

    - **FileKeyUpdate** *(string) --*

      The new file key for the object containing the application code.

    - **ObjectVersionUpdate** *(string) --*

      The new version of the object containing the application code.
    """


_ClientUpdateApplicationApplicationConfigurationUpdateApplicationCodeConfigurationUpdateCodeContentUpdateTypeDef = TypedDict(
    "_ClientUpdateApplicationApplicationConfigurationUpdateApplicationCodeConfigurationUpdateCodeContentUpdateTypeDef",
    {
        "TextContentUpdate": str,
        "ZipFileContentUpdate": bytes,
        "S3ContentLocationUpdate": ClientUpdateApplicationApplicationConfigurationUpdateApplicationCodeConfigurationUpdateCodeContentUpdateS3ContentLocationUpdateTypeDef,
    },
    total=False,
)


class ClientUpdateApplicationApplicationConfigurationUpdateApplicationCodeConfigurationUpdateCodeContentUpdateTypeDef(
    _ClientUpdateApplicationApplicationConfigurationUpdateApplicationCodeConfigurationUpdateCodeContentUpdateTypeDef
):
    """
    Type definition for `ClientUpdateApplicationApplicationConfigurationUpdateApplicationCodeConfigurationUpdate` `CodeContentUpdate`

    Describes updates to the code content of an application.

    - **TextContentUpdate** *(string) --*

      Describes an update to the text code for an application.

    - **ZipFileContentUpdate** *(bytes) --*

      Describes an update to the zipped code for an application.

    - **S3ContentLocationUpdate** *(dict) --*

      Describes an update to the location of code for an application.

      - **BucketARNUpdate** *(string) --*

        The new Amazon Resource Name (ARN) for the S3 bucket containing the application code.

      - **FileKeyUpdate** *(string) --*

        The new file key for the object containing the application code.

      - **ObjectVersionUpdate** *(string) --*

        The new version of the object containing the application code.
    """


_ClientUpdateApplicationApplicationConfigurationUpdateApplicationCodeConfigurationUpdateTypeDef = TypedDict(
    "_ClientUpdateApplicationApplicationConfigurationUpdateApplicationCodeConfigurationUpdateTypeDef",
    {
        "CodeContentTypeUpdate": str,
        "CodeContentUpdate": ClientUpdateApplicationApplicationConfigurationUpdateApplicationCodeConfigurationUpdateCodeContentUpdateTypeDef,
    },
    total=False,
)


class ClientUpdateApplicationApplicationConfigurationUpdateApplicationCodeConfigurationUpdateTypeDef(
    _ClientUpdateApplicationApplicationConfigurationUpdateApplicationCodeConfigurationUpdateTypeDef
):
    """
    Type definition for `ClientUpdateApplicationApplicationConfigurationUpdate` `ApplicationCodeConfigurationUpdate`

    Describes updates to a Java-based Kinesis Data Analytics application's code configuration.

    - **CodeContentTypeUpdate** *(string) --*

      Describes updates to the code content type.

    - **CodeContentUpdate** *(dict) --*

      Describes updates to the code content of an application.

      - **TextContentUpdate** *(string) --*

        Describes an update to the text code for an application.

      - **ZipFileContentUpdate** *(bytes) --*

        Describes an update to the zipped code for an application.

      - **S3ContentLocationUpdate** *(dict) --*

        Describes an update to the location of code for an application.

        - **BucketARNUpdate** *(string) --*

          The new Amazon Resource Name (ARN) for the S3 bucket containing the application code.

        - **FileKeyUpdate** *(string) --*

          The new file key for the object containing the application code.

        - **ObjectVersionUpdate** *(string) --*

          The new version of the object containing the application code.
    """


_ClientUpdateApplicationApplicationConfigurationUpdateApplicationSnapshotConfigurationUpdateTypeDef = TypedDict(
    "_ClientUpdateApplicationApplicationConfigurationUpdateApplicationSnapshotConfigurationUpdateTypeDef",
    {"SnapshotsEnabledUpdate": bool},
)


class ClientUpdateApplicationApplicationConfigurationUpdateApplicationSnapshotConfigurationUpdateTypeDef(
    _ClientUpdateApplicationApplicationConfigurationUpdateApplicationSnapshotConfigurationUpdateTypeDef
):
    """
    Type definition for `ClientUpdateApplicationApplicationConfigurationUpdate` `ApplicationSnapshotConfigurationUpdate`

    Describes whether snapshots are enabled for a Java-based Kinesis Data Analytics application.

    - **SnapshotsEnabledUpdate** *(boolean) --* **[REQUIRED]**

      Describes updates to whether snapshots are enabled for a Java-based Kinesis Data Analytics
      application.
    """


_ClientUpdateApplicationApplicationConfigurationUpdateEnvironmentPropertyUpdatesPropertyGroupsTypeDef = TypedDict(
    "_ClientUpdateApplicationApplicationConfigurationUpdateEnvironmentPropertyUpdatesPropertyGroupsTypeDef",
    {"PropertyGroupId": str, "PropertyMap": Dict[str, str]},
)


class ClientUpdateApplicationApplicationConfigurationUpdateEnvironmentPropertyUpdatesPropertyGroupsTypeDef(
    _ClientUpdateApplicationApplicationConfigurationUpdateEnvironmentPropertyUpdatesPropertyGroupsTypeDef
):
    """
    Type definition for `ClientUpdateApplicationApplicationConfigurationUpdateEnvironmentPropertyUpdates` `PropertyGroups`

    Property key-value pairs passed into a Java-based Kinesis Data Analytics application.

    - **PropertyGroupId** *(string) --* **[REQUIRED]**

      Describes the key of an application execution property key-value pair.

    - **PropertyMap** *(dict) --* **[REQUIRED]**

      Describes the value of an application execution property key-value pair.

      - *(string) --*

        - *(string) --*
    """


_ClientUpdateApplicationApplicationConfigurationUpdateEnvironmentPropertyUpdatesTypeDef = TypedDict(
    "_ClientUpdateApplicationApplicationConfigurationUpdateEnvironmentPropertyUpdatesTypeDef",
    {
        "PropertyGroups": List[
            ClientUpdateApplicationApplicationConfigurationUpdateEnvironmentPropertyUpdatesPropertyGroupsTypeDef
        ]
    },
)


class ClientUpdateApplicationApplicationConfigurationUpdateEnvironmentPropertyUpdatesTypeDef(
    _ClientUpdateApplicationApplicationConfigurationUpdateEnvironmentPropertyUpdatesTypeDef
):
    """
    Type definition for `ClientUpdateApplicationApplicationConfigurationUpdate` `EnvironmentPropertyUpdates`

    Describes updates to the environment properties for a Java-based Kinesis Data Analytics
    application.

    - **PropertyGroups** *(list) --* **[REQUIRED]**

      Describes updates to the execution property groups.

      - *(dict) --*

        Property key-value pairs passed into a Java-based Kinesis Data Analytics application.

        - **PropertyGroupId** *(string) --* **[REQUIRED]**

          Describes the key of an application execution property key-value pair.

        - **PropertyMap** *(dict) --* **[REQUIRED]**

          Describes the value of an application execution property key-value pair.

          - *(string) --*

            - *(string) --*
    """


_ClientUpdateApplicationApplicationConfigurationUpdateFlinkApplicationConfigurationUpdateCheckpointConfigurationUpdateTypeDef = TypedDict(
    "_ClientUpdateApplicationApplicationConfigurationUpdateFlinkApplicationConfigurationUpdateCheckpointConfigurationUpdateTypeDef",
    {
        "ConfigurationTypeUpdate": str,
        "CheckpointingEnabledUpdate": bool,
        "CheckpointIntervalUpdate": int,
        "MinPauseBetweenCheckpointsUpdate": int,
    },
    total=False,
)


class ClientUpdateApplicationApplicationConfigurationUpdateFlinkApplicationConfigurationUpdateCheckpointConfigurationUpdateTypeDef(
    _ClientUpdateApplicationApplicationConfigurationUpdateFlinkApplicationConfigurationUpdateCheckpointConfigurationUpdateTypeDef
):
    """
    Type definition for `ClientUpdateApplicationApplicationConfigurationUpdateFlinkApplicationConfigurationUpdate` `CheckpointConfigurationUpdate`

    Describes updates to an application's checkpointing configuration. Checkpointing is the
    process of persisting application state for fault tolerance.

    - **ConfigurationTypeUpdate** *(string) --*

      Describes updates to whether the application uses the default checkpointing behavior of
      Kinesis Data Analytics.

    - **CheckpointingEnabledUpdate** *(boolean) --*

      Describes updates to whether checkpointing is enabled for an application.

    - **CheckpointIntervalUpdate** *(integer) --*

      Describes updates to the interval in milliseconds between checkpoint operations.

    - **MinPauseBetweenCheckpointsUpdate** *(integer) --*

      Describes updates to the minimum time in milliseconds after a checkpoint operation
      completes that a new checkpoint operation can start.
    """


_ClientUpdateApplicationApplicationConfigurationUpdateFlinkApplicationConfigurationUpdateMonitoringConfigurationUpdateTypeDef = TypedDict(
    "_ClientUpdateApplicationApplicationConfigurationUpdateFlinkApplicationConfigurationUpdateMonitoringConfigurationUpdateTypeDef",
    {"ConfigurationTypeUpdate": str, "MetricsLevelUpdate": str, "LogLevelUpdate": str},
    total=False,
)


class ClientUpdateApplicationApplicationConfigurationUpdateFlinkApplicationConfigurationUpdateMonitoringConfigurationUpdateTypeDef(
    _ClientUpdateApplicationApplicationConfigurationUpdateFlinkApplicationConfigurationUpdateMonitoringConfigurationUpdateTypeDef
):
    """
    Type definition for `ClientUpdateApplicationApplicationConfigurationUpdateFlinkApplicationConfigurationUpdate` `MonitoringConfigurationUpdate`

    Describes updates to the configuration parameters for Amazon CloudWatch logging for an
    application.

    - **ConfigurationTypeUpdate** *(string) --*

      Describes updates to whether to use the default CloudWatch logging configuration for an
      application.

    - **MetricsLevelUpdate** *(string) --*

      Describes updates to the granularity of the CloudWatch Logs for an application.

    - **LogLevelUpdate** *(string) --*

      Describes updates to the verbosity of the CloudWatch Logs for an application.
    """


_ClientUpdateApplicationApplicationConfigurationUpdateFlinkApplicationConfigurationUpdateParallelismConfigurationUpdateTypeDef = TypedDict(
    "_ClientUpdateApplicationApplicationConfigurationUpdateFlinkApplicationConfigurationUpdateParallelismConfigurationUpdateTypeDef",
    {
        "ConfigurationTypeUpdate": str,
        "ParallelismUpdate": int,
        "ParallelismPerKPUUpdate": int,
        "AutoScalingEnabledUpdate": bool,
    },
    total=False,
)


class ClientUpdateApplicationApplicationConfigurationUpdateFlinkApplicationConfigurationUpdateParallelismConfigurationUpdateTypeDef(
    _ClientUpdateApplicationApplicationConfigurationUpdateFlinkApplicationConfigurationUpdateParallelismConfigurationUpdateTypeDef
):
    """
    Type definition for `ClientUpdateApplicationApplicationConfigurationUpdateFlinkApplicationConfigurationUpdate` `ParallelismConfigurationUpdate`

    Describes updates to the parameters for how an application executes multiple tasks
    simultaneously.

    - **ConfigurationTypeUpdate** *(string) --*

      Describes updates to whether the application uses the default parallelism for the Kinesis
      Data Analytics service, or if a custom parallelism is used.

    - **ParallelismUpdate** *(integer) --*

      Describes updates to the initial number of parallel tasks an application can perform.

    - **ParallelismPerKPUUpdate** *(integer) --*

      Describes updates to the number of parallel tasks an application can perform per Kinesis
      Processing Unit (KPU) used by the application.

    - **AutoScalingEnabledUpdate** *(boolean) --*

      Describes updates to whether the Kinesis Data Analytics service can increase the
      parallelism of the application in response to increased throughput.
    """


_ClientUpdateApplicationApplicationConfigurationUpdateFlinkApplicationConfigurationUpdateTypeDef = TypedDict(
    "_ClientUpdateApplicationApplicationConfigurationUpdateFlinkApplicationConfigurationUpdateTypeDef",
    {
        "CheckpointConfigurationUpdate": ClientUpdateApplicationApplicationConfigurationUpdateFlinkApplicationConfigurationUpdateCheckpointConfigurationUpdateTypeDef,
        "MonitoringConfigurationUpdate": ClientUpdateApplicationApplicationConfigurationUpdateFlinkApplicationConfigurationUpdateMonitoringConfigurationUpdateTypeDef,
        "ParallelismConfigurationUpdate": ClientUpdateApplicationApplicationConfigurationUpdateFlinkApplicationConfigurationUpdateParallelismConfigurationUpdateTypeDef,
    },
    total=False,
)


class ClientUpdateApplicationApplicationConfigurationUpdateFlinkApplicationConfigurationUpdateTypeDef(
    _ClientUpdateApplicationApplicationConfigurationUpdateFlinkApplicationConfigurationUpdateTypeDef
):
    """
    Type definition for `ClientUpdateApplicationApplicationConfigurationUpdate` `FlinkApplicationConfigurationUpdate`

    Describes updates to a Java-based Kinesis Data Analytics application's configuration.

    - **CheckpointConfigurationUpdate** *(dict) --*

      Describes updates to an application's checkpointing configuration. Checkpointing is the
      process of persisting application state for fault tolerance.

      - **ConfigurationTypeUpdate** *(string) --*

        Describes updates to whether the application uses the default checkpointing behavior of
        Kinesis Data Analytics.

      - **CheckpointingEnabledUpdate** *(boolean) --*

        Describes updates to whether checkpointing is enabled for an application.

      - **CheckpointIntervalUpdate** *(integer) --*

        Describes updates to the interval in milliseconds between checkpoint operations.

      - **MinPauseBetweenCheckpointsUpdate** *(integer) --*

        Describes updates to the minimum time in milliseconds after a checkpoint operation
        completes that a new checkpoint operation can start.

    - **MonitoringConfigurationUpdate** *(dict) --*

      Describes updates to the configuration parameters for Amazon CloudWatch logging for an
      application.

      - **ConfigurationTypeUpdate** *(string) --*

        Describes updates to whether to use the default CloudWatch logging configuration for an
        application.

      - **MetricsLevelUpdate** *(string) --*

        Describes updates to the granularity of the CloudWatch Logs for an application.

      - **LogLevelUpdate** *(string) --*

        Describes updates to the verbosity of the CloudWatch Logs for an application.

    - **ParallelismConfigurationUpdate** *(dict) --*

      Describes updates to the parameters for how an application executes multiple tasks
      simultaneously.

      - **ConfigurationTypeUpdate** *(string) --*

        Describes updates to whether the application uses the default parallelism for the Kinesis
        Data Analytics service, or if a custom parallelism is used.

      - **ParallelismUpdate** *(integer) --*

        Describes updates to the initial number of parallel tasks an application can perform.

      - **ParallelismPerKPUUpdate** *(integer) --*

        Describes updates to the number of parallel tasks an application can perform per Kinesis
        Processing Unit (KPU) used by the application.

      - **AutoScalingEnabledUpdate** *(boolean) --*

        Describes updates to whether the Kinesis Data Analytics service can increase the
        parallelism of the application in response to increased throughput.
    """


_ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdatesInputParallelismUpdateTypeDef = TypedDict(
    "_ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdatesInputParallelismUpdateTypeDef",
    {"CountUpdate": int},
)


class ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdatesInputParallelismUpdateTypeDef(
    _ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdatesInputParallelismUpdateTypeDef
):
    """
    Type definition for `ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdates` `InputParallelismUpdate`

    Describes the parallelism updates (the number of in-application streams Kinesis Data
    Analytics creates for the specific streaming source).

    - **CountUpdate** *(integer) --* **[REQUIRED]**

      The number of in-application streams to create for the specified streaming source.
    """


_ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdatesInputProcessingConfigurationUpdateInputLambdaProcessorUpdateTypeDef = TypedDict(
    "_ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdatesInputProcessingConfigurationUpdateInputLambdaProcessorUpdateTypeDef",
    {"ResourceARNUpdate": str},
)


class ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdatesInputProcessingConfigurationUpdateInputLambdaProcessorUpdateTypeDef(
    _ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdatesInputProcessingConfigurationUpdateInputLambdaProcessorUpdateTypeDef
):
    """
    Type definition for `ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdatesInputProcessingConfigurationUpdate` `InputLambdaProcessorUpdate`

    Provides update information for an  InputLambdaProcessor .

    - **ResourceARNUpdate** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the new AWS Lambda function that is used to
      preprocess the records in the stream.

      .. note::

        To specify an earlier version of the Lambda function than the latest, include the
        Lambda function version in the Lambda function ARN. For more information about
        Lambda ARNs, see `Example ARNs\\: AWS Lambda
        </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__
    """


_ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdatesInputProcessingConfigurationUpdateTypeDef = TypedDict(
    "_ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdatesInputProcessingConfigurationUpdateTypeDef",
    {
        "InputLambdaProcessorUpdate": ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdatesInputProcessingConfigurationUpdateInputLambdaProcessorUpdateTypeDef
    },
)


class ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdatesInputProcessingConfigurationUpdateTypeDef(
    _ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdatesInputProcessingConfigurationUpdateTypeDef
):
    """
    Type definition for `ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdates` `InputProcessingConfigurationUpdate`

    Describes updates to an  InputProcessingConfiguration .

    - **InputLambdaProcessorUpdate** *(dict) --* **[REQUIRED]**

      Provides update information for an  InputLambdaProcessor .

      - **ResourceARNUpdate** *(string) --* **[REQUIRED]**

        The Amazon Resource Name (ARN) of the new AWS Lambda function that is used to
        preprocess the records in the stream.

        .. note::

          To specify an earlier version of the Lambda function than the latest, include the
          Lambda function version in the Lambda function ARN. For more information about
          Lambda ARNs, see `Example ARNs\\: AWS Lambda
          </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__
    """


_RequiredClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdatesInputSchemaUpdateRecordColumnUpdatesTypeDef = TypedDict(
    "_RequiredClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdatesInputSchemaUpdateRecordColumnUpdatesTypeDef",
    {"Name": str, "SqlType": str},
)
_OptionalClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdatesInputSchemaUpdateRecordColumnUpdatesTypeDef = TypedDict(
    "_OptionalClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdatesInputSchemaUpdateRecordColumnUpdatesTypeDef",
    {"Mapping": str},
    total=False,
)


class ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdatesInputSchemaUpdateRecordColumnUpdatesTypeDef(
    _RequiredClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdatesInputSchemaUpdateRecordColumnUpdatesTypeDef,
    _OptionalClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdatesInputSchemaUpdateRecordColumnUpdatesTypeDef,
):
    """
    Type definition for `ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdatesInputSchemaUpdate` `RecordColumnUpdates`

    For an SQL-based Amazon Kinesis Data Analytics application, describes the mapping of
    each data element in the streaming source to the corresponding column in the
    in-application stream.

    Also used to describe the format of the reference data source.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the column that is created in the in-application input stream or
      reference table.

    - **Mapping** *(string) --*

      A reference to the data element in the streaming input or the reference data source.

    - **SqlType** *(string) --* **[REQUIRED]**

      The type of column created in the in-application input stream or reference table.
    """


_ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateMappingParametersCSVMappingParametersTypeDef = TypedDict(
    "_ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateMappingParametersCSVMappingParametersTypeDef",
    {"RecordRowDelimiter": str, "RecordColumnDelimiter": str},
)


class ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateMappingParametersCSVMappingParametersTypeDef(
    _ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateMappingParametersCSVMappingParametersTypeDef
):
    """
    Type definition for `ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateMappingParameters` `CSVMappingParameters`

    Provides additional mapping information when the record format uses delimiters (for
    example, CSV).

    - **RecordRowDelimiter** *(string) --* **[REQUIRED]**

      The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
      delimiter.

    - **RecordColumnDelimiter** *(string) --* **[REQUIRED]**

      The column delimiter. For example, in a CSV format, a comma (",") is the typical
      column delimiter.
    """


_ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateMappingParametersJSONMappingParametersTypeDef = TypedDict(
    "_ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateMappingParametersJSONMappingParametersTypeDef",
    {"RecordRowPath": str},
)


class ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateMappingParametersJSONMappingParametersTypeDef(
    _ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateMappingParametersJSONMappingParametersTypeDef
):
    """
    Type definition for `ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateMappingParameters` `JSONMappingParameters`

    Provides additional mapping information when JSON is the record format on the
    streaming source.

    - **RecordRowPath** *(string) --* **[REQUIRED]**

      The path to the top-level parent that contains the records.
    """


_ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateMappingParametersTypeDef = TypedDict(
    "_ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateMappingParametersTypeDef",
    {
        "JSONMappingParameters": ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateMappingParametersJSONMappingParametersTypeDef,
        "CSVMappingParameters": ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateMappingParametersCSVMappingParametersTypeDef,
    },
    total=False,
)


class ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateMappingParametersTypeDef(
    _ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateMappingParametersTypeDef
):
    """
    Type definition for `ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdate` `MappingParameters`

    When you configure application input at the time of creating or updating an
    application, provides additional mapping information specific to the record format
    (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming
    source.

    - **JSONMappingParameters** *(dict) --*

      Provides additional mapping information when JSON is the record format on the
      streaming source.

      - **RecordRowPath** *(string) --* **[REQUIRED]**

        The path to the top-level parent that contains the records.

    - **CSVMappingParameters** *(dict) --*

      Provides additional mapping information when the record format uses delimiters (for
      example, CSV).

      - **RecordRowDelimiter** *(string) --* **[REQUIRED]**

        The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
        delimiter.

      - **RecordColumnDelimiter** *(string) --* **[REQUIRED]**

        The column delimiter. For example, in a CSV format, a comma (",") is the typical
        column delimiter.
    """


_RequiredClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateTypeDef = TypedDict(
    "_RequiredClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateTypeDef",
    {"RecordFormatType": str},
)
_OptionalClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateTypeDef = TypedDict(
    "_OptionalClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateTypeDef",
    {
        "MappingParameters": ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateMappingParametersTypeDef
    },
    total=False,
)


class ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateTypeDef(
    _RequiredClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateTypeDef,
    _OptionalClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateTypeDef,
):
    """
    Type definition for `ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdatesInputSchemaUpdate` `RecordFormatUpdate`

    Specifies the format of the records on the streaming source.

    - **RecordFormatType** *(string) --* **[REQUIRED]**

      The type of record format.

    - **MappingParameters** *(dict) --*

      When you configure application input at the time of creating or updating an
      application, provides additional mapping information specific to the record format
      (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming
      source.

      - **JSONMappingParameters** *(dict) --*

        Provides additional mapping information when JSON is the record format on the
        streaming source.

        - **RecordRowPath** *(string) --* **[REQUIRED]**

          The path to the top-level parent that contains the records.

      - **CSVMappingParameters** *(dict) --*

        Provides additional mapping information when the record format uses delimiters (for
        example, CSV).

        - **RecordRowDelimiter** *(string) --* **[REQUIRED]**

          The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
          delimiter.

        - **RecordColumnDelimiter** *(string) --* **[REQUIRED]**

          The column delimiter. For example, in a CSV format, a comma (",") is the typical
          column delimiter.
    """


_ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdatesInputSchemaUpdateTypeDef = TypedDict(
    "_ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdatesInputSchemaUpdateTypeDef",
    {
        "RecordFormatUpdate": ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateTypeDef,
        "RecordEncodingUpdate": str,
        "RecordColumnUpdates": List[
            ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdatesInputSchemaUpdateRecordColumnUpdatesTypeDef
        ],
    },
    total=False,
)


class ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdatesInputSchemaUpdateTypeDef(
    _ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdatesInputSchemaUpdateTypeDef
):
    """
    Type definition for `ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdates` `InputSchemaUpdate`

    Describes the data format on the streaming source, and how record elements on the
    streaming source map to columns of the in-application stream that is created.

    - **RecordFormatUpdate** *(dict) --*

      Specifies the format of the records on the streaming source.

      - **RecordFormatType** *(string) --* **[REQUIRED]**

        The type of record format.

      - **MappingParameters** *(dict) --*

        When you configure application input at the time of creating or updating an
        application, provides additional mapping information specific to the record format
        (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming
        source.

        - **JSONMappingParameters** *(dict) --*

          Provides additional mapping information when JSON is the record format on the
          streaming source.

          - **RecordRowPath** *(string) --* **[REQUIRED]**

            The path to the top-level parent that contains the records.

        - **CSVMappingParameters** *(dict) --*

          Provides additional mapping information when the record format uses delimiters (for
          example, CSV).

          - **RecordRowDelimiter** *(string) --* **[REQUIRED]**

            The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
            delimiter.

          - **RecordColumnDelimiter** *(string) --* **[REQUIRED]**

            The column delimiter. For example, in a CSV format, a comma (",") is the typical
            column delimiter.

    - **RecordEncodingUpdate** *(string) --*

      Specifies the encoding of the records in the streaming source; for example, UTF-8.

    - **RecordColumnUpdates** *(list) --*

      A list of ``RecordColumn`` objects. Each object describes the mapping of the streaming
      source element to the corresponding column in the in-application stream.

      - *(dict) --*

        For an SQL-based Amazon Kinesis Data Analytics application, describes the mapping of
        each data element in the streaming source to the corresponding column in the
        in-application stream.

        Also used to describe the format of the reference data source.

        - **Name** *(string) --* **[REQUIRED]**

          The name of the column that is created in the in-application input stream or
          reference table.

        - **Mapping** *(string) --*

          A reference to the data element in the streaming input or the reference data source.

        - **SqlType** *(string) --* **[REQUIRED]**

          The type of column created in the in-application input stream or reference table.
    """


_ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdatesKinesisFirehoseInputUpdateTypeDef = TypedDict(
    "_ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdatesKinesisFirehoseInputUpdateTypeDef",
    {"ResourceARNUpdate": str},
)


class ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdatesKinesisFirehoseInputUpdateTypeDef(
    _ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdatesKinesisFirehoseInputUpdateTypeDef
):
    """
    Type definition for `ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdates` `KinesisFirehoseInputUpdate`

    If a Kinesis Data Firehose delivery stream is the streaming source to be updated,
    provides an updated stream ARN.

    - **ResourceARNUpdate** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the input delivery stream to read.
    """


_ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdatesKinesisStreamsInputUpdateTypeDef = TypedDict(
    "_ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdatesKinesisStreamsInputUpdateTypeDef",
    {"ResourceARNUpdate": str},
)


class ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdatesKinesisStreamsInputUpdateTypeDef(
    _ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdatesKinesisStreamsInputUpdateTypeDef
):
    """
    Type definition for `ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdates` `KinesisStreamsInputUpdate`

    If a Kinesis data stream is the streaming source to be updated, provides an updated
    stream Amazon Resource Name (ARN).

    - **ResourceARNUpdate** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the input Kinesis data stream to read.
    """


_RequiredClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdatesTypeDef = TypedDict(
    "_RequiredClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdatesTypeDef",
    {"InputId": str},
)
_OptionalClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdatesTypeDef = TypedDict(
    "_OptionalClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdatesTypeDef",
    {
        "NamePrefixUpdate": str,
        "InputProcessingConfigurationUpdate": ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdatesInputProcessingConfigurationUpdateTypeDef,
        "KinesisStreamsInputUpdate": ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdatesKinesisStreamsInputUpdateTypeDef,
        "KinesisFirehoseInputUpdate": ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdatesKinesisFirehoseInputUpdateTypeDef,
        "InputSchemaUpdate": ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdatesInputSchemaUpdateTypeDef,
        "InputParallelismUpdate": ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdatesInputParallelismUpdateTypeDef,
    },
    total=False,
)


class ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdatesTypeDef(
    _RequiredClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdatesTypeDef,
    _OptionalClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdatesTypeDef,
):
    """
    Type definition for `ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdate` `InputUpdates`

    For an SQL-based Amazon Kinesis Data Analytics application, describes updates to a specific
    input configuration (identified by the ``InputId`` of an application).

    - **InputId** *(string) --* **[REQUIRED]**

      The input ID of the application input to be updated.

    - **NamePrefixUpdate** *(string) --*

      The name prefix for in-application streams that Kinesis Data Analytics creates for the
      specific streaming source.

    - **InputProcessingConfigurationUpdate** *(dict) --*

      Describes updates to an  InputProcessingConfiguration .

      - **InputLambdaProcessorUpdate** *(dict) --* **[REQUIRED]**

        Provides update information for an  InputLambdaProcessor .

        - **ResourceARNUpdate** *(string) --* **[REQUIRED]**

          The Amazon Resource Name (ARN) of the new AWS Lambda function that is used to
          preprocess the records in the stream.

          .. note::

            To specify an earlier version of the Lambda function than the latest, include the
            Lambda function version in the Lambda function ARN. For more information about
            Lambda ARNs, see `Example ARNs\\: AWS Lambda
            </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__

    - **KinesisStreamsInputUpdate** *(dict) --*

      If a Kinesis data stream is the streaming source to be updated, provides an updated
      stream Amazon Resource Name (ARN).

      - **ResourceARNUpdate** *(string) --* **[REQUIRED]**

        The Amazon Resource Name (ARN) of the input Kinesis data stream to read.

    - **KinesisFirehoseInputUpdate** *(dict) --*

      If a Kinesis Data Firehose delivery stream is the streaming source to be updated,
      provides an updated stream ARN.

      - **ResourceARNUpdate** *(string) --* **[REQUIRED]**

        The Amazon Resource Name (ARN) of the input delivery stream to read.

    - **InputSchemaUpdate** *(dict) --*

      Describes the data format on the streaming source, and how record elements on the
      streaming source map to columns of the in-application stream that is created.

      - **RecordFormatUpdate** *(dict) --*

        Specifies the format of the records on the streaming source.

        - **RecordFormatType** *(string) --* **[REQUIRED]**

          The type of record format.

        - **MappingParameters** *(dict) --*

          When you configure application input at the time of creating or updating an
          application, provides additional mapping information specific to the record format
          (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming
          source.

          - **JSONMappingParameters** *(dict) --*

            Provides additional mapping information when JSON is the record format on the
            streaming source.

            - **RecordRowPath** *(string) --* **[REQUIRED]**

              The path to the top-level parent that contains the records.

          - **CSVMappingParameters** *(dict) --*

            Provides additional mapping information when the record format uses delimiters (for
            example, CSV).

            - **RecordRowDelimiter** *(string) --* **[REQUIRED]**

              The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
              delimiter.

            - **RecordColumnDelimiter** *(string) --* **[REQUIRED]**

              The column delimiter. For example, in a CSV format, a comma (",") is the typical
              column delimiter.

      - **RecordEncodingUpdate** *(string) --*

        Specifies the encoding of the records in the streaming source; for example, UTF-8.

      - **RecordColumnUpdates** *(list) --*

        A list of ``RecordColumn`` objects. Each object describes the mapping of the streaming
        source element to the corresponding column in the in-application stream.

        - *(dict) --*

          For an SQL-based Amazon Kinesis Data Analytics application, describes the mapping of
          each data element in the streaming source to the corresponding column in the
          in-application stream.

          Also used to describe the format of the reference data source.

          - **Name** *(string) --* **[REQUIRED]**

            The name of the column that is created in the in-application input stream or
            reference table.

          - **Mapping** *(string) --*

            A reference to the data element in the streaming input or the reference data source.

          - **SqlType** *(string) --* **[REQUIRED]**

            The type of column created in the in-application input stream or reference table.

    - **InputParallelismUpdate** *(dict) --*

      Describes the parallelism updates (the number of in-application streams Kinesis Data
      Analytics creates for the specific streaming source).

      - **CountUpdate** *(integer) --* **[REQUIRED]**

        The number of in-application streams to create for the specified streaming source.
    """


_ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateOutputUpdatesDestinationSchemaUpdateTypeDef = TypedDict(
    "_ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateOutputUpdatesDestinationSchemaUpdateTypeDef",
    {"RecordFormatType": str},
)


class ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateOutputUpdatesDestinationSchemaUpdateTypeDef(
    _ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateOutputUpdatesDestinationSchemaUpdateTypeDef
):
    """
    Type definition for `ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateOutputUpdates` `DestinationSchemaUpdate`

    Describes the data format when records are written to the destination.

    - **RecordFormatType** *(string) --* **[REQUIRED]**

      Specifies the format of the records on the output stream.
    """


_ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateOutputUpdatesKinesisFirehoseOutputUpdateTypeDef = TypedDict(
    "_ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateOutputUpdatesKinesisFirehoseOutputUpdateTypeDef",
    {"ResourceARNUpdate": str},
)


class ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateOutputUpdatesKinesisFirehoseOutputUpdateTypeDef(
    _ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateOutputUpdatesKinesisFirehoseOutputUpdateTypeDef
):
    """
    Type definition for `ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateOutputUpdates` `KinesisFirehoseOutputUpdate`

    Describes a Kinesis Data Firehose delivery stream as the destination for the output.

    - **ResourceARNUpdate** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the delivery stream to write to.
    """


_ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateOutputUpdatesKinesisStreamsOutputUpdateTypeDef = TypedDict(
    "_ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateOutputUpdatesKinesisStreamsOutputUpdateTypeDef",
    {"ResourceARNUpdate": str},
)


class ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateOutputUpdatesKinesisStreamsOutputUpdateTypeDef(
    _ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateOutputUpdatesKinesisStreamsOutputUpdateTypeDef
):
    """
    Type definition for `ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateOutputUpdates` `KinesisStreamsOutputUpdate`

    Describes a Kinesis data stream as the destination for the output.

    - **ResourceARNUpdate** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the Kinesis data stream where you want to write the
      output.
    """


_ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateOutputUpdatesLambdaOutputUpdateTypeDef = TypedDict(
    "_ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateOutputUpdatesLambdaOutputUpdateTypeDef",
    {"ResourceARNUpdate": str},
)


class ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateOutputUpdatesLambdaOutputUpdateTypeDef(
    _ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateOutputUpdatesLambdaOutputUpdateTypeDef
):
    """
    Type definition for `ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateOutputUpdates` `LambdaOutputUpdate`

    Describes an AWS Lambda function as the destination for the output.

    - **ResourceARNUpdate** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the destination AWS Lambda function.

      .. note::

        To specify an earlier version of the Lambda function than the latest, include the
        Lambda function version in the Lambda function ARN. For more information about Lambda
        ARNs, see `Example ARNs\\: AWS Lambda
        </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__
    """


_RequiredClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateOutputUpdatesTypeDef = TypedDict(
    "_RequiredClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateOutputUpdatesTypeDef",
    {"OutputId": str},
)
_OptionalClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateOutputUpdatesTypeDef = TypedDict(
    "_OptionalClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateOutputUpdatesTypeDef",
    {
        "NameUpdate": str,
        "KinesisStreamsOutputUpdate": ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateOutputUpdatesKinesisStreamsOutputUpdateTypeDef,
        "KinesisFirehoseOutputUpdate": ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateOutputUpdatesKinesisFirehoseOutputUpdateTypeDef,
        "LambdaOutputUpdate": ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateOutputUpdatesLambdaOutputUpdateTypeDef,
        "DestinationSchemaUpdate": ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateOutputUpdatesDestinationSchemaUpdateTypeDef,
    },
    total=False,
)


class ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateOutputUpdatesTypeDef(
    _RequiredClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateOutputUpdatesTypeDef,
    _OptionalClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateOutputUpdatesTypeDef,
):
    """
    Type definition for `ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdate` `OutputUpdates`

    For an SQL-based Amazon Kinesis Data Analytics application, describes updates to the output
    configuration identified by the ``OutputId`` .

    - **OutputId** *(string) --* **[REQUIRED]**

      Identifies the specific output configuration that you want to update.

    - **NameUpdate** *(string) --*

      If you want to specify a different in-application stream for this output configuration,
      use this field to specify the new in-application stream name.

    - **KinesisStreamsOutputUpdate** *(dict) --*

      Describes a Kinesis data stream as the destination for the output.

      - **ResourceARNUpdate** *(string) --* **[REQUIRED]**

        The Amazon Resource Name (ARN) of the Kinesis data stream where you want to write the
        output.

    - **KinesisFirehoseOutputUpdate** *(dict) --*

      Describes a Kinesis Data Firehose delivery stream as the destination for the output.

      - **ResourceARNUpdate** *(string) --* **[REQUIRED]**

        The Amazon Resource Name (ARN) of the delivery stream to write to.

    - **LambdaOutputUpdate** *(dict) --*

      Describes an AWS Lambda function as the destination for the output.

      - **ResourceARNUpdate** *(string) --* **[REQUIRED]**

        The Amazon Resource Name (ARN) of the destination AWS Lambda function.

        .. note::

          To specify an earlier version of the Lambda function than the latest, include the
          Lambda function version in the Lambda function ARN. For more information about Lambda
          ARNs, see `Example ARNs\\: AWS Lambda
          </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__

    - **DestinationSchemaUpdate** *(dict) --*

      Describes the data format when records are written to the destination.

      - **RecordFormatType** *(string) --* **[REQUIRED]**

        Specifies the format of the records on the output stream.
    """


_RequiredClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordColumnsTypeDef = TypedDict(
    "_RequiredClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordColumnsTypeDef",
    {"Name": str, "SqlType": str},
)
_OptionalClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordColumnsTypeDef = TypedDict(
    "_OptionalClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordColumnsTypeDef",
    {"Mapping": str},
    total=False,
)


class ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordColumnsTypeDef(
    _RequiredClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordColumnsTypeDef,
    _OptionalClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordColumnsTypeDef,
):
    """
    Type definition for `ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdate` `RecordColumns`

    For an SQL-based Amazon Kinesis Data Analytics application, describes the mapping of
    each data element in the streaming source to the corresponding column in the
    in-application stream.

    Also used to describe the format of the reference data source.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the column that is created in the in-application input stream or
      reference table.

    - **Mapping** *(string) --*

      A reference to the data element in the streaming input or the reference data source.

    - **SqlType** *(string) --* **[REQUIRED]**

      The type of column created in the in-application input stream or reference table.
    """


_ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatMappingParametersCSVMappingParametersTypeDef = TypedDict(
    "_ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatMappingParametersCSVMappingParametersTypeDef",
    {"RecordRowDelimiter": str, "RecordColumnDelimiter": str},
)


class ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatMappingParametersCSVMappingParametersTypeDef(
    _ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatMappingParametersCSVMappingParametersTypeDef
):
    """
    Type definition for `ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatMappingParameters` `CSVMappingParameters`

    Provides additional mapping information when the record format uses delimiters (for
    example, CSV).

    - **RecordRowDelimiter** *(string) --* **[REQUIRED]**

      The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
      delimiter.

    - **RecordColumnDelimiter** *(string) --* **[REQUIRED]**

      The column delimiter. For example, in a CSV format, a comma (",") is the typical
      column delimiter.
    """


_ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatMappingParametersJSONMappingParametersTypeDef = TypedDict(
    "_ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatMappingParametersJSONMappingParametersTypeDef",
    {"RecordRowPath": str},
)


class ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatMappingParametersJSONMappingParametersTypeDef(
    _ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatMappingParametersJSONMappingParametersTypeDef
):
    """
    Type definition for `ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatMappingParameters` `JSONMappingParameters`

    Provides additional mapping information when JSON is the record format on the
    streaming source.

    - **RecordRowPath** *(string) --* **[REQUIRED]**

      The path to the top-level parent that contains the records.
    """


_ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatMappingParametersTypeDef = TypedDict(
    "_ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatMappingParametersTypeDef",
    {
        "JSONMappingParameters": ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatMappingParametersJSONMappingParametersTypeDef,
        "CSVMappingParameters": ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatMappingParametersCSVMappingParametersTypeDef,
    },
    total=False,
)


class ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatMappingParametersTypeDef(
    _ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatMappingParametersTypeDef
):
    """
    Type definition for `ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormat` `MappingParameters`

    When you configure application input at the time of creating or updating an
    application, provides additional mapping information specific to the record format
    (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming
    source.

    - **JSONMappingParameters** *(dict) --*

      Provides additional mapping information when JSON is the record format on the
      streaming source.

      - **RecordRowPath** *(string) --* **[REQUIRED]**

        The path to the top-level parent that contains the records.

    - **CSVMappingParameters** *(dict) --*

      Provides additional mapping information when the record format uses delimiters (for
      example, CSV).

      - **RecordRowDelimiter** *(string) --* **[REQUIRED]**

        The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
        delimiter.

      - **RecordColumnDelimiter** *(string) --* **[REQUIRED]**

        The column delimiter. For example, in a CSV format, a comma (",") is the typical
        column delimiter.
    """


_RequiredClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatTypeDef = TypedDict(
    "_RequiredClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatTypeDef",
    {"RecordFormatType": str},
)
_OptionalClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatTypeDef = TypedDict(
    "_OptionalClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatTypeDef",
    {
        "MappingParameters": ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatMappingParametersTypeDef
    },
    total=False,
)


class ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatTypeDef(
    _RequiredClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatTypeDef,
    _OptionalClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatTypeDef,
):
    """
    Type definition for `ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdate` `RecordFormat`

    Specifies the format of the records on the streaming source.

    - **RecordFormatType** *(string) --* **[REQUIRED]**

      The type of record format.

    - **MappingParameters** *(dict) --*

      When you configure application input at the time of creating or updating an
      application, provides additional mapping information specific to the record format
      (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming
      source.

      - **JSONMappingParameters** *(dict) --*

        Provides additional mapping information when JSON is the record format on the
        streaming source.

        - **RecordRowPath** *(string) --* **[REQUIRED]**

          The path to the top-level parent that contains the records.

      - **CSVMappingParameters** *(dict) --*

        Provides additional mapping information when the record format uses delimiters (for
        example, CSV).

        - **RecordRowDelimiter** *(string) --* **[REQUIRED]**

          The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
          delimiter.

        - **RecordColumnDelimiter** *(string) --* **[REQUIRED]**

          The column delimiter. For example, in a CSV format, a comma (",") is the typical
          column delimiter.
    """


_RequiredClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateTypeDef = TypedDict(
    "_RequiredClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateTypeDef",
    {
        "RecordFormat": ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatTypeDef,
        "RecordColumns": List[
            ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordColumnsTypeDef
        ],
    },
)
_OptionalClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateTypeDef = TypedDict(
    "_OptionalClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateTypeDef",
    {"RecordEncoding": str},
    total=False,
)


class ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateTypeDef(
    _RequiredClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateTypeDef,
    _OptionalClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateTypeDef,
):
    """
    Type definition for `ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateReferenceDataSourceUpdates` `ReferenceSchemaUpdate`

    Describes the format of the data in the streaming source, and how each data element maps
    to corresponding columns created in the in-application stream.

    - **RecordFormat** *(dict) --* **[REQUIRED]**

      Specifies the format of the records on the streaming source.

      - **RecordFormatType** *(string) --* **[REQUIRED]**

        The type of record format.

      - **MappingParameters** *(dict) --*

        When you configure application input at the time of creating or updating an
        application, provides additional mapping information specific to the record format
        (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming
        source.

        - **JSONMappingParameters** *(dict) --*

          Provides additional mapping information when JSON is the record format on the
          streaming source.

          - **RecordRowPath** *(string) --* **[REQUIRED]**

            The path to the top-level parent that contains the records.

        - **CSVMappingParameters** *(dict) --*

          Provides additional mapping information when the record format uses delimiters (for
          example, CSV).

          - **RecordRowDelimiter** *(string) --* **[REQUIRED]**

            The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
            delimiter.

          - **RecordColumnDelimiter** *(string) --* **[REQUIRED]**

            The column delimiter. For example, in a CSV format, a comma (",") is the typical
            column delimiter.

    - **RecordEncoding** *(string) --*

      Specifies the encoding of the records in the streaming source. For example, UTF-8.

    - **RecordColumns** *(list) --* **[REQUIRED]**

      A list of ``RecordColumn`` objects.

      - *(dict) --*

        For an SQL-based Amazon Kinesis Data Analytics application, describes the mapping of
        each data element in the streaming source to the corresponding column in the
        in-application stream.

        Also used to describe the format of the reference data source.

        - **Name** *(string) --* **[REQUIRED]**

          The name of the column that is created in the in-application input stream or
          reference table.

        - **Mapping** *(string) --*

          A reference to the data element in the streaming input or the reference data source.

        - **SqlType** *(string) --* **[REQUIRED]**

          The type of column created in the in-application input stream or reference table.
    """


_ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateReferenceDataSourceUpdatesS3ReferenceDataSourceUpdateTypeDef = TypedDict(
    "_ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateReferenceDataSourceUpdatesS3ReferenceDataSourceUpdateTypeDef",
    {"BucketARNUpdate": str, "FileKeyUpdate": str},
    total=False,
)


class ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateReferenceDataSourceUpdatesS3ReferenceDataSourceUpdateTypeDef(
    _ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateReferenceDataSourceUpdatesS3ReferenceDataSourceUpdateTypeDef
):
    """
    Type definition for `ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateReferenceDataSourceUpdates` `S3ReferenceDataSourceUpdate`

    Describes the S3 bucket name, object key name, and IAM role that Kinesis Data Analytics
    can assume to read the Amazon S3 object on your behalf and populate the in-application
    reference table.

    - **BucketARNUpdate** *(string) --*

      The Amazon Resource Name (ARN) of the S3 bucket.

    - **FileKeyUpdate** *(string) --*

      The object key name.
    """


_RequiredClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateReferenceDataSourceUpdatesTypeDef = TypedDict(
    "_RequiredClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateReferenceDataSourceUpdatesTypeDef",
    {"ReferenceId": str},
)
_OptionalClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateReferenceDataSourceUpdatesTypeDef = TypedDict(
    "_OptionalClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateReferenceDataSourceUpdatesTypeDef",
    {
        "TableNameUpdate": str,
        "S3ReferenceDataSourceUpdate": ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateReferenceDataSourceUpdatesS3ReferenceDataSourceUpdateTypeDef,
        "ReferenceSchemaUpdate": ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateTypeDef,
    },
    total=False,
)


class ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateReferenceDataSourceUpdatesTypeDef(
    _RequiredClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateReferenceDataSourceUpdatesTypeDef,
    _OptionalClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateReferenceDataSourceUpdatesTypeDef,
):
    """
    Type definition for `ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdate` `ReferenceDataSourceUpdates`

    When you update a reference data source configuration for a SQL-based Amazon Kinesis Data
    Analytics application, this object provides all the updated values (such as the source
    bucket name and object key name), the in-application table name that is created, and
    updated mapping information that maps the data in the Amazon S3 object to the
    in-application reference table that is created.

    - **ReferenceId** *(string) --* **[REQUIRED]**

      The ID of the reference data source that is being updated. You can use the
      DescribeApplication operation to get this value.

    - **TableNameUpdate** *(string) --*

      The in-application table name that is created by this update.

    - **S3ReferenceDataSourceUpdate** *(dict) --*

      Describes the S3 bucket name, object key name, and IAM role that Kinesis Data Analytics
      can assume to read the Amazon S3 object on your behalf and populate the in-application
      reference table.

      - **BucketARNUpdate** *(string) --*

        The Amazon Resource Name (ARN) of the S3 bucket.

      - **FileKeyUpdate** *(string) --*

        The object key name.

    - **ReferenceSchemaUpdate** *(dict) --*

      Describes the format of the data in the streaming source, and how each data element maps
      to corresponding columns created in the in-application stream.

      - **RecordFormat** *(dict) --* **[REQUIRED]**

        Specifies the format of the records on the streaming source.

        - **RecordFormatType** *(string) --* **[REQUIRED]**

          The type of record format.

        - **MappingParameters** *(dict) --*

          When you configure application input at the time of creating or updating an
          application, provides additional mapping information specific to the record format
          (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming
          source.

          - **JSONMappingParameters** *(dict) --*

            Provides additional mapping information when JSON is the record format on the
            streaming source.

            - **RecordRowPath** *(string) --* **[REQUIRED]**

              The path to the top-level parent that contains the records.

          - **CSVMappingParameters** *(dict) --*

            Provides additional mapping information when the record format uses delimiters (for
            example, CSV).

            - **RecordRowDelimiter** *(string) --* **[REQUIRED]**

              The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
              delimiter.

            - **RecordColumnDelimiter** *(string) --* **[REQUIRED]**

              The column delimiter. For example, in a CSV format, a comma (",") is the typical
              column delimiter.

      - **RecordEncoding** *(string) --*

        Specifies the encoding of the records in the streaming source. For example, UTF-8.

      - **RecordColumns** *(list) --* **[REQUIRED]**

        A list of ``RecordColumn`` objects.

        - *(dict) --*

          For an SQL-based Amazon Kinesis Data Analytics application, describes the mapping of
          each data element in the streaming source to the corresponding column in the
          in-application stream.

          Also used to describe the format of the reference data source.

          - **Name** *(string) --* **[REQUIRED]**

            The name of the column that is created in the in-application input stream or
            reference table.

          - **Mapping** *(string) --*

            A reference to the data element in the streaming input or the reference data source.

          - **SqlType** *(string) --* **[REQUIRED]**

            The type of column created in the in-application input stream or reference table.
    """


_ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateTypeDef = TypedDict(
    "_ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateTypeDef",
    {
        "InputUpdates": List[
            ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateInputUpdatesTypeDef
        ],
        "OutputUpdates": List[
            ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateOutputUpdatesTypeDef
        ],
        "ReferenceDataSourceUpdates": List[
            ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateReferenceDataSourceUpdatesTypeDef
        ],
    },
    total=False,
)


class ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateTypeDef(
    _ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateTypeDef
):
    """
    Type definition for `ClientUpdateApplicationApplicationConfigurationUpdate` `SqlApplicationConfigurationUpdate`

    Describes updates to an SQL-based Kinesis Data Analytics application's configuration.

    - **InputUpdates** *(list) --*

      The array of  InputUpdate objects describing the new input streams used by the application.

      - *(dict) --*

        For an SQL-based Amazon Kinesis Data Analytics application, describes updates to a specific
        input configuration (identified by the ``InputId`` of an application).

        - **InputId** *(string) --* **[REQUIRED]**

          The input ID of the application input to be updated.

        - **NamePrefixUpdate** *(string) --*

          The name prefix for in-application streams that Kinesis Data Analytics creates for the
          specific streaming source.

        - **InputProcessingConfigurationUpdate** *(dict) --*

          Describes updates to an  InputProcessingConfiguration .

          - **InputLambdaProcessorUpdate** *(dict) --* **[REQUIRED]**

            Provides update information for an  InputLambdaProcessor .

            - **ResourceARNUpdate** *(string) --* **[REQUIRED]**

              The Amazon Resource Name (ARN) of the new AWS Lambda function that is used to
              preprocess the records in the stream.

              .. note::

                To specify an earlier version of the Lambda function than the latest, include the
                Lambda function version in the Lambda function ARN. For more information about
                Lambda ARNs, see `Example ARNs\\: AWS Lambda
                </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__

        - **KinesisStreamsInputUpdate** *(dict) --*

          If a Kinesis data stream is the streaming source to be updated, provides an updated
          stream Amazon Resource Name (ARN).

          - **ResourceARNUpdate** *(string) --* **[REQUIRED]**

            The Amazon Resource Name (ARN) of the input Kinesis data stream to read.

        - **KinesisFirehoseInputUpdate** *(dict) --*

          If a Kinesis Data Firehose delivery stream is the streaming source to be updated,
          provides an updated stream ARN.

          - **ResourceARNUpdate** *(string) --* **[REQUIRED]**

            The Amazon Resource Name (ARN) of the input delivery stream to read.

        - **InputSchemaUpdate** *(dict) --*

          Describes the data format on the streaming source, and how record elements on the
          streaming source map to columns of the in-application stream that is created.

          - **RecordFormatUpdate** *(dict) --*

            Specifies the format of the records on the streaming source.

            - **RecordFormatType** *(string) --* **[REQUIRED]**

              The type of record format.

            - **MappingParameters** *(dict) --*

              When you configure application input at the time of creating or updating an
              application, provides additional mapping information specific to the record format
              (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming
              source.

              - **JSONMappingParameters** *(dict) --*

                Provides additional mapping information when JSON is the record format on the
                streaming source.

                - **RecordRowPath** *(string) --* **[REQUIRED]**

                  The path to the top-level parent that contains the records.

              - **CSVMappingParameters** *(dict) --*

                Provides additional mapping information when the record format uses delimiters (for
                example, CSV).

                - **RecordRowDelimiter** *(string) --* **[REQUIRED]**

                  The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
                  delimiter.

                - **RecordColumnDelimiter** *(string) --* **[REQUIRED]**

                  The column delimiter. For example, in a CSV format, a comma (",") is the typical
                  column delimiter.

          - **RecordEncodingUpdate** *(string) --*

            Specifies the encoding of the records in the streaming source; for example, UTF-8.

          - **RecordColumnUpdates** *(list) --*

            A list of ``RecordColumn`` objects. Each object describes the mapping of the streaming
            source element to the corresponding column in the in-application stream.

            - *(dict) --*

              For an SQL-based Amazon Kinesis Data Analytics application, describes the mapping of
              each data element in the streaming source to the corresponding column in the
              in-application stream.

              Also used to describe the format of the reference data source.

              - **Name** *(string) --* **[REQUIRED]**

                The name of the column that is created in the in-application input stream or
                reference table.

              - **Mapping** *(string) --*

                A reference to the data element in the streaming input or the reference data source.

              - **SqlType** *(string) --* **[REQUIRED]**

                The type of column created in the in-application input stream or reference table.

        - **InputParallelismUpdate** *(dict) --*

          Describes the parallelism updates (the number of in-application streams Kinesis Data
          Analytics creates for the specific streaming source).

          - **CountUpdate** *(integer) --* **[REQUIRED]**

            The number of in-application streams to create for the specified streaming source.

    - **OutputUpdates** *(list) --*

      The array of  OutputUpdate objects describing the new destination streams used by the
      application.

      - *(dict) --*

        For an SQL-based Amazon Kinesis Data Analytics application, describes updates to the output
        configuration identified by the ``OutputId`` .

        - **OutputId** *(string) --* **[REQUIRED]**

          Identifies the specific output configuration that you want to update.

        - **NameUpdate** *(string) --*

          If you want to specify a different in-application stream for this output configuration,
          use this field to specify the new in-application stream name.

        - **KinesisStreamsOutputUpdate** *(dict) --*

          Describes a Kinesis data stream as the destination for the output.

          - **ResourceARNUpdate** *(string) --* **[REQUIRED]**

            The Amazon Resource Name (ARN) of the Kinesis data stream where you want to write the
            output.

        - **KinesisFirehoseOutputUpdate** *(dict) --*

          Describes a Kinesis Data Firehose delivery stream as the destination for the output.

          - **ResourceARNUpdate** *(string) --* **[REQUIRED]**

            The Amazon Resource Name (ARN) of the delivery stream to write to.

        - **LambdaOutputUpdate** *(dict) --*

          Describes an AWS Lambda function as the destination for the output.

          - **ResourceARNUpdate** *(string) --* **[REQUIRED]**

            The Amazon Resource Name (ARN) of the destination AWS Lambda function.

            .. note::

              To specify an earlier version of the Lambda function than the latest, include the
              Lambda function version in the Lambda function ARN. For more information about Lambda
              ARNs, see `Example ARNs\\: AWS Lambda
              </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__

        - **DestinationSchemaUpdate** *(dict) --*

          Describes the data format when records are written to the destination.

          - **RecordFormatType** *(string) --* **[REQUIRED]**

            Specifies the format of the records on the output stream.

    - **ReferenceDataSourceUpdates** *(list) --*

      The array of  ReferenceDataSourceUpdate objects describing the new reference data sources
      used by the application.

      - *(dict) --*

        When you update a reference data source configuration for a SQL-based Amazon Kinesis Data
        Analytics application, this object provides all the updated values (such as the source
        bucket name and object key name), the in-application table name that is created, and
        updated mapping information that maps the data in the Amazon S3 object to the
        in-application reference table that is created.

        - **ReferenceId** *(string) --* **[REQUIRED]**

          The ID of the reference data source that is being updated. You can use the
          DescribeApplication operation to get this value.

        - **TableNameUpdate** *(string) --*

          The in-application table name that is created by this update.

        - **S3ReferenceDataSourceUpdate** *(dict) --*

          Describes the S3 bucket name, object key name, and IAM role that Kinesis Data Analytics
          can assume to read the Amazon S3 object on your behalf and populate the in-application
          reference table.

          - **BucketARNUpdate** *(string) --*

            The Amazon Resource Name (ARN) of the S3 bucket.

          - **FileKeyUpdate** *(string) --*

            The object key name.

        - **ReferenceSchemaUpdate** *(dict) --*

          Describes the format of the data in the streaming source, and how each data element maps
          to corresponding columns created in the in-application stream.

          - **RecordFormat** *(dict) --* **[REQUIRED]**

            Specifies the format of the records on the streaming source.

            - **RecordFormatType** *(string) --* **[REQUIRED]**

              The type of record format.

            - **MappingParameters** *(dict) --*

              When you configure application input at the time of creating or updating an
              application, provides additional mapping information specific to the record format
              (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming
              source.

              - **JSONMappingParameters** *(dict) --*

                Provides additional mapping information when JSON is the record format on the
                streaming source.

                - **RecordRowPath** *(string) --* **[REQUIRED]**

                  The path to the top-level parent that contains the records.

              - **CSVMappingParameters** *(dict) --*

                Provides additional mapping information when the record format uses delimiters (for
                example, CSV).

                - **RecordRowDelimiter** *(string) --* **[REQUIRED]**

                  The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
                  delimiter.

                - **RecordColumnDelimiter** *(string) --* **[REQUIRED]**

                  The column delimiter. For example, in a CSV format, a comma (",") is the typical
                  column delimiter.

          - **RecordEncoding** *(string) --*

            Specifies the encoding of the records in the streaming source. For example, UTF-8.

          - **RecordColumns** *(list) --* **[REQUIRED]**

            A list of ``RecordColumn`` objects.

            - *(dict) --*

              For an SQL-based Amazon Kinesis Data Analytics application, describes the mapping of
              each data element in the streaming source to the corresponding column in the
              in-application stream.

              Also used to describe the format of the reference data source.

              - **Name** *(string) --* **[REQUIRED]**

                The name of the column that is created in the in-application input stream or
                reference table.

              - **Mapping** *(string) --*

                A reference to the data element in the streaming input or the reference data source.

              - **SqlType** *(string) --* **[REQUIRED]**

                The type of column created in the in-application input stream or reference table.
    """


_ClientUpdateApplicationApplicationConfigurationUpdateTypeDef = TypedDict(
    "_ClientUpdateApplicationApplicationConfigurationUpdateTypeDef",
    {
        "SqlApplicationConfigurationUpdate": ClientUpdateApplicationApplicationConfigurationUpdateSqlApplicationConfigurationUpdateTypeDef,
        "ApplicationCodeConfigurationUpdate": ClientUpdateApplicationApplicationConfigurationUpdateApplicationCodeConfigurationUpdateTypeDef,
        "FlinkApplicationConfigurationUpdate": ClientUpdateApplicationApplicationConfigurationUpdateFlinkApplicationConfigurationUpdateTypeDef,
        "EnvironmentPropertyUpdates": ClientUpdateApplicationApplicationConfigurationUpdateEnvironmentPropertyUpdatesTypeDef,
        "ApplicationSnapshotConfigurationUpdate": ClientUpdateApplicationApplicationConfigurationUpdateApplicationSnapshotConfigurationUpdateTypeDef,
    },
    total=False,
)


class ClientUpdateApplicationApplicationConfigurationUpdateTypeDef(
    _ClientUpdateApplicationApplicationConfigurationUpdateTypeDef
):
    """
    Type definition for `ClientUpdateApplication` `ApplicationConfigurationUpdate`

    Describes application configuration updates.

    - **SqlApplicationConfigurationUpdate** *(dict) --*

      Describes updates to an SQL-based Kinesis Data Analytics application's configuration.

      - **InputUpdates** *(list) --*

        The array of  InputUpdate objects describing the new input streams used by the application.

        - *(dict) --*

          For an SQL-based Amazon Kinesis Data Analytics application, describes updates to a specific
          input configuration (identified by the ``InputId`` of an application).

          - **InputId** *(string) --* **[REQUIRED]**

            The input ID of the application input to be updated.

          - **NamePrefixUpdate** *(string) --*

            The name prefix for in-application streams that Kinesis Data Analytics creates for the
            specific streaming source.

          - **InputProcessingConfigurationUpdate** *(dict) --*

            Describes updates to an  InputProcessingConfiguration .

            - **InputLambdaProcessorUpdate** *(dict) --* **[REQUIRED]**

              Provides update information for an  InputLambdaProcessor .

              - **ResourceARNUpdate** *(string) --* **[REQUIRED]**

                The Amazon Resource Name (ARN) of the new AWS Lambda function that is used to
                preprocess the records in the stream.

                .. note::

                  To specify an earlier version of the Lambda function than the latest, include the
                  Lambda function version in the Lambda function ARN. For more information about
                  Lambda ARNs, see `Example ARNs\\: AWS Lambda
                  </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__

          - **KinesisStreamsInputUpdate** *(dict) --*

            If a Kinesis data stream is the streaming source to be updated, provides an updated
            stream Amazon Resource Name (ARN).

            - **ResourceARNUpdate** *(string) --* **[REQUIRED]**

              The Amazon Resource Name (ARN) of the input Kinesis data stream to read.

          - **KinesisFirehoseInputUpdate** *(dict) --*

            If a Kinesis Data Firehose delivery stream is the streaming source to be updated,
            provides an updated stream ARN.

            - **ResourceARNUpdate** *(string) --* **[REQUIRED]**

              The Amazon Resource Name (ARN) of the input delivery stream to read.

          - **InputSchemaUpdate** *(dict) --*

            Describes the data format on the streaming source, and how record elements on the
            streaming source map to columns of the in-application stream that is created.

            - **RecordFormatUpdate** *(dict) --*

              Specifies the format of the records on the streaming source.

              - **RecordFormatType** *(string) --* **[REQUIRED]**

                The type of record format.

              - **MappingParameters** *(dict) --*

                When you configure application input at the time of creating or updating an
                application, provides additional mapping information specific to the record format
                (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming
                source.

                - **JSONMappingParameters** *(dict) --*

                  Provides additional mapping information when JSON is the record format on the
                  streaming source.

                  - **RecordRowPath** *(string) --* **[REQUIRED]**

                    The path to the top-level parent that contains the records.

                - **CSVMappingParameters** *(dict) --*

                  Provides additional mapping information when the record format uses delimiters (for
                  example, CSV).

                  - **RecordRowDelimiter** *(string) --* **[REQUIRED]**

                    The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
                    delimiter.

                  - **RecordColumnDelimiter** *(string) --* **[REQUIRED]**

                    The column delimiter. For example, in a CSV format, a comma (",") is the typical
                    column delimiter.

            - **RecordEncodingUpdate** *(string) --*

              Specifies the encoding of the records in the streaming source; for example, UTF-8.

            - **RecordColumnUpdates** *(list) --*

              A list of ``RecordColumn`` objects. Each object describes the mapping of the streaming
              source element to the corresponding column in the in-application stream.

              - *(dict) --*

                For an SQL-based Amazon Kinesis Data Analytics application, describes the mapping of
                each data element in the streaming source to the corresponding column in the
                in-application stream.

                Also used to describe the format of the reference data source.

                - **Name** *(string) --* **[REQUIRED]**

                  The name of the column that is created in the in-application input stream or
                  reference table.

                - **Mapping** *(string) --*

                  A reference to the data element in the streaming input or the reference data source.

                - **SqlType** *(string) --* **[REQUIRED]**

                  The type of column created in the in-application input stream or reference table.

          - **InputParallelismUpdate** *(dict) --*

            Describes the parallelism updates (the number of in-application streams Kinesis Data
            Analytics creates for the specific streaming source).

            - **CountUpdate** *(integer) --* **[REQUIRED]**

              The number of in-application streams to create for the specified streaming source.

      - **OutputUpdates** *(list) --*

        The array of  OutputUpdate objects describing the new destination streams used by the
        application.

        - *(dict) --*

          For an SQL-based Amazon Kinesis Data Analytics application, describes updates to the output
          configuration identified by the ``OutputId`` .

          - **OutputId** *(string) --* **[REQUIRED]**

            Identifies the specific output configuration that you want to update.

          - **NameUpdate** *(string) --*

            If you want to specify a different in-application stream for this output configuration,
            use this field to specify the new in-application stream name.

          - **KinesisStreamsOutputUpdate** *(dict) --*

            Describes a Kinesis data stream as the destination for the output.

            - **ResourceARNUpdate** *(string) --* **[REQUIRED]**

              The Amazon Resource Name (ARN) of the Kinesis data stream where you want to write the
              output.

          - **KinesisFirehoseOutputUpdate** *(dict) --*

            Describes a Kinesis Data Firehose delivery stream as the destination for the output.

            - **ResourceARNUpdate** *(string) --* **[REQUIRED]**

              The Amazon Resource Name (ARN) of the delivery stream to write to.

          - **LambdaOutputUpdate** *(dict) --*

            Describes an AWS Lambda function as the destination for the output.

            - **ResourceARNUpdate** *(string) --* **[REQUIRED]**

              The Amazon Resource Name (ARN) of the destination AWS Lambda function.

              .. note::

                To specify an earlier version of the Lambda function than the latest, include the
                Lambda function version in the Lambda function ARN. For more information about Lambda
                ARNs, see `Example ARNs\\: AWS Lambda
                </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__

          - **DestinationSchemaUpdate** *(dict) --*

            Describes the data format when records are written to the destination.

            - **RecordFormatType** *(string) --* **[REQUIRED]**

              Specifies the format of the records on the output stream.

      - **ReferenceDataSourceUpdates** *(list) --*

        The array of  ReferenceDataSourceUpdate objects describing the new reference data sources
        used by the application.

        - *(dict) --*

          When you update a reference data source configuration for a SQL-based Amazon Kinesis Data
          Analytics application, this object provides all the updated values (such as the source
          bucket name and object key name), the in-application table name that is created, and
          updated mapping information that maps the data in the Amazon S3 object to the
          in-application reference table that is created.

          - **ReferenceId** *(string) --* **[REQUIRED]**

            The ID of the reference data source that is being updated. You can use the
            DescribeApplication operation to get this value.

          - **TableNameUpdate** *(string) --*

            The in-application table name that is created by this update.

          - **S3ReferenceDataSourceUpdate** *(dict) --*

            Describes the S3 bucket name, object key name, and IAM role that Kinesis Data Analytics
            can assume to read the Amazon S3 object on your behalf and populate the in-application
            reference table.

            - **BucketARNUpdate** *(string) --*

              The Amazon Resource Name (ARN) of the S3 bucket.

            - **FileKeyUpdate** *(string) --*

              The object key name.

          - **ReferenceSchemaUpdate** *(dict) --*

            Describes the format of the data in the streaming source, and how each data element maps
            to corresponding columns created in the in-application stream.

            - **RecordFormat** *(dict) --* **[REQUIRED]**

              Specifies the format of the records on the streaming source.

              - **RecordFormatType** *(string) --* **[REQUIRED]**

                The type of record format.

              - **MappingParameters** *(dict) --*

                When you configure application input at the time of creating or updating an
                application, provides additional mapping information specific to the record format
                (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming
                source.

                - **JSONMappingParameters** *(dict) --*

                  Provides additional mapping information when JSON is the record format on the
                  streaming source.

                  - **RecordRowPath** *(string) --* **[REQUIRED]**

                    The path to the top-level parent that contains the records.

                - **CSVMappingParameters** *(dict) --*

                  Provides additional mapping information when the record format uses delimiters (for
                  example, CSV).

                  - **RecordRowDelimiter** *(string) --* **[REQUIRED]**

                    The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
                    delimiter.

                  - **RecordColumnDelimiter** *(string) --* **[REQUIRED]**

                    The column delimiter. For example, in a CSV format, a comma (",") is the typical
                    column delimiter.

            - **RecordEncoding** *(string) --*

              Specifies the encoding of the records in the streaming source. For example, UTF-8.

            - **RecordColumns** *(list) --* **[REQUIRED]**

              A list of ``RecordColumn`` objects.

              - *(dict) --*

                For an SQL-based Amazon Kinesis Data Analytics application, describes the mapping of
                each data element in the streaming source to the corresponding column in the
                in-application stream.

                Also used to describe the format of the reference data source.

                - **Name** *(string) --* **[REQUIRED]**

                  The name of the column that is created in the in-application input stream or
                  reference table.

                - **Mapping** *(string) --*

                  A reference to the data element in the streaming input or the reference data source.

                - **SqlType** *(string) --* **[REQUIRED]**

                  The type of column created in the in-application input stream or reference table.

    - **ApplicationCodeConfigurationUpdate** *(dict) --*

      Describes updates to a Java-based Kinesis Data Analytics application's code configuration.

      - **CodeContentTypeUpdate** *(string) --*

        Describes updates to the code content type.

      - **CodeContentUpdate** *(dict) --*

        Describes updates to the code content of an application.

        - **TextContentUpdate** *(string) --*

          Describes an update to the text code for an application.

        - **ZipFileContentUpdate** *(bytes) --*

          Describes an update to the zipped code for an application.

        - **S3ContentLocationUpdate** *(dict) --*

          Describes an update to the location of code for an application.

          - **BucketARNUpdate** *(string) --*

            The new Amazon Resource Name (ARN) for the S3 bucket containing the application code.

          - **FileKeyUpdate** *(string) --*

            The new file key for the object containing the application code.

          - **ObjectVersionUpdate** *(string) --*

            The new version of the object containing the application code.

    - **FlinkApplicationConfigurationUpdate** *(dict) --*

      Describes updates to a Java-based Kinesis Data Analytics application's configuration.

      - **CheckpointConfigurationUpdate** *(dict) --*

        Describes updates to an application's checkpointing configuration. Checkpointing is the
        process of persisting application state for fault tolerance.

        - **ConfigurationTypeUpdate** *(string) --*

          Describes updates to whether the application uses the default checkpointing behavior of
          Kinesis Data Analytics.

        - **CheckpointingEnabledUpdate** *(boolean) --*

          Describes updates to whether checkpointing is enabled for an application.

        - **CheckpointIntervalUpdate** *(integer) --*

          Describes updates to the interval in milliseconds between checkpoint operations.

        - **MinPauseBetweenCheckpointsUpdate** *(integer) --*

          Describes updates to the minimum time in milliseconds after a checkpoint operation
          completes that a new checkpoint operation can start.

      - **MonitoringConfigurationUpdate** *(dict) --*

        Describes updates to the configuration parameters for Amazon CloudWatch logging for an
        application.

        - **ConfigurationTypeUpdate** *(string) --*

          Describes updates to whether to use the default CloudWatch logging configuration for an
          application.

        - **MetricsLevelUpdate** *(string) --*

          Describes updates to the granularity of the CloudWatch Logs for an application.

        - **LogLevelUpdate** *(string) --*

          Describes updates to the verbosity of the CloudWatch Logs for an application.

      - **ParallelismConfigurationUpdate** *(dict) --*

        Describes updates to the parameters for how an application executes multiple tasks
        simultaneously.

        - **ConfigurationTypeUpdate** *(string) --*

          Describes updates to whether the application uses the default parallelism for the Kinesis
          Data Analytics service, or if a custom parallelism is used.

        - **ParallelismUpdate** *(integer) --*

          Describes updates to the initial number of parallel tasks an application can perform.

        - **ParallelismPerKPUUpdate** *(integer) --*

          Describes updates to the number of parallel tasks an application can perform per Kinesis
          Processing Unit (KPU) used by the application.

        - **AutoScalingEnabledUpdate** *(boolean) --*

          Describes updates to whether the Kinesis Data Analytics service can increase the
          parallelism of the application in response to increased throughput.

    - **EnvironmentPropertyUpdates** *(dict) --*

      Describes updates to the environment properties for a Java-based Kinesis Data Analytics
      application.

      - **PropertyGroups** *(list) --* **[REQUIRED]**

        Describes updates to the execution property groups.

        - *(dict) --*

          Property key-value pairs passed into a Java-based Kinesis Data Analytics application.

          - **PropertyGroupId** *(string) --* **[REQUIRED]**

            Describes the key of an application execution property key-value pair.

          - **PropertyMap** *(dict) --* **[REQUIRED]**

            Describes the value of an application execution property key-value pair.

            - *(string) --*

              - *(string) --*

    - **ApplicationSnapshotConfigurationUpdate** *(dict) --*

      Describes whether snapshots are enabled for a Java-based Kinesis Data Analytics application.

      - **SnapshotsEnabledUpdate** *(boolean) --* **[REQUIRED]**

        Describes updates to whether snapshots are enabled for a Java-based Kinesis Data Analytics
        application.
    """


_RequiredClientUpdateApplicationCloudWatchLoggingOptionUpdatesTypeDef = TypedDict(
    "_RequiredClientUpdateApplicationCloudWatchLoggingOptionUpdatesTypeDef",
    {"CloudWatchLoggingOptionId": str},
)
_OptionalClientUpdateApplicationCloudWatchLoggingOptionUpdatesTypeDef = TypedDict(
    "_OptionalClientUpdateApplicationCloudWatchLoggingOptionUpdatesTypeDef",
    {"LogStreamARNUpdate": str},
    total=False,
)


class ClientUpdateApplicationCloudWatchLoggingOptionUpdatesTypeDef(
    _RequiredClientUpdateApplicationCloudWatchLoggingOptionUpdatesTypeDef,
    _OptionalClientUpdateApplicationCloudWatchLoggingOptionUpdatesTypeDef,
):
    """
    Type definition for `ClientUpdateApplication` `CloudWatchLoggingOptionUpdates`

    Describes the Amazon CloudWatch logging option updates.

    - **CloudWatchLoggingOptionId** *(string) --* **[REQUIRED]**

      The ID of the CloudWatch logging option to update

    - **LogStreamARNUpdate** *(string) --*

      The Amazon Resource Name (ARN) of the CloudWatch log to receive application messages.
    """


_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionApplicationCodeConfigurationDescriptionCodeContentDescriptionS3ApplicationCodeLocationDescriptionTypeDef = TypedDict(
    "_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionApplicationCodeConfigurationDescriptionCodeContentDescriptionS3ApplicationCodeLocationDescriptionTypeDef",
    {"BucketARN": str, "FileKey": str, "ObjectVersion": str},
    total=False,
)


class ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionApplicationCodeConfigurationDescriptionCodeContentDescriptionS3ApplicationCodeLocationDescriptionTypeDef(
    _ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionApplicationCodeConfigurationDescriptionCodeContentDescriptionS3ApplicationCodeLocationDescriptionTypeDef
):
    """
    Type definition for `ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionApplicationCodeConfigurationDescriptionCodeContentDescription` `S3ApplicationCodeLocationDescription`

    The S3 bucket Amazon Resource Name (ARN), file key, and object version of the
    application code stored in Amazon S3.

    - **BucketARN** *(string) --*

      The Amazon Resource Name (ARN) for the S3 bucket containing the application code.

    - **FileKey** *(string) --*

      The file key for the object containing the application code.

    - **ObjectVersion** *(string) --*

      The version of the object containing the application code.
    """


_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionApplicationCodeConfigurationDescriptionCodeContentDescriptionTypeDef = TypedDict(
    "_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionApplicationCodeConfigurationDescriptionCodeContentDescriptionTypeDef",
    {
        "TextContent": str,
        "CodeMD5": str,
        "CodeSize": int,
        "S3ApplicationCodeLocationDescription": ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionApplicationCodeConfigurationDescriptionCodeContentDescriptionS3ApplicationCodeLocationDescriptionTypeDef,
    },
    total=False,
)


class ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionApplicationCodeConfigurationDescriptionCodeContentDescriptionTypeDef(
    _ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionApplicationCodeConfigurationDescriptionCodeContentDescriptionTypeDef
):
    """
    Type definition for `ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionApplicationCodeConfigurationDescription` `CodeContentDescription`

    Describes details about the location and format of the application code.

    - **TextContent** *(string) --*

      The text-format code

    - **CodeMD5** *(string) --*

      The checksum that can be used to validate zip-format code.

    - **CodeSize** *(integer) --*

      The size in bytes of the application code. Can be used to validate zip-format code.

    - **S3ApplicationCodeLocationDescription** *(dict) --*

      The S3 bucket Amazon Resource Name (ARN), file key, and object version of the
      application code stored in Amazon S3.

      - **BucketARN** *(string) --*

        The Amazon Resource Name (ARN) for the S3 bucket containing the application code.

      - **FileKey** *(string) --*

        The file key for the object containing the application code.

      - **ObjectVersion** *(string) --*

        The version of the object containing the application code.
    """


_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionApplicationCodeConfigurationDescriptionTypeDef = TypedDict(
    "_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionApplicationCodeConfigurationDescriptionTypeDef",
    {
        "CodeContentType": str,
        "CodeContentDescription": ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionApplicationCodeConfigurationDescriptionCodeContentDescriptionTypeDef,
    },
    total=False,
)


class ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionApplicationCodeConfigurationDescriptionTypeDef(
    _ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionApplicationCodeConfigurationDescriptionTypeDef
):
    """
    Type definition for `ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescription` `ApplicationCodeConfigurationDescription`

    The details about the application code for a Java-based Kinesis Data Analytics
    application.

    - **CodeContentType** *(string) --*

      Specifies whether the code content is in text or zip format.

    - **CodeContentDescription** *(dict) --*

      Describes details about the location and format of the application code.

      - **TextContent** *(string) --*

        The text-format code

      - **CodeMD5** *(string) --*

        The checksum that can be used to validate zip-format code.

      - **CodeSize** *(integer) --*

        The size in bytes of the application code. Can be used to validate zip-format code.

      - **S3ApplicationCodeLocationDescription** *(dict) --*

        The S3 bucket Amazon Resource Name (ARN), file key, and object version of the
        application code stored in Amazon S3.

        - **BucketARN** *(string) --*

          The Amazon Resource Name (ARN) for the S3 bucket containing the application code.

        - **FileKey** *(string) --*

          The file key for the object containing the application code.

        - **ObjectVersion** *(string) --*

          The version of the object containing the application code.
    """


_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionApplicationSnapshotConfigurationDescriptionTypeDef = TypedDict(
    "_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionApplicationSnapshotConfigurationDescriptionTypeDef",
    {"SnapshotsEnabled": bool},
    total=False,
)


class ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionApplicationSnapshotConfigurationDescriptionTypeDef(
    _ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionApplicationSnapshotConfigurationDescriptionTypeDef
):
    """
    Type definition for `ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescription` `ApplicationSnapshotConfigurationDescription`

    Describes whether snapshots are enabled for a Java-based Kinesis Data Analytics
    application.

    - **SnapshotsEnabled** *(boolean) --*

      Describes whether snapshots are enabled for a Java-based Kinesis Data Analytics
      application.
    """


_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionEnvironmentPropertyDescriptionsPropertyGroupDescriptionsTypeDef = TypedDict(
    "_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionEnvironmentPropertyDescriptionsPropertyGroupDescriptionsTypeDef",
    {"PropertyGroupId": str, "PropertyMap": Dict[str, str]},
    total=False,
)


class ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionEnvironmentPropertyDescriptionsPropertyGroupDescriptionsTypeDef(
    _ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionEnvironmentPropertyDescriptionsPropertyGroupDescriptionsTypeDef
):
    """
    Type definition for `ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionEnvironmentPropertyDescriptions` `PropertyGroupDescriptions`

    Property key-value pairs passed into a Java-based Kinesis Data Analytics application.

    - **PropertyGroupId** *(string) --*

      Describes the key of an application execution property key-value pair.

    - **PropertyMap** *(dict) --*

      Describes the value of an application execution property key-value pair.

      - *(string) --*

        - *(string) --*
    """


_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionEnvironmentPropertyDescriptionsTypeDef = TypedDict(
    "_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionEnvironmentPropertyDescriptionsTypeDef",
    {
        "PropertyGroupDescriptions": List[
            ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionEnvironmentPropertyDescriptionsPropertyGroupDescriptionsTypeDef
        ]
    },
    total=False,
)


class ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionEnvironmentPropertyDescriptionsTypeDef(
    _ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionEnvironmentPropertyDescriptionsTypeDef
):
    """
    Type definition for `ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescription` `EnvironmentPropertyDescriptions`

    Describes execution properties for a Java-based Kinesis Data Analytics application.

    - **PropertyGroupDescriptions** *(list) --*

      Describes the execution property groups.

      - *(dict) --*

        Property key-value pairs passed into a Java-based Kinesis Data Analytics application.

        - **PropertyGroupId** *(string) --*

          Describes the key of an application execution property key-value pair.

        - **PropertyMap** *(dict) --*

          Describes the value of an application execution property key-value pair.

          - *(string) --*

            - *(string) --*
    """


_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionFlinkApplicationConfigurationDescriptionCheckpointConfigurationDescriptionTypeDef = TypedDict(
    "_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionFlinkApplicationConfigurationDescriptionCheckpointConfigurationDescriptionTypeDef",
    {
        "ConfigurationType": str,
        "CheckpointingEnabled": bool,
        "CheckpointInterval": int,
        "MinPauseBetweenCheckpoints": int,
    },
    total=False,
)


class ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionFlinkApplicationConfigurationDescriptionCheckpointConfigurationDescriptionTypeDef(
    _ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionFlinkApplicationConfigurationDescriptionCheckpointConfigurationDescriptionTypeDef
):
    """
    Type definition for `ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionFlinkApplicationConfigurationDescription` `CheckpointConfigurationDescription`

    Describes an application's checkpointing configuration. Checkpointing is the process of
    persisting application state for fault tolerance.

    - **ConfigurationType** *(string) --*

      Describes whether the application uses the default checkpointing behavior in Kinesis
      Data Analytics.

    - **CheckpointingEnabled** *(boolean) --*

      Describes whether checkpointing is enabled for a Java-based Kinesis Data Analytics
      application.

    - **CheckpointInterval** *(integer) --*

      Describes the interval in milliseconds between checkpoint operations.

    - **MinPauseBetweenCheckpoints** *(integer) --*

      Describes the minimum time in milliseconds after a checkpoint operation completes
      that a new checkpoint operation can start.
    """


_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionFlinkApplicationConfigurationDescriptionMonitoringConfigurationDescriptionTypeDef = TypedDict(
    "_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionFlinkApplicationConfigurationDescriptionMonitoringConfigurationDescriptionTypeDef",
    {"ConfigurationType": str, "MetricsLevel": str, "LogLevel": str},
    total=False,
)


class ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionFlinkApplicationConfigurationDescriptionMonitoringConfigurationDescriptionTypeDef(
    _ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionFlinkApplicationConfigurationDescriptionMonitoringConfigurationDescriptionTypeDef
):
    """
    Type definition for `ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionFlinkApplicationConfigurationDescription` `MonitoringConfigurationDescription`

    Describes configuration parameters for Amazon CloudWatch logging for an application.

    - **ConfigurationType** *(string) --*

      Describes whether to use the default CloudWatch logging configuration for an
      application.

    - **MetricsLevel** *(string) --*

      Describes the granularity of the CloudWatch Logs for an application.

    - **LogLevel** *(string) --*

      Describes the verbosity of the CloudWatch Logs for an application.
    """


_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionFlinkApplicationConfigurationDescriptionParallelismConfigurationDescriptionTypeDef = TypedDict(
    "_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionFlinkApplicationConfigurationDescriptionParallelismConfigurationDescriptionTypeDef",
    {
        "ConfigurationType": str,
        "Parallelism": int,
        "ParallelismPerKPU": int,
        "CurrentParallelism": int,
        "AutoScalingEnabled": bool,
    },
    total=False,
)


class ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionFlinkApplicationConfigurationDescriptionParallelismConfigurationDescriptionTypeDef(
    _ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionFlinkApplicationConfigurationDescriptionParallelismConfigurationDescriptionTypeDef
):
    """
    Type definition for `ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionFlinkApplicationConfigurationDescription` `ParallelismConfigurationDescription`

    Describes parameters for how an application executes multiple tasks simultaneously.

    - **ConfigurationType** *(string) --*

      Describes whether the application uses the default parallelism for the Kinesis Data
      Analytics service.

    - **Parallelism** *(integer) --*

      Describes the initial number of parallel tasks that a Java-based Kinesis Data
      Analytics application can perform.

    - **ParallelismPerKPU** *(integer) --*

      Describes the number of parallel tasks that a Java-based Kinesis Data Analytics
      application can perform per Kinesis Processing Unit (KPU) used by the application.

    - **CurrentParallelism** *(integer) --*

      Describes the current number of parallel tasks that a Java-based Kinesis Data
      Analytics application can perform.

    - **AutoScalingEnabled** *(boolean) --*

      Describes whether the Kinesis Data Analytics service can increase the parallelism of
      the application in response to increased throughput.
    """


_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionFlinkApplicationConfigurationDescriptionTypeDef = TypedDict(
    "_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionFlinkApplicationConfigurationDescriptionTypeDef",
    {
        "CheckpointConfigurationDescription": ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionFlinkApplicationConfigurationDescriptionCheckpointConfigurationDescriptionTypeDef,
        "MonitoringConfigurationDescription": ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionFlinkApplicationConfigurationDescriptionMonitoringConfigurationDescriptionTypeDef,
        "ParallelismConfigurationDescription": ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionFlinkApplicationConfigurationDescriptionParallelismConfigurationDescriptionTypeDef,
        "JobPlanDescription": str,
    },
    total=False,
)


class ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionFlinkApplicationConfigurationDescriptionTypeDef(
    _ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionFlinkApplicationConfigurationDescriptionTypeDef
):
    """
    Type definition for `ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescription` `FlinkApplicationConfigurationDescription`

    The details about a Java-based Kinesis Data Analytics application.

    - **CheckpointConfigurationDescription** *(dict) --*

      Describes an application's checkpointing configuration. Checkpointing is the process of
      persisting application state for fault tolerance.

      - **ConfigurationType** *(string) --*

        Describes whether the application uses the default checkpointing behavior in Kinesis
        Data Analytics.

      - **CheckpointingEnabled** *(boolean) --*

        Describes whether checkpointing is enabled for a Java-based Kinesis Data Analytics
        application.

      - **CheckpointInterval** *(integer) --*

        Describes the interval in milliseconds between checkpoint operations.

      - **MinPauseBetweenCheckpoints** *(integer) --*

        Describes the minimum time in milliseconds after a checkpoint operation completes
        that a new checkpoint operation can start.

    - **MonitoringConfigurationDescription** *(dict) --*

      Describes configuration parameters for Amazon CloudWatch logging for an application.

      - **ConfigurationType** *(string) --*

        Describes whether to use the default CloudWatch logging configuration for an
        application.

      - **MetricsLevel** *(string) --*

        Describes the granularity of the CloudWatch Logs for an application.

      - **LogLevel** *(string) --*

        Describes the verbosity of the CloudWatch Logs for an application.

    - **ParallelismConfigurationDescription** *(dict) --*

      Describes parameters for how an application executes multiple tasks simultaneously.

      - **ConfigurationType** *(string) --*

        Describes whether the application uses the default parallelism for the Kinesis Data
        Analytics service.

      - **Parallelism** *(integer) --*

        Describes the initial number of parallel tasks that a Java-based Kinesis Data
        Analytics application can perform.

      - **ParallelismPerKPU** *(integer) --*

        Describes the number of parallel tasks that a Java-based Kinesis Data Analytics
        application can perform per Kinesis Processing Unit (KPU) used by the application.

      - **CurrentParallelism** *(integer) --*

        Describes the current number of parallel tasks that a Java-based Kinesis Data
        Analytics application can perform.

      - **AutoScalingEnabled** *(boolean) --*

        Describes whether the Kinesis Data Analytics service can increase the parallelism of
        the application in response to increased throughput.

    - **JobPlanDescription** *(string) --*

      The job plan for an application. For more information about the job plan, see `Jobs and
      Scheduling
      <https://ci.apache.org/projects/flink/flink-docs-stable/internals/job_scheduling.html>`__
      in the `Apache Flink Documentation
      <https://ci.apache.org/projects/flink/flink-docs-release-1.6/>`__ . To retrieve the job
      plan for the application, use the  DescribeApplicationRequest$IncludeAdditionalDetails
      parameter of the  DescribeApplication operation.
    """


_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionRunConfigurationDescriptionApplicationRestoreConfigurationDescriptionTypeDef = TypedDict(
    "_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionRunConfigurationDescriptionApplicationRestoreConfigurationDescriptionTypeDef",
    {"ApplicationRestoreType": str, "SnapshotName": str},
    total=False,
)


class ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionRunConfigurationDescriptionApplicationRestoreConfigurationDescriptionTypeDef(
    _ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionRunConfigurationDescriptionApplicationRestoreConfigurationDescriptionTypeDef
):
    """
    Type definition for `ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionRunConfigurationDescription` `ApplicationRestoreConfigurationDescription`

    Describes the restore behavior of a restarting application.

    - **ApplicationRestoreType** *(string) --*

      Specifies how the application should be restored.

    - **SnapshotName** *(string) --*

      The identifier of an existing snapshot of application state to use to restart an
      application. The application uses this value if ``RESTORE_FROM_CUSTOM_SNAPSHOT`` is
      specified for the ``ApplicationRestoreType`` .
    """


_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionRunConfigurationDescriptionTypeDef = TypedDict(
    "_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionRunConfigurationDescriptionTypeDef",
    {
        "ApplicationRestoreConfigurationDescription": ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionRunConfigurationDescriptionApplicationRestoreConfigurationDescriptionTypeDef
    },
    total=False,
)


class ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionRunConfigurationDescriptionTypeDef(
    _ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionRunConfigurationDescriptionTypeDef
):
    """
    Type definition for `ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescription` `RunConfigurationDescription`

    The details about the starting properties for a Kinesis Data Analytics application.

    - **ApplicationRestoreConfigurationDescription** *(dict) --*

      Describes the restore behavior of a restarting application.

      - **ApplicationRestoreType** *(string) --*

        Specifies how the application should be restored.

      - **SnapshotName** *(string) --*

        The identifier of an existing snapshot of application state to use to restart an
        application. The application uses this value if ``RESTORE_FROM_CUSTOM_SNAPSHOT`` is
        specified for the ``ApplicationRestoreType`` .
    """


_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputParallelismTypeDef = TypedDict(
    "_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputParallelismTypeDef",
    {"Count": int},
    total=False,
)


class ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputParallelismTypeDef(
    _ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputParallelismTypeDef
):
    """
    Type definition for `ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptions` `InputParallelism`

    Describes the configured parallelism (number of in-application streams mapped to
    the streaming source).

    - **Count** *(integer) --*

      The number of in-application streams to create.
    """


_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputProcessingConfigurationDescriptionInputLambdaProcessorDescriptionTypeDef = TypedDict(
    "_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputProcessingConfigurationDescriptionInputLambdaProcessorDescriptionTypeDef",
    {"ResourceARN": str, "RoleARN": str},
    total=False,
)


class ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputProcessingConfigurationDescriptionInputLambdaProcessorDescriptionTypeDef(
    _ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputProcessingConfigurationDescriptionInputLambdaProcessorDescriptionTypeDef
):
    """
    Type definition for `ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputProcessingConfigurationDescription` `InputLambdaProcessorDescription`

    Provides configuration information about the associated
    InputLambdaProcessorDescription

    - **ResourceARN** *(string) --*

      The ARN of the AWS Lambda function that is used to preprocess the records in
      the stream.

      .. note::

        To specify an earlier version of the Lambda function than the latest, include
        the Lambda function version in the Lambda function ARN. For more information
        about Lambda ARNs, see `Example ARNs\\: AWS Lambda
        </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__

    - **RoleARN** *(string) --*

      The ARN of the IAM role that is used to access the AWS Lambda function.

      .. note::

        Provided for backward compatibility. Applications that are created with the
        current API version have an application-level service execution role rather
        than a resource-level role.
    """


_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputProcessingConfigurationDescriptionTypeDef = TypedDict(
    "_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputProcessingConfigurationDescriptionTypeDef",
    {
        "InputLambdaProcessorDescription": ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputProcessingConfigurationDescriptionInputLambdaProcessorDescriptionTypeDef
    },
    total=False,
)


class ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputProcessingConfigurationDescriptionTypeDef(
    _ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputProcessingConfigurationDescriptionTypeDef
):
    """
    Type definition for `ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptions` `InputProcessingConfigurationDescription`

    The description of the preprocessor that executes on records in this input before
    the application's code is run.

    - **InputLambdaProcessorDescription** *(dict) --*

      Provides configuration information about the associated
      InputLambdaProcessorDescription

      - **ResourceARN** *(string) --*

        The ARN of the AWS Lambda function that is used to preprocess the records in
        the stream.

        .. note::

          To specify an earlier version of the Lambda function than the latest, include
          the Lambda function version in the Lambda function ARN. For more information
          about Lambda ARNs, see `Example ARNs\\: AWS Lambda
          </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__

      - **RoleARN** *(string) --*

        The ARN of the IAM role that is used to access the AWS Lambda function.

        .. note::

          Provided for backward compatibility. Applications that are created with the
          current API version have an application-level service execution role rather
          than a resource-level role.
    """


_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordColumnsTypeDef = TypedDict(
    "_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordColumnsTypeDef",
    {"Name": str, "Mapping": str, "SqlType": str},
    total=False,
)


class ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordColumnsTypeDef(
    _ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordColumnsTypeDef
):
    """
    Type definition for `ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchema` `RecordColumns`

    For an SQL-based Amazon Kinesis Data Analytics application, describes the
    mapping of each data element in the streaming source to the corresponding
    column in the in-application stream.

    Also used to describe the format of the reference data source.

    - **Name** *(string) --*

      The name of the column that is created in the in-application input stream or
      reference table.

    - **Mapping** *(string) --*

      A reference to the data element in the streaming input or the reference data
      source.

    - **SqlType** *(string) --*

      The type of column created in the in-application input stream or reference
      table.
    """


_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef = TypedDict(
    "_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef",
    {"RecordRowDelimiter": str, "RecordColumnDelimiter": str},
    total=False,
)


class ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef(
    _ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef
):
    """
    Type definition for `ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordFormatMappingParameters` `CSVMappingParameters`

    Provides additional mapping information when the record format uses
    delimiters (for example, CSV).

    - **RecordRowDelimiter** *(string) --*

      The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
      delimiter.

    - **RecordColumnDelimiter** *(string) --*

      The column delimiter. For example, in a CSV format, a comma (",") is the
      typical column delimiter.
    """


_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef = TypedDict(
    "_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef",
    {"RecordRowPath": str},
    total=False,
)


class ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef(
    _ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef
):
    """
    Type definition for `ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordFormatMappingParameters` `JSONMappingParameters`

    Provides additional mapping information when JSON is the record format on the
    streaming source.

    - **RecordRowPath** *(string) --*

      The path to the top-level parent that contains the records.
    """


_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordFormatMappingParametersTypeDef = TypedDict(
    "_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordFormatMappingParametersTypeDef",
    {
        "JSONMappingParameters": ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef,
        "CSVMappingParameters": ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef,
    },
    total=False,
)


class ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordFormatMappingParametersTypeDef(
    _ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordFormatMappingParametersTypeDef
):
    """
    Type definition for `ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordFormat` `MappingParameters`

    When you configure application input at the time of creating or updating an
    application, provides additional mapping information specific to the record
    format (such as JSON, CSV, or record fields delimited by some delimiter) on the
    streaming source.

    - **JSONMappingParameters** *(dict) --*

      Provides additional mapping information when JSON is the record format on the
      streaming source.

      - **RecordRowPath** *(string) --*

        The path to the top-level parent that contains the records.

    - **CSVMappingParameters** *(dict) --*

      Provides additional mapping information when the record format uses
      delimiters (for example, CSV).

      - **RecordRowDelimiter** *(string) --*

        The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
        delimiter.

      - **RecordColumnDelimiter** *(string) --*

        The column delimiter. For example, in a CSV format, a comma (",") is the
        typical column delimiter.
    """


_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordFormatTypeDef = TypedDict(
    "_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordFormatTypeDef",
    {
        "RecordFormatType": str,
        "MappingParameters": ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordFormatMappingParametersTypeDef,
    },
    total=False,
)


class ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordFormatTypeDef(
    _ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordFormatTypeDef
):
    """
    Type definition for `ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchema` `RecordFormat`

    Specifies the format of the records on the streaming source.

    - **RecordFormatType** *(string) --*

      The type of record format.

    - **MappingParameters** *(dict) --*

      When you configure application input at the time of creating or updating an
      application, provides additional mapping information specific to the record
      format (such as JSON, CSV, or record fields delimited by some delimiter) on the
      streaming source.

      - **JSONMappingParameters** *(dict) --*

        Provides additional mapping information when JSON is the record format on the
        streaming source.

        - **RecordRowPath** *(string) --*

          The path to the top-level parent that contains the records.

      - **CSVMappingParameters** *(dict) --*

        Provides additional mapping information when the record format uses
        delimiters (for example, CSV).

        - **RecordRowDelimiter** *(string) --*

          The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
          delimiter.

        - **RecordColumnDelimiter** *(string) --*

          The column delimiter. For example, in a CSV format, a comma (",") is the
          typical column delimiter.
    """


_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaTypeDef = TypedDict(
    "_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaTypeDef",
    {
        "RecordFormat": ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordFormatTypeDef,
        "RecordEncoding": str,
        "RecordColumns": List[
            ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaRecordColumnsTypeDef
        ],
    },
    total=False,
)


class ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaTypeDef(
    _ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaTypeDef
):
    """
    Type definition for `ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptions` `InputSchema`

    Describes the format of the data in the streaming source, and how each data element
    maps to corresponding columns in the in-application stream that is being created.

    - **RecordFormat** *(dict) --*

      Specifies the format of the records on the streaming source.

      - **RecordFormatType** *(string) --*

        The type of record format.

      - **MappingParameters** *(dict) --*

        When you configure application input at the time of creating or updating an
        application, provides additional mapping information specific to the record
        format (such as JSON, CSV, or record fields delimited by some delimiter) on the
        streaming source.

        - **JSONMappingParameters** *(dict) --*

          Provides additional mapping information when JSON is the record format on the
          streaming source.

          - **RecordRowPath** *(string) --*

            The path to the top-level parent that contains the records.

        - **CSVMappingParameters** *(dict) --*

          Provides additional mapping information when the record format uses
          delimiters (for example, CSV).

          - **RecordRowDelimiter** *(string) --*

            The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
            delimiter.

          - **RecordColumnDelimiter** *(string) --*

            The column delimiter. For example, in a CSV format, a comma (",") is the
            typical column delimiter.

    - **RecordEncoding** *(string) --*

      Specifies the encoding of the records in the streaming source. For example, UTF-8.

    - **RecordColumns** *(list) --*

      A list of ``RecordColumn`` objects.

      - *(dict) --*

        For an SQL-based Amazon Kinesis Data Analytics application, describes the
        mapping of each data element in the streaming source to the corresponding
        column in the in-application stream.

        Also used to describe the format of the reference data source.

        - **Name** *(string) --*

          The name of the column that is created in the in-application input stream or
          reference table.

        - **Mapping** *(string) --*

          A reference to the data element in the streaming input or the reference data
          source.

        - **SqlType** *(string) --*

          The type of column created in the in-application input stream or reference
          table.
    """


_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputStartingPositionConfigurationTypeDef = TypedDict(
    "_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputStartingPositionConfigurationTypeDef",
    {"InputStartingPosition": str},
    total=False,
)


class ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputStartingPositionConfigurationTypeDef(
    _ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputStartingPositionConfigurationTypeDef
):
    """
    Type definition for `ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptions` `InputStartingPositionConfiguration`

    The point at which the application is configured to read from the input stream.

    - **InputStartingPosition** *(string) --*

      The starting position on the stream.

      * ``NOW`` - Start reading just after the most recent record in the stream, and
      start at the request timestamp that the customer issued.

      * ``TRIM_HORIZON`` - Start reading at the last untrimmed record in the stream,
      which is the oldest record available in the stream. This option is not available
      for an Amazon Kinesis Data Firehose delivery stream.

      * ``LAST_STOPPED_POINT`` - Resume reading from where the application last stopped
      reading.
    """


_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsKinesisFirehoseInputDescriptionTypeDef = TypedDict(
    "_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsKinesisFirehoseInputDescriptionTypeDef",
    {"ResourceARN": str, "RoleARN": str},
    total=False,
)


class ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsKinesisFirehoseInputDescriptionTypeDef(
    _ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsKinesisFirehoseInputDescriptionTypeDef
):
    """
    Type definition for `ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptions` `KinesisFirehoseInputDescription`

    If a Kinesis Data Firehose delivery stream is configured as a streaming source,
    provides the delivery stream's ARN.

    - **ResourceARN** *(string) --*

      The Amazon Resource Name (ARN) of the delivery stream.

    - **RoleARN** *(string) --*

      The ARN of the IAM role that Kinesis Data Analytics assumes to access the stream.

      .. note::

        Provided for backward compatibility. Applications that are created with the
        current API version have an application-level service execution role rather
        than a resource-level role.
    """


_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsKinesisStreamsInputDescriptionTypeDef = TypedDict(
    "_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsKinesisStreamsInputDescriptionTypeDef",
    {"ResourceARN": str, "RoleARN": str},
    total=False,
)


class ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsKinesisStreamsInputDescriptionTypeDef(
    _ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsKinesisStreamsInputDescriptionTypeDef
):
    """
    Type definition for `ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptions` `KinesisStreamsInputDescription`

    If a Kinesis data stream is configured as a streaming source, provides the Kinesis
    data stream's Amazon Resource Name (ARN).

    - **ResourceARN** *(string) --*

      The Amazon Resource Name (ARN) of the Kinesis data stream.

    - **RoleARN** *(string) --*

      The ARN of the IAM role that Kinesis Data Analytics can assume to access the
      stream.

      .. note::

        Provided for backward compatibility. Applications that are created with the
        current API version have an application-level service execution role rather
        than a resource-level role.
    """


_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsTypeDef = TypedDict(
    "_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsTypeDef",
    {
        "InputId": str,
        "NamePrefix": str,
        "InAppStreamNames": List[str],
        "InputProcessingConfigurationDescription": ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputProcessingConfigurationDescriptionTypeDef,
        "KinesisStreamsInputDescription": ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsKinesisStreamsInputDescriptionTypeDef,
        "KinesisFirehoseInputDescription": ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsKinesisFirehoseInputDescriptionTypeDef,
        "InputSchema": ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputSchemaTypeDef,
        "InputParallelism": ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputParallelismTypeDef,
        "InputStartingPositionConfiguration": ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsInputStartingPositionConfigurationTypeDef,
    },
    total=False,
)


class ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsTypeDef(
    _ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsTypeDef
):
    """
    Type definition for `ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescription` `InputDescriptions`

    Describes the application input configuration for an SQL-based Amazon Kinesis Data
    Analytics application.

    - **InputId** *(string) --*

      The input ID that is associated with the application input. This is the ID that
      Kinesis Data Analytics assigns to each input configuration that you add to your
      application.

    - **NamePrefix** *(string) --*

      The in-application name prefix.

    - **InAppStreamNames** *(list) --*

      Returns the in-application stream names that are mapped to the stream source.

      - *(string) --*

    - **InputProcessingConfigurationDescription** *(dict) --*

      The description of the preprocessor that executes on records in this input before
      the application's code is run.

      - **InputLambdaProcessorDescription** *(dict) --*

        Provides configuration information about the associated
        InputLambdaProcessorDescription

        - **ResourceARN** *(string) --*

          The ARN of the AWS Lambda function that is used to preprocess the records in
          the stream.

          .. note::

            To specify an earlier version of the Lambda function than the latest, include
            the Lambda function version in the Lambda function ARN. For more information
            about Lambda ARNs, see `Example ARNs\\: AWS Lambda
            </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__

        - **RoleARN** *(string) --*

          The ARN of the IAM role that is used to access the AWS Lambda function.

          .. note::

            Provided for backward compatibility. Applications that are created with the
            current API version have an application-level service execution role rather
            than a resource-level role.

    - **KinesisStreamsInputDescription** *(dict) --*

      If a Kinesis data stream is configured as a streaming source, provides the Kinesis
      data stream's Amazon Resource Name (ARN).

      - **ResourceARN** *(string) --*

        The Amazon Resource Name (ARN) of the Kinesis data stream.

      - **RoleARN** *(string) --*

        The ARN of the IAM role that Kinesis Data Analytics can assume to access the
        stream.

        .. note::

          Provided for backward compatibility. Applications that are created with the
          current API version have an application-level service execution role rather
          than a resource-level role.

    - **KinesisFirehoseInputDescription** *(dict) --*

      If a Kinesis Data Firehose delivery stream is configured as a streaming source,
      provides the delivery stream's ARN.

      - **ResourceARN** *(string) --*

        The Amazon Resource Name (ARN) of the delivery stream.

      - **RoleARN** *(string) --*

        The ARN of the IAM role that Kinesis Data Analytics assumes to access the stream.

        .. note::

          Provided for backward compatibility. Applications that are created with the
          current API version have an application-level service execution role rather
          than a resource-level role.

    - **InputSchema** *(dict) --*

      Describes the format of the data in the streaming source, and how each data element
      maps to corresponding columns in the in-application stream that is being created.

      - **RecordFormat** *(dict) --*

        Specifies the format of the records on the streaming source.

        - **RecordFormatType** *(string) --*

          The type of record format.

        - **MappingParameters** *(dict) --*

          When you configure application input at the time of creating or updating an
          application, provides additional mapping information specific to the record
          format (such as JSON, CSV, or record fields delimited by some delimiter) on the
          streaming source.

          - **JSONMappingParameters** *(dict) --*

            Provides additional mapping information when JSON is the record format on the
            streaming source.

            - **RecordRowPath** *(string) --*

              The path to the top-level parent that contains the records.

          - **CSVMappingParameters** *(dict) --*

            Provides additional mapping information when the record format uses
            delimiters (for example, CSV).

            - **RecordRowDelimiter** *(string) --*

              The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
              delimiter.

            - **RecordColumnDelimiter** *(string) --*

              The column delimiter. For example, in a CSV format, a comma (",") is the
              typical column delimiter.

      - **RecordEncoding** *(string) --*

        Specifies the encoding of the records in the streaming source. For example, UTF-8.

      - **RecordColumns** *(list) --*

        A list of ``RecordColumn`` objects.

        - *(dict) --*

          For an SQL-based Amazon Kinesis Data Analytics application, describes the
          mapping of each data element in the streaming source to the corresponding
          column in the in-application stream.

          Also used to describe the format of the reference data source.

          - **Name** *(string) --*

            The name of the column that is created in the in-application input stream or
            reference table.

          - **Mapping** *(string) --*

            A reference to the data element in the streaming input or the reference data
            source.

          - **SqlType** *(string) --*

            The type of column created in the in-application input stream or reference
            table.

    - **InputParallelism** *(dict) --*

      Describes the configured parallelism (number of in-application streams mapped to
      the streaming source).

      - **Count** *(integer) --*

        The number of in-application streams to create.

    - **InputStartingPositionConfiguration** *(dict) --*

      The point at which the application is configured to read from the input stream.

      - **InputStartingPosition** *(string) --*

        The starting position on the stream.

        * ``NOW`` - Start reading just after the most recent record in the stream, and
        start at the request timestamp that the customer issued.

        * ``TRIM_HORIZON`` - Start reading at the last untrimmed record in the stream,
        which is the oldest record available in the stream. This option is not available
        for an Amazon Kinesis Data Firehose delivery stream.

        * ``LAST_STOPPED_POINT`` - Resume reading from where the application last stopped
        reading.
    """


_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptionsDestinationSchemaTypeDef = TypedDict(
    "_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptionsDestinationSchemaTypeDef",
    {"RecordFormatType": str},
    total=False,
)


class ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptionsDestinationSchemaTypeDef(
    _ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptionsDestinationSchemaTypeDef
):
    """
    Type definition for `ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptions` `DestinationSchema`

    The data format used for writing data to the destination.

    - **RecordFormatType** *(string) --*

      Specifies the format of the records on the output stream.
    """


_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptionsKinesisFirehoseOutputDescriptionTypeDef = TypedDict(
    "_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptionsKinesisFirehoseOutputDescriptionTypeDef",
    {"ResourceARN": str, "RoleARN": str},
    total=False,
)


class ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptionsKinesisFirehoseOutputDescriptionTypeDef(
    _ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptionsKinesisFirehoseOutputDescriptionTypeDef
):
    """
    Type definition for `ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptions` `KinesisFirehoseOutputDescription`

    Describes the Kinesis Data Firehose delivery stream that is configured as the
    destination where output is written.

    - **ResourceARN** *(string) --*

      The Amazon Resource Name (ARN) of the delivery stream.

    - **RoleARN** *(string) --*

      The ARN of the IAM role that Kinesis Data Analytics can assume to access the
      stream.

      .. note::

        Provided for backward compatibility. Applications that are created with the
        current API version have an application-level service execution role rather
        than a resource-level role.
    """


_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptionsKinesisStreamsOutputDescriptionTypeDef = TypedDict(
    "_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptionsKinesisStreamsOutputDescriptionTypeDef",
    {"ResourceARN": str, "RoleARN": str},
    total=False,
)


class ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptionsKinesisStreamsOutputDescriptionTypeDef(
    _ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptionsKinesisStreamsOutputDescriptionTypeDef
):
    """
    Type definition for `ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptions` `KinesisStreamsOutputDescription`

    Describes the Kinesis data stream that is configured as the destination where
    output is written.

    - **ResourceARN** *(string) --*

      The Amazon Resource Name (ARN) of the Kinesis data stream.

    - **RoleARN** *(string) --*

      The ARN of the IAM role that Kinesis Data Analytics can assume to access the
      stream.

      .. note::

        Provided for backward compatibility. Applications that are created with the
        current API version have an application-level service execution role rather
        than a resource-level role.
    """


_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptionsLambdaOutputDescriptionTypeDef = TypedDict(
    "_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptionsLambdaOutputDescriptionTypeDef",
    {"ResourceARN": str, "RoleARN": str},
    total=False,
)


class ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptionsLambdaOutputDescriptionTypeDef(
    _ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptionsLambdaOutputDescriptionTypeDef
):
    """
    Type definition for `ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptions` `LambdaOutputDescription`

    Describes the Lambda function that is configured as the destination where output is
    written.

    - **ResourceARN** *(string) --*

      The Amazon Resource Name (ARN) of the destination Lambda function.

    - **RoleARN** *(string) --*

      The ARN of the IAM role that Kinesis Data Analytics can assume to write to the
      destination function.

      .. note::

        Provided for backward compatibility. Applications that are created with the
        current API version have an application-level service execution role rather
        than a resource-level role.
    """


_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptionsTypeDef = TypedDict(
    "_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptionsTypeDef",
    {
        "OutputId": str,
        "Name": str,
        "KinesisStreamsOutputDescription": ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptionsKinesisStreamsOutputDescriptionTypeDef,
        "KinesisFirehoseOutputDescription": ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptionsKinesisFirehoseOutputDescriptionTypeDef,
        "LambdaOutputDescription": ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptionsLambdaOutputDescriptionTypeDef,
        "DestinationSchema": ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptionsDestinationSchemaTypeDef,
    },
    total=False,
)


class ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptionsTypeDef(
    _ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptionsTypeDef
):
    """
    Type definition for `ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescription` `OutputDescriptions`

    For an SQL-based Amazon Kinesis Data Analytics application, describes the application
    output configuration, which includes the in-application stream name and the
    destination where the stream data is written. The destination can be a Kinesis data
    stream or a Kinesis Data Firehose delivery stream.

    - **OutputId** *(string) --*

      A unique identifier for the output configuration.

    - **Name** *(string) --*

      The name of the in-application stream that is configured as output.

    - **KinesisStreamsOutputDescription** *(dict) --*

      Describes the Kinesis data stream that is configured as the destination where
      output is written.

      - **ResourceARN** *(string) --*

        The Amazon Resource Name (ARN) of the Kinesis data stream.

      - **RoleARN** *(string) --*

        The ARN of the IAM role that Kinesis Data Analytics can assume to access the
        stream.

        .. note::

          Provided for backward compatibility. Applications that are created with the
          current API version have an application-level service execution role rather
          than a resource-level role.

    - **KinesisFirehoseOutputDescription** *(dict) --*

      Describes the Kinesis Data Firehose delivery stream that is configured as the
      destination where output is written.

      - **ResourceARN** *(string) --*

        The Amazon Resource Name (ARN) of the delivery stream.

      - **RoleARN** *(string) --*

        The ARN of the IAM role that Kinesis Data Analytics can assume to access the
        stream.

        .. note::

          Provided for backward compatibility. Applications that are created with the
          current API version have an application-level service execution role rather
          than a resource-level role.

    - **LambdaOutputDescription** *(dict) --*

      Describes the Lambda function that is configured as the destination where output is
      written.

      - **ResourceARN** *(string) --*

        The Amazon Resource Name (ARN) of the destination Lambda function.

      - **RoleARN** *(string) --*

        The ARN of the IAM role that Kinesis Data Analytics can assume to write to the
        destination function.

        .. note::

          Provided for backward compatibility. Applications that are created with the
          current API version have an application-level service execution role rather
          than a resource-level role.

    - **DestinationSchema** *(dict) --*

      The data format used for writing data to the destination.

      - **RecordFormatType** *(string) --*

        Specifies the format of the records on the output stream.
    """


_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordColumnsTypeDef = TypedDict(
    "_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordColumnsTypeDef",
    {"Name": str, "Mapping": str, "SqlType": str},
    total=False,
)


class ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordColumnsTypeDef(
    _ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordColumnsTypeDef
):
    """
    Type definition for `ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchema` `RecordColumns`

    For an SQL-based Amazon Kinesis Data Analytics application, describes the
    mapping of each data element in the streaming source to the corresponding
    column in the in-application stream.

    Also used to describe the format of the reference data source.

    - **Name** *(string) --*

      The name of the column that is created in the in-application input stream or
      reference table.

    - **Mapping** *(string) --*

      A reference to the data element in the streaming input or the reference data
      source.

    - **SqlType** *(string) --*

      The type of column created in the in-application input stream or reference
      table.
    """


_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef = TypedDict(
    "_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef",
    {"RecordRowDelimiter": str, "RecordColumnDelimiter": str},
    total=False,
)


class ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef(
    _ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef
):
    """
    Type definition for `ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParameters` `CSVMappingParameters`

    Provides additional mapping information when the record format uses
    delimiters (for example, CSV).

    - **RecordRowDelimiter** *(string) --*

      The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
      delimiter.

    - **RecordColumnDelimiter** *(string) --*

      The column delimiter. For example, in a CSV format, a comma (",") is the
      typical column delimiter.
    """


_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef = TypedDict(
    "_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef",
    {"RecordRowPath": str},
    total=False,
)


class ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef(
    _ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef
):
    """
    Type definition for `ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParameters` `JSONMappingParameters`

    Provides additional mapping information when JSON is the record format on the
    streaming source.

    - **RecordRowPath** *(string) --*

      The path to the top-level parent that contains the records.
    """


_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersTypeDef = TypedDict(
    "_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersTypeDef",
    {
        "JSONMappingParameters": ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef,
        "CSVMappingParameters": ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef,
    },
    total=False,
)


class ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersTypeDef(
    _ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersTypeDef
):
    """
    Type definition for `ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordFormat` `MappingParameters`

    When you configure application input at the time of creating or updating an
    application, provides additional mapping information specific to the record
    format (such as JSON, CSV, or record fields delimited by some delimiter) on the
    streaming source.

    - **JSONMappingParameters** *(dict) --*

      Provides additional mapping information when JSON is the record format on the
      streaming source.

      - **RecordRowPath** *(string) --*

        The path to the top-level parent that contains the records.

    - **CSVMappingParameters** *(dict) --*

      Provides additional mapping information when the record format uses
      delimiters (for example, CSV).

      - **RecordRowDelimiter** *(string) --*

        The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
        delimiter.

      - **RecordColumnDelimiter** *(string) --*

        The column delimiter. For example, in a CSV format, a comma (",") is the
        typical column delimiter.
    """


_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordFormatTypeDef = TypedDict(
    "_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordFormatTypeDef",
    {
        "RecordFormatType": str,
        "MappingParameters": ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersTypeDef,
    },
    total=False,
)


class ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordFormatTypeDef(
    _ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordFormatTypeDef
):
    """
    Type definition for `ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchema` `RecordFormat`

    Specifies the format of the records on the streaming source.

    - **RecordFormatType** *(string) --*

      The type of record format.

    - **MappingParameters** *(dict) --*

      When you configure application input at the time of creating or updating an
      application, provides additional mapping information specific to the record
      format (such as JSON, CSV, or record fields delimited by some delimiter) on the
      streaming source.

      - **JSONMappingParameters** *(dict) --*

        Provides additional mapping information when JSON is the record format on the
        streaming source.

        - **RecordRowPath** *(string) --*

          The path to the top-level parent that contains the records.

      - **CSVMappingParameters** *(dict) --*

        Provides additional mapping information when the record format uses
        delimiters (for example, CSV).

        - **RecordRowDelimiter** *(string) --*

          The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
          delimiter.

        - **RecordColumnDelimiter** *(string) --*

          The column delimiter. For example, in a CSV format, a comma (",") is the
          typical column delimiter.
    """


_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaTypeDef = TypedDict(
    "_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaTypeDef",
    {
        "RecordFormat": ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordFormatTypeDef,
        "RecordEncoding": str,
        "RecordColumns": List[
            ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaRecordColumnsTypeDef
        ],
    },
    total=False,
)


class ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaTypeDef(
    _ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaTypeDef
):
    """
    Type definition for `ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptions` `ReferenceSchema`

    Describes the format of the data in the streaming source, and how each data element
    maps to corresponding columns created in the in-application stream.

    - **RecordFormat** *(dict) --*

      Specifies the format of the records on the streaming source.

      - **RecordFormatType** *(string) --*

        The type of record format.

      - **MappingParameters** *(dict) --*

        When you configure application input at the time of creating or updating an
        application, provides additional mapping information specific to the record
        format (such as JSON, CSV, or record fields delimited by some delimiter) on the
        streaming source.

        - **JSONMappingParameters** *(dict) --*

          Provides additional mapping information when JSON is the record format on the
          streaming source.

          - **RecordRowPath** *(string) --*

            The path to the top-level parent that contains the records.

        - **CSVMappingParameters** *(dict) --*

          Provides additional mapping information when the record format uses
          delimiters (for example, CSV).

          - **RecordRowDelimiter** *(string) --*

            The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
            delimiter.

          - **RecordColumnDelimiter** *(string) --*

            The column delimiter. For example, in a CSV format, a comma (",") is the
            typical column delimiter.

    - **RecordEncoding** *(string) --*

      Specifies the encoding of the records in the streaming source. For example, UTF-8.

    - **RecordColumns** *(list) --*

      A list of ``RecordColumn`` objects.

      - *(dict) --*

        For an SQL-based Amazon Kinesis Data Analytics application, describes the
        mapping of each data element in the streaming source to the corresponding
        column in the in-application stream.

        Also used to describe the format of the reference data source.

        - **Name** *(string) --*

          The name of the column that is created in the in-application input stream or
          reference table.

        - **Mapping** *(string) --*

          A reference to the data element in the streaming input or the reference data
          source.

        - **SqlType** *(string) --*

          The type of column created in the in-application input stream or reference
          table.
    """


_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsS3ReferenceDataSourceDescriptionTypeDef = TypedDict(
    "_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsS3ReferenceDataSourceDescriptionTypeDef",
    {"BucketARN": str, "FileKey": str, "ReferenceRoleARN": str},
    total=False,
)


class ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsS3ReferenceDataSourceDescriptionTypeDef(
    _ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsS3ReferenceDataSourceDescriptionTypeDef
):
    """
    Type definition for `ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptions` `S3ReferenceDataSourceDescription`

    Provides the Amazon S3 bucket name, the object key name that contains the reference
    data.

    - **BucketARN** *(string) --*

      The Amazon Resource Name (ARN) of the S3 bucket.

    - **FileKey** *(string) --*

      Amazon S3 object key name.

    - **ReferenceRoleARN** *(string) --*

      The ARN of the IAM role that Kinesis Data Analytics can assume to read the Amazon
      S3 object on your behalf to populate the in-application reference table.

      .. note::

        Provided for backward compatibility. Applications that are created with the
        current API version have an application-level service execution role rather
        than a resource-level role.
    """


_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsTypeDef = TypedDict(
    "_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsTypeDef",
    {
        "ReferenceId": str,
        "TableName": str,
        "S3ReferenceDataSourceDescription": ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsS3ReferenceDataSourceDescriptionTypeDef,
        "ReferenceSchema": ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsReferenceSchemaTypeDef,
    },
    total=False,
)


class ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsTypeDef(
    _ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsTypeDef
):
    """
    Type definition for `ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescription` `ReferenceDataSourceDescriptions`

    For an SQL-based Amazon Kinesis Data Analytics application, describes the reference
    data source configured for an application.

    - **ReferenceId** *(string) --*

      The ID of the reference data source. This is the ID that Kinesis Data Analytics
      assigns when you add the reference data source to your application using the
      CreateApplication or  UpdateApplication operation.

    - **TableName** *(string) --*

      The in-application table name created by the specific reference data source
      configuration.

    - **S3ReferenceDataSourceDescription** *(dict) --*

      Provides the Amazon S3 bucket name, the object key name that contains the reference
      data.

      - **BucketARN** *(string) --*

        The Amazon Resource Name (ARN) of the S3 bucket.

      - **FileKey** *(string) --*

        Amazon S3 object key name.

      - **ReferenceRoleARN** *(string) --*

        The ARN of the IAM role that Kinesis Data Analytics can assume to read the Amazon
        S3 object on your behalf to populate the in-application reference table.

        .. note::

          Provided for backward compatibility. Applications that are created with the
          current API version have an application-level service execution role rather
          than a resource-level role.

    - **ReferenceSchema** *(dict) --*

      Describes the format of the data in the streaming source, and how each data element
      maps to corresponding columns created in the in-application stream.

      - **RecordFormat** *(dict) --*

        Specifies the format of the records on the streaming source.

        - **RecordFormatType** *(string) --*

          The type of record format.

        - **MappingParameters** *(dict) --*

          When you configure application input at the time of creating or updating an
          application, provides additional mapping information specific to the record
          format (such as JSON, CSV, or record fields delimited by some delimiter) on the
          streaming source.

          - **JSONMappingParameters** *(dict) --*

            Provides additional mapping information when JSON is the record format on the
            streaming source.

            - **RecordRowPath** *(string) --*

              The path to the top-level parent that contains the records.

          - **CSVMappingParameters** *(dict) --*

            Provides additional mapping information when the record format uses
            delimiters (for example, CSV).

            - **RecordRowDelimiter** *(string) --*

              The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
              delimiter.

            - **RecordColumnDelimiter** *(string) --*

              The column delimiter. For example, in a CSV format, a comma (",") is the
              typical column delimiter.

      - **RecordEncoding** *(string) --*

        Specifies the encoding of the records in the streaming source. For example, UTF-8.

      - **RecordColumns** *(list) --*

        A list of ``RecordColumn`` objects.

        - *(dict) --*

          For an SQL-based Amazon Kinesis Data Analytics application, describes the
          mapping of each data element in the streaming source to the corresponding
          column in the in-application stream.

          Also used to describe the format of the reference data source.

          - **Name** *(string) --*

            The name of the column that is created in the in-application input stream or
            reference table.

          - **Mapping** *(string) --*

            A reference to the data element in the streaming input or the reference data
            source.

          - **SqlType** *(string) --*

            The type of column created in the in-application input stream or reference
            table.
    """


_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionTypeDef = TypedDict(
    "_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionTypeDef",
    {
        "InputDescriptions": List[
            ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionInputDescriptionsTypeDef
        ],
        "OutputDescriptions": List[
            ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionOutputDescriptionsTypeDef
        ],
        "ReferenceDataSourceDescriptions": List[
            ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionReferenceDataSourceDescriptionsTypeDef
        ],
    },
    total=False,
)


class ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionTypeDef(
    _ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionTypeDef
):
    """
    Type definition for `ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescription` `SqlApplicationConfigurationDescription`

    The details about inputs, outputs, and reference data sources for an SQL-based Kinesis
    Data Analytics application.

    - **InputDescriptions** *(list) --*

      The array of  InputDescription objects describing the input streams used by the
      application.

      - *(dict) --*

        Describes the application input configuration for an SQL-based Amazon Kinesis Data
        Analytics application.

        - **InputId** *(string) --*

          The input ID that is associated with the application input. This is the ID that
          Kinesis Data Analytics assigns to each input configuration that you add to your
          application.

        - **NamePrefix** *(string) --*

          The in-application name prefix.

        - **InAppStreamNames** *(list) --*

          Returns the in-application stream names that are mapped to the stream source.

          - *(string) --*

        - **InputProcessingConfigurationDescription** *(dict) --*

          The description of the preprocessor that executes on records in this input before
          the application's code is run.

          - **InputLambdaProcessorDescription** *(dict) --*

            Provides configuration information about the associated
            InputLambdaProcessorDescription

            - **ResourceARN** *(string) --*

              The ARN of the AWS Lambda function that is used to preprocess the records in
              the stream.

              .. note::

                To specify an earlier version of the Lambda function than the latest, include
                the Lambda function version in the Lambda function ARN. For more information
                about Lambda ARNs, see `Example ARNs\\: AWS Lambda
                </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__

            - **RoleARN** *(string) --*

              The ARN of the IAM role that is used to access the AWS Lambda function.

              .. note::

                Provided for backward compatibility. Applications that are created with the
                current API version have an application-level service execution role rather
                than a resource-level role.

        - **KinesisStreamsInputDescription** *(dict) --*

          If a Kinesis data stream is configured as a streaming source, provides the Kinesis
          data stream's Amazon Resource Name (ARN).

          - **ResourceARN** *(string) --*

            The Amazon Resource Name (ARN) of the Kinesis data stream.

          - **RoleARN** *(string) --*

            The ARN of the IAM role that Kinesis Data Analytics can assume to access the
            stream.

            .. note::

              Provided for backward compatibility. Applications that are created with the
              current API version have an application-level service execution role rather
              than a resource-level role.

        - **KinesisFirehoseInputDescription** *(dict) --*

          If a Kinesis Data Firehose delivery stream is configured as a streaming source,
          provides the delivery stream's ARN.

          - **ResourceARN** *(string) --*

            The Amazon Resource Name (ARN) of the delivery stream.

          - **RoleARN** *(string) --*

            The ARN of the IAM role that Kinesis Data Analytics assumes to access the stream.

            .. note::

              Provided for backward compatibility. Applications that are created with the
              current API version have an application-level service execution role rather
              than a resource-level role.

        - **InputSchema** *(dict) --*

          Describes the format of the data in the streaming source, and how each data element
          maps to corresponding columns in the in-application stream that is being created.

          - **RecordFormat** *(dict) --*

            Specifies the format of the records on the streaming source.

            - **RecordFormatType** *(string) --*

              The type of record format.

            - **MappingParameters** *(dict) --*

              When you configure application input at the time of creating or updating an
              application, provides additional mapping information specific to the record
              format (such as JSON, CSV, or record fields delimited by some delimiter) on the
              streaming source.

              - **JSONMappingParameters** *(dict) --*

                Provides additional mapping information when JSON is the record format on the
                streaming source.

                - **RecordRowPath** *(string) --*

                  The path to the top-level parent that contains the records.

              - **CSVMappingParameters** *(dict) --*

                Provides additional mapping information when the record format uses
                delimiters (for example, CSV).

                - **RecordRowDelimiter** *(string) --*

                  The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
                  delimiter.

                - **RecordColumnDelimiter** *(string) --*

                  The column delimiter. For example, in a CSV format, a comma (",") is the
                  typical column delimiter.

          - **RecordEncoding** *(string) --*

            Specifies the encoding of the records in the streaming source. For example, UTF-8.

          - **RecordColumns** *(list) --*

            A list of ``RecordColumn`` objects.

            - *(dict) --*

              For an SQL-based Amazon Kinesis Data Analytics application, describes the
              mapping of each data element in the streaming source to the corresponding
              column in the in-application stream.

              Also used to describe the format of the reference data source.

              - **Name** *(string) --*

                The name of the column that is created in the in-application input stream or
                reference table.

              - **Mapping** *(string) --*

                A reference to the data element in the streaming input or the reference data
                source.

              - **SqlType** *(string) --*

                The type of column created in the in-application input stream or reference
                table.

        - **InputParallelism** *(dict) --*

          Describes the configured parallelism (number of in-application streams mapped to
          the streaming source).

          - **Count** *(integer) --*

            The number of in-application streams to create.

        - **InputStartingPositionConfiguration** *(dict) --*

          The point at which the application is configured to read from the input stream.

          - **InputStartingPosition** *(string) --*

            The starting position on the stream.

            * ``NOW`` - Start reading just after the most recent record in the stream, and
            start at the request timestamp that the customer issued.

            * ``TRIM_HORIZON`` - Start reading at the last untrimmed record in the stream,
            which is the oldest record available in the stream. This option is not available
            for an Amazon Kinesis Data Firehose delivery stream.

            * ``LAST_STOPPED_POINT`` - Resume reading from where the application last stopped
            reading.

    - **OutputDescriptions** *(list) --*

      The array of  OutputDescription objects describing the destination streams used by the
      application.

      - *(dict) --*

        For an SQL-based Amazon Kinesis Data Analytics application, describes the application
        output configuration, which includes the in-application stream name and the
        destination where the stream data is written. The destination can be a Kinesis data
        stream or a Kinesis Data Firehose delivery stream.

        - **OutputId** *(string) --*

          A unique identifier for the output configuration.

        - **Name** *(string) --*

          The name of the in-application stream that is configured as output.

        - **KinesisStreamsOutputDescription** *(dict) --*

          Describes the Kinesis data stream that is configured as the destination where
          output is written.

          - **ResourceARN** *(string) --*

            The Amazon Resource Name (ARN) of the Kinesis data stream.

          - **RoleARN** *(string) --*

            The ARN of the IAM role that Kinesis Data Analytics can assume to access the
            stream.

            .. note::

              Provided for backward compatibility. Applications that are created with the
              current API version have an application-level service execution role rather
              than a resource-level role.

        - **KinesisFirehoseOutputDescription** *(dict) --*

          Describes the Kinesis Data Firehose delivery stream that is configured as the
          destination where output is written.

          - **ResourceARN** *(string) --*

            The Amazon Resource Name (ARN) of the delivery stream.

          - **RoleARN** *(string) --*

            The ARN of the IAM role that Kinesis Data Analytics can assume to access the
            stream.

            .. note::

              Provided for backward compatibility. Applications that are created with the
              current API version have an application-level service execution role rather
              than a resource-level role.

        - **LambdaOutputDescription** *(dict) --*

          Describes the Lambda function that is configured as the destination where output is
          written.

          - **ResourceARN** *(string) --*

            The Amazon Resource Name (ARN) of the destination Lambda function.

          - **RoleARN** *(string) --*

            The ARN of the IAM role that Kinesis Data Analytics can assume to write to the
            destination function.

            .. note::

              Provided for backward compatibility. Applications that are created with the
              current API version have an application-level service execution role rather
              than a resource-level role.

        - **DestinationSchema** *(dict) --*

          The data format used for writing data to the destination.

          - **RecordFormatType** *(string) --*

            Specifies the format of the records on the output stream.

    - **ReferenceDataSourceDescriptions** *(list) --*

      The array of  ReferenceDataSourceDescription objects describing the reference data
      sources used by the application.

      - *(dict) --*

        For an SQL-based Amazon Kinesis Data Analytics application, describes the reference
        data source configured for an application.

        - **ReferenceId** *(string) --*

          The ID of the reference data source. This is the ID that Kinesis Data Analytics
          assigns when you add the reference data source to your application using the
          CreateApplication or  UpdateApplication operation.

        - **TableName** *(string) --*

          The in-application table name created by the specific reference data source
          configuration.

        - **S3ReferenceDataSourceDescription** *(dict) --*

          Provides the Amazon S3 bucket name, the object key name that contains the reference
          data.

          - **BucketARN** *(string) --*

            The Amazon Resource Name (ARN) of the S3 bucket.

          - **FileKey** *(string) --*

            Amazon S3 object key name.

          - **ReferenceRoleARN** *(string) --*

            The ARN of the IAM role that Kinesis Data Analytics can assume to read the Amazon
            S3 object on your behalf to populate the in-application reference table.

            .. note::

              Provided for backward compatibility. Applications that are created with the
              current API version have an application-level service execution role rather
              than a resource-level role.

        - **ReferenceSchema** *(dict) --*

          Describes the format of the data in the streaming source, and how each data element
          maps to corresponding columns created in the in-application stream.

          - **RecordFormat** *(dict) --*

            Specifies the format of the records on the streaming source.

            - **RecordFormatType** *(string) --*

              The type of record format.

            - **MappingParameters** *(dict) --*

              When you configure application input at the time of creating or updating an
              application, provides additional mapping information specific to the record
              format (such as JSON, CSV, or record fields delimited by some delimiter) on the
              streaming source.

              - **JSONMappingParameters** *(dict) --*

                Provides additional mapping information when JSON is the record format on the
                streaming source.

                - **RecordRowPath** *(string) --*

                  The path to the top-level parent that contains the records.

              - **CSVMappingParameters** *(dict) --*

                Provides additional mapping information when the record format uses
                delimiters (for example, CSV).

                - **RecordRowDelimiter** *(string) --*

                  The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
                  delimiter.

                - **RecordColumnDelimiter** *(string) --*

                  The column delimiter. For example, in a CSV format, a comma (",") is the
                  typical column delimiter.

          - **RecordEncoding** *(string) --*

            Specifies the encoding of the records in the streaming source. For example, UTF-8.

          - **RecordColumns** *(list) --*

            A list of ``RecordColumn`` objects.

            - *(dict) --*

              For an SQL-based Amazon Kinesis Data Analytics application, describes the
              mapping of each data element in the streaming source to the corresponding
              column in the in-application stream.

              Also used to describe the format of the reference data source.

              - **Name** *(string) --*

                The name of the column that is created in the in-application input stream or
                reference table.

              - **Mapping** *(string) --*

                A reference to the data element in the streaming input or the reference data
                source.

              - **SqlType** *(string) --*

                The type of column created in the in-application input stream or reference
                table.
    """


_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionTypeDef = TypedDict(
    "_ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionTypeDef",
    {
        "SqlApplicationConfigurationDescription": ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionSqlApplicationConfigurationDescriptionTypeDef,
        "ApplicationCodeConfigurationDescription": ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionApplicationCodeConfigurationDescriptionTypeDef,
        "RunConfigurationDescription": ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionRunConfigurationDescriptionTypeDef,
        "FlinkApplicationConfigurationDescription": ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionFlinkApplicationConfigurationDescriptionTypeDef,
        "EnvironmentPropertyDescriptions": ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionEnvironmentPropertyDescriptionsTypeDef,
        "ApplicationSnapshotConfigurationDescription": ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionApplicationSnapshotConfigurationDescriptionTypeDef,
    },
    total=False,
)


class ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionTypeDef(
    _ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionTypeDef
):
    """
    Type definition for `ClientUpdateApplicationResponseApplicationDetail` `ApplicationConfigurationDescription`

    Provides details about the application's SQL or Java code and starting parameters.

    - **SqlApplicationConfigurationDescription** *(dict) --*

      The details about inputs, outputs, and reference data sources for an SQL-based Kinesis
      Data Analytics application.

      - **InputDescriptions** *(list) --*

        The array of  InputDescription objects describing the input streams used by the
        application.

        - *(dict) --*

          Describes the application input configuration for an SQL-based Amazon Kinesis Data
          Analytics application.

          - **InputId** *(string) --*

            The input ID that is associated with the application input. This is the ID that
            Kinesis Data Analytics assigns to each input configuration that you add to your
            application.

          - **NamePrefix** *(string) --*

            The in-application name prefix.

          - **InAppStreamNames** *(list) --*

            Returns the in-application stream names that are mapped to the stream source.

            - *(string) --*

          - **InputProcessingConfigurationDescription** *(dict) --*

            The description of the preprocessor that executes on records in this input before
            the application's code is run.

            - **InputLambdaProcessorDescription** *(dict) --*

              Provides configuration information about the associated
              InputLambdaProcessorDescription

              - **ResourceARN** *(string) --*

                The ARN of the AWS Lambda function that is used to preprocess the records in
                the stream.

                .. note::

                  To specify an earlier version of the Lambda function than the latest, include
                  the Lambda function version in the Lambda function ARN. For more information
                  about Lambda ARNs, see `Example ARNs\\: AWS Lambda
                  </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__

              - **RoleARN** *(string) --*

                The ARN of the IAM role that is used to access the AWS Lambda function.

                .. note::

                  Provided for backward compatibility. Applications that are created with the
                  current API version have an application-level service execution role rather
                  than a resource-level role.

          - **KinesisStreamsInputDescription** *(dict) --*

            If a Kinesis data stream is configured as a streaming source, provides the Kinesis
            data stream's Amazon Resource Name (ARN).

            - **ResourceARN** *(string) --*

              The Amazon Resource Name (ARN) of the Kinesis data stream.

            - **RoleARN** *(string) --*

              The ARN of the IAM role that Kinesis Data Analytics can assume to access the
              stream.

              .. note::

                Provided for backward compatibility. Applications that are created with the
                current API version have an application-level service execution role rather
                than a resource-level role.

          - **KinesisFirehoseInputDescription** *(dict) --*

            If a Kinesis Data Firehose delivery stream is configured as a streaming source,
            provides the delivery stream's ARN.

            - **ResourceARN** *(string) --*

              The Amazon Resource Name (ARN) of the delivery stream.

            - **RoleARN** *(string) --*

              The ARN of the IAM role that Kinesis Data Analytics assumes to access the stream.

              .. note::

                Provided for backward compatibility. Applications that are created with the
                current API version have an application-level service execution role rather
                than a resource-level role.

          - **InputSchema** *(dict) --*

            Describes the format of the data in the streaming source, and how each data element
            maps to corresponding columns in the in-application stream that is being created.

            - **RecordFormat** *(dict) --*

              Specifies the format of the records on the streaming source.

              - **RecordFormatType** *(string) --*

                The type of record format.

              - **MappingParameters** *(dict) --*

                When you configure application input at the time of creating or updating an
                application, provides additional mapping information specific to the record
                format (such as JSON, CSV, or record fields delimited by some delimiter) on the
                streaming source.

                - **JSONMappingParameters** *(dict) --*

                  Provides additional mapping information when JSON is the record format on the
                  streaming source.

                  - **RecordRowPath** *(string) --*

                    The path to the top-level parent that contains the records.

                - **CSVMappingParameters** *(dict) --*

                  Provides additional mapping information when the record format uses
                  delimiters (for example, CSV).

                  - **RecordRowDelimiter** *(string) --*

                    The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
                    delimiter.

                  - **RecordColumnDelimiter** *(string) --*

                    The column delimiter. For example, in a CSV format, a comma (",") is the
                    typical column delimiter.

            - **RecordEncoding** *(string) --*

              Specifies the encoding of the records in the streaming source. For example, UTF-8.

            - **RecordColumns** *(list) --*

              A list of ``RecordColumn`` objects.

              - *(dict) --*

                For an SQL-based Amazon Kinesis Data Analytics application, describes the
                mapping of each data element in the streaming source to the corresponding
                column in the in-application stream.

                Also used to describe the format of the reference data source.

                - **Name** *(string) --*

                  The name of the column that is created in the in-application input stream or
                  reference table.

                - **Mapping** *(string) --*

                  A reference to the data element in the streaming input or the reference data
                  source.

                - **SqlType** *(string) --*

                  The type of column created in the in-application input stream or reference
                  table.

          - **InputParallelism** *(dict) --*

            Describes the configured parallelism (number of in-application streams mapped to
            the streaming source).

            - **Count** *(integer) --*

              The number of in-application streams to create.

          - **InputStartingPositionConfiguration** *(dict) --*

            The point at which the application is configured to read from the input stream.

            - **InputStartingPosition** *(string) --*

              The starting position on the stream.

              * ``NOW`` - Start reading just after the most recent record in the stream, and
              start at the request timestamp that the customer issued.

              * ``TRIM_HORIZON`` - Start reading at the last untrimmed record in the stream,
              which is the oldest record available in the stream. This option is not available
              for an Amazon Kinesis Data Firehose delivery stream.

              * ``LAST_STOPPED_POINT`` - Resume reading from where the application last stopped
              reading.

      - **OutputDescriptions** *(list) --*

        The array of  OutputDescription objects describing the destination streams used by the
        application.

        - *(dict) --*

          For an SQL-based Amazon Kinesis Data Analytics application, describes the application
          output configuration, which includes the in-application stream name and the
          destination where the stream data is written. The destination can be a Kinesis data
          stream or a Kinesis Data Firehose delivery stream.

          - **OutputId** *(string) --*

            A unique identifier for the output configuration.

          - **Name** *(string) --*

            The name of the in-application stream that is configured as output.

          - **KinesisStreamsOutputDescription** *(dict) --*

            Describes the Kinesis data stream that is configured as the destination where
            output is written.

            - **ResourceARN** *(string) --*

              The Amazon Resource Name (ARN) of the Kinesis data stream.

            - **RoleARN** *(string) --*

              The ARN of the IAM role that Kinesis Data Analytics can assume to access the
              stream.

              .. note::

                Provided for backward compatibility. Applications that are created with the
                current API version have an application-level service execution role rather
                than a resource-level role.

          - **KinesisFirehoseOutputDescription** *(dict) --*

            Describes the Kinesis Data Firehose delivery stream that is configured as the
            destination where output is written.

            - **ResourceARN** *(string) --*

              The Amazon Resource Name (ARN) of the delivery stream.

            - **RoleARN** *(string) --*

              The ARN of the IAM role that Kinesis Data Analytics can assume to access the
              stream.

              .. note::

                Provided for backward compatibility. Applications that are created with the
                current API version have an application-level service execution role rather
                than a resource-level role.

          - **LambdaOutputDescription** *(dict) --*

            Describes the Lambda function that is configured as the destination where output is
            written.

            - **ResourceARN** *(string) --*

              The Amazon Resource Name (ARN) of the destination Lambda function.

            - **RoleARN** *(string) --*

              The ARN of the IAM role that Kinesis Data Analytics can assume to write to the
              destination function.

              .. note::

                Provided for backward compatibility. Applications that are created with the
                current API version have an application-level service execution role rather
                than a resource-level role.

          - **DestinationSchema** *(dict) --*

            The data format used for writing data to the destination.

            - **RecordFormatType** *(string) --*

              Specifies the format of the records on the output stream.

      - **ReferenceDataSourceDescriptions** *(list) --*

        The array of  ReferenceDataSourceDescription objects describing the reference data
        sources used by the application.

        - *(dict) --*

          For an SQL-based Amazon Kinesis Data Analytics application, describes the reference
          data source configured for an application.

          - **ReferenceId** *(string) --*

            The ID of the reference data source. This is the ID that Kinesis Data Analytics
            assigns when you add the reference data source to your application using the
            CreateApplication or  UpdateApplication operation.

          - **TableName** *(string) --*

            The in-application table name created by the specific reference data source
            configuration.

          - **S3ReferenceDataSourceDescription** *(dict) --*

            Provides the Amazon S3 bucket name, the object key name that contains the reference
            data.

            - **BucketARN** *(string) --*

              The Amazon Resource Name (ARN) of the S3 bucket.

            - **FileKey** *(string) --*

              Amazon S3 object key name.

            - **ReferenceRoleARN** *(string) --*

              The ARN of the IAM role that Kinesis Data Analytics can assume to read the Amazon
              S3 object on your behalf to populate the in-application reference table.

              .. note::

                Provided for backward compatibility. Applications that are created with the
                current API version have an application-level service execution role rather
                than a resource-level role.

          - **ReferenceSchema** *(dict) --*

            Describes the format of the data in the streaming source, and how each data element
            maps to corresponding columns created in the in-application stream.

            - **RecordFormat** *(dict) --*

              Specifies the format of the records on the streaming source.

              - **RecordFormatType** *(string) --*

                The type of record format.

              - **MappingParameters** *(dict) --*

                When you configure application input at the time of creating or updating an
                application, provides additional mapping information specific to the record
                format (such as JSON, CSV, or record fields delimited by some delimiter) on the
                streaming source.

                - **JSONMappingParameters** *(dict) --*

                  Provides additional mapping information when JSON is the record format on the
                  streaming source.

                  - **RecordRowPath** *(string) --*

                    The path to the top-level parent that contains the records.

                - **CSVMappingParameters** *(dict) --*

                  Provides additional mapping information when the record format uses
                  delimiters (for example, CSV).

                  - **RecordRowDelimiter** *(string) --*

                    The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
                    delimiter.

                  - **RecordColumnDelimiter** *(string) --*

                    The column delimiter. For example, in a CSV format, a comma (",") is the
                    typical column delimiter.

            - **RecordEncoding** *(string) --*

              Specifies the encoding of the records in the streaming source. For example, UTF-8.

            - **RecordColumns** *(list) --*

              A list of ``RecordColumn`` objects.

              - *(dict) --*

                For an SQL-based Amazon Kinesis Data Analytics application, describes the
                mapping of each data element in the streaming source to the corresponding
                column in the in-application stream.

                Also used to describe the format of the reference data source.

                - **Name** *(string) --*

                  The name of the column that is created in the in-application input stream or
                  reference table.

                - **Mapping** *(string) --*

                  A reference to the data element in the streaming input or the reference data
                  source.

                - **SqlType** *(string) --*

                  The type of column created in the in-application input stream or reference
                  table.

    - **ApplicationCodeConfigurationDescription** *(dict) --*

      The details about the application code for a Java-based Kinesis Data Analytics
      application.

      - **CodeContentType** *(string) --*

        Specifies whether the code content is in text or zip format.

      - **CodeContentDescription** *(dict) --*

        Describes details about the location and format of the application code.

        - **TextContent** *(string) --*

          The text-format code

        - **CodeMD5** *(string) --*

          The checksum that can be used to validate zip-format code.

        - **CodeSize** *(integer) --*

          The size in bytes of the application code. Can be used to validate zip-format code.

        - **S3ApplicationCodeLocationDescription** *(dict) --*

          The S3 bucket Amazon Resource Name (ARN), file key, and object version of the
          application code stored in Amazon S3.

          - **BucketARN** *(string) --*

            The Amazon Resource Name (ARN) for the S3 bucket containing the application code.

          - **FileKey** *(string) --*

            The file key for the object containing the application code.

          - **ObjectVersion** *(string) --*

            The version of the object containing the application code.

    - **RunConfigurationDescription** *(dict) --*

      The details about the starting properties for a Kinesis Data Analytics application.

      - **ApplicationRestoreConfigurationDescription** *(dict) --*

        Describes the restore behavior of a restarting application.

        - **ApplicationRestoreType** *(string) --*

          Specifies how the application should be restored.

        - **SnapshotName** *(string) --*

          The identifier of an existing snapshot of application state to use to restart an
          application. The application uses this value if ``RESTORE_FROM_CUSTOM_SNAPSHOT`` is
          specified for the ``ApplicationRestoreType`` .

    - **FlinkApplicationConfigurationDescription** *(dict) --*

      The details about a Java-based Kinesis Data Analytics application.

      - **CheckpointConfigurationDescription** *(dict) --*

        Describes an application's checkpointing configuration. Checkpointing is the process of
        persisting application state for fault tolerance.

        - **ConfigurationType** *(string) --*

          Describes whether the application uses the default checkpointing behavior in Kinesis
          Data Analytics.

        - **CheckpointingEnabled** *(boolean) --*

          Describes whether checkpointing is enabled for a Java-based Kinesis Data Analytics
          application.

        - **CheckpointInterval** *(integer) --*

          Describes the interval in milliseconds between checkpoint operations.

        - **MinPauseBetweenCheckpoints** *(integer) --*

          Describes the minimum time in milliseconds after a checkpoint operation completes
          that a new checkpoint operation can start.

      - **MonitoringConfigurationDescription** *(dict) --*

        Describes configuration parameters for Amazon CloudWatch logging for an application.

        - **ConfigurationType** *(string) --*

          Describes whether to use the default CloudWatch logging configuration for an
          application.

        - **MetricsLevel** *(string) --*

          Describes the granularity of the CloudWatch Logs for an application.

        - **LogLevel** *(string) --*

          Describes the verbosity of the CloudWatch Logs for an application.

      - **ParallelismConfigurationDescription** *(dict) --*

        Describes parameters for how an application executes multiple tasks simultaneously.

        - **ConfigurationType** *(string) --*

          Describes whether the application uses the default parallelism for the Kinesis Data
          Analytics service.

        - **Parallelism** *(integer) --*

          Describes the initial number of parallel tasks that a Java-based Kinesis Data
          Analytics application can perform.

        - **ParallelismPerKPU** *(integer) --*

          Describes the number of parallel tasks that a Java-based Kinesis Data Analytics
          application can perform per Kinesis Processing Unit (KPU) used by the application.

        - **CurrentParallelism** *(integer) --*

          Describes the current number of parallel tasks that a Java-based Kinesis Data
          Analytics application can perform.

        - **AutoScalingEnabled** *(boolean) --*

          Describes whether the Kinesis Data Analytics service can increase the parallelism of
          the application in response to increased throughput.

      - **JobPlanDescription** *(string) --*

        The job plan for an application. For more information about the job plan, see `Jobs and
        Scheduling
        <https://ci.apache.org/projects/flink/flink-docs-stable/internals/job_scheduling.html>`__
        in the `Apache Flink Documentation
        <https://ci.apache.org/projects/flink/flink-docs-release-1.6/>`__ . To retrieve the job
        plan for the application, use the  DescribeApplicationRequest$IncludeAdditionalDetails
        parameter of the  DescribeApplication operation.

    - **EnvironmentPropertyDescriptions** *(dict) --*

      Describes execution properties for a Java-based Kinesis Data Analytics application.

      - **PropertyGroupDescriptions** *(list) --*

        Describes the execution property groups.

        - *(dict) --*

          Property key-value pairs passed into a Java-based Kinesis Data Analytics application.

          - **PropertyGroupId** *(string) --*

            Describes the key of an application execution property key-value pair.

          - **PropertyMap** *(dict) --*

            Describes the value of an application execution property key-value pair.

            - *(string) --*

              - *(string) --*

    - **ApplicationSnapshotConfigurationDescription** *(dict) --*

      Describes whether snapshots are enabled for a Java-based Kinesis Data Analytics
      application.

      - **SnapshotsEnabled** *(boolean) --*

        Describes whether snapshots are enabled for a Java-based Kinesis Data Analytics
        application.
    """


_ClientUpdateApplicationResponseApplicationDetailCloudWatchLoggingOptionDescriptionsTypeDef = TypedDict(
    "_ClientUpdateApplicationResponseApplicationDetailCloudWatchLoggingOptionDescriptionsTypeDef",
    {"CloudWatchLoggingOptionId": str, "LogStreamARN": str, "RoleARN": str},
    total=False,
)


class ClientUpdateApplicationResponseApplicationDetailCloudWatchLoggingOptionDescriptionsTypeDef(
    _ClientUpdateApplicationResponseApplicationDetailCloudWatchLoggingOptionDescriptionsTypeDef
):
    """
    Type definition for `ClientUpdateApplicationResponseApplicationDetail` `CloudWatchLoggingOptionDescriptions`

    Describes the Amazon CloudWatch logging option.

    - **CloudWatchLoggingOptionId** *(string) --*

      The ID of the CloudWatch logging option description.

    - **LogStreamARN** *(string) --*

      The Amazon Resource Name (ARN) of the CloudWatch log to receive application messages.

    - **RoleARN** *(string) --*

      The IAM ARN of the role to use to send application messages.

      .. note::

        Provided for backward compatibility. Applications created with the current API
        version have an application-level service execution role rather than a resource-level
        role.
    """


_ClientUpdateApplicationResponseApplicationDetailTypeDef = TypedDict(
    "_ClientUpdateApplicationResponseApplicationDetailTypeDef",
    {
        "ApplicationARN": str,
        "ApplicationDescription": str,
        "ApplicationName": str,
        "RuntimeEnvironment": str,
        "ServiceExecutionRole": str,
        "ApplicationStatus": str,
        "ApplicationVersionId": int,
        "CreateTimestamp": datetime,
        "LastUpdateTimestamp": datetime,
        "ApplicationConfigurationDescription": ClientUpdateApplicationResponseApplicationDetailApplicationConfigurationDescriptionTypeDef,
        "CloudWatchLoggingOptionDescriptions": List[
            ClientUpdateApplicationResponseApplicationDetailCloudWatchLoggingOptionDescriptionsTypeDef
        ],
    },
    total=False,
)


class ClientUpdateApplicationResponseApplicationDetailTypeDef(
    _ClientUpdateApplicationResponseApplicationDetailTypeDef
):
    """
    Type definition for `ClientUpdateApplicationResponse` `ApplicationDetail`

    Describes application updates.

    - **ApplicationARN** *(string) --*

      The ARN of the application.

    - **ApplicationDescription** *(string) --*

      The description of the application.

    - **ApplicationName** *(string) --*

      The name of the application.

    - **RuntimeEnvironment** *(string) --*

      The runtime environment for the application (``SQL-1.0`` or ``FLINK-1_6`` ).

    - **ServiceExecutionRole** *(string) --*

      Specifies the IAM role that the application uses to access external resources.

    - **ApplicationStatus** *(string) --*

      The status of the application.

    - **ApplicationVersionId** *(integer) --*

      Provides the current application version. Kinesis Data Analytics updates the
      ``ApplicationVersionId`` each time you update the application.

    - **CreateTimestamp** *(datetime) --*

      The current timestamp when the application was created.

    - **LastUpdateTimestamp** *(datetime) --*

      The current timestamp when the application was last updated.

    - **ApplicationConfigurationDescription** *(dict) --*

      Provides details about the application's SQL or Java code and starting parameters.

      - **SqlApplicationConfigurationDescription** *(dict) --*

        The details about inputs, outputs, and reference data sources for an SQL-based Kinesis
        Data Analytics application.

        - **InputDescriptions** *(list) --*

          The array of  InputDescription objects describing the input streams used by the
          application.

          - *(dict) --*

            Describes the application input configuration for an SQL-based Amazon Kinesis Data
            Analytics application.

            - **InputId** *(string) --*

              The input ID that is associated with the application input. This is the ID that
              Kinesis Data Analytics assigns to each input configuration that you add to your
              application.

            - **NamePrefix** *(string) --*

              The in-application name prefix.

            - **InAppStreamNames** *(list) --*

              Returns the in-application stream names that are mapped to the stream source.

              - *(string) --*

            - **InputProcessingConfigurationDescription** *(dict) --*

              The description of the preprocessor that executes on records in this input before
              the application's code is run.

              - **InputLambdaProcessorDescription** *(dict) --*

                Provides configuration information about the associated
                InputLambdaProcessorDescription

                - **ResourceARN** *(string) --*

                  The ARN of the AWS Lambda function that is used to preprocess the records in
                  the stream.

                  .. note::

                    To specify an earlier version of the Lambda function than the latest, include
                    the Lambda function version in the Lambda function ARN. For more information
                    about Lambda ARNs, see `Example ARNs\\: AWS Lambda
                    </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__

                - **RoleARN** *(string) --*

                  The ARN of the IAM role that is used to access the AWS Lambda function.

                  .. note::

                    Provided for backward compatibility. Applications that are created with the
                    current API version have an application-level service execution role rather
                    than a resource-level role.

            - **KinesisStreamsInputDescription** *(dict) --*

              If a Kinesis data stream is configured as a streaming source, provides the Kinesis
              data stream's Amazon Resource Name (ARN).

              - **ResourceARN** *(string) --*

                The Amazon Resource Name (ARN) of the Kinesis data stream.

              - **RoleARN** *(string) --*

                The ARN of the IAM role that Kinesis Data Analytics can assume to access the
                stream.

                .. note::

                  Provided for backward compatibility. Applications that are created with the
                  current API version have an application-level service execution role rather
                  than a resource-level role.

            - **KinesisFirehoseInputDescription** *(dict) --*

              If a Kinesis Data Firehose delivery stream is configured as a streaming source,
              provides the delivery stream's ARN.

              - **ResourceARN** *(string) --*

                The Amazon Resource Name (ARN) of the delivery stream.

              - **RoleARN** *(string) --*

                The ARN of the IAM role that Kinesis Data Analytics assumes to access the stream.

                .. note::

                  Provided for backward compatibility. Applications that are created with the
                  current API version have an application-level service execution role rather
                  than a resource-level role.

            - **InputSchema** *(dict) --*

              Describes the format of the data in the streaming source, and how each data element
              maps to corresponding columns in the in-application stream that is being created.

              - **RecordFormat** *(dict) --*

                Specifies the format of the records on the streaming source.

                - **RecordFormatType** *(string) --*

                  The type of record format.

                - **MappingParameters** *(dict) --*

                  When you configure application input at the time of creating or updating an
                  application, provides additional mapping information specific to the record
                  format (such as JSON, CSV, or record fields delimited by some delimiter) on the
                  streaming source.

                  - **JSONMappingParameters** *(dict) --*

                    Provides additional mapping information when JSON is the record format on the
                    streaming source.

                    - **RecordRowPath** *(string) --*

                      The path to the top-level parent that contains the records.

                  - **CSVMappingParameters** *(dict) --*

                    Provides additional mapping information when the record format uses
                    delimiters (for example, CSV).

                    - **RecordRowDelimiter** *(string) --*

                      The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
                      delimiter.

                    - **RecordColumnDelimiter** *(string) --*

                      The column delimiter. For example, in a CSV format, a comma (",") is the
                      typical column delimiter.

              - **RecordEncoding** *(string) --*

                Specifies the encoding of the records in the streaming source. For example, UTF-8.

              - **RecordColumns** *(list) --*

                A list of ``RecordColumn`` objects.

                - *(dict) --*

                  For an SQL-based Amazon Kinesis Data Analytics application, describes the
                  mapping of each data element in the streaming source to the corresponding
                  column in the in-application stream.

                  Also used to describe the format of the reference data source.

                  - **Name** *(string) --*

                    The name of the column that is created in the in-application input stream or
                    reference table.

                  - **Mapping** *(string) --*

                    A reference to the data element in the streaming input or the reference data
                    source.

                  - **SqlType** *(string) --*

                    The type of column created in the in-application input stream or reference
                    table.

            - **InputParallelism** *(dict) --*

              Describes the configured parallelism (number of in-application streams mapped to
              the streaming source).

              - **Count** *(integer) --*

                The number of in-application streams to create.

            - **InputStartingPositionConfiguration** *(dict) --*

              The point at which the application is configured to read from the input stream.

              - **InputStartingPosition** *(string) --*

                The starting position on the stream.

                * ``NOW`` - Start reading just after the most recent record in the stream, and
                start at the request timestamp that the customer issued.

                * ``TRIM_HORIZON`` - Start reading at the last untrimmed record in the stream,
                which is the oldest record available in the stream. This option is not available
                for an Amazon Kinesis Data Firehose delivery stream.

                * ``LAST_STOPPED_POINT`` - Resume reading from where the application last stopped
                reading.

        - **OutputDescriptions** *(list) --*

          The array of  OutputDescription objects describing the destination streams used by the
          application.

          - *(dict) --*

            For an SQL-based Amazon Kinesis Data Analytics application, describes the application
            output configuration, which includes the in-application stream name and the
            destination where the stream data is written. The destination can be a Kinesis data
            stream or a Kinesis Data Firehose delivery stream.

            - **OutputId** *(string) --*

              A unique identifier for the output configuration.

            - **Name** *(string) --*

              The name of the in-application stream that is configured as output.

            - **KinesisStreamsOutputDescription** *(dict) --*

              Describes the Kinesis data stream that is configured as the destination where
              output is written.

              - **ResourceARN** *(string) --*

                The Amazon Resource Name (ARN) of the Kinesis data stream.

              - **RoleARN** *(string) --*

                The ARN of the IAM role that Kinesis Data Analytics can assume to access the
                stream.

                .. note::

                  Provided for backward compatibility. Applications that are created with the
                  current API version have an application-level service execution role rather
                  than a resource-level role.

            - **KinesisFirehoseOutputDescription** *(dict) --*

              Describes the Kinesis Data Firehose delivery stream that is configured as the
              destination where output is written.

              - **ResourceARN** *(string) --*

                The Amazon Resource Name (ARN) of the delivery stream.

              - **RoleARN** *(string) --*

                The ARN of the IAM role that Kinesis Data Analytics can assume to access the
                stream.

                .. note::

                  Provided for backward compatibility. Applications that are created with the
                  current API version have an application-level service execution role rather
                  than a resource-level role.

            - **LambdaOutputDescription** *(dict) --*

              Describes the Lambda function that is configured as the destination where output is
              written.

              - **ResourceARN** *(string) --*

                The Amazon Resource Name (ARN) of the destination Lambda function.

              - **RoleARN** *(string) --*

                The ARN of the IAM role that Kinesis Data Analytics can assume to write to the
                destination function.

                .. note::

                  Provided for backward compatibility. Applications that are created with the
                  current API version have an application-level service execution role rather
                  than a resource-level role.

            - **DestinationSchema** *(dict) --*

              The data format used for writing data to the destination.

              - **RecordFormatType** *(string) --*

                Specifies the format of the records on the output stream.

        - **ReferenceDataSourceDescriptions** *(list) --*

          The array of  ReferenceDataSourceDescription objects describing the reference data
          sources used by the application.

          - *(dict) --*

            For an SQL-based Amazon Kinesis Data Analytics application, describes the reference
            data source configured for an application.

            - **ReferenceId** *(string) --*

              The ID of the reference data source. This is the ID that Kinesis Data Analytics
              assigns when you add the reference data source to your application using the
              CreateApplication or  UpdateApplication operation.

            - **TableName** *(string) --*

              The in-application table name created by the specific reference data source
              configuration.

            - **S3ReferenceDataSourceDescription** *(dict) --*

              Provides the Amazon S3 bucket name, the object key name that contains the reference
              data.

              - **BucketARN** *(string) --*

                The Amazon Resource Name (ARN) of the S3 bucket.

              - **FileKey** *(string) --*

                Amazon S3 object key name.

              - **ReferenceRoleARN** *(string) --*

                The ARN of the IAM role that Kinesis Data Analytics can assume to read the Amazon
                S3 object on your behalf to populate the in-application reference table.

                .. note::

                  Provided for backward compatibility. Applications that are created with the
                  current API version have an application-level service execution role rather
                  than a resource-level role.

            - **ReferenceSchema** *(dict) --*

              Describes the format of the data in the streaming source, and how each data element
              maps to corresponding columns created in the in-application stream.

              - **RecordFormat** *(dict) --*

                Specifies the format of the records on the streaming source.

                - **RecordFormatType** *(string) --*

                  The type of record format.

                - **MappingParameters** *(dict) --*

                  When you configure application input at the time of creating or updating an
                  application, provides additional mapping information specific to the record
                  format (such as JSON, CSV, or record fields delimited by some delimiter) on the
                  streaming source.

                  - **JSONMappingParameters** *(dict) --*

                    Provides additional mapping information when JSON is the record format on the
                    streaming source.

                    - **RecordRowPath** *(string) --*

                      The path to the top-level parent that contains the records.

                  - **CSVMappingParameters** *(dict) --*

                    Provides additional mapping information when the record format uses
                    delimiters (for example, CSV).

                    - **RecordRowDelimiter** *(string) --*

                      The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
                      delimiter.

                    - **RecordColumnDelimiter** *(string) --*

                      The column delimiter. For example, in a CSV format, a comma (",") is the
                      typical column delimiter.

              - **RecordEncoding** *(string) --*

                Specifies the encoding of the records in the streaming source. For example, UTF-8.

              - **RecordColumns** *(list) --*

                A list of ``RecordColumn`` objects.

                - *(dict) --*

                  For an SQL-based Amazon Kinesis Data Analytics application, describes the
                  mapping of each data element in the streaming source to the corresponding
                  column in the in-application stream.

                  Also used to describe the format of the reference data source.

                  - **Name** *(string) --*

                    The name of the column that is created in the in-application input stream or
                    reference table.

                  - **Mapping** *(string) --*

                    A reference to the data element in the streaming input or the reference data
                    source.

                  - **SqlType** *(string) --*

                    The type of column created in the in-application input stream or reference
                    table.

      - **ApplicationCodeConfigurationDescription** *(dict) --*

        The details about the application code for a Java-based Kinesis Data Analytics
        application.

        - **CodeContentType** *(string) --*

          Specifies whether the code content is in text or zip format.

        - **CodeContentDescription** *(dict) --*

          Describes details about the location and format of the application code.

          - **TextContent** *(string) --*

            The text-format code

          - **CodeMD5** *(string) --*

            The checksum that can be used to validate zip-format code.

          - **CodeSize** *(integer) --*

            The size in bytes of the application code. Can be used to validate zip-format code.

          - **S3ApplicationCodeLocationDescription** *(dict) --*

            The S3 bucket Amazon Resource Name (ARN), file key, and object version of the
            application code stored in Amazon S3.

            - **BucketARN** *(string) --*

              The Amazon Resource Name (ARN) for the S3 bucket containing the application code.

            - **FileKey** *(string) --*

              The file key for the object containing the application code.

            - **ObjectVersion** *(string) --*

              The version of the object containing the application code.

      - **RunConfigurationDescription** *(dict) --*

        The details about the starting properties for a Kinesis Data Analytics application.

        - **ApplicationRestoreConfigurationDescription** *(dict) --*

          Describes the restore behavior of a restarting application.

          - **ApplicationRestoreType** *(string) --*

            Specifies how the application should be restored.

          - **SnapshotName** *(string) --*

            The identifier of an existing snapshot of application state to use to restart an
            application. The application uses this value if ``RESTORE_FROM_CUSTOM_SNAPSHOT`` is
            specified for the ``ApplicationRestoreType`` .

      - **FlinkApplicationConfigurationDescription** *(dict) --*

        The details about a Java-based Kinesis Data Analytics application.

        - **CheckpointConfigurationDescription** *(dict) --*

          Describes an application's checkpointing configuration. Checkpointing is the process of
          persisting application state for fault tolerance.

          - **ConfigurationType** *(string) --*

            Describes whether the application uses the default checkpointing behavior in Kinesis
            Data Analytics.

          - **CheckpointingEnabled** *(boolean) --*

            Describes whether checkpointing is enabled for a Java-based Kinesis Data Analytics
            application.

          - **CheckpointInterval** *(integer) --*

            Describes the interval in milliseconds between checkpoint operations.

          - **MinPauseBetweenCheckpoints** *(integer) --*

            Describes the minimum time in milliseconds after a checkpoint operation completes
            that a new checkpoint operation can start.

        - **MonitoringConfigurationDescription** *(dict) --*

          Describes configuration parameters for Amazon CloudWatch logging for an application.

          - **ConfigurationType** *(string) --*

            Describes whether to use the default CloudWatch logging configuration for an
            application.

          - **MetricsLevel** *(string) --*

            Describes the granularity of the CloudWatch Logs for an application.

          - **LogLevel** *(string) --*

            Describes the verbosity of the CloudWatch Logs for an application.

        - **ParallelismConfigurationDescription** *(dict) --*

          Describes parameters for how an application executes multiple tasks simultaneously.

          - **ConfigurationType** *(string) --*

            Describes whether the application uses the default parallelism for the Kinesis Data
            Analytics service.

          - **Parallelism** *(integer) --*

            Describes the initial number of parallel tasks that a Java-based Kinesis Data
            Analytics application can perform.

          - **ParallelismPerKPU** *(integer) --*

            Describes the number of parallel tasks that a Java-based Kinesis Data Analytics
            application can perform per Kinesis Processing Unit (KPU) used by the application.

          - **CurrentParallelism** *(integer) --*

            Describes the current number of parallel tasks that a Java-based Kinesis Data
            Analytics application can perform.

          - **AutoScalingEnabled** *(boolean) --*

            Describes whether the Kinesis Data Analytics service can increase the parallelism of
            the application in response to increased throughput.

        - **JobPlanDescription** *(string) --*

          The job plan for an application. For more information about the job plan, see `Jobs and
          Scheduling
          <https://ci.apache.org/projects/flink/flink-docs-stable/internals/job_scheduling.html>`__
          in the `Apache Flink Documentation
          <https://ci.apache.org/projects/flink/flink-docs-release-1.6/>`__ . To retrieve the job
          plan for the application, use the  DescribeApplicationRequest$IncludeAdditionalDetails
          parameter of the  DescribeApplication operation.

      - **EnvironmentPropertyDescriptions** *(dict) --*

        Describes execution properties for a Java-based Kinesis Data Analytics application.

        - **PropertyGroupDescriptions** *(list) --*

          Describes the execution property groups.

          - *(dict) --*

            Property key-value pairs passed into a Java-based Kinesis Data Analytics application.

            - **PropertyGroupId** *(string) --*

              Describes the key of an application execution property key-value pair.

            - **PropertyMap** *(dict) --*

              Describes the value of an application execution property key-value pair.

              - *(string) --*

                - *(string) --*

      - **ApplicationSnapshotConfigurationDescription** *(dict) --*

        Describes whether snapshots are enabled for a Java-based Kinesis Data Analytics
        application.

        - **SnapshotsEnabled** *(boolean) --*

          Describes whether snapshots are enabled for a Java-based Kinesis Data Analytics
          application.

    - **CloudWatchLoggingOptionDescriptions** *(list) --*

      Describes the application Amazon CloudWatch logging options.

      - *(dict) --*

        Describes the Amazon CloudWatch logging option.

        - **CloudWatchLoggingOptionId** *(string) --*

          The ID of the CloudWatch logging option description.

        - **LogStreamARN** *(string) --*

          The Amazon Resource Name (ARN) of the CloudWatch log to receive application messages.

        - **RoleARN** *(string) --*

          The IAM ARN of the role to use to send application messages.

          .. note::

            Provided for backward compatibility. Applications created with the current API
            version have an application-level service execution role rather than a resource-level
            role.
    """


_ClientUpdateApplicationResponseTypeDef = TypedDict(
    "_ClientUpdateApplicationResponseTypeDef",
    {"ApplicationDetail": ClientUpdateApplicationResponseApplicationDetailTypeDef},
    total=False,
)


class ClientUpdateApplicationResponseTypeDef(_ClientUpdateApplicationResponseTypeDef):
    """
    Type definition for `ClientUpdateApplication` `Response`

    - **ApplicationDetail** *(dict) --*

      Describes application updates.

      - **ApplicationARN** *(string) --*

        The ARN of the application.

      - **ApplicationDescription** *(string) --*

        The description of the application.

      - **ApplicationName** *(string) --*

        The name of the application.

      - **RuntimeEnvironment** *(string) --*

        The runtime environment for the application (``SQL-1.0`` or ``FLINK-1_6`` ).

      - **ServiceExecutionRole** *(string) --*

        Specifies the IAM role that the application uses to access external resources.

      - **ApplicationStatus** *(string) --*

        The status of the application.

      - **ApplicationVersionId** *(integer) --*

        Provides the current application version. Kinesis Data Analytics updates the
        ``ApplicationVersionId`` each time you update the application.

      - **CreateTimestamp** *(datetime) --*

        The current timestamp when the application was created.

      - **LastUpdateTimestamp** *(datetime) --*

        The current timestamp when the application was last updated.

      - **ApplicationConfigurationDescription** *(dict) --*

        Provides details about the application's SQL or Java code and starting parameters.

        - **SqlApplicationConfigurationDescription** *(dict) --*

          The details about inputs, outputs, and reference data sources for an SQL-based Kinesis
          Data Analytics application.

          - **InputDescriptions** *(list) --*

            The array of  InputDescription objects describing the input streams used by the
            application.

            - *(dict) --*

              Describes the application input configuration for an SQL-based Amazon Kinesis Data
              Analytics application.

              - **InputId** *(string) --*

                The input ID that is associated with the application input. This is the ID that
                Kinesis Data Analytics assigns to each input configuration that you add to your
                application.

              - **NamePrefix** *(string) --*

                The in-application name prefix.

              - **InAppStreamNames** *(list) --*

                Returns the in-application stream names that are mapped to the stream source.

                - *(string) --*

              - **InputProcessingConfigurationDescription** *(dict) --*

                The description of the preprocessor that executes on records in this input before
                the application's code is run.

                - **InputLambdaProcessorDescription** *(dict) --*

                  Provides configuration information about the associated
                  InputLambdaProcessorDescription

                  - **ResourceARN** *(string) --*

                    The ARN of the AWS Lambda function that is used to preprocess the records in
                    the stream.

                    .. note::

                      To specify an earlier version of the Lambda function than the latest, include
                      the Lambda function version in the Lambda function ARN. For more information
                      about Lambda ARNs, see `Example ARNs\\: AWS Lambda
                      </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__

                  - **RoleARN** *(string) --*

                    The ARN of the IAM role that is used to access the AWS Lambda function.

                    .. note::

                      Provided for backward compatibility. Applications that are created with the
                      current API version have an application-level service execution role rather
                      than a resource-level role.

              - **KinesisStreamsInputDescription** *(dict) --*

                If a Kinesis data stream is configured as a streaming source, provides the Kinesis
                data stream's Amazon Resource Name (ARN).

                - **ResourceARN** *(string) --*

                  The Amazon Resource Name (ARN) of the Kinesis data stream.

                - **RoleARN** *(string) --*

                  The ARN of the IAM role that Kinesis Data Analytics can assume to access the
                  stream.

                  .. note::

                    Provided for backward compatibility. Applications that are created with the
                    current API version have an application-level service execution role rather
                    than a resource-level role.

              - **KinesisFirehoseInputDescription** *(dict) --*

                If a Kinesis Data Firehose delivery stream is configured as a streaming source,
                provides the delivery stream's ARN.

                - **ResourceARN** *(string) --*

                  The Amazon Resource Name (ARN) of the delivery stream.

                - **RoleARN** *(string) --*

                  The ARN of the IAM role that Kinesis Data Analytics assumes to access the stream.

                  .. note::

                    Provided for backward compatibility. Applications that are created with the
                    current API version have an application-level service execution role rather
                    than a resource-level role.

              - **InputSchema** *(dict) --*

                Describes the format of the data in the streaming source, and how each data element
                maps to corresponding columns in the in-application stream that is being created.

                - **RecordFormat** *(dict) --*

                  Specifies the format of the records on the streaming source.

                  - **RecordFormatType** *(string) --*

                    The type of record format.

                  - **MappingParameters** *(dict) --*

                    When you configure application input at the time of creating or updating an
                    application, provides additional mapping information specific to the record
                    format (such as JSON, CSV, or record fields delimited by some delimiter) on the
                    streaming source.

                    - **JSONMappingParameters** *(dict) --*

                      Provides additional mapping information when JSON is the record format on the
                      streaming source.

                      - **RecordRowPath** *(string) --*

                        The path to the top-level parent that contains the records.

                    - **CSVMappingParameters** *(dict) --*

                      Provides additional mapping information when the record format uses
                      delimiters (for example, CSV).

                      - **RecordRowDelimiter** *(string) --*

                        The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
                        delimiter.

                      - **RecordColumnDelimiter** *(string) --*

                        The column delimiter. For example, in a CSV format, a comma (",") is the
                        typical column delimiter.

                - **RecordEncoding** *(string) --*

                  Specifies the encoding of the records in the streaming source. For example, UTF-8.

                - **RecordColumns** *(list) --*

                  A list of ``RecordColumn`` objects.

                  - *(dict) --*

                    For an SQL-based Amazon Kinesis Data Analytics application, describes the
                    mapping of each data element in the streaming source to the corresponding
                    column in the in-application stream.

                    Also used to describe the format of the reference data source.

                    - **Name** *(string) --*

                      The name of the column that is created in the in-application input stream or
                      reference table.

                    - **Mapping** *(string) --*

                      A reference to the data element in the streaming input or the reference data
                      source.

                    - **SqlType** *(string) --*

                      The type of column created in the in-application input stream or reference
                      table.

              - **InputParallelism** *(dict) --*

                Describes the configured parallelism (number of in-application streams mapped to
                the streaming source).

                - **Count** *(integer) --*

                  The number of in-application streams to create.

              - **InputStartingPositionConfiguration** *(dict) --*

                The point at which the application is configured to read from the input stream.

                - **InputStartingPosition** *(string) --*

                  The starting position on the stream.

                  * ``NOW`` - Start reading just after the most recent record in the stream, and
                  start at the request timestamp that the customer issued.

                  * ``TRIM_HORIZON`` - Start reading at the last untrimmed record in the stream,
                  which is the oldest record available in the stream. This option is not available
                  for an Amazon Kinesis Data Firehose delivery stream.

                  * ``LAST_STOPPED_POINT`` - Resume reading from where the application last stopped
                  reading.

          - **OutputDescriptions** *(list) --*

            The array of  OutputDescription objects describing the destination streams used by the
            application.

            - *(dict) --*

              For an SQL-based Amazon Kinesis Data Analytics application, describes the application
              output configuration, which includes the in-application stream name and the
              destination where the stream data is written. The destination can be a Kinesis data
              stream or a Kinesis Data Firehose delivery stream.

              - **OutputId** *(string) --*

                A unique identifier for the output configuration.

              - **Name** *(string) --*

                The name of the in-application stream that is configured as output.

              - **KinesisStreamsOutputDescription** *(dict) --*

                Describes the Kinesis data stream that is configured as the destination where
                output is written.

                - **ResourceARN** *(string) --*

                  The Amazon Resource Name (ARN) of the Kinesis data stream.

                - **RoleARN** *(string) --*

                  The ARN of the IAM role that Kinesis Data Analytics can assume to access the
                  stream.

                  .. note::

                    Provided for backward compatibility. Applications that are created with the
                    current API version have an application-level service execution role rather
                    than a resource-level role.

              - **KinesisFirehoseOutputDescription** *(dict) --*

                Describes the Kinesis Data Firehose delivery stream that is configured as the
                destination where output is written.

                - **ResourceARN** *(string) --*

                  The Amazon Resource Name (ARN) of the delivery stream.

                - **RoleARN** *(string) --*

                  The ARN of the IAM role that Kinesis Data Analytics can assume to access the
                  stream.

                  .. note::

                    Provided for backward compatibility. Applications that are created with the
                    current API version have an application-level service execution role rather
                    than a resource-level role.

              - **LambdaOutputDescription** *(dict) --*

                Describes the Lambda function that is configured as the destination where output is
                written.

                - **ResourceARN** *(string) --*

                  The Amazon Resource Name (ARN) of the destination Lambda function.

                - **RoleARN** *(string) --*

                  The ARN of the IAM role that Kinesis Data Analytics can assume to write to the
                  destination function.

                  .. note::

                    Provided for backward compatibility. Applications that are created with the
                    current API version have an application-level service execution role rather
                    than a resource-level role.

              - **DestinationSchema** *(dict) --*

                The data format used for writing data to the destination.

                - **RecordFormatType** *(string) --*

                  Specifies the format of the records on the output stream.

          - **ReferenceDataSourceDescriptions** *(list) --*

            The array of  ReferenceDataSourceDescription objects describing the reference data
            sources used by the application.

            - *(dict) --*

              For an SQL-based Amazon Kinesis Data Analytics application, describes the reference
              data source configured for an application.

              - **ReferenceId** *(string) --*

                The ID of the reference data source. This is the ID that Kinesis Data Analytics
                assigns when you add the reference data source to your application using the
                CreateApplication or  UpdateApplication operation.

              - **TableName** *(string) --*

                The in-application table name created by the specific reference data source
                configuration.

              - **S3ReferenceDataSourceDescription** *(dict) --*

                Provides the Amazon S3 bucket name, the object key name that contains the reference
                data.

                - **BucketARN** *(string) --*

                  The Amazon Resource Name (ARN) of the S3 bucket.

                - **FileKey** *(string) --*

                  Amazon S3 object key name.

                - **ReferenceRoleARN** *(string) --*

                  The ARN of the IAM role that Kinesis Data Analytics can assume to read the Amazon
                  S3 object on your behalf to populate the in-application reference table.

                  .. note::

                    Provided for backward compatibility. Applications that are created with the
                    current API version have an application-level service execution role rather
                    than a resource-level role.

              - **ReferenceSchema** *(dict) --*

                Describes the format of the data in the streaming source, and how each data element
                maps to corresponding columns created in the in-application stream.

                - **RecordFormat** *(dict) --*

                  Specifies the format of the records on the streaming source.

                  - **RecordFormatType** *(string) --*

                    The type of record format.

                  - **MappingParameters** *(dict) --*

                    When you configure application input at the time of creating or updating an
                    application, provides additional mapping information specific to the record
                    format (such as JSON, CSV, or record fields delimited by some delimiter) on the
                    streaming source.

                    - **JSONMappingParameters** *(dict) --*

                      Provides additional mapping information when JSON is the record format on the
                      streaming source.

                      - **RecordRowPath** *(string) --*

                        The path to the top-level parent that contains the records.

                    - **CSVMappingParameters** *(dict) --*

                      Provides additional mapping information when the record format uses
                      delimiters (for example, CSV).

                      - **RecordRowDelimiter** *(string) --*

                        The row delimiter. For example, in a CSV format, *'\\n'* is the typical row
                        delimiter.

                      - **RecordColumnDelimiter** *(string) --*

                        The column delimiter. For example, in a CSV format, a comma (",") is the
                        typical column delimiter.

                - **RecordEncoding** *(string) --*

                  Specifies the encoding of the records in the streaming source. For example, UTF-8.

                - **RecordColumns** *(list) --*

                  A list of ``RecordColumn`` objects.

                  - *(dict) --*

                    For an SQL-based Amazon Kinesis Data Analytics application, describes the
                    mapping of each data element in the streaming source to the corresponding
                    column in the in-application stream.

                    Also used to describe the format of the reference data source.

                    - **Name** *(string) --*

                      The name of the column that is created in the in-application input stream or
                      reference table.

                    - **Mapping** *(string) --*

                      A reference to the data element in the streaming input or the reference data
                      source.

                    - **SqlType** *(string) --*

                      The type of column created in the in-application input stream or reference
                      table.

        - **ApplicationCodeConfigurationDescription** *(dict) --*

          The details about the application code for a Java-based Kinesis Data Analytics
          application.

          - **CodeContentType** *(string) --*

            Specifies whether the code content is in text or zip format.

          - **CodeContentDescription** *(dict) --*

            Describes details about the location and format of the application code.

            - **TextContent** *(string) --*

              The text-format code

            - **CodeMD5** *(string) --*

              The checksum that can be used to validate zip-format code.

            - **CodeSize** *(integer) --*

              The size in bytes of the application code. Can be used to validate zip-format code.

            - **S3ApplicationCodeLocationDescription** *(dict) --*

              The S3 bucket Amazon Resource Name (ARN), file key, and object version of the
              application code stored in Amazon S3.

              - **BucketARN** *(string) --*

                The Amazon Resource Name (ARN) for the S3 bucket containing the application code.

              - **FileKey** *(string) --*

                The file key for the object containing the application code.

              - **ObjectVersion** *(string) --*

                The version of the object containing the application code.

        - **RunConfigurationDescription** *(dict) --*

          The details about the starting properties for a Kinesis Data Analytics application.

          - **ApplicationRestoreConfigurationDescription** *(dict) --*

            Describes the restore behavior of a restarting application.

            - **ApplicationRestoreType** *(string) --*

              Specifies how the application should be restored.

            - **SnapshotName** *(string) --*

              The identifier of an existing snapshot of application state to use to restart an
              application. The application uses this value if ``RESTORE_FROM_CUSTOM_SNAPSHOT`` is
              specified for the ``ApplicationRestoreType`` .

        - **FlinkApplicationConfigurationDescription** *(dict) --*

          The details about a Java-based Kinesis Data Analytics application.

          - **CheckpointConfigurationDescription** *(dict) --*

            Describes an application's checkpointing configuration. Checkpointing is the process of
            persisting application state for fault tolerance.

            - **ConfigurationType** *(string) --*

              Describes whether the application uses the default checkpointing behavior in Kinesis
              Data Analytics.

            - **CheckpointingEnabled** *(boolean) --*

              Describes whether checkpointing is enabled for a Java-based Kinesis Data Analytics
              application.

            - **CheckpointInterval** *(integer) --*

              Describes the interval in milliseconds between checkpoint operations.

            - **MinPauseBetweenCheckpoints** *(integer) --*

              Describes the minimum time in milliseconds after a checkpoint operation completes
              that a new checkpoint operation can start.

          - **MonitoringConfigurationDescription** *(dict) --*

            Describes configuration parameters for Amazon CloudWatch logging for an application.

            - **ConfigurationType** *(string) --*

              Describes whether to use the default CloudWatch logging configuration for an
              application.

            - **MetricsLevel** *(string) --*

              Describes the granularity of the CloudWatch Logs for an application.

            - **LogLevel** *(string) --*

              Describes the verbosity of the CloudWatch Logs for an application.

          - **ParallelismConfigurationDescription** *(dict) --*

            Describes parameters for how an application executes multiple tasks simultaneously.

            - **ConfigurationType** *(string) --*

              Describes whether the application uses the default parallelism for the Kinesis Data
              Analytics service.

            - **Parallelism** *(integer) --*

              Describes the initial number of parallel tasks that a Java-based Kinesis Data
              Analytics application can perform.

            - **ParallelismPerKPU** *(integer) --*

              Describes the number of parallel tasks that a Java-based Kinesis Data Analytics
              application can perform per Kinesis Processing Unit (KPU) used by the application.

            - **CurrentParallelism** *(integer) --*

              Describes the current number of parallel tasks that a Java-based Kinesis Data
              Analytics application can perform.

            - **AutoScalingEnabled** *(boolean) --*

              Describes whether the Kinesis Data Analytics service can increase the parallelism of
              the application in response to increased throughput.

          - **JobPlanDescription** *(string) --*

            The job plan for an application. For more information about the job plan, see `Jobs and
            Scheduling
            <https://ci.apache.org/projects/flink/flink-docs-stable/internals/job_scheduling.html>`__
            in the `Apache Flink Documentation
            <https://ci.apache.org/projects/flink/flink-docs-release-1.6/>`__ . To retrieve the job
            plan for the application, use the  DescribeApplicationRequest$IncludeAdditionalDetails
            parameter of the  DescribeApplication operation.

        - **EnvironmentPropertyDescriptions** *(dict) --*

          Describes execution properties for a Java-based Kinesis Data Analytics application.

          - **PropertyGroupDescriptions** *(list) --*

            Describes the execution property groups.

            - *(dict) --*

              Property key-value pairs passed into a Java-based Kinesis Data Analytics application.

              - **PropertyGroupId** *(string) --*

                Describes the key of an application execution property key-value pair.

              - **PropertyMap** *(dict) --*

                Describes the value of an application execution property key-value pair.

                - *(string) --*

                  - *(string) --*

        - **ApplicationSnapshotConfigurationDescription** *(dict) --*

          Describes whether snapshots are enabled for a Java-based Kinesis Data Analytics
          application.

          - **SnapshotsEnabled** *(boolean) --*

            Describes whether snapshots are enabled for a Java-based Kinesis Data Analytics
            application.

      - **CloudWatchLoggingOptionDescriptions** *(list) --*

        Describes the application Amazon CloudWatch logging options.

        - *(dict) --*

          Describes the Amazon CloudWatch logging option.

          - **CloudWatchLoggingOptionId** *(string) --*

            The ID of the CloudWatch logging option description.

          - **LogStreamARN** *(string) --*

            The Amazon Resource Name (ARN) of the CloudWatch log to receive application messages.

          - **RoleARN** *(string) --*

            The IAM ARN of the role to use to send application messages.

            .. note::

              Provided for backward compatibility. Applications created with the current API
              version have an application-level service execution role rather than a resource-level
              role.
    """


_RequiredClientUpdateApplicationRunConfigurationUpdateApplicationRestoreConfigurationTypeDef = TypedDict(
    "_RequiredClientUpdateApplicationRunConfigurationUpdateApplicationRestoreConfigurationTypeDef",
    {"ApplicationRestoreType": str},
)
_OptionalClientUpdateApplicationRunConfigurationUpdateApplicationRestoreConfigurationTypeDef = TypedDict(
    "_OptionalClientUpdateApplicationRunConfigurationUpdateApplicationRestoreConfigurationTypeDef",
    {"SnapshotName": str},
    total=False,
)


class ClientUpdateApplicationRunConfigurationUpdateApplicationRestoreConfigurationTypeDef(
    _RequiredClientUpdateApplicationRunConfigurationUpdateApplicationRestoreConfigurationTypeDef,
    _OptionalClientUpdateApplicationRunConfigurationUpdateApplicationRestoreConfigurationTypeDef,
):
    """
    Type definition for `ClientUpdateApplicationRunConfigurationUpdate` `ApplicationRestoreConfiguration`

    Describes updates to the restore behavior of a restarting application.

    - **ApplicationRestoreType** *(string) --* **[REQUIRED]**

      Specifies how the application should be restored.

    - **SnapshotName** *(string) --*

      The identifier of an existing snapshot of application state to use to restart an application.
      The application uses this value if ``RESTORE_FROM_CUSTOM_SNAPSHOT`` is specified for the
      ``ApplicationRestoreType`` .
    """


_ClientUpdateApplicationRunConfigurationUpdateTypeDef = TypedDict(
    "_ClientUpdateApplicationRunConfigurationUpdateTypeDef",
    {
        "ApplicationRestoreConfiguration": ClientUpdateApplicationRunConfigurationUpdateApplicationRestoreConfigurationTypeDef
    },
    total=False,
)


class ClientUpdateApplicationRunConfigurationUpdateTypeDef(
    _ClientUpdateApplicationRunConfigurationUpdateTypeDef
):
    """
    Type definition for `ClientUpdateApplication` `RunConfigurationUpdate`

    Describes updates to the application's starting parameters.

    - **ApplicationRestoreConfiguration** *(dict) --*

      Describes updates to the restore behavior of a restarting application.

      - **ApplicationRestoreType** *(string) --* **[REQUIRED]**

        Specifies how the application should be restored.

      - **SnapshotName** *(string) --*

        The identifier of an existing snapshot of application state to use to restart an application.
        The application uses this value if ``RESTORE_FROM_CUSTOM_SNAPSHOT`` is specified for the
        ``ApplicationRestoreType`` .
    """


_ListApplicationSnapshotsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListApplicationSnapshotsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListApplicationSnapshotsPaginatePaginationConfigTypeDef(
    _ListApplicationSnapshotsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListApplicationSnapshotsPaginate` `PaginationConfig`

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


_ListApplicationSnapshotsPaginateResponseSnapshotSummariesTypeDef = TypedDict(
    "_ListApplicationSnapshotsPaginateResponseSnapshotSummariesTypeDef",
    {
        "SnapshotName": str,
        "SnapshotStatus": str,
        "ApplicationVersionId": int,
        "SnapshotCreationTimestamp": datetime,
    },
    total=False,
)


class ListApplicationSnapshotsPaginateResponseSnapshotSummariesTypeDef(
    _ListApplicationSnapshotsPaginateResponseSnapshotSummariesTypeDef
):
    """
    Type definition for `ListApplicationSnapshotsPaginateResponse` `SnapshotSummaries`

    Provides details about a snapshot of application state.

    - **SnapshotName** *(string) --*

      The identifier for the application snapshot.

    - **SnapshotStatus** *(string) --*

      The status of the application snapshot.

    - **ApplicationVersionId** *(integer) --*

      The current application version ID when the snapshot was created.

    - **SnapshotCreationTimestamp** *(datetime) --*

      The timestamp of the application snapshot.
    """


_ListApplicationSnapshotsPaginateResponseTypeDef = TypedDict(
    "_ListApplicationSnapshotsPaginateResponseTypeDef",
    {
        "SnapshotSummaries": List[
            ListApplicationSnapshotsPaginateResponseSnapshotSummariesTypeDef
        ]
    },
    total=False,
)


class ListApplicationSnapshotsPaginateResponseTypeDef(
    _ListApplicationSnapshotsPaginateResponseTypeDef
):
    """
    Type definition for `ListApplicationSnapshotsPaginate` `Response`

    - **SnapshotSummaries** *(list) --*

      A collection of objects containing information about the application snapshots.

      - *(dict) --*

        Provides details about a snapshot of application state.

        - **SnapshotName** *(string) --*

          The identifier for the application snapshot.

        - **SnapshotStatus** *(string) --*

          The status of the application snapshot.

        - **ApplicationVersionId** *(integer) --*

          The current application version ID when the snapshot was created.

        - **SnapshotCreationTimestamp** *(datetime) --*

          The timestamp of the application snapshot.
    """


_ListApplicationsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListApplicationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListApplicationsPaginatePaginationConfigTypeDef(
    _ListApplicationsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListApplicationsPaginate` `PaginationConfig`

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


_ListApplicationsPaginateResponseApplicationSummariesTypeDef = TypedDict(
    "_ListApplicationsPaginateResponseApplicationSummariesTypeDef",
    {
        "ApplicationName": str,
        "ApplicationARN": str,
        "ApplicationStatus": str,
        "ApplicationVersionId": int,
        "RuntimeEnvironment": str,
    },
    total=False,
)


class ListApplicationsPaginateResponseApplicationSummariesTypeDef(
    _ListApplicationsPaginateResponseApplicationSummariesTypeDef
):
    """
    Type definition for `ListApplicationsPaginateResponse` `ApplicationSummaries`

    Provides application summary information, including the application Amazon Resource Name
    (ARN), name, and status.

    - **ApplicationName** *(string) --*

      The name of the application.

    - **ApplicationARN** *(string) --*

      The ARN of the application.

    - **ApplicationStatus** *(string) --*

      The status of the application.

    - **ApplicationVersionId** *(integer) --*

      Provides the current application version.

    - **RuntimeEnvironment** *(string) --*

      The runtime environment for the application (``SQL-1.0`` or ``FLINK-1_6`` ).
    """


_ListApplicationsPaginateResponseTypeDef = TypedDict(
    "_ListApplicationsPaginateResponseTypeDef",
    {
        "ApplicationSummaries": List[
            ListApplicationsPaginateResponseApplicationSummariesTypeDef
        ]
    },
    total=False,
)


class ListApplicationsPaginateResponseTypeDef(_ListApplicationsPaginateResponseTypeDef):
    """
    Type definition for `ListApplicationsPaginate` `Response`

    - **ApplicationSummaries** *(list) --*

      A list of ``ApplicationSummary`` objects.

      - *(dict) --*

        Provides application summary information, including the application Amazon Resource Name
        (ARN), name, and status.

        - **ApplicationName** *(string) --*

          The name of the application.

        - **ApplicationARN** *(string) --*

          The ARN of the application.

        - **ApplicationStatus** *(string) --*

          The status of the application.

        - **ApplicationVersionId** *(integer) --*

          Provides the current application version.

        - **RuntimeEnvironment** *(string) --*

          The runtime environment for the application (``SQL-1.0`` or ``FLINK-1_6`` ).
    """
