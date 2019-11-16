"Main interface for firehose type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientCreateDeliveryStreamElasticsearchDestinationConfigurationBufferingHintsTypeDef",
    "ClientCreateDeliveryStreamElasticsearchDestinationConfigurationCloudWatchLoggingOptionsTypeDef",
    "ClientCreateDeliveryStreamElasticsearchDestinationConfigurationProcessingConfigurationProcessorsParametersTypeDef",
    "ClientCreateDeliveryStreamElasticsearchDestinationConfigurationProcessingConfigurationProcessorsTypeDef",
    "ClientCreateDeliveryStreamElasticsearchDestinationConfigurationProcessingConfigurationTypeDef",
    "ClientCreateDeliveryStreamElasticsearchDestinationConfigurationRetryOptionsTypeDef",
    "ClientCreateDeliveryStreamElasticsearchDestinationConfigurationS3ConfigurationBufferingHintsTypeDef",
    "ClientCreateDeliveryStreamElasticsearchDestinationConfigurationS3ConfigurationCloudWatchLoggingOptionsTypeDef",
    "ClientCreateDeliveryStreamElasticsearchDestinationConfigurationS3ConfigurationEncryptionConfigurationKMSEncryptionConfigTypeDef",
    "ClientCreateDeliveryStreamElasticsearchDestinationConfigurationS3ConfigurationEncryptionConfigurationTypeDef",
    "ClientCreateDeliveryStreamElasticsearchDestinationConfigurationS3ConfigurationTypeDef",
    "ClientCreateDeliveryStreamElasticsearchDestinationConfigurationTypeDef",
    "ClientCreateDeliveryStreamExtendedS3DestinationConfigurationBufferingHintsTypeDef",
    "ClientCreateDeliveryStreamExtendedS3DestinationConfigurationCloudWatchLoggingOptionsTypeDef",
    "ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDeTypeDef",
    "ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDeTypeDef",
    "ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerTypeDef",
    "ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationInputFormatConfigurationTypeDef",
    "ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDeTypeDef",
    "ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDeTypeDef",
    "ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerTypeDef",
    "ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationOutputFormatConfigurationTypeDef",
    "ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationSchemaConfigurationTypeDef",
    "ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationTypeDef",
    "ClientCreateDeliveryStreamExtendedS3DestinationConfigurationEncryptionConfigurationKMSEncryptionConfigTypeDef",
    "ClientCreateDeliveryStreamExtendedS3DestinationConfigurationEncryptionConfigurationTypeDef",
    "ClientCreateDeliveryStreamExtendedS3DestinationConfigurationProcessingConfigurationProcessorsParametersTypeDef",
    "ClientCreateDeliveryStreamExtendedS3DestinationConfigurationProcessingConfigurationProcessorsTypeDef",
    "ClientCreateDeliveryStreamExtendedS3DestinationConfigurationProcessingConfigurationTypeDef",
    "ClientCreateDeliveryStreamExtendedS3DestinationConfigurationS3BackupConfigurationBufferingHintsTypeDef",
    "ClientCreateDeliveryStreamExtendedS3DestinationConfigurationS3BackupConfigurationCloudWatchLoggingOptionsTypeDef",
    "ClientCreateDeliveryStreamExtendedS3DestinationConfigurationS3BackupConfigurationEncryptionConfigurationKMSEncryptionConfigTypeDef",
    "ClientCreateDeliveryStreamExtendedS3DestinationConfigurationS3BackupConfigurationEncryptionConfigurationTypeDef",
    "ClientCreateDeliveryStreamExtendedS3DestinationConfigurationS3BackupConfigurationTypeDef",
    "ClientCreateDeliveryStreamExtendedS3DestinationConfigurationTypeDef",
    "ClientCreateDeliveryStreamKinesisStreamSourceConfigurationTypeDef",
    "ClientCreateDeliveryStreamRedshiftDestinationConfigurationCloudWatchLoggingOptionsTypeDef",
    "ClientCreateDeliveryStreamRedshiftDestinationConfigurationCopyCommandTypeDef",
    "ClientCreateDeliveryStreamRedshiftDestinationConfigurationProcessingConfigurationProcessorsParametersTypeDef",
    "ClientCreateDeliveryStreamRedshiftDestinationConfigurationProcessingConfigurationProcessorsTypeDef",
    "ClientCreateDeliveryStreamRedshiftDestinationConfigurationProcessingConfigurationTypeDef",
    "ClientCreateDeliveryStreamRedshiftDestinationConfigurationRetryOptionsTypeDef",
    "ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3BackupConfigurationBufferingHintsTypeDef",
    "ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3BackupConfigurationCloudWatchLoggingOptionsTypeDef",
    "ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3BackupConfigurationEncryptionConfigurationKMSEncryptionConfigTypeDef",
    "ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3BackupConfigurationEncryptionConfigurationTypeDef",
    "ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3BackupConfigurationTypeDef",
    "ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3ConfigurationBufferingHintsTypeDef",
    "ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3ConfigurationCloudWatchLoggingOptionsTypeDef",
    "ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3ConfigurationEncryptionConfigurationKMSEncryptionConfigTypeDef",
    "ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3ConfigurationEncryptionConfigurationTypeDef",
    "ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3ConfigurationTypeDef",
    "ClientCreateDeliveryStreamRedshiftDestinationConfigurationTypeDef",
    "ClientCreateDeliveryStreamResponseTypeDef",
    "ClientCreateDeliveryStreamS3DestinationConfigurationBufferingHintsTypeDef",
    "ClientCreateDeliveryStreamS3DestinationConfigurationCloudWatchLoggingOptionsTypeDef",
    "ClientCreateDeliveryStreamS3DestinationConfigurationEncryptionConfigurationKMSEncryptionConfigTypeDef",
    "ClientCreateDeliveryStreamS3DestinationConfigurationEncryptionConfigurationTypeDef",
    "ClientCreateDeliveryStreamS3DestinationConfigurationTypeDef",
    "ClientCreateDeliveryStreamSplunkDestinationConfigurationCloudWatchLoggingOptionsTypeDef",
    "ClientCreateDeliveryStreamSplunkDestinationConfigurationProcessingConfigurationProcessorsParametersTypeDef",
    "ClientCreateDeliveryStreamSplunkDestinationConfigurationProcessingConfigurationProcessorsTypeDef",
    "ClientCreateDeliveryStreamSplunkDestinationConfigurationProcessingConfigurationTypeDef",
    "ClientCreateDeliveryStreamSplunkDestinationConfigurationRetryOptionsTypeDef",
    "ClientCreateDeliveryStreamSplunkDestinationConfigurationS3ConfigurationBufferingHintsTypeDef",
    "ClientCreateDeliveryStreamSplunkDestinationConfigurationS3ConfigurationCloudWatchLoggingOptionsTypeDef",
    "ClientCreateDeliveryStreamSplunkDestinationConfigurationS3ConfigurationEncryptionConfigurationKMSEncryptionConfigTypeDef",
    "ClientCreateDeliveryStreamSplunkDestinationConfigurationS3ConfigurationEncryptionConfigurationTypeDef",
    "ClientCreateDeliveryStreamSplunkDestinationConfigurationS3ConfigurationTypeDef",
    "ClientCreateDeliveryStreamSplunkDestinationConfigurationTypeDef",
    "ClientCreateDeliveryStreamTagsTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDeliveryStreamEncryptionConfigurationTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionBufferingHintsTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionCloudWatchLoggingOptionsTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionProcessingConfigurationProcessorsParametersTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionProcessingConfigurationProcessorsTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionProcessingConfigurationTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionRetryOptionsTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionS3DestinationDescriptionBufferingHintsTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionS3DestinationDescriptionCloudWatchLoggingOptionsTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionS3DestinationDescriptionEncryptionConfigurationKMSEncryptionConfigTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionS3DestinationDescriptionEncryptionConfigurationTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionS3DestinationDescriptionTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionBufferingHintsTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionCloudWatchLoggingOptionsTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDeTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDeTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationInputFormatConfigurationDeserializerTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationInputFormatConfigurationTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDeTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDeTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationOutputFormatConfigurationSerializerTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationOutputFormatConfigurationTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationSchemaConfigurationTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionEncryptionConfigurationKMSEncryptionConfigTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionEncryptionConfigurationTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionProcessingConfigurationProcessorsParametersTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionProcessingConfigurationProcessorsTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionProcessingConfigurationTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionS3BackupDescriptionBufferingHintsTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionS3BackupDescriptionCloudWatchLoggingOptionsTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionS3BackupDescriptionEncryptionConfigurationKMSEncryptionConfigTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionS3BackupDescriptionEncryptionConfigurationTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionS3BackupDescriptionTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionCloudWatchLoggingOptionsTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionCopyCommandTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionProcessingConfigurationProcessorsParametersTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionProcessingConfigurationProcessorsTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionProcessingConfigurationTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionRetryOptionsTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3BackupDescriptionBufferingHintsTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3BackupDescriptionCloudWatchLoggingOptionsTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3BackupDescriptionEncryptionConfigurationKMSEncryptionConfigTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3BackupDescriptionEncryptionConfigurationTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3BackupDescriptionTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3DestinationDescriptionBufferingHintsTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3DestinationDescriptionCloudWatchLoggingOptionsTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3DestinationDescriptionEncryptionConfigurationKMSEncryptionConfigTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3DestinationDescriptionEncryptionConfigurationTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3DestinationDescriptionTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsS3DestinationDescriptionBufferingHintsTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsS3DestinationDescriptionCloudWatchLoggingOptionsTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsS3DestinationDescriptionEncryptionConfigurationKMSEncryptionConfigTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsS3DestinationDescriptionEncryptionConfigurationTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsS3DestinationDescriptionTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionCloudWatchLoggingOptionsTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionProcessingConfigurationProcessorsParametersTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionProcessingConfigurationProcessorsTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionProcessingConfigurationTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionRetryOptionsTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionS3DestinationDescriptionBufferingHintsTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionS3DestinationDescriptionCloudWatchLoggingOptionsTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionS3DestinationDescriptionEncryptionConfigurationKMSEncryptionConfigTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionS3DestinationDescriptionEncryptionConfigurationTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionS3DestinationDescriptionTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionSourceKinesisStreamSourceDescriptionTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionSourceTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionTypeDef",
    "ClientDescribeDeliveryStreamResponseTypeDef",
    "ClientListDeliveryStreamsResponseTypeDef",
    "ClientListTagsForDeliveryStreamResponseTagsTypeDef",
    "ClientListTagsForDeliveryStreamResponseTypeDef",
    "ClientPutRecordBatchRecordsTypeDef",
    "ClientPutRecordBatchResponseRequestResponsesTypeDef",
    "ClientPutRecordBatchResponseTypeDef",
    "ClientPutRecordRecordTypeDef",
    "ClientPutRecordResponseTypeDef",
    "ClientTagDeliveryStreamTagsTypeDef",
    "ClientUpdateDestinationElasticsearchDestinationUpdateBufferingHintsTypeDef",
    "ClientUpdateDestinationElasticsearchDestinationUpdateCloudWatchLoggingOptionsTypeDef",
    "ClientUpdateDestinationElasticsearchDestinationUpdateProcessingConfigurationProcessorsParametersTypeDef",
    "ClientUpdateDestinationElasticsearchDestinationUpdateProcessingConfigurationProcessorsTypeDef",
    "ClientUpdateDestinationElasticsearchDestinationUpdateProcessingConfigurationTypeDef",
    "ClientUpdateDestinationElasticsearchDestinationUpdateRetryOptionsTypeDef",
    "ClientUpdateDestinationElasticsearchDestinationUpdateS3UpdateBufferingHintsTypeDef",
    "ClientUpdateDestinationElasticsearchDestinationUpdateS3UpdateCloudWatchLoggingOptionsTypeDef",
    "ClientUpdateDestinationElasticsearchDestinationUpdateS3UpdateEncryptionConfigurationKMSEncryptionConfigTypeDef",
    "ClientUpdateDestinationElasticsearchDestinationUpdateS3UpdateEncryptionConfigurationTypeDef",
    "ClientUpdateDestinationElasticsearchDestinationUpdateS3UpdateTypeDef",
    "ClientUpdateDestinationElasticsearchDestinationUpdateTypeDef",
    "ClientUpdateDestinationExtendedS3DestinationUpdateBufferingHintsTypeDef",
    "ClientUpdateDestinationExtendedS3DestinationUpdateCloudWatchLoggingOptionsTypeDef",
    "ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDeTypeDef",
    "ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDeTypeDef",
    "ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationInputFormatConfigurationDeserializerTypeDef",
    "ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationInputFormatConfigurationTypeDef",
    "ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDeTypeDef",
    "ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDeTypeDef",
    "ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationOutputFormatConfigurationSerializerTypeDef",
    "ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationOutputFormatConfigurationTypeDef",
    "ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationSchemaConfigurationTypeDef",
    "ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationTypeDef",
    "ClientUpdateDestinationExtendedS3DestinationUpdateEncryptionConfigurationKMSEncryptionConfigTypeDef",
    "ClientUpdateDestinationExtendedS3DestinationUpdateEncryptionConfigurationTypeDef",
    "ClientUpdateDestinationExtendedS3DestinationUpdateProcessingConfigurationProcessorsParametersTypeDef",
    "ClientUpdateDestinationExtendedS3DestinationUpdateProcessingConfigurationProcessorsTypeDef",
    "ClientUpdateDestinationExtendedS3DestinationUpdateProcessingConfigurationTypeDef",
    "ClientUpdateDestinationExtendedS3DestinationUpdateS3BackupUpdateBufferingHintsTypeDef",
    "ClientUpdateDestinationExtendedS3DestinationUpdateS3BackupUpdateCloudWatchLoggingOptionsTypeDef",
    "ClientUpdateDestinationExtendedS3DestinationUpdateS3BackupUpdateEncryptionConfigurationKMSEncryptionConfigTypeDef",
    "ClientUpdateDestinationExtendedS3DestinationUpdateS3BackupUpdateEncryptionConfigurationTypeDef",
    "ClientUpdateDestinationExtendedS3DestinationUpdateS3BackupUpdateTypeDef",
    "ClientUpdateDestinationExtendedS3DestinationUpdateTypeDef",
    "ClientUpdateDestinationRedshiftDestinationUpdateCloudWatchLoggingOptionsTypeDef",
    "ClientUpdateDestinationRedshiftDestinationUpdateCopyCommandTypeDef",
    "ClientUpdateDestinationRedshiftDestinationUpdateProcessingConfigurationProcessorsParametersTypeDef",
    "ClientUpdateDestinationRedshiftDestinationUpdateProcessingConfigurationProcessorsTypeDef",
    "ClientUpdateDestinationRedshiftDestinationUpdateProcessingConfigurationTypeDef",
    "ClientUpdateDestinationRedshiftDestinationUpdateRetryOptionsTypeDef",
    "ClientUpdateDestinationRedshiftDestinationUpdateS3BackupUpdateBufferingHintsTypeDef",
    "ClientUpdateDestinationRedshiftDestinationUpdateS3BackupUpdateCloudWatchLoggingOptionsTypeDef",
    "ClientUpdateDestinationRedshiftDestinationUpdateS3BackupUpdateEncryptionConfigurationKMSEncryptionConfigTypeDef",
    "ClientUpdateDestinationRedshiftDestinationUpdateS3BackupUpdateEncryptionConfigurationTypeDef",
    "ClientUpdateDestinationRedshiftDestinationUpdateS3BackupUpdateTypeDef",
    "ClientUpdateDestinationRedshiftDestinationUpdateS3UpdateBufferingHintsTypeDef",
    "ClientUpdateDestinationRedshiftDestinationUpdateS3UpdateCloudWatchLoggingOptionsTypeDef",
    "ClientUpdateDestinationRedshiftDestinationUpdateS3UpdateEncryptionConfigurationKMSEncryptionConfigTypeDef",
    "ClientUpdateDestinationRedshiftDestinationUpdateS3UpdateEncryptionConfigurationTypeDef",
    "ClientUpdateDestinationRedshiftDestinationUpdateS3UpdateTypeDef",
    "ClientUpdateDestinationRedshiftDestinationUpdateTypeDef",
    "ClientUpdateDestinationS3DestinationUpdateBufferingHintsTypeDef",
    "ClientUpdateDestinationS3DestinationUpdateCloudWatchLoggingOptionsTypeDef",
    "ClientUpdateDestinationS3DestinationUpdateEncryptionConfigurationKMSEncryptionConfigTypeDef",
    "ClientUpdateDestinationS3DestinationUpdateEncryptionConfigurationTypeDef",
    "ClientUpdateDestinationS3DestinationUpdateTypeDef",
    "ClientUpdateDestinationSplunkDestinationUpdateCloudWatchLoggingOptionsTypeDef",
    "ClientUpdateDestinationSplunkDestinationUpdateProcessingConfigurationProcessorsParametersTypeDef",
    "ClientUpdateDestinationSplunkDestinationUpdateProcessingConfigurationProcessorsTypeDef",
    "ClientUpdateDestinationSplunkDestinationUpdateProcessingConfigurationTypeDef",
    "ClientUpdateDestinationSplunkDestinationUpdateRetryOptionsTypeDef",
    "ClientUpdateDestinationSplunkDestinationUpdateS3UpdateBufferingHintsTypeDef",
    "ClientUpdateDestinationSplunkDestinationUpdateS3UpdateCloudWatchLoggingOptionsTypeDef",
    "ClientUpdateDestinationSplunkDestinationUpdateS3UpdateEncryptionConfigurationKMSEncryptionConfigTypeDef",
    "ClientUpdateDestinationSplunkDestinationUpdateS3UpdateEncryptionConfigurationTypeDef",
    "ClientUpdateDestinationSplunkDestinationUpdateS3UpdateTypeDef",
    "ClientUpdateDestinationSplunkDestinationUpdateTypeDef",
)


_ClientCreateDeliveryStreamElasticsearchDestinationConfigurationBufferingHintsTypeDef = TypedDict(
    "_ClientCreateDeliveryStreamElasticsearchDestinationConfigurationBufferingHintsTypeDef",
    {"IntervalInSeconds": int, "SizeInMBs": int},
    total=False,
)


class ClientCreateDeliveryStreamElasticsearchDestinationConfigurationBufferingHintsTypeDef(
    _ClientCreateDeliveryStreamElasticsearchDestinationConfigurationBufferingHintsTypeDef
):
    """
    Type definition for `ClientCreateDeliveryStreamElasticsearchDestinationConfiguration` `BufferingHints`

    The buffering options. If no value is specified, the default values for
    ``ElasticsearchBufferingHints`` are used.

    - **IntervalInSeconds** *(integer) --*

      Buffer incoming data for the specified period of time, in seconds, before delivering it to
      the destination. The default value is 300 (5 minutes).

    - **SizeInMBs** *(integer) --*

      Buffer incoming data to the specified size, in MBs, before delivering it to the destination.
      The default value is 5.

      We recommend setting this parameter to a value greater than the amount of data you typically
      ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1
      MB/sec, the value should be 10 MB or higher.
    """


_ClientCreateDeliveryStreamElasticsearchDestinationConfigurationCloudWatchLoggingOptionsTypeDef = TypedDict(
    "_ClientCreateDeliveryStreamElasticsearchDestinationConfigurationCloudWatchLoggingOptionsTypeDef",
    {"Enabled": bool, "LogGroupName": str, "LogStreamName": str},
    total=False,
)


class ClientCreateDeliveryStreamElasticsearchDestinationConfigurationCloudWatchLoggingOptionsTypeDef(
    _ClientCreateDeliveryStreamElasticsearchDestinationConfigurationCloudWatchLoggingOptionsTypeDef
):
    """
    Type definition for `ClientCreateDeliveryStreamElasticsearchDestinationConfiguration` `CloudWatchLoggingOptions`

    The Amazon CloudWatch logging options for your delivery stream.

    - **Enabled** *(boolean) --*

      Enables or disables CloudWatch logging.

    - **LogGroupName** *(string) --*

      The CloudWatch group name for logging. This value is required if CloudWatch logging is
      enabled.

    - **LogStreamName** *(string) --*

      The CloudWatch log stream name for logging. This value is required if CloudWatch logging is
      enabled.
    """


_ClientCreateDeliveryStreamElasticsearchDestinationConfigurationProcessingConfigurationProcessorsParametersTypeDef = TypedDict(
    "_ClientCreateDeliveryStreamElasticsearchDestinationConfigurationProcessingConfigurationProcessorsParametersTypeDef",
    {"ParameterName": str, "ParameterValue": str},
)


class ClientCreateDeliveryStreamElasticsearchDestinationConfigurationProcessingConfigurationProcessorsParametersTypeDef(
    _ClientCreateDeliveryStreamElasticsearchDestinationConfigurationProcessingConfigurationProcessorsParametersTypeDef
):
    """
    Type definition for `ClientCreateDeliveryStreamElasticsearchDestinationConfigurationProcessingConfigurationProcessors` `Parameters`

    Describes the processor parameter.

    - **ParameterName** *(string) --* **[REQUIRED]**

      The name of the parameter.

    - **ParameterValue** *(string) --* **[REQUIRED]**

      The parameter value.
    """


_RequiredClientCreateDeliveryStreamElasticsearchDestinationConfigurationProcessingConfigurationProcessorsTypeDef = TypedDict(
    "_RequiredClientCreateDeliveryStreamElasticsearchDestinationConfigurationProcessingConfigurationProcessorsTypeDef",
    {"Type": str},
)
_OptionalClientCreateDeliveryStreamElasticsearchDestinationConfigurationProcessingConfigurationProcessorsTypeDef = TypedDict(
    "_OptionalClientCreateDeliveryStreamElasticsearchDestinationConfigurationProcessingConfigurationProcessorsTypeDef",
    {
        "Parameters": List[
            ClientCreateDeliveryStreamElasticsearchDestinationConfigurationProcessingConfigurationProcessorsParametersTypeDef
        ]
    },
    total=False,
)


class ClientCreateDeliveryStreamElasticsearchDestinationConfigurationProcessingConfigurationProcessorsTypeDef(
    _RequiredClientCreateDeliveryStreamElasticsearchDestinationConfigurationProcessingConfigurationProcessorsTypeDef,
    _OptionalClientCreateDeliveryStreamElasticsearchDestinationConfigurationProcessingConfigurationProcessorsTypeDef,
):
    """
    Type definition for `ClientCreateDeliveryStreamElasticsearchDestinationConfigurationProcessingConfiguration` `Processors`

    Describes a data processor.

    - **Type** *(string) --* **[REQUIRED]**

      The type of processor.

    - **Parameters** *(list) --*

      The processor parameters.

      - *(dict) --*

        Describes the processor parameter.

        - **ParameterName** *(string) --* **[REQUIRED]**

          The name of the parameter.

        - **ParameterValue** *(string) --* **[REQUIRED]**

          The parameter value.
    """


_ClientCreateDeliveryStreamElasticsearchDestinationConfigurationProcessingConfigurationTypeDef = TypedDict(
    "_ClientCreateDeliveryStreamElasticsearchDestinationConfigurationProcessingConfigurationTypeDef",
    {
        "Enabled": bool,
        "Processors": List[
            ClientCreateDeliveryStreamElasticsearchDestinationConfigurationProcessingConfigurationProcessorsTypeDef
        ],
    },
    total=False,
)


class ClientCreateDeliveryStreamElasticsearchDestinationConfigurationProcessingConfigurationTypeDef(
    _ClientCreateDeliveryStreamElasticsearchDestinationConfigurationProcessingConfigurationTypeDef
):
    """
    Type definition for `ClientCreateDeliveryStreamElasticsearchDestinationConfiguration` `ProcessingConfiguration`

    The data processing configuration.

    - **Enabled** *(boolean) --*

      Enables or disables data processing.

    - **Processors** *(list) --*

      The data processors.

      - *(dict) --*

        Describes a data processor.

        - **Type** *(string) --* **[REQUIRED]**

          The type of processor.

        - **Parameters** *(list) --*

          The processor parameters.

          - *(dict) --*

            Describes the processor parameter.

            - **ParameterName** *(string) --* **[REQUIRED]**

              The name of the parameter.

            - **ParameterValue** *(string) --* **[REQUIRED]**

              The parameter value.
    """


_ClientCreateDeliveryStreamElasticsearchDestinationConfigurationRetryOptionsTypeDef = TypedDict(
    "_ClientCreateDeliveryStreamElasticsearchDestinationConfigurationRetryOptionsTypeDef",
    {"DurationInSeconds": int},
    total=False,
)


class ClientCreateDeliveryStreamElasticsearchDestinationConfigurationRetryOptionsTypeDef(
    _ClientCreateDeliveryStreamElasticsearchDestinationConfigurationRetryOptionsTypeDef
):
    """
    Type definition for `ClientCreateDeliveryStreamElasticsearchDestinationConfiguration` `RetryOptions`

    The retry behavior in case Kinesis Data Firehose is unable to deliver documents to Amazon ES.
    The default value is 300 (5 minutes).

    - **DurationInSeconds** *(integer) --*

      After an initial failure to deliver to Amazon ES, the total amount of time during which
      Kinesis Data Firehose retries delivery (including the first attempt). After this time has
      elapsed, the failed documents are written to Amazon S3. Default value is 300 seconds (5
      minutes). A value of 0 (zero) results in no retries.
    """


_ClientCreateDeliveryStreamElasticsearchDestinationConfigurationS3ConfigurationBufferingHintsTypeDef = TypedDict(
    "_ClientCreateDeliveryStreamElasticsearchDestinationConfigurationS3ConfigurationBufferingHintsTypeDef",
    {"SizeInMBs": int, "IntervalInSeconds": int},
    total=False,
)


class ClientCreateDeliveryStreamElasticsearchDestinationConfigurationS3ConfigurationBufferingHintsTypeDef(
    _ClientCreateDeliveryStreamElasticsearchDestinationConfigurationS3ConfigurationBufferingHintsTypeDef
):
    """
    Type definition for `ClientCreateDeliveryStreamElasticsearchDestinationConfigurationS3Configuration` `BufferingHints`

    The buffering option. If no value is specified, ``BufferingHints`` object default values are
    used.

    - **SizeInMBs** *(integer) --*

      Buffer incoming data to the specified size, in MiBs, before delivering it to the
      destination. The default value is 5. This parameter is optional but if you specify a value
      for it, you must also specify a value for ``IntervalInSeconds`` , and vice versa.

      We recommend setting this parameter to a value greater than the amount of data you
      typically ingest into the delivery stream in 10 seconds. For example, if you typically
      ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

    - **IntervalInSeconds** *(integer) --*

      Buffer incoming data for the specified period of time, in seconds, before delivering it to
      the destination. The default value is 300. This parameter is optional but if you specify a
      value for it, you must also specify a value for ``SizeInMBs`` , and vice versa.
    """


_ClientCreateDeliveryStreamElasticsearchDestinationConfigurationS3ConfigurationCloudWatchLoggingOptionsTypeDef = TypedDict(
    "_ClientCreateDeliveryStreamElasticsearchDestinationConfigurationS3ConfigurationCloudWatchLoggingOptionsTypeDef",
    {"Enabled": bool, "LogGroupName": str, "LogStreamName": str},
    total=False,
)


class ClientCreateDeliveryStreamElasticsearchDestinationConfigurationS3ConfigurationCloudWatchLoggingOptionsTypeDef(
    _ClientCreateDeliveryStreamElasticsearchDestinationConfigurationS3ConfigurationCloudWatchLoggingOptionsTypeDef
):
    """
    Type definition for `ClientCreateDeliveryStreamElasticsearchDestinationConfigurationS3Configuration` `CloudWatchLoggingOptions`

    The CloudWatch logging options for your delivery stream.

    - **Enabled** *(boolean) --*

      Enables or disables CloudWatch logging.

    - **LogGroupName** *(string) --*

      The CloudWatch group name for logging. This value is required if CloudWatch logging is
      enabled.

    - **LogStreamName** *(string) --*

      The CloudWatch log stream name for logging. This value is required if CloudWatch logging is
      enabled.
    """


_ClientCreateDeliveryStreamElasticsearchDestinationConfigurationS3ConfigurationEncryptionConfigurationKMSEncryptionConfigTypeDef = TypedDict(
    "_ClientCreateDeliveryStreamElasticsearchDestinationConfigurationS3ConfigurationEncryptionConfigurationKMSEncryptionConfigTypeDef",
    {"AWSKMSKeyARN": str},
)


class ClientCreateDeliveryStreamElasticsearchDestinationConfigurationS3ConfigurationEncryptionConfigurationKMSEncryptionConfigTypeDef(
    _ClientCreateDeliveryStreamElasticsearchDestinationConfigurationS3ConfigurationEncryptionConfigurationKMSEncryptionConfigTypeDef
):
    """
    Type definition for `ClientCreateDeliveryStreamElasticsearchDestinationConfigurationS3ConfigurationEncryptionConfiguration` `KMSEncryptionConfig`

    The encryption key.

    - **AWSKMSKeyARN** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region
      as the destination Amazon S3 bucket. For more information, see `Amazon Resource Names
      (ARNs) and AWS Service Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
    """


_ClientCreateDeliveryStreamElasticsearchDestinationConfigurationS3ConfigurationEncryptionConfigurationTypeDef = TypedDict(
    "_ClientCreateDeliveryStreamElasticsearchDestinationConfigurationS3ConfigurationEncryptionConfigurationTypeDef",
    {
        "NoEncryptionConfig": str,
        "KMSEncryptionConfig": ClientCreateDeliveryStreamElasticsearchDestinationConfigurationS3ConfigurationEncryptionConfigurationKMSEncryptionConfigTypeDef,
    },
    total=False,
)


class ClientCreateDeliveryStreamElasticsearchDestinationConfigurationS3ConfigurationEncryptionConfigurationTypeDef(
    _ClientCreateDeliveryStreamElasticsearchDestinationConfigurationS3ConfigurationEncryptionConfigurationTypeDef
):
    """
    Type definition for `ClientCreateDeliveryStreamElasticsearchDestinationConfigurationS3Configuration` `EncryptionConfiguration`

    The encryption configuration. If no value is specified, the default is no encryption.

    - **NoEncryptionConfig** *(string) --*

      Specifically override existing encryption information to ensure that no encryption is used.

    - **KMSEncryptionConfig** *(dict) --*

      The encryption key.

      - **AWSKMSKeyARN** *(string) --* **[REQUIRED]**

        The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region
        as the destination Amazon S3 bucket. For more information, see `Amazon Resource Names
        (ARNs) and AWS Service Namespaces
        <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
    """


_RequiredClientCreateDeliveryStreamElasticsearchDestinationConfigurationS3ConfigurationTypeDef = TypedDict(
    "_RequiredClientCreateDeliveryStreamElasticsearchDestinationConfigurationS3ConfigurationTypeDef",
    {"RoleARN": str, "BucketARN": str},
)
_OptionalClientCreateDeliveryStreamElasticsearchDestinationConfigurationS3ConfigurationTypeDef = TypedDict(
    "_OptionalClientCreateDeliveryStreamElasticsearchDestinationConfigurationS3ConfigurationTypeDef",
    {
        "Prefix": str,
        "ErrorOutputPrefix": str,
        "BufferingHints": ClientCreateDeliveryStreamElasticsearchDestinationConfigurationS3ConfigurationBufferingHintsTypeDef,
        "CompressionFormat": str,
        "EncryptionConfiguration": ClientCreateDeliveryStreamElasticsearchDestinationConfigurationS3ConfigurationEncryptionConfigurationTypeDef,
        "CloudWatchLoggingOptions": ClientCreateDeliveryStreamElasticsearchDestinationConfigurationS3ConfigurationCloudWatchLoggingOptionsTypeDef,
    },
    total=False,
)


class ClientCreateDeliveryStreamElasticsearchDestinationConfigurationS3ConfigurationTypeDef(
    _RequiredClientCreateDeliveryStreamElasticsearchDestinationConfigurationS3ConfigurationTypeDef,
    _OptionalClientCreateDeliveryStreamElasticsearchDestinationConfigurationS3ConfigurationTypeDef,
):
    """
    Type definition for `ClientCreateDeliveryStreamElasticsearchDestinationConfiguration` `S3Configuration`

    The configuration for the backup Amazon S3 location.

    - **RoleARN** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the AWS credentials. For more information, see `Amazon
      Resource Names (ARNs) and AWS Service Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

    - **BucketARN** *(string) --* **[REQUIRED]**

      The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs) and AWS
      Service Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

    - **Prefix** *(string) --*

      The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered Amazon S3 files.
      You can also specify a custom prefix, as described in `Custom Prefixes for Amazon S3 Objects
      <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

    - **ErrorOutputPrefix** *(string) --*

      A prefix that Kinesis Data Firehose evaluates and adds to failed records before writing them
      to S3. This prefix appears immediately following the bucket name. For information about how
      to specify this prefix, see `Custom Prefixes for Amazon S3 Objects
      <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

    - **BufferingHints** *(dict) --*

      The buffering option. If no value is specified, ``BufferingHints`` object default values are
      used.

      - **SizeInMBs** *(integer) --*

        Buffer incoming data to the specified size, in MiBs, before delivering it to the
        destination. The default value is 5. This parameter is optional but if you specify a value
        for it, you must also specify a value for ``IntervalInSeconds`` , and vice versa.

        We recommend setting this parameter to a value greater than the amount of data you
        typically ingest into the delivery stream in 10 seconds. For example, if you typically
        ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

      - **IntervalInSeconds** *(integer) --*

        Buffer incoming data for the specified period of time, in seconds, before delivering it to
        the destination. The default value is 300. This parameter is optional but if you specify a
        value for it, you must also specify a value for ``SizeInMBs`` , and vice versa.

    - **CompressionFormat** *(string) --*

      The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .

      The compression formats ``SNAPPY`` or ``ZIP`` cannot be specified for Amazon Redshift
      destinations because they are not supported by the Amazon Redshift ``COPY`` operation that
      reads from the S3 bucket.

    - **EncryptionConfiguration** *(dict) --*

      The encryption configuration. If no value is specified, the default is no encryption.

      - **NoEncryptionConfig** *(string) --*

        Specifically override existing encryption information to ensure that no encryption is used.

      - **KMSEncryptionConfig** *(dict) --*

        The encryption key.

        - **AWSKMSKeyARN** *(string) --* **[REQUIRED]**

          The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region
          as the destination Amazon S3 bucket. For more information, see `Amazon Resource Names
          (ARNs) and AWS Service Namespaces
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

    - **CloudWatchLoggingOptions** *(dict) --*

      The CloudWatch logging options for your delivery stream.

      - **Enabled** *(boolean) --*

        Enables or disables CloudWatch logging.

      - **LogGroupName** *(string) --*

        The CloudWatch group name for logging. This value is required if CloudWatch logging is
        enabled.

      - **LogStreamName** *(string) --*

        The CloudWatch log stream name for logging. This value is required if CloudWatch logging is
        enabled.
    """


_RequiredClientCreateDeliveryStreamElasticsearchDestinationConfigurationTypeDef = TypedDict(
    "_RequiredClientCreateDeliveryStreamElasticsearchDestinationConfigurationTypeDef",
    {
        "RoleARN": str,
        "IndexName": str,
        "S3Configuration": ClientCreateDeliveryStreamElasticsearchDestinationConfigurationS3ConfigurationTypeDef,
    },
)
_OptionalClientCreateDeliveryStreamElasticsearchDestinationConfigurationTypeDef = TypedDict(
    "_OptionalClientCreateDeliveryStreamElasticsearchDestinationConfigurationTypeDef",
    {
        "DomainARN": str,
        "ClusterEndpoint": str,
        "TypeName": str,
        "IndexRotationPeriod": str,
        "BufferingHints": ClientCreateDeliveryStreamElasticsearchDestinationConfigurationBufferingHintsTypeDef,
        "RetryOptions": ClientCreateDeliveryStreamElasticsearchDestinationConfigurationRetryOptionsTypeDef,
        "S3BackupMode": str,
        "ProcessingConfiguration": ClientCreateDeliveryStreamElasticsearchDestinationConfigurationProcessingConfigurationTypeDef,
        "CloudWatchLoggingOptions": ClientCreateDeliveryStreamElasticsearchDestinationConfigurationCloudWatchLoggingOptionsTypeDef,
    },
    total=False,
)


class ClientCreateDeliveryStreamElasticsearchDestinationConfigurationTypeDef(
    _RequiredClientCreateDeliveryStreamElasticsearchDestinationConfigurationTypeDef,
    _OptionalClientCreateDeliveryStreamElasticsearchDestinationConfigurationTypeDef,
):
    """
    Type definition for `ClientCreateDeliveryStream` `ElasticsearchDestinationConfiguration`

    The destination in Amazon ES. You can specify only one destination.

    - **RoleARN** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the IAM role to be assumed by Kinesis Data Firehose for
      calling the Amazon ES Configuration API and for indexing documents. For more information, see
      `Grant Kinesis Data Firehose Access to an Amazon S3 Destination
      <https://docs.aws.amazon.com/firehose/latest/dev/controlling-access.html#using-iam-s3>`__ and
      `Amazon Resource Names (ARNs) and AWS Service Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

    - **DomainARN** *(string) --*

      The ARN of the Amazon ES domain. The IAM role must have permissions for
      ``DescribeElasticsearchDomain`` , ``DescribeElasticsearchDomains`` , and
      ``DescribeElasticsearchDomainConfig`` after assuming the role specified in **RoleARN** . For
      more information, see `Amazon Resource Names (ARNs) and AWS Service Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

      Specify either ``ClusterEndpoint`` or ``DomainARN`` .

    - **ClusterEndpoint** *(string) --*

      The endpoint to use when communicating with the cluster. Specify either this
      ``ClusterEndpoint`` or the ``DomainARN`` field.

    - **IndexName** *(string) --* **[REQUIRED]**

      The Elasticsearch index name.

    - **TypeName** *(string) --*

      The Elasticsearch type name. For Elasticsearch 6.x, there can be only one type per index. If
      you try to specify a new type for an existing index that already has another type, Kinesis Data
      Firehose returns an error during run time.

      For Elasticsearch 7.x, don't specify a ``TypeName`` .

    - **IndexRotationPeriod** *(string) --*

      The Elasticsearch index rotation period. Index rotation appends a timestamp to the
      ``IndexName`` to facilitate the expiration of old data. For more information, see `Index
      Rotation for the Amazon ES Destination
      <https://docs.aws.amazon.com/firehose/latest/dev/basic-deliver.html#es-index-rotation>`__ . The
      default value is ``OneDay`` .

    - **BufferingHints** *(dict) --*

      The buffering options. If no value is specified, the default values for
      ``ElasticsearchBufferingHints`` are used.

      - **IntervalInSeconds** *(integer) --*

        Buffer incoming data for the specified period of time, in seconds, before delivering it to
        the destination. The default value is 300 (5 minutes).

      - **SizeInMBs** *(integer) --*

        Buffer incoming data to the specified size, in MBs, before delivering it to the destination.
        The default value is 5.

        We recommend setting this parameter to a value greater than the amount of data you typically
        ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1
        MB/sec, the value should be 10 MB or higher.

    - **RetryOptions** *(dict) --*

      The retry behavior in case Kinesis Data Firehose is unable to deliver documents to Amazon ES.
      The default value is 300 (5 minutes).

      - **DurationInSeconds** *(integer) --*

        After an initial failure to deliver to Amazon ES, the total amount of time during which
        Kinesis Data Firehose retries delivery (including the first attempt). After this time has
        elapsed, the failed documents are written to Amazon S3. Default value is 300 seconds (5
        minutes). A value of 0 (zero) results in no retries.

    - **S3BackupMode** *(string) --*

      Defines how documents should be delivered to Amazon S3. When it is set to
      ``FailedDocumentsOnly`` , Kinesis Data Firehose writes any documents that could not be indexed
      to the configured Amazon S3 destination, with ``elasticsearch-failed/`` appended to the key
      prefix. When set to ``AllDocuments`` , Kinesis Data Firehose delivers all incoming records to
      Amazon S3, and also writes failed documents with ``elasticsearch-failed/`` appended to the
      prefix. For more information, see `Amazon S3 Backup for the Amazon ES Destination
      <https://docs.aws.amazon.com/firehose/latest/dev/basic-deliver.html#es-s3-backup>`__ . Default
      value is ``FailedDocumentsOnly`` .

    - **S3Configuration** *(dict) --* **[REQUIRED]**

      The configuration for the backup Amazon S3 location.

      - **RoleARN** *(string) --* **[REQUIRED]**

        The Amazon Resource Name (ARN) of the AWS credentials. For more information, see `Amazon
        Resource Names (ARNs) and AWS Service Namespaces
        <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

      - **BucketARN** *(string) --* **[REQUIRED]**

        The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs) and AWS
        Service Namespaces
        <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

      - **Prefix** *(string) --*

        The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered Amazon S3 files.
        You can also specify a custom prefix, as described in `Custom Prefixes for Amazon S3 Objects
        <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

      - **ErrorOutputPrefix** *(string) --*

        A prefix that Kinesis Data Firehose evaluates and adds to failed records before writing them
        to S3. This prefix appears immediately following the bucket name. For information about how
        to specify this prefix, see `Custom Prefixes for Amazon S3 Objects
        <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

      - **BufferingHints** *(dict) --*

        The buffering option. If no value is specified, ``BufferingHints`` object default values are
        used.

        - **SizeInMBs** *(integer) --*

          Buffer incoming data to the specified size, in MiBs, before delivering it to the
          destination. The default value is 5. This parameter is optional but if you specify a value
          for it, you must also specify a value for ``IntervalInSeconds`` , and vice versa.

          We recommend setting this parameter to a value greater than the amount of data you
          typically ingest into the delivery stream in 10 seconds. For example, if you typically
          ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

        - **IntervalInSeconds** *(integer) --*

          Buffer incoming data for the specified period of time, in seconds, before delivering it to
          the destination. The default value is 300. This parameter is optional but if you specify a
          value for it, you must also specify a value for ``SizeInMBs`` , and vice versa.

      - **CompressionFormat** *(string) --*

        The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .

        The compression formats ``SNAPPY`` or ``ZIP`` cannot be specified for Amazon Redshift
        destinations because they are not supported by the Amazon Redshift ``COPY`` operation that
        reads from the S3 bucket.

      - **EncryptionConfiguration** *(dict) --*

        The encryption configuration. If no value is specified, the default is no encryption.

        - **NoEncryptionConfig** *(string) --*

          Specifically override existing encryption information to ensure that no encryption is used.

        - **KMSEncryptionConfig** *(dict) --*

          The encryption key.

          - **AWSKMSKeyARN** *(string) --* **[REQUIRED]**

            The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region
            as the destination Amazon S3 bucket. For more information, see `Amazon Resource Names
            (ARNs) and AWS Service Namespaces
            <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

      - **CloudWatchLoggingOptions** *(dict) --*

        The CloudWatch logging options for your delivery stream.

        - **Enabled** *(boolean) --*

          Enables or disables CloudWatch logging.

        - **LogGroupName** *(string) --*

          The CloudWatch group name for logging. This value is required if CloudWatch logging is
          enabled.

        - **LogStreamName** *(string) --*

          The CloudWatch log stream name for logging. This value is required if CloudWatch logging is
          enabled.

    - **ProcessingConfiguration** *(dict) --*

      The data processing configuration.

      - **Enabled** *(boolean) --*

        Enables or disables data processing.

      - **Processors** *(list) --*

        The data processors.

        - *(dict) --*

          Describes a data processor.

          - **Type** *(string) --* **[REQUIRED]**

            The type of processor.

          - **Parameters** *(list) --*

            The processor parameters.

            - *(dict) --*

              Describes the processor parameter.

              - **ParameterName** *(string) --* **[REQUIRED]**

                The name of the parameter.

              - **ParameterValue** *(string) --* **[REQUIRED]**

                The parameter value.

    - **CloudWatchLoggingOptions** *(dict) --*

      The Amazon CloudWatch logging options for your delivery stream.

      - **Enabled** *(boolean) --*

        Enables or disables CloudWatch logging.

      - **LogGroupName** *(string) --*

        The CloudWatch group name for logging. This value is required if CloudWatch logging is
        enabled.

      - **LogStreamName** *(string) --*

        The CloudWatch log stream name for logging. This value is required if CloudWatch logging is
        enabled.
    """


_ClientCreateDeliveryStreamExtendedS3DestinationConfigurationBufferingHintsTypeDef = TypedDict(
    "_ClientCreateDeliveryStreamExtendedS3DestinationConfigurationBufferingHintsTypeDef",
    {"SizeInMBs": int, "IntervalInSeconds": int},
    total=False,
)


class ClientCreateDeliveryStreamExtendedS3DestinationConfigurationBufferingHintsTypeDef(
    _ClientCreateDeliveryStreamExtendedS3DestinationConfigurationBufferingHintsTypeDef
):
    """
    Type definition for `ClientCreateDeliveryStreamExtendedS3DestinationConfiguration` `BufferingHints`

    The buffering option.

    - **SizeInMBs** *(integer) --*

      Buffer incoming data to the specified size, in MiBs, before delivering it to the destination.
      The default value is 5. This parameter is optional but if you specify a value for it, you
      must also specify a value for ``IntervalInSeconds`` , and vice versa.

      We recommend setting this parameter to a value greater than the amount of data you typically
      ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1
      MiB/sec, the value should be 10 MiB or higher.

    - **IntervalInSeconds** *(integer) --*

      Buffer incoming data for the specified period of time, in seconds, before delivering it to
      the destination. The default value is 300. This parameter is optional but if you specify a
      value for it, you must also specify a value for ``SizeInMBs`` , and vice versa.
    """


_ClientCreateDeliveryStreamExtendedS3DestinationConfigurationCloudWatchLoggingOptionsTypeDef = TypedDict(
    "_ClientCreateDeliveryStreamExtendedS3DestinationConfigurationCloudWatchLoggingOptionsTypeDef",
    {"Enabled": bool, "LogGroupName": str, "LogStreamName": str},
    total=False,
)


class ClientCreateDeliveryStreamExtendedS3DestinationConfigurationCloudWatchLoggingOptionsTypeDef(
    _ClientCreateDeliveryStreamExtendedS3DestinationConfigurationCloudWatchLoggingOptionsTypeDef
):
    """
    Type definition for `ClientCreateDeliveryStreamExtendedS3DestinationConfiguration` `CloudWatchLoggingOptions`

    The Amazon CloudWatch logging options for your delivery stream.

    - **Enabled** *(boolean) --*

      Enables or disables CloudWatch logging.

    - **LogGroupName** *(string) --*

      The CloudWatch group name for logging. This value is required if CloudWatch logging is
      enabled.

    - **LogStreamName** *(string) --*

      The CloudWatch log stream name for logging. This value is required if CloudWatch logging is
      enabled.
    """


_ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDeTypeDef = TypedDict(
    "_ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDeTypeDef",
    {"TimestampFormats": List[str]},
    total=False,
)


class ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDeTypeDef(
    _ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDeTypeDef
):
    """
    Type definition for `ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializer` `HiveJsonSerDe`

    The native Hive / HCatalog JsonSerDe. Used by Kinesis Data Firehose for deserializing
    data, which means converting it from the JSON format in preparation for serializing it to
    the Parquet or ORC format. This is one of two deserializers you can choose, depending on
    which one offers the functionality you need. The other option is the OpenX SerDe.

    - **TimestampFormats** *(list) --*

      Indicates how you want Kinesis Data Firehose to parse the date and timestamps that may
      be present in your input data JSON. To specify these format strings, follow the pattern
      syntax of JodaTime's DateTimeFormat format strings. For more information, see `Class
      DateTimeFormat
      <https://www.joda.org/joda-time/apidocs/org/joda/time/format/DateTimeFormat.html>`__ .
      You can also use the special value ``millis`` to parse timestamps in epoch
      milliseconds. If you don't specify a format, Kinesis Data Firehose uses
      ``java.sql.Timestamp::valueOf`` by default.

      - *(string) --*
    """


_ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDeTypeDef = TypedDict(
    "_ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDeTypeDef",
    {
        "ConvertDotsInJsonKeysToUnderscores": bool,
        "CaseInsensitive": bool,
        "ColumnToJsonKeyMappings": Dict[str, str],
    },
    total=False,
)


class ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDeTypeDef(
    _ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDeTypeDef
):
    """
    Type definition for `ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializer` `OpenXJsonSerDe`

    The OpenX SerDe. Used by Kinesis Data Firehose for deserializing data, which means
    converting it from the JSON format in preparation for serializing it to the Parquet or
    ORC format. This is one of two deserializers you can choose, depending on which one
    offers the functionality you need. The other option is the native Hive / HCatalog
    JsonSerDe.

    - **ConvertDotsInJsonKeysToUnderscores** *(boolean) --*

      When set to ``true`` , specifies that the names of the keys include dots and that you
      want Kinesis Data Firehose to replace them with underscores. This is useful because
      Apache Hive does not allow dots in column names. For example, if the JSON contains a
      key whose name is "a.b", you can define the column name to be "a_b" when using this
      option.

      The default is ``false`` .

    - **CaseInsensitive** *(boolean) --*

      When set to ``true`` , which is the default, Kinesis Data Firehose converts JSON keys
      to lowercase before deserializing them.

    - **ColumnToJsonKeyMappings** *(dict) --*

      Maps column names to JSON keys that aren't identical to the column names. This is
      useful when the JSON contains keys that are Hive keywords. For example, ``timestamp``
      is a Hive keyword. If you have a JSON key named ``timestamp`` , set this parameter to
      ``{"ts": "timestamp"}`` to map this key to a column named ``ts`` .

      - *(string) --*

        - *(string) --*
    """


_ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerTypeDef = TypedDict(
    "_ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerTypeDef",
    {
        "OpenXJsonSerDe": ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDeTypeDef,
        "HiveJsonSerDe": ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDeTypeDef,
    },
    total=False,
)


class ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerTypeDef(
    _ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerTypeDef
):
    """
    Type definition for `ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationInputFormatConfiguration` `Deserializer`

    Specifies which deserializer to use. You can choose either the Apache Hive JSON SerDe or
    the OpenX JSON SerDe. If both are non-null, the server rejects the request.

    - **OpenXJsonSerDe** *(dict) --*

      The OpenX SerDe. Used by Kinesis Data Firehose for deserializing data, which means
      converting it from the JSON format in preparation for serializing it to the Parquet or
      ORC format. This is one of two deserializers you can choose, depending on which one
      offers the functionality you need. The other option is the native Hive / HCatalog
      JsonSerDe.

      - **ConvertDotsInJsonKeysToUnderscores** *(boolean) --*

        When set to ``true`` , specifies that the names of the keys include dots and that you
        want Kinesis Data Firehose to replace them with underscores. This is useful because
        Apache Hive does not allow dots in column names. For example, if the JSON contains a
        key whose name is "a.b", you can define the column name to be "a_b" when using this
        option.

        The default is ``false`` .

      - **CaseInsensitive** *(boolean) --*

        When set to ``true`` , which is the default, Kinesis Data Firehose converts JSON keys
        to lowercase before deserializing them.

      - **ColumnToJsonKeyMappings** *(dict) --*

        Maps column names to JSON keys that aren't identical to the column names. This is
        useful when the JSON contains keys that are Hive keywords. For example, ``timestamp``
        is a Hive keyword. If you have a JSON key named ``timestamp`` , set this parameter to
        ``{"ts": "timestamp"}`` to map this key to a column named ``ts`` .

        - *(string) --*

          - *(string) --*

    - **HiveJsonSerDe** *(dict) --*

      The native Hive / HCatalog JsonSerDe. Used by Kinesis Data Firehose for deserializing
      data, which means converting it from the JSON format in preparation for serializing it to
      the Parquet or ORC format. This is one of two deserializers you can choose, depending on
      which one offers the functionality you need. The other option is the OpenX SerDe.

      - **TimestampFormats** *(list) --*

        Indicates how you want Kinesis Data Firehose to parse the date and timestamps that may
        be present in your input data JSON. To specify these format strings, follow the pattern
        syntax of JodaTime's DateTimeFormat format strings. For more information, see `Class
        DateTimeFormat
        <https://www.joda.org/joda-time/apidocs/org/joda/time/format/DateTimeFormat.html>`__ .
        You can also use the special value ``millis`` to parse timestamps in epoch
        milliseconds. If you don't specify a format, Kinesis Data Firehose uses
        ``java.sql.Timestamp::valueOf`` by default.

        - *(string) --*
    """


_ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationInputFormatConfigurationTypeDef = TypedDict(
    "_ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationInputFormatConfigurationTypeDef",
    {
        "Deserializer": ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerTypeDef
    },
    total=False,
)


class ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationInputFormatConfigurationTypeDef(
    _ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationInputFormatConfigurationTypeDef
):
    """
    Type definition for `ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfiguration` `InputFormatConfiguration`

    Specifies the deserializer that you want Kinesis Data Firehose to use to convert the format
    of your data from JSON.

    - **Deserializer** *(dict) --*

      Specifies which deserializer to use. You can choose either the Apache Hive JSON SerDe or
      the OpenX JSON SerDe. If both are non-null, the server rejects the request.

      - **OpenXJsonSerDe** *(dict) --*

        The OpenX SerDe. Used by Kinesis Data Firehose for deserializing data, which means
        converting it from the JSON format in preparation for serializing it to the Parquet or
        ORC format. This is one of two deserializers you can choose, depending on which one
        offers the functionality you need. The other option is the native Hive / HCatalog
        JsonSerDe.

        - **ConvertDotsInJsonKeysToUnderscores** *(boolean) --*

          When set to ``true`` , specifies that the names of the keys include dots and that you
          want Kinesis Data Firehose to replace them with underscores. This is useful because
          Apache Hive does not allow dots in column names. For example, if the JSON contains a
          key whose name is "a.b", you can define the column name to be "a_b" when using this
          option.

          The default is ``false`` .

        - **CaseInsensitive** *(boolean) --*

          When set to ``true`` , which is the default, Kinesis Data Firehose converts JSON keys
          to lowercase before deserializing them.

        - **ColumnToJsonKeyMappings** *(dict) --*

          Maps column names to JSON keys that aren't identical to the column names. This is
          useful when the JSON contains keys that are Hive keywords. For example, ``timestamp``
          is a Hive keyword. If you have a JSON key named ``timestamp`` , set this parameter to
          ``{"ts": "timestamp"}`` to map this key to a column named ``ts`` .

          - *(string) --*

            - *(string) --*

      - **HiveJsonSerDe** *(dict) --*

        The native Hive / HCatalog JsonSerDe. Used by Kinesis Data Firehose for deserializing
        data, which means converting it from the JSON format in preparation for serializing it to
        the Parquet or ORC format. This is one of two deserializers you can choose, depending on
        which one offers the functionality you need. The other option is the OpenX SerDe.

        - **TimestampFormats** *(list) --*

          Indicates how you want Kinesis Data Firehose to parse the date and timestamps that may
          be present in your input data JSON. To specify these format strings, follow the pattern
          syntax of JodaTime's DateTimeFormat format strings. For more information, see `Class
          DateTimeFormat
          <https://www.joda.org/joda-time/apidocs/org/joda/time/format/DateTimeFormat.html>`__ .
          You can also use the special value ``millis`` to parse timestamps in epoch
          milliseconds. If you don't specify a format, Kinesis Data Firehose uses
          ``java.sql.Timestamp::valueOf`` by default.

          - *(string) --*
    """


_ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDeTypeDef = TypedDict(
    "_ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDeTypeDef",
    {
        "StripeSizeBytes": int,
        "BlockSizeBytes": int,
        "RowIndexStride": int,
        "EnablePadding": bool,
        "PaddingTolerance": float,
        "Compression": str,
        "BloomFilterColumns": List[str],
        "BloomFilterFalsePositiveProbability": float,
        "DictionaryKeyThreshold": float,
        "FormatVersion": str,
    },
    total=False,
)


class ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDeTypeDef(
    _ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDeTypeDef
):
    """
    Type definition for `ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializer` `OrcSerDe`

    A serializer to use for converting data to the ORC format before storing it in Amazon S3.
    For more information, see `Apache ORC <https://orc.apache.org/docs/>`__ .

    - **StripeSizeBytes** *(integer) --*

      The number of bytes in each stripe. The default is 64 MiB and the minimum is 8 MiB.

    - **BlockSizeBytes** *(integer) --*

      The Hadoop Distributed File System (HDFS) block size. This is useful if you intend to
      copy the data from Amazon S3 to HDFS before querying. The default is 256 MiB and the
      minimum is 64 MiB. Kinesis Data Firehose uses this value for padding calculations.

    - **RowIndexStride** *(integer) --*

      The number of rows between index entries. The default is 10,000 and the minimum is
      1,000.

    - **EnablePadding** *(boolean) --*

      Set this to ``true`` to indicate that you want stripes to be padded to the HDFS block
      boundaries. This is useful if you intend to copy the data from Amazon S3 to HDFS before
      querying. The default is ``false`` .

    - **PaddingTolerance** *(float) --*

      A number between 0 and 1 that defines the tolerance for block padding as a decimal
      fraction of stripe size. The default value is 0.05, which means 5 percent of stripe
      size.

      For the default values of 64 MiB ORC stripes and 256 MiB HDFS blocks, the default block
      padding tolerance of 5 percent reserves a maximum of 3.2 MiB for padding within the 256
      MiB block. In such a case, if the available size within the block is more than 3.2 MiB,
      a new, smaller stripe is inserted to fit within that space. This ensures that no stripe
      crosses block boundaries and causes remote reads within a node-local task.

      Kinesis Data Firehose ignores this parameter when  OrcSerDe$EnablePadding is ``false`` .

    - **Compression** *(string) --*

      The compression code to use over data blocks. The default is ``SNAPPY`` .

    - **BloomFilterColumns** *(list) --*

      The column names for which you want Kinesis Data Firehose to create bloom filters. The
      default is ``null`` .

      - *(string) --*

    - **BloomFilterFalsePositiveProbability** *(float) --*

      The Bloom filter false positive probability (FPP). The lower the FPP, the bigger the
      Bloom filter. The default value is 0.05, the minimum is 0, and the maximum is 1.

    - **DictionaryKeyThreshold** *(float) --*

      Represents the fraction of the total number of non-null rows. To turn off dictionary
      encoding, set this fraction to a number that is less than the number of distinct keys
      in a dictionary. To always use dictionary encoding, set this threshold to 1.

    - **FormatVersion** *(string) --*

      The version of the file to write. The possible values are ``V0_11`` and ``V0_12`` . The
      default is ``V0_12`` .
    """


_ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDeTypeDef = TypedDict(
    "_ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDeTypeDef",
    {
        "BlockSizeBytes": int,
        "PageSizeBytes": int,
        "Compression": str,
        "EnableDictionaryCompression": bool,
        "MaxPaddingBytes": int,
        "WriterVersion": str,
    },
    total=False,
)


class ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDeTypeDef(
    _ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDeTypeDef
):
    """
    Type definition for `ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializer` `ParquetSerDe`

    A serializer to use for converting data to the Parquet format before storing it in Amazon
    S3. For more information, see `Apache Parquet
    <https://parquet.apache.org/documentation/latest/>`__ .

    - **BlockSizeBytes** *(integer) --*

      The Hadoop Distributed File System (HDFS) block size. This is useful if you intend to
      copy the data from Amazon S3 to HDFS before querying. The default is 256 MiB and the
      minimum is 64 MiB. Kinesis Data Firehose uses this value for padding calculations.

    - **PageSizeBytes** *(integer) --*

      The Parquet page size. Column chunks are divided into pages. A page is conceptually an
      indivisible unit (in terms of compression and encoding). The minimum value is 64 KiB
      and the default is 1 MiB.

    - **Compression** *(string) --*

      The compression code to use over data blocks. The possible values are ``UNCOMPRESSED``
      , ``SNAPPY`` , and ``GZIP`` , with the default being ``SNAPPY`` . Use ``SNAPPY`` for
      higher decompression speed. Use ``GZIP`` if the compression ration is more important
      than speed.

    - **EnableDictionaryCompression** *(boolean) --*

      Indicates whether to enable dictionary compression.

    - **MaxPaddingBytes** *(integer) --*

      The maximum amount of padding to apply. This is useful if you intend to copy the data
      from Amazon S3 to HDFS before querying. The default is 0.

    - **WriterVersion** *(string) --*

      Indicates the version of row format to output. The possible values are ``V1`` and
      ``V2`` . The default is ``V1`` .
    """


_ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerTypeDef = TypedDict(
    "_ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerTypeDef",
    {
        "ParquetSerDe": ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDeTypeDef,
        "OrcSerDe": ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDeTypeDef,
    },
    total=False,
)


class ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerTypeDef(
    _ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerTypeDef
):
    """
    Type definition for `ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationOutputFormatConfiguration` `Serializer`

    Specifies which serializer to use. You can choose either the ORC SerDe or the Parquet
    SerDe. If both are non-null, the server rejects the request.

    - **ParquetSerDe** *(dict) --*

      A serializer to use for converting data to the Parquet format before storing it in Amazon
      S3. For more information, see `Apache Parquet
      <https://parquet.apache.org/documentation/latest/>`__ .

      - **BlockSizeBytes** *(integer) --*

        The Hadoop Distributed File System (HDFS) block size. This is useful if you intend to
        copy the data from Amazon S3 to HDFS before querying. The default is 256 MiB and the
        minimum is 64 MiB. Kinesis Data Firehose uses this value for padding calculations.

      - **PageSizeBytes** *(integer) --*

        The Parquet page size. Column chunks are divided into pages. A page is conceptually an
        indivisible unit (in terms of compression and encoding). The minimum value is 64 KiB
        and the default is 1 MiB.

      - **Compression** *(string) --*

        The compression code to use over data blocks. The possible values are ``UNCOMPRESSED``
        , ``SNAPPY`` , and ``GZIP`` , with the default being ``SNAPPY`` . Use ``SNAPPY`` for
        higher decompression speed. Use ``GZIP`` if the compression ration is more important
        than speed.

      - **EnableDictionaryCompression** *(boolean) --*

        Indicates whether to enable dictionary compression.

      - **MaxPaddingBytes** *(integer) --*

        The maximum amount of padding to apply. This is useful if you intend to copy the data
        from Amazon S3 to HDFS before querying. The default is 0.

      - **WriterVersion** *(string) --*

        Indicates the version of row format to output. The possible values are ``V1`` and
        ``V2`` . The default is ``V1`` .

    - **OrcSerDe** *(dict) --*

      A serializer to use for converting data to the ORC format before storing it in Amazon S3.
      For more information, see `Apache ORC <https://orc.apache.org/docs/>`__ .

      - **StripeSizeBytes** *(integer) --*

        The number of bytes in each stripe. The default is 64 MiB and the minimum is 8 MiB.

      - **BlockSizeBytes** *(integer) --*

        The Hadoop Distributed File System (HDFS) block size. This is useful if you intend to
        copy the data from Amazon S3 to HDFS before querying. The default is 256 MiB and the
        minimum is 64 MiB. Kinesis Data Firehose uses this value for padding calculations.

      - **RowIndexStride** *(integer) --*

        The number of rows between index entries. The default is 10,000 and the minimum is
        1,000.

      - **EnablePadding** *(boolean) --*

        Set this to ``true`` to indicate that you want stripes to be padded to the HDFS block
        boundaries. This is useful if you intend to copy the data from Amazon S3 to HDFS before
        querying. The default is ``false`` .

      - **PaddingTolerance** *(float) --*

        A number between 0 and 1 that defines the tolerance for block padding as a decimal
        fraction of stripe size. The default value is 0.05, which means 5 percent of stripe
        size.

        For the default values of 64 MiB ORC stripes and 256 MiB HDFS blocks, the default block
        padding tolerance of 5 percent reserves a maximum of 3.2 MiB for padding within the 256
        MiB block. In such a case, if the available size within the block is more than 3.2 MiB,
        a new, smaller stripe is inserted to fit within that space. This ensures that no stripe
        crosses block boundaries and causes remote reads within a node-local task.

        Kinesis Data Firehose ignores this parameter when  OrcSerDe$EnablePadding is ``false`` .

      - **Compression** *(string) --*

        The compression code to use over data blocks. The default is ``SNAPPY`` .

      - **BloomFilterColumns** *(list) --*

        The column names for which you want Kinesis Data Firehose to create bloom filters. The
        default is ``null`` .

        - *(string) --*

      - **BloomFilterFalsePositiveProbability** *(float) --*

        The Bloom filter false positive probability (FPP). The lower the FPP, the bigger the
        Bloom filter. The default value is 0.05, the minimum is 0, and the maximum is 1.

      - **DictionaryKeyThreshold** *(float) --*

        Represents the fraction of the total number of non-null rows. To turn off dictionary
        encoding, set this fraction to a number that is less than the number of distinct keys
        in a dictionary. To always use dictionary encoding, set this threshold to 1.

      - **FormatVersion** *(string) --*

        The version of the file to write. The possible values are ``V0_11`` and ``V0_12`` . The
        default is ``V0_12`` .
    """


_ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationOutputFormatConfigurationTypeDef = TypedDict(
    "_ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationOutputFormatConfigurationTypeDef",
    {
        "Serializer": ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerTypeDef
    },
    total=False,
)


class ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationOutputFormatConfigurationTypeDef(
    _ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationOutputFormatConfigurationTypeDef
):
    """
    Type definition for `ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfiguration` `OutputFormatConfiguration`

    Specifies the serializer that you want Kinesis Data Firehose to use to convert the format of
    your data to the Parquet or ORC format.

    - **Serializer** *(dict) --*

      Specifies which serializer to use. You can choose either the ORC SerDe or the Parquet
      SerDe. If both are non-null, the server rejects the request.

      - **ParquetSerDe** *(dict) --*

        A serializer to use for converting data to the Parquet format before storing it in Amazon
        S3. For more information, see `Apache Parquet
        <https://parquet.apache.org/documentation/latest/>`__ .

        - **BlockSizeBytes** *(integer) --*

          The Hadoop Distributed File System (HDFS) block size. This is useful if you intend to
          copy the data from Amazon S3 to HDFS before querying. The default is 256 MiB and the
          minimum is 64 MiB. Kinesis Data Firehose uses this value for padding calculations.

        - **PageSizeBytes** *(integer) --*

          The Parquet page size. Column chunks are divided into pages. A page is conceptually an
          indivisible unit (in terms of compression and encoding). The minimum value is 64 KiB
          and the default is 1 MiB.

        - **Compression** *(string) --*

          The compression code to use over data blocks. The possible values are ``UNCOMPRESSED``
          , ``SNAPPY`` , and ``GZIP`` , with the default being ``SNAPPY`` . Use ``SNAPPY`` for
          higher decompression speed. Use ``GZIP`` if the compression ration is more important
          than speed.

        - **EnableDictionaryCompression** *(boolean) --*

          Indicates whether to enable dictionary compression.

        - **MaxPaddingBytes** *(integer) --*

          The maximum amount of padding to apply. This is useful if you intend to copy the data
          from Amazon S3 to HDFS before querying. The default is 0.

        - **WriterVersion** *(string) --*

          Indicates the version of row format to output. The possible values are ``V1`` and
          ``V2`` . The default is ``V1`` .

      - **OrcSerDe** *(dict) --*

        A serializer to use for converting data to the ORC format before storing it in Amazon S3.
        For more information, see `Apache ORC <https://orc.apache.org/docs/>`__ .

        - **StripeSizeBytes** *(integer) --*

          The number of bytes in each stripe. The default is 64 MiB and the minimum is 8 MiB.

        - **BlockSizeBytes** *(integer) --*

          The Hadoop Distributed File System (HDFS) block size. This is useful if you intend to
          copy the data from Amazon S3 to HDFS before querying. The default is 256 MiB and the
          minimum is 64 MiB. Kinesis Data Firehose uses this value for padding calculations.

        - **RowIndexStride** *(integer) --*

          The number of rows between index entries. The default is 10,000 and the minimum is
          1,000.

        - **EnablePadding** *(boolean) --*

          Set this to ``true`` to indicate that you want stripes to be padded to the HDFS block
          boundaries. This is useful if you intend to copy the data from Amazon S3 to HDFS before
          querying. The default is ``false`` .

        - **PaddingTolerance** *(float) --*

          A number between 0 and 1 that defines the tolerance for block padding as a decimal
          fraction of stripe size. The default value is 0.05, which means 5 percent of stripe
          size.

          For the default values of 64 MiB ORC stripes and 256 MiB HDFS blocks, the default block
          padding tolerance of 5 percent reserves a maximum of 3.2 MiB for padding within the 256
          MiB block. In such a case, if the available size within the block is more than 3.2 MiB,
          a new, smaller stripe is inserted to fit within that space. This ensures that no stripe
          crosses block boundaries and causes remote reads within a node-local task.

          Kinesis Data Firehose ignores this parameter when  OrcSerDe$EnablePadding is ``false`` .

        - **Compression** *(string) --*

          The compression code to use over data blocks. The default is ``SNAPPY`` .

        - **BloomFilterColumns** *(list) --*

          The column names for which you want Kinesis Data Firehose to create bloom filters. The
          default is ``null`` .

          - *(string) --*

        - **BloomFilterFalsePositiveProbability** *(float) --*

          The Bloom filter false positive probability (FPP). The lower the FPP, the bigger the
          Bloom filter. The default value is 0.05, the minimum is 0, and the maximum is 1.

        - **DictionaryKeyThreshold** *(float) --*

          Represents the fraction of the total number of non-null rows. To turn off dictionary
          encoding, set this fraction to a number that is less than the number of distinct keys
          in a dictionary. To always use dictionary encoding, set this threshold to 1.

        - **FormatVersion** *(string) --*

          The version of the file to write. The possible values are ``V0_11`` and ``V0_12`` . The
          default is ``V0_12`` .
    """


_ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationSchemaConfigurationTypeDef = TypedDict(
    "_ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationSchemaConfigurationTypeDef",
    {
        "RoleARN": str,
        "CatalogId": str,
        "DatabaseName": str,
        "TableName": str,
        "Region": str,
        "VersionId": str,
    },
    total=False,
)


class ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationSchemaConfigurationTypeDef(
    _ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationSchemaConfigurationTypeDef
):
    """
    Type definition for `ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfiguration` `SchemaConfiguration`

    Specifies the AWS Glue Data Catalog table that contains the column information.

    - **RoleARN** *(string) --*

      The role that Kinesis Data Firehose can use to access AWS Glue. This role must be in the
      same account you use for Kinesis Data Firehose. Cross-account roles aren't allowed.

    - **CatalogId** *(string) --*

      The ID of the AWS Glue Data Catalog. If you don't supply this, the AWS account ID is used
      by default.

    - **DatabaseName** *(string) --*

      Specifies the name of the AWS Glue database that contains the schema for the output data.

    - **TableName** *(string) --*

      Specifies the AWS Glue table that contains the column information that constitutes your
      data schema.

    - **Region** *(string) --*

      If you don't specify an AWS Region, the default is the current Region.

    - **VersionId** *(string) --*

      Specifies the table version for the output data schema. If you don't specify this version
      ID, or if you set it to ``LATEST`` , Kinesis Data Firehose uses the most recent version.
      This means that any updates to the table are automatically picked up.
    """


_ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationTypeDef = TypedDict(
    "_ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationTypeDef",
    {
        "SchemaConfiguration": ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationSchemaConfigurationTypeDef,
        "InputFormatConfiguration": ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationInputFormatConfigurationTypeDef,
        "OutputFormatConfiguration": ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationOutputFormatConfigurationTypeDef,
        "Enabled": bool,
    },
    total=False,
)


class ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationTypeDef(
    _ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationTypeDef
):
    """
    Type definition for `ClientCreateDeliveryStreamExtendedS3DestinationConfiguration` `DataFormatConversionConfiguration`

    The serializer, deserializer, and schema for converting data from the JSON format to the
    Parquet or ORC format before writing it to Amazon S3.

    - **SchemaConfiguration** *(dict) --*

      Specifies the AWS Glue Data Catalog table that contains the column information.

      - **RoleARN** *(string) --*

        The role that Kinesis Data Firehose can use to access AWS Glue. This role must be in the
        same account you use for Kinesis Data Firehose. Cross-account roles aren't allowed.

      - **CatalogId** *(string) --*

        The ID of the AWS Glue Data Catalog. If you don't supply this, the AWS account ID is used
        by default.

      - **DatabaseName** *(string) --*

        Specifies the name of the AWS Glue database that contains the schema for the output data.

      - **TableName** *(string) --*

        Specifies the AWS Glue table that contains the column information that constitutes your
        data schema.

      - **Region** *(string) --*

        If you don't specify an AWS Region, the default is the current Region.

      - **VersionId** *(string) --*

        Specifies the table version for the output data schema. If you don't specify this version
        ID, or if you set it to ``LATEST`` , Kinesis Data Firehose uses the most recent version.
        This means that any updates to the table are automatically picked up.

    - **InputFormatConfiguration** *(dict) --*

      Specifies the deserializer that you want Kinesis Data Firehose to use to convert the format
      of your data from JSON.

      - **Deserializer** *(dict) --*

        Specifies which deserializer to use. You can choose either the Apache Hive JSON SerDe or
        the OpenX JSON SerDe. If both are non-null, the server rejects the request.

        - **OpenXJsonSerDe** *(dict) --*

          The OpenX SerDe. Used by Kinesis Data Firehose for deserializing data, which means
          converting it from the JSON format in preparation for serializing it to the Parquet or
          ORC format. This is one of two deserializers you can choose, depending on which one
          offers the functionality you need. The other option is the native Hive / HCatalog
          JsonSerDe.

          - **ConvertDotsInJsonKeysToUnderscores** *(boolean) --*

            When set to ``true`` , specifies that the names of the keys include dots and that you
            want Kinesis Data Firehose to replace them with underscores. This is useful because
            Apache Hive does not allow dots in column names. For example, if the JSON contains a
            key whose name is "a.b", you can define the column name to be "a_b" when using this
            option.

            The default is ``false`` .

          - **CaseInsensitive** *(boolean) --*

            When set to ``true`` , which is the default, Kinesis Data Firehose converts JSON keys
            to lowercase before deserializing them.

          - **ColumnToJsonKeyMappings** *(dict) --*

            Maps column names to JSON keys that aren't identical to the column names. This is
            useful when the JSON contains keys that are Hive keywords. For example, ``timestamp``
            is a Hive keyword. If you have a JSON key named ``timestamp`` , set this parameter to
            ``{"ts": "timestamp"}`` to map this key to a column named ``ts`` .

            - *(string) --*

              - *(string) --*

        - **HiveJsonSerDe** *(dict) --*

          The native Hive / HCatalog JsonSerDe. Used by Kinesis Data Firehose for deserializing
          data, which means converting it from the JSON format in preparation for serializing it to
          the Parquet or ORC format. This is one of two deserializers you can choose, depending on
          which one offers the functionality you need. The other option is the OpenX SerDe.

          - **TimestampFormats** *(list) --*

            Indicates how you want Kinesis Data Firehose to parse the date and timestamps that may
            be present in your input data JSON. To specify these format strings, follow the pattern
            syntax of JodaTime's DateTimeFormat format strings. For more information, see `Class
            DateTimeFormat
            <https://www.joda.org/joda-time/apidocs/org/joda/time/format/DateTimeFormat.html>`__ .
            You can also use the special value ``millis`` to parse timestamps in epoch
            milliseconds. If you don't specify a format, Kinesis Data Firehose uses
            ``java.sql.Timestamp::valueOf`` by default.

            - *(string) --*

    - **OutputFormatConfiguration** *(dict) --*

      Specifies the serializer that you want Kinesis Data Firehose to use to convert the format of
      your data to the Parquet or ORC format.

      - **Serializer** *(dict) --*

        Specifies which serializer to use. You can choose either the ORC SerDe or the Parquet
        SerDe. If both are non-null, the server rejects the request.

        - **ParquetSerDe** *(dict) --*

          A serializer to use for converting data to the Parquet format before storing it in Amazon
          S3. For more information, see `Apache Parquet
          <https://parquet.apache.org/documentation/latest/>`__ .

          - **BlockSizeBytes** *(integer) --*

            The Hadoop Distributed File System (HDFS) block size. This is useful if you intend to
            copy the data from Amazon S3 to HDFS before querying. The default is 256 MiB and the
            minimum is 64 MiB. Kinesis Data Firehose uses this value for padding calculations.

          - **PageSizeBytes** *(integer) --*

            The Parquet page size. Column chunks are divided into pages. A page is conceptually an
            indivisible unit (in terms of compression and encoding). The minimum value is 64 KiB
            and the default is 1 MiB.

          - **Compression** *(string) --*

            The compression code to use over data blocks. The possible values are ``UNCOMPRESSED``
            , ``SNAPPY`` , and ``GZIP`` , with the default being ``SNAPPY`` . Use ``SNAPPY`` for
            higher decompression speed. Use ``GZIP`` if the compression ration is more important
            than speed.

          - **EnableDictionaryCompression** *(boolean) --*

            Indicates whether to enable dictionary compression.

          - **MaxPaddingBytes** *(integer) --*

            The maximum amount of padding to apply. This is useful if you intend to copy the data
            from Amazon S3 to HDFS before querying. The default is 0.

          - **WriterVersion** *(string) --*

            Indicates the version of row format to output. The possible values are ``V1`` and
            ``V2`` . The default is ``V1`` .

        - **OrcSerDe** *(dict) --*

          A serializer to use for converting data to the ORC format before storing it in Amazon S3.
          For more information, see `Apache ORC <https://orc.apache.org/docs/>`__ .

          - **StripeSizeBytes** *(integer) --*

            The number of bytes in each stripe. The default is 64 MiB and the minimum is 8 MiB.

          - **BlockSizeBytes** *(integer) --*

            The Hadoop Distributed File System (HDFS) block size. This is useful if you intend to
            copy the data from Amazon S3 to HDFS before querying. The default is 256 MiB and the
            minimum is 64 MiB. Kinesis Data Firehose uses this value for padding calculations.

          - **RowIndexStride** *(integer) --*

            The number of rows between index entries. The default is 10,000 and the minimum is
            1,000.

          - **EnablePadding** *(boolean) --*

            Set this to ``true`` to indicate that you want stripes to be padded to the HDFS block
            boundaries. This is useful if you intend to copy the data from Amazon S3 to HDFS before
            querying. The default is ``false`` .

          - **PaddingTolerance** *(float) --*

            A number between 0 and 1 that defines the tolerance for block padding as a decimal
            fraction of stripe size. The default value is 0.05, which means 5 percent of stripe
            size.

            For the default values of 64 MiB ORC stripes and 256 MiB HDFS blocks, the default block
            padding tolerance of 5 percent reserves a maximum of 3.2 MiB for padding within the 256
            MiB block. In such a case, if the available size within the block is more than 3.2 MiB,
            a new, smaller stripe is inserted to fit within that space. This ensures that no stripe
            crosses block boundaries and causes remote reads within a node-local task.

            Kinesis Data Firehose ignores this parameter when  OrcSerDe$EnablePadding is ``false`` .

          - **Compression** *(string) --*

            The compression code to use over data blocks. The default is ``SNAPPY`` .

          - **BloomFilterColumns** *(list) --*

            The column names for which you want Kinesis Data Firehose to create bloom filters. The
            default is ``null`` .

            - *(string) --*

          - **BloomFilterFalsePositiveProbability** *(float) --*

            The Bloom filter false positive probability (FPP). The lower the FPP, the bigger the
            Bloom filter. The default value is 0.05, the minimum is 0, and the maximum is 1.

          - **DictionaryKeyThreshold** *(float) --*

            Represents the fraction of the total number of non-null rows. To turn off dictionary
            encoding, set this fraction to a number that is less than the number of distinct keys
            in a dictionary. To always use dictionary encoding, set this threshold to 1.

          - **FormatVersion** *(string) --*

            The version of the file to write. The possible values are ``V0_11`` and ``V0_12`` . The
            default is ``V0_12`` .

    - **Enabled** *(boolean) --*

      Defaults to ``true`` . Set it to ``false`` if you want to disable format conversion while
      preserving the configuration details.
    """


_ClientCreateDeliveryStreamExtendedS3DestinationConfigurationEncryptionConfigurationKMSEncryptionConfigTypeDef = TypedDict(
    "_ClientCreateDeliveryStreamExtendedS3DestinationConfigurationEncryptionConfigurationKMSEncryptionConfigTypeDef",
    {"AWSKMSKeyARN": str},
)


class ClientCreateDeliveryStreamExtendedS3DestinationConfigurationEncryptionConfigurationKMSEncryptionConfigTypeDef(
    _ClientCreateDeliveryStreamExtendedS3DestinationConfigurationEncryptionConfigurationKMSEncryptionConfigTypeDef
):
    """
    Type definition for `ClientCreateDeliveryStreamExtendedS3DestinationConfigurationEncryptionConfiguration` `KMSEncryptionConfig`

    The encryption key.

    - **AWSKMSKeyARN** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region as
      the destination Amazon S3 bucket. For more information, see `Amazon Resource Names (ARNs)
      and AWS Service Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
    """


_ClientCreateDeliveryStreamExtendedS3DestinationConfigurationEncryptionConfigurationTypeDef = TypedDict(
    "_ClientCreateDeliveryStreamExtendedS3DestinationConfigurationEncryptionConfigurationTypeDef",
    {
        "NoEncryptionConfig": str,
        "KMSEncryptionConfig": ClientCreateDeliveryStreamExtendedS3DestinationConfigurationEncryptionConfigurationKMSEncryptionConfigTypeDef,
    },
    total=False,
)


class ClientCreateDeliveryStreamExtendedS3DestinationConfigurationEncryptionConfigurationTypeDef(
    _ClientCreateDeliveryStreamExtendedS3DestinationConfigurationEncryptionConfigurationTypeDef
):
    """
    Type definition for `ClientCreateDeliveryStreamExtendedS3DestinationConfiguration` `EncryptionConfiguration`

    The encryption configuration. If no value is specified, the default is no encryption.

    - **NoEncryptionConfig** *(string) --*

      Specifically override existing encryption information to ensure that no encryption is used.

    - **KMSEncryptionConfig** *(dict) --*

      The encryption key.

      - **AWSKMSKeyARN** *(string) --* **[REQUIRED]**

        The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region as
        the destination Amazon S3 bucket. For more information, see `Amazon Resource Names (ARNs)
        and AWS Service Namespaces
        <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
    """


_ClientCreateDeliveryStreamExtendedS3DestinationConfigurationProcessingConfigurationProcessorsParametersTypeDef = TypedDict(
    "_ClientCreateDeliveryStreamExtendedS3DestinationConfigurationProcessingConfigurationProcessorsParametersTypeDef",
    {"ParameterName": str, "ParameterValue": str},
)


class ClientCreateDeliveryStreamExtendedS3DestinationConfigurationProcessingConfigurationProcessorsParametersTypeDef(
    _ClientCreateDeliveryStreamExtendedS3DestinationConfigurationProcessingConfigurationProcessorsParametersTypeDef
):
    """
    Type definition for `ClientCreateDeliveryStreamExtendedS3DestinationConfigurationProcessingConfigurationProcessors` `Parameters`

    Describes the processor parameter.

    - **ParameterName** *(string) --* **[REQUIRED]**

      The name of the parameter.

    - **ParameterValue** *(string) --* **[REQUIRED]**

      The parameter value.
    """


_RequiredClientCreateDeliveryStreamExtendedS3DestinationConfigurationProcessingConfigurationProcessorsTypeDef = TypedDict(
    "_RequiredClientCreateDeliveryStreamExtendedS3DestinationConfigurationProcessingConfigurationProcessorsTypeDef",
    {"Type": str},
)
_OptionalClientCreateDeliveryStreamExtendedS3DestinationConfigurationProcessingConfigurationProcessorsTypeDef = TypedDict(
    "_OptionalClientCreateDeliveryStreamExtendedS3DestinationConfigurationProcessingConfigurationProcessorsTypeDef",
    {
        "Parameters": List[
            ClientCreateDeliveryStreamExtendedS3DestinationConfigurationProcessingConfigurationProcessorsParametersTypeDef
        ]
    },
    total=False,
)


class ClientCreateDeliveryStreamExtendedS3DestinationConfigurationProcessingConfigurationProcessorsTypeDef(
    _RequiredClientCreateDeliveryStreamExtendedS3DestinationConfigurationProcessingConfigurationProcessorsTypeDef,
    _OptionalClientCreateDeliveryStreamExtendedS3DestinationConfigurationProcessingConfigurationProcessorsTypeDef,
):
    """
    Type definition for `ClientCreateDeliveryStreamExtendedS3DestinationConfigurationProcessingConfiguration` `Processors`

    Describes a data processor.

    - **Type** *(string) --* **[REQUIRED]**

      The type of processor.

    - **Parameters** *(list) --*

      The processor parameters.

      - *(dict) --*

        Describes the processor parameter.

        - **ParameterName** *(string) --* **[REQUIRED]**

          The name of the parameter.

        - **ParameterValue** *(string) --* **[REQUIRED]**

          The parameter value.
    """


_ClientCreateDeliveryStreamExtendedS3DestinationConfigurationProcessingConfigurationTypeDef = TypedDict(
    "_ClientCreateDeliveryStreamExtendedS3DestinationConfigurationProcessingConfigurationTypeDef",
    {
        "Enabled": bool,
        "Processors": List[
            ClientCreateDeliveryStreamExtendedS3DestinationConfigurationProcessingConfigurationProcessorsTypeDef
        ],
    },
    total=False,
)


class ClientCreateDeliveryStreamExtendedS3DestinationConfigurationProcessingConfigurationTypeDef(
    _ClientCreateDeliveryStreamExtendedS3DestinationConfigurationProcessingConfigurationTypeDef
):
    """
    Type definition for `ClientCreateDeliveryStreamExtendedS3DestinationConfiguration` `ProcessingConfiguration`

    The data processing configuration.

    - **Enabled** *(boolean) --*

      Enables or disables data processing.

    - **Processors** *(list) --*

      The data processors.

      - *(dict) --*

        Describes a data processor.

        - **Type** *(string) --* **[REQUIRED]**

          The type of processor.

        - **Parameters** *(list) --*

          The processor parameters.

          - *(dict) --*

            Describes the processor parameter.

            - **ParameterName** *(string) --* **[REQUIRED]**

              The name of the parameter.

            - **ParameterValue** *(string) --* **[REQUIRED]**

              The parameter value.
    """


_ClientCreateDeliveryStreamExtendedS3DestinationConfigurationS3BackupConfigurationBufferingHintsTypeDef = TypedDict(
    "_ClientCreateDeliveryStreamExtendedS3DestinationConfigurationS3BackupConfigurationBufferingHintsTypeDef",
    {"SizeInMBs": int, "IntervalInSeconds": int},
    total=False,
)


class ClientCreateDeliveryStreamExtendedS3DestinationConfigurationS3BackupConfigurationBufferingHintsTypeDef(
    _ClientCreateDeliveryStreamExtendedS3DestinationConfigurationS3BackupConfigurationBufferingHintsTypeDef
):
    """
    Type definition for `ClientCreateDeliveryStreamExtendedS3DestinationConfigurationS3BackupConfiguration` `BufferingHints`

    The buffering option. If no value is specified, ``BufferingHints`` object default values are
    used.

    - **SizeInMBs** *(integer) --*

      Buffer incoming data to the specified size, in MiBs, before delivering it to the
      destination. The default value is 5. This parameter is optional but if you specify a value
      for it, you must also specify a value for ``IntervalInSeconds`` , and vice versa.

      We recommend setting this parameter to a value greater than the amount of data you
      typically ingest into the delivery stream in 10 seconds. For example, if you typically
      ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

    - **IntervalInSeconds** *(integer) --*

      Buffer incoming data for the specified period of time, in seconds, before delivering it to
      the destination. The default value is 300. This parameter is optional but if you specify a
      value for it, you must also specify a value for ``SizeInMBs`` , and vice versa.
    """


_ClientCreateDeliveryStreamExtendedS3DestinationConfigurationS3BackupConfigurationCloudWatchLoggingOptionsTypeDef = TypedDict(
    "_ClientCreateDeliveryStreamExtendedS3DestinationConfigurationS3BackupConfigurationCloudWatchLoggingOptionsTypeDef",
    {"Enabled": bool, "LogGroupName": str, "LogStreamName": str},
    total=False,
)


class ClientCreateDeliveryStreamExtendedS3DestinationConfigurationS3BackupConfigurationCloudWatchLoggingOptionsTypeDef(
    _ClientCreateDeliveryStreamExtendedS3DestinationConfigurationS3BackupConfigurationCloudWatchLoggingOptionsTypeDef
):
    """
    Type definition for `ClientCreateDeliveryStreamExtendedS3DestinationConfigurationS3BackupConfiguration` `CloudWatchLoggingOptions`

    The CloudWatch logging options for your delivery stream.

    - **Enabled** *(boolean) --*

      Enables or disables CloudWatch logging.

    - **LogGroupName** *(string) --*

      The CloudWatch group name for logging. This value is required if CloudWatch logging is
      enabled.

    - **LogStreamName** *(string) --*

      The CloudWatch log stream name for logging. This value is required if CloudWatch logging is
      enabled.
    """


_ClientCreateDeliveryStreamExtendedS3DestinationConfigurationS3BackupConfigurationEncryptionConfigurationKMSEncryptionConfigTypeDef = TypedDict(
    "_ClientCreateDeliveryStreamExtendedS3DestinationConfigurationS3BackupConfigurationEncryptionConfigurationKMSEncryptionConfigTypeDef",
    {"AWSKMSKeyARN": str},
)


class ClientCreateDeliveryStreamExtendedS3DestinationConfigurationS3BackupConfigurationEncryptionConfigurationKMSEncryptionConfigTypeDef(
    _ClientCreateDeliveryStreamExtendedS3DestinationConfigurationS3BackupConfigurationEncryptionConfigurationKMSEncryptionConfigTypeDef
):
    """
    Type definition for `ClientCreateDeliveryStreamExtendedS3DestinationConfigurationS3BackupConfigurationEncryptionConfiguration` `KMSEncryptionConfig`

    The encryption key.

    - **AWSKMSKeyARN** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region
      as the destination Amazon S3 bucket. For more information, see `Amazon Resource Names
      (ARNs) and AWS Service Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
    """


_ClientCreateDeliveryStreamExtendedS3DestinationConfigurationS3BackupConfigurationEncryptionConfigurationTypeDef = TypedDict(
    "_ClientCreateDeliveryStreamExtendedS3DestinationConfigurationS3BackupConfigurationEncryptionConfigurationTypeDef",
    {
        "NoEncryptionConfig": str,
        "KMSEncryptionConfig": ClientCreateDeliveryStreamExtendedS3DestinationConfigurationS3BackupConfigurationEncryptionConfigurationKMSEncryptionConfigTypeDef,
    },
    total=False,
)


class ClientCreateDeliveryStreamExtendedS3DestinationConfigurationS3BackupConfigurationEncryptionConfigurationTypeDef(
    _ClientCreateDeliveryStreamExtendedS3DestinationConfigurationS3BackupConfigurationEncryptionConfigurationTypeDef
):
    """
    Type definition for `ClientCreateDeliveryStreamExtendedS3DestinationConfigurationS3BackupConfiguration` `EncryptionConfiguration`

    The encryption configuration. If no value is specified, the default is no encryption.

    - **NoEncryptionConfig** *(string) --*

      Specifically override existing encryption information to ensure that no encryption is used.

    - **KMSEncryptionConfig** *(dict) --*

      The encryption key.

      - **AWSKMSKeyARN** *(string) --* **[REQUIRED]**

        The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region
        as the destination Amazon S3 bucket. For more information, see `Amazon Resource Names
        (ARNs) and AWS Service Namespaces
        <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
    """


_RequiredClientCreateDeliveryStreamExtendedS3DestinationConfigurationS3BackupConfigurationTypeDef = TypedDict(
    "_RequiredClientCreateDeliveryStreamExtendedS3DestinationConfigurationS3BackupConfigurationTypeDef",
    {"RoleARN": str, "BucketARN": str},
)
_OptionalClientCreateDeliveryStreamExtendedS3DestinationConfigurationS3BackupConfigurationTypeDef = TypedDict(
    "_OptionalClientCreateDeliveryStreamExtendedS3DestinationConfigurationS3BackupConfigurationTypeDef",
    {
        "Prefix": str,
        "ErrorOutputPrefix": str,
        "BufferingHints": ClientCreateDeliveryStreamExtendedS3DestinationConfigurationS3BackupConfigurationBufferingHintsTypeDef,
        "CompressionFormat": str,
        "EncryptionConfiguration": ClientCreateDeliveryStreamExtendedS3DestinationConfigurationS3BackupConfigurationEncryptionConfigurationTypeDef,
        "CloudWatchLoggingOptions": ClientCreateDeliveryStreamExtendedS3DestinationConfigurationS3BackupConfigurationCloudWatchLoggingOptionsTypeDef,
    },
    total=False,
)


class ClientCreateDeliveryStreamExtendedS3DestinationConfigurationS3BackupConfigurationTypeDef(
    _RequiredClientCreateDeliveryStreamExtendedS3DestinationConfigurationS3BackupConfigurationTypeDef,
    _OptionalClientCreateDeliveryStreamExtendedS3DestinationConfigurationS3BackupConfigurationTypeDef,
):
    """
    Type definition for `ClientCreateDeliveryStreamExtendedS3DestinationConfiguration` `S3BackupConfiguration`

    The configuration for backup in Amazon S3.

    - **RoleARN** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the AWS credentials. For more information, see `Amazon
      Resource Names (ARNs) and AWS Service Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

    - **BucketARN** *(string) --* **[REQUIRED]**

      The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs) and AWS
      Service Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

    - **Prefix** *(string) --*

      The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered Amazon S3 files.
      You can also specify a custom prefix, as described in `Custom Prefixes for Amazon S3 Objects
      <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

    - **ErrorOutputPrefix** *(string) --*

      A prefix that Kinesis Data Firehose evaluates and adds to failed records before writing them
      to S3. This prefix appears immediately following the bucket name. For information about how
      to specify this prefix, see `Custom Prefixes for Amazon S3 Objects
      <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

    - **BufferingHints** *(dict) --*

      The buffering option. If no value is specified, ``BufferingHints`` object default values are
      used.

      - **SizeInMBs** *(integer) --*

        Buffer incoming data to the specified size, in MiBs, before delivering it to the
        destination. The default value is 5. This parameter is optional but if you specify a value
        for it, you must also specify a value for ``IntervalInSeconds`` , and vice versa.

        We recommend setting this parameter to a value greater than the amount of data you
        typically ingest into the delivery stream in 10 seconds. For example, if you typically
        ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

      - **IntervalInSeconds** *(integer) --*

        Buffer incoming data for the specified period of time, in seconds, before delivering it to
        the destination. The default value is 300. This parameter is optional but if you specify a
        value for it, you must also specify a value for ``SizeInMBs`` , and vice versa.

    - **CompressionFormat** *(string) --*

      The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .

      The compression formats ``SNAPPY`` or ``ZIP`` cannot be specified for Amazon Redshift
      destinations because they are not supported by the Amazon Redshift ``COPY`` operation that
      reads from the S3 bucket.

    - **EncryptionConfiguration** *(dict) --*

      The encryption configuration. If no value is specified, the default is no encryption.

      - **NoEncryptionConfig** *(string) --*

        Specifically override existing encryption information to ensure that no encryption is used.

      - **KMSEncryptionConfig** *(dict) --*

        The encryption key.

        - **AWSKMSKeyARN** *(string) --* **[REQUIRED]**

          The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region
          as the destination Amazon S3 bucket. For more information, see `Amazon Resource Names
          (ARNs) and AWS Service Namespaces
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

    - **CloudWatchLoggingOptions** *(dict) --*

      The CloudWatch logging options for your delivery stream.

      - **Enabled** *(boolean) --*

        Enables or disables CloudWatch logging.

      - **LogGroupName** *(string) --*

        The CloudWatch group name for logging. This value is required if CloudWatch logging is
        enabled.

      - **LogStreamName** *(string) --*

        The CloudWatch log stream name for logging. This value is required if CloudWatch logging is
        enabled.
    """


_RequiredClientCreateDeliveryStreamExtendedS3DestinationConfigurationTypeDef = TypedDict(
    "_RequiredClientCreateDeliveryStreamExtendedS3DestinationConfigurationTypeDef",
    {"RoleARN": str, "BucketARN": str},
)
_OptionalClientCreateDeliveryStreamExtendedS3DestinationConfigurationTypeDef = TypedDict(
    "_OptionalClientCreateDeliveryStreamExtendedS3DestinationConfigurationTypeDef",
    {
        "Prefix": str,
        "ErrorOutputPrefix": str,
        "BufferingHints": ClientCreateDeliveryStreamExtendedS3DestinationConfigurationBufferingHintsTypeDef,
        "CompressionFormat": str,
        "EncryptionConfiguration": ClientCreateDeliveryStreamExtendedS3DestinationConfigurationEncryptionConfigurationTypeDef,
        "CloudWatchLoggingOptions": ClientCreateDeliveryStreamExtendedS3DestinationConfigurationCloudWatchLoggingOptionsTypeDef,
        "ProcessingConfiguration": ClientCreateDeliveryStreamExtendedS3DestinationConfigurationProcessingConfigurationTypeDef,
        "S3BackupMode": str,
        "S3BackupConfiguration": ClientCreateDeliveryStreamExtendedS3DestinationConfigurationS3BackupConfigurationTypeDef,
        "DataFormatConversionConfiguration": ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationTypeDef,
    },
    total=False,
)


class ClientCreateDeliveryStreamExtendedS3DestinationConfigurationTypeDef(
    _RequiredClientCreateDeliveryStreamExtendedS3DestinationConfigurationTypeDef,
    _OptionalClientCreateDeliveryStreamExtendedS3DestinationConfigurationTypeDef,
):
    """
    Type definition for `ClientCreateDeliveryStream` `ExtendedS3DestinationConfiguration`

    The destination in Amazon S3. You can specify only one destination.

    - **RoleARN** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the AWS credentials. For more information, see `Amazon
      Resource Names (ARNs) and AWS Service Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

    - **BucketARN** *(string) --* **[REQUIRED]**

      The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs) and AWS
      Service Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

    - **Prefix** *(string) --*

      The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered Amazon S3 files. You
      can also specify a custom prefix, as described in `Custom Prefixes for Amazon S3 Objects
      <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

    - **ErrorOutputPrefix** *(string) --*

      A prefix that Kinesis Data Firehose evaluates and adds to failed records before writing them to
      S3. This prefix appears immediately following the bucket name. For information about how to
      specify this prefix, see `Custom Prefixes for Amazon S3 Objects
      <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

    - **BufferingHints** *(dict) --*

      The buffering option.

      - **SizeInMBs** *(integer) --*

        Buffer incoming data to the specified size, in MiBs, before delivering it to the destination.
        The default value is 5. This parameter is optional but if you specify a value for it, you
        must also specify a value for ``IntervalInSeconds`` , and vice versa.

        We recommend setting this parameter to a value greater than the amount of data you typically
        ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1
        MiB/sec, the value should be 10 MiB or higher.

      - **IntervalInSeconds** *(integer) --*

        Buffer incoming data for the specified period of time, in seconds, before delivering it to
        the destination. The default value is 300. This parameter is optional but if you specify a
        value for it, you must also specify a value for ``SizeInMBs`` , and vice versa.

    - **CompressionFormat** *(string) --*

      The compression format. If no value is specified, the default is UNCOMPRESSED.

    - **EncryptionConfiguration** *(dict) --*

      The encryption configuration. If no value is specified, the default is no encryption.

      - **NoEncryptionConfig** *(string) --*

        Specifically override existing encryption information to ensure that no encryption is used.

      - **KMSEncryptionConfig** *(dict) --*

        The encryption key.

        - **AWSKMSKeyARN** *(string) --* **[REQUIRED]**

          The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region as
          the destination Amazon S3 bucket. For more information, see `Amazon Resource Names (ARNs)
          and AWS Service Namespaces
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

    - **CloudWatchLoggingOptions** *(dict) --*

      The Amazon CloudWatch logging options for your delivery stream.

      - **Enabled** *(boolean) --*

        Enables or disables CloudWatch logging.

      - **LogGroupName** *(string) --*

        The CloudWatch group name for logging. This value is required if CloudWatch logging is
        enabled.

      - **LogStreamName** *(string) --*

        The CloudWatch log stream name for logging. This value is required if CloudWatch logging is
        enabled.

    - **ProcessingConfiguration** *(dict) --*

      The data processing configuration.

      - **Enabled** *(boolean) --*

        Enables or disables data processing.

      - **Processors** *(list) --*

        The data processors.

        - *(dict) --*

          Describes a data processor.

          - **Type** *(string) --* **[REQUIRED]**

            The type of processor.

          - **Parameters** *(list) --*

            The processor parameters.

            - *(dict) --*

              Describes the processor parameter.

              - **ParameterName** *(string) --* **[REQUIRED]**

                The name of the parameter.

              - **ParameterValue** *(string) --* **[REQUIRED]**

                The parameter value.

    - **S3BackupMode** *(string) --*

      The Amazon S3 backup mode.

    - **S3BackupConfiguration** *(dict) --*

      The configuration for backup in Amazon S3.

      - **RoleARN** *(string) --* **[REQUIRED]**

        The Amazon Resource Name (ARN) of the AWS credentials. For more information, see `Amazon
        Resource Names (ARNs) and AWS Service Namespaces
        <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

      - **BucketARN** *(string) --* **[REQUIRED]**

        The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs) and AWS
        Service Namespaces
        <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

      - **Prefix** *(string) --*

        The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered Amazon S3 files.
        You can also specify a custom prefix, as described in `Custom Prefixes for Amazon S3 Objects
        <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

      - **ErrorOutputPrefix** *(string) --*

        A prefix that Kinesis Data Firehose evaluates and adds to failed records before writing them
        to S3. This prefix appears immediately following the bucket name. For information about how
        to specify this prefix, see `Custom Prefixes for Amazon S3 Objects
        <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

      - **BufferingHints** *(dict) --*

        The buffering option. If no value is specified, ``BufferingHints`` object default values are
        used.

        - **SizeInMBs** *(integer) --*

          Buffer incoming data to the specified size, in MiBs, before delivering it to the
          destination. The default value is 5. This parameter is optional but if you specify a value
          for it, you must also specify a value for ``IntervalInSeconds`` , and vice versa.

          We recommend setting this parameter to a value greater than the amount of data you
          typically ingest into the delivery stream in 10 seconds. For example, if you typically
          ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

        - **IntervalInSeconds** *(integer) --*

          Buffer incoming data for the specified period of time, in seconds, before delivering it to
          the destination. The default value is 300. This parameter is optional but if you specify a
          value for it, you must also specify a value for ``SizeInMBs`` , and vice versa.

      - **CompressionFormat** *(string) --*

        The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .

        The compression formats ``SNAPPY`` or ``ZIP`` cannot be specified for Amazon Redshift
        destinations because they are not supported by the Amazon Redshift ``COPY`` operation that
        reads from the S3 bucket.

      - **EncryptionConfiguration** *(dict) --*

        The encryption configuration. If no value is specified, the default is no encryption.

        - **NoEncryptionConfig** *(string) --*

          Specifically override existing encryption information to ensure that no encryption is used.

        - **KMSEncryptionConfig** *(dict) --*

          The encryption key.

          - **AWSKMSKeyARN** *(string) --* **[REQUIRED]**

            The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region
            as the destination Amazon S3 bucket. For more information, see `Amazon Resource Names
            (ARNs) and AWS Service Namespaces
            <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

      - **CloudWatchLoggingOptions** *(dict) --*

        The CloudWatch logging options for your delivery stream.

        - **Enabled** *(boolean) --*

          Enables or disables CloudWatch logging.

        - **LogGroupName** *(string) --*

          The CloudWatch group name for logging. This value is required if CloudWatch logging is
          enabled.

        - **LogStreamName** *(string) --*

          The CloudWatch log stream name for logging. This value is required if CloudWatch logging is
          enabled.

    - **DataFormatConversionConfiguration** *(dict) --*

      The serializer, deserializer, and schema for converting data from the JSON format to the
      Parquet or ORC format before writing it to Amazon S3.

      - **SchemaConfiguration** *(dict) --*

        Specifies the AWS Glue Data Catalog table that contains the column information.

        - **RoleARN** *(string) --*

          The role that Kinesis Data Firehose can use to access AWS Glue. This role must be in the
          same account you use for Kinesis Data Firehose. Cross-account roles aren't allowed.

        - **CatalogId** *(string) --*

          The ID of the AWS Glue Data Catalog. If you don't supply this, the AWS account ID is used
          by default.

        - **DatabaseName** *(string) --*

          Specifies the name of the AWS Glue database that contains the schema for the output data.

        - **TableName** *(string) --*

          Specifies the AWS Glue table that contains the column information that constitutes your
          data schema.

        - **Region** *(string) --*

          If you don't specify an AWS Region, the default is the current Region.

        - **VersionId** *(string) --*

          Specifies the table version for the output data schema. If you don't specify this version
          ID, or if you set it to ``LATEST`` , Kinesis Data Firehose uses the most recent version.
          This means that any updates to the table are automatically picked up.

      - **InputFormatConfiguration** *(dict) --*

        Specifies the deserializer that you want Kinesis Data Firehose to use to convert the format
        of your data from JSON.

        - **Deserializer** *(dict) --*

          Specifies which deserializer to use. You can choose either the Apache Hive JSON SerDe or
          the OpenX JSON SerDe. If both are non-null, the server rejects the request.

          - **OpenXJsonSerDe** *(dict) --*

            The OpenX SerDe. Used by Kinesis Data Firehose for deserializing data, which means
            converting it from the JSON format in preparation for serializing it to the Parquet or
            ORC format. This is one of two deserializers you can choose, depending on which one
            offers the functionality you need. The other option is the native Hive / HCatalog
            JsonSerDe.

            - **ConvertDotsInJsonKeysToUnderscores** *(boolean) --*

              When set to ``true`` , specifies that the names of the keys include dots and that you
              want Kinesis Data Firehose to replace them with underscores. This is useful because
              Apache Hive does not allow dots in column names. For example, if the JSON contains a
              key whose name is "a.b", you can define the column name to be "a_b" when using this
              option.

              The default is ``false`` .

            - **CaseInsensitive** *(boolean) --*

              When set to ``true`` , which is the default, Kinesis Data Firehose converts JSON keys
              to lowercase before deserializing them.

            - **ColumnToJsonKeyMappings** *(dict) --*

              Maps column names to JSON keys that aren't identical to the column names. This is
              useful when the JSON contains keys that are Hive keywords. For example, ``timestamp``
              is a Hive keyword. If you have a JSON key named ``timestamp`` , set this parameter to
              ``{"ts": "timestamp"}`` to map this key to a column named ``ts`` .

              - *(string) --*

                - *(string) --*

          - **HiveJsonSerDe** *(dict) --*

            The native Hive / HCatalog JsonSerDe. Used by Kinesis Data Firehose for deserializing
            data, which means converting it from the JSON format in preparation for serializing it to
            the Parquet or ORC format. This is one of two deserializers you can choose, depending on
            which one offers the functionality you need. The other option is the OpenX SerDe.

            - **TimestampFormats** *(list) --*

              Indicates how you want Kinesis Data Firehose to parse the date and timestamps that may
              be present in your input data JSON. To specify these format strings, follow the pattern
              syntax of JodaTime's DateTimeFormat format strings. For more information, see `Class
              DateTimeFormat
              <https://www.joda.org/joda-time/apidocs/org/joda/time/format/DateTimeFormat.html>`__ .
              You can also use the special value ``millis`` to parse timestamps in epoch
              milliseconds. If you don't specify a format, Kinesis Data Firehose uses
              ``java.sql.Timestamp::valueOf`` by default.

              - *(string) --*

      - **OutputFormatConfiguration** *(dict) --*

        Specifies the serializer that you want Kinesis Data Firehose to use to convert the format of
        your data to the Parquet or ORC format.

        - **Serializer** *(dict) --*

          Specifies which serializer to use. You can choose either the ORC SerDe or the Parquet
          SerDe. If both are non-null, the server rejects the request.

          - **ParquetSerDe** *(dict) --*

            A serializer to use for converting data to the Parquet format before storing it in Amazon
            S3. For more information, see `Apache Parquet
            <https://parquet.apache.org/documentation/latest/>`__ .

            - **BlockSizeBytes** *(integer) --*

              The Hadoop Distributed File System (HDFS) block size. This is useful if you intend to
              copy the data from Amazon S3 to HDFS before querying. The default is 256 MiB and the
              minimum is 64 MiB. Kinesis Data Firehose uses this value for padding calculations.

            - **PageSizeBytes** *(integer) --*

              The Parquet page size. Column chunks are divided into pages. A page is conceptually an
              indivisible unit (in terms of compression and encoding). The minimum value is 64 KiB
              and the default is 1 MiB.

            - **Compression** *(string) --*

              The compression code to use over data blocks. The possible values are ``UNCOMPRESSED``
              , ``SNAPPY`` , and ``GZIP`` , with the default being ``SNAPPY`` . Use ``SNAPPY`` for
              higher decompression speed. Use ``GZIP`` if the compression ration is more important
              than speed.

            - **EnableDictionaryCompression** *(boolean) --*

              Indicates whether to enable dictionary compression.

            - **MaxPaddingBytes** *(integer) --*

              The maximum amount of padding to apply. This is useful if you intend to copy the data
              from Amazon S3 to HDFS before querying. The default is 0.

            - **WriterVersion** *(string) --*

              Indicates the version of row format to output. The possible values are ``V1`` and
              ``V2`` . The default is ``V1`` .

          - **OrcSerDe** *(dict) --*

            A serializer to use for converting data to the ORC format before storing it in Amazon S3.
            For more information, see `Apache ORC <https://orc.apache.org/docs/>`__ .

            - **StripeSizeBytes** *(integer) --*

              The number of bytes in each stripe. The default is 64 MiB and the minimum is 8 MiB.

            - **BlockSizeBytes** *(integer) --*

              The Hadoop Distributed File System (HDFS) block size. This is useful if you intend to
              copy the data from Amazon S3 to HDFS before querying. The default is 256 MiB and the
              minimum is 64 MiB. Kinesis Data Firehose uses this value for padding calculations.

            - **RowIndexStride** *(integer) --*

              The number of rows between index entries. The default is 10,000 and the minimum is
              1,000.

            - **EnablePadding** *(boolean) --*

              Set this to ``true`` to indicate that you want stripes to be padded to the HDFS block
              boundaries. This is useful if you intend to copy the data from Amazon S3 to HDFS before
              querying. The default is ``false`` .

            - **PaddingTolerance** *(float) --*

              A number between 0 and 1 that defines the tolerance for block padding as a decimal
              fraction of stripe size. The default value is 0.05, which means 5 percent of stripe
              size.

              For the default values of 64 MiB ORC stripes and 256 MiB HDFS blocks, the default block
              padding tolerance of 5 percent reserves a maximum of 3.2 MiB for padding within the 256
              MiB block. In such a case, if the available size within the block is more than 3.2 MiB,
              a new, smaller stripe is inserted to fit within that space. This ensures that no stripe
              crosses block boundaries and causes remote reads within a node-local task.

              Kinesis Data Firehose ignores this parameter when  OrcSerDe$EnablePadding is ``false`` .

            - **Compression** *(string) --*

              The compression code to use over data blocks. The default is ``SNAPPY`` .

            - **BloomFilterColumns** *(list) --*

              The column names for which you want Kinesis Data Firehose to create bloom filters. The
              default is ``null`` .

              - *(string) --*

            - **BloomFilterFalsePositiveProbability** *(float) --*

              The Bloom filter false positive probability (FPP). The lower the FPP, the bigger the
              Bloom filter. The default value is 0.05, the minimum is 0, and the maximum is 1.

            - **DictionaryKeyThreshold** *(float) --*

              Represents the fraction of the total number of non-null rows. To turn off dictionary
              encoding, set this fraction to a number that is less than the number of distinct keys
              in a dictionary. To always use dictionary encoding, set this threshold to 1.

            - **FormatVersion** *(string) --*

              The version of the file to write. The possible values are ``V0_11`` and ``V0_12`` . The
              default is ``V0_12`` .

      - **Enabled** *(boolean) --*

        Defaults to ``true`` . Set it to ``false`` if you want to disable format conversion while
        preserving the configuration details.
    """


_ClientCreateDeliveryStreamKinesisStreamSourceConfigurationTypeDef = TypedDict(
    "_ClientCreateDeliveryStreamKinesisStreamSourceConfigurationTypeDef",
    {"KinesisStreamARN": str, "RoleARN": str},
)


class ClientCreateDeliveryStreamKinesisStreamSourceConfigurationTypeDef(
    _ClientCreateDeliveryStreamKinesisStreamSourceConfigurationTypeDef
):
    """
    Type definition for `ClientCreateDeliveryStream` `KinesisStreamSourceConfiguration`

    When a Kinesis data stream is used as the source for the delivery stream, a
    KinesisStreamSourceConfiguration containing the Kinesis data stream Amazon Resource Name (ARN)
    and the role ARN for the source stream.

    - **KinesisStreamARN** *(string) --* **[REQUIRED]**

      The ARN of the source Kinesis data stream. For more information, see `Amazon Kinesis Data
      Streams ARN Format
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-kinesis-streams>`__
      .

    - **RoleARN** *(string) --* **[REQUIRED]**

      The ARN of the role that provides access to the source Kinesis data stream. For more
      information, see `AWS Identity and Access Management (IAM) ARN Format
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-iam>`__ .
    """


_ClientCreateDeliveryStreamRedshiftDestinationConfigurationCloudWatchLoggingOptionsTypeDef = TypedDict(
    "_ClientCreateDeliveryStreamRedshiftDestinationConfigurationCloudWatchLoggingOptionsTypeDef",
    {"Enabled": bool, "LogGroupName": str, "LogStreamName": str},
    total=False,
)


class ClientCreateDeliveryStreamRedshiftDestinationConfigurationCloudWatchLoggingOptionsTypeDef(
    _ClientCreateDeliveryStreamRedshiftDestinationConfigurationCloudWatchLoggingOptionsTypeDef
):
    """
    Type definition for `ClientCreateDeliveryStreamRedshiftDestinationConfiguration` `CloudWatchLoggingOptions`

    The CloudWatch logging options for your delivery stream.

    - **Enabled** *(boolean) --*

      Enables or disables CloudWatch logging.

    - **LogGroupName** *(string) --*

      The CloudWatch group name for logging. This value is required if CloudWatch logging is
      enabled.

    - **LogStreamName** *(string) --*

      The CloudWatch log stream name for logging. This value is required if CloudWatch logging is
      enabled.
    """


_RequiredClientCreateDeliveryStreamRedshiftDestinationConfigurationCopyCommandTypeDef = TypedDict(
    "_RequiredClientCreateDeliveryStreamRedshiftDestinationConfigurationCopyCommandTypeDef",
    {"DataTableName": str},
)
_OptionalClientCreateDeliveryStreamRedshiftDestinationConfigurationCopyCommandTypeDef = TypedDict(
    "_OptionalClientCreateDeliveryStreamRedshiftDestinationConfigurationCopyCommandTypeDef",
    {"DataTableColumns": str, "CopyOptions": str},
    total=False,
)


class ClientCreateDeliveryStreamRedshiftDestinationConfigurationCopyCommandTypeDef(
    _RequiredClientCreateDeliveryStreamRedshiftDestinationConfigurationCopyCommandTypeDef,
    _OptionalClientCreateDeliveryStreamRedshiftDestinationConfigurationCopyCommandTypeDef,
):
    """
    Type definition for `ClientCreateDeliveryStreamRedshiftDestinationConfiguration` `CopyCommand`

    The ``COPY`` command.

    - **DataTableName** *(string) --* **[REQUIRED]**

      The name of the target table. The table must already exist in the database.

    - **DataTableColumns** *(string) --*

      A comma-separated list of column names.

    - **CopyOptions** *(string) --*

      Optional parameters to use with the Amazon Redshift ``COPY`` command. For more information,
      see the "Optional Parameters" section of `Amazon Redshift COPY command
      <https://docs.aws.amazon.com/redshift/latest/dg/r_COPY.html>`__ . Some possible examples that
      would apply to Kinesis Data Firehose are as follows:

       ``delimiter '\\t' lzop;`` - fields are delimited with "\\t" (TAB character) and compressed
       using lzop.

       ``delimiter '|'`` - fields are delimited with "|" (this is the default delimiter).

       ``delimiter '|' escape`` - the delimiter should be escaped.

       ``fixedwidth 'venueid:3,venuename:25,venuecity:12,venuestate:2,venueseats:6'`` - fields are
       fixed width in the source, with each width specified after every column in the table.

       ``JSON 's3://mybucket/jsonpaths.txt'`` - data is in JSON format, and the path specified is
       the format of the data.

      For more examples, see `Amazon Redshift COPY command examples
      <https://docs.aws.amazon.com/redshift/latest/dg/r_COPY_command_examples.html>`__ .
    """


_ClientCreateDeliveryStreamRedshiftDestinationConfigurationProcessingConfigurationProcessorsParametersTypeDef = TypedDict(
    "_ClientCreateDeliveryStreamRedshiftDestinationConfigurationProcessingConfigurationProcessorsParametersTypeDef",
    {"ParameterName": str, "ParameterValue": str},
)


class ClientCreateDeliveryStreamRedshiftDestinationConfigurationProcessingConfigurationProcessorsParametersTypeDef(
    _ClientCreateDeliveryStreamRedshiftDestinationConfigurationProcessingConfigurationProcessorsParametersTypeDef
):
    """
    Type definition for `ClientCreateDeliveryStreamRedshiftDestinationConfigurationProcessingConfigurationProcessors` `Parameters`

    Describes the processor parameter.

    - **ParameterName** *(string) --* **[REQUIRED]**

      The name of the parameter.

    - **ParameterValue** *(string) --* **[REQUIRED]**

      The parameter value.
    """


_RequiredClientCreateDeliveryStreamRedshiftDestinationConfigurationProcessingConfigurationProcessorsTypeDef = TypedDict(
    "_RequiredClientCreateDeliveryStreamRedshiftDestinationConfigurationProcessingConfigurationProcessorsTypeDef",
    {"Type": str},
)
_OptionalClientCreateDeliveryStreamRedshiftDestinationConfigurationProcessingConfigurationProcessorsTypeDef = TypedDict(
    "_OptionalClientCreateDeliveryStreamRedshiftDestinationConfigurationProcessingConfigurationProcessorsTypeDef",
    {
        "Parameters": List[
            ClientCreateDeliveryStreamRedshiftDestinationConfigurationProcessingConfigurationProcessorsParametersTypeDef
        ]
    },
    total=False,
)


class ClientCreateDeliveryStreamRedshiftDestinationConfigurationProcessingConfigurationProcessorsTypeDef(
    _RequiredClientCreateDeliveryStreamRedshiftDestinationConfigurationProcessingConfigurationProcessorsTypeDef,
    _OptionalClientCreateDeliveryStreamRedshiftDestinationConfigurationProcessingConfigurationProcessorsTypeDef,
):
    """
    Type definition for `ClientCreateDeliveryStreamRedshiftDestinationConfigurationProcessingConfiguration` `Processors`

    Describes a data processor.

    - **Type** *(string) --* **[REQUIRED]**

      The type of processor.

    - **Parameters** *(list) --*

      The processor parameters.

      - *(dict) --*

        Describes the processor parameter.

        - **ParameterName** *(string) --* **[REQUIRED]**

          The name of the parameter.

        - **ParameterValue** *(string) --* **[REQUIRED]**

          The parameter value.
    """


_ClientCreateDeliveryStreamRedshiftDestinationConfigurationProcessingConfigurationTypeDef = TypedDict(
    "_ClientCreateDeliveryStreamRedshiftDestinationConfigurationProcessingConfigurationTypeDef",
    {
        "Enabled": bool,
        "Processors": List[
            ClientCreateDeliveryStreamRedshiftDestinationConfigurationProcessingConfigurationProcessorsTypeDef
        ],
    },
    total=False,
)


class ClientCreateDeliveryStreamRedshiftDestinationConfigurationProcessingConfigurationTypeDef(
    _ClientCreateDeliveryStreamRedshiftDestinationConfigurationProcessingConfigurationTypeDef
):
    """
    Type definition for `ClientCreateDeliveryStreamRedshiftDestinationConfiguration` `ProcessingConfiguration`

    The data processing configuration.

    - **Enabled** *(boolean) --*

      Enables or disables data processing.

    - **Processors** *(list) --*

      The data processors.

      - *(dict) --*

        Describes a data processor.

        - **Type** *(string) --* **[REQUIRED]**

          The type of processor.

        - **Parameters** *(list) --*

          The processor parameters.

          - *(dict) --*

            Describes the processor parameter.

            - **ParameterName** *(string) --* **[REQUIRED]**

              The name of the parameter.

            - **ParameterValue** *(string) --* **[REQUIRED]**

              The parameter value.
    """


_ClientCreateDeliveryStreamRedshiftDestinationConfigurationRetryOptionsTypeDef = TypedDict(
    "_ClientCreateDeliveryStreamRedshiftDestinationConfigurationRetryOptionsTypeDef",
    {"DurationInSeconds": int},
    total=False,
)


class ClientCreateDeliveryStreamRedshiftDestinationConfigurationRetryOptionsTypeDef(
    _ClientCreateDeliveryStreamRedshiftDestinationConfigurationRetryOptionsTypeDef
):
    """
    Type definition for `ClientCreateDeliveryStreamRedshiftDestinationConfiguration` `RetryOptions`

    The retry behavior in case Kinesis Data Firehose is unable to deliver documents to Amazon
    Redshift. Default value is 3600 (60 minutes).

    - **DurationInSeconds** *(integer) --*

      The length of time during which Kinesis Data Firehose retries delivery after a failure,
      starting from the initial request and including the first attempt. The default value is 3600
      seconds (60 minutes). Kinesis Data Firehose does not retry if the value of
      ``DurationInSeconds`` is 0 (zero) or if the first delivery attempt takes longer than the
      current value.
    """


_ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3BackupConfigurationBufferingHintsTypeDef = TypedDict(
    "_ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3BackupConfigurationBufferingHintsTypeDef",
    {"SizeInMBs": int, "IntervalInSeconds": int},
    total=False,
)


class ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3BackupConfigurationBufferingHintsTypeDef(
    _ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3BackupConfigurationBufferingHintsTypeDef
):
    """
    Type definition for `ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3BackupConfiguration` `BufferingHints`

    The buffering option. If no value is specified, ``BufferingHints`` object default values are
    used.

    - **SizeInMBs** *(integer) --*

      Buffer incoming data to the specified size, in MiBs, before delivering it to the
      destination. The default value is 5. This parameter is optional but if you specify a value
      for it, you must also specify a value for ``IntervalInSeconds`` , and vice versa.

      We recommend setting this parameter to a value greater than the amount of data you
      typically ingest into the delivery stream in 10 seconds. For example, if you typically
      ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

    - **IntervalInSeconds** *(integer) --*

      Buffer incoming data for the specified period of time, in seconds, before delivering it to
      the destination. The default value is 300. This parameter is optional but if you specify a
      value for it, you must also specify a value for ``SizeInMBs`` , and vice versa.
    """


_ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3BackupConfigurationCloudWatchLoggingOptionsTypeDef = TypedDict(
    "_ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3BackupConfigurationCloudWatchLoggingOptionsTypeDef",
    {"Enabled": bool, "LogGroupName": str, "LogStreamName": str},
    total=False,
)


class ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3BackupConfigurationCloudWatchLoggingOptionsTypeDef(
    _ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3BackupConfigurationCloudWatchLoggingOptionsTypeDef
):
    """
    Type definition for `ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3BackupConfiguration` `CloudWatchLoggingOptions`

    The CloudWatch logging options for your delivery stream.

    - **Enabled** *(boolean) --*

      Enables or disables CloudWatch logging.

    - **LogGroupName** *(string) --*

      The CloudWatch group name for logging. This value is required if CloudWatch logging is
      enabled.

    - **LogStreamName** *(string) --*

      The CloudWatch log stream name for logging. This value is required if CloudWatch logging is
      enabled.
    """


_ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3BackupConfigurationEncryptionConfigurationKMSEncryptionConfigTypeDef = TypedDict(
    "_ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3BackupConfigurationEncryptionConfigurationKMSEncryptionConfigTypeDef",
    {"AWSKMSKeyARN": str},
)


class ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3BackupConfigurationEncryptionConfigurationKMSEncryptionConfigTypeDef(
    _ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3BackupConfigurationEncryptionConfigurationKMSEncryptionConfigTypeDef
):
    """
    Type definition for `ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3BackupConfigurationEncryptionConfiguration` `KMSEncryptionConfig`

    The encryption key.

    - **AWSKMSKeyARN** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region
      as the destination Amazon S3 bucket. For more information, see `Amazon Resource Names
      (ARNs) and AWS Service Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
    """


_ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3BackupConfigurationEncryptionConfigurationTypeDef = TypedDict(
    "_ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3BackupConfigurationEncryptionConfigurationTypeDef",
    {
        "NoEncryptionConfig": str,
        "KMSEncryptionConfig": ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3BackupConfigurationEncryptionConfigurationKMSEncryptionConfigTypeDef,
    },
    total=False,
)


class ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3BackupConfigurationEncryptionConfigurationTypeDef(
    _ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3BackupConfigurationEncryptionConfigurationTypeDef
):
    """
    Type definition for `ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3BackupConfiguration` `EncryptionConfiguration`

    The encryption configuration. If no value is specified, the default is no encryption.

    - **NoEncryptionConfig** *(string) --*

      Specifically override existing encryption information to ensure that no encryption is used.

    - **KMSEncryptionConfig** *(dict) --*

      The encryption key.

      - **AWSKMSKeyARN** *(string) --* **[REQUIRED]**

        The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region
        as the destination Amazon S3 bucket. For more information, see `Amazon Resource Names
        (ARNs) and AWS Service Namespaces
        <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
    """


_RequiredClientCreateDeliveryStreamRedshiftDestinationConfigurationS3BackupConfigurationTypeDef = TypedDict(
    "_RequiredClientCreateDeliveryStreamRedshiftDestinationConfigurationS3BackupConfigurationTypeDef",
    {"RoleARN": str, "BucketARN": str},
)
_OptionalClientCreateDeliveryStreamRedshiftDestinationConfigurationS3BackupConfigurationTypeDef = TypedDict(
    "_OptionalClientCreateDeliveryStreamRedshiftDestinationConfigurationS3BackupConfigurationTypeDef",
    {
        "Prefix": str,
        "ErrorOutputPrefix": str,
        "BufferingHints": ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3BackupConfigurationBufferingHintsTypeDef,
        "CompressionFormat": str,
        "EncryptionConfiguration": ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3BackupConfigurationEncryptionConfigurationTypeDef,
        "CloudWatchLoggingOptions": ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3BackupConfigurationCloudWatchLoggingOptionsTypeDef,
    },
    total=False,
)


class ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3BackupConfigurationTypeDef(
    _RequiredClientCreateDeliveryStreamRedshiftDestinationConfigurationS3BackupConfigurationTypeDef,
    _OptionalClientCreateDeliveryStreamRedshiftDestinationConfigurationS3BackupConfigurationTypeDef,
):
    """
    Type definition for `ClientCreateDeliveryStreamRedshiftDestinationConfiguration` `S3BackupConfiguration`

    The configuration for backup in Amazon S3.

    - **RoleARN** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the AWS credentials. For more information, see `Amazon
      Resource Names (ARNs) and AWS Service Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

    - **BucketARN** *(string) --* **[REQUIRED]**

      The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs) and AWS
      Service Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

    - **Prefix** *(string) --*

      The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered Amazon S3 files.
      You can also specify a custom prefix, as described in `Custom Prefixes for Amazon S3 Objects
      <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

    - **ErrorOutputPrefix** *(string) --*

      A prefix that Kinesis Data Firehose evaluates and adds to failed records before writing them
      to S3. This prefix appears immediately following the bucket name. For information about how
      to specify this prefix, see `Custom Prefixes for Amazon S3 Objects
      <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

    - **BufferingHints** *(dict) --*

      The buffering option. If no value is specified, ``BufferingHints`` object default values are
      used.

      - **SizeInMBs** *(integer) --*

        Buffer incoming data to the specified size, in MiBs, before delivering it to the
        destination. The default value is 5. This parameter is optional but if you specify a value
        for it, you must also specify a value for ``IntervalInSeconds`` , and vice versa.

        We recommend setting this parameter to a value greater than the amount of data you
        typically ingest into the delivery stream in 10 seconds. For example, if you typically
        ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

      - **IntervalInSeconds** *(integer) --*

        Buffer incoming data for the specified period of time, in seconds, before delivering it to
        the destination. The default value is 300. This parameter is optional but if you specify a
        value for it, you must also specify a value for ``SizeInMBs`` , and vice versa.

    - **CompressionFormat** *(string) --*

      The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .

      The compression formats ``SNAPPY`` or ``ZIP`` cannot be specified for Amazon Redshift
      destinations because they are not supported by the Amazon Redshift ``COPY`` operation that
      reads from the S3 bucket.

    - **EncryptionConfiguration** *(dict) --*

      The encryption configuration. If no value is specified, the default is no encryption.

      - **NoEncryptionConfig** *(string) --*

        Specifically override existing encryption information to ensure that no encryption is used.

      - **KMSEncryptionConfig** *(dict) --*

        The encryption key.

        - **AWSKMSKeyARN** *(string) --* **[REQUIRED]**

          The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region
          as the destination Amazon S3 bucket. For more information, see `Amazon Resource Names
          (ARNs) and AWS Service Namespaces
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

    - **CloudWatchLoggingOptions** *(dict) --*

      The CloudWatch logging options for your delivery stream.

      - **Enabled** *(boolean) --*

        Enables or disables CloudWatch logging.

      - **LogGroupName** *(string) --*

        The CloudWatch group name for logging. This value is required if CloudWatch logging is
        enabled.

      - **LogStreamName** *(string) --*

        The CloudWatch log stream name for logging. This value is required if CloudWatch logging is
        enabled.
    """


_ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3ConfigurationBufferingHintsTypeDef = TypedDict(
    "_ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3ConfigurationBufferingHintsTypeDef",
    {"SizeInMBs": int, "IntervalInSeconds": int},
    total=False,
)


class ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3ConfigurationBufferingHintsTypeDef(
    _ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3ConfigurationBufferingHintsTypeDef
):
    """
    Type definition for `ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3Configuration` `BufferingHints`

    The buffering option. If no value is specified, ``BufferingHints`` object default values are
    used.

    - **SizeInMBs** *(integer) --*

      Buffer incoming data to the specified size, in MiBs, before delivering it to the
      destination. The default value is 5. This parameter is optional but if you specify a value
      for it, you must also specify a value for ``IntervalInSeconds`` , and vice versa.

      We recommend setting this parameter to a value greater than the amount of data you
      typically ingest into the delivery stream in 10 seconds. For example, if you typically
      ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

    - **IntervalInSeconds** *(integer) --*

      Buffer incoming data for the specified period of time, in seconds, before delivering it to
      the destination. The default value is 300. This parameter is optional but if you specify a
      value for it, you must also specify a value for ``SizeInMBs`` , and vice versa.
    """


_ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3ConfigurationCloudWatchLoggingOptionsTypeDef = TypedDict(
    "_ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3ConfigurationCloudWatchLoggingOptionsTypeDef",
    {"Enabled": bool, "LogGroupName": str, "LogStreamName": str},
    total=False,
)


class ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3ConfigurationCloudWatchLoggingOptionsTypeDef(
    _ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3ConfigurationCloudWatchLoggingOptionsTypeDef
):
    """
    Type definition for `ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3Configuration` `CloudWatchLoggingOptions`

    The CloudWatch logging options for your delivery stream.

    - **Enabled** *(boolean) --*

      Enables or disables CloudWatch logging.

    - **LogGroupName** *(string) --*

      The CloudWatch group name for logging. This value is required if CloudWatch logging is
      enabled.

    - **LogStreamName** *(string) --*

      The CloudWatch log stream name for logging. This value is required if CloudWatch logging is
      enabled.
    """


_ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3ConfigurationEncryptionConfigurationKMSEncryptionConfigTypeDef = TypedDict(
    "_ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3ConfigurationEncryptionConfigurationKMSEncryptionConfigTypeDef",
    {"AWSKMSKeyARN": str},
)


class ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3ConfigurationEncryptionConfigurationKMSEncryptionConfigTypeDef(
    _ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3ConfigurationEncryptionConfigurationKMSEncryptionConfigTypeDef
):
    """
    Type definition for `ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3ConfigurationEncryptionConfiguration` `KMSEncryptionConfig`

    The encryption key.

    - **AWSKMSKeyARN** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region
      as the destination Amazon S3 bucket. For more information, see `Amazon Resource Names
      (ARNs) and AWS Service Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
    """


_ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3ConfigurationEncryptionConfigurationTypeDef = TypedDict(
    "_ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3ConfigurationEncryptionConfigurationTypeDef",
    {
        "NoEncryptionConfig": str,
        "KMSEncryptionConfig": ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3ConfigurationEncryptionConfigurationKMSEncryptionConfigTypeDef,
    },
    total=False,
)


class ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3ConfigurationEncryptionConfigurationTypeDef(
    _ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3ConfigurationEncryptionConfigurationTypeDef
):
    """
    Type definition for `ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3Configuration` `EncryptionConfiguration`

    The encryption configuration. If no value is specified, the default is no encryption.

    - **NoEncryptionConfig** *(string) --*

      Specifically override existing encryption information to ensure that no encryption is used.

    - **KMSEncryptionConfig** *(dict) --*

      The encryption key.

      - **AWSKMSKeyARN** *(string) --* **[REQUIRED]**

        The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region
        as the destination Amazon S3 bucket. For more information, see `Amazon Resource Names
        (ARNs) and AWS Service Namespaces
        <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
    """


_RequiredClientCreateDeliveryStreamRedshiftDestinationConfigurationS3ConfigurationTypeDef = TypedDict(
    "_RequiredClientCreateDeliveryStreamRedshiftDestinationConfigurationS3ConfigurationTypeDef",
    {"RoleARN": str, "BucketARN": str},
)
_OptionalClientCreateDeliveryStreamRedshiftDestinationConfigurationS3ConfigurationTypeDef = TypedDict(
    "_OptionalClientCreateDeliveryStreamRedshiftDestinationConfigurationS3ConfigurationTypeDef",
    {
        "Prefix": str,
        "ErrorOutputPrefix": str,
        "BufferingHints": ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3ConfigurationBufferingHintsTypeDef,
        "CompressionFormat": str,
        "EncryptionConfiguration": ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3ConfigurationEncryptionConfigurationTypeDef,
        "CloudWatchLoggingOptions": ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3ConfigurationCloudWatchLoggingOptionsTypeDef,
    },
    total=False,
)


class ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3ConfigurationTypeDef(
    _RequiredClientCreateDeliveryStreamRedshiftDestinationConfigurationS3ConfigurationTypeDef,
    _OptionalClientCreateDeliveryStreamRedshiftDestinationConfigurationS3ConfigurationTypeDef,
):
    """
    Type definition for `ClientCreateDeliveryStreamRedshiftDestinationConfiguration` `S3Configuration`

    The configuration for the intermediate Amazon S3 location from which Amazon Redshift obtains
    data. Restrictions are described in the topic for  CreateDeliveryStream .

    The compression formats ``SNAPPY`` or ``ZIP`` cannot be specified in
    ``RedshiftDestinationConfiguration.S3Configuration`` because the Amazon Redshift ``COPY``
    operation that reads from the S3 bucket doesn't support these compression formats.

    - **RoleARN** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the AWS credentials. For more information, see `Amazon
      Resource Names (ARNs) and AWS Service Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

    - **BucketARN** *(string) --* **[REQUIRED]**

      The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs) and AWS
      Service Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

    - **Prefix** *(string) --*

      The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered Amazon S3 files.
      You can also specify a custom prefix, as described in `Custom Prefixes for Amazon S3 Objects
      <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

    - **ErrorOutputPrefix** *(string) --*

      A prefix that Kinesis Data Firehose evaluates and adds to failed records before writing them
      to S3. This prefix appears immediately following the bucket name. For information about how
      to specify this prefix, see `Custom Prefixes for Amazon S3 Objects
      <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

    - **BufferingHints** *(dict) --*

      The buffering option. If no value is specified, ``BufferingHints`` object default values are
      used.

      - **SizeInMBs** *(integer) --*

        Buffer incoming data to the specified size, in MiBs, before delivering it to the
        destination. The default value is 5. This parameter is optional but if you specify a value
        for it, you must also specify a value for ``IntervalInSeconds`` , and vice versa.

        We recommend setting this parameter to a value greater than the amount of data you
        typically ingest into the delivery stream in 10 seconds. For example, if you typically
        ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

      - **IntervalInSeconds** *(integer) --*

        Buffer incoming data for the specified period of time, in seconds, before delivering it to
        the destination. The default value is 300. This parameter is optional but if you specify a
        value for it, you must also specify a value for ``SizeInMBs`` , and vice versa.

    - **CompressionFormat** *(string) --*

      The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .

      The compression formats ``SNAPPY`` or ``ZIP`` cannot be specified for Amazon Redshift
      destinations because they are not supported by the Amazon Redshift ``COPY`` operation that
      reads from the S3 bucket.

    - **EncryptionConfiguration** *(dict) --*

      The encryption configuration. If no value is specified, the default is no encryption.

      - **NoEncryptionConfig** *(string) --*

        Specifically override existing encryption information to ensure that no encryption is used.

      - **KMSEncryptionConfig** *(dict) --*

        The encryption key.

        - **AWSKMSKeyARN** *(string) --* **[REQUIRED]**

          The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region
          as the destination Amazon S3 bucket. For more information, see `Amazon Resource Names
          (ARNs) and AWS Service Namespaces
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

    - **CloudWatchLoggingOptions** *(dict) --*

      The CloudWatch logging options for your delivery stream.

      - **Enabled** *(boolean) --*

        Enables or disables CloudWatch logging.

      - **LogGroupName** *(string) --*

        The CloudWatch group name for logging. This value is required if CloudWatch logging is
        enabled.

      - **LogStreamName** *(string) --*

        The CloudWatch log stream name for logging. This value is required if CloudWatch logging is
        enabled.
    """


_RequiredClientCreateDeliveryStreamRedshiftDestinationConfigurationTypeDef = TypedDict(
    "_RequiredClientCreateDeliveryStreamRedshiftDestinationConfigurationTypeDef",
    {
        "RoleARN": str,
        "ClusterJDBCURL": str,
        "CopyCommand": ClientCreateDeliveryStreamRedshiftDestinationConfigurationCopyCommandTypeDef,
        "Username": str,
        "Password": str,
        "S3Configuration": ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3ConfigurationTypeDef,
    },
)
_OptionalClientCreateDeliveryStreamRedshiftDestinationConfigurationTypeDef = TypedDict(
    "_OptionalClientCreateDeliveryStreamRedshiftDestinationConfigurationTypeDef",
    {
        "RetryOptions": ClientCreateDeliveryStreamRedshiftDestinationConfigurationRetryOptionsTypeDef,
        "ProcessingConfiguration": ClientCreateDeliveryStreamRedshiftDestinationConfigurationProcessingConfigurationTypeDef,
        "S3BackupMode": str,
        "S3BackupConfiguration": ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3BackupConfigurationTypeDef,
        "CloudWatchLoggingOptions": ClientCreateDeliveryStreamRedshiftDestinationConfigurationCloudWatchLoggingOptionsTypeDef,
    },
    total=False,
)


class ClientCreateDeliveryStreamRedshiftDestinationConfigurationTypeDef(
    _RequiredClientCreateDeliveryStreamRedshiftDestinationConfigurationTypeDef,
    _OptionalClientCreateDeliveryStreamRedshiftDestinationConfigurationTypeDef,
):
    """
    Type definition for `ClientCreateDeliveryStream` `RedshiftDestinationConfiguration`

    The destination in Amazon Redshift. You can specify only one destination.

    - **RoleARN** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the AWS credentials. For more information, see `Amazon
      Resource Names (ARNs) and AWS Service Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

    - **ClusterJDBCURL** *(string) --* **[REQUIRED]**

      The database connection string.

    - **CopyCommand** *(dict) --* **[REQUIRED]**

      The ``COPY`` command.

      - **DataTableName** *(string) --* **[REQUIRED]**

        The name of the target table. The table must already exist in the database.

      - **DataTableColumns** *(string) --*

        A comma-separated list of column names.

      - **CopyOptions** *(string) --*

        Optional parameters to use with the Amazon Redshift ``COPY`` command. For more information,
        see the "Optional Parameters" section of `Amazon Redshift COPY command
        <https://docs.aws.amazon.com/redshift/latest/dg/r_COPY.html>`__ . Some possible examples that
        would apply to Kinesis Data Firehose are as follows:

         ``delimiter '\\t' lzop;`` - fields are delimited with "\\t" (TAB character) and compressed
         using lzop.

         ``delimiter '|'`` - fields are delimited with "|" (this is the default delimiter).

         ``delimiter '|' escape`` - the delimiter should be escaped.

         ``fixedwidth 'venueid:3,venuename:25,venuecity:12,venuestate:2,venueseats:6'`` - fields are
         fixed width in the source, with each width specified after every column in the table.

         ``JSON 's3://mybucket/jsonpaths.txt'`` - data is in JSON format, and the path specified is
         the format of the data.

        For more examples, see `Amazon Redshift COPY command examples
        <https://docs.aws.amazon.com/redshift/latest/dg/r_COPY_command_examples.html>`__ .

    - **Username** *(string) --* **[REQUIRED]**

      The name of the user.

    - **Password** *(string) --* **[REQUIRED]**

      The user password.

    - **RetryOptions** *(dict) --*

      The retry behavior in case Kinesis Data Firehose is unable to deliver documents to Amazon
      Redshift. Default value is 3600 (60 minutes).

      - **DurationInSeconds** *(integer) --*

        The length of time during which Kinesis Data Firehose retries delivery after a failure,
        starting from the initial request and including the first attempt. The default value is 3600
        seconds (60 minutes). Kinesis Data Firehose does not retry if the value of
        ``DurationInSeconds`` is 0 (zero) or if the first delivery attempt takes longer than the
        current value.

    - **S3Configuration** *(dict) --* **[REQUIRED]**

      The configuration for the intermediate Amazon S3 location from which Amazon Redshift obtains
      data. Restrictions are described in the topic for  CreateDeliveryStream .

      The compression formats ``SNAPPY`` or ``ZIP`` cannot be specified in
      ``RedshiftDestinationConfiguration.S3Configuration`` because the Amazon Redshift ``COPY``
      operation that reads from the S3 bucket doesn't support these compression formats.

      - **RoleARN** *(string) --* **[REQUIRED]**

        The Amazon Resource Name (ARN) of the AWS credentials. For more information, see `Amazon
        Resource Names (ARNs) and AWS Service Namespaces
        <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

      - **BucketARN** *(string) --* **[REQUIRED]**

        The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs) and AWS
        Service Namespaces
        <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

      - **Prefix** *(string) --*

        The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered Amazon S3 files.
        You can also specify a custom prefix, as described in `Custom Prefixes for Amazon S3 Objects
        <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

      - **ErrorOutputPrefix** *(string) --*

        A prefix that Kinesis Data Firehose evaluates and adds to failed records before writing them
        to S3. This prefix appears immediately following the bucket name. For information about how
        to specify this prefix, see `Custom Prefixes for Amazon S3 Objects
        <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

      - **BufferingHints** *(dict) --*

        The buffering option. If no value is specified, ``BufferingHints`` object default values are
        used.

        - **SizeInMBs** *(integer) --*

          Buffer incoming data to the specified size, in MiBs, before delivering it to the
          destination. The default value is 5. This parameter is optional but if you specify a value
          for it, you must also specify a value for ``IntervalInSeconds`` , and vice versa.

          We recommend setting this parameter to a value greater than the amount of data you
          typically ingest into the delivery stream in 10 seconds. For example, if you typically
          ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

        - **IntervalInSeconds** *(integer) --*

          Buffer incoming data for the specified period of time, in seconds, before delivering it to
          the destination. The default value is 300. This parameter is optional but if you specify a
          value for it, you must also specify a value for ``SizeInMBs`` , and vice versa.

      - **CompressionFormat** *(string) --*

        The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .

        The compression formats ``SNAPPY`` or ``ZIP`` cannot be specified for Amazon Redshift
        destinations because they are not supported by the Amazon Redshift ``COPY`` operation that
        reads from the S3 bucket.

      - **EncryptionConfiguration** *(dict) --*

        The encryption configuration. If no value is specified, the default is no encryption.

        - **NoEncryptionConfig** *(string) --*

          Specifically override existing encryption information to ensure that no encryption is used.

        - **KMSEncryptionConfig** *(dict) --*

          The encryption key.

          - **AWSKMSKeyARN** *(string) --* **[REQUIRED]**

            The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region
            as the destination Amazon S3 bucket. For more information, see `Amazon Resource Names
            (ARNs) and AWS Service Namespaces
            <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

      - **CloudWatchLoggingOptions** *(dict) --*

        The CloudWatch logging options for your delivery stream.

        - **Enabled** *(boolean) --*

          Enables or disables CloudWatch logging.

        - **LogGroupName** *(string) --*

          The CloudWatch group name for logging. This value is required if CloudWatch logging is
          enabled.

        - **LogStreamName** *(string) --*

          The CloudWatch log stream name for logging. This value is required if CloudWatch logging is
          enabled.

    - **ProcessingConfiguration** *(dict) --*

      The data processing configuration.

      - **Enabled** *(boolean) --*

        Enables or disables data processing.

      - **Processors** *(list) --*

        The data processors.

        - *(dict) --*

          Describes a data processor.

          - **Type** *(string) --* **[REQUIRED]**

            The type of processor.

          - **Parameters** *(list) --*

            The processor parameters.

            - *(dict) --*

              Describes the processor parameter.

              - **ParameterName** *(string) --* **[REQUIRED]**

                The name of the parameter.

              - **ParameterValue** *(string) --* **[REQUIRED]**

                The parameter value.

    - **S3BackupMode** *(string) --*

      The Amazon S3 backup mode.

    - **S3BackupConfiguration** *(dict) --*

      The configuration for backup in Amazon S3.

      - **RoleARN** *(string) --* **[REQUIRED]**

        The Amazon Resource Name (ARN) of the AWS credentials. For more information, see `Amazon
        Resource Names (ARNs) and AWS Service Namespaces
        <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

      - **BucketARN** *(string) --* **[REQUIRED]**

        The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs) and AWS
        Service Namespaces
        <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

      - **Prefix** *(string) --*

        The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered Amazon S3 files.
        You can also specify a custom prefix, as described in `Custom Prefixes for Amazon S3 Objects
        <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

      - **ErrorOutputPrefix** *(string) --*

        A prefix that Kinesis Data Firehose evaluates and adds to failed records before writing them
        to S3. This prefix appears immediately following the bucket name. For information about how
        to specify this prefix, see `Custom Prefixes for Amazon S3 Objects
        <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

      - **BufferingHints** *(dict) --*

        The buffering option. If no value is specified, ``BufferingHints`` object default values are
        used.

        - **SizeInMBs** *(integer) --*

          Buffer incoming data to the specified size, in MiBs, before delivering it to the
          destination. The default value is 5. This parameter is optional but if you specify a value
          for it, you must also specify a value for ``IntervalInSeconds`` , and vice versa.

          We recommend setting this parameter to a value greater than the amount of data you
          typically ingest into the delivery stream in 10 seconds. For example, if you typically
          ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

        - **IntervalInSeconds** *(integer) --*

          Buffer incoming data for the specified period of time, in seconds, before delivering it to
          the destination. The default value is 300. This parameter is optional but if you specify a
          value for it, you must also specify a value for ``SizeInMBs`` , and vice versa.

      - **CompressionFormat** *(string) --*

        The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .

        The compression formats ``SNAPPY`` or ``ZIP`` cannot be specified for Amazon Redshift
        destinations because they are not supported by the Amazon Redshift ``COPY`` operation that
        reads from the S3 bucket.

      - **EncryptionConfiguration** *(dict) --*

        The encryption configuration. If no value is specified, the default is no encryption.

        - **NoEncryptionConfig** *(string) --*

          Specifically override existing encryption information to ensure that no encryption is used.

        - **KMSEncryptionConfig** *(dict) --*

          The encryption key.

          - **AWSKMSKeyARN** *(string) --* **[REQUIRED]**

            The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region
            as the destination Amazon S3 bucket. For more information, see `Amazon Resource Names
            (ARNs) and AWS Service Namespaces
            <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

      - **CloudWatchLoggingOptions** *(dict) --*

        The CloudWatch logging options for your delivery stream.

        - **Enabled** *(boolean) --*

          Enables or disables CloudWatch logging.

        - **LogGroupName** *(string) --*

          The CloudWatch group name for logging. This value is required if CloudWatch logging is
          enabled.

        - **LogStreamName** *(string) --*

          The CloudWatch log stream name for logging. This value is required if CloudWatch logging is
          enabled.

    - **CloudWatchLoggingOptions** *(dict) --*

      The CloudWatch logging options for your delivery stream.

      - **Enabled** *(boolean) --*

        Enables or disables CloudWatch logging.

      - **LogGroupName** *(string) --*

        The CloudWatch group name for logging. This value is required if CloudWatch logging is
        enabled.

      - **LogStreamName** *(string) --*

        The CloudWatch log stream name for logging. This value is required if CloudWatch logging is
        enabled.
    """


_ClientCreateDeliveryStreamResponseTypeDef = TypedDict(
    "_ClientCreateDeliveryStreamResponseTypeDef",
    {"DeliveryStreamARN": str},
    total=False,
)


class ClientCreateDeliveryStreamResponseTypeDef(
    _ClientCreateDeliveryStreamResponseTypeDef
):
    """
    Type definition for `ClientCreateDeliveryStream` `Response`

    - **DeliveryStreamARN** *(string) --*

      The ARN of the delivery stream.
    """


_ClientCreateDeliveryStreamS3DestinationConfigurationBufferingHintsTypeDef = TypedDict(
    "_ClientCreateDeliveryStreamS3DestinationConfigurationBufferingHintsTypeDef",
    {"SizeInMBs": int, "IntervalInSeconds": int},
    total=False,
)


class ClientCreateDeliveryStreamS3DestinationConfigurationBufferingHintsTypeDef(
    _ClientCreateDeliveryStreamS3DestinationConfigurationBufferingHintsTypeDef
):
    """
    Type definition for `ClientCreateDeliveryStreamS3DestinationConfiguration` `BufferingHints`

    The buffering option. If no value is specified, ``BufferingHints`` object default values are
    used.

    - **SizeInMBs** *(integer) --*

      Buffer incoming data to the specified size, in MiBs, before delivering it to the destination.
      The default value is 5. This parameter is optional but if you specify a value for it, you
      must also specify a value for ``IntervalInSeconds`` , and vice versa.

      We recommend setting this parameter to a value greater than the amount of data you typically
      ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1
      MiB/sec, the value should be 10 MiB or higher.

    - **IntervalInSeconds** *(integer) --*

      Buffer incoming data for the specified period of time, in seconds, before delivering it to
      the destination. The default value is 300. This parameter is optional but if you specify a
      value for it, you must also specify a value for ``SizeInMBs`` , and vice versa.
    """


_ClientCreateDeliveryStreamS3DestinationConfigurationCloudWatchLoggingOptionsTypeDef = TypedDict(
    "_ClientCreateDeliveryStreamS3DestinationConfigurationCloudWatchLoggingOptionsTypeDef",
    {"Enabled": bool, "LogGroupName": str, "LogStreamName": str},
    total=False,
)


class ClientCreateDeliveryStreamS3DestinationConfigurationCloudWatchLoggingOptionsTypeDef(
    _ClientCreateDeliveryStreamS3DestinationConfigurationCloudWatchLoggingOptionsTypeDef
):
    """
    Type definition for `ClientCreateDeliveryStreamS3DestinationConfiguration` `CloudWatchLoggingOptions`

    The CloudWatch logging options for your delivery stream.

    - **Enabled** *(boolean) --*

      Enables or disables CloudWatch logging.

    - **LogGroupName** *(string) --*

      The CloudWatch group name for logging. This value is required if CloudWatch logging is
      enabled.

    - **LogStreamName** *(string) --*

      The CloudWatch log stream name for logging. This value is required if CloudWatch logging is
      enabled.
    """


_ClientCreateDeliveryStreamS3DestinationConfigurationEncryptionConfigurationKMSEncryptionConfigTypeDef = TypedDict(
    "_ClientCreateDeliveryStreamS3DestinationConfigurationEncryptionConfigurationKMSEncryptionConfigTypeDef",
    {"AWSKMSKeyARN": str},
)


class ClientCreateDeliveryStreamS3DestinationConfigurationEncryptionConfigurationKMSEncryptionConfigTypeDef(
    _ClientCreateDeliveryStreamS3DestinationConfigurationEncryptionConfigurationKMSEncryptionConfigTypeDef
):
    """
    Type definition for `ClientCreateDeliveryStreamS3DestinationConfigurationEncryptionConfiguration` `KMSEncryptionConfig`

    The encryption key.

    - **AWSKMSKeyARN** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region as
      the destination Amazon S3 bucket. For more information, see `Amazon Resource Names (ARNs)
      and AWS Service Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
    """


_ClientCreateDeliveryStreamS3DestinationConfigurationEncryptionConfigurationTypeDef = TypedDict(
    "_ClientCreateDeliveryStreamS3DestinationConfigurationEncryptionConfigurationTypeDef",
    {
        "NoEncryptionConfig": str,
        "KMSEncryptionConfig": ClientCreateDeliveryStreamS3DestinationConfigurationEncryptionConfigurationKMSEncryptionConfigTypeDef,
    },
    total=False,
)


class ClientCreateDeliveryStreamS3DestinationConfigurationEncryptionConfigurationTypeDef(
    _ClientCreateDeliveryStreamS3DestinationConfigurationEncryptionConfigurationTypeDef
):
    """
    Type definition for `ClientCreateDeliveryStreamS3DestinationConfiguration` `EncryptionConfiguration`

    The encryption configuration. If no value is specified, the default is no encryption.

    - **NoEncryptionConfig** *(string) --*

      Specifically override existing encryption information to ensure that no encryption is used.

    - **KMSEncryptionConfig** *(dict) --*

      The encryption key.

      - **AWSKMSKeyARN** *(string) --* **[REQUIRED]**

        The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region as
        the destination Amazon S3 bucket. For more information, see `Amazon Resource Names (ARNs)
        and AWS Service Namespaces
        <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
    """


_RequiredClientCreateDeliveryStreamS3DestinationConfigurationTypeDef = TypedDict(
    "_RequiredClientCreateDeliveryStreamS3DestinationConfigurationTypeDef",
    {"RoleARN": str, "BucketARN": str},
)
_OptionalClientCreateDeliveryStreamS3DestinationConfigurationTypeDef = TypedDict(
    "_OptionalClientCreateDeliveryStreamS3DestinationConfigurationTypeDef",
    {
        "Prefix": str,
        "ErrorOutputPrefix": str,
        "BufferingHints": ClientCreateDeliveryStreamS3DestinationConfigurationBufferingHintsTypeDef,
        "CompressionFormat": str,
        "EncryptionConfiguration": ClientCreateDeliveryStreamS3DestinationConfigurationEncryptionConfigurationTypeDef,
        "CloudWatchLoggingOptions": ClientCreateDeliveryStreamS3DestinationConfigurationCloudWatchLoggingOptionsTypeDef,
    },
    total=False,
)


class ClientCreateDeliveryStreamS3DestinationConfigurationTypeDef(
    _RequiredClientCreateDeliveryStreamS3DestinationConfigurationTypeDef,
    _OptionalClientCreateDeliveryStreamS3DestinationConfigurationTypeDef,
):
    """
    Type definition for `ClientCreateDeliveryStream` `S3DestinationConfiguration`

    [Deprecated] The destination in Amazon S3. You can specify only one destination.

    - **RoleARN** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the AWS credentials. For more information, see `Amazon
      Resource Names (ARNs) and AWS Service Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

    - **BucketARN** *(string) --* **[REQUIRED]**

      The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs) and AWS
      Service Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

    - **Prefix** *(string) --*

      The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered Amazon S3 files. You
      can also specify a custom prefix, as described in `Custom Prefixes for Amazon S3 Objects
      <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

    - **ErrorOutputPrefix** *(string) --*

      A prefix that Kinesis Data Firehose evaluates and adds to failed records before writing them to
      S3. This prefix appears immediately following the bucket name. For information about how to
      specify this prefix, see `Custom Prefixes for Amazon S3 Objects
      <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

    - **BufferingHints** *(dict) --*

      The buffering option. If no value is specified, ``BufferingHints`` object default values are
      used.

      - **SizeInMBs** *(integer) --*

        Buffer incoming data to the specified size, in MiBs, before delivering it to the destination.
        The default value is 5. This parameter is optional but if you specify a value for it, you
        must also specify a value for ``IntervalInSeconds`` , and vice versa.

        We recommend setting this parameter to a value greater than the amount of data you typically
        ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1
        MiB/sec, the value should be 10 MiB or higher.

      - **IntervalInSeconds** *(integer) --*

        Buffer incoming data for the specified period of time, in seconds, before delivering it to
        the destination. The default value is 300. This parameter is optional but if you specify a
        value for it, you must also specify a value for ``SizeInMBs`` , and vice versa.

    - **CompressionFormat** *(string) --*

      The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .

      The compression formats ``SNAPPY`` or ``ZIP`` cannot be specified for Amazon Redshift
      destinations because they are not supported by the Amazon Redshift ``COPY`` operation that
      reads from the S3 bucket.

    - **EncryptionConfiguration** *(dict) --*

      The encryption configuration. If no value is specified, the default is no encryption.

      - **NoEncryptionConfig** *(string) --*

        Specifically override existing encryption information to ensure that no encryption is used.

      - **KMSEncryptionConfig** *(dict) --*

        The encryption key.

        - **AWSKMSKeyARN** *(string) --* **[REQUIRED]**

          The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region as
          the destination Amazon S3 bucket. For more information, see `Amazon Resource Names (ARNs)
          and AWS Service Namespaces
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

    - **CloudWatchLoggingOptions** *(dict) --*

      The CloudWatch logging options for your delivery stream.

      - **Enabled** *(boolean) --*

        Enables or disables CloudWatch logging.

      - **LogGroupName** *(string) --*

        The CloudWatch group name for logging. This value is required if CloudWatch logging is
        enabled.

      - **LogStreamName** *(string) --*

        The CloudWatch log stream name for logging. This value is required if CloudWatch logging is
        enabled.
    """


_ClientCreateDeliveryStreamSplunkDestinationConfigurationCloudWatchLoggingOptionsTypeDef = TypedDict(
    "_ClientCreateDeliveryStreamSplunkDestinationConfigurationCloudWatchLoggingOptionsTypeDef",
    {"Enabled": bool, "LogGroupName": str, "LogStreamName": str},
    total=False,
)


class ClientCreateDeliveryStreamSplunkDestinationConfigurationCloudWatchLoggingOptionsTypeDef(
    _ClientCreateDeliveryStreamSplunkDestinationConfigurationCloudWatchLoggingOptionsTypeDef
):
    """
    Type definition for `ClientCreateDeliveryStreamSplunkDestinationConfiguration` `CloudWatchLoggingOptions`

    The Amazon CloudWatch logging options for your delivery stream.

    - **Enabled** *(boolean) --*

      Enables or disables CloudWatch logging.

    - **LogGroupName** *(string) --*

      The CloudWatch group name for logging. This value is required if CloudWatch logging is
      enabled.

    - **LogStreamName** *(string) --*

      The CloudWatch log stream name for logging. This value is required if CloudWatch logging is
      enabled.
    """


_ClientCreateDeliveryStreamSplunkDestinationConfigurationProcessingConfigurationProcessorsParametersTypeDef = TypedDict(
    "_ClientCreateDeliveryStreamSplunkDestinationConfigurationProcessingConfigurationProcessorsParametersTypeDef",
    {"ParameterName": str, "ParameterValue": str},
)


class ClientCreateDeliveryStreamSplunkDestinationConfigurationProcessingConfigurationProcessorsParametersTypeDef(
    _ClientCreateDeliveryStreamSplunkDestinationConfigurationProcessingConfigurationProcessorsParametersTypeDef
):
    """
    Type definition for `ClientCreateDeliveryStreamSplunkDestinationConfigurationProcessingConfigurationProcessors` `Parameters`

    Describes the processor parameter.

    - **ParameterName** *(string) --* **[REQUIRED]**

      The name of the parameter.

    - **ParameterValue** *(string) --* **[REQUIRED]**

      The parameter value.
    """


_RequiredClientCreateDeliveryStreamSplunkDestinationConfigurationProcessingConfigurationProcessorsTypeDef = TypedDict(
    "_RequiredClientCreateDeliveryStreamSplunkDestinationConfigurationProcessingConfigurationProcessorsTypeDef",
    {"Type": str},
)
_OptionalClientCreateDeliveryStreamSplunkDestinationConfigurationProcessingConfigurationProcessorsTypeDef = TypedDict(
    "_OptionalClientCreateDeliveryStreamSplunkDestinationConfigurationProcessingConfigurationProcessorsTypeDef",
    {
        "Parameters": List[
            ClientCreateDeliveryStreamSplunkDestinationConfigurationProcessingConfigurationProcessorsParametersTypeDef
        ]
    },
    total=False,
)


class ClientCreateDeliveryStreamSplunkDestinationConfigurationProcessingConfigurationProcessorsTypeDef(
    _RequiredClientCreateDeliveryStreamSplunkDestinationConfigurationProcessingConfigurationProcessorsTypeDef,
    _OptionalClientCreateDeliveryStreamSplunkDestinationConfigurationProcessingConfigurationProcessorsTypeDef,
):
    """
    Type definition for `ClientCreateDeliveryStreamSplunkDestinationConfigurationProcessingConfiguration` `Processors`

    Describes a data processor.

    - **Type** *(string) --* **[REQUIRED]**

      The type of processor.

    - **Parameters** *(list) --*

      The processor parameters.

      - *(dict) --*

        Describes the processor parameter.

        - **ParameterName** *(string) --* **[REQUIRED]**

          The name of the parameter.

        - **ParameterValue** *(string) --* **[REQUIRED]**

          The parameter value.
    """


_ClientCreateDeliveryStreamSplunkDestinationConfigurationProcessingConfigurationTypeDef = TypedDict(
    "_ClientCreateDeliveryStreamSplunkDestinationConfigurationProcessingConfigurationTypeDef",
    {
        "Enabled": bool,
        "Processors": List[
            ClientCreateDeliveryStreamSplunkDestinationConfigurationProcessingConfigurationProcessorsTypeDef
        ],
    },
    total=False,
)


class ClientCreateDeliveryStreamSplunkDestinationConfigurationProcessingConfigurationTypeDef(
    _ClientCreateDeliveryStreamSplunkDestinationConfigurationProcessingConfigurationTypeDef
):
    """
    Type definition for `ClientCreateDeliveryStreamSplunkDestinationConfiguration` `ProcessingConfiguration`

    The data processing configuration.

    - **Enabled** *(boolean) --*

      Enables or disables data processing.

    - **Processors** *(list) --*

      The data processors.

      - *(dict) --*

        Describes a data processor.

        - **Type** *(string) --* **[REQUIRED]**

          The type of processor.

        - **Parameters** *(list) --*

          The processor parameters.

          - *(dict) --*

            Describes the processor parameter.

            - **ParameterName** *(string) --* **[REQUIRED]**

              The name of the parameter.

            - **ParameterValue** *(string) --* **[REQUIRED]**

              The parameter value.
    """


_ClientCreateDeliveryStreamSplunkDestinationConfigurationRetryOptionsTypeDef = TypedDict(
    "_ClientCreateDeliveryStreamSplunkDestinationConfigurationRetryOptionsTypeDef",
    {"DurationInSeconds": int},
    total=False,
)


class ClientCreateDeliveryStreamSplunkDestinationConfigurationRetryOptionsTypeDef(
    _ClientCreateDeliveryStreamSplunkDestinationConfigurationRetryOptionsTypeDef
):
    """
    Type definition for `ClientCreateDeliveryStreamSplunkDestinationConfiguration` `RetryOptions`

    The retry behavior in case Kinesis Data Firehose is unable to deliver data to Splunk, or if it
    doesn't receive an acknowledgment of receipt from Splunk.

    - **DurationInSeconds** *(integer) --*

      The total amount of time that Kinesis Data Firehose spends on retries. This duration starts
      after the initial attempt to send data to Splunk fails. It doesn't include the periods during
      which Kinesis Data Firehose waits for acknowledgment from Splunk after each attempt.
    """


_ClientCreateDeliveryStreamSplunkDestinationConfigurationS3ConfigurationBufferingHintsTypeDef = TypedDict(
    "_ClientCreateDeliveryStreamSplunkDestinationConfigurationS3ConfigurationBufferingHintsTypeDef",
    {"SizeInMBs": int, "IntervalInSeconds": int},
    total=False,
)


class ClientCreateDeliveryStreamSplunkDestinationConfigurationS3ConfigurationBufferingHintsTypeDef(
    _ClientCreateDeliveryStreamSplunkDestinationConfigurationS3ConfigurationBufferingHintsTypeDef
):
    """
    Type definition for `ClientCreateDeliveryStreamSplunkDestinationConfigurationS3Configuration` `BufferingHints`

    The buffering option. If no value is specified, ``BufferingHints`` object default values are
    used.

    - **SizeInMBs** *(integer) --*

      Buffer incoming data to the specified size, in MiBs, before delivering it to the
      destination. The default value is 5. This parameter is optional but if you specify a value
      for it, you must also specify a value for ``IntervalInSeconds`` , and vice versa.

      We recommend setting this parameter to a value greater than the amount of data you
      typically ingest into the delivery stream in 10 seconds. For example, if you typically
      ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

    - **IntervalInSeconds** *(integer) --*

      Buffer incoming data for the specified period of time, in seconds, before delivering it to
      the destination. The default value is 300. This parameter is optional but if you specify a
      value for it, you must also specify a value for ``SizeInMBs`` , and vice versa.
    """


_ClientCreateDeliveryStreamSplunkDestinationConfigurationS3ConfigurationCloudWatchLoggingOptionsTypeDef = TypedDict(
    "_ClientCreateDeliveryStreamSplunkDestinationConfigurationS3ConfigurationCloudWatchLoggingOptionsTypeDef",
    {"Enabled": bool, "LogGroupName": str, "LogStreamName": str},
    total=False,
)


class ClientCreateDeliveryStreamSplunkDestinationConfigurationS3ConfigurationCloudWatchLoggingOptionsTypeDef(
    _ClientCreateDeliveryStreamSplunkDestinationConfigurationS3ConfigurationCloudWatchLoggingOptionsTypeDef
):
    """
    Type definition for `ClientCreateDeliveryStreamSplunkDestinationConfigurationS3Configuration` `CloudWatchLoggingOptions`

    The CloudWatch logging options for your delivery stream.

    - **Enabled** *(boolean) --*

      Enables or disables CloudWatch logging.

    - **LogGroupName** *(string) --*

      The CloudWatch group name for logging. This value is required if CloudWatch logging is
      enabled.

    - **LogStreamName** *(string) --*

      The CloudWatch log stream name for logging. This value is required if CloudWatch logging is
      enabled.
    """


_ClientCreateDeliveryStreamSplunkDestinationConfigurationS3ConfigurationEncryptionConfigurationKMSEncryptionConfigTypeDef = TypedDict(
    "_ClientCreateDeliveryStreamSplunkDestinationConfigurationS3ConfigurationEncryptionConfigurationKMSEncryptionConfigTypeDef",
    {"AWSKMSKeyARN": str},
)


class ClientCreateDeliveryStreamSplunkDestinationConfigurationS3ConfigurationEncryptionConfigurationKMSEncryptionConfigTypeDef(
    _ClientCreateDeliveryStreamSplunkDestinationConfigurationS3ConfigurationEncryptionConfigurationKMSEncryptionConfigTypeDef
):
    """
    Type definition for `ClientCreateDeliveryStreamSplunkDestinationConfigurationS3ConfigurationEncryptionConfiguration` `KMSEncryptionConfig`

    The encryption key.

    - **AWSKMSKeyARN** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region
      as the destination Amazon S3 bucket. For more information, see `Amazon Resource Names
      (ARNs) and AWS Service Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
    """


_ClientCreateDeliveryStreamSplunkDestinationConfigurationS3ConfigurationEncryptionConfigurationTypeDef = TypedDict(
    "_ClientCreateDeliveryStreamSplunkDestinationConfigurationS3ConfigurationEncryptionConfigurationTypeDef",
    {
        "NoEncryptionConfig": str,
        "KMSEncryptionConfig": ClientCreateDeliveryStreamSplunkDestinationConfigurationS3ConfigurationEncryptionConfigurationKMSEncryptionConfigTypeDef,
    },
    total=False,
)


class ClientCreateDeliveryStreamSplunkDestinationConfigurationS3ConfigurationEncryptionConfigurationTypeDef(
    _ClientCreateDeliveryStreamSplunkDestinationConfigurationS3ConfigurationEncryptionConfigurationTypeDef
):
    """
    Type definition for `ClientCreateDeliveryStreamSplunkDestinationConfigurationS3Configuration` `EncryptionConfiguration`

    The encryption configuration. If no value is specified, the default is no encryption.

    - **NoEncryptionConfig** *(string) --*

      Specifically override existing encryption information to ensure that no encryption is used.

    - **KMSEncryptionConfig** *(dict) --*

      The encryption key.

      - **AWSKMSKeyARN** *(string) --* **[REQUIRED]**

        The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region
        as the destination Amazon S3 bucket. For more information, see `Amazon Resource Names
        (ARNs) and AWS Service Namespaces
        <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
    """


_RequiredClientCreateDeliveryStreamSplunkDestinationConfigurationS3ConfigurationTypeDef = TypedDict(
    "_RequiredClientCreateDeliveryStreamSplunkDestinationConfigurationS3ConfigurationTypeDef",
    {"RoleARN": str, "BucketARN": str},
)
_OptionalClientCreateDeliveryStreamSplunkDestinationConfigurationS3ConfigurationTypeDef = TypedDict(
    "_OptionalClientCreateDeliveryStreamSplunkDestinationConfigurationS3ConfigurationTypeDef",
    {
        "Prefix": str,
        "ErrorOutputPrefix": str,
        "BufferingHints": ClientCreateDeliveryStreamSplunkDestinationConfigurationS3ConfigurationBufferingHintsTypeDef,
        "CompressionFormat": str,
        "EncryptionConfiguration": ClientCreateDeliveryStreamSplunkDestinationConfigurationS3ConfigurationEncryptionConfigurationTypeDef,
        "CloudWatchLoggingOptions": ClientCreateDeliveryStreamSplunkDestinationConfigurationS3ConfigurationCloudWatchLoggingOptionsTypeDef,
    },
    total=False,
)


class ClientCreateDeliveryStreamSplunkDestinationConfigurationS3ConfigurationTypeDef(
    _RequiredClientCreateDeliveryStreamSplunkDestinationConfigurationS3ConfigurationTypeDef,
    _OptionalClientCreateDeliveryStreamSplunkDestinationConfigurationS3ConfigurationTypeDef,
):
    """
    Type definition for `ClientCreateDeliveryStreamSplunkDestinationConfiguration` `S3Configuration`

    The configuration for the backup Amazon S3 location.

    - **RoleARN** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the AWS credentials. For more information, see `Amazon
      Resource Names (ARNs) and AWS Service Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

    - **BucketARN** *(string) --* **[REQUIRED]**

      The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs) and AWS
      Service Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

    - **Prefix** *(string) --*

      The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered Amazon S3 files.
      You can also specify a custom prefix, as described in `Custom Prefixes for Amazon S3 Objects
      <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

    - **ErrorOutputPrefix** *(string) --*

      A prefix that Kinesis Data Firehose evaluates and adds to failed records before writing them
      to S3. This prefix appears immediately following the bucket name. For information about how
      to specify this prefix, see `Custom Prefixes for Amazon S3 Objects
      <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

    - **BufferingHints** *(dict) --*

      The buffering option. If no value is specified, ``BufferingHints`` object default values are
      used.

      - **SizeInMBs** *(integer) --*

        Buffer incoming data to the specified size, in MiBs, before delivering it to the
        destination. The default value is 5. This parameter is optional but if you specify a value
        for it, you must also specify a value for ``IntervalInSeconds`` , and vice versa.

        We recommend setting this parameter to a value greater than the amount of data you
        typically ingest into the delivery stream in 10 seconds. For example, if you typically
        ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

      - **IntervalInSeconds** *(integer) --*

        Buffer incoming data for the specified period of time, in seconds, before delivering it to
        the destination. The default value is 300. This parameter is optional but if you specify a
        value for it, you must also specify a value for ``SizeInMBs`` , and vice versa.

    - **CompressionFormat** *(string) --*

      The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .

      The compression formats ``SNAPPY`` or ``ZIP`` cannot be specified for Amazon Redshift
      destinations because they are not supported by the Amazon Redshift ``COPY`` operation that
      reads from the S3 bucket.

    - **EncryptionConfiguration** *(dict) --*

      The encryption configuration. If no value is specified, the default is no encryption.

      - **NoEncryptionConfig** *(string) --*

        Specifically override existing encryption information to ensure that no encryption is used.

      - **KMSEncryptionConfig** *(dict) --*

        The encryption key.

        - **AWSKMSKeyARN** *(string) --* **[REQUIRED]**

          The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region
          as the destination Amazon S3 bucket. For more information, see `Amazon Resource Names
          (ARNs) and AWS Service Namespaces
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

    - **CloudWatchLoggingOptions** *(dict) --*

      The CloudWatch logging options for your delivery stream.

      - **Enabled** *(boolean) --*

        Enables or disables CloudWatch logging.

      - **LogGroupName** *(string) --*

        The CloudWatch group name for logging. This value is required if CloudWatch logging is
        enabled.

      - **LogStreamName** *(string) --*

        The CloudWatch log stream name for logging. This value is required if CloudWatch logging is
        enabled.
    """


_RequiredClientCreateDeliveryStreamSplunkDestinationConfigurationTypeDef = TypedDict(
    "_RequiredClientCreateDeliveryStreamSplunkDestinationConfigurationTypeDef",
    {
        "HECEndpoint": str,
        "HECEndpointType": str,
        "HECToken": str,
        "S3Configuration": ClientCreateDeliveryStreamSplunkDestinationConfigurationS3ConfigurationTypeDef,
    },
)
_OptionalClientCreateDeliveryStreamSplunkDestinationConfigurationTypeDef = TypedDict(
    "_OptionalClientCreateDeliveryStreamSplunkDestinationConfigurationTypeDef",
    {
        "HECAcknowledgmentTimeoutInSeconds": int,
        "RetryOptions": ClientCreateDeliveryStreamSplunkDestinationConfigurationRetryOptionsTypeDef,
        "S3BackupMode": str,
        "ProcessingConfiguration": ClientCreateDeliveryStreamSplunkDestinationConfigurationProcessingConfigurationTypeDef,
        "CloudWatchLoggingOptions": ClientCreateDeliveryStreamSplunkDestinationConfigurationCloudWatchLoggingOptionsTypeDef,
    },
    total=False,
)


class ClientCreateDeliveryStreamSplunkDestinationConfigurationTypeDef(
    _RequiredClientCreateDeliveryStreamSplunkDestinationConfigurationTypeDef,
    _OptionalClientCreateDeliveryStreamSplunkDestinationConfigurationTypeDef,
):
    """
    Type definition for `ClientCreateDeliveryStream` `SplunkDestinationConfiguration`

    The destination in Splunk. You can specify only one destination.

    - **HECEndpoint** *(string) --* **[REQUIRED]**

      The HTTP Event Collector (HEC) endpoint to which Kinesis Data Firehose sends your data.

    - **HECEndpointType** *(string) --* **[REQUIRED]**

      This type can be either "Raw" or "Event."

    - **HECToken** *(string) --* **[REQUIRED]**

      This is a GUID that you obtain from your Splunk cluster when you create a new HEC endpoint.

    - **HECAcknowledgmentTimeoutInSeconds** *(integer) --*

      The amount of time that Kinesis Data Firehose waits to receive an acknowledgment from Splunk
      after it sends it data. At the end of the timeout period, Kinesis Data Firehose either tries to
      send the data again or considers it an error, based on your retry settings.

    - **RetryOptions** *(dict) --*

      The retry behavior in case Kinesis Data Firehose is unable to deliver data to Splunk, or if it
      doesn't receive an acknowledgment of receipt from Splunk.

      - **DurationInSeconds** *(integer) --*

        The total amount of time that Kinesis Data Firehose spends on retries. This duration starts
        after the initial attempt to send data to Splunk fails. It doesn't include the periods during
        which Kinesis Data Firehose waits for acknowledgment from Splunk after each attempt.

    - **S3BackupMode** *(string) --*

      Defines how documents should be delivered to Amazon S3. When set to ``FailedDocumentsOnly`` ,
      Kinesis Data Firehose writes any data that could not be indexed to the configured Amazon S3
      destination. When set to ``AllDocuments`` , Kinesis Data Firehose delivers all incoming records
      to Amazon S3, and also writes failed documents to Amazon S3. Default value is
      ``FailedDocumentsOnly`` .

    - **S3Configuration** *(dict) --* **[REQUIRED]**

      The configuration for the backup Amazon S3 location.

      - **RoleARN** *(string) --* **[REQUIRED]**

        The Amazon Resource Name (ARN) of the AWS credentials. For more information, see `Amazon
        Resource Names (ARNs) and AWS Service Namespaces
        <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

      - **BucketARN** *(string) --* **[REQUIRED]**

        The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs) and AWS
        Service Namespaces
        <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

      - **Prefix** *(string) --*

        The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered Amazon S3 files.
        You can also specify a custom prefix, as described in `Custom Prefixes for Amazon S3 Objects
        <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

      - **ErrorOutputPrefix** *(string) --*

        A prefix that Kinesis Data Firehose evaluates and adds to failed records before writing them
        to S3. This prefix appears immediately following the bucket name. For information about how
        to specify this prefix, see `Custom Prefixes for Amazon S3 Objects
        <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

      - **BufferingHints** *(dict) --*

        The buffering option. If no value is specified, ``BufferingHints`` object default values are
        used.

        - **SizeInMBs** *(integer) --*

          Buffer incoming data to the specified size, in MiBs, before delivering it to the
          destination. The default value is 5. This parameter is optional but if you specify a value
          for it, you must also specify a value for ``IntervalInSeconds`` , and vice versa.

          We recommend setting this parameter to a value greater than the amount of data you
          typically ingest into the delivery stream in 10 seconds. For example, if you typically
          ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

        - **IntervalInSeconds** *(integer) --*

          Buffer incoming data for the specified period of time, in seconds, before delivering it to
          the destination. The default value is 300. This parameter is optional but if you specify a
          value for it, you must also specify a value for ``SizeInMBs`` , and vice versa.

      - **CompressionFormat** *(string) --*

        The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .

        The compression formats ``SNAPPY`` or ``ZIP`` cannot be specified for Amazon Redshift
        destinations because they are not supported by the Amazon Redshift ``COPY`` operation that
        reads from the S3 bucket.

      - **EncryptionConfiguration** *(dict) --*

        The encryption configuration. If no value is specified, the default is no encryption.

        - **NoEncryptionConfig** *(string) --*

          Specifically override existing encryption information to ensure that no encryption is used.

        - **KMSEncryptionConfig** *(dict) --*

          The encryption key.

          - **AWSKMSKeyARN** *(string) --* **[REQUIRED]**

            The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region
            as the destination Amazon S3 bucket. For more information, see `Amazon Resource Names
            (ARNs) and AWS Service Namespaces
            <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

      - **CloudWatchLoggingOptions** *(dict) --*

        The CloudWatch logging options for your delivery stream.

        - **Enabled** *(boolean) --*

          Enables or disables CloudWatch logging.

        - **LogGroupName** *(string) --*

          The CloudWatch group name for logging. This value is required if CloudWatch logging is
          enabled.

        - **LogStreamName** *(string) --*

          The CloudWatch log stream name for logging. This value is required if CloudWatch logging is
          enabled.

    - **ProcessingConfiguration** *(dict) --*

      The data processing configuration.

      - **Enabled** *(boolean) --*

        Enables or disables data processing.

      - **Processors** *(list) --*

        The data processors.

        - *(dict) --*

          Describes a data processor.

          - **Type** *(string) --* **[REQUIRED]**

            The type of processor.

          - **Parameters** *(list) --*

            The processor parameters.

            - *(dict) --*

              Describes the processor parameter.

              - **ParameterName** *(string) --* **[REQUIRED]**

                The name of the parameter.

              - **ParameterValue** *(string) --* **[REQUIRED]**

                The parameter value.

    - **CloudWatchLoggingOptions** *(dict) --*

      The Amazon CloudWatch logging options for your delivery stream.

      - **Enabled** *(boolean) --*

        Enables or disables CloudWatch logging.

      - **LogGroupName** *(string) --*

        The CloudWatch group name for logging. This value is required if CloudWatch logging is
        enabled.

      - **LogStreamName** *(string) --*

        The CloudWatch log stream name for logging. This value is required if CloudWatch logging is
        enabled.
    """


_RequiredClientCreateDeliveryStreamTagsTypeDef = TypedDict(
    "_RequiredClientCreateDeliveryStreamTagsTypeDef", {"Key": str}
)
_OptionalClientCreateDeliveryStreamTagsTypeDef = TypedDict(
    "_OptionalClientCreateDeliveryStreamTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateDeliveryStreamTagsTypeDef(
    _RequiredClientCreateDeliveryStreamTagsTypeDef,
    _OptionalClientCreateDeliveryStreamTagsTypeDef,
):
    """
    Type definition for `ClientCreateDeliveryStream` `Tags`

    Metadata that you can assign to a delivery stream, consisting of a key-value pair.

    - **Key** *(string) --* **[REQUIRED]**

      A unique identifier for the tag. Maximum length: 128 characters. Valid characters: Unicode
      letters, digits, white space, _ . / = + - % @

    - **Value** *(string) --*

      An optional string, which you can use to describe or define the tag. Maximum length: 256
      characters. Valid characters: Unicode letters, digits, white space, _ . / = + - % @
    """


_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDeliveryStreamEncryptionConfigurationTypeDef = TypedDict(
    "_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDeliveryStreamEncryptionConfigurationTypeDef",
    {"Status": str},
    total=False,
)


class ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDeliveryStreamEncryptionConfigurationTypeDef(
    _ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDeliveryStreamEncryptionConfigurationTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryStreamResponseDeliveryStreamDescription` `DeliveryStreamEncryptionConfiguration`

    Indicates the server-side encryption (SSE) status for the delivery stream.

    - **Status** *(string) --*

      For a full description of the different values of this status, see
      StartDeliveryStreamEncryption and  StopDeliveryStreamEncryption .
    """


_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionBufferingHintsTypeDef = TypedDict(
    "_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionBufferingHintsTypeDef",
    {"IntervalInSeconds": int, "SizeInMBs": int},
    total=False,
)


class ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionBufferingHintsTypeDef(
    _ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionBufferingHintsTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescription` `BufferingHints`

    The buffering options.

    - **IntervalInSeconds** *(integer) --*

      Buffer incoming data for the specified period of time, in seconds, before
      delivering it to the destination. The default value is 300 (5 minutes).

    - **SizeInMBs** *(integer) --*

      Buffer incoming data to the specified size, in MBs, before delivering it to the
      destination. The default value is 5.

      We recommend setting this parameter to a value greater than the amount of data you
      typically ingest into the delivery stream in 10 seconds. For example, if you
      typically ingest data at 1 MB/sec, the value should be 10 MB or higher.
    """


_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionCloudWatchLoggingOptionsTypeDef = TypedDict(
    "_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionCloudWatchLoggingOptionsTypeDef",
    {"Enabled": bool, "LogGroupName": str, "LogStreamName": str},
    total=False,
)


class ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionCloudWatchLoggingOptionsTypeDef(
    _ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionCloudWatchLoggingOptionsTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescription` `CloudWatchLoggingOptions`

    The Amazon CloudWatch logging options.

    - **Enabled** *(boolean) --*

      Enables or disables CloudWatch logging.

    - **LogGroupName** *(string) --*

      The CloudWatch group name for logging. This value is required if CloudWatch logging
      is enabled.

    - **LogStreamName** *(string) --*

      The CloudWatch log stream name for logging. This value is required if CloudWatch
      logging is enabled.
    """


_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionProcessingConfigurationProcessorsParametersTypeDef = TypedDict(
    "_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionProcessingConfigurationProcessorsParametersTypeDef",
    {"ParameterName": str, "ParameterValue": str},
    total=False,
)


class ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionProcessingConfigurationProcessorsParametersTypeDef(
    _ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionProcessingConfigurationProcessorsParametersTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionProcessingConfigurationProcessors` `Parameters`

    Describes the processor parameter.

    - **ParameterName** *(string) --*

      The name of the parameter.

    - **ParameterValue** *(string) --*

      The parameter value.
    """


_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionProcessingConfigurationProcessorsTypeDef = TypedDict(
    "_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionProcessingConfigurationProcessorsTypeDef",
    {
        "Type": str,
        "Parameters": List[
            ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionProcessingConfigurationProcessorsParametersTypeDef
        ],
    },
    total=False,
)


class ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionProcessingConfigurationProcessorsTypeDef(
    _ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionProcessingConfigurationProcessorsTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionProcessingConfiguration` `Processors`

    Describes a data processor.

    - **Type** *(string) --*

      The type of processor.

    - **Parameters** *(list) --*

      The processor parameters.

      - *(dict) --*

        Describes the processor parameter.

        - **ParameterName** *(string) --*

          The name of the parameter.

        - **ParameterValue** *(string) --*

          The parameter value.
    """


_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionProcessingConfigurationTypeDef = TypedDict(
    "_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionProcessingConfigurationTypeDef",
    {
        "Enabled": bool,
        "Processors": List[
            ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionProcessingConfigurationProcessorsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionProcessingConfigurationTypeDef(
    _ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionProcessingConfigurationTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescription` `ProcessingConfiguration`

    The data processing configuration.

    - **Enabled** *(boolean) --*

      Enables or disables data processing.

    - **Processors** *(list) --*

      The data processors.

      - *(dict) --*

        Describes a data processor.

        - **Type** *(string) --*

          The type of processor.

        - **Parameters** *(list) --*

          The processor parameters.

          - *(dict) --*

            Describes the processor parameter.

            - **ParameterName** *(string) --*

              The name of the parameter.

            - **ParameterValue** *(string) --*

              The parameter value.
    """


_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionRetryOptionsTypeDef = TypedDict(
    "_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionRetryOptionsTypeDef",
    {"DurationInSeconds": int},
    total=False,
)


class ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionRetryOptionsTypeDef(
    _ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionRetryOptionsTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescription` `RetryOptions`

    The Amazon ES retry options.

    - **DurationInSeconds** *(integer) --*

      After an initial failure to deliver to Amazon ES, the total amount of time during
      which Kinesis Data Firehose retries delivery (including the first attempt). After
      this time has elapsed, the failed documents are written to Amazon S3. Default value
      is 300 seconds (5 minutes). A value of 0 (zero) results in no retries.
    """


_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionS3DestinationDescriptionBufferingHintsTypeDef = TypedDict(
    "_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionS3DestinationDescriptionBufferingHintsTypeDef",
    {"SizeInMBs": int, "IntervalInSeconds": int},
    total=False,
)


class ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionS3DestinationDescriptionBufferingHintsTypeDef(
    _ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionS3DestinationDescriptionBufferingHintsTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionS3DestinationDescription` `BufferingHints`

    The buffering option. If no value is specified, ``BufferingHints`` object default
    values are used.

    - **SizeInMBs** *(integer) --*

      Buffer incoming data to the specified size, in MiBs, before delivering it to the
      destination. The default value is 5. This parameter is optional but if you
      specify a value for it, you must also specify a value for ``IntervalInSeconds`` ,
      and vice versa.

      We recommend setting this parameter to a value greater than the amount of data
      you typically ingest into the delivery stream in 10 seconds. For example, if you
      typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

    - **IntervalInSeconds** *(integer) --*

      Buffer incoming data for the specified period of time, in seconds, before
      delivering it to the destination. The default value is 300. This parameter is
      optional but if you specify a value for it, you must also specify a value for
      ``SizeInMBs`` , and vice versa.
    """


_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionS3DestinationDescriptionCloudWatchLoggingOptionsTypeDef = TypedDict(
    "_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionS3DestinationDescriptionCloudWatchLoggingOptionsTypeDef",
    {"Enabled": bool, "LogGroupName": str, "LogStreamName": str},
    total=False,
)


class ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionS3DestinationDescriptionCloudWatchLoggingOptionsTypeDef(
    _ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionS3DestinationDescriptionCloudWatchLoggingOptionsTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionS3DestinationDescription` `CloudWatchLoggingOptions`

    The Amazon CloudWatch logging options for your delivery stream.

    - **Enabled** *(boolean) --*

      Enables or disables CloudWatch logging.

    - **LogGroupName** *(string) --*

      The CloudWatch group name for logging. This value is required if CloudWatch
      logging is enabled.

    - **LogStreamName** *(string) --*

      The CloudWatch log stream name for logging. This value is required if CloudWatch
      logging is enabled.
    """


_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionS3DestinationDescriptionEncryptionConfigurationKMSEncryptionConfigTypeDef = TypedDict(
    "_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionS3DestinationDescriptionEncryptionConfigurationKMSEncryptionConfigTypeDef",
    {"AWSKMSKeyARN": str},
    total=False,
)


class ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionS3DestinationDescriptionEncryptionConfigurationKMSEncryptionConfigTypeDef(
    _ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionS3DestinationDescriptionEncryptionConfigurationKMSEncryptionConfigTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionS3DestinationDescriptionEncryptionConfiguration` `KMSEncryptionConfig`

    The encryption key.

    - **AWSKMSKeyARN** *(string) --*

      The Amazon Resource Name (ARN) of the encryption key. Must belong to the same
      AWS Region as the destination Amazon S3 bucket. For more information, see
      `Amazon Resource Names (ARNs) and AWS Service Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__
      .
    """


_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionS3DestinationDescriptionEncryptionConfigurationTypeDef = TypedDict(
    "_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionS3DestinationDescriptionEncryptionConfigurationTypeDef",
    {
        "NoEncryptionConfig": str,
        "KMSEncryptionConfig": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionS3DestinationDescriptionEncryptionConfigurationKMSEncryptionConfigTypeDef,
    },
    total=False,
)


class ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionS3DestinationDescriptionEncryptionConfigurationTypeDef(
    _ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionS3DestinationDescriptionEncryptionConfigurationTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionS3DestinationDescription` `EncryptionConfiguration`

    The encryption configuration. If no value is specified, the default is no
    encryption.

    - **NoEncryptionConfig** *(string) --*

      Specifically override existing encryption information to ensure that no
      encryption is used.

    - **KMSEncryptionConfig** *(dict) --*

      The encryption key.

      - **AWSKMSKeyARN** *(string) --*

        The Amazon Resource Name (ARN) of the encryption key. Must belong to the same
        AWS Region as the destination Amazon S3 bucket. For more information, see
        `Amazon Resource Names (ARNs) and AWS Service Namespaces
        <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__
        .
    """


_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionS3DestinationDescriptionTypeDef = TypedDict(
    "_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionS3DestinationDescriptionTypeDef",
    {
        "RoleARN": str,
        "BucketARN": str,
        "Prefix": str,
        "ErrorOutputPrefix": str,
        "BufferingHints": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionS3DestinationDescriptionBufferingHintsTypeDef,
        "CompressionFormat": str,
        "EncryptionConfiguration": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionS3DestinationDescriptionEncryptionConfigurationTypeDef,
        "CloudWatchLoggingOptions": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionS3DestinationDescriptionCloudWatchLoggingOptionsTypeDef,
    },
    total=False,
)


class ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionS3DestinationDescriptionTypeDef(
    _ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionS3DestinationDescriptionTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescription` `S3DestinationDescription`

    The Amazon S3 destination.

    - **RoleARN** *(string) --*

      The Amazon Resource Name (ARN) of the AWS credentials. For more information, see
      `Amazon Resource Names (ARNs) and AWS Service Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

    - **BucketARN** *(string) --*

      The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs)
      and AWS Service Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

    - **Prefix** *(string) --*

      The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered Amazon
      S3 files. You can also specify a custom prefix, as described in `Custom Prefixes
      for Amazon S3 Objects
      <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

    - **ErrorOutputPrefix** *(string) --*

      A prefix that Kinesis Data Firehose evaluates and adds to failed records before
      writing them to S3. This prefix appears immediately following the bucket name. For
      information about how to specify this prefix, see `Custom Prefixes for Amazon S3
      Objects <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

    - **BufferingHints** *(dict) --*

      The buffering option. If no value is specified, ``BufferingHints`` object default
      values are used.

      - **SizeInMBs** *(integer) --*

        Buffer incoming data to the specified size, in MiBs, before delivering it to the
        destination. The default value is 5. This parameter is optional but if you
        specify a value for it, you must also specify a value for ``IntervalInSeconds`` ,
        and vice versa.

        We recommend setting this parameter to a value greater than the amount of data
        you typically ingest into the delivery stream in 10 seconds. For example, if you
        typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

      - **IntervalInSeconds** *(integer) --*

        Buffer incoming data for the specified period of time, in seconds, before
        delivering it to the destination. The default value is 300. This parameter is
        optional but if you specify a value for it, you must also specify a value for
        ``SizeInMBs`` , and vice versa.

    - **CompressionFormat** *(string) --*

      The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .

    - **EncryptionConfiguration** *(dict) --*

      The encryption configuration. If no value is specified, the default is no
      encryption.

      - **NoEncryptionConfig** *(string) --*

        Specifically override existing encryption information to ensure that no
        encryption is used.

      - **KMSEncryptionConfig** *(dict) --*

        The encryption key.

        - **AWSKMSKeyARN** *(string) --*

          The Amazon Resource Name (ARN) of the encryption key. Must belong to the same
          AWS Region as the destination Amazon S3 bucket. For more information, see
          `Amazon Resource Names (ARNs) and AWS Service Namespaces
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__
          .

    - **CloudWatchLoggingOptions** *(dict) --*

      The Amazon CloudWatch logging options for your delivery stream.

      - **Enabled** *(boolean) --*

        Enables or disables CloudWatch logging.

      - **LogGroupName** *(string) --*

        The CloudWatch group name for logging. This value is required if CloudWatch
        logging is enabled.

      - **LogStreamName** *(string) --*

        The CloudWatch log stream name for logging. This value is required if CloudWatch
        logging is enabled.
    """


_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionTypeDef = TypedDict(
    "_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionTypeDef",
    {
        "RoleARN": str,
        "DomainARN": str,
        "ClusterEndpoint": str,
        "IndexName": str,
        "TypeName": str,
        "IndexRotationPeriod": str,
        "BufferingHints": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionBufferingHintsTypeDef,
        "RetryOptions": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionRetryOptionsTypeDef,
        "S3BackupMode": str,
        "S3DestinationDescription": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionS3DestinationDescriptionTypeDef,
        "ProcessingConfiguration": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionProcessingConfigurationTypeDef,
        "CloudWatchLoggingOptions": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionCloudWatchLoggingOptionsTypeDef,
    },
    total=False,
)


class ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionTypeDef(
    _ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinations` `ElasticsearchDestinationDescription`

    The destination in Amazon ES.

    - **RoleARN** *(string) --*

      The Amazon Resource Name (ARN) of the AWS credentials. For more information, see
      `Amazon Resource Names (ARNs) and AWS Service Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

    - **DomainARN** *(string) --*

      The ARN of the Amazon ES domain. For more information, see `Amazon Resource Names
      (ARNs) and AWS Service Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

      Kinesis Data Firehose uses either ``ClusterEndpoint`` or ``DomainARN`` to send data
      to Amazon ES.

    - **ClusterEndpoint** *(string) --*

      The endpoint to use when communicating with the cluster. Kinesis Data Firehose uses
      either this ``ClusterEndpoint`` or the ``DomainARN`` field to send data to Amazon ES.

    - **IndexName** *(string) --*

      The Elasticsearch index name.

    - **TypeName** *(string) --*

      The Elasticsearch type name. This applies to Elasticsearch 6.x and lower versions.
      For Elasticsearch 7.x, there's no value for ``TypeName`` .

    - **IndexRotationPeriod** *(string) --*

      The Elasticsearch index rotation period

    - **BufferingHints** *(dict) --*

      The buffering options.

      - **IntervalInSeconds** *(integer) --*

        Buffer incoming data for the specified period of time, in seconds, before
        delivering it to the destination. The default value is 300 (5 minutes).

      - **SizeInMBs** *(integer) --*

        Buffer incoming data to the specified size, in MBs, before delivering it to the
        destination. The default value is 5.

        We recommend setting this parameter to a value greater than the amount of data you
        typically ingest into the delivery stream in 10 seconds. For example, if you
        typically ingest data at 1 MB/sec, the value should be 10 MB or higher.

    - **RetryOptions** *(dict) --*

      The Amazon ES retry options.

      - **DurationInSeconds** *(integer) --*

        After an initial failure to deliver to Amazon ES, the total amount of time during
        which Kinesis Data Firehose retries delivery (including the first attempt). After
        this time has elapsed, the failed documents are written to Amazon S3. Default value
        is 300 seconds (5 minutes). A value of 0 (zero) results in no retries.

    - **S3BackupMode** *(string) --*

      The Amazon S3 backup mode.

    - **S3DestinationDescription** *(dict) --*

      The Amazon S3 destination.

      - **RoleARN** *(string) --*

        The Amazon Resource Name (ARN) of the AWS credentials. For more information, see
        `Amazon Resource Names (ARNs) and AWS Service Namespaces
        <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

      - **BucketARN** *(string) --*

        The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs)
        and AWS Service Namespaces
        <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

      - **Prefix** *(string) --*

        The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered Amazon
        S3 files. You can also specify a custom prefix, as described in `Custom Prefixes
        for Amazon S3 Objects
        <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

      - **ErrorOutputPrefix** *(string) --*

        A prefix that Kinesis Data Firehose evaluates and adds to failed records before
        writing them to S3. This prefix appears immediately following the bucket name. For
        information about how to specify this prefix, see `Custom Prefixes for Amazon S3
        Objects <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

      - **BufferingHints** *(dict) --*

        The buffering option. If no value is specified, ``BufferingHints`` object default
        values are used.

        - **SizeInMBs** *(integer) --*

          Buffer incoming data to the specified size, in MiBs, before delivering it to the
          destination. The default value is 5. This parameter is optional but if you
          specify a value for it, you must also specify a value for ``IntervalInSeconds`` ,
          and vice versa.

          We recommend setting this parameter to a value greater than the amount of data
          you typically ingest into the delivery stream in 10 seconds. For example, if you
          typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

        - **IntervalInSeconds** *(integer) --*

          Buffer incoming data for the specified period of time, in seconds, before
          delivering it to the destination. The default value is 300. This parameter is
          optional but if you specify a value for it, you must also specify a value for
          ``SizeInMBs`` , and vice versa.

      - **CompressionFormat** *(string) --*

        The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .

      - **EncryptionConfiguration** *(dict) --*

        The encryption configuration. If no value is specified, the default is no
        encryption.

        - **NoEncryptionConfig** *(string) --*

          Specifically override existing encryption information to ensure that no
          encryption is used.

        - **KMSEncryptionConfig** *(dict) --*

          The encryption key.

          - **AWSKMSKeyARN** *(string) --*

            The Amazon Resource Name (ARN) of the encryption key. Must belong to the same
            AWS Region as the destination Amazon S3 bucket. For more information, see
            `Amazon Resource Names (ARNs) and AWS Service Namespaces
            <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__
            .

      - **CloudWatchLoggingOptions** *(dict) --*

        The Amazon CloudWatch logging options for your delivery stream.

        - **Enabled** *(boolean) --*

          Enables or disables CloudWatch logging.

        - **LogGroupName** *(string) --*

          The CloudWatch group name for logging. This value is required if CloudWatch
          logging is enabled.

        - **LogStreamName** *(string) --*

          The CloudWatch log stream name for logging. This value is required if CloudWatch
          logging is enabled.

    - **ProcessingConfiguration** *(dict) --*

      The data processing configuration.

      - **Enabled** *(boolean) --*

        Enables or disables data processing.

      - **Processors** *(list) --*

        The data processors.

        - *(dict) --*

          Describes a data processor.

          - **Type** *(string) --*

            The type of processor.

          - **Parameters** *(list) --*

            The processor parameters.

            - *(dict) --*

              Describes the processor parameter.

              - **ParameterName** *(string) --*

                The name of the parameter.

              - **ParameterValue** *(string) --*

                The parameter value.

    - **CloudWatchLoggingOptions** *(dict) --*

      The Amazon CloudWatch logging options.

      - **Enabled** *(boolean) --*

        Enables or disables CloudWatch logging.

      - **LogGroupName** *(string) --*

        The CloudWatch group name for logging. This value is required if CloudWatch logging
        is enabled.

      - **LogStreamName** *(string) --*

        The CloudWatch log stream name for logging. This value is required if CloudWatch
        logging is enabled.
    """


_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionBufferingHintsTypeDef = TypedDict(
    "_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionBufferingHintsTypeDef",
    {"SizeInMBs": int, "IntervalInSeconds": int},
    total=False,
)


class ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionBufferingHintsTypeDef(
    _ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionBufferingHintsTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescription` `BufferingHints`

    The buffering option.

    - **SizeInMBs** *(integer) --*

      Buffer incoming data to the specified size, in MiBs, before delivering it to the
      destination. The default value is 5. This parameter is optional but if you specify
      a value for it, you must also specify a value for ``IntervalInSeconds`` , and vice
      versa.

      We recommend setting this parameter to a value greater than the amount of data you
      typically ingest into the delivery stream in 10 seconds. For example, if you
      typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

    - **IntervalInSeconds** *(integer) --*

      Buffer incoming data for the specified period of time, in seconds, before
      delivering it to the destination. The default value is 300. This parameter is
      optional but if you specify a value for it, you must also specify a value for
      ``SizeInMBs`` , and vice versa.
    """


_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionCloudWatchLoggingOptionsTypeDef = TypedDict(
    "_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionCloudWatchLoggingOptionsTypeDef",
    {"Enabled": bool, "LogGroupName": str, "LogStreamName": str},
    total=False,
)


class ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionCloudWatchLoggingOptionsTypeDef(
    _ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionCloudWatchLoggingOptionsTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescription` `CloudWatchLoggingOptions`

    The Amazon CloudWatch logging options for your delivery stream.

    - **Enabled** *(boolean) --*

      Enables or disables CloudWatch logging.

    - **LogGroupName** *(string) --*

      The CloudWatch group name for logging. This value is required if CloudWatch logging
      is enabled.

    - **LogStreamName** *(string) --*

      The CloudWatch log stream name for logging. This value is required if CloudWatch
      logging is enabled.
    """


_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDeTypeDef = TypedDict(
    "_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDeTypeDef",
    {"TimestampFormats": List[str]},
    total=False,
)


class ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDeTypeDef(
    _ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDeTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationInputFormatConfigurationDeserializer` `HiveJsonSerDe`

    The native Hive / HCatalog JsonSerDe. Used by Kinesis Data Firehose for
    deserializing data, which means converting it from the JSON format in
    preparation for serializing it to the Parquet or ORC format. This is one of two
    deserializers you can choose, depending on which one offers the functionality
    you need. The other option is the OpenX SerDe.

    - **TimestampFormats** *(list) --*

      Indicates how you want Kinesis Data Firehose to parse the date and timestamps
      that may be present in your input data JSON. To specify these format strings,
      follow the pattern syntax of JodaTime's DateTimeFormat format strings. For
      more information, see `Class DateTimeFormat
      <https://www.joda.org/joda-time/apidocs/org/joda/time/format/DateTimeFormat.html>`__
      . You can also use the special value ``millis`` to parse timestamps in epoch
      milliseconds. If you don't specify a format, Kinesis Data Firehose uses
      ``java.sql.Timestamp::valueOf`` by default.

      - *(string) --*
    """


_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDeTypeDef = TypedDict(
    "_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDeTypeDef",
    {
        "ConvertDotsInJsonKeysToUnderscores": bool,
        "CaseInsensitive": bool,
        "ColumnToJsonKeyMappings": Dict[str, str],
    },
    total=False,
)


class ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDeTypeDef(
    _ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDeTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationInputFormatConfigurationDeserializer` `OpenXJsonSerDe`

    The OpenX SerDe. Used by Kinesis Data Firehose for deserializing data, which
    means converting it from the JSON format in preparation for serializing it to
    the Parquet or ORC format. This is one of two deserializers you can choose,
    depending on which one offers the functionality you need. The other option is
    the native Hive / HCatalog JsonSerDe.

    - **ConvertDotsInJsonKeysToUnderscores** *(boolean) --*

      When set to ``true`` , specifies that the names of the keys include dots and
      that you want Kinesis Data Firehose to replace them with underscores. This is
      useful because Apache Hive does not allow dots in column names. For example,
      if the JSON contains a key whose name is "a.b", you can define the column
      name to be "a_b" when using this option.

      The default is ``false`` .

    - **CaseInsensitive** *(boolean) --*

      When set to ``true`` , which is the default, Kinesis Data Firehose converts
      JSON keys to lowercase before deserializing them.

    - **ColumnToJsonKeyMappings** *(dict) --*

      Maps column names to JSON keys that aren't identical to the column names.
      This is useful when the JSON contains keys that are Hive keywords. For
      example, ``timestamp`` is a Hive keyword. If you have a JSON key named
      ``timestamp`` , set this parameter to ``{"ts": "timestamp"}`` to map this key
      to a column named ``ts`` .

      - *(string) --*

        - *(string) --*
    """


_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationInputFormatConfigurationDeserializerTypeDef = TypedDict(
    "_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationInputFormatConfigurationDeserializerTypeDef",
    {
        "OpenXJsonSerDe": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDeTypeDef,
        "HiveJsonSerDe": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDeTypeDef,
    },
    total=False,
)


class ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationInputFormatConfigurationDeserializerTypeDef(
    _ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationInputFormatConfigurationDeserializerTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationInputFormatConfiguration` `Deserializer`

    Specifies which deserializer to use. You can choose either the Apache Hive JSON
    SerDe or the OpenX JSON SerDe. If both are non-null, the server rejects the
    request.

    - **OpenXJsonSerDe** *(dict) --*

      The OpenX SerDe. Used by Kinesis Data Firehose for deserializing data, which
      means converting it from the JSON format in preparation for serializing it to
      the Parquet or ORC format. This is one of two deserializers you can choose,
      depending on which one offers the functionality you need. The other option is
      the native Hive / HCatalog JsonSerDe.

      - **ConvertDotsInJsonKeysToUnderscores** *(boolean) --*

        When set to ``true`` , specifies that the names of the keys include dots and
        that you want Kinesis Data Firehose to replace them with underscores. This is
        useful because Apache Hive does not allow dots in column names. For example,
        if the JSON contains a key whose name is "a.b", you can define the column
        name to be "a_b" when using this option.

        The default is ``false`` .

      - **CaseInsensitive** *(boolean) --*

        When set to ``true`` , which is the default, Kinesis Data Firehose converts
        JSON keys to lowercase before deserializing them.

      - **ColumnToJsonKeyMappings** *(dict) --*

        Maps column names to JSON keys that aren't identical to the column names.
        This is useful when the JSON contains keys that are Hive keywords. For
        example, ``timestamp`` is a Hive keyword. If you have a JSON key named
        ``timestamp`` , set this parameter to ``{"ts": "timestamp"}`` to map this key
        to a column named ``ts`` .

        - *(string) --*

          - *(string) --*

    - **HiveJsonSerDe** *(dict) --*

      The native Hive / HCatalog JsonSerDe. Used by Kinesis Data Firehose for
      deserializing data, which means converting it from the JSON format in
      preparation for serializing it to the Parquet or ORC format. This is one of two
      deserializers you can choose, depending on which one offers the functionality
      you need. The other option is the OpenX SerDe.

      - **TimestampFormats** *(list) --*

        Indicates how you want Kinesis Data Firehose to parse the date and timestamps
        that may be present in your input data JSON. To specify these format strings,
        follow the pattern syntax of JodaTime's DateTimeFormat format strings. For
        more information, see `Class DateTimeFormat
        <https://www.joda.org/joda-time/apidocs/org/joda/time/format/DateTimeFormat.html>`__
        . You can also use the special value ``millis`` to parse timestamps in epoch
        milliseconds. If you don't specify a format, Kinesis Data Firehose uses
        ``java.sql.Timestamp::valueOf`` by default.

        - *(string) --*
    """


_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationInputFormatConfigurationTypeDef = TypedDict(
    "_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationInputFormatConfigurationTypeDef",
    {
        "Deserializer": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationInputFormatConfigurationDeserializerTypeDef
    },
    total=False,
)


class ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationInputFormatConfigurationTypeDef(
    _ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationInputFormatConfigurationTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfiguration` `InputFormatConfiguration`

    Specifies the deserializer that you want Kinesis Data Firehose to use to convert
    the format of your data from JSON.

    - **Deserializer** *(dict) --*

      Specifies which deserializer to use. You can choose either the Apache Hive JSON
      SerDe or the OpenX JSON SerDe. If both are non-null, the server rejects the
      request.

      - **OpenXJsonSerDe** *(dict) --*

        The OpenX SerDe. Used by Kinesis Data Firehose for deserializing data, which
        means converting it from the JSON format in preparation for serializing it to
        the Parquet or ORC format. This is one of two deserializers you can choose,
        depending on which one offers the functionality you need. The other option is
        the native Hive / HCatalog JsonSerDe.

        - **ConvertDotsInJsonKeysToUnderscores** *(boolean) --*

          When set to ``true`` , specifies that the names of the keys include dots and
          that you want Kinesis Data Firehose to replace them with underscores. This is
          useful because Apache Hive does not allow dots in column names. For example,
          if the JSON contains a key whose name is "a.b", you can define the column
          name to be "a_b" when using this option.

          The default is ``false`` .

        - **CaseInsensitive** *(boolean) --*

          When set to ``true`` , which is the default, Kinesis Data Firehose converts
          JSON keys to lowercase before deserializing them.

        - **ColumnToJsonKeyMappings** *(dict) --*

          Maps column names to JSON keys that aren't identical to the column names.
          This is useful when the JSON contains keys that are Hive keywords. For
          example, ``timestamp`` is a Hive keyword. If you have a JSON key named
          ``timestamp`` , set this parameter to ``{"ts": "timestamp"}`` to map this key
          to a column named ``ts`` .

          - *(string) --*

            - *(string) --*

      - **HiveJsonSerDe** *(dict) --*

        The native Hive / HCatalog JsonSerDe. Used by Kinesis Data Firehose for
        deserializing data, which means converting it from the JSON format in
        preparation for serializing it to the Parquet or ORC format. This is one of two
        deserializers you can choose, depending on which one offers the functionality
        you need. The other option is the OpenX SerDe.

        - **TimestampFormats** *(list) --*

          Indicates how you want Kinesis Data Firehose to parse the date and timestamps
          that may be present in your input data JSON. To specify these format strings,
          follow the pattern syntax of JodaTime's DateTimeFormat format strings. For
          more information, see `Class DateTimeFormat
          <https://www.joda.org/joda-time/apidocs/org/joda/time/format/DateTimeFormat.html>`__
          . You can also use the special value ``millis`` to parse timestamps in epoch
          milliseconds. If you don't specify a format, Kinesis Data Firehose uses
          ``java.sql.Timestamp::valueOf`` by default.

          - *(string) --*
    """


_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDeTypeDef = TypedDict(
    "_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDeTypeDef",
    {
        "StripeSizeBytes": int,
        "BlockSizeBytes": int,
        "RowIndexStride": int,
        "EnablePadding": bool,
        "PaddingTolerance": float,
        "Compression": str,
        "BloomFilterColumns": List[str],
        "BloomFilterFalsePositiveProbability": float,
        "DictionaryKeyThreshold": float,
        "FormatVersion": str,
    },
    total=False,
)


class ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDeTypeDef(
    _ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDeTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationOutputFormatConfigurationSerializer` `OrcSerDe`

    A serializer to use for converting data to the ORC format before storing it in
    Amazon S3. For more information, see `Apache ORC
    <https://orc.apache.org/docs/>`__ .

    - **StripeSizeBytes** *(integer) --*

      The number of bytes in each stripe. The default is 64 MiB and the minimum is
      8 MiB.

    - **BlockSizeBytes** *(integer) --*

      The Hadoop Distributed File System (HDFS) block size. This is useful if you
      intend to copy the data from Amazon S3 to HDFS before querying. The default
      is 256 MiB and the minimum is 64 MiB. Kinesis Data Firehose uses this value
      for padding calculations.

    - **RowIndexStride** *(integer) --*

      The number of rows between index entries. The default is 10,000 and the
      minimum is 1,000.

    - **EnablePadding** *(boolean) --*

      Set this to ``true`` to indicate that you want stripes to be padded to the
      HDFS block boundaries. This is useful if you intend to copy the data from
      Amazon S3 to HDFS before querying. The default is ``false`` .

    - **PaddingTolerance** *(float) --*

      A number between 0 and 1 that defines the tolerance for block padding as a
      decimal fraction of stripe size. The default value is 0.05, which means 5
      percent of stripe size.

      For the default values of 64 MiB ORC stripes and 256 MiB HDFS blocks, the
      default block padding tolerance of 5 percent reserves a maximum of 3.2 MiB
      for padding within the 256 MiB block. In such a case, if the available size
      within the block is more than 3.2 MiB, a new, smaller stripe is inserted to
      fit within that space. This ensures that no stripe crosses block boundaries
      and causes remote reads within a node-local task.

      Kinesis Data Firehose ignores this parameter when  OrcSerDe$EnablePadding is
      ``false`` .

    - **Compression** *(string) --*

      The compression code to use over data blocks. The default is ``SNAPPY`` .

    - **BloomFilterColumns** *(list) --*

      The column names for which you want Kinesis Data Firehose to create bloom
      filters. The default is ``null`` .

      - *(string) --*

    - **BloomFilterFalsePositiveProbability** *(float) --*

      The Bloom filter false positive probability (FPP). The lower the FPP, the
      bigger the Bloom filter. The default value is 0.05, the minimum is 0, and the
      maximum is 1.

    - **DictionaryKeyThreshold** *(float) --*

      Represents the fraction of the total number of non-null rows. To turn off
      dictionary encoding, set this fraction to a number that is less than the
      number of distinct keys in a dictionary. To always use dictionary encoding,
      set this threshold to 1.

    - **FormatVersion** *(string) --*

      The version of the file to write. The possible values are ``V0_11`` and
      ``V0_12`` . The default is ``V0_12`` .
    """


_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDeTypeDef = TypedDict(
    "_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDeTypeDef",
    {
        "BlockSizeBytes": int,
        "PageSizeBytes": int,
        "Compression": str,
        "EnableDictionaryCompression": bool,
        "MaxPaddingBytes": int,
        "WriterVersion": str,
    },
    total=False,
)


class ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDeTypeDef(
    _ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDeTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationOutputFormatConfigurationSerializer` `ParquetSerDe`

    A serializer to use for converting data to the Parquet format before storing it
    in Amazon S3. For more information, see `Apache Parquet
    <https://parquet.apache.org/documentation/latest/>`__ .

    - **BlockSizeBytes** *(integer) --*

      The Hadoop Distributed File System (HDFS) block size. This is useful if you
      intend to copy the data from Amazon S3 to HDFS before querying. The default
      is 256 MiB and the minimum is 64 MiB. Kinesis Data Firehose uses this value
      for padding calculations.

    - **PageSizeBytes** *(integer) --*

      The Parquet page size. Column chunks are divided into pages. A page is
      conceptually an indivisible unit (in terms of compression and encoding). The
      minimum value is 64 KiB and the default is 1 MiB.

    - **Compression** *(string) --*

      The compression code to use over data blocks. The possible values are
      ``UNCOMPRESSED`` , ``SNAPPY`` , and ``GZIP`` , with the default being
      ``SNAPPY`` . Use ``SNAPPY`` for higher decompression speed. Use ``GZIP`` if
      the compression ration is more important than speed.

    - **EnableDictionaryCompression** *(boolean) --*

      Indicates whether to enable dictionary compression.

    - **MaxPaddingBytes** *(integer) --*

      The maximum amount of padding to apply. This is useful if you intend to copy
      the data from Amazon S3 to HDFS before querying. The default is 0.

    - **WriterVersion** *(string) --*

      Indicates the version of row format to output. The possible values are ``V1``
      and ``V2`` . The default is ``V1`` .
    """


_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationOutputFormatConfigurationSerializerTypeDef = TypedDict(
    "_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationOutputFormatConfigurationSerializerTypeDef",
    {
        "ParquetSerDe": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDeTypeDef,
        "OrcSerDe": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDeTypeDef,
    },
    total=False,
)


class ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationOutputFormatConfigurationSerializerTypeDef(
    _ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationOutputFormatConfigurationSerializerTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationOutputFormatConfiguration` `Serializer`

    Specifies which serializer to use. You can choose either the ORC SerDe or the
    Parquet SerDe. If both are non-null, the server rejects the request.

    - **ParquetSerDe** *(dict) --*

      A serializer to use for converting data to the Parquet format before storing it
      in Amazon S3. For more information, see `Apache Parquet
      <https://parquet.apache.org/documentation/latest/>`__ .

      - **BlockSizeBytes** *(integer) --*

        The Hadoop Distributed File System (HDFS) block size. This is useful if you
        intend to copy the data from Amazon S3 to HDFS before querying. The default
        is 256 MiB and the minimum is 64 MiB. Kinesis Data Firehose uses this value
        for padding calculations.

      - **PageSizeBytes** *(integer) --*

        The Parquet page size. Column chunks are divided into pages. A page is
        conceptually an indivisible unit (in terms of compression and encoding). The
        minimum value is 64 KiB and the default is 1 MiB.

      - **Compression** *(string) --*

        The compression code to use over data blocks. The possible values are
        ``UNCOMPRESSED`` , ``SNAPPY`` , and ``GZIP`` , with the default being
        ``SNAPPY`` . Use ``SNAPPY`` for higher decompression speed. Use ``GZIP`` if
        the compression ration is more important than speed.

      - **EnableDictionaryCompression** *(boolean) --*

        Indicates whether to enable dictionary compression.

      - **MaxPaddingBytes** *(integer) --*

        The maximum amount of padding to apply. This is useful if you intend to copy
        the data from Amazon S3 to HDFS before querying. The default is 0.

      - **WriterVersion** *(string) --*

        Indicates the version of row format to output. The possible values are ``V1``
        and ``V2`` . The default is ``V1`` .

    - **OrcSerDe** *(dict) --*

      A serializer to use for converting data to the ORC format before storing it in
      Amazon S3. For more information, see `Apache ORC
      <https://orc.apache.org/docs/>`__ .

      - **StripeSizeBytes** *(integer) --*

        The number of bytes in each stripe. The default is 64 MiB and the minimum is
        8 MiB.

      - **BlockSizeBytes** *(integer) --*

        The Hadoop Distributed File System (HDFS) block size. This is useful if you
        intend to copy the data from Amazon S3 to HDFS before querying. The default
        is 256 MiB and the minimum is 64 MiB. Kinesis Data Firehose uses this value
        for padding calculations.

      - **RowIndexStride** *(integer) --*

        The number of rows between index entries. The default is 10,000 and the
        minimum is 1,000.

      - **EnablePadding** *(boolean) --*

        Set this to ``true`` to indicate that you want stripes to be padded to the
        HDFS block boundaries. This is useful if you intend to copy the data from
        Amazon S3 to HDFS before querying. The default is ``false`` .

      - **PaddingTolerance** *(float) --*

        A number between 0 and 1 that defines the tolerance for block padding as a
        decimal fraction of stripe size. The default value is 0.05, which means 5
        percent of stripe size.

        For the default values of 64 MiB ORC stripes and 256 MiB HDFS blocks, the
        default block padding tolerance of 5 percent reserves a maximum of 3.2 MiB
        for padding within the 256 MiB block. In such a case, if the available size
        within the block is more than 3.2 MiB, a new, smaller stripe is inserted to
        fit within that space. This ensures that no stripe crosses block boundaries
        and causes remote reads within a node-local task.

        Kinesis Data Firehose ignores this parameter when  OrcSerDe$EnablePadding is
        ``false`` .

      - **Compression** *(string) --*

        The compression code to use over data blocks. The default is ``SNAPPY`` .

      - **BloomFilterColumns** *(list) --*

        The column names for which you want Kinesis Data Firehose to create bloom
        filters. The default is ``null`` .

        - *(string) --*

      - **BloomFilterFalsePositiveProbability** *(float) --*

        The Bloom filter false positive probability (FPP). The lower the FPP, the
        bigger the Bloom filter. The default value is 0.05, the minimum is 0, and the
        maximum is 1.

      - **DictionaryKeyThreshold** *(float) --*

        Represents the fraction of the total number of non-null rows. To turn off
        dictionary encoding, set this fraction to a number that is less than the
        number of distinct keys in a dictionary. To always use dictionary encoding,
        set this threshold to 1.

      - **FormatVersion** *(string) --*

        The version of the file to write. The possible values are ``V0_11`` and
        ``V0_12`` . The default is ``V0_12`` .
    """


_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationOutputFormatConfigurationTypeDef = TypedDict(
    "_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationOutputFormatConfigurationTypeDef",
    {
        "Serializer": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationOutputFormatConfigurationSerializerTypeDef
    },
    total=False,
)


class ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationOutputFormatConfigurationTypeDef(
    _ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationOutputFormatConfigurationTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfiguration` `OutputFormatConfiguration`

    Specifies the serializer that you want Kinesis Data Firehose to use to convert the
    format of your data to the Parquet or ORC format.

    - **Serializer** *(dict) --*

      Specifies which serializer to use. You can choose either the ORC SerDe or the
      Parquet SerDe. If both are non-null, the server rejects the request.

      - **ParquetSerDe** *(dict) --*

        A serializer to use for converting data to the Parquet format before storing it
        in Amazon S3. For more information, see `Apache Parquet
        <https://parquet.apache.org/documentation/latest/>`__ .

        - **BlockSizeBytes** *(integer) --*

          The Hadoop Distributed File System (HDFS) block size. This is useful if you
          intend to copy the data from Amazon S3 to HDFS before querying. The default
          is 256 MiB and the minimum is 64 MiB. Kinesis Data Firehose uses this value
          for padding calculations.

        - **PageSizeBytes** *(integer) --*

          The Parquet page size. Column chunks are divided into pages. A page is
          conceptually an indivisible unit (in terms of compression and encoding). The
          minimum value is 64 KiB and the default is 1 MiB.

        - **Compression** *(string) --*

          The compression code to use over data blocks. The possible values are
          ``UNCOMPRESSED`` , ``SNAPPY`` , and ``GZIP`` , with the default being
          ``SNAPPY`` . Use ``SNAPPY`` for higher decompression speed. Use ``GZIP`` if
          the compression ration is more important than speed.

        - **EnableDictionaryCompression** *(boolean) --*

          Indicates whether to enable dictionary compression.

        - **MaxPaddingBytes** *(integer) --*

          The maximum amount of padding to apply. This is useful if you intend to copy
          the data from Amazon S3 to HDFS before querying. The default is 0.

        - **WriterVersion** *(string) --*

          Indicates the version of row format to output. The possible values are ``V1``
          and ``V2`` . The default is ``V1`` .

      - **OrcSerDe** *(dict) --*

        A serializer to use for converting data to the ORC format before storing it in
        Amazon S3. For more information, see `Apache ORC
        <https://orc.apache.org/docs/>`__ .

        - **StripeSizeBytes** *(integer) --*

          The number of bytes in each stripe. The default is 64 MiB and the minimum is
          8 MiB.

        - **BlockSizeBytes** *(integer) --*

          The Hadoop Distributed File System (HDFS) block size. This is useful if you
          intend to copy the data from Amazon S3 to HDFS before querying. The default
          is 256 MiB and the minimum is 64 MiB. Kinesis Data Firehose uses this value
          for padding calculations.

        - **RowIndexStride** *(integer) --*

          The number of rows between index entries. The default is 10,000 and the
          minimum is 1,000.

        - **EnablePadding** *(boolean) --*

          Set this to ``true`` to indicate that you want stripes to be padded to the
          HDFS block boundaries. This is useful if you intend to copy the data from
          Amazon S3 to HDFS before querying. The default is ``false`` .

        - **PaddingTolerance** *(float) --*

          A number between 0 and 1 that defines the tolerance for block padding as a
          decimal fraction of stripe size. The default value is 0.05, which means 5
          percent of stripe size.

          For the default values of 64 MiB ORC stripes and 256 MiB HDFS blocks, the
          default block padding tolerance of 5 percent reserves a maximum of 3.2 MiB
          for padding within the 256 MiB block. In such a case, if the available size
          within the block is more than 3.2 MiB, a new, smaller stripe is inserted to
          fit within that space. This ensures that no stripe crosses block boundaries
          and causes remote reads within a node-local task.

          Kinesis Data Firehose ignores this parameter when  OrcSerDe$EnablePadding is
          ``false`` .

        - **Compression** *(string) --*

          The compression code to use over data blocks. The default is ``SNAPPY`` .

        - **BloomFilterColumns** *(list) --*

          The column names for which you want Kinesis Data Firehose to create bloom
          filters. The default is ``null`` .

          - *(string) --*

        - **BloomFilterFalsePositiveProbability** *(float) --*

          The Bloom filter false positive probability (FPP). The lower the FPP, the
          bigger the Bloom filter. The default value is 0.05, the minimum is 0, and the
          maximum is 1.

        - **DictionaryKeyThreshold** *(float) --*

          Represents the fraction of the total number of non-null rows. To turn off
          dictionary encoding, set this fraction to a number that is less than the
          number of distinct keys in a dictionary. To always use dictionary encoding,
          set this threshold to 1.

        - **FormatVersion** *(string) --*

          The version of the file to write. The possible values are ``V0_11`` and
          ``V0_12`` . The default is ``V0_12`` .
    """


_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationSchemaConfigurationTypeDef = TypedDict(
    "_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationSchemaConfigurationTypeDef",
    {
        "RoleARN": str,
        "CatalogId": str,
        "DatabaseName": str,
        "TableName": str,
        "Region": str,
        "VersionId": str,
    },
    total=False,
)


class ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationSchemaConfigurationTypeDef(
    _ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationSchemaConfigurationTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfiguration` `SchemaConfiguration`

    Specifies the AWS Glue Data Catalog table that contains the column information.

    - **RoleARN** *(string) --*

      The role that Kinesis Data Firehose can use to access AWS Glue. This role must be
      in the same account you use for Kinesis Data Firehose. Cross-account roles aren't
      allowed.

    - **CatalogId** *(string) --*

      The ID of the AWS Glue Data Catalog. If you don't supply this, the AWS account ID
      is used by default.

    - **DatabaseName** *(string) --*

      Specifies the name of the AWS Glue database that contains the schema for the
      output data.

    - **TableName** *(string) --*

      Specifies the AWS Glue table that contains the column information that
      constitutes your data schema.

    - **Region** *(string) --*

      If you don't specify an AWS Region, the default is the current Region.

    - **VersionId** *(string) --*

      Specifies the table version for the output data schema. If you don't specify this
      version ID, or if you set it to ``LATEST`` , Kinesis Data Firehose uses the most
      recent version. This means that any updates to the table are automatically picked
      up.
    """


_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationTypeDef = TypedDict(
    "_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationTypeDef",
    {
        "SchemaConfiguration": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationSchemaConfigurationTypeDef,
        "InputFormatConfiguration": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationInputFormatConfigurationTypeDef,
        "OutputFormatConfiguration": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationOutputFormatConfigurationTypeDef,
        "Enabled": bool,
    },
    total=False,
)


class ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationTypeDef(
    _ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescription` `DataFormatConversionConfiguration`

    The serializer, deserializer, and schema for converting data from the JSON format to
    the Parquet or ORC format before writing it to Amazon S3.

    - **SchemaConfiguration** *(dict) --*

      Specifies the AWS Glue Data Catalog table that contains the column information.

      - **RoleARN** *(string) --*

        The role that Kinesis Data Firehose can use to access AWS Glue. This role must be
        in the same account you use for Kinesis Data Firehose. Cross-account roles aren't
        allowed.

      - **CatalogId** *(string) --*

        The ID of the AWS Glue Data Catalog. If you don't supply this, the AWS account ID
        is used by default.

      - **DatabaseName** *(string) --*

        Specifies the name of the AWS Glue database that contains the schema for the
        output data.

      - **TableName** *(string) --*

        Specifies the AWS Glue table that contains the column information that
        constitutes your data schema.

      - **Region** *(string) --*

        If you don't specify an AWS Region, the default is the current Region.

      - **VersionId** *(string) --*

        Specifies the table version for the output data schema. If you don't specify this
        version ID, or if you set it to ``LATEST`` , Kinesis Data Firehose uses the most
        recent version. This means that any updates to the table are automatically picked
        up.

    - **InputFormatConfiguration** *(dict) --*

      Specifies the deserializer that you want Kinesis Data Firehose to use to convert
      the format of your data from JSON.

      - **Deserializer** *(dict) --*

        Specifies which deserializer to use. You can choose either the Apache Hive JSON
        SerDe or the OpenX JSON SerDe. If both are non-null, the server rejects the
        request.

        - **OpenXJsonSerDe** *(dict) --*

          The OpenX SerDe. Used by Kinesis Data Firehose for deserializing data, which
          means converting it from the JSON format in preparation for serializing it to
          the Parquet or ORC format. This is one of two deserializers you can choose,
          depending on which one offers the functionality you need. The other option is
          the native Hive / HCatalog JsonSerDe.

          - **ConvertDotsInJsonKeysToUnderscores** *(boolean) --*

            When set to ``true`` , specifies that the names of the keys include dots and
            that you want Kinesis Data Firehose to replace them with underscores. This is
            useful because Apache Hive does not allow dots in column names. For example,
            if the JSON contains a key whose name is "a.b", you can define the column
            name to be "a_b" when using this option.

            The default is ``false`` .

          - **CaseInsensitive** *(boolean) --*

            When set to ``true`` , which is the default, Kinesis Data Firehose converts
            JSON keys to lowercase before deserializing them.

          - **ColumnToJsonKeyMappings** *(dict) --*

            Maps column names to JSON keys that aren't identical to the column names.
            This is useful when the JSON contains keys that are Hive keywords. For
            example, ``timestamp`` is a Hive keyword. If you have a JSON key named
            ``timestamp`` , set this parameter to ``{"ts": "timestamp"}`` to map this key
            to a column named ``ts`` .

            - *(string) --*

              - *(string) --*

        - **HiveJsonSerDe** *(dict) --*

          The native Hive / HCatalog JsonSerDe. Used by Kinesis Data Firehose for
          deserializing data, which means converting it from the JSON format in
          preparation for serializing it to the Parquet or ORC format. This is one of two
          deserializers you can choose, depending on which one offers the functionality
          you need. The other option is the OpenX SerDe.

          - **TimestampFormats** *(list) --*

            Indicates how you want Kinesis Data Firehose to parse the date and timestamps
            that may be present in your input data JSON. To specify these format strings,
            follow the pattern syntax of JodaTime's DateTimeFormat format strings. For
            more information, see `Class DateTimeFormat
            <https://www.joda.org/joda-time/apidocs/org/joda/time/format/DateTimeFormat.html>`__
            . You can also use the special value ``millis`` to parse timestamps in epoch
            milliseconds. If you don't specify a format, Kinesis Data Firehose uses
            ``java.sql.Timestamp::valueOf`` by default.

            - *(string) --*

    - **OutputFormatConfiguration** *(dict) --*

      Specifies the serializer that you want Kinesis Data Firehose to use to convert the
      format of your data to the Parquet or ORC format.

      - **Serializer** *(dict) --*

        Specifies which serializer to use. You can choose either the ORC SerDe or the
        Parquet SerDe. If both are non-null, the server rejects the request.

        - **ParquetSerDe** *(dict) --*

          A serializer to use for converting data to the Parquet format before storing it
          in Amazon S3. For more information, see `Apache Parquet
          <https://parquet.apache.org/documentation/latest/>`__ .

          - **BlockSizeBytes** *(integer) --*

            The Hadoop Distributed File System (HDFS) block size. This is useful if you
            intend to copy the data from Amazon S3 to HDFS before querying. The default
            is 256 MiB and the minimum is 64 MiB. Kinesis Data Firehose uses this value
            for padding calculations.

          - **PageSizeBytes** *(integer) --*

            The Parquet page size. Column chunks are divided into pages. A page is
            conceptually an indivisible unit (in terms of compression and encoding). The
            minimum value is 64 KiB and the default is 1 MiB.

          - **Compression** *(string) --*

            The compression code to use over data blocks. The possible values are
            ``UNCOMPRESSED`` , ``SNAPPY`` , and ``GZIP`` , with the default being
            ``SNAPPY`` . Use ``SNAPPY`` for higher decompression speed. Use ``GZIP`` if
            the compression ration is more important than speed.

          - **EnableDictionaryCompression** *(boolean) --*

            Indicates whether to enable dictionary compression.

          - **MaxPaddingBytes** *(integer) --*

            The maximum amount of padding to apply. This is useful if you intend to copy
            the data from Amazon S3 to HDFS before querying. The default is 0.

          - **WriterVersion** *(string) --*

            Indicates the version of row format to output. The possible values are ``V1``
            and ``V2`` . The default is ``V1`` .

        - **OrcSerDe** *(dict) --*

          A serializer to use for converting data to the ORC format before storing it in
          Amazon S3. For more information, see `Apache ORC
          <https://orc.apache.org/docs/>`__ .

          - **StripeSizeBytes** *(integer) --*

            The number of bytes in each stripe. The default is 64 MiB and the minimum is
            8 MiB.

          - **BlockSizeBytes** *(integer) --*

            The Hadoop Distributed File System (HDFS) block size. This is useful if you
            intend to copy the data from Amazon S3 to HDFS before querying. The default
            is 256 MiB and the minimum is 64 MiB. Kinesis Data Firehose uses this value
            for padding calculations.

          - **RowIndexStride** *(integer) --*

            The number of rows between index entries. The default is 10,000 and the
            minimum is 1,000.

          - **EnablePadding** *(boolean) --*

            Set this to ``true`` to indicate that you want stripes to be padded to the
            HDFS block boundaries. This is useful if you intend to copy the data from
            Amazon S3 to HDFS before querying. The default is ``false`` .

          - **PaddingTolerance** *(float) --*

            A number between 0 and 1 that defines the tolerance for block padding as a
            decimal fraction of stripe size. The default value is 0.05, which means 5
            percent of stripe size.

            For the default values of 64 MiB ORC stripes and 256 MiB HDFS blocks, the
            default block padding tolerance of 5 percent reserves a maximum of 3.2 MiB
            for padding within the 256 MiB block. In such a case, if the available size
            within the block is more than 3.2 MiB, a new, smaller stripe is inserted to
            fit within that space. This ensures that no stripe crosses block boundaries
            and causes remote reads within a node-local task.

            Kinesis Data Firehose ignores this parameter when  OrcSerDe$EnablePadding is
            ``false`` .

          - **Compression** *(string) --*

            The compression code to use over data blocks. The default is ``SNAPPY`` .

          - **BloomFilterColumns** *(list) --*

            The column names for which you want Kinesis Data Firehose to create bloom
            filters. The default is ``null`` .

            - *(string) --*

          - **BloomFilterFalsePositiveProbability** *(float) --*

            The Bloom filter false positive probability (FPP). The lower the FPP, the
            bigger the Bloom filter. The default value is 0.05, the minimum is 0, and the
            maximum is 1.

          - **DictionaryKeyThreshold** *(float) --*

            Represents the fraction of the total number of non-null rows. To turn off
            dictionary encoding, set this fraction to a number that is less than the
            number of distinct keys in a dictionary. To always use dictionary encoding,
            set this threshold to 1.

          - **FormatVersion** *(string) --*

            The version of the file to write. The possible values are ``V0_11`` and
            ``V0_12`` . The default is ``V0_12`` .

    - **Enabled** *(boolean) --*

      Defaults to ``true`` . Set it to ``false`` if you want to disable format conversion
      while preserving the configuration details.
    """


_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionEncryptionConfigurationKMSEncryptionConfigTypeDef = TypedDict(
    "_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionEncryptionConfigurationKMSEncryptionConfigTypeDef",
    {"AWSKMSKeyARN": str},
    total=False,
)


class ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionEncryptionConfigurationKMSEncryptionConfigTypeDef(
    _ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionEncryptionConfigurationKMSEncryptionConfigTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionEncryptionConfiguration` `KMSEncryptionConfig`

    The encryption key.

    - **AWSKMSKeyARN** *(string) --*

      The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS
      Region as the destination Amazon S3 bucket. For more information, see `Amazon
      Resource Names (ARNs) and AWS Service Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
    """


_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionEncryptionConfigurationTypeDef = TypedDict(
    "_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionEncryptionConfigurationTypeDef",
    {
        "NoEncryptionConfig": str,
        "KMSEncryptionConfig": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionEncryptionConfigurationKMSEncryptionConfigTypeDef,
    },
    total=False,
)


class ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionEncryptionConfigurationTypeDef(
    _ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionEncryptionConfigurationTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescription` `EncryptionConfiguration`

    The encryption configuration. If no value is specified, the default is no encryption.

    - **NoEncryptionConfig** *(string) --*

      Specifically override existing encryption information to ensure that no encryption
      is used.

    - **KMSEncryptionConfig** *(dict) --*

      The encryption key.

      - **AWSKMSKeyARN** *(string) --*

        The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS
        Region as the destination Amazon S3 bucket. For more information, see `Amazon
        Resource Names (ARNs) and AWS Service Namespaces
        <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
    """


_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionProcessingConfigurationProcessorsParametersTypeDef = TypedDict(
    "_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionProcessingConfigurationProcessorsParametersTypeDef",
    {"ParameterName": str, "ParameterValue": str},
    total=False,
)


class ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionProcessingConfigurationProcessorsParametersTypeDef(
    _ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionProcessingConfigurationProcessorsParametersTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionProcessingConfigurationProcessors` `Parameters`

    Describes the processor parameter.

    - **ParameterName** *(string) --*

      The name of the parameter.

    - **ParameterValue** *(string) --*

      The parameter value.
    """


_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionProcessingConfigurationProcessorsTypeDef = TypedDict(
    "_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionProcessingConfigurationProcessorsTypeDef",
    {
        "Type": str,
        "Parameters": List[
            ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionProcessingConfigurationProcessorsParametersTypeDef
        ],
    },
    total=False,
)


class ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionProcessingConfigurationProcessorsTypeDef(
    _ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionProcessingConfigurationProcessorsTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionProcessingConfiguration` `Processors`

    Describes a data processor.

    - **Type** *(string) --*

      The type of processor.

    - **Parameters** *(list) --*

      The processor parameters.

      - *(dict) --*

        Describes the processor parameter.

        - **ParameterName** *(string) --*

          The name of the parameter.

        - **ParameterValue** *(string) --*

          The parameter value.
    """


_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionProcessingConfigurationTypeDef = TypedDict(
    "_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionProcessingConfigurationTypeDef",
    {
        "Enabled": bool,
        "Processors": List[
            ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionProcessingConfigurationProcessorsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionProcessingConfigurationTypeDef(
    _ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionProcessingConfigurationTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescription` `ProcessingConfiguration`

    The data processing configuration.

    - **Enabled** *(boolean) --*

      Enables or disables data processing.

    - **Processors** *(list) --*

      The data processors.

      - *(dict) --*

        Describes a data processor.

        - **Type** *(string) --*

          The type of processor.

        - **Parameters** *(list) --*

          The processor parameters.

          - *(dict) --*

            Describes the processor parameter.

            - **ParameterName** *(string) --*

              The name of the parameter.

            - **ParameterValue** *(string) --*

              The parameter value.
    """


_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionS3BackupDescriptionBufferingHintsTypeDef = TypedDict(
    "_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionS3BackupDescriptionBufferingHintsTypeDef",
    {"SizeInMBs": int, "IntervalInSeconds": int},
    total=False,
)


class ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionS3BackupDescriptionBufferingHintsTypeDef(
    _ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionS3BackupDescriptionBufferingHintsTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionS3BackupDescription` `BufferingHints`

    The buffering option. If no value is specified, ``BufferingHints`` object default
    values are used.

    - **SizeInMBs** *(integer) --*

      Buffer incoming data to the specified size, in MiBs, before delivering it to the
      destination. The default value is 5. This parameter is optional but if you
      specify a value for it, you must also specify a value for ``IntervalInSeconds`` ,
      and vice versa.

      We recommend setting this parameter to a value greater than the amount of data
      you typically ingest into the delivery stream in 10 seconds. For example, if you
      typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

    - **IntervalInSeconds** *(integer) --*

      Buffer incoming data for the specified period of time, in seconds, before
      delivering it to the destination. The default value is 300. This parameter is
      optional but if you specify a value for it, you must also specify a value for
      ``SizeInMBs`` , and vice versa.
    """


_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionS3BackupDescriptionCloudWatchLoggingOptionsTypeDef = TypedDict(
    "_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionS3BackupDescriptionCloudWatchLoggingOptionsTypeDef",
    {"Enabled": bool, "LogGroupName": str, "LogStreamName": str},
    total=False,
)


class ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionS3BackupDescriptionCloudWatchLoggingOptionsTypeDef(
    _ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionS3BackupDescriptionCloudWatchLoggingOptionsTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionS3BackupDescription` `CloudWatchLoggingOptions`

    The Amazon CloudWatch logging options for your delivery stream.

    - **Enabled** *(boolean) --*

      Enables or disables CloudWatch logging.

    - **LogGroupName** *(string) --*

      The CloudWatch group name for logging. This value is required if CloudWatch
      logging is enabled.

    - **LogStreamName** *(string) --*

      The CloudWatch log stream name for logging. This value is required if CloudWatch
      logging is enabled.
    """


_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionS3BackupDescriptionEncryptionConfigurationKMSEncryptionConfigTypeDef = TypedDict(
    "_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionS3BackupDescriptionEncryptionConfigurationKMSEncryptionConfigTypeDef",
    {"AWSKMSKeyARN": str},
    total=False,
)


class ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionS3BackupDescriptionEncryptionConfigurationKMSEncryptionConfigTypeDef(
    _ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionS3BackupDescriptionEncryptionConfigurationKMSEncryptionConfigTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionS3BackupDescriptionEncryptionConfiguration` `KMSEncryptionConfig`

    The encryption key.

    - **AWSKMSKeyARN** *(string) --*

      The Amazon Resource Name (ARN) of the encryption key. Must belong to the same
      AWS Region as the destination Amazon S3 bucket. For more information, see
      `Amazon Resource Names (ARNs) and AWS Service Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__
      .
    """


_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionS3BackupDescriptionEncryptionConfigurationTypeDef = TypedDict(
    "_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionS3BackupDescriptionEncryptionConfigurationTypeDef",
    {
        "NoEncryptionConfig": str,
        "KMSEncryptionConfig": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionS3BackupDescriptionEncryptionConfigurationKMSEncryptionConfigTypeDef,
    },
    total=False,
)


class ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionS3BackupDescriptionEncryptionConfigurationTypeDef(
    _ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionS3BackupDescriptionEncryptionConfigurationTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionS3BackupDescription` `EncryptionConfiguration`

    The encryption configuration. If no value is specified, the default is no
    encryption.

    - **NoEncryptionConfig** *(string) --*

      Specifically override existing encryption information to ensure that no
      encryption is used.

    - **KMSEncryptionConfig** *(dict) --*

      The encryption key.

      - **AWSKMSKeyARN** *(string) --*

        The Amazon Resource Name (ARN) of the encryption key. Must belong to the same
        AWS Region as the destination Amazon S3 bucket. For more information, see
        `Amazon Resource Names (ARNs) and AWS Service Namespaces
        <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__
        .
    """


_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionS3BackupDescriptionTypeDef = TypedDict(
    "_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionS3BackupDescriptionTypeDef",
    {
        "RoleARN": str,
        "BucketARN": str,
        "Prefix": str,
        "ErrorOutputPrefix": str,
        "BufferingHints": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionS3BackupDescriptionBufferingHintsTypeDef,
        "CompressionFormat": str,
        "EncryptionConfiguration": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionS3BackupDescriptionEncryptionConfigurationTypeDef,
        "CloudWatchLoggingOptions": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionS3BackupDescriptionCloudWatchLoggingOptionsTypeDef,
    },
    total=False,
)


class ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionS3BackupDescriptionTypeDef(
    _ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionS3BackupDescriptionTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescription` `S3BackupDescription`

    The configuration for backup in Amazon S3.

    - **RoleARN** *(string) --*

      The Amazon Resource Name (ARN) of the AWS credentials. For more information, see
      `Amazon Resource Names (ARNs) and AWS Service Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

    - **BucketARN** *(string) --*

      The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs)
      and AWS Service Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

    - **Prefix** *(string) --*

      The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered Amazon
      S3 files. You can also specify a custom prefix, as described in `Custom Prefixes
      for Amazon S3 Objects
      <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

    - **ErrorOutputPrefix** *(string) --*

      A prefix that Kinesis Data Firehose evaluates and adds to failed records before
      writing them to S3. This prefix appears immediately following the bucket name. For
      information about how to specify this prefix, see `Custom Prefixes for Amazon S3
      Objects <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

    - **BufferingHints** *(dict) --*

      The buffering option. If no value is specified, ``BufferingHints`` object default
      values are used.

      - **SizeInMBs** *(integer) --*

        Buffer incoming data to the specified size, in MiBs, before delivering it to the
        destination. The default value is 5. This parameter is optional but if you
        specify a value for it, you must also specify a value for ``IntervalInSeconds`` ,
        and vice versa.

        We recommend setting this parameter to a value greater than the amount of data
        you typically ingest into the delivery stream in 10 seconds. For example, if you
        typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

      - **IntervalInSeconds** *(integer) --*

        Buffer incoming data for the specified period of time, in seconds, before
        delivering it to the destination. The default value is 300. This parameter is
        optional but if you specify a value for it, you must also specify a value for
        ``SizeInMBs`` , and vice versa.

    - **CompressionFormat** *(string) --*

      The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .

    - **EncryptionConfiguration** *(dict) --*

      The encryption configuration. If no value is specified, the default is no
      encryption.

      - **NoEncryptionConfig** *(string) --*

        Specifically override existing encryption information to ensure that no
        encryption is used.

      - **KMSEncryptionConfig** *(dict) --*

        The encryption key.

        - **AWSKMSKeyARN** *(string) --*

          The Amazon Resource Name (ARN) of the encryption key. Must belong to the same
          AWS Region as the destination Amazon S3 bucket. For more information, see
          `Amazon Resource Names (ARNs) and AWS Service Namespaces
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__
          .

    - **CloudWatchLoggingOptions** *(dict) --*

      The Amazon CloudWatch logging options for your delivery stream.

      - **Enabled** *(boolean) --*

        Enables or disables CloudWatch logging.

      - **LogGroupName** *(string) --*

        The CloudWatch group name for logging. This value is required if CloudWatch
        logging is enabled.

      - **LogStreamName** *(string) --*

        The CloudWatch log stream name for logging. This value is required if CloudWatch
        logging is enabled.
    """


_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionTypeDef = TypedDict(
    "_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionTypeDef",
    {
        "RoleARN": str,
        "BucketARN": str,
        "Prefix": str,
        "ErrorOutputPrefix": str,
        "BufferingHints": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionBufferingHintsTypeDef,
        "CompressionFormat": str,
        "EncryptionConfiguration": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionEncryptionConfigurationTypeDef,
        "CloudWatchLoggingOptions": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionCloudWatchLoggingOptionsTypeDef,
        "ProcessingConfiguration": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionProcessingConfigurationTypeDef,
        "S3BackupMode": str,
        "S3BackupDescription": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionS3BackupDescriptionTypeDef,
        "DataFormatConversionConfiguration": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationTypeDef,
    },
    total=False,
)


class ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionTypeDef(
    _ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinations` `ExtendedS3DestinationDescription`

    The destination in Amazon S3.

    - **RoleARN** *(string) --*

      The Amazon Resource Name (ARN) of the AWS credentials. For more information, see
      `Amazon Resource Names (ARNs) and AWS Service Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

    - **BucketARN** *(string) --*

      The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs) and
      AWS Service Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

    - **Prefix** *(string) --*

      The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered Amazon S3
      files. You can also specify a custom prefix, as described in `Custom Prefixes for
      Amazon S3 Objects
      <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

    - **ErrorOutputPrefix** *(string) --*

      A prefix that Kinesis Data Firehose evaluates and adds to failed records before
      writing them to S3. This prefix appears immediately following the bucket name. For
      information about how to specify this prefix, see `Custom Prefixes for Amazon S3
      Objects <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

    - **BufferingHints** *(dict) --*

      The buffering option.

      - **SizeInMBs** *(integer) --*

        Buffer incoming data to the specified size, in MiBs, before delivering it to the
        destination. The default value is 5. This parameter is optional but if you specify
        a value for it, you must also specify a value for ``IntervalInSeconds`` , and vice
        versa.

        We recommend setting this parameter to a value greater than the amount of data you
        typically ingest into the delivery stream in 10 seconds. For example, if you
        typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

      - **IntervalInSeconds** *(integer) --*

        Buffer incoming data for the specified period of time, in seconds, before
        delivering it to the destination. The default value is 300. This parameter is
        optional but if you specify a value for it, you must also specify a value for
        ``SizeInMBs`` , and vice versa.

    - **CompressionFormat** *(string) --*

      The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .

    - **EncryptionConfiguration** *(dict) --*

      The encryption configuration. If no value is specified, the default is no encryption.

      - **NoEncryptionConfig** *(string) --*

        Specifically override existing encryption information to ensure that no encryption
        is used.

      - **KMSEncryptionConfig** *(dict) --*

        The encryption key.

        - **AWSKMSKeyARN** *(string) --*

          The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS
          Region as the destination Amazon S3 bucket. For more information, see `Amazon
          Resource Names (ARNs) and AWS Service Namespaces
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

    - **CloudWatchLoggingOptions** *(dict) --*

      The Amazon CloudWatch logging options for your delivery stream.

      - **Enabled** *(boolean) --*

        Enables or disables CloudWatch logging.

      - **LogGroupName** *(string) --*

        The CloudWatch group name for logging. This value is required if CloudWatch logging
        is enabled.

      - **LogStreamName** *(string) --*

        The CloudWatch log stream name for logging. This value is required if CloudWatch
        logging is enabled.

    - **ProcessingConfiguration** *(dict) --*

      The data processing configuration.

      - **Enabled** *(boolean) --*

        Enables or disables data processing.

      - **Processors** *(list) --*

        The data processors.

        - *(dict) --*

          Describes a data processor.

          - **Type** *(string) --*

            The type of processor.

          - **Parameters** *(list) --*

            The processor parameters.

            - *(dict) --*

              Describes the processor parameter.

              - **ParameterName** *(string) --*

                The name of the parameter.

              - **ParameterValue** *(string) --*

                The parameter value.

    - **S3BackupMode** *(string) --*

      The Amazon S3 backup mode.

    - **S3BackupDescription** *(dict) --*

      The configuration for backup in Amazon S3.

      - **RoleARN** *(string) --*

        The Amazon Resource Name (ARN) of the AWS credentials. For more information, see
        `Amazon Resource Names (ARNs) and AWS Service Namespaces
        <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

      - **BucketARN** *(string) --*

        The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs)
        and AWS Service Namespaces
        <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

      - **Prefix** *(string) --*

        The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered Amazon
        S3 files. You can also specify a custom prefix, as described in `Custom Prefixes
        for Amazon S3 Objects
        <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

      - **ErrorOutputPrefix** *(string) --*

        A prefix that Kinesis Data Firehose evaluates and adds to failed records before
        writing them to S3. This prefix appears immediately following the bucket name. For
        information about how to specify this prefix, see `Custom Prefixes for Amazon S3
        Objects <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

      - **BufferingHints** *(dict) --*

        The buffering option. If no value is specified, ``BufferingHints`` object default
        values are used.

        - **SizeInMBs** *(integer) --*

          Buffer incoming data to the specified size, in MiBs, before delivering it to the
          destination. The default value is 5. This parameter is optional but if you
          specify a value for it, you must also specify a value for ``IntervalInSeconds`` ,
          and vice versa.

          We recommend setting this parameter to a value greater than the amount of data
          you typically ingest into the delivery stream in 10 seconds. For example, if you
          typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

        - **IntervalInSeconds** *(integer) --*

          Buffer incoming data for the specified period of time, in seconds, before
          delivering it to the destination. The default value is 300. This parameter is
          optional but if you specify a value for it, you must also specify a value for
          ``SizeInMBs`` , and vice versa.

      - **CompressionFormat** *(string) --*

        The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .

      - **EncryptionConfiguration** *(dict) --*

        The encryption configuration. If no value is specified, the default is no
        encryption.

        - **NoEncryptionConfig** *(string) --*

          Specifically override existing encryption information to ensure that no
          encryption is used.

        - **KMSEncryptionConfig** *(dict) --*

          The encryption key.

          - **AWSKMSKeyARN** *(string) --*

            The Amazon Resource Name (ARN) of the encryption key. Must belong to the same
            AWS Region as the destination Amazon S3 bucket. For more information, see
            `Amazon Resource Names (ARNs) and AWS Service Namespaces
            <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__
            .

      - **CloudWatchLoggingOptions** *(dict) --*

        The Amazon CloudWatch logging options for your delivery stream.

        - **Enabled** *(boolean) --*

          Enables or disables CloudWatch logging.

        - **LogGroupName** *(string) --*

          The CloudWatch group name for logging. This value is required if CloudWatch
          logging is enabled.

        - **LogStreamName** *(string) --*

          The CloudWatch log stream name for logging. This value is required if CloudWatch
          logging is enabled.

    - **DataFormatConversionConfiguration** *(dict) --*

      The serializer, deserializer, and schema for converting data from the JSON format to
      the Parquet or ORC format before writing it to Amazon S3.

      - **SchemaConfiguration** *(dict) --*

        Specifies the AWS Glue Data Catalog table that contains the column information.

        - **RoleARN** *(string) --*

          The role that Kinesis Data Firehose can use to access AWS Glue. This role must be
          in the same account you use for Kinesis Data Firehose. Cross-account roles aren't
          allowed.

        - **CatalogId** *(string) --*

          The ID of the AWS Glue Data Catalog. If you don't supply this, the AWS account ID
          is used by default.

        - **DatabaseName** *(string) --*

          Specifies the name of the AWS Glue database that contains the schema for the
          output data.

        - **TableName** *(string) --*

          Specifies the AWS Glue table that contains the column information that
          constitutes your data schema.

        - **Region** *(string) --*

          If you don't specify an AWS Region, the default is the current Region.

        - **VersionId** *(string) --*

          Specifies the table version for the output data schema. If you don't specify this
          version ID, or if you set it to ``LATEST`` , Kinesis Data Firehose uses the most
          recent version. This means that any updates to the table are automatically picked
          up.

      - **InputFormatConfiguration** *(dict) --*

        Specifies the deserializer that you want Kinesis Data Firehose to use to convert
        the format of your data from JSON.

        - **Deserializer** *(dict) --*

          Specifies which deserializer to use. You can choose either the Apache Hive JSON
          SerDe or the OpenX JSON SerDe. If both are non-null, the server rejects the
          request.

          - **OpenXJsonSerDe** *(dict) --*

            The OpenX SerDe. Used by Kinesis Data Firehose for deserializing data, which
            means converting it from the JSON format in preparation for serializing it to
            the Parquet or ORC format. This is one of two deserializers you can choose,
            depending on which one offers the functionality you need. The other option is
            the native Hive / HCatalog JsonSerDe.

            - **ConvertDotsInJsonKeysToUnderscores** *(boolean) --*

              When set to ``true`` , specifies that the names of the keys include dots and
              that you want Kinesis Data Firehose to replace them with underscores. This is
              useful because Apache Hive does not allow dots in column names. For example,
              if the JSON contains a key whose name is "a.b", you can define the column
              name to be "a_b" when using this option.

              The default is ``false`` .

            - **CaseInsensitive** *(boolean) --*

              When set to ``true`` , which is the default, Kinesis Data Firehose converts
              JSON keys to lowercase before deserializing them.

            - **ColumnToJsonKeyMappings** *(dict) --*

              Maps column names to JSON keys that aren't identical to the column names.
              This is useful when the JSON contains keys that are Hive keywords. For
              example, ``timestamp`` is a Hive keyword. If you have a JSON key named
              ``timestamp`` , set this parameter to ``{"ts": "timestamp"}`` to map this key
              to a column named ``ts`` .

              - *(string) --*

                - *(string) --*

          - **HiveJsonSerDe** *(dict) --*

            The native Hive / HCatalog JsonSerDe. Used by Kinesis Data Firehose for
            deserializing data, which means converting it from the JSON format in
            preparation for serializing it to the Parquet or ORC format. This is one of two
            deserializers you can choose, depending on which one offers the functionality
            you need. The other option is the OpenX SerDe.

            - **TimestampFormats** *(list) --*

              Indicates how you want Kinesis Data Firehose to parse the date and timestamps
              that may be present in your input data JSON. To specify these format strings,
              follow the pattern syntax of JodaTime's DateTimeFormat format strings. For
              more information, see `Class DateTimeFormat
              <https://www.joda.org/joda-time/apidocs/org/joda/time/format/DateTimeFormat.html>`__
              . You can also use the special value ``millis`` to parse timestamps in epoch
              milliseconds. If you don't specify a format, Kinesis Data Firehose uses
              ``java.sql.Timestamp::valueOf`` by default.

              - *(string) --*

      - **OutputFormatConfiguration** *(dict) --*

        Specifies the serializer that you want Kinesis Data Firehose to use to convert the
        format of your data to the Parquet or ORC format.

        - **Serializer** *(dict) --*

          Specifies which serializer to use. You can choose either the ORC SerDe or the
          Parquet SerDe. If both are non-null, the server rejects the request.

          - **ParquetSerDe** *(dict) --*

            A serializer to use for converting data to the Parquet format before storing it
            in Amazon S3. For more information, see `Apache Parquet
            <https://parquet.apache.org/documentation/latest/>`__ .

            - **BlockSizeBytes** *(integer) --*

              The Hadoop Distributed File System (HDFS) block size. This is useful if you
              intend to copy the data from Amazon S3 to HDFS before querying. The default
              is 256 MiB and the minimum is 64 MiB. Kinesis Data Firehose uses this value
              for padding calculations.

            - **PageSizeBytes** *(integer) --*

              The Parquet page size. Column chunks are divided into pages. A page is
              conceptually an indivisible unit (in terms of compression and encoding). The
              minimum value is 64 KiB and the default is 1 MiB.

            - **Compression** *(string) --*

              The compression code to use over data blocks. The possible values are
              ``UNCOMPRESSED`` , ``SNAPPY`` , and ``GZIP`` , with the default being
              ``SNAPPY`` . Use ``SNAPPY`` for higher decompression speed. Use ``GZIP`` if
              the compression ration is more important than speed.

            - **EnableDictionaryCompression** *(boolean) --*

              Indicates whether to enable dictionary compression.

            - **MaxPaddingBytes** *(integer) --*

              The maximum amount of padding to apply. This is useful if you intend to copy
              the data from Amazon S3 to HDFS before querying. The default is 0.

            - **WriterVersion** *(string) --*

              Indicates the version of row format to output. The possible values are ``V1``
              and ``V2`` . The default is ``V1`` .

          - **OrcSerDe** *(dict) --*

            A serializer to use for converting data to the ORC format before storing it in
            Amazon S3. For more information, see `Apache ORC
            <https://orc.apache.org/docs/>`__ .

            - **StripeSizeBytes** *(integer) --*

              The number of bytes in each stripe. The default is 64 MiB and the minimum is
              8 MiB.

            - **BlockSizeBytes** *(integer) --*

              The Hadoop Distributed File System (HDFS) block size. This is useful if you
              intend to copy the data from Amazon S3 to HDFS before querying. The default
              is 256 MiB and the minimum is 64 MiB. Kinesis Data Firehose uses this value
              for padding calculations.

            - **RowIndexStride** *(integer) --*

              The number of rows between index entries. The default is 10,000 and the
              minimum is 1,000.

            - **EnablePadding** *(boolean) --*

              Set this to ``true`` to indicate that you want stripes to be padded to the
              HDFS block boundaries. This is useful if you intend to copy the data from
              Amazon S3 to HDFS before querying. The default is ``false`` .

            - **PaddingTolerance** *(float) --*

              A number between 0 and 1 that defines the tolerance for block padding as a
              decimal fraction of stripe size. The default value is 0.05, which means 5
              percent of stripe size.

              For the default values of 64 MiB ORC stripes and 256 MiB HDFS blocks, the
              default block padding tolerance of 5 percent reserves a maximum of 3.2 MiB
              for padding within the 256 MiB block. In such a case, if the available size
              within the block is more than 3.2 MiB, a new, smaller stripe is inserted to
              fit within that space. This ensures that no stripe crosses block boundaries
              and causes remote reads within a node-local task.

              Kinesis Data Firehose ignores this parameter when  OrcSerDe$EnablePadding is
              ``false`` .

            - **Compression** *(string) --*

              The compression code to use over data blocks. The default is ``SNAPPY`` .

            - **BloomFilterColumns** *(list) --*

              The column names for which you want Kinesis Data Firehose to create bloom
              filters. The default is ``null`` .

              - *(string) --*

            - **BloomFilterFalsePositiveProbability** *(float) --*

              The Bloom filter false positive probability (FPP). The lower the FPP, the
              bigger the Bloom filter. The default value is 0.05, the minimum is 0, and the
              maximum is 1.

            - **DictionaryKeyThreshold** *(float) --*

              Represents the fraction of the total number of non-null rows. To turn off
              dictionary encoding, set this fraction to a number that is less than the
              number of distinct keys in a dictionary. To always use dictionary encoding,
              set this threshold to 1.

            - **FormatVersion** *(string) --*

              The version of the file to write. The possible values are ``V0_11`` and
              ``V0_12`` . The default is ``V0_12`` .

      - **Enabled** *(boolean) --*

        Defaults to ``true`` . Set it to ``false`` if you want to disable format conversion
        while preserving the configuration details.
    """


_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionCloudWatchLoggingOptionsTypeDef = TypedDict(
    "_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionCloudWatchLoggingOptionsTypeDef",
    {"Enabled": bool, "LogGroupName": str, "LogStreamName": str},
    total=False,
)


class ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionCloudWatchLoggingOptionsTypeDef(
    _ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionCloudWatchLoggingOptionsTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescription` `CloudWatchLoggingOptions`

    The Amazon CloudWatch logging options for your delivery stream.

    - **Enabled** *(boolean) --*

      Enables or disables CloudWatch logging.

    - **LogGroupName** *(string) --*

      The CloudWatch group name for logging. This value is required if CloudWatch logging
      is enabled.

    - **LogStreamName** *(string) --*

      The CloudWatch log stream name for logging. This value is required if CloudWatch
      logging is enabled.
    """


_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionCopyCommandTypeDef = TypedDict(
    "_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionCopyCommandTypeDef",
    {"DataTableName": str, "DataTableColumns": str, "CopyOptions": str},
    total=False,
)


class ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionCopyCommandTypeDef(
    _ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionCopyCommandTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescription` `CopyCommand`

    The ``COPY`` command.

    - **DataTableName** *(string) --*

      The name of the target table. The table must already exist in the database.

    - **DataTableColumns** *(string) --*

      A comma-separated list of column names.

    - **CopyOptions** *(string) --*

      Optional parameters to use with the Amazon Redshift ``COPY`` command. For more
      information, see the "Optional Parameters" section of `Amazon Redshift COPY command
      <https://docs.aws.amazon.com/redshift/latest/dg/r_COPY.html>`__ . Some possible
      examples that would apply to Kinesis Data Firehose are as follows:

       ``delimiter '\\t' lzop;`` - fields are delimited with "\\t" (TAB character) and
       compressed using lzop.

       ``delimiter '|'`` - fields are delimited with "|" (this is the default delimiter).

       ``delimiter '|' escape`` - the delimiter should be escaped.

       ``fixedwidth 'venueid:3,venuename:25,venuecity:12,venuestate:2,venueseats:6'`` -
       fields are fixed width in the source, with each width specified after every column
       in the table.

       ``JSON 's3://mybucket/jsonpaths.txt'`` - data is in JSON format, and the path
       specified is the format of the data.

      For more examples, see `Amazon Redshift COPY command examples
      <https://docs.aws.amazon.com/redshift/latest/dg/r_COPY_command_examples.html>`__ .
    """


_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionProcessingConfigurationProcessorsParametersTypeDef = TypedDict(
    "_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionProcessingConfigurationProcessorsParametersTypeDef",
    {"ParameterName": str, "ParameterValue": str},
    total=False,
)


class ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionProcessingConfigurationProcessorsParametersTypeDef(
    _ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionProcessingConfigurationProcessorsParametersTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionProcessingConfigurationProcessors` `Parameters`

    Describes the processor parameter.

    - **ParameterName** *(string) --*

      The name of the parameter.

    - **ParameterValue** *(string) --*

      The parameter value.
    """


_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionProcessingConfigurationProcessorsTypeDef = TypedDict(
    "_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionProcessingConfigurationProcessorsTypeDef",
    {
        "Type": str,
        "Parameters": List[
            ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionProcessingConfigurationProcessorsParametersTypeDef
        ],
    },
    total=False,
)


class ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionProcessingConfigurationProcessorsTypeDef(
    _ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionProcessingConfigurationProcessorsTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionProcessingConfiguration` `Processors`

    Describes a data processor.

    - **Type** *(string) --*

      The type of processor.

    - **Parameters** *(list) --*

      The processor parameters.

      - *(dict) --*

        Describes the processor parameter.

        - **ParameterName** *(string) --*

          The name of the parameter.

        - **ParameterValue** *(string) --*

          The parameter value.
    """


_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionProcessingConfigurationTypeDef = TypedDict(
    "_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionProcessingConfigurationTypeDef",
    {
        "Enabled": bool,
        "Processors": List[
            ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionProcessingConfigurationProcessorsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionProcessingConfigurationTypeDef(
    _ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionProcessingConfigurationTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescription` `ProcessingConfiguration`

    The data processing configuration.

    - **Enabled** *(boolean) --*

      Enables or disables data processing.

    - **Processors** *(list) --*

      The data processors.

      - *(dict) --*

        Describes a data processor.

        - **Type** *(string) --*

          The type of processor.

        - **Parameters** *(list) --*

          The processor parameters.

          - *(dict) --*

            Describes the processor parameter.

            - **ParameterName** *(string) --*

              The name of the parameter.

            - **ParameterValue** *(string) --*

              The parameter value.
    """


_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionRetryOptionsTypeDef = TypedDict(
    "_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionRetryOptionsTypeDef",
    {"DurationInSeconds": int},
    total=False,
)


class ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionRetryOptionsTypeDef(
    _ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionRetryOptionsTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescription` `RetryOptions`

    The retry behavior in case Kinesis Data Firehose is unable to deliver documents to
    Amazon Redshift. Default value is 3600 (60 minutes).

    - **DurationInSeconds** *(integer) --*

      The length of time during which Kinesis Data Firehose retries delivery after a
      failure, starting from the initial request and including the first attempt. The
      default value is 3600 seconds (60 minutes). Kinesis Data Firehose does not retry if
      the value of ``DurationInSeconds`` is 0 (zero) or if the first delivery attempt
      takes longer than the current value.
    """


_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3BackupDescriptionBufferingHintsTypeDef = TypedDict(
    "_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3BackupDescriptionBufferingHintsTypeDef",
    {"SizeInMBs": int, "IntervalInSeconds": int},
    total=False,
)


class ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3BackupDescriptionBufferingHintsTypeDef(
    _ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3BackupDescriptionBufferingHintsTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3BackupDescription` `BufferingHints`

    The buffering option. If no value is specified, ``BufferingHints`` object default
    values are used.

    - **SizeInMBs** *(integer) --*

      Buffer incoming data to the specified size, in MiBs, before delivering it to the
      destination. The default value is 5. This parameter is optional but if you
      specify a value for it, you must also specify a value for ``IntervalInSeconds`` ,
      and vice versa.

      We recommend setting this parameter to a value greater than the amount of data
      you typically ingest into the delivery stream in 10 seconds. For example, if you
      typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

    - **IntervalInSeconds** *(integer) --*

      Buffer incoming data for the specified period of time, in seconds, before
      delivering it to the destination. The default value is 300. This parameter is
      optional but if you specify a value for it, you must also specify a value for
      ``SizeInMBs`` , and vice versa.
    """


_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3BackupDescriptionCloudWatchLoggingOptionsTypeDef = TypedDict(
    "_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3BackupDescriptionCloudWatchLoggingOptionsTypeDef",
    {"Enabled": bool, "LogGroupName": str, "LogStreamName": str},
    total=False,
)


class ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3BackupDescriptionCloudWatchLoggingOptionsTypeDef(
    _ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3BackupDescriptionCloudWatchLoggingOptionsTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3BackupDescription` `CloudWatchLoggingOptions`

    The Amazon CloudWatch logging options for your delivery stream.

    - **Enabled** *(boolean) --*

      Enables or disables CloudWatch logging.

    - **LogGroupName** *(string) --*

      The CloudWatch group name for logging. This value is required if CloudWatch
      logging is enabled.

    - **LogStreamName** *(string) --*

      The CloudWatch log stream name for logging. This value is required if CloudWatch
      logging is enabled.
    """


_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3BackupDescriptionEncryptionConfigurationKMSEncryptionConfigTypeDef = TypedDict(
    "_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3BackupDescriptionEncryptionConfigurationKMSEncryptionConfigTypeDef",
    {"AWSKMSKeyARN": str},
    total=False,
)


class ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3BackupDescriptionEncryptionConfigurationKMSEncryptionConfigTypeDef(
    _ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3BackupDescriptionEncryptionConfigurationKMSEncryptionConfigTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3BackupDescriptionEncryptionConfiguration` `KMSEncryptionConfig`

    The encryption key.

    - **AWSKMSKeyARN** *(string) --*

      The Amazon Resource Name (ARN) of the encryption key. Must belong to the same
      AWS Region as the destination Amazon S3 bucket. For more information, see
      `Amazon Resource Names (ARNs) and AWS Service Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__
      .
    """


_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3BackupDescriptionEncryptionConfigurationTypeDef = TypedDict(
    "_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3BackupDescriptionEncryptionConfigurationTypeDef",
    {
        "NoEncryptionConfig": str,
        "KMSEncryptionConfig": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3BackupDescriptionEncryptionConfigurationKMSEncryptionConfigTypeDef,
    },
    total=False,
)


class ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3BackupDescriptionEncryptionConfigurationTypeDef(
    _ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3BackupDescriptionEncryptionConfigurationTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3BackupDescription` `EncryptionConfiguration`

    The encryption configuration. If no value is specified, the default is no
    encryption.

    - **NoEncryptionConfig** *(string) --*

      Specifically override existing encryption information to ensure that no
      encryption is used.

    - **KMSEncryptionConfig** *(dict) --*

      The encryption key.

      - **AWSKMSKeyARN** *(string) --*

        The Amazon Resource Name (ARN) of the encryption key. Must belong to the same
        AWS Region as the destination Amazon S3 bucket. For more information, see
        `Amazon Resource Names (ARNs) and AWS Service Namespaces
        <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__
        .
    """


_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3BackupDescriptionTypeDef = TypedDict(
    "_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3BackupDescriptionTypeDef",
    {
        "RoleARN": str,
        "BucketARN": str,
        "Prefix": str,
        "ErrorOutputPrefix": str,
        "BufferingHints": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3BackupDescriptionBufferingHintsTypeDef,
        "CompressionFormat": str,
        "EncryptionConfiguration": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3BackupDescriptionEncryptionConfigurationTypeDef,
        "CloudWatchLoggingOptions": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3BackupDescriptionCloudWatchLoggingOptionsTypeDef,
    },
    total=False,
)


class ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3BackupDescriptionTypeDef(
    _ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3BackupDescriptionTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescription` `S3BackupDescription`

    The configuration for backup in Amazon S3.

    - **RoleARN** *(string) --*

      The Amazon Resource Name (ARN) of the AWS credentials. For more information, see
      `Amazon Resource Names (ARNs) and AWS Service Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

    - **BucketARN** *(string) --*

      The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs)
      and AWS Service Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

    - **Prefix** *(string) --*

      The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered Amazon
      S3 files. You can also specify a custom prefix, as described in `Custom Prefixes
      for Amazon S3 Objects
      <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

    - **ErrorOutputPrefix** *(string) --*

      A prefix that Kinesis Data Firehose evaluates and adds to failed records before
      writing them to S3. This prefix appears immediately following the bucket name. For
      information about how to specify this prefix, see `Custom Prefixes for Amazon S3
      Objects <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

    - **BufferingHints** *(dict) --*

      The buffering option. If no value is specified, ``BufferingHints`` object default
      values are used.

      - **SizeInMBs** *(integer) --*

        Buffer incoming data to the specified size, in MiBs, before delivering it to the
        destination. The default value is 5. This parameter is optional but if you
        specify a value for it, you must also specify a value for ``IntervalInSeconds`` ,
        and vice versa.

        We recommend setting this parameter to a value greater than the amount of data
        you typically ingest into the delivery stream in 10 seconds. For example, if you
        typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

      - **IntervalInSeconds** *(integer) --*

        Buffer incoming data for the specified period of time, in seconds, before
        delivering it to the destination. The default value is 300. This parameter is
        optional but if you specify a value for it, you must also specify a value for
        ``SizeInMBs`` , and vice versa.

    - **CompressionFormat** *(string) --*

      The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .

    - **EncryptionConfiguration** *(dict) --*

      The encryption configuration. If no value is specified, the default is no
      encryption.

      - **NoEncryptionConfig** *(string) --*

        Specifically override existing encryption information to ensure that no
        encryption is used.

      - **KMSEncryptionConfig** *(dict) --*

        The encryption key.

        - **AWSKMSKeyARN** *(string) --*

          The Amazon Resource Name (ARN) of the encryption key. Must belong to the same
          AWS Region as the destination Amazon S3 bucket. For more information, see
          `Amazon Resource Names (ARNs) and AWS Service Namespaces
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__
          .

    - **CloudWatchLoggingOptions** *(dict) --*

      The Amazon CloudWatch logging options for your delivery stream.

      - **Enabled** *(boolean) --*

        Enables or disables CloudWatch logging.

      - **LogGroupName** *(string) --*

        The CloudWatch group name for logging. This value is required if CloudWatch
        logging is enabled.

      - **LogStreamName** *(string) --*

        The CloudWatch log stream name for logging. This value is required if CloudWatch
        logging is enabled.
    """


_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3DestinationDescriptionBufferingHintsTypeDef = TypedDict(
    "_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3DestinationDescriptionBufferingHintsTypeDef",
    {"SizeInMBs": int, "IntervalInSeconds": int},
    total=False,
)


class ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3DestinationDescriptionBufferingHintsTypeDef(
    _ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3DestinationDescriptionBufferingHintsTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3DestinationDescription` `BufferingHints`

    The buffering option. If no value is specified, ``BufferingHints`` object default
    values are used.

    - **SizeInMBs** *(integer) --*

      Buffer incoming data to the specified size, in MiBs, before delivering it to the
      destination. The default value is 5. This parameter is optional but if you
      specify a value for it, you must also specify a value for ``IntervalInSeconds`` ,
      and vice versa.

      We recommend setting this parameter to a value greater than the amount of data
      you typically ingest into the delivery stream in 10 seconds. For example, if you
      typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

    - **IntervalInSeconds** *(integer) --*

      Buffer incoming data for the specified period of time, in seconds, before
      delivering it to the destination. The default value is 300. This parameter is
      optional but if you specify a value for it, you must also specify a value for
      ``SizeInMBs`` , and vice versa.
    """


_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3DestinationDescriptionCloudWatchLoggingOptionsTypeDef = TypedDict(
    "_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3DestinationDescriptionCloudWatchLoggingOptionsTypeDef",
    {"Enabled": bool, "LogGroupName": str, "LogStreamName": str},
    total=False,
)


class ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3DestinationDescriptionCloudWatchLoggingOptionsTypeDef(
    _ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3DestinationDescriptionCloudWatchLoggingOptionsTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3DestinationDescription` `CloudWatchLoggingOptions`

    The Amazon CloudWatch logging options for your delivery stream.

    - **Enabled** *(boolean) --*

      Enables or disables CloudWatch logging.

    - **LogGroupName** *(string) --*

      The CloudWatch group name for logging. This value is required if CloudWatch
      logging is enabled.

    - **LogStreamName** *(string) --*

      The CloudWatch log stream name for logging. This value is required if CloudWatch
      logging is enabled.
    """


_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3DestinationDescriptionEncryptionConfigurationKMSEncryptionConfigTypeDef = TypedDict(
    "_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3DestinationDescriptionEncryptionConfigurationKMSEncryptionConfigTypeDef",
    {"AWSKMSKeyARN": str},
    total=False,
)


class ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3DestinationDescriptionEncryptionConfigurationKMSEncryptionConfigTypeDef(
    _ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3DestinationDescriptionEncryptionConfigurationKMSEncryptionConfigTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3DestinationDescriptionEncryptionConfiguration` `KMSEncryptionConfig`

    The encryption key.

    - **AWSKMSKeyARN** *(string) --*

      The Amazon Resource Name (ARN) of the encryption key. Must belong to the same
      AWS Region as the destination Amazon S3 bucket. For more information, see
      `Amazon Resource Names (ARNs) and AWS Service Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__
      .
    """


_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3DestinationDescriptionEncryptionConfigurationTypeDef = TypedDict(
    "_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3DestinationDescriptionEncryptionConfigurationTypeDef",
    {
        "NoEncryptionConfig": str,
        "KMSEncryptionConfig": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3DestinationDescriptionEncryptionConfigurationKMSEncryptionConfigTypeDef,
    },
    total=False,
)


class ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3DestinationDescriptionEncryptionConfigurationTypeDef(
    _ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3DestinationDescriptionEncryptionConfigurationTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3DestinationDescription` `EncryptionConfiguration`

    The encryption configuration. If no value is specified, the default is no
    encryption.

    - **NoEncryptionConfig** *(string) --*

      Specifically override existing encryption information to ensure that no
      encryption is used.

    - **KMSEncryptionConfig** *(dict) --*

      The encryption key.

      - **AWSKMSKeyARN** *(string) --*

        The Amazon Resource Name (ARN) of the encryption key. Must belong to the same
        AWS Region as the destination Amazon S3 bucket. For more information, see
        `Amazon Resource Names (ARNs) and AWS Service Namespaces
        <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__
        .
    """


_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3DestinationDescriptionTypeDef = TypedDict(
    "_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3DestinationDescriptionTypeDef",
    {
        "RoleARN": str,
        "BucketARN": str,
        "Prefix": str,
        "ErrorOutputPrefix": str,
        "BufferingHints": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3DestinationDescriptionBufferingHintsTypeDef,
        "CompressionFormat": str,
        "EncryptionConfiguration": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3DestinationDescriptionEncryptionConfigurationTypeDef,
        "CloudWatchLoggingOptions": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3DestinationDescriptionCloudWatchLoggingOptionsTypeDef,
    },
    total=False,
)


class ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3DestinationDescriptionTypeDef(
    _ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3DestinationDescriptionTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescription` `S3DestinationDescription`

    The Amazon S3 destination.

    - **RoleARN** *(string) --*

      The Amazon Resource Name (ARN) of the AWS credentials. For more information, see
      `Amazon Resource Names (ARNs) and AWS Service Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

    - **BucketARN** *(string) --*

      The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs)
      and AWS Service Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

    - **Prefix** *(string) --*

      The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered Amazon
      S3 files. You can also specify a custom prefix, as described in `Custom Prefixes
      for Amazon S3 Objects
      <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

    - **ErrorOutputPrefix** *(string) --*

      A prefix that Kinesis Data Firehose evaluates and adds to failed records before
      writing them to S3. This prefix appears immediately following the bucket name. For
      information about how to specify this prefix, see `Custom Prefixes for Amazon S3
      Objects <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

    - **BufferingHints** *(dict) --*

      The buffering option. If no value is specified, ``BufferingHints`` object default
      values are used.

      - **SizeInMBs** *(integer) --*

        Buffer incoming data to the specified size, in MiBs, before delivering it to the
        destination. The default value is 5. This parameter is optional but if you
        specify a value for it, you must also specify a value for ``IntervalInSeconds`` ,
        and vice versa.

        We recommend setting this parameter to a value greater than the amount of data
        you typically ingest into the delivery stream in 10 seconds. For example, if you
        typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

      - **IntervalInSeconds** *(integer) --*

        Buffer incoming data for the specified period of time, in seconds, before
        delivering it to the destination. The default value is 300. This parameter is
        optional but if you specify a value for it, you must also specify a value for
        ``SizeInMBs`` , and vice versa.

    - **CompressionFormat** *(string) --*

      The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .

    - **EncryptionConfiguration** *(dict) --*

      The encryption configuration. If no value is specified, the default is no
      encryption.

      - **NoEncryptionConfig** *(string) --*

        Specifically override existing encryption information to ensure that no
        encryption is used.

      - **KMSEncryptionConfig** *(dict) --*

        The encryption key.

        - **AWSKMSKeyARN** *(string) --*

          The Amazon Resource Name (ARN) of the encryption key. Must belong to the same
          AWS Region as the destination Amazon S3 bucket. For more information, see
          `Amazon Resource Names (ARNs) and AWS Service Namespaces
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__
          .

    - **CloudWatchLoggingOptions** *(dict) --*

      The Amazon CloudWatch logging options for your delivery stream.

      - **Enabled** *(boolean) --*

        Enables or disables CloudWatch logging.

      - **LogGroupName** *(string) --*

        The CloudWatch group name for logging. This value is required if CloudWatch
        logging is enabled.

      - **LogStreamName** *(string) --*

        The CloudWatch log stream name for logging. This value is required if CloudWatch
        logging is enabled.
    """


_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionTypeDef = TypedDict(
    "_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionTypeDef",
    {
        "RoleARN": str,
        "ClusterJDBCURL": str,
        "CopyCommand": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionCopyCommandTypeDef,
        "Username": str,
        "RetryOptions": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionRetryOptionsTypeDef,
        "S3DestinationDescription": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3DestinationDescriptionTypeDef,
        "ProcessingConfiguration": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionProcessingConfigurationTypeDef,
        "S3BackupMode": str,
        "S3BackupDescription": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3BackupDescriptionTypeDef,
        "CloudWatchLoggingOptions": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionCloudWatchLoggingOptionsTypeDef,
    },
    total=False,
)


class ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionTypeDef(
    _ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinations` `RedshiftDestinationDescription`

    The destination in Amazon Redshift.

    - **RoleARN** *(string) --*

      The Amazon Resource Name (ARN) of the AWS credentials. For more information, see
      `Amazon Resource Names (ARNs) and AWS Service Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

    - **ClusterJDBCURL** *(string) --*

      The database connection string.

    - **CopyCommand** *(dict) --*

      The ``COPY`` command.

      - **DataTableName** *(string) --*

        The name of the target table. The table must already exist in the database.

      - **DataTableColumns** *(string) --*

        A comma-separated list of column names.

      - **CopyOptions** *(string) --*

        Optional parameters to use with the Amazon Redshift ``COPY`` command. For more
        information, see the "Optional Parameters" section of `Amazon Redshift COPY command
        <https://docs.aws.amazon.com/redshift/latest/dg/r_COPY.html>`__ . Some possible
        examples that would apply to Kinesis Data Firehose are as follows:

         ``delimiter '\\t' lzop;`` - fields are delimited with "\\t" (TAB character) and
         compressed using lzop.

         ``delimiter '|'`` - fields are delimited with "|" (this is the default delimiter).

         ``delimiter '|' escape`` - the delimiter should be escaped.

         ``fixedwidth 'venueid:3,venuename:25,venuecity:12,venuestate:2,venueseats:6'`` -
         fields are fixed width in the source, with each width specified after every column
         in the table.

         ``JSON 's3://mybucket/jsonpaths.txt'`` - data is in JSON format, and the path
         specified is the format of the data.

        For more examples, see `Amazon Redshift COPY command examples
        <https://docs.aws.amazon.com/redshift/latest/dg/r_COPY_command_examples.html>`__ .

    - **Username** *(string) --*

      The name of the user.

    - **RetryOptions** *(dict) --*

      The retry behavior in case Kinesis Data Firehose is unable to deliver documents to
      Amazon Redshift. Default value is 3600 (60 minutes).

      - **DurationInSeconds** *(integer) --*

        The length of time during which Kinesis Data Firehose retries delivery after a
        failure, starting from the initial request and including the first attempt. The
        default value is 3600 seconds (60 minutes). Kinesis Data Firehose does not retry if
        the value of ``DurationInSeconds`` is 0 (zero) or if the first delivery attempt
        takes longer than the current value.

    - **S3DestinationDescription** *(dict) --*

      The Amazon S3 destination.

      - **RoleARN** *(string) --*

        The Amazon Resource Name (ARN) of the AWS credentials. For more information, see
        `Amazon Resource Names (ARNs) and AWS Service Namespaces
        <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

      - **BucketARN** *(string) --*

        The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs)
        and AWS Service Namespaces
        <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

      - **Prefix** *(string) --*

        The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered Amazon
        S3 files. You can also specify a custom prefix, as described in `Custom Prefixes
        for Amazon S3 Objects
        <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

      - **ErrorOutputPrefix** *(string) --*

        A prefix that Kinesis Data Firehose evaluates and adds to failed records before
        writing them to S3. This prefix appears immediately following the bucket name. For
        information about how to specify this prefix, see `Custom Prefixes for Amazon S3
        Objects <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

      - **BufferingHints** *(dict) --*

        The buffering option. If no value is specified, ``BufferingHints`` object default
        values are used.

        - **SizeInMBs** *(integer) --*

          Buffer incoming data to the specified size, in MiBs, before delivering it to the
          destination. The default value is 5. This parameter is optional but if you
          specify a value for it, you must also specify a value for ``IntervalInSeconds`` ,
          and vice versa.

          We recommend setting this parameter to a value greater than the amount of data
          you typically ingest into the delivery stream in 10 seconds. For example, if you
          typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

        - **IntervalInSeconds** *(integer) --*

          Buffer incoming data for the specified period of time, in seconds, before
          delivering it to the destination. The default value is 300. This parameter is
          optional but if you specify a value for it, you must also specify a value for
          ``SizeInMBs`` , and vice versa.

      - **CompressionFormat** *(string) --*

        The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .

      - **EncryptionConfiguration** *(dict) --*

        The encryption configuration. If no value is specified, the default is no
        encryption.

        - **NoEncryptionConfig** *(string) --*

          Specifically override existing encryption information to ensure that no
          encryption is used.

        - **KMSEncryptionConfig** *(dict) --*

          The encryption key.

          - **AWSKMSKeyARN** *(string) --*

            The Amazon Resource Name (ARN) of the encryption key. Must belong to the same
            AWS Region as the destination Amazon S3 bucket. For more information, see
            `Amazon Resource Names (ARNs) and AWS Service Namespaces
            <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__
            .

      - **CloudWatchLoggingOptions** *(dict) --*

        The Amazon CloudWatch logging options for your delivery stream.

        - **Enabled** *(boolean) --*

          Enables or disables CloudWatch logging.

        - **LogGroupName** *(string) --*

          The CloudWatch group name for logging. This value is required if CloudWatch
          logging is enabled.

        - **LogStreamName** *(string) --*

          The CloudWatch log stream name for logging. This value is required if CloudWatch
          logging is enabled.

    - **ProcessingConfiguration** *(dict) --*

      The data processing configuration.

      - **Enabled** *(boolean) --*

        Enables or disables data processing.

      - **Processors** *(list) --*

        The data processors.

        - *(dict) --*

          Describes a data processor.

          - **Type** *(string) --*

            The type of processor.

          - **Parameters** *(list) --*

            The processor parameters.

            - *(dict) --*

              Describes the processor parameter.

              - **ParameterName** *(string) --*

                The name of the parameter.

              - **ParameterValue** *(string) --*

                The parameter value.

    - **S3BackupMode** *(string) --*

      The Amazon S3 backup mode.

    - **S3BackupDescription** *(dict) --*

      The configuration for backup in Amazon S3.

      - **RoleARN** *(string) --*

        The Amazon Resource Name (ARN) of the AWS credentials. For more information, see
        `Amazon Resource Names (ARNs) and AWS Service Namespaces
        <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

      - **BucketARN** *(string) --*

        The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs)
        and AWS Service Namespaces
        <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

      - **Prefix** *(string) --*

        The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered Amazon
        S3 files. You can also specify a custom prefix, as described in `Custom Prefixes
        for Amazon S3 Objects
        <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

      - **ErrorOutputPrefix** *(string) --*

        A prefix that Kinesis Data Firehose evaluates and adds to failed records before
        writing them to S3. This prefix appears immediately following the bucket name. For
        information about how to specify this prefix, see `Custom Prefixes for Amazon S3
        Objects <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

      - **BufferingHints** *(dict) --*

        The buffering option. If no value is specified, ``BufferingHints`` object default
        values are used.

        - **SizeInMBs** *(integer) --*

          Buffer incoming data to the specified size, in MiBs, before delivering it to the
          destination. The default value is 5. This parameter is optional but if you
          specify a value for it, you must also specify a value for ``IntervalInSeconds`` ,
          and vice versa.

          We recommend setting this parameter to a value greater than the amount of data
          you typically ingest into the delivery stream in 10 seconds. For example, if you
          typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

        - **IntervalInSeconds** *(integer) --*

          Buffer incoming data for the specified period of time, in seconds, before
          delivering it to the destination. The default value is 300. This parameter is
          optional but if you specify a value for it, you must also specify a value for
          ``SizeInMBs`` , and vice versa.

      - **CompressionFormat** *(string) --*

        The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .

      - **EncryptionConfiguration** *(dict) --*

        The encryption configuration. If no value is specified, the default is no
        encryption.

        - **NoEncryptionConfig** *(string) --*

          Specifically override existing encryption information to ensure that no
          encryption is used.

        - **KMSEncryptionConfig** *(dict) --*

          The encryption key.

          - **AWSKMSKeyARN** *(string) --*

            The Amazon Resource Name (ARN) of the encryption key. Must belong to the same
            AWS Region as the destination Amazon S3 bucket. For more information, see
            `Amazon Resource Names (ARNs) and AWS Service Namespaces
            <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__
            .

      - **CloudWatchLoggingOptions** *(dict) --*

        The Amazon CloudWatch logging options for your delivery stream.

        - **Enabled** *(boolean) --*

          Enables or disables CloudWatch logging.

        - **LogGroupName** *(string) --*

          The CloudWatch group name for logging. This value is required if CloudWatch
          logging is enabled.

        - **LogStreamName** *(string) --*

          The CloudWatch log stream name for logging. This value is required if CloudWatch
          logging is enabled.

    - **CloudWatchLoggingOptions** *(dict) --*

      The Amazon CloudWatch logging options for your delivery stream.

      - **Enabled** *(boolean) --*

        Enables or disables CloudWatch logging.

      - **LogGroupName** *(string) --*

        The CloudWatch group name for logging. This value is required if CloudWatch logging
        is enabled.

      - **LogStreamName** *(string) --*

        The CloudWatch log stream name for logging. This value is required if CloudWatch
        logging is enabled.
    """


_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsS3DestinationDescriptionBufferingHintsTypeDef = TypedDict(
    "_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsS3DestinationDescriptionBufferingHintsTypeDef",
    {"SizeInMBs": int, "IntervalInSeconds": int},
    total=False,
)


class ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsS3DestinationDescriptionBufferingHintsTypeDef(
    _ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsS3DestinationDescriptionBufferingHintsTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsS3DestinationDescription` `BufferingHints`

    The buffering option. If no value is specified, ``BufferingHints`` object default
    values are used.

    - **SizeInMBs** *(integer) --*

      Buffer incoming data to the specified size, in MiBs, before delivering it to the
      destination. The default value is 5. This parameter is optional but if you specify
      a value for it, you must also specify a value for ``IntervalInSeconds`` , and vice
      versa.

      We recommend setting this parameter to a value greater than the amount of data you
      typically ingest into the delivery stream in 10 seconds. For example, if you
      typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

    - **IntervalInSeconds** *(integer) --*

      Buffer incoming data for the specified period of time, in seconds, before
      delivering it to the destination. The default value is 300. This parameter is
      optional but if you specify a value for it, you must also specify a value for
      ``SizeInMBs`` , and vice versa.
    """


_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsS3DestinationDescriptionCloudWatchLoggingOptionsTypeDef = TypedDict(
    "_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsS3DestinationDescriptionCloudWatchLoggingOptionsTypeDef",
    {"Enabled": bool, "LogGroupName": str, "LogStreamName": str},
    total=False,
)


class ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsS3DestinationDescriptionCloudWatchLoggingOptionsTypeDef(
    _ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsS3DestinationDescriptionCloudWatchLoggingOptionsTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsS3DestinationDescription` `CloudWatchLoggingOptions`

    The Amazon CloudWatch logging options for your delivery stream.

    - **Enabled** *(boolean) --*

      Enables or disables CloudWatch logging.

    - **LogGroupName** *(string) --*

      The CloudWatch group name for logging. This value is required if CloudWatch logging
      is enabled.

    - **LogStreamName** *(string) --*

      The CloudWatch log stream name for logging. This value is required if CloudWatch
      logging is enabled.
    """


_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsS3DestinationDescriptionEncryptionConfigurationKMSEncryptionConfigTypeDef = TypedDict(
    "_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsS3DestinationDescriptionEncryptionConfigurationKMSEncryptionConfigTypeDef",
    {"AWSKMSKeyARN": str},
    total=False,
)


class ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsS3DestinationDescriptionEncryptionConfigurationKMSEncryptionConfigTypeDef(
    _ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsS3DestinationDescriptionEncryptionConfigurationKMSEncryptionConfigTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsS3DestinationDescriptionEncryptionConfiguration` `KMSEncryptionConfig`

    The encryption key.

    - **AWSKMSKeyARN** *(string) --*

      The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS
      Region as the destination Amazon S3 bucket. For more information, see `Amazon
      Resource Names (ARNs) and AWS Service Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
    """


_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsS3DestinationDescriptionEncryptionConfigurationTypeDef = TypedDict(
    "_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsS3DestinationDescriptionEncryptionConfigurationTypeDef",
    {
        "NoEncryptionConfig": str,
        "KMSEncryptionConfig": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsS3DestinationDescriptionEncryptionConfigurationKMSEncryptionConfigTypeDef,
    },
    total=False,
)


class ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsS3DestinationDescriptionEncryptionConfigurationTypeDef(
    _ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsS3DestinationDescriptionEncryptionConfigurationTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsS3DestinationDescription` `EncryptionConfiguration`

    The encryption configuration. If no value is specified, the default is no encryption.

    - **NoEncryptionConfig** *(string) --*

      Specifically override existing encryption information to ensure that no encryption
      is used.

    - **KMSEncryptionConfig** *(dict) --*

      The encryption key.

      - **AWSKMSKeyARN** *(string) --*

        The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS
        Region as the destination Amazon S3 bucket. For more information, see `Amazon
        Resource Names (ARNs) and AWS Service Namespaces
        <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
    """


_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsS3DestinationDescriptionTypeDef = TypedDict(
    "_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsS3DestinationDescriptionTypeDef",
    {
        "RoleARN": str,
        "BucketARN": str,
        "Prefix": str,
        "ErrorOutputPrefix": str,
        "BufferingHints": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsS3DestinationDescriptionBufferingHintsTypeDef,
        "CompressionFormat": str,
        "EncryptionConfiguration": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsS3DestinationDescriptionEncryptionConfigurationTypeDef,
        "CloudWatchLoggingOptions": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsS3DestinationDescriptionCloudWatchLoggingOptionsTypeDef,
    },
    total=False,
)


class ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsS3DestinationDescriptionTypeDef(
    _ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsS3DestinationDescriptionTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinations` `S3DestinationDescription`

    [Deprecated] The destination in Amazon S3.

    - **RoleARN** *(string) --*

      The Amazon Resource Name (ARN) of the AWS credentials. For more information, see
      `Amazon Resource Names (ARNs) and AWS Service Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

    - **BucketARN** *(string) --*

      The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs) and
      AWS Service Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

    - **Prefix** *(string) --*

      The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered Amazon S3
      files. You can also specify a custom prefix, as described in `Custom Prefixes for
      Amazon S3 Objects
      <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

    - **ErrorOutputPrefix** *(string) --*

      A prefix that Kinesis Data Firehose evaluates and adds to failed records before
      writing them to S3. This prefix appears immediately following the bucket name. For
      information about how to specify this prefix, see `Custom Prefixes for Amazon S3
      Objects <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

    - **BufferingHints** *(dict) --*

      The buffering option. If no value is specified, ``BufferingHints`` object default
      values are used.

      - **SizeInMBs** *(integer) --*

        Buffer incoming data to the specified size, in MiBs, before delivering it to the
        destination. The default value is 5. This parameter is optional but if you specify
        a value for it, you must also specify a value for ``IntervalInSeconds`` , and vice
        versa.

        We recommend setting this parameter to a value greater than the amount of data you
        typically ingest into the delivery stream in 10 seconds. For example, if you
        typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

      - **IntervalInSeconds** *(integer) --*

        Buffer incoming data for the specified period of time, in seconds, before
        delivering it to the destination. The default value is 300. This parameter is
        optional but if you specify a value for it, you must also specify a value for
        ``SizeInMBs`` , and vice versa.

    - **CompressionFormat** *(string) --*

      The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .

    - **EncryptionConfiguration** *(dict) --*

      The encryption configuration. If no value is specified, the default is no encryption.

      - **NoEncryptionConfig** *(string) --*

        Specifically override existing encryption information to ensure that no encryption
        is used.

      - **KMSEncryptionConfig** *(dict) --*

        The encryption key.

        - **AWSKMSKeyARN** *(string) --*

          The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS
          Region as the destination Amazon S3 bucket. For more information, see `Amazon
          Resource Names (ARNs) and AWS Service Namespaces
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

    - **CloudWatchLoggingOptions** *(dict) --*

      The Amazon CloudWatch logging options for your delivery stream.

      - **Enabled** *(boolean) --*

        Enables or disables CloudWatch logging.

      - **LogGroupName** *(string) --*

        The CloudWatch group name for logging. This value is required if CloudWatch logging
        is enabled.

      - **LogStreamName** *(string) --*

        The CloudWatch log stream name for logging. This value is required if CloudWatch
        logging is enabled.
    """


_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionCloudWatchLoggingOptionsTypeDef = TypedDict(
    "_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionCloudWatchLoggingOptionsTypeDef",
    {"Enabled": bool, "LogGroupName": str, "LogStreamName": str},
    total=False,
)


class ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionCloudWatchLoggingOptionsTypeDef(
    _ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionCloudWatchLoggingOptionsTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescription` `CloudWatchLoggingOptions`

    The Amazon CloudWatch logging options for your delivery stream.

    - **Enabled** *(boolean) --*

      Enables or disables CloudWatch logging.

    - **LogGroupName** *(string) --*

      The CloudWatch group name for logging. This value is required if CloudWatch logging
      is enabled.

    - **LogStreamName** *(string) --*

      The CloudWatch log stream name for logging. This value is required if CloudWatch
      logging is enabled.
    """


_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionProcessingConfigurationProcessorsParametersTypeDef = TypedDict(
    "_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionProcessingConfigurationProcessorsParametersTypeDef",
    {"ParameterName": str, "ParameterValue": str},
    total=False,
)


class ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionProcessingConfigurationProcessorsParametersTypeDef(
    _ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionProcessingConfigurationProcessorsParametersTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionProcessingConfigurationProcessors` `Parameters`

    Describes the processor parameter.

    - **ParameterName** *(string) --*

      The name of the parameter.

    - **ParameterValue** *(string) --*

      The parameter value.
    """


_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionProcessingConfigurationProcessorsTypeDef = TypedDict(
    "_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionProcessingConfigurationProcessorsTypeDef",
    {
        "Type": str,
        "Parameters": List[
            ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionProcessingConfigurationProcessorsParametersTypeDef
        ],
    },
    total=False,
)


class ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionProcessingConfigurationProcessorsTypeDef(
    _ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionProcessingConfigurationProcessorsTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionProcessingConfiguration` `Processors`

    Describes a data processor.

    - **Type** *(string) --*

      The type of processor.

    - **Parameters** *(list) --*

      The processor parameters.

      - *(dict) --*

        Describes the processor parameter.

        - **ParameterName** *(string) --*

          The name of the parameter.

        - **ParameterValue** *(string) --*

          The parameter value.
    """


_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionProcessingConfigurationTypeDef = TypedDict(
    "_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionProcessingConfigurationTypeDef",
    {
        "Enabled": bool,
        "Processors": List[
            ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionProcessingConfigurationProcessorsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionProcessingConfigurationTypeDef(
    _ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionProcessingConfigurationTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescription` `ProcessingConfiguration`

    The data processing configuration.

    - **Enabled** *(boolean) --*

      Enables or disables data processing.

    - **Processors** *(list) --*

      The data processors.

      - *(dict) --*

        Describes a data processor.

        - **Type** *(string) --*

          The type of processor.

        - **Parameters** *(list) --*

          The processor parameters.

          - *(dict) --*

            Describes the processor parameter.

            - **ParameterName** *(string) --*

              The name of the parameter.

            - **ParameterValue** *(string) --*

              The parameter value.
    """


_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionRetryOptionsTypeDef = TypedDict(
    "_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionRetryOptionsTypeDef",
    {"DurationInSeconds": int},
    total=False,
)


class ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionRetryOptionsTypeDef(
    _ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionRetryOptionsTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescription` `RetryOptions`

    The retry behavior in case Kinesis Data Firehose is unable to deliver data to Splunk
    or if it doesn't receive an acknowledgment of receipt from Splunk.

    - **DurationInSeconds** *(integer) --*

      The total amount of time that Kinesis Data Firehose spends on retries. This
      duration starts after the initial attempt to send data to Splunk fails. It doesn't
      include the periods during which Kinesis Data Firehose waits for acknowledgment
      from Splunk after each attempt.
    """


_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionS3DestinationDescriptionBufferingHintsTypeDef = TypedDict(
    "_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionS3DestinationDescriptionBufferingHintsTypeDef",
    {"SizeInMBs": int, "IntervalInSeconds": int},
    total=False,
)


class ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionS3DestinationDescriptionBufferingHintsTypeDef(
    _ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionS3DestinationDescriptionBufferingHintsTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionS3DestinationDescription` `BufferingHints`

    The buffering option. If no value is specified, ``BufferingHints`` object default
    values are used.

    - **SizeInMBs** *(integer) --*

      Buffer incoming data to the specified size, in MiBs, before delivering it to the
      destination. The default value is 5. This parameter is optional but if you
      specify a value for it, you must also specify a value for ``IntervalInSeconds`` ,
      and vice versa.

      We recommend setting this parameter to a value greater than the amount of data
      you typically ingest into the delivery stream in 10 seconds. For example, if you
      typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

    - **IntervalInSeconds** *(integer) --*

      Buffer incoming data for the specified period of time, in seconds, before
      delivering it to the destination. The default value is 300. This parameter is
      optional but if you specify a value for it, you must also specify a value for
      ``SizeInMBs`` , and vice versa.
    """


_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionS3DestinationDescriptionCloudWatchLoggingOptionsTypeDef = TypedDict(
    "_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionS3DestinationDescriptionCloudWatchLoggingOptionsTypeDef",
    {"Enabled": bool, "LogGroupName": str, "LogStreamName": str},
    total=False,
)


class ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionS3DestinationDescriptionCloudWatchLoggingOptionsTypeDef(
    _ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionS3DestinationDescriptionCloudWatchLoggingOptionsTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionS3DestinationDescription` `CloudWatchLoggingOptions`

    The Amazon CloudWatch logging options for your delivery stream.

    - **Enabled** *(boolean) --*

      Enables or disables CloudWatch logging.

    - **LogGroupName** *(string) --*

      The CloudWatch group name for logging. This value is required if CloudWatch
      logging is enabled.

    - **LogStreamName** *(string) --*

      The CloudWatch log stream name for logging. This value is required if CloudWatch
      logging is enabled.
    """


_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionS3DestinationDescriptionEncryptionConfigurationKMSEncryptionConfigTypeDef = TypedDict(
    "_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionS3DestinationDescriptionEncryptionConfigurationKMSEncryptionConfigTypeDef",
    {"AWSKMSKeyARN": str},
    total=False,
)


class ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionS3DestinationDescriptionEncryptionConfigurationKMSEncryptionConfigTypeDef(
    _ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionS3DestinationDescriptionEncryptionConfigurationKMSEncryptionConfigTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionS3DestinationDescriptionEncryptionConfiguration` `KMSEncryptionConfig`

    The encryption key.

    - **AWSKMSKeyARN** *(string) --*

      The Amazon Resource Name (ARN) of the encryption key. Must belong to the same
      AWS Region as the destination Amazon S3 bucket. For more information, see
      `Amazon Resource Names (ARNs) and AWS Service Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__
      .
    """


_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionS3DestinationDescriptionEncryptionConfigurationTypeDef = TypedDict(
    "_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionS3DestinationDescriptionEncryptionConfigurationTypeDef",
    {
        "NoEncryptionConfig": str,
        "KMSEncryptionConfig": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionS3DestinationDescriptionEncryptionConfigurationKMSEncryptionConfigTypeDef,
    },
    total=False,
)


class ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionS3DestinationDescriptionEncryptionConfigurationTypeDef(
    _ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionS3DestinationDescriptionEncryptionConfigurationTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionS3DestinationDescription` `EncryptionConfiguration`

    The encryption configuration. If no value is specified, the default is no
    encryption.

    - **NoEncryptionConfig** *(string) --*

      Specifically override existing encryption information to ensure that no
      encryption is used.

    - **KMSEncryptionConfig** *(dict) --*

      The encryption key.

      - **AWSKMSKeyARN** *(string) --*

        The Amazon Resource Name (ARN) of the encryption key. Must belong to the same
        AWS Region as the destination Amazon S3 bucket. For more information, see
        `Amazon Resource Names (ARNs) and AWS Service Namespaces
        <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__
        .
    """


_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionS3DestinationDescriptionTypeDef = TypedDict(
    "_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionS3DestinationDescriptionTypeDef",
    {
        "RoleARN": str,
        "BucketARN": str,
        "Prefix": str,
        "ErrorOutputPrefix": str,
        "BufferingHints": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionS3DestinationDescriptionBufferingHintsTypeDef,
        "CompressionFormat": str,
        "EncryptionConfiguration": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionS3DestinationDescriptionEncryptionConfigurationTypeDef,
        "CloudWatchLoggingOptions": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionS3DestinationDescriptionCloudWatchLoggingOptionsTypeDef,
    },
    total=False,
)


class ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionS3DestinationDescriptionTypeDef(
    _ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionS3DestinationDescriptionTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescription` `S3DestinationDescription`

    The Amazon S3 destination.>

    - **RoleARN** *(string) --*

      The Amazon Resource Name (ARN) of the AWS credentials. For more information, see
      `Amazon Resource Names (ARNs) and AWS Service Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

    - **BucketARN** *(string) --*

      The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs)
      and AWS Service Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

    - **Prefix** *(string) --*

      The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered Amazon
      S3 files. You can also specify a custom prefix, as described in `Custom Prefixes
      for Amazon S3 Objects
      <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

    - **ErrorOutputPrefix** *(string) --*

      A prefix that Kinesis Data Firehose evaluates and adds to failed records before
      writing them to S3. This prefix appears immediately following the bucket name. For
      information about how to specify this prefix, see `Custom Prefixes for Amazon S3
      Objects <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

    - **BufferingHints** *(dict) --*

      The buffering option. If no value is specified, ``BufferingHints`` object default
      values are used.

      - **SizeInMBs** *(integer) --*

        Buffer incoming data to the specified size, in MiBs, before delivering it to the
        destination. The default value is 5. This parameter is optional but if you
        specify a value for it, you must also specify a value for ``IntervalInSeconds`` ,
        and vice versa.

        We recommend setting this parameter to a value greater than the amount of data
        you typically ingest into the delivery stream in 10 seconds. For example, if you
        typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

      - **IntervalInSeconds** *(integer) --*

        Buffer incoming data for the specified period of time, in seconds, before
        delivering it to the destination. The default value is 300. This parameter is
        optional but if you specify a value for it, you must also specify a value for
        ``SizeInMBs`` , and vice versa.

    - **CompressionFormat** *(string) --*

      The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .

    - **EncryptionConfiguration** *(dict) --*

      The encryption configuration. If no value is specified, the default is no
      encryption.

      - **NoEncryptionConfig** *(string) --*

        Specifically override existing encryption information to ensure that no
        encryption is used.

      - **KMSEncryptionConfig** *(dict) --*

        The encryption key.

        - **AWSKMSKeyARN** *(string) --*

          The Amazon Resource Name (ARN) of the encryption key. Must belong to the same
          AWS Region as the destination Amazon S3 bucket. For more information, see
          `Amazon Resource Names (ARNs) and AWS Service Namespaces
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__
          .

    - **CloudWatchLoggingOptions** *(dict) --*

      The Amazon CloudWatch logging options for your delivery stream.

      - **Enabled** *(boolean) --*

        Enables or disables CloudWatch logging.

      - **LogGroupName** *(string) --*

        The CloudWatch group name for logging. This value is required if CloudWatch
        logging is enabled.

      - **LogStreamName** *(string) --*

        The CloudWatch log stream name for logging. This value is required if CloudWatch
        logging is enabled.
    """


_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionTypeDef = TypedDict(
    "_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionTypeDef",
    {
        "HECEndpoint": str,
        "HECEndpointType": str,
        "HECToken": str,
        "HECAcknowledgmentTimeoutInSeconds": int,
        "RetryOptions": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionRetryOptionsTypeDef,
        "S3BackupMode": str,
        "S3DestinationDescription": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionS3DestinationDescriptionTypeDef,
        "ProcessingConfiguration": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionProcessingConfigurationTypeDef,
        "CloudWatchLoggingOptions": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionCloudWatchLoggingOptionsTypeDef,
    },
    total=False,
)


class ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionTypeDef(
    _ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinations` `SplunkDestinationDescription`

    The destination in Splunk.

    - **HECEndpoint** *(string) --*

      The HTTP Event Collector (HEC) endpoint to which Kinesis Data Firehose sends your
      data.

    - **HECEndpointType** *(string) --*

      This type can be either "Raw" or "Event."

    - **HECToken** *(string) --*

      A GUID you obtain from your Splunk cluster when you create a new HEC endpoint.

    - **HECAcknowledgmentTimeoutInSeconds** *(integer) --*

      The amount of time that Kinesis Data Firehose waits to receive an acknowledgment from
      Splunk after it sends it data. At the end of the timeout period, Kinesis Data
      Firehose either tries to send the data again or considers it an error, based on your
      retry settings.

    - **RetryOptions** *(dict) --*

      The retry behavior in case Kinesis Data Firehose is unable to deliver data to Splunk
      or if it doesn't receive an acknowledgment of receipt from Splunk.

      - **DurationInSeconds** *(integer) --*

        The total amount of time that Kinesis Data Firehose spends on retries. This
        duration starts after the initial attempt to send data to Splunk fails. It doesn't
        include the periods during which Kinesis Data Firehose waits for acknowledgment
        from Splunk after each attempt.

    - **S3BackupMode** *(string) --*

      Defines how documents should be delivered to Amazon S3. When set to
      ``FailedDocumentsOnly`` , Kinesis Data Firehose writes any data that could not be
      indexed to the configured Amazon S3 destination. When set to ``AllDocuments`` ,
      Kinesis Data Firehose delivers all incoming records to Amazon S3, and also writes
      failed documents to Amazon S3. Default value is ``FailedDocumentsOnly`` .

    - **S3DestinationDescription** *(dict) --*

      The Amazon S3 destination.>

      - **RoleARN** *(string) --*

        The Amazon Resource Name (ARN) of the AWS credentials. For more information, see
        `Amazon Resource Names (ARNs) and AWS Service Namespaces
        <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

      - **BucketARN** *(string) --*

        The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs)
        and AWS Service Namespaces
        <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

      - **Prefix** *(string) --*

        The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered Amazon
        S3 files. You can also specify a custom prefix, as described in `Custom Prefixes
        for Amazon S3 Objects
        <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

      - **ErrorOutputPrefix** *(string) --*

        A prefix that Kinesis Data Firehose evaluates and adds to failed records before
        writing them to S3. This prefix appears immediately following the bucket name. For
        information about how to specify this prefix, see `Custom Prefixes for Amazon S3
        Objects <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

      - **BufferingHints** *(dict) --*

        The buffering option. If no value is specified, ``BufferingHints`` object default
        values are used.

        - **SizeInMBs** *(integer) --*

          Buffer incoming data to the specified size, in MiBs, before delivering it to the
          destination. The default value is 5. This parameter is optional but if you
          specify a value for it, you must also specify a value for ``IntervalInSeconds`` ,
          and vice versa.

          We recommend setting this parameter to a value greater than the amount of data
          you typically ingest into the delivery stream in 10 seconds. For example, if you
          typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

        - **IntervalInSeconds** *(integer) --*

          Buffer incoming data for the specified period of time, in seconds, before
          delivering it to the destination. The default value is 300. This parameter is
          optional but if you specify a value for it, you must also specify a value for
          ``SizeInMBs`` , and vice versa.

      - **CompressionFormat** *(string) --*

        The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .

      - **EncryptionConfiguration** *(dict) --*

        The encryption configuration. If no value is specified, the default is no
        encryption.

        - **NoEncryptionConfig** *(string) --*

          Specifically override existing encryption information to ensure that no
          encryption is used.

        - **KMSEncryptionConfig** *(dict) --*

          The encryption key.

          - **AWSKMSKeyARN** *(string) --*

            The Amazon Resource Name (ARN) of the encryption key. Must belong to the same
            AWS Region as the destination Amazon S3 bucket. For more information, see
            `Amazon Resource Names (ARNs) and AWS Service Namespaces
            <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__
            .

      - **CloudWatchLoggingOptions** *(dict) --*

        The Amazon CloudWatch logging options for your delivery stream.

        - **Enabled** *(boolean) --*

          Enables or disables CloudWatch logging.

        - **LogGroupName** *(string) --*

          The CloudWatch group name for logging. This value is required if CloudWatch
          logging is enabled.

        - **LogStreamName** *(string) --*

          The CloudWatch log stream name for logging. This value is required if CloudWatch
          logging is enabled.

    - **ProcessingConfiguration** *(dict) --*

      The data processing configuration.

      - **Enabled** *(boolean) --*

        Enables or disables data processing.

      - **Processors** *(list) --*

        The data processors.

        - *(dict) --*

          Describes a data processor.

          - **Type** *(string) --*

            The type of processor.

          - **Parameters** *(list) --*

            The processor parameters.

            - *(dict) --*

              Describes the processor parameter.

              - **ParameterName** *(string) --*

                The name of the parameter.

              - **ParameterValue** *(string) --*

                The parameter value.

    - **CloudWatchLoggingOptions** *(dict) --*

      The Amazon CloudWatch logging options for your delivery stream.

      - **Enabled** *(boolean) --*

        Enables or disables CloudWatch logging.

      - **LogGroupName** *(string) --*

        The CloudWatch group name for logging. This value is required if CloudWatch logging
        is enabled.

      - **LogStreamName** *(string) --*

        The CloudWatch log stream name for logging. This value is required if CloudWatch
        logging is enabled.
    """


_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsTypeDef = TypedDict(
    "_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsTypeDef",
    {
        "DestinationId": str,
        "S3DestinationDescription": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsS3DestinationDescriptionTypeDef,
        "ExtendedS3DestinationDescription": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionTypeDef,
        "RedshiftDestinationDescription": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionTypeDef,
        "ElasticsearchDestinationDescription": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionTypeDef,
        "SplunkDestinationDescription": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionTypeDef,
    },
    total=False,
)


class ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsTypeDef(
    _ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryStreamResponseDeliveryStreamDescription` `Destinations`

    Describes the destination for a delivery stream.

    - **DestinationId** *(string) --*

      The ID of the destination.

    - **S3DestinationDescription** *(dict) --*

      [Deprecated] The destination in Amazon S3.

      - **RoleARN** *(string) --*

        The Amazon Resource Name (ARN) of the AWS credentials. For more information, see
        `Amazon Resource Names (ARNs) and AWS Service Namespaces
        <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

      - **BucketARN** *(string) --*

        The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs) and
        AWS Service Namespaces
        <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

      - **Prefix** *(string) --*

        The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered Amazon S3
        files. You can also specify a custom prefix, as described in `Custom Prefixes for
        Amazon S3 Objects
        <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

      - **ErrorOutputPrefix** *(string) --*

        A prefix that Kinesis Data Firehose evaluates and adds to failed records before
        writing them to S3. This prefix appears immediately following the bucket name. For
        information about how to specify this prefix, see `Custom Prefixes for Amazon S3
        Objects <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

      - **BufferingHints** *(dict) --*

        The buffering option. If no value is specified, ``BufferingHints`` object default
        values are used.

        - **SizeInMBs** *(integer) --*

          Buffer incoming data to the specified size, in MiBs, before delivering it to the
          destination. The default value is 5. This parameter is optional but if you specify
          a value for it, you must also specify a value for ``IntervalInSeconds`` , and vice
          versa.

          We recommend setting this parameter to a value greater than the amount of data you
          typically ingest into the delivery stream in 10 seconds. For example, if you
          typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

        - **IntervalInSeconds** *(integer) --*

          Buffer incoming data for the specified period of time, in seconds, before
          delivering it to the destination. The default value is 300. This parameter is
          optional but if you specify a value for it, you must also specify a value for
          ``SizeInMBs`` , and vice versa.

      - **CompressionFormat** *(string) --*

        The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .

      - **EncryptionConfiguration** *(dict) --*

        The encryption configuration. If no value is specified, the default is no encryption.

        - **NoEncryptionConfig** *(string) --*

          Specifically override existing encryption information to ensure that no encryption
          is used.

        - **KMSEncryptionConfig** *(dict) --*

          The encryption key.

          - **AWSKMSKeyARN** *(string) --*

            The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS
            Region as the destination Amazon S3 bucket. For more information, see `Amazon
            Resource Names (ARNs) and AWS Service Namespaces
            <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

      - **CloudWatchLoggingOptions** *(dict) --*

        The Amazon CloudWatch logging options for your delivery stream.

        - **Enabled** *(boolean) --*

          Enables or disables CloudWatch logging.

        - **LogGroupName** *(string) --*

          The CloudWatch group name for logging. This value is required if CloudWatch logging
          is enabled.

        - **LogStreamName** *(string) --*

          The CloudWatch log stream name for logging. This value is required if CloudWatch
          logging is enabled.

    - **ExtendedS3DestinationDescription** *(dict) --*

      The destination in Amazon S3.

      - **RoleARN** *(string) --*

        The Amazon Resource Name (ARN) of the AWS credentials. For more information, see
        `Amazon Resource Names (ARNs) and AWS Service Namespaces
        <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

      - **BucketARN** *(string) --*

        The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs) and
        AWS Service Namespaces
        <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

      - **Prefix** *(string) --*

        The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered Amazon S3
        files. You can also specify a custom prefix, as described in `Custom Prefixes for
        Amazon S3 Objects
        <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

      - **ErrorOutputPrefix** *(string) --*

        A prefix that Kinesis Data Firehose evaluates and adds to failed records before
        writing them to S3. This prefix appears immediately following the bucket name. For
        information about how to specify this prefix, see `Custom Prefixes for Amazon S3
        Objects <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

      - **BufferingHints** *(dict) --*

        The buffering option.

        - **SizeInMBs** *(integer) --*

          Buffer incoming data to the specified size, in MiBs, before delivering it to the
          destination. The default value is 5. This parameter is optional but if you specify
          a value for it, you must also specify a value for ``IntervalInSeconds`` , and vice
          versa.

          We recommend setting this parameter to a value greater than the amount of data you
          typically ingest into the delivery stream in 10 seconds. For example, if you
          typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

        - **IntervalInSeconds** *(integer) --*

          Buffer incoming data for the specified period of time, in seconds, before
          delivering it to the destination. The default value is 300. This parameter is
          optional but if you specify a value for it, you must also specify a value for
          ``SizeInMBs`` , and vice versa.

      - **CompressionFormat** *(string) --*

        The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .

      - **EncryptionConfiguration** *(dict) --*

        The encryption configuration. If no value is specified, the default is no encryption.

        - **NoEncryptionConfig** *(string) --*

          Specifically override existing encryption information to ensure that no encryption
          is used.

        - **KMSEncryptionConfig** *(dict) --*

          The encryption key.

          - **AWSKMSKeyARN** *(string) --*

            The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS
            Region as the destination Amazon S3 bucket. For more information, see `Amazon
            Resource Names (ARNs) and AWS Service Namespaces
            <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

      - **CloudWatchLoggingOptions** *(dict) --*

        The Amazon CloudWatch logging options for your delivery stream.

        - **Enabled** *(boolean) --*

          Enables or disables CloudWatch logging.

        - **LogGroupName** *(string) --*

          The CloudWatch group name for logging. This value is required if CloudWatch logging
          is enabled.

        - **LogStreamName** *(string) --*

          The CloudWatch log stream name for logging. This value is required if CloudWatch
          logging is enabled.

      - **ProcessingConfiguration** *(dict) --*

        The data processing configuration.

        - **Enabled** *(boolean) --*

          Enables or disables data processing.

        - **Processors** *(list) --*

          The data processors.

          - *(dict) --*

            Describes a data processor.

            - **Type** *(string) --*

              The type of processor.

            - **Parameters** *(list) --*

              The processor parameters.

              - *(dict) --*

                Describes the processor parameter.

                - **ParameterName** *(string) --*

                  The name of the parameter.

                - **ParameterValue** *(string) --*

                  The parameter value.

      - **S3BackupMode** *(string) --*

        The Amazon S3 backup mode.

      - **S3BackupDescription** *(dict) --*

        The configuration for backup in Amazon S3.

        - **RoleARN** *(string) --*

          The Amazon Resource Name (ARN) of the AWS credentials. For more information, see
          `Amazon Resource Names (ARNs) and AWS Service Namespaces
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

        - **BucketARN** *(string) --*

          The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs)
          and AWS Service Namespaces
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

        - **Prefix** *(string) --*

          The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered Amazon
          S3 files. You can also specify a custom prefix, as described in `Custom Prefixes
          for Amazon S3 Objects
          <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

        - **ErrorOutputPrefix** *(string) --*

          A prefix that Kinesis Data Firehose evaluates and adds to failed records before
          writing them to S3. This prefix appears immediately following the bucket name. For
          information about how to specify this prefix, see `Custom Prefixes for Amazon S3
          Objects <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

        - **BufferingHints** *(dict) --*

          The buffering option. If no value is specified, ``BufferingHints`` object default
          values are used.

          - **SizeInMBs** *(integer) --*

            Buffer incoming data to the specified size, in MiBs, before delivering it to the
            destination. The default value is 5. This parameter is optional but if you
            specify a value for it, you must also specify a value for ``IntervalInSeconds`` ,
            and vice versa.

            We recommend setting this parameter to a value greater than the amount of data
            you typically ingest into the delivery stream in 10 seconds. For example, if you
            typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

          - **IntervalInSeconds** *(integer) --*

            Buffer incoming data for the specified period of time, in seconds, before
            delivering it to the destination. The default value is 300. This parameter is
            optional but if you specify a value for it, you must also specify a value for
            ``SizeInMBs`` , and vice versa.

        - **CompressionFormat** *(string) --*

          The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .

        - **EncryptionConfiguration** *(dict) --*

          The encryption configuration. If no value is specified, the default is no
          encryption.

          - **NoEncryptionConfig** *(string) --*

            Specifically override existing encryption information to ensure that no
            encryption is used.

          - **KMSEncryptionConfig** *(dict) --*

            The encryption key.

            - **AWSKMSKeyARN** *(string) --*

              The Amazon Resource Name (ARN) of the encryption key. Must belong to the same
              AWS Region as the destination Amazon S3 bucket. For more information, see
              `Amazon Resource Names (ARNs) and AWS Service Namespaces
              <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__
              .

        - **CloudWatchLoggingOptions** *(dict) --*

          The Amazon CloudWatch logging options for your delivery stream.

          - **Enabled** *(boolean) --*

            Enables or disables CloudWatch logging.

          - **LogGroupName** *(string) --*

            The CloudWatch group name for logging. This value is required if CloudWatch
            logging is enabled.

          - **LogStreamName** *(string) --*

            The CloudWatch log stream name for logging. This value is required if CloudWatch
            logging is enabled.

      - **DataFormatConversionConfiguration** *(dict) --*

        The serializer, deserializer, and schema for converting data from the JSON format to
        the Parquet or ORC format before writing it to Amazon S3.

        - **SchemaConfiguration** *(dict) --*

          Specifies the AWS Glue Data Catalog table that contains the column information.

          - **RoleARN** *(string) --*

            The role that Kinesis Data Firehose can use to access AWS Glue. This role must be
            in the same account you use for Kinesis Data Firehose. Cross-account roles aren't
            allowed.

          - **CatalogId** *(string) --*

            The ID of the AWS Glue Data Catalog. If you don't supply this, the AWS account ID
            is used by default.

          - **DatabaseName** *(string) --*

            Specifies the name of the AWS Glue database that contains the schema for the
            output data.

          - **TableName** *(string) --*

            Specifies the AWS Glue table that contains the column information that
            constitutes your data schema.

          - **Region** *(string) --*

            If you don't specify an AWS Region, the default is the current Region.

          - **VersionId** *(string) --*

            Specifies the table version for the output data schema. If you don't specify this
            version ID, or if you set it to ``LATEST`` , Kinesis Data Firehose uses the most
            recent version. This means that any updates to the table are automatically picked
            up.

        - **InputFormatConfiguration** *(dict) --*

          Specifies the deserializer that you want Kinesis Data Firehose to use to convert
          the format of your data from JSON.

          - **Deserializer** *(dict) --*

            Specifies which deserializer to use. You can choose either the Apache Hive JSON
            SerDe or the OpenX JSON SerDe. If both are non-null, the server rejects the
            request.

            - **OpenXJsonSerDe** *(dict) --*

              The OpenX SerDe. Used by Kinesis Data Firehose for deserializing data, which
              means converting it from the JSON format in preparation for serializing it to
              the Parquet or ORC format. This is one of two deserializers you can choose,
              depending on which one offers the functionality you need. The other option is
              the native Hive / HCatalog JsonSerDe.

              - **ConvertDotsInJsonKeysToUnderscores** *(boolean) --*

                When set to ``true`` , specifies that the names of the keys include dots and
                that you want Kinesis Data Firehose to replace them with underscores. This is
                useful because Apache Hive does not allow dots in column names. For example,
                if the JSON contains a key whose name is "a.b", you can define the column
                name to be "a_b" when using this option.

                The default is ``false`` .

              - **CaseInsensitive** *(boolean) --*

                When set to ``true`` , which is the default, Kinesis Data Firehose converts
                JSON keys to lowercase before deserializing them.

              - **ColumnToJsonKeyMappings** *(dict) --*

                Maps column names to JSON keys that aren't identical to the column names.
                This is useful when the JSON contains keys that are Hive keywords. For
                example, ``timestamp`` is a Hive keyword. If you have a JSON key named
                ``timestamp`` , set this parameter to ``{"ts": "timestamp"}`` to map this key
                to a column named ``ts`` .

                - *(string) --*

                  - *(string) --*

            - **HiveJsonSerDe** *(dict) --*

              The native Hive / HCatalog JsonSerDe. Used by Kinesis Data Firehose for
              deserializing data, which means converting it from the JSON format in
              preparation for serializing it to the Parquet or ORC format. This is one of two
              deserializers you can choose, depending on which one offers the functionality
              you need. The other option is the OpenX SerDe.

              - **TimestampFormats** *(list) --*

                Indicates how you want Kinesis Data Firehose to parse the date and timestamps
                that may be present in your input data JSON. To specify these format strings,
                follow the pattern syntax of JodaTime's DateTimeFormat format strings. For
                more information, see `Class DateTimeFormat
                <https://www.joda.org/joda-time/apidocs/org/joda/time/format/DateTimeFormat.html>`__
                . You can also use the special value ``millis`` to parse timestamps in epoch
                milliseconds. If you don't specify a format, Kinesis Data Firehose uses
                ``java.sql.Timestamp::valueOf`` by default.

                - *(string) --*

        - **OutputFormatConfiguration** *(dict) --*

          Specifies the serializer that you want Kinesis Data Firehose to use to convert the
          format of your data to the Parquet or ORC format.

          - **Serializer** *(dict) --*

            Specifies which serializer to use. You can choose either the ORC SerDe or the
            Parquet SerDe. If both are non-null, the server rejects the request.

            - **ParquetSerDe** *(dict) --*

              A serializer to use for converting data to the Parquet format before storing it
              in Amazon S3. For more information, see `Apache Parquet
              <https://parquet.apache.org/documentation/latest/>`__ .

              - **BlockSizeBytes** *(integer) --*

                The Hadoop Distributed File System (HDFS) block size. This is useful if you
                intend to copy the data from Amazon S3 to HDFS before querying. The default
                is 256 MiB and the minimum is 64 MiB. Kinesis Data Firehose uses this value
                for padding calculations.

              - **PageSizeBytes** *(integer) --*

                The Parquet page size. Column chunks are divided into pages. A page is
                conceptually an indivisible unit (in terms of compression and encoding). The
                minimum value is 64 KiB and the default is 1 MiB.

              - **Compression** *(string) --*

                The compression code to use over data blocks. The possible values are
                ``UNCOMPRESSED`` , ``SNAPPY`` , and ``GZIP`` , with the default being
                ``SNAPPY`` . Use ``SNAPPY`` for higher decompression speed. Use ``GZIP`` if
                the compression ration is more important than speed.

              - **EnableDictionaryCompression** *(boolean) --*

                Indicates whether to enable dictionary compression.

              - **MaxPaddingBytes** *(integer) --*

                The maximum amount of padding to apply. This is useful if you intend to copy
                the data from Amazon S3 to HDFS before querying. The default is 0.

              - **WriterVersion** *(string) --*

                Indicates the version of row format to output. The possible values are ``V1``
                and ``V2`` . The default is ``V1`` .

            - **OrcSerDe** *(dict) --*

              A serializer to use for converting data to the ORC format before storing it in
              Amazon S3. For more information, see `Apache ORC
              <https://orc.apache.org/docs/>`__ .

              - **StripeSizeBytes** *(integer) --*

                The number of bytes in each stripe. The default is 64 MiB and the minimum is
                8 MiB.

              - **BlockSizeBytes** *(integer) --*

                The Hadoop Distributed File System (HDFS) block size. This is useful if you
                intend to copy the data from Amazon S3 to HDFS before querying. The default
                is 256 MiB and the minimum is 64 MiB. Kinesis Data Firehose uses this value
                for padding calculations.

              - **RowIndexStride** *(integer) --*

                The number of rows between index entries. The default is 10,000 and the
                minimum is 1,000.

              - **EnablePadding** *(boolean) --*

                Set this to ``true`` to indicate that you want stripes to be padded to the
                HDFS block boundaries. This is useful if you intend to copy the data from
                Amazon S3 to HDFS before querying. The default is ``false`` .

              - **PaddingTolerance** *(float) --*

                A number between 0 and 1 that defines the tolerance for block padding as a
                decimal fraction of stripe size. The default value is 0.05, which means 5
                percent of stripe size.

                For the default values of 64 MiB ORC stripes and 256 MiB HDFS blocks, the
                default block padding tolerance of 5 percent reserves a maximum of 3.2 MiB
                for padding within the 256 MiB block. In such a case, if the available size
                within the block is more than 3.2 MiB, a new, smaller stripe is inserted to
                fit within that space. This ensures that no stripe crosses block boundaries
                and causes remote reads within a node-local task.

                Kinesis Data Firehose ignores this parameter when  OrcSerDe$EnablePadding is
                ``false`` .

              - **Compression** *(string) --*

                The compression code to use over data blocks. The default is ``SNAPPY`` .

              - **BloomFilterColumns** *(list) --*

                The column names for which you want Kinesis Data Firehose to create bloom
                filters. The default is ``null`` .

                - *(string) --*

              - **BloomFilterFalsePositiveProbability** *(float) --*

                The Bloom filter false positive probability (FPP). The lower the FPP, the
                bigger the Bloom filter. The default value is 0.05, the minimum is 0, and the
                maximum is 1.

              - **DictionaryKeyThreshold** *(float) --*

                Represents the fraction of the total number of non-null rows. To turn off
                dictionary encoding, set this fraction to a number that is less than the
                number of distinct keys in a dictionary. To always use dictionary encoding,
                set this threshold to 1.

              - **FormatVersion** *(string) --*

                The version of the file to write. The possible values are ``V0_11`` and
                ``V0_12`` . The default is ``V0_12`` .

        - **Enabled** *(boolean) --*

          Defaults to ``true`` . Set it to ``false`` if you want to disable format conversion
          while preserving the configuration details.

    - **RedshiftDestinationDescription** *(dict) --*

      The destination in Amazon Redshift.

      - **RoleARN** *(string) --*

        The Amazon Resource Name (ARN) of the AWS credentials. For more information, see
        `Amazon Resource Names (ARNs) and AWS Service Namespaces
        <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

      - **ClusterJDBCURL** *(string) --*

        The database connection string.

      - **CopyCommand** *(dict) --*

        The ``COPY`` command.

        - **DataTableName** *(string) --*

          The name of the target table. The table must already exist in the database.

        - **DataTableColumns** *(string) --*

          A comma-separated list of column names.

        - **CopyOptions** *(string) --*

          Optional parameters to use with the Amazon Redshift ``COPY`` command. For more
          information, see the "Optional Parameters" section of `Amazon Redshift COPY command
          <https://docs.aws.amazon.com/redshift/latest/dg/r_COPY.html>`__ . Some possible
          examples that would apply to Kinesis Data Firehose are as follows:

           ``delimiter '\\t' lzop;`` - fields are delimited with "\\t" (TAB character) and
           compressed using lzop.

           ``delimiter '|'`` - fields are delimited with "|" (this is the default delimiter).

           ``delimiter '|' escape`` - the delimiter should be escaped.

           ``fixedwidth 'venueid:3,venuename:25,venuecity:12,venuestate:2,venueseats:6'`` -
           fields are fixed width in the source, with each width specified after every column
           in the table.

           ``JSON 's3://mybucket/jsonpaths.txt'`` - data is in JSON format, and the path
           specified is the format of the data.

          For more examples, see `Amazon Redshift COPY command examples
          <https://docs.aws.amazon.com/redshift/latest/dg/r_COPY_command_examples.html>`__ .

      - **Username** *(string) --*

        The name of the user.

      - **RetryOptions** *(dict) --*

        The retry behavior in case Kinesis Data Firehose is unable to deliver documents to
        Amazon Redshift. Default value is 3600 (60 minutes).

        - **DurationInSeconds** *(integer) --*

          The length of time during which Kinesis Data Firehose retries delivery after a
          failure, starting from the initial request and including the first attempt. The
          default value is 3600 seconds (60 minutes). Kinesis Data Firehose does not retry if
          the value of ``DurationInSeconds`` is 0 (zero) or if the first delivery attempt
          takes longer than the current value.

      - **S3DestinationDescription** *(dict) --*

        The Amazon S3 destination.

        - **RoleARN** *(string) --*

          The Amazon Resource Name (ARN) of the AWS credentials. For more information, see
          `Amazon Resource Names (ARNs) and AWS Service Namespaces
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

        - **BucketARN** *(string) --*

          The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs)
          and AWS Service Namespaces
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

        - **Prefix** *(string) --*

          The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered Amazon
          S3 files. You can also specify a custom prefix, as described in `Custom Prefixes
          for Amazon S3 Objects
          <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

        - **ErrorOutputPrefix** *(string) --*

          A prefix that Kinesis Data Firehose evaluates and adds to failed records before
          writing them to S3. This prefix appears immediately following the bucket name. For
          information about how to specify this prefix, see `Custom Prefixes for Amazon S3
          Objects <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

        - **BufferingHints** *(dict) --*

          The buffering option. If no value is specified, ``BufferingHints`` object default
          values are used.

          - **SizeInMBs** *(integer) --*

            Buffer incoming data to the specified size, in MiBs, before delivering it to the
            destination. The default value is 5. This parameter is optional but if you
            specify a value for it, you must also specify a value for ``IntervalInSeconds`` ,
            and vice versa.

            We recommend setting this parameter to a value greater than the amount of data
            you typically ingest into the delivery stream in 10 seconds. For example, if you
            typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

          - **IntervalInSeconds** *(integer) --*

            Buffer incoming data for the specified period of time, in seconds, before
            delivering it to the destination. The default value is 300. This parameter is
            optional but if you specify a value for it, you must also specify a value for
            ``SizeInMBs`` , and vice versa.

        - **CompressionFormat** *(string) --*

          The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .

        - **EncryptionConfiguration** *(dict) --*

          The encryption configuration. If no value is specified, the default is no
          encryption.

          - **NoEncryptionConfig** *(string) --*

            Specifically override existing encryption information to ensure that no
            encryption is used.

          - **KMSEncryptionConfig** *(dict) --*

            The encryption key.

            - **AWSKMSKeyARN** *(string) --*

              The Amazon Resource Name (ARN) of the encryption key. Must belong to the same
              AWS Region as the destination Amazon S3 bucket. For more information, see
              `Amazon Resource Names (ARNs) and AWS Service Namespaces
              <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__
              .

        - **CloudWatchLoggingOptions** *(dict) --*

          The Amazon CloudWatch logging options for your delivery stream.

          - **Enabled** *(boolean) --*

            Enables or disables CloudWatch logging.

          - **LogGroupName** *(string) --*

            The CloudWatch group name for logging. This value is required if CloudWatch
            logging is enabled.

          - **LogStreamName** *(string) --*

            The CloudWatch log stream name for logging. This value is required if CloudWatch
            logging is enabled.

      - **ProcessingConfiguration** *(dict) --*

        The data processing configuration.

        - **Enabled** *(boolean) --*

          Enables or disables data processing.

        - **Processors** *(list) --*

          The data processors.

          - *(dict) --*

            Describes a data processor.

            - **Type** *(string) --*

              The type of processor.

            - **Parameters** *(list) --*

              The processor parameters.

              - *(dict) --*

                Describes the processor parameter.

                - **ParameterName** *(string) --*

                  The name of the parameter.

                - **ParameterValue** *(string) --*

                  The parameter value.

      - **S3BackupMode** *(string) --*

        The Amazon S3 backup mode.

      - **S3BackupDescription** *(dict) --*

        The configuration for backup in Amazon S3.

        - **RoleARN** *(string) --*

          The Amazon Resource Name (ARN) of the AWS credentials. For more information, see
          `Amazon Resource Names (ARNs) and AWS Service Namespaces
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

        - **BucketARN** *(string) --*

          The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs)
          and AWS Service Namespaces
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

        - **Prefix** *(string) --*

          The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered Amazon
          S3 files. You can also specify a custom prefix, as described in `Custom Prefixes
          for Amazon S3 Objects
          <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

        - **ErrorOutputPrefix** *(string) --*

          A prefix that Kinesis Data Firehose evaluates and adds to failed records before
          writing them to S3. This prefix appears immediately following the bucket name. For
          information about how to specify this prefix, see `Custom Prefixes for Amazon S3
          Objects <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

        - **BufferingHints** *(dict) --*

          The buffering option. If no value is specified, ``BufferingHints`` object default
          values are used.

          - **SizeInMBs** *(integer) --*

            Buffer incoming data to the specified size, in MiBs, before delivering it to the
            destination. The default value is 5. This parameter is optional but if you
            specify a value for it, you must also specify a value for ``IntervalInSeconds`` ,
            and vice versa.

            We recommend setting this parameter to a value greater than the amount of data
            you typically ingest into the delivery stream in 10 seconds. For example, if you
            typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

          - **IntervalInSeconds** *(integer) --*

            Buffer incoming data for the specified period of time, in seconds, before
            delivering it to the destination. The default value is 300. This parameter is
            optional but if you specify a value for it, you must also specify a value for
            ``SizeInMBs`` , and vice versa.

        - **CompressionFormat** *(string) --*

          The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .

        - **EncryptionConfiguration** *(dict) --*

          The encryption configuration. If no value is specified, the default is no
          encryption.

          - **NoEncryptionConfig** *(string) --*

            Specifically override existing encryption information to ensure that no
            encryption is used.

          - **KMSEncryptionConfig** *(dict) --*

            The encryption key.

            - **AWSKMSKeyARN** *(string) --*

              The Amazon Resource Name (ARN) of the encryption key. Must belong to the same
              AWS Region as the destination Amazon S3 bucket. For more information, see
              `Amazon Resource Names (ARNs) and AWS Service Namespaces
              <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__
              .

        - **CloudWatchLoggingOptions** *(dict) --*

          The Amazon CloudWatch logging options for your delivery stream.

          - **Enabled** *(boolean) --*

            Enables or disables CloudWatch logging.

          - **LogGroupName** *(string) --*

            The CloudWatch group name for logging. This value is required if CloudWatch
            logging is enabled.

          - **LogStreamName** *(string) --*

            The CloudWatch log stream name for logging. This value is required if CloudWatch
            logging is enabled.

      - **CloudWatchLoggingOptions** *(dict) --*

        The Amazon CloudWatch logging options for your delivery stream.

        - **Enabled** *(boolean) --*

          Enables or disables CloudWatch logging.

        - **LogGroupName** *(string) --*

          The CloudWatch group name for logging. This value is required if CloudWatch logging
          is enabled.

        - **LogStreamName** *(string) --*

          The CloudWatch log stream name for logging. This value is required if CloudWatch
          logging is enabled.

    - **ElasticsearchDestinationDescription** *(dict) --*

      The destination in Amazon ES.

      - **RoleARN** *(string) --*

        The Amazon Resource Name (ARN) of the AWS credentials. For more information, see
        `Amazon Resource Names (ARNs) and AWS Service Namespaces
        <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

      - **DomainARN** *(string) --*

        The ARN of the Amazon ES domain. For more information, see `Amazon Resource Names
        (ARNs) and AWS Service Namespaces
        <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

        Kinesis Data Firehose uses either ``ClusterEndpoint`` or ``DomainARN`` to send data
        to Amazon ES.

      - **ClusterEndpoint** *(string) --*

        The endpoint to use when communicating with the cluster. Kinesis Data Firehose uses
        either this ``ClusterEndpoint`` or the ``DomainARN`` field to send data to Amazon ES.

      - **IndexName** *(string) --*

        The Elasticsearch index name.

      - **TypeName** *(string) --*

        The Elasticsearch type name. This applies to Elasticsearch 6.x and lower versions.
        For Elasticsearch 7.x, there's no value for ``TypeName`` .

      - **IndexRotationPeriod** *(string) --*

        The Elasticsearch index rotation period

      - **BufferingHints** *(dict) --*

        The buffering options.

        - **IntervalInSeconds** *(integer) --*

          Buffer incoming data for the specified period of time, in seconds, before
          delivering it to the destination. The default value is 300 (5 minutes).

        - **SizeInMBs** *(integer) --*

          Buffer incoming data to the specified size, in MBs, before delivering it to the
          destination. The default value is 5.

          We recommend setting this parameter to a value greater than the amount of data you
          typically ingest into the delivery stream in 10 seconds. For example, if you
          typically ingest data at 1 MB/sec, the value should be 10 MB or higher.

      - **RetryOptions** *(dict) --*

        The Amazon ES retry options.

        - **DurationInSeconds** *(integer) --*

          After an initial failure to deliver to Amazon ES, the total amount of time during
          which Kinesis Data Firehose retries delivery (including the first attempt). After
          this time has elapsed, the failed documents are written to Amazon S3. Default value
          is 300 seconds (5 minutes). A value of 0 (zero) results in no retries.

      - **S3BackupMode** *(string) --*

        The Amazon S3 backup mode.

      - **S3DestinationDescription** *(dict) --*

        The Amazon S3 destination.

        - **RoleARN** *(string) --*

          The Amazon Resource Name (ARN) of the AWS credentials. For more information, see
          `Amazon Resource Names (ARNs) and AWS Service Namespaces
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

        - **BucketARN** *(string) --*

          The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs)
          and AWS Service Namespaces
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

        - **Prefix** *(string) --*

          The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered Amazon
          S3 files. You can also specify a custom prefix, as described in `Custom Prefixes
          for Amazon S3 Objects
          <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

        - **ErrorOutputPrefix** *(string) --*

          A prefix that Kinesis Data Firehose evaluates and adds to failed records before
          writing them to S3. This prefix appears immediately following the bucket name. For
          information about how to specify this prefix, see `Custom Prefixes for Amazon S3
          Objects <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

        - **BufferingHints** *(dict) --*

          The buffering option. If no value is specified, ``BufferingHints`` object default
          values are used.

          - **SizeInMBs** *(integer) --*

            Buffer incoming data to the specified size, in MiBs, before delivering it to the
            destination. The default value is 5. This parameter is optional but if you
            specify a value for it, you must also specify a value for ``IntervalInSeconds`` ,
            and vice versa.

            We recommend setting this parameter to a value greater than the amount of data
            you typically ingest into the delivery stream in 10 seconds. For example, if you
            typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

          - **IntervalInSeconds** *(integer) --*

            Buffer incoming data for the specified period of time, in seconds, before
            delivering it to the destination. The default value is 300. This parameter is
            optional but if you specify a value for it, you must also specify a value for
            ``SizeInMBs`` , and vice versa.

        - **CompressionFormat** *(string) --*

          The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .

        - **EncryptionConfiguration** *(dict) --*

          The encryption configuration. If no value is specified, the default is no
          encryption.

          - **NoEncryptionConfig** *(string) --*

            Specifically override existing encryption information to ensure that no
            encryption is used.

          - **KMSEncryptionConfig** *(dict) --*

            The encryption key.

            - **AWSKMSKeyARN** *(string) --*

              The Amazon Resource Name (ARN) of the encryption key. Must belong to the same
              AWS Region as the destination Amazon S3 bucket. For more information, see
              `Amazon Resource Names (ARNs) and AWS Service Namespaces
              <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__
              .

        - **CloudWatchLoggingOptions** *(dict) --*

          The Amazon CloudWatch logging options for your delivery stream.

          - **Enabled** *(boolean) --*

            Enables or disables CloudWatch logging.

          - **LogGroupName** *(string) --*

            The CloudWatch group name for logging. This value is required if CloudWatch
            logging is enabled.

          - **LogStreamName** *(string) --*

            The CloudWatch log stream name for logging. This value is required if CloudWatch
            logging is enabled.

      - **ProcessingConfiguration** *(dict) --*

        The data processing configuration.

        - **Enabled** *(boolean) --*

          Enables or disables data processing.

        - **Processors** *(list) --*

          The data processors.

          - *(dict) --*

            Describes a data processor.

            - **Type** *(string) --*

              The type of processor.

            - **Parameters** *(list) --*

              The processor parameters.

              - *(dict) --*

                Describes the processor parameter.

                - **ParameterName** *(string) --*

                  The name of the parameter.

                - **ParameterValue** *(string) --*

                  The parameter value.

      - **CloudWatchLoggingOptions** *(dict) --*

        The Amazon CloudWatch logging options.

        - **Enabled** *(boolean) --*

          Enables or disables CloudWatch logging.

        - **LogGroupName** *(string) --*

          The CloudWatch group name for logging. This value is required if CloudWatch logging
          is enabled.

        - **LogStreamName** *(string) --*

          The CloudWatch log stream name for logging. This value is required if CloudWatch
          logging is enabled.

    - **SplunkDestinationDescription** *(dict) --*

      The destination in Splunk.

      - **HECEndpoint** *(string) --*

        The HTTP Event Collector (HEC) endpoint to which Kinesis Data Firehose sends your
        data.

      - **HECEndpointType** *(string) --*

        This type can be either "Raw" or "Event."

      - **HECToken** *(string) --*

        A GUID you obtain from your Splunk cluster when you create a new HEC endpoint.

      - **HECAcknowledgmentTimeoutInSeconds** *(integer) --*

        The amount of time that Kinesis Data Firehose waits to receive an acknowledgment from
        Splunk after it sends it data. At the end of the timeout period, Kinesis Data
        Firehose either tries to send the data again or considers it an error, based on your
        retry settings.

      - **RetryOptions** *(dict) --*

        The retry behavior in case Kinesis Data Firehose is unable to deliver data to Splunk
        or if it doesn't receive an acknowledgment of receipt from Splunk.

        - **DurationInSeconds** *(integer) --*

          The total amount of time that Kinesis Data Firehose spends on retries. This
          duration starts after the initial attempt to send data to Splunk fails. It doesn't
          include the periods during which Kinesis Data Firehose waits for acknowledgment
          from Splunk after each attempt.

      - **S3BackupMode** *(string) --*

        Defines how documents should be delivered to Amazon S3. When set to
        ``FailedDocumentsOnly`` , Kinesis Data Firehose writes any data that could not be
        indexed to the configured Amazon S3 destination. When set to ``AllDocuments`` ,
        Kinesis Data Firehose delivers all incoming records to Amazon S3, and also writes
        failed documents to Amazon S3. Default value is ``FailedDocumentsOnly`` .

      - **S3DestinationDescription** *(dict) --*

        The Amazon S3 destination.>

        - **RoleARN** *(string) --*

          The Amazon Resource Name (ARN) of the AWS credentials. For more information, see
          `Amazon Resource Names (ARNs) and AWS Service Namespaces
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

        - **BucketARN** *(string) --*

          The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs)
          and AWS Service Namespaces
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

        - **Prefix** *(string) --*

          The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered Amazon
          S3 files. You can also specify a custom prefix, as described in `Custom Prefixes
          for Amazon S3 Objects
          <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

        - **ErrorOutputPrefix** *(string) --*

          A prefix that Kinesis Data Firehose evaluates and adds to failed records before
          writing them to S3. This prefix appears immediately following the bucket name. For
          information about how to specify this prefix, see `Custom Prefixes for Amazon S3
          Objects <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

        - **BufferingHints** *(dict) --*

          The buffering option. If no value is specified, ``BufferingHints`` object default
          values are used.

          - **SizeInMBs** *(integer) --*

            Buffer incoming data to the specified size, in MiBs, before delivering it to the
            destination. The default value is 5. This parameter is optional but if you
            specify a value for it, you must also specify a value for ``IntervalInSeconds`` ,
            and vice versa.

            We recommend setting this parameter to a value greater than the amount of data
            you typically ingest into the delivery stream in 10 seconds. For example, if you
            typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

          - **IntervalInSeconds** *(integer) --*

            Buffer incoming data for the specified period of time, in seconds, before
            delivering it to the destination. The default value is 300. This parameter is
            optional but if you specify a value for it, you must also specify a value for
            ``SizeInMBs`` , and vice versa.

        - **CompressionFormat** *(string) --*

          The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .

        - **EncryptionConfiguration** *(dict) --*

          The encryption configuration. If no value is specified, the default is no
          encryption.

          - **NoEncryptionConfig** *(string) --*

            Specifically override existing encryption information to ensure that no
            encryption is used.

          - **KMSEncryptionConfig** *(dict) --*

            The encryption key.

            - **AWSKMSKeyARN** *(string) --*

              The Amazon Resource Name (ARN) of the encryption key. Must belong to the same
              AWS Region as the destination Amazon S3 bucket. For more information, see
              `Amazon Resource Names (ARNs) and AWS Service Namespaces
              <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__
              .

        - **CloudWatchLoggingOptions** *(dict) --*

          The Amazon CloudWatch logging options for your delivery stream.

          - **Enabled** *(boolean) --*

            Enables or disables CloudWatch logging.

          - **LogGroupName** *(string) --*

            The CloudWatch group name for logging. This value is required if CloudWatch
            logging is enabled.

          - **LogStreamName** *(string) --*

            The CloudWatch log stream name for logging. This value is required if CloudWatch
            logging is enabled.

      - **ProcessingConfiguration** *(dict) --*

        The data processing configuration.

        - **Enabled** *(boolean) --*

          Enables or disables data processing.

        - **Processors** *(list) --*

          The data processors.

          - *(dict) --*

            Describes a data processor.

            - **Type** *(string) --*

              The type of processor.

            - **Parameters** *(list) --*

              The processor parameters.

              - *(dict) --*

                Describes the processor parameter.

                - **ParameterName** *(string) --*

                  The name of the parameter.

                - **ParameterValue** *(string) --*

                  The parameter value.

      - **CloudWatchLoggingOptions** *(dict) --*

        The Amazon CloudWatch logging options for your delivery stream.

        - **Enabled** *(boolean) --*

          Enables or disables CloudWatch logging.

        - **LogGroupName** *(string) --*

          The CloudWatch group name for logging. This value is required if CloudWatch logging
          is enabled.

        - **LogStreamName** *(string) --*

          The CloudWatch log stream name for logging. This value is required if CloudWatch
          logging is enabled.
    """


_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionSourceKinesisStreamSourceDescriptionTypeDef = TypedDict(
    "_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionSourceKinesisStreamSourceDescriptionTypeDef",
    {"KinesisStreamARN": str, "RoleARN": str, "DeliveryStartTimestamp": datetime},
    total=False,
)


class ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionSourceKinesisStreamSourceDescriptionTypeDef(
    _ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionSourceKinesisStreamSourceDescriptionTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionSource` `KinesisStreamSourceDescription`

    The  KinesisStreamSourceDescription value for the source Kinesis data stream.

    - **KinesisStreamARN** *(string) --*

      The Amazon Resource Name (ARN) of the source Kinesis data stream. For more information,
      see `Amazon Kinesis Data Streams ARN Format
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-kinesis-streams>`__
      .

    - **RoleARN** *(string) --*

      The ARN of the role used by the source Kinesis data stream. For more information, see
      `AWS Identity and Access Management (IAM) ARN Format
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-iam>`__
      .

    - **DeliveryStartTimestamp** *(datetime) --*

      Kinesis Data Firehose starts retrieving records from the Kinesis data stream starting
      with this timestamp.
    """


_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionSourceTypeDef = TypedDict(
    "_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionSourceTypeDef",
    {
        "KinesisStreamSourceDescription": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionSourceKinesisStreamSourceDescriptionTypeDef
    },
    total=False,
)


class ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionSourceTypeDef(
    _ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionSourceTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryStreamResponseDeliveryStreamDescription` `Source`

    If the ``DeliveryStreamType`` parameter is ``KinesisStreamAsSource`` , a  SourceDescription
    object describing the source Kinesis data stream.

    - **KinesisStreamSourceDescription** *(dict) --*

      The  KinesisStreamSourceDescription value for the source Kinesis data stream.

      - **KinesisStreamARN** *(string) --*

        The Amazon Resource Name (ARN) of the source Kinesis data stream. For more information,
        see `Amazon Kinesis Data Streams ARN Format
        <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-kinesis-streams>`__
        .

      - **RoleARN** *(string) --*

        The ARN of the role used by the source Kinesis data stream. For more information, see
        `AWS Identity and Access Management (IAM) ARN Format
        <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-iam>`__
        .

      - **DeliveryStartTimestamp** *(datetime) --*

        Kinesis Data Firehose starts retrieving records from the Kinesis data stream starting
        with this timestamp.
    """


_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionTypeDef = TypedDict(
    "_ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionTypeDef",
    {
        "DeliveryStreamName": str,
        "DeliveryStreamARN": str,
        "DeliveryStreamStatus": str,
        "DeliveryStreamEncryptionConfiguration": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDeliveryStreamEncryptionConfigurationTypeDef,
        "DeliveryStreamType": str,
        "VersionId": str,
        "CreateTimestamp": datetime,
        "LastUpdateTimestamp": datetime,
        "Source": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionSourceTypeDef,
        "Destinations": List[
            ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsTypeDef
        ],
        "HasMoreDestinations": bool,
    },
    total=False,
)


class ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionTypeDef(
    _ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryStreamResponse` `DeliveryStreamDescription`

    Information about the delivery stream.

    - **DeliveryStreamName** *(string) --*

      The name of the delivery stream.

    - **DeliveryStreamARN** *(string) --*

      The Amazon Resource Name (ARN) of the delivery stream. For more information, see `Amazon
      Resource Names (ARNs) and AWS Service Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

    - **DeliveryStreamStatus** *(string) --*

      The status of the delivery stream.

    - **DeliveryStreamEncryptionConfiguration** *(dict) --*

      Indicates the server-side encryption (SSE) status for the delivery stream.

      - **Status** *(string) --*

        For a full description of the different values of this status, see
        StartDeliveryStreamEncryption and  StopDeliveryStreamEncryption .

    - **DeliveryStreamType** *(string) --*

      The delivery stream type. This can be one of the following values:

      * ``DirectPut`` : Provider applications access the delivery stream directly.

      * ``KinesisStreamAsSource`` : The delivery stream uses a Kinesis data stream as a source.

    - **VersionId** *(string) --*

      Each time the destination is updated for a delivery stream, the version ID is changed, and
      the current version ID is required when updating the destination. This is so that the
      service knows it is applying the changes to the correct version of the delivery stream.

    - **CreateTimestamp** *(datetime) --*

      The date and time that the delivery stream was created.

    - **LastUpdateTimestamp** *(datetime) --*

      The date and time that the delivery stream was last updated.

    - **Source** *(dict) --*

      If the ``DeliveryStreamType`` parameter is ``KinesisStreamAsSource`` , a  SourceDescription
      object describing the source Kinesis data stream.

      - **KinesisStreamSourceDescription** *(dict) --*

        The  KinesisStreamSourceDescription value for the source Kinesis data stream.

        - **KinesisStreamARN** *(string) --*

          The Amazon Resource Name (ARN) of the source Kinesis data stream. For more information,
          see `Amazon Kinesis Data Streams ARN Format
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-kinesis-streams>`__
          .

        - **RoleARN** *(string) --*

          The ARN of the role used by the source Kinesis data stream. For more information, see
          `AWS Identity and Access Management (IAM) ARN Format
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-iam>`__
          .

        - **DeliveryStartTimestamp** *(datetime) --*

          Kinesis Data Firehose starts retrieving records from the Kinesis data stream starting
          with this timestamp.

    - **Destinations** *(list) --*

      The destinations.

      - *(dict) --*

        Describes the destination for a delivery stream.

        - **DestinationId** *(string) --*

          The ID of the destination.

        - **S3DestinationDescription** *(dict) --*

          [Deprecated] The destination in Amazon S3.

          - **RoleARN** *(string) --*

            The Amazon Resource Name (ARN) of the AWS credentials. For more information, see
            `Amazon Resource Names (ARNs) and AWS Service Namespaces
            <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

          - **BucketARN** *(string) --*

            The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs) and
            AWS Service Namespaces
            <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

          - **Prefix** *(string) --*

            The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered Amazon S3
            files. You can also specify a custom prefix, as described in `Custom Prefixes for
            Amazon S3 Objects
            <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

          - **ErrorOutputPrefix** *(string) --*

            A prefix that Kinesis Data Firehose evaluates and adds to failed records before
            writing them to S3. This prefix appears immediately following the bucket name. For
            information about how to specify this prefix, see `Custom Prefixes for Amazon S3
            Objects <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

          - **BufferingHints** *(dict) --*

            The buffering option. If no value is specified, ``BufferingHints`` object default
            values are used.

            - **SizeInMBs** *(integer) --*

              Buffer incoming data to the specified size, in MiBs, before delivering it to the
              destination. The default value is 5. This parameter is optional but if you specify
              a value for it, you must also specify a value for ``IntervalInSeconds`` , and vice
              versa.

              We recommend setting this parameter to a value greater than the amount of data you
              typically ingest into the delivery stream in 10 seconds. For example, if you
              typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

            - **IntervalInSeconds** *(integer) --*

              Buffer incoming data for the specified period of time, in seconds, before
              delivering it to the destination. The default value is 300. This parameter is
              optional but if you specify a value for it, you must also specify a value for
              ``SizeInMBs`` , and vice versa.

          - **CompressionFormat** *(string) --*

            The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .

          - **EncryptionConfiguration** *(dict) --*

            The encryption configuration. If no value is specified, the default is no encryption.

            - **NoEncryptionConfig** *(string) --*

              Specifically override existing encryption information to ensure that no encryption
              is used.

            - **KMSEncryptionConfig** *(dict) --*

              The encryption key.

              - **AWSKMSKeyARN** *(string) --*

                The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS
                Region as the destination Amazon S3 bucket. For more information, see `Amazon
                Resource Names (ARNs) and AWS Service Namespaces
                <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

          - **CloudWatchLoggingOptions** *(dict) --*

            The Amazon CloudWatch logging options for your delivery stream.

            - **Enabled** *(boolean) --*

              Enables or disables CloudWatch logging.

            - **LogGroupName** *(string) --*

              The CloudWatch group name for logging. This value is required if CloudWatch logging
              is enabled.

            - **LogStreamName** *(string) --*

              The CloudWatch log stream name for logging. This value is required if CloudWatch
              logging is enabled.

        - **ExtendedS3DestinationDescription** *(dict) --*

          The destination in Amazon S3.

          - **RoleARN** *(string) --*

            The Amazon Resource Name (ARN) of the AWS credentials. For more information, see
            `Amazon Resource Names (ARNs) and AWS Service Namespaces
            <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

          - **BucketARN** *(string) --*

            The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs) and
            AWS Service Namespaces
            <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

          - **Prefix** *(string) --*

            The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered Amazon S3
            files. You can also specify a custom prefix, as described in `Custom Prefixes for
            Amazon S3 Objects
            <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

          - **ErrorOutputPrefix** *(string) --*

            A prefix that Kinesis Data Firehose evaluates and adds to failed records before
            writing them to S3. This prefix appears immediately following the bucket name. For
            information about how to specify this prefix, see `Custom Prefixes for Amazon S3
            Objects <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

          - **BufferingHints** *(dict) --*

            The buffering option.

            - **SizeInMBs** *(integer) --*

              Buffer incoming data to the specified size, in MiBs, before delivering it to the
              destination. The default value is 5. This parameter is optional but if you specify
              a value for it, you must also specify a value for ``IntervalInSeconds`` , and vice
              versa.

              We recommend setting this parameter to a value greater than the amount of data you
              typically ingest into the delivery stream in 10 seconds. For example, if you
              typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

            - **IntervalInSeconds** *(integer) --*

              Buffer incoming data for the specified period of time, in seconds, before
              delivering it to the destination. The default value is 300. This parameter is
              optional but if you specify a value for it, you must also specify a value for
              ``SizeInMBs`` , and vice versa.

          - **CompressionFormat** *(string) --*

            The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .

          - **EncryptionConfiguration** *(dict) --*

            The encryption configuration. If no value is specified, the default is no encryption.

            - **NoEncryptionConfig** *(string) --*

              Specifically override existing encryption information to ensure that no encryption
              is used.

            - **KMSEncryptionConfig** *(dict) --*

              The encryption key.

              - **AWSKMSKeyARN** *(string) --*

                The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS
                Region as the destination Amazon S3 bucket. For more information, see `Amazon
                Resource Names (ARNs) and AWS Service Namespaces
                <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

          - **CloudWatchLoggingOptions** *(dict) --*

            The Amazon CloudWatch logging options for your delivery stream.

            - **Enabled** *(boolean) --*

              Enables or disables CloudWatch logging.

            - **LogGroupName** *(string) --*

              The CloudWatch group name for logging. This value is required if CloudWatch logging
              is enabled.

            - **LogStreamName** *(string) --*

              The CloudWatch log stream name for logging. This value is required if CloudWatch
              logging is enabled.

          - **ProcessingConfiguration** *(dict) --*

            The data processing configuration.

            - **Enabled** *(boolean) --*

              Enables or disables data processing.

            - **Processors** *(list) --*

              The data processors.

              - *(dict) --*

                Describes a data processor.

                - **Type** *(string) --*

                  The type of processor.

                - **Parameters** *(list) --*

                  The processor parameters.

                  - *(dict) --*

                    Describes the processor parameter.

                    - **ParameterName** *(string) --*

                      The name of the parameter.

                    - **ParameterValue** *(string) --*

                      The parameter value.

          - **S3BackupMode** *(string) --*

            The Amazon S3 backup mode.

          - **S3BackupDescription** *(dict) --*

            The configuration for backup in Amazon S3.

            - **RoleARN** *(string) --*

              The Amazon Resource Name (ARN) of the AWS credentials. For more information, see
              `Amazon Resource Names (ARNs) and AWS Service Namespaces
              <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

            - **BucketARN** *(string) --*

              The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs)
              and AWS Service Namespaces
              <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

            - **Prefix** *(string) --*

              The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered Amazon
              S3 files. You can also specify a custom prefix, as described in `Custom Prefixes
              for Amazon S3 Objects
              <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

            - **ErrorOutputPrefix** *(string) --*

              A prefix that Kinesis Data Firehose evaluates and adds to failed records before
              writing them to S3. This prefix appears immediately following the bucket name. For
              information about how to specify this prefix, see `Custom Prefixes for Amazon S3
              Objects <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

            - **BufferingHints** *(dict) --*

              The buffering option. If no value is specified, ``BufferingHints`` object default
              values are used.

              - **SizeInMBs** *(integer) --*

                Buffer incoming data to the specified size, in MiBs, before delivering it to the
                destination. The default value is 5. This parameter is optional but if you
                specify a value for it, you must also specify a value for ``IntervalInSeconds`` ,
                and vice versa.

                We recommend setting this parameter to a value greater than the amount of data
                you typically ingest into the delivery stream in 10 seconds. For example, if you
                typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

              - **IntervalInSeconds** *(integer) --*

                Buffer incoming data for the specified period of time, in seconds, before
                delivering it to the destination. The default value is 300. This parameter is
                optional but if you specify a value for it, you must also specify a value for
                ``SizeInMBs`` , and vice versa.

            - **CompressionFormat** *(string) --*

              The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .

            - **EncryptionConfiguration** *(dict) --*

              The encryption configuration. If no value is specified, the default is no
              encryption.

              - **NoEncryptionConfig** *(string) --*

                Specifically override existing encryption information to ensure that no
                encryption is used.

              - **KMSEncryptionConfig** *(dict) --*

                The encryption key.

                - **AWSKMSKeyARN** *(string) --*

                  The Amazon Resource Name (ARN) of the encryption key. Must belong to the same
                  AWS Region as the destination Amazon S3 bucket. For more information, see
                  `Amazon Resource Names (ARNs) and AWS Service Namespaces
                  <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__
                  .

            - **CloudWatchLoggingOptions** *(dict) --*

              The Amazon CloudWatch logging options for your delivery stream.

              - **Enabled** *(boolean) --*

                Enables or disables CloudWatch logging.

              - **LogGroupName** *(string) --*

                The CloudWatch group name for logging. This value is required if CloudWatch
                logging is enabled.

              - **LogStreamName** *(string) --*

                The CloudWatch log stream name for logging. This value is required if CloudWatch
                logging is enabled.

          - **DataFormatConversionConfiguration** *(dict) --*

            The serializer, deserializer, and schema for converting data from the JSON format to
            the Parquet or ORC format before writing it to Amazon S3.

            - **SchemaConfiguration** *(dict) --*

              Specifies the AWS Glue Data Catalog table that contains the column information.

              - **RoleARN** *(string) --*

                The role that Kinesis Data Firehose can use to access AWS Glue. This role must be
                in the same account you use for Kinesis Data Firehose. Cross-account roles aren't
                allowed.

              - **CatalogId** *(string) --*

                The ID of the AWS Glue Data Catalog. If you don't supply this, the AWS account ID
                is used by default.

              - **DatabaseName** *(string) --*

                Specifies the name of the AWS Glue database that contains the schema for the
                output data.

              - **TableName** *(string) --*

                Specifies the AWS Glue table that contains the column information that
                constitutes your data schema.

              - **Region** *(string) --*

                If you don't specify an AWS Region, the default is the current Region.

              - **VersionId** *(string) --*

                Specifies the table version for the output data schema. If you don't specify this
                version ID, or if you set it to ``LATEST`` , Kinesis Data Firehose uses the most
                recent version. This means that any updates to the table are automatically picked
                up.

            - **InputFormatConfiguration** *(dict) --*

              Specifies the deserializer that you want Kinesis Data Firehose to use to convert
              the format of your data from JSON.

              - **Deserializer** *(dict) --*

                Specifies which deserializer to use. You can choose either the Apache Hive JSON
                SerDe or the OpenX JSON SerDe. If both are non-null, the server rejects the
                request.

                - **OpenXJsonSerDe** *(dict) --*

                  The OpenX SerDe. Used by Kinesis Data Firehose for deserializing data, which
                  means converting it from the JSON format in preparation for serializing it to
                  the Parquet or ORC format. This is one of two deserializers you can choose,
                  depending on which one offers the functionality you need. The other option is
                  the native Hive / HCatalog JsonSerDe.

                  - **ConvertDotsInJsonKeysToUnderscores** *(boolean) --*

                    When set to ``true`` , specifies that the names of the keys include dots and
                    that you want Kinesis Data Firehose to replace them with underscores. This is
                    useful because Apache Hive does not allow dots in column names. For example,
                    if the JSON contains a key whose name is "a.b", you can define the column
                    name to be "a_b" when using this option.

                    The default is ``false`` .

                  - **CaseInsensitive** *(boolean) --*

                    When set to ``true`` , which is the default, Kinesis Data Firehose converts
                    JSON keys to lowercase before deserializing them.

                  - **ColumnToJsonKeyMappings** *(dict) --*

                    Maps column names to JSON keys that aren't identical to the column names.
                    This is useful when the JSON contains keys that are Hive keywords. For
                    example, ``timestamp`` is a Hive keyword. If you have a JSON key named
                    ``timestamp`` , set this parameter to ``{"ts": "timestamp"}`` to map this key
                    to a column named ``ts`` .

                    - *(string) --*

                      - *(string) --*

                - **HiveJsonSerDe** *(dict) --*

                  The native Hive / HCatalog JsonSerDe. Used by Kinesis Data Firehose for
                  deserializing data, which means converting it from the JSON format in
                  preparation for serializing it to the Parquet or ORC format. This is one of two
                  deserializers you can choose, depending on which one offers the functionality
                  you need. The other option is the OpenX SerDe.

                  - **TimestampFormats** *(list) --*

                    Indicates how you want Kinesis Data Firehose to parse the date and timestamps
                    that may be present in your input data JSON. To specify these format strings,
                    follow the pattern syntax of JodaTime's DateTimeFormat format strings. For
                    more information, see `Class DateTimeFormat
                    <https://www.joda.org/joda-time/apidocs/org/joda/time/format/DateTimeFormat.html>`__
                    . You can also use the special value ``millis`` to parse timestamps in epoch
                    milliseconds. If you don't specify a format, Kinesis Data Firehose uses
                    ``java.sql.Timestamp::valueOf`` by default.

                    - *(string) --*

            - **OutputFormatConfiguration** *(dict) --*

              Specifies the serializer that you want Kinesis Data Firehose to use to convert the
              format of your data to the Parquet or ORC format.

              - **Serializer** *(dict) --*

                Specifies which serializer to use. You can choose either the ORC SerDe or the
                Parquet SerDe. If both are non-null, the server rejects the request.

                - **ParquetSerDe** *(dict) --*

                  A serializer to use for converting data to the Parquet format before storing it
                  in Amazon S3. For more information, see `Apache Parquet
                  <https://parquet.apache.org/documentation/latest/>`__ .

                  - **BlockSizeBytes** *(integer) --*

                    The Hadoop Distributed File System (HDFS) block size. This is useful if you
                    intend to copy the data from Amazon S3 to HDFS before querying. The default
                    is 256 MiB and the minimum is 64 MiB. Kinesis Data Firehose uses this value
                    for padding calculations.

                  - **PageSizeBytes** *(integer) --*

                    The Parquet page size. Column chunks are divided into pages. A page is
                    conceptually an indivisible unit (in terms of compression and encoding). The
                    minimum value is 64 KiB and the default is 1 MiB.

                  - **Compression** *(string) --*

                    The compression code to use over data blocks. The possible values are
                    ``UNCOMPRESSED`` , ``SNAPPY`` , and ``GZIP`` , with the default being
                    ``SNAPPY`` . Use ``SNAPPY`` for higher decompression speed. Use ``GZIP`` if
                    the compression ration is more important than speed.

                  - **EnableDictionaryCompression** *(boolean) --*

                    Indicates whether to enable dictionary compression.

                  - **MaxPaddingBytes** *(integer) --*

                    The maximum amount of padding to apply. This is useful if you intend to copy
                    the data from Amazon S3 to HDFS before querying. The default is 0.

                  - **WriterVersion** *(string) --*

                    Indicates the version of row format to output. The possible values are ``V1``
                    and ``V2`` . The default is ``V1`` .

                - **OrcSerDe** *(dict) --*

                  A serializer to use for converting data to the ORC format before storing it in
                  Amazon S3. For more information, see `Apache ORC
                  <https://orc.apache.org/docs/>`__ .

                  - **StripeSizeBytes** *(integer) --*

                    The number of bytes in each stripe. The default is 64 MiB and the minimum is
                    8 MiB.

                  - **BlockSizeBytes** *(integer) --*

                    The Hadoop Distributed File System (HDFS) block size. This is useful if you
                    intend to copy the data from Amazon S3 to HDFS before querying. The default
                    is 256 MiB and the minimum is 64 MiB. Kinesis Data Firehose uses this value
                    for padding calculations.

                  - **RowIndexStride** *(integer) --*

                    The number of rows between index entries. The default is 10,000 and the
                    minimum is 1,000.

                  - **EnablePadding** *(boolean) --*

                    Set this to ``true`` to indicate that you want stripes to be padded to the
                    HDFS block boundaries. This is useful if you intend to copy the data from
                    Amazon S3 to HDFS before querying. The default is ``false`` .

                  - **PaddingTolerance** *(float) --*

                    A number between 0 and 1 that defines the tolerance for block padding as a
                    decimal fraction of stripe size. The default value is 0.05, which means 5
                    percent of stripe size.

                    For the default values of 64 MiB ORC stripes and 256 MiB HDFS blocks, the
                    default block padding tolerance of 5 percent reserves a maximum of 3.2 MiB
                    for padding within the 256 MiB block. In such a case, if the available size
                    within the block is more than 3.2 MiB, a new, smaller stripe is inserted to
                    fit within that space. This ensures that no stripe crosses block boundaries
                    and causes remote reads within a node-local task.

                    Kinesis Data Firehose ignores this parameter when  OrcSerDe$EnablePadding is
                    ``false`` .

                  - **Compression** *(string) --*

                    The compression code to use over data blocks. The default is ``SNAPPY`` .

                  - **BloomFilterColumns** *(list) --*

                    The column names for which you want Kinesis Data Firehose to create bloom
                    filters. The default is ``null`` .

                    - *(string) --*

                  - **BloomFilterFalsePositiveProbability** *(float) --*

                    The Bloom filter false positive probability (FPP). The lower the FPP, the
                    bigger the Bloom filter. The default value is 0.05, the minimum is 0, and the
                    maximum is 1.

                  - **DictionaryKeyThreshold** *(float) --*

                    Represents the fraction of the total number of non-null rows. To turn off
                    dictionary encoding, set this fraction to a number that is less than the
                    number of distinct keys in a dictionary. To always use dictionary encoding,
                    set this threshold to 1.

                  - **FormatVersion** *(string) --*

                    The version of the file to write. The possible values are ``V0_11`` and
                    ``V0_12`` . The default is ``V0_12`` .

            - **Enabled** *(boolean) --*

              Defaults to ``true`` . Set it to ``false`` if you want to disable format conversion
              while preserving the configuration details.

        - **RedshiftDestinationDescription** *(dict) --*

          The destination in Amazon Redshift.

          - **RoleARN** *(string) --*

            The Amazon Resource Name (ARN) of the AWS credentials. For more information, see
            `Amazon Resource Names (ARNs) and AWS Service Namespaces
            <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

          - **ClusterJDBCURL** *(string) --*

            The database connection string.

          - **CopyCommand** *(dict) --*

            The ``COPY`` command.

            - **DataTableName** *(string) --*

              The name of the target table. The table must already exist in the database.

            - **DataTableColumns** *(string) --*

              A comma-separated list of column names.

            - **CopyOptions** *(string) --*

              Optional parameters to use with the Amazon Redshift ``COPY`` command. For more
              information, see the "Optional Parameters" section of `Amazon Redshift COPY command
              <https://docs.aws.amazon.com/redshift/latest/dg/r_COPY.html>`__ . Some possible
              examples that would apply to Kinesis Data Firehose are as follows:

               ``delimiter '\\t' lzop;`` - fields are delimited with "\\t" (TAB character) and
               compressed using lzop.

               ``delimiter '|'`` - fields are delimited with "|" (this is the default delimiter).

               ``delimiter '|' escape`` - the delimiter should be escaped.

               ``fixedwidth 'venueid:3,venuename:25,venuecity:12,venuestate:2,venueseats:6'`` -
               fields are fixed width in the source, with each width specified after every column
               in the table.

               ``JSON 's3://mybucket/jsonpaths.txt'`` - data is in JSON format, and the path
               specified is the format of the data.

              For more examples, see `Amazon Redshift COPY command examples
              <https://docs.aws.amazon.com/redshift/latest/dg/r_COPY_command_examples.html>`__ .

          - **Username** *(string) --*

            The name of the user.

          - **RetryOptions** *(dict) --*

            The retry behavior in case Kinesis Data Firehose is unable to deliver documents to
            Amazon Redshift. Default value is 3600 (60 minutes).

            - **DurationInSeconds** *(integer) --*

              The length of time during which Kinesis Data Firehose retries delivery after a
              failure, starting from the initial request and including the first attempt. The
              default value is 3600 seconds (60 minutes). Kinesis Data Firehose does not retry if
              the value of ``DurationInSeconds`` is 0 (zero) or if the first delivery attempt
              takes longer than the current value.

          - **S3DestinationDescription** *(dict) --*

            The Amazon S3 destination.

            - **RoleARN** *(string) --*

              The Amazon Resource Name (ARN) of the AWS credentials. For more information, see
              `Amazon Resource Names (ARNs) and AWS Service Namespaces
              <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

            - **BucketARN** *(string) --*

              The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs)
              and AWS Service Namespaces
              <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

            - **Prefix** *(string) --*

              The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered Amazon
              S3 files. You can also specify a custom prefix, as described in `Custom Prefixes
              for Amazon S3 Objects
              <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

            - **ErrorOutputPrefix** *(string) --*

              A prefix that Kinesis Data Firehose evaluates and adds to failed records before
              writing them to S3. This prefix appears immediately following the bucket name. For
              information about how to specify this prefix, see `Custom Prefixes for Amazon S3
              Objects <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

            - **BufferingHints** *(dict) --*

              The buffering option. If no value is specified, ``BufferingHints`` object default
              values are used.

              - **SizeInMBs** *(integer) --*

                Buffer incoming data to the specified size, in MiBs, before delivering it to the
                destination. The default value is 5. This parameter is optional but if you
                specify a value for it, you must also specify a value for ``IntervalInSeconds`` ,
                and vice versa.

                We recommend setting this parameter to a value greater than the amount of data
                you typically ingest into the delivery stream in 10 seconds. For example, if you
                typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

              - **IntervalInSeconds** *(integer) --*

                Buffer incoming data for the specified period of time, in seconds, before
                delivering it to the destination. The default value is 300. This parameter is
                optional but if you specify a value for it, you must also specify a value for
                ``SizeInMBs`` , and vice versa.

            - **CompressionFormat** *(string) --*

              The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .

            - **EncryptionConfiguration** *(dict) --*

              The encryption configuration. If no value is specified, the default is no
              encryption.

              - **NoEncryptionConfig** *(string) --*

                Specifically override existing encryption information to ensure that no
                encryption is used.

              - **KMSEncryptionConfig** *(dict) --*

                The encryption key.

                - **AWSKMSKeyARN** *(string) --*

                  The Amazon Resource Name (ARN) of the encryption key. Must belong to the same
                  AWS Region as the destination Amazon S3 bucket. For more information, see
                  `Amazon Resource Names (ARNs) and AWS Service Namespaces
                  <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__
                  .

            - **CloudWatchLoggingOptions** *(dict) --*

              The Amazon CloudWatch logging options for your delivery stream.

              - **Enabled** *(boolean) --*

                Enables or disables CloudWatch logging.

              - **LogGroupName** *(string) --*

                The CloudWatch group name for logging. This value is required if CloudWatch
                logging is enabled.

              - **LogStreamName** *(string) --*

                The CloudWatch log stream name for logging. This value is required if CloudWatch
                logging is enabled.

          - **ProcessingConfiguration** *(dict) --*

            The data processing configuration.

            - **Enabled** *(boolean) --*

              Enables or disables data processing.

            - **Processors** *(list) --*

              The data processors.

              - *(dict) --*

                Describes a data processor.

                - **Type** *(string) --*

                  The type of processor.

                - **Parameters** *(list) --*

                  The processor parameters.

                  - *(dict) --*

                    Describes the processor parameter.

                    - **ParameterName** *(string) --*

                      The name of the parameter.

                    - **ParameterValue** *(string) --*

                      The parameter value.

          - **S3BackupMode** *(string) --*

            The Amazon S3 backup mode.

          - **S3BackupDescription** *(dict) --*

            The configuration for backup in Amazon S3.

            - **RoleARN** *(string) --*

              The Amazon Resource Name (ARN) of the AWS credentials. For more information, see
              `Amazon Resource Names (ARNs) and AWS Service Namespaces
              <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

            - **BucketARN** *(string) --*

              The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs)
              and AWS Service Namespaces
              <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

            - **Prefix** *(string) --*

              The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered Amazon
              S3 files. You can also specify a custom prefix, as described in `Custom Prefixes
              for Amazon S3 Objects
              <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

            - **ErrorOutputPrefix** *(string) --*

              A prefix that Kinesis Data Firehose evaluates and adds to failed records before
              writing them to S3. This prefix appears immediately following the bucket name. For
              information about how to specify this prefix, see `Custom Prefixes for Amazon S3
              Objects <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

            - **BufferingHints** *(dict) --*

              The buffering option. If no value is specified, ``BufferingHints`` object default
              values are used.

              - **SizeInMBs** *(integer) --*

                Buffer incoming data to the specified size, in MiBs, before delivering it to the
                destination. The default value is 5. This parameter is optional but if you
                specify a value for it, you must also specify a value for ``IntervalInSeconds`` ,
                and vice versa.

                We recommend setting this parameter to a value greater than the amount of data
                you typically ingest into the delivery stream in 10 seconds. For example, if you
                typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

              - **IntervalInSeconds** *(integer) --*

                Buffer incoming data for the specified period of time, in seconds, before
                delivering it to the destination. The default value is 300. This parameter is
                optional but if you specify a value for it, you must also specify a value for
                ``SizeInMBs`` , and vice versa.

            - **CompressionFormat** *(string) --*

              The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .

            - **EncryptionConfiguration** *(dict) --*

              The encryption configuration. If no value is specified, the default is no
              encryption.

              - **NoEncryptionConfig** *(string) --*

                Specifically override existing encryption information to ensure that no
                encryption is used.

              - **KMSEncryptionConfig** *(dict) --*

                The encryption key.

                - **AWSKMSKeyARN** *(string) --*

                  The Amazon Resource Name (ARN) of the encryption key. Must belong to the same
                  AWS Region as the destination Amazon S3 bucket. For more information, see
                  `Amazon Resource Names (ARNs) and AWS Service Namespaces
                  <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__
                  .

            - **CloudWatchLoggingOptions** *(dict) --*

              The Amazon CloudWatch logging options for your delivery stream.

              - **Enabled** *(boolean) --*

                Enables or disables CloudWatch logging.

              - **LogGroupName** *(string) --*

                The CloudWatch group name for logging. This value is required if CloudWatch
                logging is enabled.

              - **LogStreamName** *(string) --*

                The CloudWatch log stream name for logging. This value is required if CloudWatch
                logging is enabled.

          - **CloudWatchLoggingOptions** *(dict) --*

            The Amazon CloudWatch logging options for your delivery stream.

            - **Enabled** *(boolean) --*

              Enables or disables CloudWatch logging.

            - **LogGroupName** *(string) --*

              The CloudWatch group name for logging. This value is required if CloudWatch logging
              is enabled.

            - **LogStreamName** *(string) --*

              The CloudWatch log stream name for logging. This value is required if CloudWatch
              logging is enabled.

        - **ElasticsearchDestinationDescription** *(dict) --*

          The destination in Amazon ES.

          - **RoleARN** *(string) --*

            The Amazon Resource Name (ARN) of the AWS credentials. For more information, see
            `Amazon Resource Names (ARNs) and AWS Service Namespaces
            <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

          - **DomainARN** *(string) --*

            The ARN of the Amazon ES domain. For more information, see `Amazon Resource Names
            (ARNs) and AWS Service Namespaces
            <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

            Kinesis Data Firehose uses either ``ClusterEndpoint`` or ``DomainARN`` to send data
            to Amazon ES.

          - **ClusterEndpoint** *(string) --*

            The endpoint to use when communicating with the cluster. Kinesis Data Firehose uses
            either this ``ClusterEndpoint`` or the ``DomainARN`` field to send data to Amazon ES.

          - **IndexName** *(string) --*

            The Elasticsearch index name.

          - **TypeName** *(string) --*

            The Elasticsearch type name. This applies to Elasticsearch 6.x and lower versions.
            For Elasticsearch 7.x, there's no value for ``TypeName`` .

          - **IndexRotationPeriod** *(string) --*

            The Elasticsearch index rotation period

          - **BufferingHints** *(dict) --*

            The buffering options.

            - **IntervalInSeconds** *(integer) --*

              Buffer incoming data for the specified period of time, in seconds, before
              delivering it to the destination. The default value is 300 (5 minutes).

            - **SizeInMBs** *(integer) --*

              Buffer incoming data to the specified size, in MBs, before delivering it to the
              destination. The default value is 5.

              We recommend setting this parameter to a value greater than the amount of data you
              typically ingest into the delivery stream in 10 seconds. For example, if you
              typically ingest data at 1 MB/sec, the value should be 10 MB or higher.

          - **RetryOptions** *(dict) --*

            The Amazon ES retry options.

            - **DurationInSeconds** *(integer) --*

              After an initial failure to deliver to Amazon ES, the total amount of time during
              which Kinesis Data Firehose retries delivery (including the first attempt). After
              this time has elapsed, the failed documents are written to Amazon S3. Default value
              is 300 seconds (5 minutes). A value of 0 (zero) results in no retries.

          - **S3BackupMode** *(string) --*

            The Amazon S3 backup mode.

          - **S3DestinationDescription** *(dict) --*

            The Amazon S3 destination.

            - **RoleARN** *(string) --*

              The Amazon Resource Name (ARN) of the AWS credentials. For more information, see
              `Amazon Resource Names (ARNs) and AWS Service Namespaces
              <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

            - **BucketARN** *(string) --*

              The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs)
              and AWS Service Namespaces
              <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

            - **Prefix** *(string) --*

              The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered Amazon
              S3 files. You can also specify a custom prefix, as described in `Custom Prefixes
              for Amazon S3 Objects
              <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

            - **ErrorOutputPrefix** *(string) --*

              A prefix that Kinesis Data Firehose evaluates and adds to failed records before
              writing them to S3. This prefix appears immediately following the bucket name. For
              information about how to specify this prefix, see `Custom Prefixes for Amazon S3
              Objects <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

            - **BufferingHints** *(dict) --*

              The buffering option. If no value is specified, ``BufferingHints`` object default
              values are used.

              - **SizeInMBs** *(integer) --*

                Buffer incoming data to the specified size, in MiBs, before delivering it to the
                destination. The default value is 5. This parameter is optional but if you
                specify a value for it, you must also specify a value for ``IntervalInSeconds`` ,
                and vice versa.

                We recommend setting this parameter to a value greater than the amount of data
                you typically ingest into the delivery stream in 10 seconds. For example, if you
                typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

              - **IntervalInSeconds** *(integer) --*

                Buffer incoming data for the specified period of time, in seconds, before
                delivering it to the destination. The default value is 300. This parameter is
                optional but if you specify a value for it, you must also specify a value for
                ``SizeInMBs`` , and vice versa.

            - **CompressionFormat** *(string) --*

              The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .

            - **EncryptionConfiguration** *(dict) --*

              The encryption configuration. If no value is specified, the default is no
              encryption.

              - **NoEncryptionConfig** *(string) --*

                Specifically override existing encryption information to ensure that no
                encryption is used.

              - **KMSEncryptionConfig** *(dict) --*

                The encryption key.

                - **AWSKMSKeyARN** *(string) --*

                  The Amazon Resource Name (ARN) of the encryption key. Must belong to the same
                  AWS Region as the destination Amazon S3 bucket. For more information, see
                  `Amazon Resource Names (ARNs) and AWS Service Namespaces
                  <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__
                  .

            - **CloudWatchLoggingOptions** *(dict) --*

              The Amazon CloudWatch logging options for your delivery stream.

              - **Enabled** *(boolean) --*

                Enables or disables CloudWatch logging.

              - **LogGroupName** *(string) --*

                The CloudWatch group name for logging. This value is required if CloudWatch
                logging is enabled.

              - **LogStreamName** *(string) --*

                The CloudWatch log stream name for logging. This value is required if CloudWatch
                logging is enabled.

          - **ProcessingConfiguration** *(dict) --*

            The data processing configuration.

            - **Enabled** *(boolean) --*

              Enables or disables data processing.

            - **Processors** *(list) --*

              The data processors.

              - *(dict) --*

                Describes a data processor.

                - **Type** *(string) --*

                  The type of processor.

                - **Parameters** *(list) --*

                  The processor parameters.

                  - *(dict) --*

                    Describes the processor parameter.

                    - **ParameterName** *(string) --*

                      The name of the parameter.

                    - **ParameterValue** *(string) --*

                      The parameter value.

          - **CloudWatchLoggingOptions** *(dict) --*

            The Amazon CloudWatch logging options.

            - **Enabled** *(boolean) --*

              Enables or disables CloudWatch logging.

            - **LogGroupName** *(string) --*

              The CloudWatch group name for logging. This value is required if CloudWatch logging
              is enabled.

            - **LogStreamName** *(string) --*

              The CloudWatch log stream name for logging. This value is required if CloudWatch
              logging is enabled.

        - **SplunkDestinationDescription** *(dict) --*

          The destination in Splunk.

          - **HECEndpoint** *(string) --*

            The HTTP Event Collector (HEC) endpoint to which Kinesis Data Firehose sends your
            data.

          - **HECEndpointType** *(string) --*

            This type can be either "Raw" or "Event."

          - **HECToken** *(string) --*

            A GUID you obtain from your Splunk cluster when you create a new HEC endpoint.

          - **HECAcknowledgmentTimeoutInSeconds** *(integer) --*

            The amount of time that Kinesis Data Firehose waits to receive an acknowledgment from
            Splunk after it sends it data. At the end of the timeout period, Kinesis Data
            Firehose either tries to send the data again or considers it an error, based on your
            retry settings.

          - **RetryOptions** *(dict) --*

            The retry behavior in case Kinesis Data Firehose is unable to deliver data to Splunk
            or if it doesn't receive an acknowledgment of receipt from Splunk.

            - **DurationInSeconds** *(integer) --*

              The total amount of time that Kinesis Data Firehose spends on retries. This
              duration starts after the initial attempt to send data to Splunk fails. It doesn't
              include the periods during which Kinesis Data Firehose waits for acknowledgment
              from Splunk after each attempt.

          - **S3BackupMode** *(string) --*

            Defines how documents should be delivered to Amazon S3. When set to
            ``FailedDocumentsOnly`` , Kinesis Data Firehose writes any data that could not be
            indexed to the configured Amazon S3 destination. When set to ``AllDocuments`` ,
            Kinesis Data Firehose delivers all incoming records to Amazon S3, and also writes
            failed documents to Amazon S3. Default value is ``FailedDocumentsOnly`` .

          - **S3DestinationDescription** *(dict) --*

            The Amazon S3 destination.>

            - **RoleARN** *(string) --*

              The Amazon Resource Name (ARN) of the AWS credentials. For more information, see
              `Amazon Resource Names (ARNs) and AWS Service Namespaces
              <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

            - **BucketARN** *(string) --*

              The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs)
              and AWS Service Namespaces
              <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

            - **Prefix** *(string) --*

              The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered Amazon
              S3 files. You can also specify a custom prefix, as described in `Custom Prefixes
              for Amazon S3 Objects
              <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

            - **ErrorOutputPrefix** *(string) --*

              A prefix that Kinesis Data Firehose evaluates and adds to failed records before
              writing them to S3. This prefix appears immediately following the bucket name. For
              information about how to specify this prefix, see `Custom Prefixes for Amazon S3
              Objects <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

            - **BufferingHints** *(dict) --*

              The buffering option. If no value is specified, ``BufferingHints`` object default
              values are used.

              - **SizeInMBs** *(integer) --*

                Buffer incoming data to the specified size, in MiBs, before delivering it to the
                destination. The default value is 5. This parameter is optional but if you
                specify a value for it, you must also specify a value for ``IntervalInSeconds`` ,
                and vice versa.

                We recommend setting this parameter to a value greater than the amount of data
                you typically ingest into the delivery stream in 10 seconds. For example, if you
                typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

              - **IntervalInSeconds** *(integer) --*

                Buffer incoming data for the specified period of time, in seconds, before
                delivering it to the destination. The default value is 300. This parameter is
                optional but if you specify a value for it, you must also specify a value for
                ``SizeInMBs`` , and vice versa.

            - **CompressionFormat** *(string) --*

              The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .

            - **EncryptionConfiguration** *(dict) --*

              The encryption configuration. If no value is specified, the default is no
              encryption.

              - **NoEncryptionConfig** *(string) --*

                Specifically override existing encryption information to ensure that no
                encryption is used.

              - **KMSEncryptionConfig** *(dict) --*

                The encryption key.

                - **AWSKMSKeyARN** *(string) --*

                  The Amazon Resource Name (ARN) of the encryption key. Must belong to the same
                  AWS Region as the destination Amazon S3 bucket. For more information, see
                  `Amazon Resource Names (ARNs) and AWS Service Namespaces
                  <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__
                  .

            - **CloudWatchLoggingOptions** *(dict) --*

              The Amazon CloudWatch logging options for your delivery stream.

              - **Enabled** *(boolean) --*

                Enables or disables CloudWatch logging.

              - **LogGroupName** *(string) --*

                The CloudWatch group name for logging. This value is required if CloudWatch
                logging is enabled.

              - **LogStreamName** *(string) --*

                The CloudWatch log stream name for logging. This value is required if CloudWatch
                logging is enabled.

          - **ProcessingConfiguration** *(dict) --*

            The data processing configuration.

            - **Enabled** *(boolean) --*

              Enables or disables data processing.

            - **Processors** *(list) --*

              The data processors.

              - *(dict) --*

                Describes a data processor.

                - **Type** *(string) --*

                  The type of processor.

                - **Parameters** *(list) --*

                  The processor parameters.

                  - *(dict) --*

                    Describes the processor parameter.

                    - **ParameterName** *(string) --*

                      The name of the parameter.

                    - **ParameterValue** *(string) --*

                      The parameter value.

          - **CloudWatchLoggingOptions** *(dict) --*

            The Amazon CloudWatch logging options for your delivery stream.

            - **Enabled** *(boolean) --*

              Enables or disables CloudWatch logging.

            - **LogGroupName** *(string) --*

              The CloudWatch group name for logging. This value is required if CloudWatch logging
              is enabled.

            - **LogStreamName** *(string) --*

              The CloudWatch log stream name for logging. This value is required if CloudWatch
              logging is enabled.

    - **HasMoreDestinations** *(boolean) --*

      Indicates whether there are more destinations available to list.
    """


_ClientDescribeDeliveryStreamResponseTypeDef = TypedDict(
    "_ClientDescribeDeliveryStreamResponseTypeDef",
    {
        "DeliveryStreamDescription": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionTypeDef
    },
    total=False,
)


class ClientDescribeDeliveryStreamResponseTypeDef(
    _ClientDescribeDeliveryStreamResponseTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryStream` `Response`

    - **DeliveryStreamDescription** *(dict) --*

      Information about the delivery stream.

      - **DeliveryStreamName** *(string) --*

        The name of the delivery stream.

      - **DeliveryStreamARN** *(string) --*

        The Amazon Resource Name (ARN) of the delivery stream. For more information, see `Amazon
        Resource Names (ARNs) and AWS Service Namespaces
        <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

      - **DeliveryStreamStatus** *(string) --*

        The status of the delivery stream.

      - **DeliveryStreamEncryptionConfiguration** *(dict) --*

        Indicates the server-side encryption (SSE) status for the delivery stream.

        - **Status** *(string) --*

          For a full description of the different values of this status, see
          StartDeliveryStreamEncryption and  StopDeliveryStreamEncryption .

      - **DeliveryStreamType** *(string) --*

        The delivery stream type. This can be one of the following values:

        * ``DirectPut`` : Provider applications access the delivery stream directly.

        * ``KinesisStreamAsSource`` : The delivery stream uses a Kinesis data stream as a source.

      - **VersionId** *(string) --*

        Each time the destination is updated for a delivery stream, the version ID is changed, and
        the current version ID is required when updating the destination. This is so that the
        service knows it is applying the changes to the correct version of the delivery stream.

      - **CreateTimestamp** *(datetime) --*

        The date and time that the delivery stream was created.

      - **LastUpdateTimestamp** *(datetime) --*

        The date and time that the delivery stream was last updated.

      - **Source** *(dict) --*

        If the ``DeliveryStreamType`` parameter is ``KinesisStreamAsSource`` , a  SourceDescription
        object describing the source Kinesis data stream.

        - **KinesisStreamSourceDescription** *(dict) --*

          The  KinesisStreamSourceDescription value for the source Kinesis data stream.

          - **KinesisStreamARN** *(string) --*

            The Amazon Resource Name (ARN) of the source Kinesis data stream. For more information,
            see `Amazon Kinesis Data Streams ARN Format
            <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-kinesis-streams>`__
            .

          - **RoleARN** *(string) --*

            The ARN of the role used by the source Kinesis data stream. For more information, see
            `AWS Identity and Access Management (IAM) ARN Format
            <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-iam>`__
            .

          - **DeliveryStartTimestamp** *(datetime) --*

            Kinesis Data Firehose starts retrieving records from the Kinesis data stream starting
            with this timestamp.

      - **Destinations** *(list) --*

        The destinations.

        - *(dict) --*

          Describes the destination for a delivery stream.

          - **DestinationId** *(string) --*

            The ID of the destination.

          - **S3DestinationDescription** *(dict) --*

            [Deprecated] The destination in Amazon S3.

            - **RoleARN** *(string) --*

              The Amazon Resource Name (ARN) of the AWS credentials. For more information, see
              `Amazon Resource Names (ARNs) and AWS Service Namespaces
              <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

            - **BucketARN** *(string) --*

              The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs) and
              AWS Service Namespaces
              <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

            - **Prefix** *(string) --*

              The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered Amazon S3
              files. You can also specify a custom prefix, as described in `Custom Prefixes for
              Amazon S3 Objects
              <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

            - **ErrorOutputPrefix** *(string) --*

              A prefix that Kinesis Data Firehose evaluates and adds to failed records before
              writing them to S3. This prefix appears immediately following the bucket name. For
              information about how to specify this prefix, see `Custom Prefixes for Amazon S3
              Objects <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

            - **BufferingHints** *(dict) --*

              The buffering option. If no value is specified, ``BufferingHints`` object default
              values are used.

              - **SizeInMBs** *(integer) --*

                Buffer incoming data to the specified size, in MiBs, before delivering it to the
                destination. The default value is 5. This parameter is optional but if you specify
                a value for it, you must also specify a value for ``IntervalInSeconds`` , and vice
                versa.

                We recommend setting this parameter to a value greater than the amount of data you
                typically ingest into the delivery stream in 10 seconds. For example, if you
                typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

              - **IntervalInSeconds** *(integer) --*

                Buffer incoming data for the specified period of time, in seconds, before
                delivering it to the destination. The default value is 300. This parameter is
                optional but if you specify a value for it, you must also specify a value for
                ``SizeInMBs`` , and vice versa.

            - **CompressionFormat** *(string) --*

              The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .

            - **EncryptionConfiguration** *(dict) --*

              The encryption configuration. If no value is specified, the default is no encryption.

              - **NoEncryptionConfig** *(string) --*

                Specifically override existing encryption information to ensure that no encryption
                is used.

              - **KMSEncryptionConfig** *(dict) --*

                The encryption key.

                - **AWSKMSKeyARN** *(string) --*

                  The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS
                  Region as the destination Amazon S3 bucket. For more information, see `Amazon
                  Resource Names (ARNs) and AWS Service Namespaces
                  <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

            - **CloudWatchLoggingOptions** *(dict) --*

              The Amazon CloudWatch logging options for your delivery stream.

              - **Enabled** *(boolean) --*

                Enables or disables CloudWatch logging.

              - **LogGroupName** *(string) --*

                The CloudWatch group name for logging. This value is required if CloudWatch logging
                is enabled.

              - **LogStreamName** *(string) --*

                The CloudWatch log stream name for logging. This value is required if CloudWatch
                logging is enabled.

          - **ExtendedS3DestinationDescription** *(dict) --*

            The destination in Amazon S3.

            - **RoleARN** *(string) --*

              The Amazon Resource Name (ARN) of the AWS credentials. For more information, see
              `Amazon Resource Names (ARNs) and AWS Service Namespaces
              <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

            - **BucketARN** *(string) --*

              The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs) and
              AWS Service Namespaces
              <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

            - **Prefix** *(string) --*

              The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered Amazon S3
              files. You can also specify a custom prefix, as described in `Custom Prefixes for
              Amazon S3 Objects
              <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

            - **ErrorOutputPrefix** *(string) --*

              A prefix that Kinesis Data Firehose evaluates and adds to failed records before
              writing them to S3. This prefix appears immediately following the bucket name. For
              information about how to specify this prefix, see `Custom Prefixes for Amazon S3
              Objects <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

            - **BufferingHints** *(dict) --*

              The buffering option.

              - **SizeInMBs** *(integer) --*

                Buffer incoming data to the specified size, in MiBs, before delivering it to the
                destination. The default value is 5. This parameter is optional but if you specify
                a value for it, you must also specify a value for ``IntervalInSeconds`` , and vice
                versa.

                We recommend setting this parameter to a value greater than the amount of data you
                typically ingest into the delivery stream in 10 seconds. For example, if you
                typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

              - **IntervalInSeconds** *(integer) --*

                Buffer incoming data for the specified period of time, in seconds, before
                delivering it to the destination. The default value is 300. This parameter is
                optional but if you specify a value for it, you must also specify a value for
                ``SizeInMBs`` , and vice versa.

            - **CompressionFormat** *(string) --*

              The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .

            - **EncryptionConfiguration** *(dict) --*

              The encryption configuration. If no value is specified, the default is no encryption.

              - **NoEncryptionConfig** *(string) --*

                Specifically override existing encryption information to ensure that no encryption
                is used.

              - **KMSEncryptionConfig** *(dict) --*

                The encryption key.

                - **AWSKMSKeyARN** *(string) --*

                  The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS
                  Region as the destination Amazon S3 bucket. For more information, see `Amazon
                  Resource Names (ARNs) and AWS Service Namespaces
                  <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

            - **CloudWatchLoggingOptions** *(dict) --*

              The Amazon CloudWatch logging options for your delivery stream.

              - **Enabled** *(boolean) --*

                Enables or disables CloudWatch logging.

              - **LogGroupName** *(string) --*

                The CloudWatch group name for logging. This value is required if CloudWatch logging
                is enabled.

              - **LogStreamName** *(string) --*

                The CloudWatch log stream name for logging. This value is required if CloudWatch
                logging is enabled.

            - **ProcessingConfiguration** *(dict) --*

              The data processing configuration.

              - **Enabled** *(boolean) --*

                Enables or disables data processing.

              - **Processors** *(list) --*

                The data processors.

                - *(dict) --*

                  Describes a data processor.

                  - **Type** *(string) --*

                    The type of processor.

                  - **Parameters** *(list) --*

                    The processor parameters.

                    - *(dict) --*

                      Describes the processor parameter.

                      - **ParameterName** *(string) --*

                        The name of the parameter.

                      - **ParameterValue** *(string) --*

                        The parameter value.

            - **S3BackupMode** *(string) --*

              The Amazon S3 backup mode.

            - **S3BackupDescription** *(dict) --*

              The configuration for backup in Amazon S3.

              - **RoleARN** *(string) --*

                The Amazon Resource Name (ARN) of the AWS credentials. For more information, see
                `Amazon Resource Names (ARNs) and AWS Service Namespaces
                <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

              - **BucketARN** *(string) --*

                The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs)
                and AWS Service Namespaces
                <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

              - **Prefix** *(string) --*

                The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered Amazon
                S3 files. You can also specify a custom prefix, as described in `Custom Prefixes
                for Amazon S3 Objects
                <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

              - **ErrorOutputPrefix** *(string) --*

                A prefix that Kinesis Data Firehose evaluates and adds to failed records before
                writing them to S3. This prefix appears immediately following the bucket name. For
                information about how to specify this prefix, see `Custom Prefixes for Amazon S3
                Objects <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

              - **BufferingHints** *(dict) --*

                The buffering option. If no value is specified, ``BufferingHints`` object default
                values are used.

                - **SizeInMBs** *(integer) --*

                  Buffer incoming data to the specified size, in MiBs, before delivering it to the
                  destination. The default value is 5. This parameter is optional but if you
                  specify a value for it, you must also specify a value for ``IntervalInSeconds`` ,
                  and vice versa.

                  We recommend setting this parameter to a value greater than the amount of data
                  you typically ingest into the delivery stream in 10 seconds. For example, if you
                  typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

                - **IntervalInSeconds** *(integer) --*

                  Buffer incoming data for the specified period of time, in seconds, before
                  delivering it to the destination. The default value is 300. This parameter is
                  optional but if you specify a value for it, you must also specify a value for
                  ``SizeInMBs`` , and vice versa.

              - **CompressionFormat** *(string) --*

                The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .

              - **EncryptionConfiguration** *(dict) --*

                The encryption configuration. If no value is specified, the default is no
                encryption.

                - **NoEncryptionConfig** *(string) --*

                  Specifically override existing encryption information to ensure that no
                  encryption is used.

                - **KMSEncryptionConfig** *(dict) --*

                  The encryption key.

                  - **AWSKMSKeyARN** *(string) --*

                    The Amazon Resource Name (ARN) of the encryption key. Must belong to the same
                    AWS Region as the destination Amazon S3 bucket. For more information, see
                    `Amazon Resource Names (ARNs) and AWS Service Namespaces
                    <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__
                    .

              - **CloudWatchLoggingOptions** *(dict) --*

                The Amazon CloudWatch logging options for your delivery stream.

                - **Enabled** *(boolean) --*

                  Enables or disables CloudWatch logging.

                - **LogGroupName** *(string) --*

                  The CloudWatch group name for logging. This value is required if CloudWatch
                  logging is enabled.

                - **LogStreamName** *(string) --*

                  The CloudWatch log stream name for logging. This value is required if CloudWatch
                  logging is enabled.

            - **DataFormatConversionConfiguration** *(dict) --*

              The serializer, deserializer, and schema for converting data from the JSON format to
              the Parquet or ORC format before writing it to Amazon S3.

              - **SchemaConfiguration** *(dict) --*

                Specifies the AWS Glue Data Catalog table that contains the column information.

                - **RoleARN** *(string) --*

                  The role that Kinesis Data Firehose can use to access AWS Glue. This role must be
                  in the same account you use for Kinesis Data Firehose. Cross-account roles aren't
                  allowed.

                - **CatalogId** *(string) --*

                  The ID of the AWS Glue Data Catalog. If you don't supply this, the AWS account ID
                  is used by default.

                - **DatabaseName** *(string) --*

                  Specifies the name of the AWS Glue database that contains the schema for the
                  output data.

                - **TableName** *(string) --*

                  Specifies the AWS Glue table that contains the column information that
                  constitutes your data schema.

                - **Region** *(string) --*

                  If you don't specify an AWS Region, the default is the current Region.

                - **VersionId** *(string) --*

                  Specifies the table version for the output data schema. If you don't specify this
                  version ID, or if you set it to ``LATEST`` , Kinesis Data Firehose uses the most
                  recent version. This means that any updates to the table are automatically picked
                  up.

              - **InputFormatConfiguration** *(dict) --*

                Specifies the deserializer that you want Kinesis Data Firehose to use to convert
                the format of your data from JSON.

                - **Deserializer** *(dict) --*

                  Specifies which deserializer to use. You can choose either the Apache Hive JSON
                  SerDe or the OpenX JSON SerDe. If both are non-null, the server rejects the
                  request.

                  - **OpenXJsonSerDe** *(dict) --*

                    The OpenX SerDe. Used by Kinesis Data Firehose for deserializing data, which
                    means converting it from the JSON format in preparation for serializing it to
                    the Parquet or ORC format. This is one of two deserializers you can choose,
                    depending on which one offers the functionality you need. The other option is
                    the native Hive / HCatalog JsonSerDe.

                    - **ConvertDotsInJsonKeysToUnderscores** *(boolean) --*

                      When set to ``true`` , specifies that the names of the keys include dots and
                      that you want Kinesis Data Firehose to replace them with underscores. This is
                      useful because Apache Hive does not allow dots in column names. For example,
                      if the JSON contains a key whose name is "a.b", you can define the column
                      name to be "a_b" when using this option.

                      The default is ``false`` .

                    - **CaseInsensitive** *(boolean) --*

                      When set to ``true`` , which is the default, Kinesis Data Firehose converts
                      JSON keys to lowercase before deserializing them.

                    - **ColumnToJsonKeyMappings** *(dict) --*

                      Maps column names to JSON keys that aren't identical to the column names.
                      This is useful when the JSON contains keys that are Hive keywords. For
                      example, ``timestamp`` is a Hive keyword. If you have a JSON key named
                      ``timestamp`` , set this parameter to ``{"ts": "timestamp"}`` to map this key
                      to a column named ``ts`` .

                      - *(string) --*

                        - *(string) --*

                  - **HiveJsonSerDe** *(dict) --*

                    The native Hive / HCatalog JsonSerDe. Used by Kinesis Data Firehose for
                    deserializing data, which means converting it from the JSON format in
                    preparation for serializing it to the Parquet or ORC format. This is one of two
                    deserializers you can choose, depending on which one offers the functionality
                    you need. The other option is the OpenX SerDe.

                    - **TimestampFormats** *(list) --*

                      Indicates how you want Kinesis Data Firehose to parse the date and timestamps
                      that may be present in your input data JSON. To specify these format strings,
                      follow the pattern syntax of JodaTime's DateTimeFormat format strings. For
                      more information, see `Class DateTimeFormat
                      <https://www.joda.org/joda-time/apidocs/org/joda/time/format/DateTimeFormat.html>`__
                      . You can also use the special value ``millis`` to parse timestamps in epoch
                      milliseconds. If you don't specify a format, Kinesis Data Firehose uses
                      ``java.sql.Timestamp::valueOf`` by default.

                      - *(string) --*

              - **OutputFormatConfiguration** *(dict) --*

                Specifies the serializer that you want Kinesis Data Firehose to use to convert the
                format of your data to the Parquet or ORC format.

                - **Serializer** *(dict) --*

                  Specifies which serializer to use. You can choose either the ORC SerDe or the
                  Parquet SerDe. If both are non-null, the server rejects the request.

                  - **ParquetSerDe** *(dict) --*

                    A serializer to use for converting data to the Parquet format before storing it
                    in Amazon S3. For more information, see `Apache Parquet
                    <https://parquet.apache.org/documentation/latest/>`__ .

                    - **BlockSizeBytes** *(integer) --*

                      The Hadoop Distributed File System (HDFS) block size. This is useful if you
                      intend to copy the data from Amazon S3 to HDFS before querying. The default
                      is 256 MiB and the minimum is 64 MiB. Kinesis Data Firehose uses this value
                      for padding calculations.

                    - **PageSizeBytes** *(integer) --*

                      The Parquet page size. Column chunks are divided into pages. A page is
                      conceptually an indivisible unit (in terms of compression and encoding). The
                      minimum value is 64 KiB and the default is 1 MiB.

                    - **Compression** *(string) --*

                      The compression code to use over data blocks. The possible values are
                      ``UNCOMPRESSED`` , ``SNAPPY`` , and ``GZIP`` , with the default being
                      ``SNAPPY`` . Use ``SNAPPY`` for higher decompression speed. Use ``GZIP`` if
                      the compression ration is more important than speed.

                    - **EnableDictionaryCompression** *(boolean) --*

                      Indicates whether to enable dictionary compression.

                    - **MaxPaddingBytes** *(integer) --*

                      The maximum amount of padding to apply. This is useful if you intend to copy
                      the data from Amazon S3 to HDFS before querying. The default is 0.

                    - **WriterVersion** *(string) --*

                      Indicates the version of row format to output. The possible values are ``V1``
                      and ``V2`` . The default is ``V1`` .

                  - **OrcSerDe** *(dict) --*

                    A serializer to use for converting data to the ORC format before storing it in
                    Amazon S3. For more information, see `Apache ORC
                    <https://orc.apache.org/docs/>`__ .

                    - **StripeSizeBytes** *(integer) --*

                      The number of bytes in each stripe. The default is 64 MiB and the minimum is
                      8 MiB.

                    - **BlockSizeBytes** *(integer) --*

                      The Hadoop Distributed File System (HDFS) block size. This is useful if you
                      intend to copy the data from Amazon S3 to HDFS before querying. The default
                      is 256 MiB and the minimum is 64 MiB. Kinesis Data Firehose uses this value
                      for padding calculations.

                    - **RowIndexStride** *(integer) --*

                      The number of rows between index entries. The default is 10,000 and the
                      minimum is 1,000.

                    - **EnablePadding** *(boolean) --*

                      Set this to ``true`` to indicate that you want stripes to be padded to the
                      HDFS block boundaries. This is useful if you intend to copy the data from
                      Amazon S3 to HDFS before querying. The default is ``false`` .

                    - **PaddingTolerance** *(float) --*

                      A number between 0 and 1 that defines the tolerance for block padding as a
                      decimal fraction of stripe size. The default value is 0.05, which means 5
                      percent of stripe size.

                      For the default values of 64 MiB ORC stripes and 256 MiB HDFS blocks, the
                      default block padding tolerance of 5 percent reserves a maximum of 3.2 MiB
                      for padding within the 256 MiB block. In such a case, if the available size
                      within the block is more than 3.2 MiB, a new, smaller stripe is inserted to
                      fit within that space. This ensures that no stripe crosses block boundaries
                      and causes remote reads within a node-local task.

                      Kinesis Data Firehose ignores this parameter when  OrcSerDe$EnablePadding is
                      ``false`` .

                    - **Compression** *(string) --*

                      The compression code to use over data blocks. The default is ``SNAPPY`` .

                    - **BloomFilterColumns** *(list) --*

                      The column names for which you want Kinesis Data Firehose to create bloom
                      filters. The default is ``null`` .

                      - *(string) --*

                    - **BloomFilterFalsePositiveProbability** *(float) --*

                      The Bloom filter false positive probability (FPP). The lower the FPP, the
                      bigger the Bloom filter. The default value is 0.05, the minimum is 0, and the
                      maximum is 1.

                    - **DictionaryKeyThreshold** *(float) --*

                      Represents the fraction of the total number of non-null rows. To turn off
                      dictionary encoding, set this fraction to a number that is less than the
                      number of distinct keys in a dictionary. To always use dictionary encoding,
                      set this threshold to 1.

                    - **FormatVersion** *(string) --*

                      The version of the file to write. The possible values are ``V0_11`` and
                      ``V0_12`` . The default is ``V0_12`` .

              - **Enabled** *(boolean) --*

                Defaults to ``true`` . Set it to ``false`` if you want to disable format conversion
                while preserving the configuration details.

          - **RedshiftDestinationDescription** *(dict) --*

            The destination in Amazon Redshift.

            - **RoleARN** *(string) --*

              The Amazon Resource Name (ARN) of the AWS credentials. For more information, see
              `Amazon Resource Names (ARNs) and AWS Service Namespaces
              <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

            - **ClusterJDBCURL** *(string) --*

              The database connection string.

            - **CopyCommand** *(dict) --*

              The ``COPY`` command.

              - **DataTableName** *(string) --*

                The name of the target table. The table must already exist in the database.

              - **DataTableColumns** *(string) --*

                A comma-separated list of column names.

              - **CopyOptions** *(string) --*

                Optional parameters to use with the Amazon Redshift ``COPY`` command. For more
                information, see the "Optional Parameters" section of `Amazon Redshift COPY command
                <https://docs.aws.amazon.com/redshift/latest/dg/r_COPY.html>`__ . Some possible
                examples that would apply to Kinesis Data Firehose are as follows:

                 ``delimiter '\\t' lzop;`` - fields are delimited with "\\t" (TAB character) and
                 compressed using lzop.

                 ``delimiter '|'`` - fields are delimited with "|" (this is the default delimiter).

                 ``delimiter '|' escape`` - the delimiter should be escaped.

                 ``fixedwidth 'venueid:3,venuename:25,venuecity:12,venuestate:2,venueseats:6'`` -
                 fields are fixed width in the source, with each width specified after every column
                 in the table.

                 ``JSON 's3://mybucket/jsonpaths.txt'`` - data is in JSON format, and the path
                 specified is the format of the data.

                For more examples, see `Amazon Redshift COPY command examples
                <https://docs.aws.amazon.com/redshift/latest/dg/r_COPY_command_examples.html>`__ .

            - **Username** *(string) --*

              The name of the user.

            - **RetryOptions** *(dict) --*

              The retry behavior in case Kinesis Data Firehose is unable to deliver documents to
              Amazon Redshift. Default value is 3600 (60 minutes).

              - **DurationInSeconds** *(integer) --*

                The length of time during which Kinesis Data Firehose retries delivery after a
                failure, starting from the initial request and including the first attempt. The
                default value is 3600 seconds (60 minutes). Kinesis Data Firehose does not retry if
                the value of ``DurationInSeconds`` is 0 (zero) or if the first delivery attempt
                takes longer than the current value.

            - **S3DestinationDescription** *(dict) --*

              The Amazon S3 destination.

              - **RoleARN** *(string) --*

                The Amazon Resource Name (ARN) of the AWS credentials. For more information, see
                `Amazon Resource Names (ARNs) and AWS Service Namespaces
                <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

              - **BucketARN** *(string) --*

                The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs)
                and AWS Service Namespaces
                <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

              - **Prefix** *(string) --*

                The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered Amazon
                S3 files. You can also specify a custom prefix, as described in `Custom Prefixes
                for Amazon S3 Objects
                <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

              - **ErrorOutputPrefix** *(string) --*

                A prefix that Kinesis Data Firehose evaluates and adds to failed records before
                writing them to S3. This prefix appears immediately following the bucket name. For
                information about how to specify this prefix, see `Custom Prefixes for Amazon S3
                Objects <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

              - **BufferingHints** *(dict) --*

                The buffering option. If no value is specified, ``BufferingHints`` object default
                values are used.

                - **SizeInMBs** *(integer) --*

                  Buffer incoming data to the specified size, in MiBs, before delivering it to the
                  destination. The default value is 5. This parameter is optional but if you
                  specify a value for it, you must also specify a value for ``IntervalInSeconds`` ,
                  and vice versa.

                  We recommend setting this parameter to a value greater than the amount of data
                  you typically ingest into the delivery stream in 10 seconds. For example, if you
                  typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

                - **IntervalInSeconds** *(integer) --*

                  Buffer incoming data for the specified period of time, in seconds, before
                  delivering it to the destination. The default value is 300. This parameter is
                  optional but if you specify a value for it, you must also specify a value for
                  ``SizeInMBs`` , and vice versa.

              - **CompressionFormat** *(string) --*

                The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .

              - **EncryptionConfiguration** *(dict) --*

                The encryption configuration. If no value is specified, the default is no
                encryption.

                - **NoEncryptionConfig** *(string) --*

                  Specifically override existing encryption information to ensure that no
                  encryption is used.

                - **KMSEncryptionConfig** *(dict) --*

                  The encryption key.

                  - **AWSKMSKeyARN** *(string) --*

                    The Amazon Resource Name (ARN) of the encryption key. Must belong to the same
                    AWS Region as the destination Amazon S3 bucket. For more information, see
                    `Amazon Resource Names (ARNs) and AWS Service Namespaces
                    <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__
                    .

              - **CloudWatchLoggingOptions** *(dict) --*

                The Amazon CloudWatch logging options for your delivery stream.

                - **Enabled** *(boolean) --*

                  Enables or disables CloudWatch logging.

                - **LogGroupName** *(string) --*

                  The CloudWatch group name for logging. This value is required if CloudWatch
                  logging is enabled.

                - **LogStreamName** *(string) --*

                  The CloudWatch log stream name for logging. This value is required if CloudWatch
                  logging is enabled.

            - **ProcessingConfiguration** *(dict) --*

              The data processing configuration.

              - **Enabled** *(boolean) --*

                Enables or disables data processing.

              - **Processors** *(list) --*

                The data processors.

                - *(dict) --*

                  Describes a data processor.

                  - **Type** *(string) --*

                    The type of processor.

                  - **Parameters** *(list) --*

                    The processor parameters.

                    - *(dict) --*

                      Describes the processor parameter.

                      - **ParameterName** *(string) --*

                        The name of the parameter.

                      - **ParameterValue** *(string) --*

                        The parameter value.

            - **S3BackupMode** *(string) --*

              The Amazon S3 backup mode.

            - **S3BackupDescription** *(dict) --*

              The configuration for backup in Amazon S3.

              - **RoleARN** *(string) --*

                The Amazon Resource Name (ARN) of the AWS credentials. For more information, see
                `Amazon Resource Names (ARNs) and AWS Service Namespaces
                <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

              - **BucketARN** *(string) --*

                The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs)
                and AWS Service Namespaces
                <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

              - **Prefix** *(string) --*

                The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered Amazon
                S3 files. You can also specify a custom prefix, as described in `Custom Prefixes
                for Amazon S3 Objects
                <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

              - **ErrorOutputPrefix** *(string) --*

                A prefix that Kinesis Data Firehose evaluates and adds to failed records before
                writing them to S3. This prefix appears immediately following the bucket name. For
                information about how to specify this prefix, see `Custom Prefixes for Amazon S3
                Objects <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

              - **BufferingHints** *(dict) --*

                The buffering option. If no value is specified, ``BufferingHints`` object default
                values are used.

                - **SizeInMBs** *(integer) --*

                  Buffer incoming data to the specified size, in MiBs, before delivering it to the
                  destination. The default value is 5. This parameter is optional but if you
                  specify a value for it, you must also specify a value for ``IntervalInSeconds`` ,
                  and vice versa.

                  We recommend setting this parameter to a value greater than the amount of data
                  you typically ingest into the delivery stream in 10 seconds. For example, if you
                  typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

                - **IntervalInSeconds** *(integer) --*

                  Buffer incoming data for the specified period of time, in seconds, before
                  delivering it to the destination. The default value is 300. This parameter is
                  optional but if you specify a value for it, you must also specify a value for
                  ``SizeInMBs`` , and vice versa.

              - **CompressionFormat** *(string) --*

                The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .

              - **EncryptionConfiguration** *(dict) --*

                The encryption configuration. If no value is specified, the default is no
                encryption.

                - **NoEncryptionConfig** *(string) --*

                  Specifically override existing encryption information to ensure that no
                  encryption is used.

                - **KMSEncryptionConfig** *(dict) --*

                  The encryption key.

                  - **AWSKMSKeyARN** *(string) --*

                    The Amazon Resource Name (ARN) of the encryption key. Must belong to the same
                    AWS Region as the destination Amazon S3 bucket. For more information, see
                    `Amazon Resource Names (ARNs) and AWS Service Namespaces
                    <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__
                    .

              - **CloudWatchLoggingOptions** *(dict) --*

                The Amazon CloudWatch logging options for your delivery stream.

                - **Enabled** *(boolean) --*

                  Enables or disables CloudWatch logging.

                - **LogGroupName** *(string) --*

                  The CloudWatch group name for logging. This value is required if CloudWatch
                  logging is enabled.

                - **LogStreamName** *(string) --*

                  The CloudWatch log stream name for logging. This value is required if CloudWatch
                  logging is enabled.

            - **CloudWatchLoggingOptions** *(dict) --*

              The Amazon CloudWatch logging options for your delivery stream.

              - **Enabled** *(boolean) --*

                Enables or disables CloudWatch logging.

              - **LogGroupName** *(string) --*

                The CloudWatch group name for logging. This value is required if CloudWatch logging
                is enabled.

              - **LogStreamName** *(string) --*

                The CloudWatch log stream name for logging. This value is required if CloudWatch
                logging is enabled.

          - **ElasticsearchDestinationDescription** *(dict) --*

            The destination in Amazon ES.

            - **RoleARN** *(string) --*

              The Amazon Resource Name (ARN) of the AWS credentials. For more information, see
              `Amazon Resource Names (ARNs) and AWS Service Namespaces
              <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

            - **DomainARN** *(string) --*

              The ARN of the Amazon ES domain. For more information, see `Amazon Resource Names
              (ARNs) and AWS Service Namespaces
              <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

              Kinesis Data Firehose uses either ``ClusterEndpoint`` or ``DomainARN`` to send data
              to Amazon ES.

            - **ClusterEndpoint** *(string) --*

              The endpoint to use when communicating with the cluster. Kinesis Data Firehose uses
              either this ``ClusterEndpoint`` or the ``DomainARN`` field to send data to Amazon ES.

            - **IndexName** *(string) --*

              The Elasticsearch index name.

            - **TypeName** *(string) --*

              The Elasticsearch type name. This applies to Elasticsearch 6.x and lower versions.
              For Elasticsearch 7.x, there's no value for ``TypeName`` .

            - **IndexRotationPeriod** *(string) --*

              The Elasticsearch index rotation period

            - **BufferingHints** *(dict) --*

              The buffering options.

              - **IntervalInSeconds** *(integer) --*

                Buffer incoming data for the specified period of time, in seconds, before
                delivering it to the destination. The default value is 300 (5 minutes).

              - **SizeInMBs** *(integer) --*

                Buffer incoming data to the specified size, in MBs, before delivering it to the
                destination. The default value is 5.

                We recommend setting this parameter to a value greater than the amount of data you
                typically ingest into the delivery stream in 10 seconds. For example, if you
                typically ingest data at 1 MB/sec, the value should be 10 MB or higher.

            - **RetryOptions** *(dict) --*

              The Amazon ES retry options.

              - **DurationInSeconds** *(integer) --*

                After an initial failure to deliver to Amazon ES, the total amount of time during
                which Kinesis Data Firehose retries delivery (including the first attempt). After
                this time has elapsed, the failed documents are written to Amazon S3. Default value
                is 300 seconds (5 minutes). A value of 0 (zero) results in no retries.

            - **S3BackupMode** *(string) --*

              The Amazon S3 backup mode.

            - **S3DestinationDescription** *(dict) --*

              The Amazon S3 destination.

              - **RoleARN** *(string) --*

                The Amazon Resource Name (ARN) of the AWS credentials. For more information, see
                `Amazon Resource Names (ARNs) and AWS Service Namespaces
                <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

              - **BucketARN** *(string) --*

                The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs)
                and AWS Service Namespaces
                <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

              - **Prefix** *(string) --*

                The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered Amazon
                S3 files. You can also specify a custom prefix, as described in `Custom Prefixes
                for Amazon S3 Objects
                <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

              - **ErrorOutputPrefix** *(string) --*

                A prefix that Kinesis Data Firehose evaluates and adds to failed records before
                writing them to S3. This prefix appears immediately following the bucket name. For
                information about how to specify this prefix, see `Custom Prefixes for Amazon S3
                Objects <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

              - **BufferingHints** *(dict) --*

                The buffering option. If no value is specified, ``BufferingHints`` object default
                values are used.

                - **SizeInMBs** *(integer) --*

                  Buffer incoming data to the specified size, in MiBs, before delivering it to the
                  destination. The default value is 5. This parameter is optional but if you
                  specify a value for it, you must also specify a value for ``IntervalInSeconds`` ,
                  and vice versa.

                  We recommend setting this parameter to a value greater than the amount of data
                  you typically ingest into the delivery stream in 10 seconds. For example, if you
                  typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

                - **IntervalInSeconds** *(integer) --*

                  Buffer incoming data for the specified period of time, in seconds, before
                  delivering it to the destination. The default value is 300. This parameter is
                  optional but if you specify a value for it, you must also specify a value for
                  ``SizeInMBs`` , and vice versa.

              - **CompressionFormat** *(string) --*

                The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .

              - **EncryptionConfiguration** *(dict) --*

                The encryption configuration. If no value is specified, the default is no
                encryption.

                - **NoEncryptionConfig** *(string) --*

                  Specifically override existing encryption information to ensure that no
                  encryption is used.

                - **KMSEncryptionConfig** *(dict) --*

                  The encryption key.

                  - **AWSKMSKeyARN** *(string) --*

                    The Amazon Resource Name (ARN) of the encryption key. Must belong to the same
                    AWS Region as the destination Amazon S3 bucket. For more information, see
                    `Amazon Resource Names (ARNs) and AWS Service Namespaces
                    <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__
                    .

              - **CloudWatchLoggingOptions** *(dict) --*

                The Amazon CloudWatch logging options for your delivery stream.

                - **Enabled** *(boolean) --*

                  Enables or disables CloudWatch logging.

                - **LogGroupName** *(string) --*

                  The CloudWatch group name for logging. This value is required if CloudWatch
                  logging is enabled.

                - **LogStreamName** *(string) --*

                  The CloudWatch log stream name for logging. This value is required if CloudWatch
                  logging is enabled.

            - **ProcessingConfiguration** *(dict) --*

              The data processing configuration.

              - **Enabled** *(boolean) --*

                Enables or disables data processing.

              - **Processors** *(list) --*

                The data processors.

                - *(dict) --*

                  Describes a data processor.

                  - **Type** *(string) --*

                    The type of processor.

                  - **Parameters** *(list) --*

                    The processor parameters.

                    - *(dict) --*

                      Describes the processor parameter.

                      - **ParameterName** *(string) --*

                        The name of the parameter.

                      - **ParameterValue** *(string) --*

                        The parameter value.

            - **CloudWatchLoggingOptions** *(dict) --*

              The Amazon CloudWatch logging options.

              - **Enabled** *(boolean) --*

                Enables or disables CloudWatch logging.

              - **LogGroupName** *(string) --*

                The CloudWatch group name for logging. This value is required if CloudWatch logging
                is enabled.

              - **LogStreamName** *(string) --*

                The CloudWatch log stream name for logging. This value is required if CloudWatch
                logging is enabled.

          - **SplunkDestinationDescription** *(dict) --*

            The destination in Splunk.

            - **HECEndpoint** *(string) --*

              The HTTP Event Collector (HEC) endpoint to which Kinesis Data Firehose sends your
              data.

            - **HECEndpointType** *(string) --*

              This type can be either "Raw" or "Event."

            - **HECToken** *(string) --*

              A GUID you obtain from your Splunk cluster when you create a new HEC endpoint.

            - **HECAcknowledgmentTimeoutInSeconds** *(integer) --*

              The amount of time that Kinesis Data Firehose waits to receive an acknowledgment from
              Splunk after it sends it data. At the end of the timeout period, Kinesis Data
              Firehose either tries to send the data again or considers it an error, based on your
              retry settings.

            - **RetryOptions** *(dict) --*

              The retry behavior in case Kinesis Data Firehose is unable to deliver data to Splunk
              or if it doesn't receive an acknowledgment of receipt from Splunk.

              - **DurationInSeconds** *(integer) --*

                The total amount of time that Kinesis Data Firehose spends on retries. This
                duration starts after the initial attempt to send data to Splunk fails. It doesn't
                include the periods during which Kinesis Data Firehose waits for acknowledgment
                from Splunk after each attempt.

            - **S3BackupMode** *(string) --*

              Defines how documents should be delivered to Amazon S3. When set to
              ``FailedDocumentsOnly`` , Kinesis Data Firehose writes any data that could not be
              indexed to the configured Amazon S3 destination. When set to ``AllDocuments`` ,
              Kinesis Data Firehose delivers all incoming records to Amazon S3, and also writes
              failed documents to Amazon S3. Default value is ``FailedDocumentsOnly`` .

            - **S3DestinationDescription** *(dict) --*

              The Amazon S3 destination.>

              - **RoleARN** *(string) --*

                The Amazon Resource Name (ARN) of the AWS credentials. For more information, see
                `Amazon Resource Names (ARNs) and AWS Service Namespaces
                <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

              - **BucketARN** *(string) --*

                The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs)
                and AWS Service Namespaces
                <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

              - **Prefix** *(string) --*

                The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered Amazon
                S3 files. You can also specify a custom prefix, as described in `Custom Prefixes
                for Amazon S3 Objects
                <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

              - **ErrorOutputPrefix** *(string) --*

                A prefix that Kinesis Data Firehose evaluates and adds to failed records before
                writing them to S3. This prefix appears immediately following the bucket name. For
                information about how to specify this prefix, see `Custom Prefixes for Amazon S3
                Objects <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

              - **BufferingHints** *(dict) --*

                The buffering option. If no value is specified, ``BufferingHints`` object default
                values are used.

                - **SizeInMBs** *(integer) --*

                  Buffer incoming data to the specified size, in MiBs, before delivering it to the
                  destination. The default value is 5. This parameter is optional but if you
                  specify a value for it, you must also specify a value for ``IntervalInSeconds`` ,
                  and vice versa.

                  We recommend setting this parameter to a value greater than the amount of data
                  you typically ingest into the delivery stream in 10 seconds. For example, if you
                  typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

                - **IntervalInSeconds** *(integer) --*

                  Buffer incoming data for the specified period of time, in seconds, before
                  delivering it to the destination. The default value is 300. This parameter is
                  optional but if you specify a value for it, you must also specify a value for
                  ``SizeInMBs`` , and vice versa.

              - **CompressionFormat** *(string) --*

                The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .

              - **EncryptionConfiguration** *(dict) --*

                The encryption configuration. If no value is specified, the default is no
                encryption.

                - **NoEncryptionConfig** *(string) --*

                  Specifically override existing encryption information to ensure that no
                  encryption is used.

                - **KMSEncryptionConfig** *(dict) --*

                  The encryption key.

                  - **AWSKMSKeyARN** *(string) --*

                    The Amazon Resource Name (ARN) of the encryption key. Must belong to the same
                    AWS Region as the destination Amazon S3 bucket. For more information, see
                    `Amazon Resource Names (ARNs) and AWS Service Namespaces
                    <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__
                    .

              - **CloudWatchLoggingOptions** *(dict) --*

                The Amazon CloudWatch logging options for your delivery stream.

                - **Enabled** *(boolean) --*

                  Enables or disables CloudWatch logging.

                - **LogGroupName** *(string) --*

                  The CloudWatch group name for logging. This value is required if CloudWatch
                  logging is enabled.

                - **LogStreamName** *(string) --*

                  The CloudWatch log stream name for logging. This value is required if CloudWatch
                  logging is enabled.

            - **ProcessingConfiguration** *(dict) --*

              The data processing configuration.

              - **Enabled** *(boolean) --*

                Enables or disables data processing.

              - **Processors** *(list) --*

                The data processors.

                - *(dict) --*

                  Describes a data processor.

                  - **Type** *(string) --*

                    The type of processor.

                  - **Parameters** *(list) --*

                    The processor parameters.

                    - *(dict) --*

                      Describes the processor parameter.

                      - **ParameterName** *(string) --*

                        The name of the parameter.

                      - **ParameterValue** *(string) --*

                        The parameter value.

            - **CloudWatchLoggingOptions** *(dict) --*

              The Amazon CloudWatch logging options for your delivery stream.

              - **Enabled** *(boolean) --*

                Enables or disables CloudWatch logging.

              - **LogGroupName** *(string) --*

                The CloudWatch group name for logging. This value is required if CloudWatch logging
                is enabled.

              - **LogStreamName** *(string) --*

                The CloudWatch log stream name for logging. This value is required if CloudWatch
                logging is enabled.

      - **HasMoreDestinations** *(boolean) --*

        Indicates whether there are more destinations available to list.
    """


_ClientListDeliveryStreamsResponseTypeDef = TypedDict(
    "_ClientListDeliveryStreamsResponseTypeDef",
    {"DeliveryStreamNames": List[str], "HasMoreDeliveryStreams": bool},
    total=False,
)


class ClientListDeliveryStreamsResponseTypeDef(
    _ClientListDeliveryStreamsResponseTypeDef
):
    """
    Type definition for `ClientListDeliveryStreams` `Response`

    - **DeliveryStreamNames** *(list) --*

      The names of the delivery streams.

      - *(string) --*

    - **HasMoreDeliveryStreams** *(boolean) --*

      Indicates whether there are more delivery streams available to list.
    """


_ClientListTagsForDeliveryStreamResponseTagsTypeDef = TypedDict(
    "_ClientListTagsForDeliveryStreamResponseTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientListTagsForDeliveryStreamResponseTagsTypeDef(
    _ClientListTagsForDeliveryStreamResponseTagsTypeDef
):
    """
    Type definition for `ClientListTagsForDeliveryStreamResponse` `Tags`

    Metadata that you can assign to a delivery stream, consisting of a key-value pair.

    - **Key** *(string) --*

      A unique identifier for the tag. Maximum length: 128 characters. Valid characters:
      Unicode letters, digits, white space, _ . / = + - % @

    - **Value** *(string) --*

      An optional string, which you can use to describe or define the tag. Maximum length: 256
      characters. Valid characters: Unicode letters, digits, white space, _ . / = + - % @
    """


_ClientListTagsForDeliveryStreamResponseTypeDef = TypedDict(
    "_ClientListTagsForDeliveryStreamResponseTypeDef",
    {
        "Tags": List[ClientListTagsForDeliveryStreamResponseTagsTypeDef],
        "HasMoreTags": bool,
    },
    total=False,
)


class ClientListTagsForDeliveryStreamResponseTypeDef(
    _ClientListTagsForDeliveryStreamResponseTypeDef
):
    """
    Type definition for `ClientListTagsForDeliveryStream` `Response`

    - **Tags** *(list) --*

      A list of tags associated with ``DeliveryStreamName`` , starting with the first tag after
      ``ExclusiveStartTagKey`` and up to the specified ``Limit`` .

      - *(dict) --*

        Metadata that you can assign to a delivery stream, consisting of a key-value pair.

        - **Key** *(string) --*

          A unique identifier for the tag. Maximum length: 128 characters. Valid characters:
          Unicode letters, digits, white space, _ . / = + - % @

        - **Value** *(string) --*

          An optional string, which you can use to describe or define the tag. Maximum length: 256
          characters. Valid characters: Unicode letters, digits, white space, _ . / = + - % @

    - **HasMoreTags** *(boolean) --*

      If this is ``true`` in the response, more tags are available. To list the remaining tags, set
      ``ExclusiveStartTagKey`` to the key of the last tag returned and call
      ``ListTagsForDeliveryStream`` again.
    """


_ClientPutRecordBatchRecordsTypeDef = TypedDict(
    "_ClientPutRecordBatchRecordsTypeDef", {"Data": bytes}
)


class ClientPutRecordBatchRecordsTypeDef(_ClientPutRecordBatchRecordsTypeDef):
    """
    Type definition for `ClientPutRecordBatch` `Records`

    The unit of data in a delivery stream.

    - **Data** *(bytes) --* **[REQUIRED]**

      The data blob, which is base64-encoded when the blob is serialized. The maximum size of the
      data blob, before base64-encoding, is 1,000 KiB.
    """


_ClientPutRecordBatchResponseRequestResponsesTypeDef = TypedDict(
    "_ClientPutRecordBatchResponseRequestResponsesTypeDef",
    {"RecordId": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class ClientPutRecordBatchResponseRequestResponsesTypeDef(
    _ClientPutRecordBatchResponseRequestResponsesTypeDef
):
    """
    Type definition for `ClientPutRecordBatchResponse` `RequestResponses`

    Contains the result for an individual record from a  PutRecordBatch request. If the record
    is successfully added to your delivery stream, it receives a record ID. If the record fails
    to be added to your delivery stream, the result includes an error code and an error message.

    - **RecordId** *(string) --*

      The ID of the record.

    - **ErrorCode** *(string) --*

      The error code for an individual record result.

    - **ErrorMessage** *(string) --*

      The error message for an individual record result.
    """


_ClientPutRecordBatchResponseTypeDef = TypedDict(
    "_ClientPutRecordBatchResponseTypeDef",
    {
        "FailedPutCount": int,
        "Encrypted": bool,
        "RequestResponses": List[ClientPutRecordBatchResponseRequestResponsesTypeDef],
    },
    total=False,
)


class ClientPutRecordBatchResponseTypeDef(_ClientPutRecordBatchResponseTypeDef):
    """
    Type definition for `ClientPutRecordBatch` `Response`

    - **FailedPutCount** *(integer) --*

      The number of records that might have failed processing. This number might be greater than 0
      even if the  PutRecordBatch call succeeds. Check ``FailedPutCount`` to determine whether
      there are records that you need to resend.

    - **Encrypted** *(boolean) --*

      Indicates whether server-side encryption (SSE) was enabled during this operation.

    - **RequestResponses** *(list) --*

      The results array. For each record, the index of the response element is the same as the
      index used in the request array.

      - *(dict) --*

        Contains the result for an individual record from a  PutRecordBatch request. If the record
        is successfully added to your delivery stream, it receives a record ID. If the record fails
        to be added to your delivery stream, the result includes an error code and an error message.

        - **RecordId** *(string) --*

          The ID of the record.

        - **ErrorCode** *(string) --*

          The error code for an individual record result.

        - **ErrorMessage** *(string) --*

          The error message for an individual record result.
    """


_ClientPutRecordRecordTypeDef = TypedDict(
    "_ClientPutRecordRecordTypeDef", {"Data": bytes}
)


class ClientPutRecordRecordTypeDef(_ClientPutRecordRecordTypeDef):
    """
    Type definition for `ClientPutRecord` `Record`

    The record.

    - **Data** *(bytes) --* **[REQUIRED]**

      The data blob, which is base64-encoded when the blob is serialized. The maximum size of the
      data blob, before base64-encoding, is 1,000 KiB.
    """


_ClientPutRecordResponseTypeDef = TypedDict(
    "_ClientPutRecordResponseTypeDef", {"RecordId": str, "Encrypted": bool}, total=False
)


class ClientPutRecordResponseTypeDef(_ClientPutRecordResponseTypeDef):
    """
    Type definition for `ClientPutRecord` `Response`

    - **RecordId** *(string) --*

      The ID of the record.

    - **Encrypted** *(boolean) --*

      Indicates whether server-side encryption (SSE) was enabled during this operation.
    """


_RequiredClientTagDeliveryStreamTagsTypeDef = TypedDict(
    "_RequiredClientTagDeliveryStreamTagsTypeDef", {"Key": str}
)
_OptionalClientTagDeliveryStreamTagsTypeDef = TypedDict(
    "_OptionalClientTagDeliveryStreamTagsTypeDef", {"Value": str}, total=False
)


class ClientTagDeliveryStreamTagsTypeDef(
    _RequiredClientTagDeliveryStreamTagsTypeDef,
    _OptionalClientTagDeliveryStreamTagsTypeDef,
):
    """
    Type definition for `ClientTagDeliveryStream` `Tags`

    Metadata that you can assign to a delivery stream, consisting of a key-value pair.

    - **Key** *(string) --* **[REQUIRED]**

      A unique identifier for the tag. Maximum length: 128 characters. Valid characters: Unicode
      letters, digits, white space, _ . / = + - % @

    - **Value** *(string) --*

      An optional string, which you can use to describe or define the tag. Maximum length: 256
      characters. Valid characters: Unicode letters, digits, white space, _ . / = + - % @
    """


_ClientUpdateDestinationElasticsearchDestinationUpdateBufferingHintsTypeDef = TypedDict(
    "_ClientUpdateDestinationElasticsearchDestinationUpdateBufferingHintsTypeDef",
    {"IntervalInSeconds": int, "SizeInMBs": int},
    total=False,
)


class ClientUpdateDestinationElasticsearchDestinationUpdateBufferingHintsTypeDef(
    _ClientUpdateDestinationElasticsearchDestinationUpdateBufferingHintsTypeDef
):
    """
    Type definition for `ClientUpdateDestinationElasticsearchDestinationUpdate` `BufferingHints`

    The buffering options. If no value is specified, ``ElasticsearchBufferingHints`` object default
    values are used.

    - **IntervalInSeconds** *(integer) --*

      Buffer incoming data for the specified period of time, in seconds, before delivering it to
      the destination. The default value is 300 (5 minutes).

    - **SizeInMBs** *(integer) --*

      Buffer incoming data to the specified size, in MBs, before delivering it to the destination.
      The default value is 5.

      We recommend setting this parameter to a value greater than the amount of data you typically
      ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1
      MB/sec, the value should be 10 MB or higher.
    """


_ClientUpdateDestinationElasticsearchDestinationUpdateCloudWatchLoggingOptionsTypeDef = TypedDict(
    "_ClientUpdateDestinationElasticsearchDestinationUpdateCloudWatchLoggingOptionsTypeDef",
    {"Enabled": bool, "LogGroupName": str, "LogStreamName": str},
    total=False,
)


class ClientUpdateDestinationElasticsearchDestinationUpdateCloudWatchLoggingOptionsTypeDef(
    _ClientUpdateDestinationElasticsearchDestinationUpdateCloudWatchLoggingOptionsTypeDef
):
    """
    Type definition for `ClientUpdateDestinationElasticsearchDestinationUpdate` `CloudWatchLoggingOptions`

    The CloudWatch logging options for your delivery stream.

    - **Enabled** *(boolean) --*

      Enables or disables CloudWatch logging.

    - **LogGroupName** *(string) --*

      The CloudWatch group name for logging. This value is required if CloudWatch logging is
      enabled.

    - **LogStreamName** *(string) --*

      The CloudWatch log stream name for logging. This value is required if CloudWatch logging is
      enabled.
    """


_ClientUpdateDestinationElasticsearchDestinationUpdateProcessingConfigurationProcessorsParametersTypeDef = TypedDict(
    "_ClientUpdateDestinationElasticsearchDestinationUpdateProcessingConfigurationProcessorsParametersTypeDef",
    {"ParameterName": str, "ParameterValue": str},
)


class ClientUpdateDestinationElasticsearchDestinationUpdateProcessingConfigurationProcessorsParametersTypeDef(
    _ClientUpdateDestinationElasticsearchDestinationUpdateProcessingConfigurationProcessorsParametersTypeDef
):
    """
    Type definition for `ClientUpdateDestinationElasticsearchDestinationUpdateProcessingConfigurationProcessors` `Parameters`

    Describes the processor parameter.

    - **ParameterName** *(string) --* **[REQUIRED]**

      The name of the parameter.

    - **ParameterValue** *(string) --* **[REQUIRED]**

      The parameter value.
    """


_RequiredClientUpdateDestinationElasticsearchDestinationUpdateProcessingConfigurationProcessorsTypeDef = TypedDict(
    "_RequiredClientUpdateDestinationElasticsearchDestinationUpdateProcessingConfigurationProcessorsTypeDef",
    {"Type": str},
)
_OptionalClientUpdateDestinationElasticsearchDestinationUpdateProcessingConfigurationProcessorsTypeDef = TypedDict(
    "_OptionalClientUpdateDestinationElasticsearchDestinationUpdateProcessingConfigurationProcessorsTypeDef",
    {
        "Parameters": List[
            ClientUpdateDestinationElasticsearchDestinationUpdateProcessingConfigurationProcessorsParametersTypeDef
        ]
    },
    total=False,
)


class ClientUpdateDestinationElasticsearchDestinationUpdateProcessingConfigurationProcessorsTypeDef(
    _RequiredClientUpdateDestinationElasticsearchDestinationUpdateProcessingConfigurationProcessorsTypeDef,
    _OptionalClientUpdateDestinationElasticsearchDestinationUpdateProcessingConfigurationProcessorsTypeDef,
):
    """
    Type definition for `ClientUpdateDestinationElasticsearchDestinationUpdateProcessingConfiguration` `Processors`

    Describes a data processor.

    - **Type** *(string) --* **[REQUIRED]**

      The type of processor.

    - **Parameters** *(list) --*

      The processor parameters.

      - *(dict) --*

        Describes the processor parameter.

        - **ParameterName** *(string) --* **[REQUIRED]**

          The name of the parameter.

        - **ParameterValue** *(string) --* **[REQUIRED]**

          The parameter value.
    """


_ClientUpdateDestinationElasticsearchDestinationUpdateProcessingConfigurationTypeDef = TypedDict(
    "_ClientUpdateDestinationElasticsearchDestinationUpdateProcessingConfigurationTypeDef",
    {
        "Enabled": bool,
        "Processors": List[
            ClientUpdateDestinationElasticsearchDestinationUpdateProcessingConfigurationProcessorsTypeDef
        ],
    },
    total=False,
)


class ClientUpdateDestinationElasticsearchDestinationUpdateProcessingConfigurationTypeDef(
    _ClientUpdateDestinationElasticsearchDestinationUpdateProcessingConfigurationTypeDef
):
    """
    Type definition for `ClientUpdateDestinationElasticsearchDestinationUpdate` `ProcessingConfiguration`

    The data processing configuration.

    - **Enabled** *(boolean) --*

      Enables or disables data processing.

    - **Processors** *(list) --*

      The data processors.

      - *(dict) --*

        Describes a data processor.

        - **Type** *(string) --* **[REQUIRED]**

          The type of processor.

        - **Parameters** *(list) --*

          The processor parameters.

          - *(dict) --*

            Describes the processor parameter.

            - **ParameterName** *(string) --* **[REQUIRED]**

              The name of the parameter.

            - **ParameterValue** *(string) --* **[REQUIRED]**

              The parameter value.
    """


_ClientUpdateDestinationElasticsearchDestinationUpdateRetryOptionsTypeDef = TypedDict(
    "_ClientUpdateDestinationElasticsearchDestinationUpdateRetryOptionsTypeDef",
    {"DurationInSeconds": int},
    total=False,
)


class ClientUpdateDestinationElasticsearchDestinationUpdateRetryOptionsTypeDef(
    _ClientUpdateDestinationElasticsearchDestinationUpdateRetryOptionsTypeDef
):
    """
    Type definition for `ClientUpdateDestinationElasticsearchDestinationUpdate` `RetryOptions`

    The retry behavior in case Kinesis Data Firehose is unable to deliver documents to Amazon ES.
    The default value is 300 (5 minutes).

    - **DurationInSeconds** *(integer) --*

      After an initial failure to deliver to Amazon ES, the total amount of time during which
      Kinesis Data Firehose retries delivery (including the first attempt). After this time has
      elapsed, the failed documents are written to Amazon S3. Default value is 300 seconds (5
      minutes). A value of 0 (zero) results in no retries.
    """


_ClientUpdateDestinationElasticsearchDestinationUpdateS3UpdateBufferingHintsTypeDef = TypedDict(
    "_ClientUpdateDestinationElasticsearchDestinationUpdateS3UpdateBufferingHintsTypeDef",
    {"SizeInMBs": int, "IntervalInSeconds": int},
    total=False,
)


class ClientUpdateDestinationElasticsearchDestinationUpdateS3UpdateBufferingHintsTypeDef(
    _ClientUpdateDestinationElasticsearchDestinationUpdateS3UpdateBufferingHintsTypeDef
):
    """
    Type definition for `ClientUpdateDestinationElasticsearchDestinationUpdateS3Update` `BufferingHints`

    The buffering option. If no value is specified, ``BufferingHints`` object default values are
    used.

    - **SizeInMBs** *(integer) --*

      Buffer incoming data to the specified size, in MiBs, before delivering it to the
      destination. The default value is 5. This parameter is optional but if you specify a value
      for it, you must also specify a value for ``IntervalInSeconds`` , and vice versa.

      We recommend setting this parameter to a value greater than the amount of data you
      typically ingest into the delivery stream in 10 seconds. For example, if you typically
      ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

    - **IntervalInSeconds** *(integer) --*

      Buffer incoming data for the specified period of time, in seconds, before delivering it to
      the destination. The default value is 300. This parameter is optional but if you specify a
      value for it, you must also specify a value for ``SizeInMBs`` , and vice versa.
    """


_ClientUpdateDestinationElasticsearchDestinationUpdateS3UpdateCloudWatchLoggingOptionsTypeDef = TypedDict(
    "_ClientUpdateDestinationElasticsearchDestinationUpdateS3UpdateCloudWatchLoggingOptionsTypeDef",
    {"Enabled": bool, "LogGroupName": str, "LogStreamName": str},
    total=False,
)


class ClientUpdateDestinationElasticsearchDestinationUpdateS3UpdateCloudWatchLoggingOptionsTypeDef(
    _ClientUpdateDestinationElasticsearchDestinationUpdateS3UpdateCloudWatchLoggingOptionsTypeDef
):
    """
    Type definition for `ClientUpdateDestinationElasticsearchDestinationUpdateS3Update` `CloudWatchLoggingOptions`

    The CloudWatch logging options for your delivery stream.

    - **Enabled** *(boolean) --*

      Enables or disables CloudWatch logging.

    - **LogGroupName** *(string) --*

      The CloudWatch group name for logging. This value is required if CloudWatch logging is
      enabled.

    - **LogStreamName** *(string) --*

      The CloudWatch log stream name for logging. This value is required if CloudWatch logging is
      enabled.
    """


_ClientUpdateDestinationElasticsearchDestinationUpdateS3UpdateEncryptionConfigurationKMSEncryptionConfigTypeDef = TypedDict(
    "_ClientUpdateDestinationElasticsearchDestinationUpdateS3UpdateEncryptionConfigurationKMSEncryptionConfigTypeDef",
    {"AWSKMSKeyARN": str},
)


class ClientUpdateDestinationElasticsearchDestinationUpdateS3UpdateEncryptionConfigurationKMSEncryptionConfigTypeDef(
    _ClientUpdateDestinationElasticsearchDestinationUpdateS3UpdateEncryptionConfigurationKMSEncryptionConfigTypeDef
):
    """
    Type definition for `ClientUpdateDestinationElasticsearchDestinationUpdateS3UpdateEncryptionConfiguration` `KMSEncryptionConfig`

    The encryption key.

    - **AWSKMSKeyARN** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region
      as the destination Amazon S3 bucket. For more information, see `Amazon Resource Names
      (ARNs) and AWS Service Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
    """


_ClientUpdateDestinationElasticsearchDestinationUpdateS3UpdateEncryptionConfigurationTypeDef = TypedDict(
    "_ClientUpdateDestinationElasticsearchDestinationUpdateS3UpdateEncryptionConfigurationTypeDef",
    {
        "NoEncryptionConfig": str,
        "KMSEncryptionConfig": ClientUpdateDestinationElasticsearchDestinationUpdateS3UpdateEncryptionConfigurationKMSEncryptionConfigTypeDef,
    },
    total=False,
)


class ClientUpdateDestinationElasticsearchDestinationUpdateS3UpdateEncryptionConfigurationTypeDef(
    _ClientUpdateDestinationElasticsearchDestinationUpdateS3UpdateEncryptionConfigurationTypeDef
):
    """
    Type definition for `ClientUpdateDestinationElasticsearchDestinationUpdateS3Update` `EncryptionConfiguration`

    The encryption configuration. If no value is specified, the default is no encryption.

    - **NoEncryptionConfig** *(string) --*

      Specifically override existing encryption information to ensure that no encryption is used.

    - **KMSEncryptionConfig** *(dict) --*

      The encryption key.

      - **AWSKMSKeyARN** *(string) --* **[REQUIRED]**

        The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region
        as the destination Amazon S3 bucket. For more information, see `Amazon Resource Names
        (ARNs) and AWS Service Namespaces
        <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
    """


_ClientUpdateDestinationElasticsearchDestinationUpdateS3UpdateTypeDef = TypedDict(
    "_ClientUpdateDestinationElasticsearchDestinationUpdateS3UpdateTypeDef",
    {
        "RoleARN": str,
        "BucketARN": str,
        "Prefix": str,
        "ErrorOutputPrefix": str,
        "BufferingHints": ClientUpdateDestinationElasticsearchDestinationUpdateS3UpdateBufferingHintsTypeDef,
        "CompressionFormat": str,
        "EncryptionConfiguration": ClientUpdateDestinationElasticsearchDestinationUpdateS3UpdateEncryptionConfigurationTypeDef,
        "CloudWatchLoggingOptions": ClientUpdateDestinationElasticsearchDestinationUpdateS3UpdateCloudWatchLoggingOptionsTypeDef,
    },
    total=False,
)


class ClientUpdateDestinationElasticsearchDestinationUpdateS3UpdateTypeDef(
    _ClientUpdateDestinationElasticsearchDestinationUpdateS3UpdateTypeDef
):
    """
    Type definition for `ClientUpdateDestinationElasticsearchDestinationUpdate` `S3Update`

    The Amazon S3 destination.

    - **RoleARN** *(string) --*

      The Amazon Resource Name (ARN) of the AWS credentials. For more information, see `Amazon
      Resource Names (ARNs) and AWS Service Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

    - **BucketARN** *(string) --*

      The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs) and AWS
      Service Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

    - **Prefix** *(string) --*

      The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered Amazon S3 files.
      You can also specify a custom prefix, as described in `Custom Prefixes for Amazon S3 Objects
      <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

    - **ErrorOutputPrefix** *(string) --*

      A prefix that Kinesis Data Firehose evaluates and adds to failed records before writing them
      to S3. This prefix appears immediately following the bucket name. For information about how
      to specify this prefix, see `Custom Prefixes for Amazon S3 Objects
      <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

    - **BufferingHints** *(dict) --*

      The buffering option. If no value is specified, ``BufferingHints`` object default values are
      used.

      - **SizeInMBs** *(integer) --*

        Buffer incoming data to the specified size, in MiBs, before delivering it to the
        destination. The default value is 5. This parameter is optional but if you specify a value
        for it, you must also specify a value for ``IntervalInSeconds`` , and vice versa.

        We recommend setting this parameter to a value greater than the amount of data you
        typically ingest into the delivery stream in 10 seconds. For example, if you typically
        ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

      - **IntervalInSeconds** *(integer) --*

        Buffer incoming data for the specified period of time, in seconds, before delivering it to
        the destination. The default value is 300. This parameter is optional but if you specify a
        value for it, you must also specify a value for ``SizeInMBs`` , and vice versa.

    - **CompressionFormat** *(string) --*

      The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .

      The compression formats ``SNAPPY`` or ``ZIP`` cannot be specified for Amazon Redshift
      destinations because they are not supported by the Amazon Redshift ``COPY`` operation that
      reads from the S3 bucket.

    - **EncryptionConfiguration** *(dict) --*

      The encryption configuration. If no value is specified, the default is no encryption.

      - **NoEncryptionConfig** *(string) --*

        Specifically override existing encryption information to ensure that no encryption is used.

      - **KMSEncryptionConfig** *(dict) --*

        The encryption key.

        - **AWSKMSKeyARN** *(string) --* **[REQUIRED]**

          The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region
          as the destination Amazon S3 bucket. For more information, see `Amazon Resource Names
          (ARNs) and AWS Service Namespaces
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

    - **CloudWatchLoggingOptions** *(dict) --*

      The CloudWatch logging options for your delivery stream.

      - **Enabled** *(boolean) --*

        Enables or disables CloudWatch logging.

      - **LogGroupName** *(string) --*

        The CloudWatch group name for logging. This value is required if CloudWatch logging is
        enabled.

      - **LogStreamName** *(string) --*

        The CloudWatch log stream name for logging. This value is required if CloudWatch logging is
        enabled.
    """


_ClientUpdateDestinationElasticsearchDestinationUpdateTypeDef = TypedDict(
    "_ClientUpdateDestinationElasticsearchDestinationUpdateTypeDef",
    {
        "RoleARN": str,
        "DomainARN": str,
        "ClusterEndpoint": str,
        "IndexName": str,
        "TypeName": str,
        "IndexRotationPeriod": str,
        "BufferingHints": ClientUpdateDestinationElasticsearchDestinationUpdateBufferingHintsTypeDef,
        "RetryOptions": ClientUpdateDestinationElasticsearchDestinationUpdateRetryOptionsTypeDef,
        "S3Update": ClientUpdateDestinationElasticsearchDestinationUpdateS3UpdateTypeDef,
        "ProcessingConfiguration": ClientUpdateDestinationElasticsearchDestinationUpdateProcessingConfigurationTypeDef,
        "CloudWatchLoggingOptions": ClientUpdateDestinationElasticsearchDestinationUpdateCloudWatchLoggingOptionsTypeDef,
    },
    total=False,
)


class ClientUpdateDestinationElasticsearchDestinationUpdateTypeDef(
    _ClientUpdateDestinationElasticsearchDestinationUpdateTypeDef
):
    """
    Type definition for `ClientUpdateDestination` `ElasticsearchDestinationUpdate`

    Describes an update for a destination in Amazon ES.

    - **RoleARN** *(string) --*

      The Amazon Resource Name (ARN) of the IAM role to be assumed by Kinesis Data Firehose for
      calling the Amazon ES Configuration API and for indexing documents. For more information, see
      `Grant Kinesis Data Firehose Access to an Amazon S3 Destination
      <https://docs.aws.amazon.com/firehose/latest/dev/controlling-access.html#using-iam-s3>`__ and
      `Amazon Resource Names (ARNs) and AWS Service Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

    - **DomainARN** *(string) --*

      The ARN of the Amazon ES domain. The IAM role must have permissions for
      ``DescribeElasticsearchDomain`` , ``DescribeElasticsearchDomains`` , and
      ``DescribeElasticsearchDomainConfig`` after assuming the IAM role specified in ``RoleARN`` .
      For more information, see `Amazon Resource Names (ARNs) and AWS Service Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

      Specify either ``ClusterEndpoint`` or ``DomainARN`` .

    - **ClusterEndpoint** *(string) --*

      The endpoint to use when communicating with the cluster. Specify either this
      ``ClusterEndpoint`` or the ``DomainARN`` field.

    - **IndexName** *(string) --*

      The Elasticsearch index name.

    - **TypeName** *(string) --*

      The Elasticsearch type name. For Elasticsearch 6.x, there can be only one type per index. If
      you try to specify a new type for an existing index that already has another type, Kinesis Data
      Firehose returns an error during runtime.

      If you upgrade Elasticsearch from 6.x to 7.x and don’t update your delivery stream, Kinesis
      Data Firehose still delivers data to Elasticsearch with the old index name and type name. If
      you want to update your delivery stream with a new index name, provide an empty string for
      ``TypeName`` .

    - **IndexRotationPeriod** *(string) --*

      The Elasticsearch index rotation period. Index rotation appends a timestamp to ``IndexName`` to
      facilitate the expiration of old data. For more information, see `Index Rotation for the Amazon
      ES Destination
      <https://docs.aws.amazon.com/firehose/latest/dev/basic-deliver.html#es-index-rotation>`__ .
      Default value is ``OneDay`` .

    - **BufferingHints** *(dict) --*

      The buffering options. If no value is specified, ``ElasticsearchBufferingHints`` object default
      values are used.

      - **IntervalInSeconds** *(integer) --*

        Buffer incoming data for the specified period of time, in seconds, before delivering it to
        the destination. The default value is 300 (5 minutes).

      - **SizeInMBs** *(integer) --*

        Buffer incoming data to the specified size, in MBs, before delivering it to the destination.
        The default value is 5.

        We recommend setting this parameter to a value greater than the amount of data you typically
        ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1
        MB/sec, the value should be 10 MB or higher.

    - **RetryOptions** *(dict) --*

      The retry behavior in case Kinesis Data Firehose is unable to deliver documents to Amazon ES.
      The default value is 300 (5 minutes).

      - **DurationInSeconds** *(integer) --*

        After an initial failure to deliver to Amazon ES, the total amount of time during which
        Kinesis Data Firehose retries delivery (including the first attempt). After this time has
        elapsed, the failed documents are written to Amazon S3. Default value is 300 seconds (5
        minutes). A value of 0 (zero) results in no retries.

    - **S3Update** *(dict) --*

      The Amazon S3 destination.

      - **RoleARN** *(string) --*

        The Amazon Resource Name (ARN) of the AWS credentials. For more information, see `Amazon
        Resource Names (ARNs) and AWS Service Namespaces
        <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

      - **BucketARN** *(string) --*

        The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs) and AWS
        Service Namespaces
        <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

      - **Prefix** *(string) --*

        The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered Amazon S3 files.
        You can also specify a custom prefix, as described in `Custom Prefixes for Amazon S3 Objects
        <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

      - **ErrorOutputPrefix** *(string) --*

        A prefix that Kinesis Data Firehose evaluates and adds to failed records before writing them
        to S3. This prefix appears immediately following the bucket name. For information about how
        to specify this prefix, see `Custom Prefixes for Amazon S3 Objects
        <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

      - **BufferingHints** *(dict) --*

        The buffering option. If no value is specified, ``BufferingHints`` object default values are
        used.

        - **SizeInMBs** *(integer) --*

          Buffer incoming data to the specified size, in MiBs, before delivering it to the
          destination. The default value is 5. This parameter is optional but if you specify a value
          for it, you must also specify a value for ``IntervalInSeconds`` , and vice versa.

          We recommend setting this parameter to a value greater than the amount of data you
          typically ingest into the delivery stream in 10 seconds. For example, if you typically
          ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

        - **IntervalInSeconds** *(integer) --*

          Buffer incoming data for the specified period of time, in seconds, before delivering it to
          the destination. The default value is 300. This parameter is optional but if you specify a
          value for it, you must also specify a value for ``SizeInMBs`` , and vice versa.

      - **CompressionFormat** *(string) --*

        The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .

        The compression formats ``SNAPPY`` or ``ZIP`` cannot be specified for Amazon Redshift
        destinations because they are not supported by the Amazon Redshift ``COPY`` operation that
        reads from the S3 bucket.

      - **EncryptionConfiguration** *(dict) --*

        The encryption configuration. If no value is specified, the default is no encryption.

        - **NoEncryptionConfig** *(string) --*

          Specifically override existing encryption information to ensure that no encryption is used.

        - **KMSEncryptionConfig** *(dict) --*

          The encryption key.

          - **AWSKMSKeyARN** *(string) --* **[REQUIRED]**

            The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region
            as the destination Amazon S3 bucket. For more information, see `Amazon Resource Names
            (ARNs) and AWS Service Namespaces
            <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

      - **CloudWatchLoggingOptions** *(dict) --*

        The CloudWatch logging options for your delivery stream.

        - **Enabled** *(boolean) --*

          Enables or disables CloudWatch logging.

        - **LogGroupName** *(string) --*

          The CloudWatch group name for logging. This value is required if CloudWatch logging is
          enabled.

        - **LogStreamName** *(string) --*

          The CloudWatch log stream name for logging. This value is required if CloudWatch logging is
          enabled.

    - **ProcessingConfiguration** *(dict) --*

      The data processing configuration.

      - **Enabled** *(boolean) --*

        Enables or disables data processing.

      - **Processors** *(list) --*

        The data processors.

        - *(dict) --*

          Describes a data processor.

          - **Type** *(string) --* **[REQUIRED]**

            The type of processor.

          - **Parameters** *(list) --*

            The processor parameters.

            - *(dict) --*

              Describes the processor parameter.

              - **ParameterName** *(string) --* **[REQUIRED]**

                The name of the parameter.

              - **ParameterValue** *(string) --* **[REQUIRED]**

                The parameter value.

    - **CloudWatchLoggingOptions** *(dict) --*

      The CloudWatch logging options for your delivery stream.

      - **Enabled** *(boolean) --*

        Enables or disables CloudWatch logging.

      - **LogGroupName** *(string) --*

        The CloudWatch group name for logging. This value is required if CloudWatch logging is
        enabled.

      - **LogStreamName** *(string) --*

        The CloudWatch log stream name for logging. This value is required if CloudWatch logging is
        enabled.
    """


_ClientUpdateDestinationExtendedS3DestinationUpdateBufferingHintsTypeDef = TypedDict(
    "_ClientUpdateDestinationExtendedS3DestinationUpdateBufferingHintsTypeDef",
    {"SizeInMBs": int, "IntervalInSeconds": int},
    total=False,
)


class ClientUpdateDestinationExtendedS3DestinationUpdateBufferingHintsTypeDef(
    _ClientUpdateDestinationExtendedS3DestinationUpdateBufferingHintsTypeDef
):
    """
    Type definition for `ClientUpdateDestinationExtendedS3DestinationUpdate` `BufferingHints`

    The buffering option.

    - **SizeInMBs** *(integer) --*

      Buffer incoming data to the specified size, in MiBs, before delivering it to the destination.
      The default value is 5. This parameter is optional but if you specify a value for it, you
      must also specify a value for ``IntervalInSeconds`` , and vice versa.

      We recommend setting this parameter to a value greater than the amount of data you typically
      ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1
      MiB/sec, the value should be 10 MiB or higher.

    - **IntervalInSeconds** *(integer) --*

      Buffer incoming data for the specified period of time, in seconds, before delivering it to
      the destination. The default value is 300. This parameter is optional but if you specify a
      value for it, you must also specify a value for ``SizeInMBs`` , and vice versa.
    """


_ClientUpdateDestinationExtendedS3DestinationUpdateCloudWatchLoggingOptionsTypeDef = TypedDict(
    "_ClientUpdateDestinationExtendedS3DestinationUpdateCloudWatchLoggingOptionsTypeDef",
    {"Enabled": bool, "LogGroupName": str, "LogStreamName": str},
    total=False,
)


class ClientUpdateDestinationExtendedS3DestinationUpdateCloudWatchLoggingOptionsTypeDef(
    _ClientUpdateDestinationExtendedS3DestinationUpdateCloudWatchLoggingOptionsTypeDef
):
    """
    Type definition for `ClientUpdateDestinationExtendedS3DestinationUpdate` `CloudWatchLoggingOptions`

    The Amazon CloudWatch logging options for your delivery stream.

    - **Enabled** *(boolean) --*

      Enables or disables CloudWatch logging.

    - **LogGroupName** *(string) --*

      The CloudWatch group name for logging. This value is required if CloudWatch logging is
      enabled.

    - **LogStreamName** *(string) --*

      The CloudWatch log stream name for logging. This value is required if CloudWatch logging is
      enabled.
    """


_ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDeTypeDef = TypedDict(
    "_ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDeTypeDef",
    {"TimestampFormats": List[str]},
    total=False,
)


class ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDeTypeDef(
    _ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDeTypeDef
):
    """
    Type definition for `ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationInputFormatConfigurationDeserializer` `HiveJsonSerDe`

    The native Hive / HCatalog JsonSerDe. Used by Kinesis Data Firehose for deserializing
    data, which means converting it from the JSON format in preparation for serializing it to
    the Parquet or ORC format. This is one of two deserializers you can choose, depending on
    which one offers the functionality you need. The other option is the OpenX SerDe.

    - **TimestampFormats** *(list) --*

      Indicates how you want Kinesis Data Firehose to parse the date and timestamps that may
      be present in your input data JSON. To specify these format strings, follow the pattern
      syntax of JodaTime's DateTimeFormat format strings. For more information, see `Class
      DateTimeFormat
      <https://www.joda.org/joda-time/apidocs/org/joda/time/format/DateTimeFormat.html>`__ .
      You can also use the special value ``millis`` to parse timestamps in epoch
      milliseconds. If you don't specify a format, Kinesis Data Firehose uses
      ``java.sql.Timestamp::valueOf`` by default.

      - *(string) --*
    """


_ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDeTypeDef = TypedDict(
    "_ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDeTypeDef",
    {
        "ConvertDotsInJsonKeysToUnderscores": bool,
        "CaseInsensitive": bool,
        "ColumnToJsonKeyMappings": Dict[str, str],
    },
    total=False,
)


class ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDeTypeDef(
    _ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDeTypeDef
):
    """
    Type definition for `ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationInputFormatConfigurationDeserializer` `OpenXJsonSerDe`

    The OpenX SerDe. Used by Kinesis Data Firehose for deserializing data, which means
    converting it from the JSON format in preparation for serializing it to the Parquet or
    ORC format. This is one of two deserializers you can choose, depending on which one
    offers the functionality you need. The other option is the native Hive / HCatalog
    JsonSerDe.

    - **ConvertDotsInJsonKeysToUnderscores** *(boolean) --*

      When set to ``true`` , specifies that the names of the keys include dots and that you
      want Kinesis Data Firehose to replace them with underscores. This is useful because
      Apache Hive does not allow dots in column names. For example, if the JSON contains a
      key whose name is "a.b", you can define the column name to be "a_b" when using this
      option.

      The default is ``false`` .

    - **CaseInsensitive** *(boolean) --*

      When set to ``true`` , which is the default, Kinesis Data Firehose converts JSON keys
      to lowercase before deserializing them.

    - **ColumnToJsonKeyMappings** *(dict) --*

      Maps column names to JSON keys that aren't identical to the column names. This is
      useful when the JSON contains keys that are Hive keywords. For example, ``timestamp``
      is a Hive keyword. If you have a JSON key named ``timestamp`` , set this parameter to
      ``{"ts": "timestamp"}`` to map this key to a column named ``ts`` .

      - *(string) --*

        - *(string) --*
    """


_ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationInputFormatConfigurationDeserializerTypeDef = TypedDict(
    "_ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationInputFormatConfigurationDeserializerTypeDef",
    {
        "OpenXJsonSerDe": ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDeTypeDef,
        "HiveJsonSerDe": ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDeTypeDef,
    },
    total=False,
)


class ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationInputFormatConfigurationDeserializerTypeDef(
    _ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationInputFormatConfigurationDeserializerTypeDef
):
    """
    Type definition for `ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationInputFormatConfiguration` `Deserializer`

    Specifies which deserializer to use. You can choose either the Apache Hive JSON SerDe or
    the OpenX JSON SerDe. If both are non-null, the server rejects the request.

    - **OpenXJsonSerDe** *(dict) --*

      The OpenX SerDe. Used by Kinesis Data Firehose for deserializing data, which means
      converting it from the JSON format in preparation for serializing it to the Parquet or
      ORC format. This is one of two deserializers you can choose, depending on which one
      offers the functionality you need. The other option is the native Hive / HCatalog
      JsonSerDe.

      - **ConvertDotsInJsonKeysToUnderscores** *(boolean) --*

        When set to ``true`` , specifies that the names of the keys include dots and that you
        want Kinesis Data Firehose to replace them with underscores. This is useful because
        Apache Hive does not allow dots in column names. For example, if the JSON contains a
        key whose name is "a.b", you can define the column name to be "a_b" when using this
        option.

        The default is ``false`` .

      - **CaseInsensitive** *(boolean) --*

        When set to ``true`` , which is the default, Kinesis Data Firehose converts JSON keys
        to lowercase before deserializing them.

      - **ColumnToJsonKeyMappings** *(dict) --*

        Maps column names to JSON keys that aren't identical to the column names. This is
        useful when the JSON contains keys that are Hive keywords. For example, ``timestamp``
        is a Hive keyword. If you have a JSON key named ``timestamp`` , set this parameter to
        ``{"ts": "timestamp"}`` to map this key to a column named ``ts`` .

        - *(string) --*

          - *(string) --*

    - **HiveJsonSerDe** *(dict) --*

      The native Hive / HCatalog JsonSerDe. Used by Kinesis Data Firehose for deserializing
      data, which means converting it from the JSON format in preparation for serializing it to
      the Parquet or ORC format. This is one of two deserializers you can choose, depending on
      which one offers the functionality you need. The other option is the OpenX SerDe.

      - **TimestampFormats** *(list) --*

        Indicates how you want Kinesis Data Firehose to parse the date and timestamps that may
        be present in your input data JSON. To specify these format strings, follow the pattern
        syntax of JodaTime's DateTimeFormat format strings. For more information, see `Class
        DateTimeFormat
        <https://www.joda.org/joda-time/apidocs/org/joda/time/format/DateTimeFormat.html>`__ .
        You can also use the special value ``millis`` to parse timestamps in epoch
        milliseconds. If you don't specify a format, Kinesis Data Firehose uses
        ``java.sql.Timestamp::valueOf`` by default.

        - *(string) --*
    """


_ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationInputFormatConfigurationTypeDef = TypedDict(
    "_ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationInputFormatConfigurationTypeDef",
    {
        "Deserializer": ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationInputFormatConfigurationDeserializerTypeDef
    },
    total=False,
)


class ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationInputFormatConfigurationTypeDef(
    _ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationInputFormatConfigurationTypeDef
):
    """
    Type definition for `ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfiguration` `InputFormatConfiguration`

    Specifies the deserializer that you want Kinesis Data Firehose to use to convert the format
    of your data from JSON.

    - **Deserializer** *(dict) --*

      Specifies which deserializer to use. You can choose either the Apache Hive JSON SerDe or
      the OpenX JSON SerDe. If both are non-null, the server rejects the request.

      - **OpenXJsonSerDe** *(dict) --*

        The OpenX SerDe. Used by Kinesis Data Firehose for deserializing data, which means
        converting it from the JSON format in preparation for serializing it to the Parquet or
        ORC format. This is one of two deserializers you can choose, depending on which one
        offers the functionality you need. The other option is the native Hive / HCatalog
        JsonSerDe.

        - **ConvertDotsInJsonKeysToUnderscores** *(boolean) --*

          When set to ``true`` , specifies that the names of the keys include dots and that you
          want Kinesis Data Firehose to replace them with underscores. This is useful because
          Apache Hive does not allow dots in column names. For example, if the JSON contains a
          key whose name is "a.b", you can define the column name to be "a_b" when using this
          option.

          The default is ``false`` .

        - **CaseInsensitive** *(boolean) --*

          When set to ``true`` , which is the default, Kinesis Data Firehose converts JSON keys
          to lowercase before deserializing them.

        - **ColumnToJsonKeyMappings** *(dict) --*

          Maps column names to JSON keys that aren't identical to the column names. This is
          useful when the JSON contains keys that are Hive keywords. For example, ``timestamp``
          is a Hive keyword. If you have a JSON key named ``timestamp`` , set this parameter to
          ``{"ts": "timestamp"}`` to map this key to a column named ``ts`` .

          - *(string) --*

            - *(string) --*

      - **HiveJsonSerDe** *(dict) --*

        The native Hive / HCatalog JsonSerDe. Used by Kinesis Data Firehose for deserializing
        data, which means converting it from the JSON format in preparation for serializing it to
        the Parquet or ORC format. This is one of two deserializers you can choose, depending on
        which one offers the functionality you need. The other option is the OpenX SerDe.

        - **TimestampFormats** *(list) --*

          Indicates how you want Kinesis Data Firehose to parse the date and timestamps that may
          be present in your input data JSON. To specify these format strings, follow the pattern
          syntax of JodaTime's DateTimeFormat format strings. For more information, see `Class
          DateTimeFormat
          <https://www.joda.org/joda-time/apidocs/org/joda/time/format/DateTimeFormat.html>`__ .
          You can also use the special value ``millis`` to parse timestamps in epoch
          milliseconds. If you don't specify a format, Kinesis Data Firehose uses
          ``java.sql.Timestamp::valueOf`` by default.

          - *(string) --*
    """


_ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDeTypeDef = TypedDict(
    "_ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDeTypeDef",
    {
        "StripeSizeBytes": int,
        "BlockSizeBytes": int,
        "RowIndexStride": int,
        "EnablePadding": bool,
        "PaddingTolerance": float,
        "Compression": str,
        "BloomFilterColumns": List[str],
        "BloomFilterFalsePositiveProbability": float,
        "DictionaryKeyThreshold": float,
        "FormatVersion": str,
    },
    total=False,
)


class ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDeTypeDef(
    _ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDeTypeDef
):
    """
    Type definition for `ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationOutputFormatConfigurationSerializer` `OrcSerDe`

    A serializer to use for converting data to the ORC format before storing it in Amazon S3.
    For more information, see `Apache ORC <https://orc.apache.org/docs/>`__ .

    - **StripeSizeBytes** *(integer) --*

      The number of bytes in each stripe. The default is 64 MiB and the minimum is 8 MiB.

    - **BlockSizeBytes** *(integer) --*

      The Hadoop Distributed File System (HDFS) block size. This is useful if you intend to
      copy the data from Amazon S3 to HDFS before querying. The default is 256 MiB and the
      minimum is 64 MiB. Kinesis Data Firehose uses this value for padding calculations.

    - **RowIndexStride** *(integer) --*

      The number of rows between index entries. The default is 10,000 and the minimum is
      1,000.

    - **EnablePadding** *(boolean) --*

      Set this to ``true`` to indicate that you want stripes to be padded to the HDFS block
      boundaries. This is useful if you intend to copy the data from Amazon S3 to HDFS before
      querying. The default is ``false`` .

    - **PaddingTolerance** *(float) --*

      A number between 0 and 1 that defines the tolerance for block padding as a decimal
      fraction of stripe size. The default value is 0.05, which means 5 percent of stripe
      size.

      For the default values of 64 MiB ORC stripes and 256 MiB HDFS blocks, the default block
      padding tolerance of 5 percent reserves a maximum of 3.2 MiB for padding within the 256
      MiB block. In such a case, if the available size within the block is more than 3.2 MiB,
      a new, smaller stripe is inserted to fit within that space. This ensures that no stripe
      crosses block boundaries and causes remote reads within a node-local task.

      Kinesis Data Firehose ignores this parameter when  OrcSerDe$EnablePadding is ``false`` .

    - **Compression** *(string) --*

      The compression code to use over data blocks. The default is ``SNAPPY`` .

    - **BloomFilterColumns** *(list) --*

      The column names for which you want Kinesis Data Firehose to create bloom filters. The
      default is ``null`` .

      - *(string) --*

    - **BloomFilterFalsePositiveProbability** *(float) --*

      The Bloom filter false positive probability (FPP). The lower the FPP, the bigger the
      Bloom filter. The default value is 0.05, the minimum is 0, and the maximum is 1.

    - **DictionaryKeyThreshold** *(float) --*

      Represents the fraction of the total number of non-null rows. To turn off dictionary
      encoding, set this fraction to a number that is less than the number of distinct keys
      in a dictionary. To always use dictionary encoding, set this threshold to 1.

    - **FormatVersion** *(string) --*

      The version of the file to write. The possible values are ``V0_11`` and ``V0_12`` . The
      default is ``V0_12`` .
    """


_ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDeTypeDef = TypedDict(
    "_ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDeTypeDef",
    {
        "BlockSizeBytes": int,
        "PageSizeBytes": int,
        "Compression": str,
        "EnableDictionaryCompression": bool,
        "MaxPaddingBytes": int,
        "WriterVersion": str,
    },
    total=False,
)


class ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDeTypeDef(
    _ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDeTypeDef
):
    """
    Type definition for `ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationOutputFormatConfigurationSerializer` `ParquetSerDe`

    A serializer to use for converting data to the Parquet format before storing it in Amazon
    S3. For more information, see `Apache Parquet
    <https://parquet.apache.org/documentation/latest/>`__ .

    - **BlockSizeBytes** *(integer) --*

      The Hadoop Distributed File System (HDFS) block size. This is useful if you intend to
      copy the data from Amazon S3 to HDFS before querying. The default is 256 MiB and the
      minimum is 64 MiB. Kinesis Data Firehose uses this value for padding calculations.

    - **PageSizeBytes** *(integer) --*

      The Parquet page size. Column chunks are divided into pages. A page is conceptually an
      indivisible unit (in terms of compression and encoding). The minimum value is 64 KiB
      and the default is 1 MiB.

    - **Compression** *(string) --*

      The compression code to use over data blocks. The possible values are ``UNCOMPRESSED``
      , ``SNAPPY`` , and ``GZIP`` , with the default being ``SNAPPY`` . Use ``SNAPPY`` for
      higher decompression speed. Use ``GZIP`` if the compression ration is more important
      than speed.

    - **EnableDictionaryCompression** *(boolean) --*

      Indicates whether to enable dictionary compression.

    - **MaxPaddingBytes** *(integer) --*

      The maximum amount of padding to apply. This is useful if you intend to copy the data
      from Amazon S3 to HDFS before querying. The default is 0.

    - **WriterVersion** *(string) --*

      Indicates the version of row format to output. The possible values are ``V1`` and
      ``V2`` . The default is ``V1`` .
    """


_ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationOutputFormatConfigurationSerializerTypeDef = TypedDict(
    "_ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationOutputFormatConfigurationSerializerTypeDef",
    {
        "ParquetSerDe": ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDeTypeDef,
        "OrcSerDe": ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDeTypeDef,
    },
    total=False,
)


class ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationOutputFormatConfigurationSerializerTypeDef(
    _ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationOutputFormatConfigurationSerializerTypeDef
):
    """
    Type definition for `ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationOutputFormatConfiguration` `Serializer`

    Specifies which serializer to use. You can choose either the ORC SerDe or the Parquet
    SerDe. If both are non-null, the server rejects the request.

    - **ParquetSerDe** *(dict) --*

      A serializer to use for converting data to the Parquet format before storing it in Amazon
      S3. For more information, see `Apache Parquet
      <https://parquet.apache.org/documentation/latest/>`__ .

      - **BlockSizeBytes** *(integer) --*

        The Hadoop Distributed File System (HDFS) block size. This is useful if you intend to
        copy the data from Amazon S3 to HDFS before querying. The default is 256 MiB and the
        minimum is 64 MiB. Kinesis Data Firehose uses this value for padding calculations.

      - **PageSizeBytes** *(integer) --*

        The Parquet page size. Column chunks are divided into pages. A page is conceptually an
        indivisible unit (in terms of compression and encoding). The minimum value is 64 KiB
        and the default is 1 MiB.

      - **Compression** *(string) --*

        The compression code to use over data blocks. The possible values are ``UNCOMPRESSED``
        , ``SNAPPY`` , and ``GZIP`` , with the default being ``SNAPPY`` . Use ``SNAPPY`` for
        higher decompression speed. Use ``GZIP`` if the compression ration is more important
        than speed.

      - **EnableDictionaryCompression** *(boolean) --*

        Indicates whether to enable dictionary compression.

      - **MaxPaddingBytes** *(integer) --*

        The maximum amount of padding to apply. This is useful if you intend to copy the data
        from Amazon S3 to HDFS before querying. The default is 0.

      - **WriterVersion** *(string) --*

        Indicates the version of row format to output. The possible values are ``V1`` and
        ``V2`` . The default is ``V1`` .

    - **OrcSerDe** *(dict) --*

      A serializer to use for converting data to the ORC format before storing it in Amazon S3.
      For more information, see `Apache ORC <https://orc.apache.org/docs/>`__ .

      - **StripeSizeBytes** *(integer) --*

        The number of bytes in each stripe. The default is 64 MiB and the minimum is 8 MiB.

      - **BlockSizeBytes** *(integer) --*

        The Hadoop Distributed File System (HDFS) block size. This is useful if you intend to
        copy the data from Amazon S3 to HDFS before querying. The default is 256 MiB and the
        minimum is 64 MiB. Kinesis Data Firehose uses this value for padding calculations.

      - **RowIndexStride** *(integer) --*

        The number of rows between index entries. The default is 10,000 and the minimum is
        1,000.

      - **EnablePadding** *(boolean) --*

        Set this to ``true`` to indicate that you want stripes to be padded to the HDFS block
        boundaries. This is useful if you intend to copy the data from Amazon S3 to HDFS before
        querying. The default is ``false`` .

      - **PaddingTolerance** *(float) --*

        A number between 0 and 1 that defines the tolerance for block padding as a decimal
        fraction of stripe size. The default value is 0.05, which means 5 percent of stripe
        size.

        For the default values of 64 MiB ORC stripes and 256 MiB HDFS blocks, the default block
        padding tolerance of 5 percent reserves a maximum of 3.2 MiB for padding within the 256
        MiB block. In such a case, if the available size within the block is more than 3.2 MiB,
        a new, smaller stripe is inserted to fit within that space. This ensures that no stripe
        crosses block boundaries and causes remote reads within a node-local task.

        Kinesis Data Firehose ignores this parameter when  OrcSerDe$EnablePadding is ``false`` .

      - **Compression** *(string) --*

        The compression code to use over data blocks. The default is ``SNAPPY`` .

      - **BloomFilterColumns** *(list) --*

        The column names for which you want Kinesis Data Firehose to create bloom filters. The
        default is ``null`` .

        - *(string) --*

      - **BloomFilterFalsePositiveProbability** *(float) --*

        The Bloom filter false positive probability (FPP). The lower the FPP, the bigger the
        Bloom filter. The default value is 0.05, the minimum is 0, and the maximum is 1.

      - **DictionaryKeyThreshold** *(float) --*

        Represents the fraction of the total number of non-null rows. To turn off dictionary
        encoding, set this fraction to a number that is less than the number of distinct keys
        in a dictionary. To always use dictionary encoding, set this threshold to 1.

      - **FormatVersion** *(string) --*

        The version of the file to write. The possible values are ``V0_11`` and ``V0_12`` . The
        default is ``V0_12`` .
    """


_ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationOutputFormatConfigurationTypeDef = TypedDict(
    "_ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationOutputFormatConfigurationTypeDef",
    {
        "Serializer": ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationOutputFormatConfigurationSerializerTypeDef
    },
    total=False,
)


class ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationOutputFormatConfigurationTypeDef(
    _ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationOutputFormatConfigurationTypeDef
):
    """
    Type definition for `ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfiguration` `OutputFormatConfiguration`

    Specifies the serializer that you want Kinesis Data Firehose to use to convert the format of
    your data to the Parquet or ORC format.

    - **Serializer** *(dict) --*

      Specifies which serializer to use. You can choose either the ORC SerDe or the Parquet
      SerDe. If both are non-null, the server rejects the request.

      - **ParquetSerDe** *(dict) --*

        A serializer to use for converting data to the Parquet format before storing it in Amazon
        S3. For more information, see `Apache Parquet
        <https://parquet.apache.org/documentation/latest/>`__ .

        - **BlockSizeBytes** *(integer) --*

          The Hadoop Distributed File System (HDFS) block size. This is useful if you intend to
          copy the data from Amazon S3 to HDFS before querying. The default is 256 MiB and the
          minimum is 64 MiB. Kinesis Data Firehose uses this value for padding calculations.

        - **PageSizeBytes** *(integer) --*

          The Parquet page size. Column chunks are divided into pages. A page is conceptually an
          indivisible unit (in terms of compression and encoding). The minimum value is 64 KiB
          and the default is 1 MiB.

        - **Compression** *(string) --*

          The compression code to use over data blocks. The possible values are ``UNCOMPRESSED``
          , ``SNAPPY`` , and ``GZIP`` , with the default being ``SNAPPY`` . Use ``SNAPPY`` for
          higher decompression speed. Use ``GZIP`` if the compression ration is more important
          than speed.

        - **EnableDictionaryCompression** *(boolean) --*

          Indicates whether to enable dictionary compression.

        - **MaxPaddingBytes** *(integer) --*

          The maximum amount of padding to apply. This is useful if you intend to copy the data
          from Amazon S3 to HDFS before querying. The default is 0.

        - **WriterVersion** *(string) --*

          Indicates the version of row format to output. The possible values are ``V1`` and
          ``V2`` . The default is ``V1`` .

      - **OrcSerDe** *(dict) --*

        A serializer to use for converting data to the ORC format before storing it in Amazon S3.
        For more information, see `Apache ORC <https://orc.apache.org/docs/>`__ .

        - **StripeSizeBytes** *(integer) --*

          The number of bytes in each stripe. The default is 64 MiB and the minimum is 8 MiB.

        - **BlockSizeBytes** *(integer) --*

          The Hadoop Distributed File System (HDFS) block size. This is useful if you intend to
          copy the data from Amazon S3 to HDFS before querying. The default is 256 MiB and the
          minimum is 64 MiB. Kinesis Data Firehose uses this value for padding calculations.

        - **RowIndexStride** *(integer) --*

          The number of rows between index entries. The default is 10,000 and the minimum is
          1,000.

        - **EnablePadding** *(boolean) --*

          Set this to ``true`` to indicate that you want stripes to be padded to the HDFS block
          boundaries. This is useful if you intend to copy the data from Amazon S3 to HDFS before
          querying. The default is ``false`` .

        - **PaddingTolerance** *(float) --*

          A number between 0 and 1 that defines the tolerance for block padding as a decimal
          fraction of stripe size. The default value is 0.05, which means 5 percent of stripe
          size.

          For the default values of 64 MiB ORC stripes and 256 MiB HDFS blocks, the default block
          padding tolerance of 5 percent reserves a maximum of 3.2 MiB for padding within the 256
          MiB block. In such a case, if the available size within the block is more than 3.2 MiB,
          a new, smaller stripe is inserted to fit within that space. This ensures that no stripe
          crosses block boundaries and causes remote reads within a node-local task.

          Kinesis Data Firehose ignores this parameter when  OrcSerDe$EnablePadding is ``false`` .

        - **Compression** *(string) --*

          The compression code to use over data blocks. The default is ``SNAPPY`` .

        - **BloomFilterColumns** *(list) --*

          The column names for which you want Kinesis Data Firehose to create bloom filters. The
          default is ``null`` .

          - *(string) --*

        - **BloomFilterFalsePositiveProbability** *(float) --*

          The Bloom filter false positive probability (FPP). The lower the FPP, the bigger the
          Bloom filter. The default value is 0.05, the minimum is 0, and the maximum is 1.

        - **DictionaryKeyThreshold** *(float) --*

          Represents the fraction of the total number of non-null rows. To turn off dictionary
          encoding, set this fraction to a number that is less than the number of distinct keys
          in a dictionary. To always use dictionary encoding, set this threshold to 1.

        - **FormatVersion** *(string) --*

          The version of the file to write. The possible values are ``V0_11`` and ``V0_12`` . The
          default is ``V0_12`` .
    """


_ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationSchemaConfigurationTypeDef = TypedDict(
    "_ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationSchemaConfigurationTypeDef",
    {
        "RoleARN": str,
        "CatalogId": str,
        "DatabaseName": str,
        "TableName": str,
        "Region": str,
        "VersionId": str,
    },
    total=False,
)


class ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationSchemaConfigurationTypeDef(
    _ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationSchemaConfigurationTypeDef
):
    """
    Type definition for `ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfiguration` `SchemaConfiguration`

    Specifies the AWS Glue Data Catalog table that contains the column information.

    - **RoleARN** *(string) --*

      The role that Kinesis Data Firehose can use to access AWS Glue. This role must be in the
      same account you use for Kinesis Data Firehose. Cross-account roles aren't allowed.

    - **CatalogId** *(string) --*

      The ID of the AWS Glue Data Catalog. If you don't supply this, the AWS account ID is used
      by default.

    - **DatabaseName** *(string) --*

      Specifies the name of the AWS Glue database that contains the schema for the output data.

    - **TableName** *(string) --*

      Specifies the AWS Glue table that contains the column information that constitutes your
      data schema.

    - **Region** *(string) --*

      If you don't specify an AWS Region, the default is the current Region.

    - **VersionId** *(string) --*

      Specifies the table version for the output data schema. If you don't specify this version
      ID, or if you set it to ``LATEST`` , Kinesis Data Firehose uses the most recent version.
      This means that any updates to the table are automatically picked up.
    """


_ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationTypeDef = TypedDict(
    "_ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationTypeDef",
    {
        "SchemaConfiguration": ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationSchemaConfigurationTypeDef,
        "InputFormatConfiguration": ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationInputFormatConfigurationTypeDef,
        "OutputFormatConfiguration": ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationOutputFormatConfigurationTypeDef,
        "Enabled": bool,
    },
    total=False,
)


class ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationTypeDef(
    _ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationTypeDef
):
    """
    Type definition for `ClientUpdateDestinationExtendedS3DestinationUpdate` `DataFormatConversionConfiguration`

    The serializer, deserializer, and schema for converting data from the JSON format to the
    Parquet or ORC format before writing it to Amazon S3.

    - **SchemaConfiguration** *(dict) --*

      Specifies the AWS Glue Data Catalog table that contains the column information.

      - **RoleARN** *(string) --*

        The role that Kinesis Data Firehose can use to access AWS Glue. This role must be in the
        same account you use for Kinesis Data Firehose. Cross-account roles aren't allowed.

      - **CatalogId** *(string) --*

        The ID of the AWS Glue Data Catalog. If you don't supply this, the AWS account ID is used
        by default.

      - **DatabaseName** *(string) --*

        Specifies the name of the AWS Glue database that contains the schema for the output data.

      - **TableName** *(string) --*

        Specifies the AWS Glue table that contains the column information that constitutes your
        data schema.

      - **Region** *(string) --*

        If you don't specify an AWS Region, the default is the current Region.

      - **VersionId** *(string) --*

        Specifies the table version for the output data schema. If you don't specify this version
        ID, or if you set it to ``LATEST`` , Kinesis Data Firehose uses the most recent version.
        This means that any updates to the table are automatically picked up.

    - **InputFormatConfiguration** *(dict) --*

      Specifies the deserializer that you want Kinesis Data Firehose to use to convert the format
      of your data from JSON.

      - **Deserializer** *(dict) --*

        Specifies which deserializer to use. You can choose either the Apache Hive JSON SerDe or
        the OpenX JSON SerDe. If both are non-null, the server rejects the request.

        - **OpenXJsonSerDe** *(dict) --*

          The OpenX SerDe. Used by Kinesis Data Firehose for deserializing data, which means
          converting it from the JSON format in preparation for serializing it to the Parquet or
          ORC format. This is one of two deserializers you can choose, depending on which one
          offers the functionality you need. The other option is the native Hive / HCatalog
          JsonSerDe.

          - **ConvertDotsInJsonKeysToUnderscores** *(boolean) --*

            When set to ``true`` , specifies that the names of the keys include dots and that you
            want Kinesis Data Firehose to replace them with underscores. This is useful because
            Apache Hive does not allow dots in column names. For example, if the JSON contains a
            key whose name is "a.b", you can define the column name to be "a_b" when using this
            option.

            The default is ``false`` .

          - **CaseInsensitive** *(boolean) --*

            When set to ``true`` , which is the default, Kinesis Data Firehose converts JSON keys
            to lowercase before deserializing them.

          - **ColumnToJsonKeyMappings** *(dict) --*

            Maps column names to JSON keys that aren't identical to the column names. This is
            useful when the JSON contains keys that are Hive keywords. For example, ``timestamp``
            is a Hive keyword. If you have a JSON key named ``timestamp`` , set this parameter to
            ``{"ts": "timestamp"}`` to map this key to a column named ``ts`` .

            - *(string) --*

              - *(string) --*

        - **HiveJsonSerDe** *(dict) --*

          The native Hive / HCatalog JsonSerDe. Used by Kinesis Data Firehose for deserializing
          data, which means converting it from the JSON format in preparation for serializing it to
          the Parquet or ORC format. This is one of two deserializers you can choose, depending on
          which one offers the functionality you need. The other option is the OpenX SerDe.

          - **TimestampFormats** *(list) --*

            Indicates how you want Kinesis Data Firehose to parse the date and timestamps that may
            be present in your input data JSON. To specify these format strings, follow the pattern
            syntax of JodaTime's DateTimeFormat format strings. For more information, see `Class
            DateTimeFormat
            <https://www.joda.org/joda-time/apidocs/org/joda/time/format/DateTimeFormat.html>`__ .
            You can also use the special value ``millis`` to parse timestamps in epoch
            milliseconds. If you don't specify a format, Kinesis Data Firehose uses
            ``java.sql.Timestamp::valueOf`` by default.

            - *(string) --*

    - **OutputFormatConfiguration** *(dict) --*

      Specifies the serializer that you want Kinesis Data Firehose to use to convert the format of
      your data to the Parquet or ORC format.

      - **Serializer** *(dict) --*

        Specifies which serializer to use. You can choose either the ORC SerDe or the Parquet
        SerDe. If both are non-null, the server rejects the request.

        - **ParquetSerDe** *(dict) --*

          A serializer to use for converting data to the Parquet format before storing it in Amazon
          S3. For more information, see `Apache Parquet
          <https://parquet.apache.org/documentation/latest/>`__ .

          - **BlockSizeBytes** *(integer) --*

            The Hadoop Distributed File System (HDFS) block size. This is useful if you intend to
            copy the data from Amazon S3 to HDFS before querying. The default is 256 MiB and the
            minimum is 64 MiB. Kinesis Data Firehose uses this value for padding calculations.

          - **PageSizeBytes** *(integer) --*

            The Parquet page size. Column chunks are divided into pages. A page is conceptually an
            indivisible unit (in terms of compression and encoding). The minimum value is 64 KiB
            and the default is 1 MiB.

          - **Compression** *(string) --*

            The compression code to use over data blocks. The possible values are ``UNCOMPRESSED``
            , ``SNAPPY`` , and ``GZIP`` , with the default being ``SNAPPY`` . Use ``SNAPPY`` for
            higher decompression speed. Use ``GZIP`` if the compression ration is more important
            than speed.

          - **EnableDictionaryCompression** *(boolean) --*

            Indicates whether to enable dictionary compression.

          - **MaxPaddingBytes** *(integer) --*

            The maximum amount of padding to apply. This is useful if you intend to copy the data
            from Amazon S3 to HDFS before querying. The default is 0.

          - **WriterVersion** *(string) --*

            Indicates the version of row format to output. The possible values are ``V1`` and
            ``V2`` . The default is ``V1`` .

        - **OrcSerDe** *(dict) --*

          A serializer to use for converting data to the ORC format before storing it in Amazon S3.
          For more information, see `Apache ORC <https://orc.apache.org/docs/>`__ .

          - **StripeSizeBytes** *(integer) --*

            The number of bytes in each stripe. The default is 64 MiB and the minimum is 8 MiB.

          - **BlockSizeBytes** *(integer) --*

            The Hadoop Distributed File System (HDFS) block size. This is useful if you intend to
            copy the data from Amazon S3 to HDFS before querying. The default is 256 MiB and the
            minimum is 64 MiB. Kinesis Data Firehose uses this value for padding calculations.

          - **RowIndexStride** *(integer) --*

            The number of rows between index entries. The default is 10,000 and the minimum is
            1,000.

          - **EnablePadding** *(boolean) --*

            Set this to ``true`` to indicate that you want stripes to be padded to the HDFS block
            boundaries. This is useful if you intend to copy the data from Amazon S3 to HDFS before
            querying. The default is ``false`` .

          - **PaddingTolerance** *(float) --*

            A number between 0 and 1 that defines the tolerance for block padding as a decimal
            fraction of stripe size. The default value is 0.05, which means 5 percent of stripe
            size.

            For the default values of 64 MiB ORC stripes and 256 MiB HDFS blocks, the default block
            padding tolerance of 5 percent reserves a maximum of 3.2 MiB for padding within the 256
            MiB block. In such a case, if the available size within the block is more than 3.2 MiB,
            a new, smaller stripe is inserted to fit within that space. This ensures that no stripe
            crosses block boundaries and causes remote reads within a node-local task.

            Kinesis Data Firehose ignores this parameter when  OrcSerDe$EnablePadding is ``false`` .

          - **Compression** *(string) --*

            The compression code to use over data blocks. The default is ``SNAPPY`` .

          - **BloomFilterColumns** *(list) --*

            The column names for which you want Kinesis Data Firehose to create bloom filters. The
            default is ``null`` .

            - *(string) --*

          - **BloomFilterFalsePositiveProbability** *(float) --*

            The Bloom filter false positive probability (FPP). The lower the FPP, the bigger the
            Bloom filter. The default value is 0.05, the minimum is 0, and the maximum is 1.

          - **DictionaryKeyThreshold** *(float) --*

            Represents the fraction of the total number of non-null rows. To turn off dictionary
            encoding, set this fraction to a number that is less than the number of distinct keys
            in a dictionary. To always use dictionary encoding, set this threshold to 1.

          - **FormatVersion** *(string) --*

            The version of the file to write. The possible values are ``V0_11`` and ``V0_12`` . The
            default is ``V0_12`` .

    - **Enabled** *(boolean) --*

      Defaults to ``true`` . Set it to ``false`` if you want to disable format conversion while
      preserving the configuration details.
    """


_ClientUpdateDestinationExtendedS3DestinationUpdateEncryptionConfigurationKMSEncryptionConfigTypeDef = TypedDict(
    "_ClientUpdateDestinationExtendedS3DestinationUpdateEncryptionConfigurationKMSEncryptionConfigTypeDef",
    {"AWSKMSKeyARN": str},
)


class ClientUpdateDestinationExtendedS3DestinationUpdateEncryptionConfigurationKMSEncryptionConfigTypeDef(
    _ClientUpdateDestinationExtendedS3DestinationUpdateEncryptionConfigurationKMSEncryptionConfigTypeDef
):
    """
    Type definition for `ClientUpdateDestinationExtendedS3DestinationUpdateEncryptionConfiguration` `KMSEncryptionConfig`

    The encryption key.

    - **AWSKMSKeyARN** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region as
      the destination Amazon S3 bucket. For more information, see `Amazon Resource Names (ARNs)
      and AWS Service Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
    """


_ClientUpdateDestinationExtendedS3DestinationUpdateEncryptionConfigurationTypeDef = TypedDict(
    "_ClientUpdateDestinationExtendedS3DestinationUpdateEncryptionConfigurationTypeDef",
    {
        "NoEncryptionConfig": str,
        "KMSEncryptionConfig": ClientUpdateDestinationExtendedS3DestinationUpdateEncryptionConfigurationKMSEncryptionConfigTypeDef,
    },
    total=False,
)


class ClientUpdateDestinationExtendedS3DestinationUpdateEncryptionConfigurationTypeDef(
    _ClientUpdateDestinationExtendedS3DestinationUpdateEncryptionConfigurationTypeDef
):
    """
    Type definition for `ClientUpdateDestinationExtendedS3DestinationUpdate` `EncryptionConfiguration`

    The encryption configuration. If no value is specified, the default is no encryption.

    - **NoEncryptionConfig** *(string) --*

      Specifically override existing encryption information to ensure that no encryption is used.

    - **KMSEncryptionConfig** *(dict) --*

      The encryption key.

      - **AWSKMSKeyARN** *(string) --* **[REQUIRED]**

        The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region as
        the destination Amazon S3 bucket. For more information, see `Amazon Resource Names (ARNs)
        and AWS Service Namespaces
        <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
    """


_ClientUpdateDestinationExtendedS3DestinationUpdateProcessingConfigurationProcessorsParametersTypeDef = TypedDict(
    "_ClientUpdateDestinationExtendedS3DestinationUpdateProcessingConfigurationProcessorsParametersTypeDef",
    {"ParameterName": str, "ParameterValue": str},
)


class ClientUpdateDestinationExtendedS3DestinationUpdateProcessingConfigurationProcessorsParametersTypeDef(
    _ClientUpdateDestinationExtendedS3DestinationUpdateProcessingConfigurationProcessorsParametersTypeDef
):
    """
    Type definition for `ClientUpdateDestinationExtendedS3DestinationUpdateProcessingConfigurationProcessors` `Parameters`

    Describes the processor parameter.

    - **ParameterName** *(string) --* **[REQUIRED]**

      The name of the parameter.

    - **ParameterValue** *(string) --* **[REQUIRED]**

      The parameter value.
    """


_RequiredClientUpdateDestinationExtendedS3DestinationUpdateProcessingConfigurationProcessorsTypeDef = TypedDict(
    "_RequiredClientUpdateDestinationExtendedS3DestinationUpdateProcessingConfigurationProcessorsTypeDef",
    {"Type": str},
)
_OptionalClientUpdateDestinationExtendedS3DestinationUpdateProcessingConfigurationProcessorsTypeDef = TypedDict(
    "_OptionalClientUpdateDestinationExtendedS3DestinationUpdateProcessingConfigurationProcessorsTypeDef",
    {
        "Parameters": List[
            ClientUpdateDestinationExtendedS3DestinationUpdateProcessingConfigurationProcessorsParametersTypeDef
        ]
    },
    total=False,
)


class ClientUpdateDestinationExtendedS3DestinationUpdateProcessingConfigurationProcessorsTypeDef(
    _RequiredClientUpdateDestinationExtendedS3DestinationUpdateProcessingConfigurationProcessorsTypeDef,
    _OptionalClientUpdateDestinationExtendedS3DestinationUpdateProcessingConfigurationProcessorsTypeDef,
):
    """
    Type definition for `ClientUpdateDestinationExtendedS3DestinationUpdateProcessingConfiguration` `Processors`

    Describes a data processor.

    - **Type** *(string) --* **[REQUIRED]**

      The type of processor.

    - **Parameters** *(list) --*

      The processor parameters.

      - *(dict) --*

        Describes the processor parameter.

        - **ParameterName** *(string) --* **[REQUIRED]**

          The name of the parameter.

        - **ParameterValue** *(string) --* **[REQUIRED]**

          The parameter value.
    """


_ClientUpdateDestinationExtendedS3DestinationUpdateProcessingConfigurationTypeDef = TypedDict(
    "_ClientUpdateDestinationExtendedS3DestinationUpdateProcessingConfigurationTypeDef",
    {
        "Enabled": bool,
        "Processors": List[
            ClientUpdateDestinationExtendedS3DestinationUpdateProcessingConfigurationProcessorsTypeDef
        ],
    },
    total=False,
)


class ClientUpdateDestinationExtendedS3DestinationUpdateProcessingConfigurationTypeDef(
    _ClientUpdateDestinationExtendedS3DestinationUpdateProcessingConfigurationTypeDef
):
    """
    Type definition for `ClientUpdateDestinationExtendedS3DestinationUpdate` `ProcessingConfiguration`

    The data processing configuration.

    - **Enabled** *(boolean) --*

      Enables or disables data processing.

    - **Processors** *(list) --*

      The data processors.

      - *(dict) --*

        Describes a data processor.

        - **Type** *(string) --* **[REQUIRED]**

          The type of processor.

        - **Parameters** *(list) --*

          The processor parameters.

          - *(dict) --*

            Describes the processor parameter.

            - **ParameterName** *(string) --* **[REQUIRED]**

              The name of the parameter.

            - **ParameterValue** *(string) --* **[REQUIRED]**

              The parameter value.
    """


_ClientUpdateDestinationExtendedS3DestinationUpdateS3BackupUpdateBufferingHintsTypeDef = TypedDict(
    "_ClientUpdateDestinationExtendedS3DestinationUpdateS3BackupUpdateBufferingHintsTypeDef",
    {"SizeInMBs": int, "IntervalInSeconds": int},
    total=False,
)


class ClientUpdateDestinationExtendedS3DestinationUpdateS3BackupUpdateBufferingHintsTypeDef(
    _ClientUpdateDestinationExtendedS3DestinationUpdateS3BackupUpdateBufferingHintsTypeDef
):
    """
    Type definition for `ClientUpdateDestinationExtendedS3DestinationUpdateS3BackupUpdate` `BufferingHints`

    The buffering option. If no value is specified, ``BufferingHints`` object default values are
    used.

    - **SizeInMBs** *(integer) --*

      Buffer incoming data to the specified size, in MiBs, before delivering it to the
      destination. The default value is 5. This parameter is optional but if you specify a value
      for it, you must also specify a value for ``IntervalInSeconds`` , and vice versa.

      We recommend setting this parameter to a value greater than the amount of data you
      typically ingest into the delivery stream in 10 seconds. For example, if you typically
      ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

    - **IntervalInSeconds** *(integer) --*

      Buffer incoming data for the specified period of time, in seconds, before delivering it to
      the destination. The default value is 300. This parameter is optional but if you specify a
      value for it, you must also specify a value for ``SizeInMBs`` , and vice versa.
    """


_ClientUpdateDestinationExtendedS3DestinationUpdateS3BackupUpdateCloudWatchLoggingOptionsTypeDef = TypedDict(
    "_ClientUpdateDestinationExtendedS3DestinationUpdateS3BackupUpdateCloudWatchLoggingOptionsTypeDef",
    {"Enabled": bool, "LogGroupName": str, "LogStreamName": str},
    total=False,
)


class ClientUpdateDestinationExtendedS3DestinationUpdateS3BackupUpdateCloudWatchLoggingOptionsTypeDef(
    _ClientUpdateDestinationExtendedS3DestinationUpdateS3BackupUpdateCloudWatchLoggingOptionsTypeDef
):
    """
    Type definition for `ClientUpdateDestinationExtendedS3DestinationUpdateS3BackupUpdate` `CloudWatchLoggingOptions`

    The CloudWatch logging options for your delivery stream.

    - **Enabled** *(boolean) --*

      Enables or disables CloudWatch logging.

    - **LogGroupName** *(string) --*

      The CloudWatch group name for logging. This value is required if CloudWatch logging is
      enabled.

    - **LogStreamName** *(string) --*

      The CloudWatch log stream name for logging. This value is required if CloudWatch logging is
      enabled.
    """


_ClientUpdateDestinationExtendedS3DestinationUpdateS3BackupUpdateEncryptionConfigurationKMSEncryptionConfigTypeDef = TypedDict(
    "_ClientUpdateDestinationExtendedS3DestinationUpdateS3BackupUpdateEncryptionConfigurationKMSEncryptionConfigTypeDef",
    {"AWSKMSKeyARN": str},
)


class ClientUpdateDestinationExtendedS3DestinationUpdateS3BackupUpdateEncryptionConfigurationKMSEncryptionConfigTypeDef(
    _ClientUpdateDestinationExtendedS3DestinationUpdateS3BackupUpdateEncryptionConfigurationKMSEncryptionConfigTypeDef
):
    """
    Type definition for `ClientUpdateDestinationExtendedS3DestinationUpdateS3BackupUpdateEncryptionConfiguration` `KMSEncryptionConfig`

    The encryption key.

    - **AWSKMSKeyARN** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region
      as the destination Amazon S3 bucket. For more information, see `Amazon Resource Names
      (ARNs) and AWS Service Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
    """


_ClientUpdateDestinationExtendedS3DestinationUpdateS3BackupUpdateEncryptionConfigurationTypeDef = TypedDict(
    "_ClientUpdateDestinationExtendedS3DestinationUpdateS3BackupUpdateEncryptionConfigurationTypeDef",
    {
        "NoEncryptionConfig": str,
        "KMSEncryptionConfig": ClientUpdateDestinationExtendedS3DestinationUpdateS3BackupUpdateEncryptionConfigurationKMSEncryptionConfigTypeDef,
    },
    total=False,
)


class ClientUpdateDestinationExtendedS3DestinationUpdateS3BackupUpdateEncryptionConfigurationTypeDef(
    _ClientUpdateDestinationExtendedS3DestinationUpdateS3BackupUpdateEncryptionConfigurationTypeDef
):
    """
    Type definition for `ClientUpdateDestinationExtendedS3DestinationUpdateS3BackupUpdate` `EncryptionConfiguration`

    The encryption configuration. If no value is specified, the default is no encryption.

    - **NoEncryptionConfig** *(string) --*

      Specifically override existing encryption information to ensure that no encryption is used.

    - **KMSEncryptionConfig** *(dict) --*

      The encryption key.

      - **AWSKMSKeyARN** *(string) --* **[REQUIRED]**

        The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region
        as the destination Amazon S3 bucket. For more information, see `Amazon Resource Names
        (ARNs) and AWS Service Namespaces
        <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
    """


_ClientUpdateDestinationExtendedS3DestinationUpdateS3BackupUpdateTypeDef = TypedDict(
    "_ClientUpdateDestinationExtendedS3DestinationUpdateS3BackupUpdateTypeDef",
    {
        "RoleARN": str,
        "BucketARN": str,
        "Prefix": str,
        "ErrorOutputPrefix": str,
        "BufferingHints": ClientUpdateDestinationExtendedS3DestinationUpdateS3BackupUpdateBufferingHintsTypeDef,
        "CompressionFormat": str,
        "EncryptionConfiguration": ClientUpdateDestinationExtendedS3DestinationUpdateS3BackupUpdateEncryptionConfigurationTypeDef,
        "CloudWatchLoggingOptions": ClientUpdateDestinationExtendedS3DestinationUpdateS3BackupUpdateCloudWatchLoggingOptionsTypeDef,
    },
    total=False,
)


class ClientUpdateDestinationExtendedS3DestinationUpdateS3BackupUpdateTypeDef(
    _ClientUpdateDestinationExtendedS3DestinationUpdateS3BackupUpdateTypeDef
):
    """
    Type definition for `ClientUpdateDestinationExtendedS3DestinationUpdate` `S3BackupUpdate`

    The Amazon S3 destination for backup.

    - **RoleARN** *(string) --*

      The Amazon Resource Name (ARN) of the AWS credentials. For more information, see `Amazon
      Resource Names (ARNs) and AWS Service Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

    - **BucketARN** *(string) --*

      The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs) and AWS
      Service Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

    - **Prefix** *(string) --*

      The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered Amazon S3 files.
      You can also specify a custom prefix, as described in `Custom Prefixes for Amazon S3 Objects
      <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

    - **ErrorOutputPrefix** *(string) --*

      A prefix that Kinesis Data Firehose evaluates and adds to failed records before writing them
      to S3. This prefix appears immediately following the bucket name. For information about how
      to specify this prefix, see `Custom Prefixes for Amazon S3 Objects
      <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

    - **BufferingHints** *(dict) --*

      The buffering option. If no value is specified, ``BufferingHints`` object default values are
      used.

      - **SizeInMBs** *(integer) --*

        Buffer incoming data to the specified size, in MiBs, before delivering it to the
        destination. The default value is 5. This parameter is optional but if you specify a value
        for it, you must also specify a value for ``IntervalInSeconds`` , and vice versa.

        We recommend setting this parameter to a value greater than the amount of data you
        typically ingest into the delivery stream in 10 seconds. For example, if you typically
        ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

      - **IntervalInSeconds** *(integer) --*

        Buffer incoming data for the specified period of time, in seconds, before delivering it to
        the destination. The default value is 300. This parameter is optional but if you specify a
        value for it, you must also specify a value for ``SizeInMBs`` , and vice versa.

    - **CompressionFormat** *(string) --*

      The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .

      The compression formats ``SNAPPY`` or ``ZIP`` cannot be specified for Amazon Redshift
      destinations because they are not supported by the Amazon Redshift ``COPY`` operation that
      reads from the S3 bucket.

    - **EncryptionConfiguration** *(dict) --*

      The encryption configuration. If no value is specified, the default is no encryption.

      - **NoEncryptionConfig** *(string) --*

        Specifically override existing encryption information to ensure that no encryption is used.

      - **KMSEncryptionConfig** *(dict) --*

        The encryption key.

        - **AWSKMSKeyARN** *(string) --* **[REQUIRED]**

          The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region
          as the destination Amazon S3 bucket. For more information, see `Amazon Resource Names
          (ARNs) and AWS Service Namespaces
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

    - **CloudWatchLoggingOptions** *(dict) --*

      The CloudWatch logging options for your delivery stream.

      - **Enabled** *(boolean) --*

        Enables or disables CloudWatch logging.

      - **LogGroupName** *(string) --*

        The CloudWatch group name for logging. This value is required if CloudWatch logging is
        enabled.

      - **LogStreamName** *(string) --*

        The CloudWatch log stream name for logging. This value is required if CloudWatch logging is
        enabled.
    """


_ClientUpdateDestinationExtendedS3DestinationUpdateTypeDef = TypedDict(
    "_ClientUpdateDestinationExtendedS3DestinationUpdateTypeDef",
    {
        "RoleARN": str,
        "BucketARN": str,
        "Prefix": str,
        "ErrorOutputPrefix": str,
        "BufferingHints": ClientUpdateDestinationExtendedS3DestinationUpdateBufferingHintsTypeDef,
        "CompressionFormat": str,
        "EncryptionConfiguration": ClientUpdateDestinationExtendedS3DestinationUpdateEncryptionConfigurationTypeDef,
        "CloudWatchLoggingOptions": ClientUpdateDestinationExtendedS3DestinationUpdateCloudWatchLoggingOptionsTypeDef,
        "ProcessingConfiguration": ClientUpdateDestinationExtendedS3DestinationUpdateProcessingConfigurationTypeDef,
        "S3BackupMode": str,
        "S3BackupUpdate": ClientUpdateDestinationExtendedS3DestinationUpdateS3BackupUpdateTypeDef,
        "DataFormatConversionConfiguration": ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationTypeDef,
    },
    total=False,
)


class ClientUpdateDestinationExtendedS3DestinationUpdateTypeDef(
    _ClientUpdateDestinationExtendedS3DestinationUpdateTypeDef
):
    """
    Type definition for `ClientUpdateDestination` `ExtendedS3DestinationUpdate`

    Describes an update for a destination in Amazon S3.

    - **RoleARN** *(string) --*

      The Amazon Resource Name (ARN) of the AWS credentials. For more information, see `Amazon
      Resource Names (ARNs) and AWS Service Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

    - **BucketARN** *(string) --*

      The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs) and AWS
      Service Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

    - **Prefix** *(string) --*

      The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered Amazon S3 files. You
      can also specify a custom prefix, as described in `Custom Prefixes for Amazon S3 Objects
      <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

    - **ErrorOutputPrefix** *(string) --*

      A prefix that Kinesis Data Firehose evaluates and adds to failed records before writing them to
      S3. This prefix appears immediately following the bucket name. For information about how to
      specify this prefix, see `Custom Prefixes for Amazon S3 Objects
      <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

    - **BufferingHints** *(dict) --*

      The buffering option.

      - **SizeInMBs** *(integer) --*

        Buffer incoming data to the specified size, in MiBs, before delivering it to the destination.
        The default value is 5. This parameter is optional but if you specify a value for it, you
        must also specify a value for ``IntervalInSeconds`` , and vice versa.

        We recommend setting this parameter to a value greater than the amount of data you typically
        ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1
        MiB/sec, the value should be 10 MiB or higher.

      - **IntervalInSeconds** *(integer) --*

        Buffer incoming data for the specified period of time, in seconds, before delivering it to
        the destination. The default value is 300. This parameter is optional but if you specify a
        value for it, you must also specify a value for ``SizeInMBs`` , and vice versa.

    - **CompressionFormat** *(string) --*

      The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .

    - **EncryptionConfiguration** *(dict) --*

      The encryption configuration. If no value is specified, the default is no encryption.

      - **NoEncryptionConfig** *(string) --*

        Specifically override existing encryption information to ensure that no encryption is used.

      - **KMSEncryptionConfig** *(dict) --*

        The encryption key.

        - **AWSKMSKeyARN** *(string) --* **[REQUIRED]**

          The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region as
          the destination Amazon S3 bucket. For more information, see `Amazon Resource Names (ARNs)
          and AWS Service Namespaces
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

    - **CloudWatchLoggingOptions** *(dict) --*

      The Amazon CloudWatch logging options for your delivery stream.

      - **Enabled** *(boolean) --*

        Enables or disables CloudWatch logging.

      - **LogGroupName** *(string) --*

        The CloudWatch group name for logging. This value is required if CloudWatch logging is
        enabled.

      - **LogStreamName** *(string) --*

        The CloudWatch log stream name for logging. This value is required if CloudWatch logging is
        enabled.

    - **ProcessingConfiguration** *(dict) --*

      The data processing configuration.

      - **Enabled** *(boolean) --*

        Enables or disables data processing.

      - **Processors** *(list) --*

        The data processors.

        - *(dict) --*

          Describes a data processor.

          - **Type** *(string) --* **[REQUIRED]**

            The type of processor.

          - **Parameters** *(list) --*

            The processor parameters.

            - *(dict) --*

              Describes the processor parameter.

              - **ParameterName** *(string) --* **[REQUIRED]**

                The name of the parameter.

              - **ParameterValue** *(string) --* **[REQUIRED]**

                The parameter value.

    - **S3BackupMode** *(string) --*

      Enables or disables Amazon S3 backup mode.

    - **S3BackupUpdate** *(dict) --*

      The Amazon S3 destination for backup.

      - **RoleARN** *(string) --*

        The Amazon Resource Name (ARN) of the AWS credentials. For more information, see `Amazon
        Resource Names (ARNs) and AWS Service Namespaces
        <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

      - **BucketARN** *(string) --*

        The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs) and AWS
        Service Namespaces
        <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

      - **Prefix** *(string) --*

        The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered Amazon S3 files.
        You can also specify a custom prefix, as described in `Custom Prefixes for Amazon S3 Objects
        <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

      - **ErrorOutputPrefix** *(string) --*

        A prefix that Kinesis Data Firehose evaluates and adds to failed records before writing them
        to S3. This prefix appears immediately following the bucket name. For information about how
        to specify this prefix, see `Custom Prefixes for Amazon S3 Objects
        <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

      - **BufferingHints** *(dict) --*

        The buffering option. If no value is specified, ``BufferingHints`` object default values are
        used.

        - **SizeInMBs** *(integer) --*

          Buffer incoming data to the specified size, in MiBs, before delivering it to the
          destination. The default value is 5. This parameter is optional but if you specify a value
          for it, you must also specify a value for ``IntervalInSeconds`` , and vice versa.

          We recommend setting this parameter to a value greater than the amount of data you
          typically ingest into the delivery stream in 10 seconds. For example, if you typically
          ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

        - **IntervalInSeconds** *(integer) --*

          Buffer incoming data for the specified period of time, in seconds, before delivering it to
          the destination. The default value is 300. This parameter is optional but if you specify a
          value for it, you must also specify a value for ``SizeInMBs`` , and vice versa.

      - **CompressionFormat** *(string) --*

        The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .

        The compression formats ``SNAPPY`` or ``ZIP`` cannot be specified for Amazon Redshift
        destinations because they are not supported by the Amazon Redshift ``COPY`` operation that
        reads from the S3 bucket.

      - **EncryptionConfiguration** *(dict) --*

        The encryption configuration. If no value is specified, the default is no encryption.

        - **NoEncryptionConfig** *(string) --*

          Specifically override existing encryption information to ensure that no encryption is used.

        - **KMSEncryptionConfig** *(dict) --*

          The encryption key.

          - **AWSKMSKeyARN** *(string) --* **[REQUIRED]**

            The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region
            as the destination Amazon S3 bucket. For more information, see `Amazon Resource Names
            (ARNs) and AWS Service Namespaces
            <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

      - **CloudWatchLoggingOptions** *(dict) --*

        The CloudWatch logging options for your delivery stream.

        - **Enabled** *(boolean) --*

          Enables or disables CloudWatch logging.

        - **LogGroupName** *(string) --*

          The CloudWatch group name for logging. This value is required if CloudWatch logging is
          enabled.

        - **LogStreamName** *(string) --*

          The CloudWatch log stream name for logging. This value is required if CloudWatch logging is
          enabled.

    - **DataFormatConversionConfiguration** *(dict) --*

      The serializer, deserializer, and schema for converting data from the JSON format to the
      Parquet or ORC format before writing it to Amazon S3.

      - **SchemaConfiguration** *(dict) --*

        Specifies the AWS Glue Data Catalog table that contains the column information.

        - **RoleARN** *(string) --*

          The role that Kinesis Data Firehose can use to access AWS Glue. This role must be in the
          same account you use for Kinesis Data Firehose. Cross-account roles aren't allowed.

        - **CatalogId** *(string) --*

          The ID of the AWS Glue Data Catalog. If you don't supply this, the AWS account ID is used
          by default.

        - **DatabaseName** *(string) --*

          Specifies the name of the AWS Glue database that contains the schema for the output data.

        - **TableName** *(string) --*

          Specifies the AWS Glue table that contains the column information that constitutes your
          data schema.

        - **Region** *(string) --*

          If you don't specify an AWS Region, the default is the current Region.

        - **VersionId** *(string) --*

          Specifies the table version for the output data schema. If you don't specify this version
          ID, or if you set it to ``LATEST`` , Kinesis Data Firehose uses the most recent version.
          This means that any updates to the table are automatically picked up.

      - **InputFormatConfiguration** *(dict) --*

        Specifies the deserializer that you want Kinesis Data Firehose to use to convert the format
        of your data from JSON.

        - **Deserializer** *(dict) --*

          Specifies which deserializer to use. You can choose either the Apache Hive JSON SerDe or
          the OpenX JSON SerDe. If both are non-null, the server rejects the request.

          - **OpenXJsonSerDe** *(dict) --*

            The OpenX SerDe. Used by Kinesis Data Firehose for deserializing data, which means
            converting it from the JSON format in preparation for serializing it to the Parquet or
            ORC format. This is one of two deserializers you can choose, depending on which one
            offers the functionality you need. The other option is the native Hive / HCatalog
            JsonSerDe.

            - **ConvertDotsInJsonKeysToUnderscores** *(boolean) --*

              When set to ``true`` , specifies that the names of the keys include dots and that you
              want Kinesis Data Firehose to replace them with underscores. This is useful because
              Apache Hive does not allow dots in column names. For example, if the JSON contains a
              key whose name is "a.b", you can define the column name to be "a_b" when using this
              option.

              The default is ``false`` .

            - **CaseInsensitive** *(boolean) --*

              When set to ``true`` , which is the default, Kinesis Data Firehose converts JSON keys
              to lowercase before deserializing them.

            - **ColumnToJsonKeyMappings** *(dict) --*

              Maps column names to JSON keys that aren't identical to the column names. This is
              useful when the JSON contains keys that are Hive keywords. For example, ``timestamp``
              is a Hive keyword. If you have a JSON key named ``timestamp`` , set this parameter to
              ``{"ts": "timestamp"}`` to map this key to a column named ``ts`` .

              - *(string) --*

                - *(string) --*

          - **HiveJsonSerDe** *(dict) --*

            The native Hive / HCatalog JsonSerDe. Used by Kinesis Data Firehose for deserializing
            data, which means converting it from the JSON format in preparation for serializing it to
            the Parquet or ORC format. This is one of two deserializers you can choose, depending on
            which one offers the functionality you need. The other option is the OpenX SerDe.

            - **TimestampFormats** *(list) --*

              Indicates how you want Kinesis Data Firehose to parse the date and timestamps that may
              be present in your input data JSON. To specify these format strings, follow the pattern
              syntax of JodaTime's DateTimeFormat format strings. For more information, see `Class
              DateTimeFormat
              <https://www.joda.org/joda-time/apidocs/org/joda/time/format/DateTimeFormat.html>`__ .
              You can also use the special value ``millis`` to parse timestamps in epoch
              milliseconds. If you don't specify a format, Kinesis Data Firehose uses
              ``java.sql.Timestamp::valueOf`` by default.

              - *(string) --*

      - **OutputFormatConfiguration** *(dict) --*

        Specifies the serializer that you want Kinesis Data Firehose to use to convert the format of
        your data to the Parquet or ORC format.

        - **Serializer** *(dict) --*

          Specifies which serializer to use. You can choose either the ORC SerDe or the Parquet
          SerDe. If both are non-null, the server rejects the request.

          - **ParquetSerDe** *(dict) --*

            A serializer to use for converting data to the Parquet format before storing it in Amazon
            S3. For more information, see `Apache Parquet
            <https://parquet.apache.org/documentation/latest/>`__ .

            - **BlockSizeBytes** *(integer) --*

              The Hadoop Distributed File System (HDFS) block size. This is useful if you intend to
              copy the data from Amazon S3 to HDFS before querying. The default is 256 MiB and the
              minimum is 64 MiB. Kinesis Data Firehose uses this value for padding calculations.

            - **PageSizeBytes** *(integer) --*

              The Parquet page size. Column chunks are divided into pages. A page is conceptually an
              indivisible unit (in terms of compression and encoding). The minimum value is 64 KiB
              and the default is 1 MiB.

            - **Compression** *(string) --*

              The compression code to use over data blocks. The possible values are ``UNCOMPRESSED``
              , ``SNAPPY`` , and ``GZIP`` , with the default being ``SNAPPY`` . Use ``SNAPPY`` for
              higher decompression speed. Use ``GZIP`` if the compression ration is more important
              than speed.

            - **EnableDictionaryCompression** *(boolean) --*

              Indicates whether to enable dictionary compression.

            - **MaxPaddingBytes** *(integer) --*

              The maximum amount of padding to apply. This is useful if you intend to copy the data
              from Amazon S3 to HDFS before querying. The default is 0.

            - **WriterVersion** *(string) --*

              Indicates the version of row format to output. The possible values are ``V1`` and
              ``V2`` . The default is ``V1`` .

          - **OrcSerDe** *(dict) --*

            A serializer to use for converting data to the ORC format before storing it in Amazon S3.
            For more information, see `Apache ORC <https://orc.apache.org/docs/>`__ .

            - **StripeSizeBytes** *(integer) --*

              The number of bytes in each stripe. The default is 64 MiB and the minimum is 8 MiB.

            - **BlockSizeBytes** *(integer) --*

              The Hadoop Distributed File System (HDFS) block size. This is useful if you intend to
              copy the data from Amazon S3 to HDFS before querying. The default is 256 MiB and the
              minimum is 64 MiB. Kinesis Data Firehose uses this value for padding calculations.

            - **RowIndexStride** *(integer) --*

              The number of rows between index entries. The default is 10,000 and the minimum is
              1,000.

            - **EnablePadding** *(boolean) --*

              Set this to ``true`` to indicate that you want stripes to be padded to the HDFS block
              boundaries. This is useful if you intend to copy the data from Amazon S3 to HDFS before
              querying. The default is ``false`` .

            - **PaddingTolerance** *(float) --*

              A number between 0 and 1 that defines the tolerance for block padding as a decimal
              fraction of stripe size. The default value is 0.05, which means 5 percent of stripe
              size.

              For the default values of 64 MiB ORC stripes and 256 MiB HDFS blocks, the default block
              padding tolerance of 5 percent reserves a maximum of 3.2 MiB for padding within the 256
              MiB block. In such a case, if the available size within the block is more than 3.2 MiB,
              a new, smaller stripe is inserted to fit within that space. This ensures that no stripe
              crosses block boundaries and causes remote reads within a node-local task.

              Kinesis Data Firehose ignores this parameter when  OrcSerDe$EnablePadding is ``false`` .

            - **Compression** *(string) --*

              The compression code to use over data blocks. The default is ``SNAPPY`` .

            - **BloomFilterColumns** *(list) --*

              The column names for which you want Kinesis Data Firehose to create bloom filters. The
              default is ``null`` .

              - *(string) --*

            - **BloomFilterFalsePositiveProbability** *(float) --*

              The Bloom filter false positive probability (FPP). The lower the FPP, the bigger the
              Bloom filter. The default value is 0.05, the minimum is 0, and the maximum is 1.

            - **DictionaryKeyThreshold** *(float) --*

              Represents the fraction of the total number of non-null rows. To turn off dictionary
              encoding, set this fraction to a number that is less than the number of distinct keys
              in a dictionary. To always use dictionary encoding, set this threshold to 1.

            - **FormatVersion** *(string) --*

              The version of the file to write. The possible values are ``V0_11`` and ``V0_12`` . The
              default is ``V0_12`` .

      - **Enabled** *(boolean) --*

        Defaults to ``true`` . Set it to ``false`` if you want to disable format conversion while
        preserving the configuration details.
    """


_ClientUpdateDestinationRedshiftDestinationUpdateCloudWatchLoggingOptionsTypeDef = TypedDict(
    "_ClientUpdateDestinationRedshiftDestinationUpdateCloudWatchLoggingOptionsTypeDef",
    {"Enabled": bool, "LogGroupName": str, "LogStreamName": str},
    total=False,
)


class ClientUpdateDestinationRedshiftDestinationUpdateCloudWatchLoggingOptionsTypeDef(
    _ClientUpdateDestinationRedshiftDestinationUpdateCloudWatchLoggingOptionsTypeDef
):
    """
    Type definition for `ClientUpdateDestinationRedshiftDestinationUpdate` `CloudWatchLoggingOptions`

    The Amazon CloudWatch logging options for your delivery stream.

    - **Enabled** *(boolean) --*

      Enables or disables CloudWatch logging.

    - **LogGroupName** *(string) --*

      The CloudWatch group name for logging. This value is required if CloudWatch logging is
      enabled.

    - **LogStreamName** *(string) --*

      The CloudWatch log stream name for logging. This value is required if CloudWatch logging is
      enabled.
    """


_RequiredClientUpdateDestinationRedshiftDestinationUpdateCopyCommandTypeDef = TypedDict(
    "_RequiredClientUpdateDestinationRedshiftDestinationUpdateCopyCommandTypeDef",
    {"DataTableName": str},
)
_OptionalClientUpdateDestinationRedshiftDestinationUpdateCopyCommandTypeDef = TypedDict(
    "_OptionalClientUpdateDestinationRedshiftDestinationUpdateCopyCommandTypeDef",
    {"DataTableColumns": str, "CopyOptions": str},
    total=False,
)


class ClientUpdateDestinationRedshiftDestinationUpdateCopyCommandTypeDef(
    _RequiredClientUpdateDestinationRedshiftDestinationUpdateCopyCommandTypeDef,
    _OptionalClientUpdateDestinationRedshiftDestinationUpdateCopyCommandTypeDef,
):
    """
    Type definition for `ClientUpdateDestinationRedshiftDestinationUpdate` `CopyCommand`

    The ``COPY`` command.

    - **DataTableName** *(string) --* **[REQUIRED]**

      The name of the target table. The table must already exist in the database.

    - **DataTableColumns** *(string) --*

      A comma-separated list of column names.

    - **CopyOptions** *(string) --*

      Optional parameters to use with the Amazon Redshift ``COPY`` command. For more information,
      see the "Optional Parameters" section of `Amazon Redshift COPY command
      <https://docs.aws.amazon.com/redshift/latest/dg/r_COPY.html>`__ . Some possible examples that
      would apply to Kinesis Data Firehose are as follows:

       ``delimiter '\\t' lzop;`` - fields are delimited with "\\t" (TAB character) and compressed
       using lzop.

       ``delimiter '|'`` - fields are delimited with "|" (this is the default delimiter).

       ``delimiter '|' escape`` - the delimiter should be escaped.

       ``fixedwidth 'venueid:3,venuename:25,venuecity:12,venuestate:2,venueseats:6'`` - fields are
       fixed width in the source, with each width specified after every column in the table.

       ``JSON 's3://mybucket/jsonpaths.txt'`` - data is in JSON format, and the path specified is
       the format of the data.

      For more examples, see `Amazon Redshift COPY command examples
      <https://docs.aws.amazon.com/redshift/latest/dg/r_COPY_command_examples.html>`__ .
    """


_ClientUpdateDestinationRedshiftDestinationUpdateProcessingConfigurationProcessorsParametersTypeDef = TypedDict(
    "_ClientUpdateDestinationRedshiftDestinationUpdateProcessingConfigurationProcessorsParametersTypeDef",
    {"ParameterName": str, "ParameterValue": str},
)


class ClientUpdateDestinationRedshiftDestinationUpdateProcessingConfigurationProcessorsParametersTypeDef(
    _ClientUpdateDestinationRedshiftDestinationUpdateProcessingConfigurationProcessorsParametersTypeDef
):
    """
    Type definition for `ClientUpdateDestinationRedshiftDestinationUpdateProcessingConfigurationProcessors` `Parameters`

    Describes the processor parameter.

    - **ParameterName** *(string) --* **[REQUIRED]**

      The name of the parameter.

    - **ParameterValue** *(string) --* **[REQUIRED]**

      The parameter value.
    """


_RequiredClientUpdateDestinationRedshiftDestinationUpdateProcessingConfigurationProcessorsTypeDef = TypedDict(
    "_RequiredClientUpdateDestinationRedshiftDestinationUpdateProcessingConfigurationProcessorsTypeDef",
    {"Type": str},
)
_OptionalClientUpdateDestinationRedshiftDestinationUpdateProcessingConfigurationProcessorsTypeDef = TypedDict(
    "_OptionalClientUpdateDestinationRedshiftDestinationUpdateProcessingConfigurationProcessorsTypeDef",
    {
        "Parameters": List[
            ClientUpdateDestinationRedshiftDestinationUpdateProcessingConfigurationProcessorsParametersTypeDef
        ]
    },
    total=False,
)


class ClientUpdateDestinationRedshiftDestinationUpdateProcessingConfigurationProcessorsTypeDef(
    _RequiredClientUpdateDestinationRedshiftDestinationUpdateProcessingConfigurationProcessorsTypeDef,
    _OptionalClientUpdateDestinationRedshiftDestinationUpdateProcessingConfigurationProcessorsTypeDef,
):
    """
    Type definition for `ClientUpdateDestinationRedshiftDestinationUpdateProcessingConfiguration` `Processors`

    Describes a data processor.

    - **Type** *(string) --* **[REQUIRED]**

      The type of processor.

    - **Parameters** *(list) --*

      The processor parameters.

      - *(dict) --*

        Describes the processor parameter.

        - **ParameterName** *(string) --* **[REQUIRED]**

          The name of the parameter.

        - **ParameterValue** *(string) --* **[REQUIRED]**

          The parameter value.
    """


_ClientUpdateDestinationRedshiftDestinationUpdateProcessingConfigurationTypeDef = TypedDict(
    "_ClientUpdateDestinationRedshiftDestinationUpdateProcessingConfigurationTypeDef",
    {
        "Enabled": bool,
        "Processors": List[
            ClientUpdateDestinationRedshiftDestinationUpdateProcessingConfigurationProcessorsTypeDef
        ],
    },
    total=False,
)


class ClientUpdateDestinationRedshiftDestinationUpdateProcessingConfigurationTypeDef(
    _ClientUpdateDestinationRedshiftDestinationUpdateProcessingConfigurationTypeDef
):
    """
    Type definition for `ClientUpdateDestinationRedshiftDestinationUpdate` `ProcessingConfiguration`

    The data processing configuration.

    - **Enabled** *(boolean) --*

      Enables or disables data processing.

    - **Processors** *(list) --*

      The data processors.

      - *(dict) --*

        Describes a data processor.

        - **Type** *(string) --* **[REQUIRED]**

          The type of processor.

        - **Parameters** *(list) --*

          The processor parameters.

          - *(dict) --*

            Describes the processor parameter.

            - **ParameterName** *(string) --* **[REQUIRED]**

              The name of the parameter.

            - **ParameterValue** *(string) --* **[REQUIRED]**

              The parameter value.
    """


_ClientUpdateDestinationRedshiftDestinationUpdateRetryOptionsTypeDef = TypedDict(
    "_ClientUpdateDestinationRedshiftDestinationUpdateRetryOptionsTypeDef",
    {"DurationInSeconds": int},
    total=False,
)


class ClientUpdateDestinationRedshiftDestinationUpdateRetryOptionsTypeDef(
    _ClientUpdateDestinationRedshiftDestinationUpdateRetryOptionsTypeDef
):
    """
    Type definition for `ClientUpdateDestinationRedshiftDestinationUpdate` `RetryOptions`

    The retry behavior in case Kinesis Data Firehose is unable to deliver documents to Amazon
    Redshift. Default value is 3600 (60 minutes).

    - **DurationInSeconds** *(integer) --*

      The length of time during which Kinesis Data Firehose retries delivery after a failure,
      starting from the initial request and including the first attempt. The default value is 3600
      seconds (60 minutes). Kinesis Data Firehose does not retry if the value of
      ``DurationInSeconds`` is 0 (zero) or if the first delivery attempt takes longer than the
      current value.
    """


_ClientUpdateDestinationRedshiftDestinationUpdateS3BackupUpdateBufferingHintsTypeDef = TypedDict(
    "_ClientUpdateDestinationRedshiftDestinationUpdateS3BackupUpdateBufferingHintsTypeDef",
    {"SizeInMBs": int, "IntervalInSeconds": int},
    total=False,
)


class ClientUpdateDestinationRedshiftDestinationUpdateS3BackupUpdateBufferingHintsTypeDef(
    _ClientUpdateDestinationRedshiftDestinationUpdateS3BackupUpdateBufferingHintsTypeDef
):
    """
    Type definition for `ClientUpdateDestinationRedshiftDestinationUpdateS3BackupUpdate` `BufferingHints`

    The buffering option. If no value is specified, ``BufferingHints`` object default values are
    used.

    - **SizeInMBs** *(integer) --*

      Buffer incoming data to the specified size, in MiBs, before delivering it to the
      destination. The default value is 5. This parameter is optional but if you specify a value
      for it, you must also specify a value for ``IntervalInSeconds`` , and vice versa.

      We recommend setting this parameter to a value greater than the amount of data you
      typically ingest into the delivery stream in 10 seconds. For example, if you typically
      ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

    - **IntervalInSeconds** *(integer) --*

      Buffer incoming data for the specified period of time, in seconds, before delivering it to
      the destination. The default value is 300. This parameter is optional but if you specify a
      value for it, you must also specify a value for ``SizeInMBs`` , and vice versa.
    """


_ClientUpdateDestinationRedshiftDestinationUpdateS3BackupUpdateCloudWatchLoggingOptionsTypeDef = TypedDict(
    "_ClientUpdateDestinationRedshiftDestinationUpdateS3BackupUpdateCloudWatchLoggingOptionsTypeDef",
    {"Enabled": bool, "LogGroupName": str, "LogStreamName": str},
    total=False,
)


class ClientUpdateDestinationRedshiftDestinationUpdateS3BackupUpdateCloudWatchLoggingOptionsTypeDef(
    _ClientUpdateDestinationRedshiftDestinationUpdateS3BackupUpdateCloudWatchLoggingOptionsTypeDef
):
    """
    Type definition for `ClientUpdateDestinationRedshiftDestinationUpdateS3BackupUpdate` `CloudWatchLoggingOptions`

    The CloudWatch logging options for your delivery stream.

    - **Enabled** *(boolean) --*

      Enables or disables CloudWatch logging.

    - **LogGroupName** *(string) --*

      The CloudWatch group name for logging. This value is required if CloudWatch logging is
      enabled.

    - **LogStreamName** *(string) --*

      The CloudWatch log stream name for logging. This value is required if CloudWatch logging is
      enabled.
    """


_ClientUpdateDestinationRedshiftDestinationUpdateS3BackupUpdateEncryptionConfigurationKMSEncryptionConfigTypeDef = TypedDict(
    "_ClientUpdateDestinationRedshiftDestinationUpdateS3BackupUpdateEncryptionConfigurationKMSEncryptionConfigTypeDef",
    {"AWSKMSKeyARN": str},
)


class ClientUpdateDestinationRedshiftDestinationUpdateS3BackupUpdateEncryptionConfigurationKMSEncryptionConfigTypeDef(
    _ClientUpdateDestinationRedshiftDestinationUpdateS3BackupUpdateEncryptionConfigurationKMSEncryptionConfigTypeDef
):
    """
    Type definition for `ClientUpdateDestinationRedshiftDestinationUpdateS3BackupUpdateEncryptionConfiguration` `KMSEncryptionConfig`

    The encryption key.

    - **AWSKMSKeyARN** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region
      as the destination Amazon S3 bucket. For more information, see `Amazon Resource Names
      (ARNs) and AWS Service Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
    """


_ClientUpdateDestinationRedshiftDestinationUpdateS3BackupUpdateEncryptionConfigurationTypeDef = TypedDict(
    "_ClientUpdateDestinationRedshiftDestinationUpdateS3BackupUpdateEncryptionConfigurationTypeDef",
    {
        "NoEncryptionConfig": str,
        "KMSEncryptionConfig": ClientUpdateDestinationRedshiftDestinationUpdateS3BackupUpdateEncryptionConfigurationKMSEncryptionConfigTypeDef,
    },
    total=False,
)


class ClientUpdateDestinationRedshiftDestinationUpdateS3BackupUpdateEncryptionConfigurationTypeDef(
    _ClientUpdateDestinationRedshiftDestinationUpdateS3BackupUpdateEncryptionConfigurationTypeDef
):
    """
    Type definition for `ClientUpdateDestinationRedshiftDestinationUpdateS3BackupUpdate` `EncryptionConfiguration`

    The encryption configuration. If no value is specified, the default is no encryption.

    - **NoEncryptionConfig** *(string) --*

      Specifically override existing encryption information to ensure that no encryption is used.

    - **KMSEncryptionConfig** *(dict) --*

      The encryption key.

      - **AWSKMSKeyARN** *(string) --* **[REQUIRED]**

        The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region
        as the destination Amazon S3 bucket. For more information, see `Amazon Resource Names
        (ARNs) and AWS Service Namespaces
        <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
    """


_ClientUpdateDestinationRedshiftDestinationUpdateS3BackupUpdateTypeDef = TypedDict(
    "_ClientUpdateDestinationRedshiftDestinationUpdateS3BackupUpdateTypeDef",
    {
        "RoleARN": str,
        "BucketARN": str,
        "Prefix": str,
        "ErrorOutputPrefix": str,
        "BufferingHints": ClientUpdateDestinationRedshiftDestinationUpdateS3BackupUpdateBufferingHintsTypeDef,
        "CompressionFormat": str,
        "EncryptionConfiguration": ClientUpdateDestinationRedshiftDestinationUpdateS3BackupUpdateEncryptionConfigurationTypeDef,
        "CloudWatchLoggingOptions": ClientUpdateDestinationRedshiftDestinationUpdateS3BackupUpdateCloudWatchLoggingOptionsTypeDef,
    },
    total=False,
)


class ClientUpdateDestinationRedshiftDestinationUpdateS3BackupUpdateTypeDef(
    _ClientUpdateDestinationRedshiftDestinationUpdateS3BackupUpdateTypeDef
):
    """
    Type definition for `ClientUpdateDestinationRedshiftDestinationUpdate` `S3BackupUpdate`

    The Amazon S3 destination for backup.

    - **RoleARN** *(string) --*

      The Amazon Resource Name (ARN) of the AWS credentials. For more information, see `Amazon
      Resource Names (ARNs) and AWS Service Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

    - **BucketARN** *(string) --*

      The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs) and AWS
      Service Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

    - **Prefix** *(string) --*

      The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered Amazon S3 files.
      You can also specify a custom prefix, as described in `Custom Prefixes for Amazon S3 Objects
      <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

    - **ErrorOutputPrefix** *(string) --*

      A prefix that Kinesis Data Firehose evaluates and adds to failed records before writing them
      to S3. This prefix appears immediately following the bucket name. For information about how
      to specify this prefix, see `Custom Prefixes for Amazon S3 Objects
      <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

    - **BufferingHints** *(dict) --*

      The buffering option. If no value is specified, ``BufferingHints`` object default values are
      used.

      - **SizeInMBs** *(integer) --*

        Buffer incoming data to the specified size, in MiBs, before delivering it to the
        destination. The default value is 5. This parameter is optional but if you specify a value
        for it, you must also specify a value for ``IntervalInSeconds`` , and vice versa.

        We recommend setting this parameter to a value greater than the amount of data you
        typically ingest into the delivery stream in 10 seconds. For example, if you typically
        ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

      - **IntervalInSeconds** *(integer) --*

        Buffer incoming data for the specified period of time, in seconds, before delivering it to
        the destination. The default value is 300. This parameter is optional but if you specify a
        value for it, you must also specify a value for ``SizeInMBs`` , and vice versa.

    - **CompressionFormat** *(string) --*

      The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .

      The compression formats ``SNAPPY`` or ``ZIP`` cannot be specified for Amazon Redshift
      destinations because they are not supported by the Amazon Redshift ``COPY`` operation that
      reads from the S3 bucket.

    - **EncryptionConfiguration** *(dict) --*

      The encryption configuration. If no value is specified, the default is no encryption.

      - **NoEncryptionConfig** *(string) --*

        Specifically override existing encryption information to ensure that no encryption is used.

      - **KMSEncryptionConfig** *(dict) --*

        The encryption key.

        - **AWSKMSKeyARN** *(string) --* **[REQUIRED]**

          The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region
          as the destination Amazon S3 bucket. For more information, see `Amazon Resource Names
          (ARNs) and AWS Service Namespaces
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

    - **CloudWatchLoggingOptions** *(dict) --*

      The CloudWatch logging options for your delivery stream.

      - **Enabled** *(boolean) --*

        Enables or disables CloudWatch logging.

      - **LogGroupName** *(string) --*

        The CloudWatch group name for logging. This value is required if CloudWatch logging is
        enabled.

      - **LogStreamName** *(string) --*

        The CloudWatch log stream name for logging. This value is required if CloudWatch logging is
        enabled.
    """


_ClientUpdateDestinationRedshiftDestinationUpdateS3UpdateBufferingHintsTypeDef = TypedDict(
    "_ClientUpdateDestinationRedshiftDestinationUpdateS3UpdateBufferingHintsTypeDef",
    {"SizeInMBs": int, "IntervalInSeconds": int},
    total=False,
)


class ClientUpdateDestinationRedshiftDestinationUpdateS3UpdateBufferingHintsTypeDef(
    _ClientUpdateDestinationRedshiftDestinationUpdateS3UpdateBufferingHintsTypeDef
):
    """
    Type definition for `ClientUpdateDestinationRedshiftDestinationUpdateS3Update` `BufferingHints`

    The buffering option. If no value is specified, ``BufferingHints`` object default values are
    used.

    - **SizeInMBs** *(integer) --*

      Buffer incoming data to the specified size, in MiBs, before delivering it to the
      destination. The default value is 5. This parameter is optional but if you specify a value
      for it, you must also specify a value for ``IntervalInSeconds`` , and vice versa.

      We recommend setting this parameter to a value greater than the amount of data you
      typically ingest into the delivery stream in 10 seconds. For example, if you typically
      ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

    - **IntervalInSeconds** *(integer) --*

      Buffer incoming data for the specified period of time, in seconds, before delivering it to
      the destination. The default value is 300. This parameter is optional but if you specify a
      value for it, you must also specify a value for ``SizeInMBs`` , and vice versa.
    """


_ClientUpdateDestinationRedshiftDestinationUpdateS3UpdateCloudWatchLoggingOptionsTypeDef = TypedDict(
    "_ClientUpdateDestinationRedshiftDestinationUpdateS3UpdateCloudWatchLoggingOptionsTypeDef",
    {"Enabled": bool, "LogGroupName": str, "LogStreamName": str},
    total=False,
)


class ClientUpdateDestinationRedshiftDestinationUpdateS3UpdateCloudWatchLoggingOptionsTypeDef(
    _ClientUpdateDestinationRedshiftDestinationUpdateS3UpdateCloudWatchLoggingOptionsTypeDef
):
    """
    Type definition for `ClientUpdateDestinationRedshiftDestinationUpdateS3Update` `CloudWatchLoggingOptions`

    The CloudWatch logging options for your delivery stream.

    - **Enabled** *(boolean) --*

      Enables or disables CloudWatch logging.

    - **LogGroupName** *(string) --*

      The CloudWatch group name for logging. This value is required if CloudWatch logging is
      enabled.

    - **LogStreamName** *(string) --*

      The CloudWatch log stream name for logging. This value is required if CloudWatch logging is
      enabled.
    """


_ClientUpdateDestinationRedshiftDestinationUpdateS3UpdateEncryptionConfigurationKMSEncryptionConfigTypeDef = TypedDict(
    "_ClientUpdateDestinationRedshiftDestinationUpdateS3UpdateEncryptionConfigurationKMSEncryptionConfigTypeDef",
    {"AWSKMSKeyARN": str},
)


class ClientUpdateDestinationRedshiftDestinationUpdateS3UpdateEncryptionConfigurationKMSEncryptionConfigTypeDef(
    _ClientUpdateDestinationRedshiftDestinationUpdateS3UpdateEncryptionConfigurationKMSEncryptionConfigTypeDef
):
    """
    Type definition for `ClientUpdateDestinationRedshiftDestinationUpdateS3UpdateEncryptionConfiguration` `KMSEncryptionConfig`

    The encryption key.

    - **AWSKMSKeyARN** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region
      as the destination Amazon S3 bucket. For more information, see `Amazon Resource Names
      (ARNs) and AWS Service Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
    """


_ClientUpdateDestinationRedshiftDestinationUpdateS3UpdateEncryptionConfigurationTypeDef = TypedDict(
    "_ClientUpdateDestinationRedshiftDestinationUpdateS3UpdateEncryptionConfigurationTypeDef",
    {
        "NoEncryptionConfig": str,
        "KMSEncryptionConfig": ClientUpdateDestinationRedshiftDestinationUpdateS3UpdateEncryptionConfigurationKMSEncryptionConfigTypeDef,
    },
    total=False,
)


class ClientUpdateDestinationRedshiftDestinationUpdateS3UpdateEncryptionConfigurationTypeDef(
    _ClientUpdateDestinationRedshiftDestinationUpdateS3UpdateEncryptionConfigurationTypeDef
):
    """
    Type definition for `ClientUpdateDestinationRedshiftDestinationUpdateS3Update` `EncryptionConfiguration`

    The encryption configuration. If no value is specified, the default is no encryption.

    - **NoEncryptionConfig** *(string) --*

      Specifically override existing encryption information to ensure that no encryption is used.

    - **KMSEncryptionConfig** *(dict) --*

      The encryption key.

      - **AWSKMSKeyARN** *(string) --* **[REQUIRED]**

        The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region
        as the destination Amazon S3 bucket. For more information, see `Amazon Resource Names
        (ARNs) and AWS Service Namespaces
        <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
    """


_ClientUpdateDestinationRedshiftDestinationUpdateS3UpdateTypeDef = TypedDict(
    "_ClientUpdateDestinationRedshiftDestinationUpdateS3UpdateTypeDef",
    {
        "RoleARN": str,
        "BucketARN": str,
        "Prefix": str,
        "ErrorOutputPrefix": str,
        "BufferingHints": ClientUpdateDestinationRedshiftDestinationUpdateS3UpdateBufferingHintsTypeDef,
        "CompressionFormat": str,
        "EncryptionConfiguration": ClientUpdateDestinationRedshiftDestinationUpdateS3UpdateEncryptionConfigurationTypeDef,
        "CloudWatchLoggingOptions": ClientUpdateDestinationRedshiftDestinationUpdateS3UpdateCloudWatchLoggingOptionsTypeDef,
    },
    total=False,
)


class ClientUpdateDestinationRedshiftDestinationUpdateS3UpdateTypeDef(
    _ClientUpdateDestinationRedshiftDestinationUpdateS3UpdateTypeDef
):
    """
    Type definition for `ClientUpdateDestinationRedshiftDestinationUpdate` `S3Update`

    The Amazon S3 destination.

    The compression formats ``SNAPPY`` or ``ZIP`` cannot be specified in
    ``RedshiftDestinationUpdate.S3Update`` because the Amazon Redshift ``COPY`` operation that
    reads from the S3 bucket doesn't support these compression formats.

    - **RoleARN** *(string) --*

      The Amazon Resource Name (ARN) of the AWS credentials. For more information, see `Amazon
      Resource Names (ARNs) and AWS Service Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

    - **BucketARN** *(string) --*

      The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs) and AWS
      Service Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

    - **Prefix** *(string) --*

      The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered Amazon S3 files.
      You can also specify a custom prefix, as described in `Custom Prefixes for Amazon S3 Objects
      <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

    - **ErrorOutputPrefix** *(string) --*

      A prefix that Kinesis Data Firehose evaluates and adds to failed records before writing them
      to S3. This prefix appears immediately following the bucket name. For information about how
      to specify this prefix, see `Custom Prefixes for Amazon S3 Objects
      <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

    - **BufferingHints** *(dict) --*

      The buffering option. If no value is specified, ``BufferingHints`` object default values are
      used.

      - **SizeInMBs** *(integer) --*

        Buffer incoming data to the specified size, in MiBs, before delivering it to the
        destination. The default value is 5. This parameter is optional but if you specify a value
        for it, you must also specify a value for ``IntervalInSeconds`` , and vice versa.

        We recommend setting this parameter to a value greater than the amount of data you
        typically ingest into the delivery stream in 10 seconds. For example, if you typically
        ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

      - **IntervalInSeconds** *(integer) --*

        Buffer incoming data for the specified period of time, in seconds, before delivering it to
        the destination. The default value is 300. This parameter is optional but if you specify a
        value for it, you must also specify a value for ``SizeInMBs`` , and vice versa.

    - **CompressionFormat** *(string) --*

      The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .

      The compression formats ``SNAPPY`` or ``ZIP`` cannot be specified for Amazon Redshift
      destinations because they are not supported by the Amazon Redshift ``COPY`` operation that
      reads from the S3 bucket.

    - **EncryptionConfiguration** *(dict) --*

      The encryption configuration. If no value is specified, the default is no encryption.

      - **NoEncryptionConfig** *(string) --*

        Specifically override existing encryption information to ensure that no encryption is used.

      - **KMSEncryptionConfig** *(dict) --*

        The encryption key.

        - **AWSKMSKeyARN** *(string) --* **[REQUIRED]**

          The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region
          as the destination Amazon S3 bucket. For more information, see `Amazon Resource Names
          (ARNs) and AWS Service Namespaces
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

    - **CloudWatchLoggingOptions** *(dict) --*

      The CloudWatch logging options for your delivery stream.

      - **Enabled** *(boolean) --*

        Enables or disables CloudWatch logging.

      - **LogGroupName** *(string) --*

        The CloudWatch group name for logging. This value is required if CloudWatch logging is
        enabled.

      - **LogStreamName** *(string) --*

        The CloudWatch log stream name for logging. This value is required if CloudWatch logging is
        enabled.
    """


_ClientUpdateDestinationRedshiftDestinationUpdateTypeDef = TypedDict(
    "_ClientUpdateDestinationRedshiftDestinationUpdateTypeDef",
    {
        "RoleARN": str,
        "ClusterJDBCURL": str,
        "CopyCommand": ClientUpdateDestinationRedshiftDestinationUpdateCopyCommandTypeDef,
        "Username": str,
        "Password": str,
        "RetryOptions": ClientUpdateDestinationRedshiftDestinationUpdateRetryOptionsTypeDef,
        "S3Update": ClientUpdateDestinationRedshiftDestinationUpdateS3UpdateTypeDef,
        "ProcessingConfiguration": ClientUpdateDestinationRedshiftDestinationUpdateProcessingConfigurationTypeDef,
        "S3BackupMode": str,
        "S3BackupUpdate": ClientUpdateDestinationRedshiftDestinationUpdateS3BackupUpdateTypeDef,
        "CloudWatchLoggingOptions": ClientUpdateDestinationRedshiftDestinationUpdateCloudWatchLoggingOptionsTypeDef,
    },
    total=False,
)


class ClientUpdateDestinationRedshiftDestinationUpdateTypeDef(
    _ClientUpdateDestinationRedshiftDestinationUpdateTypeDef
):
    """
    Type definition for `ClientUpdateDestination` `RedshiftDestinationUpdate`

    Describes an update for a destination in Amazon Redshift.

    - **RoleARN** *(string) --*

      The Amazon Resource Name (ARN) of the AWS credentials. For more information, see `Amazon
      Resource Names (ARNs) and AWS Service Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

    - **ClusterJDBCURL** *(string) --*

      The database connection string.

    - **CopyCommand** *(dict) --*

      The ``COPY`` command.

      - **DataTableName** *(string) --* **[REQUIRED]**

        The name of the target table. The table must already exist in the database.

      - **DataTableColumns** *(string) --*

        A comma-separated list of column names.

      - **CopyOptions** *(string) --*

        Optional parameters to use with the Amazon Redshift ``COPY`` command. For more information,
        see the "Optional Parameters" section of `Amazon Redshift COPY command
        <https://docs.aws.amazon.com/redshift/latest/dg/r_COPY.html>`__ . Some possible examples that
        would apply to Kinesis Data Firehose are as follows:

         ``delimiter '\\t' lzop;`` - fields are delimited with "\\t" (TAB character) and compressed
         using lzop.

         ``delimiter '|'`` - fields are delimited with "|" (this is the default delimiter).

         ``delimiter '|' escape`` - the delimiter should be escaped.

         ``fixedwidth 'venueid:3,venuename:25,venuecity:12,venuestate:2,venueseats:6'`` - fields are
         fixed width in the source, with each width specified after every column in the table.

         ``JSON 's3://mybucket/jsonpaths.txt'`` - data is in JSON format, and the path specified is
         the format of the data.

        For more examples, see `Amazon Redshift COPY command examples
        <https://docs.aws.amazon.com/redshift/latest/dg/r_COPY_command_examples.html>`__ .

    - **Username** *(string) --*

      The name of the user.

    - **Password** *(string) --*

      The user password.

    - **RetryOptions** *(dict) --*

      The retry behavior in case Kinesis Data Firehose is unable to deliver documents to Amazon
      Redshift. Default value is 3600 (60 minutes).

      - **DurationInSeconds** *(integer) --*

        The length of time during which Kinesis Data Firehose retries delivery after a failure,
        starting from the initial request and including the first attempt. The default value is 3600
        seconds (60 minutes). Kinesis Data Firehose does not retry if the value of
        ``DurationInSeconds`` is 0 (zero) or if the first delivery attempt takes longer than the
        current value.

    - **S3Update** *(dict) --*

      The Amazon S3 destination.

      The compression formats ``SNAPPY`` or ``ZIP`` cannot be specified in
      ``RedshiftDestinationUpdate.S3Update`` because the Amazon Redshift ``COPY`` operation that
      reads from the S3 bucket doesn't support these compression formats.

      - **RoleARN** *(string) --*

        The Amazon Resource Name (ARN) of the AWS credentials. For more information, see `Amazon
        Resource Names (ARNs) and AWS Service Namespaces
        <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

      - **BucketARN** *(string) --*

        The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs) and AWS
        Service Namespaces
        <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

      - **Prefix** *(string) --*

        The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered Amazon S3 files.
        You can also specify a custom prefix, as described in `Custom Prefixes for Amazon S3 Objects
        <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

      - **ErrorOutputPrefix** *(string) --*

        A prefix that Kinesis Data Firehose evaluates and adds to failed records before writing them
        to S3. This prefix appears immediately following the bucket name. For information about how
        to specify this prefix, see `Custom Prefixes for Amazon S3 Objects
        <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

      - **BufferingHints** *(dict) --*

        The buffering option. If no value is specified, ``BufferingHints`` object default values are
        used.

        - **SizeInMBs** *(integer) --*

          Buffer incoming data to the specified size, in MiBs, before delivering it to the
          destination. The default value is 5. This parameter is optional but if you specify a value
          for it, you must also specify a value for ``IntervalInSeconds`` , and vice versa.

          We recommend setting this parameter to a value greater than the amount of data you
          typically ingest into the delivery stream in 10 seconds. For example, if you typically
          ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

        - **IntervalInSeconds** *(integer) --*

          Buffer incoming data for the specified period of time, in seconds, before delivering it to
          the destination. The default value is 300. This parameter is optional but if you specify a
          value for it, you must also specify a value for ``SizeInMBs`` , and vice versa.

      - **CompressionFormat** *(string) --*

        The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .

        The compression formats ``SNAPPY`` or ``ZIP`` cannot be specified for Amazon Redshift
        destinations because they are not supported by the Amazon Redshift ``COPY`` operation that
        reads from the S3 bucket.

      - **EncryptionConfiguration** *(dict) --*

        The encryption configuration. If no value is specified, the default is no encryption.

        - **NoEncryptionConfig** *(string) --*

          Specifically override existing encryption information to ensure that no encryption is used.

        - **KMSEncryptionConfig** *(dict) --*

          The encryption key.

          - **AWSKMSKeyARN** *(string) --* **[REQUIRED]**

            The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region
            as the destination Amazon S3 bucket. For more information, see `Amazon Resource Names
            (ARNs) and AWS Service Namespaces
            <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

      - **CloudWatchLoggingOptions** *(dict) --*

        The CloudWatch logging options for your delivery stream.

        - **Enabled** *(boolean) --*

          Enables or disables CloudWatch logging.

        - **LogGroupName** *(string) --*

          The CloudWatch group name for logging. This value is required if CloudWatch logging is
          enabled.

        - **LogStreamName** *(string) --*

          The CloudWatch log stream name for logging. This value is required if CloudWatch logging is
          enabled.

    - **ProcessingConfiguration** *(dict) --*

      The data processing configuration.

      - **Enabled** *(boolean) --*

        Enables or disables data processing.

      - **Processors** *(list) --*

        The data processors.

        - *(dict) --*

          Describes a data processor.

          - **Type** *(string) --* **[REQUIRED]**

            The type of processor.

          - **Parameters** *(list) --*

            The processor parameters.

            - *(dict) --*

              Describes the processor parameter.

              - **ParameterName** *(string) --* **[REQUIRED]**

                The name of the parameter.

              - **ParameterValue** *(string) --* **[REQUIRED]**

                The parameter value.

    - **S3BackupMode** *(string) --*

      The Amazon S3 backup mode.

    - **S3BackupUpdate** *(dict) --*

      The Amazon S3 destination for backup.

      - **RoleARN** *(string) --*

        The Amazon Resource Name (ARN) of the AWS credentials. For more information, see `Amazon
        Resource Names (ARNs) and AWS Service Namespaces
        <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

      - **BucketARN** *(string) --*

        The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs) and AWS
        Service Namespaces
        <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

      - **Prefix** *(string) --*

        The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered Amazon S3 files.
        You can also specify a custom prefix, as described in `Custom Prefixes for Amazon S3 Objects
        <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

      - **ErrorOutputPrefix** *(string) --*

        A prefix that Kinesis Data Firehose evaluates and adds to failed records before writing them
        to S3. This prefix appears immediately following the bucket name. For information about how
        to specify this prefix, see `Custom Prefixes for Amazon S3 Objects
        <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

      - **BufferingHints** *(dict) --*

        The buffering option. If no value is specified, ``BufferingHints`` object default values are
        used.

        - **SizeInMBs** *(integer) --*

          Buffer incoming data to the specified size, in MiBs, before delivering it to the
          destination. The default value is 5. This parameter is optional but if you specify a value
          for it, you must also specify a value for ``IntervalInSeconds`` , and vice versa.

          We recommend setting this parameter to a value greater than the amount of data you
          typically ingest into the delivery stream in 10 seconds. For example, if you typically
          ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

        - **IntervalInSeconds** *(integer) --*

          Buffer incoming data for the specified period of time, in seconds, before delivering it to
          the destination. The default value is 300. This parameter is optional but if you specify a
          value for it, you must also specify a value for ``SizeInMBs`` , and vice versa.

      - **CompressionFormat** *(string) --*

        The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .

        The compression formats ``SNAPPY`` or ``ZIP`` cannot be specified for Amazon Redshift
        destinations because they are not supported by the Amazon Redshift ``COPY`` operation that
        reads from the S3 bucket.

      - **EncryptionConfiguration** *(dict) --*

        The encryption configuration. If no value is specified, the default is no encryption.

        - **NoEncryptionConfig** *(string) --*

          Specifically override existing encryption information to ensure that no encryption is used.

        - **KMSEncryptionConfig** *(dict) --*

          The encryption key.

          - **AWSKMSKeyARN** *(string) --* **[REQUIRED]**

            The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region
            as the destination Amazon S3 bucket. For more information, see `Amazon Resource Names
            (ARNs) and AWS Service Namespaces
            <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

      - **CloudWatchLoggingOptions** *(dict) --*

        The CloudWatch logging options for your delivery stream.

        - **Enabled** *(boolean) --*

          Enables or disables CloudWatch logging.

        - **LogGroupName** *(string) --*

          The CloudWatch group name for logging. This value is required if CloudWatch logging is
          enabled.

        - **LogStreamName** *(string) --*

          The CloudWatch log stream name for logging. This value is required if CloudWatch logging is
          enabled.

    - **CloudWatchLoggingOptions** *(dict) --*

      The Amazon CloudWatch logging options for your delivery stream.

      - **Enabled** *(boolean) --*

        Enables or disables CloudWatch logging.

      - **LogGroupName** *(string) --*

        The CloudWatch group name for logging. This value is required if CloudWatch logging is
        enabled.

      - **LogStreamName** *(string) --*

        The CloudWatch log stream name for logging. This value is required if CloudWatch logging is
        enabled.
    """


_ClientUpdateDestinationS3DestinationUpdateBufferingHintsTypeDef = TypedDict(
    "_ClientUpdateDestinationS3DestinationUpdateBufferingHintsTypeDef",
    {"SizeInMBs": int, "IntervalInSeconds": int},
    total=False,
)


class ClientUpdateDestinationS3DestinationUpdateBufferingHintsTypeDef(
    _ClientUpdateDestinationS3DestinationUpdateBufferingHintsTypeDef
):
    """
    Type definition for `ClientUpdateDestinationS3DestinationUpdate` `BufferingHints`

    The buffering option. If no value is specified, ``BufferingHints`` object default values are
    used.

    - **SizeInMBs** *(integer) --*

      Buffer incoming data to the specified size, in MiBs, before delivering it to the destination.
      The default value is 5. This parameter is optional but if you specify a value for it, you
      must also specify a value for ``IntervalInSeconds`` , and vice versa.

      We recommend setting this parameter to a value greater than the amount of data you typically
      ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1
      MiB/sec, the value should be 10 MiB or higher.

    - **IntervalInSeconds** *(integer) --*

      Buffer incoming data for the specified period of time, in seconds, before delivering it to
      the destination. The default value is 300. This parameter is optional but if you specify a
      value for it, you must also specify a value for ``SizeInMBs`` , and vice versa.
    """


_ClientUpdateDestinationS3DestinationUpdateCloudWatchLoggingOptionsTypeDef = TypedDict(
    "_ClientUpdateDestinationS3DestinationUpdateCloudWatchLoggingOptionsTypeDef",
    {"Enabled": bool, "LogGroupName": str, "LogStreamName": str},
    total=False,
)


class ClientUpdateDestinationS3DestinationUpdateCloudWatchLoggingOptionsTypeDef(
    _ClientUpdateDestinationS3DestinationUpdateCloudWatchLoggingOptionsTypeDef
):
    """
    Type definition for `ClientUpdateDestinationS3DestinationUpdate` `CloudWatchLoggingOptions`

    The CloudWatch logging options for your delivery stream.

    - **Enabled** *(boolean) --*

      Enables or disables CloudWatch logging.

    - **LogGroupName** *(string) --*

      The CloudWatch group name for logging. This value is required if CloudWatch logging is
      enabled.

    - **LogStreamName** *(string) --*

      The CloudWatch log stream name for logging. This value is required if CloudWatch logging is
      enabled.
    """


_ClientUpdateDestinationS3DestinationUpdateEncryptionConfigurationKMSEncryptionConfigTypeDef = TypedDict(
    "_ClientUpdateDestinationS3DestinationUpdateEncryptionConfigurationKMSEncryptionConfigTypeDef",
    {"AWSKMSKeyARN": str},
)


class ClientUpdateDestinationS3DestinationUpdateEncryptionConfigurationKMSEncryptionConfigTypeDef(
    _ClientUpdateDestinationS3DestinationUpdateEncryptionConfigurationKMSEncryptionConfigTypeDef
):
    """
    Type definition for `ClientUpdateDestinationS3DestinationUpdateEncryptionConfiguration` `KMSEncryptionConfig`

    The encryption key.

    - **AWSKMSKeyARN** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region as
      the destination Amazon S3 bucket. For more information, see `Amazon Resource Names (ARNs)
      and AWS Service Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
    """


_ClientUpdateDestinationS3DestinationUpdateEncryptionConfigurationTypeDef = TypedDict(
    "_ClientUpdateDestinationS3DestinationUpdateEncryptionConfigurationTypeDef",
    {
        "NoEncryptionConfig": str,
        "KMSEncryptionConfig": ClientUpdateDestinationS3DestinationUpdateEncryptionConfigurationKMSEncryptionConfigTypeDef,
    },
    total=False,
)


class ClientUpdateDestinationS3DestinationUpdateEncryptionConfigurationTypeDef(
    _ClientUpdateDestinationS3DestinationUpdateEncryptionConfigurationTypeDef
):
    """
    Type definition for `ClientUpdateDestinationS3DestinationUpdate` `EncryptionConfiguration`

    The encryption configuration. If no value is specified, the default is no encryption.

    - **NoEncryptionConfig** *(string) --*

      Specifically override existing encryption information to ensure that no encryption is used.

    - **KMSEncryptionConfig** *(dict) --*

      The encryption key.

      - **AWSKMSKeyARN** *(string) --* **[REQUIRED]**

        The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region as
        the destination Amazon S3 bucket. For more information, see `Amazon Resource Names (ARNs)
        and AWS Service Namespaces
        <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
    """


_ClientUpdateDestinationS3DestinationUpdateTypeDef = TypedDict(
    "_ClientUpdateDestinationS3DestinationUpdateTypeDef",
    {
        "RoleARN": str,
        "BucketARN": str,
        "Prefix": str,
        "ErrorOutputPrefix": str,
        "BufferingHints": ClientUpdateDestinationS3DestinationUpdateBufferingHintsTypeDef,
        "CompressionFormat": str,
        "EncryptionConfiguration": ClientUpdateDestinationS3DestinationUpdateEncryptionConfigurationTypeDef,
        "CloudWatchLoggingOptions": ClientUpdateDestinationS3DestinationUpdateCloudWatchLoggingOptionsTypeDef,
    },
    total=False,
)


class ClientUpdateDestinationS3DestinationUpdateTypeDef(
    _ClientUpdateDestinationS3DestinationUpdateTypeDef
):
    """
    Type definition for `ClientUpdateDestination` `S3DestinationUpdate`

    [Deprecated] Describes an update for a destination in Amazon S3.

    - **RoleARN** *(string) --*

      The Amazon Resource Name (ARN) of the AWS credentials. For more information, see `Amazon
      Resource Names (ARNs) and AWS Service Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

    - **BucketARN** *(string) --*

      The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs) and AWS
      Service Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

    - **Prefix** *(string) --*

      The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered Amazon S3 files. You
      can also specify a custom prefix, as described in `Custom Prefixes for Amazon S3 Objects
      <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

    - **ErrorOutputPrefix** *(string) --*

      A prefix that Kinesis Data Firehose evaluates and adds to failed records before writing them to
      S3. This prefix appears immediately following the bucket name. For information about how to
      specify this prefix, see `Custom Prefixes for Amazon S3 Objects
      <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

    - **BufferingHints** *(dict) --*

      The buffering option. If no value is specified, ``BufferingHints`` object default values are
      used.

      - **SizeInMBs** *(integer) --*

        Buffer incoming data to the specified size, in MiBs, before delivering it to the destination.
        The default value is 5. This parameter is optional but if you specify a value for it, you
        must also specify a value for ``IntervalInSeconds`` , and vice versa.

        We recommend setting this parameter to a value greater than the amount of data you typically
        ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1
        MiB/sec, the value should be 10 MiB or higher.

      - **IntervalInSeconds** *(integer) --*

        Buffer incoming data for the specified period of time, in seconds, before delivering it to
        the destination. The default value is 300. This parameter is optional but if you specify a
        value for it, you must also specify a value for ``SizeInMBs`` , and vice versa.

    - **CompressionFormat** *(string) --*

      The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .

      The compression formats ``SNAPPY`` or ``ZIP`` cannot be specified for Amazon Redshift
      destinations because they are not supported by the Amazon Redshift ``COPY`` operation that
      reads from the S3 bucket.

    - **EncryptionConfiguration** *(dict) --*

      The encryption configuration. If no value is specified, the default is no encryption.

      - **NoEncryptionConfig** *(string) --*

        Specifically override existing encryption information to ensure that no encryption is used.

      - **KMSEncryptionConfig** *(dict) --*

        The encryption key.

        - **AWSKMSKeyARN** *(string) --* **[REQUIRED]**

          The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region as
          the destination Amazon S3 bucket. For more information, see `Amazon Resource Names (ARNs)
          and AWS Service Namespaces
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

    - **CloudWatchLoggingOptions** *(dict) --*

      The CloudWatch logging options for your delivery stream.

      - **Enabled** *(boolean) --*

        Enables or disables CloudWatch logging.

      - **LogGroupName** *(string) --*

        The CloudWatch group name for logging. This value is required if CloudWatch logging is
        enabled.

      - **LogStreamName** *(string) --*

        The CloudWatch log stream name for logging. This value is required if CloudWatch logging is
        enabled.
    """


_ClientUpdateDestinationSplunkDestinationUpdateCloudWatchLoggingOptionsTypeDef = TypedDict(
    "_ClientUpdateDestinationSplunkDestinationUpdateCloudWatchLoggingOptionsTypeDef",
    {"Enabled": bool, "LogGroupName": str, "LogStreamName": str},
    total=False,
)


class ClientUpdateDestinationSplunkDestinationUpdateCloudWatchLoggingOptionsTypeDef(
    _ClientUpdateDestinationSplunkDestinationUpdateCloudWatchLoggingOptionsTypeDef
):
    """
    Type definition for `ClientUpdateDestinationSplunkDestinationUpdate` `CloudWatchLoggingOptions`

    The Amazon CloudWatch logging options for your delivery stream.

    - **Enabled** *(boolean) --*

      Enables or disables CloudWatch logging.

    - **LogGroupName** *(string) --*

      The CloudWatch group name for logging. This value is required if CloudWatch logging is
      enabled.

    - **LogStreamName** *(string) --*

      The CloudWatch log stream name for logging. This value is required if CloudWatch logging is
      enabled.
    """


_ClientUpdateDestinationSplunkDestinationUpdateProcessingConfigurationProcessorsParametersTypeDef = TypedDict(
    "_ClientUpdateDestinationSplunkDestinationUpdateProcessingConfigurationProcessorsParametersTypeDef",
    {"ParameterName": str, "ParameterValue": str},
)


class ClientUpdateDestinationSplunkDestinationUpdateProcessingConfigurationProcessorsParametersTypeDef(
    _ClientUpdateDestinationSplunkDestinationUpdateProcessingConfigurationProcessorsParametersTypeDef
):
    """
    Type definition for `ClientUpdateDestinationSplunkDestinationUpdateProcessingConfigurationProcessors` `Parameters`

    Describes the processor parameter.

    - **ParameterName** *(string) --* **[REQUIRED]**

      The name of the parameter.

    - **ParameterValue** *(string) --* **[REQUIRED]**

      The parameter value.
    """


_RequiredClientUpdateDestinationSplunkDestinationUpdateProcessingConfigurationProcessorsTypeDef = TypedDict(
    "_RequiredClientUpdateDestinationSplunkDestinationUpdateProcessingConfigurationProcessorsTypeDef",
    {"Type": str},
)
_OptionalClientUpdateDestinationSplunkDestinationUpdateProcessingConfigurationProcessorsTypeDef = TypedDict(
    "_OptionalClientUpdateDestinationSplunkDestinationUpdateProcessingConfigurationProcessorsTypeDef",
    {
        "Parameters": List[
            ClientUpdateDestinationSplunkDestinationUpdateProcessingConfigurationProcessorsParametersTypeDef
        ]
    },
    total=False,
)


class ClientUpdateDestinationSplunkDestinationUpdateProcessingConfigurationProcessorsTypeDef(
    _RequiredClientUpdateDestinationSplunkDestinationUpdateProcessingConfigurationProcessorsTypeDef,
    _OptionalClientUpdateDestinationSplunkDestinationUpdateProcessingConfigurationProcessorsTypeDef,
):
    """
    Type definition for `ClientUpdateDestinationSplunkDestinationUpdateProcessingConfiguration` `Processors`

    Describes a data processor.

    - **Type** *(string) --* **[REQUIRED]**

      The type of processor.

    - **Parameters** *(list) --*

      The processor parameters.

      - *(dict) --*

        Describes the processor parameter.

        - **ParameterName** *(string) --* **[REQUIRED]**

          The name of the parameter.

        - **ParameterValue** *(string) --* **[REQUIRED]**

          The parameter value.
    """


_ClientUpdateDestinationSplunkDestinationUpdateProcessingConfigurationTypeDef = TypedDict(
    "_ClientUpdateDestinationSplunkDestinationUpdateProcessingConfigurationTypeDef",
    {
        "Enabled": bool,
        "Processors": List[
            ClientUpdateDestinationSplunkDestinationUpdateProcessingConfigurationProcessorsTypeDef
        ],
    },
    total=False,
)


class ClientUpdateDestinationSplunkDestinationUpdateProcessingConfigurationTypeDef(
    _ClientUpdateDestinationSplunkDestinationUpdateProcessingConfigurationTypeDef
):
    """
    Type definition for `ClientUpdateDestinationSplunkDestinationUpdate` `ProcessingConfiguration`

    The data processing configuration.

    - **Enabled** *(boolean) --*

      Enables or disables data processing.

    - **Processors** *(list) --*

      The data processors.

      - *(dict) --*

        Describes a data processor.

        - **Type** *(string) --* **[REQUIRED]**

          The type of processor.

        - **Parameters** *(list) --*

          The processor parameters.

          - *(dict) --*

            Describes the processor parameter.

            - **ParameterName** *(string) --* **[REQUIRED]**

              The name of the parameter.

            - **ParameterValue** *(string) --* **[REQUIRED]**

              The parameter value.
    """


_ClientUpdateDestinationSplunkDestinationUpdateRetryOptionsTypeDef = TypedDict(
    "_ClientUpdateDestinationSplunkDestinationUpdateRetryOptionsTypeDef",
    {"DurationInSeconds": int},
    total=False,
)


class ClientUpdateDestinationSplunkDestinationUpdateRetryOptionsTypeDef(
    _ClientUpdateDestinationSplunkDestinationUpdateRetryOptionsTypeDef
):
    """
    Type definition for `ClientUpdateDestinationSplunkDestinationUpdate` `RetryOptions`

    The retry behavior in case Kinesis Data Firehose is unable to deliver data to Splunk or if it
    doesn't receive an acknowledgment of receipt from Splunk.

    - **DurationInSeconds** *(integer) --*

      The total amount of time that Kinesis Data Firehose spends on retries. This duration starts
      after the initial attempt to send data to Splunk fails. It doesn't include the periods during
      which Kinesis Data Firehose waits for acknowledgment from Splunk after each attempt.
    """


_ClientUpdateDestinationSplunkDestinationUpdateS3UpdateBufferingHintsTypeDef = TypedDict(
    "_ClientUpdateDestinationSplunkDestinationUpdateS3UpdateBufferingHintsTypeDef",
    {"SizeInMBs": int, "IntervalInSeconds": int},
    total=False,
)


class ClientUpdateDestinationSplunkDestinationUpdateS3UpdateBufferingHintsTypeDef(
    _ClientUpdateDestinationSplunkDestinationUpdateS3UpdateBufferingHintsTypeDef
):
    """
    Type definition for `ClientUpdateDestinationSplunkDestinationUpdateS3Update` `BufferingHints`

    The buffering option. If no value is specified, ``BufferingHints`` object default values are
    used.

    - **SizeInMBs** *(integer) --*

      Buffer incoming data to the specified size, in MiBs, before delivering it to the
      destination. The default value is 5. This parameter is optional but if you specify a value
      for it, you must also specify a value for ``IntervalInSeconds`` , and vice versa.

      We recommend setting this parameter to a value greater than the amount of data you
      typically ingest into the delivery stream in 10 seconds. For example, if you typically
      ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

    - **IntervalInSeconds** *(integer) --*

      Buffer incoming data for the specified period of time, in seconds, before delivering it to
      the destination. The default value is 300. This parameter is optional but if you specify a
      value for it, you must also specify a value for ``SizeInMBs`` , and vice versa.
    """


_ClientUpdateDestinationSplunkDestinationUpdateS3UpdateCloudWatchLoggingOptionsTypeDef = TypedDict(
    "_ClientUpdateDestinationSplunkDestinationUpdateS3UpdateCloudWatchLoggingOptionsTypeDef",
    {"Enabled": bool, "LogGroupName": str, "LogStreamName": str},
    total=False,
)


class ClientUpdateDestinationSplunkDestinationUpdateS3UpdateCloudWatchLoggingOptionsTypeDef(
    _ClientUpdateDestinationSplunkDestinationUpdateS3UpdateCloudWatchLoggingOptionsTypeDef
):
    """
    Type definition for `ClientUpdateDestinationSplunkDestinationUpdateS3Update` `CloudWatchLoggingOptions`

    The CloudWatch logging options for your delivery stream.

    - **Enabled** *(boolean) --*

      Enables or disables CloudWatch logging.

    - **LogGroupName** *(string) --*

      The CloudWatch group name for logging. This value is required if CloudWatch logging is
      enabled.

    - **LogStreamName** *(string) --*

      The CloudWatch log stream name for logging. This value is required if CloudWatch logging is
      enabled.
    """


_ClientUpdateDestinationSplunkDestinationUpdateS3UpdateEncryptionConfigurationKMSEncryptionConfigTypeDef = TypedDict(
    "_ClientUpdateDestinationSplunkDestinationUpdateS3UpdateEncryptionConfigurationKMSEncryptionConfigTypeDef",
    {"AWSKMSKeyARN": str},
)


class ClientUpdateDestinationSplunkDestinationUpdateS3UpdateEncryptionConfigurationKMSEncryptionConfigTypeDef(
    _ClientUpdateDestinationSplunkDestinationUpdateS3UpdateEncryptionConfigurationKMSEncryptionConfigTypeDef
):
    """
    Type definition for `ClientUpdateDestinationSplunkDestinationUpdateS3UpdateEncryptionConfiguration` `KMSEncryptionConfig`

    The encryption key.

    - **AWSKMSKeyARN** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region
      as the destination Amazon S3 bucket. For more information, see `Amazon Resource Names
      (ARNs) and AWS Service Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
    """


_ClientUpdateDestinationSplunkDestinationUpdateS3UpdateEncryptionConfigurationTypeDef = TypedDict(
    "_ClientUpdateDestinationSplunkDestinationUpdateS3UpdateEncryptionConfigurationTypeDef",
    {
        "NoEncryptionConfig": str,
        "KMSEncryptionConfig": ClientUpdateDestinationSplunkDestinationUpdateS3UpdateEncryptionConfigurationKMSEncryptionConfigTypeDef,
    },
    total=False,
)


class ClientUpdateDestinationSplunkDestinationUpdateS3UpdateEncryptionConfigurationTypeDef(
    _ClientUpdateDestinationSplunkDestinationUpdateS3UpdateEncryptionConfigurationTypeDef
):
    """
    Type definition for `ClientUpdateDestinationSplunkDestinationUpdateS3Update` `EncryptionConfiguration`

    The encryption configuration. If no value is specified, the default is no encryption.

    - **NoEncryptionConfig** *(string) --*

      Specifically override existing encryption information to ensure that no encryption is used.

    - **KMSEncryptionConfig** *(dict) --*

      The encryption key.

      - **AWSKMSKeyARN** *(string) --* **[REQUIRED]**

        The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region
        as the destination Amazon S3 bucket. For more information, see `Amazon Resource Names
        (ARNs) and AWS Service Namespaces
        <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
    """


_ClientUpdateDestinationSplunkDestinationUpdateS3UpdateTypeDef = TypedDict(
    "_ClientUpdateDestinationSplunkDestinationUpdateS3UpdateTypeDef",
    {
        "RoleARN": str,
        "BucketARN": str,
        "Prefix": str,
        "ErrorOutputPrefix": str,
        "BufferingHints": ClientUpdateDestinationSplunkDestinationUpdateS3UpdateBufferingHintsTypeDef,
        "CompressionFormat": str,
        "EncryptionConfiguration": ClientUpdateDestinationSplunkDestinationUpdateS3UpdateEncryptionConfigurationTypeDef,
        "CloudWatchLoggingOptions": ClientUpdateDestinationSplunkDestinationUpdateS3UpdateCloudWatchLoggingOptionsTypeDef,
    },
    total=False,
)


class ClientUpdateDestinationSplunkDestinationUpdateS3UpdateTypeDef(
    _ClientUpdateDestinationSplunkDestinationUpdateS3UpdateTypeDef
):
    """
    Type definition for `ClientUpdateDestinationSplunkDestinationUpdate` `S3Update`

    Your update to the configuration of the backup Amazon S3 location.

    - **RoleARN** *(string) --*

      The Amazon Resource Name (ARN) of the AWS credentials. For more information, see `Amazon
      Resource Names (ARNs) and AWS Service Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

    - **BucketARN** *(string) --*

      The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs) and AWS
      Service Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

    - **Prefix** *(string) --*

      The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered Amazon S3 files.
      You can also specify a custom prefix, as described in `Custom Prefixes for Amazon S3 Objects
      <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

    - **ErrorOutputPrefix** *(string) --*

      A prefix that Kinesis Data Firehose evaluates and adds to failed records before writing them
      to S3. This prefix appears immediately following the bucket name. For information about how
      to specify this prefix, see `Custom Prefixes for Amazon S3 Objects
      <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

    - **BufferingHints** *(dict) --*

      The buffering option. If no value is specified, ``BufferingHints`` object default values are
      used.

      - **SizeInMBs** *(integer) --*

        Buffer incoming data to the specified size, in MiBs, before delivering it to the
        destination. The default value is 5. This parameter is optional but if you specify a value
        for it, you must also specify a value for ``IntervalInSeconds`` , and vice versa.

        We recommend setting this parameter to a value greater than the amount of data you
        typically ingest into the delivery stream in 10 seconds. For example, if you typically
        ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

      - **IntervalInSeconds** *(integer) --*

        Buffer incoming data for the specified period of time, in seconds, before delivering it to
        the destination. The default value is 300. This parameter is optional but if you specify a
        value for it, you must also specify a value for ``SizeInMBs`` , and vice versa.

    - **CompressionFormat** *(string) --*

      The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .

      The compression formats ``SNAPPY`` or ``ZIP`` cannot be specified for Amazon Redshift
      destinations because they are not supported by the Amazon Redshift ``COPY`` operation that
      reads from the S3 bucket.

    - **EncryptionConfiguration** *(dict) --*

      The encryption configuration. If no value is specified, the default is no encryption.

      - **NoEncryptionConfig** *(string) --*

        Specifically override existing encryption information to ensure that no encryption is used.

      - **KMSEncryptionConfig** *(dict) --*

        The encryption key.

        - **AWSKMSKeyARN** *(string) --* **[REQUIRED]**

          The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region
          as the destination Amazon S3 bucket. For more information, see `Amazon Resource Names
          (ARNs) and AWS Service Namespaces
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

    - **CloudWatchLoggingOptions** *(dict) --*

      The CloudWatch logging options for your delivery stream.

      - **Enabled** *(boolean) --*

        Enables or disables CloudWatch logging.

      - **LogGroupName** *(string) --*

        The CloudWatch group name for logging. This value is required if CloudWatch logging is
        enabled.

      - **LogStreamName** *(string) --*

        The CloudWatch log stream name for logging. This value is required if CloudWatch logging is
        enabled.
    """


_ClientUpdateDestinationSplunkDestinationUpdateTypeDef = TypedDict(
    "_ClientUpdateDestinationSplunkDestinationUpdateTypeDef",
    {
        "HECEndpoint": str,
        "HECEndpointType": str,
        "HECToken": str,
        "HECAcknowledgmentTimeoutInSeconds": int,
        "RetryOptions": ClientUpdateDestinationSplunkDestinationUpdateRetryOptionsTypeDef,
        "S3BackupMode": str,
        "S3Update": ClientUpdateDestinationSplunkDestinationUpdateS3UpdateTypeDef,
        "ProcessingConfiguration": ClientUpdateDestinationSplunkDestinationUpdateProcessingConfigurationTypeDef,
        "CloudWatchLoggingOptions": ClientUpdateDestinationSplunkDestinationUpdateCloudWatchLoggingOptionsTypeDef,
    },
    total=False,
)


class ClientUpdateDestinationSplunkDestinationUpdateTypeDef(
    _ClientUpdateDestinationSplunkDestinationUpdateTypeDef
):
    """
    Type definition for `ClientUpdateDestination` `SplunkDestinationUpdate`

    Describes an update for a destination in Splunk.

    - **HECEndpoint** *(string) --*

      The HTTP Event Collector (HEC) endpoint to which Kinesis Data Firehose sends your data.

    - **HECEndpointType** *(string) --*

      This type can be either "Raw" or "Event."

    - **HECToken** *(string) --*

      A GUID that you obtain from your Splunk cluster when you create a new HEC endpoint.

    - **HECAcknowledgmentTimeoutInSeconds** *(integer) --*

      The amount of time that Kinesis Data Firehose waits to receive an acknowledgment from Splunk
      after it sends data. At the end of the timeout period, Kinesis Data Firehose either tries to
      send the data again or considers it an error, based on your retry settings.

    - **RetryOptions** *(dict) --*

      The retry behavior in case Kinesis Data Firehose is unable to deliver data to Splunk or if it
      doesn't receive an acknowledgment of receipt from Splunk.

      - **DurationInSeconds** *(integer) --*

        The total amount of time that Kinesis Data Firehose spends on retries. This duration starts
        after the initial attempt to send data to Splunk fails. It doesn't include the periods during
        which Kinesis Data Firehose waits for acknowledgment from Splunk after each attempt.

    - **S3BackupMode** *(string) --*

      Defines how documents should be delivered to Amazon S3. When set to ``FailedDocumentsOnly`` ,
      Kinesis Data Firehose writes any data that could not be indexed to the configured Amazon S3
      destination. When set to ``AllDocuments`` , Kinesis Data Firehose delivers all incoming records
      to Amazon S3, and also writes failed documents to Amazon S3. Default value is
      ``FailedDocumentsOnly`` .

    - **S3Update** *(dict) --*

      Your update to the configuration of the backup Amazon S3 location.

      - **RoleARN** *(string) --*

        The Amazon Resource Name (ARN) of the AWS credentials. For more information, see `Amazon
        Resource Names (ARNs) and AWS Service Namespaces
        <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

      - **BucketARN** *(string) --*

        The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs) and AWS
        Service Namespaces
        <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

      - **Prefix** *(string) --*

        The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered Amazon S3 files.
        You can also specify a custom prefix, as described in `Custom Prefixes for Amazon S3 Objects
        <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

      - **ErrorOutputPrefix** *(string) --*

        A prefix that Kinesis Data Firehose evaluates and adds to failed records before writing them
        to S3. This prefix appears immediately following the bucket name. For information about how
        to specify this prefix, see `Custom Prefixes for Amazon S3 Objects
        <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`__ .

      - **BufferingHints** *(dict) --*

        The buffering option. If no value is specified, ``BufferingHints`` object default values are
        used.

        - **SizeInMBs** *(integer) --*

          Buffer incoming data to the specified size, in MiBs, before delivering it to the
          destination. The default value is 5. This parameter is optional but if you specify a value
          for it, you must also specify a value for ``IntervalInSeconds`` , and vice versa.

          We recommend setting this parameter to a value greater than the amount of data you
          typically ingest into the delivery stream in 10 seconds. For example, if you typically
          ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

        - **IntervalInSeconds** *(integer) --*

          Buffer incoming data for the specified period of time, in seconds, before delivering it to
          the destination. The default value is 300. This parameter is optional but if you specify a
          value for it, you must also specify a value for ``SizeInMBs`` , and vice versa.

      - **CompressionFormat** *(string) --*

        The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .

        The compression formats ``SNAPPY`` or ``ZIP`` cannot be specified for Amazon Redshift
        destinations because they are not supported by the Amazon Redshift ``COPY`` operation that
        reads from the S3 bucket.

      - **EncryptionConfiguration** *(dict) --*

        The encryption configuration. If no value is specified, the default is no encryption.

        - **NoEncryptionConfig** *(string) --*

          Specifically override existing encryption information to ensure that no encryption is used.

        - **KMSEncryptionConfig** *(dict) --*

          The encryption key.

          - **AWSKMSKeyARN** *(string) --* **[REQUIRED]**

            The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region
            as the destination Amazon S3 bucket. For more information, see `Amazon Resource Names
            (ARNs) and AWS Service Namespaces
            <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

      - **CloudWatchLoggingOptions** *(dict) --*

        The CloudWatch logging options for your delivery stream.

        - **Enabled** *(boolean) --*

          Enables or disables CloudWatch logging.

        - **LogGroupName** *(string) --*

          The CloudWatch group name for logging. This value is required if CloudWatch logging is
          enabled.

        - **LogStreamName** *(string) --*

          The CloudWatch log stream name for logging. This value is required if CloudWatch logging is
          enabled.

    - **ProcessingConfiguration** *(dict) --*

      The data processing configuration.

      - **Enabled** *(boolean) --*

        Enables or disables data processing.

      - **Processors** *(list) --*

        The data processors.

        - *(dict) --*

          Describes a data processor.

          - **Type** *(string) --* **[REQUIRED]**

            The type of processor.

          - **Parameters** *(list) --*

            The processor parameters.

            - *(dict) --*

              Describes the processor parameter.

              - **ParameterName** *(string) --* **[REQUIRED]**

                The name of the parameter.

              - **ParameterValue** *(string) --* **[REQUIRED]**

                The parameter value.

    - **CloudWatchLoggingOptions** *(dict) --*

      The Amazon CloudWatch logging options for your delivery stream.

      - **Enabled** *(boolean) --*

        Enables or disables CloudWatch logging.

      - **LogGroupName** *(string) --*

        The CloudWatch group name for logging. This value is required if CloudWatch logging is
        enabled.

      - **LogStreamName** *(string) --*

        The CloudWatch log stream name for logging. This value is required if CloudWatch logging is
        enabled.
    """
