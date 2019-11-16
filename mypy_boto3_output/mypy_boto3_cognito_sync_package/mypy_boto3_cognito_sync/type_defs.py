"Main interface for cognito-sync type defs"
from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientBulkPublishResponseTypeDef",
    "ClientDeleteDatasetResponseTypeDef",
    "ClientDescribeDatasetResponseTypeDef",
    "ClientDescribeIdentityPoolUsageResponseIdentityPoolUsageTypeDef",
    "ClientDescribeIdentityPoolUsageResponseTypeDef",
    "ClientDescribeIdentityUsageResponseIdentityUsageTypeDef",
    "ClientDescribeIdentityUsageResponseTypeDef",
    "ClientGetBulkPublishDetailsResponseTypeDef",
    "ClientGetCognitoEventsResponseTypeDef",
    "ClientGetIdentityPoolConfigurationResponsePushSyncTypeDef",
    "ClientGetIdentityPoolConfigurationResponseTypeDef",
    "ClientListDatasetsResponseTypeDef",
    "ClientListIdentityPoolUsageResponseIdentityPoolUsagesTypeDef",
    "ClientListIdentityPoolUsageResponseTypeDef",
    "ClientListRecordsResponseRecordsTypeDef",
    "ClientListRecordsResponseTypeDef",
    "ClientRegisterDeviceResponseTypeDef",
    "ClientSetIdentityPoolConfigurationCognitoStreamsTypeDef",
    "ClientSetIdentityPoolConfigurationPushSyncTypeDef",
    "ClientSetIdentityPoolConfigurationResponsePushSyncTypeDef",
    "ClientSetIdentityPoolConfigurationResponseTypeDef",
    "ClientUpdateRecordsRecordPatchesTypeDef",
    "ClientUpdateRecordsResponseRecordsTypeDef",
    "ClientUpdateRecordsResponseTypeDef",
)


_ClientBulkPublishResponseTypeDef = TypedDict(
    "_ClientBulkPublishResponseTypeDef", {"IdentityPoolId": str}, total=False
)


class ClientBulkPublishResponseTypeDef(_ClientBulkPublishResponseTypeDef):
    """
    Type definition for `ClientBulkPublish` `Response`

    - **IdentityPoolId** *(string) --* A name-spaced GUID (for example,
    us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is
    unique within a region.
    """


_ClientDeleteDatasetResponseTypeDef = TypedDict(
    "_ClientDeleteDatasetResponseTypeDef", {"Dataset": Dict[str, Any]}, total=False
)


class ClientDeleteDatasetResponseTypeDef(_ClientDeleteDatasetResponseTypeDef):
    """
    Type definition for `ClientDeleteDataset` `Response`

    - **Dataset** *(dict) --* A collection of data for an identity pool. An identity pool can have
    multiple datasets. A dataset is per identity and can be general or associated with a particular
    entity in an application (like a saved game). Datasets are automatically created if they don't
    exist. Data is synced by dataset, and a dataset can hold up to 1MB of key-value pairs.

      - **IdentityId** *(string) --* A name-spaced GUID (for example,
      us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is
      unique within a region.

      - **DatasetName** *(string) --* A string of up to 128 characters. Allowed characters are a-z,
      A-Z, 0-9, '_' (underscore), '-' (dash), and '.' (dot).

      - **CreationDate** *(datetime) --* Date on which the dataset was created.

      - **LastModifiedDate** *(datetime) --* Date when the dataset was last modified.

      - **LastModifiedBy** *(string) --* The device that made the last change to this dataset.

      - **DataStorage** *(integer) --* Total size in bytes of the records in this dataset.

      - **NumRecords** *(integer) --* Number of records in this dataset.
    """


_ClientDescribeDatasetResponseTypeDef = TypedDict(
    "_ClientDescribeDatasetResponseTypeDef", {"Dataset": Dict[str, Any]}, total=False
)


