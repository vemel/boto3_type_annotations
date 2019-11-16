"Main interface for iotanalytics type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientBatchPutMessageResponsebatchPutMessageErrorEntriesTypeDef",
    "ClientBatchPutMessageResponseTypeDef",
    "ClientBatchPutMessagemessagesTypeDef",
    "ClientCreateChannelResponseretentionPeriodTypeDef",
    "ClientCreateChannelResponseTypeDef",
    "ClientCreateChannelchannelStoragecustomerManagedS3TypeDef",
    "ClientCreateChannelchannelStorageTypeDef",
    "ClientCreateChannelretentionPeriodTypeDef",
    "ClientCreateChanneltagsTypeDef",
    "ClientCreateDatasetContentResponseTypeDef",
    "ClientCreateDatasetResponseretentionPeriodTypeDef",
    "ClientCreateDatasetResponseTypeDef",
    "ClientCreateDatasetactionscontainerActionresourceConfigurationTypeDef",
    "ClientCreateDatasetactionscontainerActionvariablesdatasetContentVersionValueTypeDef",
    "ClientCreateDatasetactionscontainerActionvariablesoutputFileUriValueTypeDef",
    "ClientCreateDatasetactionscontainerActionvariablesTypeDef",
    "ClientCreateDatasetactionscontainerActionTypeDef",
    "ClientCreateDatasetactionsqueryActionfiltersdeltaTimeTypeDef",
    "ClientCreateDatasetactionsqueryActionfiltersTypeDef",
    "ClientCreateDatasetactionsqueryActionTypeDef",
    "ClientCreateDatasetactionsTypeDef",
    "ClientCreateDatasetcontentDeliveryRulesdestinationiotEventsDestinationConfigurationTypeDef",
    "ClientCreateDatasetcontentDeliveryRulesdestinations3DestinationConfigurationglueConfigurationTypeDef",
    "ClientCreateDatasetcontentDeliveryRulesdestinations3DestinationConfigurationTypeDef",
    "ClientCreateDatasetcontentDeliveryRulesdestinationTypeDef",
    "ClientCreateDatasetcontentDeliveryRulesTypeDef",
    "ClientCreateDatasettagsTypeDef",
    "ClientCreateDatasettriggersdatasetTypeDef",
    "ClientCreateDatasettriggersscheduleTypeDef",
    "ClientCreateDatasettriggersTypeDef",
    "ClientCreateDatastoreResponseretentionPeriodTypeDef",
    "ClientCreateDatastoreResponseTypeDef",
    "ClientCreateDatastoredatastoreStoragecustomerManagedS3TypeDef",
    "ClientCreateDatastoredatastoreStorageTypeDef",
    "ClientCreateDatastoreretentionPeriodTypeDef",
    "ClientCreateDatastoretagsTypeDef",
    "ClientCreatePipelineResponseTypeDef",
    "ClientCreatePipelinepipelineActivitiesaddAttributesTypeDef",
    "ClientCreatePipelinepipelineActivitieschannelTypeDef",
    "ClientCreatePipelinepipelineActivitiesdatastoreTypeDef",
    "ClientCreatePipelinepipelineActivitiesdeviceRegistryEnrichTypeDef",
    "ClientCreatePipelinepipelineActivitiesdeviceShadowEnrichTypeDef",
    "ClientCreatePipelinepipelineActivitiesfilterTypeDef",
    "ClientCreatePipelinepipelineActivitieslambdaTypeDef",
    "ClientCreatePipelinepipelineActivitiesmathTypeDef",
    "ClientCreatePipelinepipelineActivitiesremoveAttributesTypeDef",
    "ClientCreatePipelinepipelineActivitiesselectAttributesTypeDef",
    "ClientCreatePipelinepipelineActivitiesTypeDef",
    "ClientCreatePipelinetagsTypeDef",
    "ClientDescribeChannelResponsechannelretentionPeriodTypeDef",
    "ClientDescribeChannelResponsechannelstoragecustomerManagedS3TypeDef",
    "ClientDescribeChannelResponsechannelstorageTypeDef",
    "ClientDescribeChannelResponsechannelTypeDef",
    "ClientDescribeChannelResponsestatisticssizeTypeDef",
    "ClientDescribeChannelResponsestatisticsTypeDef",
    "ClientDescribeChannelResponseTypeDef",
    "ClientDescribeDatastoreResponsedatastoreretentionPeriodTypeDef",
    "ClientDescribeDatastoreResponsedatastorestoragecustomerManagedS3TypeDef",
    "ClientDescribeDatastoreResponsedatastorestorageTypeDef",
    "ClientDescribeDatastoreResponsedatastoreTypeDef",
    "ClientDescribeDatastoreResponsestatisticssizeTypeDef",
    "ClientDescribeDatastoreResponsestatisticsTypeDef",
    "ClientDescribeDatastoreResponseTypeDef",
    "ClientDescribeLoggingOptionsResponseloggingOptionsTypeDef",
    "ClientDescribeLoggingOptionsResponseTypeDef",
    "ClientDescribePipelineResponsepipelineactivitiesaddAttributesTypeDef",
    "ClientDescribePipelineResponsepipelineactivitieschannelTypeDef",
    "ClientDescribePipelineResponsepipelineactivitiesdatastoreTypeDef",
    "ClientDescribePipelineResponsepipelineactivitiesdeviceRegistryEnrichTypeDef",
    "ClientDescribePipelineResponsepipelineactivitiesdeviceShadowEnrichTypeDef",
    "ClientDescribePipelineResponsepipelineactivitiesfilterTypeDef",
    "ClientDescribePipelineResponsepipelineactivitieslambdaTypeDef",
    "ClientDescribePipelineResponsepipelineactivitiesmathTypeDef",
    "ClientDescribePipelineResponsepipelineactivitiesremoveAttributesTypeDef",
    "ClientDescribePipelineResponsepipelineactivitiesselectAttributesTypeDef",
    "ClientDescribePipelineResponsepipelineactivitiesTypeDef",
    "ClientDescribePipelineResponsepipelinereprocessingSummariesTypeDef",
    "ClientDescribePipelineResponsepipelineTypeDef",
    "ClientDescribePipelineResponseTypeDef",
    "ClientGetDatasetContentResponseentriesTypeDef",
    "ClientGetDatasetContentResponsestatusTypeDef",
    "ClientGetDatasetContentResponseTypeDef",
    "ClientListChannelsResponsechannelSummarieschannelStoragecustomerManagedS3TypeDef",
    "ClientListChannelsResponsechannelSummarieschannelStorageTypeDef",
    "ClientListChannelsResponsechannelSummariesTypeDef",
    "ClientListChannelsResponseTypeDef",
    "ClientListDatasetContentsResponsedatasetContentSummariesstatusTypeDef",
    "ClientListDatasetContentsResponsedatasetContentSummariesTypeDef",
    "ClientListDatasetContentsResponseTypeDef",
    "ClientListDatasetsResponsedatasetSummariesactionsTypeDef",
    "ClientListDatasetsResponsedatasetSummariestriggersdatasetTypeDef",
    "ClientListDatasetsResponsedatasetSummariestriggersscheduleTypeDef",
    "ClientListDatasetsResponsedatasetSummariestriggersTypeDef",
    "ClientListDatasetsResponsedatasetSummariesTypeDef",
    "ClientListDatasetsResponseTypeDef",
    "ClientListDatastoresResponsedatastoreSummariesdatastoreStoragecustomerManagedS3TypeDef",
    "ClientListDatastoresResponsedatastoreSummariesdatastoreStorageTypeDef",
    "ClientListDatastoresResponsedatastoreSummariesTypeDef",
    "ClientListDatastoresResponseTypeDef",
    "ClientListPipelinesResponsepipelineSummariesreprocessingSummariesTypeDef",
    "ClientListPipelinesResponsepipelineSummariesTypeDef",
    "ClientListPipelinesResponseTypeDef",
    "ClientListTagsForResourceResponsetagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientPutLoggingOptionsloggingOptionsTypeDef",
    "ClientRunPipelineActivityResponseTypeDef",
    "ClientRunPipelineActivitypipelineActivityaddAttributesTypeDef",
    "ClientRunPipelineActivitypipelineActivitychannelTypeDef",
    "ClientRunPipelineActivitypipelineActivitydatastoreTypeDef",
    "ClientRunPipelineActivitypipelineActivitydeviceRegistryEnrichTypeDef",
    "ClientRunPipelineActivitypipelineActivitydeviceShadowEnrichTypeDef",
    "ClientRunPipelineActivitypipelineActivityfilterTypeDef",
    "ClientRunPipelineActivitypipelineActivitylambdaTypeDef",
    "ClientRunPipelineActivitypipelineActivitymathTypeDef",
    "ClientRunPipelineActivitypipelineActivityremoveAttributesTypeDef",
    "ClientRunPipelineActivitypipelineActivityselectAttributesTypeDef",
    "ClientRunPipelineActivitypipelineActivityTypeDef",
    "ClientSampleChannelDataResponseTypeDef",
    "ClientStartPipelineReprocessingResponseTypeDef",
    "ClientTagResourcetagsTypeDef",
    "ClientUpdateChannelchannelStoragecustomerManagedS3TypeDef",
    "ClientUpdateChannelchannelStorageTypeDef",
    "ClientUpdateChannelretentionPeriodTypeDef",
    "ClientUpdateDatasetactionscontainerActionresourceConfigurationTypeDef",
    "ClientUpdateDatasetactionscontainerActionvariablesdatasetContentVersionValueTypeDef",
    "ClientUpdateDatasetactionscontainerActionvariablesoutputFileUriValueTypeDef",
    "ClientUpdateDatasetactionscontainerActionvariablesTypeDef",
    "ClientUpdateDatasetactionscontainerActionTypeDef",
    "ClientUpdateDatasetactionsqueryActionfiltersdeltaTimeTypeDef",
    "ClientUpdateDatasetactionsqueryActionfiltersTypeDef",
    "ClientUpdateDatasetactionsqueryActionTypeDef",
    "ClientUpdateDatasetactionsTypeDef",
    "ClientUpdateDatasetcontentDeliveryRulesdestinationiotEventsDestinationConfigurationTypeDef",
    "ClientUpdateDatasetcontentDeliveryRulesdestinations3DestinationConfigurationglueConfigurationTypeDef",
    "ClientUpdateDatasetcontentDeliveryRulesdestinations3DestinationConfigurationTypeDef",
    "ClientUpdateDatasetcontentDeliveryRulesdestinationTypeDef",
    "ClientUpdateDatasetcontentDeliveryRulesTypeDef",
    "ClientUpdateDatasetretentionPeriodTypeDef",
    "ClientUpdateDatasettriggersdatasetTypeDef",
    "ClientUpdateDatasettriggersscheduleTypeDef",
    "ClientUpdateDatasettriggersTypeDef",
    "ClientUpdateDatastoredatastoreStoragecustomerManagedS3TypeDef",
    "ClientUpdateDatastoredatastoreStorageTypeDef",
    "ClientUpdateDatastoreretentionPeriodTypeDef",
    "ClientUpdatePipelinepipelineActivitiesaddAttributesTypeDef",
    "ClientUpdatePipelinepipelineActivitieschannelTypeDef",
    "ClientUpdatePipelinepipelineActivitiesdatastoreTypeDef",
    "ClientUpdatePipelinepipelineActivitiesdeviceRegistryEnrichTypeDef",
    "ClientUpdatePipelinepipelineActivitiesdeviceShadowEnrichTypeDef",
    "ClientUpdatePipelinepipelineActivitiesfilterTypeDef",
    "ClientUpdatePipelinepipelineActivitieslambdaTypeDef",
    "ClientUpdatePipelinepipelineActivitiesmathTypeDef",
    "ClientUpdatePipelinepipelineActivitiesremoveAttributesTypeDef",
    "ClientUpdatePipelinepipelineActivitiesselectAttributesTypeDef",
    "ClientUpdatePipelinepipelineActivitiesTypeDef",
    "ListChannelsPaginatePaginationConfigTypeDef",
    "ListChannelsPaginateResponsechannelSummarieschannelStoragecustomerManagedS3TypeDef",
    "ListChannelsPaginateResponsechannelSummarieschannelStorageTypeDef",
    "ListChannelsPaginateResponsechannelSummariesTypeDef",
    "ListChannelsPaginateResponseTypeDef",
    "ListDatasetContentsPaginatePaginationConfigTypeDef",
    "ListDatasetContentsPaginateResponsedatasetContentSummariesstatusTypeDef",
    "ListDatasetContentsPaginateResponsedatasetContentSummariesTypeDef",
    "ListDatasetContentsPaginateResponseTypeDef",
    "ListDatasetsPaginatePaginationConfigTypeDef",
    "ListDatasetsPaginateResponsedatasetSummariesactionsTypeDef",
    "ListDatasetsPaginateResponsedatasetSummariestriggersdatasetTypeDef",
    "ListDatasetsPaginateResponsedatasetSummariestriggersscheduleTypeDef",
    "ListDatasetsPaginateResponsedatasetSummariestriggersTypeDef",
    "ListDatasetsPaginateResponsedatasetSummariesTypeDef",
    "ListDatasetsPaginateResponseTypeDef",
    "ListDatastoresPaginatePaginationConfigTypeDef",
    "ListDatastoresPaginateResponsedatastoreSummariesdatastoreStoragecustomerManagedS3TypeDef",
    "ListDatastoresPaginateResponsedatastoreSummariesdatastoreStorageTypeDef",
    "ListDatastoresPaginateResponsedatastoreSummariesTypeDef",
    "ListDatastoresPaginateResponseTypeDef",
    "ListPipelinesPaginatePaginationConfigTypeDef",
    "ListPipelinesPaginateResponsepipelineSummariesreprocessingSummariesTypeDef",
    "ListPipelinesPaginateResponsepipelineSummariesTypeDef",
    "ListPipelinesPaginateResponseTypeDef",
)


_ClientBatchPutMessageResponsebatchPutMessageErrorEntriesTypeDef = TypedDict(
    "_ClientBatchPutMessageResponsebatchPutMessageErrorEntriesTypeDef",
    {"messageId": str, "errorCode": str, "errorMessage": str},
    total=False,
)


class ClientBatchPutMessageResponsebatchPutMessageErrorEntriesTypeDef(
    _ClientBatchPutMessageResponsebatchPutMessageErrorEntriesTypeDef
):
    """
    Type definition for `ClientBatchPutMessageResponse` `batchPutMessageErrorEntries`

    Contains informations about errors.

    - **messageId** *(string) --*

      The ID of the message that caused the error. (See the value corresponding to the
      "messageId" key in the message object.)

    - **errorCode** *(string) --*

      The code associated with the error.

    - **errorMessage** *(string) --*

      The message associated with the error.
    """


_ClientBatchPutMessageResponseTypeDef = TypedDict(
    "_ClientBatchPutMessageResponseTypeDef",
    {
        "batchPutMessageErrorEntries": List[
            ClientBatchPutMessageResponsebatchPutMessageErrorEntriesTypeDef
        ]
    },
    total=False,
)


class ClientBatchPutMessageResponseTypeDef(_ClientBatchPutMessageResponseTypeDef):
    """
    Type definition for `ClientBatchPutMessage` `Response`

    - **batchPutMessageErrorEntries** *(list) --*

      A list of any errors encountered when sending the messages to the channel.

      - *(dict) --*

        Contains informations about errors.

        - **messageId** *(string) --*

          The ID of the message that caused the error. (See the value corresponding to the
          "messageId" key in the message object.)

        - **errorCode** *(string) --*

          The code associated with the error.

        - **errorMessage** *(string) --*

          The message associated with the error.
    """


_ClientBatchPutMessagemessagesTypeDef = TypedDict(
    "_ClientBatchPutMessagemessagesTypeDef", {"messageId": str, "payload": bytes}
)


class ClientBatchPutMessagemessagesTypeDef(_ClientBatchPutMessagemessagesTypeDef):
    """
    Type definition for `ClientBatchPutMessage` `messages`

    Information about a message.

    - **messageId** *(string) --* **[REQUIRED]**

      The ID you wish to assign to the message. Each "messageId" must be unique within each batch
      sent.

    - **payload** *(bytes) --* **[REQUIRED]**

      The payload of the message. This may be a JSON string or a Base64-encoded string representing
      binary data (in which case you must decode it by means of a pipeline activity).
    """


_ClientCreateChannelResponseretentionPeriodTypeDef = TypedDict(
    "_ClientCreateChannelResponseretentionPeriodTypeDef",
    {"unlimited": bool, "numberOfDays": int},
    total=False,
)


class ClientCreateChannelResponseretentionPeriodTypeDef(
    _ClientCreateChannelResponseretentionPeriodTypeDef
):
    """
    Type definition for `ClientCreateChannelResponse` `retentionPeriod`

    How long, in days, message data is kept for the channel.

    - **unlimited** *(boolean) --*

      If true, message data is kept indefinitely.

    - **numberOfDays** *(integer) --*

      The number of days that message data is kept. The "unlimited" parameter must be false.
    """


_ClientCreateChannelResponseTypeDef = TypedDict(
    "_ClientCreateChannelResponseTypeDef",
    {
        "channelName": str,
        "channelArn": str,
        "retentionPeriod": ClientCreateChannelResponseretentionPeriodTypeDef,
    },
    total=False,
)


class ClientCreateChannelResponseTypeDef(_ClientCreateChannelResponseTypeDef):
    """
    Type definition for `ClientCreateChannel` `Response`

    - **channelName** *(string) --*

      The name of the channel.

    - **channelArn** *(string) --*

      The ARN of the channel.

    - **retentionPeriod** *(dict) --*

      How long, in days, message data is kept for the channel.

      - **unlimited** *(boolean) --*

        If true, message data is kept indefinitely.

      - **numberOfDays** *(integer) --*

        The number of days that message data is kept. The "unlimited" parameter must be false.
    """


_RequiredClientCreateChannelchannelStoragecustomerManagedS3TypeDef = TypedDict(
    "_RequiredClientCreateChannelchannelStoragecustomerManagedS3TypeDef",
    {"bucket": str, "roleArn": str},
)
_OptionalClientCreateChannelchannelStoragecustomerManagedS3TypeDef = TypedDict(
    "_OptionalClientCreateChannelchannelStoragecustomerManagedS3TypeDef",
    {"keyPrefix": str},
    total=False,
)


class ClientCreateChannelchannelStoragecustomerManagedS3TypeDef(
    _RequiredClientCreateChannelchannelStoragecustomerManagedS3TypeDef,
    _OptionalClientCreateChannelchannelStoragecustomerManagedS3TypeDef,
):
    """
    Type definition for `ClientCreateChannelchannelStorage` `customerManagedS3`

    Use this to store channel data in an S3 bucket that you manage. If customer managed storage is
    selected, the "retentionPeriod" parameter is ignored. The choice of service-managed or
    customer-managed S3 storage cannot be changed after creation of the channel.

    - **bucket** *(string) --* **[REQUIRED]**

      The name of the Amazon S3 bucket in which channel data is stored.

    - **keyPrefix** *(string) --*

      [Optional] The prefix used to create the keys of the channel data objects. Each object in an
      Amazon S3 bucket has a key that is its unique identifier within the bucket (each object in a
      bucket has exactly one key). The prefix must end with a '/'.

    - **roleArn** *(string) --* **[REQUIRED]**

      The ARN of the role which grants AWS IoT Analytics permission to interact with your Amazon S3
      resources.
    """


_ClientCreateChannelchannelStorageTypeDef = TypedDict(
    "_ClientCreateChannelchannelStorageTypeDef",
    {
        "serviceManagedS3": Dict,
        "customerManagedS3": ClientCreateChannelchannelStoragecustomerManagedS3TypeDef,
    },
    total=False,
)


class ClientCreateChannelchannelStorageTypeDef(
    _ClientCreateChannelchannelStorageTypeDef
):
    """
    Type definition for `ClientCreateChannel` `channelStorage`

    Where channel data is stored. You may choose one of "serviceManagedS3" or "customerManagedS3"
    storage. If not specified, the default is "serviceManagedS3". This cannot be changed after
    creation of the channel.

    - **serviceManagedS3** *(dict) --*

      Use this to store channel data in an S3 bucket managed by the AWS IoT Analytics service. The
      choice of service-managed or customer-managed S3 storage cannot be changed after creation of
      the channel.

    - **customerManagedS3** *(dict) --*

      Use this to store channel data in an S3 bucket that you manage. If customer managed storage is
      selected, the "retentionPeriod" parameter is ignored. The choice of service-managed or
      customer-managed S3 storage cannot be changed after creation of the channel.

      - **bucket** *(string) --* **[REQUIRED]**

        The name of the Amazon S3 bucket in which channel data is stored.

      - **keyPrefix** *(string) --*

        [Optional] The prefix used to create the keys of the channel data objects. Each object in an
        Amazon S3 bucket has a key that is its unique identifier within the bucket (each object in a
        bucket has exactly one key). The prefix must end with a '/'.

      - **roleArn** *(string) --* **[REQUIRED]**

        The ARN of the role which grants AWS IoT Analytics permission to interact with your Amazon S3
        resources.
    """


_ClientCreateChannelretentionPeriodTypeDef = TypedDict(
    "_ClientCreateChannelretentionPeriodTypeDef",
    {"unlimited": bool, "numberOfDays": int},
    total=False,
)


class ClientCreateChannelretentionPeriodTypeDef(
    _ClientCreateChannelretentionPeriodTypeDef
):
    """
    Type definition for `ClientCreateChannel` `retentionPeriod`

    How long, in days, message data is kept for the channel. When "customerManagedS3" storage is
    selected, this parameter is ignored.

    - **unlimited** *(boolean) --*

      If true, message data is kept indefinitely.

    - **numberOfDays** *(integer) --*

      The number of days that message data is kept. The "unlimited" parameter must be false.
    """


_ClientCreateChanneltagsTypeDef = TypedDict(
    "_ClientCreateChanneltagsTypeDef", {"key": str, "value": str}
)


class ClientCreateChanneltagsTypeDef(_ClientCreateChanneltagsTypeDef):
    """
    Type definition for `ClientCreateChannel` `tags`

    A set of key/value pairs which are used to manage the resource.

    - **key** *(string) --* **[REQUIRED]**

      The tag's key.

    - **value** *(string) --* **[REQUIRED]**

      The tag's value.
    """


_ClientCreateDatasetContentResponseTypeDef = TypedDict(
    "_ClientCreateDatasetContentResponseTypeDef", {"versionId": str}, total=False
)


class ClientCreateDatasetContentResponseTypeDef(
    _ClientCreateDatasetContentResponseTypeDef
):
    """
    Type definition for `ClientCreateDatasetContent` `Response`

    - **versionId** *(string) --*

      The version ID of the data set contents which are being created.
    """


_ClientCreateDatasetResponseretentionPeriodTypeDef = TypedDict(
    "_ClientCreateDatasetResponseretentionPeriodTypeDef",
    {"unlimited": bool, "numberOfDays": int},
    total=False,
)


class ClientCreateDatasetResponseretentionPeriodTypeDef(
    _ClientCreateDatasetResponseretentionPeriodTypeDef
):
    """
    Type definition for `ClientCreateDatasetResponse` `retentionPeriod`

    How long, in days, data set contents are kept for the data set.

    - **unlimited** *(boolean) --*

      If true, message data is kept indefinitely.

    - **numberOfDays** *(integer) --*

      The number of days that message data is kept. The "unlimited" parameter must be false.
    """


_ClientCreateDatasetResponseTypeDef = TypedDict(
    "_ClientCreateDatasetResponseTypeDef",
    {
        "datasetName": str,
        "datasetArn": str,
        "retentionPeriod": ClientCreateDatasetResponseretentionPeriodTypeDef,
    },
    total=False,
)


class ClientCreateDatasetResponseTypeDef(_ClientCreateDatasetResponseTypeDef):
    """
    Type definition for `ClientCreateDataset` `Response`

    - **datasetName** *(string) --*

      The name of the data set.

    - **datasetArn** *(string) --*

      The ARN of the data set.

    - **retentionPeriod** *(dict) --*

      How long, in days, data set contents are kept for the data set.

      - **unlimited** *(boolean) --*

        If true, message data is kept indefinitely.

      - **numberOfDays** *(integer) --*

        The number of days that message data is kept. The "unlimited" parameter must be false.
    """


_ClientCreateDatasetactionscontainerActionresourceConfigurationTypeDef = TypedDict(
    "_ClientCreateDatasetactionscontainerActionresourceConfigurationTypeDef",
    {"computeType": str, "volumeSizeInGB": int},
)


class ClientCreateDatasetactionscontainerActionresourceConfigurationTypeDef(
    _ClientCreateDatasetactionscontainerActionresourceConfigurationTypeDef
):
    """
    Type definition for `ClientCreateDatasetactionscontainerAction` `resourceConfiguration`

    Configuration of the resource which executes the "containerAction".

    - **computeType** *(string) --* **[REQUIRED]**

      The type of the compute resource used to execute the "containerAction". Possible values
      are: ACU_1 (vCPU=4, memory=16GiB) or ACU_2 (vCPU=8, memory=32GiB).

    - **volumeSizeInGB** *(integer) --* **[REQUIRED]**

      The size (in GB) of the persistent storage available to the resource instance used to
      execute the "containerAction" (min: 1, max: 50).
    """


_ClientCreateDatasetactionscontainerActionvariablesdatasetContentVersionValueTypeDef = TypedDict(
    "_ClientCreateDatasetactionscontainerActionvariablesdatasetContentVersionValueTypeDef",
    {"datasetName": str},
)


class ClientCreateDatasetactionscontainerActionvariablesdatasetContentVersionValueTypeDef(
    _ClientCreateDatasetactionscontainerActionvariablesdatasetContentVersionValueTypeDef
):
    """
    Type definition for `ClientCreateDatasetactionscontainerActionvariables` `datasetContentVersionValue`

    The value of the variable as a structure that specifies a data set content version.

    - **datasetName** *(string) --* **[REQUIRED]**

      The name of the data set whose latest contents are used as input to the notebook or
      application.
    """


_ClientCreateDatasetactionscontainerActionvariablesoutputFileUriValueTypeDef = TypedDict(
    "_ClientCreateDatasetactionscontainerActionvariablesoutputFileUriValueTypeDef",
    {"fileName": str},
)


class ClientCreateDatasetactionscontainerActionvariablesoutputFileUriValueTypeDef(
    _ClientCreateDatasetactionscontainerActionvariablesoutputFileUriValueTypeDef
):
    """
    Type definition for `ClientCreateDatasetactionscontainerActionvariables` `outputFileUriValue`

    The value of the variable as a structure that specifies an output file URI.

    - **fileName** *(string) --* **[REQUIRED]**

      The URI of the location where data set contents are stored, usually the URI of a file
      in an S3 bucket.
    """


_RequiredClientCreateDatasetactionscontainerActionvariablesTypeDef = TypedDict(
    "_RequiredClientCreateDatasetactionscontainerActionvariablesTypeDef", {"name": str}
)
_OptionalClientCreateDatasetactionscontainerActionvariablesTypeDef = TypedDict(
    "_OptionalClientCreateDatasetactionscontainerActionvariablesTypeDef",
    {
        "stringValue": str,
        "doubleValue": float,
        "datasetContentVersionValue": ClientCreateDatasetactionscontainerActionvariablesdatasetContentVersionValueTypeDef,
        "outputFileUriValue": ClientCreateDatasetactionscontainerActionvariablesoutputFileUriValueTypeDef,
    },
    total=False,
)


class ClientCreateDatasetactionscontainerActionvariablesTypeDef(
    _RequiredClientCreateDatasetactionscontainerActionvariablesTypeDef,
    _OptionalClientCreateDatasetactionscontainerActionvariablesTypeDef,
):
    """
    Type definition for `ClientCreateDatasetactionscontainerAction` `variables`

    An instance of a variable to be passed to the "containerAction" execution. Each variable
    must have a name and a value given by one of "stringValue", "datasetContentVersionValue",
    or "outputFileUriValue".

    - **name** *(string) --* **[REQUIRED]**

      The name of the variable.

    - **stringValue** *(string) --*

      The value of the variable as a string.

    - **doubleValue** *(float) --*

      The value of the variable as a double (numeric).

    - **datasetContentVersionValue** *(dict) --*

      The value of the variable as a structure that specifies a data set content version.

      - **datasetName** *(string) --* **[REQUIRED]**

        The name of the data set whose latest contents are used as input to the notebook or
        application.

    - **outputFileUriValue** *(dict) --*

      The value of the variable as a structure that specifies an output file URI.

      - **fileName** *(string) --* **[REQUIRED]**

        The URI of the location where data set contents are stored, usually the URI of a file
        in an S3 bucket.
    """


_RequiredClientCreateDatasetactionscontainerActionTypeDef = TypedDict(
    "_RequiredClientCreateDatasetactionscontainerActionTypeDef",
    {
        "image": str,
        "executionRoleArn": str,
        "resourceConfiguration": ClientCreateDatasetactionscontainerActionresourceConfigurationTypeDef,
    },
)
_OptionalClientCreateDatasetactionscontainerActionTypeDef = TypedDict(
    "_OptionalClientCreateDatasetactionscontainerActionTypeDef",
    {"variables": List[ClientCreateDatasetactionscontainerActionvariablesTypeDef]},
    total=False,
)


class ClientCreateDatasetactionscontainerActionTypeDef(
    _RequiredClientCreateDatasetactionscontainerActionTypeDef,
    _OptionalClientCreateDatasetactionscontainerActionTypeDef,
):
    """
    Type definition for `ClientCreateDatasetactions` `containerAction`

    Information which allows the system to run a containerized application in order to create the
    data set contents. The application must be in a Docker container along with any needed
    support libraries.

    - **image** *(string) --* **[REQUIRED]**

      The ARN of the Docker container stored in your account. The Docker container contains an
      application and needed support libraries and is used to generate data set contents.

    - **executionRoleArn** *(string) --* **[REQUIRED]**

      The ARN of the role which gives permission to the system to access needed resources in
      order to run the "containerAction". This includes, at minimum, permission to retrieve the
      data set contents which are the input to the containerized application.

    - **resourceConfiguration** *(dict) --* **[REQUIRED]**

      Configuration of the resource which executes the "containerAction".

      - **computeType** *(string) --* **[REQUIRED]**

        The type of the compute resource used to execute the "containerAction". Possible values
        are: ACU_1 (vCPU=4, memory=16GiB) or ACU_2 (vCPU=8, memory=32GiB).

      - **volumeSizeInGB** *(integer) --* **[REQUIRED]**

        The size (in GB) of the persistent storage available to the resource instance used to
        execute the "containerAction" (min: 1, max: 50).

    - **variables** *(list) --*

      The values of variables used within the context of the execution of the containerized
      application (basically, parameters passed to the application). Each variable must have a
      name and a value given by one of "stringValue", "datasetContentVersionValue", or
      "outputFileUriValue".

      - *(dict) --*

        An instance of a variable to be passed to the "containerAction" execution. Each variable
        must have a name and a value given by one of "stringValue", "datasetContentVersionValue",
        or "outputFileUriValue".

        - **name** *(string) --* **[REQUIRED]**

          The name of the variable.

        - **stringValue** *(string) --*

          The value of the variable as a string.

        - **doubleValue** *(float) --*

          The value of the variable as a double (numeric).

        - **datasetContentVersionValue** *(dict) --*

          The value of the variable as a structure that specifies a data set content version.

          - **datasetName** *(string) --* **[REQUIRED]**

            The name of the data set whose latest contents are used as input to the notebook or
            application.

        - **outputFileUriValue** *(dict) --*

          The value of the variable as a structure that specifies an output file URI.

          - **fileName** *(string) --* **[REQUIRED]**

            The URI of the location where data set contents are stored, usually the URI of a file
            in an S3 bucket.
    """


_ClientCreateDatasetactionsqueryActionfiltersdeltaTimeTypeDef = TypedDict(
    "_ClientCreateDatasetactionsqueryActionfiltersdeltaTimeTypeDef",
    {"offsetSeconds": int, "timeExpression": str},
)


class ClientCreateDatasetactionsqueryActionfiltersdeltaTimeTypeDef(
    _ClientCreateDatasetactionsqueryActionfiltersdeltaTimeTypeDef
):
    """
    Type definition for `ClientCreateDatasetactionsqueryActionfilters` `deltaTime`

    Used to limit data to that which has arrived since the last execution of the action.

    - **offsetSeconds** *(integer) --* **[REQUIRED]**

      The number of seconds of estimated "in flight" lag time of message data. When you
      create data set contents using message data from a specified time frame, some message
      data may still be "in flight" when processing begins, and so will not arrive in time
      to be processed. Use this field to make allowances for the "in flight" time of your
      message data, so that data not processed from a previous time frame will be included
      with the next time frame. Without this, missed message data would be excluded from
      processing during the next time frame as well, because its timestamp places it within
      the previous time frame.

    - **timeExpression** *(string) --* **[REQUIRED]**

      An expression by which the time of the message data may be determined. This may be
      the name of a timestamp field, or a SQL expression which is used to derive the time
      the message data was generated.
    """


