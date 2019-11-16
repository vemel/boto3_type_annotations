"Main interface for dms type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from typing_extensions import TypedDict


__all__ = (
    "ClientAddTagsToResourceTagsTypeDef",
    "ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef",
    "ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsTypeDef",
    "ClientApplyPendingMaintenanceActionResponseTypeDef",
    "ClientCreateEndpointDmsTransferSettingsTypeDef",
    "ClientCreateEndpointDynamoDbSettingsTypeDef",
    "ClientCreateEndpointElasticsearchSettingsTypeDef",
    "ClientCreateEndpointKinesisSettingsTypeDef",
    "ClientCreateEndpointMongoDbSettingsTypeDef",
    "ClientCreateEndpointRedshiftSettingsTypeDef",
    "ClientCreateEndpointResponseEndpointDmsTransferSettingsTypeDef",
    "ClientCreateEndpointResponseEndpointDynamoDbSettingsTypeDef",
    "ClientCreateEndpointResponseEndpointElasticsearchSettingsTypeDef",
    "ClientCreateEndpointResponseEndpointKinesisSettingsTypeDef",
    "ClientCreateEndpointResponseEndpointMongoDbSettingsTypeDef",
    "ClientCreateEndpointResponseEndpointRedshiftSettingsTypeDef",
    "ClientCreateEndpointResponseEndpointS3SettingsTypeDef",
    "ClientCreateEndpointResponseEndpointTypeDef",
    "ClientCreateEndpointResponseTypeDef",
    "ClientCreateEndpointS3SettingsTypeDef",
    "ClientCreateEndpointTagsTypeDef",
    "ClientCreateEventSubscriptionResponseEventSubscriptionTypeDef",
    "ClientCreateEventSubscriptionResponseTypeDef",
    "ClientCreateEventSubscriptionTagsTypeDef",
    "ClientCreateReplicationInstanceResponseReplicationInstancePendingModifiedValuesTypeDef",
    "ClientCreateReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientCreateReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsTypeDef",
    "ClientCreateReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupTypeDef",
    "ClientCreateReplicationInstanceResponseReplicationInstanceVpcSecurityGroupsTypeDef",
    "ClientCreateReplicationInstanceResponseReplicationInstanceTypeDef",
    "ClientCreateReplicationInstanceResponseTypeDef",
    "ClientCreateReplicationInstanceTagsTypeDef",
    "ClientCreateReplicationSubnetGroupResponseReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientCreateReplicationSubnetGroupResponseReplicationSubnetGroupSubnetsTypeDef",
    "ClientCreateReplicationSubnetGroupResponseReplicationSubnetGroupTypeDef",
    "ClientCreateReplicationSubnetGroupResponseTypeDef",
    "ClientCreateReplicationSubnetGroupTagsTypeDef",
    "ClientCreateReplicationTaskTagsTypeDef",
    "ClientDeleteCertificateResponseCertificateTypeDef",
    "ClientDeleteCertificateResponseTypeDef",
    "ClientDeleteConnectionResponseConnectionTypeDef",
    "ClientDeleteConnectionResponseTypeDef",
    "ClientDeleteEndpointResponseEndpointDmsTransferSettingsTypeDef",
    "ClientDeleteEndpointResponseEndpointDynamoDbSettingsTypeDef",
    "ClientDeleteEndpointResponseEndpointElasticsearchSettingsTypeDef",
    "ClientDeleteEndpointResponseEndpointKinesisSettingsTypeDef",
    "ClientDeleteEndpointResponseEndpointMongoDbSettingsTypeDef",
    "ClientDeleteEndpointResponseEndpointRedshiftSettingsTypeDef",
    "ClientDeleteEndpointResponseEndpointS3SettingsTypeDef",
    "ClientDeleteEndpointResponseEndpointTypeDef",
    "ClientDeleteEndpointResponseTypeDef",
    "ClientDeleteEventSubscriptionResponseEventSubscriptionTypeDef",
    "ClientDeleteEventSubscriptionResponseTypeDef",
    "ClientDeleteReplicationInstanceResponseReplicationInstancePendingModifiedValuesTypeDef",
    "ClientDeleteReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientDeleteReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsTypeDef",
    "ClientDeleteReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupTypeDef",
    "ClientDeleteReplicationInstanceResponseReplicationInstanceVpcSecurityGroupsTypeDef",
    "ClientDeleteReplicationInstanceResponseReplicationInstanceTypeDef",
    "ClientDeleteReplicationInstanceResponseTypeDef",
    "ClientDescribeAccountAttributesResponseAccountQuotasTypeDef",
    "ClientDescribeAccountAttributesResponseTypeDef",
    "ClientDescribeCertificatesFiltersTypeDef",
    "ClientDescribeCertificatesResponseCertificatesTypeDef",
    "ClientDescribeCertificatesResponseTypeDef",
    "ClientDescribeConnectionsFiltersTypeDef",
    "ClientDescribeConnectionsResponseConnectionsTypeDef",
    "ClientDescribeConnectionsResponseTypeDef",
    "ClientDescribeEndpointTypesFiltersTypeDef",
    "ClientDescribeEndpointTypesResponseSupportedEndpointTypesTypeDef",
    "ClientDescribeEndpointTypesResponseTypeDef",
    "ClientDescribeEndpointsFiltersTypeDef",
    "ClientDescribeEndpointsResponseEndpointsDmsTransferSettingsTypeDef",
    "ClientDescribeEndpointsResponseEndpointsDynamoDbSettingsTypeDef",
    "ClientDescribeEndpointsResponseEndpointsElasticsearchSettingsTypeDef",
    "ClientDescribeEndpointsResponseEndpointsKinesisSettingsTypeDef",
    "ClientDescribeEndpointsResponseEndpointsMongoDbSettingsTypeDef",
    "ClientDescribeEndpointsResponseEndpointsRedshiftSettingsTypeDef",
    "ClientDescribeEndpointsResponseEndpointsS3SettingsTypeDef",
    "ClientDescribeEndpointsResponseEndpointsTypeDef",
    "ClientDescribeEndpointsResponseTypeDef",
    "ClientDescribeEventCategoriesFiltersTypeDef",
    "ClientDescribeEventCategoriesResponseEventCategoryGroupListTypeDef",
    "ClientDescribeEventCategoriesResponseTypeDef",
    "ClientDescribeEventSubscriptionsFiltersTypeDef",
    "ClientDescribeEventSubscriptionsResponseEventSubscriptionsListTypeDef",
    "ClientDescribeEventSubscriptionsResponseTypeDef",
    "ClientDescribeEventsFiltersTypeDef",
    "ClientDescribeEventsResponseEventsTypeDef",
    "ClientDescribeEventsResponseTypeDef",
    "ClientDescribeOrderableReplicationInstancesResponseOrderableReplicationInstancesTypeDef",
    "ClientDescribeOrderableReplicationInstancesResponseTypeDef",
    "ClientDescribePendingMaintenanceActionsFiltersTypeDef",
    "ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef",
    "ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsTypeDef",
    "ClientDescribePendingMaintenanceActionsResponseTypeDef",
    "ClientDescribeRefreshSchemasStatusResponseRefreshSchemasStatusTypeDef",
    "ClientDescribeRefreshSchemasStatusResponseTypeDef",
    "ClientDescribeReplicationInstanceTaskLogsResponseReplicationInstanceTaskLogsTypeDef",
    "ClientDescribeReplicationInstanceTaskLogsResponseTypeDef",
    "ClientDescribeReplicationInstancesFiltersTypeDef",
    "ClientDescribeReplicationInstancesResponseReplicationInstancesPendingModifiedValuesTypeDef",
    "ClientDescribeReplicationInstancesResponseReplicationInstancesReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientDescribeReplicationInstancesResponseReplicationInstancesReplicationSubnetGroupSubnetsTypeDef",
    "ClientDescribeReplicationInstancesResponseReplicationInstancesReplicationSubnetGroupTypeDef",
    "ClientDescribeReplicationInstancesResponseReplicationInstancesVpcSecurityGroupsTypeDef",
    "ClientDescribeReplicationInstancesResponseReplicationInstancesTypeDef",
    "ClientDescribeReplicationInstancesResponseTypeDef",
    "ClientDescribeReplicationSubnetGroupsFiltersTypeDef",
    "ClientDescribeReplicationSubnetGroupsResponseReplicationSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientDescribeReplicationSubnetGroupsResponseReplicationSubnetGroupsSubnetsTypeDef",
    "ClientDescribeReplicationSubnetGroupsResponseReplicationSubnetGroupsTypeDef",
    "ClientDescribeReplicationSubnetGroupsResponseTypeDef",
    "ClientDescribeReplicationTaskAssessmentResultsResponseReplicationTaskAssessmentResultsTypeDef",
    "ClientDescribeReplicationTaskAssessmentResultsResponseTypeDef",
    "ClientDescribeReplicationTasksFiltersTypeDef",
    "ClientDescribeSchemasResponseTypeDef",
    "ClientDescribeTableStatisticsFiltersTypeDef",
    "ClientDescribeTableStatisticsResponseTableStatisticsTypeDef",
    "ClientDescribeTableStatisticsResponseTypeDef",
    "ClientImportCertificateResponseCertificateTypeDef",
    "ClientImportCertificateResponseTypeDef",
    "ClientImportCertificateTagsTypeDef",
    "ClientListTagsForResourceResponseTagListTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientModifyEndpointDmsTransferSettingsTypeDef",
    "ClientModifyEndpointDynamoDbSettingsTypeDef",
    "ClientModifyEndpointElasticsearchSettingsTypeDef",
    "ClientModifyEndpointKinesisSettingsTypeDef",
    "ClientModifyEndpointMongoDbSettingsTypeDef",
    "ClientModifyEndpointRedshiftSettingsTypeDef",
    "ClientModifyEndpointResponseEndpointDmsTransferSettingsTypeDef",
    "ClientModifyEndpointResponseEndpointDynamoDbSettingsTypeDef",
    "ClientModifyEndpointResponseEndpointElasticsearchSettingsTypeDef",
    "ClientModifyEndpointResponseEndpointKinesisSettingsTypeDef",
    "ClientModifyEndpointResponseEndpointMongoDbSettingsTypeDef",
    "ClientModifyEndpointResponseEndpointRedshiftSettingsTypeDef",
    "ClientModifyEndpointResponseEndpointS3SettingsTypeDef",
    "ClientModifyEndpointResponseEndpointTypeDef",
    "ClientModifyEndpointResponseTypeDef",
    "ClientModifyEndpointS3SettingsTypeDef",
    "ClientModifyEventSubscriptionResponseEventSubscriptionTypeDef",
    "ClientModifyEventSubscriptionResponseTypeDef",
    "ClientModifyReplicationInstanceResponseReplicationInstancePendingModifiedValuesTypeDef",
    "ClientModifyReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientModifyReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsTypeDef",
    "ClientModifyReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupTypeDef",
    "ClientModifyReplicationInstanceResponseReplicationInstanceVpcSecurityGroupsTypeDef",
    "ClientModifyReplicationInstanceResponseReplicationInstanceTypeDef",
    "ClientModifyReplicationInstanceResponseTypeDef",
    "ClientModifyReplicationSubnetGroupResponseReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientModifyReplicationSubnetGroupResponseReplicationSubnetGroupSubnetsTypeDef",
    "ClientModifyReplicationSubnetGroupResponseReplicationSubnetGroupTypeDef",
    "ClientModifyReplicationSubnetGroupResponseTypeDef",
    "ClientRebootReplicationInstanceResponseReplicationInstancePendingModifiedValuesTypeDef",
    "ClientRebootReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientRebootReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsTypeDef",
    "ClientRebootReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupTypeDef",
    "ClientRebootReplicationInstanceResponseReplicationInstanceVpcSecurityGroupsTypeDef",
    "ClientRebootReplicationInstanceResponseReplicationInstanceTypeDef",
    "ClientRebootReplicationInstanceResponseTypeDef",
    "ClientRefreshSchemasResponseRefreshSchemasStatusTypeDef",
    "ClientRefreshSchemasResponseTypeDef",
    "ClientReloadTablesResponseTypeDef",
    "ClientReloadTablesTablesToReloadTypeDef",
    "ClientTestConnectionResponseConnectionTypeDef",
    "ClientTestConnectionResponseTypeDef",
    "DescribeCertificatesPaginateFiltersTypeDef",
    "DescribeCertificatesPaginatePaginationConfigTypeDef",
    "DescribeCertificatesPaginateResponseCertificatesTypeDef",
    "DescribeCertificatesPaginateResponseTypeDef",
    "DescribeConnectionsPaginateFiltersTypeDef",
    "DescribeConnectionsPaginatePaginationConfigTypeDef",
    "DescribeConnectionsPaginateResponseConnectionsTypeDef",
    "DescribeConnectionsPaginateResponseTypeDef",
    "DescribeEndpointTypesPaginateFiltersTypeDef",
    "DescribeEndpointTypesPaginatePaginationConfigTypeDef",
    "DescribeEndpointTypesPaginateResponseSupportedEndpointTypesTypeDef",
    "DescribeEndpointTypesPaginateResponseTypeDef",
    "DescribeEndpointsPaginateFiltersTypeDef",
    "DescribeEndpointsPaginatePaginationConfigTypeDef",
    "DescribeEndpointsPaginateResponseEndpointsDmsTransferSettingsTypeDef",
    "DescribeEndpointsPaginateResponseEndpointsDynamoDbSettingsTypeDef",
    "DescribeEndpointsPaginateResponseEndpointsElasticsearchSettingsTypeDef",
    "DescribeEndpointsPaginateResponseEndpointsKinesisSettingsTypeDef",
    "DescribeEndpointsPaginateResponseEndpointsMongoDbSettingsTypeDef",
    "DescribeEndpointsPaginateResponseEndpointsRedshiftSettingsTypeDef",
    "DescribeEndpointsPaginateResponseEndpointsS3SettingsTypeDef",
    "DescribeEndpointsPaginateResponseEndpointsTypeDef",
    "DescribeEndpointsPaginateResponseTypeDef",
    "DescribeEventSubscriptionsPaginateFiltersTypeDef",
    "DescribeEventSubscriptionsPaginatePaginationConfigTypeDef",
    "DescribeEventSubscriptionsPaginateResponseEventSubscriptionsListTypeDef",
    "DescribeEventSubscriptionsPaginateResponseTypeDef",
    "DescribeEventsPaginateFiltersTypeDef",
    "DescribeEventsPaginatePaginationConfigTypeDef",
    "DescribeEventsPaginateResponseEventsTypeDef",
    "DescribeEventsPaginateResponseTypeDef",
    "DescribeOrderableReplicationInstancesPaginatePaginationConfigTypeDef",
    "DescribeOrderableReplicationInstancesPaginateResponseOrderableReplicationInstancesTypeDef",
    "DescribeOrderableReplicationInstancesPaginateResponseTypeDef",
    "DescribeReplicationInstancesPaginateFiltersTypeDef",
    "DescribeReplicationInstancesPaginatePaginationConfigTypeDef",
    "DescribeReplicationInstancesPaginateResponseReplicationInstancesPendingModifiedValuesTypeDef",
    "DescribeReplicationInstancesPaginateResponseReplicationInstancesReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "DescribeReplicationInstancesPaginateResponseReplicationInstancesReplicationSubnetGroupSubnetsTypeDef",
    "DescribeReplicationInstancesPaginateResponseReplicationInstancesReplicationSubnetGroupTypeDef",
    "DescribeReplicationInstancesPaginateResponseReplicationInstancesVpcSecurityGroupsTypeDef",
    "DescribeReplicationInstancesPaginateResponseReplicationInstancesTypeDef",
    "DescribeReplicationInstancesPaginateResponseTypeDef",
    "DescribeReplicationSubnetGroupsPaginateFiltersTypeDef",
    "DescribeReplicationSubnetGroupsPaginatePaginationConfigTypeDef",
    "DescribeReplicationSubnetGroupsPaginateResponseReplicationSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef",
    "DescribeReplicationSubnetGroupsPaginateResponseReplicationSubnetGroupsSubnetsTypeDef",
    "DescribeReplicationSubnetGroupsPaginateResponseReplicationSubnetGroupsTypeDef",
    "DescribeReplicationSubnetGroupsPaginateResponseTypeDef",
    "DescribeReplicationTaskAssessmentResultsPaginatePaginationConfigTypeDef",
    "DescribeReplicationTaskAssessmentResultsPaginateResponseReplicationTaskAssessmentResultsTypeDef",
    "DescribeReplicationTaskAssessmentResultsPaginateResponseTypeDef",
    "DescribeReplicationTasksPaginateFiltersTypeDef",
    "DescribeReplicationTasksPaginatePaginationConfigTypeDef",
    "DescribeSchemasPaginatePaginationConfigTypeDef",
    "DescribeSchemasPaginateResponseTypeDef",
    "DescribeTableStatisticsPaginateFiltersTypeDef",
    "DescribeTableStatisticsPaginatePaginationConfigTypeDef",
    "DescribeTableStatisticsPaginateResponseTableStatisticsTypeDef",
    "DescribeTableStatisticsPaginateResponseTypeDef",
    "EndpointDeletedWaitFiltersTypeDef",
    "EndpointDeletedWaitWaiterConfigTypeDef",
    "ReplicationInstanceAvailableWaitFiltersTypeDef",
    "ReplicationInstanceAvailableWaitWaiterConfigTypeDef",
    "ReplicationInstanceDeletedWaitFiltersTypeDef",
    "ReplicationInstanceDeletedWaitWaiterConfigTypeDef",
    "ReplicationTaskDeletedWaitFiltersTypeDef",
    "ReplicationTaskDeletedWaitWaiterConfigTypeDef",
    "ReplicationTaskReadyWaitFiltersTypeDef",
    "ReplicationTaskReadyWaitWaiterConfigTypeDef",
    "ReplicationTaskRunningWaitFiltersTypeDef",
    "ReplicationTaskRunningWaitWaiterConfigTypeDef",
    "ReplicationTaskStoppedWaitFiltersTypeDef",
    "ReplicationTaskStoppedWaitWaiterConfigTypeDef",
    "TestConnectionSucceedsWaitFiltersTypeDef",
    "TestConnectionSucceedsWaitWaiterConfigTypeDef",
)


_ClientAddTagsToResourceTagsTypeDef = TypedDict(
    "_ClientAddTagsToResourceTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientAddTagsToResourceTagsTypeDef(_ClientAddTagsToResourceTagsTypeDef):
    """
    Type definition for `ClientAddTagsToResource` `Tags`

    - **Key** *(string) --*

      A key is the required name of the tag. The string value can be from 1 to 128 Unicode
      characters in length and cannot be prefixed with "aws:" or "dms:". The string can only
      contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-'
      (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").

    - **Value** *(string) --*

      A value is the optional value of the tag. The string value can be from 1 to 256 Unicode
      characters in length and cannot be prefixed with "aws:" or "dms:". The string can only
      contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-'
      (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef = TypedDict(
    "_ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef",
    {
        "Action": str,
        "AutoAppliedAfterDate": datetime,
        "ForcedApplyDate": datetime,
        "OptInStatus": str,
        "CurrentApplyDate": datetime,
        "Description": str,
    },
    total=False,
)


class ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef(
    _ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef
):
    """
    Type definition for `ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActions` `PendingMaintenanceActionDetails`

    - **Action** *(string) --*

      The type of pending maintenance action that is available for the resource.

    - **AutoAppliedAfterDate** *(datetime) --*

      The date of the maintenance window when the action will be applied. The maintenance
      action will be applied to the resource during its first maintenance window after this
      date. If this date is specified, any ``next-maintenance`` opt-in requests are ignored.

    - **ForcedApplyDate** *(datetime) --*

      The date when the maintenance action will be automatically applied. The maintenance
      action will be applied to the resource on this date regardless of the maintenance
      window for the resource. If this date is specified, any ``immediate`` opt-in requests
      are ignored.

    - **OptInStatus** *(string) --*

      Indicates the type of opt-in request that has been received for the resource.

    - **CurrentApplyDate** *(datetime) --*

      The effective date when the pending maintenance action will be applied to the resource.
      This date takes into account opt-in requests received from the
      ``ApplyPendingMaintenanceAction`` API, the ``AutoAppliedAfterDate`` , and the
      ``ForcedApplyDate`` . This value is blank if an opt-in request has not been received
      and nothing has been specified as ``AutoAppliedAfterDate`` or ``ForcedApplyDate`` .

    - **Description** *(string) --*

      A description providing more detail about the maintenance action.
    """


_ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsTypeDef = TypedDict(
    "_ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsTypeDef",
    {
        "ResourceIdentifier": str,
        "PendingMaintenanceActionDetails": List[
            ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef
        ],
    },
    total=False,
)


class ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsTypeDef(
    _ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsTypeDef
):
    """
    Type definition for `ClientApplyPendingMaintenanceActionResponse` `ResourcePendingMaintenanceActions`

    The AWS DMS resource that the pending maintenance action will be applied to.

    - **ResourceIdentifier** *(string) --*

      The Amazon Resource Name (ARN) of the DMS resource that the pending maintenance action
      applies to. For information about creating an ARN, see `Constructing an Amazon Resource
      Name (ARN) for AWS DMS
      <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.AWS.ARN.html>`__ in the
      DMS documentation.

    - **PendingMaintenanceActionDetails** *(list) --*

      Detailed information about the pending maintenance action.

      - *(dict) --*

        - **Action** *(string) --*

          The type of pending maintenance action that is available for the resource.

        - **AutoAppliedAfterDate** *(datetime) --*

          The date of the maintenance window when the action will be applied. The maintenance
          action will be applied to the resource during its first maintenance window after this
          date. If this date is specified, any ``next-maintenance`` opt-in requests are ignored.

        - **ForcedApplyDate** *(datetime) --*

          The date when the maintenance action will be automatically applied. The maintenance
          action will be applied to the resource on this date regardless of the maintenance
          window for the resource. If this date is specified, any ``immediate`` opt-in requests
          are ignored.

        - **OptInStatus** *(string) --*

          Indicates the type of opt-in request that has been received for the resource.

        - **CurrentApplyDate** *(datetime) --*

          The effective date when the pending maintenance action will be applied to the resource.
          This date takes into account opt-in requests received from the
          ``ApplyPendingMaintenanceAction`` API, the ``AutoAppliedAfterDate`` , and the
          ``ForcedApplyDate`` . This value is blank if an opt-in request has not been received
          and nothing has been specified as ``AutoAppliedAfterDate`` or ``ForcedApplyDate`` .

        - **Description** *(string) --*

          A description providing more detail about the maintenance action.
    """


_ClientApplyPendingMaintenanceActionResponseTypeDef = TypedDict(
    "_ClientApplyPendingMaintenanceActionResponseTypeDef",
    {
        "ResourcePendingMaintenanceActions": ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsTypeDef
    },
    total=False,
)


class ClientApplyPendingMaintenanceActionResponseTypeDef(
    _ClientApplyPendingMaintenanceActionResponseTypeDef
):
    """
    Type definition for `ClientApplyPendingMaintenanceAction` `Response`

    - **ResourcePendingMaintenanceActions** *(dict) --*

      The AWS DMS resource that the pending maintenance action will be applied to.

      - **ResourceIdentifier** *(string) --*

        The Amazon Resource Name (ARN) of the DMS resource that the pending maintenance action
        applies to. For information about creating an ARN, see `Constructing an Amazon Resource
        Name (ARN) for AWS DMS
        <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.AWS.ARN.html>`__ in the
        DMS documentation.

      - **PendingMaintenanceActionDetails** *(list) --*

        Detailed information about the pending maintenance action.

        - *(dict) --*

          - **Action** *(string) --*

            The type of pending maintenance action that is available for the resource.

          - **AutoAppliedAfterDate** *(datetime) --*

            The date of the maintenance window when the action will be applied. The maintenance
            action will be applied to the resource during its first maintenance window after this
            date. If this date is specified, any ``next-maintenance`` opt-in requests are ignored.

          - **ForcedApplyDate** *(datetime) --*

            The date when the maintenance action will be automatically applied. The maintenance
            action will be applied to the resource on this date regardless of the maintenance
            window for the resource. If this date is specified, any ``immediate`` opt-in requests
            are ignored.

          - **OptInStatus** *(string) --*

            Indicates the type of opt-in request that has been received for the resource.

          - **CurrentApplyDate** *(datetime) --*

            The effective date when the pending maintenance action will be applied to the resource.
            This date takes into account opt-in requests received from the
            ``ApplyPendingMaintenanceAction`` API, the ``AutoAppliedAfterDate`` , and the
            ``ForcedApplyDate`` . This value is blank if an opt-in request has not been received
            and nothing has been specified as ``AutoAppliedAfterDate`` or ``ForcedApplyDate`` .

          - **Description** *(string) --*

            A description providing more detail about the maintenance action.
    """


_ClientCreateEndpointDmsTransferSettingsTypeDef = TypedDict(
    "_ClientCreateEndpointDmsTransferSettingsTypeDef",
    {"ServiceAccessRoleArn": str, "BucketName": str},
    total=False,
)


class ClientCreateEndpointDmsTransferSettingsTypeDef(
    _ClientCreateEndpointDmsTransferSettingsTypeDef
):
    """
    Type definition for `ClientCreateEndpoint` `DmsTransferSettings`

    The settings in JSON format for the DMS transfer type of source endpoint.

    Possible settings include the following:

    * ``ServiceAccessRoleArn`` - The IAM role that has permission to access the Amazon S3 bucket.

    * ``BucketName`` - The name of the S3 bucket to use.

    * ``CompressionType`` - An optional parameter to use GZIP to compress the target files. To use
    GZIP, set this value to ``NONE`` (the default). To keep the files uncompressed, don't use this
    value.

    Shorthand syntax for these settings is as follows:
    ``ServiceAccessRoleArn=string,BucketName=string,CompressionType=string``

    JSON syntax for these settings is as follows: ``{ "ServiceAccessRoleArn": "string", "BucketName":
    "string", "CompressionType": "none"|"gzip" }``

    - **ServiceAccessRoleArn** *(string) --*

      The IAM role that has permission to access the Amazon S3 bucket.

    - **BucketName** *(string) --*

      The name of the S3 bucket to use.
    """


_ClientCreateEndpointDynamoDbSettingsTypeDef = TypedDict(
    "_ClientCreateEndpointDynamoDbSettingsTypeDef", {"ServiceAccessRoleArn": str}
)


class ClientCreateEndpointDynamoDbSettingsTypeDef(
    _ClientCreateEndpointDynamoDbSettingsTypeDef
):
    """
    Type definition for `ClientCreateEndpoint` `DynamoDbSettings`

    Settings in JSON format for the target Amazon DynamoDB endpoint. For more information about the
    available settings, see `Using Object Mapping to Migrate Data to DynamoDB
    <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.DynamoDB.html>`__ in the *AWS
    Database Migration Service User Guide.*

    - **ServiceAccessRoleArn** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) used by the service access IAM role.
    """


_RequiredClientCreateEndpointElasticsearchSettingsTypeDef = TypedDict(
    "_RequiredClientCreateEndpointElasticsearchSettingsTypeDef",
    {"ServiceAccessRoleArn": str, "EndpointUri": str},
)
_OptionalClientCreateEndpointElasticsearchSettingsTypeDef = TypedDict(
    "_OptionalClientCreateEndpointElasticsearchSettingsTypeDef",
    {"FullLoadErrorPercentage": int, "ErrorRetryDuration": int},
    total=False,
)


class ClientCreateEndpointElasticsearchSettingsTypeDef(
    _RequiredClientCreateEndpointElasticsearchSettingsTypeDef,
    _OptionalClientCreateEndpointElasticsearchSettingsTypeDef,
):
    """
    Type definition for `ClientCreateEndpoint` `ElasticsearchSettings`

    Settings in JSON format for the target Elasticsearch endpoint. For more information about the
    available settings, see `Extra Connection Attributes When Using Elasticsearch as a Target for AWS
    DMS
    <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Elasticsearch.html#CHAP_Target.Elasticsearch.Configuration>`__
    in the *AWS Database Migration User Guide.*

    - **ServiceAccessRoleArn** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) used by service to access the IAM role.

    - **EndpointUri** *(string) --* **[REQUIRED]**

      The endpoint for the Elasticsearch cluster.

    - **FullLoadErrorPercentage** *(integer) --*

      The maximum percentage of records that can fail to be written before a full load operation
      stops.

    - **ErrorRetryDuration** *(integer) --*

      The maximum number of seconds that DMS retries failed API requests to the Elasticsearch cluster.
    """


_ClientCreateEndpointKinesisSettingsTypeDef = TypedDict(
    "_ClientCreateEndpointKinesisSettingsTypeDef",
    {"StreamArn": str, "MessageFormat": str, "ServiceAccessRoleArn": str},
    total=False,
)


class ClientCreateEndpointKinesisSettingsTypeDef(
    _ClientCreateEndpointKinesisSettingsTypeDef
):
    """
    Type definition for `ClientCreateEndpoint` `KinesisSettings`

    Settings in JSON format for the target Amazon Kinesis Data Streams endpoint. For more information
    about the available settings, see `Using Object Mapping to Migrate Data to a Kinesis Data Stream
    <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Kinesis.html#CHAP_Target.Kinesis.ObjectMapping>`__
    in the *AWS Database Migration User Guide.*

    - **StreamArn** *(string) --*

      The Amazon Resource Name (ARN) for the Amazon Kinesis Data Streams endpoint.

    - **MessageFormat** *(string) --*

      The output format for the records created on the endpoint. The message format is ``JSON`` .

    - **ServiceAccessRoleArn** *(string) --*

      The Amazon Resource Name (ARN) for the IAM role that DMS uses to write to the Amazon Kinesis
      data stream.
    """


_ClientCreateEndpointMongoDbSettingsTypeDef = TypedDict(
    "_ClientCreateEndpointMongoDbSettingsTypeDef",
    {
        "Username": str,
        "Password": str,
        "ServerName": str,
        "Port": int,
        "DatabaseName": str,
        "AuthType": str,
        "AuthMechanism": str,
        "NestingLevel": str,
        "ExtractDocId": str,
        "DocsToInvestigate": str,
        "AuthSource": str,
        "KmsKeyId": str,
    },
    total=False,
)


class ClientCreateEndpointMongoDbSettingsTypeDef(
    _ClientCreateEndpointMongoDbSettingsTypeDef
):
    """
    Type definition for `ClientCreateEndpoint` `MongoDbSettings`

    Settings in JSON format for the source MongoDB endpoint. For more information about the available
    settings, see the configuration properties section in `Using MongoDB as a Target for AWS Database
    Migration Service <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MongoDB.html>`__
    in the *AWS Database Migration Service User Guide.*

    - **Username** *(string) --*

      The user name you use to access the MongoDB source endpoint.

    - **Password** *(string) --*

      The password for the user account you use to access the MongoDB source endpoint.

    - **ServerName** *(string) --*

      The name of the server on the MongoDB source endpoint.

    - **Port** *(integer) --*

      The port value for the MongoDB source endpoint.

    - **DatabaseName** *(string) --*

      The database name on the MongoDB source endpoint.

    - **AuthType** *(string) --*

      The authentication type you use to access the MongoDB source endpoint.

      Valid values: NO, PASSWORD

      When NO is selected, user name and password parameters are not used and can be empty.

    - **AuthMechanism** *(string) --*

      The authentication mechanism you use to access the MongoDB source endpoint.

      Valid values: DEFAULT, MONGODB_CR, SCRAM_SHA_1

      DEFAULT – For MongoDB version 2.x, use MONGODB_CR. For MongoDB version 3.x, use SCRAM_SHA_1.
      This setting is not used when authType=No.

    - **NestingLevel** *(string) --*

      Specifies either document or table mode.

      Valid values: NONE, ONE

      Default value is NONE. Specify NONE to use document mode. Specify ONE to use table mode.

    - **ExtractDocId** *(string) --*

      Specifies the document ID. Use this setting when ``NestingLevel`` is set to NONE.

      Default value is false.

    - **DocsToInvestigate** *(string) --*

      Indicates the number of documents to preview to determine the document organization. Use this
      setting when ``NestingLevel`` is set to ONE.

      Must be a positive value greater than 0. Default value is 1000.

    - **AuthSource** *(string) --*

      The MongoDB database name. This setting is not used when ``authType=NO`` .

      The default is admin.

    - **KmsKeyId** *(string) --*

      The AWS KMS key identifier that is used to encrypt the content on the replication instance. If
      you don't specify a value for the ``KmsKeyId`` parameter, then AWS DMS uses your default
      encryption key. AWS KMS creates the default encryption key for your AWS account. Your AWS
      account has a different default encryption key for each AWS Region.
    """


_ClientCreateEndpointRedshiftSettingsTypeDef = TypedDict(
    "_ClientCreateEndpointRedshiftSettingsTypeDef",
    {
        "AcceptAnyDate": bool,
        "AfterConnectScript": str,
        "BucketFolder": str,
        "BucketName": str,
        "ConnectionTimeout": int,
        "DatabaseName": str,
        "DateFormat": str,
        "EmptyAsNull": bool,
        "EncryptionMode": str,
        "FileTransferUploadStreams": int,
        "LoadTimeout": int,
        "MaxFileSize": int,
        "Password": str,
        "Port": int,
        "RemoveQuotes": bool,
        "ReplaceInvalidChars": str,
        "ReplaceChars": str,
        "ServerName": str,
        "ServiceAccessRoleArn": str,
        "ServerSideEncryptionKmsKeyId": str,
        "TimeFormat": str,
        "TrimBlanks": bool,
        "TruncateColumns": bool,
        "Username": str,
        "WriteBufferSize": int,
    },
    total=False,
)


class ClientCreateEndpointRedshiftSettingsTypeDef(
    _ClientCreateEndpointRedshiftSettingsTypeDef
):
    """
    Type definition for `ClientCreateEndpoint` `RedshiftSettings`

    - **AcceptAnyDate** *(boolean) --*

      A value that indicates to allow any date format, including invalid formats such as 00/00/00
      00:00:00, to be loaded without generating an error. You can choose ``true`` or ``false`` (the
      default).

      This parameter applies only to TIMESTAMP and DATE columns. Always use ACCEPTANYDATE with the
      DATEFORMAT parameter. If the date format for the data doesn't match the DATEFORMAT
      specification, Amazon Redshift inserts a NULL value into that field.

    - **AfterConnectScript** *(string) --*

      Code to run after connecting. This parameter should contain the code itself, not the name of a
      file containing the code.

    - **BucketFolder** *(string) --*

      The location where the comma-separated value (.csv) files are stored before being uploaded to
      the S3 bucket.

    - **BucketName** *(string) --*

      The name of the S3 bucket you want to use

    - **ConnectionTimeout** *(integer) --*

      A value that sets the amount of time to wait (in milliseconds) before timing out, beginning
      from when you initially establish a connection.

    - **DatabaseName** *(string) --*

      The name of the Amazon Redshift data warehouse (service) that you are working with.

    - **DateFormat** *(string) --*

      The date format that you are using. Valid values are ``auto`` (case-sensitive), your date
      format string enclosed in quotes, or NULL. If this parameter is left unset (NULL), it defaults
      to a format of 'YYYY-MM-DD'. Using ``auto`` recognizes most strings, even some that aren't
      supported when you use a date format string.

      If your date and time values use formats different from each other, set this to ``auto`` .

    - **EmptyAsNull** *(boolean) --*

      A value that specifies whether AWS DMS should migrate empty CHAR and VARCHAR fields as NULL. A
      value of ``true`` sets empty CHAR and VARCHAR fields to null. The default is ``false`` .

    - **EncryptionMode** *(string) --*

      The type of server-side encryption that you want to use for your data. This encryption type is
      part of the endpoint settings or the extra connections attributes for Amazon S3. You can choose
      either ``SSE_S3`` (the default) or ``SSE_KMS`` . To use ``SSE_S3`` , create an AWS Identity and
      Access Management (IAM) role with a policy that allows ``"arn:aws:s3:::*"`` to use the
      following actions: ``"s3:PutObject", "s3:ListBucket"``

    - **FileTransferUploadStreams** *(integer) --*

      The number of threads used to upload a single file. This parameter accepts a value from 1
      through 64. It defaults to 10.

    - **LoadTimeout** *(integer) --*

      The amount of time to wait (in milliseconds) before timing out, beginning from when you begin
      loading.

    - **MaxFileSize** *(integer) --*

      The maximum size (in KB) of any .csv file used to transfer data to Amazon Redshift. This
      accepts a value from 1 through 1,048,576. It defaults to 32,768 KB (32 MB).

    - **Password** *(string) --*

      The password for the user named in the ``username`` property.

    - **Port** *(integer) --*

      The port number for Amazon Redshift. The default value is 5439.

    - **RemoveQuotes** *(boolean) --*

      A value that specifies to remove surrounding quotation marks from strings in the incoming data.
      All characters within the quotation marks, including delimiters, are retained. Choose ``true``
      to remove quotation marks. The default is ``false`` .

    - **ReplaceInvalidChars** *(string) --*

      A list of characters that you want to replace. Use with ``ReplaceChars`` .

    - **ReplaceChars** *(string) --*

      A value that specifies to replaces the invalid characters specified in ``ReplaceInvalidChars``
      , substituting the specified characters instead. The default is ``"?"`` .

    - **ServerName** *(string) --*

      The name of the Amazon Redshift cluster you are using.

    - **ServiceAccessRoleArn** *(string) --*

      The Amazon Resource Name (ARN) of the IAM role that has access to the Amazon Redshift service.

    - **ServerSideEncryptionKmsKeyId** *(string) --*

      The AWS KMS key ID. If you are using ``SSE_KMS`` for the ``EncryptionMode`` , provide this key
      ID. The key that you use needs an attached policy that enables IAM user permissions and allows
      use of the key.

    - **TimeFormat** *(string) --*

      The time format that you want to use. Valid values are ``auto`` (case-sensitive),
      ``'timeformat_string'`` , ``'epochsecs'`` , or ``'epochmillisecs'`` . It defaults to 10. Using
      ``auto`` recognizes most strings, even some that aren't supported when you use a time format
      string.

      If your date and time values use formats different from each other, set this parameter to
      ``auto`` .

    - **TrimBlanks** *(boolean) --*

      A value that specifies to remove the trailing white space characters from a VARCHAR string.
      This parameter applies only to columns with a VARCHAR data type. Choose ``true`` to remove
      unneeded white space. The default is ``false`` .

    - **TruncateColumns** *(boolean) --*

      A value that specifies to truncate data in columns to the appropriate number of characters, so
      that the data fits in the column. This parameter applies only to columns with a VARCHAR or CHAR
      data type, and rows with a size of 4 MB or less. Choose ``true`` to truncate data. The default
      is ``false`` .

    - **Username** *(string) --*

      An Amazon Redshift user name for a registered user.

    - **WriteBufferSize** *(integer) --*

      The size of the write buffer to use in rows. Valid values range from 1 through 2,048. The
      default is 1,024. Use this setting to tune performance.
    """


_ClientCreateEndpointResponseEndpointDmsTransferSettingsTypeDef = TypedDict(
    "_ClientCreateEndpointResponseEndpointDmsTransferSettingsTypeDef",
    {"ServiceAccessRoleArn": str, "BucketName": str},
    total=False,
)


class ClientCreateEndpointResponseEndpointDmsTransferSettingsTypeDef(
    _ClientCreateEndpointResponseEndpointDmsTransferSettingsTypeDef
):
    """
    Type definition for `ClientCreateEndpointResponseEndpoint` `DmsTransferSettings`

    The settings in JSON format for the DMS transfer type of source endpoint.

    Possible settings include the following:

    * ``ServiceAccessRoleArn`` - The IAM role that has permission to access the Amazon S3
    bucket.

    * ``BucketName`` - The name of the S3 bucket to use.

    * ``CompressionType`` - An optional parameter to use GZIP to compress the target files. To
    use GZIP, set this value to ``NONE`` (the default). To keep the files uncompressed, don't
    use this value.

    Shorthand syntax for these settings is as follows:
    ``ServiceAccessRoleArn=string,BucketName=string,CompressionType=string``

    JSON syntax for these settings is as follows: ``{ "ServiceAccessRoleArn": "string",
    "BucketName": "string", "CompressionType": "none"|"gzip" }``

    - **ServiceAccessRoleArn** *(string) --*

      The IAM role that has permission to access the Amazon S3 bucket.

    - **BucketName** *(string) --*

      The name of the S3 bucket to use.
    """


_ClientCreateEndpointResponseEndpointDynamoDbSettingsTypeDef = TypedDict(
    "_ClientCreateEndpointResponseEndpointDynamoDbSettingsTypeDef",
    {"ServiceAccessRoleArn": str},
    total=False,
)


class ClientCreateEndpointResponseEndpointDynamoDbSettingsTypeDef(
    _ClientCreateEndpointResponseEndpointDynamoDbSettingsTypeDef
):
    """
    Type definition for `ClientCreateEndpointResponseEndpoint` `DynamoDbSettings`

    The settings for the target DynamoDB database. For more information, see the
    ``DynamoDBSettings`` structure.

    - **ServiceAccessRoleArn** *(string) --*

      The Amazon Resource Name (ARN) used by the service access IAM role.
    """


_ClientCreateEndpointResponseEndpointElasticsearchSettingsTypeDef = TypedDict(
    "_ClientCreateEndpointResponseEndpointElasticsearchSettingsTypeDef",
    {
        "ServiceAccessRoleArn": str,
        "EndpointUri": str,
        "FullLoadErrorPercentage": int,
        "ErrorRetryDuration": int,
    },
    total=False,
)


class ClientCreateEndpointResponseEndpointElasticsearchSettingsTypeDef(
    _ClientCreateEndpointResponseEndpointElasticsearchSettingsTypeDef
):
    """
    Type definition for `ClientCreateEndpointResponseEndpoint` `ElasticsearchSettings`

    The settings for the Elasticsearch source endpoint. For more information, see the
    ``ElasticsearchSettings`` structure.

    - **ServiceAccessRoleArn** *(string) --*

      The Amazon Resource Name (ARN) used by service to access the IAM role.

    - **EndpointUri** *(string) --*

      The endpoint for the Elasticsearch cluster.

    - **FullLoadErrorPercentage** *(integer) --*

      The maximum percentage of records that can fail to be written before a full load
      operation stops.

    - **ErrorRetryDuration** *(integer) --*

      The maximum number of seconds that DMS retries failed API requests to the Elasticsearch
      cluster.
    """


_ClientCreateEndpointResponseEndpointKinesisSettingsTypeDef = TypedDict(
    "_ClientCreateEndpointResponseEndpointKinesisSettingsTypeDef",
    {"StreamArn": str, "MessageFormat": str, "ServiceAccessRoleArn": str},
    total=False,
)


class ClientCreateEndpointResponseEndpointKinesisSettingsTypeDef(
    _ClientCreateEndpointResponseEndpointKinesisSettingsTypeDef
):
    """
    Type definition for `ClientCreateEndpointResponseEndpoint` `KinesisSettings`

    The settings for the Amazon Kinesis source endpoint. For more information, see the
    ``KinesisSettings`` structure.

    - **StreamArn** *(string) --*

      The Amazon Resource Name (ARN) for the Amazon Kinesis Data Streams endpoint.

    - **MessageFormat** *(string) --*

      The output format for the records created on the endpoint. The message format is ``JSON``
      .

    - **ServiceAccessRoleArn** *(string) --*

      The Amazon Resource Name (ARN) for the IAM role that DMS uses to write to the Amazon
      Kinesis data stream.
    """


_ClientCreateEndpointResponseEndpointMongoDbSettingsTypeDef = TypedDict(
    "_ClientCreateEndpointResponseEndpointMongoDbSettingsTypeDef",
    {
        "Username": str,
        "Password": str,
        "ServerName": str,
        "Port": int,
        "DatabaseName": str,
        "AuthType": str,
        "AuthMechanism": str,
        "NestingLevel": str,
        "ExtractDocId": str,
        "DocsToInvestigate": str,
        "AuthSource": str,
        "KmsKeyId": str,
    },
    total=False,
)


class ClientCreateEndpointResponseEndpointMongoDbSettingsTypeDef(
    _ClientCreateEndpointResponseEndpointMongoDbSettingsTypeDef
):
    """
    Type definition for `ClientCreateEndpointResponseEndpoint` `MongoDbSettings`

    The settings for the MongoDB source endpoint. For more information, see the
    ``MongoDbSettings`` structure.

    - **Username** *(string) --*

      The user name you use to access the MongoDB source endpoint.

    - **Password** *(string) --*

      The password for the user account you use to access the MongoDB source endpoint.

    - **ServerName** *(string) --*

      The name of the server on the MongoDB source endpoint.

    - **Port** *(integer) --*

      The port value for the MongoDB source endpoint.

    - **DatabaseName** *(string) --*

      The database name on the MongoDB source endpoint.

    - **AuthType** *(string) --*

      The authentication type you use to access the MongoDB source endpoint.

      Valid values: NO, PASSWORD

      When NO is selected, user name and password parameters are not used and can be empty.

    - **AuthMechanism** *(string) --*

      The authentication mechanism you use to access the MongoDB source endpoint.

      Valid values: DEFAULT, MONGODB_CR, SCRAM_SHA_1

      DEFAULT – For MongoDB version 2.x, use MONGODB_CR. For MongoDB version 3.x, use
      SCRAM_SHA_1. This setting is not used when authType=No.

    - **NestingLevel** *(string) --*

      Specifies either document or table mode.

      Valid values: NONE, ONE

      Default value is NONE. Specify NONE to use document mode. Specify ONE to use table mode.

    - **ExtractDocId** *(string) --*

      Specifies the document ID. Use this setting when ``NestingLevel`` is set to NONE.

      Default value is false.

    - **DocsToInvestigate** *(string) --*

      Indicates the number of documents to preview to determine the document organization. Use
      this setting when ``NestingLevel`` is set to ONE.

      Must be a positive value greater than 0. Default value is 1000.

    - **AuthSource** *(string) --*

      The MongoDB database name. This setting is not used when ``authType=NO`` .

      The default is admin.

    - **KmsKeyId** *(string) --*

      The AWS KMS key identifier that is used to encrypt the content on the replication
      instance. If you don't specify a value for the ``KmsKeyId`` parameter, then AWS DMS uses
      your default encryption key. AWS KMS creates the default encryption key for your AWS
      account. Your AWS account has a different default encryption key for each AWS Region.
    """


_ClientCreateEndpointResponseEndpointRedshiftSettingsTypeDef = TypedDict(
    "_ClientCreateEndpointResponseEndpointRedshiftSettingsTypeDef",
    {
        "AcceptAnyDate": bool,
        "AfterConnectScript": str,
        "BucketFolder": str,
        "BucketName": str,
        "ConnectionTimeout": int,
        "DatabaseName": str,
        "DateFormat": str,
        "EmptyAsNull": bool,
        "EncryptionMode": str,
        "FileTransferUploadStreams": int,
        "LoadTimeout": int,
        "MaxFileSize": int,
        "Password": str,
        "Port": int,
        "RemoveQuotes": bool,
        "ReplaceInvalidChars": str,
        "ReplaceChars": str,
        "ServerName": str,
        "ServiceAccessRoleArn": str,
        "ServerSideEncryptionKmsKeyId": str,
        "TimeFormat": str,
        "TrimBlanks": bool,
        "TruncateColumns": bool,
        "Username": str,
        "WriteBufferSize": int,
    },
    total=False,
)


class ClientCreateEndpointResponseEndpointRedshiftSettingsTypeDef(
    _ClientCreateEndpointResponseEndpointRedshiftSettingsTypeDef
):
    """
    Type definition for `ClientCreateEndpointResponseEndpoint` `RedshiftSettings`

    Settings for the Amazon Redshift endpoint.

    - **AcceptAnyDate** *(boolean) --*

      A value that indicates to allow any date format, including invalid formats such as
      00/00/00 00:00:00, to be loaded without generating an error. You can choose ``true`` or
      ``false`` (the default).

      This parameter applies only to TIMESTAMP and DATE columns. Always use ACCEPTANYDATE with
      the DATEFORMAT parameter. If the date format for the data doesn't match the DATEFORMAT
      specification, Amazon Redshift inserts a NULL value into that field.

    - **AfterConnectScript** *(string) --*

      Code to run after connecting. This parameter should contain the code itself, not the name
      of a file containing the code.

    - **BucketFolder** *(string) --*

      The location where the comma-separated value (.csv) files are stored before being
      uploaded to the S3 bucket.

    - **BucketName** *(string) --*

      The name of the S3 bucket you want to use

    - **ConnectionTimeout** *(integer) --*

      A value that sets the amount of time to wait (in milliseconds) before timing out,
      beginning from when you initially establish a connection.

    - **DatabaseName** *(string) --*

      The name of the Amazon Redshift data warehouse (service) that you are working with.

    - **DateFormat** *(string) --*

      The date format that you are using. Valid values are ``auto`` (case-sensitive), your date
      format string enclosed in quotes, or NULL. If this parameter is left unset (NULL), it
      defaults to a format of 'YYYY-MM-DD'. Using ``auto`` recognizes most strings, even some
      that aren't supported when you use a date format string.

      If your date and time values use formats different from each other, set this to ``auto`` .

    - **EmptyAsNull** *(boolean) --*

      A value that specifies whether AWS DMS should migrate empty CHAR and VARCHAR fields as
      NULL. A value of ``true`` sets empty CHAR and VARCHAR fields to null. The default is
      ``false`` .

    - **EncryptionMode** *(string) --*

      The type of server-side encryption that you want to use for your data. This encryption
      type is part of the endpoint settings or the extra connections attributes for Amazon S3.
      You can choose either ``SSE_S3`` (the default) or ``SSE_KMS`` . To use ``SSE_S3`` ,
      create an AWS Identity and Access Management (IAM) role with a policy that allows
      ``"arn:aws:s3:::*"`` to use the following actions: ``"s3:PutObject", "s3:ListBucket"``

    - **FileTransferUploadStreams** *(integer) --*

      The number of threads used to upload a single file. This parameter accepts a value from 1
      through 64. It defaults to 10.

    - **LoadTimeout** *(integer) --*

      The amount of time to wait (in milliseconds) before timing out, beginning from when you
      begin loading.

    - **MaxFileSize** *(integer) --*

      The maximum size (in KB) of any .csv file used to transfer data to Amazon Redshift. This
      accepts a value from 1 through 1,048,576. It defaults to 32,768 KB (32 MB).

    - **Password** *(string) --*

      The password for the user named in the ``username`` property.

    - **Port** *(integer) --*

      The port number for Amazon Redshift. The default value is 5439.

    - **RemoveQuotes** *(boolean) --*

      A value that specifies to remove surrounding quotation marks from strings in the incoming
      data. All characters within the quotation marks, including delimiters, are retained.
      Choose ``true`` to remove quotation marks. The default is ``false`` .

    - **ReplaceInvalidChars** *(string) --*

      A list of characters that you want to replace. Use with ``ReplaceChars`` .

    - **ReplaceChars** *(string) --*

      A value that specifies to replaces the invalid characters specified in
      ``ReplaceInvalidChars`` , substituting the specified characters instead. The default is
      ``"?"`` .

    - **ServerName** *(string) --*

      The name of the Amazon Redshift cluster you are using.

    - **ServiceAccessRoleArn** *(string) --*

      The Amazon Resource Name (ARN) of the IAM role that has access to the Amazon Redshift
      service.

    - **ServerSideEncryptionKmsKeyId** *(string) --*

      The AWS KMS key ID. If you are using ``SSE_KMS`` for the ``EncryptionMode`` , provide
      this key ID. The key that you use needs an attached policy that enables IAM user
      permissions and allows use of the key.

    - **TimeFormat** *(string) --*

      The time format that you want to use. Valid values are ``auto`` (case-sensitive),
      ``'timeformat_string'`` , ``'epochsecs'`` , or ``'epochmillisecs'`` . It defaults to 10.
      Using ``auto`` recognizes most strings, even some that aren't supported when you use a
      time format string.

      If your date and time values use formats different from each other, set this parameter to
      ``auto`` .

    - **TrimBlanks** *(boolean) --*

      A value that specifies to remove the trailing white space characters from a VARCHAR
      string. This parameter applies only to columns with a VARCHAR data type. Choose ``true``
      to remove unneeded white space. The default is ``false`` .

    - **TruncateColumns** *(boolean) --*

      A value that specifies to truncate data in columns to the appropriate number of
      characters, so that the data fits in the column. This parameter applies only to columns
      with a VARCHAR or CHAR data type, and rows with a size of 4 MB or less. Choose ``true``
      to truncate data. The default is ``false`` .

    - **Username** *(string) --*

      An Amazon Redshift user name for a registered user.

    - **WriteBufferSize** *(integer) --*

      The size of the write buffer to use in rows. Valid values range from 1 through 2,048. The
      default is 1,024. Use this setting to tune performance.
    """


_ClientCreateEndpointResponseEndpointS3SettingsTypeDef = TypedDict(
    "_ClientCreateEndpointResponseEndpointS3SettingsTypeDef",
    {
        "ServiceAccessRoleArn": str,
        "ExternalTableDefinition": str,
        "CsvRowDelimiter": str,
        "CsvDelimiter": str,
        "BucketFolder": str,
        "BucketName": str,
        "CompressionType": str,
        "EncryptionMode": str,
        "ServerSideEncryptionKmsKeyId": str,
        "DataFormat": str,
        "EncodingType": str,
        "DictPageSizeLimit": int,
        "RowGroupLength": int,
        "DataPageSize": int,
        "ParquetVersion": str,
        "EnableStatistics": bool,
        "IncludeOpForFullLoad": bool,
        "CdcInsertsOnly": bool,
        "TimestampColumnName": str,
        "ParquetTimestampInMillisecond": bool,
    },
    total=False,
)


class ClientCreateEndpointResponseEndpointS3SettingsTypeDef(
    _ClientCreateEndpointResponseEndpointS3SettingsTypeDef
):
    """
    Type definition for `ClientCreateEndpointResponseEndpoint` `S3Settings`

    The settings for the S3 target endpoint. For more information, see the ``S3Settings``
    structure.

    - **ServiceAccessRoleArn** *(string) --*

      The Amazon Resource Name (ARN) used by the service access IAM role.

    - **ExternalTableDefinition** *(string) --*

      The external table definition.

    - **CsvRowDelimiter** *(string) --*

      The delimiter used to separate rows in the source files. The default is a carriage return
      (``\\n`` ).

    - **CsvDelimiter** *(string) --*

      The delimiter used to separate columns in the source files. The default is a comma.

    - **BucketFolder** *(string) --*

      An optional parameter to set a folder name in the S3 bucket. If provided, tables are
      created in the path `` *bucketFolder* /*schema_name* /*table_name* /`` . If this
      parameter is not specified, then the path used is `` *schema_name* /*table_name* /`` .

    - **BucketName** *(string) --*

      The name of the S3 bucket.

    - **CompressionType** *(string) --*

      An optional parameter to use GZIP to compress the target files. Set to GZIP to compress
      the target files. Set to NONE (the default) or do not use to leave the files
      uncompressed. Applies to both .csv and .parquet file formats.

    - **EncryptionMode** *(string) --*

      The type of server-side encryption that you want to use for your data. This encryption
      type is part of the endpoint settings or the extra connections attributes for Amazon S3.
      You can choose either ``SSE_S3`` (the default) or ``SSE_KMS`` . To use ``SSE_S3`` , you
      need an AWS Identity and Access Management (IAM) role with permission to allow
      ``"arn:aws:s3:::dms-*"`` to use the following actions:

      * ``s3:CreateBucket``

      * ``s3:ListBucket``

      * ``s3:DeleteBucket``

      * ``s3:GetBucketLocation``

      * ``s3:GetObject``

      * ``s3:PutObject``

      * ``s3:DeleteObject``

      * ``s3:GetObjectVersion``

      * ``s3:GetBucketPolicy``

      * ``s3:PutBucketPolicy``

      * ``s3:DeleteBucketPolicy``

    - **ServerSideEncryptionKmsKeyId** *(string) --*

      If you are using ``SSE_KMS`` for the ``EncryptionMode`` , provide the AWS KMS key ID. The
      key that you use needs an attached policy that enables AWS Identity and Access Management
      (IAM) user permissions and allows use of the key.

      Here is a CLI example: ``aws dms create-endpoint --endpoint-identifier *value*
      --endpoint-type target --engine-name s3 --s3-settings ServiceAccessRoleArn=*value*
      ,BucketFolder=*value* ,BucketName=*value*
      ,EncryptionMode=SSE_KMS,ServerSideEncryptionKmsKeyId=*value* ``

    - **DataFormat** *(string) --*

      The format of the data that you want to use for output. You can choose one of the
      following:

      * ``csv`` : This is a row-based file format with comma-separated values (.csv).

      * ``parquet`` : Apache Parquet (.parquet) is a columnar storage file format that features
      efficient compression and provides faster query response.

    - **EncodingType** *(string) --*

      The type of encoding you are using:

      * ``RLE_DICTIONARY`` uses a combination of bit-packing and run-length encoding to store
      repeated values more efficiently. This is the default.

      * ``PLAIN`` doesn't use encoding at all. Values are stored as they are.

      * ``PLAIN_DICTIONARY`` builds a dictionary of the values encountered in a given column.
      The dictionary is stored in a dictionary page for each column chunk.

    - **DictPageSizeLimit** *(integer) --*

      The maximum size of an encoded dictionary page of a column. If the dictionary page
      exceeds this, this column is stored using an encoding type of ``PLAIN`` . This parameter
      defaults to 1024 * 1024 bytes (1 MiB), the maximum size of a dictionary page before it
      reverts to ``PLAIN`` encoding. This size is used for .parquet file format only.

    - **RowGroupLength** *(integer) --*

      The number of rows in a row group. A smaller row group size provides faster reads. But as
      the number of row groups grows, the slower writes become. This parameter defaults to
      10,000 rows. This number is used for .parquet file format only.

      If you choose a value larger than the maximum, ``RowGroupLength`` is set to the max row
      group length in bytes (64 * 1024 * 1024).

    - **DataPageSize** *(integer) --*

      The size of one data page in bytes. This parameter defaults to 1024 * 1024 bytes (1 MiB).
      This number is used for .parquet file format only.

    - **ParquetVersion** *(string) --*

      The version of the Apache Parquet format that you want to use: ``parquet_1_0`` (the
      default) or ``parquet_2_0`` .

    - **EnableStatistics** *(boolean) --*

      A value that enables statistics for Parquet pages and row groups. Choose ``true`` to
      enable statistics, ``false`` to disable. Statistics include ``NULL`` , ``DISTINCT`` ,
      ``MAX`` , and ``MIN`` values. This parameter defaults to ``true`` . This value is used
      for .parquet file format only.

    - **IncludeOpForFullLoad** *(boolean) --*

      A value that enables a full load to write INSERT operations to the comma-separated value
      (.csv) output files only to indicate how the rows were added to the source database.

      .. note::

        AWS DMS supports the ``IncludeOpForFullLoad`` parameter in versions 3.1.4 and later.

      For full load, records can only be inserted. By default (the ``false`` setting), no
      information is recorded in these output files for a full load to indicate that the rows
      were inserted at the source database. If ``IncludeOpForFullLoad`` is set to ``true`` or
      ``y`` , the INSERT is recorded as an I annotation in the first field of the .csv file.
      This allows the format of your target records from a full load to be consistent with the
      target records from a CDC load.

      .. note::

        This setting works together with the ``CdcInsertsOnly`` parameter for output to .csv
        files only. For more information about how these settings work together, see
        `Indicating Source DB Operations in Migrated S3 Data
        <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring.InsertOps>`__
        in the *AWS Database Migration Service User Guide.* .

    - **CdcInsertsOnly** *(boolean) --*

      A value that enables a change data capture (CDC) load to write only INSERT operations to
      .csv or columnar storage (.parquet) output files. By default (the ``false`` setting), the
      first field in a .csv or .parquet record contains the letter I (INSERT), U (UPDATE), or D
      (DELETE). These values indicate whether the row was inserted, updated, or deleted at the
      source database for a CDC load to the target.

      If ``CdcInsertsOnly`` is set to ``true`` or ``y`` , only INSERTs from the source database
      are migrated to the .csv or .parquet file. For .csv format only, how these INSERTs are
      recorded depends on the value of ``IncludeOpForFullLoad`` . If ``IncludeOpForFullLoad``
      is set to ``true`` , the first field of every CDC record is set to I to indicate the
      INSERT operation at the source. If ``IncludeOpForFullLoad`` is set to ``false`` , every
      CDC record is written without a first field to indicate the INSERT operation at the
      source. For more information about how these settings work together, see `Indicating
      Source DB Operations in Migrated S3 Data
      <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring.InsertOps>`__
      in the *AWS Database Migration Service User Guide.* .

      .. note::

        AWS DMS supports this interaction between the ``CdcInsertsOnly`` and
        ``IncludeOpForFullLoad`` parameters in versions 3.1.4 and later.

    - **TimestampColumnName** *(string) --*

      A value that when nonblank causes AWS DMS to add a column with timestamp information to
      the endpoint data for an Amazon S3 target.

      .. note::

        AWS DMS supports the ``TimestampColumnName`` parameter in versions 3.1.4 and later.

      DMS includes an additional ``STRING`` column in the .csv or .parquet object files of your
      migrated data when you set ``TimestampColumnName`` to a nonblank value.

      For a full load, each row of this timestamp column contains a timestamp for when the data
      was transferred from the source to the target by DMS.

      For a change data capture (CDC) load, each row of the timestamp column contains the
      timestamp for the commit of that row in the source database.

      The string format for this timestamp column value is ``yyyy-MM-dd HH:mm:ss.SSSSSS`` . By
      default, the precision of this value is in microseconds. For a CDC load, the rounding of
      the precision depends on the commit timestamp supported by DMS for the source database.

      When the ``AddColumnName`` parameter is set to ``true`` , DMS also includes a name for
      the timestamp column that you set with ``TimestampColumnName`` .

    - **ParquetTimestampInMillisecond** *(boolean) --*

      A value that specifies the precision of any ``TIMESTAMP`` column values that are written
      to an Amazon S3 object file in .parquet format.

      .. note::

        AWS DMS supports the ``ParquetTimestampInMillisecond`` parameter in versions 3.1.4 and
        later.

      When ``ParquetTimestampInMillisecond`` is set to ``true`` or ``y`` , AWS DMS writes all
      ``TIMESTAMP`` columns in a .parquet formatted file with millisecond precision. Otherwise,
      DMS writes them with microsecond precision.

      Currently, Amazon Athena and AWS Glue can handle only millisecond precision for
      ``TIMESTAMP`` values. Set this parameter to ``true`` for S3 endpoint object files that
      are .parquet formatted only if you plan to query or process the data with Athena or AWS
      Glue.

      .. note::

        AWS DMS writes any ``TIMESTAMP`` column values written to an S3 file in .csv format
        with microsecond precision.

        Setting ``ParquetTimestampInMillisecond`` has no effect on the string format of the
        timestamp column value that is inserted by setting the ``TimestampColumnName``
        parameter.
    """


_ClientCreateEndpointResponseEndpointTypeDef = TypedDict(
    "_ClientCreateEndpointResponseEndpointTypeDef",
    {
        "EndpointIdentifier": str,
        "EndpointType": str,
        "EngineName": str,
        "EngineDisplayName": str,
        "Username": str,
        "ServerName": str,
        "Port": int,
        "DatabaseName": str,
        "ExtraConnectionAttributes": str,
        "Status": str,
        "KmsKeyId": str,
        "EndpointArn": str,
        "CertificateArn": str,
        "SslMode": str,
        "ServiceAccessRoleArn": str,
        "ExternalTableDefinition": str,
        "ExternalId": str,
        "DynamoDbSettings": ClientCreateEndpointResponseEndpointDynamoDbSettingsTypeDef,
        "S3Settings": ClientCreateEndpointResponseEndpointS3SettingsTypeDef,
        "DmsTransferSettings": ClientCreateEndpointResponseEndpointDmsTransferSettingsTypeDef,
        "MongoDbSettings": ClientCreateEndpointResponseEndpointMongoDbSettingsTypeDef,
        "KinesisSettings": ClientCreateEndpointResponseEndpointKinesisSettingsTypeDef,
        "ElasticsearchSettings": ClientCreateEndpointResponseEndpointElasticsearchSettingsTypeDef,
        "RedshiftSettings": ClientCreateEndpointResponseEndpointRedshiftSettingsTypeDef,
    },
    total=False,
)


class ClientCreateEndpointResponseEndpointTypeDef(
    _ClientCreateEndpointResponseEndpointTypeDef
):
    """
    Type definition for `ClientCreateEndpointResponse` `Endpoint`

    The endpoint that was created.

    - **EndpointIdentifier** *(string) --*

      The database endpoint identifier. Identifiers must begin with a letter; must contain only
      ASCII letters, digits, and hyphens; and must not end with a hyphen or contain two
      consecutive hyphens.

    - **EndpointType** *(string) --*

      The type of endpoint. Valid values are ``source`` and ``target`` .

    - **EngineName** *(string) --*

      The database engine name. Valid values, depending on the EndpointType, include mysql,
      oracle, postgres, mariadb, aurora, aurora-postgresql, redshift, s3, db2, azuredb, sybase,
      dynamodb, mongodb, and sqlserver.

    - **EngineDisplayName** *(string) --*

      The expanded name for the engine name. For example, if the ``EngineName`` parameter is
      "aurora," this value would be "Amazon Aurora MySQL."

    - **Username** *(string) --*

      The user name used to connect to the endpoint.

    - **ServerName** *(string) --*

      The name of the server at the endpoint.

    - **Port** *(integer) --*

      The port value used to access the endpoint.

    - **DatabaseName** *(string) --*

      The name of the database at the endpoint.

    - **ExtraConnectionAttributes** *(string) --*

      Additional connection attributes used to connect to the endpoint.

    - **Status** *(string) --*

      The status of the endpoint.

    - **KmsKeyId** *(string) --*

      An AWS KMS key identifier that is used to encrypt the connection parameters for the
      endpoint.

      If you don't specify a value for the ``KmsKeyId`` parameter, then AWS DMS uses your default
      encryption key.

      AWS KMS creates the default encryption key for your AWS account. Your AWS account has a
      different default encryption key for each AWS Region.

    - **EndpointArn** *(string) --*

      The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

    - **CertificateArn** *(string) --*

      The Amazon Resource Name (ARN) used for SSL connection to the endpoint.

    - **SslMode** *(string) --*

      The SSL mode used to connect to the endpoint. The default value is ``none`` .

    - **ServiceAccessRoleArn** *(string) --*

      The Amazon Resource Name (ARN) used by the service access IAM role.

    - **ExternalTableDefinition** *(string) --*

      The external table definition.

    - **ExternalId** *(string) --*

      Value returned by a call to CreateEndpoint that can be used for cross-account validation.
      Use it on a subsequent call to CreateEndpoint to create the endpoint with a cross-account.

    - **DynamoDbSettings** *(dict) --*

      The settings for the target DynamoDB database. For more information, see the
      ``DynamoDBSettings`` structure.

      - **ServiceAccessRoleArn** *(string) --*

        The Amazon Resource Name (ARN) used by the service access IAM role.

    - **S3Settings** *(dict) --*

      The settings for the S3 target endpoint. For more information, see the ``S3Settings``
      structure.

      - **ServiceAccessRoleArn** *(string) --*

        The Amazon Resource Name (ARN) used by the service access IAM role.

      - **ExternalTableDefinition** *(string) --*

        The external table definition.

      - **CsvRowDelimiter** *(string) --*

        The delimiter used to separate rows in the source files. The default is a carriage return
        (``\\n`` ).

      - **CsvDelimiter** *(string) --*

        The delimiter used to separate columns in the source files. The default is a comma.

      - **BucketFolder** *(string) --*

        An optional parameter to set a folder name in the S3 bucket. If provided, tables are
        created in the path `` *bucketFolder* /*schema_name* /*table_name* /`` . If this
        parameter is not specified, then the path used is `` *schema_name* /*table_name* /`` .

      - **BucketName** *(string) --*

        The name of the S3 bucket.

      - **CompressionType** *(string) --*

        An optional parameter to use GZIP to compress the target files. Set to GZIP to compress
        the target files. Set to NONE (the default) or do not use to leave the files
        uncompressed. Applies to both .csv and .parquet file formats.

      - **EncryptionMode** *(string) --*

        The type of server-side encryption that you want to use for your data. This encryption
        type is part of the endpoint settings or the extra connections attributes for Amazon S3.
        You can choose either ``SSE_S3`` (the default) or ``SSE_KMS`` . To use ``SSE_S3`` , you
        need an AWS Identity and Access Management (IAM) role with permission to allow
        ``"arn:aws:s3:::dms-*"`` to use the following actions:

        * ``s3:CreateBucket``

        * ``s3:ListBucket``

        * ``s3:DeleteBucket``

        * ``s3:GetBucketLocation``

        * ``s3:GetObject``

        * ``s3:PutObject``

        * ``s3:DeleteObject``

        * ``s3:GetObjectVersion``

        * ``s3:GetBucketPolicy``

        * ``s3:PutBucketPolicy``

        * ``s3:DeleteBucketPolicy``

      - **ServerSideEncryptionKmsKeyId** *(string) --*

        If you are using ``SSE_KMS`` for the ``EncryptionMode`` , provide the AWS KMS key ID. The
        key that you use needs an attached policy that enables AWS Identity and Access Management
        (IAM) user permissions and allows use of the key.

        Here is a CLI example: ``aws dms create-endpoint --endpoint-identifier *value*
        --endpoint-type target --engine-name s3 --s3-settings ServiceAccessRoleArn=*value*
        ,BucketFolder=*value* ,BucketName=*value*
        ,EncryptionMode=SSE_KMS,ServerSideEncryptionKmsKeyId=*value* ``

      - **DataFormat** *(string) --*

        The format of the data that you want to use for output. You can choose one of the
        following:

        * ``csv`` : This is a row-based file format with comma-separated values (.csv).

        * ``parquet`` : Apache Parquet (.parquet) is a columnar storage file format that features
        efficient compression and provides faster query response.

      - **EncodingType** *(string) --*

        The type of encoding you are using:

        * ``RLE_DICTIONARY`` uses a combination of bit-packing and run-length encoding to store
        repeated values more efficiently. This is the default.

        * ``PLAIN`` doesn't use encoding at all. Values are stored as they are.

        * ``PLAIN_DICTIONARY`` builds a dictionary of the values encountered in a given column.
        The dictionary is stored in a dictionary page for each column chunk.

      - **DictPageSizeLimit** *(integer) --*

        The maximum size of an encoded dictionary page of a column. If the dictionary page
        exceeds this, this column is stored using an encoding type of ``PLAIN`` . This parameter
        defaults to 1024 * 1024 bytes (1 MiB), the maximum size of a dictionary page before it
        reverts to ``PLAIN`` encoding. This size is used for .parquet file format only.

      - **RowGroupLength** *(integer) --*

        The number of rows in a row group. A smaller row group size provides faster reads. But as
        the number of row groups grows, the slower writes become. This parameter defaults to
        10,000 rows. This number is used for .parquet file format only.

        If you choose a value larger than the maximum, ``RowGroupLength`` is set to the max row
        group length in bytes (64 * 1024 * 1024).

      - **DataPageSize** *(integer) --*

        The size of one data page in bytes. This parameter defaults to 1024 * 1024 bytes (1 MiB).
        This number is used for .parquet file format only.

      - **ParquetVersion** *(string) --*

        The version of the Apache Parquet format that you want to use: ``parquet_1_0`` (the
        default) or ``parquet_2_0`` .

      - **EnableStatistics** *(boolean) --*

        A value that enables statistics for Parquet pages and row groups. Choose ``true`` to
        enable statistics, ``false`` to disable. Statistics include ``NULL`` , ``DISTINCT`` ,
        ``MAX`` , and ``MIN`` values. This parameter defaults to ``true`` . This value is used
        for .parquet file format only.

      - **IncludeOpForFullLoad** *(boolean) --*

        A value that enables a full load to write INSERT operations to the comma-separated value
        (.csv) output files only to indicate how the rows were added to the source database.

        .. note::

          AWS DMS supports the ``IncludeOpForFullLoad`` parameter in versions 3.1.4 and later.

        For full load, records can only be inserted. By default (the ``false`` setting), no
        information is recorded in these output files for a full load to indicate that the rows
        were inserted at the source database. If ``IncludeOpForFullLoad`` is set to ``true`` or
        ``y`` , the INSERT is recorded as an I annotation in the first field of the .csv file.
        This allows the format of your target records from a full load to be consistent with the
        target records from a CDC load.

        .. note::

          This setting works together with the ``CdcInsertsOnly`` parameter for output to .csv
          files only. For more information about how these settings work together, see
          `Indicating Source DB Operations in Migrated S3 Data
          <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring.InsertOps>`__
          in the *AWS Database Migration Service User Guide.* .

      - **CdcInsertsOnly** *(boolean) --*

        A value that enables a change data capture (CDC) load to write only INSERT operations to
        .csv or columnar storage (.parquet) output files. By default (the ``false`` setting), the
        first field in a .csv or .parquet record contains the letter I (INSERT), U (UPDATE), or D
        (DELETE). These values indicate whether the row was inserted, updated, or deleted at the
        source database for a CDC load to the target.

        If ``CdcInsertsOnly`` is set to ``true`` or ``y`` , only INSERTs from the source database
        are migrated to the .csv or .parquet file. For .csv format only, how these INSERTs are
        recorded depends on the value of ``IncludeOpForFullLoad`` . If ``IncludeOpForFullLoad``
        is set to ``true`` , the first field of every CDC record is set to I to indicate the
        INSERT operation at the source. If ``IncludeOpForFullLoad`` is set to ``false`` , every
        CDC record is written without a first field to indicate the INSERT operation at the
        source. For more information about how these settings work together, see `Indicating
        Source DB Operations in Migrated S3 Data
        <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring.InsertOps>`__
        in the *AWS Database Migration Service User Guide.* .

        .. note::

          AWS DMS supports this interaction between the ``CdcInsertsOnly`` and
          ``IncludeOpForFullLoad`` parameters in versions 3.1.4 and later.

      - **TimestampColumnName** *(string) --*

        A value that when nonblank causes AWS DMS to add a column with timestamp information to
        the endpoint data for an Amazon S3 target.

        .. note::

          AWS DMS supports the ``TimestampColumnName`` parameter in versions 3.1.4 and later.

        DMS includes an additional ``STRING`` column in the .csv or .parquet object files of your
        migrated data when you set ``TimestampColumnName`` to a nonblank value.

        For a full load, each row of this timestamp column contains a timestamp for when the data
        was transferred from the source to the target by DMS.

        For a change data capture (CDC) load, each row of the timestamp column contains the
        timestamp for the commit of that row in the source database.

        The string format for this timestamp column value is ``yyyy-MM-dd HH:mm:ss.SSSSSS`` . By
        default, the precision of this value is in microseconds. For a CDC load, the rounding of
        the precision depends on the commit timestamp supported by DMS for the source database.

        When the ``AddColumnName`` parameter is set to ``true`` , DMS also includes a name for
        the timestamp column that you set with ``TimestampColumnName`` .

      - **ParquetTimestampInMillisecond** *(boolean) --*

        A value that specifies the precision of any ``TIMESTAMP`` column values that are written
        to an Amazon S3 object file in .parquet format.

        .. note::

          AWS DMS supports the ``ParquetTimestampInMillisecond`` parameter in versions 3.1.4 and
          later.

        When ``ParquetTimestampInMillisecond`` is set to ``true`` or ``y`` , AWS DMS writes all
        ``TIMESTAMP`` columns in a .parquet formatted file with millisecond precision. Otherwise,
        DMS writes them with microsecond precision.

        Currently, Amazon Athena and AWS Glue can handle only millisecond precision for
        ``TIMESTAMP`` values. Set this parameter to ``true`` for S3 endpoint object files that
        are .parquet formatted only if you plan to query or process the data with Athena or AWS
        Glue.

        .. note::

          AWS DMS writes any ``TIMESTAMP`` column values written to an S3 file in .csv format
          with microsecond precision.

          Setting ``ParquetTimestampInMillisecond`` has no effect on the string format of the
          timestamp column value that is inserted by setting the ``TimestampColumnName``
          parameter.

    - **DmsTransferSettings** *(dict) --*

      The settings in JSON format for the DMS transfer type of source endpoint.

      Possible settings include the following:

      * ``ServiceAccessRoleArn`` - The IAM role that has permission to access the Amazon S3
      bucket.

      * ``BucketName`` - The name of the S3 bucket to use.

      * ``CompressionType`` - An optional parameter to use GZIP to compress the target files. To
      use GZIP, set this value to ``NONE`` (the default). To keep the files uncompressed, don't
      use this value.

      Shorthand syntax for these settings is as follows:
      ``ServiceAccessRoleArn=string,BucketName=string,CompressionType=string``

      JSON syntax for these settings is as follows: ``{ "ServiceAccessRoleArn": "string",
      "BucketName": "string", "CompressionType": "none"|"gzip" }``

      - **ServiceAccessRoleArn** *(string) --*

        The IAM role that has permission to access the Amazon S3 bucket.

      - **BucketName** *(string) --*

        The name of the S3 bucket to use.

    - **MongoDbSettings** *(dict) --*

      The settings for the MongoDB source endpoint. For more information, see the
      ``MongoDbSettings`` structure.

      - **Username** *(string) --*

        The user name you use to access the MongoDB source endpoint.

      - **Password** *(string) --*

        The password for the user account you use to access the MongoDB source endpoint.

      - **ServerName** *(string) --*

        The name of the server on the MongoDB source endpoint.

      - **Port** *(integer) --*

        The port value for the MongoDB source endpoint.

      - **DatabaseName** *(string) --*

        The database name on the MongoDB source endpoint.

      - **AuthType** *(string) --*

        The authentication type you use to access the MongoDB source endpoint.

        Valid values: NO, PASSWORD

        When NO is selected, user name and password parameters are not used and can be empty.

      - **AuthMechanism** *(string) --*

        The authentication mechanism you use to access the MongoDB source endpoint.

        Valid values: DEFAULT, MONGODB_CR, SCRAM_SHA_1

        DEFAULT – For MongoDB version 2.x, use MONGODB_CR. For MongoDB version 3.x, use
        SCRAM_SHA_1. This setting is not used when authType=No.

      - **NestingLevel** *(string) --*

        Specifies either document or table mode.

        Valid values: NONE, ONE

        Default value is NONE. Specify NONE to use document mode. Specify ONE to use table mode.

      - **ExtractDocId** *(string) --*

        Specifies the document ID. Use this setting when ``NestingLevel`` is set to NONE.

        Default value is false.

      - **DocsToInvestigate** *(string) --*

        Indicates the number of documents to preview to determine the document organization. Use
        this setting when ``NestingLevel`` is set to ONE.

        Must be a positive value greater than 0. Default value is 1000.

      - **AuthSource** *(string) --*

        The MongoDB database name. This setting is not used when ``authType=NO`` .

        The default is admin.

      - **KmsKeyId** *(string) --*

        The AWS KMS key identifier that is used to encrypt the content on the replication
        instance. If you don't specify a value for the ``KmsKeyId`` parameter, then AWS DMS uses
        your default encryption key. AWS KMS creates the default encryption key for your AWS
        account. Your AWS account has a different default encryption key for each AWS Region.

    - **KinesisSettings** *(dict) --*

      The settings for the Amazon Kinesis source endpoint. For more information, see the
      ``KinesisSettings`` structure.

      - **StreamArn** *(string) --*

        The Amazon Resource Name (ARN) for the Amazon Kinesis Data Streams endpoint.

      - **MessageFormat** *(string) --*

        The output format for the records created on the endpoint. The message format is ``JSON``
        .

      - **ServiceAccessRoleArn** *(string) --*

        The Amazon Resource Name (ARN) for the IAM role that DMS uses to write to the Amazon
        Kinesis data stream.

    - **ElasticsearchSettings** *(dict) --*

      The settings for the Elasticsearch source endpoint. For more information, see the
      ``ElasticsearchSettings`` structure.

      - **ServiceAccessRoleArn** *(string) --*

        The Amazon Resource Name (ARN) used by service to access the IAM role.

      - **EndpointUri** *(string) --*

        The endpoint for the Elasticsearch cluster.

      - **FullLoadErrorPercentage** *(integer) --*

        The maximum percentage of records that can fail to be written before a full load
        operation stops.

      - **ErrorRetryDuration** *(integer) --*

        The maximum number of seconds that DMS retries failed API requests to the Elasticsearch
        cluster.

    - **RedshiftSettings** *(dict) --*

      Settings for the Amazon Redshift endpoint.

      - **AcceptAnyDate** *(boolean) --*

        A value that indicates to allow any date format, including invalid formats such as
        00/00/00 00:00:00, to be loaded without generating an error. You can choose ``true`` or
        ``false`` (the default).

        This parameter applies only to TIMESTAMP and DATE columns. Always use ACCEPTANYDATE with
        the DATEFORMAT parameter. If the date format for the data doesn't match the DATEFORMAT
        specification, Amazon Redshift inserts a NULL value into that field.

      - **AfterConnectScript** *(string) --*

        Code to run after connecting. This parameter should contain the code itself, not the name
        of a file containing the code.

      - **BucketFolder** *(string) --*

        The location where the comma-separated value (.csv) files are stored before being
        uploaded to the S3 bucket.

      - **BucketName** *(string) --*

        The name of the S3 bucket you want to use

      - **ConnectionTimeout** *(integer) --*

        A value that sets the amount of time to wait (in milliseconds) before timing out,
        beginning from when you initially establish a connection.

      - **DatabaseName** *(string) --*

        The name of the Amazon Redshift data warehouse (service) that you are working with.

      - **DateFormat** *(string) --*

        The date format that you are using. Valid values are ``auto`` (case-sensitive), your date
        format string enclosed in quotes, or NULL. If this parameter is left unset (NULL), it
        defaults to a format of 'YYYY-MM-DD'. Using ``auto`` recognizes most strings, even some
        that aren't supported when you use a date format string.

        If your date and time values use formats different from each other, set this to ``auto`` .

      - **EmptyAsNull** *(boolean) --*

        A value that specifies whether AWS DMS should migrate empty CHAR and VARCHAR fields as
        NULL. A value of ``true`` sets empty CHAR and VARCHAR fields to null. The default is
        ``false`` .

      - **EncryptionMode** *(string) --*

        The type of server-side encryption that you want to use for your data. This encryption
        type is part of the endpoint settings or the extra connections attributes for Amazon S3.
        You can choose either ``SSE_S3`` (the default) or ``SSE_KMS`` . To use ``SSE_S3`` ,
        create an AWS Identity and Access Management (IAM) role with a policy that allows
        ``"arn:aws:s3:::*"`` to use the following actions: ``"s3:PutObject", "s3:ListBucket"``

      - **FileTransferUploadStreams** *(integer) --*

        The number of threads used to upload a single file. This parameter accepts a value from 1
        through 64. It defaults to 10.

      - **LoadTimeout** *(integer) --*

        The amount of time to wait (in milliseconds) before timing out, beginning from when you
        begin loading.

      - **MaxFileSize** *(integer) --*

        The maximum size (in KB) of any .csv file used to transfer data to Amazon Redshift. This
        accepts a value from 1 through 1,048,576. It defaults to 32,768 KB (32 MB).

      - **Password** *(string) --*

        The password for the user named in the ``username`` property.

      - **Port** *(integer) --*

        The port number for Amazon Redshift. The default value is 5439.

      - **RemoveQuotes** *(boolean) --*

        A value that specifies to remove surrounding quotation marks from strings in the incoming
        data. All characters within the quotation marks, including delimiters, are retained.
        Choose ``true`` to remove quotation marks. The default is ``false`` .

      - **ReplaceInvalidChars** *(string) --*

        A list of characters that you want to replace. Use with ``ReplaceChars`` .

      - **ReplaceChars** *(string) --*

        A value that specifies to replaces the invalid characters specified in
        ``ReplaceInvalidChars`` , substituting the specified characters instead. The default is
        ``"?"`` .

      - **ServerName** *(string) --*

        The name of the Amazon Redshift cluster you are using.

      - **ServiceAccessRoleArn** *(string) --*

        The Amazon Resource Name (ARN) of the IAM role that has access to the Amazon Redshift
        service.

      - **ServerSideEncryptionKmsKeyId** *(string) --*

        The AWS KMS key ID. If you are using ``SSE_KMS`` for the ``EncryptionMode`` , provide
        this key ID. The key that you use needs an attached policy that enables IAM user
        permissions and allows use of the key.

      - **TimeFormat** *(string) --*

        The time format that you want to use. Valid values are ``auto`` (case-sensitive),
        ``'timeformat_string'`` , ``'epochsecs'`` , or ``'epochmillisecs'`` . It defaults to 10.
        Using ``auto`` recognizes most strings, even some that aren't supported when you use a
        time format string.

        If your date and time values use formats different from each other, set this parameter to
        ``auto`` .

      - **TrimBlanks** *(boolean) --*

        A value that specifies to remove the trailing white space characters from a VARCHAR
        string. This parameter applies only to columns with a VARCHAR data type. Choose ``true``
        to remove unneeded white space. The default is ``false`` .

      - **TruncateColumns** *(boolean) --*

        A value that specifies to truncate data in columns to the appropriate number of
        characters, so that the data fits in the column. This parameter applies only to columns
        with a VARCHAR or CHAR data type, and rows with a size of 4 MB or less. Choose ``true``
        to truncate data. The default is ``false`` .

      - **Username** *(string) --*

        An Amazon Redshift user name for a registered user.

      - **WriteBufferSize** *(integer) --*

        The size of the write buffer to use in rows. Valid values range from 1 through 2,048. The
        default is 1,024. Use this setting to tune performance.
    """


_ClientCreateEndpointResponseTypeDef = TypedDict(
    "_ClientCreateEndpointResponseTypeDef",
    {"Endpoint": ClientCreateEndpointResponseEndpointTypeDef},
    total=False,
)


class ClientCreateEndpointResponseTypeDef(_ClientCreateEndpointResponseTypeDef):
    """
    Type definition for `ClientCreateEndpoint` `Response`

    - **Endpoint** *(dict) --*

      The endpoint that was created.

      - **EndpointIdentifier** *(string) --*

        The database endpoint identifier. Identifiers must begin with a letter; must contain only
        ASCII letters, digits, and hyphens; and must not end with a hyphen or contain two
        consecutive hyphens.

      - **EndpointType** *(string) --*

        The type of endpoint. Valid values are ``source`` and ``target`` .

      - **EngineName** *(string) --*

        The database engine name. Valid values, depending on the EndpointType, include mysql,
        oracle, postgres, mariadb, aurora, aurora-postgresql, redshift, s3, db2, azuredb, sybase,
        dynamodb, mongodb, and sqlserver.

      - **EngineDisplayName** *(string) --*

        The expanded name for the engine name. For example, if the ``EngineName`` parameter is
        "aurora," this value would be "Amazon Aurora MySQL."

      - **Username** *(string) --*

        The user name used to connect to the endpoint.

      - **ServerName** *(string) --*

        The name of the server at the endpoint.

      - **Port** *(integer) --*

        The port value used to access the endpoint.

      - **DatabaseName** *(string) --*

        The name of the database at the endpoint.

      - **ExtraConnectionAttributes** *(string) --*

        Additional connection attributes used to connect to the endpoint.

      - **Status** *(string) --*

        The status of the endpoint.

      - **KmsKeyId** *(string) --*

        An AWS KMS key identifier that is used to encrypt the connection parameters for the
        endpoint.

        If you don't specify a value for the ``KmsKeyId`` parameter, then AWS DMS uses your default
        encryption key.

        AWS KMS creates the default encryption key for your AWS account. Your AWS account has a
        different default encryption key for each AWS Region.

      - **EndpointArn** *(string) --*

        The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

      - **CertificateArn** *(string) --*

        The Amazon Resource Name (ARN) used for SSL connection to the endpoint.

      - **SslMode** *(string) --*

        The SSL mode used to connect to the endpoint. The default value is ``none`` .

      - **ServiceAccessRoleArn** *(string) --*

        The Amazon Resource Name (ARN) used by the service access IAM role.

      - **ExternalTableDefinition** *(string) --*

        The external table definition.

      - **ExternalId** *(string) --*

        Value returned by a call to CreateEndpoint that can be used for cross-account validation.
        Use it on a subsequent call to CreateEndpoint to create the endpoint with a cross-account.

      - **DynamoDbSettings** *(dict) --*

        The settings for the target DynamoDB database. For more information, see the
        ``DynamoDBSettings`` structure.

        - **ServiceAccessRoleArn** *(string) --*

          The Amazon Resource Name (ARN) used by the service access IAM role.

      - **S3Settings** *(dict) --*

        The settings for the S3 target endpoint. For more information, see the ``S3Settings``
        structure.

        - **ServiceAccessRoleArn** *(string) --*

          The Amazon Resource Name (ARN) used by the service access IAM role.

        - **ExternalTableDefinition** *(string) --*

          The external table definition.

        - **CsvRowDelimiter** *(string) --*

          The delimiter used to separate rows in the source files. The default is a carriage return
          (``\\n`` ).

        - **CsvDelimiter** *(string) --*

          The delimiter used to separate columns in the source files. The default is a comma.

        - **BucketFolder** *(string) --*

          An optional parameter to set a folder name in the S3 bucket. If provided, tables are
          created in the path `` *bucketFolder* /*schema_name* /*table_name* /`` . If this
          parameter is not specified, then the path used is `` *schema_name* /*table_name* /`` .

        - **BucketName** *(string) --*

          The name of the S3 bucket.

        - **CompressionType** *(string) --*

          An optional parameter to use GZIP to compress the target files. Set to GZIP to compress
          the target files. Set to NONE (the default) or do not use to leave the files
          uncompressed. Applies to both .csv and .parquet file formats.

        - **EncryptionMode** *(string) --*

          The type of server-side encryption that you want to use for your data. This encryption
          type is part of the endpoint settings or the extra connections attributes for Amazon S3.
          You can choose either ``SSE_S3`` (the default) or ``SSE_KMS`` . To use ``SSE_S3`` , you
          need an AWS Identity and Access Management (IAM) role with permission to allow
          ``"arn:aws:s3:::dms-*"`` to use the following actions:

          * ``s3:CreateBucket``

          * ``s3:ListBucket``

          * ``s3:DeleteBucket``

          * ``s3:GetBucketLocation``

          * ``s3:GetObject``

          * ``s3:PutObject``

          * ``s3:DeleteObject``

          * ``s3:GetObjectVersion``

          * ``s3:GetBucketPolicy``

          * ``s3:PutBucketPolicy``

          * ``s3:DeleteBucketPolicy``

        - **ServerSideEncryptionKmsKeyId** *(string) --*

          If you are using ``SSE_KMS`` for the ``EncryptionMode`` , provide the AWS KMS key ID. The
          key that you use needs an attached policy that enables AWS Identity and Access Management
          (IAM) user permissions and allows use of the key.

          Here is a CLI example: ``aws dms create-endpoint --endpoint-identifier *value*
          --endpoint-type target --engine-name s3 --s3-settings ServiceAccessRoleArn=*value*
          ,BucketFolder=*value* ,BucketName=*value*
          ,EncryptionMode=SSE_KMS,ServerSideEncryptionKmsKeyId=*value* ``

        - **DataFormat** *(string) --*

          The format of the data that you want to use for output. You can choose one of the
          following:

          * ``csv`` : This is a row-based file format with comma-separated values (.csv).

          * ``parquet`` : Apache Parquet (.parquet) is a columnar storage file format that features
          efficient compression and provides faster query response.

        - **EncodingType** *(string) --*

          The type of encoding you are using:

          * ``RLE_DICTIONARY`` uses a combination of bit-packing and run-length encoding to store
          repeated values more efficiently. This is the default.

          * ``PLAIN`` doesn't use encoding at all. Values are stored as they are.

          * ``PLAIN_DICTIONARY`` builds a dictionary of the values encountered in a given column.
          The dictionary is stored in a dictionary page for each column chunk.

        - **DictPageSizeLimit** *(integer) --*

          The maximum size of an encoded dictionary page of a column. If the dictionary page
          exceeds this, this column is stored using an encoding type of ``PLAIN`` . This parameter
          defaults to 1024 * 1024 bytes (1 MiB), the maximum size of a dictionary page before it
          reverts to ``PLAIN`` encoding. This size is used for .parquet file format only.

        - **RowGroupLength** *(integer) --*

          The number of rows in a row group. A smaller row group size provides faster reads. But as
          the number of row groups grows, the slower writes become. This parameter defaults to
          10,000 rows. This number is used for .parquet file format only.

          If you choose a value larger than the maximum, ``RowGroupLength`` is set to the max row
          group length in bytes (64 * 1024 * 1024).

        - **DataPageSize** *(integer) --*

          The size of one data page in bytes. This parameter defaults to 1024 * 1024 bytes (1 MiB).
          This number is used for .parquet file format only.

        - **ParquetVersion** *(string) --*

          The version of the Apache Parquet format that you want to use: ``parquet_1_0`` (the
          default) or ``parquet_2_0`` .

        - **EnableStatistics** *(boolean) --*

          A value that enables statistics for Parquet pages and row groups. Choose ``true`` to
          enable statistics, ``false`` to disable. Statistics include ``NULL`` , ``DISTINCT`` ,
          ``MAX`` , and ``MIN`` values. This parameter defaults to ``true`` . This value is used
          for .parquet file format only.

        - **IncludeOpForFullLoad** *(boolean) --*

          A value that enables a full load to write INSERT operations to the comma-separated value
          (.csv) output files only to indicate how the rows were added to the source database.

          .. note::

            AWS DMS supports the ``IncludeOpForFullLoad`` parameter in versions 3.1.4 and later.

          For full load, records can only be inserted. By default (the ``false`` setting), no
          information is recorded in these output files for a full load to indicate that the rows
          were inserted at the source database. If ``IncludeOpForFullLoad`` is set to ``true`` or
          ``y`` , the INSERT is recorded as an I annotation in the first field of the .csv file.
          This allows the format of your target records from a full load to be consistent with the
          target records from a CDC load.

          .. note::

            This setting works together with the ``CdcInsertsOnly`` parameter for output to .csv
            files only. For more information about how these settings work together, see
            `Indicating Source DB Operations in Migrated S3 Data
            <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring.InsertOps>`__
            in the *AWS Database Migration Service User Guide.* .

        - **CdcInsertsOnly** *(boolean) --*

          A value that enables a change data capture (CDC) load to write only INSERT operations to
          .csv or columnar storage (.parquet) output files. By default (the ``false`` setting), the
          first field in a .csv or .parquet record contains the letter I (INSERT), U (UPDATE), or D
          (DELETE). These values indicate whether the row was inserted, updated, or deleted at the
          source database for a CDC load to the target.

          If ``CdcInsertsOnly`` is set to ``true`` or ``y`` , only INSERTs from the source database
          are migrated to the .csv or .parquet file. For .csv format only, how these INSERTs are
          recorded depends on the value of ``IncludeOpForFullLoad`` . If ``IncludeOpForFullLoad``
          is set to ``true`` , the first field of every CDC record is set to I to indicate the
          INSERT operation at the source. If ``IncludeOpForFullLoad`` is set to ``false`` , every
          CDC record is written without a first field to indicate the INSERT operation at the
          source. For more information about how these settings work together, see `Indicating
          Source DB Operations in Migrated S3 Data
          <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring.InsertOps>`__
          in the *AWS Database Migration Service User Guide.* .

          .. note::

            AWS DMS supports this interaction between the ``CdcInsertsOnly`` and
            ``IncludeOpForFullLoad`` parameters in versions 3.1.4 and later.

        - **TimestampColumnName** *(string) --*

          A value that when nonblank causes AWS DMS to add a column with timestamp information to
          the endpoint data for an Amazon S3 target.

          .. note::

            AWS DMS supports the ``TimestampColumnName`` parameter in versions 3.1.4 and later.

          DMS includes an additional ``STRING`` column in the .csv or .parquet object files of your
          migrated data when you set ``TimestampColumnName`` to a nonblank value.

          For a full load, each row of this timestamp column contains a timestamp for when the data
          was transferred from the source to the target by DMS.

          For a change data capture (CDC) load, each row of the timestamp column contains the
          timestamp for the commit of that row in the source database.

          The string format for this timestamp column value is ``yyyy-MM-dd HH:mm:ss.SSSSSS`` . By
          default, the precision of this value is in microseconds. For a CDC load, the rounding of
          the precision depends on the commit timestamp supported by DMS for the source database.

          When the ``AddColumnName`` parameter is set to ``true`` , DMS also includes a name for
          the timestamp column that you set with ``TimestampColumnName`` .

        - **ParquetTimestampInMillisecond** *(boolean) --*

          A value that specifies the precision of any ``TIMESTAMP`` column values that are written
          to an Amazon S3 object file in .parquet format.

          .. note::

            AWS DMS supports the ``ParquetTimestampInMillisecond`` parameter in versions 3.1.4 and
            later.

          When ``ParquetTimestampInMillisecond`` is set to ``true`` or ``y`` , AWS DMS writes all
          ``TIMESTAMP`` columns in a .parquet formatted file with millisecond precision. Otherwise,
          DMS writes them with microsecond precision.

          Currently, Amazon Athena and AWS Glue can handle only millisecond precision for
          ``TIMESTAMP`` values. Set this parameter to ``true`` for S3 endpoint object files that
          are .parquet formatted only if you plan to query or process the data with Athena or AWS
          Glue.

          .. note::

            AWS DMS writes any ``TIMESTAMP`` column values written to an S3 file in .csv format
            with microsecond precision.

            Setting ``ParquetTimestampInMillisecond`` has no effect on the string format of the
            timestamp column value that is inserted by setting the ``TimestampColumnName``
            parameter.

      - **DmsTransferSettings** *(dict) --*

        The settings in JSON format for the DMS transfer type of source endpoint.

        Possible settings include the following:

        * ``ServiceAccessRoleArn`` - The IAM role that has permission to access the Amazon S3
        bucket.

        * ``BucketName`` - The name of the S3 bucket to use.

        * ``CompressionType`` - An optional parameter to use GZIP to compress the target files. To
        use GZIP, set this value to ``NONE`` (the default). To keep the files uncompressed, don't
        use this value.

        Shorthand syntax for these settings is as follows:
        ``ServiceAccessRoleArn=string,BucketName=string,CompressionType=string``

        JSON syntax for these settings is as follows: ``{ "ServiceAccessRoleArn": "string",
        "BucketName": "string", "CompressionType": "none"|"gzip" }``

        - **ServiceAccessRoleArn** *(string) --*

          The IAM role that has permission to access the Amazon S3 bucket.

        - **BucketName** *(string) --*

          The name of the S3 bucket to use.

      - **MongoDbSettings** *(dict) --*

        The settings for the MongoDB source endpoint. For more information, see the
        ``MongoDbSettings`` structure.

        - **Username** *(string) --*

          The user name you use to access the MongoDB source endpoint.

        - **Password** *(string) --*

          The password for the user account you use to access the MongoDB source endpoint.

        - **ServerName** *(string) --*

          The name of the server on the MongoDB source endpoint.

        - **Port** *(integer) --*

          The port value for the MongoDB source endpoint.

        - **DatabaseName** *(string) --*

          The database name on the MongoDB source endpoint.

        - **AuthType** *(string) --*

          The authentication type you use to access the MongoDB source endpoint.

          Valid values: NO, PASSWORD

          When NO is selected, user name and password parameters are not used and can be empty.

        - **AuthMechanism** *(string) --*

          The authentication mechanism you use to access the MongoDB source endpoint.

          Valid values: DEFAULT, MONGODB_CR, SCRAM_SHA_1

          DEFAULT – For MongoDB version 2.x, use MONGODB_CR. For MongoDB version 3.x, use
          SCRAM_SHA_1. This setting is not used when authType=No.

        - **NestingLevel** *(string) --*

          Specifies either document or table mode.

          Valid values: NONE, ONE

          Default value is NONE. Specify NONE to use document mode. Specify ONE to use table mode.

        - **ExtractDocId** *(string) --*

          Specifies the document ID. Use this setting when ``NestingLevel`` is set to NONE.

          Default value is false.

        - **DocsToInvestigate** *(string) --*

          Indicates the number of documents to preview to determine the document organization. Use
          this setting when ``NestingLevel`` is set to ONE.

          Must be a positive value greater than 0. Default value is 1000.

        - **AuthSource** *(string) --*

          The MongoDB database name. This setting is not used when ``authType=NO`` .

          The default is admin.

        - **KmsKeyId** *(string) --*

          The AWS KMS key identifier that is used to encrypt the content on the replication
          instance. If you don't specify a value for the ``KmsKeyId`` parameter, then AWS DMS uses
          your default encryption key. AWS KMS creates the default encryption key for your AWS
          account. Your AWS account has a different default encryption key for each AWS Region.

      - **KinesisSettings** *(dict) --*

        The settings for the Amazon Kinesis source endpoint. For more information, see the
        ``KinesisSettings`` structure.

        - **StreamArn** *(string) --*

          The Amazon Resource Name (ARN) for the Amazon Kinesis Data Streams endpoint.

        - **MessageFormat** *(string) --*

          The output format for the records created on the endpoint. The message format is ``JSON``
          .

        - **ServiceAccessRoleArn** *(string) --*

          The Amazon Resource Name (ARN) for the IAM role that DMS uses to write to the Amazon
          Kinesis data stream.

      - **ElasticsearchSettings** *(dict) --*

        The settings for the Elasticsearch source endpoint. For more information, see the
        ``ElasticsearchSettings`` structure.

        - **ServiceAccessRoleArn** *(string) --*

          The Amazon Resource Name (ARN) used by service to access the IAM role.

        - **EndpointUri** *(string) --*

          The endpoint for the Elasticsearch cluster.

        - **FullLoadErrorPercentage** *(integer) --*

          The maximum percentage of records that can fail to be written before a full load
          operation stops.

        - **ErrorRetryDuration** *(integer) --*

          The maximum number of seconds that DMS retries failed API requests to the Elasticsearch
          cluster.

      - **RedshiftSettings** *(dict) --*

        Settings for the Amazon Redshift endpoint.

        - **AcceptAnyDate** *(boolean) --*

          A value that indicates to allow any date format, including invalid formats such as
          00/00/00 00:00:00, to be loaded without generating an error. You can choose ``true`` or
          ``false`` (the default).

          This parameter applies only to TIMESTAMP and DATE columns. Always use ACCEPTANYDATE with
          the DATEFORMAT parameter. If the date format for the data doesn't match the DATEFORMAT
          specification, Amazon Redshift inserts a NULL value into that field.

        - **AfterConnectScript** *(string) --*

          Code to run after connecting. This parameter should contain the code itself, not the name
          of a file containing the code.

        - **BucketFolder** *(string) --*

          The location where the comma-separated value (.csv) files are stored before being
          uploaded to the S3 bucket.

        - **BucketName** *(string) --*

          The name of the S3 bucket you want to use

        - **ConnectionTimeout** *(integer) --*

          A value that sets the amount of time to wait (in milliseconds) before timing out,
          beginning from when you initially establish a connection.

        - **DatabaseName** *(string) --*

          The name of the Amazon Redshift data warehouse (service) that you are working with.

        - **DateFormat** *(string) --*

          The date format that you are using. Valid values are ``auto`` (case-sensitive), your date
          format string enclosed in quotes, or NULL. If this parameter is left unset (NULL), it
          defaults to a format of 'YYYY-MM-DD'. Using ``auto`` recognizes most strings, even some
          that aren't supported when you use a date format string.

          If your date and time values use formats different from each other, set this to ``auto`` .

        - **EmptyAsNull** *(boolean) --*

          A value that specifies whether AWS DMS should migrate empty CHAR and VARCHAR fields as
          NULL. A value of ``true`` sets empty CHAR and VARCHAR fields to null. The default is
          ``false`` .

        - **EncryptionMode** *(string) --*

          The type of server-side encryption that you want to use for your data. This encryption
          type is part of the endpoint settings or the extra connections attributes for Amazon S3.
          You can choose either ``SSE_S3`` (the default) or ``SSE_KMS`` . To use ``SSE_S3`` ,
          create an AWS Identity and Access Management (IAM) role with a policy that allows
          ``"arn:aws:s3:::*"`` to use the following actions: ``"s3:PutObject", "s3:ListBucket"``

        - **FileTransferUploadStreams** *(integer) --*

          The number of threads used to upload a single file. This parameter accepts a value from 1
          through 64. It defaults to 10.

        - **LoadTimeout** *(integer) --*

          The amount of time to wait (in milliseconds) before timing out, beginning from when you
          begin loading.

        - **MaxFileSize** *(integer) --*

          The maximum size (in KB) of any .csv file used to transfer data to Amazon Redshift. This
          accepts a value from 1 through 1,048,576. It defaults to 32,768 KB (32 MB).

        - **Password** *(string) --*

          The password for the user named in the ``username`` property.

        - **Port** *(integer) --*

          The port number for Amazon Redshift. The default value is 5439.

        - **RemoveQuotes** *(boolean) --*

          A value that specifies to remove surrounding quotation marks from strings in the incoming
          data. All characters within the quotation marks, including delimiters, are retained.
          Choose ``true`` to remove quotation marks. The default is ``false`` .

        - **ReplaceInvalidChars** *(string) --*

          A list of characters that you want to replace. Use with ``ReplaceChars`` .

        - **ReplaceChars** *(string) --*

          A value that specifies to replaces the invalid characters specified in
          ``ReplaceInvalidChars`` , substituting the specified characters instead. The default is
          ``"?"`` .

        - **ServerName** *(string) --*

          The name of the Amazon Redshift cluster you are using.

        - **ServiceAccessRoleArn** *(string) --*

          The Amazon Resource Name (ARN) of the IAM role that has access to the Amazon Redshift
          service.

        - **ServerSideEncryptionKmsKeyId** *(string) --*

          The AWS KMS key ID. If you are using ``SSE_KMS`` for the ``EncryptionMode`` , provide
          this key ID. The key that you use needs an attached policy that enables IAM user
          permissions and allows use of the key.

        - **TimeFormat** *(string) --*

          The time format that you want to use. Valid values are ``auto`` (case-sensitive),
          ``'timeformat_string'`` , ``'epochsecs'`` , or ``'epochmillisecs'`` . It defaults to 10.
          Using ``auto`` recognizes most strings, even some that aren't supported when you use a
          time format string.

          If your date and time values use formats different from each other, set this parameter to
          ``auto`` .

        - **TrimBlanks** *(boolean) --*

          A value that specifies to remove the trailing white space characters from a VARCHAR
          string. This parameter applies only to columns with a VARCHAR data type. Choose ``true``
          to remove unneeded white space. The default is ``false`` .

        - **TruncateColumns** *(boolean) --*

          A value that specifies to truncate data in columns to the appropriate number of
          characters, so that the data fits in the column. This parameter applies only to columns
          with a VARCHAR or CHAR data type, and rows with a size of 4 MB or less. Choose ``true``
          to truncate data. The default is ``false`` .

        - **Username** *(string) --*

          An Amazon Redshift user name for a registered user.

        - **WriteBufferSize** *(integer) --*

          The size of the write buffer to use in rows. Valid values range from 1 through 2,048. The
          default is 1,024. Use this setting to tune performance.
    """


_ClientCreateEndpointS3SettingsTypeDef = TypedDict(
    "_ClientCreateEndpointS3SettingsTypeDef",
    {
        "ServiceAccessRoleArn": str,
        "ExternalTableDefinition": str,
        "CsvRowDelimiter": str,
        "CsvDelimiter": str,
        "BucketFolder": str,
        "BucketName": str,
        "CompressionType": str,
        "EncryptionMode": str,
        "ServerSideEncryptionKmsKeyId": str,
        "DataFormat": str,
        "EncodingType": str,
        "DictPageSizeLimit": int,
        "RowGroupLength": int,
        "DataPageSize": int,
        "ParquetVersion": str,
        "EnableStatistics": bool,
        "IncludeOpForFullLoad": bool,
        "CdcInsertsOnly": bool,
        "TimestampColumnName": str,
        "ParquetTimestampInMillisecond": bool,
    },
    total=False,
)


class ClientCreateEndpointS3SettingsTypeDef(_ClientCreateEndpointS3SettingsTypeDef):
    """
    Type definition for `ClientCreateEndpoint` `S3Settings`

    Settings in JSON format for the target Amazon S3 endpoint. For more information about the
    available settings, see `Extra Connection Attributes When Using Amazon S3 as a Target for AWS DMS
    <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring>`__
    in the *AWS Database Migration Service User Guide.*

    - **ServiceAccessRoleArn** *(string) --*

      The Amazon Resource Name (ARN) used by the service access IAM role.

    - **ExternalTableDefinition** *(string) --*

      The external table definition.

    - **CsvRowDelimiter** *(string) --*

      The delimiter used to separate rows in the source files. The default is a carriage return
      (``\\n`` ).

    - **CsvDelimiter** *(string) --*

      The delimiter used to separate columns in the source files. The default is a comma.

    - **BucketFolder** *(string) --*

      An optional parameter to set a folder name in the S3 bucket. If provided, tables are created in
      the path `` *bucketFolder* /*schema_name* /*table_name* /`` . If this parameter is not
      specified, then the path used is `` *schema_name* /*table_name* /`` .

    - **BucketName** *(string) --*

      The name of the S3 bucket.

    - **CompressionType** *(string) --*

      An optional parameter to use GZIP to compress the target files. Set to GZIP to compress the
      target files. Set to NONE (the default) or do not use to leave the files uncompressed. Applies
      to both .csv and .parquet file formats.

    - **EncryptionMode** *(string) --*

      The type of server-side encryption that you want to use for your data. This encryption type is
      part of the endpoint settings or the extra connections attributes for Amazon S3. You can choose
      either ``SSE_S3`` (the default) or ``SSE_KMS`` . To use ``SSE_S3`` , you need an AWS Identity
      and Access Management (IAM) role with permission to allow ``"arn:aws:s3:::dms-*"`` to use the
      following actions:

      * ``s3:CreateBucket``

      * ``s3:ListBucket``

      * ``s3:DeleteBucket``

      * ``s3:GetBucketLocation``

      * ``s3:GetObject``

      * ``s3:PutObject``

      * ``s3:DeleteObject``

      * ``s3:GetObjectVersion``

      * ``s3:GetBucketPolicy``

      * ``s3:PutBucketPolicy``

      * ``s3:DeleteBucketPolicy``

    - **ServerSideEncryptionKmsKeyId** *(string) --*

      If you are using ``SSE_KMS`` for the ``EncryptionMode`` , provide the AWS KMS key ID. The key
      that you use needs an attached policy that enables AWS Identity and Access Management (IAM)
      user permissions and allows use of the key.

      Here is a CLI example: ``aws dms create-endpoint --endpoint-identifier *value* --endpoint-type
      target --engine-name s3 --s3-settings ServiceAccessRoleArn=*value* ,BucketFolder=*value*
      ,BucketName=*value* ,EncryptionMode=SSE_KMS,ServerSideEncryptionKmsKeyId=*value* ``

    - **DataFormat** *(string) --*

      The format of the data that you want to use for output. You can choose one of the following:

      * ``csv`` : This is a row-based file format with comma-separated values (.csv).

      * ``parquet`` : Apache Parquet (.parquet) is a columnar storage file format that features
      efficient compression and provides faster query response.

    - **EncodingType** *(string) --*

      The type of encoding you are using:

      * ``RLE_DICTIONARY`` uses a combination of bit-packing and run-length encoding to store
      repeated values more efficiently. This is the default.

      * ``PLAIN`` doesn't use encoding at all. Values are stored as they are.

      * ``PLAIN_DICTIONARY`` builds a dictionary of the values encountered in a given column. The
      dictionary is stored in a dictionary page for each column chunk.

    - **DictPageSizeLimit** *(integer) --*

      The maximum size of an encoded dictionary page of a column. If the dictionary page exceeds
      this, this column is stored using an encoding type of ``PLAIN`` . This parameter defaults to
      1024 * 1024 bytes (1 MiB), the maximum size of a dictionary page before it reverts to ``PLAIN``
      encoding. This size is used for .parquet file format only.

    - **RowGroupLength** *(integer) --*

      The number of rows in a row group. A smaller row group size provides faster reads. But as the
      number of row groups grows, the slower writes become. This parameter defaults to 10,000 rows.
      This number is used for .parquet file format only.

      If you choose a value larger than the maximum, ``RowGroupLength`` is set to the max row group
      length in bytes (64 * 1024 * 1024).

    - **DataPageSize** *(integer) --*

      The size of one data page in bytes. This parameter defaults to 1024 * 1024 bytes (1 MiB). This
      number is used for .parquet file format only.

    - **ParquetVersion** *(string) --*

      The version of the Apache Parquet format that you want to use: ``parquet_1_0`` (the default) or
      ``parquet_2_0`` .

    - **EnableStatistics** *(boolean) --*

      A value that enables statistics for Parquet pages and row groups. Choose ``true`` to enable
      statistics, ``false`` to disable. Statistics include ``NULL`` , ``DISTINCT`` , ``MAX`` , and
      ``MIN`` values. This parameter defaults to ``true`` . This value is used for .parquet file
      format only.

    - **IncludeOpForFullLoad** *(boolean) --*

      A value that enables a full load to write INSERT operations to the comma-separated value (.csv)
      output files only to indicate how the rows were added to the source database.

      .. note::

        AWS DMS supports the ``IncludeOpForFullLoad`` parameter in versions 3.1.4 and later.

      For full load, records can only be inserted. By default (the ``false`` setting), no information
      is recorded in these output files for a full load to indicate that the rows were inserted at
      the source database. If ``IncludeOpForFullLoad`` is set to ``true`` or ``y`` , the INSERT is
      recorded as an I annotation in the first field of the .csv file. This allows the format of your
      target records from a full load to be consistent with the target records from a CDC load.

      .. note::

        This setting works together with the ``CdcInsertsOnly`` parameter for output to .csv files
        only. For more information about how these settings work together, see `Indicating Source DB
        Operations in Migrated S3 Data
        <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring.InsertOps>`__
        in the *AWS Database Migration Service User Guide.* .

    - **CdcInsertsOnly** *(boolean) --*

      A value that enables a change data capture (CDC) load to write only INSERT operations to .csv
      or columnar storage (.parquet) output files. By default (the ``false`` setting), the first
      field in a .csv or .parquet record contains the letter I (INSERT), U (UPDATE), or D (DELETE).
      These values indicate whether the row was inserted, updated, or deleted at the source database
      for a CDC load to the target.

      If ``CdcInsertsOnly`` is set to ``true`` or ``y`` , only INSERTs from the source database are
      migrated to the .csv or .parquet file. For .csv format only, how these INSERTs are recorded
      depends on the value of ``IncludeOpForFullLoad`` . If ``IncludeOpForFullLoad`` is set to
      ``true`` , the first field of every CDC record is set to I to indicate the INSERT operation at
      the source. If ``IncludeOpForFullLoad`` is set to ``false`` , every CDC record is written
      without a first field to indicate the INSERT operation at the source. For more information
      about how these settings work together, see `Indicating Source DB Operations in Migrated S3
      Data
      <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring.InsertOps>`__
      in the *AWS Database Migration Service User Guide.* .

      .. note::

        AWS DMS supports this interaction between the ``CdcInsertsOnly`` and ``IncludeOpForFullLoad``
        parameters in versions 3.1.4 and later.

    - **TimestampColumnName** *(string) --*

      A value that when nonblank causes AWS DMS to add a column with timestamp information to the
      endpoint data for an Amazon S3 target.

      .. note::

        AWS DMS supports the ``TimestampColumnName`` parameter in versions 3.1.4 and later.

      DMS includes an additional ``STRING`` column in the .csv or .parquet object files of your
      migrated data when you set ``TimestampColumnName`` to a nonblank value.

      For a full load, each row of this timestamp column contains a timestamp for when the data was
      transferred from the source to the target by DMS.

      For a change data capture (CDC) load, each row of the timestamp column contains the timestamp
      for the commit of that row in the source database.

      The string format for this timestamp column value is ``yyyy-MM-dd HH:mm:ss.SSSSSS`` . By
      default, the precision of this value is in microseconds. For a CDC load, the rounding of the
      precision depends on the commit timestamp supported by DMS for the source database.

      When the ``AddColumnName`` parameter is set to ``true`` , DMS also includes a name for the
      timestamp column that you set with ``TimestampColumnName`` .

    - **ParquetTimestampInMillisecond** *(boolean) --*

      A value that specifies the precision of any ``TIMESTAMP`` column values that are written to an
      Amazon S3 object file in .parquet format.

      .. note::

        AWS DMS supports the ``ParquetTimestampInMillisecond`` parameter in versions 3.1.4 and later.

      When ``ParquetTimestampInMillisecond`` is set to ``true`` or ``y`` , AWS DMS writes all
      ``TIMESTAMP`` columns in a .parquet formatted file with millisecond precision. Otherwise, DMS
      writes them with microsecond precision.

      Currently, Amazon Athena and AWS Glue can handle only millisecond precision for ``TIMESTAMP``
      values. Set this parameter to ``true`` for S3 endpoint object files that are .parquet formatted
      only if you plan to query or process the data with Athena or AWS Glue.

      .. note::

        AWS DMS writes any ``TIMESTAMP`` column values written to an S3 file in .csv format with
        microsecond precision.

        Setting ``ParquetTimestampInMillisecond`` has no effect on the string format of the timestamp
        column value that is inserted by setting the ``TimestampColumnName`` parameter.
    """


_ClientCreateEndpointTagsTypeDef = TypedDict(
    "_ClientCreateEndpointTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateEndpointTagsTypeDef(_ClientCreateEndpointTagsTypeDef):
    """
    Type definition for `ClientCreateEndpoint` `Tags`

    - **Key** *(string) --*

      A key is the required name of the tag. The string value can be from 1 to 128 Unicode
      characters in length and cannot be prefixed with "aws:" or "dms:". The string can only
      contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-'
      (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").

    - **Value** *(string) --*

      A value is the optional value of the tag. The string value can be from 1 to 256 Unicode
      characters in length and cannot be prefixed with "aws:" or "dms:". The string can only
      contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-'
      (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientCreateEventSubscriptionResponseEventSubscriptionTypeDef = TypedDict(
    "_ClientCreateEventSubscriptionResponseEventSubscriptionTypeDef",
    {
        "CustomerAwsId": str,
        "CustSubscriptionId": str,
        "SnsTopicArn": str,
        "Status": str,
        "SubscriptionCreationTime": str,
        "SourceType": str,
        "SourceIdsList": List[str],
        "EventCategoriesList": List[str],
        "Enabled": bool,
    },
    total=False,
)


class ClientCreateEventSubscriptionResponseEventSubscriptionTypeDef(
    _ClientCreateEventSubscriptionResponseEventSubscriptionTypeDef
):
    """
    Type definition for `ClientCreateEventSubscriptionResponse` `EventSubscription`

    The event subscription that was created.

    - **CustomerAwsId** *(string) --*

      The AWS customer account associated with the AWS DMS event notification subscription.

    - **CustSubscriptionId** *(string) --*

      The AWS DMS event notification subscription Id.

    - **SnsTopicArn** *(string) --*

      The topic ARN of the AWS DMS event notification subscription.

    - **Status** *(string) --*

      The status of the AWS DMS event notification subscription.

      Constraints:

      Can be one of the following: creating | modifying | deleting | active | no-permission |
      topic-not-exist

      The status "no-permission" indicates that AWS DMS no longer has permission to post to the
      SNS topic. The status "topic-not-exist" indicates that the topic was deleted after the
      subscription was created.

    - **SubscriptionCreationTime** *(string) --*

      The time the RDS event notification subscription was created.

    - **SourceType** *(string) --*

      The type of AWS DMS resource that generates events.

      Valid values: replication-instance | replication-server | security-group | replication-task

    - **SourceIdsList** *(list) --*

      A list of source Ids for the event subscription.

      - *(string) --*

    - **EventCategoriesList** *(list) --*

      A lists of event categories.

      - *(string) --*

    - **Enabled** *(boolean) --*

      Boolean value that indicates if the event subscription is enabled.
    """


_ClientCreateEventSubscriptionResponseTypeDef = TypedDict(
    "_ClientCreateEventSubscriptionResponseTypeDef",
    {
        "EventSubscription": ClientCreateEventSubscriptionResponseEventSubscriptionTypeDef
    },
    total=False,
)


class ClientCreateEventSubscriptionResponseTypeDef(
    _ClientCreateEventSubscriptionResponseTypeDef
):
    """
    Type definition for `ClientCreateEventSubscription` `Response`

    - **EventSubscription** *(dict) --*

      The event subscription that was created.

      - **CustomerAwsId** *(string) --*

        The AWS customer account associated with the AWS DMS event notification subscription.

      - **CustSubscriptionId** *(string) --*

        The AWS DMS event notification subscription Id.

      - **SnsTopicArn** *(string) --*

        The topic ARN of the AWS DMS event notification subscription.

      - **Status** *(string) --*

        The status of the AWS DMS event notification subscription.

        Constraints:

        Can be one of the following: creating | modifying | deleting | active | no-permission |
        topic-not-exist

        The status "no-permission" indicates that AWS DMS no longer has permission to post to the
        SNS topic. The status "topic-not-exist" indicates that the topic was deleted after the
        subscription was created.

      - **SubscriptionCreationTime** *(string) --*

        The time the RDS event notification subscription was created.

      - **SourceType** *(string) --*

        The type of AWS DMS resource that generates events.

        Valid values: replication-instance | replication-server | security-group | replication-task

      - **SourceIdsList** *(list) --*

        A list of source Ids for the event subscription.

        - *(string) --*

      - **EventCategoriesList** *(list) --*

        A lists of event categories.

        - *(string) --*

      - **Enabled** *(boolean) --*

        Boolean value that indicates if the event subscription is enabled.
    """


_ClientCreateEventSubscriptionTagsTypeDef = TypedDict(
    "_ClientCreateEventSubscriptionTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateEventSubscriptionTagsTypeDef(
    _ClientCreateEventSubscriptionTagsTypeDef
):
    """
    Type definition for `ClientCreateEventSubscription` `Tags`

    - **Key** *(string) --*

      A key is the required name of the tag. The string value can be from 1 to 128 Unicode
      characters in length and cannot be prefixed with "aws:" or "dms:". The string can only
      contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-'
      (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").

    - **Value** *(string) --*

      A value is the optional value of the tag. The string value can be from 1 to 256 Unicode
      characters in length and cannot be prefixed with "aws:" or "dms:". The string can only
      contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-'
      (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientCreateReplicationInstanceResponseReplicationInstancePendingModifiedValuesTypeDef = TypedDict(
    "_ClientCreateReplicationInstanceResponseReplicationInstancePendingModifiedValuesTypeDef",
    {
        "ReplicationInstanceClass": str,
        "AllocatedStorage": int,
        "MultiAZ": bool,
        "EngineVersion": str,
    },
    total=False,
)


class ClientCreateReplicationInstanceResponseReplicationInstancePendingModifiedValuesTypeDef(
    _ClientCreateReplicationInstanceResponseReplicationInstancePendingModifiedValuesTypeDef
):
    """
    Type definition for `ClientCreateReplicationInstanceResponseReplicationInstance` `PendingModifiedValues`

    The pending modification values.

    - **ReplicationInstanceClass** *(string) --*

      The compute and memory capacity of the replication instance.

      Valid Values: ``dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large | dms.c4.large
      | dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge``

    - **AllocatedStorage** *(integer) --*

      The amount of storage (in gigabytes) that is allocated for the replication instance.

    - **MultiAZ** *(boolean) --*

      Specifies whether the replication instance is a Multi-AZ deployment. You cannot set the
      ``AvailabilityZone`` parameter if the Multi-AZ parameter is set to ``true`` .

    - **EngineVersion** *(string) --*

      The engine version number of the replication instance.
    """


_ClientCreateReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "_ClientCreateReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)


class ClientCreateReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef(
    _ClientCreateReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef
):
    """
    Type definition for `ClientCreateReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnets` `SubnetAvailabilityZone`

    The Availability Zone of the subnet.

    - **Name** *(string) --*

      The name of the availability zone.
    """


_ClientCreateReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsTypeDef = TypedDict(
    "_ClientCreateReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientCreateReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)


class ClientCreateReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsTypeDef(
    _ClientCreateReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsTypeDef
):
    """
    Type definition for `ClientCreateReplicationInstanceResponseReplicationInstanceReplicationSubnetGroup` `Subnets`

    - **SubnetIdentifier** *(string) --*

      The subnet identifier.

    - **SubnetAvailabilityZone** *(dict) --*

      The Availability Zone of the subnet.

      - **Name** *(string) --*

        The name of the availability zone.

    - **SubnetStatus** *(string) --*

      The status of the subnet.
    """


_ClientCreateReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupTypeDef = TypedDict(
    "_ClientCreateReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupTypeDef",
    {
        "ReplicationSubnetGroupIdentifier": str,
        "ReplicationSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[
            ClientCreateReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsTypeDef
        ],
    },
    total=False,
)


class ClientCreateReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupTypeDef(
    _ClientCreateReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupTypeDef
):
    """
    Type definition for `ClientCreateReplicationInstanceResponseReplicationInstance` `ReplicationSubnetGroup`

    The subnet group for the replication instance.

    - **ReplicationSubnetGroupIdentifier** *(string) --*

      The identifier of the replication instance subnet group.

    - **ReplicationSubnetGroupDescription** *(string) --*

      A description for the replication subnet group.

    - **VpcId** *(string) --*

      The ID of the VPC.

    - **SubnetGroupStatus** *(string) --*

      The status of the subnet group.

    - **Subnets** *(list) --*

      The subnets that are in the subnet group.

      - *(dict) --*

        - **SubnetIdentifier** *(string) --*

          The subnet identifier.

        - **SubnetAvailabilityZone** *(dict) --*

          The Availability Zone of the subnet.

          - **Name** *(string) --*

            The name of the availability zone.

        - **SubnetStatus** *(string) --*

          The status of the subnet.
    """


_ClientCreateReplicationInstanceResponseReplicationInstanceVpcSecurityGroupsTypeDef = TypedDict(
    "_ClientCreateReplicationInstanceResponseReplicationInstanceVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientCreateReplicationInstanceResponseReplicationInstanceVpcSecurityGroupsTypeDef(
    _ClientCreateReplicationInstanceResponseReplicationInstanceVpcSecurityGroupsTypeDef
):
    """
    Type definition for `ClientCreateReplicationInstanceResponseReplicationInstance` `VpcSecurityGroups`

    - **VpcSecurityGroupId** *(string) --*

      The VPC security group Id.

    - **Status** *(string) --*

      The status of the VPC security group.
    """


_ClientCreateReplicationInstanceResponseReplicationInstanceTypeDef = TypedDict(
    "_ClientCreateReplicationInstanceResponseReplicationInstanceTypeDef",
    {
        "ReplicationInstanceIdentifier": str,
        "ReplicationInstanceClass": str,
        "ReplicationInstanceStatus": str,
        "AllocatedStorage": int,
        "InstanceCreateTime": datetime,
        "VpcSecurityGroups": List[
            ClientCreateReplicationInstanceResponseReplicationInstanceVpcSecurityGroupsTypeDef
        ],
        "AvailabilityZone": str,
        "ReplicationSubnetGroup": ClientCreateReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupTypeDef,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientCreateReplicationInstanceResponseReplicationInstancePendingModifiedValuesTypeDef,
        "MultiAZ": bool,
        "EngineVersion": str,
        "AutoMinorVersionUpgrade": bool,
        "KmsKeyId": str,
        "ReplicationInstanceArn": str,
        "ReplicationInstancePublicIpAddress": str,
        "ReplicationInstancePrivateIpAddress": str,
        "ReplicationInstancePublicIpAddresses": List[str],
        "ReplicationInstancePrivateIpAddresses": List[str],
        "PubliclyAccessible": bool,
        "SecondaryAvailabilityZone": str,
        "FreeUntil": datetime,
        "DnsNameServers": str,
    },
    total=False,
)


class ClientCreateReplicationInstanceResponseReplicationInstanceTypeDef(
    _ClientCreateReplicationInstanceResponseReplicationInstanceTypeDef
):
    """
    Type definition for `ClientCreateReplicationInstanceResponse` `ReplicationInstance`

    The replication instance that was created.

    - **ReplicationInstanceIdentifier** *(string) --*

      The replication instance identifier. This parameter is stored as a lowercase string.

      Constraints:

      * Must contain from 1 to 63 alphanumeric characters or hyphens.

      * First character must be a letter.

      * Cannot end with a hyphen or contain two consecutive hyphens.

      Example: ``myrepinstance``

    - **ReplicationInstanceClass** *(string) --*

      The compute and memory capacity of the replication instance.

      Valid Values: ``dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large | dms.c4.large |
      dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge``

    - **ReplicationInstanceStatus** *(string) --*

      The status of the replication instance.

    - **AllocatedStorage** *(integer) --*

      The amount of storage (in gigabytes) that is allocated for the replication instance.

    - **InstanceCreateTime** *(datetime) --*

      The time the replication instance was created.

    - **VpcSecurityGroups** *(list) --*

      The VPC security group for the instance.

      - *(dict) --*

        - **VpcSecurityGroupId** *(string) --*

          The VPC security group Id.

        - **Status** *(string) --*

          The status of the VPC security group.

    - **AvailabilityZone** *(string) --*

      The Availability Zone for the instance.

    - **ReplicationSubnetGroup** *(dict) --*

      The subnet group for the replication instance.

      - **ReplicationSubnetGroupIdentifier** *(string) --*

        The identifier of the replication instance subnet group.

      - **ReplicationSubnetGroupDescription** *(string) --*

        A description for the replication subnet group.

      - **VpcId** *(string) --*

        The ID of the VPC.

      - **SubnetGroupStatus** *(string) --*

        The status of the subnet group.

      - **Subnets** *(list) --*

        The subnets that are in the subnet group.

        - *(dict) --*

          - **SubnetIdentifier** *(string) --*

            The subnet identifier.

          - **SubnetAvailabilityZone** *(dict) --*

            The Availability Zone of the subnet.

            - **Name** *(string) --*

              The name of the availability zone.

          - **SubnetStatus** *(string) --*

            The status of the subnet.

    - **PreferredMaintenanceWindow** *(string) --*

      The maintenance window times for the replication instance.

    - **PendingModifiedValues** *(dict) --*

      The pending modification values.

      - **ReplicationInstanceClass** *(string) --*

        The compute and memory capacity of the replication instance.

        Valid Values: ``dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large | dms.c4.large
        | dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge``

      - **AllocatedStorage** *(integer) --*

        The amount of storage (in gigabytes) that is allocated for the replication instance.

      - **MultiAZ** *(boolean) --*

        Specifies whether the replication instance is a Multi-AZ deployment. You cannot set the
        ``AvailabilityZone`` parameter if the Multi-AZ parameter is set to ``true`` .

      - **EngineVersion** *(string) --*

        The engine version number of the replication instance.

    - **MultiAZ** *(boolean) --*

      Specifies whether the replication instance is a Multi-AZ deployment. You cannot set the
      ``AvailabilityZone`` parameter if the Multi-AZ parameter is set to ``true`` .

    - **EngineVersion** *(string) --*

      The engine version number of the replication instance.

    - **AutoMinorVersionUpgrade** *(boolean) --*

      Boolean value indicating if minor version upgrades will be automatically applied to the
      instance.

    - **KmsKeyId** *(string) --*

      An AWS KMS key identifier that is used to encrypt the data on the replication instance.

      If you don't specify a value for the ``KmsKeyId`` parameter, then AWS DMS uses your default
      encryption key.

      AWS KMS creates the default encryption key for your AWS account. Your AWS account has a
      different default encryption key for each AWS Region.

    - **ReplicationInstanceArn** *(string) --*

      The Amazon Resource Name (ARN) of the replication instance.

    - **ReplicationInstancePublicIpAddress** *(string) --*

      The public IP address of the replication instance.

    - **ReplicationInstancePrivateIpAddress** *(string) --*

      The private IP address of the replication instance.

    - **ReplicationInstancePublicIpAddresses** *(list) --*

      One or more public IP addresses for the replication instance.

      - *(string) --*

    - **ReplicationInstancePrivateIpAddresses** *(list) --*

      One or more private IP addresses for the replication instance.

      - *(string) --*

    - **PubliclyAccessible** *(boolean) --*

      Specifies the accessibility options for the replication instance. A value of ``true``
      represents an instance with a public IP address. A value of ``false`` represents an
      instance with a private IP address. The default value is ``true`` .

    - **SecondaryAvailabilityZone** *(string) --*

      The availability zone of the standby replication instance in a Multi-AZ deployment.

    - **FreeUntil** *(datetime) --*

      The expiration date of the free replication instance that is part of the Free DMS program.

    - **DnsNameServers** *(string) --*

      The DNS name servers for the replication instance.
    """


_ClientCreateReplicationInstanceResponseTypeDef = TypedDict(
    "_ClientCreateReplicationInstanceResponseTypeDef",
    {
        "ReplicationInstance": ClientCreateReplicationInstanceResponseReplicationInstanceTypeDef
    },
    total=False,
)


class ClientCreateReplicationInstanceResponseTypeDef(
    _ClientCreateReplicationInstanceResponseTypeDef
):
    """
    Type definition for `ClientCreateReplicationInstance` `Response`

    - **ReplicationInstance** *(dict) --*

      The replication instance that was created.

      - **ReplicationInstanceIdentifier** *(string) --*

        The replication instance identifier. This parameter is stored as a lowercase string.

        Constraints:

        * Must contain from 1 to 63 alphanumeric characters or hyphens.

        * First character must be a letter.

        * Cannot end with a hyphen or contain two consecutive hyphens.

        Example: ``myrepinstance``

      - **ReplicationInstanceClass** *(string) --*

        The compute and memory capacity of the replication instance.

        Valid Values: ``dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large | dms.c4.large |
        dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge``

      - **ReplicationInstanceStatus** *(string) --*

        The status of the replication instance.

      - **AllocatedStorage** *(integer) --*

        The amount of storage (in gigabytes) that is allocated for the replication instance.

      - **InstanceCreateTime** *(datetime) --*

        The time the replication instance was created.

      - **VpcSecurityGroups** *(list) --*

        The VPC security group for the instance.

        - *(dict) --*

          - **VpcSecurityGroupId** *(string) --*

            The VPC security group Id.

          - **Status** *(string) --*

            The status of the VPC security group.

      - **AvailabilityZone** *(string) --*

        The Availability Zone for the instance.

      - **ReplicationSubnetGroup** *(dict) --*

        The subnet group for the replication instance.

        - **ReplicationSubnetGroupIdentifier** *(string) --*

          The identifier of the replication instance subnet group.

        - **ReplicationSubnetGroupDescription** *(string) --*

          A description for the replication subnet group.

        - **VpcId** *(string) --*

          The ID of the VPC.

        - **SubnetGroupStatus** *(string) --*

          The status of the subnet group.

        - **Subnets** *(list) --*

          The subnets that are in the subnet group.

          - *(dict) --*

            - **SubnetIdentifier** *(string) --*

              The subnet identifier.

            - **SubnetAvailabilityZone** *(dict) --*

              The Availability Zone of the subnet.

              - **Name** *(string) --*

                The name of the availability zone.

            - **SubnetStatus** *(string) --*

              The status of the subnet.

      - **PreferredMaintenanceWindow** *(string) --*

        The maintenance window times for the replication instance.

      - **PendingModifiedValues** *(dict) --*

        The pending modification values.

        - **ReplicationInstanceClass** *(string) --*

          The compute and memory capacity of the replication instance.

          Valid Values: ``dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large | dms.c4.large
          | dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge``

        - **AllocatedStorage** *(integer) --*

          The amount of storage (in gigabytes) that is allocated for the replication instance.

        - **MultiAZ** *(boolean) --*

          Specifies whether the replication instance is a Multi-AZ deployment. You cannot set the
          ``AvailabilityZone`` parameter if the Multi-AZ parameter is set to ``true`` .

        - **EngineVersion** *(string) --*

          The engine version number of the replication instance.

      - **MultiAZ** *(boolean) --*

        Specifies whether the replication instance is a Multi-AZ deployment. You cannot set the
        ``AvailabilityZone`` parameter if the Multi-AZ parameter is set to ``true`` .

      - **EngineVersion** *(string) --*

        The engine version number of the replication instance.

      - **AutoMinorVersionUpgrade** *(boolean) --*

        Boolean value indicating if minor version upgrades will be automatically applied to the
        instance.

      - **KmsKeyId** *(string) --*

        An AWS KMS key identifier that is used to encrypt the data on the replication instance.

        If you don't specify a value for the ``KmsKeyId`` parameter, then AWS DMS uses your default
        encryption key.

        AWS KMS creates the default encryption key for your AWS account. Your AWS account has a
        different default encryption key for each AWS Region.

      - **ReplicationInstanceArn** *(string) --*

        The Amazon Resource Name (ARN) of the replication instance.

      - **ReplicationInstancePublicIpAddress** *(string) --*

        The public IP address of the replication instance.

      - **ReplicationInstancePrivateIpAddress** *(string) --*

        The private IP address of the replication instance.

      - **ReplicationInstancePublicIpAddresses** *(list) --*

        One or more public IP addresses for the replication instance.

        - *(string) --*

      - **ReplicationInstancePrivateIpAddresses** *(list) --*

        One or more private IP addresses for the replication instance.

        - *(string) --*

      - **PubliclyAccessible** *(boolean) --*

        Specifies the accessibility options for the replication instance. A value of ``true``
        represents an instance with a public IP address. A value of ``false`` represents an
        instance with a private IP address. The default value is ``true`` .

      - **SecondaryAvailabilityZone** *(string) --*

        The availability zone of the standby replication instance in a Multi-AZ deployment.

      - **FreeUntil** *(datetime) --*

        The expiration date of the free replication instance that is part of the Free DMS program.

      - **DnsNameServers** *(string) --*

        The DNS name servers for the replication instance.
    """


_ClientCreateReplicationInstanceTagsTypeDef = TypedDict(
    "_ClientCreateReplicationInstanceTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientCreateReplicationInstanceTagsTypeDef(
    _ClientCreateReplicationInstanceTagsTypeDef
):
    """
    Type definition for `ClientCreateReplicationInstance` `Tags`

    - **Key** *(string) --*

      A key is the required name of the tag. The string value can be from 1 to 128 Unicode
      characters in length and cannot be prefixed with "aws:" or "dms:". The string can only
      contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-'
      (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").

    - **Value** *(string) --*

      A value is the optional value of the tag. The string value can be from 1 to 256 Unicode
      characters in length and cannot be prefixed with "aws:" or "dms:". The string can only
      contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-'
      (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientCreateReplicationSubnetGroupResponseReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "_ClientCreateReplicationSubnetGroupResponseReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)


class ClientCreateReplicationSubnetGroupResponseReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef(
    _ClientCreateReplicationSubnetGroupResponseReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef
):
    """
    Type definition for `ClientCreateReplicationSubnetGroupResponseReplicationSubnetGroupSubnets` `SubnetAvailabilityZone`

    The Availability Zone of the subnet.

    - **Name** *(string) --*

      The name of the availability zone.
    """


_ClientCreateReplicationSubnetGroupResponseReplicationSubnetGroupSubnetsTypeDef = TypedDict(
    "_ClientCreateReplicationSubnetGroupResponseReplicationSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientCreateReplicationSubnetGroupResponseReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)


class ClientCreateReplicationSubnetGroupResponseReplicationSubnetGroupSubnetsTypeDef(
    _ClientCreateReplicationSubnetGroupResponseReplicationSubnetGroupSubnetsTypeDef
):
    """
    Type definition for `ClientCreateReplicationSubnetGroupResponseReplicationSubnetGroup` `Subnets`

    - **SubnetIdentifier** *(string) --*

      The subnet identifier.

    - **SubnetAvailabilityZone** *(dict) --*

      The Availability Zone of the subnet.

      - **Name** *(string) --*

        The name of the availability zone.

    - **SubnetStatus** *(string) --*

      The status of the subnet.
    """


_ClientCreateReplicationSubnetGroupResponseReplicationSubnetGroupTypeDef = TypedDict(
    "_ClientCreateReplicationSubnetGroupResponseReplicationSubnetGroupTypeDef",
    {
        "ReplicationSubnetGroupIdentifier": str,
        "ReplicationSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[
            ClientCreateReplicationSubnetGroupResponseReplicationSubnetGroupSubnetsTypeDef
        ],
    },
    total=False,
)


class ClientCreateReplicationSubnetGroupResponseReplicationSubnetGroupTypeDef(
    _ClientCreateReplicationSubnetGroupResponseReplicationSubnetGroupTypeDef
):
    """
    Type definition for `ClientCreateReplicationSubnetGroupResponse` `ReplicationSubnetGroup`

    The replication subnet group that was created.

    - **ReplicationSubnetGroupIdentifier** *(string) --*

      The identifier of the replication instance subnet group.

    - **ReplicationSubnetGroupDescription** *(string) --*

      A description for the replication subnet group.

    - **VpcId** *(string) --*

      The ID of the VPC.

    - **SubnetGroupStatus** *(string) --*

      The status of the subnet group.

    - **Subnets** *(list) --*

      The subnets that are in the subnet group.

      - *(dict) --*

        - **SubnetIdentifier** *(string) --*

          The subnet identifier.

        - **SubnetAvailabilityZone** *(dict) --*

          The Availability Zone of the subnet.

          - **Name** *(string) --*

            The name of the availability zone.

        - **SubnetStatus** *(string) --*

          The status of the subnet.
    """


_ClientCreateReplicationSubnetGroupResponseTypeDef = TypedDict(
    "_ClientCreateReplicationSubnetGroupResponseTypeDef",
    {
        "ReplicationSubnetGroup": ClientCreateReplicationSubnetGroupResponseReplicationSubnetGroupTypeDef
    },
    total=False,
)


class ClientCreateReplicationSubnetGroupResponseTypeDef(
    _ClientCreateReplicationSubnetGroupResponseTypeDef
):
    """
    Type definition for `ClientCreateReplicationSubnetGroup` `Response`

    - **ReplicationSubnetGroup** *(dict) --*

      The replication subnet group that was created.

      - **ReplicationSubnetGroupIdentifier** *(string) --*

        The identifier of the replication instance subnet group.

      - **ReplicationSubnetGroupDescription** *(string) --*

        A description for the replication subnet group.

      - **VpcId** *(string) --*

        The ID of the VPC.

      - **SubnetGroupStatus** *(string) --*

        The status of the subnet group.

      - **Subnets** *(list) --*

        The subnets that are in the subnet group.

        - *(dict) --*

          - **SubnetIdentifier** *(string) --*

            The subnet identifier.

          - **SubnetAvailabilityZone** *(dict) --*

            The Availability Zone of the subnet.

            - **Name** *(string) --*

              The name of the availability zone.

          - **SubnetStatus** *(string) --*

            The status of the subnet.
    """


_ClientCreateReplicationSubnetGroupTagsTypeDef = TypedDict(
    "_ClientCreateReplicationSubnetGroupTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientCreateReplicationSubnetGroupTagsTypeDef(
    _ClientCreateReplicationSubnetGroupTagsTypeDef
):
    """
    Type definition for `ClientCreateReplicationSubnetGroup` `Tags`

    - **Key** *(string) --*

      A key is the required name of the tag. The string value can be from 1 to 128 Unicode
      characters in length and cannot be prefixed with "aws:" or "dms:". The string can only
      contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-'
      (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").

    - **Value** *(string) --*

      A value is the optional value of the tag. The string value can be from 1 to 256 Unicode
      characters in length and cannot be prefixed with "aws:" or "dms:". The string can only
      contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-'
      (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientCreateReplicationTaskTagsTypeDef = TypedDict(
    "_ClientCreateReplicationTaskTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateReplicationTaskTagsTypeDef(_ClientCreateReplicationTaskTagsTypeDef):
    """
    Type definition for `ClientCreateReplicationTask` `Tags`

    - **Key** *(string) --*

      A key is the required name of the tag. The string value can be from 1 to 128 Unicode
      characters in length and cannot be prefixed with "aws:" or "dms:". The string can only
      contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-'
      (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").

    - **Value** *(string) --*

      A value is the optional value of the tag. The string value can be from 1 to 256 Unicode
      characters in length and cannot be prefixed with "aws:" or "dms:". The string can only
      contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-'
      (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientDeleteCertificateResponseCertificateTypeDef = TypedDict(
    "_ClientDeleteCertificateResponseCertificateTypeDef",
    {
        "CertificateIdentifier": str,
        "CertificateCreationDate": datetime,
        "CertificatePem": str,
        "CertificateWallet": bytes,
        "CertificateArn": str,
        "CertificateOwner": str,
        "ValidFromDate": datetime,
        "ValidToDate": datetime,
        "SigningAlgorithm": str,
        "KeyLength": int,
    },
    total=False,
)


class ClientDeleteCertificateResponseCertificateTypeDef(
    _ClientDeleteCertificateResponseCertificateTypeDef
):
    """
    Type definition for `ClientDeleteCertificateResponse` `Certificate`

    The Secure Sockets Layer (SSL) certificate.

    - **CertificateIdentifier** *(string) --*

      A customer-assigned name for the certificate. Identifiers must begin with a letter; must
      contain only ASCII letters, digits, and hyphens; and must not end with a hyphen or contain
      two consecutive hyphens.

    - **CertificateCreationDate** *(datetime) --*

      The date that the certificate was created.

    - **CertificatePem** *(string) --*

      The contents of a ``.pem`` file, which contains an X.509 certificate.

    - **CertificateWallet** *(bytes) --*

      The location of an imported Oracle Wallet certificate for use with SSL.

    - **CertificateArn** *(string) --*

      The Amazon Resource Name (ARN) for the certificate.

    - **CertificateOwner** *(string) --*

      The owner of the certificate.

    - **ValidFromDate** *(datetime) --*

      The beginning date that the certificate is valid.

    - **ValidToDate** *(datetime) --*

      The final date that the certificate is valid.

    - **SigningAlgorithm** *(string) --*

      The signing algorithm for the certificate.

    - **KeyLength** *(integer) --*

      The key length of the cryptographic algorithm being used.
    """


_ClientDeleteCertificateResponseTypeDef = TypedDict(
    "_ClientDeleteCertificateResponseTypeDef",
    {"Certificate": ClientDeleteCertificateResponseCertificateTypeDef},
    total=False,
)


class ClientDeleteCertificateResponseTypeDef(_ClientDeleteCertificateResponseTypeDef):
    """
    Type definition for `ClientDeleteCertificate` `Response`

    - **Certificate** *(dict) --*

      The Secure Sockets Layer (SSL) certificate.

      - **CertificateIdentifier** *(string) --*

        A customer-assigned name for the certificate. Identifiers must begin with a letter; must
        contain only ASCII letters, digits, and hyphens; and must not end with a hyphen or contain
        two consecutive hyphens.

      - **CertificateCreationDate** *(datetime) --*

        The date that the certificate was created.

      - **CertificatePem** *(string) --*

        The contents of a ``.pem`` file, which contains an X.509 certificate.

      - **CertificateWallet** *(bytes) --*

        The location of an imported Oracle Wallet certificate for use with SSL.

      - **CertificateArn** *(string) --*

        The Amazon Resource Name (ARN) for the certificate.

      - **CertificateOwner** *(string) --*

        The owner of the certificate.

      - **ValidFromDate** *(datetime) --*

        The beginning date that the certificate is valid.

      - **ValidToDate** *(datetime) --*

        The final date that the certificate is valid.

      - **SigningAlgorithm** *(string) --*

        The signing algorithm for the certificate.

      - **KeyLength** *(integer) --*

        The key length of the cryptographic algorithm being used.
    """


_ClientDeleteConnectionResponseConnectionTypeDef = TypedDict(
    "_ClientDeleteConnectionResponseConnectionTypeDef",
    {
        "ReplicationInstanceArn": str,
        "EndpointArn": str,
        "Status": str,
        "LastFailureMessage": str,
        "EndpointIdentifier": str,
        "ReplicationInstanceIdentifier": str,
    },
    total=False,
)


class ClientDeleteConnectionResponseConnectionTypeDef(
    _ClientDeleteConnectionResponseConnectionTypeDef
):
    """
    Type definition for `ClientDeleteConnectionResponse` `Connection`

    The connection that is being deleted.

    - **ReplicationInstanceArn** *(string) --*

      The Amazon Resource Name (ARN) of the replication instance.

    - **EndpointArn** *(string) --*

      The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

    - **Status** *(string) --*

      The connection status.

    - **LastFailureMessage** *(string) --*

      The error message when the connection last failed.

    - **EndpointIdentifier** *(string) --*

      The identifier of the endpoint. Identifiers must begin with a letter; must contain only
      ASCII letters, digits, and hyphens; and must not end with a hyphen or contain two
      consecutive hyphens.

    - **ReplicationInstanceIdentifier** *(string) --*

      The replication instance identifier. This parameter is stored as a lowercase string.
    """


_ClientDeleteConnectionResponseTypeDef = TypedDict(
    "_ClientDeleteConnectionResponseTypeDef",
    {"Connection": ClientDeleteConnectionResponseConnectionTypeDef},
    total=False,
)


class ClientDeleteConnectionResponseTypeDef(_ClientDeleteConnectionResponseTypeDef):
    """
    Type definition for `ClientDeleteConnection` `Response`

    - **Connection** *(dict) --*

      The connection that is being deleted.

      - **ReplicationInstanceArn** *(string) --*

        The Amazon Resource Name (ARN) of the replication instance.

      - **EndpointArn** *(string) --*

        The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

      - **Status** *(string) --*

        The connection status.

      - **LastFailureMessage** *(string) --*

        The error message when the connection last failed.

      - **EndpointIdentifier** *(string) --*

        The identifier of the endpoint. Identifiers must begin with a letter; must contain only
        ASCII letters, digits, and hyphens; and must not end with a hyphen or contain two
        consecutive hyphens.

      - **ReplicationInstanceIdentifier** *(string) --*

        The replication instance identifier. This parameter is stored as a lowercase string.
    """


_ClientDeleteEndpointResponseEndpointDmsTransferSettingsTypeDef = TypedDict(
    "_ClientDeleteEndpointResponseEndpointDmsTransferSettingsTypeDef",
    {"ServiceAccessRoleArn": str, "BucketName": str},
    total=False,
)


class ClientDeleteEndpointResponseEndpointDmsTransferSettingsTypeDef(
    _ClientDeleteEndpointResponseEndpointDmsTransferSettingsTypeDef
):
    """
    Type definition for `ClientDeleteEndpointResponseEndpoint` `DmsTransferSettings`

    The settings in JSON format for the DMS transfer type of source endpoint.

    Possible settings include the following:

    * ``ServiceAccessRoleArn`` - The IAM role that has permission to access the Amazon S3
    bucket.

    * ``BucketName`` - The name of the S3 bucket to use.

    * ``CompressionType`` - An optional parameter to use GZIP to compress the target files. To
    use GZIP, set this value to ``NONE`` (the default). To keep the files uncompressed, don't
    use this value.

    Shorthand syntax for these settings is as follows:
    ``ServiceAccessRoleArn=string,BucketName=string,CompressionType=string``

    JSON syntax for these settings is as follows: ``{ "ServiceAccessRoleArn": "string",
    "BucketName": "string", "CompressionType": "none"|"gzip" }``

    - **ServiceAccessRoleArn** *(string) --*

      The IAM role that has permission to access the Amazon S3 bucket.

    - **BucketName** *(string) --*

      The name of the S3 bucket to use.
    """


_ClientDeleteEndpointResponseEndpointDynamoDbSettingsTypeDef = TypedDict(
    "_ClientDeleteEndpointResponseEndpointDynamoDbSettingsTypeDef",
    {"ServiceAccessRoleArn": str},
    total=False,
)


class ClientDeleteEndpointResponseEndpointDynamoDbSettingsTypeDef(
    _ClientDeleteEndpointResponseEndpointDynamoDbSettingsTypeDef
):
    """
    Type definition for `ClientDeleteEndpointResponseEndpoint` `DynamoDbSettings`

    The settings for the target DynamoDB database. For more information, see the
    ``DynamoDBSettings`` structure.

    - **ServiceAccessRoleArn** *(string) --*

      The Amazon Resource Name (ARN) used by the service access IAM role.
    """


_ClientDeleteEndpointResponseEndpointElasticsearchSettingsTypeDef = TypedDict(
    "_ClientDeleteEndpointResponseEndpointElasticsearchSettingsTypeDef",
    {
        "ServiceAccessRoleArn": str,
        "EndpointUri": str,
        "FullLoadErrorPercentage": int,
        "ErrorRetryDuration": int,
    },
    total=False,
)


class ClientDeleteEndpointResponseEndpointElasticsearchSettingsTypeDef(
    _ClientDeleteEndpointResponseEndpointElasticsearchSettingsTypeDef
):
    """
    Type definition for `ClientDeleteEndpointResponseEndpoint` `ElasticsearchSettings`

    The settings for the Elasticsearch source endpoint. For more information, see the
    ``ElasticsearchSettings`` structure.

    - **ServiceAccessRoleArn** *(string) --*

      The Amazon Resource Name (ARN) used by service to access the IAM role.

    - **EndpointUri** *(string) --*

      The endpoint for the Elasticsearch cluster.

    - **FullLoadErrorPercentage** *(integer) --*

      The maximum percentage of records that can fail to be written before a full load
      operation stops.

    - **ErrorRetryDuration** *(integer) --*

      The maximum number of seconds that DMS retries failed API requests to the Elasticsearch
      cluster.
    """


_ClientDeleteEndpointResponseEndpointKinesisSettingsTypeDef = TypedDict(
    "_ClientDeleteEndpointResponseEndpointKinesisSettingsTypeDef",
    {"StreamArn": str, "MessageFormat": str, "ServiceAccessRoleArn": str},
    total=False,
)


class ClientDeleteEndpointResponseEndpointKinesisSettingsTypeDef(
    _ClientDeleteEndpointResponseEndpointKinesisSettingsTypeDef
):
    """
    Type definition for `ClientDeleteEndpointResponseEndpoint` `KinesisSettings`

    The settings for the Amazon Kinesis source endpoint. For more information, see the
    ``KinesisSettings`` structure.

    - **StreamArn** *(string) --*

      The Amazon Resource Name (ARN) for the Amazon Kinesis Data Streams endpoint.

    - **MessageFormat** *(string) --*

      The output format for the records created on the endpoint. The message format is ``JSON``
      .

    - **ServiceAccessRoleArn** *(string) --*

      The Amazon Resource Name (ARN) for the IAM role that DMS uses to write to the Amazon
      Kinesis data stream.
    """


_ClientDeleteEndpointResponseEndpointMongoDbSettingsTypeDef = TypedDict(
    "_ClientDeleteEndpointResponseEndpointMongoDbSettingsTypeDef",
    {
        "Username": str,
        "Password": str,
        "ServerName": str,
        "Port": int,
        "DatabaseName": str,
        "AuthType": str,
        "AuthMechanism": str,
        "NestingLevel": str,
        "ExtractDocId": str,
        "DocsToInvestigate": str,
        "AuthSource": str,
        "KmsKeyId": str,
    },
    total=False,
)


class ClientDeleteEndpointResponseEndpointMongoDbSettingsTypeDef(
    _ClientDeleteEndpointResponseEndpointMongoDbSettingsTypeDef
):
    """
    Type definition for `ClientDeleteEndpointResponseEndpoint` `MongoDbSettings`

    The settings for the MongoDB source endpoint. For more information, see the
    ``MongoDbSettings`` structure.

    - **Username** *(string) --*

      The user name you use to access the MongoDB source endpoint.

    - **Password** *(string) --*

      The password for the user account you use to access the MongoDB source endpoint.

    - **ServerName** *(string) --*

      The name of the server on the MongoDB source endpoint.

    - **Port** *(integer) --*

      The port value for the MongoDB source endpoint.

    - **DatabaseName** *(string) --*

      The database name on the MongoDB source endpoint.

    - **AuthType** *(string) --*

      The authentication type you use to access the MongoDB source endpoint.

      Valid values: NO, PASSWORD

      When NO is selected, user name and password parameters are not used and can be empty.

    - **AuthMechanism** *(string) --*

      The authentication mechanism you use to access the MongoDB source endpoint.

      Valid values: DEFAULT, MONGODB_CR, SCRAM_SHA_1

      DEFAULT – For MongoDB version 2.x, use MONGODB_CR. For MongoDB version 3.x, use
      SCRAM_SHA_1. This setting is not used when authType=No.

    - **NestingLevel** *(string) --*

      Specifies either document or table mode.

      Valid values: NONE, ONE

      Default value is NONE. Specify NONE to use document mode. Specify ONE to use table mode.

    - **ExtractDocId** *(string) --*

      Specifies the document ID. Use this setting when ``NestingLevel`` is set to NONE.

      Default value is false.

    - **DocsToInvestigate** *(string) --*

      Indicates the number of documents to preview to determine the document organization. Use
      this setting when ``NestingLevel`` is set to ONE.

      Must be a positive value greater than 0. Default value is 1000.

    - **AuthSource** *(string) --*

      The MongoDB database name. This setting is not used when ``authType=NO`` .

      The default is admin.

    - **KmsKeyId** *(string) --*

      The AWS KMS key identifier that is used to encrypt the content on the replication
      instance. If you don't specify a value for the ``KmsKeyId`` parameter, then AWS DMS uses
      your default encryption key. AWS KMS creates the default encryption key for your AWS
      account. Your AWS account has a different default encryption key for each AWS Region.
    """


_ClientDeleteEndpointResponseEndpointRedshiftSettingsTypeDef = TypedDict(
    "_ClientDeleteEndpointResponseEndpointRedshiftSettingsTypeDef",
    {
        "AcceptAnyDate": bool,
        "AfterConnectScript": str,
        "BucketFolder": str,
        "BucketName": str,
        "ConnectionTimeout": int,
        "DatabaseName": str,
        "DateFormat": str,
        "EmptyAsNull": bool,
        "EncryptionMode": str,
        "FileTransferUploadStreams": int,
        "LoadTimeout": int,
        "MaxFileSize": int,
        "Password": str,
        "Port": int,
        "RemoveQuotes": bool,
        "ReplaceInvalidChars": str,
        "ReplaceChars": str,
        "ServerName": str,
        "ServiceAccessRoleArn": str,
        "ServerSideEncryptionKmsKeyId": str,
        "TimeFormat": str,
        "TrimBlanks": bool,
        "TruncateColumns": bool,
        "Username": str,
        "WriteBufferSize": int,
    },
    total=False,
)


class ClientDeleteEndpointResponseEndpointRedshiftSettingsTypeDef(
    _ClientDeleteEndpointResponseEndpointRedshiftSettingsTypeDef
):
    """
    Type definition for `ClientDeleteEndpointResponseEndpoint` `RedshiftSettings`

    Settings for the Amazon Redshift endpoint.

    - **AcceptAnyDate** *(boolean) --*

      A value that indicates to allow any date format, including invalid formats such as
      00/00/00 00:00:00, to be loaded without generating an error. You can choose ``true`` or
      ``false`` (the default).

      This parameter applies only to TIMESTAMP and DATE columns. Always use ACCEPTANYDATE with
      the DATEFORMAT parameter. If the date format for the data doesn't match the DATEFORMAT
      specification, Amazon Redshift inserts a NULL value into that field.

    - **AfterConnectScript** *(string) --*

      Code to run after connecting. This parameter should contain the code itself, not the name
      of a file containing the code.

    - **BucketFolder** *(string) --*

      The location where the comma-separated value (.csv) files are stored before being
      uploaded to the S3 bucket.

    - **BucketName** *(string) --*

      The name of the S3 bucket you want to use

    - **ConnectionTimeout** *(integer) --*

      A value that sets the amount of time to wait (in milliseconds) before timing out,
      beginning from when you initially establish a connection.

    - **DatabaseName** *(string) --*

      The name of the Amazon Redshift data warehouse (service) that you are working with.

    - **DateFormat** *(string) --*

      The date format that you are using. Valid values are ``auto`` (case-sensitive), your date
      format string enclosed in quotes, or NULL. If this parameter is left unset (NULL), it
      defaults to a format of 'YYYY-MM-DD'. Using ``auto`` recognizes most strings, even some
      that aren't supported when you use a date format string.

      If your date and time values use formats different from each other, set this to ``auto`` .

    - **EmptyAsNull** *(boolean) --*

      A value that specifies whether AWS DMS should migrate empty CHAR and VARCHAR fields as
      NULL. A value of ``true`` sets empty CHAR and VARCHAR fields to null. The default is
      ``false`` .

    - **EncryptionMode** *(string) --*

      The type of server-side encryption that you want to use for your data. This encryption
      type is part of the endpoint settings or the extra connections attributes for Amazon S3.
      You can choose either ``SSE_S3`` (the default) or ``SSE_KMS`` . To use ``SSE_S3`` ,
      create an AWS Identity and Access Management (IAM) role with a policy that allows
      ``"arn:aws:s3:::*"`` to use the following actions: ``"s3:PutObject", "s3:ListBucket"``

    - **FileTransferUploadStreams** *(integer) --*

      The number of threads used to upload a single file. This parameter accepts a value from 1
      through 64. It defaults to 10.

    - **LoadTimeout** *(integer) --*

      The amount of time to wait (in milliseconds) before timing out, beginning from when you
      begin loading.

    - **MaxFileSize** *(integer) --*

      The maximum size (in KB) of any .csv file used to transfer data to Amazon Redshift. This
      accepts a value from 1 through 1,048,576. It defaults to 32,768 KB (32 MB).

    - **Password** *(string) --*

      The password for the user named in the ``username`` property.

    - **Port** *(integer) --*

      The port number for Amazon Redshift. The default value is 5439.

    - **RemoveQuotes** *(boolean) --*

      A value that specifies to remove surrounding quotation marks from strings in the incoming
      data. All characters within the quotation marks, including delimiters, are retained.
      Choose ``true`` to remove quotation marks. The default is ``false`` .

    - **ReplaceInvalidChars** *(string) --*

      A list of characters that you want to replace. Use with ``ReplaceChars`` .

    - **ReplaceChars** *(string) --*

      A value that specifies to replaces the invalid characters specified in
      ``ReplaceInvalidChars`` , substituting the specified characters instead. The default is
      ``"?"`` .

    - **ServerName** *(string) --*

      The name of the Amazon Redshift cluster you are using.

    - **ServiceAccessRoleArn** *(string) --*

      The Amazon Resource Name (ARN) of the IAM role that has access to the Amazon Redshift
      service.

    - **ServerSideEncryptionKmsKeyId** *(string) --*

      The AWS KMS key ID. If you are using ``SSE_KMS`` for the ``EncryptionMode`` , provide
      this key ID. The key that you use needs an attached policy that enables IAM user
      permissions and allows use of the key.

    - **TimeFormat** *(string) --*

      The time format that you want to use. Valid values are ``auto`` (case-sensitive),
      ``'timeformat_string'`` , ``'epochsecs'`` , or ``'epochmillisecs'`` . It defaults to 10.
      Using ``auto`` recognizes most strings, even some that aren't supported when you use a
      time format string.

      If your date and time values use formats different from each other, set this parameter to
      ``auto`` .

    - **TrimBlanks** *(boolean) --*

      A value that specifies to remove the trailing white space characters from a VARCHAR
      string. This parameter applies only to columns with a VARCHAR data type. Choose ``true``
      to remove unneeded white space. The default is ``false`` .

    - **TruncateColumns** *(boolean) --*

      A value that specifies to truncate data in columns to the appropriate number of
      characters, so that the data fits in the column. This parameter applies only to columns
      with a VARCHAR or CHAR data type, and rows with a size of 4 MB or less. Choose ``true``
      to truncate data. The default is ``false`` .

    - **Username** *(string) --*

      An Amazon Redshift user name for a registered user.

    - **WriteBufferSize** *(integer) --*

      The size of the write buffer to use in rows. Valid values range from 1 through 2,048. The
      default is 1,024. Use this setting to tune performance.
    """


_ClientDeleteEndpointResponseEndpointS3SettingsTypeDef = TypedDict(
    "_ClientDeleteEndpointResponseEndpointS3SettingsTypeDef",
    {
        "ServiceAccessRoleArn": str,
        "ExternalTableDefinition": str,
        "CsvRowDelimiter": str,
        "CsvDelimiter": str,
        "BucketFolder": str,
        "BucketName": str,
        "CompressionType": str,
        "EncryptionMode": str,
        "ServerSideEncryptionKmsKeyId": str,
        "DataFormat": str,
        "EncodingType": str,
        "DictPageSizeLimit": int,
        "RowGroupLength": int,
        "DataPageSize": int,
        "ParquetVersion": str,
        "EnableStatistics": bool,
        "IncludeOpForFullLoad": bool,
        "CdcInsertsOnly": bool,
        "TimestampColumnName": str,
        "ParquetTimestampInMillisecond": bool,
    },
    total=False,
)


class ClientDeleteEndpointResponseEndpointS3SettingsTypeDef(
    _ClientDeleteEndpointResponseEndpointS3SettingsTypeDef
):
    """
    Type definition for `ClientDeleteEndpointResponseEndpoint` `S3Settings`

    The settings for the S3 target endpoint. For more information, see the ``S3Settings``
    structure.

    - **ServiceAccessRoleArn** *(string) --*

      The Amazon Resource Name (ARN) used by the service access IAM role.

    - **ExternalTableDefinition** *(string) --*

      The external table definition.

    - **CsvRowDelimiter** *(string) --*

      The delimiter used to separate rows in the source files. The default is a carriage return
      (``\\n`` ).

    - **CsvDelimiter** *(string) --*

      The delimiter used to separate columns in the source files. The default is a comma.

    - **BucketFolder** *(string) --*

      An optional parameter to set a folder name in the S3 bucket. If provided, tables are
      created in the path `` *bucketFolder* /*schema_name* /*table_name* /`` . If this
      parameter is not specified, then the path used is `` *schema_name* /*table_name* /`` .

    - **BucketName** *(string) --*

      The name of the S3 bucket.

    - **CompressionType** *(string) --*

      An optional parameter to use GZIP to compress the target files. Set to GZIP to compress
      the target files. Set to NONE (the default) or do not use to leave the files
      uncompressed. Applies to both .csv and .parquet file formats.

    - **EncryptionMode** *(string) --*

      The type of server-side encryption that you want to use for your data. This encryption
      type is part of the endpoint settings or the extra connections attributes for Amazon S3.
      You can choose either ``SSE_S3`` (the default) or ``SSE_KMS`` . To use ``SSE_S3`` , you
      need an AWS Identity and Access Management (IAM) role with permission to allow
      ``"arn:aws:s3:::dms-*"`` to use the following actions:

      * ``s3:CreateBucket``

      * ``s3:ListBucket``

      * ``s3:DeleteBucket``

      * ``s3:GetBucketLocation``

      * ``s3:GetObject``

      * ``s3:PutObject``

      * ``s3:DeleteObject``

      * ``s3:GetObjectVersion``

      * ``s3:GetBucketPolicy``

      * ``s3:PutBucketPolicy``

      * ``s3:DeleteBucketPolicy``

    - **ServerSideEncryptionKmsKeyId** *(string) --*

      If you are using ``SSE_KMS`` for the ``EncryptionMode`` , provide the AWS KMS key ID. The
      key that you use needs an attached policy that enables AWS Identity and Access Management
      (IAM) user permissions and allows use of the key.

      Here is a CLI example: ``aws dms create-endpoint --endpoint-identifier *value*
      --endpoint-type target --engine-name s3 --s3-settings ServiceAccessRoleArn=*value*
      ,BucketFolder=*value* ,BucketName=*value*
      ,EncryptionMode=SSE_KMS,ServerSideEncryptionKmsKeyId=*value* ``

    - **DataFormat** *(string) --*

      The format of the data that you want to use for output. You can choose one of the
      following:

      * ``csv`` : This is a row-based file format with comma-separated values (.csv).

      * ``parquet`` : Apache Parquet (.parquet) is a columnar storage file format that features
      efficient compression and provides faster query response.

    - **EncodingType** *(string) --*

      The type of encoding you are using:

      * ``RLE_DICTIONARY`` uses a combination of bit-packing and run-length encoding to store
      repeated values more efficiently. This is the default.

      * ``PLAIN`` doesn't use encoding at all. Values are stored as they are.

      * ``PLAIN_DICTIONARY`` builds a dictionary of the values encountered in a given column.
      The dictionary is stored in a dictionary page for each column chunk.

    - **DictPageSizeLimit** *(integer) --*

      The maximum size of an encoded dictionary page of a column. If the dictionary page
      exceeds this, this column is stored using an encoding type of ``PLAIN`` . This parameter
      defaults to 1024 * 1024 bytes (1 MiB), the maximum size of a dictionary page before it
      reverts to ``PLAIN`` encoding. This size is used for .parquet file format only.

    - **RowGroupLength** *(integer) --*

      The number of rows in a row group. A smaller row group size provides faster reads. But as
      the number of row groups grows, the slower writes become. This parameter defaults to
      10,000 rows. This number is used for .parquet file format only.

      If you choose a value larger than the maximum, ``RowGroupLength`` is set to the max row
      group length in bytes (64 * 1024 * 1024).

    - **DataPageSize** *(integer) --*

      The size of one data page in bytes. This parameter defaults to 1024 * 1024 bytes (1 MiB).
      This number is used for .parquet file format only.

    - **ParquetVersion** *(string) --*

      The version of the Apache Parquet format that you want to use: ``parquet_1_0`` (the
      default) or ``parquet_2_0`` .

    - **EnableStatistics** *(boolean) --*

      A value that enables statistics for Parquet pages and row groups. Choose ``true`` to
      enable statistics, ``false`` to disable. Statistics include ``NULL`` , ``DISTINCT`` ,
      ``MAX`` , and ``MIN`` values. This parameter defaults to ``true`` . This value is used
      for .parquet file format only.

    - **IncludeOpForFullLoad** *(boolean) --*

      A value that enables a full load to write INSERT operations to the comma-separated value
      (.csv) output files only to indicate how the rows were added to the source database.

      .. note::

        AWS DMS supports the ``IncludeOpForFullLoad`` parameter in versions 3.1.4 and later.

      For full load, records can only be inserted. By default (the ``false`` setting), no
      information is recorded in these output files for a full load to indicate that the rows
      were inserted at the source database. If ``IncludeOpForFullLoad`` is set to ``true`` or
      ``y`` , the INSERT is recorded as an I annotation in the first field of the .csv file.
      This allows the format of your target records from a full load to be consistent with the
      target records from a CDC load.

      .. note::

        This setting works together with the ``CdcInsertsOnly`` parameter for output to .csv
        files only. For more information about how these settings work together, see
        `Indicating Source DB Operations in Migrated S3 Data
        <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring.InsertOps>`__
        in the *AWS Database Migration Service User Guide.* .

    - **CdcInsertsOnly** *(boolean) --*

      A value that enables a change data capture (CDC) load to write only INSERT operations to
      .csv or columnar storage (.parquet) output files. By default (the ``false`` setting), the
      first field in a .csv or .parquet record contains the letter I (INSERT), U (UPDATE), or D
      (DELETE). These values indicate whether the row was inserted, updated, or deleted at the
      source database for a CDC load to the target.

      If ``CdcInsertsOnly`` is set to ``true`` or ``y`` , only INSERTs from the source database
      are migrated to the .csv or .parquet file. For .csv format only, how these INSERTs are
      recorded depends on the value of ``IncludeOpForFullLoad`` . If ``IncludeOpForFullLoad``
      is set to ``true`` , the first field of every CDC record is set to I to indicate the
      INSERT operation at the source. If ``IncludeOpForFullLoad`` is set to ``false`` , every
      CDC record is written without a first field to indicate the INSERT operation at the
      source. For more information about how these settings work together, see `Indicating
      Source DB Operations in Migrated S3 Data
      <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring.InsertOps>`__
      in the *AWS Database Migration Service User Guide.* .

      .. note::

        AWS DMS supports this interaction between the ``CdcInsertsOnly`` and
        ``IncludeOpForFullLoad`` parameters in versions 3.1.4 and later.

    - **TimestampColumnName** *(string) --*

      A value that when nonblank causes AWS DMS to add a column with timestamp information to
      the endpoint data for an Amazon S3 target.

      .. note::

        AWS DMS supports the ``TimestampColumnName`` parameter in versions 3.1.4 and later.

      DMS includes an additional ``STRING`` column in the .csv or .parquet object files of your
      migrated data when you set ``TimestampColumnName`` to a nonblank value.

      For a full load, each row of this timestamp column contains a timestamp for when the data
      was transferred from the source to the target by DMS.

      For a change data capture (CDC) load, each row of the timestamp column contains the
      timestamp for the commit of that row in the source database.

      The string format for this timestamp column value is ``yyyy-MM-dd HH:mm:ss.SSSSSS`` . By
      default, the precision of this value is in microseconds. For a CDC load, the rounding of
      the precision depends on the commit timestamp supported by DMS for the source database.

      When the ``AddColumnName`` parameter is set to ``true`` , DMS also includes a name for
      the timestamp column that you set with ``TimestampColumnName`` .

    - **ParquetTimestampInMillisecond** *(boolean) --*

      A value that specifies the precision of any ``TIMESTAMP`` column values that are written
      to an Amazon S3 object file in .parquet format.

      .. note::

        AWS DMS supports the ``ParquetTimestampInMillisecond`` parameter in versions 3.1.4 and
        later.

      When ``ParquetTimestampInMillisecond`` is set to ``true`` or ``y`` , AWS DMS writes all
      ``TIMESTAMP`` columns in a .parquet formatted file with millisecond precision. Otherwise,
      DMS writes them with microsecond precision.

      Currently, Amazon Athena and AWS Glue can handle only millisecond precision for
      ``TIMESTAMP`` values. Set this parameter to ``true`` for S3 endpoint object files that
      are .parquet formatted only if you plan to query or process the data with Athena or AWS
      Glue.

      .. note::

        AWS DMS writes any ``TIMESTAMP`` column values written to an S3 file in .csv format
        with microsecond precision.

        Setting ``ParquetTimestampInMillisecond`` has no effect on the string format of the
        timestamp column value that is inserted by setting the ``TimestampColumnName``
        parameter.
    """


_ClientDeleteEndpointResponseEndpointTypeDef = TypedDict(
    "_ClientDeleteEndpointResponseEndpointTypeDef",
    {
        "EndpointIdentifier": str,
        "EndpointType": str,
        "EngineName": str,
        "EngineDisplayName": str,
        "Username": str,
        "ServerName": str,
        "Port": int,
        "DatabaseName": str,
        "ExtraConnectionAttributes": str,
        "Status": str,
        "KmsKeyId": str,
        "EndpointArn": str,
        "CertificateArn": str,
        "SslMode": str,
        "ServiceAccessRoleArn": str,
        "ExternalTableDefinition": str,
        "ExternalId": str,
        "DynamoDbSettings": ClientDeleteEndpointResponseEndpointDynamoDbSettingsTypeDef,
        "S3Settings": ClientDeleteEndpointResponseEndpointS3SettingsTypeDef,
        "DmsTransferSettings": ClientDeleteEndpointResponseEndpointDmsTransferSettingsTypeDef,
        "MongoDbSettings": ClientDeleteEndpointResponseEndpointMongoDbSettingsTypeDef,
        "KinesisSettings": ClientDeleteEndpointResponseEndpointKinesisSettingsTypeDef,
        "ElasticsearchSettings": ClientDeleteEndpointResponseEndpointElasticsearchSettingsTypeDef,
        "RedshiftSettings": ClientDeleteEndpointResponseEndpointRedshiftSettingsTypeDef,
    },
    total=False,
)


class ClientDeleteEndpointResponseEndpointTypeDef(
    _ClientDeleteEndpointResponseEndpointTypeDef
):
    """
    Type definition for `ClientDeleteEndpointResponse` `Endpoint`

    The endpoint that was deleted.

    - **EndpointIdentifier** *(string) --*

      The database endpoint identifier. Identifiers must begin with a letter; must contain only
      ASCII letters, digits, and hyphens; and must not end with a hyphen or contain two
      consecutive hyphens.

    - **EndpointType** *(string) --*

      The type of endpoint. Valid values are ``source`` and ``target`` .

    - **EngineName** *(string) --*

      The database engine name. Valid values, depending on the EndpointType, include mysql,
      oracle, postgres, mariadb, aurora, aurora-postgresql, redshift, s3, db2, azuredb, sybase,
      dynamodb, mongodb, and sqlserver.

    - **EngineDisplayName** *(string) --*

      The expanded name for the engine name. For example, if the ``EngineName`` parameter is
      "aurora," this value would be "Amazon Aurora MySQL."

    - **Username** *(string) --*

      The user name used to connect to the endpoint.

    - **ServerName** *(string) --*

      The name of the server at the endpoint.

    - **Port** *(integer) --*

      The port value used to access the endpoint.

    - **DatabaseName** *(string) --*

      The name of the database at the endpoint.

    - **ExtraConnectionAttributes** *(string) --*

      Additional connection attributes used to connect to the endpoint.

    - **Status** *(string) --*

      The status of the endpoint.

    - **KmsKeyId** *(string) --*

      An AWS KMS key identifier that is used to encrypt the connection parameters for the
      endpoint.

      If you don't specify a value for the ``KmsKeyId`` parameter, then AWS DMS uses your default
      encryption key.

      AWS KMS creates the default encryption key for your AWS account. Your AWS account has a
      different default encryption key for each AWS Region.

    - **EndpointArn** *(string) --*

      The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

    - **CertificateArn** *(string) --*

      The Amazon Resource Name (ARN) used for SSL connection to the endpoint.

    - **SslMode** *(string) --*

      The SSL mode used to connect to the endpoint. The default value is ``none`` .

    - **ServiceAccessRoleArn** *(string) --*

      The Amazon Resource Name (ARN) used by the service access IAM role.

    - **ExternalTableDefinition** *(string) --*

      The external table definition.

    - **ExternalId** *(string) --*

      Value returned by a call to CreateEndpoint that can be used for cross-account validation.
      Use it on a subsequent call to CreateEndpoint to create the endpoint with a cross-account.

    - **DynamoDbSettings** *(dict) --*

      The settings for the target DynamoDB database. For more information, see the
      ``DynamoDBSettings`` structure.

      - **ServiceAccessRoleArn** *(string) --*

        The Amazon Resource Name (ARN) used by the service access IAM role.

    - **S3Settings** *(dict) --*

      The settings for the S3 target endpoint. For more information, see the ``S3Settings``
      structure.

      - **ServiceAccessRoleArn** *(string) --*

        The Amazon Resource Name (ARN) used by the service access IAM role.

      - **ExternalTableDefinition** *(string) --*

        The external table definition.

      - **CsvRowDelimiter** *(string) --*

        The delimiter used to separate rows in the source files. The default is a carriage return
        (``\\n`` ).

      - **CsvDelimiter** *(string) --*

        The delimiter used to separate columns in the source files. The default is a comma.

      - **BucketFolder** *(string) --*

        An optional parameter to set a folder name in the S3 bucket. If provided, tables are
        created in the path `` *bucketFolder* /*schema_name* /*table_name* /`` . If this
        parameter is not specified, then the path used is `` *schema_name* /*table_name* /`` .

      - **BucketName** *(string) --*

        The name of the S3 bucket.

      - **CompressionType** *(string) --*

        An optional parameter to use GZIP to compress the target files. Set to GZIP to compress
        the target files. Set to NONE (the default) or do not use to leave the files
        uncompressed. Applies to both .csv and .parquet file formats.

      - **EncryptionMode** *(string) --*

        The type of server-side encryption that you want to use for your data. This encryption
        type is part of the endpoint settings or the extra connections attributes for Amazon S3.
        You can choose either ``SSE_S3`` (the default) or ``SSE_KMS`` . To use ``SSE_S3`` , you
        need an AWS Identity and Access Management (IAM) role with permission to allow
        ``"arn:aws:s3:::dms-*"`` to use the following actions:

        * ``s3:CreateBucket``

        * ``s3:ListBucket``

        * ``s3:DeleteBucket``

        * ``s3:GetBucketLocation``

        * ``s3:GetObject``

        * ``s3:PutObject``

        * ``s3:DeleteObject``

        * ``s3:GetObjectVersion``

        * ``s3:GetBucketPolicy``

        * ``s3:PutBucketPolicy``

        * ``s3:DeleteBucketPolicy``

      - **ServerSideEncryptionKmsKeyId** *(string) --*

        If you are using ``SSE_KMS`` for the ``EncryptionMode`` , provide the AWS KMS key ID. The
        key that you use needs an attached policy that enables AWS Identity and Access Management
        (IAM) user permissions and allows use of the key.

        Here is a CLI example: ``aws dms create-endpoint --endpoint-identifier *value*
        --endpoint-type target --engine-name s3 --s3-settings ServiceAccessRoleArn=*value*
        ,BucketFolder=*value* ,BucketName=*value*
        ,EncryptionMode=SSE_KMS,ServerSideEncryptionKmsKeyId=*value* ``

      - **DataFormat** *(string) --*

        The format of the data that you want to use for output. You can choose one of the
        following:

        * ``csv`` : This is a row-based file format with comma-separated values (.csv).

        * ``parquet`` : Apache Parquet (.parquet) is a columnar storage file format that features
        efficient compression and provides faster query response.

      - **EncodingType** *(string) --*

        The type of encoding you are using:

        * ``RLE_DICTIONARY`` uses a combination of bit-packing and run-length encoding to store
        repeated values more efficiently. This is the default.

        * ``PLAIN`` doesn't use encoding at all. Values are stored as they are.

        * ``PLAIN_DICTIONARY`` builds a dictionary of the values encountered in a given column.
        The dictionary is stored in a dictionary page for each column chunk.

      - **DictPageSizeLimit** *(integer) --*

        The maximum size of an encoded dictionary page of a column. If the dictionary page
        exceeds this, this column is stored using an encoding type of ``PLAIN`` . This parameter
        defaults to 1024 * 1024 bytes (1 MiB), the maximum size of a dictionary page before it
        reverts to ``PLAIN`` encoding. This size is used for .parquet file format only.

      - **RowGroupLength** *(integer) --*

        The number of rows in a row group. A smaller row group size provides faster reads. But as
        the number of row groups grows, the slower writes become. This parameter defaults to
        10,000 rows. This number is used for .parquet file format only.

        If you choose a value larger than the maximum, ``RowGroupLength`` is set to the max row
        group length in bytes (64 * 1024 * 1024).

      - **DataPageSize** *(integer) --*

        The size of one data page in bytes. This parameter defaults to 1024 * 1024 bytes (1 MiB).
        This number is used for .parquet file format only.

      - **ParquetVersion** *(string) --*

        The version of the Apache Parquet format that you want to use: ``parquet_1_0`` (the
        default) or ``parquet_2_0`` .

      - **EnableStatistics** *(boolean) --*

        A value that enables statistics for Parquet pages and row groups. Choose ``true`` to
        enable statistics, ``false`` to disable. Statistics include ``NULL`` , ``DISTINCT`` ,
        ``MAX`` , and ``MIN`` values. This parameter defaults to ``true`` . This value is used
        for .parquet file format only.

      - **IncludeOpForFullLoad** *(boolean) --*

        A value that enables a full load to write INSERT operations to the comma-separated value
        (.csv) output files only to indicate how the rows were added to the source database.

        .. note::

          AWS DMS supports the ``IncludeOpForFullLoad`` parameter in versions 3.1.4 and later.

        For full load, records can only be inserted. By default (the ``false`` setting), no
        information is recorded in these output files for a full load to indicate that the rows
        were inserted at the source database. If ``IncludeOpForFullLoad`` is set to ``true`` or
        ``y`` , the INSERT is recorded as an I annotation in the first field of the .csv file.
        This allows the format of your target records from a full load to be consistent with the
        target records from a CDC load.

        .. note::

          This setting works together with the ``CdcInsertsOnly`` parameter for output to .csv
          files only. For more information about how these settings work together, see
          `Indicating Source DB Operations in Migrated S3 Data
          <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring.InsertOps>`__
          in the *AWS Database Migration Service User Guide.* .

      - **CdcInsertsOnly** *(boolean) --*

        A value that enables a change data capture (CDC) load to write only INSERT operations to
        .csv or columnar storage (.parquet) output files. By default (the ``false`` setting), the
        first field in a .csv or .parquet record contains the letter I (INSERT), U (UPDATE), or D
        (DELETE). These values indicate whether the row was inserted, updated, or deleted at the
        source database for a CDC load to the target.

        If ``CdcInsertsOnly`` is set to ``true`` or ``y`` , only INSERTs from the source database
        are migrated to the .csv or .parquet file. For .csv format only, how these INSERTs are
        recorded depends on the value of ``IncludeOpForFullLoad`` . If ``IncludeOpForFullLoad``
        is set to ``true`` , the first field of every CDC record is set to I to indicate the
        INSERT operation at the source. If ``IncludeOpForFullLoad`` is set to ``false`` , every
        CDC record is written without a first field to indicate the INSERT operation at the
        source. For more information about how these settings work together, see `Indicating
        Source DB Operations in Migrated S3 Data
        <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring.InsertOps>`__
        in the *AWS Database Migration Service User Guide.* .

        .. note::

          AWS DMS supports this interaction between the ``CdcInsertsOnly`` and
          ``IncludeOpForFullLoad`` parameters in versions 3.1.4 and later.

      - **TimestampColumnName** *(string) --*

        A value that when nonblank causes AWS DMS to add a column with timestamp information to
        the endpoint data for an Amazon S3 target.

        .. note::

          AWS DMS supports the ``TimestampColumnName`` parameter in versions 3.1.4 and later.

        DMS includes an additional ``STRING`` column in the .csv or .parquet object files of your
        migrated data when you set ``TimestampColumnName`` to a nonblank value.

        For a full load, each row of this timestamp column contains a timestamp for when the data
        was transferred from the source to the target by DMS.

        For a change data capture (CDC) load, each row of the timestamp column contains the
        timestamp for the commit of that row in the source database.

        The string format for this timestamp column value is ``yyyy-MM-dd HH:mm:ss.SSSSSS`` . By
        default, the precision of this value is in microseconds. For a CDC load, the rounding of
        the precision depends on the commit timestamp supported by DMS for the source database.

        When the ``AddColumnName`` parameter is set to ``true`` , DMS also includes a name for
        the timestamp column that you set with ``TimestampColumnName`` .

      - **ParquetTimestampInMillisecond** *(boolean) --*

        A value that specifies the precision of any ``TIMESTAMP`` column values that are written
        to an Amazon S3 object file in .parquet format.

        .. note::

          AWS DMS supports the ``ParquetTimestampInMillisecond`` parameter in versions 3.1.4 and
          later.

        When ``ParquetTimestampInMillisecond`` is set to ``true`` or ``y`` , AWS DMS writes all
        ``TIMESTAMP`` columns in a .parquet formatted file with millisecond precision. Otherwise,
        DMS writes them with microsecond precision.

        Currently, Amazon Athena and AWS Glue can handle only millisecond precision for
        ``TIMESTAMP`` values. Set this parameter to ``true`` for S3 endpoint object files that
        are .parquet formatted only if you plan to query or process the data with Athena or AWS
        Glue.

        .. note::

          AWS DMS writes any ``TIMESTAMP`` column values written to an S3 file in .csv format
          with microsecond precision.

          Setting ``ParquetTimestampInMillisecond`` has no effect on the string format of the
          timestamp column value that is inserted by setting the ``TimestampColumnName``
          parameter.

    - **DmsTransferSettings** *(dict) --*

      The settings in JSON format for the DMS transfer type of source endpoint.

      Possible settings include the following:

      * ``ServiceAccessRoleArn`` - The IAM role that has permission to access the Amazon S3
      bucket.

      * ``BucketName`` - The name of the S3 bucket to use.

      * ``CompressionType`` - An optional parameter to use GZIP to compress the target files. To
      use GZIP, set this value to ``NONE`` (the default). To keep the files uncompressed, don't
      use this value.

      Shorthand syntax for these settings is as follows:
      ``ServiceAccessRoleArn=string,BucketName=string,CompressionType=string``

      JSON syntax for these settings is as follows: ``{ "ServiceAccessRoleArn": "string",
      "BucketName": "string", "CompressionType": "none"|"gzip" }``

      - **ServiceAccessRoleArn** *(string) --*

        The IAM role that has permission to access the Amazon S3 bucket.

      - **BucketName** *(string) --*

        The name of the S3 bucket to use.

    - **MongoDbSettings** *(dict) --*

      The settings for the MongoDB source endpoint. For more information, see the
      ``MongoDbSettings`` structure.

      - **Username** *(string) --*

        The user name you use to access the MongoDB source endpoint.

      - **Password** *(string) --*

        The password for the user account you use to access the MongoDB source endpoint.

      - **ServerName** *(string) --*

        The name of the server on the MongoDB source endpoint.

      - **Port** *(integer) --*

        The port value for the MongoDB source endpoint.

      - **DatabaseName** *(string) --*

        The database name on the MongoDB source endpoint.

      - **AuthType** *(string) --*

        The authentication type you use to access the MongoDB source endpoint.

        Valid values: NO, PASSWORD

        When NO is selected, user name and password parameters are not used and can be empty.

      - **AuthMechanism** *(string) --*

        The authentication mechanism you use to access the MongoDB source endpoint.

        Valid values: DEFAULT, MONGODB_CR, SCRAM_SHA_1

        DEFAULT – For MongoDB version 2.x, use MONGODB_CR. For MongoDB version 3.x, use
        SCRAM_SHA_1. This setting is not used when authType=No.

      - **NestingLevel** *(string) --*

        Specifies either document or table mode.

        Valid values: NONE, ONE

        Default value is NONE. Specify NONE to use document mode. Specify ONE to use table mode.

      - **ExtractDocId** *(string) --*

        Specifies the document ID. Use this setting when ``NestingLevel`` is set to NONE.

        Default value is false.

      - **DocsToInvestigate** *(string) --*

        Indicates the number of documents to preview to determine the document organization. Use
        this setting when ``NestingLevel`` is set to ONE.

        Must be a positive value greater than 0. Default value is 1000.

      - **AuthSource** *(string) --*

        The MongoDB database name. This setting is not used when ``authType=NO`` .

        The default is admin.

      - **KmsKeyId** *(string) --*

        The AWS KMS key identifier that is used to encrypt the content on the replication
        instance. If you don't specify a value for the ``KmsKeyId`` parameter, then AWS DMS uses
        your default encryption key. AWS KMS creates the default encryption key for your AWS
        account. Your AWS account has a different default encryption key for each AWS Region.

    - **KinesisSettings** *(dict) --*

      The settings for the Amazon Kinesis source endpoint. For more information, see the
      ``KinesisSettings`` structure.

      - **StreamArn** *(string) --*

        The Amazon Resource Name (ARN) for the Amazon Kinesis Data Streams endpoint.

      - **MessageFormat** *(string) --*

        The output format for the records created on the endpoint. The message format is ``JSON``
        .

      - **ServiceAccessRoleArn** *(string) --*

        The Amazon Resource Name (ARN) for the IAM role that DMS uses to write to the Amazon
        Kinesis data stream.

    - **ElasticsearchSettings** *(dict) --*

      The settings for the Elasticsearch source endpoint. For more information, see the
      ``ElasticsearchSettings`` structure.

      - **ServiceAccessRoleArn** *(string) --*

        The Amazon Resource Name (ARN) used by service to access the IAM role.

      - **EndpointUri** *(string) --*

        The endpoint for the Elasticsearch cluster.

      - **FullLoadErrorPercentage** *(integer) --*

        The maximum percentage of records that can fail to be written before a full load
        operation stops.

      - **ErrorRetryDuration** *(integer) --*

        The maximum number of seconds that DMS retries failed API requests to the Elasticsearch
        cluster.

    - **RedshiftSettings** *(dict) --*

      Settings for the Amazon Redshift endpoint.

      - **AcceptAnyDate** *(boolean) --*

        A value that indicates to allow any date format, including invalid formats such as
        00/00/00 00:00:00, to be loaded without generating an error. You can choose ``true`` or
        ``false`` (the default).

        This parameter applies only to TIMESTAMP and DATE columns. Always use ACCEPTANYDATE with
        the DATEFORMAT parameter. If the date format for the data doesn't match the DATEFORMAT
        specification, Amazon Redshift inserts a NULL value into that field.

      - **AfterConnectScript** *(string) --*

        Code to run after connecting. This parameter should contain the code itself, not the name
        of a file containing the code.

      - **BucketFolder** *(string) --*

        The location where the comma-separated value (.csv) files are stored before being
        uploaded to the S3 bucket.

      - **BucketName** *(string) --*

        The name of the S3 bucket you want to use

      - **ConnectionTimeout** *(integer) --*

        A value that sets the amount of time to wait (in milliseconds) before timing out,
        beginning from when you initially establish a connection.

      - **DatabaseName** *(string) --*

        The name of the Amazon Redshift data warehouse (service) that you are working with.

      - **DateFormat** *(string) --*

        The date format that you are using. Valid values are ``auto`` (case-sensitive), your date
        format string enclosed in quotes, or NULL. If this parameter is left unset (NULL), it
        defaults to a format of 'YYYY-MM-DD'. Using ``auto`` recognizes most strings, even some
        that aren't supported when you use a date format string.

        If your date and time values use formats different from each other, set this to ``auto`` .

      - **EmptyAsNull** *(boolean) --*

        A value that specifies whether AWS DMS should migrate empty CHAR and VARCHAR fields as
        NULL. A value of ``true`` sets empty CHAR and VARCHAR fields to null. The default is
        ``false`` .

      - **EncryptionMode** *(string) --*

        The type of server-side encryption that you want to use for your data. This encryption
        type is part of the endpoint settings or the extra connections attributes for Amazon S3.
        You can choose either ``SSE_S3`` (the default) or ``SSE_KMS`` . To use ``SSE_S3`` ,
        create an AWS Identity and Access Management (IAM) role with a policy that allows
        ``"arn:aws:s3:::*"`` to use the following actions: ``"s3:PutObject", "s3:ListBucket"``

      - **FileTransferUploadStreams** *(integer) --*

        The number of threads used to upload a single file. This parameter accepts a value from 1
        through 64. It defaults to 10.

      - **LoadTimeout** *(integer) --*

        The amount of time to wait (in milliseconds) before timing out, beginning from when you
        begin loading.

      - **MaxFileSize** *(integer) --*

        The maximum size (in KB) of any .csv file used to transfer data to Amazon Redshift. This
        accepts a value from 1 through 1,048,576. It defaults to 32,768 KB (32 MB).

      - **Password** *(string) --*

        The password for the user named in the ``username`` property.

      - **Port** *(integer) --*

        The port number for Amazon Redshift. The default value is 5439.

      - **RemoveQuotes** *(boolean) --*

        A value that specifies to remove surrounding quotation marks from strings in the incoming
        data. All characters within the quotation marks, including delimiters, are retained.
        Choose ``true`` to remove quotation marks. The default is ``false`` .

      - **ReplaceInvalidChars** *(string) --*

        A list of characters that you want to replace. Use with ``ReplaceChars`` .

      - **ReplaceChars** *(string) --*

        A value that specifies to replaces the invalid characters specified in
        ``ReplaceInvalidChars`` , substituting the specified characters instead. The default is
        ``"?"`` .

      - **ServerName** *(string) --*

        The name of the Amazon Redshift cluster you are using.

      - **ServiceAccessRoleArn** *(string) --*

        The Amazon Resource Name (ARN) of the IAM role that has access to the Amazon Redshift
        service.

      - **ServerSideEncryptionKmsKeyId** *(string) --*

        The AWS KMS key ID. If you are using ``SSE_KMS`` for the ``EncryptionMode`` , provide
        this key ID. The key that you use needs an attached policy that enables IAM user
        permissions and allows use of the key.

      - **TimeFormat** *(string) --*

        The time format that you want to use. Valid values are ``auto`` (case-sensitive),
        ``'timeformat_string'`` , ``'epochsecs'`` , or ``'epochmillisecs'`` . It defaults to 10.
        Using ``auto`` recognizes most strings, even some that aren't supported when you use a
        time format string.

        If your date and time values use formats different from each other, set this parameter to
        ``auto`` .

      - **TrimBlanks** *(boolean) --*

        A value that specifies to remove the trailing white space characters from a VARCHAR
        string. This parameter applies only to columns with a VARCHAR data type. Choose ``true``
        to remove unneeded white space. The default is ``false`` .

      - **TruncateColumns** *(boolean) --*

        A value that specifies to truncate data in columns to the appropriate number of
        characters, so that the data fits in the column. This parameter applies only to columns
        with a VARCHAR or CHAR data type, and rows with a size of 4 MB or less. Choose ``true``
        to truncate data. The default is ``false`` .

      - **Username** *(string) --*

        An Amazon Redshift user name for a registered user.

      - **WriteBufferSize** *(integer) --*

        The size of the write buffer to use in rows. Valid values range from 1 through 2,048. The
        default is 1,024. Use this setting to tune performance.
    """


_ClientDeleteEndpointResponseTypeDef = TypedDict(
    "_ClientDeleteEndpointResponseTypeDef",
    {"Endpoint": ClientDeleteEndpointResponseEndpointTypeDef},
    total=False,
)


class ClientDeleteEndpointResponseTypeDef(_ClientDeleteEndpointResponseTypeDef):
    """
    Type definition for `ClientDeleteEndpoint` `Response`

    - **Endpoint** *(dict) --*

      The endpoint that was deleted.

      - **EndpointIdentifier** *(string) --*

        The database endpoint identifier. Identifiers must begin with a letter; must contain only
        ASCII letters, digits, and hyphens; and must not end with a hyphen or contain two
        consecutive hyphens.

      - **EndpointType** *(string) --*

        The type of endpoint. Valid values are ``source`` and ``target`` .

      - **EngineName** *(string) --*

        The database engine name. Valid values, depending on the EndpointType, include mysql,
        oracle, postgres, mariadb, aurora, aurora-postgresql, redshift, s3, db2, azuredb, sybase,
        dynamodb, mongodb, and sqlserver.

      - **EngineDisplayName** *(string) --*

        The expanded name for the engine name. For example, if the ``EngineName`` parameter is
        "aurora," this value would be "Amazon Aurora MySQL."

      - **Username** *(string) --*

        The user name used to connect to the endpoint.

      - **ServerName** *(string) --*

        The name of the server at the endpoint.

      - **Port** *(integer) --*

        The port value used to access the endpoint.

      - **DatabaseName** *(string) --*

        The name of the database at the endpoint.

      - **ExtraConnectionAttributes** *(string) --*

        Additional connection attributes used to connect to the endpoint.

      - **Status** *(string) --*

        The status of the endpoint.

      - **KmsKeyId** *(string) --*

        An AWS KMS key identifier that is used to encrypt the connection parameters for the
        endpoint.

        If you don't specify a value for the ``KmsKeyId`` parameter, then AWS DMS uses your default
        encryption key.

        AWS KMS creates the default encryption key for your AWS account. Your AWS account has a
        different default encryption key for each AWS Region.

      - **EndpointArn** *(string) --*

        The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

      - **CertificateArn** *(string) --*

        The Amazon Resource Name (ARN) used for SSL connection to the endpoint.

      - **SslMode** *(string) --*

        The SSL mode used to connect to the endpoint. The default value is ``none`` .

      - **ServiceAccessRoleArn** *(string) --*

        The Amazon Resource Name (ARN) used by the service access IAM role.

      - **ExternalTableDefinition** *(string) --*

        The external table definition.

      - **ExternalId** *(string) --*

        Value returned by a call to CreateEndpoint that can be used for cross-account validation.
        Use it on a subsequent call to CreateEndpoint to create the endpoint with a cross-account.

      - **DynamoDbSettings** *(dict) --*

        The settings for the target DynamoDB database. For more information, see the
        ``DynamoDBSettings`` structure.

        - **ServiceAccessRoleArn** *(string) --*

          The Amazon Resource Name (ARN) used by the service access IAM role.

      - **S3Settings** *(dict) --*

        The settings for the S3 target endpoint. For more information, see the ``S3Settings``
        structure.

        - **ServiceAccessRoleArn** *(string) --*

          The Amazon Resource Name (ARN) used by the service access IAM role.

        - **ExternalTableDefinition** *(string) --*

          The external table definition.

        - **CsvRowDelimiter** *(string) --*

          The delimiter used to separate rows in the source files. The default is a carriage return
          (``\\n`` ).

        - **CsvDelimiter** *(string) --*

          The delimiter used to separate columns in the source files. The default is a comma.

        - **BucketFolder** *(string) --*

          An optional parameter to set a folder name in the S3 bucket. If provided, tables are
          created in the path `` *bucketFolder* /*schema_name* /*table_name* /`` . If this
          parameter is not specified, then the path used is `` *schema_name* /*table_name* /`` .

        - **BucketName** *(string) --*

          The name of the S3 bucket.

        - **CompressionType** *(string) --*

          An optional parameter to use GZIP to compress the target files. Set to GZIP to compress
          the target files. Set to NONE (the default) or do not use to leave the files
          uncompressed. Applies to both .csv and .parquet file formats.

        - **EncryptionMode** *(string) --*

          The type of server-side encryption that you want to use for your data. This encryption
          type is part of the endpoint settings or the extra connections attributes for Amazon S3.
          You can choose either ``SSE_S3`` (the default) or ``SSE_KMS`` . To use ``SSE_S3`` , you
          need an AWS Identity and Access Management (IAM) role with permission to allow
          ``"arn:aws:s3:::dms-*"`` to use the following actions:

          * ``s3:CreateBucket``

          * ``s3:ListBucket``

          * ``s3:DeleteBucket``

          * ``s3:GetBucketLocation``

          * ``s3:GetObject``

          * ``s3:PutObject``

          * ``s3:DeleteObject``

          * ``s3:GetObjectVersion``

          * ``s3:GetBucketPolicy``

          * ``s3:PutBucketPolicy``

          * ``s3:DeleteBucketPolicy``

        - **ServerSideEncryptionKmsKeyId** *(string) --*

          If you are using ``SSE_KMS`` for the ``EncryptionMode`` , provide the AWS KMS key ID. The
          key that you use needs an attached policy that enables AWS Identity and Access Management
          (IAM) user permissions and allows use of the key.

          Here is a CLI example: ``aws dms create-endpoint --endpoint-identifier *value*
          --endpoint-type target --engine-name s3 --s3-settings ServiceAccessRoleArn=*value*
          ,BucketFolder=*value* ,BucketName=*value*
          ,EncryptionMode=SSE_KMS,ServerSideEncryptionKmsKeyId=*value* ``

        - **DataFormat** *(string) --*

          The format of the data that you want to use for output. You can choose one of the
          following:

          * ``csv`` : This is a row-based file format with comma-separated values (.csv).

          * ``parquet`` : Apache Parquet (.parquet) is a columnar storage file format that features
          efficient compression and provides faster query response.

        - **EncodingType** *(string) --*

          The type of encoding you are using:

          * ``RLE_DICTIONARY`` uses a combination of bit-packing and run-length encoding to store
          repeated values more efficiently. This is the default.

          * ``PLAIN`` doesn't use encoding at all. Values are stored as they are.

          * ``PLAIN_DICTIONARY`` builds a dictionary of the values encountered in a given column.
          The dictionary is stored in a dictionary page for each column chunk.

        - **DictPageSizeLimit** *(integer) --*

          The maximum size of an encoded dictionary page of a column. If the dictionary page
          exceeds this, this column is stored using an encoding type of ``PLAIN`` . This parameter
          defaults to 1024 * 1024 bytes (1 MiB), the maximum size of a dictionary page before it
          reverts to ``PLAIN`` encoding. This size is used for .parquet file format only.

        - **RowGroupLength** *(integer) --*

          The number of rows in a row group. A smaller row group size provides faster reads. But as
          the number of row groups grows, the slower writes become. This parameter defaults to
          10,000 rows. This number is used for .parquet file format only.

          If you choose a value larger than the maximum, ``RowGroupLength`` is set to the max row
          group length in bytes (64 * 1024 * 1024).

        - **DataPageSize** *(integer) --*

          The size of one data page in bytes. This parameter defaults to 1024 * 1024 bytes (1 MiB).
          This number is used for .parquet file format only.

        - **ParquetVersion** *(string) --*

          The version of the Apache Parquet format that you want to use: ``parquet_1_0`` (the
          default) or ``parquet_2_0`` .

        - **EnableStatistics** *(boolean) --*

          A value that enables statistics for Parquet pages and row groups. Choose ``true`` to
          enable statistics, ``false`` to disable. Statistics include ``NULL`` , ``DISTINCT`` ,
          ``MAX`` , and ``MIN`` values. This parameter defaults to ``true`` . This value is used
          for .parquet file format only.

        - **IncludeOpForFullLoad** *(boolean) --*

          A value that enables a full load to write INSERT operations to the comma-separated value
          (.csv) output files only to indicate how the rows were added to the source database.

          .. note::

            AWS DMS supports the ``IncludeOpForFullLoad`` parameter in versions 3.1.4 and later.

          For full load, records can only be inserted. By default (the ``false`` setting), no
          information is recorded in these output files for a full load to indicate that the rows
          were inserted at the source database. If ``IncludeOpForFullLoad`` is set to ``true`` or
          ``y`` , the INSERT is recorded as an I annotation in the first field of the .csv file.
          This allows the format of your target records from a full load to be consistent with the
          target records from a CDC load.

          .. note::

            This setting works together with the ``CdcInsertsOnly`` parameter for output to .csv
            files only. For more information about how these settings work together, see
            `Indicating Source DB Operations in Migrated S3 Data
            <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring.InsertOps>`__
            in the *AWS Database Migration Service User Guide.* .

        - **CdcInsertsOnly** *(boolean) --*

          A value that enables a change data capture (CDC) load to write only INSERT operations to
          .csv or columnar storage (.parquet) output files. By default (the ``false`` setting), the
          first field in a .csv or .parquet record contains the letter I (INSERT), U (UPDATE), or D
          (DELETE). These values indicate whether the row was inserted, updated, or deleted at the
          source database for a CDC load to the target.

          If ``CdcInsertsOnly`` is set to ``true`` or ``y`` , only INSERTs from the source database
          are migrated to the .csv or .parquet file. For .csv format only, how these INSERTs are
          recorded depends on the value of ``IncludeOpForFullLoad`` . If ``IncludeOpForFullLoad``
          is set to ``true`` , the first field of every CDC record is set to I to indicate the
          INSERT operation at the source. If ``IncludeOpForFullLoad`` is set to ``false`` , every
          CDC record is written without a first field to indicate the INSERT operation at the
          source. For more information about how these settings work together, see `Indicating
          Source DB Operations in Migrated S3 Data
          <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring.InsertOps>`__
          in the *AWS Database Migration Service User Guide.* .

          .. note::

            AWS DMS supports this interaction between the ``CdcInsertsOnly`` and
            ``IncludeOpForFullLoad`` parameters in versions 3.1.4 and later.

        - **TimestampColumnName** *(string) --*

          A value that when nonblank causes AWS DMS to add a column with timestamp information to
          the endpoint data for an Amazon S3 target.

          .. note::

            AWS DMS supports the ``TimestampColumnName`` parameter in versions 3.1.4 and later.

          DMS includes an additional ``STRING`` column in the .csv or .parquet object files of your
          migrated data when you set ``TimestampColumnName`` to a nonblank value.

          For a full load, each row of this timestamp column contains a timestamp for when the data
          was transferred from the source to the target by DMS.

          For a change data capture (CDC) load, each row of the timestamp column contains the
          timestamp for the commit of that row in the source database.

          The string format for this timestamp column value is ``yyyy-MM-dd HH:mm:ss.SSSSSS`` . By
          default, the precision of this value is in microseconds. For a CDC load, the rounding of
          the precision depends on the commit timestamp supported by DMS for the source database.

          When the ``AddColumnName`` parameter is set to ``true`` , DMS also includes a name for
          the timestamp column that you set with ``TimestampColumnName`` .

        - **ParquetTimestampInMillisecond** *(boolean) --*

          A value that specifies the precision of any ``TIMESTAMP`` column values that are written
          to an Amazon S3 object file in .parquet format.

          .. note::

            AWS DMS supports the ``ParquetTimestampInMillisecond`` parameter in versions 3.1.4 and
            later.

          When ``ParquetTimestampInMillisecond`` is set to ``true`` or ``y`` , AWS DMS writes all
          ``TIMESTAMP`` columns in a .parquet formatted file with millisecond precision. Otherwise,
          DMS writes them with microsecond precision.

          Currently, Amazon Athena and AWS Glue can handle only millisecond precision for
          ``TIMESTAMP`` values. Set this parameter to ``true`` for S3 endpoint object files that
          are .parquet formatted only if you plan to query or process the data with Athena or AWS
          Glue.

          .. note::

            AWS DMS writes any ``TIMESTAMP`` column values written to an S3 file in .csv format
            with microsecond precision.

            Setting ``ParquetTimestampInMillisecond`` has no effect on the string format of the
            timestamp column value that is inserted by setting the ``TimestampColumnName``
            parameter.

      - **DmsTransferSettings** *(dict) --*

        The settings in JSON format for the DMS transfer type of source endpoint.

        Possible settings include the following:

        * ``ServiceAccessRoleArn`` - The IAM role that has permission to access the Amazon S3
        bucket.

        * ``BucketName`` - The name of the S3 bucket to use.

        * ``CompressionType`` - An optional parameter to use GZIP to compress the target files. To
        use GZIP, set this value to ``NONE`` (the default). To keep the files uncompressed, don't
        use this value.

        Shorthand syntax for these settings is as follows:
        ``ServiceAccessRoleArn=string,BucketName=string,CompressionType=string``

        JSON syntax for these settings is as follows: ``{ "ServiceAccessRoleArn": "string",
        "BucketName": "string", "CompressionType": "none"|"gzip" }``

        - **ServiceAccessRoleArn** *(string) --*

          The IAM role that has permission to access the Amazon S3 bucket.

        - **BucketName** *(string) --*

          The name of the S3 bucket to use.

      - **MongoDbSettings** *(dict) --*

        The settings for the MongoDB source endpoint. For more information, see the
        ``MongoDbSettings`` structure.

        - **Username** *(string) --*

          The user name you use to access the MongoDB source endpoint.

        - **Password** *(string) --*

          The password for the user account you use to access the MongoDB source endpoint.

        - **ServerName** *(string) --*

          The name of the server on the MongoDB source endpoint.

        - **Port** *(integer) --*

          The port value for the MongoDB source endpoint.

        - **DatabaseName** *(string) --*

          The database name on the MongoDB source endpoint.

        - **AuthType** *(string) --*

          The authentication type you use to access the MongoDB source endpoint.

          Valid values: NO, PASSWORD

          When NO is selected, user name and password parameters are not used and can be empty.

        - **AuthMechanism** *(string) --*

          The authentication mechanism you use to access the MongoDB source endpoint.

          Valid values: DEFAULT, MONGODB_CR, SCRAM_SHA_1

          DEFAULT – For MongoDB version 2.x, use MONGODB_CR. For MongoDB version 3.x, use
          SCRAM_SHA_1. This setting is not used when authType=No.

        - **NestingLevel** *(string) --*

          Specifies either document or table mode.

          Valid values: NONE, ONE

          Default value is NONE. Specify NONE to use document mode. Specify ONE to use table mode.

        - **ExtractDocId** *(string) --*

          Specifies the document ID. Use this setting when ``NestingLevel`` is set to NONE.

          Default value is false.

        - **DocsToInvestigate** *(string) --*

          Indicates the number of documents to preview to determine the document organization. Use
          this setting when ``NestingLevel`` is set to ONE.

          Must be a positive value greater than 0. Default value is 1000.

        - **AuthSource** *(string) --*

          The MongoDB database name. This setting is not used when ``authType=NO`` .

          The default is admin.

        - **KmsKeyId** *(string) --*

          The AWS KMS key identifier that is used to encrypt the content on the replication
          instance. If you don't specify a value for the ``KmsKeyId`` parameter, then AWS DMS uses
          your default encryption key. AWS KMS creates the default encryption key for your AWS
          account. Your AWS account has a different default encryption key for each AWS Region.

      - **KinesisSettings** *(dict) --*

        The settings for the Amazon Kinesis source endpoint. For more information, see the
        ``KinesisSettings`` structure.

        - **StreamArn** *(string) --*

          The Amazon Resource Name (ARN) for the Amazon Kinesis Data Streams endpoint.

        - **MessageFormat** *(string) --*

          The output format for the records created on the endpoint. The message format is ``JSON``
          .

        - **ServiceAccessRoleArn** *(string) --*

          The Amazon Resource Name (ARN) for the IAM role that DMS uses to write to the Amazon
          Kinesis data stream.

      - **ElasticsearchSettings** *(dict) --*

        The settings for the Elasticsearch source endpoint. For more information, see the
        ``ElasticsearchSettings`` structure.

        - **ServiceAccessRoleArn** *(string) --*

          The Amazon Resource Name (ARN) used by service to access the IAM role.

        - **EndpointUri** *(string) --*

          The endpoint for the Elasticsearch cluster.

        - **FullLoadErrorPercentage** *(integer) --*

          The maximum percentage of records that can fail to be written before a full load
          operation stops.

        - **ErrorRetryDuration** *(integer) --*

          The maximum number of seconds that DMS retries failed API requests to the Elasticsearch
          cluster.

      - **RedshiftSettings** *(dict) --*

        Settings for the Amazon Redshift endpoint.

        - **AcceptAnyDate** *(boolean) --*

          A value that indicates to allow any date format, including invalid formats such as
          00/00/00 00:00:00, to be loaded without generating an error. You can choose ``true`` or
          ``false`` (the default).

          This parameter applies only to TIMESTAMP and DATE columns. Always use ACCEPTANYDATE with
          the DATEFORMAT parameter. If the date format for the data doesn't match the DATEFORMAT
          specification, Amazon Redshift inserts a NULL value into that field.

        - **AfterConnectScript** *(string) --*

          Code to run after connecting. This parameter should contain the code itself, not the name
          of a file containing the code.

        - **BucketFolder** *(string) --*

          The location where the comma-separated value (.csv) files are stored before being
          uploaded to the S3 bucket.

        - **BucketName** *(string) --*

          The name of the S3 bucket you want to use

        - **ConnectionTimeout** *(integer) --*

          A value that sets the amount of time to wait (in milliseconds) before timing out,
          beginning from when you initially establish a connection.

        - **DatabaseName** *(string) --*

          The name of the Amazon Redshift data warehouse (service) that you are working with.

        - **DateFormat** *(string) --*

          The date format that you are using. Valid values are ``auto`` (case-sensitive), your date
          format string enclosed in quotes, or NULL. If this parameter is left unset (NULL), it
          defaults to a format of 'YYYY-MM-DD'. Using ``auto`` recognizes most strings, even some
          that aren't supported when you use a date format string.

          If your date and time values use formats different from each other, set this to ``auto`` .

        - **EmptyAsNull** *(boolean) --*

          A value that specifies whether AWS DMS should migrate empty CHAR and VARCHAR fields as
          NULL. A value of ``true`` sets empty CHAR and VARCHAR fields to null. The default is
          ``false`` .

        - **EncryptionMode** *(string) --*

          The type of server-side encryption that you want to use for your data. This encryption
          type is part of the endpoint settings or the extra connections attributes for Amazon S3.
          You can choose either ``SSE_S3`` (the default) or ``SSE_KMS`` . To use ``SSE_S3`` ,
          create an AWS Identity and Access Management (IAM) role with a policy that allows
          ``"arn:aws:s3:::*"`` to use the following actions: ``"s3:PutObject", "s3:ListBucket"``

        - **FileTransferUploadStreams** *(integer) --*

          The number of threads used to upload a single file. This parameter accepts a value from 1
          through 64. It defaults to 10.

        - **LoadTimeout** *(integer) --*

          The amount of time to wait (in milliseconds) before timing out, beginning from when you
          begin loading.

        - **MaxFileSize** *(integer) --*

          The maximum size (in KB) of any .csv file used to transfer data to Amazon Redshift. This
          accepts a value from 1 through 1,048,576. It defaults to 32,768 KB (32 MB).

        - **Password** *(string) --*

          The password for the user named in the ``username`` property.

        - **Port** *(integer) --*

          The port number for Amazon Redshift. The default value is 5439.

        - **RemoveQuotes** *(boolean) --*

          A value that specifies to remove surrounding quotation marks from strings in the incoming
          data. All characters within the quotation marks, including delimiters, are retained.
          Choose ``true`` to remove quotation marks. The default is ``false`` .

        - **ReplaceInvalidChars** *(string) --*

          A list of characters that you want to replace. Use with ``ReplaceChars`` .

        - **ReplaceChars** *(string) --*

          A value that specifies to replaces the invalid characters specified in
          ``ReplaceInvalidChars`` , substituting the specified characters instead. The default is
          ``"?"`` .

        - **ServerName** *(string) --*

          The name of the Amazon Redshift cluster you are using.

        - **ServiceAccessRoleArn** *(string) --*

          The Amazon Resource Name (ARN) of the IAM role that has access to the Amazon Redshift
          service.

        - **ServerSideEncryptionKmsKeyId** *(string) --*

          The AWS KMS key ID. If you are using ``SSE_KMS`` for the ``EncryptionMode`` , provide
          this key ID. The key that you use needs an attached policy that enables IAM user
          permissions and allows use of the key.

        - **TimeFormat** *(string) --*

          The time format that you want to use. Valid values are ``auto`` (case-sensitive),
          ``'timeformat_string'`` , ``'epochsecs'`` , or ``'epochmillisecs'`` . It defaults to 10.
          Using ``auto`` recognizes most strings, even some that aren't supported when you use a
          time format string.

          If your date and time values use formats different from each other, set this parameter to
          ``auto`` .

        - **TrimBlanks** *(boolean) --*

          A value that specifies to remove the trailing white space characters from a VARCHAR
          string. This parameter applies only to columns with a VARCHAR data type. Choose ``true``
          to remove unneeded white space. The default is ``false`` .

        - **TruncateColumns** *(boolean) --*

          A value that specifies to truncate data in columns to the appropriate number of
          characters, so that the data fits in the column. This parameter applies only to columns
          with a VARCHAR or CHAR data type, and rows with a size of 4 MB or less. Choose ``true``
          to truncate data. The default is ``false`` .

        - **Username** *(string) --*

          An Amazon Redshift user name for a registered user.

        - **WriteBufferSize** *(integer) --*

          The size of the write buffer to use in rows. Valid values range from 1 through 2,048. The
          default is 1,024. Use this setting to tune performance.
    """


_ClientDeleteEventSubscriptionResponseEventSubscriptionTypeDef = TypedDict(
    "_ClientDeleteEventSubscriptionResponseEventSubscriptionTypeDef",
    {
        "CustomerAwsId": str,
        "CustSubscriptionId": str,
        "SnsTopicArn": str,
        "Status": str,
        "SubscriptionCreationTime": str,
        "SourceType": str,
        "SourceIdsList": List[str],
        "EventCategoriesList": List[str],
        "Enabled": bool,
    },
    total=False,
)


class ClientDeleteEventSubscriptionResponseEventSubscriptionTypeDef(
    _ClientDeleteEventSubscriptionResponseEventSubscriptionTypeDef
):
    """
    Type definition for `ClientDeleteEventSubscriptionResponse` `EventSubscription`

    The event subscription that was deleted.

    - **CustomerAwsId** *(string) --*

      The AWS customer account associated with the AWS DMS event notification subscription.

    - **CustSubscriptionId** *(string) --*

      The AWS DMS event notification subscription Id.

    - **SnsTopicArn** *(string) --*

      The topic ARN of the AWS DMS event notification subscription.

    - **Status** *(string) --*

      The status of the AWS DMS event notification subscription.

      Constraints:

      Can be one of the following: creating | modifying | deleting | active | no-permission |
      topic-not-exist

      The status "no-permission" indicates that AWS DMS no longer has permission to post to the
      SNS topic. The status "topic-not-exist" indicates that the topic was deleted after the
      subscription was created.

    - **SubscriptionCreationTime** *(string) --*

      The time the RDS event notification subscription was created.

    - **SourceType** *(string) --*

      The type of AWS DMS resource that generates events.

      Valid values: replication-instance | replication-server | security-group | replication-task

    - **SourceIdsList** *(list) --*

      A list of source Ids for the event subscription.

      - *(string) --*

    - **EventCategoriesList** *(list) --*

      A lists of event categories.

      - *(string) --*

    - **Enabled** *(boolean) --*

      Boolean value that indicates if the event subscription is enabled.
    """


_ClientDeleteEventSubscriptionResponseTypeDef = TypedDict(
    "_ClientDeleteEventSubscriptionResponseTypeDef",
    {
        "EventSubscription": ClientDeleteEventSubscriptionResponseEventSubscriptionTypeDef
    },
    total=False,
)


class ClientDeleteEventSubscriptionResponseTypeDef(
    _ClientDeleteEventSubscriptionResponseTypeDef
):
    """
    Type definition for `ClientDeleteEventSubscription` `Response`

    - **EventSubscription** *(dict) --*

      The event subscription that was deleted.

      - **CustomerAwsId** *(string) --*

        The AWS customer account associated with the AWS DMS event notification subscription.

      - **CustSubscriptionId** *(string) --*

        The AWS DMS event notification subscription Id.

      - **SnsTopicArn** *(string) --*

        The topic ARN of the AWS DMS event notification subscription.

      - **Status** *(string) --*

        The status of the AWS DMS event notification subscription.

        Constraints:

        Can be one of the following: creating | modifying | deleting | active | no-permission |
        topic-not-exist

        The status "no-permission" indicates that AWS DMS no longer has permission to post to the
        SNS topic. The status "topic-not-exist" indicates that the topic was deleted after the
        subscription was created.

      - **SubscriptionCreationTime** *(string) --*

        The time the RDS event notification subscription was created.

      - **SourceType** *(string) --*

        The type of AWS DMS resource that generates events.

        Valid values: replication-instance | replication-server | security-group | replication-task

      - **SourceIdsList** *(list) --*

        A list of source Ids for the event subscription.

        - *(string) --*

      - **EventCategoriesList** *(list) --*

        A lists of event categories.

        - *(string) --*

      - **Enabled** *(boolean) --*

        Boolean value that indicates if the event subscription is enabled.
    """


_ClientDeleteReplicationInstanceResponseReplicationInstancePendingModifiedValuesTypeDef = TypedDict(
    "_ClientDeleteReplicationInstanceResponseReplicationInstancePendingModifiedValuesTypeDef",
    {
        "ReplicationInstanceClass": str,
        "AllocatedStorage": int,
        "MultiAZ": bool,
        "EngineVersion": str,
    },
    total=False,
)


class ClientDeleteReplicationInstanceResponseReplicationInstancePendingModifiedValuesTypeDef(
    _ClientDeleteReplicationInstanceResponseReplicationInstancePendingModifiedValuesTypeDef
):
    """
    Type definition for `ClientDeleteReplicationInstanceResponseReplicationInstance` `PendingModifiedValues`

    The pending modification values.

    - **ReplicationInstanceClass** *(string) --*

      The compute and memory capacity of the replication instance.

      Valid Values: ``dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large | dms.c4.large
      | dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge``

    - **AllocatedStorage** *(integer) --*

      The amount of storage (in gigabytes) that is allocated for the replication instance.

    - **MultiAZ** *(boolean) --*

      Specifies whether the replication instance is a Multi-AZ deployment. You cannot set the
      ``AvailabilityZone`` parameter if the Multi-AZ parameter is set to ``true`` .

    - **EngineVersion** *(string) --*

      The engine version number of the replication instance.
    """


_ClientDeleteReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "_ClientDeleteReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)


class ClientDeleteReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef(
    _ClientDeleteReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef
):
    """
    Type definition for `ClientDeleteReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnets` `SubnetAvailabilityZone`

    The Availability Zone of the subnet.

    - **Name** *(string) --*

      The name of the availability zone.
    """


_ClientDeleteReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsTypeDef = TypedDict(
    "_ClientDeleteReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientDeleteReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)


class ClientDeleteReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsTypeDef(
    _ClientDeleteReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsTypeDef
):
    """
    Type definition for `ClientDeleteReplicationInstanceResponseReplicationInstanceReplicationSubnetGroup` `Subnets`

    - **SubnetIdentifier** *(string) --*

      The subnet identifier.

    - **SubnetAvailabilityZone** *(dict) --*

      The Availability Zone of the subnet.

      - **Name** *(string) --*

        The name of the availability zone.

    - **SubnetStatus** *(string) --*

      The status of the subnet.
    """


_ClientDeleteReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupTypeDef = TypedDict(
    "_ClientDeleteReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupTypeDef",
    {
        "ReplicationSubnetGroupIdentifier": str,
        "ReplicationSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[
            ClientDeleteReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsTypeDef
        ],
    },
    total=False,
)


class ClientDeleteReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupTypeDef(
    _ClientDeleteReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupTypeDef
):
    """
    Type definition for `ClientDeleteReplicationInstanceResponseReplicationInstance` `ReplicationSubnetGroup`

    The subnet group for the replication instance.

    - **ReplicationSubnetGroupIdentifier** *(string) --*

      The identifier of the replication instance subnet group.

    - **ReplicationSubnetGroupDescription** *(string) --*

      A description for the replication subnet group.

    - **VpcId** *(string) --*

      The ID of the VPC.

    - **SubnetGroupStatus** *(string) --*

      The status of the subnet group.

    - **Subnets** *(list) --*

      The subnets that are in the subnet group.

      - *(dict) --*

        - **SubnetIdentifier** *(string) --*

          The subnet identifier.

        - **SubnetAvailabilityZone** *(dict) --*

          The Availability Zone of the subnet.

          - **Name** *(string) --*

            The name of the availability zone.

        - **SubnetStatus** *(string) --*

          The status of the subnet.
    """


_ClientDeleteReplicationInstanceResponseReplicationInstanceVpcSecurityGroupsTypeDef = TypedDict(
    "_ClientDeleteReplicationInstanceResponseReplicationInstanceVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientDeleteReplicationInstanceResponseReplicationInstanceVpcSecurityGroupsTypeDef(
    _ClientDeleteReplicationInstanceResponseReplicationInstanceVpcSecurityGroupsTypeDef
):
    """
    Type definition for `ClientDeleteReplicationInstanceResponseReplicationInstance` `VpcSecurityGroups`

    - **VpcSecurityGroupId** *(string) --*

      The VPC security group Id.

    - **Status** *(string) --*

      The status of the VPC security group.
    """


_ClientDeleteReplicationInstanceResponseReplicationInstanceTypeDef = TypedDict(
    "_ClientDeleteReplicationInstanceResponseReplicationInstanceTypeDef",
    {
        "ReplicationInstanceIdentifier": str,
        "ReplicationInstanceClass": str,
        "ReplicationInstanceStatus": str,
        "AllocatedStorage": int,
        "InstanceCreateTime": datetime,
        "VpcSecurityGroups": List[
            ClientDeleteReplicationInstanceResponseReplicationInstanceVpcSecurityGroupsTypeDef
        ],
        "AvailabilityZone": str,
        "ReplicationSubnetGroup": ClientDeleteReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupTypeDef,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientDeleteReplicationInstanceResponseReplicationInstancePendingModifiedValuesTypeDef,
        "MultiAZ": bool,
        "EngineVersion": str,
        "AutoMinorVersionUpgrade": bool,
        "KmsKeyId": str,
        "ReplicationInstanceArn": str,
        "ReplicationInstancePublicIpAddress": str,
        "ReplicationInstancePrivateIpAddress": str,
        "ReplicationInstancePublicIpAddresses": List[str],
        "ReplicationInstancePrivateIpAddresses": List[str],
        "PubliclyAccessible": bool,
        "SecondaryAvailabilityZone": str,
        "FreeUntil": datetime,
        "DnsNameServers": str,
    },
    total=False,
)


class ClientDeleteReplicationInstanceResponseReplicationInstanceTypeDef(
    _ClientDeleteReplicationInstanceResponseReplicationInstanceTypeDef
):
    """
    Type definition for `ClientDeleteReplicationInstanceResponse` `ReplicationInstance`

    The replication instance that was deleted.

    - **ReplicationInstanceIdentifier** *(string) --*

      The replication instance identifier. This parameter is stored as a lowercase string.

      Constraints:

      * Must contain from 1 to 63 alphanumeric characters or hyphens.

      * First character must be a letter.

      * Cannot end with a hyphen or contain two consecutive hyphens.

      Example: ``myrepinstance``

    - **ReplicationInstanceClass** *(string) --*

      The compute and memory capacity of the replication instance.

      Valid Values: ``dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large | dms.c4.large |
      dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge``

    - **ReplicationInstanceStatus** *(string) --*

      The status of the replication instance.

    - **AllocatedStorage** *(integer) --*

      The amount of storage (in gigabytes) that is allocated for the replication instance.

    - **InstanceCreateTime** *(datetime) --*

      The time the replication instance was created.

    - **VpcSecurityGroups** *(list) --*

      The VPC security group for the instance.

      - *(dict) --*

        - **VpcSecurityGroupId** *(string) --*

          The VPC security group Id.

        - **Status** *(string) --*

          The status of the VPC security group.

    - **AvailabilityZone** *(string) --*

      The Availability Zone for the instance.

    - **ReplicationSubnetGroup** *(dict) --*

      The subnet group for the replication instance.

      - **ReplicationSubnetGroupIdentifier** *(string) --*

        The identifier of the replication instance subnet group.

      - **ReplicationSubnetGroupDescription** *(string) --*

        A description for the replication subnet group.

      - **VpcId** *(string) --*

        The ID of the VPC.

      - **SubnetGroupStatus** *(string) --*

        The status of the subnet group.

      - **Subnets** *(list) --*

        The subnets that are in the subnet group.

        - *(dict) --*

          - **SubnetIdentifier** *(string) --*

            The subnet identifier.

          - **SubnetAvailabilityZone** *(dict) --*

            The Availability Zone of the subnet.

            - **Name** *(string) --*

              The name of the availability zone.

          - **SubnetStatus** *(string) --*

            The status of the subnet.

    - **PreferredMaintenanceWindow** *(string) --*

      The maintenance window times for the replication instance.

    - **PendingModifiedValues** *(dict) --*

      The pending modification values.

      - **ReplicationInstanceClass** *(string) --*

        The compute and memory capacity of the replication instance.

        Valid Values: ``dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large | dms.c4.large
        | dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge``

      - **AllocatedStorage** *(integer) --*

        The amount of storage (in gigabytes) that is allocated for the replication instance.

      - **MultiAZ** *(boolean) --*

        Specifies whether the replication instance is a Multi-AZ deployment. You cannot set the
        ``AvailabilityZone`` parameter if the Multi-AZ parameter is set to ``true`` .

      - **EngineVersion** *(string) --*

        The engine version number of the replication instance.

    - **MultiAZ** *(boolean) --*

      Specifies whether the replication instance is a Multi-AZ deployment. You cannot set the
      ``AvailabilityZone`` parameter if the Multi-AZ parameter is set to ``true`` .

    - **EngineVersion** *(string) --*

      The engine version number of the replication instance.

    - **AutoMinorVersionUpgrade** *(boolean) --*

      Boolean value indicating if minor version upgrades will be automatically applied to the
      instance.

    - **KmsKeyId** *(string) --*

      An AWS KMS key identifier that is used to encrypt the data on the replication instance.

      If you don't specify a value for the ``KmsKeyId`` parameter, then AWS DMS uses your default
      encryption key.

      AWS KMS creates the default encryption key for your AWS account. Your AWS account has a
      different default encryption key for each AWS Region.

    - **ReplicationInstanceArn** *(string) --*

      The Amazon Resource Name (ARN) of the replication instance.

    - **ReplicationInstancePublicIpAddress** *(string) --*

      The public IP address of the replication instance.

    - **ReplicationInstancePrivateIpAddress** *(string) --*

      The private IP address of the replication instance.

    - **ReplicationInstancePublicIpAddresses** *(list) --*

      One or more public IP addresses for the replication instance.

      - *(string) --*

    - **ReplicationInstancePrivateIpAddresses** *(list) --*

      One or more private IP addresses for the replication instance.

      - *(string) --*

    - **PubliclyAccessible** *(boolean) --*

      Specifies the accessibility options for the replication instance. A value of ``true``
      represents an instance with a public IP address. A value of ``false`` represents an
      instance with a private IP address. The default value is ``true`` .

    - **SecondaryAvailabilityZone** *(string) --*

      The availability zone of the standby replication instance in a Multi-AZ deployment.

    - **FreeUntil** *(datetime) --*

      The expiration date of the free replication instance that is part of the Free DMS program.

    - **DnsNameServers** *(string) --*

      The DNS name servers for the replication instance.
    """


_ClientDeleteReplicationInstanceResponseTypeDef = TypedDict(
    "_ClientDeleteReplicationInstanceResponseTypeDef",
    {
        "ReplicationInstance": ClientDeleteReplicationInstanceResponseReplicationInstanceTypeDef
    },
    total=False,
)


class ClientDeleteReplicationInstanceResponseTypeDef(
    _ClientDeleteReplicationInstanceResponseTypeDef
):
    """
    Type definition for `ClientDeleteReplicationInstance` `Response`

    - **ReplicationInstance** *(dict) --*

      The replication instance that was deleted.

      - **ReplicationInstanceIdentifier** *(string) --*

        The replication instance identifier. This parameter is stored as a lowercase string.

        Constraints:

        * Must contain from 1 to 63 alphanumeric characters or hyphens.

        * First character must be a letter.

        * Cannot end with a hyphen or contain two consecutive hyphens.

        Example: ``myrepinstance``

      - **ReplicationInstanceClass** *(string) --*

        The compute and memory capacity of the replication instance.

        Valid Values: ``dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large | dms.c4.large |
        dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge``

      - **ReplicationInstanceStatus** *(string) --*

        The status of the replication instance.

      - **AllocatedStorage** *(integer) --*

        The amount of storage (in gigabytes) that is allocated for the replication instance.

      - **InstanceCreateTime** *(datetime) --*

        The time the replication instance was created.

      - **VpcSecurityGroups** *(list) --*

        The VPC security group for the instance.

        - *(dict) --*

          - **VpcSecurityGroupId** *(string) --*

            The VPC security group Id.

          - **Status** *(string) --*

            The status of the VPC security group.

      - **AvailabilityZone** *(string) --*

        The Availability Zone for the instance.

      - **ReplicationSubnetGroup** *(dict) --*

        The subnet group for the replication instance.

        - **ReplicationSubnetGroupIdentifier** *(string) --*

          The identifier of the replication instance subnet group.

        - **ReplicationSubnetGroupDescription** *(string) --*

          A description for the replication subnet group.

        - **VpcId** *(string) --*

          The ID of the VPC.

        - **SubnetGroupStatus** *(string) --*

          The status of the subnet group.

        - **Subnets** *(list) --*

          The subnets that are in the subnet group.

          - *(dict) --*

            - **SubnetIdentifier** *(string) --*

              The subnet identifier.

            - **SubnetAvailabilityZone** *(dict) --*

              The Availability Zone of the subnet.

              - **Name** *(string) --*

                The name of the availability zone.

            - **SubnetStatus** *(string) --*

              The status of the subnet.

      - **PreferredMaintenanceWindow** *(string) --*

        The maintenance window times for the replication instance.

      - **PendingModifiedValues** *(dict) --*

        The pending modification values.

        - **ReplicationInstanceClass** *(string) --*

          The compute and memory capacity of the replication instance.

          Valid Values: ``dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large | dms.c4.large
          | dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge``

        - **AllocatedStorage** *(integer) --*

          The amount of storage (in gigabytes) that is allocated for the replication instance.

        - **MultiAZ** *(boolean) --*

          Specifies whether the replication instance is a Multi-AZ deployment. You cannot set the
          ``AvailabilityZone`` parameter if the Multi-AZ parameter is set to ``true`` .

        - **EngineVersion** *(string) --*

          The engine version number of the replication instance.

      - **MultiAZ** *(boolean) --*

        Specifies whether the replication instance is a Multi-AZ deployment. You cannot set the
        ``AvailabilityZone`` parameter if the Multi-AZ parameter is set to ``true`` .

      - **EngineVersion** *(string) --*

        The engine version number of the replication instance.

      - **AutoMinorVersionUpgrade** *(boolean) --*

        Boolean value indicating if minor version upgrades will be automatically applied to the
        instance.

      - **KmsKeyId** *(string) --*

        An AWS KMS key identifier that is used to encrypt the data on the replication instance.

        If you don't specify a value for the ``KmsKeyId`` parameter, then AWS DMS uses your default
        encryption key.

        AWS KMS creates the default encryption key for your AWS account. Your AWS account has a
        different default encryption key for each AWS Region.

      - **ReplicationInstanceArn** *(string) --*

        The Amazon Resource Name (ARN) of the replication instance.

      - **ReplicationInstancePublicIpAddress** *(string) --*

        The public IP address of the replication instance.

      - **ReplicationInstancePrivateIpAddress** *(string) --*

        The private IP address of the replication instance.

      - **ReplicationInstancePublicIpAddresses** *(list) --*

        One or more public IP addresses for the replication instance.

        - *(string) --*

      - **ReplicationInstancePrivateIpAddresses** *(list) --*

        One or more private IP addresses for the replication instance.

        - *(string) --*

      - **PubliclyAccessible** *(boolean) --*

        Specifies the accessibility options for the replication instance. A value of ``true``
        represents an instance with a public IP address. A value of ``false`` represents an
        instance with a private IP address. The default value is ``true`` .

      - **SecondaryAvailabilityZone** *(string) --*

        The availability zone of the standby replication instance in a Multi-AZ deployment.

      - **FreeUntil** *(datetime) --*

        The expiration date of the free replication instance that is part of the Free DMS program.

      - **DnsNameServers** *(string) --*

        The DNS name servers for the replication instance.
    """


_ClientDescribeAccountAttributesResponseAccountQuotasTypeDef = TypedDict(
    "_ClientDescribeAccountAttributesResponseAccountQuotasTypeDef",
    {"AccountQuotaName": str, "Used": int, "Max": int},
    total=False,
)


class ClientDescribeAccountAttributesResponseAccountQuotasTypeDef(
    _ClientDescribeAccountAttributesResponseAccountQuotasTypeDef
):
    """
    Type definition for `ClientDescribeAccountAttributesResponse` `AccountQuotas`

    Describes a quota for an AWS account, for example, the number of replication instances
    allowed.

    - **AccountQuotaName** *(string) --*

      The name of the AWS DMS quota for this AWS account.

    - **Used** *(integer) --*

      The amount currently used toward the quota maximum.

    - **Max** *(integer) --*

      The maximum allowed value for the quota.
    """


_ClientDescribeAccountAttributesResponseTypeDef = TypedDict(
    "_ClientDescribeAccountAttributesResponseTypeDef",
    {
        "AccountQuotas": List[
            ClientDescribeAccountAttributesResponseAccountQuotasTypeDef
        ],
        "UniqueAccountIdentifier": str,
    },
    total=False,
)


class ClientDescribeAccountAttributesResponseTypeDef(
    _ClientDescribeAccountAttributesResponseTypeDef
):
    """
    Type definition for `ClientDescribeAccountAttributes` `Response`

    - **AccountQuotas** *(list) --*

      Account quota information.

      - *(dict) --*

        Describes a quota for an AWS account, for example, the number of replication instances
        allowed.

        - **AccountQuotaName** *(string) --*

          The name of the AWS DMS quota for this AWS account.

        - **Used** *(integer) --*

          The amount currently used toward the quota maximum.

        - **Max** *(integer) --*

          The maximum allowed value for the quota.

    - **UniqueAccountIdentifier** *(string) --*

      A unique AWS DMS identifier for an account in a particular AWS Region. The value of this
      identifier has the following format: ``c99999999999`` . DMS uses this identifier to name
      artifacts. For example, DMS uses this identifier to name the default Amazon S3 bucket for
      storing task assessment reports in a given AWS Region. The format of this S3 bucket name is
      the following: ``dms-*AccountNumber* -*UniqueAccountIdentifier* .`` Here is an example name
      for this default S3 bucket: ``dms-111122223333-c44445555666`` .

      .. note::

        AWS DMS supports the ``UniqueAccountIdentifier`` parameter in versions 3.1.4 and later.
    """


_ClientDescribeCertificatesFiltersTypeDef = TypedDict(
    "_ClientDescribeCertificatesFiltersTypeDef", {"Name": str, "Values": List[str]}
)


class ClientDescribeCertificatesFiltersTypeDef(
    _ClientDescribeCertificatesFiltersTypeDef
):
    """
    Type definition for `ClientDescribeCertificates` `Filters`

    - **Name** *(string) --* **[REQUIRED]**

      The name of the filter.

    - **Values** *(list) --* **[REQUIRED]**

      The filter value.

      - *(string) --*
    """


_ClientDescribeCertificatesResponseCertificatesTypeDef = TypedDict(
    "_ClientDescribeCertificatesResponseCertificatesTypeDef",
    {
        "CertificateIdentifier": str,
        "CertificateCreationDate": datetime,
        "CertificatePem": str,
        "CertificateWallet": bytes,
        "CertificateArn": str,
        "CertificateOwner": str,
        "ValidFromDate": datetime,
        "ValidToDate": datetime,
        "SigningAlgorithm": str,
        "KeyLength": int,
    },
    total=False,
)


class ClientDescribeCertificatesResponseCertificatesTypeDef(
    _ClientDescribeCertificatesResponseCertificatesTypeDef
):
    """
    Type definition for `ClientDescribeCertificatesResponse` `Certificates`

    The SSL certificate that can be used to encrypt connections between the endpoints and the
    replication instance.

    - **CertificateIdentifier** *(string) --*

      A customer-assigned name for the certificate. Identifiers must begin with a letter; must
      contain only ASCII letters, digits, and hyphens; and must not end with a hyphen or
      contain two consecutive hyphens.

    - **CertificateCreationDate** *(datetime) --*

      The date that the certificate was created.

    - **CertificatePem** *(string) --*

      The contents of a ``.pem`` file, which contains an X.509 certificate.

    - **CertificateWallet** *(bytes) --*

      The location of an imported Oracle Wallet certificate for use with SSL.

    - **CertificateArn** *(string) --*

      The Amazon Resource Name (ARN) for the certificate.

    - **CertificateOwner** *(string) --*

      The owner of the certificate.

    - **ValidFromDate** *(datetime) --*

      The beginning date that the certificate is valid.

    - **ValidToDate** *(datetime) --*

      The final date that the certificate is valid.

    - **SigningAlgorithm** *(string) --*

      The signing algorithm for the certificate.

    - **KeyLength** *(integer) --*

      The key length of the cryptographic algorithm being used.
    """


_ClientDescribeCertificatesResponseTypeDef = TypedDict(
    "_ClientDescribeCertificatesResponseTypeDef",
    {
        "Marker": str,
        "Certificates": List[ClientDescribeCertificatesResponseCertificatesTypeDef],
    },
    total=False,
)


class ClientDescribeCertificatesResponseTypeDef(
    _ClientDescribeCertificatesResponseTypeDef
):
    """
    Type definition for `ClientDescribeCertificates` `Response`

    - **Marker** *(string) --*

      The pagination token.

    - **Certificates** *(list) --*

      The Secure Sockets Layer (SSL) certificates associated with the replication instance.

      - *(dict) --*

        The SSL certificate that can be used to encrypt connections between the endpoints and the
        replication instance.

        - **CertificateIdentifier** *(string) --*

          A customer-assigned name for the certificate. Identifiers must begin with a letter; must
          contain only ASCII letters, digits, and hyphens; and must not end with a hyphen or
          contain two consecutive hyphens.

        - **CertificateCreationDate** *(datetime) --*

          The date that the certificate was created.

        - **CertificatePem** *(string) --*

          The contents of a ``.pem`` file, which contains an X.509 certificate.

        - **CertificateWallet** *(bytes) --*

          The location of an imported Oracle Wallet certificate for use with SSL.

        - **CertificateArn** *(string) --*

          The Amazon Resource Name (ARN) for the certificate.

        - **CertificateOwner** *(string) --*

          The owner of the certificate.

        - **ValidFromDate** *(datetime) --*

          The beginning date that the certificate is valid.

        - **ValidToDate** *(datetime) --*

          The final date that the certificate is valid.

        - **SigningAlgorithm** *(string) --*

          The signing algorithm for the certificate.

        - **KeyLength** *(integer) --*

          The key length of the cryptographic algorithm being used.
    """


_ClientDescribeConnectionsFiltersTypeDef = TypedDict(
    "_ClientDescribeConnectionsFiltersTypeDef", {"Name": str, "Values": List[str]}
)


class ClientDescribeConnectionsFiltersTypeDef(_ClientDescribeConnectionsFiltersTypeDef):
    """
    Type definition for `ClientDescribeConnections` `Filters`

    - **Name** *(string) --* **[REQUIRED]**

      The name of the filter.

    - **Values** *(list) --* **[REQUIRED]**

      The filter value.

      - *(string) --*
    """


_ClientDescribeConnectionsResponseConnectionsTypeDef = TypedDict(
    "_ClientDescribeConnectionsResponseConnectionsTypeDef",
    {
        "ReplicationInstanceArn": str,
        "EndpointArn": str,
        "Status": str,
        "LastFailureMessage": str,
        "EndpointIdentifier": str,
        "ReplicationInstanceIdentifier": str,
    },
    total=False,
)


class ClientDescribeConnectionsResponseConnectionsTypeDef(
    _ClientDescribeConnectionsResponseConnectionsTypeDef
):
    """
    Type definition for `ClientDescribeConnectionsResponse` `Connections`

    - **ReplicationInstanceArn** *(string) --*

      The Amazon Resource Name (ARN) of the replication instance.

    - **EndpointArn** *(string) --*

      The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

    - **Status** *(string) --*

      The connection status.

    - **LastFailureMessage** *(string) --*

      The error message when the connection last failed.

    - **EndpointIdentifier** *(string) --*

      The identifier of the endpoint. Identifiers must begin with a letter; must contain only
      ASCII letters, digits, and hyphens; and must not end with a hyphen or contain two
      consecutive hyphens.

    - **ReplicationInstanceIdentifier** *(string) --*

      The replication instance identifier. This parameter is stored as a lowercase string.
    """


_ClientDescribeConnectionsResponseTypeDef = TypedDict(
    "_ClientDescribeConnectionsResponseTypeDef",
    {
        "Marker": str,
        "Connections": List[ClientDescribeConnectionsResponseConnectionsTypeDef],
    },
    total=False,
)


class ClientDescribeConnectionsResponseTypeDef(
    _ClientDescribeConnectionsResponseTypeDef
):
    """
    Type definition for `ClientDescribeConnections` `Response`

    - **Marker** *(string) --*

      An optional pagination token provided by a previous request. If this parameter is specified,
      the response includes only records beyond the marker, up to the value specified by
      ``MaxRecords`` .

    - **Connections** *(list) --*

      A description of the connections.

      - *(dict) --*

        - **ReplicationInstanceArn** *(string) --*

          The Amazon Resource Name (ARN) of the replication instance.

        - **EndpointArn** *(string) --*

          The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

        - **Status** *(string) --*

          The connection status.

        - **LastFailureMessage** *(string) --*

          The error message when the connection last failed.

        - **EndpointIdentifier** *(string) --*

          The identifier of the endpoint. Identifiers must begin with a letter; must contain only
          ASCII letters, digits, and hyphens; and must not end with a hyphen or contain two
          consecutive hyphens.

        - **ReplicationInstanceIdentifier** *(string) --*

          The replication instance identifier. This parameter is stored as a lowercase string.
    """


_ClientDescribeEndpointTypesFiltersTypeDef = TypedDict(
    "_ClientDescribeEndpointTypesFiltersTypeDef", {"Name": str, "Values": List[str]}
)


class ClientDescribeEndpointTypesFiltersTypeDef(
    _ClientDescribeEndpointTypesFiltersTypeDef
):
    """
    Type definition for `ClientDescribeEndpointTypes` `Filters`

    - **Name** *(string) --* **[REQUIRED]**

      The name of the filter.

    - **Values** *(list) --* **[REQUIRED]**

      The filter value.

      - *(string) --*
    """


_ClientDescribeEndpointTypesResponseSupportedEndpointTypesTypeDef = TypedDict(
    "_ClientDescribeEndpointTypesResponseSupportedEndpointTypesTypeDef",
    {
        "EngineName": str,
        "SupportsCDC": bool,
        "EndpointType": str,
        "EngineDisplayName": str,
    },
    total=False,
)


class ClientDescribeEndpointTypesResponseSupportedEndpointTypesTypeDef(
    _ClientDescribeEndpointTypesResponseSupportedEndpointTypesTypeDef
):
    """
    Type definition for `ClientDescribeEndpointTypesResponse` `SupportedEndpointTypes`

    - **EngineName** *(string) --*

      The database engine name. Valid values, depending on the EndpointType, include mysql,
      oracle, postgres, mariadb, aurora, aurora-postgresql, redshift, s3, db2, azuredb, sybase,
      dynamodb, mongodb, and sqlserver.

    - **SupportsCDC** *(boolean) --*

      Indicates if Change Data Capture (CDC) is supported.

    - **EndpointType** *(string) --*

      The type of endpoint. Valid values are ``source`` and ``target`` .

    - **EngineDisplayName** *(string) --*

      The expanded name for the engine name. For example, if the ``EngineName`` parameter is
      "aurora," this value would be "Amazon Aurora MySQL."
    """


_ClientDescribeEndpointTypesResponseTypeDef = TypedDict(
    "_ClientDescribeEndpointTypesResponseTypeDef",
    {
        "Marker": str,
        "SupportedEndpointTypes": List[
            ClientDescribeEndpointTypesResponseSupportedEndpointTypesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeEndpointTypesResponseTypeDef(
    _ClientDescribeEndpointTypesResponseTypeDef
):
    """
    Type definition for `ClientDescribeEndpointTypes` `Response`

    - **Marker** *(string) --*

      An optional pagination token provided by a previous request. If this parameter is specified,
      the response includes only records beyond the marker, up to the value specified by
      ``MaxRecords`` .

    - **SupportedEndpointTypes** *(list) --*

      The types of endpoints that are supported.

      - *(dict) --*

        - **EngineName** *(string) --*

          The database engine name. Valid values, depending on the EndpointType, include mysql,
          oracle, postgres, mariadb, aurora, aurora-postgresql, redshift, s3, db2, azuredb, sybase,
          dynamodb, mongodb, and sqlserver.

        - **SupportsCDC** *(boolean) --*

          Indicates if Change Data Capture (CDC) is supported.

        - **EndpointType** *(string) --*

          The type of endpoint. Valid values are ``source`` and ``target`` .

        - **EngineDisplayName** *(string) --*

          The expanded name for the engine name. For example, if the ``EngineName`` parameter is
          "aurora," this value would be "Amazon Aurora MySQL."
    """


_ClientDescribeEndpointsFiltersTypeDef = TypedDict(
    "_ClientDescribeEndpointsFiltersTypeDef", {"Name": str, "Values": List[str]}
)


class ClientDescribeEndpointsFiltersTypeDef(_ClientDescribeEndpointsFiltersTypeDef):
    """
    Type definition for `ClientDescribeEndpoints` `Filters`

    - **Name** *(string) --* **[REQUIRED]**

      The name of the filter.

    - **Values** *(list) --* **[REQUIRED]**

      The filter value.

      - *(string) --*
    """


_ClientDescribeEndpointsResponseEndpointsDmsTransferSettingsTypeDef = TypedDict(
    "_ClientDescribeEndpointsResponseEndpointsDmsTransferSettingsTypeDef",
    {"ServiceAccessRoleArn": str, "BucketName": str},
    total=False,
)


class ClientDescribeEndpointsResponseEndpointsDmsTransferSettingsTypeDef(
    _ClientDescribeEndpointsResponseEndpointsDmsTransferSettingsTypeDef
):
    """
    Type definition for `ClientDescribeEndpointsResponseEndpoints` `DmsTransferSettings`

    The settings in JSON format for the DMS transfer type of source endpoint.

    Possible settings include the following:

    * ``ServiceAccessRoleArn`` - The IAM role that has permission to access the Amazon S3
    bucket.

    * ``BucketName`` - The name of the S3 bucket to use.

    * ``CompressionType`` - An optional parameter to use GZIP to compress the target files.
    To use GZIP, set this value to ``NONE`` (the default). To keep the files uncompressed,
    don't use this value.

    Shorthand syntax for these settings is as follows:
    ``ServiceAccessRoleArn=string,BucketName=string,CompressionType=string``

    JSON syntax for these settings is as follows: ``{ "ServiceAccessRoleArn": "string",
    "BucketName": "string", "CompressionType": "none"|"gzip" }``

    - **ServiceAccessRoleArn** *(string) --*

      The IAM role that has permission to access the Amazon S3 bucket.

    - **BucketName** *(string) --*

      The name of the S3 bucket to use.
    """


_ClientDescribeEndpointsResponseEndpointsDynamoDbSettingsTypeDef = TypedDict(
    "_ClientDescribeEndpointsResponseEndpointsDynamoDbSettingsTypeDef",
    {"ServiceAccessRoleArn": str},
    total=False,
)


class ClientDescribeEndpointsResponseEndpointsDynamoDbSettingsTypeDef(
    _ClientDescribeEndpointsResponseEndpointsDynamoDbSettingsTypeDef
):
    """
    Type definition for `ClientDescribeEndpointsResponseEndpoints` `DynamoDbSettings`

    The settings for the target DynamoDB database. For more information, see the
    ``DynamoDBSettings`` structure.

    - **ServiceAccessRoleArn** *(string) --*

      The Amazon Resource Name (ARN) used by the service access IAM role.
    """


_ClientDescribeEndpointsResponseEndpointsElasticsearchSettingsTypeDef = TypedDict(
    "_ClientDescribeEndpointsResponseEndpointsElasticsearchSettingsTypeDef",
    {
        "ServiceAccessRoleArn": str,
        "EndpointUri": str,
        "FullLoadErrorPercentage": int,
        "ErrorRetryDuration": int,
    },
    total=False,
)


class ClientDescribeEndpointsResponseEndpointsElasticsearchSettingsTypeDef(
    _ClientDescribeEndpointsResponseEndpointsElasticsearchSettingsTypeDef
):
    """
    Type definition for `ClientDescribeEndpointsResponseEndpoints` `ElasticsearchSettings`

    The settings for the Elasticsearch source endpoint. For more information, see the
    ``ElasticsearchSettings`` structure.

    - **ServiceAccessRoleArn** *(string) --*

      The Amazon Resource Name (ARN) used by service to access the IAM role.

    - **EndpointUri** *(string) --*

      The endpoint for the Elasticsearch cluster.

    - **FullLoadErrorPercentage** *(integer) --*

      The maximum percentage of records that can fail to be written before a full load
      operation stops.

    - **ErrorRetryDuration** *(integer) --*

      The maximum number of seconds that DMS retries failed API requests to the Elasticsearch
      cluster.
    """


_ClientDescribeEndpointsResponseEndpointsKinesisSettingsTypeDef = TypedDict(
    "_ClientDescribeEndpointsResponseEndpointsKinesisSettingsTypeDef",
    {"StreamArn": str, "MessageFormat": str, "ServiceAccessRoleArn": str},
    total=False,
)


class ClientDescribeEndpointsResponseEndpointsKinesisSettingsTypeDef(
    _ClientDescribeEndpointsResponseEndpointsKinesisSettingsTypeDef
):
    """
    Type definition for `ClientDescribeEndpointsResponseEndpoints` `KinesisSettings`

    The settings for the Amazon Kinesis source endpoint. For more information, see the
    ``KinesisSettings`` structure.

    - **StreamArn** *(string) --*

      The Amazon Resource Name (ARN) for the Amazon Kinesis Data Streams endpoint.

    - **MessageFormat** *(string) --*

      The output format for the records created on the endpoint. The message format is
      ``JSON`` .

    - **ServiceAccessRoleArn** *(string) --*

      The Amazon Resource Name (ARN) for the IAM role that DMS uses to write to the Amazon
      Kinesis data stream.
    """


_ClientDescribeEndpointsResponseEndpointsMongoDbSettingsTypeDef = TypedDict(
    "_ClientDescribeEndpointsResponseEndpointsMongoDbSettingsTypeDef",
    {
        "Username": str,
        "Password": str,
        "ServerName": str,
        "Port": int,
        "DatabaseName": str,
        "AuthType": str,
        "AuthMechanism": str,
        "NestingLevel": str,
        "ExtractDocId": str,
        "DocsToInvestigate": str,
        "AuthSource": str,
        "KmsKeyId": str,
    },
    total=False,
)


class ClientDescribeEndpointsResponseEndpointsMongoDbSettingsTypeDef(
    _ClientDescribeEndpointsResponseEndpointsMongoDbSettingsTypeDef
):
    """
    Type definition for `ClientDescribeEndpointsResponseEndpoints` `MongoDbSettings`

    The settings for the MongoDB source endpoint. For more information, see the
    ``MongoDbSettings`` structure.

    - **Username** *(string) --*

      The user name you use to access the MongoDB source endpoint.

    - **Password** *(string) --*

      The password for the user account you use to access the MongoDB source endpoint.

    - **ServerName** *(string) --*

      The name of the server on the MongoDB source endpoint.

    - **Port** *(integer) --*

      The port value for the MongoDB source endpoint.

    - **DatabaseName** *(string) --*

      The database name on the MongoDB source endpoint.

    - **AuthType** *(string) --*

      The authentication type you use to access the MongoDB source endpoint.

      Valid values: NO, PASSWORD

      When NO is selected, user name and password parameters are not used and can be empty.

    - **AuthMechanism** *(string) --*

      The authentication mechanism you use to access the MongoDB source endpoint.

      Valid values: DEFAULT, MONGODB_CR, SCRAM_SHA_1

      DEFAULT – For MongoDB version 2.x, use MONGODB_CR. For MongoDB version 3.x, use
      SCRAM_SHA_1. This setting is not used when authType=No.

    - **NestingLevel** *(string) --*

      Specifies either document or table mode.

      Valid values: NONE, ONE

      Default value is NONE. Specify NONE to use document mode. Specify ONE to use table mode.

    - **ExtractDocId** *(string) --*

      Specifies the document ID. Use this setting when ``NestingLevel`` is set to NONE.

      Default value is false.

    - **DocsToInvestigate** *(string) --*

      Indicates the number of documents to preview to determine the document organization.
      Use this setting when ``NestingLevel`` is set to ONE.

      Must be a positive value greater than 0. Default value is 1000.

    - **AuthSource** *(string) --*

      The MongoDB database name. This setting is not used when ``authType=NO`` .

      The default is admin.

    - **KmsKeyId** *(string) --*

      The AWS KMS key identifier that is used to encrypt the content on the replication
      instance. If you don't specify a value for the ``KmsKeyId`` parameter, then AWS DMS
      uses your default encryption key. AWS KMS creates the default encryption key for your
      AWS account. Your AWS account has a different default encryption key for each AWS
      Region.
    """


_ClientDescribeEndpointsResponseEndpointsRedshiftSettingsTypeDef = TypedDict(
    "_ClientDescribeEndpointsResponseEndpointsRedshiftSettingsTypeDef",
    {
        "AcceptAnyDate": bool,
        "AfterConnectScript": str,
        "BucketFolder": str,
        "BucketName": str,
        "ConnectionTimeout": int,
        "DatabaseName": str,
        "DateFormat": str,
        "EmptyAsNull": bool,
        "EncryptionMode": str,
        "FileTransferUploadStreams": int,
        "LoadTimeout": int,
        "MaxFileSize": int,
        "Password": str,
        "Port": int,
        "RemoveQuotes": bool,
        "ReplaceInvalidChars": str,
        "ReplaceChars": str,
        "ServerName": str,
        "ServiceAccessRoleArn": str,
        "ServerSideEncryptionKmsKeyId": str,
        "TimeFormat": str,
        "TrimBlanks": bool,
        "TruncateColumns": bool,
        "Username": str,
        "WriteBufferSize": int,
    },
    total=False,
)


class ClientDescribeEndpointsResponseEndpointsRedshiftSettingsTypeDef(
    _ClientDescribeEndpointsResponseEndpointsRedshiftSettingsTypeDef
):
    """
    Type definition for `ClientDescribeEndpointsResponseEndpoints` `RedshiftSettings`

    Settings for the Amazon Redshift endpoint.

    - **AcceptAnyDate** *(boolean) --*

      A value that indicates to allow any date format, including invalid formats such as
      00/00/00 00:00:00, to be loaded without generating an error. You can choose ``true`` or
      ``false`` (the default).

      This parameter applies only to TIMESTAMP and DATE columns. Always use ACCEPTANYDATE
      with the DATEFORMAT parameter. If the date format for the data doesn't match the
      DATEFORMAT specification, Amazon Redshift inserts a NULL value into that field.

    - **AfterConnectScript** *(string) --*

      Code to run after connecting. This parameter should contain the code itself, not the
      name of a file containing the code.

    - **BucketFolder** *(string) --*

      The location where the comma-separated value (.csv) files are stored before being
      uploaded to the S3 bucket.

    - **BucketName** *(string) --*

      The name of the S3 bucket you want to use

    - **ConnectionTimeout** *(integer) --*

      A value that sets the amount of time to wait (in milliseconds) before timing out,
      beginning from when you initially establish a connection.

    - **DatabaseName** *(string) --*

      The name of the Amazon Redshift data warehouse (service) that you are working with.

    - **DateFormat** *(string) --*

      The date format that you are using. Valid values are ``auto`` (case-sensitive), your
      date format string enclosed in quotes, or NULL. If this parameter is left unset (NULL),
      it defaults to a format of 'YYYY-MM-DD'. Using ``auto`` recognizes most strings, even
      some that aren't supported when you use a date format string.

      If your date and time values use formats different from each other, set this to
      ``auto`` .

    - **EmptyAsNull** *(boolean) --*

      A value that specifies whether AWS DMS should migrate empty CHAR and VARCHAR fields as
      NULL. A value of ``true`` sets empty CHAR and VARCHAR fields to null. The default is
      ``false`` .

    - **EncryptionMode** *(string) --*

      The type of server-side encryption that you want to use for your data. This encryption
      type is part of the endpoint settings or the extra connections attributes for Amazon
      S3. You can choose either ``SSE_S3`` (the default) or ``SSE_KMS`` . To use ``SSE_S3`` ,
      create an AWS Identity and Access Management (IAM) role with a policy that allows
      ``"arn:aws:s3:::*"`` to use the following actions: ``"s3:PutObject", "s3:ListBucket"``

    - **FileTransferUploadStreams** *(integer) --*

      The number of threads used to upload a single file. This parameter accepts a value from
      1 through 64. It defaults to 10.

    - **LoadTimeout** *(integer) --*

      The amount of time to wait (in milliseconds) before timing out, beginning from when you
      begin loading.

    - **MaxFileSize** *(integer) --*

      The maximum size (in KB) of any .csv file used to transfer data to Amazon Redshift.
      This accepts a value from 1 through 1,048,576. It defaults to 32,768 KB (32 MB).

    - **Password** *(string) --*

      The password for the user named in the ``username`` property.

    - **Port** *(integer) --*

      The port number for Amazon Redshift. The default value is 5439.

    - **RemoveQuotes** *(boolean) --*

      A value that specifies to remove surrounding quotation marks from strings in the
      incoming data. All characters within the quotation marks, including delimiters, are
      retained. Choose ``true`` to remove quotation marks. The default is ``false`` .

    - **ReplaceInvalidChars** *(string) --*

      A list of characters that you want to replace. Use with ``ReplaceChars`` .

    - **ReplaceChars** *(string) --*

      A value that specifies to replaces the invalid characters specified in
      ``ReplaceInvalidChars`` , substituting the specified characters instead. The default is
      ``"?"`` .

    - **ServerName** *(string) --*

      The name of the Amazon Redshift cluster you are using.

    - **ServiceAccessRoleArn** *(string) --*

      The Amazon Resource Name (ARN) of the IAM role that has access to the Amazon Redshift
      service.

    - **ServerSideEncryptionKmsKeyId** *(string) --*

      The AWS KMS key ID. If you are using ``SSE_KMS`` for the ``EncryptionMode`` , provide
      this key ID. The key that you use needs an attached policy that enables IAM user
      permissions and allows use of the key.

    - **TimeFormat** *(string) --*

      The time format that you want to use. Valid values are ``auto`` (case-sensitive),
      ``'timeformat_string'`` , ``'epochsecs'`` , or ``'epochmillisecs'`` . It defaults to
      10. Using ``auto`` recognizes most strings, even some that aren't supported when you
      use a time format string.

      If your date and time values use formats different from each other, set this parameter
      to ``auto`` .

    - **TrimBlanks** *(boolean) --*

      A value that specifies to remove the trailing white space characters from a VARCHAR
      string. This parameter applies only to columns with a VARCHAR data type. Choose
      ``true`` to remove unneeded white space. The default is ``false`` .

    - **TruncateColumns** *(boolean) --*

      A value that specifies to truncate data in columns to the appropriate number of
      characters, so that the data fits in the column. This parameter applies only to columns
      with a VARCHAR or CHAR data type, and rows with a size of 4 MB or less. Choose ``true``
      to truncate data. The default is ``false`` .

    - **Username** *(string) --*

      An Amazon Redshift user name for a registered user.

    - **WriteBufferSize** *(integer) --*

      The size of the write buffer to use in rows. Valid values range from 1 through 2,048.
      The default is 1,024. Use this setting to tune performance.
    """


_ClientDescribeEndpointsResponseEndpointsS3SettingsTypeDef = TypedDict(
    "_ClientDescribeEndpointsResponseEndpointsS3SettingsTypeDef",
    {
        "ServiceAccessRoleArn": str,
        "ExternalTableDefinition": str,
        "CsvRowDelimiter": str,
        "CsvDelimiter": str,
        "BucketFolder": str,
        "BucketName": str,
        "CompressionType": str,
        "EncryptionMode": str,
        "ServerSideEncryptionKmsKeyId": str,
        "DataFormat": str,
        "EncodingType": str,
        "DictPageSizeLimit": int,
        "RowGroupLength": int,
        "DataPageSize": int,
        "ParquetVersion": str,
        "EnableStatistics": bool,
        "IncludeOpForFullLoad": bool,
        "CdcInsertsOnly": bool,
        "TimestampColumnName": str,
        "ParquetTimestampInMillisecond": bool,
    },
    total=False,
)


class ClientDescribeEndpointsResponseEndpointsS3SettingsTypeDef(
    _ClientDescribeEndpointsResponseEndpointsS3SettingsTypeDef
):
    """
    Type definition for `ClientDescribeEndpointsResponseEndpoints` `S3Settings`

    The settings for the S3 target endpoint. For more information, see the ``S3Settings``
    structure.

    - **ServiceAccessRoleArn** *(string) --*

      The Amazon Resource Name (ARN) used by the service access IAM role.

    - **ExternalTableDefinition** *(string) --*

      The external table definition.

    - **CsvRowDelimiter** *(string) --*

      The delimiter used to separate rows in the source files. The default is a carriage
      return (``\\n`` ).

    - **CsvDelimiter** *(string) --*

      The delimiter used to separate columns in the source files. The default is a comma.

    - **BucketFolder** *(string) --*

      An optional parameter to set a folder name in the S3 bucket. If provided, tables are
      created in the path `` *bucketFolder* /*schema_name* /*table_name* /`` . If this
      parameter is not specified, then the path used is `` *schema_name* /*table_name* /`` .

    - **BucketName** *(string) --*

      The name of the S3 bucket.

    - **CompressionType** *(string) --*

      An optional parameter to use GZIP to compress the target files. Set to GZIP to compress
      the target files. Set to NONE (the default) or do not use to leave the files
      uncompressed. Applies to both .csv and .parquet file formats.

    - **EncryptionMode** *(string) --*

      The type of server-side encryption that you want to use for your data. This encryption
      type is part of the endpoint settings or the extra connections attributes for Amazon
      S3. You can choose either ``SSE_S3`` (the default) or ``SSE_KMS`` . To use ``SSE_S3`` ,
      you need an AWS Identity and Access Management (IAM) role with permission to allow
      ``"arn:aws:s3:::dms-*"`` to use the following actions:

      * ``s3:CreateBucket``

      * ``s3:ListBucket``

      * ``s3:DeleteBucket``

      * ``s3:GetBucketLocation``

      * ``s3:GetObject``

      * ``s3:PutObject``

      * ``s3:DeleteObject``

      * ``s3:GetObjectVersion``

      * ``s3:GetBucketPolicy``

      * ``s3:PutBucketPolicy``

      * ``s3:DeleteBucketPolicy``

    - **ServerSideEncryptionKmsKeyId** *(string) --*

      If you are using ``SSE_KMS`` for the ``EncryptionMode`` , provide the AWS KMS key ID.
      The key that you use needs an attached policy that enables AWS Identity and Access
      Management (IAM) user permissions and allows use of the key.

      Here is a CLI example: ``aws dms create-endpoint --endpoint-identifier *value*
      --endpoint-type target --engine-name s3 --s3-settings ServiceAccessRoleArn=*value*
      ,BucketFolder=*value* ,BucketName=*value*
      ,EncryptionMode=SSE_KMS,ServerSideEncryptionKmsKeyId=*value* ``

    - **DataFormat** *(string) --*

      The format of the data that you want to use for output. You can choose one of the
      following:

      * ``csv`` : This is a row-based file format with comma-separated values (.csv).

      * ``parquet`` : Apache Parquet (.parquet) is a columnar storage file format that
      features efficient compression and provides faster query response.

    - **EncodingType** *(string) --*

      The type of encoding you are using:

      * ``RLE_DICTIONARY`` uses a combination of bit-packing and run-length encoding to store
      repeated values more efficiently. This is the default.

      * ``PLAIN`` doesn't use encoding at all. Values are stored as they are.

      * ``PLAIN_DICTIONARY`` builds a dictionary of the values encountered in a given column.
      The dictionary is stored in a dictionary page for each column chunk.

    - **DictPageSizeLimit** *(integer) --*

      The maximum size of an encoded dictionary page of a column. If the dictionary page
      exceeds this, this column is stored using an encoding type of ``PLAIN`` . This
      parameter defaults to 1024 * 1024 bytes (1 MiB), the maximum size of a dictionary page
      before it reverts to ``PLAIN`` encoding. This size is used for .parquet file format
      only.

    - **RowGroupLength** *(integer) --*

      The number of rows in a row group. A smaller row group size provides faster reads. But
      as the number of row groups grows, the slower writes become. This parameter defaults to
      10,000 rows. This number is used for .parquet file format only.

      If you choose a value larger than the maximum, ``RowGroupLength`` is set to the max row
      group length in bytes (64 * 1024 * 1024).

    - **DataPageSize** *(integer) --*

      The size of one data page in bytes. This parameter defaults to 1024 * 1024 bytes (1
      MiB). This number is used for .parquet file format only.

    - **ParquetVersion** *(string) --*

      The version of the Apache Parquet format that you want to use: ``parquet_1_0`` (the
      default) or ``parquet_2_0`` .

    - **EnableStatistics** *(boolean) --*

      A value that enables statistics for Parquet pages and row groups. Choose ``true`` to
      enable statistics, ``false`` to disable. Statistics include ``NULL`` , ``DISTINCT`` ,
      ``MAX`` , and ``MIN`` values. This parameter defaults to ``true`` . This value is used
      for .parquet file format only.

    - **IncludeOpForFullLoad** *(boolean) --*

      A value that enables a full load to write INSERT operations to the comma-separated
      value (.csv) output files only to indicate how the rows were added to the source
      database.

      .. note::

        AWS DMS supports the ``IncludeOpForFullLoad`` parameter in versions 3.1.4 and later.

      For full load, records can only be inserted. By default (the ``false`` setting), no
      information is recorded in these output files for a full load to indicate that the rows
      were inserted at the source database. If ``IncludeOpForFullLoad`` is set to ``true`` or
      ``y`` , the INSERT is recorded as an I annotation in the first field of the .csv file.
      This allows the format of your target records from a full load to be consistent with
      the target records from a CDC load.

      .. note::

        This setting works together with the ``CdcInsertsOnly`` parameter for output to .csv
        files only. For more information about how these settings work together, see
        `Indicating Source DB Operations in Migrated S3 Data
        <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring.InsertOps>`__
        in the *AWS Database Migration Service User Guide.* .

    - **CdcInsertsOnly** *(boolean) --*

      A value that enables a change data capture (CDC) load to write only INSERT operations
      to .csv or columnar storage (.parquet) output files. By default (the ``false``
      setting), the first field in a .csv or .parquet record contains the letter I (INSERT),
      U (UPDATE), or D (DELETE). These values indicate whether the row was inserted, updated,
      or deleted at the source database for a CDC load to the target.

      If ``CdcInsertsOnly`` is set to ``true`` or ``y`` , only INSERTs from the source
      database are migrated to the .csv or .parquet file. For .csv format only, how these
      INSERTs are recorded depends on the value of ``IncludeOpForFullLoad`` . If
      ``IncludeOpForFullLoad`` is set to ``true`` , the first field of every CDC record is
      set to I to indicate the INSERT operation at the source. If ``IncludeOpForFullLoad`` is
      set to ``false`` , every CDC record is written without a first field to indicate the
      INSERT operation at the source. For more information about how these settings work
      together, see `Indicating Source DB Operations in Migrated S3 Data
      <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring.InsertOps>`__
      in the *AWS Database Migration Service User Guide.* .

      .. note::

        AWS DMS supports this interaction between the ``CdcInsertsOnly`` and
        ``IncludeOpForFullLoad`` parameters in versions 3.1.4 and later.

    - **TimestampColumnName** *(string) --*

      A value that when nonblank causes AWS DMS to add a column with timestamp information to
      the endpoint data for an Amazon S3 target.

      .. note::

        AWS DMS supports the ``TimestampColumnName`` parameter in versions 3.1.4 and later.

      DMS includes an additional ``STRING`` column in the .csv or .parquet object files of
      your migrated data when you set ``TimestampColumnName`` to a nonblank value.

      For a full load, each row of this timestamp column contains a timestamp for when the
      data was transferred from the source to the target by DMS.

      For a change data capture (CDC) load, each row of the timestamp column contains the
      timestamp for the commit of that row in the source database.

      The string format for this timestamp column value is ``yyyy-MM-dd HH:mm:ss.SSSSSS`` .
      By default, the precision of this value is in microseconds. For a CDC load, the
      rounding of the precision depends on the commit timestamp supported by DMS for the
      source database.

      When the ``AddColumnName`` parameter is set to ``true`` , DMS also includes a name for
      the timestamp column that you set with ``TimestampColumnName`` .

    - **ParquetTimestampInMillisecond** *(boolean) --*

      A value that specifies the precision of any ``TIMESTAMP`` column values that are
      written to an Amazon S3 object file in .parquet format.

      .. note::

        AWS DMS supports the ``ParquetTimestampInMillisecond`` parameter in versions 3.1.4
        and later.

      When ``ParquetTimestampInMillisecond`` is set to ``true`` or ``y`` , AWS DMS writes all
      ``TIMESTAMP`` columns in a .parquet formatted file with millisecond precision.
      Otherwise, DMS writes them with microsecond precision.

      Currently, Amazon Athena and AWS Glue can handle only millisecond precision for
      ``TIMESTAMP`` values. Set this parameter to ``true`` for S3 endpoint object files that
      are .parquet formatted only if you plan to query or process the data with Athena or AWS
      Glue.

      .. note::

        AWS DMS writes any ``TIMESTAMP`` column values written to an S3 file in .csv format
        with microsecond precision.

        Setting ``ParquetTimestampInMillisecond`` has no effect on the string format of the
        timestamp column value that is inserted by setting the ``TimestampColumnName``
        parameter.
    """


_ClientDescribeEndpointsResponseEndpointsTypeDef = TypedDict(
    "_ClientDescribeEndpointsResponseEndpointsTypeDef",
    {
        "EndpointIdentifier": str,
        "EndpointType": str,
        "EngineName": str,
        "EngineDisplayName": str,
        "Username": str,
        "ServerName": str,
        "Port": int,
        "DatabaseName": str,
        "ExtraConnectionAttributes": str,
        "Status": str,
        "KmsKeyId": str,
        "EndpointArn": str,
        "CertificateArn": str,
        "SslMode": str,
        "ServiceAccessRoleArn": str,
        "ExternalTableDefinition": str,
        "ExternalId": str,
        "DynamoDbSettings": ClientDescribeEndpointsResponseEndpointsDynamoDbSettingsTypeDef,
        "S3Settings": ClientDescribeEndpointsResponseEndpointsS3SettingsTypeDef,
        "DmsTransferSettings": ClientDescribeEndpointsResponseEndpointsDmsTransferSettingsTypeDef,
        "MongoDbSettings": ClientDescribeEndpointsResponseEndpointsMongoDbSettingsTypeDef,
        "KinesisSettings": ClientDescribeEndpointsResponseEndpointsKinesisSettingsTypeDef,
        "ElasticsearchSettings": ClientDescribeEndpointsResponseEndpointsElasticsearchSettingsTypeDef,
        "RedshiftSettings": ClientDescribeEndpointsResponseEndpointsRedshiftSettingsTypeDef,
    },
    total=False,
)


class ClientDescribeEndpointsResponseEndpointsTypeDef(
    _ClientDescribeEndpointsResponseEndpointsTypeDef
):
    """
    Type definition for `ClientDescribeEndpointsResponse` `Endpoints`

    - **EndpointIdentifier** *(string) --*

      The database endpoint identifier. Identifiers must begin with a letter; must contain only
      ASCII letters, digits, and hyphens; and must not end with a hyphen or contain two
      consecutive hyphens.

    - **EndpointType** *(string) --*

      The type of endpoint. Valid values are ``source`` and ``target`` .

    - **EngineName** *(string) --*

      The database engine name. Valid values, depending on the EndpointType, include mysql,
      oracle, postgres, mariadb, aurora, aurora-postgresql, redshift, s3, db2, azuredb, sybase,
      dynamodb, mongodb, and sqlserver.

    - **EngineDisplayName** *(string) --*

      The expanded name for the engine name. For example, if the ``EngineName`` parameter is
      "aurora," this value would be "Amazon Aurora MySQL."

    - **Username** *(string) --*

      The user name used to connect to the endpoint.

    - **ServerName** *(string) --*

      The name of the server at the endpoint.

    - **Port** *(integer) --*

      The port value used to access the endpoint.

    - **DatabaseName** *(string) --*

      The name of the database at the endpoint.

    - **ExtraConnectionAttributes** *(string) --*

      Additional connection attributes used to connect to the endpoint.

    - **Status** *(string) --*

      The status of the endpoint.

    - **KmsKeyId** *(string) --*

      An AWS KMS key identifier that is used to encrypt the connection parameters for the
      endpoint.

      If you don't specify a value for the ``KmsKeyId`` parameter, then AWS DMS uses your
      default encryption key.

      AWS KMS creates the default encryption key for your AWS account. Your AWS account has a
      different default encryption key for each AWS Region.

    - **EndpointArn** *(string) --*

      The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

    - **CertificateArn** *(string) --*

      The Amazon Resource Name (ARN) used for SSL connection to the endpoint.

    - **SslMode** *(string) --*

      The SSL mode used to connect to the endpoint. The default value is ``none`` .

    - **ServiceAccessRoleArn** *(string) --*

      The Amazon Resource Name (ARN) used by the service access IAM role.

    - **ExternalTableDefinition** *(string) --*

      The external table definition.

    - **ExternalId** *(string) --*

      Value returned by a call to CreateEndpoint that can be used for cross-account validation.
      Use it on a subsequent call to CreateEndpoint to create the endpoint with a cross-account.

    - **DynamoDbSettings** *(dict) --*

      The settings for the target DynamoDB database. For more information, see the
      ``DynamoDBSettings`` structure.

      - **ServiceAccessRoleArn** *(string) --*

        The Amazon Resource Name (ARN) used by the service access IAM role.

    - **S3Settings** *(dict) --*

      The settings for the S3 target endpoint. For more information, see the ``S3Settings``
      structure.

      - **ServiceAccessRoleArn** *(string) --*

        The Amazon Resource Name (ARN) used by the service access IAM role.

      - **ExternalTableDefinition** *(string) --*

        The external table definition.

      - **CsvRowDelimiter** *(string) --*

        The delimiter used to separate rows in the source files. The default is a carriage
        return (``\\n`` ).

      - **CsvDelimiter** *(string) --*

        The delimiter used to separate columns in the source files. The default is a comma.

      - **BucketFolder** *(string) --*

        An optional parameter to set a folder name in the S3 bucket. If provided, tables are
        created in the path `` *bucketFolder* /*schema_name* /*table_name* /`` . If this
        parameter is not specified, then the path used is `` *schema_name* /*table_name* /`` .

      - **BucketName** *(string) --*

        The name of the S3 bucket.

      - **CompressionType** *(string) --*

        An optional parameter to use GZIP to compress the target files. Set to GZIP to compress
        the target files. Set to NONE (the default) or do not use to leave the files
        uncompressed. Applies to both .csv and .parquet file formats.

      - **EncryptionMode** *(string) --*

        The type of server-side encryption that you want to use for your data. This encryption
        type is part of the endpoint settings or the extra connections attributes for Amazon
        S3. You can choose either ``SSE_S3`` (the default) or ``SSE_KMS`` . To use ``SSE_S3`` ,
        you need an AWS Identity and Access Management (IAM) role with permission to allow
        ``"arn:aws:s3:::dms-*"`` to use the following actions:

        * ``s3:CreateBucket``

        * ``s3:ListBucket``

        * ``s3:DeleteBucket``

        * ``s3:GetBucketLocation``

        * ``s3:GetObject``

        * ``s3:PutObject``

        * ``s3:DeleteObject``

        * ``s3:GetObjectVersion``

        * ``s3:GetBucketPolicy``

        * ``s3:PutBucketPolicy``

        * ``s3:DeleteBucketPolicy``

      - **ServerSideEncryptionKmsKeyId** *(string) --*

        If you are using ``SSE_KMS`` for the ``EncryptionMode`` , provide the AWS KMS key ID.
        The key that you use needs an attached policy that enables AWS Identity and Access
        Management (IAM) user permissions and allows use of the key.

        Here is a CLI example: ``aws dms create-endpoint --endpoint-identifier *value*
        --endpoint-type target --engine-name s3 --s3-settings ServiceAccessRoleArn=*value*
        ,BucketFolder=*value* ,BucketName=*value*
        ,EncryptionMode=SSE_KMS,ServerSideEncryptionKmsKeyId=*value* ``

      - **DataFormat** *(string) --*

        The format of the data that you want to use for output. You can choose one of the
        following:

        * ``csv`` : This is a row-based file format with comma-separated values (.csv).

        * ``parquet`` : Apache Parquet (.parquet) is a columnar storage file format that
        features efficient compression and provides faster query response.

      - **EncodingType** *(string) --*

        The type of encoding you are using:

        * ``RLE_DICTIONARY`` uses a combination of bit-packing and run-length encoding to store
        repeated values more efficiently. This is the default.

        * ``PLAIN`` doesn't use encoding at all. Values are stored as they are.

        * ``PLAIN_DICTIONARY`` builds a dictionary of the values encountered in a given column.
        The dictionary is stored in a dictionary page for each column chunk.

      - **DictPageSizeLimit** *(integer) --*

        The maximum size of an encoded dictionary page of a column. If the dictionary page
        exceeds this, this column is stored using an encoding type of ``PLAIN`` . This
        parameter defaults to 1024 * 1024 bytes (1 MiB), the maximum size of a dictionary page
        before it reverts to ``PLAIN`` encoding. This size is used for .parquet file format
        only.

      - **RowGroupLength** *(integer) --*

        The number of rows in a row group. A smaller row group size provides faster reads. But
        as the number of row groups grows, the slower writes become. This parameter defaults to
        10,000 rows. This number is used for .parquet file format only.

        If you choose a value larger than the maximum, ``RowGroupLength`` is set to the max row
        group length in bytes (64 * 1024 * 1024).

      - **DataPageSize** *(integer) --*

        The size of one data page in bytes. This parameter defaults to 1024 * 1024 bytes (1
        MiB). This number is used for .parquet file format only.

      - **ParquetVersion** *(string) --*

        The version of the Apache Parquet format that you want to use: ``parquet_1_0`` (the
        default) or ``parquet_2_0`` .

      - **EnableStatistics** *(boolean) --*

        A value that enables statistics for Parquet pages and row groups. Choose ``true`` to
        enable statistics, ``false`` to disable. Statistics include ``NULL`` , ``DISTINCT`` ,
        ``MAX`` , and ``MIN`` values. This parameter defaults to ``true`` . This value is used
        for .parquet file format only.

      - **IncludeOpForFullLoad** *(boolean) --*

        A value that enables a full load to write INSERT operations to the comma-separated
        value (.csv) output files only to indicate how the rows were added to the source
        database.

        .. note::

          AWS DMS supports the ``IncludeOpForFullLoad`` parameter in versions 3.1.4 and later.

        For full load, records can only be inserted. By default (the ``false`` setting), no
        information is recorded in these output files for a full load to indicate that the rows
        were inserted at the source database. If ``IncludeOpForFullLoad`` is set to ``true`` or
        ``y`` , the INSERT is recorded as an I annotation in the first field of the .csv file.
        This allows the format of your target records from a full load to be consistent with
        the target records from a CDC load.

        .. note::

          This setting works together with the ``CdcInsertsOnly`` parameter for output to .csv
          files only. For more information about how these settings work together, see
          `Indicating Source DB Operations in Migrated S3 Data
          <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring.InsertOps>`__
          in the *AWS Database Migration Service User Guide.* .

      - **CdcInsertsOnly** *(boolean) --*

        A value that enables a change data capture (CDC) load to write only INSERT operations
        to .csv or columnar storage (.parquet) output files. By default (the ``false``
        setting), the first field in a .csv or .parquet record contains the letter I (INSERT),
        U (UPDATE), or D (DELETE). These values indicate whether the row was inserted, updated,
        or deleted at the source database for a CDC load to the target.

        If ``CdcInsertsOnly`` is set to ``true`` or ``y`` , only INSERTs from the source
        database are migrated to the .csv or .parquet file. For .csv format only, how these
        INSERTs are recorded depends on the value of ``IncludeOpForFullLoad`` . If
        ``IncludeOpForFullLoad`` is set to ``true`` , the first field of every CDC record is
        set to I to indicate the INSERT operation at the source. If ``IncludeOpForFullLoad`` is
        set to ``false`` , every CDC record is written without a first field to indicate the
        INSERT operation at the source. For more information about how these settings work
        together, see `Indicating Source DB Operations in Migrated S3 Data
        <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring.InsertOps>`__
        in the *AWS Database Migration Service User Guide.* .

        .. note::

          AWS DMS supports this interaction between the ``CdcInsertsOnly`` and
          ``IncludeOpForFullLoad`` parameters in versions 3.1.4 and later.

      - **TimestampColumnName** *(string) --*

        A value that when nonblank causes AWS DMS to add a column with timestamp information to
        the endpoint data for an Amazon S3 target.

        .. note::

          AWS DMS supports the ``TimestampColumnName`` parameter in versions 3.1.4 and later.

        DMS includes an additional ``STRING`` column in the .csv or .parquet object files of
        your migrated data when you set ``TimestampColumnName`` to a nonblank value.

        For a full load, each row of this timestamp column contains a timestamp for when the
        data was transferred from the source to the target by DMS.

        For a change data capture (CDC) load, each row of the timestamp column contains the
        timestamp for the commit of that row in the source database.

        The string format for this timestamp column value is ``yyyy-MM-dd HH:mm:ss.SSSSSS`` .
        By default, the precision of this value is in microseconds. For a CDC load, the
        rounding of the precision depends on the commit timestamp supported by DMS for the
        source database.

        When the ``AddColumnName`` parameter is set to ``true`` , DMS also includes a name for
        the timestamp column that you set with ``TimestampColumnName`` .

      - **ParquetTimestampInMillisecond** *(boolean) --*

        A value that specifies the precision of any ``TIMESTAMP`` column values that are
        written to an Amazon S3 object file in .parquet format.

        .. note::

          AWS DMS supports the ``ParquetTimestampInMillisecond`` parameter in versions 3.1.4
          and later.

        When ``ParquetTimestampInMillisecond`` is set to ``true`` or ``y`` , AWS DMS writes all
        ``TIMESTAMP`` columns in a .parquet formatted file with millisecond precision.
        Otherwise, DMS writes them with microsecond precision.

        Currently, Amazon Athena and AWS Glue can handle only millisecond precision for
        ``TIMESTAMP`` values. Set this parameter to ``true`` for S3 endpoint object files that
        are .parquet formatted only if you plan to query or process the data with Athena or AWS
        Glue.

        .. note::

          AWS DMS writes any ``TIMESTAMP`` column values written to an S3 file in .csv format
          with microsecond precision.

          Setting ``ParquetTimestampInMillisecond`` has no effect on the string format of the
          timestamp column value that is inserted by setting the ``TimestampColumnName``
          parameter.

    - **DmsTransferSettings** *(dict) --*

      The settings in JSON format for the DMS transfer type of source endpoint.

      Possible settings include the following:

      * ``ServiceAccessRoleArn`` - The IAM role that has permission to access the Amazon S3
      bucket.

      * ``BucketName`` - The name of the S3 bucket to use.

      * ``CompressionType`` - An optional parameter to use GZIP to compress the target files.
      To use GZIP, set this value to ``NONE`` (the default). To keep the files uncompressed,
      don't use this value.

      Shorthand syntax for these settings is as follows:
      ``ServiceAccessRoleArn=string,BucketName=string,CompressionType=string``

      JSON syntax for these settings is as follows: ``{ "ServiceAccessRoleArn": "string",
      "BucketName": "string", "CompressionType": "none"|"gzip" }``

      - **ServiceAccessRoleArn** *(string) --*

        The IAM role that has permission to access the Amazon S3 bucket.

      - **BucketName** *(string) --*

        The name of the S3 bucket to use.

    - **MongoDbSettings** *(dict) --*

      The settings for the MongoDB source endpoint. For more information, see the
      ``MongoDbSettings`` structure.

      - **Username** *(string) --*

        The user name you use to access the MongoDB source endpoint.

      - **Password** *(string) --*

        The password for the user account you use to access the MongoDB source endpoint.

      - **ServerName** *(string) --*

        The name of the server on the MongoDB source endpoint.

      - **Port** *(integer) --*

        The port value for the MongoDB source endpoint.

      - **DatabaseName** *(string) --*

        The database name on the MongoDB source endpoint.

      - **AuthType** *(string) --*

        The authentication type you use to access the MongoDB source endpoint.

        Valid values: NO, PASSWORD

        When NO is selected, user name and password parameters are not used and can be empty.

      - **AuthMechanism** *(string) --*

        The authentication mechanism you use to access the MongoDB source endpoint.

        Valid values: DEFAULT, MONGODB_CR, SCRAM_SHA_1

        DEFAULT – For MongoDB version 2.x, use MONGODB_CR. For MongoDB version 3.x, use
        SCRAM_SHA_1. This setting is not used when authType=No.

      - **NestingLevel** *(string) --*

        Specifies either document or table mode.

        Valid values: NONE, ONE

        Default value is NONE. Specify NONE to use document mode. Specify ONE to use table mode.

      - **ExtractDocId** *(string) --*

        Specifies the document ID. Use this setting when ``NestingLevel`` is set to NONE.

        Default value is false.

      - **DocsToInvestigate** *(string) --*

        Indicates the number of documents to preview to determine the document organization.
        Use this setting when ``NestingLevel`` is set to ONE.

        Must be a positive value greater than 0. Default value is 1000.

      - **AuthSource** *(string) --*

        The MongoDB database name. This setting is not used when ``authType=NO`` .

        The default is admin.

      - **KmsKeyId** *(string) --*

        The AWS KMS key identifier that is used to encrypt the content on the replication
        instance. If you don't specify a value for the ``KmsKeyId`` parameter, then AWS DMS
        uses your default encryption key. AWS KMS creates the default encryption key for your
        AWS account. Your AWS account has a different default encryption key for each AWS
        Region.

    - **KinesisSettings** *(dict) --*

      The settings for the Amazon Kinesis source endpoint. For more information, see the
      ``KinesisSettings`` structure.

      - **StreamArn** *(string) --*

        The Amazon Resource Name (ARN) for the Amazon Kinesis Data Streams endpoint.

      - **MessageFormat** *(string) --*

        The output format for the records created on the endpoint. The message format is
        ``JSON`` .

      - **ServiceAccessRoleArn** *(string) --*

        The Amazon Resource Name (ARN) for the IAM role that DMS uses to write to the Amazon
        Kinesis data stream.

    - **ElasticsearchSettings** *(dict) --*

      The settings for the Elasticsearch source endpoint. For more information, see the
      ``ElasticsearchSettings`` structure.

      - **ServiceAccessRoleArn** *(string) --*

        The Amazon Resource Name (ARN) used by service to access the IAM role.

      - **EndpointUri** *(string) --*

        The endpoint for the Elasticsearch cluster.

      - **FullLoadErrorPercentage** *(integer) --*

        The maximum percentage of records that can fail to be written before a full load
        operation stops.

      - **ErrorRetryDuration** *(integer) --*

        The maximum number of seconds that DMS retries failed API requests to the Elasticsearch
        cluster.

    - **RedshiftSettings** *(dict) --*

      Settings for the Amazon Redshift endpoint.

      - **AcceptAnyDate** *(boolean) --*

        A value that indicates to allow any date format, including invalid formats such as
        00/00/00 00:00:00, to be loaded without generating an error. You can choose ``true`` or
        ``false`` (the default).

        This parameter applies only to TIMESTAMP and DATE columns. Always use ACCEPTANYDATE
        with the DATEFORMAT parameter. If the date format for the data doesn't match the
        DATEFORMAT specification, Amazon Redshift inserts a NULL value into that field.

      - **AfterConnectScript** *(string) --*

        Code to run after connecting. This parameter should contain the code itself, not the
        name of a file containing the code.

      - **BucketFolder** *(string) --*

        The location where the comma-separated value (.csv) files are stored before being
        uploaded to the S3 bucket.

      - **BucketName** *(string) --*

        The name of the S3 bucket you want to use

      - **ConnectionTimeout** *(integer) --*

        A value that sets the amount of time to wait (in milliseconds) before timing out,
        beginning from when you initially establish a connection.

      - **DatabaseName** *(string) --*

        The name of the Amazon Redshift data warehouse (service) that you are working with.

      - **DateFormat** *(string) --*

        The date format that you are using. Valid values are ``auto`` (case-sensitive), your
        date format string enclosed in quotes, or NULL. If this parameter is left unset (NULL),
        it defaults to a format of 'YYYY-MM-DD'. Using ``auto`` recognizes most strings, even
        some that aren't supported when you use a date format string.

        If your date and time values use formats different from each other, set this to
        ``auto`` .

      - **EmptyAsNull** *(boolean) --*

        A value that specifies whether AWS DMS should migrate empty CHAR and VARCHAR fields as
        NULL. A value of ``true`` sets empty CHAR and VARCHAR fields to null. The default is
        ``false`` .

      - **EncryptionMode** *(string) --*

        The type of server-side encryption that you want to use for your data. This encryption
        type is part of the endpoint settings or the extra connections attributes for Amazon
        S3. You can choose either ``SSE_S3`` (the default) or ``SSE_KMS`` . To use ``SSE_S3`` ,
        create an AWS Identity and Access Management (IAM) role with a policy that allows
        ``"arn:aws:s3:::*"`` to use the following actions: ``"s3:PutObject", "s3:ListBucket"``

      - **FileTransferUploadStreams** *(integer) --*

        The number of threads used to upload a single file. This parameter accepts a value from
        1 through 64. It defaults to 10.

      - **LoadTimeout** *(integer) --*

        The amount of time to wait (in milliseconds) before timing out, beginning from when you
        begin loading.

      - **MaxFileSize** *(integer) --*

        The maximum size (in KB) of any .csv file used to transfer data to Amazon Redshift.
        This accepts a value from 1 through 1,048,576. It defaults to 32,768 KB (32 MB).

      - **Password** *(string) --*

        The password for the user named in the ``username`` property.

      - **Port** *(integer) --*

        The port number for Amazon Redshift. The default value is 5439.

      - **RemoveQuotes** *(boolean) --*

        A value that specifies to remove surrounding quotation marks from strings in the
        incoming data. All characters within the quotation marks, including delimiters, are
        retained. Choose ``true`` to remove quotation marks. The default is ``false`` .

      - **ReplaceInvalidChars** *(string) --*

        A list of characters that you want to replace. Use with ``ReplaceChars`` .

      - **ReplaceChars** *(string) --*

        A value that specifies to replaces the invalid characters specified in
        ``ReplaceInvalidChars`` , substituting the specified characters instead. The default is
        ``"?"`` .

      - **ServerName** *(string) --*

        The name of the Amazon Redshift cluster you are using.

      - **ServiceAccessRoleArn** *(string) --*

        The Amazon Resource Name (ARN) of the IAM role that has access to the Amazon Redshift
        service.

      - **ServerSideEncryptionKmsKeyId** *(string) --*

        The AWS KMS key ID. If you are using ``SSE_KMS`` for the ``EncryptionMode`` , provide
        this key ID. The key that you use needs an attached policy that enables IAM user
        permissions and allows use of the key.

      - **TimeFormat** *(string) --*

        The time format that you want to use. Valid values are ``auto`` (case-sensitive),
        ``'timeformat_string'`` , ``'epochsecs'`` , or ``'epochmillisecs'`` . It defaults to
        10. Using ``auto`` recognizes most strings, even some that aren't supported when you
        use a time format string.

        If your date and time values use formats different from each other, set this parameter
        to ``auto`` .

      - **TrimBlanks** *(boolean) --*

        A value that specifies to remove the trailing white space characters from a VARCHAR
        string. This parameter applies only to columns with a VARCHAR data type. Choose
        ``true`` to remove unneeded white space. The default is ``false`` .

      - **TruncateColumns** *(boolean) --*

        A value that specifies to truncate data in columns to the appropriate number of
        characters, so that the data fits in the column. This parameter applies only to columns
        with a VARCHAR or CHAR data type, and rows with a size of 4 MB or less. Choose ``true``
        to truncate data. The default is ``false`` .

      - **Username** *(string) --*

        An Amazon Redshift user name for a registered user.

      - **WriteBufferSize** *(integer) --*

        The size of the write buffer to use in rows. Valid values range from 1 through 2,048.
        The default is 1,024. Use this setting to tune performance.
    """


_ClientDescribeEndpointsResponseTypeDef = TypedDict(
    "_ClientDescribeEndpointsResponseTypeDef",
    {"Marker": str, "Endpoints": List[ClientDescribeEndpointsResponseEndpointsTypeDef]},
    total=False,
)


class ClientDescribeEndpointsResponseTypeDef(_ClientDescribeEndpointsResponseTypeDef):
    """
    Type definition for `ClientDescribeEndpoints` `Response`

    - **Marker** *(string) --*

      An optional pagination token provided by a previous request. If this parameter is specified,
      the response includes only records beyond the marker, up to the value specified by
      ``MaxRecords`` .

    - **Endpoints** *(list) --*

      Endpoint description.

      - *(dict) --*

        - **EndpointIdentifier** *(string) --*

          The database endpoint identifier. Identifiers must begin with a letter; must contain only
          ASCII letters, digits, and hyphens; and must not end with a hyphen or contain two
          consecutive hyphens.

        - **EndpointType** *(string) --*

          The type of endpoint. Valid values are ``source`` and ``target`` .

        - **EngineName** *(string) --*

          The database engine name. Valid values, depending on the EndpointType, include mysql,
          oracle, postgres, mariadb, aurora, aurora-postgresql, redshift, s3, db2, azuredb, sybase,
          dynamodb, mongodb, and sqlserver.

        - **EngineDisplayName** *(string) --*

          The expanded name for the engine name. For example, if the ``EngineName`` parameter is
          "aurora," this value would be "Amazon Aurora MySQL."

        - **Username** *(string) --*

          The user name used to connect to the endpoint.

        - **ServerName** *(string) --*

          The name of the server at the endpoint.

        - **Port** *(integer) --*

          The port value used to access the endpoint.

        - **DatabaseName** *(string) --*

          The name of the database at the endpoint.

        - **ExtraConnectionAttributes** *(string) --*

          Additional connection attributes used to connect to the endpoint.

        - **Status** *(string) --*

          The status of the endpoint.

        - **KmsKeyId** *(string) --*

          An AWS KMS key identifier that is used to encrypt the connection parameters for the
          endpoint.

          If you don't specify a value for the ``KmsKeyId`` parameter, then AWS DMS uses your
          default encryption key.

          AWS KMS creates the default encryption key for your AWS account. Your AWS account has a
          different default encryption key for each AWS Region.

        - **EndpointArn** *(string) --*

          The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

        - **CertificateArn** *(string) --*

          The Amazon Resource Name (ARN) used for SSL connection to the endpoint.

        - **SslMode** *(string) --*

          The SSL mode used to connect to the endpoint. The default value is ``none`` .

        - **ServiceAccessRoleArn** *(string) --*

          The Amazon Resource Name (ARN) used by the service access IAM role.

        - **ExternalTableDefinition** *(string) --*

          The external table definition.

        - **ExternalId** *(string) --*

          Value returned by a call to CreateEndpoint that can be used for cross-account validation.
          Use it on a subsequent call to CreateEndpoint to create the endpoint with a cross-account.

        - **DynamoDbSettings** *(dict) --*

          The settings for the target DynamoDB database. For more information, see the
          ``DynamoDBSettings`` structure.

          - **ServiceAccessRoleArn** *(string) --*

            The Amazon Resource Name (ARN) used by the service access IAM role.

        - **S3Settings** *(dict) --*

          The settings for the S3 target endpoint. For more information, see the ``S3Settings``
          structure.

          - **ServiceAccessRoleArn** *(string) --*

            The Amazon Resource Name (ARN) used by the service access IAM role.

          - **ExternalTableDefinition** *(string) --*

            The external table definition.

          - **CsvRowDelimiter** *(string) --*

            The delimiter used to separate rows in the source files. The default is a carriage
            return (``\\n`` ).

          - **CsvDelimiter** *(string) --*

            The delimiter used to separate columns in the source files. The default is a comma.

          - **BucketFolder** *(string) --*

            An optional parameter to set a folder name in the S3 bucket. If provided, tables are
            created in the path `` *bucketFolder* /*schema_name* /*table_name* /`` . If this
            parameter is not specified, then the path used is `` *schema_name* /*table_name* /`` .

          - **BucketName** *(string) --*

            The name of the S3 bucket.

          - **CompressionType** *(string) --*

            An optional parameter to use GZIP to compress the target files. Set to GZIP to compress
            the target files. Set to NONE (the default) or do not use to leave the files
            uncompressed. Applies to both .csv and .parquet file formats.

          - **EncryptionMode** *(string) --*

            The type of server-side encryption that you want to use for your data. This encryption
            type is part of the endpoint settings or the extra connections attributes for Amazon
            S3. You can choose either ``SSE_S3`` (the default) or ``SSE_KMS`` . To use ``SSE_S3`` ,
            you need an AWS Identity and Access Management (IAM) role with permission to allow
            ``"arn:aws:s3:::dms-*"`` to use the following actions:

            * ``s3:CreateBucket``

            * ``s3:ListBucket``

            * ``s3:DeleteBucket``

            * ``s3:GetBucketLocation``

            * ``s3:GetObject``

            * ``s3:PutObject``

            * ``s3:DeleteObject``

            * ``s3:GetObjectVersion``

            * ``s3:GetBucketPolicy``

            * ``s3:PutBucketPolicy``

            * ``s3:DeleteBucketPolicy``

          - **ServerSideEncryptionKmsKeyId** *(string) --*

            If you are using ``SSE_KMS`` for the ``EncryptionMode`` , provide the AWS KMS key ID.
            The key that you use needs an attached policy that enables AWS Identity and Access
            Management (IAM) user permissions and allows use of the key.

            Here is a CLI example: ``aws dms create-endpoint --endpoint-identifier *value*
            --endpoint-type target --engine-name s3 --s3-settings ServiceAccessRoleArn=*value*
            ,BucketFolder=*value* ,BucketName=*value*
            ,EncryptionMode=SSE_KMS,ServerSideEncryptionKmsKeyId=*value* ``

          - **DataFormat** *(string) --*

            The format of the data that you want to use for output. You can choose one of the
            following:

            * ``csv`` : This is a row-based file format with comma-separated values (.csv).

            * ``parquet`` : Apache Parquet (.parquet) is a columnar storage file format that
            features efficient compression and provides faster query response.

          - **EncodingType** *(string) --*

            The type of encoding you are using:

            * ``RLE_DICTIONARY`` uses a combination of bit-packing and run-length encoding to store
            repeated values more efficiently. This is the default.

            * ``PLAIN`` doesn't use encoding at all. Values are stored as they are.

            * ``PLAIN_DICTIONARY`` builds a dictionary of the values encountered in a given column.
            The dictionary is stored in a dictionary page for each column chunk.

          - **DictPageSizeLimit** *(integer) --*

            The maximum size of an encoded dictionary page of a column. If the dictionary page
            exceeds this, this column is stored using an encoding type of ``PLAIN`` . This
            parameter defaults to 1024 * 1024 bytes (1 MiB), the maximum size of a dictionary page
            before it reverts to ``PLAIN`` encoding. This size is used for .parquet file format
            only.

          - **RowGroupLength** *(integer) --*

            The number of rows in a row group. A smaller row group size provides faster reads. But
            as the number of row groups grows, the slower writes become. This parameter defaults to
            10,000 rows. This number is used for .parquet file format only.

            If you choose a value larger than the maximum, ``RowGroupLength`` is set to the max row
            group length in bytes (64 * 1024 * 1024).

          - **DataPageSize** *(integer) --*

            The size of one data page in bytes. This parameter defaults to 1024 * 1024 bytes (1
            MiB). This number is used for .parquet file format only.

          - **ParquetVersion** *(string) --*

            The version of the Apache Parquet format that you want to use: ``parquet_1_0`` (the
            default) or ``parquet_2_0`` .

          - **EnableStatistics** *(boolean) --*

            A value that enables statistics for Parquet pages and row groups. Choose ``true`` to
            enable statistics, ``false`` to disable. Statistics include ``NULL`` , ``DISTINCT`` ,
            ``MAX`` , and ``MIN`` values. This parameter defaults to ``true`` . This value is used
            for .parquet file format only.

          - **IncludeOpForFullLoad** *(boolean) --*

            A value that enables a full load to write INSERT operations to the comma-separated
            value (.csv) output files only to indicate how the rows were added to the source
            database.

            .. note::

              AWS DMS supports the ``IncludeOpForFullLoad`` parameter in versions 3.1.4 and later.

            For full load, records can only be inserted. By default (the ``false`` setting), no
            information is recorded in these output files for a full load to indicate that the rows
            were inserted at the source database. If ``IncludeOpForFullLoad`` is set to ``true`` or
            ``y`` , the INSERT is recorded as an I annotation in the first field of the .csv file.
            This allows the format of your target records from a full load to be consistent with
            the target records from a CDC load.

            .. note::

              This setting works together with the ``CdcInsertsOnly`` parameter for output to .csv
              files only. For more information about how these settings work together, see
              `Indicating Source DB Operations in Migrated S3 Data
              <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring.InsertOps>`__
              in the *AWS Database Migration Service User Guide.* .

          - **CdcInsertsOnly** *(boolean) --*

            A value that enables a change data capture (CDC) load to write only INSERT operations
            to .csv or columnar storage (.parquet) output files. By default (the ``false``
            setting), the first field in a .csv or .parquet record contains the letter I (INSERT),
            U (UPDATE), or D (DELETE). These values indicate whether the row was inserted, updated,
            or deleted at the source database for a CDC load to the target.

            If ``CdcInsertsOnly`` is set to ``true`` or ``y`` , only INSERTs from the source
            database are migrated to the .csv or .parquet file. For .csv format only, how these
            INSERTs are recorded depends on the value of ``IncludeOpForFullLoad`` . If
            ``IncludeOpForFullLoad`` is set to ``true`` , the first field of every CDC record is
            set to I to indicate the INSERT operation at the source. If ``IncludeOpForFullLoad`` is
            set to ``false`` , every CDC record is written without a first field to indicate the
            INSERT operation at the source. For more information about how these settings work
            together, see `Indicating Source DB Operations in Migrated S3 Data
            <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring.InsertOps>`__
            in the *AWS Database Migration Service User Guide.* .

            .. note::

              AWS DMS supports this interaction between the ``CdcInsertsOnly`` and
              ``IncludeOpForFullLoad`` parameters in versions 3.1.4 and later.

          - **TimestampColumnName** *(string) --*

            A value that when nonblank causes AWS DMS to add a column with timestamp information to
            the endpoint data for an Amazon S3 target.

            .. note::

              AWS DMS supports the ``TimestampColumnName`` parameter in versions 3.1.4 and later.

            DMS includes an additional ``STRING`` column in the .csv or .parquet object files of
            your migrated data when you set ``TimestampColumnName`` to a nonblank value.

            For a full load, each row of this timestamp column contains a timestamp for when the
            data was transferred from the source to the target by DMS.

            For a change data capture (CDC) load, each row of the timestamp column contains the
            timestamp for the commit of that row in the source database.

            The string format for this timestamp column value is ``yyyy-MM-dd HH:mm:ss.SSSSSS`` .
            By default, the precision of this value is in microseconds. For a CDC load, the
            rounding of the precision depends on the commit timestamp supported by DMS for the
            source database.

            When the ``AddColumnName`` parameter is set to ``true`` , DMS also includes a name for
            the timestamp column that you set with ``TimestampColumnName`` .

          - **ParquetTimestampInMillisecond** *(boolean) --*

            A value that specifies the precision of any ``TIMESTAMP`` column values that are
            written to an Amazon S3 object file in .parquet format.

            .. note::

              AWS DMS supports the ``ParquetTimestampInMillisecond`` parameter in versions 3.1.4
              and later.

            When ``ParquetTimestampInMillisecond`` is set to ``true`` or ``y`` , AWS DMS writes all
            ``TIMESTAMP`` columns in a .parquet formatted file with millisecond precision.
            Otherwise, DMS writes them with microsecond precision.

            Currently, Amazon Athena and AWS Glue can handle only millisecond precision for
            ``TIMESTAMP`` values. Set this parameter to ``true`` for S3 endpoint object files that
            are .parquet formatted only if you plan to query or process the data with Athena or AWS
            Glue.

            .. note::

              AWS DMS writes any ``TIMESTAMP`` column values written to an S3 file in .csv format
              with microsecond precision.

              Setting ``ParquetTimestampInMillisecond`` has no effect on the string format of the
              timestamp column value that is inserted by setting the ``TimestampColumnName``
              parameter.

        - **DmsTransferSettings** *(dict) --*

          The settings in JSON format for the DMS transfer type of source endpoint.

          Possible settings include the following:

          * ``ServiceAccessRoleArn`` - The IAM role that has permission to access the Amazon S3
          bucket.

          * ``BucketName`` - The name of the S3 bucket to use.

          * ``CompressionType`` - An optional parameter to use GZIP to compress the target files.
          To use GZIP, set this value to ``NONE`` (the default). To keep the files uncompressed,
          don't use this value.

          Shorthand syntax for these settings is as follows:
          ``ServiceAccessRoleArn=string,BucketName=string,CompressionType=string``

          JSON syntax for these settings is as follows: ``{ "ServiceAccessRoleArn": "string",
          "BucketName": "string", "CompressionType": "none"|"gzip" }``

          - **ServiceAccessRoleArn** *(string) --*

            The IAM role that has permission to access the Amazon S3 bucket.

          - **BucketName** *(string) --*

            The name of the S3 bucket to use.

        - **MongoDbSettings** *(dict) --*

          The settings for the MongoDB source endpoint. For more information, see the
          ``MongoDbSettings`` structure.

          - **Username** *(string) --*

            The user name you use to access the MongoDB source endpoint.

          - **Password** *(string) --*

            The password for the user account you use to access the MongoDB source endpoint.

          - **ServerName** *(string) --*

            The name of the server on the MongoDB source endpoint.

          - **Port** *(integer) --*

            The port value for the MongoDB source endpoint.

          - **DatabaseName** *(string) --*

            The database name on the MongoDB source endpoint.

          - **AuthType** *(string) --*

            The authentication type you use to access the MongoDB source endpoint.

            Valid values: NO, PASSWORD

            When NO is selected, user name and password parameters are not used and can be empty.

          - **AuthMechanism** *(string) --*

            The authentication mechanism you use to access the MongoDB source endpoint.

            Valid values: DEFAULT, MONGODB_CR, SCRAM_SHA_1

            DEFAULT – For MongoDB version 2.x, use MONGODB_CR. For MongoDB version 3.x, use
            SCRAM_SHA_1. This setting is not used when authType=No.

          - **NestingLevel** *(string) --*

            Specifies either document or table mode.

            Valid values: NONE, ONE

            Default value is NONE. Specify NONE to use document mode. Specify ONE to use table mode.

          - **ExtractDocId** *(string) --*

            Specifies the document ID. Use this setting when ``NestingLevel`` is set to NONE.

            Default value is false.

          - **DocsToInvestigate** *(string) --*

            Indicates the number of documents to preview to determine the document organization.
            Use this setting when ``NestingLevel`` is set to ONE.

            Must be a positive value greater than 0. Default value is 1000.

          - **AuthSource** *(string) --*

            The MongoDB database name. This setting is not used when ``authType=NO`` .

            The default is admin.

          - **KmsKeyId** *(string) --*

            The AWS KMS key identifier that is used to encrypt the content on the replication
            instance. If you don't specify a value for the ``KmsKeyId`` parameter, then AWS DMS
            uses your default encryption key. AWS KMS creates the default encryption key for your
            AWS account. Your AWS account has a different default encryption key for each AWS
            Region.

        - **KinesisSettings** *(dict) --*

          The settings for the Amazon Kinesis source endpoint. For more information, see the
          ``KinesisSettings`` structure.

          - **StreamArn** *(string) --*

            The Amazon Resource Name (ARN) for the Amazon Kinesis Data Streams endpoint.

          - **MessageFormat** *(string) --*

            The output format for the records created on the endpoint. The message format is
            ``JSON`` .

          - **ServiceAccessRoleArn** *(string) --*

            The Amazon Resource Name (ARN) for the IAM role that DMS uses to write to the Amazon
            Kinesis data stream.

        - **ElasticsearchSettings** *(dict) --*

          The settings for the Elasticsearch source endpoint. For more information, see the
          ``ElasticsearchSettings`` structure.

          - **ServiceAccessRoleArn** *(string) --*

            The Amazon Resource Name (ARN) used by service to access the IAM role.

          - **EndpointUri** *(string) --*

            The endpoint for the Elasticsearch cluster.

          - **FullLoadErrorPercentage** *(integer) --*

            The maximum percentage of records that can fail to be written before a full load
            operation stops.

          - **ErrorRetryDuration** *(integer) --*

            The maximum number of seconds that DMS retries failed API requests to the Elasticsearch
            cluster.

        - **RedshiftSettings** *(dict) --*

          Settings for the Amazon Redshift endpoint.

          - **AcceptAnyDate** *(boolean) --*

            A value that indicates to allow any date format, including invalid formats such as
            00/00/00 00:00:00, to be loaded without generating an error. You can choose ``true`` or
            ``false`` (the default).

            This parameter applies only to TIMESTAMP and DATE columns. Always use ACCEPTANYDATE
            with the DATEFORMAT parameter. If the date format for the data doesn't match the
            DATEFORMAT specification, Amazon Redshift inserts a NULL value into that field.

          - **AfterConnectScript** *(string) --*

            Code to run after connecting. This parameter should contain the code itself, not the
            name of a file containing the code.

          - **BucketFolder** *(string) --*

            The location where the comma-separated value (.csv) files are stored before being
            uploaded to the S3 bucket.

          - **BucketName** *(string) --*

            The name of the S3 bucket you want to use

          - **ConnectionTimeout** *(integer) --*

            A value that sets the amount of time to wait (in milliseconds) before timing out,
            beginning from when you initially establish a connection.

          - **DatabaseName** *(string) --*

            The name of the Amazon Redshift data warehouse (service) that you are working with.

          - **DateFormat** *(string) --*

            The date format that you are using. Valid values are ``auto`` (case-sensitive), your
            date format string enclosed in quotes, or NULL. If this parameter is left unset (NULL),
            it defaults to a format of 'YYYY-MM-DD'. Using ``auto`` recognizes most strings, even
            some that aren't supported when you use a date format string.

            If your date and time values use formats different from each other, set this to
            ``auto`` .

          - **EmptyAsNull** *(boolean) --*

            A value that specifies whether AWS DMS should migrate empty CHAR and VARCHAR fields as
            NULL. A value of ``true`` sets empty CHAR and VARCHAR fields to null. The default is
            ``false`` .

          - **EncryptionMode** *(string) --*

            The type of server-side encryption that you want to use for your data. This encryption
            type is part of the endpoint settings or the extra connections attributes for Amazon
            S3. You can choose either ``SSE_S3`` (the default) or ``SSE_KMS`` . To use ``SSE_S3`` ,
            create an AWS Identity and Access Management (IAM) role with a policy that allows
            ``"arn:aws:s3:::*"`` to use the following actions: ``"s3:PutObject", "s3:ListBucket"``

          - **FileTransferUploadStreams** *(integer) --*

            The number of threads used to upload a single file. This parameter accepts a value from
            1 through 64. It defaults to 10.

          - **LoadTimeout** *(integer) --*

            The amount of time to wait (in milliseconds) before timing out, beginning from when you
            begin loading.

          - **MaxFileSize** *(integer) --*

            The maximum size (in KB) of any .csv file used to transfer data to Amazon Redshift.
            This accepts a value from 1 through 1,048,576. It defaults to 32,768 KB (32 MB).

          - **Password** *(string) --*

            The password for the user named in the ``username`` property.

          - **Port** *(integer) --*

            The port number for Amazon Redshift. The default value is 5439.

          - **RemoveQuotes** *(boolean) --*

            A value that specifies to remove surrounding quotation marks from strings in the
            incoming data. All characters within the quotation marks, including delimiters, are
            retained. Choose ``true`` to remove quotation marks. The default is ``false`` .

          - **ReplaceInvalidChars** *(string) --*

            A list of characters that you want to replace. Use with ``ReplaceChars`` .

          - **ReplaceChars** *(string) --*

            A value that specifies to replaces the invalid characters specified in
            ``ReplaceInvalidChars`` , substituting the specified characters instead. The default is
            ``"?"`` .

          - **ServerName** *(string) --*

            The name of the Amazon Redshift cluster you are using.

          - **ServiceAccessRoleArn** *(string) --*

            The Amazon Resource Name (ARN) of the IAM role that has access to the Amazon Redshift
            service.

          - **ServerSideEncryptionKmsKeyId** *(string) --*

            The AWS KMS key ID. If you are using ``SSE_KMS`` for the ``EncryptionMode`` , provide
            this key ID. The key that you use needs an attached policy that enables IAM user
            permissions and allows use of the key.

          - **TimeFormat** *(string) --*

            The time format that you want to use. Valid values are ``auto`` (case-sensitive),
            ``'timeformat_string'`` , ``'epochsecs'`` , or ``'epochmillisecs'`` . It defaults to
            10. Using ``auto`` recognizes most strings, even some that aren't supported when you
            use a time format string.

            If your date and time values use formats different from each other, set this parameter
            to ``auto`` .

          - **TrimBlanks** *(boolean) --*

            A value that specifies to remove the trailing white space characters from a VARCHAR
            string. This parameter applies only to columns with a VARCHAR data type. Choose
            ``true`` to remove unneeded white space. The default is ``false`` .

          - **TruncateColumns** *(boolean) --*

            A value that specifies to truncate data in columns to the appropriate number of
            characters, so that the data fits in the column. This parameter applies only to columns
            with a VARCHAR or CHAR data type, and rows with a size of 4 MB or less. Choose ``true``
            to truncate data. The default is ``false`` .

          - **Username** *(string) --*

            An Amazon Redshift user name for a registered user.

          - **WriteBufferSize** *(integer) --*

            The size of the write buffer to use in rows. Valid values range from 1 through 2,048.
            The default is 1,024. Use this setting to tune performance.
    """


_ClientDescribeEventCategoriesFiltersTypeDef = TypedDict(
    "_ClientDescribeEventCategoriesFiltersTypeDef", {"Name": str, "Values": List[str]}
)


class ClientDescribeEventCategoriesFiltersTypeDef(
    _ClientDescribeEventCategoriesFiltersTypeDef
):
    """
    Type definition for `ClientDescribeEventCategories` `Filters`

    - **Name** *(string) --* **[REQUIRED]**

      The name of the filter.

    - **Values** *(list) --* **[REQUIRED]**

      The filter value.

      - *(string) --*
    """


_ClientDescribeEventCategoriesResponseEventCategoryGroupListTypeDef = TypedDict(
    "_ClientDescribeEventCategoriesResponseEventCategoryGroupListTypeDef",
    {"SourceType": str, "EventCategories": List[str]},
    total=False,
)


class ClientDescribeEventCategoriesResponseEventCategoryGroupListTypeDef(
    _ClientDescribeEventCategoriesResponseEventCategoryGroupListTypeDef
):
    """
    Type definition for `ClientDescribeEventCategoriesResponse` `EventCategoryGroupList`

    - **SourceType** *(string) --*

      The type of AWS DMS resource that generates events.

      Valid values: replication-instance | replication-server | security-group |
      replication-task

    - **EventCategories** *(list) --*

      A list of event categories from a source type that you've chosen.

      - *(string) --*
    """


_ClientDescribeEventCategoriesResponseTypeDef = TypedDict(
    "_ClientDescribeEventCategoriesResponseTypeDef",
    {
        "EventCategoryGroupList": List[
            ClientDescribeEventCategoriesResponseEventCategoryGroupListTypeDef
        ]
    },
    total=False,
)


class ClientDescribeEventCategoriesResponseTypeDef(
    _ClientDescribeEventCategoriesResponseTypeDef
):
    """
    Type definition for `ClientDescribeEventCategories` `Response`

    - **EventCategoryGroupList** *(list) --*

      A list of event categories.

      - *(dict) --*

        - **SourceType** *(string) --*

          The type of AWS DMS resource that generates events.

          Valid values: replication-instance | replication-server | security-group |
          replication-task

        - **EventCategories** *(list) --*

          A list of event categories from a source type that you've chosen.

          - *(string) --*
    """


_ClientDescribeEventSubscriptionsFiltersTypeDef = TypedDict(
    "_ClientDescribeEventSubscriptionsFiltersTypeDef",
    {"Name": str, "Values": List[str]},
)


class ClientDescribeEventSubscriptionsFiltersTypeDef(
    _ClientDescribeEventSubscriptionsFiltersTypeDef
):
    """
    Type definition for `ClientDescribeEventSubscriptions` `Filters`

    - **Name** *(string) --* **[REQUIRED]**

      The name of the filter.

    - **Values** *(list) --* **[REQUIRED]**

      The filter value.

      - *(string) --*
    """


_ClientDescribeEventSubscriptionsResponseEventSubscriptionsListTypeDef = TypedDict(
    "_ClientDescribeEventSubscriptionsResponseEventSubscriptionsListTypeDef",
    {
        "CustomerAwsId": str,
        "CustSubscriptionId": str,
        "SnsTopicArn": str,
        "Status": str,
        "SubscriptionCreationTime": str,
        "SourceType": str,
        "SourceIdsList": List[str],
        "EventCategoriesList": List[str],
        "Enabled": bool,
    },
    total=False,
)


class ClientDescribeEventSubscriptionsResponseEventSubscriptionsListTypeDef(
    _ClientDescribeEventSubscriptionsResponseEventSubscriptionsListTypeDef
):
    """
    Type definition for `ClientDescribeEventSubscriptionsResponse` `EventSubscriptionsList`

    - **CustomerAwsId** *(string) --*

      The AWS customer account associated with the AWS DMS event notification subscription.

    - **CustSubscriptionId** *(string) --*

      The AWS DMS event notification subscription Id.

    - **SnsTopicArn** *(string) --*

      The topic ARN of the AWS DMS event notification subscription.

    - **Status** *(string) --*

      The status of the AWS DMS event notification subscription.

      Constraints:

      Can be one of the following: creating | modifying | deleting | active | no-permission |
      topic-not-exist

      The status "no-permission" indicates that AWS DMS no longer has permission to post to the
      SNS topic. The status "topic-not-exist" indicates that the topic was deleted after the
      subscription was created.

    - **SubscriptionCreationTime** *(string) --*

      The time the RDS event notification subscription was created.

    - **SourceType** *(string) --*

      The type of AWS DMS resource that generates events.

      Valid values: replication-instance | replication-server | security-group |
      replication-task

    - **SourceIdsList** *(list) --*

      A list of source Ids for the event subscription.

      - *(string) --*

    - **EventCategoriesList** *(list) --*

      A lists of event categories.

      - *(string) --*

    - **Enabled** *(boolean) --*

      Boolean value that indicates if the event subscription is enabled.
    """


_ClientDescribeEventSubscriptionsResponseTypeDef = TypedDict(
    "_ClientDescribeEventSubscriptionsResponseTypeDef",
    {
        "Marker": str,
        "EventSubscriptionsList": List[
            ClientDescribeEventSubscriptionsResponseEventSubscriptionsListTypeDef
        ],
    },
    total=False,
)


class ClientDescribeEventSubscriptionsResponseTypeDef(
    _ClientDescribeEventSubscriptionsResponseTypeDef
):
    """
    Type definition for `ClientDescribeEventSubscriptions` `Response`

    - **Marker** *(string) --*

      An optional pagination token provided by a previous request. If this parameter is specified,
      the response includes only records beyond the marker, up to the value specified by
      ``MaxRecords`` .

    - **EventSubscriptionsList** *(list) --*

      A list of event subscriptions.

      - *(dict) --*

        - **CustomerAwsId** *(string) --*

          The AWS customer account associated with the AWS DMS event notification subscription.

        - **CustSubscriptionId** *(string) --*

          The AWS DMS event notification subscription Id.

        - **SnsTopicArn** *(string) --*

          The topic ARN of the AWS DMS event notification subscription.

        - **Status** *(string) --*

          The status of the AWS DMS event notification subscription.

          Constraints:

          Can be one of the following: creating | modifying | deleting | active | no-permission |
          topic-not-exist

          The status "no-permission" indicates that AWS DMS no longer has permission to post to the
          SNS topic. The status "topic-not-exist" indicates that the topic was deleted after the
          subscription was created.

        - **SubscriptionCreationTime** *(string) --*

          The time the RDS event notification subscription was created.

        - **SourceType** *(string) --*

          The type of AWS DMS resource that generates events.

          Valid values: replication-instance | replication-server | security-group |
          replication-task

        - **SourceIdsList** *(list) --*

          A list of source Ids for the event subscription.

          - *(string) --*

        - **EventCategoriesList** *(list) --*

          A lists of event categories.

          - *(string) --*

        - **Enabled** *(boolean) --*

          Boolean value that indicates if the event subscription is enabled.
    """


_ClientDescribeEventsFiltersTypeDef = TypedDict(
    "_ClientDescribeEventsFiltersTypeDef", {"Name": str, "Values": List[str]}
)


class ClientDescribeEventsFiltersTypeDef(_ClientDescribeEventsFiltersTypeDef):
    """
    Type definition for `ClientDescribeEvents` `Filters`

    - **Name** *(string) --* **[REQUIRED]**

      The name of the filter.

    - **Values** *(list) --* **[REQUIRED]**

      The filter value.

      - *(string) --*
    """


_ClientDescribeEventsResponseEventsTypeDef = TypedDict(
    "_ClientDescribeEventsResponseEventsTypeDef",
    {
        "SourceIdentifier": str,
        "SourceType": str,
        "Message": str,
        "EventCategories": List[str],
        "Date": datetime,
    },
    total=False,
)


class ClientDescribeEventsResponseEventsTypeDef(
    _ClientDescribeEventsResponseEventsTypeDef
):
    """
    Type definition for `ClientDescribeEventsResponse` `Events`

    - **SourceIdentifier** *(string) --*

      The identifier of an event source.

    - **SourceType** *(string) --*

      The type of AWS DMS resource that generates events.

      Valid values: replication-instance | endpoint | replication-task

    - **Message** *(string) --*

      The event message.

    - **EventCategories** *(list) --*

      The event categories available for the specified source type.

      - *(string) --*

    - **Date** *(datetime) --*

      The date of the event.
    """


_ClientDescribeEventsResponseTypeDef = TypedDict(
    "_ClientDescribeEventsResponseTypeDef",
    {"Marker": str, "Events": List[ClientDescribeEventsResponseEventsTypeDef]},
    total=False,
)


class ClientDescribeEventsResponseTypeDef(_ClientDescribeEventsResponseTypeDef):
    """
    Type definition for `ClientDescribeEvents` `Response`

    - **Marker** *(string) --*

      An optional pagination token provided by a previous request. If this parameter is specified,
      the response includes only records beyond the marker, up to the value specified by
      ``MaxRecords`` .

    - **Events** *(list) --*

      The events described.

      - *(dict) --*

        - **SourceIdentifier** *(string) --*

          The identifier of an event source.

        - **SourceType** *(string) --*

          The type of AWS DMS resource that generates events.

          Valid values: replication-instance | endpoint | replication-task

        - **Message** *(string) --*

          The event message.

        - **EventCategories** *(list) --*

          The event categories available for the specified source type.

          - *(string) --*

        - **Date** *(datetime) --*

          The date of the event.
    """


_ClientDescribeOrderableReplicationInstancesResponseOrderableReplicationInstancesTypeDef = TypedDict(
    "_ClientDescribeOrderableReplicationInstancesResponseOrderableReplicationInstancesTypeDef",
    {
        "EngineVersion": str,
        "ReplicationInstanceClass": str,
        "StorageType": str,
        "MinAllocatedStorage": int,
        "MaxAllocatedStorage": int,
        "DefaultAllocatedStorage": int,
        "IncludedAllocatedStorage": int,
        "AvailabilityZones": List[str],
        "ReleaseStatus": str,
    },
    total=False,
)


class ClientDescribeOrderableReplicationInstancesResponseOrderableReplicationInstancesTypeDef(
    _ClientDescribeOrderableReplicationInstancesResponseOrderableReplicationInstancesTypeDef
):
    """
    Type definition for `ClientDescribeOrderableReplicationInstancesResponse` `OrderableReplicationInstances`

    - **EngineVersion** *(string) --*

      The version of the replication engine.

    - **ReplicationInstanceClass** *(string) --*

      The compute and memory capacity of the replication instance.

      Valid Values: ``dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large | dms.c4.large
      | dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge``

    - **StorageType** *(string) --*

      The type of storage used by the replication instance.

    - **MinAllocatedStorage** *(integer) --*

      The minimum amount of storage (in gigabytes) that can be allocated for the replication
      instance.

    - **MaxAllocatedStorage** *(integer) --*

      The minimum amount of storage (in gigabytes) that can be allocated for the replication
      instance.

    - **DefaultAllocatedStorage** *(integer) --*

      The default amount of storage (in gigabytes) that is allocated for the replication
      instance.

    - **IncludedAllocatedStorage** *(integer) --*

      The amount of storage (in gigabytes) that is allocated for the replication instance.

    - **AvailabilityZones** *(list) --*

      List of Availability Zones for this replication instance.

      - *(string) --*

    - **ReleaseStatus** *(string) --*

      The value returned when the specified ``EngineVersion`` of the replication instance is in
      Beta or test mode. This indicates some features might not work as expected.

      .. note::

        AWS DMS supports the ``ReleaseStatus`` parameter in versions 3.1.4 and later.
    """


_ClientDescribeOrderableReplicationInstancesResponseTypeDef = TypedDict(
    "_ClientDescribeOrderableReplicationInstancesResponseTypeDef",
    {
        "OrderableReplicationInstances": List[
            ClientDescribeOrderableReplicationInstancesResponseOrderableReplicationInstancesTypeDef
        ],
        "Marker": str,
    },
    total=False,
)


class ClientDescribeOrderableReplicationInstancesResponseTypeDef(
    _ClientDescribeOrderableReplicationInstancesResponseTypeDef
):
    """
    Type definition for `ClientDescribeOrderableReplicationInstances` `Response`

    - **OrderableReplicationInstances** *(list) --*

      The order-able replication instances available.

      - *(dict) --*

        - **EngineVersion** *(string) --*

          The version of the replication engine.

        - **ReplicationInstanceClass** *(string) --*

          The compute and memory capacity of the replication instance.

          Valid Values: ``dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large | dms.c4.large
          | dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge``

        - **StorageType** *(string) --*

          The type of storage used by the replication instance.

        - **MinAllocatedStorage** *(integer) --*

          The minimum amount of storage (in gigabytes) that can be allocated for the replication
          instance.

        - **MaxAllocatedStorage** *(integer) --*

          The minimum amount of storage (in gigabytes) that can be allocated for the replication
          instance.

        - **DefaultAllocatedStorage** *(integer) --*

          The default amount of storage (in gigabytes) that is allocated for the replication
          instance.

        - **IncludedAllocatedStorage** *(integer) --*

          The amount of storage (in gigabytes) that is allocated for the replication instance.

        - **AvailabilityZones** *(list) --*

          List of Availability Zones for this replication instance.

          - *(string) --*

        - **ReleaseStatus** *(string) --*

          The value returned when the specified ``EngineVersion`` of the replication instance is in
          Beta or test mode. This indicates some features might not work as expected.

          .. note::

            AWS DMS supports the ``ReleaseStatus`` parameter in versions 3.1.4 and later.

    - **Marker** *(string) --*

      An optional pagination token provided by a previous request. If this parameter is specified,
      the response includes only records beyond the marker, up to the value specified by
      ``MaxRecords`` .
    """


_ClientDescribePendingMaintenanceActionsFiltersTypeDef = TypedDict(
    "_ClientDescribePendingMaintenanceActionsFiltersTypeDef",
    {"Name": str, "Values": List[str]},
)


class ClientDescribePendingMaintenanceActionsFiltersTypeDef(
    _ClientDescribePendingMaintenanceActionsFiltersTypeDef
):
    """
    Type definition for `ClientDescribePendingMaintenanceActions` `Filters`

    - **Name** *(string) --* **[REQUIRED]**

      The name of the filter.

    - **Values** *(list) --* **[REQUIRED]**

      The filter value.

      - *(string) --*
    """


_ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef = TypedDict(
    "_ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef",
    {
        "Action": str,
        "AutoAppliedAfterDate": datetime,
        "ForcedApplyDate": datetime,
        "OptInStatus": str,
        "CurrentApplyDate": datetime,
        "Description": str,
    },
    total=False,
)


class ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef(
    _ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef
):
    """
    Type definition for `ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActions` `PendingMaintenanceActionDetails`

    - **Action** *(string) --*

      The type of pending maintenance action that is available for the resource.

    - **AutoAppliedAfterDate** *(datetime) --*

      The date of the maintenance window when the action will be applied. The maintenance
      action will be applied to the resource during its first maintenance window after this
      date. If this date is specified, any ``next-maintenance`` opt-in requests are ignored.

    - **ForcedApplyDate** *(datetime) --*

      The date when the maintenance action will be automatically applied. The maintenance
      action will be applied to the resource on this date regardless of the maintenance
      window for the resource. If this date is specified, any ``immediate`` opt-in requests
      are ignored.

    - **OptInStatus** *(string) --*

      Indicates the type of opt-in request that has been received for the resource.

    - **CurrentApplyDate** *(datetime) --*

      The effective date when the pending maintenance action will be applied to the
      resource. This date takes into account opt-in requests received from the
      ``ApplyPendingMaintenanceAction`` API, the ``AutoAppliedAfterDate`` , and the
      ``ForcedApplyDate`` . This value is blank if an opt-in request has not been received
      and nothing has been specified as ``AutoAppliedAfterDate`` or ``ForcedApplyDate`` .

    - **Description** *(string) --*

      A description providing more detail about the maintenance action.
    """


_ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsTypeDef = TypedDict(
    "_ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsTypeDef",
    {
        "ResourceIdentifier": str,
        "PendingMaintenanceActionDetails": List[
            ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef
        ],
    },
    total=False,
)


class ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsTypeDef(
    _ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsTypeDef
):
    """
    Type definition for `ClientDescribePendingMaintenanceActionsResponse` `PendingMaintenanceActions`

    - **ResourceIdentifier** *(string) --*

      The Amazon Resource Name (ARN) of the DMS resource that the pending maintenance action
      applies to. For information about creating an ARN, see `Constructing an Amazon Resource
      Name (ARN) for AWS DMS
      <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.AWS.ARN.html>`__ in
      the DMS documentation.

    - **PendingMaintenanceActionDetails** *(list) --*

      Detailed information about the pending maintenance action.

      - *(dict) --*

        - **Action** *(string) --*

          The type of pending maintenance action that is available for the resource.

        - **AutoAppliedAfterDate** *(datetime) --*

          The date of the maintenance window when the action will be applied. The maintenance
          action will be applied to the resource during its first maintenance window after this
          date. If this date is specified, any ``next-maintenance`` opt-in requests are ignored.

        - **ForcedApplyDate** *(datetime) --*

          The date when the maintenance action will be automatically applied. The maintenance
          action will be applied to the resource on this date regardless of the maintenance
          window for the resource. If this date is specified, any ``immediate`` opt-in requests
          are ignored.

        - **OptInStatus** *(string) --*

          Indicates the type of opt-in request that has been received for the resource.

        - **CurrentApplyDate** *(datetime) --*

          The effective date when the pending maintenance action will be applied to the
          resource. This date takes into account opt-in requests received from the
          ``ApplyPendingMaintenanceAction`` API, the ``AutoAppliedAfterDate`` , and the
          ``ForcedApplyDate`` . This value is blank if an opt-in request has not been received
          and nothing has been specified as ``AutoAppliedAfterDate`` or ``ForcedApplyDate`` .

        - **Description** *(string) --*

          A description providing more detail about the maintenance action.
    """


_ClientDescribePendingMaintenanceActionsResponseTypeDef = TypedDict(
    "_ClientDescribePendingMaintenanceActionsResponseTypeDef",
    {
        "PendingMaintenanceActions": List[
            ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsTypeDef
        ],
        "Marker": str,
    },
    total=False,
)


class ClientDescribePendingMaintenanceActionsResponseTypeDef(
    _ClientDescribePendingMaintenanceActionsResponseTypeDef
):
    """
    Type definition for `ClientDescribePendingMaintenanceActions` `Response`

    - **PendingMaintenanceActions** *(list) --*

      The pending maintenance action.

      - *(dict) --*

        - **ResourceIdentifier** *(string) --*

          The Amazon Resource Name (ARN) of the DMS resource that the pending maintenance action
          applies to. For information about creating an ARN, see `Constructing an Amazon Resource
          Name (ARN) for AWS DMS
          <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.AWS.ARN.html>`__ in
          the DMS documentation.

        - **PendingMaintenanceActionDetails** *(list) --*

          Detailed information about the pending maintenance action.

          - *(dict) --*

            - **Action** *(string) --*

              The type of pending maintenance action that is available for the resource.

            - **AutoAppliedAfterDate** *(datetime) --*

              The date of the maintenance window when the action will be applied. The maintenance
              action will be applied to the resource during its first maintenance window after this
              date. If this date is specified, any ``next-maintenance`` opt-in requests are ignored.

            - **ForcedApplyDate** *(datetime) --*

              The date when the maintenance action will be automatically applied. The maintenance
              action will be applied to the resource on this date regardless of the maintenance
              window for the resource. If this date is specified, any ``immediate`` opt-in requests
              are ignored.

            - **OptInStatus** *(string) --*

              Indicates the type of opt-in request that has been received for the resource.

            - **CurrentApplyDate** *(datetime) --*

              The effective date when the pending maintenance action will be applied to the
              resource. This date takes into account opt-in requests received from the
              ``ApplyPendingMaintenanceAction`` API, the ``AutoAppliedAfterDate`` , and the
              ``ForcedApplyDate`` . This value is blank if an opt-in request has not been received
              and nothing has been specified as ``AutoAppliedAfterDate`` or ``ForcedApplyDate`` .

            - **Description** *(string) --*

              A description providing more detail about the maintenance action.

    - **Marker** *(string) --*

      An optional pagination token provided by a previous request. If this parameter is specified,
      the response includes only records beyond the marker, up to the value specified by
      ``MaxRecords`` .
    """


_ClientDescribeRefreshSchemasStatusResponseRefreshSchemasStatusTypeDef = TypedDict(
    "_ClientDescribeRefreshSchemasStatusResponseRefreshSchemasStatusTypeDef",
    {
        "EndpointArn": str,
        "ReplicationInstanceArn": str,
        "Status": str,
        "LastRefreshDate": datetime,
        "LastFailureMessage": str,
    },
    total=False,
)


class ClientDescribeRefreshSchemasStatusResponseRefreshSchemasStatusTypeDef(
    _ClientDescribeRefreshSchemasStatusResponseRefreshSchemasStatusTypeDef
):
    """
    Type definition for `ClientDescribeRefreshSchemasStatusResponse` `RefreshSchemasStatus`

    The status of the schema.

    - **EndpointArn** *(string) --*

      The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

    - **ReplicationInstanceArn** *(string) --*

      The Amazon Resource Name (ARN) of the replication instance.

    - **Status** *(string) --*

      The status of the schema.

    - **LastRefreshDate** *(datetime) --*

      The date the schema was last refreshed.

    - **LastFailureMessage** *(string) --*

      The last failure message for the schema.
    """


_ClientDescribeRefreshSchemasStatusResponseTypeDef = TypedDict(
    "_ClientDescribeRefreshSchemasStatusResponseTypeDef",
    {
        "RefreshSchemasStatus": ClientDescribeRefreshSchemasStatusResponseRefreshSchemasStatusTypeDef
    },
    total=False,
)


class ClientDescribeRefreshSchemasStatusResponseTypeDef(
    _ClientDescribeRefreshSchemasStatusResponseTypeDef
):
    """
    Type definition for `ClientDescribeRefreshSchemasStatus` `Response`

    - **RefreshSchemasStatus** *(dict) --*

      The status of the schema.

      - **EndpointArn** *(string) --*

        The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

      - **ReplicationInstanceArn** *(string) --*

        The Amazon Resource Name (ARN) of the replication instance.

      - **Status** *(string) --*

        The status of the schema.

      - **LastRefreshDate** *(datetime) --*

        The date the schema was last refreshed.

      - **LastFailureMessage** *(string) --*

        The last failure message for the schema.
    """


_ClientDescribeReplicationInstanceTaskLogsResponseReplicationInstanceTaskLogsTypeDef = TypedDict(
    "_ClientDescribeReplicationInstanceTaskLogsResponseReplicationInstanceTaskLogsTypeDef",
    {
        "ReplicationTaskName": str,
        "ReplicationTaskArn": str,
        "ReplicationInstanceTaskLogSize": int,
    },
    total=False,
)


class ClientDescribeReplicationInstanceTaskLogsResponseReplicationInstanceTaskLogsTypeDef(
    _ClientDescribeReplicationInstanceTaskLogsResponseReplicationInstanceTaskLogsTypeDef
):
    """
    Type definition for `ClientDescribeReplicationInstanceTaskLogsResponse` `ReplicationInstanceTaskLogs`

    Contains metadata for a replication instance task log.

    - **ReplicationTaskName** *(string) --*

      The name of the replication task.

    - **ReplicationTaskArn** *(string) --*

      The Amazon Resource Name (ARN) of the replication task.

    - **ReplicationInstanceTaskLogSize** *(integer) --*

      The size, in bytes, of the replication task log.
    """


_ClientDescribeReplicationInstanceTaskLogsResponseTypeDef = TypedDict(
    "_ClientDescribeReplicationInstanceTaskLogsResponseTypeDef",
    {
        "ReplicationInstanceArn": str,
        "ReplicationInstanceTaskLogs": List[
            ClientDescribeReplicationInstanceTaskLogsResponseReplicationInstanceTaskLogsTypeDef
        ],
        "Marker": str,
    },
    total=False,
)


class ClientDescribeReplicationInstanceTaskLogsResponseTypeDef(
    _ClientDescribeReplicationInstanceTaskLogsResponseTypeDef
):
    """
    Type definition for `ClientDescribeReplicationInstanceTaskLogs` `Response`

    - **ReplicationInstanceArn** *(string) --*

      The Amazon Resource Name (ARN) of the replication instance.

    - **ReplicationInstanceTaskLogs** *(list) --*

      An array of replication task log metadata. Each member of the array contains the replication
      task name, ARN, and task log size (in bytes).

      - *(dict) --*

        Contains metadata for a replication instance task log.

        - **ReplicationTaskName** *(string) --*

          The name of the replication task.

        - **ReplicationTaskArn** *(string) --*

          The Amazon Resource Name (ARN) of the replication task.

        - **ReplicationInstanceTaskLogSize** *(integer) --*

          The size, in bytes, of the replication task log.

    - **Marker** *(string) --*

      An optional pagination token provided by a previous request. If this parameter is specified,
      the response includes only records beyond the marker, up to the value specified by
      ``MaxRecords`` .
    """


_ClientDescribeReplicationInstancesFiltersTypeDef = TypedDict(
    "_ClientDescribeReplicationInstancesFiltersTypeDef",
    {"Name": str, "Values": List[str]},
)


class ClientDescribeReplicationInstancesFiltersTypeDef(
    _ClientDescribeReplicationInstancesFiltersTypeDef
):
    """
    Type definition for `ClientDescribeReplicationInstances` `Filters`

    - **Name** *(string) --* **[REQUIRED]**

      The name of the filter.

    - **Values** *(list) --* **[REQUIRED]**

      The filter value.

      - *(string) --*
    """


_ClientDescribeReplicationInstancesResponseReplicationInstancesPendingModifiedValuesTypeDef = TypedDict(
    "_ClientDescribeReplicationInstancesResponseReplicationInstancesPendingModifiedValuesTypeDef",
    {
        "ReplicationInstanceClass": str,
        "AllocatedStorage": int,
        "MultiAZ": bool,
        "EngineVersion": str,
    },
    total=False,
)


class ClientDescribeReplicationInstancesResponseReplicationInstancesPendingModifiedValuesTypeDef(
    _ClientDescribeReplicationInstancesResponseReplicationInstancesPendingModifiedValuesTypeDef
):
    """
    Type definition for `ClientDescribeReplicationInstancesResponseReplicationInstances` `PendingModifiedValues`

    The pending modification values.

    - **ReplicationInstanceClass** *(string) --*

      The compute and memory capacity of the replication instance.

      Valid Values: ``dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large |
      dms.c4.large | dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge``

    - **AllocatedStorage** *(integer) --*

      The amount of storage (in gigabytes) that is allocated for the replication instance.

    - **MultiAZ** *(boolean) --*

      Specifies whether the replication instance is a Multi-AZ deployment. You cannot set the
      ``AvailabilityZone`` parameter if the Multi-AZ parameter is set to ``true`` .

    - **EngineVersion** *(string) --*

      The engine version number of the replication instance.
    """


_ClientDescribeReplicationInstancesResponseReplicationInstancesReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "_ClientDescribeReplicationInstancesResponseReplicationInstancesReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)


class ClientDescribeReplicationInstancesResponseReplicationInstancesReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef(
    _ClientDescribeReplicationInstancesResponseReplicationInstancesReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef
):
    """
    Type definition for `ClientDescribeReplicationInstancesResponseReplicationInstancesReplicationSubnetGroupSubnets` `SubnetAvailabilityZone`

    The Availability Zone of the subnet.

    - **Name** *(string) --*

      The name of the availability zone.
    """


_ClientDescribeReplicationInstancesResponseReplicationInstancesReplicationSubnetGroupSubnetsTypeDef = TypedDict(
    "_ClientDescribeReplicationInstancesResponseReplicationInstancesReplicationSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientDescribeReplicationInstancesResponseReplicationInstancesReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)


class ClientDescribeReplicationInstancesResponseReplicationInstancesReplicationSubnetGroupSubnetsTypeDef(
    _ClientDescribeReplicationInstancesResponseReplicationInstancesReplicationSubnetGroupSubnetsTypeDef
):
    """
    Type definition for `ClientDescribeReplicationInstancesResponseReplicationInstancesReplicationSubnetGroup` `Subnets`

    - **SubnetIdentifier** *(string) --*

      The subnet identifier.

    - **SubnetAvailabilityZone** *(dict) --*

      The Availability Zone of the subnet.

      - **Name** *(string) --*

        The name of the availability zone.

    - **SubnetStatus** *(string) --*

      The status of the subnet.
    """


_ClientDescribeReplicationInstancesResponseReplicationInstancesReplicationSubnetGroupTypeDef = TypedDict(
    "_ClientDescribeReplicationInstancesResponseReplicationInstancesReplicationSubnetGroupTypeDef",
    {
        "ReplicationSubnetGroupIdentifier": str,
        "ReplicationSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[
            ClientDescribeReplicationInstancesResponseReplicationInstancesReplicationSubnetGroupSubnetsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeReplicationInstancesResponseReplicationInstancesReplicationSubnetGroupTypeDef(
    _ClientDescribeReplicationInstancesResponseReplicationInstancesReplicationSubnetGroupTypeDef
):
    """
    Type definition for `ClientDescribeReplicationInstancesResponseReplicationInstances` `ReplicationSubnetGroup`

    The subnet group for the replication instance.

    - **ReplicationSubnetGroupIdentifier** *(string) --*

      The identifier of the replication instance subnet group.

    - **ReplicationSubnetGroupDescription** *(string) --*

      A description for the replication subnet group.

    - **VpcId** *(string) --*

      The ID of the VPC.

    - **SubnetGroupStatus** *(string) --*

      The status of the subnet group.

    - **Subnets** *(list) --*

      The subnets that are in the subnet group.

      - *(dict) --*

        - **SubnetIdentifier** *(string) --*

          The subnet identifier.

        - **SubnetAvailabilityZone** *(dict) --*

          The Availability Zone of the subnet.

          - **Name** *(string) --*

            The name of the availability zone.

        - **SubnetStatus** *(string) --*

          The status of the subnet.
    """


_ClientDescribeReplicationInstancesResponseReplicationInstancesVpcSecurityGroupsTypeDef = TypedDict(
    "_ClientDescribeReplicationInstancesResponseReplicationInstancesVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientDescribeReplicationInstancesResponseReplicationInstancesVpcSecurityGroupsTypeDef(
    _ClientDescribeReplicationInstancesResponseReplicationInstancesVpcSecurityGroupsTypeDef
):
    """
    Type definition for `ClientDescribeReplicationInstancesResponseReplicationInstances` `VpcSecurityGroups`

    - **VpcSecurityGroupId** *(string) --*

      The VPC security group Id.

    - **Status** *(string) --*

      The status of the VPC security group.
    """


_ClientDescribeReplicationInstancesResponseReplicationInstancesTypeDef = TypedDict(
    "_ClientDescribeReplicationInstancesResponseReplicationInstancesTypeDef",
    {
        "ReplicationInstanceIdentifier": str,
        "ReplicationInstanceClass": str,
        "ReplicationInstanceStatus": str,
        "AllocatedStorage": int,
        "InstanceCreateTime": datetime,
        "VpcSecurityGroups": List[
            ClientDescribeReplicationInstancesResponseReplicationInstancesVpcSecurityGroupsTypeDef
        ],
        "AvailabilityZone": str,
        "ReplicationSubnetGroup": ClientDescribeReplicationInstancesResponseReplicationInstancesReplicationSubnetGroupTypeDef,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientDescribeReplicationInstancesResponseReplicationInstancesPendingModifiedValuesTypeDef,
        "MultiAZ": bool,
        "EngineVersion": str,
        "AutoMinorVersionUpgrade": bool,
        "KmsKeyId": str,
        "ReplicationInstanceArn": str,
        "ReplicationInstancePublicIpAddress": str,
        "ReplicationInstancePrivateIpAddress": str,
        "ReplicationInstancePublicIpAddresses": List[str],
        "ReplicationInstancePrivateIpAddresses": List[str],
        "PubliclyAccessible": bool,
        "SecondaryAvailabilityZone": str,
        "FreeUntil": datetime,
        "DnsNameServers": str,
    },
    total=False,
)


class ClientDescribeReplicationInstancesResponseReplicationInstancesTypeDef(
    _ClientDescribeReplicationInstancesResponseReplicationInstancesTypeDef
):
    """
    Type definition for `ClientDescribeReplicationInstancesResponse` `ReplicationInstances`

    - **ReplicationInstanceIdentifier** *(string) --*

      The replication instance identifier. This parameter is stored as a lowercase string.

      Constraints:

      * Must contain from 1 to 63 alphanumeric characters or hyphens.

      * First character must be a letter.

      * Cannot end with a hyphen or contain two consecutive hyphens.

      Example: ``myrepinstance``

    - **ReplicationInstanceClass** *(string) --*

      The compute and memory capacity of the replication instance.

      Valid Values: ``dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large | dms.c4.large
      | dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge``

    - **ReplicationInstanceStatus** *(string) --*

      The status of the replication instance.

    - **AllocatedStorage** *(integer) --*

      The amount of storage (in gigabytes) that is allocated for the replication instance.

    - **InstanceCreateTime** *(datetime) --*

      The time the replication instance was created.

    - **VpcSecurityGroups** *(list) --*

      The VPC security group for the instance.

      - *(dict) --*

        - **VpcSecurityGroupId** *(string) --*

          The VPC security group Id.

        - **Status** *(string) --*

          The status of the VPC security group.

    - **AvailabilityZone** *(string) --*

      The Availability Zone for the instance.

    - **ReplicationSubnetGroup** *(dict) --*

      The subnet group for the replication instance.

      - **ReplicationSubnetGroupIdentifier** *(string) --*

        The identifier of the replication instance subnet group.

      - **ReplicationSubnetGroupDescription** *(string) --*

        A description for the replication subnet group.

      - **VpcId** *(string) --*

        The ID of the VPC.

      - **SubnetGroupStatus** *(string) --*

        The status of the subnet group.

      - **Subnets** *(list) --*

        The subnets that are in the subnet group.

        - *(dict) --*

          - **SubnetIdentifier** *(string) --*

            The subnet identifier.

          - **SubnetAvailabilityZone** *(dict) --*

            The Availability Zone of the subnet.

            - **Name** *(string) --*

              The name of the availability zone.

          - **SubnetStatus** *(string) --*

            The status of the subnet.

    - **PreferredMaintenanceWindow** *(string) --*

      The maintenance window times for the replication instance.

    - **PendingModifiedValues** *(dict) --*

      The pending modification values.

      - **ReplicationInstanceClass** *(string) --*

        The compute and memory capacity of the replication instance.

        Valid Values: ``dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large |
        dms.c4.large | dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge``

      - **AllocatedStorage** *(integer) --*

        The amount of storage (in gigabytes) that is allocated for the replication instance.

      - **MultiAZ** *(boolean) --*

        Specifies whether the replication instance is a Multi-AZ deployment. You cannot set the
        ``AvailabilityZone`` parameter if the Multi-AZ parameter is set to ``true`` .

      - **EngineVersion** *(string) --*

        The engine version number of the replication instance.

    - **MultiAZ** *(boolean) --*

      Specifies whether the replication instance is a Multi-AZ deployment. You cannot set the
      ``AvailabilityZone`` parameter if the Multi-AZ parameter is set to ``true`` .

    - **EngineVersion** *(string) --*

      The engine version number of the replication instance.

    - **AutoMinorVersionUpgrade** *(boolean) --*

      Boolean value indicating if minor version upgrades will be automatically applied to the
      instance.

    - **KmsKeyId** *(string) --*

      An AWS KMS key identifier that is used to encrypt the data on the replication instance.

      If you don't specify a value for the ``KmsKeyId`` parameter, then AWS DMS uses your
      default encryption key.

      AWS KMS creates the default encryption key for your AWS account. Your AWS account has a
      different default encryption key for each AWS Region.

    - **ReplicationInstanceArn** *(string) --*

      The Amazon Resource Name (ARN) of the replication instance.

    - **ReplicationInstancePublicIpAddress** *(string) --*

      The public IP address of the replication instance.

    - **ReplicationInstancePrivateIpAddress** *(string) --*

      The private IP address of the replication instance.

    - **ReplicationInstancePublicIpAddresses** *(list) --*

      One or more public IP addresses for the replication instance.

      - *(string) --*

    - **ReplicationInstancePrivateIpAddresses** *(list) --*

      One or more private IP addresses for the replication instance.

      - *(string) --*

    - **PubliclyAccessible** *(boolean) --*

      Specifies the accessibility options for the replication instance. A value of ``true``
      represents an instance with a public IP address. A value of ``false`` represents an
      instance with a private IP address. The default value is ``true`` .

    - **SecondaryAvailabilityZone** *(string) --*

      The availability zone of the standby replication instance in a Multi-AZ deployment.

    - **FreeUntil** *(datetime) --*

      The expiration date of the free replication instance that is part of the Free DMS program.

    - **DnsNameServers** *(string) --*

      The DNS name servers for the replication instance.
    """


_ClientDescribeReplicationInstancesResponseTypeDef = TypedDict(
    "_ClientDescribeReplicationInstancesResponseTypeDef",
    {
        "Marker": str,
        "ReplicationInstances": List[
            ClientDescribeReplicationInstancesResponseReplicationInstancesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeReplicationInstancesResponseTypeDef(
    _ClientDescribeReplicationInstancesResponseTypeDef
):
    """
    Type definition for `ClientDescribeReplicationInstances` `Response`

    - **Marker** *(string) --*

      An optional pagination token provided by a previous request. If this parameter is specified,
      the response includes only records beyond the marker, up to the value specified by
      ``MaxRecords`` .

    - **ReplicationInstances** *(list) --*

      The replication instances described.

      - *(dict) --*

        - **ReplicationInstanceIdentifier** *(string) --*

          The replication instance identifier. This parameter is stored as a lowercase string.

          Constraints:

          * Must contain from 1 to 63 alphanumeric characters or hyphens.

          * First character must be a letter.

          * Cannot end with a hyphen or contain two consecutive hyphens.

          Example: ``myrepinstance``

        - **ReplicationInstanceClass** *(string) --*

          The compute and memory capacity of the replication instance.

          Valid Values: ``dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large | dms.c4.large
          | dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge``

        - **ReplicationInstanceStatus** *(string) --*

          The status of the replication instance.

        - **AllocatedStorage** *(integer) --*

          The amount of storage (in gigabytes) that is allocated for the replication instance.

        - **InstanceCreateTime** *(datetime) --*

          The time the replication instance was created.

        - **VpcSecurityGroups** *(list) --*

          The VPC security group for the instance.

          - *(dict) --*

            - **VpcSecurityGroupId** *(string) --*

              The VPC security group Id.

            - **Status** *(string) --*

              The status of the VPC security group.

        - **AvailabilityZone** *(string) --*

          The Availability Zone for the instance.

        - **ReplicationSubnetGroup** *(dict) --*

          The subnet group for the replication instance.

          - **ReplicationSubnetGroupIdentifier** *(string) --*

            The identifier of the replication instance subnet group.

          - **ReplicationSubnetGroupDescription** *(string) --*

            A description for the replication subnet group.

          - **VpcId** *(string) --*

            The ID of the VPC.

          - **SubnetGroupStatus** *(string) --*

            The status of the subnet group.

          - **Subnets** *(list) --*

            The subnets that are in the subnet group.

            - *(dict) --*

              - **SubnetIdentifier** *(string) --*

                The subnet identifier.

              - **SubnetAvailabilityZone** *(dict) --*

                The Availability Zone of the subnet.

                - **Name** *(string) --*

                  The name of the availability zone.

              - **SubnetStatus** *(string) --*

                The status of the subnet.

        - **PreferredMaintenanceWindow** *(string) --*

          The maintenance window times for the replication instance.

        - **PendingModifiedValues** *(dict) --*

          The pending modification values.

          - **ReplicationInstanceClass** *(string) --*

            The compute and memory capacity of the replication instance.

            Valid Values: ``dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large |
            dms.c4.large | dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge``

          - **AllocatedStorage** *(integer) --*

            The amount of storage (in gigabytes) that is allocated for the replication instance.

          - **MultiAZ** *(boolean) --*

            Specifies whether the replication instance is a Multi-AZ deployment. You cannot set the
            ``AvailabilityZone`` parameter if the Multi-AZ parameter is set to ``true`` .

          - **EngineVersion** *(string) --*

            The engine version number of the replication instance.

        - **MultiAZ** *(boolean) --*

          Specifies whether the replication instance is a Multi-AZ deployment. You cannot set the
          ``AvailabilityZone`` parameter if the Multi-AZ parameter is set to ``true`` .

        - **EngineVersion** *(string) --*

          The engine version number of the replication instance.

        - **AutoMinorVersionUpgrade** *(boolean) --*

          Boolean value indicating if minor version upgrades will be automatically applied to the
          instance.

        - **KmsKeyId** *(string) --*

          An AWS KMS key identifier that is used to encrypt the data on the replication instance.

          If you don't specify a value for the ``KmsKeyId`` parameter, then AWS DMS uses your
          default encryption key.

          AWS KMS creates the default encryption key for your AWS account. Your AWS account has a
          different default encryption key for each AWS Region.

        - **ReplicationInstanceArn** *(string) --*

          The Amazon Resource Name (ARN) of the replication instance.

        - **ReplicationInstancePublicIpAddress** *(string) --*

          The public IP address of the replication instance.

        - **ReplicationInstancePrivateIpAddress** *(string) --*

          The private IP address of the replication instance.

        - **ReplicationInstancePublicIpAddresses** *(list) --*

          One or more public IP addresses for the replication instance.

          - *(string) --*

        - **ReplicationInstancePrivateIpAddresses** *(list) --*

          One or more private IP addresses for the replication instance.

          - *(string) --*

        - **PubliclyAccessible** *(boolean) --*

          Specifies the accessibility options for the replication instance. A value of ``true``
          represents an instance with a public IP address. A value of ``false`` represents an
          instance with a private IP address. The default value is ``true`` .

        - **SecondaryAvailabilityZone** *(string) --*

          The availability zone of the standby replication instance in a Multi-AZ deployment.

        - **FreeUntil** *(datetime) --*

          The expiration date of the free replication instance that is part of the Free DMS program.

        - **DnsNameServers** *(string) --*

          The DNS name servers for the replication instance.
    """


_ClientDescribeReplicationSubnetGroupsFiltersTypeDef = TypedDict(
    "_ClientDescribeReplicationSubnetGroupsFiltersTypeDef",
    {"Name": str, "Values": List[str]},
)


class ClientDescribeReplicationSubnetGroupsFiltersTypeDef(
    _ClientDescribeReplicationSubnetGroupsFiltersTypeDef
):
    """
    Type definition for `ClientDescribeReplicationSubnetGroups` `Filters`

    - **Name** *(string) --* **[REQUIRED]**

      The name of the filter.

    - **Values** *(list) --* **[REQUIRED]**

      The filter value.

      - *(string) --*
    """


_ClientDescribeReplicationSubnetGroupsResponseReplicationSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "_ClientDescribeReplicationSubnetGroupsResponseReplicationSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)


class ClientDescribeReplicationSubnetGroupsResponseReplicationSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef(
    _ClientDescribeReplicationSubnetGroupsResponseReplicationSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef
):
    """
    Type definition for `ClientDescribeReplicationSubnetGroupsResponseReplicationSubnetGroupsSubnets` `SubnetAvailabilityZone`

    The Availability Zone of the subnet.

    - **Name** *(string) --*

      The name of the availability zone.
    """


_ClientDescribeReplicationSubnetGroupsResponseReplicationSubnetGroupsSubnetsTypeDef = TypedDict(
    "_ClientDescribeReplicationSubnetGroupsResponseReplicationSubnetGroupsSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientDescribeReplicationSubnetGroupsResponseReplicationSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)


class ClientDescribeReplicationSubnetGroupsResponseReplicationSubnetGroupsSubnetsTypeDef(
    _ClientDescribeReplicationSubnetGroupsResponseReplicationSubnetGroupsSubnetsTypeDef
):
    """
    Type definition for `ClientDescribeReplicationSubnetGroupsResponseReplicationSubnetGroups` `Subnets`

    - **SubnetIdentifier** *(string) --*

      The subnet identifier.

    - **SubnetAvailabilityZone** *(dict) --*

      The Availability Zone of the subnet.

      - **Name** *(string) --*

        The name of the availability zone.

    - **SubnetStatus** *(string) --*

      The status of the subnet.
    """


_ClientDescribeReplicationSubnetGroupsResponseReplicationSubnetGroupsTypeDef = TypedDict(
    "_ClientDescribeReplicationSubnetGroupsResponseReplicationSubnetGroupsTypeDef",
    {
        "ReplicationSubnetGroupIdentifier": str,
        "ReplicationSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[
            ClientDescribeReplicationSubnetGroupsResponseReplicationSubnetGroupsSubnetsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeReplicationSubnetGroupsResponseReplicationSubnetGroupsTypeDef(
    _ClientDescribeReplicationSubnetGroupsResponseReplicationSubnetGroupsTypeDef
):
    """
    Type definition for `ClientDescribeReplicationSubnetGroupsResponse` `ReplicationSubnetGroups`

    - **ReplicationSubnetGroupIdentifier** *(string) --*

      The identifier of the replication instance subnet group.

    - **ReplicationSubnetGroupDescription** *(string) --*

      A description for the replication subnet group.

    - **VpcId** *(string) --*

      The ID of the VPC.

    - **SubnetGroupStatus** *(string) --*

      The status of the subnet group.

    - **Subnets** *(list) --*

      The subnets that are in the subnet group.

      - *(dict) --*

        - **SubnetIdentifier** *(string) --*

          The subnet identifier.

        - **SubnetAvailabilityZone** *(dict) --*

          The Availability Zone of the subnet.

          - **Name** *(string) --*

            The name of the availability zone.

        - **SubnetStatus** *(string) --*

          The status of the subnet.
    """


_ClientDescribeReplicationSubnetGroupsResponseTypeDef = TypedDict(
    "_ClientDescribeReplicationSubnetGroupsResponseTypeDef",
    {
        "Marker": str,
        "ReplicationSubnetGroups": List[
            ClientDescribeReplicationSubnetGroupsResponseReplicationSubnetGroupsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeReplicationSubnetGroupsResponseTypeDef(
    _ClientDescribeReplicationSubnetGroupsResponseTypeDef
):
    """
    Type definition for `ClientDescribeReplicationSubnetGroups` `Response`

    - **Marker** *(string) --*

      An optional pagination token provided by a previous request. If this parameter is specified,
      the response includes only records beyond the marker, up to the value specified by
      ``MaxRecords`` .

    - **ReplicationSubnetGroups** *(list) --*

      A description of the replication subnet groups.

      - *(dict) --*

        - **ReplicationSubnetGroupIdentifier** *(string) --*

          The identifier of the replication instance subnet group.

        - **ReplicationSubnetGroupDescription** *(string) --*

          A description for the replication subnet group.

        - **VpcId** *(string) --*

          The ID of the VPC.

        - **SubnetGroupStatus** *(string) --*

          The status of the subnet group.

        - **Subnets** *(list) --*

          The subnets that are in the subnet group.

          - *(dict) --*

            - **SubnetIdentifier** *(string) --*

              The subnet identifier.

            - **SubnetAvailabilityZone** *(dict) --*

              The Availability Zone of the subnet.

              - **Name** *(string) --*

                The name of the availability zone.

            - **SubnetStatus** *(string) --*

              The status of the subnet.
    """


_ClientDescribeReplicationTaskAssessmentResultsResponseReplicationTaskAssessmentResultsTypeDef = TypedDict(
    "_ClientDescribeReplicationTaskAssessmentResultsResponseReplicationTaskAssessmentResultsTypeDef",
    {
        "ReplicationTaskIdentifier": str,
        "ReplicationTaskArn": str,
        "ReplicationTaskLastAssessmentDate": datetime,
        "AssessmentStatus": str,
        "AssessmentResultsFile": str,
        "AssessmentResults": str,
        "S3ObjectUrl": str,
    },
    total=False,
)


class ClientDescribeReplicationTaskAssessmentResultsResponseReplicationTaskAssessmentResultsTypeDef(
    _ClientDescribeReplicationTaskAssessmentResultsResponseReplicationTaskAssessmentResultsTypeDef
):
    """
    Type definition for `ClientDescribeReplicationTaskAssessmentResultsResponse` `ReplicationTaskAssessmentResults`

    The task assessment report in JSON format.

    - **ReplicationTaskIdentifier** *(string) --*

      The replication task identifier of the task on which the task assessment was run.

    - **ReplicationTaskArn** *(string) --*

      The Amazon Resource Name (ARN) of the replication task.

    - **ReplicationTaskLastAssessmentDate** *(datetime) --*

      The date the task assessment was completed.

    - **AssessmentStatus** *(string) --*

      The status of the task assessment.

    - **AssessmentResultsFile** *(string) --*

      The file containing the results of the task assessment.

    - **AssessmentResults** *(string) --*

      The task assessment results in JSON format.

    - **S3ObjectUrl** *(string) --*

      The URL of the S3 object containing the task assessment results.
    """


_ClientDescribeReplicationTaskAssessmentResultsResponseTypeDef = TypedDict(
    "_ClientDescribeReplicationTaskAssessmentResultsResponseTypeDef",
    {
        "Marker": str,
        "BucketName": str,
        "ReplicationTaskAssessmentResults": List[
            ClientDescribeReplicationTaskAssessmentResultsResponseReplicationTaskAssessmentResultsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeReplicationTaskAssessmentResultsResponseTypeDef(
    _ClientDescribeReplicationTaskAssessmentResultsResponseTypeDef
):
    """
    Type definition for `ClientDescribeReplicationTaskAssessmentResults` `Response`

    - **Marker** *(string) --*

      An optional pagination token provided by a previous request. If this parameter is specified,
      the response includes only records beyond the marker, up to the value specified by
      ``MaxRecords`` .

    - **BucketName** *(string) --*

      - The Amazon S3 bucket where the task assessment report is located.

    - **ReplicationTaskAssessmentResults** *(list) --*

      The task assessment report.

      - *(dict) --*

        The task assessment report in JSON format.

        - **ReplicationTaskIdentifier** *(string) --*

          The replication task identifier of the task on which the task assessment was run.

        - **ReplicationTaskArn** *(string) --*

          The Amazon Resource Name (ARN) of the replication task.

        - **ReplicationTaskLastAssessmentDate** *(datetime) --*

          The date the task assessment was completed.

        - **AssessmentStatus** *(string) --*

          The status of the task assessment.

        - **AssessmentResultsFile** *(string) --*

          The file containing the results of the task assessment.

        - **AssessmentResults** *(string) --*

          The task assessment results in JSON format.

        - **S3ObjectUrl** *(string) --*

          The URL of the S3 object containing the task assessment results.
    """


_ClientDescribeReplicationTasksFiltersTypeDef = TypedDict(
    "_ClientDescribeReplicationTasksFiltersTypeDef", {"Name": str, "Values": List[str]}
)


class ClientDescribeReplicationTasksFiltersTypeDef(
    _ClientDescribeReplicationTasksFiltersTypeDef
):
    """
    Type definition for `ClientDescribeReplicationTasks` `Filters`

    - **Name** *(string) --* **[REQUIRED]**

      The name of the filter.

    - **Values** *(list) --* **[REQUIRED]**

      The filter value.

      - *(string) --*
    """


_ClientDescribeSchemasResponseTypeDef = TypedDict(
    "_ClientDescribeSchemasResponseTypeDef",
    {"Marker": str, "Schemas": List[str]},
    total=False,
)


class ClientDescribeSchemasResponseTypeDef(_ClientDescribeSchemasResponseTypeDef):
    """
    Type definition for `ClientDescribeSchemas` `Response`

    - **Marker** *(string) --*

      An optional pagination token provided by a previous request. If this parameter is specified,
      the response includes only records beyond the marker, up to the value specified by
      ``MaxRecords`` .

    - **Schemas** *(list) --*

      The described schema.

      - *(string) --*
    """


_ClientDescribeTableStatisticsFiltersTypeDef = TypedDict(
    "_ClientDescribeTableStatisticsFiltersTypeDef", {"Name": str, "Values": List[str]}
)


class ClientDescribeTableStatisticsFiltersTypeDef(
    _ClientDescribeTableStatisticsFiltersTypeDef
):
    """
    Type definition for `ClientDescribeTableStatistics` `Filters`

    - **Name** *(string) --* **[REQUIRED]**

      The name of the filter.

    - **Values** *(list) --* **[REQUIRED]**

      The filter value.

      - *(string) --*
    """


_ClientDescribeTableStatisticsResponseTableStatisticsTypeDef = TypedDict(
    "_ClientDescribeTableStatisticsResponseTableStatisticsTypeDef",
    {
        "SchemaName": str,
        "TableName": str,
        "Inserts": int,
        "Deletes": int,
        "Updates": int,
        "Ddls": int,
        "FullLoadRows": int,
        "FullLoadCondtnlChkFailedRows": int,
        "FullLoadErrorRows": int,
        "LastUpdateTime": datetime,
        "TableState": str,
        "ValidationPendingRecords": int,
        "ValidationFailedRecords": int,
        "ValidationSuspendedRecords": int,
        "ValidationState": str,
        "ValidationStateDetails": str,
    },
    total=False,
)


class ClientDescribeTableStatisticsResponseTableStatisticsTypeDef(
    _ClientDescribeTableStatisticsResponseTableStatisticsTypeDef
):
    """
    Type definition for `ClientDescribeTableStatisticsResponse` `TableStatistics`

    - **SchemaName** *(string) --*

      The schema name.

    - **TableName** *(string) --*

      The name of the table.

    - **Inserts** *(integer) --*

      The number of insert actions performed on a table.

    - **Deletes** *(integer) --*

      The number of delete actions performed on a table.

    - **Updates** *(integer) --*

      The number of update actions performed on a table.

    - **Ddls** *(integer) --*

      The Data Definition Language (DDL) used to build and modify the structure of your tables.

    - **FullLoadRows** *(integer) --*

      The number of rows added during the Full Load operation.

    - **FullLoadCondtnlChkFailedRows** *(integer) --*

      The number of rows that failed conditional checks during the Full Load operation (valid
      only for DynamoDB as a target migrations).

    - **FullLoadErrorRows** *(integer) --*

      The number of rows that failed to load during the Full Load operation (valid only for
      DynamoDB as a target migrations).

    - **LastUpdateTime** *(datetime) --*

      The last time the table was updated.

    - **TableState** *(string) --*

      The state of the tables described.

      Valid states: Table does not exist | Before load | Full load | Table completed | Table
      cancelled | Table error | Table all | Table updates | Table is being reloaded

    - **ValidationPendingRecords** *(integer) --*

      The number of records that have yet to be validated.

    - **ValidationFailedRecords** *(integer) --*

      The number of records that failed validation.

    - **ValidationSuspendedRecords** *(integer) --*

      The number of records that could not be validated.

    - **ValidationState** *(string) --*

      The validation state of the table.

      The parameter can have the following values

      * Not enabled—Validation is not enabled for the table in the migration task.

      * Pending records—Some records in the table are waiting for validation.

      * Mismatched records—Some records in the table do not match between the source and target.

      * Suspended records—Some records in the table could not be validated.

      * No primary key—The table could not be validated because it had no primary key.

      * Table error—The table was not validated because it was in an error state and some data
      was not migrated.

      * Validated—All rows in the table were validated. If the table is updated, the status can
      change from Validated.

      * Error—The table could not be validated because of an unexpected error.

    - **ValidationStateDetails** *(string) --*

      Additional details about the state of validation.
    """


_ClientDescribeTableStatisticsResponseTypeDef = TypedDict(
    "_ClientDescribeTableStatisticsResponseTypeDef",
    {
        "ReplicationTaskArn": str,
        "TableStatistics": List[
            ClientDescribeTableStatisticsResponseTableStatisticsTypeDef
        ],
        "Marker": str,
    },
    total=False,
)


class ClientDescribeTableStatisticsResponseTypeDef(
    _ClientDescribeTableStatisticsResponseTypeDef
):
    """
    Type definition for `ClientDescribeTableStatistics` `Response`

    - **ReplicationTaskArn** *(string) --*

      The Amazon Resource Name (ARN) of the replication task.

    - **TableStatistics** *(list) --*

      The table statistics.

      - *(dict) --*

        - **SchemaName** *(string) --*

          The schema name.

        - **TableName** *(string) --*

          The name of the table.

        - **Inserts** *(integer) --*

          The number of insert actions performed on a table.

        - **Deletes** *(integer) --*

          The number of delete actions performed on a table.

        - **Updates** *(integer) --*

          The number of update actions performed on a table.

        - **Ddls** *(integer) --*

          The Data Definition Language (DDL) used to build and modify the structure of your tables.

        - **FullLoadRows** *(integer) --*

          The number of rows added during the Full Load operation.

        - **FullLoadCondtnlChkFailedRows** *(integer) --*

          The number of rows that failed conditional checks during the Full Load operation (valid
          only for DynamoDB as a target migrations).

        - **FullLoadErrorRows** *(integer) --*

          The number of rows that failed to load during the Full Load operation (valid only for
          DynamoDB as a target migrations).

        - **LastUpdateTime** *(datetime) --*

          The last time the table was updated.

        - **TableState** *(string) --*

          The state of the tables described.

          Valid states: Table does not exist | Before load | Full load | Table completed | Table
          cancelled | Table error | Table all | Table updates | Table is being reloaded

        - **ValidationPendingRecords** *(integer) --*

          The number of records that have yet to be validated.

        - **ValidationFailedRecords** *(integer) --*

          The number of records that failed validation.

        - **ValidationSuspendedRecords** *(integer) --*

          The number of records that could not be validated.

        - **ValidationState** *(string) --*

          The validation state of the table.

          The parameter can have the following values

          * Not enabled—Validation is not enabled for the table in the migration task.

          * Pending records—Some records in the table are waiting for validation.

          * Mismatched records—Some records in the table do not match between the source and target.

          * Suspended records—Some records in the table could not be validated.

          * No primary key—The table could not be validated because it had no primary key.

          * Table error—The table was not validated because it was in an error state and some data
          was not migrated.

          * Validated—All rows in the table were validated. If the table is updated, the status can
          change from Validated.

          * Error—The table could not be validated because of an unexpected error.

        - **ValidationStateDetails** *(string) --*

          Additional details about the state of validation.

    - **Marker** *(string) --*

      An optional pagination token provided by a previous request. If this parameter is specified,
      the response includes only records beyond the marker, up to the value specified by
      ``MaxRecords`` .
    """


_ClientImportCertificateResponseCertificateTypeDef = TypedDict(
    "_ClientImportCertificateResponseCertificateTypeDef",
    {
        "CertificateIdentifier": str,
        "CertificateCreationDate": datetime,
        "CertificatePem": str,
        "CertificateWallet": bytes,
        "CertificateArn": str,
        "CertificateOwner": str,
        "ValidFromDate": datetime,
        "ValidToDate": datetime,
        "SigningAlgorithm": str,
        "KeyLength": int,
    },
    total=False,
)


class ClientImportCertificateResponseCertificateTypeDef(
    _ClientImportCertificateResponseCertificateTypeDef
):
    """
    Type definition for `ClientImportCertificateResponse` `Certificate`

    The certificate to be uploaded.

    - **CertificateIdentifier** *(string) --*

      A customer-assigned name for the certificate. Identifiers must begin with a letter; must
      contain only ASCII letters, digits, and hyphens; and must not end with a hyphen or contain
      two consecutive hyphens.

    - **CertificateCreationDate** *(datetime) --*

      The date that the certificate was created.

    - **CertificatePem** *(string) --*

      The contents of a ``.pem`` file, which contains an X.509 certificate.

    - **CertificateWallet** *(bytes) --*

      The location of an imported Oracle Wallet certificate for use with SSL.

    - **CertificateArn** *(string) --*

      The Amazon Resource Name (ARN) for the certificate.

    - **CertificateOwner** *(string) --*

      The owner of the certificate.

    - **ValidFromDate** *(datetime) --*

      The beginning date that the certificate is valid.

    - **ValidToDate** *(datetime) --*

      The final date that the certificate is valid.

    - **SigningAlgorithm** *(string) --*

      The signing algorithm for the certificate.

    - **KeyLength** *(integer) --*

      The key length of the cryptographic algorithm being used.
    """


_ClientImportCertificateResponseTypeDef = TypedDict(
    "_ClientImportCertificateResponseTypeDef",
    {"Certificate": ClientImportCertificateResponseCertificateTypeDef},
    total=False,
)


class ClientImportCertificateResponseTypeDef(_ClientImportCertificateResponseTypeDef):
    """
    Type definition for `ClientImportCertificate` `Response`

    - **Certificate** *(dict) --*

      The certificate to be uploaded.

      - **CertificateIdentifier** *(string) --*

        A customer-assigned name for the certificate. Identifiers must begin with a letter; must
        contain only ASCII letters, digits, and hyphens; and must not end with a hyphen or contain
        two consecutive hyphens.

      - **CertificateCreationDate** *(datetime) --*

        The date that the certificate was created.

      - **CertificatePem** *(string) --*

        The contents of a ``.pem`` file, which contains an X.509 certificate.

      - **CertificateWallet** *(bytes) --*

        The location of an imported Oracle Wallet certificate for use with SSL.

      - **CertificateArn** *(string) --*

        The Amazon Resource Name (ARN) for the certificate.

      - **CertificateOwner** *(string) --*

        The owner of the certificate.

      - **ValidFromDate** *(datetime) --*

        The beginning date that the certificate is valid.

      - **ValidToDate** *(datetime) --*

        The final date that the certificate is valid.

      - **SigningAlgorithm** *(string) --*

        The signing algorithm for the certificate.

      - **KeyLength** *(integer) --*

        The key length of the cryptographic algorithm being used.
    """


_ClientImportCertificateTagsTypeDef = TypedDict(
    "_ClientImportCertificateTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientImportCertificateTagsTypeDef(_ClientImportCertificateTagsTypeDef):
    """
    Type definition for `ClientImportCertificate` `Tags`

    - **Key** *(string) --*

      A key is the required name of the tag. The string value can be from 1 to 128 Unicode
      characters in length and cannot be prefixed with "aws:" or "dms:". The string can only
      contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-'
      (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").

    - **Value** *(string) --*

      A value is the optional value of the tag. The string value can be from 1 to 256 Unicode
      characters in length and cannot be prefixed with "aws:" or "dms:". The string can only
      contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-'
      (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientListTagsForResourceResponseTagListTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTagListTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientListTagsForResourceResponseTagListTypeDef(
    _ClientListTagsForResourceResponseTagListTypeDef
):
    """
    Type definition for `ClientListTagsForResourceResponse` `TagList`

    - **Key** *(string) --*

      A key is the required name of the tag. The string value can be from 1 to 128 Unicode
      characters in length and cannot be prefixed with "aws:" or "dms:". The string can only
      contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+',
      '-' (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").

    - **Value** *(string) --*

      A value is the optional value of the tag. The string value can be from 1 to 256 Unicode
      characters in length and cannot be prefixed with "aws:" or "dms:". The string can only
      contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+',
      '-' (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef",
    {"TagList": List[ClientListTagsForResourceResponseTagListTypeDef]},
    total=False,
)


class ClientListTagsForResourceResponseTypeDef(
    _ClientListTagsForResourceResponseTypeDef
):
    """
    Type definition for `ClientListTagsForResource` `Response`

    - **TagList** *(list) --*

      A list of tags for the resource.

      - *(dict) --*

        - **Key** *(string) --*

          A key is the required name of the tag. The string value can be from 1 to 128 Unicode
          characters in length and cannot be prefixed with "aws:" or "dms:". The string can only
          contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+',
          '-' (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").

        - **Value** *(string) --*

          A value is the optional value of the tag. The string value can be from 1 to 256 Unicode
          characters in length and cannot be prefixed with "aws:" or "dms:". The string can only
          contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+',
          '-' (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientModifyEndpointDmsTransferSettingsTypeDef = TypedDict(
    "_ClientModifyEndpointDmsTransferSettingsTypeDef",
    {"ServiceAccessRoleArn": str, "BucketName": str},
    total=False,
)


class ClientModifyEndpointDmsTransferSettingsTypeDef(
    _ClientModifyEndpointDmsTransferSettingsTypeDef
):
    """
    Type definition for `ClientModifyEndpoint` `DmsTransferSettings`

    The settings in JSON format for the DMS transfer type of source endpoint.

    Attributes include the following:

    * serviceAccessRoleArn - The IAM role that has permission to access the Amazon S3 bucket.

    * BucketName - The name of the S3 bucket to use.

    * compressionType - An optional parameter to use GZIP to compress the target files. Set to NONE
    (the default) or do not use to leave the files uncompressed.

    Shorthand syntax: ServiceAccessRoleArn=string ,BucketName=string,CompressionType=string

    JSON syntax:

    { "ServiceAccessRoleArn": "string", "BucketName": "string", "CompressionType": "none"|"gzip" }

    - **ServiceAccessRoleArn** *(string) --*

      The IAM role that has permission to access the Amazon S3 bucket.

    - **BucketName** *(string) --*

      The name of the S3 bucket to use.
    """


_ClientModifyEndpointDynamoDbSettingsTypeDef = TypedDict(
    "_ClientModifyEndpointDynamoDbSettingsTypeDef", {"ServiceAccessRoleArn": str}
)


class ClientModifyEndpointDynamoDbSettingsTypeDef(
    _ClientModifyEndpointDynamoDbSettingsTypeDef
):
    """
    Type definition for `ClientModifyEndpoint` `DynamoDbSettings`

    Settings in JSON format for the target Amazon DynamoDB endpoint. For more information about the
    available settings, see `Using Object Mapping to Migrate Data to DynamoDB
    <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.DynamoDB.html>`__ in the *AWS
    Database Migration Service User Guide.*

    - **ServiceAccessRoleArn** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) used by the service access IAM role.
    """


_RequiredClientModifyEndpointElasticsearchSettingsTypeDef = TypedDict(
    "_RequiredClientModifyEndpointElasticsearchSettingsTypeDef",
    {"ServiceAccessRoleArn": str, "EndpointUri": str},
)
_OptionalClientModifyEndpointElasticsearchSettingsTypeDef = TypedDict(
    "_OptionalClientModifyEndpointElasticsearchSettingsTypeDef",
    {"FullLoadErrorPercentage": int, "ErrorRetryDuration": int},
    total=False,
)


class ClientModifyEndpointElasticsearchSettingsTypeDef(
    _RequiredClientModifyEndpointElasticsearchSettingsTypeDef,
    _OptionalClientModifyEndpointElasticsearchSettingsTypeDef,
):
    """
    Type definition for `ClientModifyEndpoint` `ElasticsearchSettings`

    Settings in JSON format for the target Elasticsearch endpoint. For more information about the
    available settings, see `Extra Connection Attributes When Using Elasticsearch as a Target for AWS
    DMS
    <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Elasticsearch.html#CHAP_Target.Elasticsearch.Configuration>`__
    in the *AWS Database Migration User Guide.*

    - **ServiceAccessRoleArn** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) used by service to access the IAM role.

    - **EndpointUri** *(string) --* **[REQUIRED]**

      The endpoint for the Elasticsearch cluster.

    - **FullLoadErrorPercentage** *(integer) --*

      The maximum percentage of records that can fail to be written before a full load operation
      stops.

    - **ErrorRetryDuration** *(integer) --*

      The maximum number of seconds that DMS retries failed API requests to the Elasticsearch cluster.
    """


_ClientModifyEndpointKinesisSettingsTypeDef = TypedDict(
    "_ClientModifyEndpointKinesisSettingsTypeDef",
    {"StreamArn": str, "MessageFormat": str, "ServiceAccessRoleArn": str},
    total=False,
)


class ClientModifyEndpointKinesisSettingsTypeDef(
    _ClientModifyEndpointKinesisSettingsTypeDef
):
    """
    Type definition for `ClientModifyEndpoint` `KinesisSettings`

    Settings in JSON format for the target Amazon Kinesis Data Streams endpoint. For more information
    about the available settings, see `Using Object Mapping to Migrate Data to a Kinesis Data Stream
    <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Kinesis.html#CHAP_Target.Kinesis.ObjectMapping>`__
    in the *AWS Database Migration User Guide.*

    - **StreamArn** *(string) --*

      The Amazon Resource Name (ARN) for the Amazon Kinesis Data Streams endpoint.

    - **MessageFormat** *(string) --*

      The output format for the records created on the endpoint. The message format is ``JSON`` .

    - **ServiceAccessRoleArn** *(string) --*

      The Amazon Resource Name (ARN) for the IAM role that DMS uses to write to the Amazon Kinesis
      data stream.
    """


_ClientModifyEndpointMongoDbSettingsTypeDef = TypedDict(
    "_ClientModifyEndpointMongoDbSettingsTypeDef",
    {
        "Username": str,
        "Password": str,
        "ServerName": str,
        "Port": int,
        "DatabaseName": str,
        "AuthType": str,
        "AuthMechanism": str,
        "NestingLevel": str,
        "ExtractDocId": str,
        "DocsToInvestigate": str,
        "AuthSource": str,
        "KmsKeyId": str,
    },
    total=False,
)


class ClientModifyEndpointMongoDbSettingsTypeDef(
    _ClientModifyEndpointMongoDbSettingsTypeDef
):
    """
    Type definition for `ClientModifyEndpoint` `MongoDbSettings`

    Settings in JSON format for the source MongoDB endpoint. For more information about the available
    settings, see the configuration properties section in `Using MongoDB as a Target for AWS Database
    Migration Service <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MongoDB.html>`__
    in the *AWS Database Migration Service User Guide.*

    - **Username** *(string) --*

      The user name you use to access the MongoDB source endpoint.

    - **Password** *(string) --*

      The password for the user account you use to access the MongoDB source endpoint.

    - **ServerName** *(string) --*

      The name of the server on the MongoDB source endpoint.

    - **Port** *(integer) --*

      The port value for the MongoDB source endpoint.

    - **DatabaseName** *(string) --*

      The database name on the MongoDB source endpoint.

    - **AuthType** *(string) --*

      The authentication type you use to access the MongoDB source endpoint.

      Valid values: NO, PASSWORD

      When NO is selected, user name and password parameters are not used and can be empty.

    - **AuthMechanism** *(string) --*

      The authentication mechanism you use to access the MongoDB source endpoint.

      Valid values: DEFAULT, MONGODB_CR, SCRAM_SHA_1

      DEFAULT – For MongoDB version 2.x, use MONGODB_CR. For MongoDB version 3.x, use SCRAM_SHA_1.
      This setting is not used when authType=No.

    - **NestingLevel** *(string) --*

      Specifies either document or table mode.

      Valid values: NONE, ONE

      Default value is NONE. Specify NONE to use document mode. Specify ONE to use table mode.

    - **ExtractDocId** *(string) --*

      Specifies the document ID. Use this setting when ``NestingLevel`` is set to NONE.

      Default value is false.

    - **DocsToInvestigate** *(string) --*

      Indicates the number of documents to preview to determine the document organization. Use this
      setting when ``NestingLevel`` is set to ONE.

      Must be a positive value greater than 0. Default value is 1000.

    - **AuthSource** *(string) --*

      The MongoDB database name. This setting is not used when ``authType=NO`` .

      The default is admin.

    - **KmsKeyId** *(string) --*

      The AWS KMS key identifier that is used to encrypt the content on the replication instance. If
      you don't specify a value for the ``KmsKeyId`` parameter, then AWS DMS uses your default
      encryption key. AWS KMS creates the default encryption key for your AWS account. Your AWS
      account has a different default encryption key for each AWS Region.
    """


_ClientModifyEndpointRedshiftSettingsTypeDef = TypedDict(
    "_ClientModifyEndpointRedshiftSettingsTypeDef",
    {
        "AcceptAnyDate": bool,
        "AfterConnectScript": str,
        "BucketFolder": str,
        "BucketName": str,
        "ConnectionTimeout": int,
        "DatabaseName": str,
        "DateFormat": str,
        "EmptyAsNull": bool,
        "EncryptionMode": str,
        "FileTransferUploadStreams": int,
        "LoadTimeout": int,
        "MaxFileSize": int,
        "Password": str,
        "Port": int,
        "RemoveQuotes": bool,
        "ReplaceInvalidChars": str,
        "ReplaceChars": str,
        "ServerName": str,
        "ServiceAccessRoleArn": str,
        "ServerSideEncryptionKmsKeyId": str,
        "TimeFormat": str,
        "TrimBlanks": bool,
        "TruncateColumns": bool,
        "Username": str,
        "WriteBufferSize": int,
    },
    total=False,
)


class ClientModifyEndpointRedshiftSettingsTypeDef(
    _ClientModifyEndpointRedshiftSettingsTypeDef
):
    """
    Type definition for `ClientModifyEndpoint` `RedshiftSettings`

    - **AcceptAnyDate** *(boolean) --*

      A value that indicates to allow any date format, including invalid formats such as 00/00/00
      00:00:00, to be loaded without generating an error. You can choose ``true`` or ``false`` (the
      default).

      This parameter applies only to TIMESTAMP and DATE columns. Always use ACCEPTANYDATE with the
      DATEFORMAT parameter. If the date format for the data doesn't match the DATEFORMAT
      specification, Amazon Redshift inserts a NULL value into that field.

    - **AfterConnectScript** *(string) --*

      Code to run after connecting. This parameter should contain the code itself, not the name of a
      file containing the code.

    - **BucketFolder** *(string) --*

      The location where the comma-separated value (.csv) files are stored before being uploaded to
      the S3 bucket.

    - **BucketName** *(string) --*

      The name of the S3 bucket you want to use

    - **ConnectionTimeout** *(integer) --*

      A value that sets the amount of time to wait (in milliseconds) before timing out, beginning
      from when you initially establish a connection.

    - **DatabaseName** *(string) --*

      The name of the Amazon Redshift data warehouse (service) that you are working with.

    - **DateFormat** *(string) --*

      The date format that you are using. Valid values are ``auto`` (case-sensitive), your date
      format string enclosed in quotes, or NULL. If this parameter is left unset (NULL), it defaults
      to a format of 'YYYY-MM-DD'. Using ``auto`` recognizes most strings, even some that aren't
      supported when you use a date format string.

      If your date and time values use formats different from each other, set this to ``auto`` .

    - **EmptyAsNull** *(boolean) --*

      A value that specifies whether AWS DMS should migrate empty CHAR and VARCHAR fields as NULL. A
      value of ``true`` sets empty CHAR and VARCHAR fields to null. The default is ``false`` .

    - **EncryptionMode** *(string) --*

      The type of server-side encryption that you want to use for your data. This encryption type is
      part of the endpoint settings or the extra connections attributes for Amazon S3. You can choose
      either ``SSE_S3`` (the default) or ``SSE_KMS`` . To use ``SSE_S3`` , create an AWS Identity and
      Access Management (IAM) role with a policy that allows ``"arn:aws:s3:::*"`` to use the
      following actions: ``"s3:PutObject", "s3:ListBucket"``

    - **FileTransferUploadStreams** *(integer) --*

      The number of threads used to upload a single file. This parameter accepts a value from 1
      through 64. It defaults to 10.

    - **LoadTimeout** *(integer) --*

      The amount of time to wait (in milliseconds) before timing out, beginning from when you begin
      loading.

    - **MaxFileSize** *(integer) --*

      The maximum size (in KB) of any .csv file used to transfer data to Amazon Redshift. This
      accepts a value from 1 through 1,048,576. It defaults to 32,768 KB (32 MB).

    - **Password** *(string) --*

      The password for the user named in the ``username`` property.

    - **Port** *(integer) --*

      The port number for Amazon Redshift. The default value is 5439.

    - **RemoveQuotes** *(boolean) --*

      A value that specifies to remove surrounding quotation marks from strings in the incoming data.
      All characters within the quotation marks, including delimiters, are retained. Choose ``true``
      to remove quotation marks. The default is ``false`` .

    - **ReplaceInvalidChars** *(string) --*

      A list of characters that you want to replace. Use with ``ReplaceChars`` .

    - **ReplaceChars** *(string) --*

      A value that specifies to replaces the invalid characters specified in ``ReplaceInvalidChars``
      , substituting the specified characters instead. The default is ``"?"`` .

    - **ServerName** *(string) --*

      The name of the Amazon Redshift cluster you are using.

    - **ServiceAccessRoleArn** *(string) --*

      The Amazon Resource Name (ARN) of the IAM role that has access to the Amazon Redshift service.

    - **ServerSideEncryptionKmsKeyId** *(string) --*

      The AWS KMS key ID. If you are using ``SSE_KMS`` for the ``EncryptionMode`` , provide this key
      ID. The key that you use needs an attached policy that enables IAM user permissions and allows
      use of the key.

    - **TimeFormat** *(string) --*

      The time format that you want to use. Valid values are ``auto`` (case-sensitive),
      ``'timeformat_string'`` , ``'epochsecs'`` , or ``'epochmillisecs'`` . It defaults to 10. Using
      ``auto`` recognizes most strings, even some that aren't supported when you use a time format
      string.

      If your date and time values use formats different from each other, set this parameter to
      ``auto`` .

    - **TrimBlanks** *(boolean) --*

      A value that specifies to remove the trailing white space characters from a VARCHAR string.
      This parameter applies only to columns with a VARCHAR data type. Choose ``true`` to remove
      unneeded white space. The default is ``false`` .

    - **TruncateColumns** *(boolean) --*

      A value that specifies to truncate data in columns to the appropriate number of characters, so
      that the data fits in the column. This parameter applies only to columns with a VARCHAR or CHAR
      data type, and rows with a size of 4 MB or less. Choose ``true`` to truncate data. The default
      is ``false`` .

    - **Username** *(string) --*

      An Amazon Redshift user name for a registered user.

    - **WriteBufferSize** *(integer) --*

      The size of the write buffer to use in rows. Valid values range from 1 through 2,048. The
      default is 1,024. Use this setting to tune performance.
    """


_ClientModifyEndpointResponseEndpointDmsTransferSettingsTypeDef = TypedDict(
    "_ClientModifyEndpointResponseEndpointDmsTransferSettingsTypeDef",
    {"ServiceAccessRoleArn": str, "BucketName": str},
    total=False,
)


class ClientModifyEndpointResponseEndpointDmsTransferSettingsTypeDef(
    _ClientModifyEndpointResponseEndpointDmsTransferSettingsTypeDef
):
    """
    Type definition for `ClientModifyEndpointResponseEndpoint` `DmsTransferSettings`

    The settings in JSON format for the DMS transfer type of source endpoint.

    Possible settings include the following:

    * ``ServiceAccessRoleArn`` - The IAM role that has permission to access the Amazon S3
    bucket.

    * ``BucketName`` - The name of the S3 bucket to use.

    * ``CompressionType`` - An optional parameter to use GZIP to compress the target files. To
    use GZIP, set this value to ``NONE`` (the default). To keep the files uncompressed, don't
    use this value.

    Shorthand syntax for these settings is as follows:
    ``ServiceAccessRoleArn=string,BucketName=string,CompressionType=string``

    JSON syntax for these settings is as follows: ``{ "ServiceAccessRoleArn": "string",
    "BucketName": "string", "CompressionType": "none"|"gzip" }``

    - **ServiceAccessRoleArn** *(string) --*

      The IAM role that has permission to access the Amazon S3 bucket.

    - **BucketName** *(string) --*

      The name of the S3 bucket to use.
    """


_ClientModifyEndpointResponseEndpointDynamoDbSettingsTypeDef = TypedDict(
    "_ClientModifyEndpointResponseEndpointDynamoDbSettingsTypeDef",
    {"ServiceAccessRoleArn": str},
    total=False,
)


class ClientModifyEndpointResponseEndpointDynamoDbSettingsTypeDef(
    _ClientModifyEndpointResponseEndpointDynamoDbSettingsTypeDef
):
    """
    Type definition for `ClientModifyEndpointResponseEndpoint` `DynamoDbSettings`

    The settings for the target DynamoDB database. For more information, see the
    ``DynamoDBSettings`` structure.

    - **ServiceAccessRoleArn** *(string) --*

      The Amazon Resource Name (ARN) used by the service access IAM role.
    """


_ClientModifyEndpointResponseEndpointElasticsearchSettingsTypeDef = TypedDict(
    "_ClientModifyEndpointResponseEndpointElasticsearchSettingsTypeDef",
    {
        "ServiceAccessRoleArn": str,
        "EndpointUri": str,
        "FullLoadErrorPercentage": int,
        "ErrorRetryDuration": int,
    },
    total=False,
)


class ClientModifyEndpointResponseEndpointElasticsearchSettingsTypeDef(
    _ClientModifyEndpointResponseEndpointElasticsearchSettingsTypeDef
):
    """
    Type definition for `ClientModifyEndpointResponseEndpoint` `ElasticsearchSettings`

    The settings for the Elasticsearch source endpoint. For more information, see the
    ``ElasticsearchSettings`` structure.

    - **ServiceAccessRoleArn** *(string) --*

      The Amazon Resource Name (ARN) used by service to access the IAM role.

    - **EndpointUri** *(string) --*

      The endpoint for the Elasticsearch cluster.

    - **FullLoadErrorPercentage** *(integer) --*

      The maximum percentage of records that can fail to be written before a full load
      operation stops.

    - **ErrorRetryDuration** *(integer) --*

      The maximum number of seconds that DMS retries failed API requests to the Elasticsearch
      cluster.
    """


_ClientModifyEndpointResponseEndpointKinesisSettingsTypeDef = TypedDict(
    "_ClientModifyEndpointResponseEndpointKinesisSettingsTypeDef",
    {"StreamArn": str, "MessageFormat": str, "ServiceAccessRoleArn": str},
    total=False,
)


class ClientModifyEndpointResponseEndpointKinesisSettingsTypeDef(
    _ClientModifyEndpointResponseEndpointKinesisSettingsTypeDef
):
    """
    Type definition for `ClientModifyEndpointResponseEndpoint` `KinesisSettings`

    The settings for the Amazon Kinesis source endpoint. For more information, see the
    ``KinesisSettings`` structure.

    - **StreamArn** *(string) --*

      The Amazon Resource Name (ARN) for the Amazon Kinesis Data Streams endpoint.

    - **MessageFormat** *(string) --*

      The output format for the records created on the endpoint. The message format is ``JSON``
      .

    - **ServiceAccessRoleArn** *(string) --*

      The Amazon Resource Name (ARN) for the IAM role that DMS uses to write to the Amazon
      Kinesis data stream.
    """


_ClientModifyEndpointResponseEndpointMongoDbSettingsTypeDef = TypedDict(
    "_ClientModifyEndpointResponseEndpointMongoDbSettingsTypeDef",
    {
        "Username": str,
        "Password": str,
        "ServerName": str,
        "Port": int,
        "DatabaseName": str,
        "AuthType": str,
        "AuthMechanism": str,
        "NestingLevel": str,
        "ExtractDocId": str,
        "DocsToInvestigate": str,
        "AuthSource": str,
        "KmsKeyId": str,
    },
    total=False,
)


class ClientModifyEndpointResponseEndpointMongoDbSettingsTypeDef(
    _ClientModifyEndpointResponseEndpointMongoDbSettingsTypeDef
):
    """
    Type definition for `ClientModifyEndpointResponseEndpoint` `MongoDbSettings`

    The settings for the MongoDB source endpoint. For more information, see the
    ``MongoDbSettings`` structure.

    - **Username** *(string) --*

      The user name you use to access the MongoDB source endpoint.

    - **Password** *(string) --*

      The password for the user account you use to access the MongoDB source endpoint.

    - **ServerName** *(string) --*

      The name of the server on the MongoDB source endpoint.

    - **Port** *(integer) --*

      The port value for the MongoDB source endpoint.

    - **DatabaseName** *(string) --*

      The database name on the MongoDB source endpoint.

    - **AuthType** *(string) --*

      The authentication type you use to access the MongoDB source endpoint.

      Valid values: NO, PASSWORD

      When NO is selected, user name and password parameters are not used and can be empty.

    - **AuthMechanism** *(string) --*

      The authentication mechanism you use to access the MongoDB source endpoint.

      Valid values: DEFAULT, MONGODB_CR, SCRAM_SHA_1

      DEFAULT – For MongoDB version 2.x, use MONGODB_CR. For MongoDB version 3.x, use
      SCRAM_SHA_1. This setting is not used when authType=No.

    - **NestingLevel** *(string) --*

      Specifies either document or table mode.

      Valid values: NONE, ONE

      Default value is NONE. Specify NONE to use document mode. Specify ONE to use table mode.

    - **ExtractDocId** *(string) --*

      Specifies the document ID. Use this setting when ``NestingLevel`` is set to NONE.

      Default value is false.

    - **DocsToInvestigate** *(string) --*

      Indicates the number of documents to preview to determine the document organization. Use
      this setting when ``NestingLevel`` is set to ONE.

      Must be a positive value greater than 0. Default value is 1000.

    - **AuthSource** *(string) --*

      The MongoDB database name. This setting is not used when ``authType=NO`` .

      The default is admin.

    - **KmsKeyId** *(string) --*

      The AWS KMS key identifier that is used to encrypt the content on the replication
      instance. If you don't specify a value for the ``KmsKeyId`` parameter, then AWS DMS uses
      your default encryption key. AWS KMS creates the default encryption key for your AWS
      account. Your AWS account has a different default encryption key for each AWS Region.
    """


_ClientModifyEndpointResponseEndpointRedshiftSettingsTypeDef = TypedDict(
    "_ClientModifyEndpointResponseEndpointRedshiftSettingsTypeDef",
    {
        "AcceptAnyDate": bool,
        "AfterConnectScript": str,
        "BucketFolder": str,
        "BucketName": str,
        "ConnectionTimeout": int,
        "DatabaseName": str,
        "DateFormat": str,
        "EmptyAsNull": bool,
        "EncryptionMode": str,
        "FileTransferUploadStreams": int,
        "LoadTimeout": int,
        "MaxFileSize": int,
        "Password": str,
        "Port": int,
        "RemoveQuotes": bool,
        "ReplaceInvalidChars": str,
        "ReplaceChars": str,
        "ServerName": str,
        "ServiceAccessRoleArn": str,
        "ServerSideEncryptionKmsKeyId": str,
        "TimeFormat": str,
        "TrimBlanks": bool,
        "TruncateColumns": bool,
        "Username": str,
        "WriteBufferSize": int,
    },
    total=False,
)


class ClientModifyEndpointResponseEndpointRedshiftSettingsTypeDef(
    _ClientModifyEndpointResponseEndpointRedshiftSettingsTypeDef
):
    """
    Type definition for `ClientModifyEndpointResponseEndpoint` `RedshiftSettings`

    Settings for the Amazon Redshift endpoint.

    - **AcceptAnyDate** *(boolean) --*

      A value that indicates to allow any date format, including invalid formats such as
      00/00/00 00:00:00, to be loaded without generating an error. You can choose ``true`` or
      ``false`` (the default).

      This parameter applies only to TIMESTAMP and DATE columns. Always use ACCEPTANYDATE with
      the DATEFORMAT parameter. If the date format for the data doesn't match the DATEFORMAT
      specification, Amazon Redshift inserts a NULL value into that field.

    - **AfterConnectScript** *(string) --*

      Code to run after connecting. This parameter should contain the code itself, not the name
      of a file containing the code.

    - **BucketFolder** *(string) --*

      The location where the comma-separated value (.csv) files are stored before being
      uploaded to the S3 bucket.

    - **BucketName** *(string) --*

      The name of the S3 bucket you want to use

    - **ConnectionTimeout** *(integer) --*

      A value that sets the amount of time to wait (in milliseconds) before timing out,
      beginning from when you initially establish a connection.

    - **DatabaseName** *(string) --*

      The name of the Amazon Redshift data warehouse (service) that you are working with.

    - **DateFormat** *(string) --*

      The date format that you are using. Valid values are ``auto`` (case-sensitive), your date
      format string enclosed in quotes, or NULL. If this parameter is left unset (NULL), it
      defaults to a format of 'YYYY-MM-DD'. Using ``auto`` recognizes most strings, even some
      that aren't supported when you use a date format string.

      If your date and time values use formats different from each other, set this to ``auto`` .

    - **EmptyAsNull** *(boolean) --*

      A value that specifies whether AWS DMS should migrate empty CHAR and VARCHAR fields as
      NULL. A value of ``true`` sets empty CHAR and VARCHAR fields to null. The default is
      ``false`` .

    - **EncryptionMode** *(string) --*

      The type of server-side encryption that you want to use for your data. This encryption
      type is part of the endpoint settings or the extra connections attributes for Amazon S3.
      You can choose either ``SSE_S3`` (the default) or ``SSE_KMS`` . To use ``SSE_S3`` ,
      create an AWS Identity and Access Management (IAM) role with a policy that allows
      ``"arn:aws:s3:::*"`` to use the following actions: ``"s3:PutObject", "s3:ListBucket"``

    - **FileTransferUploadStreams** *(integer) --*

      The number of threads used to upload a single file. This parameter accepts a value from 1
      through 64. It defaults to 10.

    - **LoadTimeout** *(integer) --*

      The amount of time to wait (in milliseconds) before timing out, beginning from when you
      begin loading.

    - **MaxFileSize** *(integer) --*

      The maximum size (in KB) of any .csv file used to transfer data to Amazon Redshift. This
      accepts a value from 1 through 1,048,576. It defaults to 32,768 KB (32 MB).

    - **Password** *(string) --*

      The password for the user named in the ``username`` property.

    - **Port** *(integer) --*

      The port number for Amazon Redshift. The default value is 5439.

    - **RemoveQuotes** *(boolean) --*

      A value that specifies to remove surrounding quotation marks from strings in the incoming
      data. All characters within the quotation marks, including delimiters, are retained.
      Choose ``true`` to remove quotation marks. The default is ``false`` .

    - **ReplaceInvalidChars** *(string) --*

      A list of characters that you want to replace. Use with ``ReplaceChars`` .

    - **ReplaceChars** *(string) --*

      A value that specifies to replaces the invalid characters specified in
      ``ReplaceInvalidChars`` , substituting the specified characters instead. The default is
      ``"?"`` .

    - **ServerName** *(string) --*

      The name of the Amazon Redshift cluster you are using.

    - **ServiceAccessRoleArn** *(string) --*

      The Amazon Resource Name (ARN) of the IAM role that has access to the Amazon Redshift
      service.

    - **ServerSideEncryptionKmsKeyId** *(string) --*

      The AWS KMS key ID. If you are using ``SSE_KMS`` for the ``EncryptionMode`` , provide
      this key ID. The key that you use needs an attached policy that enables IAM user
      permissions and allows use of the key.

    - **TimeFormat** *(string) --*

      The time format that you want to use. Valid values are ``auto`` (case-sensitive),
      ``'timeformat_string'`` , ``'epochsecs'`` , or ``'epochmillisecs'`` . It defaults to 10.
      Using ``auto`` recognizes most strings, even some that aren't supported when you use a
      time format string.

      If your date and time values use formats different from each other, set this parameter to
      ``auto`` .

    - **TrimBlanks** *(boolean) --*

      A value that specifies to remove the trailing white space characters from a VARCHAR
      string. This parameter applies only to columns with a VARCHAR data type. Choose ``true``
      to remove unneeded white space. The default is ``false`` .

    - **TruncateColumns** *(boolean) --*

      A value that specifies to truncate data in columns to the appropriate number of
      characters, so that the data fits in the column. This parameter applies only to columns
      with a VARCHAR or CHAR data type, and rows with a size of 4 MB or less. Choose ``true``
      to truncate data. The default is ``false`` .

    - **Username** *(string) --*

      An Amazon Redshift user name for a registered user.

    - **WriteBufferSize** *(integer) --*

      The size of the write buffer to use in rows. Valid values range from 1 through 2,048. The
      default is 1,024. Use this setting to tune performance.
    """


_ClientModifyEndpointResponseEndpointS3SettingsTypeDef = TypedDict(
    "_ClientModifyEndpointResponseEndpointS3SettingsTypeDef",
    {
        "ServiceAccessRoleArn": str,
        "ExternalTableDefinition": str,
        "CsvRowDelimiter": str,
        "CsvDelimiter": str,
        "BucketFolder": str,
        "BucketName": str,
        "CompressionType": str,
        "EncryptionMode": str,
        "ServerSideEncryptionKmsKeyId": str,
        "DataFormat": str,
        "EncodingType": str,
        "DictPageSizeLimit": int,
        "RowGroupLength": int,
        "DataPageSize": int,
        "ParquetVersion": str,
        "EnableStatistics": bool,
        "IncludeOpForFullLoad": bool,
        "CdcInsertsOnly": bool,
        "TimestampColumnName": str,
        "ParquetTimestampInMillisecond": bool,
    },
    total=False,
)


class ClientModifyEndpointResponseEndpointS3SettingsTypeDef(
    _ClientModifyEndpointResponseEndpointS3SettingsTypeDef
):
    """
    Type definition for `ClientModifyEndpointResponseEndpoint` `S3Settings`

    The settings for the S3 target endpoint. For more information, see the ``S3Settings``
    structure.

    - **ServiceAccessRoleArn** *(string) --*

      The Amazon Resource Name (ARN) used by the service access IAM role.

    - **ExternalTableDefinition** *(string) --*

      The external table definition.

    - **CsvRowDelimiter** *(string) --*

      The delimiter used to separate rows in the source files. The default is a carriage return
      (``\\n`` ).

    - **CsvDelimiter** *(string) --*

      The delimiter used to separate columns in the source files. The default is a comma.

    - **BucketFolder** *(string) --*

      An optional parameter to set a folder name in the S3 bucket. If provided, tables are
      created in the path `` *bucketFolder* /*schema_name* /*table_name* /`` . If this
      parameter is not specified, then the path used is `` *schema_name* /*table_name* /`` .

    - **BucketName** *(string) --*

      The name of the S3 bucket.

    - **CompressionType** *(string) --*

      An optional parameter to use GZIP to compress the target files. Set to GZIP to compress
      the target files. Set to NONE (the default) or do not use to leave the files
      uncompressed. Applies to both .csv and .parquet file formats.

    - **EncryptionMode** *(string) --*

      The type of server-side encryption that you want to use for your data. This encryption
      type is part of the endpoint settings or the extra connections attributes for Amazon S3.
      You can choose either ``SSE_S3`` (the default) or ``SSE_KMS`` . To use ``SSE_S3`` , you
      need an AWS Identity and Access Management (IAM) role with permission to allow
      ``"arn:aws:s3:::dms-*"`` to use the following actions:

      * ``s3:CreateBucket``

      * ``s3:ListBucket``

      * ``s3:DeleteBucket``

      * ``s3:GetBucketLocation``

      * ``s3:GetObject``

      * ``s3:PutObject``

      * ``s3:DeleteObject``

      * ``s3:GetObjectVersion``

      * ``s3:GetBucketPolicy``

      * ``s3:PutBucketPolicy``

      * ``s3:DeleteBucketPolicy``

    - **ServerSideEncryptionKmsKeyId** *(string) --*

      If you are using ``SSE_KMS`` for the ``EncryptionMode`` , provide the AWS KMS key ID. The
      key that you use needs an attached policy that enables AWS Identity and Access Management
      (IAM) user permissions and allows use of the key.

      Here is a CLI example: ``aws dms create-endpoint --endpoint-identifier *value*
      --endpoint-type target --engine-name s3 --s3-settings ServiceAccessRoleArn=*value*
      ,BucketFolder=*value* ,BucketName=*value*
      ,EncryptionMode=SSE_KMS,ServerSideEncryptionKmsKeyId=*value* ``

    - **DataFormat** *(string) --*

      The format of the data that you want to use for output. You can choose one of the
      following:

      * ``csv`` : This is a row-based file format with comma-separated values (.csv).

      * ``parquet`` : Apache Parquet (.parquet) is a columnar storage file format that features
      efficient compression and provides faster query response.

    - **EncodingType** *(string) --*

      The type of encoding you are using:

      * ``RLE_DICTIONARY`` uses a combination of bit-packing and run-length encoding to store
      repeated values more efficiently. This is the default.

      * ``PLAIN`` doesn't use encoding at all. Values are stored as they are.

      * ``PLAIN_DICTIONARY`` builds a dictionary of the values encountered in a given column.
      The dictionary is stored in a dictionary page for each column chunk.

    - **DictPageSizeLimit** *(integer) --*

      The maximum size of an encoded dictionary page of a column. If the dictionary page
      exceeds this, this column is stored using an encoding type of ``PLAIN`` . This parameter
      defaults to 1024 * 1024 bytes (1 MiB), the maximum size of a dictionary page before it
      reverts to ``PLAIN`` encoding. This size is used for .parquet file format only.

    - **RowGroupLength** *(integer) --*

      The number of rows in a row group. A smaller row group size provides faster reads. But as
      the number of row groups grows, the slower writes become. This parameter defaults to
      10,000 rows. This number is used for .parquet file format only.

      If you choose a value larger than the maximum, ``RowGroupLength`` is set to the max row
      group length in bytes (64 * 1024 * 1024).

    - **DataPageSize** *(integer) --*

      The size of one data page in bytes. This parameter defaults to 1024 * 1024 bytes (1 MiB).
      This number is used for .parquet file format only.

    - **ParquetVersion** *(string) --*

      The version of the Apache Parquet format that you want to use: ``parquet_1_0`` (the
      default) or ``parquet_2_0`` .

    - **EnableStatistics** *(boolean) --*

      A value that enables statistics for Parquet pages and row groups. Choose ``true`` to
      enable statistics, ``false`` to disable. Statistics include ``NULL`` , ``DISTINCT`` ,
      ``MAX`` , and ``MIN`` values. This parameter defaults to ``true`` . This value is used
      for .parquet file format only.

    - **IncludeOpForFullLoad** *(boolean) --*

      A value that enables a full load to write INSERT operations to the comma-separated value
      (.csv) output files only to indicate how the rows were added to the source database.

      .. note::

        AWS DMS supports the ``IncludeOpForFullLoad`` parameter in versions 3.1.4 and later.

      For full load, records can only be inserted. By default (the ``false`` setting), no
      information is recorded in these output files for a full load to indicate that the rows
      were inserted at the source database. If ``IncludeOpForFullLoad`` is set to ``true`` or
      ``y`` , the INSERT is recorded as an I annotation in the first field of the .csv file.
      This allows the format of your target records from a full load to be consistent with the
      target records from a CDC load.

      .. note::

        This setting works together with the ``CdcInsertsOnly`` parameter for output to .csv
        files only. For more information about how these settings work together, see
        `Indicating Source DB Operations in Migrated S3 Data
        <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring.InsertOps>`__
        in the *AWS Database Migration Service User Guide.* .

    - **CdcInsertsOnly** *(boolean) --*

      A value that enables a change data capture (CDC) load to write only INSERT operations to
      .csv or columnar storage (.parquet) output files. By default (the ``false`` setting), the
      first field in a .csv or .parquet record contains the letter I (INSERT), U (UPDATE), or D
      (DELETE). These values indicate whether the row was inserted, updated, or deleted at the
      source database for a CDC load to the target.

      If ``CdcInsertsOnly`` is set to ``true`` or ``y`` , only INSERTs from the source database
      are migrated to the .csv or .parquet file. For .csv format only, how these INSERTs are
      recorded depends on the value of ``IncludeOpForFullLoad`` . If ``IncludeOpForFullLoad``
      is set to ``true`` , the first field of every CDC record is set to I to indicate the
      INSERT operation at the source. If ``IncludeOpForFullLoad`` is set to ``false`` , every
      CDC record is written without a first field to indicate the INSERT operation at the
      source. For more information about how these settings work together, see `Indicating
      Source DB Operations in Migrated S3 Data
      <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring.InsertOps>`__
      in the *AWS Database Migration Service User Guide.* .

      .. note::

        AWS DMS supports this interaction between the ``CdcInsertsOnly`` and
        ``IncludeOpForFullLoad`` parameters in versions 3.1.4 and later.

    - **TimestampColumnName** *(string) --*

      A value that when nonblank causes AWS DMS to add a column with timestamp information to
      the endpoint data for an Amazon S3 target.

      .. note::

        AWS DMS supports the ``TimestampColumnName`` parameter in versions 3.1.4 and later.

      DMS includes an additional ``STRING`` column in the .csv or .parquet object files of your
      migrated data when you set ``TimestampColumnName`` to a nonblank value.

      For a full load, each row of this timestamp column contains a timestamp for when the data
      was transferred from the source to the target by DMS.

      For a change data capture (CDC) load, each row of the timestamp column contains the
      timestamp for the commit of that row in the source database.

      The string format for this timestamp column value is ``yyyy-MM-dd HH:mm:ss.SSSSSS`` . By
      default, the precision of this value is in microseconds. For a CDC load, the rounding of
      the precision depends on the commit timestamp supported by DMS for the source database.

      When the ``AddColumnName`` parameter is set to ``true`` , DMS also includes a name for
      the timestamp column that you set with ``TimestampColumnName`` .

    - **ParquetTimestampInMillisecond** *(boolean) --*

      A value that specifies the precision of any ``TIMESTAMP`` column values that are written
      to an Amazon S3 object file in .parquet format.

      .. note::

        AWS DMS supports the ``ParquetTimestampInMillisecond`` parameter in versions 3.1.4 and
        later.

      When ``ParquetTimestampInMillisecond`` is set to ``true`` or ``y`` , AWS DMS writes all
      ``TIMESTAMP`` columns in a .parquet formatted file with millisecond precision. Otherwise,
      DMS writes them with microsecond precision.

      Currently, Amazon Athena and AWS Glue can handle only millisecond precision for
      ``TIMESTAMP`` values. Set this parameter to ``true`` for S3 endpoint object files that
      are .parquet formatted only if you plan to query or process the data with Athena or AWS
      Glue.

      .. note::

        AWS DMS writes any ``TIMESTAMP`` column values written to an S3 file in .csv format
        with microsecond precision.

        Setting ``ParquetTimestampInMillisecond`` has no effect on the string format of the
        timestamp column value that is inserted by setting the ``TimestampColumnName``
        parameter.
    """


_ClientModifyEndpointResponseEndpointTypeDef = TypedDict(
    "_ClientModifyEndpointResponseEndpointTypeDef",
    {
        "EndpointIdentifier": str,
        "EndpointType": str,
        "EngineName": str,
        "EngineDisplayName": str,
        "Username": str,
        "ServerName": str,
        "Port": int,
        "DatabaseName": str,
        "ExtraConnectionAttributes": str,
        "Status": str,
        "KmsKeyId": str,
        "EndpointArn": str,
        "CertificateArn": str,
        "SslMode": str,
        "ServiceAccessRoleArn": str,
        "ExternalTableDefinition": str,
        "ExternalId": str,
        "DynamoDbSettings": ClientModifyEndpointResponseEndpointDynamoDbSettingsTypeDef,
        "S3Settings": ClientModifyEndpointResponseEndpointS3SettingsTypeDef,
        "DmsTransferSettings": ClientModifyEndpointResponseEndpointDmsTransferSettingsTypeDef,
        "MongoDbSettings": ClientModifyEndpointResponseEndpointMongoDbSettingsTypeDef,
        "KinesisSettings": ClientModifyEndpointResponseEndpointKinesisSettingsTypeDef,
        "ElasticsearchSettings": ClientModifyEndpointResponseEndpointElasticsearchSettingsTypeDef,
        "RedshiftSettings": ClientModifyEndpointResponseEndpointRedshiftSettingsTypeDef,
    },
    total=False,
)


class ClientModifyEndpointResponseEndpointTypeDef(
    _ClientModifyEndpointResponseEndpointTypeDef
):
    """
    Type definition for `ClientModifyEndpointResponse` `Endpoint`

    The modified endpoint.

    - **EndpointIdentifier** *(string) --*

      The database endpoint identifier. Identifiers must begin with a letter; must contain only
      ASCII letters, digits, and hyphens; and must not end with a hyphen or contain two
      consecutive hyphens.

    - **EndpointType** *(string) --*

      The type of endpoint. Valid values are ``source`` and ``target`` .

    - **EngineName** *(string) --*

      The database engine name. Valid values, depending on the EndpointType, include mysql,
      oracle, postgres, mariadb, aurora, aurora-postgresql, redshift, s3, db2, azuredb, sybase,
      dynamodb, mongodb, and sqlserver.

    - **EngineDisplayName** *(string) --*

      The expanded name for the engine name. For example, if the ``EngineName`` parameter is
      "aurora," this value would be "Amazon Aurora MySQL."

    - **Username** *(string) --*

      The user name used to connect to the endpoint.

    - **ServerName** *(string) --*

      The name of the server at the endpoint.

    - **Port** *(integer) --*

      The port value used to access the endpoint.

    - **DatabaseName** *(string) --*

      The name of the database at the endpoint.

    - **ExtraConnectionAttributes** *(string) --*

      Additional connection attributes used to connect to the endpoint.

    - **Status** *(string) --*

      The status of the endpoint.

    - **KmsKeyId** *(string) --*

      An AWS KMS key identifier that is used to encrypt the connection parameters for the
      endpoint.

      If you don't specify a value for the ``KmsKeyId`` parameter, then AWS DMS uses your default
      encryption key.

      AWS KMS creates the default encryption key for your AWS account. Your AWS account has a
      different default encryption key for each AWS Region.

    - **EndpointArn** *(string) --*

      The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

    - **CertificateArn** *(string) --*

      The Amazon Resource Name (ARN) used for SSL connection to the endpoint.

    - **SslMode** *(string) --*

      The SSL mode used to connect to the endpoint. The default value is ``none`` .

    - **ServiceAccessRoleArn** *(string) --*

      The Amazon Resource Name (ARN) used by the service access IAM role.

    - **ExternalTableDefinition** *(string) --*

      The external table definition.

    - **ExternalId** *(string) --*

      Value returned by a call to CreateEndpoint that can be used for cross-account validation.
      Use it on a subsequent call to CreateEndpoint to create the endpoint with a cross-account.

    - **DynamoDbSettings** *(dict) --*

      The settings for the target DynamoDB database. For more information, see the
      ``DynamoDBSettings`` structure.

      - **ServiceAccessRoleArn** *(string) --*

        The Amazon Resource Name (ARN) used by the service access IAM role.

    - **S3Settings** *(dict) --*

      The settings for the S3 target endpoint. For more information, see the ``S3Settings``
      structure.

      - **ServiceAccessRoleArn** *(string) --*

        The Amazon Resource Name (ARN) used by the service access IAM role.

      - **ExternalTableDefinition** *(string) --*

        The external table definition.

      - **CsvRowDelimiter** *(string) --*

        The delimiter used to separate rows in the source files. The default is a carriage return
        (``\\n`` ).

      - **CsvDelimiter** *(string) --*

        The delimiter used to separate columns in the source files. The default is a comma.

      - **BucketFolder** *(string) --*

        An optional parameter to set a folder name in the S3 bucket. If provided, tables are
        created in the path `` *bucketFolder* /*schema_name* /*table_name* /`` . If this
        parameter is not specified, then the path used is `` *schema_name* /*table_name* /`` .

      - **BucketName** *(string) --*

        The name of the S3 bucket.

      - **CompressionType** *(string) --*

        An optional parameter to use GZIP to compress the target files. Set to GZIP to compress
        the target files. Set to NONE (the default) or do not use to leave the files
        uncompressed. Applies to both .csv and .parquet file formats.

      - **EncryptionMode** *(string) --*

        The type of server-side encryption that you want to use for your data. This encryption
        type is part of the endpoint settings or the extra connections attributes for Amazon S3.
        You can choose either ``SSE_S3`` (the default) or ``SSE_KMS`` . To use ``SSE_S3`` , you
        need an AWS Identity and Access Management (IAM) role with permission to allow
        ``"arn:aws:s3:::dms-*"`` to use the following actions:

        * ``s3:CreateBucket``

        * ``s3:ListBucket``

        * ``s3:DeleteBucket``

        * ``s3:GetBucketLocation``

        * ``s3:GetObject``

        * ``s3:PutObject``

        * ``s3:DeleteObject``

        * ``s3:GetObjectVersion``

        * ``s3:GetBucketPolicy``

        * ``s3:PutBucketPolicy``

        * ``s3:DeleteBucketPolicy``

      - **ServerSideEncryptionKmsKeyId** *(string) --*

        If you are using ``SSE_KMS`` for the ``EncryptionMode`` , provide the AWS KMS key ID. The
        key that you use needs an attached policy that enables AWS Identity and Access Management
        (IAM) user permissions and allows use of the key.

        Here is a CLI example: ``aws dms create-endpoint --endpoint-identifier *value*
        --endpoint-type target --engine-name s3 --s3-settings ServiceAccessRoleArn=*value*
        ,BucketFolder=*value* ,BucketName=*value*
        ,EncryptionMode=SSE_KMS,ServerSideEncryptionKmsKeyId=*value* ``

      - **DataFormat** *(string) --*

        The format of the data that you want to use for output. You can choose one of the
        following:

        * ``csv`` : This is a row-based file format with comma-separated values (.csv).

        * ``parquet`` : Apache Parquet (.parquet) is a columnar storage file format that features
        efficient compression and provides faster query response.

      - **EncodingType** *(string) --*

        The type of encoding you are using:

        * ``RLE_DICTIONARY`` uses a combination of bit-packing and run-length encoding to store
        repeated values more efficiently. This is the default.

        * ``PLAIN`` doesn't use encoding at all. Values are stored as they are.

        * ``PLAIN_DICTIONARY`` builds a dictionary of the values encountered in a given column.
        The dictionary is stored in a dictionary page for each column chunk.

      - **DictPageSizeLimit** *(integer) --*

        The maximum size of an encoded dictionary page of a column. If the dictionary page
        exceeds this, this column is stored using an encoding type of ``PLAIN`` . This parameter
        defaults to 1024 * 1024 bytes (1 MiB), the maximum size of a dictionary page before it
        reverts to ``PLAIN`` encoding. This size is used for .parquet file format only.

      - **RowGroupLength** *(integer) --*

        The number of rows in a row group. A smaller row group size provides faster reads. But as
        the number of row groups grows, the slower writes become. This parameter defaults to
        10,000 rows. This number is used for .parquet file format only.

        If you choose a value larger than the maximum, ``RowGroupLength`` is set to the max row
        group length in bytes (64 * 1024 * 1024).

      - **DataPageSize** *(integer) --*

        The size of one data page in bytes. This parameter defaults to 1024 * 1024 bytes (1 MiB).
        This number is used for .parquet file format only.

      - **ParquetVersion** *(string) --*

        The version of the Apache Parquet format that you want to use: ``parquet_1_0`` (the
        default) or ``parquet_2_0`` .

      - **EnableStatistics** *(boolean) --*

        A value that enables statistics for Parquet pages and row groups. Choose ``true`` to
        enable statistics, ``false`` to disable. Statistics include ``NULL`` , ``DISTINCT`` ,
        ``MAX`` , and ``MIN`` values. This parameter defaults to ``true`` . This value is used
        for .parquet file format only.

      - **IncludeOpForFullLoad** *(boolean) --*

        A value that enables a full load to write INSERT operations to the comma-separated value
        (.csv) output files only to indicate how the rows were added to the source database.

        .. note::

          AWS DMS supports the ``IncludeOpForFullLoad`` parameter in versions 3.1.4 and later.

        For full load, records can only be inserted. By default (the ``false`` setting), no
        information is recorded in these output files for a full load to indicate that the rows
        were inserted at the source database. If ``IncludeOpForFullLoad`` is set to ``true`` or
        ``y`` , the INSERT is recorded as an I annotation in the first field of the .csv file.
        This allows the format of your target records from a full load to be consistent with the
        target records from a CDC load.

        .. note::

          This setting works together with the ``CdcInsertsOnly`` parameter for output to .csv
          files only. For more information about how these settings work together, see
          `Indicating Source DB Operations in Migrated S3 Data
          <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring.InsertOps>`__
          in the *AWS Database Migration Service User Guide.* .

      - **CdcInsertsOnly** *(boolean) --*

        A value that enables a change data capture (CDC) load to write only INSERT operations to
        .csv or columnar storage (.parquet) output files. By default (the ``false`` setting), the
        first field in a .csv or .parquet record contains the letter I (INSERT), U (UPDATE), or D
        (DELETE). These values indicate whether the row was inserted, updated, or deleted at the
        source database for a CDC load to the target.

        If ``CdcInsertsOnly`` is set to ``true`` or ``y`` , only INSERTs from the source database
        are migrated to the .csv or .parquet file. For .csv format only, how these INSERTs are
        recorded depends on the value of ``IncludeOpForFullLoad`` . If ``IncludeOpForFullLoad``
        is set to ``true`` , the first field of every CDC record is set to I to indicate the
        INSERT operation at the source. If ``IncludeOpForFullLoad`` is set to ``false`` , every
        CDC record is written without a first field to indicate the INSERT operation at the
        source. For more information about how these settings work together, see `Indicating
        Source DB Operations in Migrated S3 Data
        <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring.InsertOps>`__
        in the *AWS Database Migration Service User Guide.* .

        .. note::

          AWS DMS supports this interaction between the ``CdcInsertsOnly`` and
          ``IncludeOpForFullLoad`` parameters in versions 3.1.4 and later.

      - **TimestampColumnName** *(string) --*

        A value that when nonblank causes AWS DMS to add a column with timestamp information to
        the endpoint data for an Amazon S3 target.

        .. note::

          AWS DMS supports the ``TimestampColumnName`` parameter in versions 3.1.4 and later.

        DMS includes an additional ``STRING`` column in the .csv or .parquet object files of your
        migrated data when you set ``TimestampColumnName`` to a nonblank value.

        For a full load, each row of this timestamp column contains a timestamp for when the data
        was transferred from the source to the target by DMS.

        For a change data capture (CDC) load, each row of the timestamp column contains the
        timestamp for the commit of that row in the source database.

        The string format for this timestamp column value is ``yyyy-MM-dd HH:mm:ss.SSSSSS`` . By
        default, the precision of this value is in microseconds. For a CDC load, the rounding of
        the precision depends on the commit timestamp supported by DMS for the source database.

        When the ``AddColumnName`` parameter is set to ``true`` , DMS also includes a name for
        the timestamp column that you set with ``TimestampColumnName`` .

      - **ParquetTimestampInMillisecond** *(boolean) --*

        A value that specifies the precision of any ``TIMESTAMP`` column values that are written
        to an Amazon S3 object file in .parquet format.

        .. note::

          AWS DMS supports the ``ParquetTimestampInMillisecond`` parameter in versions 3.1.4 and
          later.

        When ``ParquetTimestampInMillisecond`` is set to ``true`` or ``y`` , AWS DMS writes all
        ``TIMESTAMP`` columns in a .parquet formatted file with millisecond precision. Otherwise,
        DMS writes them with microsecond precision.

        Currently, Amazon Athena and AWS Glue can handle only millisecond precision for
        ``TIMESTAMP`` values. Set this parameter to ``true`` for S3 endpoint object files that
        are .parquet formatted only if you plan to query or process the data with Athena or AWS
        Glue.

        .. note::

          AWS DMS writes any ``TIMESTAMP`` column values written to an S3 file in .csv format
          with microsecond precision.

          Setting ``ParquetTimestampInMillisecond`` has no effect on the string format of the
          timestamp column value that is inserted by setting the ``TimestampColumnName``
          parameter.

    - **DmsTransferSettings** *(dict) --*

      The settings in JSON format for the DMS transfer type of source endpoint.

      Possible settings include the following:

      * ``ServiceAccessRoleArn`` - The IAM role that has permission to access the Amazon S3
      bucket.

      * ``BucketName`` - The name of the S3 bucket to use.

      * ``CompressionType`` - An optional parameter to use GZIP to compress the target files. To
      use GZIP, set this value to ``NONE`` (the default). To keep the files uncompressed, don't
      use this value.

      Shorthand syntax for these settings is as follows:
      ``ServiceAccessRoleArn=string,BucketName=string,CompressionType=string``

      JSON syntax for these settings is as follows: ``{ "ServiceAccessRoleArn": "string",
      "BucketName": "string", "CompressionType": "none"|"gzip" }``

      - **ServiceAccessRoleArn** *(string) --*

        The IAM role that has permission to access the Amazon S3 bucket.

      - **BucketName** *(string) --*

        The name of the S3 bucket to use.

    - **MongoDbSettings** *(dict) --*

      The settings for the MongoDB source endpoint. For more information, see the
      ``MongoDbSettings`` structure.

      - **Username** *(string) --*

        The user name you use to access the MongoDB source endpoint.

      - **Password** *(string) --*

        The password for the user account you use to access the MongoDB source endpoint.

      - **ServerName** *(string) --*

        The name of the server on the MongoDB source endpoint.

      - **Port** *(integer) --*

        The port value for the MongoDB source endpoint.

      - **DatabaseName** *(string) --*

        The database name on the MongoDB source endpoint.

      - **AuthType** *(string) --*

        The authentication type you use to access the MongoDB source endpoint.

        Valid values: NO, PASSWORD

        When NO is selected, user name and password parameters are not used and can be empty.

      - **AuthMechanism** *(string) --*

        The authentication mechanism you use to access the MongoDB source endpoint.

        Valid values: DEFAULT, MONGODB_CR, SCRAM_SHA_1

        DEFAULT – For MongoDB version 2.x, use MONGODB_CR. For MongoDB version 3.x, use
        SCRAM_SHA_1. This setting is not used when authType=No.

      - **NestingLevel** *(string) --*

        Specifies either document or table mode.

        Valid values: NONE, ONE

        Default value is NONE. Specify NONE to use document mode. Specify ONE to use table mode.

      - **ExtractDocId** *(string) --*

        Specifies the document ID. Use this setting when ``NestingLevel`` is set to NONE.

        Default value is false.

      - **DocsToInvestigate** *(string) --*

        Indicates the number of documents to preview to determine the document organization. Use
        this setting when ``NestingLevel`` is set to ONE.

        Must be a positive value greater than 0. Default value is 1000.

      - **AuthSource** *(string) --*

        The MongoDB database name. This setting is not used when ``authType=NO`` .

        The default is admin.

      - **KmsKeyId** *(string) --*

        The AWS KMS key identifier that is used to encrypt the content on the replication
        instance. If you don't specify a value for the ``KmsKeyId`` parameter, then AWS DMS uses
        your default encryption key. AWS KMS creates the default encryption key for your AWS
        account. Your AWS account has a different default encryption key for each AWS Region.

    - **KinesisSettings** *(dict) --*

      The settings for the Amazon Kinesis source endpoint. For more information, see the
      ``KinesisSettings`` structure.

      - **StreamArn** *(string) --*

        The Amazon Resource Name (ARN) for the Amazon Kinesis Data Streams endpoint.

      - **MessageFormat** *(string) --*

        The output format for the records created on the endpoint. The message format is ``JSON``
        .

      - **ServiceAccessRoleArn** *(string) --*

        The Amazon Resource Name (ARN) for the IAM role that DMS uses to write to the Amazon
        Kinesis data stream.

    - **ElasticsearchSettings** *(dict) --*

      The settings for the Elasticsearch source endpoint. For more information, see the
      ``ElasticsearchSettings`` structure.

      - **ServiceAccessRoleArn** *(string) --*

        The Amazon Resource Name (ARN) used by service to access the IAM role.

      - **EndpointUri** *(string) --*

        The endpoint for the Elasticsearch cluster.

      - **FullLoadErrorPercentage** *(integer) --*

        The maximum percentage of records that can fail to be written before a full load
        operation stops.

      - **ErrorRetryDuration** *(integer) --*

        The maximum number of seconds that DMS retries failed API requests to the Elasticsearch
        cluster.

    - **RedshiftSettings** *(dict) --*

      Settings for the Amazon Redshift endpoint.

      - **AcceptAnyDate** *(boolean) --*

        A value that indicates to allow any date format, including invalid formats such as
        00/00/00 00:00:00, to be loaded without generating an error. You can choose ``true`` or
        ``false`` (the default).

        This parameter applies only to TIMESTAMP and DATE columns. Always use ACCEPTANYDATE with
        the DATEFORMAT parameter. If the date format for the data doesn't match the DATEFORMAT
        specification, Amazon Redshift inserts a NULL value into that field.

      - **AfterConnectScript** *(string) --*

        Code to run after connecting. This parameter should contain the code itself, not the name
        of a file containing the code.

      - **BucketFolder** *(string) --*

        The location where the comma-separated value (.csv) files are stored before being
        uploaded to the S3 bucket.

      - **BucketName** *(string) --*

        The name of the S3 bucket you want to use

      - **ConnectionTimeout** *(integer) --*

        A value that sets the amount of time to wait (in milliseconds) before timing out,
        beginning from when you initially establish a connection.

      - **DatabaseName** *(string) --*

        The name of the Amazon Redshift data warehouse (service) that you are working with.

      - **DateFormat** *(string) --*

        The date format that you are using. Valid values are ``auto`` (case-sensitive), your date
        format string enclosed in quotes, or NULL. If this parameter is left unset (NULL), it
        defaults to a format of 'YYYY-MM-DD'. Using ``auto`` recognizes most strings, even some
        that aren't supported when you use a date format string.

        If your date and time values use formats different from each other, set this to ``auto`` .

      - **EmptyAsNull** *(boolean) --*

        A value that specifies whether AWS DMS should migrate empty CHAR and VARCHAR fields as
        NULL. A value of ``true`` sets empty CHAR and VARCHAR fields to null. The default is
        ``false`` .

      - **EncryptionMode** *(string) --*

        The type of server-side encryption that you want to use for your data. This encryption
        type is part of the endpoint settings or the extra connections attributes for Amazon S3.
        You can choose either ``SSE_S3`` (the default) or ``SSE_KMS`` . To use ``SSE_S3`` ,
        create an AWS Identity and Access Management (IAM) role with a policy that allows
        ``"arn:aws:s3:::*"`` to use the following actions: ``"s3:PutObject", "s3:ListBucket"``

      - **FileTransferUploadStreams** *(integer) --*

        The number of threads used to upload a single file. This parameter accepts a value from 1
        through 64. It defaults to 10.

      - **LoadTimeout** *(integer) --*

        The amount of time to wait (in milliseconds) before timing out, beginning from when you
        begin loading.

      - **MaxFileSize** *(integer) --*

        The maximum size (in KB) of any .csv file used to transfer data to Amazon Redshift. This
        accepts a value from 1 through 1,048,576. It defaults to 32,768 KB (32 MB).

      - **Password** *(string) --*

        The password for the user named in the ``username`` property.

      - **Port** *(integer) --*

        The port number for Amazon Redshift. The default value is 5439.

      - **RemoveQuotes** *(boolean) --*

        A value that specifies to remove surrounding quotation marks from strings in the incoming
        data. All characters within the quotation marks, including delimiters, are retained.
        Choose ``true`` to remove quotation marks. The default is ``false`` .

      - **ReplaceInvalidChars** *(string) --*

        A list of characters that you want to replace. Use with ``ReplaceChars`` .

      - **ReplaceChars** *(string) --*

        A value that specifies to replaces the invalid characters specified in
        ``ReplaceInvalidChars`` , substituting the specified characters instead. The default is
        ``"?"`` .

      - **ServerName** *(string) --*

        The name of the Amazon Redshift cluster you are using.

      - **ServiceAccessRoleArn** *(string) --*

        The Amazon Resource Name (ARN) of the IAM role that has access to the Amazon Redshift
        service.

      - **ServerSideEncryptionKmsKeyId** *(string) --*

        The AWS KMS key ID. If you are using ``SSE_KMS`` for the ``EncryptionMode`` , provide
        this key ID. The key that you use needs an attached policy that enables IAM user
        permissions and allows use of the key.

      - **TimeFormat** *(string) --*

        The time format that you want to use. Valid values are ``auto`` (case-sensitive),
        ``'timeformat_string'`` , ``'epochsecs'`` , or ``'epochmillisecs'`` . It defaults to 10.
        Using ``auto`` recognizes most strings, even some that aren't supported when you use a
        time format string.

        If your date and time values use formats different from each other, set this parameter to
        ``auto`` .

      - **TrimBlanks** *(boolean) --*

        A value that specifies to remove the trailing white space characters from a VARCHAR
        string. This parameter applies only to columns with a VARCHAR data type. Choose ``true``
        to remove unneeded white space. The default is ``false`` .

      - **TruncateColumns** *(boolean) --*

        A value that specifies to truncate data in columns to the appropriate number of
        characters, so that the data fits in the column. This parameter applies only to columns
        with a VARCHAR or CHAR data type, and rows with a size of 4 MB or less. Choose ``true``
        to truncate data. The default is ``false`` .

      - **Username** *(string) --*

        An Amazon Redshift user name for a registered user.

      - **WriteBufferSize** *(integer) --*

        The size of the write buffer to use in rows. Valid values range from 1 through 2,048. The
        default is 1,024. Use this setting to tune performance.
    """


_ClientModifyEndpointResponseTypeDef = TypedDict(
    "_ClientModifyEndpointResponseTypeDef",
    {"Endpoint": ClientModifyEndpointResponseEndpointTypeDef},
    total=False,
)


class ClientModifyEndpointResponseTypeDef(_ClientModifyEndpointResponseTypeDef):
    """
    Type definition for `ClientModifyEndpoint` `Response`

    - **Endpoint** *(dict) --*

      The modified endpoint.

      - **EndpointIdentifier** *(string) --*

        The database endpoint identifier. Identifiers must begin with a letter; must contain only
        ASCII letters, digits, and hyphens; and must not end with a hyphen or contain two
        consecutive hyphens.

      - **EndpointType** *(string) --*

        The type of endpoint. Valid values are ``source`` and ``target`` .

      - **EngineName** *(string) --*

        The database engine name. Valid values, depending on the EndpointType, include mysql,
        oracle, postgres, mariadb, aurora, aurora-postgresql, redshift, s3, db2, azuredb, sybase,
        dynamodb, mongodb, and sqlserver.

      - **EngineDisplayName** *(string) --*

        The expanded name for the engine name. For example, if the ``EngineName`` parameter is
        "aurora," this value would be "Amazon Aurora MySQL."

      - **Username** *(string) --*

        The user name used to connect to the endpoint.

      - **ServerName** *(string) --*

        The name of the server at the endpoint.

      - **Port** *(integer) --*

        The port value used to access the endpoint.

      - **DatabaseName** *(string) --*

        The name of the database at the endpoint.

      - **ExtraConnectionAttributes** *(string) --*

        Additional connection attributes used to connect to the endpoint.

      - **Status** *(string) --*

        The status of the endpoint.

      - **KmsKeyId** *(string) --*

        An AWS KMS key identifier that is used to encrypt the connection parameters for the
        endpoint.

        If you don't specify a value for the ``KmsKeyId`` parameter, then AWS DMS uses your default
        encryption key.

        AWS KMS creates the default encryption key for your AWS account. Your AWS account has a
        different default encryption key for each AWS Region.

      - **EndpointArn** *(string) --*

        The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

      - **CertificateArn** *(string) --*

        The Amazon Resource Name (ARN) used for SSL connection to the endpoint.

      - **SslMode** *(string) --*

        The SSL mode used to connect to the endpoint. The default value is ``none`` .

      - **ServiceAccessRoleArn** *(string) --*

        The Amazon Resource Name (ARN) used by the service access IAM role.

      - **ExternalTableDefinition** *(string) --*

        The external table definition.

      - **ExternalId** *(string) --*

        Value returned by a call to CreateEndpoint that can be used for cross-account validation.
        Use it on a subsequent call to CreateEndpoint to create the endpoint with a cross-account.

      - **DynamoDbSettings** *(dict) --*

        The settings for the target DynamoDB database. For more information, see the
        ``DynamoDBSettings`` structure.

        - **ServiceAccessRoleArn** *(string) --*

          The Amazon Resource Name (ARN) used by the service access IAM role.

      - **S3Settings** *(dict) --*

        The settings for the S3 target endpoint. For more information, see the ``S3Settings``
        structure.

        - **ServiceAccessRoleArn** *(string) --*

          The Amazon Resource Name (ARN) used by the service access IAM role.

        - **ExternalTableDefinition** *(string) --*

          The external table definition.

        - **CsvRowDelimiter** *(string) --*

          The delimiter used to separate rows in the source files. The default is a carriage return
          (``\\n`` ).

        - **CsvDelimiter** *(string) --*

          The delimiter used to separate columns in the source files. The default is a comma.

        - **BucketFolder** *(string) --*

          An optional parameter to set a folder name in the S3 bucket. If provided, tables are
          created in the path `` *bucketFolder* /*schema_name* /*table_name* /`` . If this
          parameter is not specified, then the path used is `` *schema_name* /*table_name* /`` .

        - **BucketName** *(string) --*

          The name of the S3 bucket.

        - **CompressionType** *(string) --*

          An optional parameter to use GZIP to compress the target files. Set to GZIP to compress
          the target files. Set to NONE (the default) or do not use to leave the files
          uncompressed. Applies to both .csv and .parquet file formats.

        - **EncryptionMode** *(string) --*

          The type of server-side encryption that you want to use for your data. This encryption
          type is part of the endpoint settings or the extra connections attributes for Amazon S3.
          You can choose either ``SSE_S3`` (the default) or ``SSE_KMS`` . To use ``SSE_S3`` , you
          need an AWS Identity and Access Management (IAM) role with permission to allow
          ``"arn:aws:s3:::dms-*"`` to use the following actions:

          * ``s3:CreateBucket``

          * ``s3:ListBucket``

          * ``s3:DeleteBucket``

          * ``s3:GetBucketLocation``

          * ``s3:GetObject``

          * ``s3:PutObject``

          * ``s3:DeleteObject``

          * ``s3:GetObjectVersion``

          * ``s3:GetBucketPolicy``

          * ``s3:PutBucketPolicy``

          * ``s3:DeleteBucketPolicy``

        - **ServerSideEncryptionKmsKeyId** *(string) --*

          If you are using ``SSE_KMS`` for the ``EncryptionMode`` , provide the AWS KMS key ID. The
          key that you use needs an attached policy that enables AWS Identity and Access Management
          (IAM) user permissions and allows use of the key.

          Here is a CLI example: ``aws dms create-endpoint --endpoint-identifier *value*
          --endpoint-type target --engine-name s3 --s3-settings ServiceAccessRoleArn=*value*
          ,BucketFolder=*value* ,BucketName=*value*
          ,EncryptionMode=SSE_KMS,ServerSideEncryptionKmsKeyId=*value* ``

        - **DataFormat** *(string) --*

          The format of the data that you want to use for output. You can choose one of the
          following:

          * ``csv`` : This is a row-based file format with comma-separated values (.csv).

          * ``parquet`` : Apache Parquet (.parquet) is a columnar storage file format that features
          efficient compression and provides faster query response.

        - **EncodingType** *(string) --*

          The type of encoding you are using:

          * ``RLE_DICTIONARY`` uses a combination of bit-packing and run-length encoding to store
          repeated values more efficiently. This is the default.

          * ``PLAIN`` doesn't use encoding at all. Values are stored as they are.

          * ``PLAIN_DICTIONARY`` builds a dictionary of the values encountered in a given column.
          The dictionary is stored in a dictionary page for each column chunk.

        - **DictPageSizeLimit** *(integer) --*

          The maximum size of an encoded dictionary page of a column. If the dictionary page
          exceeds this, this column is stored using an encoding type of ``PLAIN`` . This parameter
          defaults to 1024 * 1024 bytes (1 MiB), the maximum size of a dictionary page before it
          reverts to ``PLAIN`` encoding. This size is used for .parquet file format only.

        - **RowGroupLength** *(integer) --*

          The number of rows in a row group. A smaller row group size provides faster reads. But as
          the number of row groups grows, the slower writes become. This parameter defaults to
          10,000 rows. This number is used for .parquet file format only.

          If you choose a value larger than the maximum, ``RowGroupLength`` is set to the max row
          group length in bytes (64 * 1024 * 1024).

        - **DataPageSize** *(integer) --*

          The size of one data page in bytes. This parameter defaults to 1024 * 1024 bytes (1 MiB).
          This number is used for .parquet file format only.

        - **ParquetVersion** *(string) --*

          The version of the Apache Parquet format that you want to use: ``parquet_1_0`` (the
          default) or ``parquet_2_0`` .

        - **EnableStatistics** *(boolean) --*

          A value that enables statistics for Parquet pages and row groups. Choose ``true`` to
          enable statistics, ``false`` to disable. Statistics include ``NULL`` , ``DISTINCT`` ,
          ``MAX`` , and ``MIN`` values. This parameter defaults to ``true`` . This value is used
          for .parquet file format only.

        - **IncludeOpForFullLoad** *(boolean) --*

          A value that enables a full load to write INSERT operations to the comma-separated value
          (.csv) output files only to indicate how the rows were added to the source database.

          .. note::

            AWS DMS supports the ``IncludeOpForFullLoad`` parameter in versions 3.1.4 and later.

          For full load, records can only be inserted. By default (the ``false`` setting), no
          information is recorded in these output files for a full load to indicate that the rows
          were inserted at the source database. If ``IncludeOpForFullLoad`` is set to ``true`` or
          ``y`` , the INSERT is recorded as an I annotation in the first field of the .csv file.
          This allows the format of your target records from a full load to be consistent with the
          target records from a CDC load.

          .. note::

            This setting works together with the ``CdcInsertsOnly`` parameter for output to .csv
            files only. For more information about how these settings work together, see
            `Indicating Source DB Operations in Migrated S3 Data
            <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring.InsertOps>`__
            in the *AWS Database Migration Service User Guide.* .

        - **CdcInsertsOnly** *(boolean) --*

          A value that enables a change data capture (CDC) load to write only INSERT operations to
          .csv or columnar storage (.parquet) output files. By default (the ``false`` setting), the
          first field in a .csv or .parquet record contains the letter I (INSERT), U (UPDATE), or D
          (DELETE). These values indicate whether the row was inserted, updated, or deleted at the
          source database for a CDC load to the target.

          If ``CdcInsertsOnly`` is set to ``true`` or ``y`` , only INSERTs from the source database
          are migrated to the .csv or .parquet file. For .csv format only, how these INSERTs are
          recorded depends on the value of ``IncludeOpForFullLoad`` . If ``IncludeOpForFullLoad``
          is set to ``true`` , the first field of every CDC record is set to I to indicate the
          INSERT operation at the source. If ``IncludeOpForFullLoad`` is set to ``false`` , every
          CDC record is written without a first field to indicate the INSERT operation at the
          source. For more information about how these settings work together, see `Indicating
          Source DB Operations in Migrated S3 Data
          <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring.InsertOps>`__
          in the *AWS Database Migration Service User Guide.* .

          .. note::

            AWS DMS supports this interaction between the ``CdcInsertsOnly`` and
            ``IncludeOpForFullLoad`` parameters in versions 3.1.4 and later.

        - **TimestampColumnName** *(string) --*

          A value that when nonblank causes AWS DMS to add a column with timestamp information to
          the endpoint data for an Amazon S3 target.

          .. note::

            AWS DMS supports the ``TimestampColumnName`` parameter in versions 3.1.4 and later.

          DMS includes an additional ``STRING`` column in the .csv or .parquet object files of your
          migrated data when you set ``TimestampColumnName`` to a nonblank value.

          For a full load, each row of this timestamp column contains a timestamp for when the data
          was transferred from the source to the target by DMS.

          For a change data capture (CDC) load, each row of the timestamp column contains the
          timestamp for the commit of that row in the source database.

          The string format for this timestamp column value is ``yyyy-MM-dd HH:mm:ss.SSSSSS`` . By
          default, the precision of this value is in microseconds. For a CDC load, the rounding of
          the precision depends on the commit timestamp supported by DMS for the source database.

          When the ``AddColumnName`` parameter is set to ``true`` , DMS also includes a name for
          the timestamp column that you set with ``TimestampColumnName`` .

        - **ParquetTimestampInMillisecond** *(boolean) --*

          A value that specifies the precision of any ``TIMESTAMP`` column values that are written
          to an Amazon S3 object file in .parquet format.

          .. note::

            AWS DMS supports the ``ParquetTimestampInMillisecond`` parameter in versions 3.1.4 and
            later.

          When ``ParquetTimestampInMillisecond`` is set to ``true`` or ``y`` , AWS DMS writes all
          ``TIMESTAMP`` columns in a .parquet formatted file with millisecond precision. Otherwise,
          DMS writes them with microsecond precision.

          Currently, Amazon Athena and AWS Glue can handle only millisecond precision for
          ``TIMESTAMP`` values. Set this parameter to ``true`` for S3 endpoint object files that
          are .parquet formatted only if you plan to query or process the data with Athena or AWS
          Glue.

          .. note::

            AWS DMS writes any ``TIMESTAMP`` column values written to an S3 file in .csv format
            with microsecond precision.

            Setting ``ParquetTimestampInMillisecond`` has no effect on the string format of the
            timestamp column value that is inserted by setting the ``TimestampColumnName``
            parameter.

      - **DmsTransferSettings** *(dict) --*

        The settings in JSON format for the DMS transfer type of source endpoint.

        Possible settings include the following:

        * ``ServiceAccessRoleArn`` - The IAM role that has permission to access the Amazon S3
        bucket.

        * ``BucketName`` - The name of the S3 bucket to use.

        * ``CompressionType`` - An optional parameter to use GZIP to compress the target files. To
        use GZIP, set this value to ``NONE`` (the default). To keep the files uncompressed, don't
        use this value.

        Shorthand syntax for these settings is as follows:
        ``ServiceAccessRoleArn=string,BucketName=string,CompressionType=string``

        JSON syntax for these settings is as follows: ``{ "ServiceAccessRoleArn": "string",
        "BucketName": "string", "CompressionType": "none"|"gzip" }``

        - **ServiceAccessRoleArn** *(string) --*

          The IAM role that has permission to access the Amazon S3 bucket.

        - **BucketName** *(string) --*

          The name of the S3 bucket to use.

      - **MongoDbSettings** *(dict) --*

        The settings for the MongoDB source endpoint. For more information, see the
        ``MongoDbSettings`` structure.

        - **Username** *(string) --*

          The user name you use to access the MongoDB source endpoint.

        - **Password** *(string) --*

          The password for the user account you use to access the MongoDB source endpoint.

        - **ServerName** *(string) --*

          The name of the server on the MongoDB source endpoint.

        - **Port** *(integer) --*

          The port value for the MongoDB source endpoint.

        - **DatabaseName** *(string) --*

          The database name on the MongoDB source endpoint.

        - **AuthType** *(string) --*

          The authentication type you use to access the MongoDB source endpoint.

          Valid values: NO, PASSWORD

          When NO is selected, user name and password parameters are not used and can be empty.

        - **AuthMechanism** *(string) --*

          The authentication mechanism you use to access the MongoDB source endpoint.

          Valid values: DEFAULT, MONGODB_CR, SCRAM_SHA_1

          DEFAULT – For MongoDB version 2.x, use MONGODB_CR. For MongoDB version 3.x, use
          SCRAM_SHA_1. This setting is not used when authType=No.

        - **NestingLevel** *(string) --*

          Specifies either document or table mode.

          Valid values: NONE, ONE

          Default value is NONE. Specify NONE to use document mode. Specify ONE to use table mode.

        - **ExtractDocId** *(string) --*

          Specifies the document ID. Use this setting when ``NestingLevel`` is set to NONE.

          Default value is false.

        - **DocsToInvestigate** *(string) --*

          Indicates the number of documents to preview to determine the document organization. Use
          this setting when ``NestingLevel`` is set to ONE.

          Must be a positive value greater than 0. Default value is 1000.

        - **AuthSource** *(string) --*

          The MongoDB database name. This setting is not used when ``authType=NO`` .

          The default is admin.

        - **KmsKeyId** *(string) --*

          The AWS KMS key identifier that is used to encrypt the content on the replication
          instance. If you don't specify a value for the ``KmsKeyId`` parameter, then AWS DMS uses
          your default encryption key. AWS KMS creates the default encryption key for your AWS
          account. Your AWS account has a different default encryption key for each AWS Region.

      - **KinesisSettings** *(dict) --*

        The settings for the Amazon Kinesis source endpoint. For more information, see the
        ``KinesisSettings`` structure.

        - **StreamArn** *(string) --*

          The Amazon Resource Name (ARN) for the Amazon Kinesis Data Streams endpoint.

        - **MessageFormat** *(string) --*

          The output format for the records created on the endpoint. The message format is ``JSON``
          .

        - **ServiceAccessRoleArn** *(string) --*

          The Amazon Resource Name (ARN) for the IAM role that DMS uses to write to the Amazon
          Kinesis data stream.

      - **ElasticsearchSettings** *(dict) --*

        The settings for the Elasticsearch source endpoint. For more information, see the
        ``ElasticsearchSettings`` structure.

        - **ServiceAccessRoleArn** *(string) --*

          The Amazon Resource Name (ARN) used by service to access the IAM role.

        - **EndpointUri** *(string) --*

          The endpoint for the Elasticsearch cluster.

        - **FullLoadErrorPercentage** *(integer) --*

          The maximum percentage of records that can fail to be written before a full load
          operation stops.

        - **ErrorRetryDuration** *(integer) --*

          The maximum number of seconds that DMS retries failed API requests to the Elasticsearch
          cluster.

      - **RedshiftSettings** *(dict) --*

        Settings for the Amazon Redshift endpoint.

        - **AcceptAnyDate** *(boolean) --*

          A value that indicates to allow any date format, including invalid formats such as
          00/00/00 00:00:00, to be loaded without generating an error. You can choose ``true`` or
          ``false`` (the default).

          This parameter applies only to TIMESTAMP and DATE columns. Always use ACCEPTANYDATE with
          the DATEFORMAT parameter. If the date format for the data doesn't match the DATEFORMAT
          specification, Amazon Redshift inserts a NULL value into that field.

        - **AfterConnectScript** *(string) --*

          Code to run after connecting. This parameter should contain the code itself, not the name
          of a file containing the code.

        - **BucketFolder** *(string) --*

          The location where the comma-separated value (.csv) files are stored before being
          uploaded to the S3 bucket.

        - **BucketName** *(string) --*

          The name of the S3 bucket you want to use

        - **ConnectionTimeout** *(integer) --*

          A value that sets the amount of time to wait (in milliseconds) before timing out,
          beginning from when you initially establish a connection.

        - **DatabaseName** *(string) --*

          The name of the Amazon Redshift data warehouse (service) that you are working with.

        - **DateFormat** *(string) --*

          The date format that you are using. Valid values are ``auto`` (case-sensitive), your date
          format string enclosed in quotes, or NULL. If this parameter is left unset (NULL), it
          defaults to a format of 'YYYY-MM-DD'. Using ``auto`` recognizes most strings, even some
          that aren't supported when you use a date format string.

          If your date and time values use formats different from each other, set this to ``auto`` .

        - **EmptyAsNull** *(boolean) --*

          A value that specifies whether AWS DMS should migrate empty CHAR and VARCHAR fields as
          NULL. A value of ``true`` sets empty CHAR and VARCHAR fields to null. The default is
          ``false`` .

        - **EncryptionMode** *(string) --*

          The type of server-side encryption that you want to use for your data. This encryption
          type is part of the endpoint settings or the extra connections attributes for Amazon S3.
          You can choose either ``SSE_S3`` (the default) or ``SSE_KMS`` . To use ``SSE_S3`` ,
          create an AWS Identity and Access Management (IAM) role with a policy that allows
          ``"arn:aws:s3:::*"`` to use the following actions: ``"s3:PutObject", "s3:ListBucket"``

        - **FileTransferUploadStreams** *(integer) --*

          The number of threads used to upload a single file. This parameter accepts a value from 1
          through 64. It defaults to 10.

        - **LoadTimeout** *(integer) --*

          The amount of time to wait (in milliseconds) before timing out, beginning from when you
          begin loading.

        - **MaxFileSize** *(integer) --*

          The maximum size (in KB) of any .csv file used to transfer data to Amazon Redshift. This
          accepts a value from 1 through 1,048,576. It defaults to 32,768 KB (32 MB).

        - **Password** *(string) --*

          The password for the user named in the ``username`` property.

        - **Port** *(integer) --*

          The port number for Amazon Redshift. The default value is 5439.

        - **RemoveQuotes** *(boolean) --*

          A value that specifies to remove surrounding quotation marks from strings in the incoming
          data. All characters within the quotation marks, including delimiters, are retained.
          Choose ``true`` to remove quotation marks. The default is ``false`` .

        - **ReplaceInvalidChars** *(string) --*

          A list of characters that you want to replace. Use with ``ReplaceChars`` .

        - **ReplaceChars** *(string) --*

          A value that specifies to replaces the invalid characters specified in
          ``ReplaceInvalidChars`` , substituting the specified characters instead. The default is
          ``"?"`` .

        - **ServerName** *(string) --*

          The name of the Amazon Redshift cluster you are using.

        - **ServiceAccessRoleArn** *(string) --*

          The Amazon Resource Name (ARN) of the IAM role that has access to the Amazon Redshift
          service.

        - **ServerSideEncryptionKmsKeyId** *(string) --*

          The AWS KMS key ID. If you are using ``SSE_KMS`` for the ``EncryptionMode`` , provide
          this key ID. The key that you use needs an attached policy that enables IAM user
          permissions and allows use of the key.

        - **TimeFormat** *(string) --*

          The time format that you want to use. Valid values are ``auto`` (case-sensitive),
          ``'timeformat_string'`` , ``'epochsecs'`` , or ``'epochmillisecs'`` . It defaults to 10.
          Using ``auto`` recognizes most strings, even some that aren't supported when you use a
          time format string.

          If your date and time values use formats different from each other, set this parameter to
          ``auto`` .

        - **TrimBlanks** *(boolean) --*

          A value that specifies to remove the trailing white space characters from a VARCHAR
          string. This parameter applies only to columns with a VARCHAR data type. Choose ``true``
          to remove unneeded white space. The default is ``false`` .

        - **TruncateColumns** *(boolean) --*

          A value that specifies to truncate data in columns to the appropriate number of
          characters, so that the data fits in the column. This parameter applies only to columns
          with a VARCHAR or CHAR data type, and rows with a size of 4 MB or less. Choose ``true``
          to truncate data. The default is ``false`` .

        - **Username** *(string) --*

          An Amazon Redshift user name for a registered user.

        - **WriteBufferSize** *(integer) --*

          The size of the write buffer to use in rows. Valid values range from 1 through 2,048. The
          default is 1,024. Use this setting to tune performance.
    """


_ClientModifyEndpointS3SettingsTypeDef = TypedDict(
    "_ClientModifyEndpointS3SettingsTypeDef",
    {
        "ServiceAccessRoleArn": str,
        "ExternalTableDefinition": str,
        "CsvRowDelimiter": str,
        "CsvDelimiter": str,
        "BucketFolder": str,
        "BucketName": str,
        "CompressionType": str,
        "EncryptionMode": str,
        "ServerSideEncryptionKmsKeyId": str,
        "DataFormat": str,
        "EncodingType": str,
        "DictPageSizeLimit": int,
        "RowGroupLength": int,
        "DataPageSize": int,
        "ParquetVersion": str,
        "EnableStatistics": bool,
        "IncludeOpForFullLoad": bool,
        "CdcInsertsOnly": bool,
        "TimestampColumnName": str,
        "ParquetTimestampInMillisecond": bool,
    },
    total=False,
)


class ClientModifyEndpointS3SettingsTypeDef(_ClientModifyEndpointS3SettingsTypeDef):
    """
    Type definition for `ClientModifyEndpoint` `S3Settings`

    Settings in JSON format for the target Amazon S3 endpoint. For more information about the
    available settings, see `Extra Connection Attributes When Using Amazon S3 as a Target for AWS DMS
    <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring>`__
    in the *AWS Database Migration Service User Guide.*

    - **ServiceAccessRoleArn** *(string) --*

      The Amazon Resource Name (ARN) used by the service access IAM role.

    - **ExternalTableDefinition** *(string) --*

      The external table definition.

    - **CsvRowDelimiter** *(string) --*

      The delimiter used to separate rows in the source files. The default is a carriage return
      (``\\n`` ).

    - **CsvDelimiter** *(string) --*

      The delimiter used to separate columns in the source files. The default is a comma.

    - **BucketFolder** *(string) --*

      An optional parameter to set a folder name in the S3 bucket. If provided, tables are created in
      the path `` *bucketFolder* /*schema_name* /*table_name* /`` . If this parameter is not
      specified, then the path used is `` *schema_name* /*table_name* /`` .

    - **BucketName** *(string) --*

      The name of the S3 bucket.

    - **CompressionType** *(string) --*

      An optional parameter to use GZIP to compress the target files. Set to GZIP to compress the
      target files. Set to NONE (the default) or do not use to leave the files uncompressed. Applies
      to both .csv and .parquet file formats.

    - **EncryptionMode** *(string) --*

      The type of server-side encryption that you want to use for your data. This encryption type is
      part of the endpoint settings or the extra connections attributes for Amazon S3. You can choose
      either ``SSE_S3`` (the default) or ``SSE_KMS`` . To use ``SSE_S3`` , you need an AWS Identity
      and Access Management (IAM) role with permission to allow ``"arn:aws:s3:::dms-*"`` to use the
      following actions:

      * ``s3:CreateBucket``

      * ``s3:ListBucket``

      * ``s3:DeleteBucket``

      * ``s3:GetBucketLocation``

      * ``s3:GetObject``

      * ``s3:PutObject``

      * ``s3:DeleteObject``

      * ``s3:GetObjectVersion``

      * ``s3:GetBucketPolicy``

      * ``s3:PutBucketPolicy``

      * ``s3:DeleteBucketPolicy``

    - **ServerSideEncryptionKmsKeyId** *(string) --*

      If you are using ``SSE_KMS`` for the ``EncryptionMode`` , provide the AWS KMS key ID. The key
      that you use needs an attached policy that enables AWS Identity and Access Management (IAM)
      user permissions and allows use of the key.

      Here is a CLI example: ``aws dms create-endpoint --endpoint-identifier *value* --endpoint-type
      target --engine-name s3 --s3-settings ServiceAccessRoleArn=*value* ,BucketFolder=*value*
      ,BucketName=*value* ,EncryptionMode=SSE_KMS,ServerSideEncryptionKmsKeyId=*value* ``

    - **DataFormat** *(string) --*

      The format of the data that you want to use for output. You can choose one of the following:

      * ``csv`` : This is a row-based file format with comma-separated values (.csv).

      * ``parquet`` : Apache Parquet (.parquet) is a columnar storage file format that features
      efficient compression and provides faster query response.

    - **EncodingType** *(string) --*

      The type of encoding you are using:

      * ``RLE_DICTIONARY`` uses a combination of bit-packing and run-length encoding to store
      repeated values more efficiently. This is the default.

      * ``PLAIN`` doesn't use encoding at all. Values are stored as they are.

      * ``PLAIN_DICTIONARY`` builds a dictionary of the values encountered in a given column. The
      dictionary is stored in a dictionary page for each column chunk.

    - **DictPageSizeLimit** *(integer) --*

      The maximum size of an encoded dictionary page of a column. If the dictionary page exceeds
      this, this column is stored using an encoding type of ``PLAIN`` . This parameter defaults to
      1024 * 1024 bytes (1 MiB), the maximum size of a dictionary page before it reverts to ``PLAIN``
      encoding. This size is used for .parquet file format only.

    - **RowGroupLength** *(integer) --*

      The number of rows in a row group. A smaller row group size provides faster reads. But as the
      number of row groups grows, the slower writes become. This parameter defaults to 10,000 rows.
      This number is used for .parquet file format only.

      If you choose a value larger than the maximum, ``RowGroupLength`` is set to the max row group
      length in bytes (64 * 1024 * 1024).

    - **DataPageSize** *(integer) --*

      The size of one data page in bytes. This parameter defaults to 1024 * 1024 bytes (1 MiB). This
      number is used for .parquet file format only.

    - **ParquetVersion** *(string) --*

      The version of the Apache Parquet format that you want to use: ``parquet_1_0`` (the default) or
      ``parquet_2_0`` .

    - **EnableStatistics** *(boolean) --*

      A value that enables statistics for Parquet pages and row groups. Choose ``true`` to enable
      statistics, ``false`` to disable. Statistics include ``NULL`` , ``DISTINCT`` , ``MAX`` , and
      ``MIN`` values. This parameter defaults to ``true`` . This value is used for .parquet file
      format only.

    - **IncludeOpForFullLoad** *(boolean) --*

      A value that enables a full load to write INSERT operations to the comma-separated value (.csv)
      output files only to indicate how the rows were added to the source database.

      .. note::

        AWS DMS supports the ``IncludeOpForFullLoad`` parameter in versions 3.1.4 and later.

      For full load, records can only be inserted. By default (the ``false`` setting), no information
      is recorded in these output files for a full load to indicate that the rows were inserted at
      the source database. If ``IncludeOpForFullLoad`` is set to ``true`` or ``y`` , the INSERT is
      recorded as an I annotation in the first field of the .csv file. This allows the format of your
      target records from a full load to be consistent with the target records from a CDC load.

      .. note::

        This setting works together with the ``CdcInsertsOnly`` parameter for output to .csv files
        only. For more information about how these settings work together, see `Indicating Source DB
        Operations in Migrated S3 Data
        <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring.InsertOps>`__
        in the *AWS Database Migration Service User Guide.* .

    - **CdcInsertsOnly** *(boolean) --*

      A value that enables a change data capture (CDC) load to write only INSERT operations to .csv
      or columnar storage (.parquet) output files. By default (the ``false`` setting), the first
      field in a .csv or .parquet record contains the letter I (INSERT), U (UPDATE), or D (DELETE).
      These values indicate whether the row was inserted, updated, or deleted at the source database
      for a CDC load to the target.

      If ``CdcInsertsOnly`` is set to ``true`` or ``y`` , only INSERTs from the source database are
      migrated to the .csv or .parquet file. For .csv format only, how these INSERTs are recorded
      depends on the value of ``IncludeOpForFullLoad`` . If ``IncludeOpForFullLoad`` is set to
      ``true`` , the first field of every CDC record is set to I to indicate the INSERT operation at
      the source. If ``IncludeOpForFullLoad`` is set to ``false`` , every CDC record is written
      without a first field to indicate the INSERT operation at the source. For more information
      about how these settings work together, see `Indicating Source DB Operations in Migrated S3
      Data
      <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring.InsertOps>`__
      in the *AWS Database Migration Service User Guide.* .

      .. note::

        AWS DMS supports this interaction between the ``CdcInsertsOnly`` and ``IncludeOpForFullLoad``
        parameters in versions 3.1.4 and later.

    - **TimestampColumnName** *(string) --*

      A value that when nonblank causes AWS DMS to add a column with timestamp information to the
      endpoint data for an Amazon S3 target.

      .. note::

        AWS DMS supports the ``TimestampColumnName`` parameter in versions 3.1.4 and later.

      DMS includes an additional ``STRING`` column in the .csv or .parquet object files of your
      migrated data when you set ``TimestampColumnName`` to a nonblank value.

      For a full load, each row of this timestamp column contains a timestamp for when the data was
      transferred from the source to the target by DMS.

      For a change data capture (CDC) load, each row of the timestamp column contains the timestamp
      for the commit of that row in the source database.

      The string format for this timestamp column value is ``yyyy-MM-dd HH:mm:ss.SSSSSS`` . By
      default, the precision of this value is in microseconds. For a CDC load, the rounding of the
      precision depends on the commit timestamp supported by DMS for the source database.

      When the ``AddColumnName`` parameter is set to ``true`` , DMS also includes a name for the
      timestamp column that you set with ``TimestampColumnName`` .

    - **ParquetTimestampInMillisecond** *(boolean) --*

      A value that specifies the precision of any ``TIMESTAMP`` column values that are written to an
      Amazon S3 object file in .parquet format.

      .. note::

        AWS DMS supports the ``ParquetTimestampInMillisecond`` parameter in versions 3.1.4 and later.

      When ``ParquetTimestampInMillisecond`` is set to ``true`` or ``y`` , AWS DMS writes all
      ``TIMESTAMP`` columns in a .parquet formatted file with millisecond precision. Otherwise, DMS
      writes them with microsecond precision.

      Currently, Amazon Athena and AWS Glue can handle only millisecond precision for ``TIMESTAMP``
      values. Set this parameter to ``true`` for S3 endpoint object files that are .parquet formatted
      only if you plan to query or process the data with Athena or AWS Glue.

      .. note::

        AWS DMS writes any ``TIMESTAMP`` column values written to an S3 file in .csv format with
        microsecond precision.

        Setting ``ParquetTimestampInMillisecond`` has no effect on the string format of the timestamp
        column value that is inserted by setting the ``TimestampColumnName`` parameter.
    """


_ClientModifyEventSubscriptionResponseEventSubscriptionTypeDef = TypedDict(
    "_ClientModifyEventSubscriptionResponseEventSubscriptionTypeDef",
    {
        "CustomerAwsId": str,
        "CustSubscriptionId": str,
        "SnsTopicArn": str,
        "Status": str,
        "SubscriptionCreationTime": str,
        "SourceType": str,
        "SourceIdsList": List[str],
        "EventCategoriesList": List[str],
        "Enabled": bool,
    },
    total=False,
)


class ClientModifyEventSubscriptionResponseEventSubscriptionTypeDef(
    _ClientModifyEventSubscriptionResponseEventSubscriptionTypeDef
):
    """
    Type definition for `ClientModifyEventSubscriptionResponse` `EventSubscription`

    The modified event subscription.

    - **CustomerAwsId** *(string) --*

      The AWS customer account associated with the AWS DMS event notification subscription.

    - **CustSubscriptionId** *(string) --*

      The AWS DMS event notification subscription Id.

    - **SnsTopicArn** *(string) --*

      The topic ARN of the AWS DMS event notification subscription.

    - **Status** *(string) --*

      The status of the AWS DMS event notification subscription.

      Constraints:

      Can be one of the following: creating | modifying | deleting | active | no-permission |
      topic-not-exist

      The status "no-permission" indicates that AWS DMS no longer has permission to post to the
      SNS topic. The status "topic-not-exist" indicates that the topic was deleted after the
      subscription was created.

    - **SubscriptionCreationTime** *(string) --*

      The time the RDS event notification subscription was created.

    - **SourceType** *(string) --*

      The type of AWS DMS resource that generates events.

      Valid values: replication-instance | replication-server | security-group | replication-task

    - **SourceIdsList** *(list) --*

      A list of source Ids for the event subscription.

      - *(string) --*

    - **EventCategoriesList** *(list) --*

      A lists of event categories.

      - *(string) --*

    - **Enabled** *(boolean) --*

      Boolean value that indicates if the event subscription is enabled.
    """


_ClientModifyEventSubscriptionResponseTypeDef = TypedDict(
    "_ClientModifyEventSubscriptionResponseTypeDef",
    {
        "EventSubscription": ClientModifyEventSubscriptionResponseEventSubscriptionTypeDef
    },
    total=False,
)


class ClientModifyEventSubscriptionResponseTypeDef(
    _ClientModifyEventSubscriptionResponseTypeDef
):
    """
    Type definition for `ClientModifyEventSubscription` `Response`

    - **EventSubscription** *(dict) --*

      The modified event subscription.

      - **CustomerAwsId** *(string) --*

        The AWS customer account associated with the AWS DMS event notification subscription.

      - **CustSubscriptionId** *(string) --*

        The AWS DMS event notification subscription Id.

      - **SnsTopicArn** *(string) --*

        The topic ARN of the AWS DMS event notification subscription.

      - **Status** *(string) --*

        The status of the AWS DMS event notification subscription.

        Constraints:

        Can be one of the following: creating | modifying | deleting | active | no-permission |
        topic-not-exist

        The status "no-permission" indicates that AWS DMS no longer has permission to post to the
        SNS topic. The status "topic-not-exist" indicates that the topic was deleted after the
        subscription was created.

      - **SubscriptionCreationTime** *(string) --*

        The time the RDS event notification subscription was created.

      - **SourceType** *(string) --*

        The type of AWS DMS resource that generates events.

        Valid values: replication-instance | replication-server | security-group | replication-task

      - **SourceIdsList** *(list) --*

        A list of source Ids for the event subscription.

        - *(string) --*

      - **EventCategoriesList** *(list) --*

        A lists of event categories.

        - *(string) --*

      - **Enabled** *(boolean) --*

        Boolean value that indicates if the event subscription is enabled.
    """


_ClientModifyReplicationInstanceResponseReplicationInstancePendingModifiedValuesTypeDef = TypedDict(
    "_ClientModifyReplicationInstanceResponseReplicationInstancePendingModifiedValuesTypeDef",
    {
        "ReplicationInstanceClass": str,
        "AllocatedStorage": int,
        "MultiAZ": bool,
        "EngineVersion": str,
    },
    total=False,
)


class ClientModifyReplicationInstanceResponseReplicationInstancePendingModifiedValuesTypeDef(
    _ClientModifyReplicationInstanceResponseReplicationInstancePendingModifiedValuesTypeDef
):
    """
    Type definition for `ClientModifyReplicationInstanceResponseReplicationInstance` `PendingModifiedValues`

    The pending modification values.

    - **ReplicationInstanceClass** *(string) --*

      The compute and memory capacity of the replication instance.

      Valid Values: ``dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large | dms.c4.large
      | dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge``

    - **AllocatedStorage** *(integer) --*

      The amount of storage (in gigabytes) that is allocated for the replication instance.

    - **MultiAZ** *(boolean) --*

      Specifies whether the replication instance is a Multi-AZ deployment. You cannot set the
      ``AvailabilityZone`` parameter if the Multi-AZ parameter is set to ``true`` .

    - **EngineVersion** *(string) --*

      The engine version number of the replication instance.
    """


_ClientModifyReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "_ClientModifyReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)


class ClientModifyReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef(
    _ClientModifyReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef
):
    """
    Type definition for `ClientModifyReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnets` `SubnetAvailabilityZone`

    The Availability Zone of the subnet.

    - **Name** *(string) --*

      The name of the availability zone.
    """


_ClientModifyReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsTypeDef = TypedDict(
    "_ClientModifyReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientModifyReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)


class ClientModifyReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsTypeDef(
    _ClientModifyReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsTypeDef
):
    """
    Type definition for `ClientModifyReplicationInstanceResponseReplicationInstanceReplicationSubnetGroup` `Subnets`

    - **SubnetIdentifier** *(string) --*

      The subnet identifier.

    - **SubnetAvailabilityZone** *(dict) --*

      The Availability Zone of the subnet.

      - **Name** *(string) --*

        The name of the availability zone.

    - **SubnetStatus** *(string) --*

      The status of the subnet.
    """


_ClientModifyReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupTypeDef = TypedDict(
    "_ClientModifyReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupTypeDef",
    {
        "ReplicationSubnetGroupIdentifier": str,
        "ReplicationSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[
            ClientModifyReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsTypeDef
        ],
    },
    total=False,
)


class ClientModifyReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupTypeDef(
    _ClientModifyReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupTypeDef
):
    """
    Type definition for `ClientModifyReplicationInstanceResponseReplicationInstance` `ReplicationSubnetGroup`

    The subnet group for the replication instance.

    - **ReplicationSubnetGroupIdentifier** *(string) --*

      The identifier of the replication instance subnet group.

    - **ReplicationSubnetGroupDescription** *(string) --*

      A description for the replication subnet group.

    - **VpcId** *(string) --*

      The ID of the VPC.

    - **SubnetGroupStatus** *(string) --*

      The status of the subnet group.

    - **Subnets** *(list) --*

      The subnets that are in the subnet group.

      - *(dict) --*

        - **SubnetIdentifier** *(string) --*

          The subnet identifier.

        - **SubnetAvailabilityZone** *(dict) --*

          The Availability Zone of the subnet.

          - **Name** *(string) --*

            The name of the availability zone.

        - **SubnetStatus** *(string) --*

          The status of the subnet.
    """


_ClientModifyReplicationInstanceResponseReplicationInstanceVpcSecurityGroupsTypeDef = TypedDict(
    "_ClientModifyReplicationInstanceResponseReplicationInstanceVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientModifyReplicationInstanceResponseReplicationInstanceVpcSecurityGroupsTypeDef(
    _ClientModifyReplicationInstanceResponseReplicationInstanceVpcSecurityGroupsTypeDef
):
    """
    Type definition for `ClientModifyReplicationInstanceResponseReplicationInstance` `VpcSecurityGroups`

    - **VpcSecurityGroupId** *(string) --*

      The VPC security group Id.

    - **Status** *(string) --*

      The status of the VPC security group.
    """


_ClientModifyReplicationInstanceResponseReplicationInstanceTypeDef = TypedDict(
    "_ClientModifyReplicationInstanceResponseReplicationInstanceTypeDef",
    {
        "ReplicationInstanceIdentifier": str,
        "ReplicationInstanceClass": str,
        "ReplicationInstanceStatus": str,
        "AllocatedStorage": int,
        "InstanceCreateTime": datetime,
        "VpcSecurityGroups": List[
            ClientModifyReplicationInstanceResponseReplicationInstanceVpcSecurityGroupsTypeDef
        ],
        "AvailabilityZone": str,
        "ReplicationSubnetGroup": ClientModifyReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupTypeDef,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientModifyReplicationInstanceResponseReplicationInstancePendingModifiedValuesTypeDef,
        "MultiAZ": bool,
        "EngineVersion": str,
        "AutoMinorVersionUpgrade": bool,
        "KmsKeyId": str,
        "ReplicationInstanceArn": str,
        "ReplicationInstancePublicIpAddress": str,
        "ReplicationInstancePrivateIpAddress": str,
        "ReplicationInstancePublicIpAddresses": List[str],
        "ReplicationInstancePrivateIpAddresses": List[str],
        "PubliclyAccessible": bool,
        "SecondaryAvailabilityZone": str,
        "FreeUntil": datetime,
        "DnsNameServers": str,
    },
    total=False,
)


class ClientModifyReplicationInstanceResponseReplicationInstanceTypeDef(
    _ClientModifyReplicationInstanceResponseReplicationInstanceTypeDef
):
    """
    Type definition for `ClientModifyReplicationInstanceResponse` `ReplicationInstance`

    The modified replication instance.

    - **ReplicationInstanceIdentifier** *(string) --*

      The replication instance identifier. This parameter is stored as a lowercase string.

      Constraints:

      * Must contain from 1 to 63 alphanumeric characters or hyphens.

      * First character must be a letter.

      * Cannot end with a hyphen or contain two consecutive hyphens.

      Example: ``myrepinstance``

    - **ReplicationInstanceClass** *(string) --*

      The compute and memory capacity of the replication instance.

      Valid Values: ``dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large | dms.c4.large |
      dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge``

    - **ReplicationInstanceStatus** *(string) --*

      The status of the replication instance.

    - **AllocatedStorage** *(integer) --*

      The amount of storage (in gigabytes) that is allocated for the replication instance.

    - **InstanceCreateTime** *(datetime) --*

      The time the replication instance was created.

    - **VpcSecurityGroups** *(list) --*

      The VPC security group for the instance.

      - *(dict) --*

        - **VpcSecurityGroupId** *(string) --*

          The VPC security group Id.

        - **Status** *(string) --*

          The status of the VPC security group.

    - **AvailabilityZone** *(string) --*

      The Availability Zone for the instance.

    - **ReplicationSubnetGroup** *(dict) --*

      The subnet group for the replication instance.

      - **ReplicationSubnetGroupIdentifier** *(string) --*

        The identifier of the replication instance subnet group.

      - **ReplicationSubnetGroupDescription** *(string) --*

        A description for the replication subnet group.

      - **VpcId** *(string) --*

        The ID of the VPC.

      - **SubnetGroupStatus** *(string) --*

        The status of the subnet group.

      - **Subnets** *(list) --*

        The subnets that are in the subnet group.

        - *(dict) --*

          - **SubnetIdentifier** *(string) --*

            The subnet identifier.

          - **SubnetAvailabilityZone** *(dict) --*

            The Availability Zone of the subnet.

            - **Name** *(string) --*

              The name of the availability zone.

          - **SubnetStatus** *(string) --*

            The status of the subnet.

    - **PreferredMaintenanceWindow** *(string) --*

      The maintenance window times for the replication instance.

    - **PendingModifiedValues** *(dict) --*

      The pending modification values.

      - **ReplicationInstanceClass** *(string) --*

        The compute and memory capacity of the replication instance.

        Valid Values: ``dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large | dms.c4.large
        | dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge``

      - **AllocatedStorage** *(integer) --*

        The amount of storage (in gigabytes) that is allocated for the replication instance.

      - **MultiAZ** *(boolean) --*

        Specifies whether the replication instance is a Multi-AZ deployment. You cannot set the
        ``AvailabilityZone`` parameter if the Multi-AZ parameter is set to ``true`` .

      - **EngineVersion** *(string) --*

        The engine version number of the replication instance.

    - **MultiAZ** *(boolean) --*

      Specifies whether the replication instance is a Multi-AZ deployment. You cannot set the
      ``AvailabilityZone`` parameter if the Multi-AZ parameter is set to ``true`` .

    - **EngineVersion** *(string) --*

      The engine version number of the replication instance.

    - **AutoMinorVersionUpgrade** *(boolean) --*

      Boolean value indicating if minor version upgrades will be automatically applied to the
      instance.

    - **KmsKeyId** *(string) --*

      An AWS KMS key identifier that is used to encrypt the data on the replication instance.

      If you don't specify a value for the ``KmsKeyId`` parameter, then AWS DMS uses your default
      encryption key.

      AWS KMS creates the default encryption key for your AWS account. Your AWS account has a
      different default encryption key for each AWS Region.

    - **ReplicationInstanceArn** *(string) --*

      The Amazon Resource Name (ARN) of the replication instance.

    - **ReplicationInstancePublicIpAddress** *(string) --*

      The public IP address of the replication instance.

    - **ReplicationInstancePrivateIpAddress** *(string) --*

      The private IP address of the replication instance.

    - **ReplicationInstancePublicIpAddresses** *(list) --*

      One or more public IP addresses for the replication instance.

      - *(string) --*

    - **ReplicationInstancePrivateIpAddresses** *(list) --*

      One or more private IP addresses for the replication instance.

      - *(string) --*

    - **PubliclyAccessible** *(boolean) --*

      Specifies the accessibility options for the replication instance. A value of ``true``
      represents an instance with a public IP address. A value of ``false`` represents an
      instance with a private IP address. The default value is ``true`` .

    - **SecondaryAvailabilityZone** *(string) --*

      The availability zone of the standby replication instance in a Multi-AZ deployment.

    - **FreeUntil** *(datetime) --*

      The expiration date of the free replication instance that is part of the Free DMS program.

    - **DnsNameServers** *(string) --*

      The DNS name servers for the replication instance.
    """


_ClientModifyReplicationInstanceResponseTypeDef = TypedDict(
    "_ClientModifyReplicationInstanceResponseTypeDef",
    {
        "ReplicationInstance": ClientModifyReplicationInstanceResponseReplicationInstanceTypeDef
    },
    total=False,
)


class ClientModifyReplicationInstanceResponseTypeDef(
    _ClientModifyReplicationInstanceResponseTypeDef
):
    """
    Type definition for `ClientModifyReplicationInstance` `Response`

    - **ReplicationInstance** *(dict) --*

      The modified replication instance.

      - **ReplicationInstanceIdentifier** *(string) --*

        The replication instance identifier. This parameter is stored as a lowercase string.

        Constraints:

        * Must contain from 1 to 63 alphanumeric characters or hyphens.

        * First character must be a letter.

        * Cannot end with a hyphen or contain two consecutive hyphens.

        Example: ``myrepinstance``

      - **ReplicationInstanceClass** *(string) --*

        The compute and memory capacity of the replication instance.

        Valid Values: ``dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large | dms.c4.large |
        dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge``

      - **ReplicationInstanceStatus** *(string) --*

        The status of the replication instance.

      - **AllocatedStorage** *(integer) --*

        The amount of storage (in gigabytes) that is allocated for the replication instance.

      - **InstanceCreateTime** *(datetime) --*

        The time the replication instance was created.

      - **VpcSecurityGroups** *(list) --*

        The VPC security group for the instance.

        - *(dict) --*

          - **VpcSecurityGroupId** *(string) --*

            The VPC security group Id.

          - **Status** *(string) --*

            The status of the VPC security group.

      - **AvailabilityZone** *(string) --*

        The Availability Zone for the instance.

      - **ReplicationSubnetGroup** *(dict) --*

        The subnet group for the replication instance.

        - **ReplicationSubnetGroupIdentifier** *(string) --*

          The identifier of the replication instance subnet group.

        - **ReplicationSubnetGroupDescription** *(string) --*

          A description for the replication subnet group.

        - **VpcId** *(string) --*

          The ID of the VPC.

        - **SubnetGroupStatus** *(string) --*

          The status of the subnet group.

        - **Subnets** *(list) --*

          The subnets that are in the subnet group.

          - *(dict) --*

            - **SubnetIdentifier** *(string) --*

              The subnet identifier.

            - **SubnetAvailabilityZone** *(dict) --*

              The Availability Zone of the subnet.

              - **Name** *(string) --*

                The name of the availability zone.

            - **SubnetStatus** *(string) --*

              The status of the subnet.

      - **PreferredMaintenanceWindow** *(string) --*

        The maintenance window times for the replication instance.

      - **PendingModifiedValues** *(dict) --*

        The pending modification values.

        - **ReplicationInstanceClass** *(string) --*

          The compute and memory capacity of the replication instance.

          Valid Values: ``dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large | dms.c4.large
          | dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge``

        - **AllocatedStorage** *(integer) --*

          The amount of storage (in gigabytes) that is allocated for the replication instance.

        - **MultiAZ** *(boolean) --*

          Specifies whether the replication instance is a Multi-AZ deployment. You cannot set the
          ``AvailabilityZone`` parameter if the Multi-AZ parameter is set to ``true`` .

        - **EngineVersion** *(string) --*

          The engine version number of the replication instance.

      - **MultiAZ** *(boolean) --*

        Specifies whether the replication instance is a Multi-AZ deployment. You cannot set the
        ``AvailabilityZone`` parameter if the Multi-AZ parameter is set to ``true`` .

      - **EngineVersion** *(string) --*

        The engine version number of the replication instance.

      - **AutoMinorVersionUpgrade** *(boolean) --*

        Boolean value indicating if minor version upgrades will be automatically applied to the
        instance.

      - **KmsKeyId** *(string) --*

        An AWS KMS key identifier that is used to encrypt the data on the replication instance.

        If you don't specify a value for the ``KmsKeyId`` parameter, then AWS DMS uses your default
        encryption key.

        AWS KMS creates the default encryption key for your AWS account. Your AWS account has a
        different default encryption key for each AWS Region.

      - **ReplicationInstanceArn** *(string) --*

        The Amazon Resource Name (ARN) of the replication instance.

      - **ReplicationInstancePublicIpAddress** *(string) --*

        The public IP address of the replication instance.

      - **ReplicationInstancePrivateIpAddress** *(string) --*

        The private IP address of the replication instance.

      - **ReplicationInstancePublicIpAddresses** *(list) --*

        One or more public IP addresses for the replication instance.

        - *(string) --*

      - **ReplicationInstancePrivateIpAddresses** *(list) --*

        One or more private IP addresses for the replication instance.

        - *(string) --*

      - **PubliclyAccessible** *(boolean) --*

        Specifies the accessibility options for the replication instance. A value of ``true``
        represents an instance with a public IP address. A value of ``false`` represents an
        instance with a private IP address. The default value is ``true`` .

      - **SecondaryAvailabilityZone** *(string) --*

        The availability zone of the standby replication instance in a Multi-AZ deployment.

      - **FreeUntil** *(datetime) --*

        The expiration date of the free replication instance that is part of the Free DMS program.

      - **DnsNameServers** *(string) --*

        The DNS name servers for the replication instance.
    """


_ClientModifyReplicationSubnetGroupResponseReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "_ClientModifyReplicationSubnetGroupResponseReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)


class ClientModifyReplicationSubnetGroupResponseReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef(
    _ClientModifyReplicationSubnetGroupResponseReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef
):
    """
    Type definition for `ClientModifyReplicationSubnetGroupResponseReplicationSubnetGroupSubnets` `SubnetAvailabilityZone`

    The Availability Zone of the subnet.

    - **Name** *(string) --*

      The name of the availability zone.
    """


_ClientModifyReplicationSubnetGroupResponseReplicationSubnetGroupSubnetsTypeDef = TypedDict(
    "_ClientModifyReplicationSubnetGroupResponseReplicationSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientModifyReplicationSubnetGroupResponseReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)


class ClientModifyReplicationSubnetGroupResponseReplicationSubnetGroupSubnetsTypeDef(
    _ClientModifyReplicationSubnetGroupResponseReplicationSubnetGroupSubnetsTypeDef
):
    """
    Type definition for `ClientModifyReplicationSubnetGroupResponseReplicationSubnetGroup` `Subnets`

    - **SubnetIdentifier** *(string) --*

      The subnet identifier.

    - **SubnetAvailabilityZone** *(dict) --*

      The Availability Zone of the subnet.

      - **Name** *(string) --*

        The name of the availability zone.

    - **SubnetStatus** *(string) --*

      The status of the subnet.
    """


_ClientModifyReplicationSubnetGroupResponseReplicationSubnetGroupTypeDef = TypedDict(
    "_ClientModifyReplicationSubnetGroupResponseReplicationSubnetGroupTypeDef",
    {
        "ReplicationSubnetGroupIdentifier": str,
        "ReplicationSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[
            ClientModifyReplicationSubnetGroupResponseReplicationSubnetGroupSubnetsTypeDef
        ],
    },
    total=False,
)


class ClientModifyReplicationSubnetGroupResponseReplicationSubnetGroupTypeDef(
    _ClientModifyReplicationSubnetGroupResponseReplicationSubnetGroupTypeDef
):
    """
    Type definition for `ClientModifyReplicationSubnetGroupResponse` `ReplicationSubnetGroup`

    The modified replication subnet group.

    - **ReplicationSubnetGroupIdentifier** *(string) --*

      The identifier of the replication instance subnet group.

    - **ReplicationSubnetGroupDescription** *(string) --*

      A description for the replication subnet group.

    - **VpcId** *(string) --*

      The ID of the VPC.

    - **SubnetGroupStatus** *(string) --*

      The status of the subnet group.

    - **Subnets** *(list) --*

      The subnets that are in the subnet group.

      - *(dict) --*

        - **SubnetIdentifier** *(string) --*

          The subnet identifier.

        - **SubnetAvailabilityZone** *(dict) --*

          The Availability Zone of the subnet.

          - **Name** *(string) --*

            The name of the availability zone.

        - **SubnetStatus** *(string) --*

          The status of the subnet.
    """


_ClientModifyReplicationSubnetGroupResponseTypeDef = TypedDict(
    "_ClientModifyReplicationSubnetGroupResponseTypeDef",
    {
        "ReplicationSubnetGroup": ClientModifyReplicationSubnetGroupResponseReplicationSubnetGroupTypeDef
    },
    total=False,
)


class ClientModifyReplicationSubnetGroupResponseTypeDef(
    _ClientModifyReplicationSubnetGroupResponseTypeDef
):
    """
    Type definition for `ClientModifyReplicationSubnetGroup` `Response`

    - **ReplicationSubnetGroup** *(dict) --*

      The modified replication subnet group.

      - **ReplicationSubnetGroupIdentifier** *(string) --*

        The identifier of the replication instance subnet group.

      - **ReplicationSubnetGroupDescription** *(string) --*

        A description for the replication subnet group.

      - **VpcId** *(string) --*

        The ID of the VPC.

      - **SubnetGroupStatus** *(string) --*

        The status of the subnet group.

      - **Subnets** *(list) --*

        The subnets that are in the subnet group.

        - *(dict) --*

          - **SubnetIdentifier** *(string) --*

            The subnet identifier.

          - **SubnetAvailabilityZone** *(dict) --*

            The Availability Zone of the subnet.

            - **Name** *(string) --*

              The name of the availability zone.

          - **SubnetStatus** *(string) --*

            The status of the subnet.
    """


_ClientRebootReplicationInstanceResponseReplicationInstancePendingModifiedValuesTypeDef = TypedDict(
    "_ClientRebootReplicationInstanceResponseReplicationInstancePendingModifiedValuesTypeDef",
    {
        "ReplicationInstanceClass": str,
        "AllocatedStorage": int,
        "MultiAZ": bool,
        "EngineVersion": str,
    },
    total=False,
)


class ClientRebootReplicationInstanceResponseReplicationInstancePendingModifiedValuesTypeDef(
    _ClientRebootReplicationInstanceResponseReplicationInstancePendingModifiedValuesTypeDef
):
    """
    Type definition for `ClientRebootReplicationInstanceResponseReplicationInstance` `PendingModifiedValues`

    The pending modification values.

    - **ReplicationInstanceClass** *(string) --*

      The compute and memory capacity of the replication instance.

      Valid Values: ``dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large | dms.c4.large
      | dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge``

    - **AllocatedStorage** *(integer) --*

      The amount of storage (in gigabytes) that is allocated for the replication instance.

    - **MultiAZ** *(boolean) --*

      Specifies whether the replication instance is a Multi-AZ deployment. You cannot set the
      ``AvailabilityZone`` parameter if the Multi-AZ parameter is set to ``true`` .

    - **EngineVersion** *(string) --*

      The engine version number of the replication instance.
    """


_ClientRebootReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "_ClientRebootReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)


class ClientRebootReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef(
    _ClientRebootReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef
):
    """
    Type definition for `ClientRebootReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnets` `SubnetAvailabilityZone`

    The Availability Zone of the subnet.

    - **Name** *(string) --*

      The name of the availability zone.
    """


_ClientRebootReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsTypeDef = TypedDict(
    "_ClientRebootReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientRebootReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)


class ClientRebootReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsTypeDef(
    _ClientRebootReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsTypeDef
):
    """
    Type definition for `ClientRebootReplicationInstanceResponseReplicationInstanceReplicationSubnetGroup` `Subnets`

    - **SubnetIdentifier** *(string) --*

      The subnet identifier.

    - **SubnetAvailabilityZone** *(dict) --*

      The Availability Zone of the subnet.

      - **Name** *(string) --*

        The name of the availability zone.

    - **SubnetStatus** *(string) --*

      The status of the subnet.
    """


_ClientRebootReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupTypeDef = TypedDict(
    "_ClientRebootReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupTypeDef",
    {
        "ReplicationSubnetGroupIdentifier": str,
        "ReplicationSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[
            ClientRebootReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsTypeDef
        ],
    },
    total=False,
)


class ClientRebootReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupTypeDef(
    _ClientRebootReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupTypeDef
):
    """
    Type definition for `ClientRebootReplicationInstanceResponseReplicationInstance` `ReplicationSubnetGroup`

    The subnet group for the replication instance.

    - **ReplicationSubnetGroupIdentifier** *(string) --*

      The identifier of the replication instance subnet group.

    - **ReplicationSubnetGroupDescription** *(string) --*

      A description for the replication subnet group.

    - **VpcId** *(string) --*

      The ID of the VPC.

    - **SubnetGroupStatus** *(string) --*

      The status of the subnet group.

    - **Subnets** *(list) --*

      The subnets that are in the subnet group.

      - *(dict) --*

        - **SubnetIdentifier** *(string) --*

          The subnet identifier.

        - **SubnetAvailabilityZone** *(dict) --*

          The Availability Zone of the subnet.

          - **Name** *(string) --*

            The name of the availability zone.

        - **SubnetStatus** *(string) --*

          The status of the subnet.
    """


_ClientRebootReplicationInstanceResponseReplicationInstanceVpcSecurityGroupsTypeDef = TypedDict(
    "_ClientRebootReplicationInstanceResponseReplicationInstanceVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientRebootReplicationInstanceResponseReplicationInstanceVpcSecurityGroupsTypeDef(
    _ClientRebootReplicationInstanceResponseReplicationInstanceVpcSecurityGroupsTypeDef
):
    """
    Type definition for `ClientRebootReplicationInstanceResponseReplicationInstance` `VpcSecurityGroups`

    - **VpcSecurityGroupId** *(string) --*

      The VPC security group Id.

    - **Status** *(string) --*

      The status of the VPC security group.
    """


_ClientRebootReplicationInstanceResponseReplicationInstanceTypeDef = TypedDict(
    "_ClientRebootReplicationInstanceResponseReplicationInstanceTypeDef",
    {
        "ReplicationInstanceIdentifier": str,
        "ReplicationInstanceClass": str,
        "ReplicationInstanceStatus": str,
        "AllocatedStorage": int,
        "InstanceCreateTime": datetime,
        "VpcSecurityGroups": List[
            ClientRebootReplicationInstanceResponseReplicationInstanceVpcSecurityGroupsTypeDef
        ],
        "AvailabilityZone": str,
        "ReplicationSubnetGroup": ClientRebootReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupTypeDef,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientRebootReplicationInstanceResponseReplicationInstancePendingModifiedValuesTypeDef,
        "MultiAZ": bool,
        "EngineVersion": str,
        "AutoMinorVersionUpgrade": bool,
        "KmsKeyId": str,
        "ReplicationInstanceArn": str,
        "ReplicationInstancePublicIpAddress": str,
        "ReplicationInstancePrivateIpAddress": str,
        "ReplicationInstancePublicIpAddresses": List[str],
        "ReplicationInstancePrivateIpAddresses": List[str],
        "PubliclyAccessible": bool,
        "SecondaryAvailabilityZone": str,
        "FreeUntil": datetime,
        "DnsNameServers": str,
    },
    total=False,
)


class ClientRebootReplicationInstanceResponseReplicationInstanceTypeDef(
    _ClientRebootReplicationInstanceResponseReplicationInstanceTypeDef
):
    """
    Type definition for `ClientRebootReplicationInstanceResponse` `ReplicationInstance`

    The replication instance that is being rebooted.

    - **ReplicationInstanceIdentifier** *(string) --*

      The replication instance identifier. This parameter is stored as a lowercase string.

      Constraints:

      * Must contain from 1 to 63 alphanumeric characters or hyphens.

      * First character must be a letter.

      * Cannot end with a hyphen or contain two consecutive hyphens.

      Example: ``myrepinstance``

    - **ReplicationInstanceClass** *(string) --*

      The compute and memory capacity of the replication instance.

      Valid Values: ``dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large | dms.c4.large |
      dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge``

    - **ReplicationInstanceStatus** *(string) --*

      The status of the replication instance.

    - **AllocatedStorage** *(integer) --*

      The amount of storage (in gigabytes) that is allocated for the replication instance.

    - **InstanceCreateTime** *(datetime) --*

      The time the replication instance was created.

    - **VpcSecurityGroups** *(list) --*

      The VPC security group for the instance.

      - *(dict) --*

        - **VpcSecurityGroupId** *(string) --*

          The VPC security group Id.

        - **Status** *(string) --*

          The status of the VPC security group.

    - **AvailabilityZone** *(string) --*

      The Availability Zone for the instance.

    - **ReplicationSubnetGroup** *(dict) --*

      The subnet group for the replication instance.

      - **ReplicationSubnetGroupIdentifier** *(string) --*

        The identifier of the replication instance subnet group.

      - **ReplicationSubnetGroupDescription** *(string) --*

        A description for the replication subnet group.

      - **VpcId** *(string) --*

        The ID of the VPC.

      - **SubnetGroupStatus** *(string) --*

        The status of the subnet group.

      - **Subnets** *(list) --*

        The subnets that are in the subnet group.

        - *(dict) --*

          - **SubnetIdentifier** *(string) --*

            The subnet identifier.

          - **SubnetAvailabilityZone** *(dict) --*

            The Availability Zone of the subnet.

            - **Name** *(string) --*

              The name of the availability zone.

          - **SubnetStatus** *(string) --*

            The status of the subnet.

    - **PreferredMaintenanceWindow** *(string) --*

      The maintenance window times for the replication instance.

    - **PendingModifiedValues** *(dict) --*

      The pending modification values.

      - **ReplicationInstanceClass** *(string) --*

        The compute and memory capacity of the replication instance.

        Valid Values: ``dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large | dms.c4.large
        | dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge``

      - **AllocatedStorage** *(integer) --*

        The amount of storage (in gigabytes) that is allocated for the replication instance.

      - **MultiAZ** *(boolean) --*

        Specifies whether the replication instance is a Multi-AZ deployment. You cannot set the
        ``AvailabilityZone`` parameter if the Multi-AZ parameter is set to ``true`` .

      - **EngineVersion** *(string) --*

        The engine version number of the replication instance.

    - **MultiAZ** *(boolean) --*

      Specifies whether the replication instance is a Multi-AZ deployment. You cannot set the
      ``AvailabilityZone`` parameter if the Multi-AZ parameter is set to ``true`` .

    - **EngineVersion** *(string) --*

      The engine version number of the replication instance.

    - **AutoMinorVersionUpgrade** *(boolean) --*

      Boolean value indicating if minor version upgrades will be automatically applied to the
      instance.

    - **KmsKeyId** *(string) --*

      An AWS KMS key identifier that is used to encrypt the data on the replication instance.

      If you don't specify a value for the ``KmsKeyId`` parameter, then AWS DMS uses your default
      encryption key.

      AWS KMS creates the default encryption key for your AWS account. Your AWS account has a
      different default encryption key for each AWS Region.

    - **ReplicationInstanceArn** *(string) --*

      The Amazon Resource Name (ARN) of the replication instance.

    - **ReplicationInstancePublicIpAddress** *(string) --*

      The public IP address of the replication instance.

    - **ReplicationInstancePrivateIpAddress** *(string) --*

      The private IP address of the replication instance.

    - **ReplicationInstancePublicIpAddresses** *(list) --*

      One or more public IP addresses for the replication instance.

      - *(string) --*

    - **ReplicationInstancePrivateIpAddresses** *(list) --*

      One or more private IP addresses for the replication instance.

      - *(string) --*

    - **PubliclyAccessible** *(boolean) --*

      Specifies the accessibility options for the replication instance. A value of ``true``
      represents an instance with a public IP address. A value of ``false`` represents an
      instance with a private IP address. The default value is ``true`` .

    - **SecondaryAvailabilityZone** *(string) --*

      The availability zone of the standby replication instance in a Multi-AZ deployment.

    - **FreeUntil** *(datetime) --*

      The expiration date of the free replication instance that is part of the Free DMS program.

    - **DnsNameServers** *(string) --*

      The DNS name servers for the replication instance.
    """


_ClientRebootReplicationInstanceResponseTypeDef = TypedDict(
    "_ClientRebootReplicationInstanceResponseTypeDef",
    {
        "ReplicationInstance": ClientRebootReplicationInstanceResponseReplicationInstanceTypeDef
    },
    total=False,
)


class ClientRebootReplicationInstanceResponseTypeDef(
    _ClientRebootReplicationInstanceResponseTypeDef
):
    """
    Type definition for `ClientRebootReplicationInstance` `Response`

    - **ReplicationInstance** *(dict) --*

      The replication instance that is being rebooted.

      - **ReplicationInstanceIdentifier** *(string) --*

        The replication instance identifier. This parameter is stored as a lowercase string.

        Constraints:

        * Must contain from 1 to 63 alphanumeric characters or hyphens.

        * First character must be a letter.

        * Cannot end with a hyphen or contain two consecutive hyphens.

        Example: ``myrepinstance``

      - **ReplicationInstanceClass** *(string) --*

        The compute and memory capacity of the replication instance.

        Valid Values: ``dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large | dms.c4.large |
        dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge``

      - **ReplicationInstanceStatus** *(string) --*

        The status of the replication instance.

      - **AllocatedStorage** *(integer) --*

        The amount of storage (in gigabytes) that is allocated for the replication instance.

      - **InstanceCreateTime** *(datetime) --*

        The time the replication instance was created.

      - **VpcSecurityGroups** *(list) --*

        The VPC security group for the instance.

        - *(dict) --*

          - **VpcSecurityGroupId** *(string) --*

            The VPC security group Id.

          - **Status** *(string) --*

            The status of the VPC security group.

      - **AvailabilityZone** *(string) --*

        The Availability Zone for the instance.

      - **ReplicationSubnetGroup** *(dict) --*

        The subnet group for the replication instance.

        - **ReplicationSubnetGroupIdentifier** *(string) --*

          The identifier of the replication instance subnet group.

        - **ReplicationSubnetGroupDescription** *(string) --*

          A description for the replication subnet group.

        - **VpcId** *(string) --*

          The ID of the VPC.

        - **SubnetGroupStatus** *(string) --*

          The status of the subnet group.

        - **Subnets** *(list) --*

          The subnets that are in the subnet group.

          - *(dict) --*

            - **SubnetIdentifier** *(string) --*

              The subnet identifier.

            - **SubnetAvailabilityZone** *(dict) --*

              The Availability Zone of the subnet.

              - **Name** *(string) --*

                The name of the availability zone.

            - **SubnetStatus** *(string) --*

              The status of the subnet.

      - **PreferredMaintenanceWindow** *(string) --*

        The maintenance window times for the replication instance.

      - **PendingModifiedValues** *(dict) --*

        The pending modification values.

        - **ReplicationInstanceClass** *(string) --*

          The compute and memory capacity of the replication instance.

          Valid Values: ``dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large | dms.c4.large
          | dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge``

        - **AllocatedStorage** *(integer) --*

          The amount of storage (in gigabytes) that is allocated for the replication instance.

        - **MultiAZ** *(boolean) --*

          Specifies whether the replication instance is a Multi-AZ deployment. You cannot set the
          ``AvailabilityZone`` parameter if the Multi-AZ parameter is set to ``true`` .

        - **EngineVersion** *(string) --*

          The engine version number of the replication instance.

      - **MultiAZ** *(boolean) --*

        Specifies whether the replication instance is a Multi-AZ deployment. You cannot set the
        ``AvailabilityZone`` parameter if the Multi-AZ parameter is set to ``true`` .

      - **EngineVersion** *(string) --*

        The engine version number of the replication instance.

      - **AutoMinorVersionUpgrade** *(boolean) --*

        Boolean value indicating if minor version upgrades will be automatically applied to the
        instance.

      - **KmsKeyId** *(string) --*

        An AWS KMS key identifier that is used to encrypt the data on the replication instance.

        If you don't specify a value for the ``KmsKeyId`` parameter, then AWS DMS uses your default
        encryption key.

        AWS KMS creates the default encryption key for your AWS account. Your AWS account has a
        different default encryption key for each AWS Region.

      - **ReplicationInstanceArn** *(string) --*

        The Amazon Resource Name (ARN) of the replication instance.

      - **ReplicationInstancePublicIpAddress** *(string) --*

        The public IP address of the replication instance.

      - **ReplicationInstancePrivateIpAddress** *(string) --*

        The private IP address of the replication instance.

      - **ReplicationInstancePublicIpAddresses** *(list) --*

        One or more public IP addresses for the replication instance.

        - *(string) --*

      - **ReplicationInstancePrivateIpAddresses** *(list) --*

        One or more private IP addresses for the replication instance.

        - *(string) --*

      - **PubliclyAccessible** *(boolean) --*

        Specifies the accessibility options for the replication instance. A value of ``true``
        represents an instance with a public IP address. A value of ``false`` represents an
        instance with a private IP address. The default value is ``true`` .

      - **SecondaryAvailabilityZone** *(string) --*

        The availability zone of the standby replication instance in a Multi-AZ deployment.

      - **FreeUntil** *(datetime) --*

        The expiration date of the free replication instance that is part of the Free DMS program.

      - **DnsNameServers** *(string) --*

        The DNS name servers for the replication instance.
    """


_ClientRefreshSchemasResponseRefreshSchemasStatusTypeDef = TypedDict(
    "_ClientRefreshSchemasResponseRefreshSchemasStatusTypeDef",
    {
        "EndpointArn": str,
        "ReplicationInstanceArn": str,
        "Status": str,
        "LastRefreshDate": datetime,
        "LastFailureMessage": str,
    },
    total=False,
)


class ClientRefreshSchemasResponseRefreshSchemasStatusTypeDef(
    _ClientRefreshSchemasResponseRefreshSchemasStatusTypeDef
):
    """
    Type definition for `ClientRefreshSchemasResponse` `RefreshSchemasStatus`

    The status of the refreshed schema.

    - **EndpointArn** *(string) --*

      The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

    - **ReplicationInstanceArn** *(string) --*

      The Amazon Resource Name (ARN) of the replication instance.

    - **Status** *(string) --*

      The status of the schema.

    - **LastRefreshDate** *(datetime) --*

      The date the schema was last refreshed.

    - **LastFailureMessage** *(string) --*

      The last failure message for the schema.
    """


_ClientRefreshSchemasResponseTypeDef = TypedDict(
    "_ClientRefreshSchemasResponseTypeDef",
    {"RefreshSchemasStatus": ClientRefreshSchemasResponseRefreshSchemasStatusTypeDef},
    total=False,
)


class ClientRefreshSchemasResponseTypeDef(_ClientRefreshSchemasResponseTypeDef):
    """
    Type definition for `ClientRefreshSchemas` `Response`

    - **RefreshSchemasStatus** *(dict) --*

      The status of the refreshed schema.

      - **EndpointArn** *(string) --*

        The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

      - **ReplicationInstanceArn** *(string) --*

        The Amazon Resource Name (ARN) of the replication instance.

      - **Status** *(string) --*

        The status of the schema.

      - **LastRefreshDate** *(datetime) --*

        The date the schema was last refreshed.

      - **LastFailureMessage** *(string) --*

        The last failure message for the schema.
    """


_ClientReloadTablesResponseTypeDef = TypedDict(
    "_ClientReloadTablesResponseTypeDef", {"ReplicationTaskArn": str}, total=False
)


class ClientReloadTablesResponseTypeDef(_ClientReloadTablesResponseTypeDef):
    """
    Type definition for `ClientReloadTables` `Response`

    - **ReplicationTaskArn** *(string) --*

      The Amazon Resource Name (ARN) of the replication task.
    """


_ClientReloadTablesTablesToReloadTypeDef = TypedDict(
    "_ClientReloadTablesTablesToReloadTypeDef",
    {"SchemaName": str, "TableName": str},
    total=False,
)


class ClientReloadTablesTablesToReloadTypeDef(_ClientReloadTablesTablesToReloadTypeDef):
    """
    Type definition for `ClientReloadTables` `TablesToReload`

    - **SchemaName** *(string) --*

      The schema name of the table to be reloaded.

    - **TableName** *(string) --*

      The table name of the table to be reloaded.
    """


_ClientTestConnectionResponseConnectionTypeDef = TypedDict(
    "_ClientTestConnectionResponseConnectionTypeDef",
    {
        "ReplicationInstanceArn": str,
        "EndpointArn": str,
        "Status": str,
        "LastFailureMessage": str,
        "EndpointIdentifier": str,
        "ReplicationInstanceIdentifier": str,
    },
    total=False,
)


class ClientTestConnectionResponseConnectionTypeDef(
    _ClientTestConnectionResponseConnectionTypeDef
):
    """
    Type definition for `ClientTestConnectionResponse` `Connection`

    The connection tested.

    - **ReplicationInstanceArn** *(string) --*

      The Amazon Resource Name (ARN) of the replication instance.

    - **EndpointArn** *(string) --*

      The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

    - **Status** *(string) --*

      The connection status.

    - **LastFailureMessage** *(string) --*

      The error message when the connection last failed.

    - **EndpointIdentifier** *(string) --*

      The identifier of the endpoint. Identifiers must begin with a letter; must contain only
      ASCII letters, digits, and hyphens; and must not end with a hyphen or contain two
      consecutive hyphens.

    - **ReplicationInstanceIdentifier** *(string) --*

      The replication instance identifier. This parameter is stored as a lowercase string.
    """


_ClientTestConnectionResponseTypeDef = TypedDict(
    "_ClientTestConnectionResponseTypeDef",
    {"Connection": ClientTestConnectionResponseConnectionTypeDef},
    total=False,
)


class ClientTestConnectionResponseTypeDef(_ClientTestConnectionResponseTypeDef):
    """
    Type definition for `ClientTestConnection` `Response`

    - **Connection** *(dict) --*

      The connection tested.

      - **ReplicationInstanceArn** *(string) --*

        The Amazon Resource Name (ARN) of the replication instance.

      - **EndpointArn** *(string) --*

        The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

      - **Status** *(string) --*

        The connection status.

      - **LastFailureMessage** *(string) --*

        The error message when the connection last failed.

      - **EndpointIdentifier** *(string) --*

        The identifier of the endpoint. Identifiers must begin with a letter; must contain only
        ASCII letters, digits, and hyphens; and must not end with a hyphen or contain two
        consecutive hyphens.

      - **ReplicationInstanceIdentifier** *(string) --*

        The replication instance identifier. This parameter is stored as a lowercase string.
    """


_DescribeCertificatesPaginateFiltersTypeDef = TypedDict(
    "_DescribeCertificatesPaginateFiltersTypeDef", {"Name": str, "Values": List[str]}
)


class DescribeCertificatesPaginateFiltersTypeDef(
    _DescribeCertificatesPaginateFiltersTypeDef
):
    """
    Type definition for `DescribeCertificatesPaginate` `Filters`

    - **Name** *(string) --* **[REQUIRED]**

      The name of the filter.

    - **Values** *(list) --* **[REQUIRED]**

      The filter value.

      - *(string) --*
    """


_DescribeCertificatesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeCertificatesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeCertificatesPaginatePaginationConfigTypeDef(
    _DescribeCertificatesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeCertificatesPaginate` `PaginationConfig`

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


_DescribeCertificatesPaginateResponseCertificatesTypeDef = TypedDict(
    "_DescribeCertificatesPaginateResponseCertificatesTypeDef",
    {
        "CertificateIdentifier": str,
        "CertificateCreationDate": datetime,
        "CertificatePem": str,
        "CertificateWallet": bytes,
        "CertificateArn": str,
        "CertificateOwner": str,
        "ValidFromDate": datetime,
        "ValidToDate": datetime,
        "SigningAlgorithm": str,
        "KeyLength": int,
    },
    total=False,
)


class DescribeCertificatesPaginateResponseCertificatesTypeDef(
    _DescribeCertificatesPaginateResponseCertificatesTypeDef
):
    """
    Type definition for `DescribeCertificatesPaginateResponse` `Certificates`

    The SSL certificate that can be used to encrypt connections between the endpoints and the
    replication instance.

    - **CertificateIdentifier** *(string) --*

      A customer-assigned name for the certificate. Identifiers must begin with a letter; must
      contain only ASCII letters, digits, and hyphens; and must not end with a hyphen or
      contain two consecutive hyphens.

    - **CertificateCreationDate** *(datetime) --*

      The date that the certificate was created.

    - **CertificatePem** *(string) --*

      The contents of a ``.pem`` file, which contains an X.509 certificate.

    - **CertificateWallet** *(bytes) --*

      The location of an imported Oracle Wallet certificate for use with SSL.

    - **CertificateArn** *(string) --*

      The Amazon Resource Name (ARN) for the certificate.

    - **CertificateOwner** *(string) --*

      The owner of the certificate.

    - **ValidFromDate** *(datetime) --*

      The beginning date that the certificate is valid.

    - **ValidToDate** *(datetime) --*

      The final date that the certificate is valid.

    - **SigningAlgorithm** *(string) --*

      The signing algorithm for the certificate.

    - **KeyLength** *(integer) --*

      The key length of the cryptographic algorithm being used.
    """


_DescribeCertificatesPaginateResponseTypeDef = TypedDict(
    "_DescribeCertificatesPaginateResponseTypeDef",
    {
        "Certificates": List[DescribeCertificatesPaginateResponseCertificatesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class DescribeCertificatesPaginateResponseTypeDef(
    _DescribeCertificatesPaginateResponseTypeDef
):
    """
    Type definition for `DescribeCertificatesPaginate` `Response`

    - **Certificates** *(list) --*

      The Secure Sockets Layer (SSL) certificates associated with the replication instance.

      - *(dict) --*

        The SSL certificate that can be used to encrypt connections between the endpoints and the
        replication instance.

        - **CertificateIdentifier** *(string) --*

          A customer-assigned name for the certificate. Identifiers must begin with a letter; must
          contain only ASCII letters, digits, and hyphens; and must not end with a hyphen or
          contain two consecutive hyphens.

        - **CertificateCreationDate** *(datetime) --*

          The date that the certificate was created.

        - **CertificatePem** *(string) --*

          The contents of a ``.pem`` file, which contains an X.509 certificate.

        - **CertificateWallet** *(bytes) --*

          The location of an imported Oracle Wallet certificate for use with SSL.

        - **CertificateArn** *(string) --*

          The Amazon Resource Name (ARN) for the certificate.

        - **CertificateOwner** *(string) --*

          The owner of the certificate.

        - **ValidFromDate** *(datetime) --*

          The beginning date that the certificate is valid.

        - **ValidToDate** *(datetime) --*

          The final date that the certificate is valid.

        - **SigningAlgorithm** *(string) --*

          The signing algorithm for the certificate.

        - **KeyLength** *(integer) --*

          The key length of the cryptographic algorithm being used.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribeConnectionsPaginateFiltersTypeDef = TypedDict(
    "_DescribeConnectionsPaginateFiltersTypeDef", {"Name": str, "Values": List[str]}
)


class DescribeConnectionsPaginateFiltersTypeDef(
    _DescribeConnectionsPaginateFiltersTypeDef
):
    """
    Type definition for `DescribeConnectionsPaginate` `Filters`

    - **Name** *(string) --* **[REQUIRED]**

      The name of the filter.

    - **Values** *(list) --* **[REQUIRED]**

      The filter value.

      - *(string) --*
    """


_DescribeConnectionsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeConnectionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeConnectionsPaginatePaginationConfigTypeDef(
    _DescribeConnectionsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeConnectionsPaginate` `PaginationConfig`

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


_DescribeConnectionsPaginateResponseConnectionsTypeDef = TypedDict(
    "_DescribeConnectionsPaginateResponseConnectionsTypeDef",
    {
        "ReplicationInstanceArn": str,
        "EndpointArn": str,
        "Status": str,
        "LastFailureMessage": str,
        "EndpointIdentifier": str,
        "ReplicationInstanceIdentifier": str,
    },
    total=False,
)


class DescribeConnectionsPaginateResponseConnectionsTypeDef(
    _DescribeConnectionsPaginateResponseConnectionsTypeDef
):
    """
    Type definition for `DescribeConnectionsPaginateResponse` `Connections`

    - **ReplicationInstanceArn** *(string) --*

      The Amazon Resource Name (ARN) of the replication instance.

    - **EndpointArn** *(string) --*

      The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

    - **Status** *(string) --*

      The connection status.

    - **LastFailureMessage** *(string) --*

      The error message when the connection last failed.

    - **EndpointIdentifier** *(string) --*

      The identifier of the endpoint. Identifiers must begin with a letter; must contain only
      ASCII letters, digits, and hyphens; and must not end with a hyphen or contain two
      consecutive hyphens.

    - **ReplicationInstanceIdentifier** *(string) --*

      The replication instance identifier. This parameter is stored as a lowercase string.
    """


_DescribeConnectionsPaginateResponseTypeDef = TypedDict(
    "_DescribeConnectionsPaginateResponseTypeDef",
    {
        "Connections": List[DescribeConnectionsPaginateResponseConnectionsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class DescribeConnectionsPaginateResponseTypeDef(
    _DescribeConnectionsPaginateResponseTypeDef
):
    """
    Type definition for `DescribeConnectionsPaginate` `Response`

    - **Connections** *(list) --*

      A description of the connections.

      - *(dict) --*

        - **ReplicationInstanceArn** *(string) --*

          The Amazon Resource Name (ARN) of the replication instance.

        - **EndpointArn** *(string) --*

          The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

        - **Status** *(string) --*

          The connection status.

        - **LastFailureMessage** *(string) --*

          The error message when the connection last failed.

        - **EndpointIdentifier** *(string) --*

          The identifier of the endpoint. Identifiers must begin with a letter; must contain only
          ASCII letters, digits, and hyphens; and must not end with a hyphen or contain two
          consecutive hyphens.

        - **ReplicationInstanceIdentifier** *(string) --*

          The replication instance identifier. This parameter is stored as a lowercase string.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribeEndpointTypesPaginateFiltersTypeDef = TypedDict(
    "_DescribeEndpointTypesPaginateFiltersTypeDef", {"Name": str, "Values": List[str]}
)


class DescribeEndpointTypesPaginateFiltersTypeDef(
    _DescribeEndpointTypesPaginateFiltersTypeDef
):
    """
    Type definition for `DescribeEndpointTypesPaginate` `Filters`

    - **Name** *(string) --* **[REQUIRED]**

      The name of the filter.

    - **Values** *(list) --* **[REQUIRED]**

      The filter value.

      - *(string) --*
    """


_DescribeEndpointTypesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeEndpointTypesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeEndpointTypesPaginatePaginationConfigTypeDef(
    _DescribeEndpointTypesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeEndpointTypesPaginate` `PaginationConfig`

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


_DescribeEndpointTypesPaginateResponseSupportedEndpointTypesTypeDef = TypedDict(
    "_DescribeEndpointTypesPaginateResponseSupportedEndpointTypesTypeDef",
    {
        "EngineName": str,
        "SupportsCDC": bool,
        "EndpointType": str,
        "EngineDisplayName": str,
    },
    total=False,
)


class DescribeEndpointTypesPaginateResponseSupportedEndpointTypesTypeDef(
    _DescribeEndpointTypesPaginateResponseSupportedEndpointTypesTypeDef
):
    """
    Type definition for `DescribeEndpointTypesPaginateResponse` `SupportedEndpointTypes`

    - **EngineName** *(string) --*

      The database engine name. Valid values, depending on the EndpointType, include mysql,
      oracle, postgres, mariadb, aurora, aurora-postgresql, redshift, s3, db2, azuredb, sybase,
      dynamodb, mongodb, and sqlserver.

    - **SupportsCDC** *(boolean) --*

      Indicates if Change Data Capture (CDC) is supported.

    - **EndpointType** *(string) --*

      The type of endpoint. Valid values are ``source`` and ``target`` .

    - **EngineDisplayName** *(string) --*

      The expanded name for the engine name. For example, if the ``EngineName`` parameter is
      "aurora," this value would be "Amazon Aurora MySQL."
    """


_DescribeEndpointTypesPaginateResponseTypeDef = TypedDict(
    "_DescribeEndpointTypesPaginateResponseTypeDef",
    {
        "SupportedEndpointTypes": List[
            DescribeEndpointTypesPaginateResponseSupportedEndpointTypesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeEndpointTypesPaginateResponseTypeDef(
    _DescribeEndpointTypesPaginateResponseTypeDef
):
    """
    Type definition for `DescribeEndpointTypesPaginate` `Response`

    - **SupportedEndpointTypes** *(list) --*

      The types of endpoints that are supported.

      - *(dict) --*

        - **EngineName** *(string) --*

          The database engine name. Valid values, depending on the EndpointType, include mysql,
          oracle, postgres, mariadb, aurora, aurora-postgresql, redshift, s3, db2, azuredb, sybase,
          dynamodb, mongodb, and sqlserver.

        - **SupportsCDC** *(boolean) --*

          Indicates if Change Data Capture (CDC) is supported.

        - **EndpointType** *(string) --*

          The type of endpoint. Valid values are ``source`` and ``target`` .

        - **EngineDisplayName** *(string) --*

          The expanded name for the engine name. For example, if the ``EngineName`` parameter is
          "aurora," this value would be "Amazon Aurora MySQL."

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribeEndpointsPaginateFiltersTypeDef = TypedDict(
    "_DescribeEndpointsPaginateFiltersTypeDef", {"Name": str, "Values": List[str]}
)


class DescribeEndpointsPaginateFiltersTypeDef(_DescribeEndpointsPaginateFiltersTypeDef):
    """
    Type definition for `DescribeEndpointsPaginate` `Filters`

    - **Name** *(string) --* **[REQUIRED]**

      The name of the filter.

    - **Values** *(list) --* **[REQUIRED]**

      The filter value.

      - *(string) --*
    """


_DescribeEndpointsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeEndpointsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeEndpointsPaginatePaginationConfigTypeDef(
    _DescribeEndpointsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeEndpointsPaginate` `PaginationConfig`

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


_DescribeEndpointsPaginateResponseEndpointsDmsTransferSettingsTypeDef = TypedDict(
    "_DescribeEndpointsPaginateResponseEndpointsDmsTransferSettingsTypeDef",
    {"ServiceAccessRoleArn": str, "BucketName": str},
    total=False,
)


class DescribeEndpointsPaginateResponseEndpointsDmsTransferSettingsTypeDef(
    _DescribeEndpointsPaginateResponseEndpointsDmsTransferSettingsTypeDef
):
    """
    Type definition for `DescribeEndpointsPaginateResponseEndpoints` `DmsTransferSettings`

    The settings in JSON format for the DMS transfer type of source endpoint.

    Possible settings include the following:

    * ``ServiceAccessRoleArn`` - The IAM role that has permission to access the Amazon S3
    bucket.

    * ``BucketName`` - The name of the S3 bucket to use.

    * ``CompressionType`` - An optional parameter to use GZIP to compress the target files.
    To use GZIP, set this value to ``NONE`` (the default). To keep the files uncompressed,
    don't use this value.

    Shorthand syntax for these settings is as follows:
    ``ServiceAccessRoleArn=string,BucketName=string,CompressionType=string``

    JSON syntax for these settings is as follows: ``{ "ServiceAccessRoleArn": "string",
    "BucketName": "string", "CompressionType": "none"|"gzip" }``

    - **ServiceAccessRoleArn** *(string) --*

      The IAM role that has permission to access the Amazon S3 bucket.

    - **BucketName** *(string) --*

      The name of the S3 bucket to use.
    """


_DescribeEndpointsPaginateResponseEndpointsDynamoDbSettingsTypeDef = TypedDict(
    "_DescribeEndpointsPaginateResponseEndpointsDynamoDbSettingsTypeDef",
    {"ServiceAccessRoleArn": str},
    total=False,
)


class DescribeEndpointsPaginateResponseEndpointsDynamoDbSettingsTypeDef(
    _DescribeEndpointsPaginateResponseEndpointsDynamoDbSettingsTypeDef
):
    """
    Type definition for `DescribeEndpointsPaginateResponseEndpoints` `DynamoDbSettings`

    The settings for the target DynamoDB database. For more information, see the
    ``DynamoDBSettings`` structure.

    - **ServiceAccessRoleArn** *(string) --*

      The Amazon Resource Name (ARN) used by the service access IAM role.
    """


_DescribeEndpointsPaginateResponseEndpointsElasticsearchSettingsTypeDef = TypedDict(
    "_DescribeEndpointsPaginateResponseEndpointsElasticsearchSettingsTypeDef",
    {
        "ServiceAccessRoleArn": str,
        "EndpointUri": str,
        "FullLoadErrorPercentage": int,
        "ErrorRetryDuration": int,
    },
    total=False,
)


class DescribeEndpointsPaginateResponseEndpointsElasticsearchSettingsTypeDef(
    _DescribeEndpointsPaginateResponseEndpointsElasticsearchSettingsTypeDef
):
    """
    Type definition for `DescribeEndpointsPaginateResponseEndpoints` `ElasticsearchSettings`

    The settings for the Elasticsearch source endpoint. For more information, see the
    ``ElasticsearchSettings`` structure.

    - **ServiceAccessRoleArn** *(string) --*

      The Amazon Resource Name (ARN) used by service to access the IAM role.

    - **EndpointUri** *(string) --*

      The endpoint for the Elasticsearch cluster.

    - **FullLoadErrorPercentage** *(integer) --*

      The maximum percentage of records that can fail to be written before a full load
      operation stops.

    - **ErrorRetryDuration** *(integer) --*

      The maximum number of seconds that DMS retries failed API requests to the Elasticsearch
      cluster.
    """


_DescribeEndpointsPaginateResponseEndpointsKinesisSettingsTypeDef = TypedDict(
    "_DescribeEndpointsPaginateResponseEndpointsKinesisSettingsTypeDef",
    {"StreamArn": str, "MessageFormat": str, "ServiceAccessRoleArn": str},
    total=False,
)


class DescribeEndpointsPaginateResponseEndpointsKinesisSettingsTypeDef(
    _DescribeEndpointsPaginateResponseEndpointsKinesisSettingsTypeDef
):
    """
    Type definition for `DescribeEndpointsPaginateResponseEndpoints` `KinesisSettings`

    The settings for the Amazon Kinesis source endpoint. For more information, see the
    ``KinesisSettings`` structure.

    - **StreamArn** *(string) --*

      The Amazon Resource Name (ARN) for the Amazon Kinesis Data Streams endpoint.

    - **MessageFormat** *(string) --*

      The output format for the records created on the endpoint. The message format is
      ``JSON`` .

    - **ServiceAccessRoleArn** *(string) --*

      The Amazon Resource Name (ARN) for the IAM role that DMS uses to write to the Amazon
      Kinesis data stream.
    """


_DescribeEndpointsPaginateResponseEndpointsMongoDbSettingsTypeDef = TypedDict(
    "_DescribeEndpointsPaginateResponseEndpointsMongoDbSettingsTypeDef",
    {
        "Username": str,
        "Password": str,
        "ServerName": str,
        "Port": int,
        "DatabaseName": str,
        "AuthType": str,
        "AuthMechanism": str,
        "NestingLevel": str,
        "ExtractDocId": str,
        "DocsToInvestigate": str,
        "AuthSource": str,
        "KmsKeyId": str,
    },
    total=False,
)


class DescribeEndpointsPaginateResponseEndpointsMongoDbSettingsTypeDef(
    _DescribeEndpointsPaginateResponseEndpointsMongoDbSettingsTypeDef
):
    """
    Type definition for `DescribeEndpointsPaginateResponseEndpoints` `MongoDbSettings`

    The settings for the MongoDB source endpoint. For more information, see the
    ``MongoDbSettings`` structure.

    - **Username** *(string) --*

      The user name you use to access the MongoDB source endpoint.

    - **Password** *(string) --*

      The password for the user account you use to access the MongoDB source endpoint.

    - **ServerName** *(string) --*

      The name of the server on the MongoDB source endpoint.

    - **Port** *(integer) --*

      The port value for the MongoDB source endpoint.

    - **DatabaseName** *(string) --*

      The database name on the MongoDB source endpoint.

    - **AuthType** *(string) --*

      The authentication type you use to access the MongoDB source endpoint.

      Valid values: NO, PASSWORD

      When NO is selected, user name and password parameters are not used and can be empty.

    - **AuthMechanism** *(string) --*

      The authentication mechanism you use to access the MongoDB source endpoint.

      Valid values: DEFAULT, MONGODB_CR, SCRAM_SHA_1

      DEFAULT – For MongoDB version 2.x, use MONGODB_CR. For MongoDB version 3.x, use
      SCRAM_SHA_1. This setting is not used when authType=No.

    - **NestingLevel** *(string) --*

      Specifies either document or table mode.

      Valid values: NONE, ONE

      Default value is NONE. Specify NONE to use document mode. Specify ONE to use table mode.

    - **ExtractDocId** *(string) --*

      Specifies the document ID. Use this setting when ``NestingLevel`` is set to NONE.

      Default value is false.

    - **DocsToInvestigate** *(string) --*

      Indicates the number of documents to preview to determine the document organization.
      Use this setting when ``NestingLevel`` is set to ONE.

      Must be a positive value greater than 0. Default value is 1000.

    - **AuthSource** *(string) --*

      The MongoDB database name. This setting is not used when ``authType=NO`` .

      The default is admin.

    - **KmsKeyId** *(string) --*

      The AWS KMS key identifier that is used to encrypt the content on the replication
      instance. If you don't specify a value for the ``KmsKeyId`` parameter, then AWS DMS
      uses your default encryption key. AWS KMS creates the default encryption key for your
      AWS account. Your AWS account has a different default encryption key for each AWS
      Region.
    """


_DescribeEndpointsPaginateResponseEndpointsRedshiftSettingsTypeDef = TypedDict(
    "_DescribeEndpointsPaginateResponseEndpointsRedshiftSettingsTypeDef",
    {
        "AcceptAnyDate": bool,
        "AfterConnectScript": str,
        "BucketFolder": str,
        "BucketName": str,
        "ConnectionTimeout": int,
        "DatabaseName": str,
        "DateFormat": str,
        "EmptyAsNull": bool,
        "EncryptionMode": str,
        "FileTransferUploadStreams": int,
        "LoadTimeout": int,
        "MaxFileSize": int,
        "Password": str,
        "Port": int,
        "RemoveQuotes": bool,
        "ReplaceInvalidChars": str,
        "ReplaceChars": str,
        "ServerName": str,
        "ServiceAccessRoleArn": str,
        "ServerSideEncryptionKmsKeyId": str,
        "TimeFormat": str,
        "TrimBlanks": bool,
        "TruncateColumns": bool,
        "Username": str,
        "WriteBufferSize": int,
    },
    total=False,
)


class DescribeEndpointsPaginateResponseEndpointsRedshiftSettingsTypeDef(
    _DescribeEndpointsPaginateResponseEndpointsRedshiftSettingsTypeDef
):
    """
    Type definition for `DescribeEndpointsPaginateResponseEndpoints` `RedshiftSettings`

    Settings for the Amazon Redshift endpoint.

    - **AcceptAnyDate** *(boolean) --*

      A value that indicates to allow any date format, including invalid formats such as
      00/00/00 00:00:00, to be loaded without generating an error. You can choose ``true`` or
      ``false`` (the default).

      This parameter applies only to TIMESTAMP and DATE columns. Always use ACCEPTANYDATE
      with the DATEFORMAT parameter. If the date format for the data doesn't match the
      DATEFORMAT specification, Amazon Redshift inserts a NULL value into that field.

    - **AfterConnectScript** *(string) --*

      Code to run after connecting. This parameter should contain the code itself, not the
      name of a file containing the code.

    - **BucketFolder** *(string) --*

      The location where the comma-separated value (.csv) files are stored before being
      uploaded to the S3 bucket.

    - **BucketName** *(string) --*

      The name of the S3 bucket you want to use

    - **ConnectionTimeout** *(integer) --*

      A value that sets the amount of time to wait (in milliseconds) before timing out,
      beginning from when you initially establish a connection.

    - **DatabaseName** *(string) --*

      The name of the Amazon Redshift data warehouse (service) that you are working with.

    - **DateFormat** *(string) --*

      The date format that you are using. Valid values are ``auto`` (case-sensitive), your
      date format string enclosed in quotes, or NULL. If this parameter is left unset (NULL),
      it defaults to a format of 'YYYY-MM-DD'. Using ``auto`` recognizes most strings, even
      some that aren't supported when you use a date format string.

      If your date and time values use formats different from each other, set this to
      ``auto`` .

    - **EmptyAsNull** *(boolean) --*

      A value that specifies whether AWS DMS should migrate empty CHAR and VARCHAR fields as
      NULL. A value of ``true`` sets empty CHAR and VARCHAR fields to null. The default is
      ``false`` .

    - **EncryptionMode** *(string) --*

      The type of server-side encryption that you want to use for your data. This encryption
      type is part of the endpoint settings or the extra connections attributes for Amazon
      S3. You can choose either ``SSE_S3`` (the default) or ``SSE_KMS`` . To use ``SSE_S3`` ,
      create an AWS Identity and Access Management (IAM) role with a policy that allows
      ``"arn:aws:s3:::*"`` to use the following actions: ``"s3:PutObject", "s3:ListBucket"``

    - **FileTransferUploadStreams** *(integer) --*

      The number of threads used to upload a single file. This parameter accepts a value from
      1 through 64. It defaults to 10.

    - **LoadTimeout** *(integer) --*

      The amount of time to wait (in milliseconds) before timing out, beginning from when you
      begin loading.

    - **MaxFileSize** *(integer) --*

      The maximum size (in KB) of any .csv file used to transfer data to Amazon Redshift.
      This accepts a value from 1 through 1,048,576. It defaults to 32,768 KB (32 MB).

    - **Password** *(string) --*

      The password for the user named in the ``username`` property.

    - **Port** *(integer) --*

      The port number for Amazon Redshift. The default value is 5439.

    - **RemoveQuotes** *(boolean) --*

      A value that specifies to remove surrounding quotation marks from strings in the
      incoming data. All characters within the quotation marks, including delimiters, are
      retained. Choose ``true`` to remove quotation marks. The default is ``false`` .

    - **ReplaceInvalidChars** *(string) --*

      A list of characters that you want to replace. Use with ``ReplaceChars`` .

    - **ReplaceChars** *(string) --*

      A value that specifies to replaces the invalid characters specified in
      ``ReplaceInvalidChars`` , substituting the specified characters instead. The default is
      ``"?"`` .

    - **ServerName** *(string) --*

      The name of the Amazon Redshift cluster you are using.

    - **ServiceAccessRoleArn** *(string) --*

      The Amazon Resource Name (ARN) of the IAM role that has access to the Amazon Redshift
      service.

    - **ServerSideEncryptionKmsKeyId** *(string) --*

      The AWS KMS key ID. If you are using ``SSE_KMS`` for the ``EncryptionMode`` , provide
      this key ID. The key that you use needs an attached policy that enables IAM user
      permissions and allows use of the key.

    - **TimeFormat** *(string) --*

      The time format that you want to use. Valid values are ``auto`` (case-sensitive),
      ``'timeformat_string'`` , ``'epochsecs'`` , or ``'epochmillisecs'`` . It defaults to
      10. Using ``auto`` recognizes most strings, even some that aren't supported when you
      use a time format string.

      If your date and time values use formats different from each other, set this parameter
      to ``auto`` .

    - **TrimBlanks** *(boolean) --*

      A value that specifies to remove the trailing white space characters from a VARCHAR
      string. This parameter applies only to columns with a VARCHAR data type. Choose
      ``true`` to remove unneeded white space. The default is ``false`` .

    - **TruncateColumns** *(boolean) --*

      A value that specifies to truncate data in columns to the appropriate number of
      characters, so that the data fits in the column. This parameter applies only to columns
      with a VARCHAR or CHAR data type, and rows with a size of 4 MB or less. Choose ``true``
      to truncate data. The default is ``false`` .

    - **Username** *(string) --*

      An Amazon Redshift user name for a registered user.

    - **WriteBufferSize** *(integer) --*

      The size of the write buffer to use in rows. Valid values range from 1 through 2,048.
      The default is 1,024. Use this setting to tune performance.
    """


_DescribeEndpointsPaginateResponseEndpointsS3SettingsTypeDef = TypedDict(
    "_DescribeEndpointsPaginateResponseEndpointsS3SettingsTypeDef",
    {
        "ServiceAccessRoleArn": str,
        "ExternalTableDefinition": str,
        "CsvRowDelimiter": str,
        "CsvDelimiter": str,
        "BucketFolder": str,
        "BucketName": str,
        "CompressionType": str,
        "EncryptionMode": str,
        "ServerSideEncryptionKmsKeyId": str,
        "DataFormat": str,
        "EncodingType": str,
        "DictPageSizeLimit": int,
        "RowGroupLength": int,
        "DataPageSize": int,
        "ParquetVersion": str,
        "EnableStatistics": bool,
        "IncludeOpForFullLoad": bool,
        "CdcInsertsOnly": bool,
        "TimestampColumnName": str,
        "ParquetTimestampInMillisecond": bool,
    },
    total=False,
)


class DescribeEndpointsPaginateResponseEndpointsS3SettingsTypeDef(
    _DescribeEndpointsPaginateResponseEndpointsS3SettingsTypeDef
):
    """
    Type definition for `DescribeEndpointsPaginateResponseEndpoints` `S3Settings`

    The settings for the S3 target endpoint. For more information, see the ``S3Settings``
    structure.

    - **ServiceAccessRoleArn** *(string) --*

      The Amazon Resource Name (ARN) used by the service access IAM role.

    - **ExternalTableDefinition** *(string) --*

      The external table definition.

    - **CsvRowDelimiter** *(string) --*

      The delimiter used to separate rows in the source files. The default is a carriage
      return (``\\n`` ).

    - **CsvDelimiter** *(string) --*

      The delimiter used to separate columns in the source files. The default is a comma.

    - **BucketFolder** *(string) --*

      An optional parameter to set a folder name in the S3 bucket. If provided, tables are
      created in the path `` *bucketFolder* /*schema_name* /*table_name* /`` . If this
      parameter is not specified, then the path used is `` *schema_name* /*table_name* /`` .

    - **BucketName** *(string) --*

      The name of the S3 bucket.

    - **CompressionType** *(string) --*

      An optional parameter to use GZIP to compress the target files. Set to GZIP to compress
      the target files. Set to NONE (the default) or do not use to leave the files
      uncompressed. Applies to both .csv and .parquet file formats.

    - **EncryptionMode** *(string) --*

      The type of server-side encryption that you want to use for your data. This encryption
      type is part of the endpoint settings or the extra connections attributes for Amazon
      S3. You can choose either ``SSE_S3`` (the default) or ``SSE_KMS`` . To use ``SSE_S3`` ,
      you need an AWS Identity and Access Management (IAM) role with permission to allow
      ``"arn:aws:s3:::dms-*"`` to use the following actions:

      * ``s3:CreateBucket``

      * ``s3:ListBucket``

      * ``s3:DeleteBucket``

      * ``s3:GetBucketLocation``

      * ``s3:GetObject``

      * ``s3:PutObject``

      * ``s3:DeleteObject``

      * ``s3:GetObjectVersion``

      * ``s3:GetBucketPolicy``

      * ``s3:PutBucketPolicy``

      * ``s3:DeleteBucketPolicy``

    - **ServerSideEncryptionKmsKeyId** *(string) --*

      If you are using ``SSE_KMS`` for the ``EncryptionMode`` , provide the AWS KMS key ID.
      The key that you use needs an attached policy that enables AWS Identity and Access
      Management (IAM) user permissions and allows use of the key.

      Here is a CLI example: ``aws dms create-endpoint --endpoint-identifier *value*
      --endpoint-type target --engine-name s3 --s3-settings ServiceAccessRoleArn=*value*
      ,BucketFolder=*value* ,BucketName=*value*
      ,EncryptionMode=SSE_KMS,ServerSideEncryptionKmsKeyId=*value* ``

    - **DataFormat** *(string) --*

      The format of the data that you want to use for output. You can choose one of the
      following:

      * ``csv`` : This is a row-based file format with comma-separated values (.csv).

      * ``parquet`` : Apache Parquet (.parquet) is a columnar storage file format that
      features efficient compression and provides faster query response.

    - **EncodingType** *(string) --*

      The type of encoding you are using:

      * ``RLE_DICTIONARY`` uses a combination of bit-packing and run-length encoding to store
      repeated values more efficiently. This is the default.

      * ``PLAIN`` doesn't use encoding at all. Values are stored as they are.

      * ``PLAIN_DICTIONARY`` builds a dictionary of the values encountered in a given column.
      The dictionary is stored in a dictionary page for each column chunk.

    - **DictPageSizeLimit** *(integer) --*

      The maximum size of an encoded dictionary page of a column. If the dictionary page
      exceeds this, this column is stored using an encoding type of ``PLAIN`` . This
      parameter defaults to 1024 * 1024 bytes (1 MiB), the maximum size of a dictionary page
      before it reverts to ``PLAIN`` encoding. This size is used for .parquet file format
      only.

    - **RowGroupLength** *(integer) --*

      The number of rows in a row group. A smaller row group size provides faster reads. But
      as the number of row groups grows, the slower writes become. This parameter defaults to
      10,000 rows. This number is used for .parquet file format only.

      If you choose a value larger than the maximum, ``RowGroupLength`` is set to the max row
      group length in bytes (64 * 1024 * 1024).

    - **DataPageSize** *(integer) --*

      The size of one data page in bytes. This parameter defaults to 1024 * 1024 bytes (1
      MiB). This number is used for .parquet file format only.

    - **ParquetVersion** *(string) --*

      The version of the Apache Parquet format that you want to use: ``parquet_1_0`` (the
      default) or ``parquet_2_0`` .

    - **EnableStatistics** *(boolean) --*

      A value that enables statistics for Parquet pages and row groups. Choose ``true`` to
      enable statistics, ``false`` to disable. Statistics include ``NULL`` , ``DISTINCT`` ,
      ``MAX`` , and ``MIN`` values. This parameter defaults to ``true`` . This value is used
      for .parquet file format only.

    - **IncludeOpForFullLoad** *(boolean) --*

      A value that enables a full load to write INSERT operations to the comma-separated
      value (.csv) output files only to indicate how the rows were added to the source
      database.

      .. note::

        AWS DMS supports the ``IncludeOpForFullLoad`` parameter in versions 3.1.4 and later.

      For full load, records can only be inserted. By default (the ``false`` setting), no
      information is recorded in these output files for a full load to indicate that the rows
      were inserted at the source database. If ``IncludeOpForFullLoad`` is set to ``true`` or
      ``y`` , the INSERT is recorded as an I annotation in the first field of the .csv file.
      This allows the format of your target records from a full load to be consistent with
      the target records from a CDC load.

      .. note::

        This setting works together with the ``CdcInsertsOnly`` parameter for output to .csv
        files only. For more information about how these settings work together, see
        `Indicating Source DB Operations in Migrated S3 Data
        <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring.InsertOps>`__
        in the *AWS Database Migration Service User Guide.* .

    - **CdcInsertsOnly** *(boolean) --*

      A value that enables a change data capture (CDC) load to write only INSERT operations
      to .csv or columnar storage (.parquet) output files. By default (the ``false``
      setting), the first field in a .csv or .parquet record contains the letter I (INSERT),
      U (UPDATE), or D (DELETE). These values indicate whether the row was inserted, updated,
      or deleted at the source database for a CDC load to the target.

      If ``CdcInsertsOnly`` is set to ``true`` or ``y`` , only INSERTs from the source
      database are migrated to the .csv or .parquet file. For .csv format only, how these
      INSERTs are recorded depends on the value of ``IncludeOpForFullLoad`` . If
      ``IncludeOpForFullLoad`` is set to ``true`` , the first field of every CDC record is
      set to I to indicate the INSERT operation at the source. If ``IncludeOpForFullLoad`` is
      set to ``false`` , every CDC record is written without a first field to indicate the
      INSERT operation at the source. For more information about how these settings work
      together, see `Indicating Source DB Operations in Migrated S3 Data
      <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring.InsertOps>`__
      in the *AWS Database Migration Service User Guide.* .

      .. note::

        AWS DMS supports this interaction between the ``CdcInsertsOnly`` and
        ``IncludeOpForFullLoad`` parameters in versions 3.1.4 and later.

    - **TimestampColumnName** *(string) --*

      A value that when nonblank causes AWS DMS to add a column with timestamp information to
      the endpoint data for an Amazon S3 target.

      .. note::

        AWS DMS supports the ``TimestampColumnName`` parameter in versions 3.1.4 and later.

      DMS includes an additional ``STRING`` column in the .csv or .parquet object files of
      your migrated data when you set ``TimestampColumnName`` to a nonblank value.

      For a full load, each row of this timestamp column contains a timestamp for when the
      data was transferred from the source to the target by DMS.

      For a change data capture (CDC) load, each row of the timestamp column contains the
      timestamp for the commit of that row in the source database.

      The string format for this timestamp column value is ``yyyy-MM-dd HH:mm:ss.SSSSSS`` .
      By default, the precision of this value is in microseconds. For a CDC load, the
      rounding of the precision depends on the commit timestamp supported by DMS for the
      source database.

      When the ``AddColumnName`` parameter is set to ``true`` , DMS also includes a name for
      the timestamp column that you set with ``TimestampColumnName`` .

    - **ParquetTimestampInMillisecond** *(boolean) --*

      A value that specifies the precision of any ``TIMESTAMP`` column values that are
      written to an Amazon S3 object file in .parquet format.

      .. note::

        AWS DMS supports the ``ParquetTimestampInMillisecond`` parameter in versions 3.1.4
        and later.

      When ``ParquetTimestampInMillisecond`` is set to ``true`` or ``y`` , AWS DMS writes all
      ``TIMESTAMP`` columns in a .parquet formatted file with millisecond precision.
      Otherwise, DMS writes them with microsecond precision.

      Currently, Amazon Athena and AWS Glue can handle only millisecond precision for
      ``TIMESTAMP`` values. Set this parameter to ``true`` for S3 endpoint object files that
      are .parquet formatted only if you plan to query or process the data with Athena or AWS
      Glue.

      .. note::

        AWS DMS writes any ``TIMESTAMP`` column values written to an S3 file in .csv format
        with microsecond precision.

        Setting ``ParquetTimestampInMillisecond`` has no effect on the string format of the
        timestamp column value that is inserted by setting the ``TimestampColumnName``
        parameter.
    """


_DescribeEndpointsPaginateResponseEndpointsTypeDef = TypedDict(
    "_DescribeEndpointsPaginateResponseEndpointsTypeDef",
    {
        "EndpointIdentifier": str,
        "EndpointType": str,
        "EngineName": str,
        "EngineDisplayName": str,
        "Username": str,
        "ServerName": str,
        "Port": int,
        "DatabaseName": str,
        "ExtraConnectionAttributes": str,
        "Status": str,
        "KmsKeyId": str,
        "EndpointArn": str,
        "CertificateArn": str,
        "SslMode": str,
        "ServiceAccessRoleArn": str,
        "ExternalTableDefinition": str,
        "ExternalId": str,
        "DynamoDbSettings": DescribeEndpointsPaginateResponseEndpointsDynamoDbSettingsTypeDef,
        "S3Settings": DescribeEndpointsPaginateResponseEndpointsS3SettingsTypeDef,
        "DmsTransferSettings": DescribeEndpointsPaginateResponseEndpointsDmsTransferSettingsTypeDef,
        "MongoDbSettings": DescribeEndpointsPaginateResponseEndpointsMongoDbSettingsTypeDef,
        "KinesisSettings": DescribeEndpointsPaginateResponseEndpointsKinesisSettingsTypeDef,
        "ElasticsearchSettings": DescribeEndpointsPaginateResponseEndpointsElasticsearchSettingsTypeDef,
        "RedshiftSettings": DescribeEndpointsPaginateResponseEndpointsRedshiftSettingsTypeDef,
    },
    total=False,
)


class DescribeEndpointsPaginateResponseEndpointsTypeDef(
    _DescribeEndpointsPaginateResponseEndpointsTypeDef
):
    """
    Type definition for `DescribeEndpointsPaginateResponse` `Endpoints`

    - **EndpointIdentifier** *(string) --*

      The database endpoint identifier. Identifiers must begin with a letter; must contain only
      ASCII letters, digits, and hyphens; and must not end with a hyphen or contain two
      consecutive hyphens.

    - **EndpointType** *(string) --*

      The type of endpoint. Valid values are ``source`` and ``target`` .

    - **EngineName** *(string) --*

      The database engine name. Valid values, depending on the EndpointType, include mysql,
      oracle, postgres, mariadb, aurora, aurora-postgresql, redshift, s3, db2, azuredb, sybase,
      dynamodb, mongodb, and sqlserver.

    - **EngineDisplayName** *(string) --*

      The expanded name for the engine name. For example, if the ``EngineName`` parameter is
      "aurora," this value would be "Amazon Aurora MySQL."

    - **Username** *(string) --*

      The user name used to connect to the endpoint.

    - **ServerName** *(string) --*

      The name of the server at the endpoint.

    - **Port** *(integer) --*

      The port value used to access the endpoint.

    - **DatabaseName** *(string) --*

      The name of the database at the endpoint.

    - **ExtraConnectionAttributes** *(string) --*

      Additional connection attributes used to connect to the endpoint.

    - **Status** *(string) --*

      The status of the endpoint.

    - **KmsKeyId** *(string) --*

      An AWS KMS key identifier that is used to encrypt the connection parameters for the
      endpoint.

      If you don't specify a value for the ``KmsKeyId`` parameter, then AWS DMS uses your
      default encryption key.

      AWS KMS creates the default encryption key for your AWS account. Your AWS account has a
      different default encryption key for each AWS Region.

    - **EndpointArn** *(string) --*

      The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

    - **CertificateArn** *(string) --*

      The Amazon Resource Name (ARN) used for SSL connection to the endpoint.

    - **SslMode** *(string) --*

      The SSL mode used to connect to the endpoint. The default value is ``none`` .

    - **ServiceAccessRoleArn** *(string) --*

      The Amazon Resource Name (ARN) used by the service access IAM role.

    - **ExternalTableDefinition** *(string) --*

      The external table definition.

    - **ExternalId** *(string) --*

      Value returned by a call to CreateEndpoint that can be used for cross-account validation.
      Use it on a subsequent call to CreateEndpoint to create the endpoint with a cross-account.

    - **DynamoDbSettings** *(dict) --*

      The settings for the target DynamoDB database. For more information, see the
      ``DynamoDBSettings`` structure.

      - **ServiceAccessRoleArn** *(string) --*

        The Amazon Resource Name (ARN) used by the service access IAM role.

    - **S3Settings** *(dict) --*

      The settings for the S3 target endpoint. For more information, see the ``S3Settings``
      structure.

      - **ServiceAccessRoleArn** *(string) --*

        The Amazon Resource Name (ARN) used by the service access IAM role.

      - **ExternalTableDefinition** *(string) --*

        The external table definition.

      - **CsvRowDelimiter** *(string) --*

        The delimiter used to separate rows in the source files. The default is a carriage
        return (``\\n`` ).

      - **CsvDelimiter** *(string) --*

        The delimiter used to separate columns in the source files. The default is a comma.

      - **BucketFolder** *(string) --*

        An optional parameter to set a folder name in the S3 bucket. If provided, tables are
        created in the path `` *bucketFolder* /*schema_name* /*table_name* /`` . If this
        parameter is not specified, then the path used is `` *schema_name* /*table_name* /`` .

      - **BucketName** *(string) --*

        The name of the S3 bucket.

      - **CompressionType** *(string) --*

        An optional parameter to use GZIP to compress the target files. Set to GZIP to compress
        the target files. Set to NONE (the default) or do not use to leave the files
        uncompressed. Applies to both .csv and .parquet file formats.

      - **EncryptionMode** *(string) --*

        The type of server-side encryption that you want to use for your data. This encryption
        type is part of the endpoint settings or the extra connections attributes for Amazon
        S3. You can choose either ``SSE_S3`` (the default) or ``SSE_KMS`` . To use ``SSE_S3`` ,
        you need an AWS Identity and Access Management (IAM) role with permission to allow
        ``"arn:aws:s3:::dms-*"`` to use the following actions:

        * ``s3:CreateBucket``

        * ``s3:ListBucket``

        * ``s3:DeleteBucket``

        * ``s3:GetBucketLocation``

        * ``s3:GetObject``

        * ``s3:PutObject``

        * ``s3:DeleteObject``

        * ``s3:GetObjectVersion``

        * ``s3:GetBucketPolicy``

        * ``s3:PutBucketPolicy``

        * ``s3:DeleteBucketPolicy``

      - **ServerSideEncryptionKmsKeyId** *(string) --*

        If you are using ``SSE_KMS`` for the ``EncryptionMode`` , provide the AWS KMS key ID.
        The key that you use needs an attached policy that enables AWS Identity and Access
        Management (IAM) user permissions and allows use of the key.

        Here is a CLI example: ``aws dms create-endpoint --endpoint-identifier *value*
        --endpoint-type target --engine-name s3 --s3-settings ServiceAccessRoleArn=*value*
        ,BucketFolder=*value* ,BucketName=*value*
        ,EncryptionMode=SSE_KMS,ServerSideEncryptionKmsKeyId=*value* ``

      - **DataFormat** *(string) --*

        The format of the data that you want to use for output. You can choose one of the
        following:

        * ``csv`` : This is a row-based file format with comma-separated values (.csv).

        * ``parquet`` : Apache Parquet (.parquet) is a columnar storage file format that
        features efficient compression and provides faster query response.

      - **EncodingType** *(string) --*

        The type of encoding you are using:

        * ``RLE_DICTIONARY`` uses a combination of bit-packing and run-length encoding to store
        repeated values more efficiently. This is the default.

        * ``PLAIN`` doesn't use encoding at all. Values are stored as they are.

        * ``PLAIN_DICTIONARY`` builds a dictionary of the values encountered in a given column.
        The dictionary is stored in a dictionary page for each column chunk.

      - **DictPageSizeLimit** *(integer) --*

        The maximum size of an encoded dictionary page of a column. If the dictionary page
        exceeds this, this column is stored using an encoding type of ``PLAIN`` . This
        parameter defaults to 1024 * 1024 bytes (1 MiB), the maximum size of a dictionary page
        before it reverts to ``PLAIN`` encoding. This size is used for .parquet file format
        only.

      - **RowGroupLength** *(integer) --*

        The number of rows in a row group. A smaller row group size provides faster reads. But
        as the number of row groups grows, the slower writes become. This parameter defaults to
        10,000 rows. This number is used for .parquet file format only.

        If you choose a value larger than the maximum, ``RowGroupLength`` is set to the max row
        group length in bytes (64 * 1024 * 1024).

      - **DataPageSize** *(integer) --*

        The size of one data page in bytes. This parameter defaults to 1024 * 1024 bytes (1
        MiB). This number is used for .parquet file format only.

      - **ParquetVersion** *(string) --*

        The version of the Apache Parquet format that you want to use: ``parquet_1_0`` (the
        default) or ``parquet_2_0`` .

      - **EnableStatistics** *(boolean) --*

        A value that enables statistics for Parquet pages and row groups. Choose ``true`` to
        enable statistics, ``false`` to disable. Statistics include ``NULL`` , ``DISTINCT`` ,
        ``MAX`` , and ``MIN`` values. This parameter defaults to ``true`` . This value is used
        for .parquet file format only.

      - **IncludeOpForFullLoad** *(boolean) --*

        A value that enables a full load to write INSERT operations to the comma-separated
        value (.csv) output files only to indicate how the rows were added to the source
        database.

        .. note::

          AWS DMS supports the ``IncludeOpForFullLoad`` parameter in versions 3.1.4 and later.

        For full load, records can only be inserted. By default (the ``false`` setting), no
        information is recorded in these output files for a full load to indicate that the rows
        were inserted at the source database. If ``IncludeOpForFullLoad`` is set to ``true`` or
        ``y`` , the INSERT is recorded as an I annotation in the first field of the .csv file.
        This allows the format of your target records from a full load to be consistent with
        the target records from a CDC load.

        .. note::

          This setting works together with the ``CdcInsertsOnly`` parameter for output to .csv
          files only. For more information about how these settings work together, see
          `Indicating Source DB Operations in Migrated S3 Data
          <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring.InsertOps>`__
          in the *AWS Database Migration Service User Guide.* .

      - **CdcInsertsOnly** *(boolean) --*

        A value that enables a change data capture (CDC) load to write only INSERT operations
        to .csv or columnar storage (.parquet) output files. By default (the ``false``
        setting), the first field in a .csv or .parquet record contains the letter I (INSERT),
        U (UPDATE), or D (DELETE). These values indicate whether the row was inserted, updated,
        or deleted at the source database for a CDC load to the target.

        If ``CdcInsertsOnly`` is set to ``true`` or ``y`` , only INSERTs from the source
        database are migrated to the .csv or .parquet file. For .csv format only, how these
        INSERTs are recorded depends on the value of ``IncludeOpForFullLoad`` . If
        ``IncludeOpForFullLoad`` is set to ``true`` , the first field of every CDC record is
        set to I to indicate the INSERT operation at the source. If ``IncludeOpForFullLoad`` is
        set to ``false`` , every CDC record is written without a first field to indicate the
        INSERT operation at the source. For more information about how these settings work
        together, see `Indicating Source DB Operations in Migrated S3 Data
        <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring.InsertOps>`__
        in the *AWS Database Migration Service User Guide.* .

        .. note::

          AWS DMS supports this interaction between the ``CdcInsertsOnly`` and
          ``IncludeOpForFullLoad`` parameters in versions 3.1.4 and later.

      - **TimestampColumnName** *(string) --*

        A value that when nonblank causes AWS DMS to add a column with timestamp information to
        the endpoint data for an Amazon S3 target.

        .. note::

          AWS DMS supports the ``TimestampColumnName`` parameter in versions 3.1.4 and later.

        DMS includes an additional ``STRING`` column in the .csv or .parquet object files of
        your migrated data when you set ``TimestampColumnName`` to a nonblank value.

        For a full load, each row of this timestamp column contains a timestamp for when the
        data was transferred from the source to the target by DMS.

        For a change data capture (CDC) load, each row of the timestamp column contains the
        timestamp for the commit of that row in the source database.

        The string format for this timestamp column value is ``yyyy-MM-dd HH:mm:ss.SSSSSS`` .
        By default, the precision of this value is in microseconds. For a CDC load, the
        rounding of the precision depends on the commit timestamp supported by DMS for the
        source database.

        When the ``AddColumnName`` parameter is set to ``true`` , DMS also includes a name for
        the timestamp column that you set with ``TimestampColumnName`` .

      - **ParquetTimestampInMillisecond** *(boolean) --*

        A value that specifies the precision of any ``TIMESTAMP`` column values that are
        written to an Amazon S3 object file in .parquet format.

        .. note::

          AWS DMS supports the ``ParquetTimestampInMillisecond`` parameter in versions 3.1.4
          and later.

        When ``ParquetTimestampInMillisecond`` is set to ``true`` or ``y`` , AWS DMS writes all
        ``TIMESTAMP`` columns in a .parquet formatted file with millisecond precision.
        Otherwise, DMS writes them with microsecond precision.

        Currently, Amazon Athena and AWS Glue can handle only millisecond precision for
        ``TIMESTAMP`` values. Set this parameter to ``true`` for S3 endpoint object files that
        are .parquet formatted only if you plan to query or process the data with Athena or AWS
        Glue.

        .. note::

          AWS DMS writes any ``TIMESTAMP`` column values written to an S3 file in .csv format
          with microsecond precision.

          Setting ``ParquetTimestampInMillisecond`` has no effect on the string format of the
          timestamp column value that is inserted by setting the ``TimestampColumnName``
          parameter.

    - **DmsTransferSettings** *(dict) --*

      The settings in JSON format for the DMS transfer type of source endpoint.

      Possible settings include the following:

      * ``ServiceAccessRoleArn`` - The IAM role that has permission to access the Amazon S3
      bucket.

      * ``BucketName`` - The name of the S3 bucket to use.

      * ``CompressionType`` - An optional parameter to use GZIP to compress the target files.
      To use GZIP, set this value to ``NONE`` (the default). To keep the files uncompressed,
      don't use this value.

      Shorthand syntax for these settings is as follows:
      ``ServiceAccessRoleArn=string,BucketName=string,CompressionType=string``

      JSON syntax for these settings is as follows: ``{ "ServiceAccessRoleArn": "string",
      "BucketName": "string", "CompressionType": "none"|"gzip" }``

      - **ServiceAccessRoleArn** *(string) --*

        The IAM role that has permission to access the Amazon S3 bucket.

      - **BucketName** *(string) --*

        The name of the S3 bucket to use.

    - **MongoDbSettings** *(dict) --*

      The settings for the MongoDB source endpoint. For more information, see the
      ``MongoDbSettings`` structure.

      - **Username** *(string) --*

        The user name you use to access the MongoDB source endpoint.

      - **Password** *(string) --*

        The password for the user account you use to access the MongoDB source endpoint.

      - **ServerName** *(string) --*

        The name of the server on the MongoDB source endpoint.

      - **Port** *(integer) --*

        The port value for the MongoDB source endpoint.

      - **DatabaseName** *(string) --*

        The database name on the MongoDB source endpoint.

      - **AuthType** *(string) --*

        The authentication type you use to access the MongoDB source endpoint.

        Valid values: NO, PASSWORD

        When NO is selected, user name and password parameters are not used and can be empty.

      - **AuthMechanism** *(string) --*

        The authentication mechanism you use to access the MongoDB source endpoint.

        Valid values: DEFAULT, MONGODB_CR, SCRAM_SHA_1

        DEFAULT – For MongoDB version 2.x, use MONGODB_CR. For MongoDB version 3.x, use
        SCRAM_SHA_1. This setting is not used when authType=No.

      - **NestingLevel** *(string) --*

        Specifies either document or table mode.

        Valid values: NONE, ONE

        Default value is NONE. Specify NONE to use document mode. Specify ONE to use table mode.

      - **ExtractDocId** *(string) --*

        Specifies the document ID. Use this setting when ``NestingLevel`` is set to NONE.

        Default value is false.

      - **DocsToInvestigate** *(string) --*

        Indicates the number of documents to preview to determine the document organization.
        Use this setting when ``NestingLevel`` is set to ONE.

        Must be a positive value greater than 0. Default value is 1000.

      - **AuthSource** *(string) --*

        The MongoDB database name. This setting is not used when ``authType=NO`` .

        The default is admin.

      - **KmsKeyId** *(string) --*

        The AWS KMS key identifier that is used to encrypt the content on the replication
        instance. If you don't specify a value for the ``KmsKeyId`` parameter, then AWS DMS
        uses your default encryption key. AWS KMS creates the default encryption key for your
        AWS account. Your AWS account has a different default encryption key for each AWS
        Region.

    - **KinesisSettings** *(dict) --*

      The settings for the Amazon Kinesis source endpoint. For more information, see the
      ``KinesisSettings`` structure.

      - **StreamArn** *(string) --*

        The Amazon Resource Name (ARN) for the Amazon Kinesis Data Streams endpoint.

      - **MessageFormat** *(string) --*

        The output format for the records created on the endpoint. The message format is
        ``JSON`` .

      - **ServiceAccessRoleArn** *(string) --*

        The Amazon Resource Name (ARN) for the IAM role that DMS uses to write to the Amazon
        Kinesis data stream.

    - **ElasticsearchSettings** *(dict) --*

      The settings for the Elasticsearch source endpoint. For more information, see the
      ``ElasticsearchSettings`` structure.

      - **ServiceAccessRoleArn** *(string) --*

        The Amazon Resource Name (ARN) used by service to access the IAM role.

      - **EndpointUri** *(string) --*

        The endpoint for the Elasticsearch cluster.

      - **FullLoadErrorPercentage** *(integer) --*

        The maximum percentage of records that can fail to be written before a full load
        operation stops.

      - **ErrorRetryDuration** *(integer) --*

        The maximum number of seconds that DMS retries failed API requests to the Elasticsearch
        cluster.

    - **RedshiftSettings** *(dict) --*

      Settings for the Amazon Redshift endpoint.

      - **AcceptAnyDate** *(boolean) --*

        A value that indicates to allow any date format, including invalid formats such as
        00/00/00 00:00:00, to be loaded without generating an error. You can choose ``true`` or
        ``false`` (the default).

        This parameter applies only to TIMESTAMP and DATE columns. Always use ACCEPTANYDATE
        with the DATEFORMAT parameter. If the date format for the data doesn't match the
        DATEFORMAT specification, Amazon Redshift inserts a NULL value into that field.

      - **AfterConnectScript** *(string) --*

        Code to run after connecting. This parameter should contain the code itself, not the
        name of a file containing the code.

      - **BucketFolder** *(string) --*

        The location where the comma-separated value (.csv) files are stored before being
        uploaded to the S3 bucket.

      - **BucketName** *(string) --*

        The name of the S3 bucket you want to use

      - **ConnectionTimeout** *(integer) --*

        A value that sets the amount of time to wait (in milliseconds) before timing out,
        beginning from when you initially establish a connection.

      - **DatabaseName** *(string) --*

        The name of the Amazon Redshift data warehouse (service) that you are working with.

      - **DateFormat** *(string) --*

        The date format that you are using. Valid values are ``auto`` (case-sensitive), your
        date format string enclosed in quotes, or NULL. If this parameter is left unset (NULL),
        it defaults to a format of 'YYYY-MM-DD'. Using ``auto`` recognizes most strings, even
        some that aren't supported when you use a date format string.

        If your date and time values use formats different from each other, set this to
        ``auto`` .

      - **EmptyAsNull** *(boolean) --*

        A value that specifies whether AWS DMS should migrate empty CHAR and VARCHAR fields as
        NULL. A value of ``true`` sets empty CHAR and VARCHAR fields to null. The default is
        ``false`` .

      - **EncryptionMode** *(string) --*

        The type of server-side encryption that you want to use for your data. This encryption
        type is part of the endpoint settings or the extra connections attributes for Amazon
        S3. You can choose either ``SSE_S3`` (the default) or ``SSE_KMS`` . To use ``SSE_S3`` ,
        create an AWS Identity and Access Management (IAM) role with a policy that allows
        ``"arn:aws:s3:::*"`` to use the following actions: ``"s3:PutObject", "s3:ListBucket"``

      - **FileTransferUploadStreams** *(integer) --*

        The number of threads used to upload a single file. This parameter accepts a value from
        1 through 64. It defaults to 10.

      - **LoadTimeout** *(integer) --*

        The amount of time to wait (in milliseconds) before timing out, beginning from when you
        begin loading.

      - **MaxFileSize** *(integer) --*

        The maximum size (in KB) of any .csv file used to transfer data to Amazon Redshift.
        This accepts a value from 1 through 1,048,576. It defaults to 32,768 KB (32 MB).

      - **Password** *(string) --*

        The password for the user named in the ``username`` property.

      - **Port** *(integer) --*

        The port number for Amazon Redshift. The default value is 5439.

      - **RemoveQuotes** *(boolean) --*

        A value that specifies to remove surrounding quotation marks from strings in the
        incoming data. All characters within the quotation marks, including delimiters, are
        retained. Choose ``true`` to remove quotation marks. The default is ``false`` .

      - **ReplaceInvalidChars** *(string) --*

        A list of characters that you want to replace. Use with ``ReplaceChars`` .

      - **ReplaceChars** *(string) --*

        A value that specifies to replaces the invalid characters specified in
        ``ReplaceInvalidChars`` , substituting the specified characters instead. The default is
        ``"?"`` .

      - **ServerName** *(string) --*

        The name of the Amazon Redshift cluster you are using.

      - **ServiceAccessRoleArn** *(string) --*

        The Amazon Resource Name (ARN) of the IAM role that has access to the Amazon Redshift
        service.

      - **ServerSideEncryptionKmsKeyId** *(string) --*

        The AWS KMS key ID. If you are using ``SSE_KMS`` for the ``EncryptionMode`` , provide
        this key ID. The key that you use needs an attached policy that enables IAM user
        permissions and allows use of the key.

      - **TimeFormat** *(string) --*

        The time format that you want to use. Valid values are ``auto`` (case-sensitive),
        ``'timeformat_string'`` , ``'epochsecs'`` , or ``'epochmillisecs'`` . It defaults to
        10. Using ``auto`` recognizes most strings, even some that aren't supported when you
        use a time format string.

        If your date and time values use formats different from each other, set this parameter
        to ``auto`` .

      - **TrimBlanks** *(boolean) --*

        A value that specifies to remove the trailing white space characters from a VARCHAR
        string. This parameter applies only to columns with a VARCHAR data type. Choose
        ``true`` to remove unneeded white space. The default is ``false`` .

      - **TruncateColumns** *(boolean) --*

        A value that specifies to truncate data in columns to the appropriate number of
        characters, so that the data fits in the column. This parameter applies only to columns
        with a VARCHAR or CHAR data type, and rows with a size of 4 MB or less. Choose ``true``
        to truncate data. The default is ``false`` .

      - **Username** *(string) --*

        An Amazon Redshift user name for a registered user.

      - **WriteBufferSize** *(integer) --*

        The size of the write buffer to use in rows. Valid values range from 1 through 2,048.
        The default is 1,024. Use this setting to tune performance.
    """


_DescribeEndpointsPaginateResponseTypeDef = TypedDict(
    "_DescribeEndpointsPaginateResponseTypeDef",
    {
        "Endpoints": List[DescribeEndpointsPaginateResponseEndpointsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class DescribeEndpointsPaginateResponseTypeDef(
    _DescribeEndpointsPaginateResponseTypeDef
):
    """
    Type definition for `DescribeEndpointsPaginate` `Response`

    - **Endpoints** *(list) --*

      Endpoint description.

      - *(dict) --*

        - **EndpointIdentifier** *(string) --*

          The database endpoint identifier. Identifiers must begin with a letter; must contain only
          ASCII letters, digits, and hyphens; and must not end with a hyphen or contain two
          consecutive hyphens.

        - **EndpointType** *(string) --*

          The type of endpoint. Valid values are ``source`` and ``target`` .

        - **EngineName** *(string) --*

          The database engine name. Valid values, depending on the EndpointType, include mysql,
          oracle, postgres, mariadb, aurora, aurora-postgresql, redshift, s3, db2, azuredb, sybase,
          dynamodb, mongodb, and sqlserver.

        - **EngineDisplayName** *(string) --*

          The expanded name for the engine name. For example, if the ``EngineName`` parameter is
          "aurora," this value would be "Amazon Aurora MySQL."

        - **Username** *(string) --*

          The user name used to connect to the endpoint.

        - **ServerName** *(string) --*

          The name of the server at the endpoint.

        - **Port** *(integer) --*

          The port value used to access the endpoint.

        - **DatabaseName** *(string) --*

          The name of the database at the endpoint.

        - **ExtraConnectionAttributes** *(string) --*

          Additional connection attributes used to connect to the endpoint.

        - **Status** *(string) --*

          The status of the endpoint.

        - **KmsKeyId** *(string) --*

          An AWS KMS key identifier that is used to encrypt the connection parameters for the
          endpoint.

          If you don't specify a value for the ``KmsKeyId`` parameter, then AWS DMS uses your
          default encryption key.

          AWS KMS creates the default encryption key for your AWS account. Your AWS account has a
          different default encryption key for each AWS Region.

        - **EndpointArn** *(string) --*

          The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

        - **CertificateArn** *(string) --*

          The Amazon Resource Name (ARN) used for SSL connection to the endpoint.

        - **SslMode** *(string) --*

          The SSL mode used to connect to the endpoint. The default value is ``none`` .

        - **ServiceAccessRoleArn** *(string) --*

          The Amazon Resource Name (ARN) used by the service access IAM role.

        - **ExternalTableDefinition** *(string) --*

          The external table definition.

        - **ExternalId** *(string) --*

          Value returned by a call to CreateEndpoint that can be used for cross-account validation.
          Use it on a subsequent call to CreateEndpoint to create the endpoint with a cross-account.

        - **DynamoDbSettings** *(dict) --*

          The settings for the target DynamoDB database. For more information, see the
          ``DynamoDBSettings`` structure.

          - **ServiceAccessRoleArn** *(string) --*

            The Amazon Resource Name (ARN) used by the service access IAM role.

        - **S3Settings** *(dict) --*

          The settings for the S3 target endpoint. For more information, see the ``S3Settings``
          structure.

          - **ServiceAccessRoleArn** *(string) --*

            The Amazon Resource Name (ARN) used by the service access IAM role.

          - **ExternalTableDefinition** *(string) --*

            The external table definition.

          - **CsvRowDelimiter** *(string) --*

            The delimiter used to separate rows in the source files. The default is a carriage
            return (``\\n`` ).

          - **CsvDelimiter** *(string) --*

            The delimiter used to separate columns in the source files. The default is a comma.

          - **BucketFolder** *(string) --*

            An optional parameter to set a folder name in the S3 bucket. If provided, tables are
            created in the path `` *bucketFolder* /*schema_name* /*table_name* /`` . If this
            parameter is not specified, then the path used is `` *schema_name* /*table_name* /`` .

          - **BucketName** *(string) --*

            The name of the S3 bucket.

          - **CompressionType** *(string) --*

            An optional parameter to use GZIP to compress the target files. Set to GZIP to compress
            the target files. Set to NONE (the default) or do not use to leave the files
            uncompressed. Applies to both .csv and .parquet file formats.

          - **EncryptionMode** *(string) --*

            The type of server-side encryption that you want to use for your data. This encryption
            type is part of the endpoint settings or the extra connections attributes for Amazon
            S3. You can choose either ``SSE_S3`` (the default) or ``SSE_KMS`` . To use ``SSE_S3`` ,
            you need an AWS Identity and Access Management (IAM) role with permission to allow
            ``"arn:aws:s3:::dms-*"`` to use the following actions:

            * ``s3:CreateBucket``

            * ``s3:ListBucket``

            * ``s3:DeleteBucket``

            * ``s3:GetBucketLocation``

            * ``s3:GetObject``

            * ``s3:PutObject``

            * ``s3:DeleteObject``

            * ``s3:GetObjectVersion``

            * ``s3:GetBucketPolicy``

            * ``s3:PutBucketPolicy``

            * ``s3:DeleteBucketPolicy``

          - **ServerSideEncryptionKmsKeyId** *(string) --*

            If you are using ``SSE_KMS`` for the ``EncryptionMode`` , provide the AWS KMS key ID.
            The key that you use needs an attached policy that enables AWS Identity and Access
            Management (IAM) user permissions and allows use of the key.

            Here is a CLI example: ``aws dms create-endpoint --endpoint-identifier *value*
            --endpoint-type target --engine-name s3 --s3-settings ServiceAccessRoleArn=*value*
            ,BucketFolder=*value* ,BucketName=*value*
            ,EncryptionMode=SSE_KMS,ServerSideEncryptionKmsKeyId=*value* ``

          - **DataFormat** *(string) --*

            The format of the data that you want to use for output. You can choose one of the
            following:

            * ``csv`` : This is a row-based file format with comma-separated values (.csv).

            * ``parquet`` : Apache Parquet (.parquet) is a columnar storage file format that
            features efficient compression and provides faster query response.

          - **EncodingType** *(string) --*

            The type of encoding you are using:

            * ``RLE_DICTIONARY`` uses a combination of bit-packing and run-length encoding to store
            repeated values more efficiently. This is the default.

            * ``PLAIN`` doesn't use encoding at all. Values are stored as they are.

            * ``PLAIN_DICTIONARY`` builds a dictionary of the values encountered in a given column.
            The dictionary is stored in a dictionary page for each column chunk.

          - **DictPageSizeLimit** *(integer) --*

            The maximum size of an encoded dictionary page of a column. If the dictionary page
            exceeds this, this column is stored using an encoding type of ``PLAIN`` . This
            parameter defaults to 1024 * 1024 bytes (1 MiB), the maximum size of a dictionary page
            before it reverts to ``PLAIN`` encoding. This size is used for .parquet file format
            only.

          - **RowGroupLength** *(integer) --*

            The number of rows in a row group. A smaller row group size provides faster reads. But
            as the number of row groups grows, the slower writes become. This parameter defaults to
            10,000 rows. This number is used for .parquet file format only.

            If you choose a value larger than the maximum, ``RowGroupLength`` is set to the max row
            group length in bytes (64 * 1024 * 1024).

          - **DataPageSize** *(integer) --*

            The size of one data page in bytes. This parameter defaults to 1024 * 1024 bytes (1
            MiB). This number is used for .parquet file format only.

          - **ParquetVersion** *(string) --*

            The version of the Apache Parquet format that you want to use: ``parquet_1_0`` (the
            default) or ``parquet_2_0`` .

          - **EnableStatistics** *(boolean) --*

            A value that enables statistics for Parquet pages and row groups. Choose ``true`` to
            enable statistics, ``false`` to disable. Statistics include ``NULL`` , ``DISTINCT`` ,
            ``MAX`` , and ``MIN`` values. This parameter defaults to ``true`` . This value is used
            for .parquet file format only.

          - **IncludeOpForFullLoad** *(boolean) --*

            A value that enables a full load to write INSERT operations to the comma-separated
            value (.csv) output files only to indicate how the rows were added to the source
            database.

            .. note::

              AWS DMS supports the ``IncludeOpForFullLoad`` parameter in versions 3.1.4 and later.

            For full load, records can only be inserted. By default (the ``false`` setting), no
            information is recorded in these output files for a full load to indicate that the rows
            were inserted at the source database. If ``IncludeOpForFullLoad`` is set to ``true`` or
            ``y`` , the INSERT is recorded as an I annotation in the first field of the .csv file.
            This allows the format of your target records from a full load to be consistent with
            the target records from a CDC load.

            .. note::

              This setting works together with the ``CdcInsertsOnly`` parameter for output to .csv
              files only. For more information about how these settings work together, see
              `Indicating Source DB Operations in Migrated S3 Data
              <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring.InsertOps>`__
              in the *AWS Database Migration Service User Guide.* .

          - **CdcInsertsOnly** *(boolean) --*

            A value that enables a change data capture (CDC) load to write only INSERT operations
            to .csv or columnar storage (.parquet) output files. By default (the ``false``
            setting), the first field in a .csv or .parquet record contains the letter I (INSERT),
            U (UPDATE), or D (DELETE). These values indicate whether the row was inserted, updated,
            or deleted at the source database for a CDC load to the target.

            If ``CdcInsertsOnly`` is set to ``true`` or ``y`` , only INSERTs from the source
            database are migrated to the .csv or .parquet file. For .csv format only, how these
            INSERTs are recorded depends on the value of ``IncludeOpForFullLoad`` . If
            ``IncludeOpForFullLoad`` is set to ``true`` , the first field of every CDC record is
            set to I to indicate the INSERT operation at the source. If ``IncludeOpForFullLoad`` is
            set to ``false`` , every CDC record is written without a first field to indicate the
            INSERT operation at the source. For more information about how these settings work
            together, see `Indicating Source DB Operations in Migrated S3 Data
            <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring.InsertOps>`__
            in the *AWS Database Migration Service User Guide.* .

            .. note::

              AWS DMS supports this interaction between the ``CdcInsertsOnly`` and
              ``IncludeOpForFullLoad`` parameters in versions 3.1.4 and later.

          - **TimestampColumnName** *(string) --*

            A value that when nonblank causes AWS DMS to add a column with timestamp information to
            the endpoint data for an Amazon S3 target.

            .. note::

              AWS DMS supports the ``TimestampColumnName`` parameter in versions 3.1.4 and later.

            DMS includes an additional ``STRING`` column in the .csv or .parquet object files of
            your migrated data when you set ``TimestampColumnName`` to a nonblank value.

            For a full load, each row of this timestamp column contains a timestamp for when the
            data was transferred from the source to the target by DMS.

            For a change data capture (CDC) load, each row of the timestamp column contains the
            timestamp for the commit of that row in the source database.

            The string format for this timestamp column value is ``yyyy-MM-dd HH:mm:ss.SSSSSS`` .
            By default, the precision of this value is in microseconds. For a CDC load, the
            rounding of the precision depends on the commit timestamp supported by DMS for the
            source database.

            When the ``AddColumnName`` parameter is set to ``true`` , DMS also includes a name for
            the timestamp column that you set with ``TimestampColumnName`` .

          - **ParquetTimestampInMillisecond** *(boolean) --*

            A value that specifies the precision of any ``TIMESTAMP`` column values that are
            written to an Amazon S3 object file in .parquet format.

            .. note::

              AWS DMS supports the ``ParquetTimestampInMillisecond`` parameter in versions 3.1.4
              and later.

            When ``ParquetTimestampInMillisecond`` is set to ``true`` or ``y`` , AWS DMS writes all
            ``TIMESTAMP`` columns in a .parquet formatted file with millisecond precision.
            Otherwise, DMS writes them with microsecond precision.

            Currently, Amazon Athena and AWS Glue can handle only millisecond precision for
            ``TIMESTAMP`` values. Set this parameter to ``true`` for S3 endpoint object files that
            are .parquet formatted only if you plan to query or process the data with Athena or AWS
            Glue.

            .. note::

              AWS DMS writes any ``TIMESTAMP`` column values written to an S3 file in .csv format
              with microsecond precision.

              Setting ``ParquetTimestampInMillisecond`` has no effect on the string format of the
              timestamp column value that is inserted by setting the ``TimestampColumnName``
              parameter.

        - **DmsTransferSettings** *(dict) --*

          The settings in JSON format for the DMS transfer type of source endpoint.

          Possible settings include the following:

          * ``ServiceAccessRoleArn`` - The IAM role that has permission to access the Amazon S3
          bucket.

          * ``BucketName`` - The name of the S3 bucket to use.

          * ``CompressionType`` - An optional parameter to use GZIP to compress the target files.
          To use GZIP, set this value to ``NONE`` (the default). To keep the files uncompressed,
          don't use this value.

          Shorthand syntax for these settings is as follows:
          ``ServiceAccessRoleArn=string,BucketName=string,CompressionType=string``

          JSON syntax for these settings is as follows: ``{ "ServiceAccessRoleArn": "string",
          "BucketName": "string", "CompressionType": "none"|"gzip" }``

          - **ServiceAccessRoleArn** *(string) --*

            The IAM role that has permission to access the Amazon S3 bucket.

          - **BucketName** *(string) --*

            The name of the S3 bucket to use.

        - **MongoDbSettings** *(dict) --*

          The settings for the MongoDB source endpoint. For more information, see the
          ``MongoDbSettings`` structure.

          - **Username** *(string) --*

            The user name you use to access the MongoDB source endpoint.

          - **Password** *(string) --*

            The password for the user account you use to access the MongoDB source endpoint.

          - **ServerName** *(string) --*

            The name of the server on the MongoDB source endpoint.

          - **Port** *(integer) --*

            The port value for the MongoDB source endpoint.

          - **DatabaseName** *(string) --*

            The database name on the MongoDB source endpoint.

          - **AuthType** *(string) --*

            The authentication type you use to access the MongoDB source endpoint.

            Valid values: NO, PASSWORD

            When NO is selected, user name and password parameters are not used and can be empty.

          - **AuthMechanism** *(string) --*

            The authentication mechanism you use to access the MongoDB source endpoint.

            Valid values: DEFAULT, MONGODB_CR, SCRAM_SHA_1

            DEFAULT – For MongoDB version 2.x, use MONGODB_CR. For MongoDB version 3.x, use
            SCRAM_SHA_1. This setting is not used when authType=No.

          - **NestingLevel** *(string) --*

            Specifies either document or table mode.

            Valid values: NONE, ONE

            Default value is NONE. Specify NONE to use document mode. Specify ONE to use table mode.

          - **ExtractDocId** *(string) --*

            Specifies the document ID. Use this setting when ``NestingLevel`` is set to NONE.

            Default value is false.

          - **DocsToInvestigate** *(string) --*

            Indicates the number of documents to preview to determine the document organization.
            Use this setting when ``NestingLevel`` is set to ONE.

            Must be a positive value greater than 0. Default value is 1000.

          - **AuthSource** *(string) --*

            The MongoDB database name. This setting is not used when ``authType=NO`` .

            The default is admin.

          - **KmsKeyId** *(string) --*

            The AWS KMS key identifier that is used to encrypt the content on the replication
            instance. If you don't specify a value for the ``KmsKeyId`` parameter, then AWS DMS
            uses your default encryption key. AWS KMS creates the default encryption key for your
            AWS account. Your AWS account has a different default encryption key for each AWS
            Region.

        - **KinesisSettings** *(dict) --*

          The settings for the Amazon Kinesis source endpoint. For more information, see the
          ``KinesisSettings`` structure.

          - **StreamArn** *(string) --*

            The Amazon Resource Name (ARN) for the Amazon Kinesis Data Streams endpoint.

          - **MessageFormat** *(string) --*

            The output format for the records created on the endpoint. The message format is
            ``JSON`` .

          - **ServiceAccessRoleArn** *(string) --*

            The Amazon Resource Name (ARN) for the IAM role that DMS uses to write to the Amazon
            Kinesis data stream.

        - **ElasticsearchSettings** *(dict) --*

          The settings for the Elasticsearch source endpoint. For more information, see the
          ``ElasticsearchSettings`` structure.

          - **ServiceAccessRoleArn** *(string) --*

            The Amazon Resource Name (ARN) used by service to access the IAM role.

          - **EndpointUri** *(string) --*

            The endpoint for the Elasticsearch cluster.

          - **FullLoadErrorPercentage** *(integer) --*

            The maximum percentage of records that can fail to be written before a full load
            operation stops.

          - **ErrorRetryDuration** *(integer) --*

            The maximum number of seconds that DMS retries failed API requests to the Elasticsearch
            cluster.

        - **RedshiftSettings** *(dict) --*

          Settings for the Amazon Redshift endpoint.

          - **AcceptAnyDate** *(boolean) --*

            A value that indicates to allow any date format, including invalid formats such as
            00/00/00 00:00:00, to be loaded without generating an error. You can choose ``true`` or
            ``false`` (the default).

            This parameter applies only to TIMESTAMP and DATE columns. Always use ACCEPTANYDATE
            with the DATEFORMAT parameter. If the date format for the data doesn't match the
            DATEFORMAT specification, Amazon Redshift inserts a NULL value into that field.

          - **AfterConnectScript** *(string) --*

            Code to run after connecting. This parameter should contain the code itself, not the
            name of a file containing the code.

          - **BucketFolder** *(string) --*

            The location where the comma-separated value (.csv) files are stored before being
            uploaded to the S3 bucket.

          - **BucketName** *(string) --*

            The name of the S3 bucket you want to use

          - **ConnectionTimeout** *(integer) --*

            A value that sets the amount of time to wait (in milliseconds) before timing out,
            beginning from when you initially establish a connection.

          - **DatabaseName** *(string) --*

            The name of the Amazon Redshift data warehouse (service) that you are working with.

          - **DateFormat** *(string) --*

            The date format that you are using. Valid values are ``auto`` (case-sensitive), your
            date format string enclosed in quotes, or NULL. If this parameter is left unset (NULL),
            it defaults to a format of 'YYYY-MM-DD'. Using ``auto`` recognizes most strings, even
            some that aren't supported when you use a date format string.

            If your date and time values use formats different from each other, set this to
            ``auto`` .

          - **EmptyAsNull** *(boolean) --*

            A value that specifies whether AWS DMS should migrate empty CHAR and VARCHAR fields as
            NULL. A value of ``true`` sets empty CHAR and VARCHAR fields to null. The default is
            ``false`` .

          - **EncryptionMode** *(string) --*

            The type of server-side encryption that you want to use for your data. This encryption
            type is part of the endpoint settings or the extra connections attributes for Amazon
            S3. You can choose either ``SSE_S3`` (the default) or ``SSE_KMS`` . To use ``SSE_S3`` ,
            create an AWS Identity and Access Management (IAM) role with a policy that allows
            ``"arn:aws:s3:::*"`` to use the following actions: ``"s3:PutObject", "s3:ListBucket"``

          - **FileTransferUploadStreams** *(integer) --*

            The number of threads used to upload a single file. This parameter accepts a value from
            1 through 64. It defaults to 10.

          - **LoadTimeout** *(integer) --*

            The amount of time to wait (in milliseconds) before timing out, beginning from when you
            begin loading.

          - **MaxFileSize** *(integer) --*

            The maximum size (in KB) of any .csv file used to transfer data to Amazon Redshift.
            This accepts a value from 1 through 1,048,576. It defaults to 32,768 KB (32 MB).

          - **Password** *(string) --*

            The password for the user named in the ``username`` property.

          - **Port** *(integer) --*

            The port number for Amazon Redshift. The default value is 5439.

          - **RemoveQuotes** *(boolean) --*

            A value that specifies to remove surrounding quotation marks from strings in the
            incoming data. All characters within the quotation marks, including delimiters, are
            retained. Choose ``true`` to remove quotation marks. The default is ``false`` .

          - **ReplaceInvalidChars** *(string) --*

            A list of characters that you want to replace. Use with ``ReplaceChars`` .

          - **ReplaceChars** *(string) --*

            A value that specifies to replaces the invalid characters specified in
            ``ReplaceInvalidChars`` , substituting the specified characters instead. The default is
            ``"?"`` .

          - **ServerName** *(string) --*

            The name of the Amazon Redshift cluster you are using.

          - **ServiceAccessRoleArn** *(string) --*

            The Amazon Resource Name (ARN) of the IAM role that has access to the Amazon Redshift
            service.

          - **ServerSideEncryptionKmsKeyId** *(string) --*

            The AWS KMS key ID. If you are using ``SSE_KMS`` for the ``EncryptionMode`` , provide
            this key ID. The key that you use needs an attached policy that enables IAM user
            permissions and allows use of the key.

          - **TimeFormat** *(string) --*

            The time format that you want to use. Valid values are ``auto`` (case-sensitive),
            ``'timeformat_string'`` , ``'epochsecs'`` , or ``'epochmillisecs'`` . It defaults to
            10. Using ``auto`` recognizes most strings, even some that aren't supported when you
            use a time format string.

            If your date and time values use formats different from each other, set this parameter
            to ``auto`` .

          - **TrimBlanks** *(boolean) --*

            A value that specifies to remove the trailing white space characters from a VARCHAR
            string. This parameter applies only to columns with a VARCHAR data type. Choose
            ``true`` to remove unneeded white space. The default is ``false`` .

          - **TruncateColumns** *(boolean) --*

            A value that specifies to truncate data in columns to the appropriate number of
            characters, so that the data fits in the column. This parameter applies only to columns
            with a VARCHAR or CHAR data type, and rows with a size of 4 MB or less. Choose ``true``
            to truncate data. The default is ``false`` .

          - **Username** *(string) --*

            An Amazon Redshift user name for a registered user.

          - **WriteBufferSize** *(integer) --*

            The size of the write buffer to use in rows. Valid values range from 1 through 2,048.
            The default is 1,024. Use this setting to tune performance.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribeEventSubscriptionsPaginateFiltersTypeDef = TypedDict(
    "_DescribeEventSubscriptionsPaginateFiltersTypeDef",
    {"Name": str, "Values": List[str]},
)


class DescribeEventSubscriptionsPaginateFiltersTypeDef(
    _DescribeEventSubscriptionsPaginateFiltersTypeDef
):
    """
    Type definition for `DescribeEventSubscriptionsPaginate` `Filters`

    - **Name** *(string) --* **[REQUIRED]**

      The name of the filter.

    - **Values** *(list) --* **[REQUIRED]**

      The filter value.

      - *(string) --*
    """


_DescribeEventSubscriptionsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeEventSubscriptionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeEventSubscriptionsPaginatePaginationConfigTypeDef(
    _DescribeEventSubscriptionsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeEventSubscriptionsPaginate` `PaginationConfig`

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


_DescribeEventSubscriptionsPaginateResponseEventSubscriptionsListTypeDef = TypedDict(
    "_DescribeEventSubscriptionsPaginateResponseEventSubscriptionsListTypeDef",
    {
        "CustomerAwsId": str,
        "CustSubscriptionId": str,
        "SnsTopicArn": str,
        "Status": str,
        "SubscriptionCreationTime": str,
        "SourceType": str,
        "SourceIdsList": List[str],
        "EventCategoriesList": List[str],
        "Enabled": bool,
    },
    total=False,
)


class DescribeEventSubscriptionsPaginateResponseEventSubscriptionsListTypeDef(
    _DescribeEventSubscriptionsPaginateResponseEventSubscriptionsListTypeDef
):
    """
    Type definition for `DescribeEventSubscriptionsPaginateResponse` `EventSubscriptionsList`

    - **CustomerAwsId** *(string) --*

      The AWS customer account associated with the AWS DMS event notification subscription.

    - **CustSubscriptionId** *(string) --*

      The AWS DMS event notification subscription Id.

    - **SnsTopicArn** *(string) --*

      The topic ARN of the AWS DMS event notification subscription.

    - **Status** *(string) --*

      The status of the AWS DMS event notification subscription.

      Constraints:

      Can be one of the following: creating | modifying | deleting | active | no-permission |
      topic-not-exist

      The status "no-permission" indicates that AWS DMS no longer has permission to post to the
      SNS topic. The status "topic-not-exist" indicates that the topic was deleted after the
      subscription was created.

    - **SubscriptionCreationTime** *(string) --*

      The time the RDS event notification subscription was created.

    - **SourceType** *(string) --*

      The type of AWS DMS resource that generates events.

      Valid values: replication-instance | replication-server | security-group |
      replication-task

    - **SourceIdsList** *(list) --*

      A list of source Ids for the event subscription.

      - *(string) --*

    - **EventCategoriesList** *(list) --*

      A lists of event categories.

      - *(string) --*

    - **Enabled** *(boolean) --*

      Boolean value that indicates if the event subscription is enabled.
    """


_DescribeEventSubscriptionsPaginateResponseTypeDef = TypedDict(
    "_DescribeEventSubscriptionsPaginateResponseTypeDef",
    {
        "EventSubscriptionsList": List[
            DescribeEventSubscriptionsPaginateResponseEventSubscriptionsListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeEventSubscriptionsPaginateResponseTypeDef(
    _DescribeEventSubscriptionsPaginateResponseTypeDef
):
    """
    Type definition for `DescribeEventSubscriptionsPaginate` `Response`

    - **EventSubscriptionsList** *(list) --*

      A list of event subscriptions.

      - *(dict) --*

        - **CustomerAwsId** *(string) --*

          The AWS customer account associated with the AWS DMS event notification subscription.

        - **CustSubscriptionId** *(string) --*

          The AWS DMS event notification subscription Id.

        - **SnsTopicArn** *(string) --*

          The topic ARN of the AWS DMS event notification subscription.

        - **Status** *(string) --*

          The status of the AWS DMS event notification subscription.

          Constraints:

          Can be one of the following: creating | modifying | deleting | active | no-permission |
          topic-not-exist

          The status "no-permission" indicates that AWS DMS no longer has permission to post to the
          SNS topic. The status "topic-not-exist" indicates that the topic was deleted after the
          subscription was created.

        - **SubscriptionCreationTime** *(string) --*

          The time the RDS event notification subscription was created.

        - **SourceType** *(string) --*

          The type of AWS DMS resource that generates events.

          Valid values: replication-instance | replication-server | security-group |
          replication-task

        - **SourceIdsList** *(list) --*

          A list of source Ids for the event subscription.

          - *(string) --*

        - **EventCategoriesList** *(list) --*

          A lists of event categories.

          - *(string) --*

        - **Enabled** *(boolean) --*

          Boolean value that indicates if the event subscription is enabled.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribeEventsPaginateFiltersTypeDef = TypedDict(
    "_DescribeEventsPaginateFiltersTypeDef", {"Name": str, "Values": List[str]}
)


class DescribeEventsPaginateFiltersTypeDef(_DescribeEventsPaginateFiltersTypeDef):
    """
    Type definition for `DescribeEventsPaginate` `Filters`

    - **Name** *(string) --* **[REQUIRED]**

      The name of the filter.

    - **Values** *(list) --* **[REQUIRED]**

      The filter value.

      - *(string) --*
    """


_DescribeEventsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeEventsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeEventsPaginatePaginationConfigTypeDef(
    _DescribeEventsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeEventsPaginate` `PaginationConfig`

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


_DescribeEventsPaginateResponseEventsTypeDef = TypedDict(
    "_DescribeEventsPaginateResponseEventsTypeDef",
    {
        "SourceIdentifier": str,
        "SourceType": str,
        "Message": str,
        "EventCategories": List[str],
        "Date": datetime,
    },
    total=False,
)


class DescribeEventsPaginateResponseEventsTypeDef(
    _DescribeEventsPaginateResponseEventsTypeDef
):
    """
    Type definition for `DescribeEventsPaginateResponse` `Events`

    - **SourceIdentifier** *(string) --*

      The identifier of an event source.

    - **SourceType** *(string) --*

      The type of AWS DMS resource that generates events.

      Valid values: replication-instance | endpoint | replication-task

    - **Message** *(string) --*

      The event message.

    - **EventCategories** *(list) --*

      The event categories available for the specified source type.

      - *(string) --*

    - **Date** *(datetime) --*

      The date of the event.
    """


_DescribeEventsPaginateResponseTypeDef = TypedDict(
    "_DescribeEventsPaginateResponseTypeDef",
    {"Events": List[DescribeEventsPaginateResponseEventsTypeDef], "NextToken": str},
    total=False,
)


class DescribeEventsPaginateResponseTypeDef(_DescribeEventsPaginateResponseTypeDef):
    """
    Type definition for `DescribeEventsPaginate` `Response`

    - **Events** *(list) --*

      The events described.

      - *(dict) --*

        - **SourceIdentifier** *(string) --*

          The identifier of an event source.

        - **SourceType** *(string) --*

          The type of AWS DMS resource that generates events.

          Valid values: replication-instance | endpoint | replication-task

        - **Message** *(string) --*

          The event message.

        - **EventCategories** *(list) --*

          The event categories available for the specified source type.

          - *(string) --*

        - **Date** *(datetime) --*

          The date of the event.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribeOrderableReplicationInstancesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeOrderableReplicationInstancesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeOrderableReplicationInstancesPaginatePaginationConfigTypeDef(
    _DescribeOrderableReplicationInstancesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeOrderableReplicationInstancesPaginate` `PaginationConfig`

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


_DescribeOrderableReplicationInstancesPaginateResponseOrderableReplicationInstancesTypeDef = TypedDict(
    "_DescribeOrderableReplicationInstancesPaginateResponseOrderableReplicationInstancesTypeDef",
    {
        "EngineVersion": str,
        "ReplicationInstanceClass": str,
        "StorageType": str,
        "MinAllocatedStorage": int,
        "MaxAllocatedStorage": int,
        "DefaultAllocatedStorage": int,
        "IncludedAllocatedStorage": int,
        "AvailabilityZones": List[str],
        "ReleaseStatus": str,
    },
    total=False,
)


class DescribeOrderableReplicationInstancesPaginateResponseOrderableReplicationInstancesTypeDef(
    _DescribeOrderableReplicationInstancesPaginateResponseOrderableReplicationInstancesTypeDef
):
    """
    Type definition for `DescribeOrderableReplicationInstancesPaginateResponse` `OrderableReplicationInstances`

    - **EngineVersion** *(string) --*

      The version of the replication engine.

    - **ReplicationInstanceClass** *(string) --*

      The compute and memory capacity of the replication instance.

      Valid Values: ``dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large | dms.c4.large
      | dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge``

    - **StorageType** *(string) --*

      The type of storage used by the replication instance.

    - **MinAllocatedStorage** *(integer) --*

      The minimum amount of storage (in gigabytes) that can be allocated for the replication
      instance.

    - **MaxAllocatedStorage** *(integer) --*

      The minimum amount of storage (in gigabytes) that can be allocated for the replication
      instance.

    - **DefaultAllocatedStorage** *(integer) --*

      The default amount of storage (in gigabytes) that is allocated for the replication
      instance.

    - **IncludedAllocatedStorage** *(integer) --*

      The amount of storage (in gigabytes) that is allocated for the replication instance.

    - **AvailabilityZones** *(list) --*

      List of Availability Zones for this replication instance.

      - *(string) --*

    - **ReleaseStatus** *(string) --*

      The value returned when the specified ``EngineVersion`` of the replication instance is in
      Beta or test mode. This indicates some features might not work as expected.

      .. note::

        AWS DMS supports the ``ReleaseStatus`` parameter in versions 3.1.4 and later.
    """


_DescribeOrderableReplicationInstancesPaginateResponseTypeDef = TypedDict(
    "_DescribeOrderableReplicationInstancesPaginateResponseTypeDef",
    {
        "OrderableReplicationInstances": List[
            DescribeOrderableReplicationInstancesPaginateResponseOrderableReplicationInstancesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeOrderableReplicationInstancesPaginateResponseTypeDef(
    _DescribeOrderableReplicationInstancesPaginateResponseTypeDef
):
    """
    Type definition for `DescribeOrderableReplicationInstancesPaginate` `Response`

    - **OrderableReplicationInstances** *(list) --*

      The order-able replication instances available.

      - *(dict) --*

        - **EngineVersion** *(string) --*

          The version of the replication engine.

        - **ReplicationInstanceClass** *(string) --*

          The compute and memory capacity of the replication instance.

          Valid Values: ``dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large | dms.c4.large
          | dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge``

        - **StorageType** *(string) --*

          The type of storage used by the replication instance.

        - **MinAllocatedStorage** *(integer) --*

          The minimum amount of storage (in gigabytes) that can be allocated for the replication
          instance.

        - **MaxAllocatedStorage** *(integer) --*

          The minimum amount of storage (in gigabytes) that can be allocated for the replication
          instance.

        - **DefaultAllocatedStorage** *(integer) --*

          The default amount of storage (in gigabytes) that is allocated for the replication
          instance.

        - **IncludedAllocatedStorage** *(integer) --*

          The amount of storage (in gigabytes) that is allocated for the replication instance.

        - **AvailabilityZones** *(list) --*

          List of Availability Zones for this replication instance.

          - *(string) --*

        - **ReleaseStatus** *(string) --*

          The value returned when the specified ``EngineVersion`` of the replication instance is in
          Beta or test mode. This indicates some features might not work as expected.

          .. note::

            AWS DMS supports the ``ReleaseStatus`` parameter in versions 3.1.4 and later.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribeReplicationInstancesPaginateFiltersTypeDef = TypedDict(
    "_DescribeReplicationInstancesPaginateFiltersTypeDef",
    {"Name": str, "Values": List[str]},
)


class DescribeReplicationInstancesPaginateFiltersTypeDef(
    _DescribeReplicationInstancesPaginateFiltersTypeDef
):
    """
    Type definition for `DescribeReplicationInstancesPaginate` `Filters`

    - **Name** *(string) --* **[REQUIRED]**

      The name of the filter.

    - **Values** *(list) --* **[REQUIRED]**

      The filter value.

      - *(string) --*
    """


_DescribeReplicationInstancesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeReplicationInstancesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeReplicationInstancesPaginatePaginationConfigTypeDef(
    _DescribeReplicationInstancesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeReplicationInstancesPaginate` `PaginationConfig`

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


_DescribeReplicationInstancesPaginateResponseReplicationInstancesPendingModifiedValuesTypeDef = TypedDict(
    "_DescribeReplicationInstancesPaginateResponseReplicationInstancesPendingModifiedValuesTypeDef",
    {
        "ReplicationInstanceClass": str,
        "AllocatedStorage": int,
        "MultiAZ": bool,
        "EngineVersion": str,
    },
    total=False,
)


class DescribeReplicationInstancesPaginateResponseReplicationInstancesPendingModifiedValuesTypeDef(
    _DescribeReplicationInstancesPaginateResponseReplicationInstancesPendingModifiedValuesTypeDef
):
    """
    Type definition for `DescribeReplicationInstancesPaginateResponseReplicationInstances` `PendingModifiedValues`

    The pending modification values.

    - **ReplicationInstanceClass** *(string) --*

      The compute and memory capacity of the replication instance.

      Valid Values: ``dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large |
      dms.c4.large | dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge``

    - **AllocatedStorage** *(integer) --*

      The amount of storage (in gigabytes) that is allocated for the replication instance.

    - **MultiAZ** *(boolean) --*

      Specifies whether the replication instance is a Multi-AZ deployment. You cannot set the
      ``AvailabilityZone`` parameter if the Multi-AZ parameter is set to ``true`` .

    - **EngineVersion** *(string) --*

      The engine version number of the replication instance.
    """


_DescribeReplicationInstancesPaginateResponseReplicationInstancesReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "_DescribeReplicationInstancesPaginateResponseReplicationInstancesReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)


class DescribeReplicationInstancesPaginateResponseReplicationInstancesReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef(
    _DescribeReplicationInstancesPaginateResponseReplicationInstancesReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef
):
    """
    Type definition for `DescribeReplicationInstancesPaginateResponseReplicationInstancesReplicationSubnetGroupSubnets` `SubnetAvailabilityZone`

    The Availability Zone of the subnet.

    - **Name** *(string) --*

      The name of the availability zone.
    """


_DescribeReplicationInstancesPaginateResponseReplicationInstancesReplicationSubnetGroupSubnetsTypeDef = TypedDict(
    "_DescribeReplicationInstancesPaginateResponseReplicationInstancesReplicationSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": DescribeReplicationInstancesPaginateResponseReplicationInstancesReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)


class DescribeReplicationInstancesPaginateResponseReplicationInstancesReplicationSubnetGroupSubnetsTypeDef(
    _DescribeReplicationInstancesPaginateResponseReplicationInstancesReplicationSubnetGroupSubnetsTypeDef
):
    """
    Type definition for `DescribeReplicationInstancesPaginateResponseReplicationInstancesReplicationSubnetGroup` `Subnets`

    - **SubnetIdentifier** *(string) --*

      The subnet identifier.

    - **SubnetAvailabilityZone** *(dict) --*

      The Availability Zone of the subnet.

      - **Name** *(string) --*

        The name of the availability zone.

    - **SubnetStatus** *(string) --*

      The status of the subnet.
    """


_DescribeReplicationInstancesPaginateResponseReplicationInstancesReplicationSubnetGroupTypeDef = TypedDict(
    "_DescribeReplicationInstancesPaginateResponseReplicationInstancesReplicationSubnetGroupTypeDef",
    {
        "ReplicationSubnetGroupIdentifier": str,
        "ReplicationSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[
            DescribeReplicationInstancesPaginateResponseReplicationInstancesReplicationSubnetGroupSubnetsTypeDef
        ],
    },
    total=False,
)


class DescribeReplicationInstancesPaginateResponseReplicationInstancesReplicationSubnetGroupTypeDef(
    _DescribeReplicationInstancesPaginateResponseReplicationInstancesReplicationSubnetGroupTypeDef
):
    """
    Type definition for `DescribeReplicationInstancesPaginateResponseReplicationInstances` `ReplicationSubnetGroup`

    The subnet group for the replication instance.

    - **ReplicationSubnetGroupIdentifier** *(string) --*

      The identifier of the replication instance subnet group.

    - **ReplicationSubnetGroupDescription** *(string) --*

      A description for the replication subnet group.

    - **VpcId** *(string) --*

      The ID of the VPC.

    - **SubnetGroupStatus** *(string) --*

      The status of the subnet group.

    - **Subnets** *(list) --*

      The subnets that are in the subnet group.

      - *(dict) --*

        - **SubnetIdentifier** *(string) --*

          The subnet identifier.

        - **SubnetAvailabilityZone** *(dict) --*

          The Availability Zone of the subnet.

          - **Name** *(string) --*

            The name of the availability zone.

        - **SubnetStatus** *(string) --*

          The status of the subnet.
    """


_DescribeReplicationInstancesPaginateResponseReplicationInstancesVpcSecurityGroupsTypeDef = TypedDict(
    "_DescribeReplicationInstancesPaginateResponseReplicationInstancesVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class DescribeReplicationInstancesPaginateResponseReplicationInstancesVpcSecurityGroupsTypeDef(
    _DescribeReplicationInstancesPaginateResponseReplicationInstancesVpcSecurityGroupsTypeDef
):
    """
    Type definition for `DescribeReplicationInstancesPaginateResponseReplicationInstances` `VpcSecurityGroups`

    - **VpcSecurityGroupId** *(string) --*

      The VPC security group Id.

    - **Status** *(string) --*

      The status of the VPC security group.
    """


_DescribeReplicationInstancesPaginateResponseReplicationInstancesTypeDef = TypedDict(
    "_DescribeReplicationInstancesPaginateResponseReplicationInstancesTypeDef",
    {
        "ReplicationInstanceIdentifier": str,
        "ReplicationInstanceClass": str,
        "ReplicationInstanceStatus": str,
        "AllocatedStorage": int,
        "InstanceCreateTime": datetime,
        "VpcSecurityGroups": List[
            DescribeReplicationInstancesPaginateResponseReplicationInstancesVpcSecurityGroupsTypeDef
        ],
        "AvailabilityZone": str,
        "ReplicationSubnetGroup": DescribeReplicationInstancesPaginateResponseReplicationInstancesReplicationSubnetGroupTypeDef,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": DescribeReplicationInstancesPaginateResponseReplicationInstancesPendingModifiedValuesTypeDef,
        "MultiAZ": bool,
        "EngineVersion": str,
        "AutoMinorVersionUpgrade": bool,
        "KmsKeyId": str,
        "ReplicationInstanceArn": str,
        "ReplicationInstancePublicIpAddress": str,
        "ReplicationInstancePrivateIpAddress": str,
        "ReplicationInstancePublicIpAddresses": List[str],
        "ReplicationInstancePrivateIpAddresses": List[str],
        "PubliclyAccessible": bool,
        "SecondaryAvailabilityZone": str,
        "FreeUntil": datetime,
        "DnsNameServers": str,
    },
    total=False,
)


class DescribeReplicationInstancesPaginateResponseReplicationInstancesTypeDef(
    _DescribeReplicationInstancesPaginateResponseReplicationInstancesTypeDef
):
    """
    Type definition for `DescribeReplicationInstancesPaginateResponse` `ReplicationInstances`

    - **ReplicationInstanceIdentifier** *(string) --*

      The replication instance identifier. This parameter is stored as a lowercase string.

      Constraints:

      * Must contain from 1 to 63 alphanumeric characters or hyphens.

      * First character must be a letter.

      * Cannot end with a hyphen or contain two consecutive hyphens.

      Example: ``myrepinstance``

    - **ReplicationInstanceClass** *(string) --*

      The compute and memory capacity of the replication instance.

      Valid Values: ``dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large | dms.c4.large
      | dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge``

    - **ReplicationInstanceStatus** *(string) --*

      The status of the replication instance.

    - **AllocatedStorage** *(integer) --*

      The amount of storage (in gigabytes) that is allocated for the replication instance.

    - **InstanceCreateTime** *(datetime) --*

      The time the replication instance was created.

    - **VpcSecurityGroups** *(list) --*

      The VPC security group for the instance.

      - *(dict) --*

        - **VpcSecurityGroupId** *(string) --*

          The VPC security group Id.

        - **Status** *(string) --*

          The status of the VPC security group.

    - **AvailabilityZone** *(string) --*

      The Availability Zone for the instance.

    - **ReplicationSubnetGroup** *(dict) --*

      The subnet group for the replication instance.

      - **ReplicationSubnetGroupIdentifier** *(string) --*

        The identifier of the replication instance subnet group.

      - **ReplicationSubnetGroupDescription** *(string) --*

        A description for the replication subnet group.

      - **VpcId** *(string) --*

        The ID of the VPC.

      - **SubnetGroupStatus** *(string) --*

        The status of the subnet group.

      - **Subnets** *(list) --*

        The subnets that are in the subnet group.

        - *(dict) --*

          - **SubnetIdentifier** *(string) --*

            The subnet identifier.

          - **SubnetAvailabilityZone** *(dict) --*

            The Availability Zone of the subnet.

            - **Name** *(string) --*

              The name of the availability zone.

          - **SubnetStatus** *(string) --*

            The status of the subnet.

    - **PreferredMaintenanceWindow** *(string) --*

      The maintenance window times for the replication instance.

    - **PendingModifiedValues** *(dict) --*

      The pending modification values.

      - **ReplicationInstanceClass** *(string) --*

        The compute and memory capacity of the replication instance.

        Valid Values: ``dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large |
        dms.c4.large | dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge``

      - **AllocatedStorage** *(integer) --*

        The amount of storage (in gigabytes) that is allocated for the replication instance.

      - **MultiAZ** *(boolean) --*

        Specifies whether the replication instance is a Multi-AZ deployment. You cannot set the
        ``AvailabilityZone`` parameter if the Multi-AZ parameter is set to ``true`` .

      - **EngineVersion** *(string) --*

        The engine version number of the replication instance.

    - **MultiAZ** *(boolean) --*

      Specifies whether the replication instance is a Multi-AZ deployment. You cannot set the
      ``AvailabilityZone`` parameter if the Multi-AZ parameter is set to ``true`` .

    - **EngineVersion** *(string) --*

      The engine version number of the replication instance.

    - **AutoMinorVersionUpgrade** *(boolean) --*

      Boolean value indicating if minor version upgrades will be automatically applied to the
      instance.

    - **KmsKeyId** *(string) --*

      An AWS KMS key identifier that is used to encrypt the data on the replication instance.

      If you don't specify a value for the ``KmsKeyId`` parameter, then AWS DMS uses your
      default encryption key.

      AWS KMS creates the default encryption key for your AWS account. Your AWS account has a
      different default encryption key for each AWS Region.

    - **ReplicationInstanceArn** *(string) --*

      The Amazon Resource Name (ARN) of the replication instance.

    - **ReplicationInstancePublicIpAddress** *(string) --*

      The public IP address of the replication instance.

    - **ReplicationInstancePrivateIpAddress** *(string) --*

      The private IP address of the replication instance.

    - **ReplicationInstancePublicIpAddresses** *(list) --*

      One or more public IP addresses for the replication instance.

      - *(string) --*

    - **ReplicationInstancePrivateIpAddresses** *(list) --*

      One or more private IP addresses for the replication instance.

      - *(string) --*

    - **PubliclyAccessible** *(boolean) --*

      Specifies the accessibility options for the replication instance. A value of ``true``
      represents an instance with a public IP address. A value of ``false`` represents an
      instance with a private IP address. The default value is ``true`` .

    - **SecondaryAvailabilityZone** *(string) --*

      The availability zone of the standby replication instance in a Multi-AZ deployment.

    - **FreeUntil** *(datetime) --*

      The expiration date of the free replication instance that is part of the Free DMS program.

    - **DnsNameServers** *(string) --*

      The DNS name servers for the replication instance.
    """


_DescribeReplicationInstancesPaginateResponseTypeDef = TypedDict(
    "_DescribeReplicationInstancesPaginateResponseTypeDef",
    {
        "ReplicationInstances": List[
            DescribeReplicationInstancesPaginateResponseReplicationInstancesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeReplicationInstancesPaginateResponseTypeDef(
    _DescribeReplicationInstancesPaginateResponseTypeDef
):
    """
    Type definition for `DescribeReplicationInstancesPaginate` `Response`

    - **ReplicationInstances** *(list) --*

      The replication instances described.

      - *(dict) --*

        - **ReplicationInstanceIdentifier** *(string) --*

          The replication instance identifier. This parameter is stored as a lowercase string.

          Constraints:

          * Must contain from 1 to 63 alphanumeric characters or hyphens.

          * First character must be a letter.

          * Cannot end with a hyphen or contain two consecutive hyphens.

          Example: ``myrepinstance``

        - **ReplicationInstanceClass** *(string) --*

          The compute and memory capacity of the replication instance.

          Valid Values: ``dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large | dms.c4.large
          | dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge``

        - **ReplicationInstanceStatus** *(string) --*

          The status of the replication instance.

        - **AllocatedStorage** *(integer) --*

          The amount of storage (in gigabytes) that is allocated for the replication instance.

        - **InstanceCreateTime** *(datetime) --*

          The time the replication instance was created.

        - **VpcSecurityGroups** *(list) --*

          The VPC security group for the instance.

          - *(dict) --*

            - **VpcSecurityGroupId** *(string) --*

              The VPC security group Id.

            - **Status** *(string) --*

              The status of the VPC security group.

        - **AvailabilityZone** *(string) --*

          The Availability Zone for the instance.

        - **ReplicationSubnetGroup** *(dict) --*

          The subnet group for the replication instance.

          - **ReplicationSubnetGroupIdentifier** *(string) --*

            The identifier of the replication instance subnet group.

          - **ReplicationSubnetGroupDescription** *(string) --*

            A description for the replication subnet group.

          - **VpcId** *(string) --*

            The ID of the VPC.

          - **SubnetGroupStatus** *(string) --*

            The status of the subnet group.

          - **Subnets** *(list) --*

            The subnets that are in the subnet group.

            - *(dict) --*

              - **SubnetIdentifier** *(string) --*

                The subnet identifier.

              - **SubnetAvailabilityZone** *(dict) --*

                The Availability Zone of the subnet.

                - **Name** *(string) --*

                  The name of the availability zone.

              - **SubnetStatus** *(string) --*

                The status of the subnet.

        - **PreferredMaintenanceWindow** *(string) --*

          The maintenance window times for the replication instance.

        - **PendingModifiedValues** *(dict) --*

          The pending modification values.

          - **ReplicationInstanceClass** *(string) --*

            The compute and memory capacity of the replication instance.

            Valid Values: ``dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large |
            dms.c4.large | dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge``

          - **AllocatedStorage** *(integer) --*

            The amount of storage (in gigabytes) that is allocated for the replication instance.

          - **MultiAZ** *(boolean) --*

            Specifies whether the replication instance is a Multi-AZ deployment. You cannot set the
            ``AvailabilityZone`` parameter if the Multi-AZ parameter is set to ``true`` .

          - **EngineVersion** *(string) --*

            The engine version number of the replication instance.

        - **MultiAZ** *(boolean) --*

          Specifies whether the replication instance is a Multi-AZ deployment. You cannot set the
          ``AvailabilityZone`` parameter if the Multi-AZ parameter is set to ``true`` .

        - **EngineVersion** *(string) --*

          The engine version number of the replication instance.

        - **AutoMinorVersionUpgrade** *(boolean) --*

          Boolean value indicating if minor version upgrades will be automatically applied to the
          instance.

        - **KmsKeyId** *(string) --*

          An AWS KMS key identifier that is used to encrypt the data on the replication instance.

          If you don't specify a value for the ``KmsKeyId`` parameter, then AWS DMS uses your
          default encryption key.

          AWS KMS creates the default encryption key for your AWS account. Your AWS account has a
          different default encryption key for each AWS Region.

        - **ReplicationInstanceArn** *(string) --*

          The Amazon Resource Name (ARN) of the replication instance.

        - **ReplicationInstancePublicIpAddress** *(string) --*

          The public IP address of the replication instance.

        - **ReplicationInstancePrivateIpAddress** *(string) --*

          The private IP address of the replication instance.

        - **ReplicationInstancePublicIpAddresses** *(list) --*

          One or more public IP addresses for the replication instance.

          - *(string) --*

        - **ReplicationInstancePrivateIpAddresses** *(list) --*

          One or more private IP addresses for the replication instance.

          - *(string) --*

        - **PubliclyAccessible** *(boolean) --*

          Specifies the accessibility options for the replication instance. A value of ``true``
          represents an instance with a public IP address. A value of ``false`` represents an
          instance with a private IP address. The default value is ``true`` .

        - **SecondaryAvailabilityZone** *(string) --*

          The availability zone of the standby replication instance in a Multi-AZ deployment.

        - **FreeUntil** *(datetime) --*

          The expiration date of the free replication instance that is part of the Free DMS program.

        - **DnsNameServers** *(string) --*

          The DNS name servers for the replication instance.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribeReplicationSubnetGroupsPaginateFiltersTypeDef = TypedDict(
    "_DescribeReplicationSubnetGroupsPaginateFiltersTypeDef",
    {"Name": str, "Values": List[str]},
)


class DescribeReplicationSubnetGroupsPaginateFiltersTypeDef(
    _DescribeReplicationSubnetGroupsPaginateFiltersTypeDef
):
    """
    Type definition for `DescribeReplicationSubnetGroupsPaginate` `Filters`

    - **Name** *(string) --* **[REQUIRED]**

      The name of the filter.

    - **Values** *(list) --* **[REQUIRED]**

      The filter value.

      - *(string) --*
    """


_DescribeReplicationSubnetGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeReplicationSubnetGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeReplicationSubnetGroupsPaginatePaginationConfigTypeDef(
    _DescribeReplicationSubnetGroupsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeReplicationSubnetGroupsPaginate` `PaginationConfig`

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


_DescribeReplicationSubnetGroupsPaginateResponseReplicationSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "_DescribeReplicationSubnetGroupsPaginateResponseReplicationSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)


class DescribeReplicationSubnetGroupsPaginateResponseReplicationSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef(
    _DescribeReplicationSubnetGroupsPaginateResponseReplicationSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef
):
    """
    Type definition for `DescribeReplicationSubnetGroupsPaginateResponseReplicationSubnetGroupsSubnets` `SubnetAvailabilityZone`

    The Availability Zone of the subnet.

    - **Name** *(string) --*

      The name of the availability zone.
    """


_DescribeReplicationSubnetGroupsPaginateResponseReplicationSubnetGroupsSubnetsTypeDef = TypedDict(
    "_DescribeReplicationSubnetGroupsPaginateResponseReplicationSubnetGroupsSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": DescribeReplicationSubnetGroupsPaginateResponseReplicationSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)


class DescribeReplicationSubnetGroupsPaginateResponseReplicationSubnetGroupsSubnetsTypeDef(
    _DescribeReplicationSubnetGroupsPaginateResponseReplicationSubnetGroupsSubnetsTypeDef
):
    """
    Type definition for `DescribeReplicationSubnetGroupsPaginateResponseReplicationSubnetGroups` `Subnets`

    - **SubnetIdentifier** *(string) --*

      The subnet identifier.

    - **SubnetAvailabilityZone** *(dict) --*

      The Availability Zone of the subnet.

      - **Name** *(string) --*

        The name of the availability zone.

    - **SubnetStatus** *(string) --*

      The status of the subnet.
    """


_DescribeReplicationSubnetGroupsPaginateResponseReplicationSubnetGroupsTypeDef = TypedDict(
    "_DescribeReplicationSubnetGroupsPaginateResponseReplicationSubnetGroupsTypeDef",
    {
        "ReplicationSubnetGroupIdentifier": str,
        "ReplicationSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[
            DescribeReplicationSubnetGroupsPaginateResponseReplicationSubnetGroupsSubnetsTypeDef
        ],
    },
    total=False,
)


class DescribeReplicationSubnetGroupsPaginateResponseReplicationSubnetGroupsTypeDef(
    _DescribeReplicationSubnetGroupsPaginateResponseReplicationSubnetGroupsTypeDef
):
    """
    Type definition for `DescribeReplicationSubnetGroupsPaginateResponse` `ReplicationSubnetGroups`

    - **ReplicationSubnetGroupIdentifier** *(string) --*

      The identifier of the replication instance subnet group.

    - **ReplicationSubnetGroupDescription** *(string) --*

      A description for the replication subnet group.

    - **VpcId** *(string) --*

      The ID of the VPC.

    - **SubnetGroupStatus** *(string) --*

      The status of the subnet group.

    - **Subnets** *(list) --*

      The subnets that are in the subnet group.

      - *(dict) --*

        - **SubnetIdentifier** *(string) --*

          The subnet identifier.

        - **SubnetAvailabilityZone** *(dict) --*

          The Availability Zone of the subnet.

          - **Name** *(string) --*

            The name of the availability zone.

        - **SubnetStatus** *(string) --*

          The status of the subnet.
    """


_DescribeReplicationSubnetGroupsPaginateResponseTypeDef = TypedDict(
    "_DescribeReplicationSubnetGroupsPaginateResponseTypeDef",
    {
        "ReplicationSubnetGroups": List[
            DescribeReplicationSubnetGroupsPaginateResponseReplicationSubnetGroupsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeReplicationSubnetGroupsPaginateResponseTypeDef(
    _DescribeReplicationSubnetGroupsPaginateResponseTypeDef
):
    """
    Type definition for `DescribeReplicationSubnetGroupsPaginate` `Response`

    - **ReplicationSubnetGroups** *(list) --*

      A description of the replication subnet groups.

      - *(dict) --*

        - **ReplicationSubnetGroupIdentifier** *(string) --*

          The identifier of the replication instance subnet group.

        - **ReplicationSubnetGroupDescription** *(string) --*

          A description for the replication subnet group.

        - **VpcId** *(string) --*

          The ID of the VPC.

        - **SubnetGroupStatus** *(string) --*

          The status of the subnet group.

        - **Subnets** *(list) --*

          The subnets that are in the subnet group.

          - *(dict) --*

            - **SubnetIdentifier** *(string) --*

              The subnet identifier.

            - **SubnetAvailabilityZone** *(dict) --*

              The Availability Zone of the subnet.

              - **Name** *(string) --*

                The name of the availability zone.

            - **SubnetStatus** *(string) --*

              The status of the subnet.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribeReplicationTaskAssessmentResultsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeReplicationTaskAssessmentResultsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeReplicationTaskAssessmentResultsPaginatePaginationConfigTypeDef(
    _DescribeReplicationTaskAssessmentResultsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeReplicationTaskAssessmentResultsPaginate` `PaginationConfig`

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


_DescribeReplicationTaskAssessmentResultsPaginateResponseReplicationTaskAssessmentResultsTypeDef = TypedDict(
    "_DescribeReplicationTaskAssessmentResultsPaginateResponseReplicationTaskAssessmentResultsTypeDef",
    {
        "ReplicationTaskIdentifier": str,
        "ReplicationTaskArn": str,
        "ReplicationTaskLastAssessmentDate": datetime,
        "AssessmentStatus": str,
        "AssessmentResultsFile": str,
        "AssessmentResults": str,
        "S3ObjectUrl": str,
    },
    total=False,
)


class DescribeReplicationTaskAssessmentResultsPaginateResponseReplicationTaskAssessmentResultsTypeDef(
    _DescribeReplicationTaskAssessmentResultsPaginateResponseReplicationTaskAssessmentResultsTypeDef
):
    """
    Type definition for `DescribeReplicationTaskAssessmentResultsPaginateResponse` `ReplicationTaskAssessmentResults`

    The task assessment report in JSON format.

    - **ReplicationTaskIdentifier** *(string) --*

      The replication task identifier of the task on which the task assessment was run.

    - **ReplicationTaskArn** *(string) --*

      The Amazon Resource Name (ARN) of the replication task.

    - **ReplicationTaskLastAssessmentDate** *(datetime) --*

      The date the task assessment was completed.

    - **AssessmentStatus** *(string) --*

      The status of the task assessment.

    - **AssessmentResultsFile** *(string) --*

      The file containing the results of the task assessment.

    - **AssessmentResults** *(string) --*

      The task assessment results in JSON format.

    - **S3ObjectUrl** *(string) --*

      The URL of the S3 object containing the task assessment results.
    """


_DescribeReplicationTaskAssessmentResultsPaginateResponseTypeDef = TypedDict(
    "_DescribeReplicationTaskAssessmentResultsPaginateResponseTypeDef",
    {
        "BucketName": str,
        "ReplicationTaskAssessmentResults": List[
            DescribeReplicationTaskAssessmentResultsPaginateResponseReplicationTaskAssessmentResultsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeReplicationTaskAssessmentResultsPaginateResponseTypeDef(
    _DescribeReplicationTaskAssessmentResultsPaginateResponseTypeDef
):
    """
    Type definition for `DescribeReplicationTaskAssessmentResultsPaginate` `Response`

    - **BucketName** *(string) --*

      - The Amazon S3 bucket where the task assessment report is located.

    - **ReplicationTaskAssessmentResults** *(list) --*

      The task assessment report.

      - *(dict) --*

        The task assessment report in JSON format.

        - **ReplicationTaskIdentifier** *(string) --*

          The replication task identifier of the task on which the task assessment was run.

        - **ReplicationTaskArn** *(string) --*

          The Amazon Resource Name (ARN) of the replication task.

        - **ReplicationTaskLastAssessmentDate** *(datetime) --*

          The date the task assessment was completed.

        - **AssessmentStatus** *(string) --*

          The status of the task assessment.

        - **AssessmentResultsFile** *(string) --*

          The file containing the results of the task assessment.

        - **AssessmentResults** *(string) --*

          The task assessment results in JSON format.

        - **S3ObjectUrl** *(string) --*

          The URL of the S3 object containing the task assessment results.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribeReplicationTasksPaginateFiltersTypeDef = TypedDict(
    "_DescribeReplicationTasksPaginateFiltersTypeDef",
    {"Name": str, "Values": List[str]},
)


class DescribeReplicationTasksPaginateFiltersTypeDef(
    _DescribeReplicationTasksPaginateFiltersTypeDef
):
    """
    Type definition for `DescribeReplicationTasksPaginate` `Filters`

    - **Name** *(string) --* **[REQUIRED]**

      The name of the filter.

    - **Values** *(list) --* **[REQUIRED]**

      The filter value.

      - *(string) --*
    """


_DescribeReplicationTasksPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeReplicationTasksPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeReplicationTasksPaginatePaginationConfigTypeDef(
    _DescribeReplicationTasksPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeReplicationTasksPaginate` `PaginationConfig`

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


_DescribeSchemasPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeSchemasPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeSchemasPaginatePaginationConfigTypeDef(
    _DescribeSchemasPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeSchemasPaginate` `PaginationConfig`

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


_DescribeSchemasPaginateResponseTypeDef = TypedDict(
    "_DescribeSchemasPaginateResponseTypeDef",
    {"Schemas": List[str], "NextToken": str},
    total=False,
)


class DescribeSchemasPaginateResponseTypeDef(_DescribeSchemasPaginateResponseTypeDef):
    """
    Type definition for `DescribeSchemasPaginate` `Response`

    - **Schemas** *(list) --*

      The described schema.

      - *(string) --*

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribeTableStatisticsPaginateFiltersTypeDef = TypedDict(
    "_DescribeTableStatisticsPaginateFiltersTypeDef", {"Name": str, "Values": List[str]}
)


class DescribeTableStatisticsPaginateFiltersTypeDef(
    _DescribeTableStatisticsPaginateFiltersTypeDef
):
    """
    Type definition for `DescribeTableStatisticsPaginate` `Filters`

    - **Name** *(string) --* **[REQUIRED]**

      The name of the filter.

    - **Values** *(list) --* **[REQUIRED]**

      The filter value.

      - *(string) --*
    """


_DescribeTableStatisticsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeTableStatisticsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeTableStatisticsPaginatePaginationConfigTypeDef(
    _DescribeTableStatisticsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeTableStatisticsPaginate` `PaginationConfig`

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


_DescribeTableStatisticsPaginateResponseTableStatisticsTypeDef = TypedDict(
    "_DescribeTableStatisticsPaginateResponseTableStatisticsTypeDef",
    {
        "SchemaName": str,
        "TableName": str,
        "Inserts": int,
        "Deletes": int,
        "Updates": int,
        "Ddls": int,
        "FullLoadRows": int,
        "FullLoadCondtnlChkFailedRows": int,
        "FullLoadErrorRows": int,
        "LastUpdateTime": datetime,
        "TableState": str,
        "ValidationPendingRecords": int,
        "ValidationFailedRecords": int,
        "ValidationSuspendedRecords": int,
        "ValidationState": str,
        "ValidationStateDetails": str,
    },
    total=False,
)


class DescribeTableStatisticsPaginateResponseTableStatisticsTypeDef(
    _DescribeTableStatisticsPaginateResponseTableStatisticsTypeDef
):
    """
    Type definition for `DescribeTableStatisticsPaginateResponse` `TableStatistics`

    - **SchemaName** *(string) --*

      The schema name.

    - **TableName** *(string) --*

      The name of the table.

    - **Inserts** *(integer) --*

      The number of insert actions performed on a table.

    - **Deletes** *(integer) --*

      The number of delete actions performed on a table.

    - **Updates** *(integer) --*

      The number of update actions performed on a table.

    - **Ddls** *(integer) --*

      The Data Definition Language (DDL) used to build and modify the structure of your tables.

    - **FullLoadRows** *(integer) --*

      The number of rows added during the Full Load operation.

    - **FullLoadCondtnlChkFailedRows** *(integer) --*

      The number of rows that failed conditional checks during the Full Load operation (valid
      only for DynamoDB as a target migrations).

    - **FullLoadErrorRows** *(integer) --*

      The number of rows that failed to load during the Full Load operation (valid only for
      DynamoDB as a target migrations).

    - **LastUpdateTime** *(datetime) --*

      The last time the table was updated.

    - **TableState** *(string) --*

      The state of the tables described.

      Valid states: Table does not exist | Before load | Full load | Table completed | Table
      cancelled | Table error | Table all | Table updates | Table is being reloaded

    - **ValidationPendingRecords** *(integer) --*

      The number of records that have yet to be validated.

    - **ValidationFailedRecords** *(integer) --*

      The number of records that failed validation.

    - **ValidationSuspendedRecords** *(integer) --*

      The number of records that could not be validated.

    - **ValidationState** *(string) --*

      The validation state of the table.

      The parameter can have the following values

      * Not enabled—Validation is not enabled for the table in the migration task.

      * Pending records—Some records in the table are waiting for validation.

      * Mismatched records—Some records in the table do not match between the source and target.

      * Suspended records—Some records in the table could not be validated.

      * No primary key—The table could not be validated because it had no primary key.

      * Table error—The table was not validated because it was in an error state and some data
      was not migrated.

      * Validated—All rows in the table were validated. If the table is updated, the status can
      change from Validated.

      * Error—The table could not be validated because of an unexpected error.

    - **ValidationStateDetails** *(string) --*

      Additional details about the state of validation.
    """


_DescribeTableStatisticsPaginateResponseTypeDef = TypedDict(
    "_DescribeTableStatisticsPaginateResponseTypeDef",
    {
        "ReplicationTaskArn": str,
        "TableStatistics": List[
            DescribeTableStatisticsPaginateResponseTableStatisticsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeTableStatisticsPaginateResponseTypeDef(
    _DescribeTableStatisticsPaginateResponseTypeDef
):
    """
    Type definition for `DescribeTableStatisticsPaginate` `Response`

    - **ReplicationTaskArn** *(string) --*

      The Amazon Resource Name (ARN) of the replication task.

    - **TableStatistics** *(list) --*

      The table statistics.

      - *(dict) --*

        - **SchemaName** *(string) --*

          The schema name.

        - **TableName** *(string) --*

          The name of the table.

        - **Inserts** *(integer) --*

          The number of insert actions performed on a table.

        - **Deletes** *(integer) --*

          The number of delete actions performed on a table.

        - **Updates** *(integer) --*

          The number of update actions performed on a table.

        - **Ddls** *(integer) --*

          The Data Definition Language (DDL) used to build and modify the structure of your tables.

        - **FullLoadRows** *(integer) --*

          The number of rows added during the Full Load operation.

        - **FullLoadCondtnlChkFailedRows** *(integer) --*

          The number of rows that failed conditional checks during the Full Load operation (valid
          only for DynamoDB as a target migrations).

        - **FullLoadErrorRows** *(integer) --*

          The number of rows that failed to load during the Full Load operation (valid only for
          DynamoDB as a target migrations).

        - **LastUpdateTime** *(datetime) --*

          The last time the table was updated.

        - **TableState** *(string) --*

          The state of the tables described.

          Valid states: Table does not exist | Before load | Full load | Table completed | Table
          cancelled | Table error | Table all | Table updates | Table is being reloaded

        - **ValidationPendingRecords** *(integer) --*

          The number of records that have yet to be validated.

        - **ValidationFailedRecords** *(integer) --*

          The number of records that failed validation.

        - **ValidationSuspendedRecords** *(integer) --*

          The number of records that could not be validated.

        - **ValidationState** *(string) --*

          The validation state of the table.

          The parameter can have the following values

          * Not enabled—Validation is not enabled for the table in the migration task.

          * Pending records—Some records in the table are waiting for validation.

          * Mismatched records—Some records in the table do not match between the source and target.

          * Suspended records—Some records in the table could not be validated.

          * No primary key—The table could not be validated because it had no primary key.

          * Table error—The table was not validated because it was in an error state and some data
          was not migrated.

          * Validated—All rows in the table were validated. If the table is updated, the status can
          change from Validated.

          * Error—The table could not be validated because of an unexpected error.

        - **ValidationStateDetails** *(string) --*

          Additional details about the state of validation.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_EndpointDeletedWaitFiltersTypeDef = TypedDict(
    "_EndpointDeletedWaitFiltersTypeDef", {"Name": str, "Values": List[str]}
)


class EndpointDeletedWaitFiltersTypeDef(_EndpointDeletedWaitFiltersTypeDef):
    """
    Type definition for `EndpointDeletedWait` `Filters`

    - **Name** *(string) --* **[REQUIRED]**

      The name of the filter.

    - **Values** *(list) --* **[REQUIRED]**

      The filter value.

      - *(string) --*
    """


_EndpointDeletedWaitWaiterConfigTypeDef = TypedDict(
    "_EndpointDeletedWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class EndpointDeletedWaitWaiterConfigTypeDef(_EndpointDeletedWaitWaiterConfigTypeDef):
    """
    Type definition for `EndpointDeletedWait` `WaiterConfig`

    A dictionary that provides parameters to control waiting behavior.

    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 5

    - **MaxAttempts** *(integer) --*

      The maximum number of attempts to be made. Default: 60
    """


_ReplicationInstanceAvailableWaitFiltersTypeDef = TypedDict(
    "_ReplicationInstanceAvailableWaitFiltersTypeDef",
    {"Name": str, "Values": List[str]},
)


class ReplicationInstanceAvailableWaitFiltersTypeDef(
    _ReplicationInstanceAvailableWaitFiltersTypeDef
):
    """
    Type definition for `ReplicationInstanceAvailableWait` `Filters`

    - **Name** *(string) --* **[REQUIRED]**

      The name of the filter.

    - **Values** *(list) --* **[REQUIRED]**

      The filter value.

      - *(string) --*
    """


_ReplicationInstanceAvailableWaitWaiterConfigTypeDef = TypedDict(
    "_ReplicationInstanceAvailableWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class ReplicationInstanceAvailableWaitWaiterConfigTypeDef(
    _ReplicationInstanceAvailableWaitWaiterConfigTypeDef
):
    """
    Type definition for `ReplicationInstanceAvailableWait` `WaiterConfig`

    A dictionary that provides parameters to control waiting behavior.

    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 60

    - **MaxAttempts** *(integer) --*

      The maximum number of attempts to be made. Default: 60
    """


_ReplicationInstanceDeletedWaitFiltersTypeDef = TypedDict(
    "_ReplicationInstanceDeletedWaitFiltersTypeDef", {"Name": str, "Values": List[str]}
)


class ReplicationInstanceDeletedWaitFiltersTypeDef(
    _ReplicationInstanceDeletedWaitFiltersTypeDef
):
    """
    Type definition for `ReplicationInstanceDeletedWait` `Filters`

    - **Name** *(string) --* **[REQUIRED]**

      The name of the filter.

    - **Values** *(list) --* **[REQUIRED]**

      The filter value.

      - *(string) --*
    """


_ReplicationInstanceDeletedWaitWaiterConfigTypeDef = TypedDict(
    "_ReplicationInstanceDeletedWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class ReplicationInstanceDeletedWaitWaiterConfigTypeDef(
    _ReplicationInstanceDeletedWaitWaiterConfigTypeDef
):
    """
    Type definition for `ReplicationInstanceDeletedWait` `WaiterConfig`

    A dictionary that provides parameters to control waiting behavior.

    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 15

    - **MaxAttempts** *(integer) --*

      The maximum number of attempts to be made. Default: 60
    """


_ReplicationTaskDeletedWaitFiltersTypeDef = TypedDict(
    "_ReplicationTaskDeletedWaitFiltersTypeDef", {"Name": str, "Values": List[str]}
)


class ReplicationTaskDeletedWaitFiltersTypeDef(
    _ReplicationTaskDeletedWaitFiltersTypeDef
):
    """
    Type definition for `ReplicationTaskDeletedWait` `Filters`

    - **Name** *(string) --* **[REQUIRED]**

      The name of the filter.

    - **Values** *(list) --* **[REQUIRED]**

      The filter value.

      - *(string) --*
    """


_ReplicationTaskDeletedWaitWaiterConfigTypeDef = TypedDict(
    "_ReplicationTaskDeletedWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class ReplicationTaskDeletedWaitWaiterConfigTypeDef(
    _ReplicationTaskDeletedWaitWaiterConfigTypeDef
):
    """
    Type definition for `ReplicationTaskDeletedWait` `WaiterConfig`

    A dictionary that provides parameters to control waiting behavior.

    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 15

    - **MaxAttempts** *(integer) --*

      The maximum number of attempts to be made. Default: 60
    """


_ReplicationTaskReadyWaitFiltersTypeDef = TypedDict(
    "_ReplicationTaskReadyWaitFiltersTypeDef", {"Name": str, "Values": List[str]}
)


class ReplicationTaskReadyWaitFiltersTypeDef(_ReplicationTaskReadyWaitFiltersTypeDef):
    """
    Type definition for `ReplicationTaskReadyWait` `Filters`

    - **Name** *(string) --* **[REQUIRED]**

      The name of the filter.

    - **Values** *(list) --* **[REQUIRED]**

      The filter value.

      - *(string) --*
    """


_ReplicationTaskReadyWaitWaiterConfigTypeDef = TypedDict(
    "_ReplicationTaskReadyWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class ReplicationTaskReadyWaitWaiterConfigTypeDef(
    _ReplicationTaskReadyWaitWaiterConfigTypeDef
):
    """
    Type definition for `ReplicationTaskReadyWait` `WaiterConfig`

    A dictionary that provides parameters to control waiting behavior.

    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 15

    - **MaxAttempts** *(integer) --*

      The maximum number of attempts to be made. Default: 60
    """


_ReplicationTaskRunningWaitFiltersTypeDef = TypedDict(
    "_ReplicationTaskRunningWaitFiltersTypeDef", {"Name": str, "Values": List[str]}
)


class ReplicationTaskRunningWaitFiltersTypeDef(
    _ReplicationTaskRunningWaitFiltersTypeDef
):
    """
    Type definition for `ReplicationTaskRunningWait` `Filters`

    - **Name** *(string) --* **[REQUIRED]**

      The name of the filter.

    - **Values** *(list) --* **[REQUIRED]**

      The filter value.

      - *(string) --*
    """


_ReplicationTaskRunningWaitWaiterConfigTypeDef = TypedDict(
    "_ReplicationTaskRunningWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class ReplicationTaskRunningWaitWaiterConfigTypeDef(
    _ReplicationTaskRunningWaitWaiterConfigTypeDef
):
    """
    Type definition for `ReplicationTaskRunningWait` `WaiterConfig`

    A dictionary that provides parameters to control waiting behavior.

    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 15

    - **MaxAttempts** *(integer) --*

      The maximum number of attempts to be made. Default: 60
    """


_ReplicationTaskStoppedWaitFiltersTypeDef = TypedDict(
    "_ReplicationTaskStoppedWaitFiltersTypeDef", {"Name": str, "Values": List[str]}
)


class ReplicationTaskStoppedWaitFiltersTypeDef(
    _ReplicationTaskStoppedWaitFiltersTypeDef
):
    """
    Type definition for `ReplicationTaskStoppedWait` `Filters`

    - **Name** *(string) --* **[REQUIRED]**

      The name of the filter.

    - **Values** *(list) --* **[REQUIRED]**

      The filter value.

      - *(string) --*
    """


_ReplicationTaskStoppedWaitWaiterConfigTypeDef = TypedDict(
    "_ReplicationTaskStoppedWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class ReplicationTaskStoppedWaitWaiterConfigTypeDef(
    _ReplicationTaskStoppedWaitWaiterConfigTypeDef
):
    """
    Type definition for `ReplicationTaskStoppedWait` `WaiterConfig`

    A dictionary that provides parameters to control waiting behavior.

    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 15

    - **MaxAttempts** *(integer) --*

      The maximum number of attempts to be made. Default: 60
    """


_TestConnectionSucceedsWaitFiltersTypeDef = TypedDict(
    "_TestConnectionSucceedsWaitFiltersTypeDef", {"Name": str, "Values": List[str]}
)


class TestConnectionSucceedsWaitFiltersTypeDef(
    _TestConnectionSucceedsWaitFiltersTypeDef
):
    """
    Type definition for `TestConnectionSucceedsWait` `Filters`

    - **Name** *(string) --* **[REQUIRED]**

      The name of the filter.

    - **Values** *(list) --* **[REQUIRED]**

      The filter value.

      - *(string) --*
    """


_TestConnectionSucceedsWaitWaiterConfigTypeDef = TypedDict(
    "_TestConnectionSucceedsWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class TestConnectionSucceedsWaitWaiterConfigTypeDef(
    _TestConnectionSucceedsWaitWaiterConfigTypeDef
):
    """
    Type definition for `TestConnectionSucceedsWait` `WaiterConfig`

    A dictionary that provides parameters to control waiting behavior.

    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 5

    - **MaxAttempts** *(integer) --*

      The maximum number of attempts to be made. Default: 60
    """