class ClientDescribeDatasetResponseTypeDef(_ClientDescribeDatasetResponseTypeDef):
    """
    Type definition for `ClientDescribeDataset` `Response`

    - **Dataset** *(dict) --* Meta data for a collection of data for an identity. An identity can
    have multiple datasets. A dataset can be general or associated with a particular entity in an
    application (like a saved game). Datasets are automatically created if they don't exist. Data
    is synced by dataset, and a dataset can hold up to 1MB of key-value pairs.

      - **IdentityId** *(string) --* A name-spaced GUID (for example,
      us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is
      unique within a region.

      - **DatasetName** *(string) --* A string of up to 128 characters. Allowed characters are a-z,
      A-Z, 0-9, '_' (underscore), '-' (dash), and '.' (dot).

      - **CreationDate** *(datetime) --* Date on which the dataset was created.

      - **LastModifiedDate** *(datetime) --* Date when the dataset was last modified.

      - **LastModifiedBy** *(string) --* The device that made the last change to this dataset.

      - **DataStorage** *(integer) --* Total size in bytes of the records in this dataset.

      - **NumRecords** *(integer) --* Number of records in this dataset.
    """


_ClientDescribeIdentityPoolUsageResponseIdentityPoolUsageTypeDef = TypedDict(
    "_ClientDescribeIdentityPoolUsageResponseIdentityPoolUsageTypeDef",
    {
        "IdentityPoolId": str,
        "SyncSessionsCount": int,
        "DataStorage": int,
        "LastModifiedDate": datetime,
    },
    total=False,
)


class ClientDescribeIdentityPoolUsageResponseIdentityPoolUsageTypeDef(
    _ClientDescribeIdentityPoolUsageResponseIdentityPoolUsageTypeDef
):
    """
    Type definition for `ClientDescribeIdentityPoolUsageResponse` `IdentityPoolUsage`

    - **IdentityPoolId** *(string) --* A name-spaced GUID (for example,
    us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is
    unique within a region.

    - **SyncSessionsCount** *(integer) --* Number of sync sessions for the identity pool.

    - **DataStorage** *(integer) --* Data storage information for the identity pool.

    - **LastModifiedDate** *(datetime) --* Date on which the identity pool was last modified.
    """


_ClientDescribeIdentityPoolUsageResponseTypeDef = TypedDict(
    "_ClientDescribeIdentityPoolUsageResponseTypeDef",
    {
        "IdentityPoolUsage": ClientDescribeIdentityPoolUsageResponseIdentityPoolUsageTypeDef
    },
    total=False,
)


class ClientDescribeIdentityPoolUsageResponseTypeDef(
    _ClientDescribeIdentityPoolUsageResponseTypeDef
):
    """
    Type definition for `ClientDescribeIdentityPoolUsage` `Response`

    - **IdentityPoolUsage** *(dict) --* Information about the usage of the identity pool.

      - **IdentityPoolId** *(string) --* A name-spaced GUID (for example,
      us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is
      unique within a region.

      - **SyncSessionsCount** *(integer) --* Number of sync sessions for the identity pool.

      - **DataStorage** *(integer) --* Data storage information for the identity pool.

      - **LastModifiedDate** *(datetime) --* Date on which the identity pool was last modified.
    """


_ClientDescribeIdentityUsageResponseIdentityUsageTypeDef = TypedDict(
    "_ClientDescribeIdentityUsageResponseIdentityUsageTypeDef",
    {
        "IdentityId": str,
        "IdentityPoolId": str,
        "LastModifiedDate": datetime,
        "DatasetCount": int,
        "DataStorage": int,
    },
    total=False,
)


class ClientDescribeIdentityUsageResponseIdentityUsageTypeDef(
    _ClientDescribeIdentityUsageResponseIdentityUsageTypeDef
):
    """
    Type definition for `ClientDescribeIdentityUsageResponse` `IdentityUsage`

    - **IdentityId** *(string) --* A name-spaced GUID (for example,
    us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is
    unique within a region.

    - **IdentityPoolId** *(string) --* A name-spaced GUID (for example,
    us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is
    unique within a region.

    - **LastModifiedDate** *(datetime) --* Date on which the identity was last modified.

    - **DatasetCount** *(integer) --* Number of datasets for the identity.

    - **DataStorage** *(integer) --* Total data storage for this identity.
    """