_ClientCreateDatasetactionsqueryActionfiltersTypeDef = TypedDict(
    "_ClientCreateDatasetactionsqueryActionfiltersTypeDef",
    {"deltaTime": ClientCreateDatasetactionsqueryActionfiltersdeltaTimeTypeDef},
    total=False,
)


class ClientCreateDatasetactionsqueryActionfiltersTypeDef(
    _ClientCreateDatasetactionsqueryActionfiltersTypeDef
):
    """
    Type definition for `ClientCreateDatasetactionsqueryAction` `filters`

    Information which is used to filter message data, to segregate it according to the time
    frame in which it arrives.

    - **deltaTime** *(dict) --*

      Used to limit data to that which has arrived since the last execution of the action.

      - **offsetSeconds** *(integer) --* **[REQUIRED]**

        The number of seconds of estimated "in flight" lag time of message data. When you
        create data set contents using message data from a specified time frame, some message
        data may still be "in flight" when processing begins, and so will not arrive in time
        to be processed. Use this field to make allowances for the "in flight" time of your
        message data, so that data not processed from a previous time frame will be included
        with the next time frame. Without this, missed message data would be excluded from
        processing during the next time frame as well, because its timestamp places it within
        the previous time frame.

      - **timeExpression** *(string) --* **[REQUIRED]**

        An expression by which the time of the message data may be determined. This may be
        the name of a timestamp field, or a SQL expression which is used to derive the time
        the message data was generated.
    """


_RequiredClientCreateDatasetactionsqueryActionTypeDef = TypedDict(
    "_RequiredClientCreateDatasetactionsqueryActionTypeDef", {"sqlQuery": str}
)
_OptionalClientCreateDatasetactionsqueryActionTypeDef = TypedDict(
    "_OptionalClientCreateDatasetactionsqueryActionTypeDef",
    {"filters": List[ClientCreateDatasetactionsqueryActionfiltersTypeDef]},
    total=False,
)


class ClientCreateDatasetactionsqueryActionTypeDef(
    _RequiredClientCreateDatasetactionsqueryActionTypeDef,
    _OptionalClientCreateDatasetactionsqueryActionTypeDef,
):
    """
    Type definition for `ClientCreateDatasetactions` `queryAction`

    An "SqlQueryDatasetAction" object that uses an SQL query to automatically create data set
    contents.

    - **sqlQuery** *(string) --* **[REQUIRED]**

      A SQL query string.

    - **filters** *(list) --*

      Pre-filters applied to message data.

      - *(dict) --*

        Information which is used to filter message data, to segregate it according to the time
        frame in which it arrives.

        - **deltaTime** *(dict) --*

          Used to limit data to that which has arrived since the last execution of the action.

          - **offsetSeconds** *(integer) --* **[REQUIRED]**

            The number of seconds of estimated "in flight" lag time of message data. When you
            create data set contents using message data from a specified time frame, some message
            data may still be "in flight" when processing begins, and so will not arrive in time
            to be processed. Use this field to make allowances for the "in flight" time of your
            message data, so that data not processed from a previous time frame will be included
            with the next time frame. Without this, missed message data would be excluded from
            processing during the next time frame as well, because its timestamp places it within
            the previous time frame.

          - **timeExpression** *(string) --* **[REQUIRED]**

            An expression by which the time of the message data may be determined. This may be
            the name of a timestamp field, or a SQL expression which is used to derive the time
            the message data was generated.
    """


_ClientCreateDatasetactionsTypeDef = TypedDict(
    "_ClientCreateDatasetactionsTypeDef",
    {
        "actionName": str,
        "queryAction": ClientCreateDatasetactionsqueryActionTypeDef,
        "containerAction": ClientCreateDatasetactionscontainerActionTypeDef,
    },
    total=False,
)


class ClientCreateDatasetactionsTypeDef(_ClientCreateDatasetactionsTypeDef):
    """
    Type definition for `ClientCreateDataset` `actions`

    A "DatasetAction" object that specifies how data set contents are automatically created.

    - **actionName** *(string) --*

      The name of the data set action by which data set contents are automatically created.

    - **queryAction** *(dict) --*

      An "SqlQueryDatasetAction" object that uses an SQL query to automatically create data set
      contents.

      - **sqlQuery** *(string) --* **[REQUIRED]**

        A SQL query string.

      - **filters** *(list) --*

        Pre-filters applied to message data.

        - *(dict) --*

          Information which is used to filter message data, to segregate it according to the time
          frame in which it arrives.

          - **deltaTime** *(dict) --*

            Used to limit data to that which has arrived since the last execution of the action.

            - **offsetSeconds** *(integer) --* **[REQUIRED]**

              The number of seconds of estimated "in flight" lag time of message data. When you
              create data set contents using message data from a specified time frame, some message
              data may still be "in flight" when processing begins, and so will not arrive in time
              to be processed. Use this field to make allowances for the "in flight" time of your
              message data, so that data not processed from a previous time frame will be included
              with the next time frame. Without this, missed message data would be excluded from
              processing during the next time frame as well, because its timestamp places it within
              the previous time frame.

            - **timeExpression** *(string) --* **[REQUIRED]**

              An expression by which the time of the message data may be determined. This may be
              the name of a timestamp field, or a SQL expression which is used to derive the time
              the message data was generated.

    - **containerAction** *(dict) --*

      Information which allows the system to run a containerized application in order to create the
      data set contents. The application must be in a Docker container along with any needed
      support libraries.

      - **image** *(string) --* **[REQUIRED]**

        The ARN of the Docker container stored in your account. The Docker container contains an
        application and needed support libraries and is used to generate data set contents.

      - **executionRoleArn** *(string) --* **[REQUIRED]**

        The ARN of the role which gives permission to the system to access needed resources in
        order to run the "containerAction". This includes, at minimum, permission to retrieve the
        data set contents which are the input to the containerized application.

      - **resourceConfiguration** *(dict) --* **[REQUIRED]**

        Configuration of the resource which executes the "containerAction".

        - **computeType** *(string) --* **[REQUIRED]**

          The type of the compute resource used to execute the "containerAction". Possible values
          are: ACU_1 (vCPU=4, memory=16GiB) or ACU_2 (vCPU=8, memory=32GiB).

        - **volumeSizeInGB** *(integer) --* **[REQUIRED]**

          The size (in GB) of the persistent storage available to the resource instance used to
          execute the "containerAction" (min: 1, max: 50).

      - **variables** *(list) --*

        The values of variables used within the context of the execution of the containerized
        application (basically, parameters passed to the application). Each variable must have a
        name and a value given by one of "stringValue", "datasetContentVersionValue", or
        "outputFileUriValue".

        - *(dict) --*

          An instance of a variable to be passed to the "containerAction" execution. Each variable
          must have a name and a value given by one of "stringValue", "datasetContentVersionValue",
          or "outputFileUriValue".

          - **name** *(string) --* **[REQUIRED]**

            The name of the variable.

          - **stringValue** *(string) --*

            The value of the variable as a string.

          - **doubleValue** *(float) --*

            The value of the variable as a double (numeric).

          - **datasetContentVersionValue** *(dict) --*

            The value of the variable as a structure that specifies a data set content version.

            - **datasetName** *(string) --* **[REQUIRED]**

              The name of the data set whose latest contents are used as input to the notebook or
              application.

          - **outputFileUriValue** *(dict) --*

            The value of the variable as a structure that specifies an output file URI.

            - **fileName** *(string) --* **[REQUIRED]**

              The URI of the location where data set contents are stored, usually the URI of a file
              in an S3 bucket.
    """


_ClientCreateDatasetcontentDeliveryRulesdestinationiotEventsDestinationConfigurationTypeDef = TypedDict(
    "_ClientCreateDatasetcontentDeliveryRulesdestinationiotEventsDestinationConfigurationTypeDef",
    {"inputName": str, "roleArn": str},
)


class ClientCreateDatasetcontentDeliveryRulesdestinationiotEventsDestinationConfigurationTypeDef(
    _ClientCreateDatasetcontentDeliveryRulesdestinationiotEventsDestinationConfigurationTypeDef
):
    """
    Type definition for `ClientCreateDatasetcontentDeliveryRulesdestination` `iotEventsDestinationConfiguration`

    Configuration information for delivery of data set contents to AWS IoT Events.

    - **inputName** *(string) --* **[REQUIRED]**

      The name of the AWS IoT Events input to which data set contents are delivered.

    - **roleArn** *(string) --* **[REQUIRED]**

      The ARN of the role which grants AWS IoT Analytics permission to deliver data set
      contents to an AWS IoT Events input.
    """


_ClientCreateDatasetcontentDeliveryRulesdestinations3DestinationConfigurationglueConfigurationTypeDef = TypedDict(
    "_ClientCreateDatasetcontentDeliveryRulesdestinations3DestinationConfigurationglueConfigurationTypeDef",
    {"tableName": str, "databaseName": str},
)


class ClientCreateDatasetcontentDeliveryRulesdestinations3DestinationConfigurationglueConfigurationTypeDef(
    _ClientCreateDatasetcontentDeliveryRulesdestinations3DestinationConfigurationglueConfigurationTypeDef
):
    """
    Type definition for `ClientCreateDatasetcontentDeliveryRulesdestinations3DestinationConfiguration` `glueConfiguration`

    Configuration information for coordination with the AWS Glue ETL (extract, transform and
    load) service.

    - **tableName** *(string) --* **[REQUIRED]**

      The name of the table in your AWS Glue Data Catalog which is used to perform the ETL
      (extract, transform and load) operations. (An AWS Glue Data Catalog table contains
      partitioned data and descriptions of data sources and targets.)

    - **databaseName** *(string) --* **[REQUIRED]**

      The name of the database in your AWS Glue Data Catalog in which the table is located.
      (An AWS Glue Data Catalog database contains Glue Data tables.)
    """


_RequiredClientCreateDatasetcontentDeliveryRulesdestinations3DestinationConfigurationTypeDef = TypedDict(
    "_RequiredClientCreateDatasetcontentDeliveryRulesdestinations3DestinationConfigurationTypeDef",
    {"bucket": str, "key": str, "roleArn": str},
)
_OptionalClientCreateDatasetcontentDeliveryRulesdestinations3DestinationConfigurationTypeDef = TypedDict(
    "_OptionalClientCreateDatasetcontentDeliveryRulesdestinations3DestinationConfigurationTypeDef",
    {
        "glueConfiguration": ClientCreateDatasetcontentDeliveryRulesdestinations3DestinationConfigurationglueConfigurationTypeDef
    },
    total=False,
)


class ClientCreateDatasetcontentDeliveryRulesdestinations3DestinationConfigurationTypeDef(
    _RequiredClientCreateDatasetcontentDeliveryRulesdestinations3DestinationConfigurationTypeDef,
    _OptionalClientCreateDatasetcontentDeliveryRulesdestinations3DestinationConfigurationTypeDef,
):
    """
    Type definition for `ClientCreateDatasetcontentDeliveryRulesdestination` `s3DestinationConfiguration`

    Configuration information for delivery of data set contents to Amazon S3.

    - **bucket** *(string) --* **[REQUIRED]**

      The name of the Amazon S3 bucket to which data set contents are delivered.

    - **key** *(string) --* **[REQUIRED]**

      The key of the data set contents object. Each object in an Amazon S3 bucket has a key
      that is its unique identifier within the bucket (each object in a bucket has exactly one
      key). To produce a unique key, you can use "!{iotanalytics:scheduledTime}" to insert the
      time of the scheduled SQL query run, or "!{iotanalytics:versioned} to insert a unique
      hash identifying the data set, for example:
      "/DataSet/!{iotanalytics:scheduledTime}/!{iotanalytics:versioned}.csv".

    - **glueConfiguration** *(dict) --*

      Configuration information for coordination with the AWS Glue ETL (extract, transform and
      load) service.

      - **tableName** *(string) --* **[REQUIRED]**

        The name of the table in your AWS Glue Data Catalog which is used to perform the ETL
        (extract, transform and load) operations. (An AWS Glue Data Catalog table contains
        partitioned data and descriptions of data sources and targets.)

      - **databaseName** *(string) --* **[REQUIRED]**

        The name of the database in your AWS Glue Data Catalog in which the table is located.
        (An AWS Glue Data Catalog database contains Glue Data tables.)

    - **roleArn** *(string) --* **[REQUIRED]**

      The ARN of the role which grants AWS IoT Analytics permission to interact with your
      Amazon S3 and AWS Glue resources.
    """


_ClientCreateDatasetcontentDeliveryRulesdestinationTypeDef = TypedDict(
    "_ClientCreateDatasetcontentDeliveryRulesdestinationTypeDef",
    {
        "iotEventsDestinationConfiguration": ClientCreateDatasetcontentDeliveryRulesdestinationiotEventsDestinationConfigurationTypeDef,
        "s3DestinationConfiguration": ClientCreateDatasetcontentDeliveryRulesdestinations3DestinationConfigurationTypeDef,
    },
    total=False,
)


class ClientCreateDatasetcontentDeliveryRulesdestinationTypeDef(
    _ClientCreateDatasetcontentDeliveryRulesdestinationTypeDef
):
    """
    Type definition for `ClientCreateDatasetcontentDeliveryRules` `destination`

    The destination to which data set contents are delivered.

    - **iotEventsDestinationConfiguration** *(dict) --*

      Configuration information for delivery of data set contents to AWS IoT Events.

      - **inputName** *(string) --* **[REQUIRED]**

        The name of the AWS IoT Events input to which data set contents are delivered.

      - **roleArn** *(string) --* **[REQUIRED]**

        The ARN of the role which grants AWS IoT Analytics permission to deliver data set
        contents to an AWS IoT Events input.

    - **s3DestinationConfiguration** *(dict) --*

      Configuration information for delivery of data set contents to Amazon S3.

      - **bucket** *(string) --* **[REQUIRED]**

        The name of the Amazon S3 bucket to which data set contents are delivered.

      - **key** *(string) --* **[REQUIRED]**

        The key of the data set contents object. Each object in an Amazon S3 bucket has a key
        that is its unique identifier within the bucket (each object in a bucket has exactly one
        key). To produce a unique key, you can use "!{iotanalytics:scheduledTime}" to insert the
        time of the scheduled SQL query run, or "!{iotanalytics:versioned} to insert a unique
        hash identifying the data set, for example:
        "/DataSet/!{iotanalytics:scheduledTime}/!{iotanalytics:versioned}.csv".

      - **glueConfiguration** *(dict) --*

        Configuration information for coordination with the AWS Glue ETL (extract, transform and
        load) service.

        - **tableName** *(string) --* **[REQUIRED]**

          The name of the table in your AWS Glue Data Catalog which is used to perform the ETL
          (extract, transform and load) operations. (An AWS Glue Data Catalog table contains
          partitioned data and descriptions of data sources and targets.)

        - **databaseName** *(string) --* **[REQUIRED]**

          The name of the database in your AWS Glue Data Catalog in which the table is located.
          (An AWS Glue Data Catalog database contains Glue Data tables.)

      - **roleArn** *(string) --* **[REQUIRED]**

        The ARN of the role which grants AWS IoT Analytics permission to interact with your
        Amazon S3 and AWS Glue resources.
    """


_RequiredClientCreateDatasetcontentDeliveryRulesTypeDef = TypedDict(
    "_RequiredClientCreateDatasetcontentDeliveryRulesTypeDef",
    {"destination": ClientCreateDatasetcontentDeliveryRulesdestinationTypeDef},
)
_OptionalClientCreateDatasetcontentDeliveryRulesTypeDef = TypedDict(
    "_OptionalClientCreateDatasetcontentDeliveryRulesTypeDef",
    {"entryName": str},
    total=False,
)


class ClientCreateDatasetcontentDeliveryRulesTypeDef(
    _RequiredClientCreateDatasetcontentDeliveryRulesTypeDef,
    _OptionalClientCreateDatasetcontentDeliveryRulesTypeDef,
):
    """
    Type definition for `ClientCreateDataset` `contentDeliveryRules`

    When data set contents are created they are delivered to destination specified here.

    - **entryName** *(string) --*

      The name of the data set content delivery rules entry.

    - **destination** *(dict) --* **[REQUIRED]**

      The destination to which data set contents are delivered.

      - **iotEventsDestinationConfiguration** *(dict) --*

        Configuration information for delivery of data set contents to AWS IoT Events.

        - **inputName** *(string) --* **[REQUIRED]**

          The name of the AWS IoT Events input to which data set contents are delivered.

        - **roleArn** *(string) --* **[REQUIRED]**

          The ARN of the role which grants AWS IoT Analytics permission to deliver data set
          contents to an AWS IoT Events input.

      - **s3DestinationConfiguration** *(dict) --*

        Configuration information for delivery of data set contents to Amazon S3.

        - **bucket** *(string) --* **[REQUIRED]**

          The name of the Amazon S3 bucket to which data set contents are delivered.

        - **key** *(string) --* **[REQUIRED]**

          The key of the data set contents object. Each object in an Amazon S3 bucket has a key
          that is its unique identifier within the bucket (each object in a bucket has exactly one
          key). To produce a unique key, you can use "!{iotanalytics:scheduledTime}" to insert the
          time of the scheduled SQL query run, or "!{iotanalytics:versioned} to insert a unique
          hash identifying the data set, for example:
          "/DataSet/!{iotanalytics:scheduledTime}/!{iotanalytics:versioned}.csv".

        - **glueConfiguration** *(dict) --*

          Configuration information for coordination with the AWS Glue ETL (extract, transform and
          load) service.

          - **tableName** *(string) --* **[REQUIRED]**

            The name of the table in your AWS Glue Data Catalog which is used to perform the ETL
            (extract, transform and load) operations. (An AWS Glue Data Catalog table contains
            partitioned data and descriptions of data sources and targets.)

          - **databaseName** *(string) --* **[REQUIRED]**

            The name of the database in your AWS Glue Data Catalog in which the table is located.
            (An AWS Glue Data Catalog database contains Glue Data tables.)

        - **roleArn** *(string) --* **[REQUIRED]**

          The ARN of the role which grants AWS IoT Analytics permission to interact with your
          Amazon S3 and AWS Glue resources.
    """


_ClientCreateDatasettagsTypeDef = TypedDict(
    "_ClientCreateDatasettagsTypeDef", {"key": str, "value": str}
)


class ClientCreateDatasettagsTypeDef(_ClientCreateDatasettagsTypeDef):
    """
    Type definition for `ClientCreateDataset` `tags`

    A set of key/value pairs which are used to manage the resource.

    - **key** *(string) --* **[REQUIRED]**

      The tag's key.

    - **value** *(string) --* **[REQUIRED]**

      The tag's value.
    """


_ClientCreateDatasettriggersdatasetTypeDef = TypedDict(
    "_ClientCreateDatasettriggersdatasetTypeDef", {"name": str}
)


class ClientCreateDatasettriggersdatasetTypeDef(
    _ClientCreateDatasettriggersdatasetTypeDef
):
    """
    Type definition for `ClientCreateDatasettriggers` `dataset`

    The data set whose content creation triggers the creation of this data set's contents.

    - **name** *(string) --* **[REQUIRED]**

      The name of the data set whose content generation triggers the new data set content
      generation.
    """


_ClientCreateDatasettriggersscheduleTypeDef = TypedDict(
    "_ClientCreateDatasettriggersscheduleTypeDef", {"expression": str}, total=False
)


class ClientCreateDatasettriggersscheduleTypeDef(
    _ClientCreateDatasettriggersscheduleTypeDef
):
    """
    Type definition for `ClientCreateDatasettriggers` `schedule`

    The "Schedule" when the trigger is initiated.

    - **expression** *(string) --*

      The expression that defines when to trigger an update. For more information, see `Schedule
      Expressions for Rules
      <https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html>`__ in the
      Amazon CloudWatch Events User Guide.
    """


_ClientCreateDatasettriggersTypeDef = TypedDict(
    "_ClientCreateDatasettriggersTypeDef",
    {
        "schedule": ClientCreateDatasettriggersscheduleTypeDef,
        "dataset": ClientCreateDatasettriggersdatasetTypeDef,
    },
    total=False,
)


class ClientCreateDatasettriggersTypeDef(_ClientCreateDatasettriggersTypeDef):
    """
    Type definition for `ClientCreateDataset` `triggers`

    The "DatasetTrigger" that specifies when the data set is automatically updated.

    - **schedule** *(dict) --*

      The "Schedule" when the trigger is initiated.

      - **expression** *(string) --*

        The expression that defines when to trigger an update. For more information, see `Schedule
        Expressions for Rules
        <https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html>`__ in the
        Amazon CloudWatch Events User Guide.

    - **dataset** *(dict) --*

      The data set whose content creation triggers the creation of this data set's contents.

      - **name** *(string) --* **[REQUIRED]**

        The name of the data set whose content generation triggers the new data set content
        generation.
    """


_ClientCreateDatastoreResponseretentionPeriodTypeDef = TypedDict(
    "_ClientCreateDatastoreResponseretentionPeriodTypeDef",
    {"unlimited": bool, "numberOfDays": int},
    total=False,
)


class ClientCreateDatastoreResponseretentionPeriodTypeDef(
    _ClientCreateDatastoreResponseretentionPeriodTypeDef
):
    """
    Type definition for `ClientCreateDatastoreResponse` `retentionPeriod`

    How long, in days, message data is kept for the data store.

    - **unlimited** *(boolean) --*

      If true, message data is kept indefinitely.

    - **numberOfDays** *(integer) --*

      The number of days that message data is kept. The "unlimited" parameter must be false.
    """


_ClientCreateDatastoreResponseTypeDef = TypedDict(
    "_ClientCreateDatastoreResponseTypeDef",
    {
        "datastoreName": str,
        "datastoreArn": str,
        "retentionPeriod": ClientCreateDatastoreResponseretentionPeriodTypeDef,
    },
    total=False,
)


class ClientCreateDatastoreResponseTypeDef(_ClientCreateDatastoreResponseTypeDef):
    """
    Type definition for `ClientCreateDatastore` `Response`

    - **datastoreName** *(string) --*

      The name of the data store.

    - **datastoreArn** *(string) --*

      The ARN of the data store.

    - **retentionPeriod** *(dict) --*

      How long, in days, message data is kept for the data store.

      - **unlimited** *(boolean) --*

        If true, message data is kept indefinitely.

      - **numberOfDays** *(integer) --*

        The number of days that message data is kept. The "unlimited" parameter must be false.
    """


_RequiredClientCreateDatastoredatastoreStoragecustomerManagedS3TypeDef = TypedDict(
    "_RequiredClientCreateDatastoredatastoreStoragecustomerManagedS3TypeDef",
    {"bucket": str, "roleArn": str},
)
_OptionalClientCreateDatastoredatastoreStoragecustomerManagedS3TypeDef = TypedDict(
    "_OptionalClientCreateDatastoredatastoreStoragecustomerManagedS3TypeDef",
    {"keyPrefix": str},
    total=False,
)


class ClientCreateDatastoredatastoreStoragecustomerManagedS3TypeDef(
    _RequiredClientCreateDatastoredatastoreStoragecustomerManagedS3TypeDef,
    _OptionalClientCreateDatastoredatastoreStoragecustomerManagedS3TypeDef,
):
    """
    Type definition for `ClientCreateDatastoredatastoreStorage` `customerManagedS3`

    Use this to store data store data in an S3 bucket that you manage. When customer managed
    storage is selected, the "retentionPeriod" parameter is ignored. The choice of service-managed
    or customer-managed S3 storage cannot be changed after creation of the data store.

    - **bucket** *(string) --* **[REQUIRED]**

      The name of the Amazon S3 bucket in which data store data is stored.

    - **keyPrefix** *(string) --*

      [Optional] The prefix used to create the keys of the data store data objects. Each object in
      an Amazon S3 bucket has a key that is its unique identifier within the bucket (each object in
      a bucket has exactly one key). The prefix must end with a '/'.

    - **roleArn** *(string) --* **[REQUIRED]**

      The ARN of the role which grants AWS IoT Analytics permission to interact with your Amazon S3
      resources.
    """


_ClientCreateDatastoredatastoreStorageTypeDef = TypedDict(
    "_ClientCreateDatastoredatastoreStorageTypeDef",
    {
        "serviceManagedS3": Dict,
        "customerManagedS3": ClientCreateDatastoredatastoreStoragecustomerManagedS3TypeDef,
    },
    total=False,
)


class ClientCreateDatastoredatastoreStorageTypeDef(
    _ClientCreateDatastoredatastoreStorageTypeDef
):
    """
    Type definition for `ClientCreateDatastore` `datastoreStorage`

    Where data store data is stored. You may choose one of "serviceManagedS3" or "customerManagedS3"
    storage. If not specified, the default is "serviceManagedS3". This cannot be changed after the
    data store is created.

    - **serviceManagedS3** *(dict) --*

      Use this to store data store data in an S3 bucket managed by the AWS IoT Analytics service. The
      choice of service-managed or customer-managed S3 storage cannot be changed after creation of
      the data store.

    - **customerManagedS3** *(dict) --*

      Use this to store data store data in an S3 bucket that you manage. When customer managed
      storage is selected, the "retentionPeriod" parameter is ignored. The choice of service-managed
      or customer-managed S3 storage cannot be changed after creation of the data store.

      - **bucket** *(string) --* **[REQUIRED]**

        The name of the Amazon S3 bucket in which data store data is stored.

      - **keyPrefix** *(string) --*

        [Optional] The prefix used to create the keys of the data store data objects. Each object in
        an Amazon S3 bucket has a key that is its unique identifier within the bucket (each object in
        a bucket has exactly one key). The prefix must end with a '/'.

      - **roleArn** *(string) --* **[REQUIRED]**

        The ARN of the role which grants AWS IoT Analytics permission to interact with your Amazon S3
        resources.
    """


_ClientCreateDatastoreretentionPeriodTypeDef = TypedDict(
    "_ClientCreateDatastoreretentionPeriodTypeDef",
    {"unlimited": bool, "numberOfDays": int},
    total=False,
)


class ClientCreateDatastoreretentionPeriodTypeDef(
    _ClientCreateDatastoreretentionPeriodTypeDef
):
    """
    Type definition for `ClientCreateDatastore` `retentionPeriod`

    How long, in days, message data is kept for the data store. When "customerManagedS3" storage is
    selected, this parameter is ignored.

    - **unlimited** *(boolean) --*

      If true, message data is kept indefinitely.

    - **numberOfDays** *(integer) --*

      The number of days that message data is kept. The "unlimited" parameter must be false.
    """


_ClientCreateDatastoretagsTypeDef = TypedDict(
    "_ClientCreateDatastoretagsTypeDef", {"key": str, "value": str}
)


class ClientCreateDatastoretagsTypeDef(_ClientCreateDatastoretagsTypeDef):
    """
    Type definition for `ClientCreateDatastore` `tags`

    A set of key/value pairs which are used to manage the resource.

    - **key** *(string) --* **[REQUIRED]**

      The tag's key.

    - **value** *(string) --* **[REQUIRED]**

      The tag's value.
    """


_ClientCreatePipelineResponseTypeDef = TypedDict(
    "_ClientCreatePipelineResponseTypeDef",
    {"pipelineName": str, "pipelineArn": str},
    total=False,
)


class ClientCreatePipelineResponseTypeDef(_ClientCreatePipelineResponseTypeDef):
    """
    Type definition for `ClientCreatePipeline` `Response`

    - **pipelineName** *(string) --*

      The name of the pipeline.

    - **pipelineArn** *(string) --*

      The ARN of the pipeline.
    """


_RequiredClientCreatePipelinepipelineActivitiesaddAttributesTypeDef = TypedDict(
    "_RequiredClientCreatePipelinepipelineActivitiesaddAttributesTypeDef",
    {"name": str, "attributes": Dict[str, str]},
)
_OptionalClientCreatePipelinepipelineActivitiesaddAttributesTypeDef = TypedDict(
    "_OptionalClientCreatePipelinepipelineActivitiesaddAttributesTypeDef",
    {"next": str},
    total=False,
)


class ClientCreatePipelinepipelineActivitiesaddAttributesTypeDef(
    _RequiredClientCreatePipelinepipelineActivitiesaddAttributesTypeDef,
    _OptionalClientCreatePipelinepipelineActivitiesaddAttributesTypeDef,
):
    """
    Type definition for `ClientCreatePipelinepipelineActivities` `addAttributes`

    Adds other attributes based on existing attributes in the message.

    - **name** *(string) --* **[REQUIRED]**

      The name of the 'addAttributes' activity.

    - **attributes** *(dict) --* **[REQUIRED]**

      A list of 1-50 "AttributeNameMapping" objects that map an existing attribute to a new
      attribute.

      .. note::

        The existing attributes remain in the message, so if you want to remove the originals,
        use "RemoveAttributeActivity".

      - *(string) --*

        - *(string) --*

    - **next** *(string) --*

      The next activity in the pipeline.
    """


_RequiredClientCreatePipelinepipelineActivitieschannelTypeDef = TypedDict(
    "_RequiredClientCreatePipelinepipelineActivitieschannelTypeDef",
    {"name": str, "channelName": str},
)
_OptionalClientCreatePipelinepipelineActivitieschannelTypeDef = TypedDict(
    "_OptionalClientCreatePipelinepipelineActivitieschannelTypeDef",
    {"next": str},
    total=False,
)


class ClientCreatePipelinepipelineActivitieschannelTypeDef(
    _RequiredClientCreatePipelinepipelineActivitieschannelTypeDef,
    _OptionalClientCreatePipelinepipelineActivitieschannelTypeDef,
):
    """
    Type definition for `ClientCreatePipelinepipelineActivities` `channel`

    Determines the source of the messages to be processed.

    - **name** *(string) --* **[REQUIRED]**

      The name of the 'channel' activity.

    - **channelName** *(string) --* **[REQUIRED]**

      The name of the channel from which the messages are processed.

    - **next** *(string) --*

      The next activity in the pipeline.
    """


_ClientCreatePipelinepipelineActivitiesdatastoreTypeDef = TypedDict(
    "_ClientCreatePipelinepipelineActivitiesdatastoreTypeDef",
    {"name": str, "datastoreName": str},
)


class ClientCreatePipelinepipelineActivitiesdatastoreTypeDef(
    _ClientCreatePipelinepipelineActivitiesdatastoreTypeDef
):
    """
    Type definition for `ClientCreatePipelinepipelineActivities` `datastore`

    Specifies where to store the processed message data.

    - **name** *(string) --* **[REQUIRED]**

      The name of the 'datastore' activity.

    - **datastoreName** *(string) --* **[REQUIRED]**

      The name of the data store where processed messages are stored.
    """


_RequiredClientCreatePipelinepipelineActivitiesdeviceRegistryEnrichTypeDef = TypedDict(
    "_RequiredClientCreatePipelinepipelineActivitiesdeviceRegistryEnrichTypeDef",
    {"name": str, "attribute": str, "thingName": str, "roleArn": str},
)
_OptionalClientCreatePipelinepipelineActivitiesdeviceRegistryEnrichTypeDef = TypedDict(
    "_OptionalClientCreatePipelinepipelineActivitiesdeviceRegistryEnrichTypeDef",
    {"next": str},
    total=False,
)


class ClientCreatePipelinepipelineActivitiesdeviceRegistryEnrichTypeDef(
    _RequiredClientCreatePipelinepipelineActivitiesdeviceRegistryEnrichTypeDef,
    _OptionalClientCreatePipelinepipelineActivitiesdeviceRegistryEnrichTypeDef,
):
    """
    Type definition for `ClientCreatePipelinepipelineActivities` `deviceRegistryEnrich`

    Adds data from the AWS IoT device registry to your message.

    - **name** *(string) --* **[REQUIRED]**

      The name of the 'deviceRegistryEnrich' activity.

    - **attribute** *(string) --* **[REQUIRED]**

      The name of the attribute that is added to the message.

    - **thingName** *(string) --* **[REQUIRED]**

      The name of the IoT device whose registry information is added to the message.

    - **roleArn** *(string) --* **[REQUIRED]**

      The ARN of the role that allows access to the device's registry information.

    - **next** *(string) --*

      The next activity in the pipeline.
    """


_RequiredClientCreatePipelinepipelineActivitiesdeviceShadowEnrichTypeDef = TypedDict(
    "_RequiredClientCreatePipelinepipelineActivitiesdeviceShadowEnrichTypeDef",
    {"name": str, "attribute": str, "thingName": str, "roleArn": str},
)
_OptionalClientCreatePipelinepipelineActivitiesdeviceShadowEnrichTypeDef = TypedDict(
    "_OptionalClientCreatePipelinepipelineActivitiesdeviceShadowEnrichTypeDef",
    {"next": str},
    total=False,
)


class ClientCreatePipelinepipelineActivitiesdeviceShadowEnrichTypeDef(
    _RequiredClientCreatePipelinepipelineActivitiesdeviceShadowEnrichTypeDef,
    _OptionalClientCreatePipelinepipelineActivitiesdeviceShadowEnrichTypeDef,
):
    """
    Type definition for `ClientCreatePipelinepipelineActivities` `deviceShadowEnrich`

    Adds information from the AWS IoT Device Shadows service to a message.

    - **name** *(string) --* **[REQUIRED]**

      The name of the 'deviceShadowEnrich' activity.

    - **attribute** *(string) --* **[REQUIRED]**

      The name of the attribute that is added to the message.

    - **thingName** *(string) --* **[REQUIRED]**

      The name of the IoT device whose shadow information is added to the message.

    - **roleArn** *(string) --* **[REQUIRED]**

      The ARN of the role that allows access to the device's shadow.

    - **next** *(string) --*

      The next activity in the pipeline.
    """


_RequiredClientCreatePipelinepipelineActivitiesfilterTypeDef = TypedDict(
    "_RequiredClientCreatePipelinepipelineActivitiesfilterTypeDef",
    {"name": str, "filter": str},
)
_OptionalClientCreatePipelinepipelineActivitiesfilterTypeDef = TypedDict(
    "_OptionalClientCreatePipelinepipelineActivitiesfilterTypeDef",
    {"next": str},
    total=False,
)


class ClientCreatePipelinepipelineActivitiesfilterTypeDef(
    _RequiredClientCreatePipelinepipelineActivitiesfilterTypeDef,
    _OptionalClientCreatePipelinepipelineActivitiesfilterTypeDef,
):
    """
    Type definition for `ClientCreatePipelinepipelineActivities` `filter`

    Filters a message based on its attributes.

    - **name** *(string) --* **[REQUIRED]**

      The name of the 'filter' activity.

    - **filter** *(string) --* **[REQUIRED]**

      An expression that looks like a SQL WHERE clause that must return a Boolean value.

    - **next** *(string) --*

      The next activity in the pipeline.
    """


_RequiredClientCreatePipelinepipelineActivitieslambdaTypeDef = TypedDict(
    "_RequiredClientCreatePipelinepipelineActivitieslambdaTypeDef",
    {"name": str, "lambdaName": str, "batchSize": int},
)
_OptionalClientCreatePipelinepipelineActivitieslambdaTypeDef = TypedDict(
    "_OptionalClientCreatePipelinepipelineActivitieslambdaTypeDef",
    {"next": str},
    total=False,
)


class ClientCreatePipelinepipelineActivitieslambdaTypeDef(
    _RequiredClientCreatePipelinepipelineActivitieslambdaTypeDef,
    _OptionalClientCreatePipelinepipelineActivitieslambdaTypeDef,
):
    """
    Type definition for `ClientCreatePipelinepipelineActivities` `lambda`

    Runs a Lambda function to modify the message.

    - **name** *(string) --* **[REQUIRED]**

      The name of the 'lambda' activity.

    - **lambdaName** *(string) --* **[REQUIRED]**

      The name of the Lambda function that is run on the message.

    - **batchSize** *(integer) --* **[REQUIRED]**

      The number of messages passed to the Lambda function for processing.

      The AWS Lambda function must be able to process all of these messages within five minutes,
      which is the maximum timeout duration for Lambda functions.

    - **next** *(string) --*

      The next activity in the pipeline.
    """


_RequiredClientCreatePipelinepipelineActivitiesmathTypeDef = TypedDict(
    "_RequiredClientCreatePipelinepipelineActivitiesmathTypeDef",
    {"name": str, "attribute": str, "math": str},
)
_OptionalClientCreatePipelinepipelineActivitiesmathTypeDef = TypedDict(
    "_OptionalClientCreatePipelinepipelineActivitiesmathTypeDef",
    {"next": str},
    total=False,
)


class ClientCreatePipelinepipelineActivitiesmathTypeDef(
    _RequiredClientCreatePipelinepipelineActivitiesmathTypeDef,
    _OptionalClientCreatePipelinepipelineActivitiesmathTypeDef,
):
    """
    Type definition for `ClientCreatePipelinepipelineActivities` `math`

    Computes an arithmetic expression using the message's attributes and adds it to the message.

    - **name** *(string) --* **[REQUIRED]**

      The name of the 'math' activity.

    - **attribute** *(string) --* **[REQUIRED]**

      The name of the attribute that contains the result of the math operation.

    - **math** *(string) --* **[REQUIRED]**

      An expression that uses one or more existing attributes and must return an integer value.

    - **next** *(string) --*

      The next activity in the pipeline.
    """


_RequiredClientCreatePipelinepipelineActivitiesremoveAttributesTypeDef = TypedDict(
    "_RequiredClientCreatePipelinepipelineActivitiesremoveAttributesTypeDef",
    {"name": str, "attributes": List[str]},
)
_OptionalClientCreatePipelinepipelineActivitiesremoveAttributesTypeDef = TypedDict(
    "_OptionalClientCreatePipelinepipelineActivitiesremoveAttributesTypeDef",
    {"next": str},
    total=False,
)


class ClientCreatePipelinepipelineActivitiesremoveAttributesTypeDef(
    _RequiredClientCreatePipelinepipelineActivitiesremoveAttributesTypeDef,
    _OptionalClientCreatePipelinepipelineActivitiesremoveAttributesTypeDef,
):
    """
    Type definition for `ClientCreatePipelinepipelineActivities` `removeAttributes`

    Removes attributes from a message.

    - **name** *(string) --* **[REQUIRED]**

      The name of the 'removeAttributes' activity.

    - **attributes** *(list) --* **[REQUIRED]**

      A list of 1-50 attributes to remove from the message.

      - *(string) --*

    - **next** *(string) --*

      The next activity in the pipeline.
    """


_RequiredClientCreatePipelinepipelineActivitiesselectAttributesTypeDef = TypedDict(
    "_RequiredClientCreatePipelinepipelineActivitiesselectAttributesTypeDef",
    {"name": str, "attributes": List[str]},
)
_OptionalClientCreatePipelinepipelineActivitiesselectAttributesTypeDef = TypedDict(
    "_OptionalClientCreatePipelinepipelineActivitiesselectAttributesTypeDef",
    {"next": str},
    total=False,
)


class ClientCreatePipelinepipelineActivitiesselectAttributesTypeDef(
    _RequiredClientCreatePipelinepipelineActivitiesselectAttributesTypeDef,
    _OptionalClientCreatePipelinepipelineActivitiesselectAttributesTypeDef,
):
    """
    Type definition for `ClientCreatePipelinepipelineActivities` `selectAttributes`

    Creates a new message using only the specified attributes from the original message.

    - **name** *(string) --* **[REQUIRED]**

      The name of the 'selectAttributes' activity.

    - **attributes** *(list) --* **[REQUIRED]**

      A list of the attributes to select from the message.

      - *(string) --*

    - **next** *(string) --*

      The next activity in the pipeline.
    """


_ClientCreatePipelinepipelineActivitiesTypeDef = TypedDict(
    "_ClientCreatePipelinepipelineActivitiesTypeDef",
    {
        "channel": ClientCreatePipelinepipelineActivitieschannelTypeDef,
        "lambda": ClientCreatePipelinepipelineActivitieslambdaTypeDef,
        "datastore": ClientCreatePipelinepipelineActivitiesdatastoreTypeDef,
        "addAttributes": ClientCreatePipelinepipelineActivitiesaddAttributesTypeDef,
        "removeAttributes": ClientCreatePipelinepipelineActivitiesremoveAttributesTypeDef,
        "selectAttributes": ClientCreatePipelinepipelineActivitiesselectAttributesTypeDef,
        "filter": ClientCreatePipelinepipelineActivitiesfilterTypeDef,
        "math": ClientCreatePipelinepipelineActivitiesmathTypeDef,
        "deviceRegistryEnrich": ClientCreatePipelinepipelineActivitiesdeviceRegistryEnrichTypeDef,
        "deviceShadowEnrich": ClientCreatePipelinepipelineActivitiesdeviceShadowEnrichTypeDef,
    },
    total=False,
)


class ClientCreatePipelinepipelineActivitiesTypeDef(
    _ClientCreatePipelinepipelineActivitiesTypeDef
):
    """
    Type definition for `ClientCreatePipeline` `pipelineActivities`

    An activity that performs a transformation on a message.

    - **channel** *(dict) --*

      Determines the source of the messages to be processed.

      - **name** *(string) --* **[REQUIRED]**

        The name of the 'channel' activity.

      - **channelName** *(string) --* **[REQUIRED]**

        The name of the channel from which the messages are processed.

      - **next** *(string) --*

        The next activity in the pipeline.

    - **lambda** *(dict) --*

      Runs a Lambda function to modify the message.

      - **name** *(string) --* **[REQUIRED]**

        The name of the 'lambda' activity.

      - **lambdaName** *(string) --* **[REQUIRED]**

        The name of the Lambda function that is run on the message.

      - **batchSize** *(integer) --* **[REQUIRED]**

        The number of messages passed to the Lambda function for processing.

        The AWS Lambda function must be able to process all of these messages within five minutes,
        which is the maximum timeout duration for Lambda functions.

      - **next** *(string) --*

        The next activity in the pipeline.

    - **datastore** *(dict) --*

      Specifies where to store the processed message data.

      - **name** *(string) --* **[REQUIRED]**

        The name of the 'datastore' activity.

      - **datastoreName** *(string) --* **[REQUIRED]**

        The name of the data store where processed messages are stored.

    - **addAttributes** *(dict) --*

      Adds other attributes based on existing attributes in the message.

      - **name** *(string) --* **[REQUIRED]**

        The name of the 'addAttributes' activity.

      - **attributes** *(dict) --* **[REQUIRED]**

        A list of 1-50 "AttributeNameMapping" objects that map an existing attribute to a new
        attribute.

        .. note::

          The existing attributes remain in the message, so if you want to remove the originals,
          use "RemoveAttributeActivity".

        - *(string) --*

          - *(string) --*

      - **next** *(string) --*

        The next activity in the pipeline.

    - **removeAttributes** *(dict) --*

      Removes attributes from a message.

      - **name** *(string) --* **[REQUIRED]**

        The name of the 'removeAttributes' activity.

      - **attributes** *(list) --* **[REQUIRED]**

        A list of 1-50 attributes to remove from the message.

        - *(string) --*

      - **next** *(string) --*

        The next activity in the pipeline.

    - **selectAttributes** *(dict) --*

      Creates a new message using only the specified attributes from the original message.

      - **name** *(string) --* **[REQUIRED]**

        The name of the 'selectAttributes' activity.

      - **attributes** *(list) --* **[REQUIRED]**

        A list of the attributes to select from the message.

        - *(string) --*

      - **next** *(string) --*

        The next activity in the pipeline.

    - **filter** *(dict) --*

      Filters a message based on its attributes.

      - **name** *(string) --* **[REQUIRED]**

        The name of the 'filter' activity.

      - **filter** *(string) --* **[REQUIRED]**

        An expression that looks like a SQL WHERE clause that must return a Boolean value.

      - **next** *(string) --*

        The next activity in the pipeline.

    - **math** *(dict) --*

      Computes an arithmetic expression using the message's attributes and adds it to the message.

      - **name** *(string) --* **[REQUIRED]**

        The name of the 'math' activity.

      - **attribute** *(string) --* **[REQUIRED]**

        The name of the attribute that contains the result of the math operation.

      - **math** *(string) --* **[REQUIRED]**

        An expression that uses one or more existing attributes and must return an integer value.

      - **next** *(string) --*

        The next activity in the pipeline.

    - **deviceRegistryEnrich** *(dict) --*

      Adds data from the AWS IoT device registry to your message.

      - **name** *(string) --* **[REQUIRED]**

        The name of the 'deviceRegistryEnrich' activity.

      - **attribute** *(string) --* **[REQUIRED]**

        The name of the attribute that is added to the message.

      - **thingName** *(string) --* **[REQUIRED]**

        The name of the IoT device whose registry information is added to the message.

      - **roleArn** *(string) --* **[REQUIRED]**

        The ARN of the role that allows access to the device's registry information.

      - **next** *(string) --*

        The next activity in the pipeline.

    - **deviceShadowEnrich** *(dict) --*

      Adds information from the AWS IoT Device Shadows service to a message.

      - **name** *(string) --* **[REQUIRED]**

        The name of the 'deviceShadowEnrich' activity.

      - **attribute** *(string) --* **[REQUIRED]**

        The name of the attribute that is added to the message.

      - **thingName** *(string) --* **[REQUIRED]**

        The name of the IoT device whose shadow information is added to the message.

      - **roleArn** *(string) --* **[REQUIRED]**

        The ARN of the role that allows access to the device's shadow.

      - **next** *(string) --*

        The next activity in the pipeline.
    """


_ClientCreatePipelinetagsTypeDef = TypedDict(
    "_ClientCreatePipelinetagsTypeDef", {"key": str, "value": str}
)


class ClientCreatePipelinetagsTypeDef(_ClientCreatePipelinetagsTypeDef):
    """
    Type definition for `ClientCreatePipeline` `tags`

    A set of key/value pairs which are used to manage the resource.

    - **key** *(string) --* **[REQUIRED]**

      The tag's key.

    - **value** *(string) --* **[REQUIRED]**

      The tag's value.
    """


_ClientDescribeChannelResponsechannelretentionPeriodTypeDef = TypedDict(
    "_ClientDescribeChannelResponsechannelretentionPeriodTypeDef",
    {"unlimited": bool, "numberOfDays": int},
    total=False,
)


class ClientDescribeChannelResponsechannelretentionPeriodTypeDef(
    _ClientDescribeChannelResponsechannelretentionPeriodTypeDef
):
    """
    Type definition for `ClientDescribeChannelResponsechannel` `retentionPeriod`

    How long, in days, message data is kept for the channel.

    - **unlimited** *(boolean) --*

      If true, message data is kept indefinitely.

    - **numberOfDays** *(integer) --*

      The number of days that message data is kept. The "unlimited" parameter must be false.
    """


_ClientDescribeChannelResponsechannelstoragecustomerManagedS3TypeDef = TypedDict(
    "_ClientDescribeChannelResponsechannelstoragecustomerManagedS3TypeDef",
    {"bucket": str, "keyPrefix": str, "roleArn": str},
    total=False,
)


class ClientDescribeChannelResponsechannelstoragecustomerManagedS3TypeDef(
    _ClientDescribeChannelResponsechannelstoragecustomerManagedS3TypeDef
):
    """
    Type definition for `ClientDescribeChannelResponsechannelstorage` `customerManagedS3`

    Use this to store channel data in an S3 bucket that you manage. If customer managed
    storage is selected, the "retentionPeriod" parameter is ignored. The choice of
    service-managed or customer-managed S3 storage cannot be changed after creation of the
    channel.

    - **bucket** *(string) --*

      The name of the Amazon S3 bucket in which channel data is stored.

    - **keyPrefix** *(string) --*

      [Optional] The prefix used to create the keys of the channel data objects. Each object
      in an Amazon S3 bucket has a key that is its unique identifier within the bucket (each
      object in a bucket has exactly one key). The prefix must end with a '/'.

    - **roleArn** *(string) --*

      The ARN of the role which grants AWS IoT Analytics permission to interact with your
      Amazon S3 resources.
    """


_ClientDescribeChannelResponsechannelstorageTypeDef = TypedDict(
    "_ClientDescribeChannelResponsechannelstorageTypeDef",
    {
        "serviceManagedS3": Dict,
        "customerManagedS3": ClientDescribeChannelResponsechannelstoragecustomerManagedS3TypeDef,
    },
    total=False,
)


class ClientDescribeChannelResponsechannelstorageTypeDef(
    _ClientDescribeChannelResponsechannelstorageTypeDef
):
    """
    Type definition for `ClientDescribeChannelResponsechannel` `storage`

    Where channel data is stored. You may choose one of "serviceManagedS3" or
    "customerManagedS3" storage. If not specified, the default is "serviceManagedS3". This
    cannot be changed after creation of the channel.

    - **serviceManagedS3** *(dict) --*

      Use this to store channel data in an S3 bucket managed by the AWS IoT Analytics service.
      The choice of service-managed or customer-managed S3 storage cannot be changed after
      creation of the channel.

    - **customerManagedS3** *(dict) --*

      Use this to store channel data in an S3 bucket that you manage. If customer managed
      storage is selected, the "retentionPeriod" parameter is ignored. The choice of
      service-managed or customer-managed S3 storage cannot be changed after creation of the
      channel.

      - **bucket** *(string) --*

        The name of the Amazon S3 bucket in which channel data is stored.

      - **keyPrefix** *(string) --*

        [Optional] The prefix used to create the keys of the channel data objects. Each object
        in an Amazon S3 bucket has a key that is its unique identifier within the bucket (each
        object in a bucket has exactly one key). The prefix must end with a '/'.

      - **roleArn** *(string) --*

        The ARN of the role which grants AWS IoT Analytics permission to interact with your
        Amazon S3 resources.
    """


_ClientDescribeChannelResponsechannelTypeDef = TypedDict(
    "_ClientDescribeChannelResponsechannelTypeDef",
    {
        "name": str,
        "storage": ClientDescribeChannelResponsechannelstorageTypeDef,
        "arn": str,
        "status": str,
        "retentionPeriod": ClientDescribeChannelResponsechannelretentionPeriodTypeDef,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
    },
    total=False,
)


class ClientDescribeChannelResponsechannelTypeDef(
    _ClientDescribeChannelResponsechannelTypeDef
):
    """
    Type definition for `ClientDescribeChannelResponse` `channel`

    An object that contains information about the channel.

    - **name** *(string) --*

      The name of the channel.

    - **storage** *(dict) --*

      Where channel data is stored. You may choose one of "serviceManagedS3" or
      "customerManagedS3" storage. If not specified, the default is "serviceManagedS3". This
      cannot be changed after creation of the channel.

      - **serviceManagedS3** *(dict) --*

        Use this to store channel data in an S3 bucket managed by the AWS IoT Analytics service.
        The choice of service-managed or customer-managed S3 storage cannot be changed after
        creation of the channel.

      - **customerManagedS3** *(dict) --*

        Use this to store channel data in an S3 bucket that you manage. If customer managed
        storage is selected, the "retentionPeriod" parameter is ignored. The choice of
        service-managed or customer-managed S3 storage cannot be changed after creation of the
        channel.

        - **bucket** *(string) --*

          The name of the Amazon S3 bucket in which channel data is stored.

        - **keyPrefix** *(string) --*

          [Optional] The prefix used to create the keys of the channel data objects. Each object
          in an Amazon S3 bucket has a key that is its unique identifier within the bucket (each
          object in a bucket has exactly one key). The prefix must end with a '/'.

        - **roleArn** *(string) --*

          The ARN of the role which grants AWS IoT Analytics permission to interact with your
          Amazon S3 resources.

    - **arn** *(string) --*

      The ARN of the channel.

    - **status** *(string) --*

      The status of the channel.

    - **retentionPeriod** *(dict) --*

      How long, in days, message data is kept for the channel.

      - **unlimited** *(boolean) --*

        If true, message data is kept indefinitely.

      - **numberOfDays** *(integer) --*

        The number of days that message data is kept. The "unlimited" parameter must be false.

    - **creationTime** *(datetime) --*

      When the channel was created.

    - **lastUpdateTime** *(datetime) --*

      When the channel was last updated.
    """


_ClientDescribeChannelResponsestatisticssizeTypeDef = TypedDict(
    "_ClientDescribeChannelResponsestatisticssizeTypeDef",
    {"estimatedSizeInBytes": float, "estimatedOn": datetime},
    total=False,
)


class ClientDescribeChannelResponsestatisticssizeTypeDef(
    _ClientDescribeChannelResponsestatisticssizeTypeDef
):
    """
    Type definition for `ClientDescribeChannelResponsestatistics` `size`

    The estimated size of the channel.

    - **estimatedSizeInBytes** *(float) --*

      The estimated size of the resource in bytes.

    - **estimatedOn** *(datetime) --*

      The time when the estimate of the size of the resource was made.
    """


_ClientDescribeChannelResponsestatisticsTypeDef = TypedDict(
    "_ClientDescribeChannelResponsestatisticsTypeDef",
    {"size": ClientDescribeChannelResponsestatisticssizeTypeDef},
    total=False,
)


class ClientDescribeChannelResponsestatisticsTypeDef(
    _ClientDescribeChannelResponsestatisticsTypeDef
):
    """
    Type definition for `ClientDescribeChannelResponse` `statistics`

    Statistics about the channel. Included if the 'includeStatistics' parameter is set to true in
    the request.

    - **size** *(dict) --*

      The estimated size of the channel.

      - **estimatedSizeInBytes** *(float) --*

        The estimated size of the resource in bytes.

      - **estimatedOn** *(datetime) --*

        The time when the estimate of the size of the resource was made.
    """


_ClientDescribeChannelResponseTypeDef = TypedDict(
    "_ClientDescribeChannelResponseTypeDef",
    {
        "channel": ClientDescribeChannelResponsechannelTypeDef,
        "statistics": ClientDescribeChannelResponsestatisticsTypeDef,
    },
    total=False,
)


class ClientDescribeChannelResponseTypeDef(_ClientDescribeChannelResponseTypeDef):
    """
    Type definition for `ClientDescribeChannel` `Response`

    - **channel** *(dict) --*

      An object that contains information about the channel.

      - **name** *(string) --*

        The name of the channel.

      - **storage** *(dict) --*

        Where channel data is stored. You may choose one of "serviceManagedS3" or
        "customerManagedS3" storage. If not specified, the default is "serviceManagedS3". This
        cannot be changed after creation of the channel.

        - **serviceManagedS3** *(dict) --*

          Use this to store channel data in an S3 bucket managed by the AWS IoT Analytics service.
          The choice of service-managed or customer-managed S3 storage cannot be changed after
          creation of the channel.

        - **customerManagedS3** *(dict) --*

          Use this to store channel data in an S3 bucket that you manage. If customer managed
          storage is selected, the "retentionPeriod" parameter is ignored. The choice of
          service-managed or customer-managed S3 storage cannot be changed after creation of the
          channel.

          - **bucket** *(string) --*

            The name of the Amazon S3 bucket in which channel data is stored.

          - **keyPrefix** *(string) --*

            [Optional] The prefix used to create the keys of the channel data objects. Each object
            in an Amazon S3 bucket has a key that is its unique identifier within the bucket (each
            object in a bucket has exactly one key). The prefix must end with a '/'.

          - **roleArn** *(string) --*

            The ARN of the role which grants AWS IoT Analytics permission to interact with your
            Amazon S3 resources.

      - **arn** *(string) --*

        The ARN of the channel.

      - **status** *(string) --*

        The status of the channel.

      - **retentionPeriod** *(dict) --*

        How long, in days, message data is kept for the channel.

        - **unlimited** *(boolean) --*

          If true, message data is kept indefinitely.

        - **numberOfDays** *(integer) --*

          The number of days that message data is kept. The "unlimited" parameter must be false.

      - **creationTime** *(datetime) --*

        When the channel was created.

      - **lastUpdateTime** *(datetime) --*

        When the channel was last updated.

    - **statistics** *(dict) --*

      Statistics about the channel. Included if the 'includeStatistics' parameter is set to true in
      the request.

      - **size** *(dict) --*

        The estimated size of the channel.

        - **estimatedSizeInBytes** *(float) --*

          The estimated size of the resource in bytes.

        - **estimatedOn** *(datetime) --*

          The time when the estimate of the size of the resource was made.
    """


_ClientDescribeDatastoreResponsedatastoreretentionPeriodTypeDef = TypedDict(
    "_ClientDescribeDatastoreResponsedatastoreretentionPeriodTypeDef",
    {"unlimited": bool, "numberOfDays": int},
    total=False,
)


class ClientDescribeDatastoreResponsedatastoreretentionPeriodTypeDef(
    _ClientDescribeDatastoreResponsedatastoreretentionPeriodTypeDef
):
    """
    Type definition for `ClientDescribeDatastoreResponsedatastore` `retentionPeriod`

    How long, in days, message data is kept for the data store. When "customerManagedS3"
    storage is selected, this parameter is ignored.

    - **unlimited** *(boolean) --*

      If true, message data is kept indefinitely.

    - **numberOfDays** *(integer) --*

      The number of days that message data is kept. The "unlimited" parameter must be false.
    """


_ClientDescribeDatastoreResponsedatastorestoragecustomerManagedS3TypeDef = TypedDict(
    "_ClientDescribeDatastoreResponsedatastorestoragecustomerManagedS3TypeDef",
    {"bucket": str, "keyPrefix": str, "roleArn": str},
    total=False,
)


class ClientDescribeDatastoreResponsedatastorestoragecustomerManagedS3TypeDef(
    _ClientDescribeDatastoreResponsedatastorestoragecustomerManagedS3TypeDef
):
    """
    Type definition for `ClientDescribeDatastoreResponsedatastorestorage` `customerManagedS3`

    Use this to store data store data in an S3 bucket that you manage. When customer managed
    storage is selected, the "retentionPeriod" parameter is ignored. The choice of
    service-managed or customer-managed S3 storage cannot be changed after creation of the
    data store.

    - **bucket** *(string) --*

      The name of the Amazon S3 bucket in which data store data is stored.

    - **keyPrefix** *(string) --*

      [Optional] The prefix used to create the keys of the data store data objects. Each
      object in an Amazon S3 bucket has a key that is its unique identifier within the bucket
      (each object in a bucket has exactly one key). The prefix must end with a '/'.

    - **roleArn** *(string) --*

      The ARN of the role which grants AWS IoT Analytics permission to interact with your
      Amazon S3 resources.
    """


_ClientDescribeDatastoreResponsedatastorestorageTypeDef = TypedDict(
    "_ClientDescribeDatastoreResponsedatastorestorageTypeDef",
    {
        "serviceManagedS3": Dict,
        "customerManagedS3": ClientDescribeDatastoreResponsedatastorestoragecustomerManagedS3TypeDef,
    },
    total=False,
)


class ClientDescribeDatastoreResponsedatastorestorageTypeDef(
    _ClientDescribeDatastoreResponsedatastorestorageTypeDef
):
    """
    Type definition for `ClientDescribeDatastoreResponsedatastore` `storage`

    Where data store data is stored. You may choose one of "serviceManagedS3" or
    "customerManagedS3" storage. If not specified, the default is "serviceManagedS3". This
    cannot be changed after the data store is created.

    - **serviceManagedS3** *(dict) --*

      Use this to store data store data in an S3 bucket managed by the AWS IoT Analytics
      service. The choice of service-managed or customer-managed S3 storage cannot be changed
      after creation of the data store.

    - **customerManagedS3** *(dict) --*

      Use this to store data store data in an S3 bucket that you manage. When customer managed
      storage is selected, the "retentionPeriod" parameter is ignored. The choice of
      service-managed or customer-managed S3 storage cannot be changed after creation of the
      data store.

      - **bucket** *(string) --*

        The name of the Amazon S3 bucket in which data store data is stored.

      - **keyPrefix** *(string) --*

        [Optional] The prefix used to create the keys of the data store data objects. Each
        object in an Amazon S3 bucket has a key that is its unique identifier within the bucket
        (each object in a bucket has exactly one key). The prefix must end with a '/'.

      - **roleArn** *(string) --*

        The ARN of the role which grants AWS IoT Analytics permission to interact with your
        Amazon S3 resources.
    """


_ClientDescribeDatastoreResponsedatastoreTypeDef = TypedDict(
    "_ClientDescribeDatastoreResponsedatastoreTypeDef",
    {
        "name": str,
        "storage": ClientDescribeDatastoreResponsedatastorestorageTypeDef,
        "arn": str,
        "status": str,
        "retentionPeriod": ClientDescribeDatastoreResponsedatastoreretentionPeriodTypeDef,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
    },
    total=False,
)


class ClientDescribeDatastoreResponsedatastoreTypeDef(
    _ClientDescribeDatastoreResponsedatastoreTypeDef
):
    """
    Type definition for `ClientDescribeDatastoreResponse` `datastore`

    Information about the data store.

    - **name** *(string) --*

      The name of the data store.

    - **storage** *(dict) --*

      Where data store data is stored. You may choose one of "serviceManagedS3" or
      "customerManagedS3" storage. If not specified, the default is "serviceManagedS3". This
      cannot be changed after the data store is created.

      - **serviceManagedS3** *(dict) --*

        Use this to store data store data in an S3 bucket managed by the AWS IoT Analytics
        service. The choice of service-managed or customer-managed S3 storage cannot be changed
        after creation of the data store.

      - **customerManagedS3** *(dict) --*

        Use this to store data store data in an S3 bucket that you manage. When customer managed
        storage is selected, the "retentionPeriod" parameter is ignored. The choice of
        service-managed or customer-managed S3 storage cannot be changed after creation of the
        data store.

        - **bucket** *(string) --*

          The name of the Amazon S3 bucket in which data store data is stored.

        - **keyPrefix** *(string) --*

          [Optional] The prefix used to create the keys of the data store data objects. Each
          object in an Amazon S3 bucket has a key that is its unique identifier within the bucket
          (each object in a bucket has exactly one key). The prefix must end with a '/'.

        - **roleArn** *(string) --*

          The ARN of the role which grants AWS IoT Analytics permission to interact with your
          Amazon S3 resources.

    - **arn** *(string) --*

      The ARN of the data store.

    - **status** *(string) --*

      The status of a data store:

        CREATING

      The data store is being created.

        ACTIVE

      The data store has been created and can be used.

        DELETING

      The data store is being deleted.

    - **retentionPeriod** *(dict) --*

      How long, in days, message data is kept for the data store. When "customerManagedS3"
      storage is selected, this parameter is ignored.

      - **unlimited** *(boolean) --*

        If true, message data is kept indefinitely.

      - **numberOfDays** *(integer) --*

        The number of days that message data is kept. The "unlimited" parameter must be false.

    - **creationTime** *(datetime) --*

      When the data store was created.

    - **lastUpdateTime** *(datetime) --*

      The last time the data store was updated.
    """


_ClientDescribeDatastoreResponsestatisticssizeTypeDef = TypedDict(
    "_ClientDescribeDatastoreResponsestatisticssizeTypeDef",
    {"estimatedSizeInBytes": float, "estimatedOn": datetime},
    total=False,
)


class ClientDescribeDatastoreResponsestatisticssizeTypeDef(
    _ClientDescribeDatastoreResponsestatisticssizeTypeDef
):
    """
    Type definition for `ClientDescribeDatastoreResponsestatistics` `size`

    The estimated size of the data store.

    - **estimatedSizeInBytes** *(float) --*

      The estimated size of the resource in bytes.

    - **estimatedOn** *(datetime) --*

      The time when the estimate of the size of the resource was made.
    """


_ClientDescribeDatastoreResponsestatisticsTypeDef = TypedDict(
    "_ClientDescribeDatastoreResponsestatisticsTypeDef",
    {"size": ClientDescribeDatastoreResponsestatisticssizeTypeDef},
    total=False,
)


class ClientDescribeDatastoreResponsestatisticsTypeDef(
    _ClientDescribeDatastoreResponsestatisticsTypeDef
):
    """
    Type definition for `ClientDescribeDatastoreResponse` `statistics`

    Additional statistical information about the data store. Included if the 'includeStatistics'
    parameter is set to true in the request.

    - **size** *(dict) --*

      The estimated size of the data store.

      - **estimatedSizeInBytes** *(float) --*

        The estimated size of the resource in bytes.

      - **estimatedOn** *(datetime) --*

        The time when the estimate of the size of the resource was made.
    """


_ClientDescribeDatastoreResponseTypeDef = TypedDict(
    "_ClientDescribeDatastoreResponseTypeDef",
    {
        "datastore": ClientDescribeDatastoreResponsedatastoreTypeDef,
        "statistics": ClientDescribeDatastoreResponsestatisticsTypeDef,
    },
    total=False,
)