_ClientDescribeIdentityUsageResponseTypeDef = TypedDict(
    "_ClientDescribeIdentityUsageResponseTypeDef",
    {"IdentityUsage": ClientDescribeIdentityUsageResponseIdentityUsageTypeDef},
    total=False,
)


class ClientDescribeIdentityUsageResponseTypeDef(
    _ClientDescribeIdentityUsageResponseTypeDef
):
    """
    Type definition for `ClientDescribeIdentityUsage` `Response`

    - **IdentityUsage** *(dict) --* Usage information for the identity.

      - **IdentityId** *(string) --* A name-spaced GUID (for example,
      us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is
      unique within a region.

      - **IdentityPoolId** *(string) --* A name-spaced GUID (for example,
      us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is
      unique within a region.

      - **LastModifiedDate** *(datetime) --* Date on which the identity was last modified.

      - **DatasetCount** *(integer) --* Number of datasets for the identity.

      - **DataStorage** *(integer) --* Total data storage for this identity.
    """


_ClientGetBulkPublishDetailsResponseTypeDef = TypedDict(
    "_ClientGetBulkPublishDetailsResponseTypeDef",
    {
        "IdentityPoolId": str,
        "BulkPublishStartTime": datetime,
        "BulkPublishCompleteTime": datetime,
        "BulkPublishStatus": str,
        "FailureMessage": str,
    },
    total=False,
)


class ClientGetBulkPublishDetailsResponseTypeDef(
    _ClientGetBulkPublishDetailsResponseTypeDef
):
    """
    Type definition for `ClientGetBulkPublishDetails` `Response`

    - **IdentityPoolId** *(string) --* A name-spaced GUID (for example,
    us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is
    unique within a region.

    - **BulkPublishStartTime** *(datetime) --* The date/time at which the last bulk publish was
    initiated.

    - **BulkPublishCompleteTime** *(datetime) --* If BulkPublishStatus is SUCCEEDED, the time the
    last bulk publish operation completed.

    - **BulkPublishStatus** *(string) --* Status of the last bulk publish operation, valid values
    are:

      NOT_STARTED - No bulk publish has been requested for this identity pool

      IN_PROGRESS - Data is being published to the configured stream

      SUCCEEDED - All data for the identity pool has been published to the configured stream

      FAILED - Some portion of the data has failed to publish, check FailureMessage for the cause.

    - **FailureMessage** *(string) --* If BulkPublishStatus is FAILED this field will contain the
    error message that caused the bulk publish to fail.
    """


_ClientGetCognitoEventsResponseTypeDef = TypedDict(
    "_ClientGetCognitoEventsResponseTypeDef", {"Events": Dict[str, str]}, total=False
)


class ClientGetCognitoEventsResponseTypeDef(_ClientGetCognitoEventsResponseTypeDef):
    """
    Type definition for `ClientGetCognitoEvents` `Response`

    The response from the GetCognitoEvents request

    - **Events** *(dict) --*

      The Cognito Events returned from the GetCognitoEvents request

      - *(string) --*

        - *(string) --*
    """


_ClientGetIdentityPoolConfigurationResponsePushSyncTypeDef = TypedDict(
    "_ClientGetIdentityPoolConfigurationResponsePushSyncTypeDef",
    {"ApplicationArns": List[str], "RoleArn": str},
    total=False,
)


class ClientGetIdentityPoolConfigurationResponsePushSyncTypeDef(
    _ClientGetIdentityPoolConfigurationResponsePushSyncTypeDef
):
    """
    Type definition for `ClientGetIdentityPoolConfigurationResponse` `PushSync`

    Options to apply to this identity pool for push synchronization.

    - **ApplicationArns** *(list) --*

      List of SNS platform application ARNs that could be used by clients.

      - *(string) --*

    - **RoleArn** *(string) --*

      A role configured to allow Cognito to call SNS on behalf of the developer.
    """


_ClientGetIdentityPoolConfigurationResponseTypeDef = TypedDict(
    "_ClientGetIdentityPoolConfigurationResponseTypeDef",
    {
        "IdentityPoolId": str,
        "PushSync": ClientGetIdentityPoolConfigurationResponsePushSyncTypeDef,
        "CognitoStreams": Dict[str, Any],
    },
    total=False,
)