class ClientDescribeDatastoreResponseTypeDef(_ClientDescribeDatastoreResponseTypeDef):
    """
    Type definition for `ClientDescribeDatastore` `Response`

    - **datastore** *(dict) --*

      Information about the data store.

      - **name** *(string) --*

        The name of the data store.

      - **storage** *(dict) --*

        Where data store data is stored. You may choose one of "serviceManagedS3" or
        "customerManagedS3" storage. If not specified, the default is "serviceManagedS3". This
        cannot be changed after the data store is created.

        - **serviceManagedS3** *(dict) --*

          Use this to store data store data in an S3 bucket managed by the AWS IoT Analytics
          service. The choice of service-managed or customer-managed S3 storage cannot be changed
          after creation of the data store.

        - **customerManagedS3** *(dict) --*

          Use this to store data store data in an S3 bucket that you manage. When customer managed
          storage is selected, the "retentionPeriod" parameter is ignored. The choice of
          service-managed or customer-managed S3 storage cannot be changed after creation of the
          data store.

          - **bucket** *(string) --*

            The name of the Amazon S3 bucket in which data store data is stored.

          - **keyPrefix** *(string) --*

            [Optional] The prefix used to create the keys of the data store data objects. Each
            object in an Amazon S3 bucket has a key that is its unique identifier within the bucket
            (each object in a bucket has exactly one key). The prefix must end with a '/'.

          - **roleArn** *(string) --*

            The ARN of the role which grants AWS IoT Analytics permission to interact with your
            Amazon S3 resources.

      - **arn** *(string) --*

        The ARN of the data store.

      - **status** *(string) --*

        The status of a data store:

          CREATING

        The data store is being created.

          ACTIVE

        The data store has been created and can be used.

          DELETING

        The data store is being deleted.

      - **retentionPeriod** *(dict) --*

        How long, in days, message data is kept for the data store. When "customerManagedS3"
        storage is selected, this parameter is ignored.

        - **unlimited** *(boolean) --*

          If true, message data is kept indefinitely.

        - **numberOfDays** *(integer) --*

          The number of days that message data is kept. The "unlimited" parameter must be false.

      - **creationTime** *(datetime) --*

        When the data store was created.

      - **lastUpdateTime** *(datetime) --*

        The last time the data store was updated.

    - **statistics** *(dict) --*

      Additional statistical information about the data store. Included if the 'includeStatistics'
      parameter is set to true in the request.

      - **size** *(dict) --*

        The estimated size of the data store.

        - **estimatedSizeInBytes** *(float) --*

          The estimated size of the resource in bytes.

        - **estimatedOn** *(datetime) --*

          The time when the estimate of the size of the resource was made.
    """


_ClientDescribeLoggingOptionsResponseloggingOptionsTypeDef = TypedDict(
    "_ClientDescribeLoggingOptionsResponseloggingOptionsTypeDef",
    {"roleArn": str, "level": str, "enabled": bool},
    total=False,
)


class ClientDescribeLoggingOptionsResponseloggingOptionsTypeDef(
    _ClientDescribeLoggingOptionsResponseloggingOptionsTypeDef
):
    """
    Type definition for `ClientDescribeLoggingOptionsResponse` `loggingOptions`

    The current settings of the AWS IoT Analytics logging options.

    - **roleArn** *(string) --*

      The ARN of the role that grants permission to AWS IoT Analytics to perform logging.

    - **level** *(string) --*

      The logging level. Currently, only "ERROR" is supported.

    - **enabled** *(boolean) --*

      If true, logging is enabled for AWS IoT Analytics.
    """


_ClientDescribeLoggingOptionsResponseTypeDef = TypedDict(
    "_ClientDescribeLoggingOptionsResponseTypeDef",
    {"loggingOptions": ClientDescribeLoggingOptionsResponseloggingOptionsTypeDef},
    total=False,
)


class ClientDescribeLoggingOptionsResponseTypeDef(
    _ClientDescribeLoggingOptionsResponseTypeDef
):
    """
    Type definition for `ClientDescribeLoggingOptions` `Response`

    - **loggingOptions** *(dict) --*

      The current settings of the AWS IoT Analytics logging options.

      - **roleArn** *(string) --*

        The ARN of the role that grants permission to AWS IoT Analytics to perform logging.

      - **level** *(string) --*

        The logging level. Currently, only "ERROR" is supported.

      - **enabled** *(boolean) --*

        If true, logging is enabled for AWS IoT Analytics.
    """


_ClientDescribePipelineResponsepipelineactivitiesaddAttributesTypeDef = TypedDict(
    "_ClientDescribePipelineResponsepipelineactivitiesaddAttributesTypeDef",
    {"name": str, "attributes": Dict[str, str], "next": str},
    total=False,
)


class ClientDescribePipelineResponsepipelineactivitiesaddAttributesTypeDef(
    _ClientDescribePipelineResponsepipelineactivitiesaddAttributesTypeDef
):
    """
    Type definition for `ClientDescribePipelineResponsepipelineactivities` `addAttributes`

    Adds other attributes based on existing attributes in the message.

    - **name** *(string) --*

      The name of the 'addAttributes' activity.

    - **attributes** *(dict) --*

      A list of 1-50 "AttributeNameMapping" objects that map an existing attribute to a new
      attribute.

      .. note::

        The existing attributes remain in the message, so if you want to remove the
        originals, use "RemoveAttributeActivity".

      - *(string) --*

        - *(string) --*

    - **next** *(string) --*

      The next activity in the pipeline.
    """


_ClientDescribePipelineResponsepipelineactivitieschannelTypeDef = TypedDict(
    "_ClientDescribePipelineResponsepipelineactivitieschannelTypeDef",
    {"name": str, "channelName": str, "next": str},
    total=False,
)


class ClientDescribePipelineResponsepipelineactivitieschannelTypeDef(
    _ClientDescribePipelineResponsepipelineactivitieschannelTypeDef
):
    """
    Type definition for `ClientDescribePipelineResponsepipelineactivities` `channel`

    Determines the source of the messages to be processed.

    - **name** *(string) --*

      The name of the 'channel' activity.

    - **channelName** *(string) --*

      The name of the channel from which the messages are processed.

    - **next** *(string) --*

      The next activity in the pipeline.
    """


_ClientDescribePipelineResponsepipelineactivitiesdatastoreTypeDef = TypedDict(
    "_ClientDescribePipelineResponsepipelineactivitiesdatastoreTypeDef",
    {"name": str, "datastoreName": str},
    total=False,
)


class ClientDescribePipelineResponsepipelineactivitiesdatastoreTypeDef(
    _ClientDescribePipelineResponsepipelineactivitiesdatastoreTypeDef
):
    """
    Type definition for `ClientDescribePipelineResponsepipelineactivities` `datastore`

    Specifies where to store the processed message data.

    - **name** *(string) --*

      The name of the 'datastore' activity.

    - **datastoreName** *(string) --*

      The name of the data store where processed messages are stored.
    """


_ClientDescribePipelineResponsepipelineactivitiesdeviceRegistryEnrichTypeDef = TypedDict(
    "_ClientDescribePipelineResponsepipelineactivitiesdeviceRegistryEnrichTypeDef",
    {"name": str, "attribute": str, "thingName": str, "roleArn": str, "next": str},
    total=False,
)


class ClientDescribePipelineResponsepipelineactivitiesdeviceRegistryEnrichTypeDef(
    _ClientDescribePipelineResponsepipelineactivitiesdeviceRegistryEnrichTypeDef
):
    """
    Type definition for `ClientDescribePipelineResponsepipelineactivities` `deviceRegistryEnrich`

    Adds data from the AWS IoT device registry to your message.

    - **name** *(string) --*

      The name of the 'deviceRegistryEnrich' activity.

    - **attribute** *(string) --*

      The name of the attribute that is added to the message.

    - **thingName** *(string) --*

      The name of the IoT device whose registry information is added to the message.

    - **roleArn** *(string) --*

      The ARN of the role that allows access to the device's registry information.

    - **next** *(string) --*

      The next activity in the pipeline.
    """


_ClientDescribePipelineResponsepipelineactivitiesdeviceShadowEnrichTypeDef = TypedDict(
    "_ClientDescribePipelineResponsepipelineactivitiesdeviceShadowEnrichTypeDef",
    {"name": str, "attribute": str, "thingName": str, "roleArn": str, "next": str},
    total=False,
)


class ClientDescribePipelineResponsepipelineactivitiesdeviceShadowEnrichTypeDef(
    _ClientDescribePipelineResponsepipelineactivitiesdeviceShadowEnrichTypeDef
):
    """
    Type definition for `ClientDescribePipelineResponsepipelineactivities` `deviceShadowEnrich`

    Adds information from the AWS IoT Device Shadows service to a message.

    - **name** *(string) --*

      The name of the 'deviceShadowEnrich' activity.

    - **attribute** *(string) --*

      The name of the attribute that is added to the message.

    - **thingName** *(string) --*

      The name of the IoT device whose shadow information is added to the message.

    - **roleArn** *(string) --*

      The ARN of the role that allows access to the device's shadow.

    - **next** *(string) --*

      The next activity in the pipeline.
    """


_ClientDescribePipelineResponsepipelineactivitiesfilterTypeDef = TypedDict(
    "_ClientDescribePipelineResponsepipelineactivitiesfilterTypeDef",
    {"name": str, "filter": str, "next": str},
    total=False,
)


class ClientDescribePipelineResponsepipelineactivitiesfilterTypeDef(
    _ClientDescribePipelineResponsepipelineactivitiesfilterTypeDef
):
    """
    Type definition for `ClientDescribePipelineResponsepipelineactivities` `filter`

    Filters a message based on its attributes.

    - **name** *(string) --*

      The name of the 'filter' activity.

    - **filter** *(string) --*

      An expression that looks like a SQL WHERE clause that must return a Boolean value.

    - **next** *(string) --*

      The next activity in the pipeline.
    """


_ClientDescribePipelineResponsepipelineactivitieslambdaTypeDef = TypedDict(
    "_ClientDescribePipelineResponsepipelineactivitieslambdaTypeDef",
    {"name": str, "lambdaName": str, "batchSize": int, "next": str},
    total=False,
)


class ClientDescribePipelineResponsepipelineactivitieslambdaTypeDef(
    _ClientDescribePipelineResponsepipelineactivitieslambdaTypeDef
):
    """
    Type definition for `ClientDescribePipelineResponsepipelineactivities` `lambda`

    Runs a Lambda function to modify the message.

    - **name** *(string) --*

      The name of the 'lambda' activity.

    - **lambdaName** *(string) --*

      The name of the Lambda function that is run on the message.

    - **batchSize** *(integer) --*

      The number of messages passed to the Lambda function for processing.

      The AWS Lambda function must be able to process all of these messages within five
      minutes, which is the maximum timeout duration for Lambda functions.

    - **next** *(string) --*

      The next activity in the pipeline.
    """


_ClientDescribePipelineResponsepipelineactivitiesmathTypeDef = TypedDict(
    "_ClientDescribePipelineResponsepipelineactivitiesmathTypeDef",
    {"name": str, "attribute": str, "math": str, "next": str},
    total=False,
)


class ClientDescribePipelineResponsepipelineactivitiesmathTypeDef(
    _ClientDescribePipelineResponsepipelineactivitiesmathTypeDef
):
    """
    Type definition for `ClientDescribePipelineResponsepipelineactivities` `math`

    Computes an arithmetic expression using the message's attributes and adds it to the
    message.

    - **name** *(string) --*

      The name of the 'math' activity.

    - **attribute** *(string) --*

      The name of the attribute that contains the result of the math operation.

    - **math** *(string) --*

      An expression that uses one or more existing attributes and must return an integer
      value.

    - **next** *(string) --*

      The next activity in the pipeline.
    """


_ClientDescribePipelineResponsepipelineactivitiesremoveAttributesTypeDef = TypedDict(
    "_ClientDescribePipelineResponsepipelineactivitiesremoveAttributesTypeDef",
    {"name": str, "attributes": List[str], "next": str},
    total=False,
)


class ClientDescribePipelineResponsepipelineactivitiesremoveAttributesTypeDef(
    _ClientDescribePipelineResponsepipelineactivitiesremoveAttributesTypeDef
):
    """
    Type definition for `ClientDescribePipelineResponsepipelineactivities` `removeAttributes`

    Removes attributes from a message.

    - **name** *(string) --*

      The name of the 'removeAttributes' activity.

    - **attributes** *(list) --*

      A list of 1-50 attributes to remove from the message.

      - *(string) --*

    - **next** *(string) --*

      The next activity in the pipeline.
    """


_ClientDescribePipelineResponsepipelineactivitiesselectAttributesTypeDef = TypedDict(
    "_ClientDescribePipelineResponsepipelineactivitiesselectAttributesTypeDef",
    {"name": str, "attributes": List[str], "next": str},
    total=False,
)


class ClientDescribePipelineResponsepipelineactivitiesselectAttributesTypeDef(
    _ClientDescribePipelineResponsepipelineactivitiesselectAttributesTypeDef
):
    """
    Type definition for `ClientDescribePipelineResponsepipelineactivities` `selectAttributes`

    Creates a new message using only the specified attributes from the original message.

    - **name** *(string) --*

      The name of the 'selectAttributes' activity.

    - **attributes** *(list) --*

      A list of the attributes to select from the message.

      - *(string) --*

    - **next** *(string) --*

      The next activity in the pipeline.
    """


_ClientDescribePipelineResponsepipelineactivitiesTypeDef = TypedDict(
    "_ClientDescribePipelineResponsepipelineactivitiesTypeDef",
    {
        "channel": ClientDescribePipelineResponsepipelineactivitieschannelTypeDef,
        "lambda": ClientDescribePipelineResponsepipelineactivitieslambdaTypeDef,
        "datastore": ClientDescribePipelineResponsepipelineactivitiesdatastoreTypeDef,
        "addAttributes": ClientDescribePipelineResponsepipelineactivitiesaddAttributesTypeDef,
        "removeAttributes": ClientDescribePipelineResponsepipelineactivitiesremoveAttributesTypeDef,
        "selectAttributes": ClientDescribePipelineResponsepipelineactivitiesselectAttributesTypeDef,
        "filter": ClientDescribePipelineResponsepipelineactivitiesfilterTypeDef,
        "math": ClientDescribePipelineResponsepipelineactivitiesmathTypeDef,
        "deviceRegistryEnrich": ClientDescribePipelineResponsepipelineactivitiesdeviceRegistryEnrichTypeDef,
        "deviceShadowEnrich": ClientDescribePipelineResponsepipelineactivitiesdeviceShadowEnrichTypeDef,
    },
    total=False,
)


class ClientDescribePipelineResponsepipelineactivitiesTypeDef(
    _ClientDescribePipelineResponsepipelineactivitiesTypeDef
):
    """
    Type definition for `ClientDescribePipelineResponsepipeline` `activities`

    An activity that performs a transformation on a message.

    - **channel** *(dict) --*

      Determines the source of the messages to be processed.

      - **name** *(string) --*

        The name of the 'channel' activity.

      - **channelName** *(string) --*

        The name of the channel from which the messages are processed.

      - **next** *(string) --*

        The next activity in the pipeline.

    - **lambda** *(dict) --*

      Runs a Lambda function to modify the message.

      - **name** *(string) --*

        The name of the 'lambda' activity.

      - **lambdaName** *(string) --*

        The name of the Lambda function that is run on the message.

      - **batchSize** *(integer) --*

        The number of messages passed to the Lambda function for processing.

        The AWS Lambda function must be able to process all of these messages within five
        minutes, which is the maximum timeout duration for Lambda functions.

      - **next** *(string) --*

        The next activity in the pipeline.

    - **datastore** *(dict) --*

      Specifies where to store the processed message data.

      - **name** *(string) --*

        The name of the 'datastore' activity.

      - **datastoreName** *(string) --*

        The name of the data store where processed messages are stored.

    - **addAttributes** *(dict) --*

      Adds other attributes based on existing attributes in the message.

      - **name** *(string) --*

        The name of the 'addAttributes' activity.

      - **attributes** *(dict) --*

        A list of 1-50 "AttributeNameMapping" objects that map an existing attribute to a new
        attribute.

        .. note::

          The existing attributes remain in the message, so if you want to remove the
          originals, use "RemoveAttributeActivity".

        - *(string) --*

          - *(string) --*

      - **next** *(string) --*

        The next activity in the pipeline.

    - **removeAttributes** *(dict) --*

      Removes attributes from a message.

      - **name** *(string) --*

        The name of the 'removeAttributes' activity.

      - **attributes** *(list) --*

        A list of 1-50 attributes to remove from the message.

        - *(string) --*

      - **next** *(string) --*

        The next activity in the pipeline.

    - **selectAttributes** *(dict) --*

      Creates a new message using only the specified attributes from the original message.

      - **name** *(string) --*

        The name of the 'selectAttributes' activity.

      - **attributes** *(list) --*

        A list of the attributes to select from the message.

        - *(string) --*

      - **next** *(string) --*

        The next activity in the pipeline.

    - **filter** *(dict) --*

      Filters a message based on its attributes.

      - **name** *(string) --*

        The name of the 'filter' activity.

      - **filter** *(string) --*

        An expression that looks like a SQL WHERE clause that must return a Boolean value.

      - **next** *(string) --*

        The next activity in the pipeline.

    - **math** *(dict) --*

      Computes an arithmetic expression using the message's attributes and adds it to the
      message.

      - **name** *(string) --*

        The name of the 'math' activity.

      - **attribute** *(string) --*

        The name of the attribute that contains the result of the math operation.

      - **math** *(string) --*

        An expression that uses one or more existing attributes and must return an integer
        value.

      - **next** *(string) --*

        The next activity in the pipeline.

    - **deviceRegistryEnrich** *(dict) --*

      Adds data from the AWS IoT device registry to your message.

      - **name** *(string) --*

        The name of the 'deviceRegistryEnrich' activity.

      - **attribute** *(string) --*

        The name of the attribute that is added to the message.

      - **thingName** *(string) --*

        The name of the IoT device whose registry information is added to the message.

      - **roleArn** *(string) --*

        The ARN of the role that allows access to the device's registry information.

      - **next** *(string) --*

        The next activity in the pipeline.

    - **deviceShadowEnrich** *(dict) --*

      Adds information from the AWS IoT Device Shadows service to a message.

      - **name** *(string) --*

        The name of the 'deviceShadowEnrich' activity.

      - **attribute** *(string) --*

        The name of the attribute that is added to the message.

      - **thingName** *(string) --*

        The name of the IoT device whose shadow information is added to the message.

      - **roleArn** *(string) --*

        The ARN of the role that allows access to the device's shadow.

      - **next** *(string) --*

        The next activity in the pipeline.
    """


_ClientDescribePipelineResponsepipelinereprocessingSummariesTypeDef = TypedDict(
    "_ClientDescribePipelineResponsepipelinereprocessingSummariesTypeDef",
    {"id": str, "status": str, "creationTime": datetime},
    total=False,
)


class ClientDescribePipelineResponsepipelinereprocessingSummariesTypeDef(
    _ClientDescribePipelineResponsepipelinereprocessingSummariesTypeDef
):
    """
    Type definition for `ClientDescribePipelineResponsepipeline` `reprocessingSummaries`

    Information about pipeline reprocessing.

    - **id** *(string) --*

      The 'reprocessingId' returned by "StartPipelineReprocessing".

    - **status** *(string) --*

      The status of the pipeline reprocessing.

    - **creationTime** *(datetime) --*

      The time the pipeline reprocessing was created.
    """


_ClientDescribePipelineResponsepipelineTypeDef = TypedDict(
    "_ClientDescribePipelineResponsepipelineTypeDef",
    {
        "name": str,
        "arn": str,
        "activities": List[ClientDescribePipelineResponsepipelineactivitiesTypeDef],
        "reprocessingSummaries": List[
            ClientDescribePipelineResponsepipelinereprocessingSummariesTypeDef
        ],
        "creationTime": datetime,
        "lastUpdateTime": datetime,
    },
    total=False,
)


class ClientDescribePipelineResponsepipelineTypeDef(
    _ClientDescribePipelineResponsepipelineTypeDef
):
    """
    Type definition for `ClientDescribePipelineResponse` `pipeline`

    A "Pipeline" object that contains information about the pipeline.

    - **name** *(string) --*

      The name of the pipeline.

    - **arn** *(string) --*

      The ARN of the pipeline.

    - **activities** *(list) --*

      The activities that perform transformations on the messages.

      - *(dict) --*

        An activity that performs a transformation on a message.

        - **channel** *(dict) --*

          Determines the source of the messages to be processed.

          - **name** *(string) --*

            The name of the 'channel' activity.

          - **channelName** *(string) --*

            The name of the channel from which the messages are processed.

          - **next** *(string) --*

            The next activity in the pipeline.

        - **lambda** *(dict) --*

          Runs a Lambda function to modify the message.

          - **name** *(string) --*

            The name of the 'lambda' activity.

          - **lambdaName** *(string) --*

            The name of the Lambda function that is run on the message.

          - **batchSize** *(integer) --*

            The number of messages passed to the Lambda function for processing.

            The AWS Lambda function must be able to process all of these messages within five
            minutes, which is the maximum timeout duration for Lambda functions.

          - **next** *(string) --*

            The next activity in the pipeline.

        - **datastore** *(dict) --*

          Specifies where to store the processed message data.

          - **name** *(string) --*

            The name of the 'datastore' activity.

          - **datastoreName** *(string) --*

            The name of the data store where processed messages are stored.

        - **addAttributes** *(dict) --*

          Adds other attributes based on existing attributes in the message.

          - **name** *(string) --*

            The name of the 'addAttributes' activity.

          - **attributes** *(dict) --*

            A list of 1-50 "AttributeNameMapping" objects that map an existing attribute to a new
            attribute.

            .. note::

              The existing attributes remain in the message, so if you want to remove the
              originals, use "RemoveAttributeActivity".

            - *(string) --*

              - *(string) --*

          - **next** *(string) --*

            The next activity in the pipeline.

        - **removeAttributes** *(dict) --*

          Removes attributes from a message.

          - **name** *(string) --*

            The name of the 'removeAttributes' activity.

          - **attributes** *(list) --*

            A list of 1-50 attributes to remove from the message.

            - *(string) --*

          - **next** *(string) --*

            The next activity in the pipeline.

        - **selectAttributes** *(dict) --*

          Creates a new message using only the specified attributes from the original message.

          - **name** *(string) --*

            The name of the 'selectAttributes' activity.

          - **attributes** *(list) --*

            A list of the attributes to select from the message.

            - *(string) --*

          - **next** *(string) --*

            The next activity in the pipeline.

        - **filter** *(dict) --*

          Filters a message based on its attributes.

          - **name** *(string) --*

            The name of the 'filter' activity.

          - **filter** *(string) --*

            An expression that looks like a SQL WHERE clause that must return a Boolean value.

          - **next** *(string) --*

            The next activity in the pipeline.

        - **math** *(dict) --*

          Computes an arithmetic expression using the message's attributes and adds it to the
          message.

          - **name** *(string) --*

            The name of the 'math' activity.

          - **attribute** *(string) --*

            The name of the attribute that contains the result of the math operation.

          - **math** *(string) --*

            An expression that uses one or more existing attributes and must return an integer
            value.

          - **next** *(string) --*

            The next activity in the pipeline.

        - **deviceRegistryEnrich** *(dict) --*

          Adds data from the AWS IoT device registry to your message.

          - **name** *(string) --*

            The name of the 'deviceRegistryEnrich' activity.

          - **attribute** *(string) --*

            The name of the attribute that is added to the message.

          - **thingName** *(string) --*

            The name of the IoT device whose registry information is added to the message.

          - **roleArn** *(string) --*

            The ARN of the role that allows access to the device's registry information.

          - **next** *(string) --*

            The next activity in the pipeline.

        - **deviceShadowEnrich** *(dict) --*

          Adds information from the AWS IoT Device Shadows service to a message.

          - **name** *(string) --*

            The name of the 'deviceShadowEnrich' activity.

          - **attribute** *(string) --*

            The name of the attribute that is added to the message.

          - **thingName** *(string) --*

            The name of the IoT device whose shadow information is added to the message.

          - **roleArn** *(string) --*

            The ARN of the role that allows access to the device's shadow.

          - **next** *(string) --*

            The next activity in the pipeline.

    - **reprocessingSummaries** *(list) --*

      A summary of information about the pipeline reprocessing.

      - *(dict) --*

        Information about pipeline reprocessing.

        - **id** *(string) --*

          The 'reprocessingId' returned by "StartPipelineReprocessing".

        - **status** *(string) --*

          The status of the pipeline reprocessing.

        - **creationTime** *(datetime) --*

          The time the pipeline reprocessing was created.

    - **creationTime** *(datetime) --*

      When the pipeline was created.

    - **lastUpdateTime** *(datetime) --*

      The last time the pipeline was updated.
    """


_ClientDescribePipelineResponseTypeDef = TypedDict(
    "_ClientDescribePipelineResponseTypeDef",
    {"pipeline": ClientDescribePipelineResponsepipelineTypeDef},
    total=False,
)


class ClientDescribePipelineResponseTypeDef(_ClientDescribePipelineResponseTypeDef):
    """
    Type definition for `ClientDescribePipeline` `Response`

    - **pipeline** *(dict) --*

      A "Pipeline" object that contains information about the pipeline.

      - **name** *(string) --*

        The name of the pipeline.

      - **arn** *(string) --*

        The ARN of the pipeline.

      - **activities** *(list) --*

        The activities that perform transformations on the messages.

        - *(dict) --*

          An activity that performs a transformation on a message.

          - **channel** *(dict) --*

            Determines the source of the messages to be processed.

            - **name** *(string) --*

              The name of the 'channel' activity.

            - **channelName** *(string) --*

              The name of the channel from which the messages are processed.

            - **next** *(string) --*

              The next activity in the pipeline.

          - **lambda** *(dict) --*

            Runs a Lambda function to modify the message.

            - **name** *(string) --*

              The name of the 'lambda' activity.

            - **lambdaName** *(string) --*

              The name of the Lambda function that is run on the message.

            - **batchSize** *(integer) --*

              The number of messages passed to the Lambda function for processing.

              The AWS Lambda function must be able to process all of these messages within five
              minutes, which is the maximum timeout duration for Lambda functions.

            - **next** *(string) --*

              The next activity in the pipeline.

          - **datastore** *(dict) --*

            Specifies where to store the processed message data.

            - **name** *(string) --*

              The name of the 'datastore' activity.

            - **datastoreName** *(string) --*

              The name of the data store where processed messages are stored.

          - **addAttributes** *(dict) --*

            Adds other attributes based on existing attributes in the message.

            - **name** *(string) --*

              The name of the 'addAttributes' activity.

            - **attributes** *(dict) --*

              A list of 1-50 "AttributeNameMapping" objects that map an existing attribute to a new
              attribute.

              .. note::

                The existing attributes remain in the message, so if you want to remove the
                originals, use "RemoveAttributeActivity".

              - *(string) --*

                - *(string) --*

            - **next** *(string) --*

              The next activity in the pipeline.

          - **removeAttributes** *(dict) --*

            Removes attributes from a message.

            - **name** *(string) --*

              The name of the 'removeAttributes' activity.

            - **attributes** *(list) --*

              A list of 1-50 attributes to remove from the message.

              - *(string) --*

            - **next** *(string) --*

              The next activity in the pipeline.

          - **selectAttributes** *(dict) --*

            Creates a new message using only the specified attributes from the original message.

            - **name** *(string) --*

              The name of the 'selectAttributes' activity.

            - **attributes** *(list) --*

              A list of the attributes to select from the message.

              - *(string) --*

            - **next** *(string) --*

              The next activity in the pipeline.

          - **filter** *(dict) --*

            Filters a message based on its attributes.

            - **name** *(string) --*

              The name of the 'filter' activity.

            - **filter** *(string) --*

              An expression that looks like a SQL WHERE clause that must return a Boolean value.

            - **next** *(string) --*

              The next activity in the pipeline.

          - **math** *(dict) --*

            Computes an arithmetic expression using the message's attributes and adds it to the
            message.

            - **name** *(string) --*

              The name of the 'math' activity.

            - **attribute** *(string) --*

              The name of the attribute that contains the result of the math operation.

            - **math** *(string) --*

              An expression that uses one or more existing attributes and must return an integer
              value.

            - **next** *(string) --*

              The next activity in the pipeline.

          - **deviceRegistryEnrich** *(dict) --*

            Adds data from the AWS IoT device registry to your message.

            - **name** *(string) --*

              The name of the 'deviceRegistryEnrich' activity.

            - **attribute** *(string) --*

              The name of the attribute that is added to the message.

            - **thingName** *(string) --*

              The name of the IoT device whose registry information is added to the message.

            - **roleArn** *(string) --*

              The ARN of the role that allows access to the device's registry information.

            - **next** *(string) --*

              The next activity in the pipeline.

          - **deviceShadowEnrich** *(dict) --*

            Adds information from the AWS IoT Device Shadows service to a message.

            - **name** *(string) --*

              The name of the 'deviceShadowEnrich' activity.

            - **attribute** *(string) --*

              The name of the attribute that is added to the message.

            - **thingName** *(string) --*

              The name of the IoT device whose shadow information is added to the message.

            - **roleArn** *(string) --*

              The ARN of the role that allows access to the device's shadow.

            - **next** *(string) --*

              The next activity in the pipeline.

      - **reprocessingSummaries** *(list) --*

        A summary of information about the pipeline reprocessing.

        - *(dict) --*

          Information about pipeline reprocessing.

          - **id** *(string) --*

            The 'reprocessingId' returned by "StartPipelineReprocessing".

          - **status** *(string) --*

            The status of the pipeline reprocessing.

          - **creationTime** *(datetime) --*

            The time the pipeline reprocessing was created.

      - **creationTime** *(datetime) --*

        When the pipeline was created.

      - **lastUpdateTime** *(datetime) --*

        The last time the pipeline was updated.
    """


_ClientGetDatasetContentResponseentriesTypeDef = TypedDict(
    "_ClientGetDatasetContentResponseentriesTypeDef",
    {"entryName": str, "dataURI": str},
    total=False,
)


class ClientGetDatasetContentResponseentriesTypeDef(
    _ClientGetDatasetContentResponseentriesTypeDef
):
    """
    Type definition for `ClientGetDatasetContentResponse` `entries`

    The reference to a data set entry.

    - **entryName** *(string) --*

      The name of the data set item.

    - **dataURI** *(string) --*

      The pre-signed URI of the data set item.
    """


_ClientGetDatasetContentResponsestatusTypeDef = TypedDict(
    "_ClientGetDatasetContentResponsestatusTypeDef",
    {"state": str, "reason": str},
    total=False,
)


class ClientGetDatasetContentResponsestatusTypeDef(
    _ClientGetDatasetContentResponsestatusTypeDef
):
    """
    Type definition for `ClientGetDatasetContentResponse` `status`

    The status of the data set content.

    - **state** *(string) --*

      The state of the data set contents. Can be one of "READY", "CREATING", "SUCCEEDED" or
      "FAILED".

    - **reason** *(string) --*

      The reason the data set contents are in this state.
    """


_ClientGetDatasetContentResponseTypeDef = TypedDict(
    "_ClientGetDatasetContentResponseTypeDef",
    {
        "entries": List[ClientGetDatasetContentResponseentriesTypeDef],
        "timestamp": datetime,
        "status": ClientGetDatasetContentResponsestatusTypeDef,
    },
    total=False,
)


class ClientGetDatasetContentResponseTypeDef(_ClientGetDatasetContentResponseTypeDef):
    """
    Type definition for `ClientGetDatasetContent` `Response`

    - **entries** *(list) --*

      A list of "DatasetEntry" objects.

      - *(dict) --*

        The reference to a data set entry.

        - **entryName** *(string) --*

          The name of the data set item.

        - **dataURI** *(string) --*

          The pre-signed URI of the data set item.

    - **timestamp** *(datetime) --*

      The time when the request was made.

    - **status** *(dict) --*

      The status of the data set content.

      - **state** *(string) --*

        The state of the data set contents. Can be one of "READY", "CREATING", "SUCCEEDED" or
        "FAILED".

      - **reason** *(string) --*

        The reason the data set contents are in this state.
    """


_ClientListChannelsResponsechannelSummarieschannelStoragecustomerManagedS3TypeDef = TypedDict(
    "_ClientListChannelsResponsechannelSummarieschannelStoragecustomerManagedS3TypeDef",
    {"bucket": str, "keyPrefix": str, "roleArn": str},
    total=False,
)


class ClientListChannelsResponsechannelSummarieschannelStoragecustomerManagedS3TypeDef(
    _ClientListChannelsResponsechannelSummarieschannelStoragecustomerManagedS3TypeDef
):
    """
    Type definition for `ClientListChannelsResponsechannelSummarieschannelStorage` `customerManagedS3`

    Used to store channel data in an S3 bucket that you manage.

    - **bucket** *(string) --*

      The name of the Amazon S3 bucket in which channel data is stored.

    - **keyPrefix** *(string) --*

      [Optional] The prefix used to create the keys of the channel data objects. Each
      object in an Amazon S3 bucket has a key that is its unique identifier within the
      bucket (each object in a bucket has exactly one key). The prefix must end with a '/'.

    - **roleArn** *(string) --*

      The ARN of the role which grants AWS IoT Analytics permission to interact with your
      Amazon S3 resources.
    """


_ClientListChannelsResponsechannelSummarieschannelStorageTypeDef = TypedDict(
    "_ClientListChannelsResponsechannelSummarieschannelStorageTypeDef",
    {
        "serviceManagedS3": Dict,
        "customerManagedS3": ClientListChannelsResponsechannelSummarieschannelStoragecustomerManagedS3TypeDef,
    },
    total=False,
)


class ClientListChannelsResponsechannelSummarieschannelStorageTypeDef(
    _ClientListChannelsResponsechannelSummarieschannelStorageTypeDef
):
    """
    Type definition for `ClientListChannelsResponsechannelSummaries` `channelStorage`

    Where channel data is stored.

    - **serviceManagedS3** *(dict) --*

      Used to store channel data in an S3 bucket managed by the AWS IoT Analytics service.

    - **customerManagedS3** *(dict) --*

      Used to store channel data in an S3 bucket that you manage.

      - **bucket** *(string) --*

        The name of the Amazon S3 bucket in which channel data is stored.

      - **keyPrefix** *(string) --*

        [Optional] The prefix used to create the keys of the channel data objects. Each
        object in an Amazon S3 bucket has a key that is its unique identifier within the
        bucket (each object in a bucket has exactly one key). The prefix must end with a '/'.

      - **roleArn** *(string) --*

        The ARN of the role which grants AWS IoT Analytics permission to interact with your
        Amazon S3 resources.
    """


_ClientListChannelsResponsechannelSummariesTypeDef = TypedDict(
    "_ClientListChannelsResponsechannelSummariesTypeDef",
    {
        "channelName": str,
        "channelStorage": ClientListChannelsResponsechannelSummarieschannelStorageTypeDef,
        "status": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
    },
    total=False,
)


class ClientListChannelsResponsechannelSummariesTypeDef(
    _ClientListChannelsResponsechannelSummariesTypeDef
):
    """
    Type definition for `ClientListChannelsResponse` `channelSummaries`

    A summary of information about a channel.

    - **channelName** *(string) --*

      The name of the channel.

    - **channelStorage** *(dict) --*

      Where channel data is stored.

      - **serviceManagedS3** *(dict) --*

        Used to store channel data in an S3 bucket managed by the AWS IoT Analytics service.

      - **customerManagedS3** *(dict) --*

        Used to store channel data in an S3 bucket that you manage.

        - **bucket** *(string) --*

          The name of the Amazon S3 bucket in which channel data is stored.

        - **keyPrefix** *(string) --*

          [Optional] The prefix used to create the keys of the channel data objects. Each
          object in an Amazon S3 bucket has a key that is its unique identifier within the
          bucket (each object in a bucket has exactly one key). The prefix must end with a '/'.

        - **roleArn** *(string) --*

          The ARN of the role which grants AWS IoT Analytics permission to interact with your
          Amazon S3 resources.

    - **status** *(string) --*

      The status of the channel.

    - **creationTime** *(datetime) --*

      When the channel was created.

    - **lastUpdateTime** *(datetime) --*

      The last time the channel was updated.
    """