class ClientGetIdentityPoolConfigurationResponseTypeDef(
    _ClientGetIdentityPoolConfigurationResponseTypeDef
):
    """
    Type definition for `ClientGetIdentityPoolConfiguration` `Response`

    The output for the GetIdentityPoolConfiguration operation.

    - **IdentityPoolId** *(string) --*

      A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by
      Amazon Cognito.

    - **PushSync** *(dict) --*

      Options to apply to this identity pool for push synchronization.

      - **ApplicationArns** *(list) --*

        List of SNS platform application ARNs that could be used by clients.

        - *(string) --*

      - **RoleArn** *(string) --*

        A role configured to allow Cognito to call SNS on behalf of the developer.

    - **CognitoStreams** *(dict) --* Options to apply to this identity pool for Amazon Cognito
    streams.

      - **StreamName** *(string) --* The name of the Cognito stream to receive updates. This stream
      must be in the developers account and in the same region as the identity pool.

      - **RoleArn** *(string) --* The ARN of the role Amazon Cognito can assume in order to publish
      to the stream. This role must grant access to Amazon Cognito (cognito-sync) to invoke
      PutRecord on your Cognito stream.

      - **StreamingStatus** *(string) --* Status of the Cognito streams. Valid values are:

        ENABLED - Streaming of updates to identity pool is enabled.

        DISABLED - Streaming of updates to identity pool is disabled. Bulk publish will also fail
        if StreamingStatus is DISABLED.
    """


_ClientListDatasetsResponseTypeDef = TypedDict(
    "_ClientListDatasetsResponseTypeDef",
    {"Datasets": List[Dict], "Count": int, "NextToken": str},
    total=False,
)


class ClientListDatasetsResponseTypeDef(_ClientListDatasetsResponseTypeDef):
    """
    Type definition for `ClientListDatasets` `Response`

    - **Datasets** *(list) --* A set of datasets.

      - *(dict) --* A collection of data for an identity pool. An identity pool can have multiple
      datasets. A dataset is per identity and can be general or associated with a particular entity
      in an application (like a saved game). Datasets are automatically created if they don't
      exist. Data is synced by dataset, and a dataset can hold up to 1MB of key-value pairs.

        - **IdentityId** *(string) --* A name-spaced GUID (for example,
        us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation
        is unique within a region.

        - **DatasetName** *(string) --* A string of up to 128 characters. Allowed characters are
        a-z, A-Z, 0-9, '_' (underscore), '-' (dash), and '.' (dot).

        - **CreationDate** *(datetime) --* Date on which the dataset was created.

        - **LastModifiedDate** *(datetime) --* Date when the dataset was last modified.

        - **LastModifiedBy** *(string) --* The device that made the last change to this dataset.

        - **DataStorage** *(integer) --* Total size in bytes of the records in this dataset.

        - **NumRecords** *(integer) --* Number of records in this dataset.

    - **Count** *(integer) --* Number of datasets returned.

    - **NextToken** *(string) --* A pagination token for obtaining the next page of results.
    """


_ClientListIdentityPoolUsageResponseIdentityPoolUsagesTypeDef = TypedDict(
    "_ClientListIdentityPoolUsageResponseIdentityPoolUsagesTypeDef",
    {
        "IdentityPoolId": str,
        "SyncSessionsCount": int,
        "DataStorage": int,
        "LastModifiedDate": datetime,
    },
    total=False,
)


class ClientListIdentityPoolUsageResponseIdentityPoolUsagesTypeDef(
    _ClientListIdentityPoolUsageResponseIdentityPoolUsagesTypeDef
):
    """
    Type definition for `ClientListIdentityPoolUsageResponse` `IdentityPoolUsages`

    - **IdentityPoolId** *(string) --* A name-spaced GUID (for example,
    us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation
    is unique within a region.

    - **SyncSessionsCount** *(integer) --* Number of sync sessions for the identity pool.

    - **DataStorage** *(integer) --* Data storage information for the identity pool.

    - **LastModifiedDate** *(datetime) --* Date on which the identity pool was last modified.
    """


_ClientListIdentityPoolUsageResponseTypeDef = TypedDict(
    "_ClientListIdentityPoolUsageResponseTypeDef",
    {
        "IdentityPoolUsages": List[
            ClientListIdentityPoolUsageResponseIdentityPoolUsagesTypeDef
        ],
        "MaxResults": int,
        "Count": int,
        "NextToken": str,
    },
    total=False,
)


class ClientListIdentityPoolUsageResponseTypeDef(
    _ClientListIdentityPoolUsageResponseTypeDef
):
    """
    Type definition for `ClientListIdentityPoolUsage` `Response`

    - **IdentityPoolUsages** *(list) --* Usage information for the identity pools.

      - *(dict) --* Usage information for the identity pool.

        - **IdentityPoolId** *(string) --* A name-spaced GUID (for example,
        us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation
        is unique within a region.

        - **SyncSessionsCount** *(integer) --* Number of sync sessions for the identity pool.

        - **DataStorage** *(integer) --* Data storage information for the identity pool.

        - **LastModifiedDate** *(datetime) --* Date on which the identity pool was last modified.

    - **MaxResults** *(integer) --* The maximum number of results to be returned.

    - **Count** *(integer) --* Total number of identities for the identity pool.

    - **NextToken** *(string) --* A pagination token for obtaining the next page of results.
    """


_ClientListRecordsResponseRecordsTypeDef = TypedDict(
    "_ClientListRecordsResponseRecordsTypeDef",
    {
        "Key": str,
        "Value": str,
        "SyncCount": int,
        "LastModifiedDate": datetime,
        "LastModifiedBy": str,
        "DeviceLastModifiedDate": datetime,
    },
    total=False,
)


class ClientListRecordsResponseRecordsTypeDef(_ClientListRecordsResponseRecordsTypeDef):
    """
    Type definition for `ClientListRecordsResponse` `Records`

    - **Key** *(string) --* The key for the record.

    - **Value** *(string) --* The value for the record.

    - **SyncCount** *(integer) --* The server sync count for this record.

    - **LastModifiedDate** *(datetime) --* The date on which the record was last modified.

    - **LastModifiedBy** *(string) --* The user/device that made the last change to this record.

    - **DeviceLastModifiedDate** *(datetime) --* The last modified date of the client device.
    """


_ClientListRecordsResponseTypeDef = TypedDict(
    "_ClientListRecordsResponseTypeDef",
    {
        "Records": List[ClientListRecordsResponseRecordsTypeDef],
        "NextToken": str,
        "Count": int,
        "DatasetSyncCount": int,
        "LastModifiedBy": str,
        "MergedDatasetNames": List[str],
        "DatasetExists": bool,
        "DatasetDeletedAfterRequestedSyncCount": bool,
        "SyncSessionToken": str,
    },
    total=False,
)


class ClientListRecordsResponseTypeDef(_ClientListRecordsResponseTypeDef):
    """
    Type definition for `ClientListRecords` `Response`

    - **Records** *(list) --* A list of all records.

      - *(dict) --* The basic data structure of a dataset.

        - **Key** *(string) --* The key for the record.

        - **Value** *(string) --* The value for the record.

        - **SyncCount** *(integer) --* The server sync count for this record.

        - **LastModifiedDate** *(datetime) --* The date on which the record was last modified.

        - **LastModifiedBy** *(string) --* The user/device that made the last change to this record.

        - **DeviceLastModifiedDate** *(datetime) --* The last modified date of the client device.

    - **NextToken** *(string) --* A pagination token for obtaining the next page of results.

    - **Count** *(integer) --* Total number of records.

    - **DatasetSyncCount** *(integer) --* Server sync count for this dataset.

    - **LastModifiedBy** *(string) --* The user/device that made the last change to this record.

    - **MergedDatasetNames** *(list) --* Names of merged datasets.

      - *(string) --*

    - **DatasetExists** *(boolean) --* Indicates whether the dataset exists.

    - **DatasetDeletedAfterRequestedSyncCount** *(boolean) --* A boolean value specifying whether
    to delete the dataset locally.

    - **SyncSessionToken** *(string) --* A token containing a session ID, identity ID, and
    expiration.
    """


_ClientRegisterDeviceResponseTypeDef = TypedDict(
    "_ClientRegisterDeviceResponseTypeDef", {"DeviceId": str}, total=False
)


class ClientRegisterDeviceResponseTypeDef(_ClientRegisterDeviceResponseTypeDef):
    """
    Type definition for `ClientRegisterDevice` `Response`

    Response to a RegisterDevice request.

    - **DeviceId** *(string) --*

      The unique ID generated for this device by Cognito.
    """


_ClientSetIdentityPoolConfigurationCognitoStreamsTypeDef = TypedDict(
    "_ClientSetIdentityPoolConfigurationCognitoStreamsTypeDef",
    {"StreamName": str, "RoleArn": str, "StreamingStatus": str},
    total=False,
)


class ClientSetIdentityPoolConfigurationCognitoStreamsTypeDef(
    _ClientSetIdentityPoolConfigurationCognitoStreamsTypeDef
):
    """
    Type definition for `ClientSetIdentityPoolConfiguration` `CognitoStreams`

    - **StreamName** *(string) --* The name of the Cognito stream to receive updates. This stream
    must be in the developers account and in the same region as the identity pool.

    - **RoleArn** *(string) --* The ARN of the role Amazon Cognito can assume in order to publish to
    the stream. This role must grant access to Amazon Cognito (cognito-sync) to invoke PutRecord on
    your Cognito stream.

    - **StreamingStatus** *(string) --* Status of the Cognito streams. Valid values are:

      ENABLED - Streaming of updates to identity pool is enabled.

      DISABLED - Streaming of updates to identity pool is disabled. Bulk publish will also fail if
      StreamingStatus is DISABLED.
    """


_ClientSetIdentityPoolConfigurationPushSyncTypeDef = TypedDict(
    "_ClientSetIdentityPoolConfigurationPushSyncTypeDef",
    {"ApplicationArns": List[str], "RoleArn": str},
    total=False,
)


class ClientSetIdentityPoolConfigurationPushSyncTypeDef(
    _ClientSetIdentityPoolConfigurationPushSyncTypeDef
):
    """
    Type definition for `ClientSetIdentityPoolConfiguration` `PushSync`

    Options to apply to this identity pool for push synchronization.

    - **ApplicationArns** *(list) --*

      List of SNS platform application ARNs that could be used by clients.

      - *(string) --*

    - **RoleArn** *(string) --*

      A role configured to allow Cognito to call SNS on behalf of the developer.
    """


_ClientSetIdentityPoolConfigurationResponsePushSyncTypeDef = TypedDict(
    "_ClientSetIdentityPoolConfigurationResponsePushSyncTypeDef",
    {"ApplicationArns": List[str], "RoleArn": str},
    total=False,
)


class ClientSetIdentityPoolConfigurationResponsePushSyncTypeDef(
    _ClientSetIdentityPoolConfigurationResponsePushSyncTypeDef
):
    """
    Type definition for `ClientSetIdentityPoolConfigurationResponse` `PushSync`

    Options to apply to this identity pool for push synchronization.

    - **ApplicationArns** *(list) --*

      List of SNS platform application ARNs that could be used by clients.

      - *(string) --*

    - **RoleArn** *(string) --*

      A role configured to allow Cognito to call SNS on behalf of the developer.
    """


_ClientSetIdentityPoolConfigurationResponseTypeDef = TypedDict(
    "_ClientSetIdentityPoolConfigurationResponseTypeDef",
    {
        "IdentityPoolId": str,
        "PushSync": ClientSetIdentityPoolConfigurationResponsePushSyncTypeDef,
        "CognitoStreams": Dict[str, Any],
    },
    total=False,
)


class ClientSetIdentityPoolConfigurationResponseTypeDef(
    _ClientSetIdentityPoolConfigurationResponseTypeDef
):
    """
    Type definition for `ClientSetIdentityPoolConfiguration` `Response`

    The output for the SetIdentityPoolConfiguration operation

    - **IdentityPoolId** *(string) --*

      A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by
      Amazon Cognito.

    - **PushSync** *(dict) --*

      Options to apply to this identity pool for push synchronization.

      - **ApplicationArns** *(list) --*

        List of SNS platform application ARNs that could be used by clients.

        - *(string) --*

      - **RoleArn** *(string) --*

        A role configured to allow Cognito to call SNS on behalf of the developer.

    - **CognitoStreams** *(dict) --* Options to apply to this identity pool for Amazon Cognito
    streams.

      - **StreamName** *(string) --* The name of the Cognito stream to receive updates. This stream
      must be in the developers account and in the same region as the identity pool.

      - **RoleArn** *(string) --* The ARN of the role Amazon Cognito can assume in order to publish
      to the stream. This role must grant access to Amazon Cognito (cognito-sync) to invoke
      PutRecord on your Cognito stream.

      - **StreamingStatus** *(string) --* Status of the Cognito streams. Valid values are:

        ENABLED - Streaming of updates to identity pool is enabled.

        DISABLED - Streaming of updates to identity pool is disabled. Bulk publish will also fail
        if StreamingStatus is DISABLED.
    """


_RequiredClientUpdateRecordsRecordPatchesTypeDef = TypedDict(
    "_RequiredClientUpdateRecordsRecordPatchesTypeDef",
    {"Op": str, "Key": str, "SyncCount": int},
)
_OptionalClientUpdateRecordsRecordPatchesTypeDef = TypedDict(
    "_OptionalClientUpdateRecordsRecordPatchesTypeDef",
    {"Value": str, "DeviceLastModifiedDate": datetime},
    total=False,
)


class ClientUpdateRecordsRecordPatchesTypeDef(
    _RequiredClientUpdateRecordsRecordPatchesTypeDef,
    _OptionalClientUpdateRecordsRecordPatchesTypeDef,
):
    """
    Type definition for `ClientUpdateRecords` `RecordPatches`

    - **Op** *(string) --* **[REQUIRED]** An operation, either replace or remove.

    - **Key** *(string) --* **[REQUIRED]** The key associated with the record patch.

    - **Value** *(string) --* The value associated with the record patch.

    - **SyncCount** *(integer) --* **[REQUIRED]** Last known server sync count for this record. Set
    to 0 if unknown.

    - **DeviceLastModifiedDate** *(datetime) --* The last modified date of the client device.
    """


_ClientUpdateRecordsResponseRecordsTypeDef = TypedDict(
    "_ClientUpdateRecordsResponseRecordsTypeDef",
    {
        "Key": str,
        "Value": str,
        "SyncCount": int,
        "LastModifiedDate": datetime,
        "LastModifiedBy": str,
        "DeviceLastModifiedDate": datetime,
    },
    total=False,
)


class ClientUpdateRecordsResponseRecordsTypeDef(
    _ClientUpdateRecordsResponseRecordsTypeDef
):
    """
    Type definition for `ClientUpdateRecordsResponse` `Records`

    - **Key** *(string) --* The key for the record.

    - **Value** *(string) --* The value for the record.

    - **SyncCount** *(integer) --* The server sync count for this record.

    - **LastModifiedDate** *(datetime) --* The date on which the record was last modified.

    - **LastModifiedBy** *(string) --* The user/device that made the last change to this record.

    - **DeviceLastModifiedDate** *(datetime) --* The last modified date of the client device.
    """


_ClientUpdateRecordsResponseTypeDef = TypedDict(
    "_ClientUpdateRecordsResponseTypeDef",
    {"Records": List[ClientUpdateRecordsResponseRecordsTypeDef]},
    total=False,
)


class ClientUpdateRecordsResponseTypeDef(_ClientUpdateRecordsResponseTypeDef):
    """
    Type definition for `ClientUpdateRecords` `Response`

    - **Records** *(list) --* A list of records that have been updated.

      - *(dict) --* The basic data structure of a dataset.

        - **Key** *(string) --* The key for the record.

        - **Value** *(string) --* The value for the record.

        - **SyncCount** *(integer) --* The server sync count for this record.

        - **LastModifiedDate** *(datetime) --* The date on which the record was last modified.

        - **LastModifiedBy** *(string) --* The user/device that made the last change to this record.

        - **DeviceLastModifiedDate** *(datetime) --* The last modified date of the client device.
    """