_ClientListChannelsResponseTypeDef = TypedDict(
    "_ClientListChannelsResponseTypeDef",
    {
        "channelSummaries": List[ClientListChannelsResponsechannelSummariesTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientListChannelsResponseTypeDef(_ClientListChannelsResponseTypeDef):
    """
    Type definition for `ClientListChannels` `Response`

    - **channelSummaries** *(list) --*

      A list of "ChannelSummary" objects.

      - *(dict) --*

        A summary of information about a channel.

        - **channelName** *(string) --*

          The name of the channel.

        - **channelStorage** *(dict) --*

          Where channel data is stored.

          - **serviceManagedS3** *(dict) --*

            Used to store channel data in an S3 bucket managed by the AWS IoT Analytics service.

          - **customerManagedS3** *(dict) --*

            Used to store channel data in an S3 bucket that you manage.

            - **bucket** *(string) --*

              The name of the Amazon S3 bucket in which channel data is stored.

            - **keyPrefix** *(string) --*

              [Optional] The prefix used to create the keys of the channel data objects. Each
              object in an Amazon S3 bucket has a key that is its unique identifier within the
              bucket (each object in a bucket has exactly one key). The prefix must end with a '/'.

            - **roleArn** *(string) --*

              The ARN of the role which grants AWS IoT Analytics permission to interact with your
              Amazon S3 resources.

        - **status** *(string) --*

          The status of the channel.

        - **creationTime** *(datetime) --*

          When the channel was created.

        - **lastUpdateTime** *(datetime) --*

          The last time the channel was updated.

    - **nextToken** *(string) --*

      The token to retrieve the next set of results, or ``null`` if there are no more results.
    """


_ClientListDatasetContentsResponsedatasetContentSummariesstatusTypeDef = TypedDict(
    "_ClientListDatasetContentsResponsedatasetContentSummariesstatusTypeDef",
    {"state": str, "reason": str},
    total=False,
)


class ClientListDatasetContentsResponsedatasetContentSummariesstatusTypeDef(
    _ClientListDatasetContentsResponsedatasetContentSummariesstatusTypeDef
):
    """
    Type definition for `ClientListDatasetContentsResponsedatasetContentSummaries` `status`

    The status of the data set contents.

    - **state** *(string) --*

      The state of the data set contents. Can be one of "READY", "CREATING", "SUCCEEDED" or
      "FAILED".

    - **reason** *(string) --*

      The reason the data set contents are in this state.
    """


_ClientListDatasetContentsResponsedatasetContentSummariesTypeDef = TypedDict(
    "_ClientListDatasetContentsResponsedatasetContentSummariesTypeDef",
    {
        "version": str,
        "status": ClientListDatasetContentsResponsedatasetContentSummariesstatusTypeDef,
        "creationTime": datetime,
        "scheduleTime": datetime,
        "completionTime": datetime,
    },
    total=False,
)


class ClientListDatasetContentsResponsedatasetContentSummariesTypeDef(
    _ClientListDatasetContentsResponsedatasetContentSummariesTypeDef
):
    """
    Type definition for `ClientListDatasetContentsResponse` `datasetContentSummaries`

    Summary information about data set contents.

    - **version** *(string) --*

      The version of the data set contents.

    - **status** *(dict) --*

      The status of the data set contents.

      - **state** *(string) --*

        The state of the data set contents. Can be one of "READY", "CREATING", "SUCCEEDED" or
        "FAILED".

      - **reason** *(string) --*

        The reason the data set contents are in this state.

    - **creationTime** *(datetime) --*

      The actual time the creation of the data set contents was started.

    - **scheduleTime** *(datetime) --*

      The time the creation of the data set contents was scheduled to start.

    - **completionTime** *(datetime) --*

      The time the dataset content status was updated to SUCCEEDED or FAILED.
    """


_ClientListDatasetContentsResponseTypeDef = TypedDict(
    "_ClientListDatasetContentsResponseTypeDef",
    {
        "datasetContentSummaries": List[
            ClientListDatasetContentsResponsedatasetContentSummariesTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientListDatasetContentsResponseTypeDef(
    _ClientListDatasetContentsResponseTypeDef
):
    """
    Type definition for `ClientListDatasetContents` `Response`

    - **datasetContentSummaries** *(list) --*

      Summary information about data set contents that have been created.

      - *(dict) --*

        Summary information about data set contents.

        - **version** *(string) --*

          The version of the data set contents.

        - **status** *(dict) --*

          The status of the data set contents.

          - **state** *(string) --*

            The state of the data set contents. Can be one of "READY", "CREATING", "SUCCEEDED" or
            "FAILED".

          - **reason** *(string) --*

            The reason the data set contents are in this state.

        - **creationTime** *(datetime) --*

          The actual time the creation of the data set contents was started.

        - **scheduleTime** *(datetime) --*

          The time the creation of the data set contents was scheduled to start.

        - **completionTime** *(datetime) --*

          The time the dataset content status was updated to SUCCEEDED or FAILED.

    - **nextToken** *(string) --*

      The token to retrieve the next set of results, or ``null`` if there are no more results.
    """


_ClientListDatasetsResponsedatasetSummariesactionsTypeDef = TypedDict(
    "_ClientListDatasetsResponsedatasetSummariesactionsTypeDef",
    {"actionName": str, "actionType": str},
    total=False,
)


class ClientListDatasetsResponsedatasetSummariesactionsTypeDef(
    _ClientListDatasetsResponsedatasetSummariesactionsTypeDef
):
    """
    Type definition for `ClientListDatasetsResponsedatasetSummaries` `actions`

    Information about the action which automatically creates the data set's contents.

    - **actionName** *(string) --*

      The name of the action which automatically creates the data set's contents.

    - **actionType** *(string) --*

      The type of action by which the data set's contents are automatically created.
    """


_ClientListDatasetsResponsedatasetSummariestriggersdatasetTypeDef = TypedDict(
    "_ClientListDatasetsResponsedatasetSummariestriggersdatasetTypeDef",
    {"name": str},
    total=False,
)


class ClientListDatasetsResponsedatasetSummariestriggersdatasetTypeDef(
    _ClientListDatasetsResponsedatasetSummariestriggersdatasetTypeDef
):
    """
    Type definition for `ClientListDatasetsResponsedatasetSummariestriggers` `dataset`

    The data set whose content creation triggers the creation of this data set's contents.

    - **name** *(string) --*

      The name of the data set whose content generation triggers the new data set content
      generation.
    """


_ClientListDatasetsResponsedatasetSummariestriggersscheduleTypeDef = TypedDict(
    "_ClientListDatasetsResponsedatasetSummariestriggersscheduleTypeDef",
    {"expression": str},
    total=False,
)


class ClientListDatasetsResponsedatasetSummariestriggersscheduleTypeDef(
    _ClientListDatasetsResponsedatasetSummariestriggersscheduleTypeDef
):
    """
    Type definition for `ClientListDatasetsResponsedatasetSummariestriggers` `schedule`

    The "Schedule" when the trigger is initiated.

    - **expression** *(string) --*

      The expression that defines when to trigger an update. For more information, see
      `Schedule Expressions for Rules
      <https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html>`__
      in the Amazon CloudWatch Events User Guide.
    """


_ClientListDatasetsResponsedatasetSummariestriggersTypeDef = TypedDict(
    "_ClientListDatasetsResponsedatasetSummariestriggersTypeDef",
    {
        "schedule": ClientListDatasetsResponsedatasetSummariestriggersscheduleTypeDef,
        "dataset": ClientListDatasetsResponsedatasetSummariestriggersdatasetTypeDef,
    },
    total=False,
)


class ClientListDatasetsResponsedatasetSummariestriggersTypeDef(
    _ClientListDatasetsResponsedatasetSummariestriggersTypeDef
):
    """
    Type definition for `ClientListDatasetsResponsedatasetSummaries` `triggers`

    The "DatasetTrigger" that specifies when the data set is automatically updated.

    - **schedule** *(dict) --*

      The "Schedule" when the trigger is initiated.

      - **expression** *(string) --*

        The expression that defines when to trigger an update. For more information, see
        `Schedule Expressions for Rules
        <https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html>`__
        in the Amazon CloudWatch Events User Guide.

    - **dataset** *(dict) --*

      The data set whose content creation triggers the creation of this data set's contents.

      - **name** *(string) --*

        The name of the data set whose content generation triggers the new data set content
        generation.
    """


_ClientListDatasetsResponsedatasetSummariesTypeDef = TypedDict(
    "_ClientListDatasetsResponsedatasetSummariesTypeDef",
    {
        "datasetName": str,
        "status": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "triggers": List[ClientListDatasetsResponsedatasetSummariestriggersTypeDef],
        "actions": List[ClientListDatasetsResponsedatasetSummariesactionsTypeDef],
    },
    total=False,
)


class ClientListDatasetsResponsedatasetSummariesTypeDef(
    _ClientListDatasetsResponsedatasetSummariesTypeDef
):
    """
    Type definition for `ClientListDatasetsResponse` `datasetSummaries`

    A summary of information about a data set.

    - **datasetName** *(string) --*

      The name of the data set.

    - **status** *(string) --*

      The status of the data set.

    - **creationTime** *(datetime) --*

      The time the data set was created.

    - **lastUpdateTime** *(datetime) --*

      The last time the data set was updated.

    - **triggers** *(list) --*

      A list of triggers. A trigger causes data set content to be populated at a specified time
      interval or when another data set is populated. The list of triggers can be empty or
      contain up to five DataSetTrigger objects

      - *(dict) --*

        The "DatasetTrigger" that specifies when the data set is automatically updated.

        - **schedule** *(dict) --*

          The "Schedule" when the trigger is initiated.

          - **expression** *(string) --*

            The expression that defines when to trigger an update. For more information, see
            `Schedule Expressions for Rules
            <https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html>`__
            in the Amazon CloudWatch Events User Guide.

        - **dataset** *(dict) --*

          The data set whose content creation triggers the creation of this data set's contents.

          - **name** *(string) --*

            The name of the data set whose content generation triggers the new data set content
            generation.

    - **actions** *(list) --*

      A list of "DataActionSummary" objects.

      - *(dict) --*

        Information about the action which automatically creates the data set's contents.

        - **actionName** *(string) --*

          The name of the action which automatically creates the data set's contents.

        - **actionType** *(string) --*

          The type of action by which the data set's contents are automatically created.
    """


_ClientListDatasetsResponseTypeDef = TypedDict(
    "_ClientListDatasetsResponseTypeDef",
    {
        "datasetSummaries": List[ClientListDatasetsResponsedatasetSummariesTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientListDatasetsResponseTypeDef(_ClientListDatasetsResponseTypeDef):
    """
    Type definition for `ClientListDatasets` `Response`

    - **datasetSummaries** *(list) --*

      A list of "DatasetSummary" objects.

      - *(dict) --*

        A summary of information about a data set.

        - **datasetName** *(string) --*

          The name of the data set.

        - **status** *(string) --*

          The status of the data set.

        - **creationTime** *(datetime) --*

          The time the data set was created.

        - **lastUpdateTime** *(datetime) --*

          The last time the data set was updated.

        - **triggers** *(list) --*

          A list of triggers. A trigger causes data set content to be populated at a specified time
          interval or when another data set is populated. The list of triggers can be empty or
          contain up to five DataSetTrigger objects

          - *(dict) --*

            The "DatasetTrigger" that specifies when the data set is automatically updated.

            - **schedule** *(dict) --*

              The "Schedule" when the trigger is initiated.

              - **expression** *(string) --*

                The expression that defines when to trigger an update. For more information, see
                `Schedule Expressions for Rules
                <https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html>`__
                in the Amazon CloudWatch Events User Guide.

            - **dataset** *(dict) --*

              The data set whose content creation triggers the creation of this data set's contents.

              - **name** *(string) --*

                The name of the data set whose content generation triggers the new data set content
                generation.

        - **actions** *(list) --*

          A list of "DataActionSummary" objects.

          - *(dict) --*

            Information about the action which automatically creates the data set's contents.

            - **actionName** *(string) --*

              The name of the action which automatically creates the data set's contents.

            - **actionType** *(string) --*

              The type of action by which the data set's contents are automatically created.

    - **nextToken** *(string) --*

      The token to retrieve the next set of results, or ``null`` if there are no more results.
    """


_ClientListDatastoresResponsedatastoreSummariesdatastoreStoragecustomerManagedS3TypeDef = TypedDict(
    "_ClientListDatastoresResponsedatastoreSummariesdatastoreStoragecustomerManagedS3TypeDef",
    {"bucket": str, "keyPrefix": str, "roleArn": str},
    total=False,
)


class ClientListDatastoresResponsedatastoreSummariesdatastoreStoragecustomerManagedS3TypeDef(
    _ClientListDatastoresResponsedatastoreSummariesdatastoreStoragecustomerManagedS3TypeDef
):
    """
    Type definition for `ClientListDatastoresResponsedatastoreSummariesdatastoreStorage` `customerManagedS3`

    Used to store data store data in an S3 bucket that you manage.

    - **bucket** *(string) --*

      The name of the Amazon S3 bucket in which data store data is stored.

    - **keyPrefix** *(string) --*

      [Optional] The prefix used to create the keys of the data store data objects. Each
      object in an Amazon S3 bucket has a key that is its unique identifier within the
      bucket (each object in a bucket has exactly one key). The prefix must end with a '/'.

    - **roleArn** *(string) --*

      The ARN of the role which grants AWS IoT Analytics permission to interact with your
      Amazon S3 resources.
    """


_ClientListDatastoresResponsedatastoreSummariesdatastoreStorageTypeDef = TypedDict(
    "_ClientListDatastoresResponsedatastoreSummariesdatastoreStorageTypeDef",
    {
        "serviceManagedS3": Dict,
        "customerManagedS3": ClientListDatastoresResponsedatastoreSummariesdatastoreStoragecustomerManagedS3TypeDef,
    },
    total=False,
)


class ClientListDatastoresResponsedatastoreSummariesdatastoreStorageTypeDef(
    _ClientListDatastoresResponsedatastoreSummariesdatastoreStorageTypeDef
):
    """
    Type definition for `ClientListDatastoresResponsedatastoreSummaries` `datastoreStorage`

    Where data store data is stored.

    - **serviceManagedS3** *(dict) --*

      Used to store data store data in an S3 bucket managed by the AWS IoT Analytics service.

    - **customerManagedS3** *(dict) --*

      Used to store data store data in an S3 bucket that you manage.

      - **bucket** *(string) --*

        The name of the Amazon S3 bucket in which data store data is stored.

      - **keyPrefix** *(string) --*

        [Optional] The prefix used to create the keys of the data store data objects. Each
        object in an Amazon S3 bucket has a key that is its unique identifier within the
        bucket (each object in a bucket has exactly one key). The prefix must end with a '/'.

      - **roleArn** *(string) --*

        The ARN of the role which grants AWS IoT Analytics permission to interact with your
        Amazon S3 resources.
    """


_ClientListDatastoresResponsedatastoreSummariesTypeDef = TypedDict(
    "_ClientListDatastoresResponsedatastoreSummariesTypeDef",
    {
        "datastoreName": str,
        "datastoreStorage": ClientListDatastoresResponsedatastoreSummariesdatastoreStorageTypeDef,
        "status": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
    },
    total=False,
)


class ClientListDatastoresResponsedatastoreSummariesTypeDef(
    _ClientListDatastoresResponsedatastoreSummariesTypeDef
):
    """
    Type definition for `ClientListDatastoresResponse` `datastoreSummaries`

    A summary of information about a data store.

    - **datastoreName** *(string) --*

      The name of the data store.

    - **datastoreStorage** *(dict) --*

      Where data store data is stored.

      - **serviceManagedS3** *(dict) --*

        Used to store data store data in an S3 bucket managed by the AWS IoT Analytics service.

      - **customerManagedS3** *(dict) --*

        Used to store data store data in an S3 bucket that you manage.

        - **bucket** *(string) --*

          The name of the Amazon S3 bucket in which data store data is stored.

        - **keyPrefix** *(string) --*

          [Optional] The prefix used to create the keys of the data store data objects. Each
          object in an Amazon S3 bucket has a key that is its unique identifier within the
          bucket (each object in a bucket has exactly one key). The prefix must end with a '/'.

        - **roleArn** *(string) --*

          The ARN of the role which grants AWS IoT Analytics permission to interact with your
          Amazon S3 resources.

    - **status** *(string) --*

      The status of the data store.

    - **creationTime** *(datetime) --*

      When the data store was created.

    - **lastUpdateTime** *(datetime) --*

      The last time the data store was updated.
    """


_ClientListDatastoresResponseTypeDef = TypedDict(
    "_ClientListDatastoresResponseTypeDef",
    {
        "datastoreSummaries": List[
            ClientListDatastoresResponsedatastoreSummariesTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientListDatastoresResponseTypeDef(_ClientListDatastoresResponseTypeDef):
    """
    Type definition for `ClientListDatastores` `Response`

    - **datastoreSummaries** *(list) --*

      A list of "DatastoreSummary" objects.

      - *(dict) --*

        A summary of information about a data store.

        - **datastoreName** *(string) --*

          The name of the data store.

        - **datastoreStorage** *(dict) --*

          Where data store data is stored.

          - **serviceManagedS3** *(dict) --*

            Used to store data store data in an S3 bucket managed by the AWS IoT Analytics service.

          - **customerManagedS3** *(dict) --*

            Used to store data store data in an S3 bucket that you manage.

            - **bucket** *(string) --*

              The name of the Amazon S3 bucket in which data store data is stored.

            - **keyPrefix** *(string) --*

              [Optional] The prefix used to create the keys of the data store data objects. Each
              object in an Amazon S3 bucket has a key that is its unique identifier within the
              bucket (each object in a bucket has exactly one key). The prefix must end with a '/'.

            - **roleArn** *(string) --*

              The ARN of the role which grants AWS IoT Analytics permission to interact with your
              Amazon S3 resources.

        - **status** *(string) --*

          The status of the data store.

        - **creationTime** *(datetime) --*

          When the data store was created.

        - **lastUpdateTime** *(datetime) --*

          The last time the data store was updated.

    - **nextToken** *(string) --*

      The token to retrieve the next set of results, or ``null`` if there are no more results.
    """


_ClientListPipelinesResponsepipelineSummariesreprocessingSummariesTypeDef = TypedDict(
    "_ClientListPipelinesResponsepipelineSummariesreprocessingSummariesTypeDef",
    {"id": str, "status": str, "creationTime": datetime},
    total=False,
)


class ClientListPipelinesResponsepipelineSummariesreprocessingSummariesTypeDef(
    _ClientListPipelinesResponsepipelineSummariesreprocessingSummariesTypeDef
):
    """
    Type definition for `ClientListPipelinesResponsepipelineSummaries` `reprocessingSummaries`

    Information about pipeline reprocessing.

    - **id** *(string) --*

      The 'reprocessingId' returned by "StartPipelineReprocessing".

    - **status** *(string) --*

      The status of the pipeline reprocessing.

    - **creationTime** *(datetime) --*

      The time the pipeline reprocessing was created.
    """


_ClientListPipelinesResponsepipelineSummariesTypeDef = TypedDict(
    "_ClientListPipelinesResponsepipelineSummariesTypeDef",
    {
        "pipelineName": str,
        "reprocessingSummaries": List[
            ClientListPipelinesResponsepipelineSummariesreprocessingSummariesTypeDef
        ],
        "creationTime": datetime,
        "lastUpdateTime": datetime,
    },
    total=False,
)


class ClientListPipelinesResponsepipelineSummariesTypeDef(
    _ClientListPipelinesResponsepipelineSummariesTypeDef
):
    """
    Type definition for `ClientListPipelinesResponse` `pipelineSummaries`

    A summary of information about a pipeline.

    - **pipelineName** *(string) --*

      The name of the pipeline.

    - **reprocessingSummaries** *(list) --*

      A summary of information about the pipeline reprocessing.

      - *(dict) --*

        Information about pipeline reprocessing.

        - **id** *(string) --*

          The 'reprocessingId' returned by "StartPipelineReprocessing".

        - **status** *(string) --*

          The status of the pipeline reprocessing.

        - **creationTime** *(datetime) --*

          The time the pipeline reprocessing was created.

    - **creationTime** *(datetime) --*

      When the pipeline was created.

    - **lastUpdateTime** *(datetime) --*

      When the pipeline was last updated.
    """


_ClientListPipelinesResponseTypeDef = TypedDict(
    "_ClientListPipelinesResponseTypeDef",
    {
        "pipelineSummaries": List[ClientListPipelinesResponsepipelineSummariesTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientListPipelinesResponseTypeDef(_ClientListPipelinesResponseTypeDef):
    """
    Type definition for `ClientListPipelines` `Response`

    - **pipelineSummaries** *(list) --*

      A list of "PipelineSummary" objects.

      - *(dict) --*

        A summary of information about a pipeline.

        - **pipelineName** *(string) --*

          The name of the pipeline.

        - **reprocessingSummaries** *(list) --*

          A summary of information about the pipeline reprocessing.

          - *(dict) --*

            Information about pipeline reprocessing.

            - **id** *(string) --*

              The 'reprocessingId' returned by "StartPipelineReprocessing".

            - **status** *(string) --*

              The status of the pipeline reprocessing.

            - **creationTime** *(datetime) --*

              The time the pipeline reprocessing was created.

        - **creationTime** *(datetime) --*

          When the pipeline was created.

        - **lastUpdateTime** *(datetime) --*

          When the pipeline was last updated.

    - **nextToken** *(string) --*

      The token to retrieve the next set of results, or ``null`` if there are no more results.
    """


_ClientListTagsForResourceResponsetagsTypeDef = TypedDict(
    "_ClientListTagsForResourceResponsetagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientListTagsForResourceResponsetagsTypeDef(
    _ClientListTagsForResourceResponsetagsTypeDef
):
    """
    Type definition for `ClientListTagsForResourceResponse` `tags`

    A set of key/value pairs which are used to manage the resource.

    - **key** *(string) --*

      The tag's key.

    - **value** *(string) --*

      The tag's value.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef",
    {"tags": List[ClientListTagsForResourceResponsetagsTypeDef]},
    total=False,
)


class ClientListTagsForResourceResponseTypeDef(
    _ClientListTagsForResourceResponseTypeDef
):
    """
    Type definition for `ClientListTagsForResource` `Response`

    - **tags** *(list) --*

      The tags (metadata) which you have assigned to the resource.

      - *(dict) --*

        A set of key/value pairs which are used to manage the resource.

        - **key** *(string) --*

          The tag's key.

        - **value** *(string) --*

          The tag's value.
    """


_ClientPutLoggingOptionsloggingOptionsTypeDef = TypedDict(
    "_ClientPutLoggingOptionsloggingOptionsTypeDef",
    {"roleArn": str, "level": str, "enabled": bool},
)


class ClientPutLoggingOptionsloggingOptionsTypeDef(
    _ClientPutLoggingOptionsloggingOptionsTypeDef
):
    """
    Type definition for `ClientPutLoggingOptions` `loggingOptions`

    The new values of the AWS IoT Analytics logging options.

    - **roleArn** *(string) --* **[REQUIRED]**

      The ARN of the role that grants permission to AWS IoT Analytics to perform logging.

    - **level** *(string) --* **[REQUIRED]**

      The logging level. Currently, only "ERROR" is supported.

    - **enabled** *(boolean) --* **[REQUIRED]**

      If true, logging is enabled for AWS IoT Analytics.
    """


_ClientRunPipelineActivityResponseTypeDef = TypedDict(
    "_ClientRunPipelineActivityResponseTypeDef",
    {"payloads": List[bytes], "logResult": str},
    total=False,
)


class ClientRunPipelineActivityResponseTypeDef(
    _ClientRunPipelineActivityResponseTypeDef
):
    """
    Type definition for `ClientRunPipelineActivity` `Response`

    - **payloads** *(list) --*

      The enriched or transformed sample message payloads as base64-encoded strings. (The results
      of running the pipeline activity on each input sample message payload, encoded in base64.)

      - *(bytes) --*

    - **logResult** *(string) --*

      In case the pipeline activity fails, the log message that is generated.
    """


_RequiredClientRunPipelineActivitypipelineActivityaddAttributesTypeDef = TypedDict(
    "_RequiredClientRunPipelineActivitypipelineActivityaddAttributesTypeDef",
    {"name": str, "attributes": Dict[str, str]},
)
_OptionalClientRunPipelineActivitypipelineActivityaddAttributesTypeDef = TypedDict(
    "_OptionalClientRunPipelineActivitypipelineActivityaddAttributesTypeDef",
    {"next": str},
    total=False,
)


class ClientRunPipelineActivitypipelineActivityaddAttributesTypeDef(
    _RequiredClientRunPipelineActivitypipelineActivityaddAttributesTypeDef,
    _OptionalClientRunPipelineActivitypipelineActivityaddAttributesTypeDef,
):
    """
    Type definition for `ClientRunPipelineActivitypipelineActivity` `addAttributes`

    Adds other attributes based on existing attributes in the message.

    - **name** *(string) --* **[REQUIRED]**

      The name of the 'addAttributes' activity.

    - **attributes** *(dict) --* **[REQUIRED]**

      A list of 1-50 "AttributeNameMapping" objects that map an existing attribute to a new
      attribute.

      .. note::

        The existing attributes remain in the message, so if you want to remove the originals, use
        "RemoveAttributeActivity".

      - *(string) --*

        - *(string) --*

    - **next** *(string) --*

      The next activity in the pipeline.
    """


_RequiredClientRunPipelineActivitypipelineActivitychannelTypeDef = TypedDict(
    "_RequiredClientRunPipelineActivitypipelineActivitychannelTypeDef",
    {"name": str, "channelName": str},
)
_OptionalClientRunPipelineActivitypipelineActivitychannelTypeDef = TypedDict(
    "_OptionalClientRunPipelineActivitypipelineActivitychannelTypeDef",
    {"next": str},
    total=False,
)


class ClientRunPipelineActivitypipelineActivitychannelTypeDef(
    _RequiredClientRunPipelineActivitypipelineActivitychannelTypeDef,
    _OptionalClientRunPipelineActivitypipelineActivitychannelTypeDef,
):
    """
    Type definition for `ClientRunPipelineActivitypipelineActivity` `channel`

    Determines the source of the messages to be processed.

    - **name** *(string) --* **[REQUIRED]**

      The name of the 'channel' activity.

    - **channelName** *(string) --* **[REQUIRED]**

      The name of the channel from which the messages are processed.

    - **next** *(string) --*

      The next activity in the pipeline.
    """


_ClientRunPipelineActivitypipelineActivitydatastoreTypeDef = TypedDict(
    "_ClientRunPipelineActivitypipelineActivitydatastoreTypeDef",
    {"name": str, "datastoreName": str},
)


class ClientRunPipelineActivitypipelineActivitydatastoreTypeDef(
    _ClientRunPipelineActivitypipelineActivitydatastoreTypeDef
):
    """
    Type definition for `ClientRunPipelineActivitypipelineActivity` `datastore`

    Specifies where to store the processed message data.

    - **name** *(string) --* **[REQUIRED]**

      The name of the 'datastore' activity.

    - **datastoreName** *(string) --* **[REQUIRED]**

      The name of the data store where processed messages are stored.
    """


_RequiredClientRunPipelineActivitypipelineActivitydeviceRegistryEnrichTypeDef = TypedDict(
    "_RequiredClientRunPipelineActivitypipelineActivitydeviceRegistryEnrichTypeDef",
    {"name": str, "attribute": str, "thingName": str, "roleArn": str},
)
_OptionalClientRunPipelineActivitypipelineActivitydeviceRegistryEnrichTypeDef = TypedDict(
    "_OptionalClientRunPipelineActivitypipelineActivitydeviceRegistryEnrichTypeDef",
    {"next": str},
    total=False,
)


class ClientRunPipelineActivitypipelineActivitydeviceRegistryEnrichTypeDef(
    _RequiredClientRunPipelineActivitypipelineActivitydeviceRegistryEnrichTypeDef,
    _OptionalClientRunPipelineActivitypipelineActivitydeviceRegistryEnrichTypeDef,
):
    """
    Type definition for `ClientRunPipelineActivitypipelineActivity` `deviceRegistryEnrich`

    Adds data from the AWS IoT device registry to your message.

    - **name** *(string) --* **[REQUIRED]**

      The name of the 'deviceRegistryEnrich' activity.

    - **attribute** *(string) --* **[REQUIRED]**

      The name of the attribute that is added to the message.

    - **thingName** *(string) --* **[REQUIRED]**

      The name of the IoT device whose registry information is added to the message.

    - **roleArn** *(string) --* **[REQUIRED]**

      The ARN of the role that allows access to the device's registry information.

    - **next** *(string) --*

      The next activity in the pipeline.
    """


_RequiredClientRunPipelineActivitypipelineActivitydeviceShadowEnrichTypeDef = TypedDict(
    "_RequiredClientRunPipelineActivitypipelineActivitydeviceShadowEnrichTypeDef",
    {"name": str, "attribute": str, "thingName": str, "roleArn": str},
)
_OptionalClientRunPipelineActivitypipelineActivitydeviceShadowEnrichTypeDef = TypedDict(
    "_OptionalClientRunPipelineActivitypipelineActivitydeviceShadowEnrichTypeDef",
    {"next": str},
    total=False,
)


class ClientRunPipelineActivitypipelineActivitydeviceShadowEnrichTypeDef(
    _RequiredClientRunPipelineActivitypipelineActivitydeviceShadowEnrichTypeDef,
    _OptionalClientRunPipelineActivitypipelineActivitydeviceShadowEnrichTypeDef,
):
    """
    Type definition for `ClientRunPipelineActivitypipelineActivity` `deviceShadowEnrich`

    Adds information from the AWS IoT Device Shadows service to a message.

    - **name** *(string) --* **[REQUIRED]**

      The name of the 'deviceShadowEnrich' activity.

    - **attribute** *(string) --* **[REQUIRED]**

      The name of the attribute that is added to the message.

    - **thingName** *(string) --* **[REQUIRED]**

      The name of the IoT device whose shadow information is added to the message.

    - **roleArn** *(string) --* **[REQUIRED]**

      The ARN of the role that allows access to the device's shadow.

    - **next** *(string) --*

      The next activity in the pipeline.
    """


_RequiredClientRunPipelineActivitypipelineActivityfilterTypeDef = TypedDict(
    "_RequiredClientRunPipelineActivitypipelineActivityfilterTypeDef",
    {"name": str, "filter": str},
)
_OptionalClientRunPipelineActivitypipelineActivityfilterTypeDef = TypedDict(
    "_OptionalClientRunPipelineActivitypipelineActivityfilterTypeDef",
    {"next": str},
    total=False,
)


class ClientRunPipelineActivitypipelineActivityfilterTypeDef(
    _RequiredClientRunPipelineActivitypipelineActivityfilterTypeDef,
    _OptionalClientRunPipelineActivitypipelineActivityfilterTypeDef,
):
    """
    Type definition for `ClientRunPipelineActivitypipelineActivity` `filter`

    Filters a message based on its attributes.

    - **name** *(string) --* **[REQUIRED]**

      The name of the 'filter' activity.

    - **filter** *(string) --* **[REQUIRED]**

      An expression that looks like a SQL WHERE clause that must return a Boolean value.

    - **next** *(string) --*

      The next activity in the pipeline.
    """


_RequiredClientRunPipelineActivitypipelineActivitylambdaTypeDef = TypedDict(
    "_RequiredClientRunPipelineActivitypipelineActivitylambdaTypeDef",
    {"name": str, "lambdaName": str, "batchSize": int},
)
_OptionalClientRunPipelineActivitypipelineActivitylambdaTypeDef = TypedDict(
    "_OptionalClientRunPipelineActivitypipelineActivitylambdaTypeDef",
    {"next": str},
    total=False,
)


class ClientRunPipelineActivitypipelineActivitylambdaTypeDef(
    _RequiredClientRunPipelineActivitypipelineActivitylambdaTypeDef,
    _OptionalClientRunPipelineActivitypipelineActivitylambdaTypeDef,
):
    """
    Type definition for `ClientRunPipelineActivitypipelineActivity` `lambda`

    Runs a Lambda function to modify the message.

    - **name** *(string) --* **[REQUIRED]**

      The name of the 'lambda' activity.

    - **lambdaName** *(string) --* **[REQUIRED]**

      The name of the Lambda function that is run on the message.

    - **batchSize** *(integer) --* **[REQUIRED]**

      The number of messages passed to the Lambda function for processing.

      The AWS Lambda function must be able to process all of these messages within five minutes,
      which is the maximum timeout duration for Lambda functions.

    - **next** *(string) --*

      The next activity in the pipeline.
    """


_RequiredClientRunPipelineActivitypipelineActivitymathTypeDef = TypedDict(
    "_RequiredClientRunPipelineActivitypipelineActivitymathTypeDef",
    {"name": str, "attribute": str, "math": str},
)
_OptionalClientRunPipelineActivitypipelineActivitymathTypeDef = TypedDict(
    "_OptionalClientRunPipelineActivitypipelineActivitymathTypeDef",
    {"next": str},
    total=False,
)


class ClientRunPipelineActivitypipelineActivitymathTypeDef(
    _RequiredClientRunPipelineActivitypipelineActivitymathTypeDef,
    _OptionalClientRunPipelineActivitypipelineActivitymathTypeDef,
):
    """
    Type definition for `ClientRunPipelineActivitypipelineActivity` `math`

    Computes an arithmetic expression using the message's attributes and adds it to the message.

    - **name** *(string) --* **[REQUIRED]**

      The name of the 'math' activity.

    - **attribute** *(string) --* **[REQUIRED]**

      The name of the attribute that contains the result of the math operation.

    - **math** *(string) --* **[REQUIRED]**

      An expression that uses one or more existing attributes and must return an integer value.

    - **next** *(string) --*

      The next activity in the pipeline.
    """


_RequiredClientRunPipelineActivitypipelineActivityremoveAttributesTypeDef = TypedDict(
    "_RequiredClientRunPipelineActivitypipelineActivityremoveAttributesTypeDef",
    {"name": str, "attributes": List[str]},
)
_OptionalClientRunPipelineActivitypipelineActivityremoveAttributesTypeDef = TypedDict(
    "_OptionalClientRunPipelineActivitypipelineActivityremoveAttributesTypeDef",
    {"next": str},
    total=False,
)


class ClientRunPipelineActivitypipelineActivityremoveAttributesTypeDef(
    _RequiredClientRunPipelineActivitypipelineActivityremoveAttributesTypeDef,
    _OptionalClientRunPipelineActivitypipelineActivityremoveAttributesTypeDef,
):
    """
    Type definition for `ClientRunPipelineActivitypipelineActivity` `removeAttributes`

    Removes attributes from a message.

    - **name** *(string) --* **[REQUIRED]**

      The name of the 'removeAttributes' activity.

    - **attributes** *(list) --* **[REQUIRED]**

      A list of 1-50 attributes to remove from the message.

      - *(string) --*

    - **next** *(string) --*

      The next activity in the pipeline.
    """


_RequiredClientRunPipelineActivitypipelineActivityselectAttributesTypeDef = TypedDict(
    "_RequiredClientRunPipelineActivitypipelineActivityselectAttributesTypeDef",
    {"name": str, "attributes": List[str]},
)
_OptionalClientRunPipelineActivitypipelineActivityselectAttributesTypeDef = TypedDict(
    "_OptionalClientRunPipelineActivitypipelineActivityselectAttributesTypeDef",
    {"next": str},
    total=False,
)


class ClientRunPipelineActivitypipelineActivityselectAttributesTypeDef(
    _RequiredClientRunPipelineActivitypipelineActivityselectAttributesTypeDef,
    _OptionalClientRunPipelineActivitypipelineActivityselectAttributesTypeDef,
):
    """
    Type definition for `ClientRunPipelineActivitypipelineActivity` `selectAttributes`

    Creates a new message using only the specified attributes from the original message.

    - **name** *(string) --* **[REQUIRED]**

      The name of the 'selectAttributes' activity.

    - **attributes** *(list) --* **[REQUIRED]**

      A list of the attributes to select from the message.

      - *(string) --*

    - **next** *(string) --*

      The next activity in the pipeline.
    """


_ClientRunPipelineActivitypipelineActivityTypeDef = TypedDict(
    "_ClientRunPipelineActivitypipelineActivityTypeDef",
    {
        "channel": ClientRunPipelineActivitypipelineActivitychannelTypeDef,
        "lambda": ClientRunPipelineActivitypipelineActivitylambdaTypeDef,
        "datastore": ClientRunPipelineActivitypipelineActivitydatastoreTypeDef,
        "addAttributes": ClientRunPipelineActivitypipelineActivityaddAttributesTypeDef,
        "removeAttributes": ClientRunPipelineActivitypipelineActivityremoveAttributesTypeDef,
        "selectAttributes": ClientRunPipelineActivitypipelineActivityselectAttributesTypeDef,
        "filter": ClientRunPipelineActivitypipelineActivityfilterTypeDef,
        "math": ClientRunPipelineActivitypipelineActivitymathTypeDef,
        "deviceRegistryEnrich": ClientRunPipelineActivitypipelineActivitydeviceRegistryEnrichTypeDef,
        "deviceShadowEnrich": ClientRunPipelineActivitypipelineActivitydeviceShadowEnrichTypeDef,
    },
    total=False,
)


class ClientRunPipelineActivitypipelineActivityTypeDef(
    _ClientRunPipelineActivitypipelineActivityTypeDef
):
    """
    Type definition for `ClientRunPipelineActivity` `pipelineActivity`

    The pipeline activity that is run. This must not be a 'channel' activity or a 'datastore'
    activity because these activities are used in a pipeline only to load the original message and to
    store the (possibly) transformed message. If a 'lambda' activity is specified, only short-running
    Lambda functions (those with a timeout of less than 30 seconds or less) can be used.

    - **channel** *(dict) --*

      Determines the source of the messages to be processed.

      - **name** *(string) --* **[REQUIRED]**

        The name of the 'channel' activity.

      - **channelName** *(string) --* **[REQUIRED]**

        The name of the channel from which the messages are processed.

      - **next** *(string) --*

        The next activity in the pipeline.

    - **lambda** *(dict) --*

      Runs a Lambda function to modify the message.

      - **name** *(string) --* **[REQUIRED]**

        The name of the 'lambda' activity.

      - **lambdaName** *(string) --* **[REQUIRED]**

        The name of the Lambda function that is run on the message.

      - **batchSize** *(integer) --* **[REQUIRED]**

        The number of messages passed to the Lambda function for processing.

        The AWS Lambda function must be able to process all of these messages within five minutes,
        which is the maximum timeout duration for Lambda functions.

      - **next** *(string) --*

        The next activity in the pipeline.

    - **datastore** *(dict) --*

      Specifies where to store the processed message data.

      - **name** *(string) --* **[REQUIRED]**

        The name of the 'datastore' activity.

      - **datastoreName** *(string) --* **[REQUIRED]**

        The name of the data store where processed messages are stored.

    - **addAttributes** *(dict) --*

      Adds other attributes based on existing attributes in the message.

      - **name** *(string) --* **[REQUIRED]**

        The name of the 'addAttributes' activity.

      - **attributes** *(dict) --* **[REQUIRED]**

        A list of 1-50 "AttributeNameMapping" objects that map an existing attribute to a new
        attribute.

        .. note::

          The existing attributes remain in the message, so if you want to remove the originals, use
          "RemoveAttributeActivity".

        - *(string) --*

          - *(string) --*

      - **next** *(string) --*

        The next activity in the pipeline.

    - **removeAttributes** *(dict) --*

      Removes attributes from a message.

      - **name** *(string) --* **[REQUIRED]**

        The name of the 'removeAttributes' activity.

      - **attributes** *(list) --* **[REQUIRED]**

        A list of 1-50 attributes to remove from the message.

        - *(string) --*

      - **next** *(string) --*

        The next activity in the pipeline.

    - **selectAttributes** *(dict) --*

      Creates a new message using only the specified attributes from the original message.

      - **name** *(string) --* **[REQUIRED]**

        The name of the 'selectAttributes' activity.

      - **attributes** *(list) --* **[REQUIRED]**

        A list of the attributes to select from the message.

        - *(string) --*

      - **next** *(string) --*

        The next activity in the pipeline.

    - **filter** *(dict) --*

      Filters a message based on its attributes.

      - **name** *(string) --* **[REQUIRED]**

        The name of the 'filter' activity.

      - **filter** *(string) --* **[REQUIRED]**

        An expression that looks like a SQL WHERE clause that must return a Boolean value.

      - **next** *(string) --*

        The next activity in the pipeline.

    - **math** *(dict) --*

      Computes an arithmetic expression using the message's attributes and adds it to the message.

      - **name** *(string) --* **[REQUIRED]**

        The name of the 'math' activity.

      - **attribute** *(string) --* **[REQUIRED]**

        The name of the attribute that contains the result of the math operation.

      - **math** *(string) --* **[REQUIRED]**

        An expression that uses one or more existing attributes and must return an integer value.

      - **next** *(string) --*

        The next activity in the pipeline.

    - **deviceRegistryEnrich** *(dict) --*

      Adds data from the AWS IoT device registry to your message.

      - **name** *(string) --* **[REQUIRED]**

        The name of the 'deviceRegistryEnrich' activity.

      - **attribute** *(string) --* **[REQUIRED]**

        The name of the attribute that is added to the message.

      - **thingName** *(string) --* **[REQUIRED]**

        The name of the IoT device whose registry information is added to the message.

      - **roleArn** *(string) --* **[REQUIRED]**

        The ARN of the role that allows access to the device's registry information.

      - **next** *(string) --*

        The next activity in the pipeline.

    - **deviceShadowEnrich** *(dict) --*

      Adds information from the AWS IoT Device Shadows service to a message.

      - **name** *(string) --* **[REQUIRED]**

        The name of the 'deviceShadowEnrich' activity.

      - **attribute** *(string) --* **[REQUIRED]**

        The name of the attribute that is added to the message.

      - **thingName** *(string) --* **[REQUIRED]**

        The name of the IoT device whose shadow information is added to the message.

      - **roleArn** *(string) --* **[REQUIRED]**

        The ARN of the role that allows access to the device's shadow.

      - **next** *(string) --*

        The next activity in the pipeline.
    """


_ClientSampleChannelDataResponseTypeDef = TypedDict(
    "_ClientSampleChannelDataResponseTypeDef", {"payloads": List[bytes]}, total=False
)


class ClientSampleChannelDataResponseTypeDef(_ClientSampleChannelDataResponseTypeDef):
    """
    Type definition for `ClientSampleChannelData` `Response`

    - **payloads** *(list) --*

      The list of message samples. Each sample message is returned as a base64-encoded string.

      - *(bytes) --*
    """


_ClientStartPipelineReprocessingResponseTypeDef = TypedDict(
    "_ClientStartPipelineReprocessingResponseTypeDef",
    {"reprocessingId": str},
    total=False,
)


class ClientStartPipelineReprocessingResponseTypeDef(
    _ClientStartPipelineReprocessingResponseTypeDef
):
    """
    Type definition for `ClientStartPipelineReprocessing` `Response`

    - **reprocessingId** *(string) --*

      The ID of the pipeline reprocessing activity that was started.
    """


_ClientTagResourcetagsTypeDef = TypedDict(
    "_ClientTagResourcetagsTypeDef", {"key": str, "value": str}
)


class ClientTagResourcetagsTypeDef(_ClientTagResourcetagsTypeDef):
    """
    Type definition for `ClientTagResource` `tags`

    A set of key/value pairs which are used to manage the resource.

    - **key** *(string) --* **[REQUIRED]**

      The tag's key.

    - **value** *(string) --* **[REQUIRED]**

      The tag's value.
    """


_RequiredClientUpdateChannelchannelStoragecustomerManagedS3TypeDef = TypedDict(
    "_RequiredClientUpdateChannelchannelStoragecustomerManagedS3TypeDef",
    {"bucket": str, "roleArn": str},
)
_OptionalClientUpdateChannelchannelStoragecustomerManagedS3TypeDef = TypedDict(
    "_OptionalClientUpdateChannelchannelStoragecustomerManagedS3TypeDef",
    {"keyPrefix": str},
    total=False,
)


class ClientUpdateChannelchannelStoragecustomerManagedS3TypeDef(
    _RequiredClientUpdateChannelchannelStoragecustomerManagedS3TypeDef,
    _OptionalClientUpdateChannelchannelStoragecustomerManagedS3TypeDef,
):
    """
    Type definition for `ClientUpdateChannelchannelStorage` `customerManagedS3`

    Use this to store channel data in an S3 bucket that you manage. If customer managed storage is
    selected, the "retentionPeriod" parameter is ignored. The choice of service-managed or
    customer-managed S3 storage cannot be changed after creation of the channel.

    - **bucket** *(string) --* **[REQUIRED]**

      The name of the Amazon S3 bucket in which channel data is stored.

    - **keyPrefix** *(string) --*

      [Optional] The prefix used to create the keys of the channel data objects. Each object in an
      Amazon S3 bucket has a key that is its unique identifier within the bucket (each object in a
      bucket has exactly one key). The prefix must end with a '/'.

    - **roleArn** *(string) --* **[REQUIRED]**

      The ARN of the role which grants AWS IoT Analytics permission to interact with your Amazon S3
      resources.
    """


_ClientUpdateChannelchannelStorageTypeDef = TypedDict(
    "_ClientUpdateChannelchannelStorageTypeDef",
    {
        "serviceManagedS3": Dict,
        "customerManagedS3": ClientUpdateChannelchannelStoragecustomerManagedS3TypeDef,
    },
    total=False,
)


class ClientUpdateChannelchannelStorageTypeDef(
    _ClientUpdateChannelchannelStorageTypeDef
):
    """
    Type definition for `ClientUpdateChannel` `channelStorage`

    Where channel data is stored. You may choose one of "serviceManagedS3" or "customerManagedS3"
    storage. If not specified, the default is "serviceManagedS3". This cannot be changed after
    creation of the channel.

    - **serviceManagedS3** *(dict) --*

      Use this to store channel data in an S3 bucket managed by the AWS IoT Analytics service. The
      choice of service-managed or customer-managed S3 storage cannot be changed after creation of
      the channel.

    - **customerManagedS3** *(dict) --*

      Use this to store channel data in an S3 bucket that you manage. If customer managed storage is
      selected, the "retentionPeriod" parameter is ignored. The choice of service-managed or
      customer-managed S3 storage cannot be changed after creation of the channel.

      - **bucket** *(string) --* **[REQUIRED]**

        The name of the Amazon S3 bucket in which channel data is stored.

      - **keyPrefix** *(string) --*

        [Optional] The prefix used to create the keys of the channel data objects. Each object in an
        Amazon S3 bucket has a key that is its unique identifier within the bucket (each object in a
        bucket has exactly one key). The prefix must end with a '/'.

      - **roleArn** *(string) --* **[REQUIRED]**

        The ARN of the role which grants AWS IoT Analytics permission to interact with your Amazon S3
        resources.
    """


_ClientUpdateChannelretentionPeriodTypeDef = TypedDict(
    "_ClientUpdateChannelretentionPeriodTypeDef",
    {"unlimited": bool, "numberOfDays": int},
    total=False,
)


class ClientUpdateChannelretentionPeriodTypeDef(
    _ClientUpdateChannelretentionPeriodTypeDef
):
    """
    Type definition for `ClientUpdateChannel` `retentionPeriod`

    How long, in days, message data is kept for the channel. The retention period cannot be updated
    if the channel's S3 storage is customer-managed.

    - **unlimited** *(boolean) --*

      If true, message data is kept indefinitely.

    - **numberOfDays** *(integer) --*

      The number of days that message data is kept. The "unlimited" parameter must be false.
    """


_ClientUpdateDatasetactionscontainerActionresourceConfigurationTypeDef = TypedDict(
    "_ClientUpdateDatasetactionscontainerActionresourceConfigurationTypeDef",
    {"computeType": str, "volumeSizeInGB": int},
)


class ClientUpdateDatasetactionscontainerActionresourceConfigurationTypeDef(
    _ClientUpdateDatasetactionscontainerActionresourceConfigurationTypeDef
):
    """
    Type definition for `ClientUpdateDatasetactionscontainerAction` `resourceConfiguration`

    Configuration of the resource which executes the "containerAction".

    - **computeType** *(string) --* **[REQUIRED]**

      The type of the compute resource used to execute the "containerAction". Possible values
      are: ACU_1 (vCPU=4, memory=16GiB) or ACU_2 (vCPU=8, memory=32GiB).

    - **volumeSizeInGB** *(integer) --* **[REQUIRED]**

      The size (in GB) of the persistent storage available to the resource instance used to
      execute the "containerAction" (min: 1, max: 50).
    """


_ClientUpdateDatasetactionscontainerActionvariablesdatasetContentVersionValueTypeDef = TypedDict(
    "_ClientUpdateDatasetactionscontainerActionvariablesdatasetContentVersionValueTypeDef",
    {"datasetName": str},
)


class ClientUpdateDatasetactionscontainerActionvariablesdatasetContentVersionValueTypeDef(
    _ClientUpdateDatasetactionscontainerActionvariablesdatasetContentVersionValueTypeDef
):
    """
    Type definition for `ClientUpdateDatasetactionscontainerActionvariables` `datasetContentVersionValue`

    The value of the variable as a structure that specifies a data set content version.

    - **datasetName** *(string) --* **[REQUIRED]**

      The name of the data set whose latest contents are used as input to the notebook or
      application.
    """


_ClientUpdateDatasetactionscontainerActionvariablesoutputFileUriValueTypeDef = TypedDict(
    "_ClientUpdateDatasetactionscontainerActionvariablesoutputFileUriValueTypeDef",
    {"fileName": str},
)


class ClientUpdateDatasetactionscontainerActionvariablesoutputFileUriValueTypeDef(
    _ClientUpdateDatasetactionscontainerActionvariablesoutputFileUriValueTypeDef
):
    """
    Type definition for `ClientUpdateDatasetactionscontainerActionvariables` `outputFileUriValue`

    The value of the variable as a structure that specifies an output file URI.

    - **fileName** *(string) --* **[REQUIRED]**

      The URI of the location where data set contents are stored, usually the URI of a file
      in an S3 bucket.
    """


_RequiredClientUpdateDatasetactionscontainerActionvariablesTypeDef = TypedDict(
    "_RequiredClientUpdateDatasetactionscontainerActionvariablesTypeDef", {"name": str}
)
_OptionalClientUpdateDatasetactionscontainerActionvariablesTypeDef = TypedDict(
    "_OptionalClientUpdateDatasetactionscontainerActionvariablesTypeDef",
    {
        "stringValue": str,
        "doubleValue": float,
        "datasetContentVersionValue": ClientUpdateDatasetactionscontainerActionvariablesdatasetContentVersionValueTypeDef,
        "outputFileUriValue": ClientUpdateDatasetactionscontainerActionvariablesoutputFileUriValueTypeDef,
    },
    total=False,
)


class ClientUpdateDatasetactionscontainerActionvariablesTypeDef(
    _RequiredClientUpdateDatasetactionscontainerActionvariablesTypeDef,
    _OptionalClientUpdateDatasetactionscontainerActionvariablesTypeDef,
):
    """
    Type definition for `ClientUpdateDatasetactionscontainerAction` `variables`

    An instance of a variable to be passed to the "containerAction" execution. Each variable
    must have a name and a value given by one of "stringValue", "datasetContentVersionValue",
    or "outputFileUriValue".

    - **name** *(string) --* **[REQUIRED]**

      The name of the variable.

    - **stringValue** *(string) --*

      The value of the variable as a string.

    - **doubleValue** *(float) --*

      The value of the variable as a double (numeric).

    - **datasetContentVersionValue** *(dict) --*

      The value of the variable as a structure that specifies a data set content version.

      - **datasetName** *(string) --* **[REQUIRED]**

        The name of the data set whose latest contents are used as input to the notebook or
        application.

    - **outputFileUriValue** *(dict) --*

      The value of the variable as a structure that specifies an output file URI.

      - **fileName** *(string) --* **[REQUIRED]**

        The URI of the location where data set contents are stored, usually the URI of a file
        in an S3 bucket.
    """


_RequiredClientUpdateDatasetactionscontainerActionTypeDef = TypedDict(
    "_RequiredClientUpdateDatasetactionscontainerActionTypeDef",
    {
        "image": str,
        "executionRoleArn": str,
        "resourceConfiguration": ClientUpdateDatasetactionscontainerActionresourceConfigurationTypeDef,
    },
)
_OptionalClientUpdateDatasetactionscontainerActionTypeDef = TypedDict(
    "_OptionalClientUpdateDatasetactionscontainerActionTypeDef",
    {"variables": List[ClientUpdateDatasetactionscontainerActionvariablesTypeDef]},
    total=False,
)


class ClientUpdateDatasetactionscontainerActionTypeDef(
    _RequiredClientUpdateDatasetactionscontainerActionTypeDef,
    _OptionalClientUpdateDatasetactionscontainerActionTypeDef,
):
    """
    Type definition for `ClientUpdateDatasetactions` `containerAction`

    Information which allows the system to run a containerized application in order to create the
    data set contents. The application must be in a Docker container along with any needed
    support libraries.

    - **image** *(string) --* **[REQUIRED]**

      The ARN of the Docker container stored in your account. The Docker container contains an
      application and needed support libraries and is used to generate data set contents.

    - **executionRoleArn** *(string) --* **[REQUIRED]**

      The ARN of the role which gives permission to the system to access needed resources in
      order to run the "containerAction". This includes, at minimum, permission to retrieve the
      data set contents which are the input to the containerized application.

    - **resourceConfiguration** *(dict) --* **[REQUIRED]**

      Configuration of the resource which executes the "containerAction".

      - **computeType** *(string) --* **[REQUIRED]**

        The type of the compute resource used to execute the "containerAction". Possible values
        are: ACU_1 (vCPU=4, memory=16GiB) or ACU_2 (vCPU=8, memory=32GiB).

      - **volumeSizeInGB** *(integer) --* **[REQUIRED]**

        The size (in GB) of the persistent storage available to the resource instance used to
        execute the "containerAction" (min: 1, max: 50).

    - **variables** *(list) --*

      The values of variables used within the context of the execution of the containerized
      application (basically, parameters passed to the application). Each variable must have a
      name and a value given by one of "stringValue", "datasetContentVersionValue", or
      "outputFileUriValue".

      - *(dict) --*

        An instance of a variable to be passed to the "containerAction" execution. Each variable
        must have a name and a value given by one of "stringValue", "datasetContentVersionValue",
        or "outputFileUriValue".

        - **name** *(string) --* **[REQUIRED]**

          The name of the variable.

        - **stringValue** *(string) --*

          The value of the variable as a string.

        - **doubleValue** *(float) --*

          The value of the variable as a double (numeric).

        - **datasetContentVersionValue** *(dict) --*

          The value of the variable as a structure that specifies a data set content version.

          - **datasetName** *(string) --* **[REQUIRED]**

            The name of the data set whose latest contents are used as input to the notebook or
            application.

        - **outputFileUriValue** *(dict) --*

          The value of the variable as a structure that specifies an output file URI.

          - **fileName** *(string) --* **[REQUIRED]**

            The URI of the location where data set contents are stored, usually the URI of a file
            in an S3 bucket.
    """


_ClientUpdateDatasetactionsqueryActionfiltersdeltaTimeTypeDef = TypedDict(
    "_ClientUpdateDatasetactionsqueryActionfiltersdeltaTimeTypeDef",
    {"offsetSeconds": int, "timeExpression": str},
)


class ClientUpdateDatasetactionsqueryActionfiltersdeltaTimeTypeDef(
    _ClientUpdateDatasetactionsqueryActionfiltersdeltaTimeTypeDef
):
    """
    Type definition for `ClientUpdateDatasetactionsqueryActionfilters` `deltaTime`

    Used to limit data to that which has arrived since the last execution of the action.

    - **offsetSeconds** *(integer) --* **[REQUIRED]**

      The number of seconds of estimated "in flight" lag time of message data. When you
      create data set contents using message data from a specified time frame, some message
      data may still be "in flight" when processing begins, and so will not arrive in time
      to be processed. Use this field to make allowances for the "in flight" time of your
      message data, so that data not processed from a previous time frame will be included
      with the next time frame. Without this, missed message data would be excluded from
      processing during the next time frame as well, because its timestamp places it within
      the previous time frame.

    - **timeExpression** *(string) --* **[REQUIRED]**

      An expression by which the time of the message data may be determined. This may be
      the name of a timestamp field, or a SQL expression which is used to derive the time
      the message data was generated.
    """


_ClientUpdateDatasetactionsqueryActionfiltersTypeDef = TypedDict(
    "_ClientUpdateDatasetactionsqueryActionfiltersTypeDef",
    {"deltaTime": ClientUpdateDatasetactionsqueryActionfiltersdeltaTimeTypeDef},
    total=False,
)


class ClientUpdateDatasetactionsqueryActionfiltersTypeDef(
    _ClientUpdateDatasetactionsqueryActionfiltersTypeDef
):
    """
    Type definition for `ClientUpdateDatasetactionsqueryAction` `filters`

    Information which is used to filter message data, to segregate it according to the time
    frame in which it arrives.

    - **deltaTime** *(dict) --*

      Used to limit data to that which has arrived since the last execution of the action.

      - **offsetSeconds** *(integer) --* **[REQUIRED]**

        The number of seconds of estimated "in flight" lag time of message data. When you
        create data set contents using message data from a specified time frame, some message
        data may still be "in flight" when processing begins, and so will not arrive in time
        to be processed. Use this field to make allowances for the "in flight" time of your
        message data, so that data not processed from a previous time frame will be included
        with the next time frame. Without this, missed message data would be excluded from
        processing during the next time frame as well, because its timestamp places it within
        the previous time frame.

      - **timeExpression** *(string) --* **[REQUIRED]**

        An expression by which the time of the message data may be determined. This may be
        the name of a timestamp field, or a SQL expression which is used to derive the time
        the message data was generated.
    """


_RequiredClientUpdateDatasetactionsqueryActionTypeDef = TypedDict(
    "_RequiredClientUpdateDatasetactionsqueryActionTypeDef", {"sqlQuery": str}
)
_OptionalClientUpdateDatasetactionsqueryActionTypeDef = TypedDict(
    "_OptionalClientUpdateDatasetactionsqueryActionTypeDef",
    {"filters": List[ClientUpdateDatasetactionsqueryActionfiltersTypeDef]},
    total=False,
)


class ClientUpdateDatasetactionsqueryActionTypeDef(
    _RequiredClientUpdateDatasetactionsqueryActionTypeDef,
    _OptionalClientUpdateDatasetactionsqueryActionTypeDef,
):
    """
    Type definition for `ClientUpdateDatasetactions` `queryAction`

    An "SqlQueryDatasetAction" object that uses an SQL query to automatically create data set
    contents.

    - **sqlQuery** *(string) --* **[REQUIRED]**

      A SQL query string.

    - **filters** *(list) --*

      Pre-filters applied to message data.

      - *(dict) --*

        Information which is used to filter message data, to segregate it according to the time
        frame in which it arrives.

        - **deltaTime** *(dict) --*

          Used to limit data to that which has arrived since the last execution of the action.

          - **offsetSeconds** *(integer) --* **[REQUIRED]**

            The number of seconds of estimated "in flight" lag time of message data. When you
            create data set contents using message data from a specified time frame, some message
            data may still be "in flight" when processing begins, and so will not arrive in time
            to be processed. Use this field to make allowances for the "in flight" time of your
            message data, so that data not processed from a previous time frame will be included
            with the next time frame. Without this, missed message data would be excluded from
            processing during the next time frame as well, because its timestamp places it within
            the previous time frame.

          - **timeExpression** *(string) --* **[REQUIRED]**

            An expression by which the time of the message data may be determined. This may be
            the name of a timestamp field, or a SQL expression which is used to derive the time
            the message data was generated.
    """


_ClientUpdateDatasetactionsTypeDef = TypedDict(
    "_ClientUpdateDatasetactionsTypeDef",
    {
        "actionName": str,
        "queryAction": ClientUpdateDatasetactionsqueryActionTypeDef,
        "containerAction": ClientUpdateDatasetactionscontainerActionTypeDef,
    },
    total=False,
)


class ClientUpdateDatasetactionsTypeDef(_ClientUpdateDatasetactionsTypeDef):
    """
    Type definition for `ClientUpdateDataset` `actions`

    A "DatasetAction" object that specifies how data set contents are automatically created.

    - **actionName** *(string) --*

      The name of the data set action by which data set contents are automatically created.

    - **queryAction** *(dict) --*

      An "SqlQueryDatasetAction" object that uses an SQL query to automatically create data set
      contents.

      - **sqlQuery** *(string) --* **[REQUIRED]**

        A SQL query string.

      - **filters** *(list) --*

        Pre-filters applied to message data.

        - *(dict) --*

          Information which is used to filter message data, to segregate it according to the time
          frame in which it arrives.

          - **deltaTime** *(dict) --*

            Used to limit data to that which has arrived since the last execution of the action.

            - **offsetSeconds** *(integer) --* **[REQUIRED]**

              The number of seconds of estimated "in flight" lag time of message data. When you
              create data set contents using message data from a specified time frame, some message
              data may still be "in flight" when processing begins, and so will not arrive in time
              to be processed. Use this field to make allowances for the "in flight" time of your
              message data, so that data not processed from a previous time frame will be included
              with the next time frame. Without this, missed message data would be excluded from
              processing during the next time frame as well, because its timestamp places it within
              the previous time frame.

            - **timeExpression** *(string) --* **[REQUIRED]**

              An expression by which the time of the message data may be determined. This may be
              the name of a timestamp field, or a SQL expression which is used to derive the time
              the message data was generated.

    - **containerAction** *(dict) --*

      Information which allows the system to run a containerized application in order to create the
      data set contents. The application must be in a Docker container along with any needed
      support libraries.

      - **image** *(string) --* **[REQUIRED]**

        The ARN of the Docker container stored in your account. The Docker container contains an
        application and needed support libraries and is used to generate data set contents.

      - **executionRoleArn** *(string) --* **[REQUIRED]**

        The ARN of the role which gives permission to the system to access needed resources in
        order to run the "containerAction". This includes, at minimum, permission to retrieve the
        data set contents which are the input to the containerized application.

      - **resourceConfiguration** *(dict) --* **[REQUIRED]**

        Configuration of the resource which executes the "containerAction".

        - **computeType** *(string) --* **[REQUIRED]**

          The type of the compute resource used to execute the "containerAction". Possible values
          are: ACU_1 (vCPU=4, memory=16GiB) or ACU_2 (vCPU=8, memory=32GiB).

        - **volumeSizeInGB** *(integer) --* **[REQUIRED]**

          The size (in GB) of the persistent storage available to the resource instance used to
          execute the "containerAction" (min: 1, max: 50).

      - **variables** *(list) --*

        The values of variables used within the context of the execution of the containerized
        application (basically, parameters passed to the application). Each variable must have a
        name and a value given by one of "stringValue", "datasetContentVersionValue", or
        "outputFileUriValue".

        - *(dict) --*

          An instance of a variable to be passed to the "containerAction" execution. Each variable
          must have a name and a value given by one of "stringValue", "datasetContentVersionValue",
          or "outputFileUriValue".

          - **name** *(string) --* **[REQUIRED]**

            The name of the variable.

          - **stringValue** *(string) --*

            The value of the variable as a string.

          - **doubleValue** *(float) --*

            The value of the variable as a double (numeric).

          - **datasetContentVersionValue** *(dict) --*

            The value of the variable as a structure that specifies a data set content version.

            - **datasetName** *(string) --* **[REQUIRED]**

              The name of the data set whose latest contents are used as input to the notebook or
              application.

          - **outputFileUriValue** *(dict) --*

            The value of the variable as a structure that specifies an output file URI.

            - **fileName** *(string) --* **[REQUIRED]**

              The URI of the location where data set contents are stored, usually the URI of a file
              in an S3 bucket.
    """


_ClientUpdateDatasetcontentDeliveryRulesdestinationiotEventsDestinationConfigurationTypeDef = TypedDict(
    "_ClientUpdateDatasetcontentDeliveryRulesdestinationiotEventsDestinationConfigurationTypeDef",
    {"inputName": str, "roleArn": str},
)


class ClientUpdateDatasetcontentDeliveryRulesdestinationiotEventsDestinationConfigurationTypeDef(
    _ClientUpdateDatasetcontentDeliveryRulesdestinationiotEventsDestinationConfigurationTypeDef
):
    """
    Type definition for `ClientUpdateDatasetcontentDeliveryRulesdestination` `iotEventsDestinationConfiguration`

    Configuration information for delivery of data set contents to AWS IoT Events.

    - **inputName** *(string) --* **[REQUIRED]**

      The name of the AWS IoT Events input to which data set contents are delivered.

    - **roleArn** *(string) --* **[REQUIRED]**

      The ARN of the role which grants AWS IoT Analytics permission to deliver data set
      contents to an AWS IoT Events input.
    """


_ClientUpdateDatasetcontentDeliveryRulesdestinations3DestinationConfigurationglueConfigurationTypeDef = TypedDict(
    "_ClientUpdateDatasetcontentDeliveryRulesdestinations3DestinationConfigurationglueConfigurationTypeDef",
    {"tableName": str, "databaseName": str},
)


class ClientUpdateDatasetcontentDeliveryRulesdestinations3DestinationConfigurationglueConfigurationTypeDef(
    _ClientUpdateDatasetcontentDeliveryRulesdestinations3DestinationConfigurationglueConfigurationTypeDef
):
    """
    Type definition for `ClientUpdateDatasetcontentDeliveryRulesdestinations3DestinationConfiguration` `glueConfiguration`

    Configuration information for coordination with the AWS Glue ETL (extract, transform and
    load) service.

    - **tableName** *(string) --* **[REQUIRED]**

      The name of the table in your AWS Glue Data Catalog which is used to perform the ETL
      (extract, transform and load) operations. (An AWS Glue Data Catalog table contains
      partitioned data and descriptions of data sources and targets.)

    - **databaseName** *(string) --* **[REQUIRED]**

      The name of the database in your AWS Glue Data Catalog in which the table is located.
      (An AWS Glue Data Catalog database contains Glue Data tables.)
    """


_RequiredClientUpdateDatasetcontentDeliveryRulesdestinations3DestinationConfigurationTypeDef = TypedDict(
    "_RequiredClientUpdateDatasetcontentDeliveryRulesdestinations3DestinationConfigurationTypeDef",
    {"bucket": str, "key": str, "roleArn": str},
)
_OptionalClientUpdateDatasetcontentDeliveryRulesdestinations3DestinationConfigurationTypeDef = TypedDict(
    "_OptionalClientUpdateDatasetcontentDeliveryRulesdestinations3DestinationConfigurationTypeDef",
    {
        "glueConfiguration": ClientUpdateDatasetcontentDeliveryRulesdestinations3DestinationConfigurationglueConfigurationTypeDef
    },
    total=False,
)


class ClientUpdateDatasetcontentDeliveryRulesdestinations3DestinationConfigurationTypeDef(
    _RequiredClientUpdateDatasetcontentDeliveryRulesdestinations3DestinationConfigurationTypeDef,
    _OptionalClientUpdateDatasetcontentDeliveryRulesdestinations3DestinationConfigurationTypeDef,
):
    """
    Type definition for `ClientUpdateDatasetcontentDeliveryRulesdestination` `s3DestinationConfiguration`

    Configuration information for delivery of data set contents to Amazon S3.

    - **bucket** *(string) --* **[REQUIRED]**

      The name of the Amazon S3 bucket to which data set contents are delivered.

    - **key** *(string) --* **[REQUIRED]**

      The key of the data set contents object. Each object in an Amazon S3 bucket has a key
      that is its unique identifier within the bucket (each object in a bucket has exactly one
      key). To produce a unique key, you can use "!{iotanalytics:scheduledTime}" to insert the
      time of the scheduled SQL query run, or "!{iotanalytics:versioned} to insert a unique
      hash identifying the data set, for example:
      "/DataSet/!{iotanalytics:scheduledTime}/!{iotanalytics:versioned}.csv".

    - **glueConfiguration** *(dict) --*

      Configuration information for coordination with the AWS Glue ETL (extract, transform and
      load) service.

      - **tableName** *(string) --* **[REQUIRED]**

        The name of the table in your AWS Glue Data Catalog which is used to perform the ETL
        (extract, transform and load) operations. (An AWS Glue Data Catalog table contains
        partitioned data and descriptions of data sources and targets.)

      - **databaseName** *(string) --* **[REQUIRED]**

        The name of the database in your AWS Glue Data Catalog in which the table is located.
        (An AWS Glue Data Catalog database contains Glue Data tables.)

    - **roleArn** *(string) --* **[REQUIRED]**

      The ARN of the role which grants AWS IoT Analytics permission to interact with your
      Amazon S3 and AWS Glue resources.
    """


_ClientUpdateDatasetcontentDeliveryRulesdestinationTypeDef = TypedDict(
    "_ClientUpdateDatasetcontentDeliveryRulesdestinationTypeDef",
    {
        "iotEventsDestinationConfiguration": ClientUpdateDatasetcontentDeliveryRulesdestinationiotEventsDestinationConfigurationTypeDef,
        "s3DestinationConfiguration": ClientUpdateDatasetcontentDeliveryRulesdestinations3DestinationConfigurationTypeDef,
    },
    total=False,
)


class ClientUpdateDatasetcontentDeliveryRulesdestinationTypeDef(
    _ClientUpdateDatasetcontentDeliveryRulesdestinationTypeDef
):
    """
    Type definition for `ClientUpdateDatasetcontentDeliveryRules` `destination`

    The destination to which data set contents are delivered.

    - **iotEventsDestinationConfiguration** *(dict) --*

      Configuration information for delivery of data set contents to AWS IoT Events.

      - **inputName** *(string) --* **[REQUIRED]**

        The name of the AWS IoT Events input to which data set contents are delivered.

      - **roleArn** *(string) --* **[REQUIRED]**

        The ARN of the role which grants AWS IoT Analytics permission to deliver data set
        contents to an AWS IoT Events input.

    - **s3DestinationConfiguration** *(dict) --*

      Configuration information for delivery of data set contents to Amazon S3.

      - **bucket** *(string) --* **[REQUIRED]**

        The name of the Amazon S3 bucket to which data set contents are delivered.

      - **key** *(string) --* **[REQUIRED]**

        The key of the data set contents object. Each object in an Amazon S3 bucket has a key
        that is its unique identifier within the bucket (each object in a bucket has exactly one
        key). To produce a unique key, you can use "!{iotanalytics:scheduledTime}" to insert the
        time of the scheduled SQL query run, or "!{iotanalytics:versioned} to insert a unique
        hash identifying the data set, for example:
        "/DataSet/!{iotanalytics:scheduledTime}/!{iotanalytics:versioned}.csv".

      - **glueConfiguration** *(dict) --*

        Configuration information for coordination with the AWS Glue ETL (extract, transform and
        load) service.

        - **tableName** *(string) --* **[REQUIRED]**

          The name of the table in your AWS Glue Data Catalog which is used to perform the ETL
          (extract, transform and load) operations. (An AWS Glue Data Catalog table contains
          partitioned data and descriptions of data sources and targets.)

        - **databaseName** *(string) --* **[REQUIRED]**

          The name of the database in your AWS Glue Data Catalog in which the table is located.
          (An AWS Glue Data Catalog database contains Glue Data tables.)

      - **roleArn** *(string) --* **[REQUIRED]**

        The ARN of the role which grants AWS IoT Analytics permission to interact with your
        Amazon S3 and AWS Glue resources.
    """


_RequiredClientUpdateDatasetcontentDeliveryRulesTypeDef = TypedDict(
    "_RequiredClientUpdateDatasetcontentDeliveryRulesTypeDef",
    {"destination": ClientUpdateDatasetcontentDeliveryRulesdestinationTypeDef},
)
_OptionalClientUpdateDatasetcontentDeliveryRulesTypeDef = TypedDict(
    "_OptionalClientUpdateDatasetcontentDeliveryRulesTypeDef",
    {"entryName": str},
    total=False,
)


class ClientUpdateDatasetcontentDeliveryRulesTypeDef(
    _RequiredClientUpdateDatasetcontentDeliveryRulesTypeDef,
    _OptionalClientUpdateDatasetcontentDeliveryRulesTypeDef,
):
    """
    Type definition for `ClientUpdateDataset` `contentDeliveryRules`

    When data set contents are created they are delivered to destination specified here.

    - **entryName** *(string) --*

      The name of the data set content delivery rules entry.

    - **destination** *(dict) --* **[REQUIRED]**

      The destination to which data set contents are delivered.

      - **iotEventsDestinationConfiguration** *(dict) --*

        Configuration information for delivery of data set contents to AWS IoT Events.

        - **inputName** *(string) --* **[REQUIRED]**

          The name of the AWS IoT Events input to which data set contents are delivered.

        - **roleArn** *(string) --* **[REQUIRED]**

          The ARN of the role which grants AWS IoT Analytics permission to deliver data set
          contents to an AWS IoT Events input.

      - **s3DestinationConfiguration** *(dict) --*

        Configuration information for delivery of data set contents to Amazon S3.

        - **bucket** *(string) --* **[REQUIRED]**

          The name of the Amazon S3 bucket to which data set contents are delivered.

        - **key** *(string) --* **[REQUIRED]**

          The key of the data set contents object. Each object in an Amazon S3 bucket has a key
          that is its unique identifier within the bucket (each object in a bucket has exactly one
          key). To produce a unique key, you can use "!{iotanalytics:scheduledTime}" to insert the
          time of the scheduled SQL query run, or "!{iotanalytics:versioned} to insert a unique
          hash identifying the data set, for example:
          "/DataSet/!{iotanalytics:scheduledTime}/!{iotanalytics:versioned}.csv".

        - **glueConfiguration** *(dict) --*

          Configuration information for coordination with the AWS Glue ETL (extract, transform and
          load) service.

          - **tableName** *(string) --* **[REQUIRED]**

            The name of the table in your AWS Glue Data Catalog which is used to perform the ETL
            (extract, transform and load) operations. (An AWS Glue Data Catalog table contains
            partitioned data and descriptions of data sources and targets.)

          - **databaseName** *(string) --* **[REQUIRED]**

            The name of the database in your AWS Glue Data Catalog in which the table is located.
            (An AWS Glue Data Catalog database contains Glue Data tables.)

        - **roleArn** *(string) --* **[REQUIRED]**

          The ARN of the role which grants AWS IoT Analytics permission to interact with your
          Amazon S3 and AWS Glue resources.
    """


_ClientUpdateDatasetretentionPeriodTypeDef = TypedDict(
    "_ClientUpdateDatasetretentionPeriodTypeDef",
    {"unlimited": bool, "numberOfDays": int},
    total=False,
)


class ClientUpdateDatasetretentionPeriodTypeDef(
    _ClientUpdateDatasetretentionPeriodTypeDef
):
    """
    Type definition for `ClientUpdateDataset` `retentionPeriod`

    How long, in days, data set contents are kept for the data set.

    - **unlimited** *(boolean) --*

      If true, message data is kept indefinitely.

    - **numberOfDays** *(integer) --*

      The number of days that message data is kept. The "unlimited" parameter must be false.
    """


_ClientUpdateDatasettriggersdatasetTypeDef = TypedDict(
    "_ClientUpdateDatasettriggersdatasetTypeDef", {"name": str}
)


class ClientUpdateDatasettriggersdatasetTypeDef(
    _ClientUpdateDatasettriggersdatasetTypeDef
):
    """
    Type definition for `ClientUpdateDatasettriggers` `dataset`

    The data set whose content creation triggers the creation of this data set's contents.

    - **name** *(string) --* **[REQUIRED]**

      The name of the data set whose content generation triggers the new data set content
      generation.
    """


_ClientUpdateDatasettriggersscheduleTypeDef = TypedDict(
    "_ClientUpdateDatasettriggersscheduleTypeDef", {"expression": str}, total=False
)


class ClientUpdateDatasettriggersscheduleTypeDef(
    _ClientUpdateDatasettriggersscheduleTypeDef
):
    """
    Type definition for `ClientUpdateDatasettriggers` `schedule`

    The "Schedule" when the trigger is initiated.

    - **expression** *(string) --*

      The expression that defines when to trigger an update. For more information, see `Schedule
      Expressions for Rules
      <https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html>`__ in the
      Amazon CloudWatch Events User Guide.
    """


_ClientUpdateDatasettriggersTypeDef = TypedDict(
    "_ClientUpdateDatasettriggersTypeDef",
    {
        "schedule": ClientUpdateDatasettriggersscheduleTypeDef,
        "dataset": ClientUpdateDatasettriggersdatasetTypeDef,
    },
    total=False,
)


class ClientUpdateDatasettriggersTypeDef(_ClientUpdateDatasettriggersTypeDef):
    """
    Type definition for `ClientUpdateDataset` `triggers`

    The "DatasetTrigger" that specifies when the data set is automatically updated.

    - **schedule** *(dict) --*

      The "Schedule" when the trigger is initiated.

      - **expression** *(string) --*

        The expression that defines when to trigger an update. For more information, see `Schedule
        Expressions for Rules
        <https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html>`__ in the
        Amazon CloudWatch Events User Guide.

    - **dataset** *(dict) --*

      The data set whose content creation triggers the creation of this data set's contents.

      - **name** *(string) --* **[REQUIRED]**

        The name of the data set whose content generation triggers the new data set content
        generation.
    """


_RequiredClientUpdateDatastoredatastoreStoragecustomerManagedS3TypeDef = TypedDict(
    "_RequiredClientUpdateDatastoredatastoreStoragecustomerManagedS3TypeDef",
    {"bucket": str, "roleArn": str},
)
_OptionalClientUpdateDatastoredatastoreStoragecustomerManagedS3TypeDef = TypedDict(
    "_OptionalClientUpdateDatastoredatastoreStoragecustomerManagedS3TypeDef",
    {"keyPrefix": str},
    total=False,
)


class ClientUpdateDatastoredatastoreStoragecustomerManagedS3TypeDef(
    _RequiredClientUpdateDatastoredatastoreStoragecustomerManagedS3TypeDef,
    _OptionalClientUpdateDatastoredatastoreStoragecustomerManagedS3TypeDef,
):
    """
    Type definition for `ClientUpdateDatastoredatastoreStorage` `customerManagedS3`

    Use this to store data store data in an S3 bucket that you manage. When customer managed
    storage is selected, the "retentionPeriod" parameter is ignored. The choice of service-managed
    or customer-managed S3 storage cannot be changed after creation of the data store.

    - **bucket** *(string) --* **[REQUIRED]**

      The name of the Amazon S3 bucket in which data store data is stored.

    - **keyPrefix** *(string) --*

      [Optional] The prefix used to create the keys of the data store data objects. Each object in
      an Amazon S3 bucket has a key that is its unique identifier within the bucket (each object in
      a bucket has exactly one key). The prefix must end with a '/'.

    - **roleArn** *(string) --* **[REQUIRED]**

      The ARN of the role which grants AWS IoT Analytics permission to interact with your Amazon S3
      resources.
    """


_ClientUpdateDatastoredatastoreStorageTypeDef = TypedDict(
    "_ClientUpdateDatastoredatastoreStorageTypeDef",
    {
        "serviceManagedS3": Dict,
        "customerManagedS3": ClientUpdateDatastoredatastoreStoragecustomerManagedS3TypeDef,
    },
    total=False,
)


class ClientUpdateDatastoredatastoreStorageTypeDef(
    _ClientUpdateDatastoredatastoreStorageTypeDef
):
    """
    Type definition for `ClientUpdateDatastore` `datastoreStorage`

    Where data store data is stored. You may choose one of "serviceManagedS3" or "customerManagedS3"
    storage. If not specified, the default is "serviceManagedS3". This cannot be changed after the
    data store is created.

    - **serviceManagedS3** *(dict) --*

      Use this to store data store data in an S3 bucket managed by the AWS IoT Analytics service. The
      choice of service-managed or customer-managed S3 storage cannot be changed after creation of
      the data store.

    - **customerManagedS3** *(dict) --*

      Use this to store data store data in an S3 bucket that you manage. When customer managed
      storage is selected, the "retentionPeriod" parameter is ignored. The choice of service-managed
      or customer-managed S3 storage cannot be changed after creation of the data store.

      - **bucket** *(string) --* **[REQUIRED]**

        The name of the Amazon S3 bucket in which data store data is stored.

      - **keyPrefix** *(string) --*

        [Optional] The prefix used to create the keys of the data store data objects. Each object in
        an Amazon S3 bucket has a key that is its unique identifier within the bucket (each object in
        a bucket has exactly one key). The prefix must end with a '/'.

      - **roleArn** *(string) --* **[REQUIRED]**

        The ARN of the role which grants AWS IoT Analytics permission to interact with your Amazon S3
        resources.
    """


_ClientUpdateDatastoreretentionPeriodTypeDef = TypedDict(
    "_ClientUpdateDatastoreretentionPeriodTypeDef",
    {"unlimited": bool, "numberOfDays": int},
    total=False,
)


class ClientUpdateDatastoreretentionPeriodTypeDef(
    _ClientUpdateDatastoreretentionPeriodTypeDef
):
    """
    Type definition for `ClientUpdateDatastore` `retentionPeriod`

    How long, in days, message data is kept for the data store. The retention period cannot be
    updated if the data store's S3 storage is customer-managed.

    - **unlimited** *(boolean) --*

      If true, message data is kept indefinitely.

    - **numberOfDays** *(integer) --*

      The number of days that message data is kept. The "unlimited" parameter must be false.
    """


_RequiredClientUpdatePipelinepipelineActivitiesaddAttributesTypeDef = TypedDict(
    "_RequiredClientUpdatePipelinepipelineActivitiesaddAttributesTypeDef",
    {"name": str, "attributes": Dict[str, str]},
)
_OptionalClientUpdatePipelinepipelineActivitiesaddAttributesTypeDef = TypedDict(
    "_OptionalClientUpdatePipelinepipelineActivitiesaddAttributesTypeDef",
    {"next": str},
    total=False,
)


class ClientUpdatePipelinepipelineActivitiesaddAttributesTypeDef(
    _RequiredClientUpdatePipelinepipelineActivitiesaddAttributesTypeDef,
    _OptionalClientUpdatePipelinepipelineActivitiesaddAttributesTypeDef,
):
    """
    Type definition for `ClientUpdatePipelinepipelineActivities` `addAttributes`

    Adds other attributes based on existing attributes in the message.

    - **name** *(string) --* **[REQUIRED]**

      The name of the 'addAttributes' activity.

    - **attributes** *(dict) --* **[REQUIRED]**

      A list of 1-50 "AttributeNameMapping" objects that map an existing attribute to a new
      attribute.

      .. note::

        The existing attributes remain in the message, so if you want to remove the originals,
        use "RemoveAttributeActivity".

      - *(string) --*

        - *(string) --*

    - **next** *(string) --*

      The next activity in the pipeline.
    """


_RequiredClientUpdatePipelinepipelineActivitieschannelTypeDef = TypedDict(
    "_RequiredClientUpdatePipelinepipelineActivitieschannelTypeDef",
    {"name": str, "channelName": str},
)
_OptionalClientUpdatePipelinepipelineActivitieschannelTypeDef = TypedDict(
    "_OptionalClientUpdatePipelinepipelineActivitieschannelTypeDef",
    {"next": str},
    total=False,
)


class ClientUpdatePipelinepipelineActivitieschannelTypeDef(
    _RequiredClientUpdatePipelinepipelineActivitieschannelTypeDef,
    _OptionalClientUpdatePipelinepipelineActivitieschannelTypeDef,
):
    """
    Type definition for `ClientUpdatePipelinepipelineActivities` `channel`

    Determines the source of the messages to be processed.

    - **name** *(string) --* **[REQUIRED]**

      The name of the 'channel' activity.

    - **channelName** *(string) --* **[REQUIRED]**

      The name of the channel from which the messages are processed.

    - **next** *(string) --*

      The next activity in the pipeline.
    """


_ClientUpdatePipelinepipelineActivitiesdatastoreTypeDef = TypedDict(
    "_ClientUpdatePipelinepipelineActivitiesdatastoreTypeDef",
    {"name": str, "datastoreName": str},
)


class ClientUpdatePipelinepipelineActivitiesdatastoreTypeDef(
    _ClientUpdatePipelinepipelineActivitiesdatastoreTypeDef
):
    """
    Type definition for `ClientUpdatePipelinepipelineActivities` `datastore`

    Specifies where to store the processed message data.

    - **name** *(string) --* **[REQUIRED]**

      The name of the 'datastore' activity.

    - **datastoreName** *(string) --* **[REQUIRED]**

      The name of the data store where processed messages are stored.
    """


_RequiredClientUpdatePipelinepipelineActivitiesdeviceRegistryEnrichTypeDef = TypedDict(
    "_RequiredClientUpdatePipelinepipelineActivitiesdeviceRegistryEnrichTypeDef",
    {"name": str, "attribute": str, "thingName": str, "roleArn": str},
)
_OptionalClientUpdatePipelinepipelineActivitiesdeviceRegistryEnrichTypeDef = TypedDict(
    "_OptionalClientUpdatePipelinepipelineActivitiesdeviceRegistryEnrichTypeDef",
    {"next": str},
    total=False,
)


class ClientUpdatePipelinepipelineActivitiesdeviceRegistryEnrichTypeDef(
    _RequiredClientUpdatePipelinepipelineActivitiesdeviceRegistryEnrichTypeDef,
    _OptionalClientUpdatePipelinepipelineActivitiesdeviceRegistryEnrichTypeDef,
):
    """
    Type definition for `ClientUpdatePipelinepipelineActivities` `deviceRegistryEnrich`

    Adds data from the AWS IoT device registry to your message.

    - **name** *(string) --* **[REQUIRED]**

      The name of the 'deviceRegistryEnrich' activity.

    - **attribute** *(string) --* **[REQUIRED]**

      The name of the attribute that is added to the message.

    - **thingName** *(string) --* **[REQUIRED]**

      The name of the IoT device whose registry information is added to the message.

    - **roleArn** *(string) --* **[REQUIRED]**

      The ARN of the role that allows access to the device's registry information.

    - **next** *(string) --*

      The next activity in the pipeline.
    """


_RequiredClientUpdatePipelinepipelineActivitiesdeviceShadowEnrichTypeDef = TypedDict(
    "_RequiredClientUpdatePipelinepipelineActivitiesdeviceShadowEnrichTypeDef",
    {"name": str, "attribute": str, "thingName": str, "roleArn": str},
)
_OptionalClientUpdatePipelinepipelineActivitiesdeviceShadowEnrichTypeDef = TypedDict(
    "_OptionalClientUpdatePipelinepipelineActivitiesdeviceShadowEnrichTypeDef",
    {"next": str},
    total=False,
)


class ClientUpdatePipelinepipelineActivitiesdeviceShadowEnrichTypeDef(
    _RequiredClientUpdatePipelinepipelineActivitiesdeviceShadowEnrichTypeDef,
    _OptionalClientUpdatePipelinepipelineActivitiesdeviceShadowEnrichTypeDef,
):
    """
    Type definition for `ClientUpdatePipelinepipelineActivities` `deviceShadowEnrich`

    Adds information from the AWS IoT Device Shadows service to a message.

    - **name** *(string) --* **[REQUIRED]**

      The name of the 'deviceShadowEnrich' activity.

    - **attribute** *(string) --* **[REQUIRED]**

      The name of the attribute that is added to the message.

    - **thingName** *(string) --* **[REQUIRED]**

      The name of the IoT device whose shadow information is added to the message.

    - **roleArn** *(string) --* **[REQUIRED]**

      The ARN of the role that allows access to the device's shadow.

    - **next** *(string) --*

      The next activity in the pipeline.
    """


_RequiredClientUpdatePipelinepipelineActivitiesfilterTypeDef = TypedDict(
    "_RequiredClientUpdatePipelinepipelineActivitiesfilterTypeDef",
    {"name": str, "filter": str},
)
_OptionalClientUpdatePipelinepipelineActivitiesfilterTypeDef = TypedDict(
    "_OptionalClientUpdatePipelinepipelineActivitiesfilterTypeDef",
    {"next": str},
    total=False,
)


class ClientUpdatePipelinepipelineActivitiesfilterTypeDef(
    _RequiredClientUpdatePipelinepipelineActivitiesfilterTypeDef,
    _OptionalClientUpdatePipelinepipelineActivitiesfilterTypeDef,
):
    """
    Type definition for `ClientUpdatePipelinepipelineActivities` `filter`

    Filters a message based on its attributes.

    - **name** *(string) --* **[REQUIRED]**

      The name of the 'filter' activity.

    - **filter** *(string) --* **[REQUIRED]**

      An expression that looks like a SQL WHERE clause that must return a Boolean value.

    - **next** *(string) --*

      The next activity in the pipeline.
    """


_RequiredClientUpdatePipelinepipelineActivitieslambdaTypeDef = TypedDict(
    "_RequiredClientUpdatePipelinepipelineActivitieslambdaTypeDef",
    {"name": str, "lambdaName": str, "batchSize": int},
)
_OptionalClientUpdatePipelinepipelineActivitieslambdaTypeDef = TypedDict(
    "_OptionalClientUpdatePipelinepipelineActivitieslambdaTypeDef",
    {"next": str},
    total=False,
)


class ClientUpdatePipelinepipelineActivitieslambdaTypeDef(
    _RequiredClientUpdatePipelinepipelineActivitieslambdaTypeDef,
    _OptionalClientUpdatePipelinepipelineActivitieslambdaTypeDef,
):
    """
    Type definition for `ClientUpdatePipelinepipelineActivities` `lambda`

    Runs a Lambda function to modify the message.

    - **name** *(string) --* **[REQUIRED]**

      The name of the 'lambda' activity.

    - **lambdaName** *(string) --* **[REQUIRED]**

      The name of the Lambda function that is run on the message.

    - **batchSize** *(integer) --* **[REQUIRED]**

      The number of messages passed to the Lambda function for processing.

      The AWS Lambda function must be able to process all of these messages within five minutes,
      which is the maximum timeout duration for Lambda functions.

    - **next** *(string) --*

      The next activity in the pipeline.
    """


_RequiredClientUpdatePipelinepipelineActivitiesmathTypeDef = TypedDict(
    "_RequiredClientUpdatePipelinepipelineActivitiesmathTypeDef",
    {"name": str, "attribute": str, "math": str},
)
_OptionalClientUpdatePipelinepipelineActivitiesmathTypeDef = TypedDict(
    "_OptionalClientUpdatePipelinepipelineActivitiesmathTypeDef",
    {"next": str},
    total=False,
)


class ClientUpdatePipelinepipelineActivitiesmathTypeDef(
    _RequiredClientUpdatePipelinepipelineActivitiesmathTypeDef,
    _OptionalClientUpdatePipelinepipelineActivitiesmathTypeDef,
):
    """
    Type definition for `ClientUpdatePipelinepipelineActivities` `math`

    Computes an arithmetic expression using the message's attributes and adds it to the message.

    - **name** *(string) --* **[REQUIRED]**

      The name of the 'math' activity.

    - **attribute** *(string) --* **[REQUIRED]**

      The name of the attribute that contains the result of the math operation.

    - **math** *(string) --* **[REQUIRED]**

      An expression that uses one or more existing attributes and must return an integer value.

    - **next** *(string) --*

      The next activity in the pipeline.
    """


_RequiredClientUpdatePipelinepipelineActivitiesremoveAttributesTypeDef = TypedDict(
    "_RequiredClientUpdatePipelinepipelineActivitiesremoveAttributesTypeDef",
    {"name": str, "attributes": List[str]},
)
_OptionalClientUpdatePipelinepipelineActivitiesremoveAttributesTypeDef = TypedDict(
    "_OptionalClientUpdatePipelinepipelineActivitiesremoveAttributesTypeDef",
    {"next": str},
    total=False,
)


class ClientUpdatePipelinepipelineActivitiesremoveAttributesTypeDef(
    _RequiredClientUpdatePipelinepipelineActivitiesremoveAttributesTypeDef,
    _OptionalClientUpdatePipelinepipelineActivitiesremoveAttributesTypeDef,
):
    """
    Type definition for `ClientUpdatePipelinepipelineActivities` `removeAttributes`

    Removes attributes from a message.

    - **name** *(string) --* **[REQUIRED]**

      The name of the 'removeAttributes' activity.

    - **attributes** *(list) --* **[REQUIRED]**

      A list of 1-50 attributes to remove from the message.

      - *(string) --*

    - **next** *(string) --*

      The next activity in the pipeline.
    """


_RequiredClientUpdatePipelinepipelineActivitiesselectAttributesTypeDef = TypedDict(
    "_RequiredClientUpdatePipelinepipelineActivitiesselectAttributesTypeDef",
    {"name": str, "attributes": List[str]},
)
_OptionalClientUpdatePipelinepipelineActivitiesselectAttributesTypeDef = TypedDict(
    "_OptionalClientUpdatePipelinepipelineActivitiesselectAttributesTypeDef",
    {"next": str},
    total=False,
)


class ClientUpdatePipelinepipelineActivitiesselectAttributesTypeDef(
    _RequiredClientUpdatePipelinepipelineActivitiesselectAttributesTypeDef,
    _OptionalClientUpdatePipelinepipelineActivitiesselectAttributesTypeDef,
):
    """
    Type definition for `ClientUpdatePipelinepipelineActivities` `selectAttributes`

    Creates a new message using only the specified attributes from the original message.

    - **name** *(string) --* **[REQUIRED]**

      The name of the 'selectAttributes' activity.

    - **attributes** *(list) --* **[REQUIRED]**

      A list of the attributes to select from the message.

      - *(string) --*

    - **next** *(string) --*

      The next activity in the pipeline.
    """


_ClientUpdatePipelinepipelineActivitiesTypeDef = TypedDict(
    "_ClientUpdatePipelinepipelineActivitiesTypeDef",
    {
        "channel": ClientUpdatePipelinepipelineActivitieschannelTypeDef,
        "lambda": ClientUpdatePipelinepipelineActivitieslambdaTypeDef,
        "datastore": ClientUpdatePipelinepipelineActivitiesdatastoreTypeDef,
        "addAttributes": ClientUpdatePipelinepipelineActivitiesaddAttributesTypeDef,
        "removeAttributes": ClientUpdatePipelinepipelineActivitiesremoveAttributesTypeDef,
        "selectAttributes": ClientUpdatePipelinepipelineActivitiesselectAttributesTypeDef,
        "filter": ClientUpdatePipelinepipelineActivitiesfilterTypeDef,
        "math": ClientUpdatePipelinepipelineActivitiesmathTypeDef,
        "deviceRegistryEnrich": ClientUpdatePipelinepipelineActivitiesdeviceRegistryEnrichTypeDef,
        "deviceShadowEnrich": ClientUpdatePipelinepipelineActivitiesdeviceShadowEnrichTypeDef,
    },
    total=False,
)


class ClientUpdatePipelinepipelineActivitiesTypeDef(
    _ClientUpdatePipelinepipelineActivitiesTypeDef
):
    """
    Type definition for `ClientUpdatePipeline` `pipelineActivities`

    An activity that performs a transformation on a message.

    - **channel** *(dict) --*

      Determines the source of the messages to be processed.

      - **name** *(string) --* **[REQUIRED]**

        The name of the 'channel' activity.

      - **channelName** *(string) --* **[REQUIRED]**

        The name of the channel from which the messages are processed.

      - **next** *(string) --*

        The next activity in the pipeline.

    - **lambda** *(dict) --*

      Runs a Lambda function to modify the message.

      - **name** *(string) --* **[REQUIRED]**

        The name of the 'lambda' activity.

      - **lambdaName** *(string) --* **[REQUIRED]**

        The name of the Lambda function that is run on the message.

      - **batchSize** *(integer) --* **[REQUIRED]**

        The number of messages passed to the Lambda function for processing.

        The AWS Lambda function must be able to process all of these messages within five minutes,
        which is the maximum timeout duration for Lambda functions.

      - **next** *(string) --*

        The next activity in the pipeline.

    - **datastore** *(dict) --*

      Specifies where to store the processed message data.

      - **name** *(string) --* **[REQUIRED]**

        The name of the 'datastore' activity.

      - **datastoreName** *(string) --* **[REQUIRED]**

        The name of the data store where processed messages are stored.

    - **addAttributes** *(dict) --*

      Adds other attributes based on existing attributes in the message.

      - **name** *(string) --* **[REQUIRED]**

        The name of the 'addAttributes' activity.

      - **attributes** *(dict) --* **[REQUIRED]**

        A list of 1-50 "AttributeNameMapping" objects that map an existing attribute to a new
        attribute.

        .. note::

          The existing attributes remain in the message, so if you want to remove the originals,
          use "RemoveAttributeActivity".

        - *(string) --*

          - *(string) --*

      - **next** *(string) --*

        The next activity in the pipeline.

    - **removeAttributes** *(dict) --*

      Removes attributes from a message.

      - **name** *(string) --* **[REQUIRED]**

        The name of the 'removeAttributes' activity.

      - **attributes** *(list) --* **[REQUIRED]**

        A list of 1-50 attributes to remove from the message.

        - *(string) --*

      - **next** *(string) --*

        The next activity in the pipeline.

    - **selectAttributes** *(dict) --*

      Creates a new message using only the specified attributes from the original message.

      - **name** *(string) --* **[REQUIRED]**

        The name of the 'selectAttributes' activity.

      - **attributes** *(list) --* **[REQUIRED]**

        A list of the attributes to select from the message.

        - *(string) --*

      - **next** *(string) --*

        The next activity in the pipeline.

    - **filter** *(dict) --*

      Filters a message based on its attributes.

      - **name** *(string) --* **[REQUIRED]**

        The name of the 'filter' activity.

      - **filter** *(string) --* **[REQUIRED]**

        An expression that looks like a SQL WHERE clause that must return a Boolean value.

      - **next** *(string) --*

        The next activity in the pipeline.

    - **math** *(dict) --*

      Computes an arithmetic expression using the message's attributes and adds it to the message.

      - **name** *(string) --* **[REQUIRED]**

        The name of the 'math' activity.

      - **attribute** *(string) --* **[REQUIRED]**

        The name of the attribute that contains the result of the math operation.

      - **math** *(string) --* **[REQUIRED]**

        An expression that uses one or more existing attributes and must return an integer value.

      - **next** *(string) --*

        The next activity in the pipeline.

    - **deviceRegistryEnrich** *(dict) --*

      Adds data from the AWS IoT device registry to your message.

      - **name** *(string) --* **[REQUIRED]**

        The name of the 'deviceRegistryEnrich' activity.

      - **attribute** *(string) --* **[REQUIRED]**

        The name of the attribute that is added to the message.

      - **thingName** *(string) --* **[REQUIRED]**

        The name of the IoT device whose registry information is added to the message.

      - **roleArn** *(string) --* **[REQUIRED]**

        The ARN of the role that allows access to the device's registry information.

      - **next** *(string) --*

        The next activity in the pipeline.

    - **deviceShadowEnrich** *(dict) --*

      Adds information from the AWS IoT Device Shadows service to a message.

      - **name** *(string) --* **[REQUIRED]**

        The name of the 'deviceShadowEnrich' activity.

      - **attribute** *(string) --* **[REQUIRED]**

        The name of the attribute that is added to the message.

      - **thingName** *(string) --* **[REQUIRED]**

        The name of the IoT device whose shadow information is added to the message.

      - **roleArn** *(string) --* **[REQUIRED]**

        The ARN of the role that allows access to the device's shadow.

      - **next** *(string) --*

        The next activity in the pipeline.
    """


_ListChannelsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListChannelsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListChannelsPaginatePaginationConfigTypeDef(
    _ListChannelsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListChannelsPaginate` `PaginationConfig`

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


_ListChannelsPaginateResponsechannelSummarieschannelStoragecustomerManagedS3TypeDef = TypedDict(
    "_ListChannelsPaginateResponsechannelSummarieschannelStoragecustomerManagedS3TypeDef",
    {"bucket": str, "keyPrefix": str, "roleArn": str},
    total=False,
)


class ListChannelsPaginateResponsechannelSummarieschannelStoragecustomerManagedS3TypeDef(
    _ListChannelsPaginateResponsechannelSummarieschannelStoragecustomerManagedS3TypeDef
):
    """
    Type definition for `ListChannelsPaginateResponsechannelSummarieschannelStorage` `customerManagedS3`

    Used to store channel data in an S3 bucket that you manage.

    - **bucket** *(string) --*

      The name of the Amazon S3 bucket in which channel data is stored.

    - **keyPrefix** *(string) --*

      [Optional] The prefix used to create the keys of the channel data objects. Each
      object in an Amazon S3 bucket has a key that is its unique identifier within the
      bucket (each object in a bucket has exactly one key). The prefix must end with a '/'.

    - **roleArn** *(string) --*

      The ARN of the role which grants AWS IoT Analytics permission to interact with your
      Amazon S3 resources.
    """


_ListChannelsPaginateResponsechannelSummarieschannelStorageTypeDef = TypedDict(
    "_ListChannelsPaginateResponsechannelSummarieschannelStorageTypeDef",
    {
        "serviceManagedS3": Dict,
        "customerManagedS3": ListChannelsPaginateResponsechannelSummarieschannelStoragecustomerManagedS3TypeDef,
    },
    total=False,
)


class ListChannelsPaginateResponsechannelSummarieschannelStorageTypeDef(
    _ListChannelsPaginateResponsechannelSummarieschannelStorageTypeDef
):
    """
    Type definition for `ListChannelsPaginateResponsechannelSummaries` `channelStorage`

    Where channel data is stored.

    - **serviceManagedS3** *(dict) --*

      Used to store channel data in an S3 bucket managed by the AWS IoT Analytics service.

    - **customerManagedS3** *(dict) --*

      Used to store channel data in an S3 bucket that you manage.

      - **bucket** *(string) --*

        The name of the Amazon S3 bucket in which channel data is stored.

      - **keyPrefix** *(string) --*

        [Optional] The prefix used to create the keys of the channel data objects. Each
        object in an Amazon S3 bucket has a key that is its unique identifier within the
        bucket (each object in a bucket has exactly one key). The prefix must end with a '/'.

      - **roleArn** *(string) --*

        The ARN of the role which grants AWS IoT Analytics permission to interact with your
        Amazon S3 resources.
    """


_ListChannelsPaginateResponsechannelSummariesTypeDef = TypedDict(
    "_ListChannelsPaginateResponsechannelSummariesTypeDef",
    {
        "channelName": str,
        "channelStorage": ListChannelsPaginateResponsechannelSummarieschannelStorageTypeDef,
        "status": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
    },
    total=False,
)


class ListChannelsPaginateResponsechannelSummariesTypeDef(
    _ListChannelsPaginateResponsechannelSummariesTypeDef
):
    """
    Type definition for `ListChannelsPaginateResponse` `channelSummaries`

    A summary of information about a channel.

    - **channelName** *(string) --*

      The name of the channel.

    - **channelStorage** *(dict) --*

      Where channel data is stored.

      - **serviceManagedS3** *(dict) --*

        Used to store channel data in an S3 bucket managed by the AWS IoT Analytics service.

      - **customerManagedS3** *(dict) --*

        Used to store channel data in an S3 bucket that you manage.

        - **bucket** *(string) --*

          The name of the Amazon S3 bucket in which channel data is stored.

        - **keyPrefix** *(string) --*

          [Optional] The prefix used to create the keys of the channel data objects. Each
          object in an Amazon S3 bucket has a key that is its unique identifier within the
          bucket (each object in a bucket has exactly one key). The prefix must end with a '/'.

        - **roleArn** *(string) --*

          The ARN of the role which grants AWS IoT Analytics permission to interact with your
          Amazon S3 resources.

    - **status** *(string) --*

      The status of the channel.

    - **creationTime** *(datetime) --*

      When the channel was created.

    - **lastUpdateTime** *(datetime) --*

      The last time the channel was updated.
    """


_ListChannelsPaginateResponseTypeDef = TypedDict(
    "_ListChannelsPaginateResponseTypeDef",
    {
        "channelSummaries": List[ListChannelsPaginateResponsechannelSummariesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListChannelsPaginateResponseTypeDef(_ListChannelsPaginateResponseTypeDef):
    """
    Type definition for `ListChannelsPaginate` `Response`

    - **channelSummaries** *(list) --*

      A list of "ChannelSummary" objects.

      - *(dict) --*

        A summary of information about a channel.

        - **channelName** *(string) --*

          The name of the channel.

        - **channelStorage** *(dict) --*

          Where channel data is stored.

          - **serviceManagedS3** *(dict) --*

            Used to store channel data in an S3 bucket managed by the AWS IoT Analytics service.

          - **customerManagedS3** *(dict) --*

            Used to store channel data in an S3 bucket that you manage.

            - **bucket** *(string) --*

              The name of the Amazon S3 bucket in which channel data is stored.

            - **keyPrefix** *(string) --*

              [Optional] The prefix used to create the keys of the channel data objects. Each
              object in an Amazon S3 bucket has a key that is its unique identifier within the
              bucket (each object in a bucket has exactly one key). The prefix must end with a '/'.

            - **roleArn** *(string) --*

              The ARN of the role which grants AWS IoT Analytics permission to interact with your
              Amazon S3 resources.

        - **status** *(string) --*

          The status of the channel.

        - **creationTime** *(datetime) --*

          When the channel was created.

        - **lastUpdateTime** *(datetime) --*

          The last time the channel was updated.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListDatasetContentsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListDatasetContentsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListDatasetContentsPaginatePaginationConfigTypeDef(
    _ListDatasetContentsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListDatasetContentsPaginate` `PaginationConfig`

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


_ListDatasetContentsPaginateResponsedatasetContentSummariesstatusTypeDef = TypedDict(
    "_ListDatasetContentsPaginateResponsedatasetContentSummariesstatusTypeDef",
    {"state": str, "reason": str},
    total=False,
)


class ListDatasetContentsPaginateResponsedatasetContentSummariesstatusTypeDef(
    _ListDatasetContentsPaginateResponsedatasetContentSummariesstatusTypeDef
):
    """
    Type definition for `ListDatasetContentsPaginateResponsedatasetContentSummaries` `status`

    The status of the data set contents.

    - **state** *(string) --*

      The state of the data set contents. Can be one of "READY", "CREATING", "SUCCEEDED" or
      "FAILED".

    - **reason** *(string) --*

      The reason the data set contents are in this state.
    """


_ListDatasetContentsPaginateResponsedatasetContentSummariesTypeDef = TypedDict(
    "_ListDatasetContentsPaginateResponsedatasetContentSummariesTypeDef",
    {
        "version": str,
        "status": ListDatasetContentsPaginateResponsedatasetContentSummariesstatusTypeDef,
        "creationTime": datetime,
        "scheduleTime": datetime,
        "completionTime": datetime,
    },
    total=False,
)


class ListDatasetContentsPaginateResponsedatasetContentSummariesTypeDef(
    _ListDatasetContentsPaginateResponsedatasetContentSummariesTypeDef
):
    """
    Type definition for `ListDatasetContentsPaginateResponse` `datasetContentSummaries`

    Summary information about data set contents.

    - **version** *(string) --*

      The version of the data set contents.

    - **status** *(dict) --*

      The status of the data set contents.

      - **state** *(string) --*

        The state of the data set contents. Can be one of "READY", "CREATING", "SUCCEEDED" or
        "FAILED".

      - **reason** *(string) --*

        The reason the data set contents are in this state.

    - **creationTime** *(datetime) --*

      The actual time the creation of the data set contents was started.

    - **scheduleTime** *(datetime) --*

      The time the creation of the data set contents was scheduled to start.

    - **completionTime** *(datetime) --*

      The time the dataset content status was updated to SUCCEEDED or FAILED.
    """


_ListDatasetContentsPaginateResponseTypeDef = TypedDict(
    "_ListDatasetContentsPaginateResponseTypeDef",
    {
        "datasetContentSummaries": List[
            ListDatasetContentsPaginateResponsedatasetContentSummariesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ListDatasetContentsPaginateResponseTypeDef(
    _ListDatasetContentsPaginateResponseTypeDef
):
    """
    Type definition for `ListDatasetContentsPaginate` `Response`

    - **datasetContentSummaries** *(list) --*

      Summary information about data set contents that have been created.

      - *(dict) --*

        Summary information about data set contents.

        - **version** *(string) --*

          The version of the data set contents.

        - **status** *(dict) --*

          The status of the data set contents.

          - **state** *(string) --*

            The state of the data set contents. Can be one of "READY", "CREATING", "SUCCEEDED" or
            "FAILED".

          - **reason** *(string) --*

            The reason the data set contents are in this state.

        - **creationTime** *(datetime) --*

          The actual time the creation of the data set contents was started.

        - **scheduleTime** *(datetime) --*

          The time the creation of the data set contents was scheduled to start.

        - **completionTime** *(datetime) --*

          The time the dataset content status was updated to SUCCEEDED or FAILED.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListDatasetsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListDatasetsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListDatasetsPaginatePaginationConfigTypeDef(
    _ListDatasetsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListDatasetsPaginate` `PaginationConfig`

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


_ListDatasetsPaginateResponsedatasetSummariesactionsTypeDef = TypedDict(
    "_ListDatasetsPaginateResponsedatasetSummariesactionsTypeDef",
    {"actionName": str, "actionType": str},
    total=False,
)


class ListDatasetsPaginateResponsedatasetSummariesactionsTypeDef(
    _ListDatasetsPaginateResponsedatasetSummariesactionsTypeDef
):
    """
    Type definition for `ListDatasetsPaginateResponsedatasetSummaries` `actions`

    Information about the action which automatically creates the data set's contents.

    - **actionName** *(string) --*

      The name of the action which automatically creates the data set's contents.

    - **actionType** *(string) --*

      The type of action by which the data set's contents are automatically created.
    """


_ListDatasetsPaginateResponsedatasetSummariestriggersdatasetTypeDef = TypedDict(
    "_ListDatasetsPaginateResponsedatasetSummariestriggersdatasetTypeDef",
    {"name": str},
    total=False,
)


class ListDatasetsPaginateResponsedatasetSummariestriggersdatasetTypeDef(
    _ListDatasetsPaginateResponsedatasetSummariestriggersdatasetTypeDef
):
    """
    Type definition for `ListDatasetsPaginateResponsedatasetSummariestriggers` `dataset`

    The data set whose content creation triggers the creation of this data set's contents.

    - **name** *(string) --*

      The name of the data set whose content generation triggers the new data set content
      generation.
    """


_ListDatasetsPaginateResponsedatasetSummariestriggersscheduleTypeDef = TypedDict(
    "_ListDatasetsPaginateResponsedatasetSummariestriggersscheduleTypeDef",
    {"expression": str},
    total=False,
)


class ListDatasetsPaginateResponsedatasetSummariestriggersscheduleTypeDef(
    _ListDatasetsPaginateResponsedatasetSummariestriggersscheduleTypeDef
):
    """
    Type definition for `ListDatasetsPaginateResponsedatasetSummariestriggers` `schedule`

    The "Schedule" when the trigger is initiated.

    - **expression** *(string) --*

      The expression that defines when to trigger an update. For more information, see
      `Schedule Expressions for Rules
      <https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html>`__
      in the Amazon CloudWatch Events User Guide.
    """


_ListDatasetsPaginateResponsedatasetSummariestriggersTypeDef = TypedDict(
    "_ListDatasetsPaginateResponsedatasetSummariestriggersTypeDef",
    {
        "schedule": ListDatasetsPaginateResponsedatasetSummariestriggersscheduleTypeDef,
        "dataset": ListDatasetsPaginateResponsedatasetSummariestriggersdatasetTypeDef,
    },
    total=False,
)


class ListDatasetsPaginateResponsedatasetSummariestriggersTypeDef(
    _ListDatasetsPaginateResponsedatasetSummariestriggersTypeDef
):
    """
    Type definition for `ListDatasetsPaginateResponsedatasetSummaries` `triggers`

    The "DatasetTrigger" that specifies when the data set is automatically updated.

    - **schedule** *(dict) --*

      The "Schedule" when the trigger is initiated.

      - **expression** *(string) --*

        The expression that defines when to trigger an update. For more information, see
        `Schedule Expressions for Rules
        <https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html>`__
        in the Amazon CloudWatch Events User Guide.

    - **dataset** *(dict) --*

      The data set whose content creation triggers the creation of this data set's contents.

      - **name** *(string) --*

        The name of the data set whose content generation triggers the new data set content
        generation.
    """


_ListDatasetsPaginateResponsedatasetSummariesTypeDef = TypedDict(
    "_ListDatasetsPaginateResponsedatasetSummariesTypeDef",
    {
        "datasetName": str,
        "status": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "triggers": List[ListDatasetsPaginateResponsedatasetSummariestriggersTypeDef],
        "actions": List[ListDatasetsPaginateResponsedatasetSummariesactionsTypeDef],
    },
    total=False,
)


class ListDatasetsPaginateResponsedatasetSummariesTypeDef(
    _ListDatasetsPaginateResponsedatasetSummariesTypeDef
):
    """
    Type definition for `ListDatasetsPaginateResponse` `datasetSummaries`

    A summary of information about a data set.

    - **datasetName** *(string) --*

      The name of the data set.

    - **status** *(string) --*

      The status of the data set.

    - **creationTime** *(datetime) --*

      The time the data set was created.

    - **lastUpdateTime** *(datetime) --*

      The last time the data set was updated.

    - **triggers** *(list) --*

      A list of triggers. A trigger causes data set content to be populated at a specified time
      interval or when another data set is populated. The list of triggers can be empty or
      contain up to five DataSetTrigger objects

      - *(dict) --*

        The "DatasetTrigger" that specifies when the data set is automatically updated.

        - **schedule** *(dict) --*

          The "Schedule" when the trigger is initiated.

          - **expression** *(string) --*

            The expression that defines when to trigger an update. For more information, see
            `Schedule Expressions for Rules
            <https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html>`__
            in the Amazon CloudWatch Events User Guide.

        - **dataset** *(dict) --*

          The data set whose content creation triggers the creation of this data set's contents.

          - **name** *(string) --*

            The name of the data set whose content generation triggers the new data set content
            generation.

    - **actions** *(list) --*

      A list of "DataActionSummary" objects.

      - *(dict) --*

        Information about the action which automatically creates the data set's contents.

        - **actionName** *(string) --*

          The name of the action which automatically creates the data set's contents.

        - **actionType** *(string) --*

          The type of action by which the data set's contents are automatically created.
    """


_ListDatasetsPaginateResponseTypeDef = TypedDict(
    "_ListDatasetsPaginateResponseTypeDef",
    {
        "datasetSummaries": List[ListDatasetsPaginateResponsedatasetSummariesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListDatasetsPaginateResponseTypeDef(_ListDatasetsPaginateResponseTypeDef):
    """
    Type definition for `ListDatasetsPaginate` `Response`

    - **datasetSummaries** *(list) --*

      A list of "DatasetSummary" objects.

      - *(dict) --*

        A summary of information about a data set.

        - **datasetName** *(string) --*

          The name of the data set.

        - **status** *(string) --*

          The status of the data set.

        - **creationTime** *(datetime) --*

          The time the data set was created.

        - **lastUpdateTime** *(datetime) --*

          The last time the data set was updated.

        - **triggers** *(list) --*

          A list of triggers. A trigger causes data set content to be populated at a specified time
          interval or when another data set is populated. The list of triggers can be empty or
          contain up to five DataSetTrigger objects

          - *(dict) --*

            The "DatasetTrigger" that specifies when the data set is automatically updated.

            - **schedule** *(dict) --*

              The "Schedule" when the trigger is initiated.

              - **expression** *(string) --*

                The expression that defines when to trigger an update. For more information, see
                `Schedule Expressions for Rules
                <https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html>`__
                in the Amazon CloudWatch Events User Guide.

            - **dataset** *(dict) --*

              The data set whose content creation triggers the creation of this data set's contents.

              - **name** *(string) --*

                The name of the data set whose content generation triggers the new data set content
                generation.

        - **actions** *(list) --*

          A list of "DataActionSummary" objects.

          - *(dict) --*

            Information about the action which automatically creates the data set's contents.

            - **actionName** *(string) --*

              The name of the action which automatically creates the data set's contents.

            - **actionType** *(string) --*

              The type of action by which the data set's contents are automatically created.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListDatastoresPaginatePaginationConfigTypeDef = TypedDict(
    "_ListDatastoresPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListDatastoresPaginatePaginationConfigTypeDef(
    _ListDatastoresPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListDatastoresPaginate` `PaginationConfig`

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


_ListDatastoresPaginateResponsedatastoreSummariesdatastoreStoragecustomerManagedS3TypeDef = TypedDict(
    "_ListDatastoresPaginateResponsedatastoreSummariesdatastoreStoragecustomerManagedS3TypeDef",
    {"bucket": str, "keyPrefix": str, "roleArn": str},
    total=False,
)


class ListDatastoresPaginateResponsedatastoreSummariesdatastoreStoragecustomerManagedS3TypeDef(
    _ListDatastoresPaginateResponsedatastoreSummariesdatastoreStoragecustomerManagedS3TypeDef
):
    """
    Type definition for `ListDatastoresPaginateResponsedatastoreSummariesdatastoreStorage` `customerManagedS3`

    Used to store data store data in an S3 bucket that you manage.

    - **bucket** *(string) --*

      The name of the Amazon S3 bucket in which data store data is stored.

    - **keyPrefix** *(string) --*

      [Optional] The prefix used to create the keys of the data store data objects. Each
      object in an Amazon S3 bucket has a key that is its unique identifier within the
      bucket (each object in a bucket has exactly one key). The prefix must end with a '/'.

    - **roleArn** *(string) --*

      The ARN of the role which grants AWS IoT Analytics permission to interact with your
      Amazon S3 resources.
    """


_ListDatastoresPaginateResponsedatastoreSummariesdatastoreStorageTypeDef = TypedDict(
    "_ListDatastoresPaginateResponsedatastoreSummariesdatastoreStorageTypeDef",
    {
        "serviceManagedS3": Dict,
        "customerManagedS3": ListDatastoresPaginateResponsedatastoreSummariesdatastoreStoragecustomerManagedS3TypeDef,
    },
    total=False,
)


class ListDatastoresPaginateResponsedatastoreSummariesdatastoreStorageTypeDef(
    _ListDatastoresPaginateResponsedatastoreSummariesdatastoreStorageTypeDef
):
    """
    Type definition for `ListDatastoresPaginateResponsedatastoreSummaries` `datastoreStorage`

    Where data store data is stored.

    - **serviceManagedS3** *(dict) --*

      Used to store data store data in an S3 bucket managed by the AWS IoT Analytics service.

    - **customerManagedS3** *(dict) --*

      Used to store data store data in an S3 bucket that you manage.

      - **bucket** *(string) --*

        The name of the Amazon S3 bucket in which data store data is stored.

      - **keyPrefix** *(string) --*

        [Optional] The prefix used to create the keys of the data store data objects. Each
        object in an Amazon S3 bucket has a key that is its unique identifier within the
        bucket (each object in a bucket has exactly one key). The prefix must end with a '/'.

      - **roleArn** *(string) --*

        The ARN of the role which grants AWS IoT Analytics permission to interact with your
        Amazon S3 resources.
    """


_ListDatastoresPaginateResponsedatastoreSummariesTypeDef = TypedDict(
    "_ListDatastoresPaginateResponsedatastoreSummariesTypeDef",
    {
        "datastoreName": str,
        "datastoreStorage": ListDatastoresPaginateResponsedatastoreSummariesdatastoreStorageTypeDef,
        "status": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
    },
    total=False,
)


class ListDatastoresPaginateResponsedatastoreSummariesTypeDef(
    _ListDatastoresPaginateResponsedatastoreSummariesTypeDef
):
    """
    Type definition for `ListDatastoresPaginateResponse` `datastoreSummaries`

    A summary of information about a data store.

    - **datastoreName** *(string) --*

      The name of the data store.

    - **datastoreStorage** *(dict) --*

      Where data store data is stored.

      - **serviceManagedS3** *(dict) --*

        Used to store data store data in an S3 bucket managed by the AWS IoT Analytics service.

      - **customerManagedS3** *(dict) --*

        Used to store data store data in an S3 bucket that you manage.

        - **bucket** *(string) --*

          The name of the Amazon S3 bucket in which data store data is stored.

        - **keyPrefix** *(string) --*

          [Optional] The prefix used to create the keys of the data store data objects. Each
          object in an Amazon S3 bucket has a key that is its unique identifier within the
          bucket (each object in a bucket has exactly one key). The prefix must end with a '/'.

        - **roleArn** *(string) --*

          The ARN of the role which grants AWS IoT Analytics permission to interact with your
          Amazon S3 resources.

    - **status** *(string) --*

      The status of the data store.

    - **creationTime** *(datetime) --*

      When the data store was created.

    - **lastUpdateTime** *(datetime) --*

      The last time the data store was updated.
    """


_ListDatastoresPaginateResponseTypeDef = TypedDict(
    "_ListDatastoresPaginateResponseTypeDef",
    {
        "datastoreSummaries": List[
            ListDatastoresPaginateResponsedatastoreSummariesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ListDatastoresPaginateResponseTypeDef(_ListDatastoresPaginateResponseTypeDef):
    """
    Type definition for `ListDatastoresPaginate` `Response`

    - **datastoreSummaries** *(list) --*

      A list of "DatastoreSummary" objects.

      - *(dict) --*

        A summary of information about a data store.

        - **datastoreName** *(string) --*

          The name of the data store.

        - **datastoreStorage** *(dict) --*

          Where data store data is stored.

          - **serviceManagedS3** *(dict) --*

            Used to store data store data in an S3 bucket managed by the AWS IoT Analytics service.

          - **customerManagedS3** *(dict) --*

            Used to store data store data in an S3 bucket that you manage.

            - **bucket** *(string) --*

              The name of the Amazon S3 bucket in which data store data is stored.

            - **keyPrefix** *(string) --*

              [Optional] The prefix used to create the keys of the data store data objects. Each
              object in an Amazon S3 bucket has a key that is its unique identifier within the
              bucket (each object in a bucket has exactly one key). The prefix must end with a '/'.

            - **roleArn** *(string) --*

              The ARN of the role which grants AWS IoT Analytics permission to interact with your
              Amazon S3 resources.

        - **status** *(string) --*

          The status of the data store.

        - **creationTime** *(datetime) --*

          When the data store was created.

        - **lastUpdateTime** *(datetime) --*

          The last time the data store was updated.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListPipelinesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListPipelinesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListPipelinesPaginatePaginationConfigTypeDef(
    _ListPipelinesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListPipelinesPaginate` `PaginationConfig`

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


_ListPipelinesPaginateResponsepipelineSummariesreprocessingSummariesTypeDef = TypedDict(
    "_ListPipelinesPaginateResponsepipelineSummariesreprocessingSummariesTypeDef",
    {"id": str, "status": str, "creationTime": datetime},
    total=False,
)


class ListPipelinesPaginateResponsepipelineSummariesreprocessingSummariesTypeDef(
    _ListPipelinesPaginateResponsepipelineSummariesreprocessingSummariesTypeDef
):
    """
    Type definition for `ListPipelinesPaginateResponsepipelineSummaries` `reprocessingSummaries`

    Information about pipeline reprocessing.

    - **id** *(string) --*

      The 'reprocessingId' returned by "StartPipelineReprocessing".

    - **status** *(string) --*

      The status of the pipeline reprocessing.

    - **creationTime** *(datetime) --*

      The time the pipeline reprocessing was created.
    """


_ListPipelinesPaginateResponsepipelineSummariesTypeDef = TypedDict(
    "_ListPipelinesPaginateResponsepipelineSummariesTypeDef",
    {
        "pipelineName": str,
        "reprocessingSummaries": List[
            ListPipelinesPaginateResponsepipelineSummariesreprocessingSummariesTypeDef
        ],
        "creationTime": datetime,
        "lastUpdateTime": datetime,
    },
    total=False,
)


class ListPipelinesPaginateResponsepipelineSummariesTypeDef(
    _ListPipelinesPaginateResponsepipelineSummariesTypeDef
):
    """
    Type definition for `ListPipelinesPaginateResponse` `pipelineSummaries`

    A summary of information about a pipeline.

    - **pipelineName** *(string) --*

      The name of the pipeline.

    - **reprocessingSummaries** *(list) --*

      A summary of information about the pipeline reprocessing.

      - *(dict) --*

        Information about pipeline reprocessing.

        - **id** *(string) --*

          The 'reprocessingId' returned by "StartPipelineReprocessing".

        - **status** *(string) --*

          The status of the pipeline reprocessing.

        - **creationTime** *(datetime) --*

          The time the pipeline reprocessing was created.

    - **creationTime** *(datetime) --*

      When the pipeline was created.

    - **lastUpdateTime** *(datetime) --*

      When the pipeline was last updated.
    """


_ListPipelinesPaginateResponseTypeDef = TypedDict(
    "_ListPipelinesPaginateResponseTypeDef",
    {
        "pipelineSummaries": List[
            ListPipelinesPaginateResponsepipelineSummariesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ListPipelinesPaginateResponseTypeDef(_ListPipelinesPaginateResponseTypeDef):
    """
    Type definition for `ListPipelinesPaginate` `Response`

    - **pipelineSummaries** *(list) --*

      A list of "PipelineSummary" objects.

      - *(dict) --*

        A summary of information about a pipeline.

        - **pipelineName** *(string) --*

          The name of the pipeline.

        - **reprocessingSummaries** *(list) --*

          A summary of information about the pipeline reprocessing.

          - *(dict) --*

            Information about pipeline reprocessing.

            - **id** *(string) --*

              The 'reprocessingId' returned by "StartPipelineReprocessing".

            - **status** *(string) --*

              The status of the pipeline reprocessing.

            - **creationTime** *(datetime) --*

              The time the pipeline reprocessing was created.

        - **creationTime** *(datetime) --*

          When the pipeline was created.

        - **lastUpdateTime** *(datetime) --*

          When the pipeline was last updated.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """
