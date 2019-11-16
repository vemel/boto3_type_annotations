"Main interface for es type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientAddTagsTagListTypeDef",
    "ClientCancelElasticsearchServiceSoftwareUpdateResponseServiceSoftwareOptionsTypeDef",
    "ClientCancelElasticsearchServiceSoftwareUpdateResponseTypeDef",
    "ClientCreateElasticsearchDomainCognitoOptionsTypeDef",
    "ClientCreateElasticsearchDomainDomainEndpointOptionsTypeDef",
    "ClientCreateElasticsearchDomainEBSOptionsTypeDef",
    "ClientCreateElasticsearchDomainElasticsearchClusterConfigZoneAwarenessConfigTypeDef",
    "ClientCreateElasticsearchDomainElasticsearchClusterConfigTypeDef",
    "ClientCreateElasticsearchDomainEncryptionAtRestOptionsTypeDef",
    "ClientCreateElasticsearchDomainLogPublishingOptionsTypeDef",
    "ClientCreateElasticsearchDomainNodeToNodeEncryptionOptionsTypeDef",
    "ClientCreateElasticsearchDomainResponseDomainStatusCognitoOptionsTypeDef",
    "ClientCreateElasticsearchDomainResponseDomainStatusDomainEndpointOptionsTypeDef",
    "ClientCreateElasticsearchDomainResponseDomainStatusEBSOptionsTypeDef",
    "ClientCreateElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigZoneAwarenessConfigTypeDef",
    "ClientCreateElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigTypeDef",
    "ClientCreateElasticsearchDomainResponseDomainStatusEncryptionAtRestOptionsTypeDef",
    "ClientCreateElasticsearchDomainResponseDomainStatusLogPublishingOptionsTypeDef",
    "ClientCreateElasticsearchDomainResponseDomainStatusNodeToNodeEncryptionOptionsTypeDef",
    "ClientCreateElasticsearchDomainResponseDomainStatusServiceSoftwareOptionsTypeDef",
    "ClientCreateElasticsearchDomainResponseDomainStatusSnapshotOptionsTypeDef",
    "ClientCreateElasticsearchDomainResponseDomainStatusVPCOptionsTypeDef",
    "ClientCreateElasticsearchDomainResponseDomainStatusTypeDef",
    "ClientCreateElasticsearchDomainResponseTypeDef",
    "ClientCreateElasticsearchDomainSnapshotOptionsTypeDef",
    "ClientCreateElasticsearchDomainVPCOptionsTypeDef",
    "ClientDeleteElasticsearchDomainResponseDomainStatusCognitoOptionsTypeDef",
    "ClientDeleteElasticsearchDomainResponseDomainStatusDomainEndpointOptionsTypeDef",
    "ClientDeleteElasticsearchDomainResponseDomainStatusEBSOptionsTypeDef",
    "ClientDeleteElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigZoneAwarenessConfigTypeDef",
    "ClientDeleteElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigTypeDef",
    "ClientDeleteElasticsearchDomainResponseDomainStatusEncryptionAtRestOptionsTypeDef",
    "ClientDeleteElasticsearchDomainResponseDomainStatusLogPublishingOptionsTypeDef",
    "ClientDeleteElasticsearchDomainResponseDomainStatusNodeToNodeEncryptionOptionsTypeDef",
    "ClientDeleteElasticsearchDomainResponseDomainStatusServiceSoftwareOptionsTypeDef",
    "ClientDeleteElasticsearchDomainResponseDomainStatusSnapshotOptionsTypeDef",
    "ClientDeleteElasticsearchDomainResponseDomainStatusVPCOptionsTypeDef",
    "ClientDeleteElasticsearchDomainResponseDomainStatusTypeDef",
    "ClientDeleteElasticsearchDomainResponseTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigAccessPoliciesStatusTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigAccessPoliciesTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigAdvancedOptionsStatusTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigAdvancedOptionsTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigCognitoOptionsOptionsTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigCognitoOptionsStatusTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigCognitoOptionsTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsOptionsTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsStatusTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigEBSOptionsOptionsTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigEBSOptionsStatusTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigEBSOptionsTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigOptionsZoneAwarenessConfigTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigOptionsTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigStatusTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchVersionStatusTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchVersionTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsOptionsTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsStatusTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsOptionsTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsStatusTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsOptionsTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsStatusTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsOptionsTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsStatusTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigVPCOptionsOptionsTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigVPCOptionsStatusTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigVPCOptionsTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseTypeDef",
    "ClientDescribeElasticsearchDomainResponseDomainStatusCognitoOptionsTypeDef",
    "ClientDescribeElasticsearchDomainResponseDomainStatusDomainEndpointOptionsTypeDef",
    "ClientDescribeElasticsearchDomainResponseDomainStatusEBSOptionsTypeDef",
    "ClientDescribeElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigZoneAwarenessConfigTypeDef",
    "ClientDescribeElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigTypeDef",
    "ClientDescribeElasticsearchDomainResponseDomainStatusEncryptionAtRestOptionsTypeDef",
    "ClientDescribeElasticsearchDomainResponseDomainStatusLogPublishingOptionsTypeDef",
    "ClientDescribeElasticsearchDomainResponseDomainStatusNodeToNodeEncryptionOptionsTypeDef",
    "ClientDescribeElasticsearchDomainResponseDomainStatusServiceSoftwareOptionsTypeDef",
    "ClientDescribeElasticsearchDomainResponseDomainStatusSnapshotOptionsTypeDef",
    "ClientDescribeElasticsearchDomainResponseDomainStatusVPCOptionsTypeDef",
    "ClientDescribeElasticsearchDomainResponseDomainStatusTypeDef",
    "ClientDescribeElasticsearchDomainResponseTypeDef",
    "ClientDescribeElasticsearchDomainsResponseDomainStatusListCognitoOptionsTypeDef",
    "ClientDescribeElasticsearchDomainsResponseDomainStatusListDomainEndpointOptionsTypeDef",
    "ClientDescribeElasticsearchDomainsResponseDomainStatusListEBSOptionsTypeDef",
    "ClientDescribeElasticsearchDomainsResponseDomainStatusListElasticsearchClusterConfigZoneAwarenessConfigTypeDef",
    "ClientDescribeElasticsearchDomainsResponseDomainStatusListElasticsearchClusterConfigTypeDef",
    "ClientDescribeElasticsearchDomainsResponseDomainStatusListEncryptionAtRestOptionsTypeDef",
    "ClientDescribeElasticsearchDomainsResponseDomainStatusListLogPublishingOptionsTypeDef",
    "ClientDescribeElasticsearchDomainsResponseDomainStatusListNodeToNodeEncryptionOptionsTypeDef",
    "ClientDescribeElasticsearchDomainsResponseDomainStatusListServiceSoftwareOptionsTypeDef",
    "ClientDescribeElasticsearchDomainsResponseDomainStatusListSnapshotOptionsTypeDef",
    "ClientDescribeElasticsearchDomainsResponseDomainStatusListVPCOptionsTypeDef",
    "ClientDescribeElasticsearchDomainsResponseDomainStatusListTypeDef",
    "ClientDescribeElasticsearchDomainsResponseTypeDef",
    "ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleAdditionalLimitsTypeDef",
    "ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleInstanceLimitsInstanceCountLimitsTypeDef",
    "ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleInstanceLimitsTypeDef",
    "ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleStorageTypesStorageTypeLimitsTypeDef",
    "ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleStorageTypesTypeDef",
    "ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleTypeDef",
    "ClientDescribeElasticsearchInstanceTypeLimitsResponseTypeDef",
    "ClientDescribeReservedElasticsearchInstanceOfferingsResponseReservedElasticsearchInstanceOfferingsRecurringChargesTypeDef",
    "ClientDescribeReservedElasticsearchInstanceOfferingsResponseReservedElasticsearchInstanceOfferingsTypeDef",
    "ClientDescribeReservedElasticsearchInstanceOfferingsResponseTypeDef",
    "ClientDescribeReservedElasticsearchInstancesResponseReservedElasticsearchInstancesRecurringChargesTypeDef",
    "ClientDescribeReservedElasticsearchInstancesResponseReservedElasticsearchInstancesTypeDef",
    "ClientDescribeReservedElasticsearchInstancesResponseTypeDef",
    "ClientGetCompatibleElasticsearchVersionsResponseCompatibleElasticsearchVersionsTypeDef",
    "ClientGetCompatibleElasticsearchVersionsResponseTypeDef",
    "ClientGetUpgradeHistoryResponseUpgradeHistoriesStepsListTypeDef",
    "ClientGetUpgradeHistoryResponseUpgradeHistoriesTypeDef",
    "ClientGetUpgradeHistoryResponseTypeDef",
    "ClientGetUpgradeStatusResponseTypeDef",
    "ClientListDomainNamesResponseDomainNamesTypeDef",
    "ClientListDomainNamesResponseTypeDef",
    "ClientListElasticsearchInstanceTypesResponseTypeDef",
    "ClientListElasticsearchVersionsResponseTypeDef",
    "ClientListTagsResponseTagListTypeDef",
    "ClientListTagsResponseTypeDef",
    "ClientPurchaseReservedElasticsearchInstanceOfferingResponseTypeDef",
    "ClientStartElasticsearchServiceSoftwareUpdateResponseServiceSoftwareOptionsTypeDef",
    "ClientStartElasticsearchServiceSoftwareUpdateResponseTypeDef",
    "ClientUpdateElasticsearchDomainConfigCognitoOptionsTypeDef",
    "ClientUpdateElasticsearchDomainConfigDomainEndpointOptionsTypeDef",
    "ClientUpdateElasticsearchDomainConfigEBSOptionsTypeDef",
    "ClientUpdateElasticsearchDomainConfigElasticsearchClusterConfigZoneAwarenessConfigTypeDef",
    "ClientUpdateElasticsearchDomainConfigElasticsearchClusterConfigTypeDef",
    "ClientUpdateElasticsearchDomainConfigLogPublishingOptionsTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigAccessPoliciesStatusTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigAccessPoliciesTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigAdvancedOptionsStatusTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigAdvancedOptionsTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigCognitoOptionsOptionsTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigCognitoOptionsStatusTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigCognitoOptionsTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsOptionsTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsStatusTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigEBSOptionsOptionsTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigEBSOptionsStatusTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigEBSOptionsTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigOptionsZoneAwarenessConfigTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigOptionsTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigStatusTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchVersionStatusTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchVersionTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsOptionsTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsStatusTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsOptionsTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsStatusTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsOptionsTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsStatusTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsOptionsTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsStatusTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigVPCOptionsOptionsTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigVPCOptionsStatusTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigVPCOptionsTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseTypeDef",
    "ClientUpdateElasticsearchDomainConfigSnapshotOptionsTypeDef",
    "ClientUpdateElasticsearchDomainConfigVPCOptionsTypeDef",
    "ClientUpgradeElasticsearchDomainResponseTypeDef",
    "DescribeReservedElasticsearchInstanceOfferingsPaginatePaginationConfigTypeDef",
    "DescribeReservedElasticsearchInstanceOfferingsPaginateResponseReservedElasticsearchInstanceOfferingsRecurringChargesTypeDef",
    "DescribeReservedElasticsearchInstanceOfferingsPaginateResponseReservedElasticsearchInstanceOfferingsTypeDef",
    "DescribeReservedElasticsearchInstanceOfferingsPaginateResponseTypeDef",
    "DescribeReservedElasticsearchInstancesPaginatePaginationConfigTypeDef",
    "DescribeReservedElasticsearchInstancesPaginateResponseReservedElasticsearchInstancesRecurringChargesTypeDef",
    "DescribeReservedElasticsearchInstancesPaginateResponseReservedElasticsearchInstancesTypeDef",
    "DescribeReservedElasticsearchInstancesPaginateResponseTypeDef",
    "GetUpgradeHistoryPaginatePaginationConfigTypeDef",
    "GetUpgradeHistoryPaginateResponseUpgradeHistoriesStepsListTypeDef",
    "GetUpgradeHistoryPaginateResponseUpgradeHistoriesTypeDef",
    "GetUpgradeHistoryPaginateResponseTypeDef",
    "ListElasticsearchInstanceTypesPaginatePaginationConfigTypeDef",
    "ListElasticsearchInstanceTypesPaginateResponseTypeDef",
    "ListElasticsearchVersionsPaginatePaginationConfigTypeDef",
    "ListElasticsearchVersionsPaginateResponseTypeDef",
)


_ClientAddTagsTagListTypeDef = TypedDict(
    "_ClientAddTagsTagListTypeDef", {"Key": str, "Value": str}
)


class ClientAddTagsTagListTypeDef(_ClientAddTagsTagListTypeDef):
    """
    Type definition for `ClientAddTags` `TagList`

    Specifies a key value pair for a resource tag.

    - **Key** *(string) --* **[REQUIRED]**

      Specifies the ``TagKey`` , the name of the tag. Tag keys must be unique for the Elasticsearch
      domain to which they are attached.

    - **Value** *(string) --* **[REQUIRED]**

      Specifies the ``TagValue`` , the value assigned to the corresponding tag key. Tag values can
      be null and do not have to be unique in a tag set. For example, you can have a key value pair
      in a tag set of ``project : Trinity`` and ``cost-center : Trinity``
    """


_ClientCancelElasticsearchServiceSoftwareUpdateResponseServiceSoftwareOptionsTypeDef = TypedDict(
    "_ClientCancelElasticsearchServiceSoftwareUpdateResponseServiceSoftwareOptionsTypeDef",
    {
        "CurrentVersion": str,
        "NewVersion": str,
        "UpdateAvailable": bool,
        "Cancellable": bool,
        "UpdateStatus": str,
        "Description": str,
        "AutomatedUpdateDate": datetime,
    },
    total=False,
)


class ClientCancelElasticsearchServiceSoftwareUpdateResponseServiceSoftwareOptionsTypeDef(
    _ClientCancelElasticsearchServiceSoftwareUpdateResponseServiceSoftwareOptionsTypeDef
):
    """
    Type definition for `ClientCancelElasticsearchServiceSoftwareUpdateResponse` `ServiceSoftwareOptions`

    The current status of the Elasticsearch service software update.

    - **CurrentVersion** *(string) --*

      The current service software version that is present on the domain.

    - **NewVersion** *(string) --*

      The new service software version if one is available.

    - **UpdateAvailable** *(boolean) --*

      ``True`` if you are able to update you service software version. ``False`` if you are not
      able to update your service software version.

    - **Cancellable** *(boolean) --*

      ``True`` if you are able to cancel your service software version update. ``False`` if you
      are not able to cancel your service software version.

    - **UpdateStatus** *(string) --*

      The status of your service software update. This field can take the following values:
      ``ELIGIBLE`` , ``PENDING_UPDATE`` , ``IN_PROGRESS`` , ``COMPLETED`` , and ``NOT_ELIGIBLE`` .

    - **Description** *(string) --*

      The description of the ``UpdateStatus`` .

    - **AutomatedUpdateDate** *(datetime) --*

      Timestamp, in Epoch time, until which you can manually request a service software update.
      After this date, we automatically update your service software.
    """


_ClientCancelElasticsearchServiceSoftwareUpdateResponseTypeDef = TypedDict(
    "_ClientCancelElasticsearchServiceSoftwareUpdateResponseTypeDef",
    {
        "ServiceSoftwareOptions": ClientCancelElasticsearchServiceSoftwareUpdateResponseServiceSoftwareOptionsTypeDef
    },
    total=False,
)


class ClientCancelElasticsearchServiceSoftwareUpdateResponseTypeDef(
    _ClientCancelElasticsearchServiceSoftwareUpdateResponseTypeDef
):
    """
    Type definition for `ClientCancelElasticsearchServiceSoftwareUpdate` `Response`

    The result of a ``CancelElasticsearchServiceSoftwareUpdate`` operation. Contains the status of
    the update.

    - **ServiceSoftwareOptions** *(dict) --*

      The current status of the Elasticsearch service software update.

      - **CurrentVersion** *(string) --*

        The current service software version that is present on the domain.

      - **NewVersion** *(string) --*

        The new service software version if one is available.

      - **UpdateAvailable** *(boolean) --*

        ``True`` if you are able to update you service software version. ``False`` if you are not
        able to update your service software version.

      - **Cancellable** *(boolean) --*

        ``True`` if you are able to cancel your service software version update. ``False`` if you
        are not able to cancel your service software version.

      - **UpdateStatus** *(string) --*

        The status of your service software update. This field can take the following values:
        ``ELIGIBLE`` , ``PENDING_UPDATE`` , ``IN_PROGRESS`` , ``COMPLETED`` , and ``NOT_ELIGIBLE`` .

      - **Description** *(string) --*

        The description of the ``UpdateStatus`` .

      - **AutomatedUpdateDate** *(datetime) --*

        Timestamp, in Epoch time, until which you can manually request a service software update.
        After this date, we automatically update your service software.
    """


_ClientCreateElasticsearchDomainCognitoOptionsTypeDef = TypedDict(
    "_ClientCreateElasticsearchDomainCognitoOptionsTypeDef",
    {"Enabled": bool, "UserPoolId": str, "IdentityPoolId": str, "RoleArn": str},
    total=False,
)


class ClientCreateElasticsearchDomainCognitoOptionsTypeDef(
    _ClientCreateElasticsearchDomainCognitoOptionsTypeDef
):
    """
    Type definition for `ClientCreateElasticsearchDomain` `CognitoOptions`

    Options to specify the Cognito user and identity pools for Kibana authentication. For more
    information, see `Amazon Cognito Authentication for Kibana
    <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-cognito-auth.html>`__ .

    - **Enabled** *(boolean) --*

      Specifies the option to enable Cognito for Kibana authentication.

    - **UserPoolId** *(string) --*

      Specifies the Cognito user pool ID for Kibana authentication.

    - **IdentityPoolId** *(string) --*

      Specifies the Cognito identity pool ID for Kibana authentication.

    - **RoleArn** *(string) --*

      Specifies the role ARN that provides Elasticsearch permissions for accessing Cognito resources.
    """


_ClientCreateElasticsearchDomainDomainEndpointOptionsTypeDef = TypedDict(
    "_ClientCreateElasticsearchDomainDomainEndpointOptionsTypeDef",
    {"EnforceHTTPS": bool, "TLSSecurityPolicy": str},
    total=False,
)


class ClientCreateElasticsearchDomainDomainEndpointOptionsTypeDef(
    _ClientCreateElasticsearchDomainDomainEndpointOptionsTypeDef
):
    """
    Type definition for `ClientCreateElasticsearchDomain` `DomainEndpointOptions`

    Options to specify configuration that will be applied to the domain endpoint.

    - **EnforceHTTPS** *(boolean) --*

      Specify if only HTTPS endpoint should be enabled for the Elasticsearch domain.

    - **TLSSecurityPolicy** *(string) --*

      Specify the TLS security policy that needs to be applied to the HTTPS endpoint of Elasticsearch
      domain. It can be one of the following values:

      * **Policy-Min-TLS-1-0-2019-07:** TLS security policy which supports TLSv1.0 and higher.

      * **Policy-Min-TLS-1-2-2019-07:** TLS security policy which supports only TLSv1.2
    """


_ClientCreateElasticsearchDomainEBSOptionsTypeDef = TypedDict(
    "_ClientCreateElasticsearchDomainEBSOptionsTypeDef",
    {"EBSEnabled": bool, "VolumeType": str, "VolumeSize": int, "Iops": int},
    total=False,
)


class ClientCreateElasticsearchDomainEBSOptionsTypeDef(
    _ClientCreateElasticsearchDomainEBSOptionsTypeDef
):
    """
    Type definition for `ClientCreateElasticsearchDomain` `EBSOptions`

    Options to enable, disable and specify the type and size of EBS storage volumes.

    - **EBSEnabled** *(boolean) --*

      Specifies whether EBS-based storage is enabled.

    - **VolumeType** *(string) --*

      Specifies the volume type for EBS-based storage.

    - **VolumeSize** *(integer) --*

      Integer to specify the size of an EBS volume.

    - **Iops** *(integer) --*

      Specifies the IOPD for a Provisioned IOPS EBS volume (SSD).
    """


_ClientCreateElasticsearchDomainElasticsearchClusterConfigZoneAwarenessConfigTypeDef = TypedDict(
    "_ClientCreateElasticsearchDomainElasticsearchClusterConfigZoneAwarenessConfigTypeDef",
    {"AvailabilityZoneCount": int},
    total=False,
)


class ClientCreateElasticsearchDomainElasticsearchClusterConfigZoneAwarenessConfigTypeDef(
    _ClientCreateElasticsearchDomainElasticsearchClusterConfigZoneAwarenessConfigTypeDef
):
    """
    Type definition for `ClientCreateElasticsearchDomainElasticsearchClusterConfig` `ZoneAwarenessConfig`

    Specifies the zone awareness configuration for a domain when zone awareness is enabled.

    - **AvailabilityZoneCount** *(integer) --*

      An integer value to indicate the number of availability zones for a domain when zone
      awareness is enabled. This should be equal to number of subnets if VPC endpoints is enabled
    """


_ClientCreateElasticsearchDomainElasticsearchClusterConfigTypeDef = TypedDict(
    "_ClientCreateElasticsearchDomainElasticsearchClusterConfigTypeDef",
    {
        "InstanceType": str,
        "InstanceCount": int,
        "DedicatedMasterEnabled": bool,
        "ZoneAwarenessEnabled": bool,
        "ZoneAwarenessConfig": ClientCreateElasticsearchDomainElasticsearchClusterConfigZoneAwarenessConfigTypeDef,
        "DedicatedMasterType": str,
        "DedicatedMasterCount": int,
    },
    total=False,
)


class ClientCreateElasticsearchDomainElasticsearchClusterConfigTypeDef(
    _ClientCreateElasticsearchDomainElasticsearchClusterConfigTypeDef
):
    """
    Type definition for `ClientCreateElasticsearchDomain` `ElasticsearchClusterConfig`

    Configuration options for an Elasticsearch domain. Specifies the instance type and number of
    instances in the domain cluster.

    - **InstanceType** *(string) --*

      The instance type for an Elasticsearch cluster.

    - **InstanceCount** *(integer) --*

      The number of instances in the specified domain cluster.

    - **DedicatedMasterEnabled** *(boolean) --*

      A boolean value to indicate whether a dedicated master node is enabled. See `About Dedicated
      Master Nodes
      <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains.html#es-managedomains-dedicatedmasternodes>`__
      for more information.

    - **ZoneAwarenessEnabled** *(boolean) --*

      A boolean value to indicate whether zone awareness is enabled. See `About Zone Awareness
      <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains.html#es-managedomains-zoneawareness>`__
      for more information.

    - **ZoneAwarenessConfig** *(dict) --*

      Specifies the zone awareness configuration for a domain when zone awareness is enabled.

      - **AvailabilityZoneCount** *(integer) --*

        An integer value to indicate the number of availability zones for a domain when zone
        awareness is enabled. This should be equal to number of subnets if VPC endpoints is enabled

    - **DedicatedMasterType** *(string) --*

      The instance type for a dedicated master node.

    - **DedicatedMasterCount** *(integer) --*

      Total number of dedicated master nodes, active and on standby, for the cluster.
    """


_ClientCreateElasticsearchDomainEncryptionAtRestOptionsTypeDef = TypedDict(
    "_ClientCreateElasticsearchDomainEncryptionAtRestOptionsTypeDef",
    {"Enabled": bool, "KmsKeyId": str},
    total=False,
)


class ClientCreateElasticsearchDomainEncryptionAtRestOptionsTypeDef(
    _ClientCreateElasticsearchDomainEncryptionAtRestOptionsTypeDef
):
    """
    Type definition for `ClientCreateElasticsearchDomain` `EncryptionAtRestOptions`

    Specifies the Encryption At Rest Options.

    - **Enabled** *(boolean) --*

      Specifies the option to enable Encryption At Rest.

    - **KmsKeyId** *(string) --*

      Specifies the KMS Key ID for Encryption At Rest options.
    """


_ClientCreateElasticsearchDomainLogPublishingOptionsTypeDef = TypedDict(
    "_ClientCreateElasticsearchDomainLogPublishingOptionsTypeDef",
    {"CloudWatchLogsLogGroupArn": str, "Enabled": bool},
    total=False,
)


class ClientCreateElasticsearchDomainLogPublishingOptionsTypeDef(
    _ClientCreateElasticsearchDomainLogPublishingOptionsTypeDef
):
    """
    Type definition for `ClientCreateElasticsearchDomain` `LogPublishingOptions`

    Log Publishing option that is set for given domain. Attributes and their details:

    * CloudWatchLogsLogGroupArn: ARN of the Cloudwatch log group to which log needs to be
    published.

    * Enabled: Whether the log publishing for given log type is enabled or not

    - **CloudWatchLogsLogGroupArn** *(string) --*

      ARN of the Cloudwatch log group to which log needs to be published.

    - **Enabled** *(boolean) --*

      Specifies whether given log publishing option is enabled or not.
    """


_ClientCreateElasticsearchDomainNodeToNodeEncryptionOptionsTypeDef = TypedDict(
    "_ClientCreateElasticsearchDomainNodeToNodeEncryptionOptionsTypeDef",
    {"Enabled": bool},
    total=False,
)


class ClientCreateElasticsearchDomainNodeToNodeEncryptionOptionsTypeDef(
    _ClientCreateElasticsearchDomainNodeToNodeEncryptionOptionsTypeDef
):
    """
    Type definition for `ClientCreateElasticsearchDomain` `NodeToNodeEncryptionOptions`

    Specifies the NodeToNodeEncryptionOptions.

    - **Enabled** *(boolean) --*

      Specify true to enable node-to-node encryption.
    """


_ClientCreateElasticsearchDomainResponseDomainStatusCognitoOptionsTypeDef = TypedDict(
    "_ClientCreateElasticsearchDomainResponseDomainStatusCognitoOptionsTypeDef",
    {"Enabled": bool, "UserPoolId": str, "IdentityPoolId": str, "RoleArn": str},
    total=False,
)


class ClientCreateElasticsearchDomainResponseDomainStatusCognitoOptionsTypeDef(
    _ClientCreateElasticsearchDomainResponseDomainStatusCognitoOptionsTypeDef
):
    """
    Type definition for `ClientCreateElasticsearchDomainResponseDomainStatus` `CognitoOptions`

    The ``CognitoOptions`` for the specified domain. For more information, see `Amazon Cognito
    Authentication for Kibana
    <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-cognito-auth.html>`__
    .

    - **Enabled** *(boolean) --*

      Specifies the option to enable Cognito for Kibana authentication.

    - **UserPoolId** *(string) --*

      Specifies the Cognito user pool ID for Kibana authentication.

    - **IdentityPoolId** *(string) --*

      Specifies the Cognito identity pool ID for Kibana authentication.

    - **RoleArn** *(string) --*

      Specifies the role ARN that provides Elasticsearch permissions for accessing Cognito
      resources.
    """


_ClientCreateElasticsearchDomainResponseDomainStatusDomainEndpointOptionsTypeDef = TypedDict(
    "_ClientCreateElasticsearchDomainResponseDomainStatusDomainEndpointOptionsTypeDef",
    {"EnforceHTTPS": bool, "TLSSecurityPolicy": str},
    total=False,
)


class ClientCreateElasticsearchDomainResponseDomainStatusDomainEndpointOptionsTypeDef(
    _ClientCreateElasticsearchDomainResponseDomainStatusDomainEndpointOptionsTypeDef
):
    """
    Type definition for `ClientCreateElasticsearchDomainResponseDomainStatus` `DomainEndpointOptions`

    The current status of the Elasticsearch domain's endpoint options.

    - **EnforceHTTPS** *(boolean) --*

      Specify if only HTTPS endpoint should be enabled for the Elasticsearch domain.

    - **TLSSecurityPolicy** *(string) --*

      Specify the TLS security policy that needs to be applied to the HTTPS endpoint of
      Elasticsearch domain. It can be one of the following values:

      * **Policy-Min-TLS-1-0-2019-07:** TLS security policy which supports TLSv1.0 and higher.

      * **Policy-Min-TLS-1-2-2019-07:** TLS security policy which supports only TLSv1.2
    """


_ClientCreateElasticsearchDomainResponseDomainStatusEBSOptionsTypeDef = TypedDict(
    "_ClientCreateElasticsearchDomainResponseDomainStatusEBSOptionsTypeDef",
    {"EBSEnabled": bool, "VolumeType": str, "VolumeSize": int, "Iops": int},
    total=False,
)


class ClientCreateElasticsearchDomainResponseDomainStatusEBSOptionsTypeDef(
    _ClientCreateElasticsearchDomainResponseDomainStatusEBSOptionsTypeDef
):
    """
    Type definition for `ClientCreateElasticsearchDomainResponseDomainStatus` `EBSOptions`

    The ``EBSOptions`` for the specified domain. See `Configuring EBS-based Storage
    <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html#es-createdomain-configure-ebs>`__
    for more information.

    - **EBSEnabled** *(boolean) --*

      Specifies whether EBS-based storage is enabled.

    - **VolumeType** *(string) --*

      Specifies the volume type for EBS-based storage.

    - **VolumeSize** *(integer) --*

      Integer to specify the size of an EBS volume.

    - **Iops** *(integer) --*

      Specifies the IOPD for a Provisioned IOPS EBS volume (SSD).
    """


_ClientCreateElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigZoneAwarenessConfigTypeDef = TypedDict(
    "_ClientCreateElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigZoneAwarenessConfigTypeDef",
    {"AvailabilityZoneCount": int},
    total=False,
)


class ClientCreateElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigZoneAwarenessConfigTypeDef(
    _ClientCreateElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigZoneAwarenessConfigTypeDef
):
    """
    Type definition for `ClientCreateElasticsearchDomainResponseDomainStatusElasticsearchClusterConfig` `ZoneAwarenessConfig`

    Specifies the zone awareness configuration for a domain when zone awareness is enabled.

    - **AvailabilityZoneCount** *(integer) --*

      An integer value to indicate the number of availability zones for a domain when zone
      awareness is enabled. This should be equal to number of subnets if VPC endpoints is
      enabled
    """


_ClientCreateElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigTypeDef = TypedDict(
    "_ClientCreateElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigTypeDef",
    {
        "InstanceType": str,
        "InstanceCount": int,
        "DedicatedMasterEnabled": bool,
        "ZoneAwarenessEnabled": bool,
        "ZoneAwarenessConfig": ClientCreateElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigZoneAwarenessConfigTypeDef,
        "DedicatedMasterType": str,
        "DedicatedMasterCount": int,
    },
    total=False,
)


class ClientCreateElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigTypeDef(
    _ClientCreateElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigTypeDef
):
    """
    Type definition for `ClientCreateElasticsearchDomainResponseDomainStatus` `ElasticsearchClusterConfig`

    The type and number of instances in the domain cluster.

    - **InstanceType** *(string) --*

      The instance type for an Elasticsearch cluster.

    - **InstanceCount** *(integer) --*

      The number of instances in the specified domain cluster.

    - **DedicatedMasterEnabled** *(boolean) --*

      A boolean value to indicate whether a dedicated master node is enabled. See `About
      Dedicated Master Nodes
      <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains.html#es-managedomains-dedicatedmasternodes>`__
      for more information.

    - **ZoneAwarenessEnabled** *(boolean) --*

      A boolean value to indicate whether zone awareness is enabled. See `About Zone Awareness
      <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains.html#es-managedomains-zoneawareness>`__
      for more information.

    - **ZoneAwarenessConfig** *(dict) --*

      Specifies the zone awareness configuration for a domain when zone awareness is enabled.

      - **AvailabilityZoneCount** *(integer) --*

        An integer value to indicate the number of availability zones for a domain when zone
        awareness is enabled. This should be equal to number of subnets if VPC endpoints is
        enabled

    - **DedicatedMasterType** *(string) --*

      The instance type for a dedicated master node.

    - **DedicatedMasterCount** *(integer) --*

      Total number of dedicated master nodes, active and on standby, for the cluster.
    """


_ClientCreateElasticsearchDomainResponseDomainStatusEncryptionAtRestOptionsTypeDef = TypedDict(
    "_ClientCreateElasticsearchDomainResponseDomainStatusEncryptionAtRestOptionsTypeDef",
    {"Enabled": bool, "KmsKeyId": str},
    total=False,
)


class ClientCreateElasticsearchDomainResponseDomainStatusEncryptionAtRestOptionsTypeDef(
    _ClientCreateElasticsearchDomainResponseDomainStatusEncryptionAtRestOptionsTypeDef
):
    """
    Type definition for `ClientCreateElasticsearchDomainResponseDomainStatus` `EncryptionAtRestOptions`

    Specifies the status of the ``EncryptionAtRestOptions`` .

    - **Enabled** *(boolean) --*

      Specifies the option to enable Encryption At Rest.

    - **KmsKeyId** *(string) --*

      Specifies the KMS Key ID for Encryption At Rest options.
    """


_ClientCreateElasticsearchDomainResponseDomainStatusLogPublishingOptionsTypeDef = TypedDict(
    "_ClientCreateElasticsearchDomainResponseDomainStatusLogPublishingOptionsTypeDef",
    {"CloudWatchLogsLogGroupArn": str, "Enabled": bool},
    total=False,
)


class ClientCreateElasticsearchDomainResponseDomainStatusLogPublishingOptionsTypeDef(
    _ClientCreateElasticsearchDomainResponseDomainStatusLogPublishingOptionsTypeDef
):
    """
    Type definition for `ClientCreateElasticsearchDomainResponseDomainStatus` `LogPublishingOptions`

    Log Publishing option that is set for given domain. Attributes and their details:

    * CloudWatchLogsLogGroupArn: ARN of the Cloudwatch log group to which log needs to be
    published.

    * Enabled: Whether the log publishing for given log type is enabled or not

    - **CloudWatchLogsLogGroupArn** *(string) --*

      ARN of the Cloudwatch log group to which log needs to be published.

    - **Enabled** *(boolean) --*

      Specifies whether given log publishing option is enabled or not.
    """


_ClientCreateElasticsearchDomainResponseDomainStatusNodeToNodeEncryptionOptionsTypeDef = TypedDict(
    "_ClientCreateElasticsearchDomainResponseDomainStatusNodeToNodeEncryptionOptionsTypeDef",
    {"Enabled": bool},
    total=False,
)


class ClientCreateElasticsearchDomainResponseDomainStatusNodeToNodeEncryptionOptionsTypeDef(
    _ClientCreateElasticsearchDomainResponseDomainStatusNodeToNodeEncryptionOptionsTypeDef
):
    """
    Type definition for `ClientCreateElasticsearchDomainResponseDomainStatus` `NodeToNodeEncryptionOptions`

    Specifies the status of the ``NodeToNodeEncryptionOptions`` .

    - **Enabled** *(boolean) --*

      Specify true to enable node-to-node encryption.
    """


_ClientCreateElasticsearchDomainResponseDomainStatusServiceSoftwareOptionsTypeDef = TypedDict(
    "_ClientCreateElasticsearchDomainResponseDomainStatusServiceSoftwareOptionsTypeDef",
    {
        "CurrentVersion": str,
        "NewVersion": str,
        "UpdateAvailable": bool,
        "Cancellable": bool,
        "UpdateStatus": str,
        "Description": str,
        "AutomatedUpdateDate": datetime,
    },
    total=False,
)


class ClientCreateElasticsearchDomainResponseDomainStatusServiceSoftwareOptionsTypeDef(
    _ClientCreateElasticsearchDomainResponseDomainStatusServiceSoftwareOptionsTypeDef
):
    """
    Type definition for `ClientCreateElasticsearchDomainResponseDomainStatus` `ServiceSoftwareOptions`

    The current status of the Elasticsearch domain's service software.

    - **CurrentVersion** *(string) --*

      The current service software version that is present on the domain.

    - **NewVersion** *(string) --*

      The new service software version if one is available.

    - **UpdateAvailable** *(boolean) --*

      ``True`` if you are able to update you service software version. ``False`` if you are not
      able to update your service software version.

    - **Cancellable** *(boolean) --*

      ``True`` if you are able to cancel your service software version update. ``False`` if you
      are not able to cancel your service software version.

    - **UpdateStatus** *(string) --*

      The status of your service software update. This field can take the following values:
      ``ELIGIBLE`` , ``PENDING_UPDATE`` , ``IN_PROGRESS`` , ``COMPLETED`` , and
      ``NOT_ELIGIBLE`` .

    - **Description** *(string) --*

      The description of the ``UpdateStatus`` .

    - **AutomatedUpdateDate** *(datetime) --*

      Timestamp, in Epoch time, until which you can manually request a service software update.
      After this date, we automatically update your service software.
    """


_ClientCreateElasticsearchDomainResponseDomainStatusSnapshotOptionsTypeDef = TypedDict(
    "_ClientCreateElasticsearchDomainResponseDomainStatusSnapshotOptionsTypeDef",
    {"AutomatedSnapshotStartHour": int},
    total=False,
)


class ClientCreateElasticsearchDomainResponseDomainStatusSnapshotOptionsTypeDef(
    _ClientCreateElasticsearchDomainResponseDomainStatusSnapshotOptionsTypeDef
):
    """
    Type definition for `ClientCreateElasticsearchDomainResponseDomainStatus` `SnapshotOptions`

    Specifies the status of the ``SnapshotOptions``

    - **AutomatedSnapshotStartHour** *(integer) --*

      Specifies the time, in UTC format, when the service takes a daily automated snapshot of
      the specified Elasticsearch domain. Default value is ``0`` hours.
    """


_ClientCreateElasticsearchDomainResponseDomainStatusVPCOptionsTypeDef = TypedDict(
    "_ClientCreateElasticsearchDomainResponseDomainStatusVPCOptionsTypeDef",
    {
        "VPCId": str,
        "SubnetIds": List[str],
        "AvailabilityZones": List[str],
        "SecurityGroupIds": List[str],
    },
    total=False,
)


class ClientCreateElasticsearchDomainResponseDomainStatusVPCOptionsTypeDef(
    _ClientCreateElasticsearchDomainResponseDomainStatusVPCOptionsTypeDef
):
    """
    Type definition for `ClientCreateElasticsearchDomainResponseDomainStatus` `VPCOptions`

    The ``VPCOptions`` for the specified domain. For more information, see `VPC Endpoints for
    Amazon Elasticsearch Service Domains
    <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html>`__ .

    - **VPCId** *(string) --*

      The VPC Id for the Elasticsearch domain. Exists only if the domain was created with
      VPCOptions.

    - **SubnetIds** *(list) --*

      Specifies the subnets for VPC endpoint.

      - *(string) --*

    - **AvailabilityZones** *(list) --*

      The availability zones for the Elasticsearch domain. Exists only if the domain was
      created with VPCOptions.

      - *(string) --*

    - **SecurityGroupIds** *(list) --*

      Specifies the security groups for VPC endpoint.

      - *(string) --*
    """


_ClientCreateElasticsearchDomainResponseDomainStatusTypeDef = TypedDict(
    "_ClientCreateElasticsearchDomainResponseDomainStatusTypeDef",
    {
        "DomainId": str,
        "DomainName": str,
        "ARN": str,
        "Created": bool,
        "Deleted": bool,
        "Endpoint": str,
        "Endpoints": Dict[str, str],
        "Processing": bool,
        "UpgradeProcessing": bool,
        "ElasticsearchVersion": str,
        "ElasticsearchClusterConfig": ClientCreateElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigTypeDef,
        "EBSOptions": ClientCreateElasticsearchDomainResponseDomainStatusEBSOptionsTypeDef,
        "AccessPolicies": str,
        "SnapshotOptions": ClientCreateElasticsearchDomainResponseDomainStatusSnapshotOptionsTypeDef,
        "VPCOptions": ClientCreateElasticsearchDomainResponseDomainStatusVPCOptionsTypeDef,
        "CognitoOptions": ClientCreateElasticsearchDomainResponseDomainStatusCognitoOptionsTypeDef,
        "EncryptionAtRestOptions": ClientCreateElasticsearchDomainResponseDomainStatusEncryptionAtRestOptionsTypeDef,
        "NodeToNodeEncryptionOptions": ClientCreateElasticsearchDomainResponseDomainStatusNodeToNodeEncryptionOptionsTypeDef,
        "AdvancedOptions": Dict[str, str],
        "LogPublishingOptions": Dict[
            str,
            ClientCreateElasticsearchDomainResponseDomainStatusLogPublishingOptionsTypeDef,
        ],
        "ServiceSoftwareOptions": ClientCreateElasticsearchDomainResponseDomainStatusServiceSoftwareOptionsTypeDef,
        "DomainEndpointOptions": ClientCreateElasticsearchDomainResponseDomainStatusDomainEndpointOptionsTypeDef,
    },
    total=False,
)


class ClientCreateElasticsearchDomainResponseDomainStatusTypeDef(
    _ClientCreateElasticsearchDomainResponseDomainStatusTypeDef
):
    """
    Type definition for `ClientCreateElasticsearchDomainResponse` `DomainStatus`

    The status of the newly created Elasticsearch domain.

    - **DomainId** *(string) --*

      The unique identifier for the specified Elasticsearch domain.

    - **DomainName** *(string) --*

      The name of an Elasticsearch domain. Domain names are unique across the domains owned by an
      account within an AWS region. Domain names start with a letter or number and can contain
      the following characters: a-z (lowercase), 0-9, and - (hyphen).

    - **ARN** *(string) --*

      The Amazon resource name (ARN) of an Elasticsearch domain. See `Identifiers for IAM
      Entities
      <http://docs.aws.amazon.com/IAM/latest/UserGuide/index.html?Using_Identifiers.html>`__ in
      *Using AWS Identity and Access Management* for more information.

    - **Created** *(boolean) --*

      The domain creation status. ``True`` if the creation of an Elasticsearch domain is
      complete. ``False`` if domain creation is still in progress.

    - **Deleted** *(boolean) --*

      The domain deletion status. ``True`` if a delete request has been received for the domain
      but resource cleanup is still in progress. ``False`` if the domain has not been deleted.
      Once domain deletion is complete, the status of the domain is no longer returned.

    - **Endpoint** *(string) --*

      The Elasticsearch domain endpoint that you use to submit index and search requests.

    - **Endpoints** *(dict) --*

      Map containing the Elasticsearch domain endpoints used to submit index and search requests.
      Example ``key, value`` :
      ``'vpc','vpc-endpoint-h2dsd34efgyghrtguk5gt6j2foh4.us-east-1.es.amazonaws.com'`` .

      - *(string) --*

        - *(string) --*

          The endpoint to which service requests are submitted. For example,
          ``search-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.es.amazonaws.com`` or
          ``doc-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.es.amazonaws.com`` .

    - **Processing** *(boolean) --*

      The status of the Elasticsearch domain configuration. ``True`` if Amazon Elasticsearch
      Service is processing configuration changes. ``False`` if the configuration is active.

    - **UpgradeProcessing** *(boolean) --*

      The status of an Elasticsearch domain version upgrade. ``True`` if Amazon Elasticsearch
      Service is undergoing a version upgrade. ``False`` if the configuration is active.

    - **ElasticsearchVersion** *(string) --*

    - **ElasticsearchClusterConfig** *(dict) --*

      The type and number of instances in the domain cluster.

      - **InstanceType** *(string) --*

        The instance type for an Elasticsearch cluster.

      - **InstanceCount** *(integer) --*

        The number of instances in the specified domain cluster.

      - **DedicatedMasterEnabled** *(boolean) --*

        A boolean value to indicate whether a dedicated master node is enabled. See `About
        Dedicated Master Nodes
        <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains.html#es-managedomains-dedicatedmasternodes>`__
        for more information.

      - **ZoneAwarenessEnabled** *(boolean) --*

        A boolean value to indicate whether zone awareness is enabled. See `About Zone Awareness
        <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains.html#es-managedomains-zoneawareness>`__
        for more information.

      - **ZoneAwarenessConfig** *(dict) --*

        Specifies the zone awareness configuration for a domain when zone awareness is enabled.

        - **AvailabilityZoneCount** *(integer) --*

          An integer value to indicate the number of availability zones for a domain when zone
          awareness is enabled. This should be equal to number of subnets if VPC endpoints is
          enabled

      - **DedicatedMasterType** *(string) --*

        The instance type for a dedicated master node.

      - **DedicatedMasterCount** *(integer) --*

        Total number of dedicated master nodes, active and on standby, for the cluster.

    - **EBSOptions** *(dict) --*

      The ``EBSOptions`` for the specified domain. See `Configuring EBS-based Storage
      <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html#es-createdomain-configure-ebs>`__
      for more information.

      - **EBSEnabled** *(boolean) --*

        Specifies whether EBS-based storage is enabled.

      - **VolumeType** *(string) --*

        Specifies the volume type for EBS-based storage.

      - **VolumeSize** *(integer) --*

        Integer to specify the size of an EBS volume.

      - **Iops** *(integer) --*

        Specifies the IOPD for a Provisioned IOPS EBS volume (SSD).

    - **AccessPolicies** *(string) --*

      IAM access policy as a JSON-formatted string.

    - **SnapshotOptions** *(dict) --*

      Specifies the status of the ``SnapshotOptions``

      - **AutomatedSnapshotStartHour** *(integer) --*

        Specifies the time, in UTC format, when the service takes a daily automated snapshot of
        the specified Elasticsearch domain. Default value is ``0`` hours.

    - **VPCOptions** *(dict) --*

      The ``VPCOptions`` for the specified domain. For more information, see `VPC Endpoints for
      Amazon Elasticsearch Service Domains
      <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html>`__ .

      - **VPCId** *(string) --*

        The VPC Id for the Elasticsearch domain. Exists only if the domain was created with
        VPCOptions.

      - **SubnetIds** *(list) --*

        Specifies the subnets for VPC endpoint.

        - *(string) --*

      - **AvailabilityZones** *(list) --*

        The availability zones for the Elasticsearch domain. Exists only if the domain was
        created with VPCOptions.

        - *(string) --*

      - **SecurityGroupIds** *(list) --*

        Specifies the security groups for VPC endpoint.

        - *(string) --*

    - **CognitoOptions** *(dict) --*

      The ``CognitoOptions`` for the specified domain. For more information, see `Amazon Cognito
      Authentication for Kibana
      <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-cognito-auth.html>`__
      .

      - **Enabled** *(boolean) --*

        Specifies the option to enable Cognito for Kibana authentication.

      - **UserPoolId** *(string) --*

        Specifies the Cognito user pool ID for Kibana authentication.

      - **IdentityPoolId** *(string) --*

        Specifies the Cognito identity pool ID for Kibana authentication.

      - **RoleArn** *(string) --*

        Specifies the role ARN that provides Elasticsearch permissions for accessing Cognito
        resources.

    - **EncryptionAtRestOptions** *(dict) --*

      Specifies the status of the ``EncryptionAtRestOptions`` .

      - **Enabled** *(boolean) --*

        Specifies the option to enable Encryption At Rest.

      - **KmsKeyId** *(string) --*

        Specifies the KMS Key ID for Encryption At Rest options.

    - **NodeToNodeEncryptionOptions** *(dict) --*

      Specifies the status of the ``NodeToNodeEncryptionOptions`` .

      - **Enabled** *(boolean) --*

        Specify true to enable node-to-node encryption.

    - **AdvancedOptions** *(dict) --*

      Specifies the status of the ``AdvancedOptions``

      - *(string) --*

        - *(string) --*

    - **LogPublishingOptions** *(dict) --*

      Log publishing options for the given domain.

      - *(string) --*

        Type of Log File, it can be one of the following:

        * INDEX_SLOW_LOGS: Index slow logs contain insert requests that took more time than
        configured index query log threshold to execute.

        * SEARCH_SLOW_LOGS: Search slow logs contain search queries that took more time than
        configured search query log threshold to execute.

        * ES_APPLICATION_LOGS: Elasticsearch application logs contain information about errors
        and warnings raised during the operation of the service and can be useful for
        troubleshooting.

        - *(dict) --*

          Log Publishing option that is set for given domain. Attributes and their details:

          * CloudWatchLogsLogGroupArn: ARN of the Cloudwatch log group to which log needs to be
          published.

          * Enabled: Whether the log publishing for given log type is enabled or not

          - **CloudWatchLogsLogGroupArn** *(string) --*

            ARN of the Cloudwatch log group to which log needs to be published.

          - **Enabled** *(boolean) --*

            Specifies whether given log publishing option is enabled or not.

    - **ServiceSoftwareOptions** *(dict) --*

      The current status of the Elasticsearch domain's service software.

      - **CurrentVersion** *(string) --*

        The current service software version that is present on the domain.

      - **NewVersion** *(string) --*

        The new service software version if one is available.

      - **UpdateAvailable** *(boolean) --*

        ``True`` if you are able to update you service software version. ``False`` if you are not
        able to update your service software version.

      - **Cancellable** *(boolean) --*

        ``True`` if you are able to cancel your service software version update. ``False`` if you
        are not able to cancel your service software version.

      - **UpdateStatus** *(string) --*

        The status of your service software update. This field can take the following values:
        ``ELIGIBLE`` , ``PENDING_UPDATE`` , ``IN_PROGRESS`` , ``COMPLETED`` , and
        ``NOT_ELIGIBLE`` .

      - **Description** *(string) --*

        The description of the ``UpdateStatus`` .

      - **AutomatedUpdateDate** *(datetime) --*

        Timestamp, in Epoch time, until which you can manually request a service software update.
        After this date, we automatically update your service software.

    - **DomainEndpointOptions** *(dict) --*

      The current status of the Elasticsearch domain's endpoint options.

      - **EnforceHTTPS** *(boolean) --*

        Specify if only HTTPS endpoint should be enabled for the Elasticsearch domain.

      - **TLSSecurityPolicy** *(string) --*

        Specify the TLS security policy that needs to be applied to the HTTPS endpoint of
        Elasticsearch domain. It can be one of the following values:

        * **Policy-Min-TLS-1-0-2019-07:** TLS security policy which supports TLSv1.0 and higher.

        * **Policy-Min-TLS-1-2-2019-07:** TLS security policy which supports only TLSv1.2
    """


_ClientCreateElasticsearchDomainResponseTypeDef = TypedDict(
    "_ClientCreateElasticsearchDomainResponseTypeDef",
    {"DomainStatus": ClientCreateElasticsearchDomainResponseDomainStatusTypeDef},
    total=False,
)


class ClientCreateElasticsearchDomainResponseTypeDef(
    _ClientCreateElasticsearchDomainResponseTypeDef
):
    """
    Type definition for `ClientCreateElasticsearchDomain` `Response`

    The result of a ``CreateElasticsearchDomain`` operation. Contains the status of the newly
    created Elasticsearch domain.

    - **DomainStatus** *(dict) --*

      The status of the newly created Elasticsearch domain.

      - **DomainId** *(string) --*

        The unique identifier for the specified Elasticsearch domain.

      - **DomainName** *(string) --*

        The name of an Elasticsearch domain. Domain names are unique across the domains owned by an
        account within an AWS region. Domain names start with a letter or number and can contain
        the following characters: a-z (lowercase), 0-9, and - (hyphen).

      - **ARN** *(string) --*

        The Amazon resource name (ARN) of an Elasticsearch domain. See `Identifiers for IAM
        Entities
        <http://docs.aws.amazon.com/IAM/latest/UserGuide/index.html?Using_Identifiers.html>`__ in
        *Using AWS Identity and Access Management* for more information.

      - **Created** *(boolean) --*

        The domain creation status. ``True`` if the creation of an Elasticsearch domain is
        complete. ``False`` if domain creation is still in progress.

      - **Deleted** *(boolean) --*

        The domain deletion status. ``True`` if a delete request has been received for the domain
        but resource cleanup is still in progress. ``False`` if the domain has not been deleted.
        Once domain deletion is complete, the status of the domain is no longer returned.

      - **Endpoint** *(string) --*

        The Elasticsearch domain endpoint that you use to submit index and search requests.

      - **Endpoints** *(dict) --*

        Map containing the Elasticsearch domain endpoints used to submit index and search requests.
        Example ``key, value`` :
        ``'vpc','vpc-endpoint-h2dsd34efgyghrtguk5gt6j2foh4.us-east-1.es.amazonaws.com'`` .

        - *(string) --*

          - *(string) --*

            The endpoint to which service requests are submitted. For example,
            ``search-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.es.amazonaws.com`` or
            ``doc-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.es.amazonaws.com`` .

      - **Processing** *(boolean) --*

        The status of the Elasticsearch domain configuration. ``True`` if Amazon Elasticsearch
        Service is processing configuration changes. ``False`` if the configuration is active.

      - **UpgradeProcessing** *(boolean) --*

        The status of an Elasticsearch domain version upgrade. ``True`` if Amazon Elasticsearch
        Service is undergoing a version upgrade. ``False`` if the configuration is active.

      - **ElasticsearchVersion** *(string) --*

      - **ElasticsearchClusterConfig** *(dict) --*

        The type and number of instances in the domain cluster.

        - **InstanceType** *(string) --*

          The instance type for an Elasticsearch cluster.

        - **InstanceCount** *(integer) --*

          The number of instances in the specified domain cluster.

        - **DedicatedMasterEnabled** *(boolean) --*

          A boolean value to indicate whether a dedicated master node is enabled. See `About
          Dedicated Master Nodes
          <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains.html#es-managedomains-dedicatedmasternodes>`__
          for more information.

        - **ZoneAwarenessEnabled** *(boolean) --*

          A boolean value to indicate whether zone awareness is enabled. See `About Zone Awareness
          <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains.html#es-managedomains-zoneawareness>`__
          for more information.

        - **ZoneAwarenessConfig** *(dict) --*

          Specifies the zone awareness configuration for a domain when zone awareness is enabled.

          - **AvailabilityZoneCount** *(integer) --*

            An integer value to indicate the number of availability zones for a domain when zone
            awareness is enabled. This should be equal to number of subnets if VPC endpoints is
            enabled

        - **DedicatedMasterType** *(string) --*

          The instance type for a dedicated master node.

        - **DedicatedMasterCount** *(integer) --*

          Total number of dedicated master nodes, active and on standby, for the cluster.

      - **EBSOptions** *(dict) --*

        The ``EBSOptions`` for the specified domain. See `Configuring EBS-based Storage
        <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html#es-createdomain-configure-ebs>`__
        for more information.

        - **EBSEnabled** *(boolean) --*

          Specifies whether EBS-based storage is enabled.

        - **VolumeType** *(string) --*

          Specifies the volume type for EBS-based storage.

        - **VolumeSize** *(integer) --*

          Integer to specify the size of an EBS volume.

        - **Iops** *(integer) --*

          Specifies the IOPD for a Provisioned IOPS EBS volume (SSD).

      - **AccessPolicies** *(string) --*

        IAM access policy as a JSON-formatted string.

      - **SnapshotOptions** *(dict) --*

        Specifies the status of the ``SnapshotOptions``

        - **AutomatedSnapshotStartHour** *(integer) --*

          Specifies the time, in UTC format, when the service takes a daily automated snapshot of
          the specified Elasticsearch domain. Default value is ``0`` hours.

      - **VPCOptions** *(dict) --*

        The ``VPCOptions`` for the specified domain. For more information, see `VPC Endpoints for
        Amazon Elasticsearch Service Domains
        <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html>`__ .

        - **VPCId** *(string) --*

          The VPC Id for the Elasticsearch domain. Exists only if the domain was created with
          VPCOptions.

        - **SubnetIds** *(list) --*

          Specifies the subnets for VPC endpoint.

          - *(string) --*

        - **AvailabilityZones** *(list) --*

          The availability zones for the Elasticsearch domain. Exists only if the domain was
          created with VPCOptions.

          - *(string) --*

        - **SecurityGroupIds** *(list) --*

          Specifies the security groups for VPC endpoint.

          - *(string) --*

      - **CognitoOptions** *(dict) --*

        The ``CognitoOptions`` for the specified domain. For more information, see `Amazon Cognito
        Authentication for Kibana
        <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-cognito-auth.html>`__
        .

        - **Enabled** *(boolean) --*

          Specifies the option to enable Cognito for Kibana authentication.

        - **UserPoolId** *(string) --*

          Specifies the Cognito user pool ID for Kibana authentication.

        - **IdentityPoolId** *(string) --*

          Specifies the Cognito identity pool ID for Kibana authentication.

        - **RoleArn** *(string) --*

          Specifies the role ARN that provides Elasticsearch permissions for accessing Cognito
          resources.

      - **EncryptionAtRestOptions** *(dict) --*

        Specifies the status of the ``EncryptionAtRestOptions`` .

        - **Enabled** *(boolean) --*

          Specifies the option to enable Encryption At Rest.

        - **KmsKeyId** *(string) --*

          Specifies the KMS Key ID for Encryption At Rest options.

      - **NodeToNodeEncryptionOptions** *(dict) --*

        Specifies the status of the ``NodeToNodeEncryptionOptions`` .

        - **Enabled** *(boolean) --*

          Specify true to enable node-to-node encryption.

      - **AdvancedOptions** *(dict) --*

        Specifies the status of the ``AdvancedOptions``

        - *(string) --*

          - *(string) --*

      - **LogPublishingOptions** *(dict) --*

        Log publishing options for the given domain.

        - *(string) --*

          Type of Log File, it can be one of the following:

          * INDEX_SLOW_LOGS: Index slow logs contain insert requests that took more time than
          configured index query log threshold to execute.

          * SEARCH_SLOW_LOGS: Search slow logs contain search queries that took more time than
          configured search query log threshold to execute.

          * ES_APPLICATION_LOGS: Elasticsearch application logs contain information about errors
          and warnings raised during the operation of the service and can be useful for
          troubleshooting.

          - *(dict) --*

            Log Publishing option that is set for given domain. Attributes and their details:

            * CloudWatchLogsLogGroupArn: ARN of the Cloudwatch log group to which log needs to be
            published.

            * Enabled: Whether the log publishing for given log type is enabled or not

            - **CloudWatchLogsLogGroupArn** *(string) --*

              ARN of the Cloudwatch log group to which log needs to be published.

            - **Enabled** *(boolean) --*

              Specifies whether given log publishing option is enabled or not.

      - **ServiceSoftwareOptions** *(dict) --*

        The current status of the Elasticsearch domain's service software.

        - **CurrentVersion** *(string) --*

          The current service software version that is present on the domain.

        - **NewVersion** *(string) --*

          The new service software version if one is available.

        - **UpdateAvailable** *(boolean) --*

          ``True`` if you are able to update you service software version. ``False`` if you are not
          able to update your service software version.

        - **Cancellable** *(boolean) --*

          ``True`` if you are able to cancel your service software version update. ``False`` if you
          are not able to cancel your service software version.

        - **UpdateStatus** *(string) --*

          The status of your service software update. This field can take the following values:
          ``ELIGIBLE`` , ``PENDING_UPDATE`` , ``IN_PROGRESS`` , ``COMPLETED`` , and
          ``NOT_ELIGIBLE`` .

        - **Description** *(string) --*

          The description of the ``UpdateStatus`` .

        - **AutomatedUpdateDate** *(datetime) --*

          Timestamp, in Epoch time, until which you can manually request a service software update.
          After this date, we automatically update your service software.

      - **DomainEndpointOptions** *(dict) --*

        The current status of the Elasticsearch domain's endpoint options.

        - **EnforceHTTPS** *(boolean) --*

          Specify if only HTTPS endpoint should be enabled for the Elasticsearch domain.

        - **TLSSecurityPolicy** *(string) --*

          Specify the TLS security policy that needs to be applied to the HTTPS endpoint of
          Elasticsearch domain. It can be one of the following values:

          * **Policy-Min-TLS-1-0-2019-07:** TLS security policy which supports TLSv1.0 and higher.

          * **Policy-Min-TLS-1-2-2019-07:** TLS security policy which supports only TLSv1.2
    """


_ClientCreateElasticsearchDomainSnapshotOptionsTypeDef = TypedDict(
    "_ClientCreateElasticsearchDomainSnapshotOptionsTypeDef",
    {"AutomatedSnapshotStartHour": int},
    total=False,
)


class ClientCreateElasticsearchDomainSnapshotOptionsTypeDef(
    _ClientCreateElasticsearchDomainSnapshotOptionsTypeDef
):
    """
    Type definition for `ClientCreateElasticsearchDomain` `SnapshotOptions`

    Option to set time, in UTC format, of the daily automated snapshot. Default value is 0 hours.

    - **AutomatedSnapshotStartHour** *(integer) --*

      Specifies the time, in UTC format, when the service takes a daily automated snapshot of the
      specified Elasticsearch domain. Default value is ``0`` hours.
    """


_ClientCreateElasticsearchDomainVPCOptionsTypeDef = TypedDict(
    "_ClientCreateElasticsearchDomainVPCOptionsTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str]},
    total=False,
)


class ClientCreateElasticsearchDomainVPCOptionsTypeDef(
    _ClientCreateElasticsearchDomainVPCOptionsTypeDef
):
    """
    Type definition for `ClientCreateElasticsearchDomain` `VPCOptions`

    Options to specify the subnets and security groups for VPC endpoint. For more information, see
    `Creating a VPC
    <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html#es-creating-vpc>`__
    in *VPC Endpoints for Amazon Elasticsearch Service Domains*

    - **SubnetIds** *(list) --*

      Specifies the subnets for VPC endpoint.

      - *(string) --*

    - **SecurityGroupIds** *(list) --*

      Specifies the security groups for VPC endpoint.

      - *(string) --*
    """


_ClientDeleteElasticsearchDomainResponseDomainStatusCognitoOptionsTypeDef = TypedDict(
    "_ClientDeleteElasticsearchDomainResponseDomainStatusCognitoOptionsTypeDef",
    {"Enabled": bool, "UserPoolId": str, "IdentityPoolId": str, "RoleArn": str},
    total=False,
)


class ClientDeleteElasticsearchDomainResponseDomainStatusCognitoOptionsTypeDef(
    _ClientDeleteElasticsearchDomainResponseDomainStatusCognitoOptionsTypeDef
):
    """
    Type definition for `ClientDeleteElasticsearchDomainResponseDomainStatus` `CognitoOptions`

    The ``CognitoOptions`` for the specified domain. For more information, see `Amazon Cognito
    Authentication for Kibana
    <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-cognito-auth.html>`__
    .

    - **Enabled** *(boolean) --*

      Specifies the option to enable Cognito for Kibana authentication.

    - **UserPoolId** *(string) --*

      Specifies the Cognito user pool ID for Kibana authentication.

    - **IdentityPoolId** *(string) --*

      Specifies the Cognito identity pool ID for Kibana authentication.

    - **RoleArn** *(string) --*

      Specifies the role ARN that provides Elasticsearch permissions for accessing Cognito
      resources.
    """


_ClientDeleteElasticsearchDomainResponseDomainStatusDomainEndpointOptionsTypeDef = TypedDict(
    "_ClientDeleteElasticsearchDomainResponseDomainStatusDomainEndpointOptionsTypeDef",
    {"EnforceHTTPS": bool, "TLSSecurityPolicy": str},
    total=False,
)


class ClientDeleteElasticsearchDomainResponseDomainStatusDomainEndpointOptionsTypeDef(
    _ClientDeleteElasticsearchDomainResponseDomainStatusDomainEndpointOptionsTypeDef
):
    """
    Type definition for `ClientDeleteElasticsearchDomainResponseDomainStatus` `DomainEndpointOptions`

    The current status of the Elasticsearch domain's endpoint options.

    - **EnforceHTTPS** *(boolean) --*

      Specify if only HTTPS endpoint should be enabled for the Elasticsearch domain.

    - **TLSSecurityPolicy** *(string) --*

      Specify the TLS security policy that needs to be applied to the HTTPS endpoint of
      Elasticsearch domain. It can be one of the following values:

      * **Policy-Min-TLS-1-0-2019-07:** TLS security policy which supports TLSv1.0 and higher.

      * **Policy-Min-TLS-1-2-2019-07:** TLS security policy which supports only TLSv1.2
    """


_ClientDeleteElasticsearchDomainResponseDomainStatusEBSOptionsTypeDef = TypedDict(
    "_ClientDeleteElasticsearchDomainResponseDomainStatusEBSOptionsTypeDef",
    {"EBSEnabled": bool, "VolumeType": str, "VolumeSize": int, "Iops": int},
    total=False,
)


class ClientDeleteElasticsearchDomainResponseDomainStatusEBSOptionsTypeDef(
    _ClientDeleteElasticsearchDomainResponseDomainStatusEBSOptionsTypeDef
):
    """
    Type definition for `ClientDeleteElasticsearchDomainResponseDomainStatus` `EBSOptions`

    The ``EBSOptions`` for the specified domain. See `Configuring EBS-based Storage
    <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html#es-createdomain-configure-ebs>`__
    for more information.

    - **EBSEnabled** *(boolean) --*

      Specifies whether EBS-based storage is enabled.

    - **VolumeType** *(string) --*

      Specifies the volume type for EBS-based storage.

    - **VolumeSize** *(integer) --*

      Integer to specify the size of an EBS volume.

    - **Iops** *(integer) --*

      Specifies the IOPD for a Provisioned IOPS EBS volume (SSD).
    """


_ClientDeleteElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigZoneAwarenessConfigTypeDef = TypedDict(
    "_ClientDeleteElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigZoneAwarenessConfigTypeDef",
    {"AvailabilityZoneCount": int},
    total=False,
)


class ClientDeleteElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigZoneAwarenessConfigTypeDef(
    _ClientDeleteElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigZoneAwarenessConfigTypeDef
):
    """
    Type definition for `ClientDeleteElasticsearchDomainResponseDomainStatusElasticsearchClusterConfig` `ZoneAwarenessConfig`

    Specifies the zone awareness configuration for a domain when zone awareness is enabled.

    - **AvailabilityZoneCount** *(integer) --*

      An integer value to indicate the number of availability zones for a domain when zone
      awareness is enabled. This should be equal to number of subnets if VPC endpoints is
      enabled
    """


_ClientDeleteElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigTypeDef = TypedDict(
    "_ClientDeleteElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigTypeDef",
    {
        "InstanceType": str,
        "InstanceCount": int,
        "DedicatedMasterEnabled": bool,
        "ZoneAwarenessEnabled": bool,
        "ZoneAwarenessConfig": ClientDeleteElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigZoneAwarenessConfigTypeDef,
        "DedicatedMasterType": str,
        "DedicatedMasterCount": int,
    },
    total=False,
)


class ClientDeleteElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigTypeDef(
    _ClientDeleteElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigTypeDef
):
    """
    Type definition for `ClientDeleteElasticsearchDomainResponseDomainStatus` `ElasticsearchClusterConfig`

    The type and number of instances in the domain cluster.

    - **InstanceType** *(string) --*

      The instance type for an Elasticsearch cluster.

    - **InstanceCount** *(integer) --*

      The number of instances in the specified domain cluster.

    - **DedicatedMasterEnabled** *(boolean) --*

      A boolean value to indicate whether a dedicated master node is enabled. See `About
      Dedicated Master Nodes
      <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains.html#es-managedomains-dedicatedmasternodes>`__
      for more information.

    - **ZoneAwarenessEnabled** *(boolean) --*

      A boolean value to indicate whether zone awareness is enabled. See `About Zone Awareness
      <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains.html#es-managedomains-zoneawareness>`__
      for more information.

    - **ZoneAwarenessConfig** *(dict) --*

      Specifies the zone awareness configuration for a domain when zone awareness is enabled.

      - **AvailabilityZoneCount** *(integer) --*

        An integer value to indicate the number of availability zones for a domain when zone
        awareness is enabled. This should be equal to number of subnets if VPC endpoints is
        enabled

    - **DedicatedMasterType** *(string) --*

      The instance type for a dedicated master node.

    - **DedicatedMasterCount** *(integer) --*

      Total number of dedicated master nodes, active and on standby, for the cluster.
    """


_ClientDeleteElasticsearchDomainResponseDomainStatusEncryptionAtRestOptionsTypeDef = TypedDict(
    "_ClientDeleteElasticsearchDomainResponseDomainStatusEncryptionAtRestOptionsTypeDef",
    {"Enabled": bool, "KmsKeyId": str},
    total=False,
)


class ClientDeleteElasticsearchDomainResponseDomainStatusEncryptionAtRestOptionsTypeDef(
    _ClientDeleteElasticsearchDomainResponseDomainStatusEncryptionAtRestOptionsTypeDef
):
    """
    Type definition for `ClientDeleteElasticsearchDomainResponseDomainStatus` `EncryptionAtRestOptions`

    Specifies the status of the ``EncryptionAtRestOptions`` .

    - **Enabled** *(boolean) --*

      Specifies the option to enable Encryption At Rest.

    - **KmsKeyId** *(string) --*

      Specifies the KMS Key ID for Encryption At Rest options.
    """


_ClientDeleteElasticsearchDomainResponseDomainStatusLogPublishingOptionsTypeDef = TypedDict(
    "_ClientDeleteElasticsearchDomainResponseDomainStatusLogPublishingOptionsTypeDef",
    {"CloudWatchLogsLogGroupArn": str, "Enabled": bool},
    total=False,
)


class ClientDeleteElasticsearchDomainResponseDomainStatusLogPublishingOptionsTypeDef(
    _ClientDeleteElasticsearchDomainResponseDomainStatusLogPublishingOptionsTypeDef
):
    """
    Type definition for `ClientDeleteElasticsearchDomainResponseDomainStatus` `LogPublishingOptions`

    Log Publishing option that is set for given domain. Attributes and their details:

    * CloudWatchLogsLogGroupArn: ARN of the Cloudwatch log group to which log needs to be
    published.

    * Enabled: Whether the log publishing for given log type is enabled or not

    - **CloudWatchLogsLogGroupArn** *(string) --*

      ARN of the Cloudwatch log group to which log needs to be published.

    - **Enabled** *(boolean) --*

      Specifies whether given log publishing option is enabled or not.
    """


_ClientDeleteElasticsearchDomainResponseDomainStatusNodeToNodeEncryptionOptionsTypeDef = TypedDict(
    "_ClientDeleteElasticsearchDomainResponseDomainStatusNodeToNodeEncryptionOptionsTypeDef",
    {"Enabled": bool},
    total=False,
)


class ClientDeleteElasticsearchDomainResponseDomainStatusNodeToNodeEncryptionOptionsTypeDef(
    _ClientDeleteElasticsearchDomainResponseDomainStatusNodeToNodeEncryptionOptionsTypeDef
):
    """
    Type definition for `ClientDeleteElasticsearchDomainResponseDomainStatus` `NodeToNodeEncryptionOptions`

    Specifies the status of the ``NodeToNodeEncryptionOptions`` .

    - **Enabled** *(boolean) --*

      Specify true to enable node-to-node encryption.
    """


_ClientDeleteElasticsearchDomainResponseDomainStatusServiceSoftwareOptionsTypeDef = TypedDict(
    "_ClientDeleteElasticsearchDomainResponseDomainStatusServiceSoftwareOptionsTypeDef",
    {
        "CurrentVersion": str,
        "NewVersion": str,
        "UpdateAvailable": bool,
        "Cancellable": bool,
        "UpdateStatus": str,
        "Description": str,
        "AutomatedUpdateDate": datetime,
    },
    total=False,
)


class ClientDeleteElasticsearchDomainResponseDomainStatusServiceSoftwareOptionsTypeDef(
    _ClientDeleteElasticsearchDomainResponseDomainStatusServiceSoftwareOptionsTypeDef
):
    """
    Type definition for `ClientDeleteElasticsearchDomainResponseDomainStatus` `ServiceSoftwareOptions`

    The current status of the Elasticsearch domain's service software.

    - **CurrentVersion** *(string) --*

      The current service software version that is present on the domain.

    - **NewVersion** *(string) --*

      The new service software version if one is available.

    - **UpdateAvailable** *(boolean) --*

      ``True`` if you are able to update you service software version. ``False`` if you are not
      able to update your service software version.

    - **Cancellable** *(boolean) --*

      ``True`` if you are able to cancel your service software version update. ``False`` if you
      are not able to cancel your service software version.

    - **UpdateStatus** *(string) --*

      The status of your service software update. This field can take the following values:
      ``ELIGIBLE`` , ``PENDING_UPDATE`` , ``IN_PROGRESS`` , ``COMPLETED`` , and
      ``NOT_ELIGIBLE`` .

    - **Description** *(string) --*

      The description of the ``UpdateStatus`` .

    - **AutomatedUpdateDate** *(datetime) --*

      Timestamp, in Epoch time, until which you can manually request a service software update.
      After this date, we automatically update your service software.
    """


_ClientDeleteElasticsearchDomainResponseDomainStatusSnapshotOptionsTypeDef = TypedDict(
    "_ClientDeleteElasticsearchDomainResponseDomainStatusSnapshotOptionsTypeDef",
    {"AutomatedSnapshotStartHour": int},
    total=False,
)


class ClientDeleteElasticsearchDomainResponseDomainStatusSnapshotOptionsTypeDef(
    _ClientDeleteElasticsearchDomainResponseDomainStatusSnapshotOptionsTypeDef
):
    """
    Type definition for `ClientDeleteElasticsearchDomainResponseDomainStatus` `SnapshotOptions`

    Specifies the status of the ``SnapshotOptions``

    - **AutomatedSnapshotStartHour** *(integer) --*

      Specifies the time, in UTC format, when the service takes a daily automated snapshot of
      the specified Elasticsearch domain. Default value is ``0`` hours.
    """


_ClientDeleteElasticsearchDomainResponseDomainStatusVPCOptionsTypeDef = TypedDict(
    "_ClientDeleteElasticsearchDomainResponseDomainStatusVPCOptionsTypeDef",
    {
        "VPCId": str,
        "SubnetIds": List[str],
        "AvailabilityZones": List[str],
        "SecurityGroupIds": List[str],
    },
    total=False,
)


class ClientDeleteElasticsearchDomainResponseDomainStatusVPCOptionsTypeDef(
    _ClientDeleteElasticsearchDomainResponseDomainStatusVPCOptionsTypeDef
):
    """
    Type definition for `ClientDeleteElasticsearchDomainResponseDomainStatus` `VPCOptions`

    The ``VPCOptions`` for the specified domain. For more information, see `VPC Endpoints for
    Amazon Elasticsearch Service Domains
    <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html>`__ .

    - **VPCId** *(string) --*

      The VPC Id for the Elasticsearch domain. Exists only if the domain was created with
      VPCOptions.

    - **SubnetIds** *(list) --*

      Specifies the subnets for VPC endpoint.

      - *(string) --*

    - **AvailabilityZones** *(list) --*

      The availability zones for the Elasticsearch domain. Exists only if the domain was
      created with VPCOptions.

      - *(string) --*

    - **SecurityGroupIds** *(list) --*

      Specifies the security groups for VPC endpoint.

      - *(string) --*
    """


_ClientDeleteElasticsearchDomainResponseDomainStatusTypeDef = TypedDict(
    "_ClientDeleteElasticsearchDomainResponseDomainStatusTypeDef",
    {
        "DomainId": str,
        "DomainName": str,
        "ARN": str,
        "Created": bool,
        "Deleted": bool,
        "Endpoint": str,
        "Endpoints": Dict[str, str],
        "Processing": bool,
        "UpgradeProcessing": bool,
        "ElasticsearchVersion": str,
        "ElasticsearchClusterConfig": ClientDeleteElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigTypeDef,
        "EBSOptions": ClientDeleteElasticsearchDomainResponseDomainStatusEBSOptionsTypeDef,
        "AccessPolicies": str,
        "SnapshotOptions": ClientDeleteElasticsearchDomainResponseDomainStatusSnapshotOptionsTypeDef,
        "VPCOptions": ClientDeleteElasticsearchDomainResponseDomainStatusVPCOptionsTypeDef,
        "CognitoOptions": ClientDeleteElasticsearchDomainResponseDomainStatusCognitoOptionsTypeDef,
        "EncryptionAtRestOptions": ClientDeleteElasticsearchDomainResponseDomainStatusEncryptionAtRestOptionsTypeDef,
        "NodeToNodeEncryptionOptions": ClientDeleteElasticsearchDomainResponseDomainStatusNodeToNodeEncryptionOptionsTypeDef,
        "AdvancedOptions": Dict[str, str],
        "LogPublishingOptions": Dict[
            str,
            ClientDeleteElasticsearchDomainResponseDomainStatusLogPublishingOptionsTypeDef,
        ],
        "ServiceSoftwareOptions": ClientDeleteElasticsearchDomainResponseDomainStatusServiceSoftwareOptionsTypeDef,
        "DomainEndpointOptions": ClientDeleteElasticsearchDomainResponseDomainStatusDomainEndpointOptionsTypeDef,
    },
    total=False,
)


class ClientDeleteElasticsearchDomainResponseDomainStatusTypeDef(
    _ClientDeleteElasticsearchDomainResponseDomainStatusTypeDef
):
    """
    Type definition for `ClientDeleteElasticsearchDomainResponse` `DomainStatus`

    The status of the Elasticsearch domain being deleted.

    - **DomainId** *(string) --*

      The unique identifier for the specified Elasticsearch domain.

    - **DomainName** *(string) --*

      The name of an Elasticsearch domain. Domain names are unique across the domains owned by an
      account within an AWS region. Domain names start with a letter or number and can contain
      the following characters: a-z (lowercase), 0-9, and - (hyphen).

    - **ARN** *(string) --*

      The Amazon resource name (ARN) of an Elasticsearch domain. See `Identifiers for IAM
      Entities
      <http://docs.aws.amazon.com/IAM/latest/UserGuide/index.html?Using_Identifiers.html>`__ in
      *Using AWS Identity and Access Management* for more information.

    - **Created** *(boolean) --*

      The domain creation status. ``True`` if the creation of an Elasticsearch domain is
      complete. ``False`` if domain creation is still in progress.

    - **Deleted** *(boolean) --*

      The domain deletion status. ``True`` if a delete request has been received for the domain
      but resource cleanup is still in progress. ``False`` if the domain has not been deleted.
      Once domain deletion is complete, the status of the domain is no longer returned.

    - **Endpoint** *(string) --*

      The Elasticsearch domain endpoint that you use to submit index and search requests.

    - **Endpoints** *(dict) --*

      Map containing the Elasticsearch domain endpoints used to submit index and search requests.
      Example ``key, value`` :
      ``'vpc','vpc-endpoint-h2dsd34efgyghrtguk5gt6j2foh4.us-east-1.es.amazonaws.com'`` .

      - *(string) --*

        - *(string) --*

          The endpoint to which service requests are submitted. For example,
          ``search-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.es.amazonaws.com`` or
          ``doc-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.es.amazonaws.com`` .

    - **Processing** *(boolean) --*

      The status of the Elasticsearch domain configuration. ``True`` if Amazon Elasticsearch
      Service is processing configuration changes. ``False`` if the configuration is active.

    - **UpgradeProcessing** *(boolean) --*

      The status of an Elasticsearch domain version upgrade. ``True`` if Amazon Elasticsearch
      Service is undergoing a version upgrade. ``False`` if the configuration is active.

    - **ElasticsearchVersion** *(string) --*

    - **ElasticsearchClusterConfig** *(dict) --*

      The type and number of instances in the domain cluster.

      - **InstanceType** *(string) --*

        The instance type for an Elasticsearch cluster.

      - **InstanceCount** *(integer) --*

        The number of instances in the specified domain cluster.

      - **DedicatedMasterEnabled** *(boolean) --*

        A boolean value to indicate whether a dedicated master node is enabled. See `About
        Dedicated Master Nodes
        <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains.html#es-managedomains-dedicatedmasternodes>`__
        for more information.

      - **ZoneAwarenessEnabled** *(boolean) --*

        A boolean value to indicate whether zone awareness is enabled. See `About Zone Awareness
        <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains.html#es-managedomains-zoneawareness>`__
        for more information.

      - **ZoneAwarenessConfig** *(dict) --*

        Specifies the zone awareness configuration for a domain when zone awareness is enabled.

        - **AvailabilityZoneCount** *(integer) --*

          An integer value to indicate the number of availability zones for a domain when zone
          awareness is enabled. This should be equal to number of subnets if VPC endpoints is
          enabled

      - **DedicatedMasterType** *(string) --*

        The instance type for a dedicated master node.

      - **DedicatedMasterCount** *(integer) --*

        Total number of dedicated master nodes, active and on standby, for the cluster.

    - **EBSOptions** *(dict) --*

      The ``EBSOptions`` for the specified domain. See `Configuring EBS-based Storage
      <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html#es-createdomain-configure-ebs>`__
      for more information.

      - **EBSEnabled** *(boolean) --*

        Specifies whether EBS-based storage is enabled.

      - **VolumeType** *(string) --*

        Specifies the volume type for EBS-based storage.

      - **VolumeSize** *(integer) --*

        Integer to specify the size of an EBS volume.

      - **Iops** *(integer) --*

        Specifies the IOPD for a Provisioned IOPS EBS volume (SSD).

    - **AccessPolicies** *(string) --*

      IAM access policy as a JSON-formatted string.

    - **SnapshotOptions** *(dict) --*

      Specifies the status of the ``SnapshotOptions``

      - **AutomatedSnapshotStartHour** *(integer) --*

        Specifies the time, in UTC format, when the service takes a daily automated snapshot of
        the specified Elasticsearch domain. Default value is ``0`` hours.

    - **VPCOptions** *(dict) --*

      The ``VPCOptions`` for the specified domain. For more information, see `VPC Endpoints for
      Amazon Elasticsearch Service Domains
      <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html>`__ .

      - **VPCId** *(string) --*

        The VPC Id for the Elasticsearch domain. Exists only if the domain was created with
        VPCOptions.

      - **SubnetIds** *(list) --*

        Specifies the subnets for VPC endpoint.

        - *(string) --*

      - **AvailabilityZones** *(list) --*

        The availability zones for the Elasticsearch domain. Exists only if the domain was
        created with VPCOptions.

        - *(string) --*

      - **SecurityGroupIds** *(list) --*

        Specifies the security groups for VPC endpoint.

        - *(string) --*

    - **CognitoOptions** *(dict) --*

      The ``CognitoOptions`` for the specified domain. For more information, see `Amazon Cognito
      Authentication for Kibana
      <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-cognito-auth.html>`__
      .

      - **Enabled** *(boolean) --*

        Specifies the option to enable Cognito for Kibana authentication.

      - **UserPoolId** *(string) --*

        Specifies the Cognito user pool ID for Kibana authentication.

      - **IdentityPoolId** *(string) --*

        Specifies the Cognito identity pool ID for Kibana authentication.

      - **RoleArn** *(string) --*

        Specifies the role ARN that provides Elasticsearch permissions for accessing Cognito
        resources.

    - **EncryptionAtRestOptions** *(dict) --*

      Specifies the status of the ``EncryptionAtRestOptions`` .

      - **Enabled** *(boolean) --*

        Specifies the option to enable Encryption At Rest.

      - **KmsKeyId** *(string) --*

        Specifies the KMS Key ID for Encryption At Rest options.

    - **NodeToNodeEncryptionOptions** *(dict) --*

      Specifies the status of the ``NodeToNodeEncryptionOptions`` .

      - **Enabled** *(boolean) --*

        Specify true to enable node-to-node encryption.

    - **AdvancedOptions** *(dict) --*

      Specifies the status of the ``AdvancedOptions``

      - *(string) --*

        - *(string) --*

    - **LogPublishingOptions** *(dict) --*

      Log publishing options for the given domain.

      - *(string) --*

        Type of Log File, it can be one of the following:

        * INDEX_SLOW_LOGS: Index slow logs contain insert requests that took more time than
        configured index query log threshold to execute.

        * SEARCH_SLOW_LOGS: Search slow logs contain search queries that took more time than
        configured search query log threshold to execute.

        * ES_APPLICATION_LOGS: Elasticsearch application logs contain information about errors
        and warnings raised during the operation of the service and can be useful for
        troubleshooting.

        - *(dict) --*

          Log Publishing option that is set for given domain. Attributes and their details:

          * CloudWatchLogsLogGroupArn: ARN of the Cloudwatch log group to which log needs to be
          published.

          * Enabled: Whether the log publishing for given log type is enabled or not

          - **CloudWatchLogsLogGroupArn** *(string) --*

            ARN of the Cloudwatch log group to which log needs to be published.

          - **Enabled** *(boolean) --*

            Specifies whether given log publishing option is enabled or not.

    - **ServiceSoftwareOptions** *(dict) --*

      The current status of the Elasticsearch domain's service software.

      - **CurrentVersion** *(string) --*

        The current service software version that is present on the domain.

      - **NewVersion** *(string) --*

        The new service software version if one is available.

      - **UpdateAvailable** *(boolean) --*

        ``True`` if you are able to update you service software version. ``False`` if you are not
        able to update your service software version.

      - **Cancellable** *(boolean) --*

        ``True`` if you are able to cancel your service software version update. ``False`` if you
        are not able to cancel your service software version.

      - **UpdateStatus** *(string) --*

        The status of your service software update. This field can take the following values:
        ``ELIGIBLE`` , ``PENDING_UPDATE`` , ``IN_PROGRESS`` , ``COMPLETED`` , and
        ``NOT_ELIGIBLE`` .

      - **Description** *(string) --*

        The description of the ``UpdateStatus`` .

      - **AutomatedUpdateDate** *(datetime) --*

        Timestamp, in Epoch time, until which you can manually request a service software update.
        After this date, we automatically update your service software.

    - **DomainEndpointOptions** *(dict) --*

      The current status of the Elasticsearch domain's endpoint options.

      - **EnforceHTTPS** *(boolean) --*

        Specify if only HTTPS endpoint should be enabled for the Elasticsearch domain.

      - **TLSSecurityPolicy** *(string) --*

        Specify the TLS security policy that needs to be applied to the HTTPS endpoint of
        Elasticsearch domain. It can be one of the following values:

        * **Policy-Min-TLS-1-0-2019-07:** TLS security policy which supports TLSv1.0 and higher.

        * **Policy-Min-TLS-1-2-2019-07:** TLS security policy which supports only TLSv1.2
    """


_ClientDeleteElasticsearchDomainResponseTypeDef = TypedDict(
    "_ClientDeleteElasticsearchDomainResponseTypeDef",
    {"DomainStatus": ClientDeleteElasticsearchDomainResponseDomainStatusTypeDef},
    total=False,
)


class ClientDeleteElasticsearchDomainResponseTypeDef(
    _ClientDeleteElasticsearchDomainResponseTypeDef
):
    """
    Type definition for `ClientDeleteElasticsearchDomain` `Response`

    The result of a ``DeleteElasticsearchDomain`` request. Contains the status of the pending
    deletion, or no status if the domain and all of its resources have been deleted.

    - **DomainStatus** *(dict) --*

      The status of the Elasticsearch domain being deleted.

      - **DomainId** *(string) --*

        The unique identifier for the specified Elasticsearch domain.

      - **DomainName** *(string) --*

        The name of an Elasticsearch domain. Domain names are unique across the domains owned by an
        account within an AWS region. Domain names start with a letter or number and can contain
        the following characters: a-z (lowercase), 0-9, and - (hyphen).

      - **ARN** *(string) --*

        The Amazon resource name (ARN) of an Elasticsearch domain. See `Identifiers for IAM
        Entities
        <http://docs.aws.amazon.com/IAM/latest/UserGuide/index.html?Using_Identifiers.html>`__ in
        *Using AWS Identity and Access Management* for more information.

      - **Created** *(boolean) --*

        The domain creation status. ``True`` if the creation of an Elasticsearch domain is
        complete. ``False`` if domain creation is still in progress.

      - **Deleted** *(boolean) --*

        The domain deletion status. ``True`` if a delete request has been received for the domain
        but resource cleanup is still in progress. ``False`` if the domain has not been deleted.
        Once domain deletion is complete, the status of the domain is no longer returned.

      - **Endpoint** *(string) --*

        The Elasticsearch domain endpoint that you use to submit index and search requests.

      - **Endpoints** *(dict) --*

        Map containing the Elasticsearch domain endpoints used to submit index and search requests.
        Example ``key, value`` :
        ``'vpc','vpc-endpoint-h2dsd34efgyghrtguk5gt6j2foh4.us-east-1.es.amazonaws.com'`` .

        - *(string) --*

          - *(string) --*

            The endpoint to which service requests are submitted. For example,
            ``search-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.es.amazonaws.com`` or
            ``doc-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.es.amazonaws.com`` .

      - **Processing** *(boolean) --*

        The status of the Elasticsearch domain configuration. ``True`` if Amazon Elasticsearch
        Service is processing configuration changes. ``False`` if the configuration is active.

      - **UpgradeProcessing** *(boolean) --*

        The status of an Elasticsearch domain version upgrade. ``True`` if Amazon Elasticsearch
        Service is undergoing a version upgrade. ``False`` if the configuration is active.

      - **ElasticsearchVersion** *(string) --*

      - **ElasticsearchClusterConfig** *(dict) --*

        The type and number of instances in the domain cluster.

        - **InstanceType** *(string) --*

          The instance type for an Elasticsearch cluster.

        - **InstanceCount** *(integer) --*

          The number of instances in the specified domain cluster.

        - **DedicatedMasterEnabled** *(boolean) --*

          A boolean value to indicate whether a dedicated master node is enabled. See `About
          Dedicated Master Nodes
          <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains.html#es-managedomains-dedicatedmasternodes>`__
          for more information.

        - **ZoneAwarenessEnabled** *(boolean) --*

          A boolean value to indicate whether zone awareness is enabled. See `About Zone Awareness
          <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains.html#es-managedomains-zoneawareness>`__
          for more information.

        - **ZoneAwarenessConfig** *(dict) --*

          Specifies the zone awareness configuration for a domain when zone awareness is enabled.

          - **AvailabilityZoneCount** *(integer) --*

            An integer value to indicate the number of availability zones for a domain when zone
            awareness is enabled. This should be equal to number of subnets if VPC endpoints is
            enabled

        - **DedicatedMasterType** *(string) --*

          The instance type for a dedicated master node.

        - **DedicatedMasterCount** *(integer) --*

          Total number of dedicated master nodes, active and on standby, for the cluster.

      - **EBSOptions** *(dict) --*

        The ``EBSOptions`` for the specified domain. See `Configuring EBS-based Storage
        <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html#es-createdomain-configure-ebs>`__
        for more information.

        - **EBSEnabled** *(boolean) --*

          Specifies whether EBS-based storage is enabled.

        - **VolumeType** *(string) --*

          Specifies the volume type for EBS-based storage.

        - **VolumeSize** *(integer) --*

          Integer to specify the size of an EBS volume.

        - **Iops** *(integer) --*

          Specifies the IOPD for a Provisioned IOPS EBS volume (SSD).

      - **AccessPolicies** *(string) --*

        IAM access policy as a JSON-formatted string.

      - **SnapshotOptions** *(dict) --*

        Specifies the status of the ``SnapshotOptions``

        - **AutomatedSnapshotStartHour** *(integer) --*

          Specifies the time, in UTC format, when the service takes a daily automated snapshot of
          the specified Elasticsearch domain. Default value is ``0`` hours.

      - **VPCOptions** *(dict) --*

        The ``VPCOptions`` for the specified domain. For more information, see `VPC Endpoints for
        Amazon Elasticsearch Service Domains
        <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html>`__ .

        - **VPCId** *(string) --*

          The VPC Id for the Elasticsearch domain. Exists only if the domain was created with
          VPCOptions.

        - **SubnetIds** *(list) --*

          Specifies the subnets for VPC endpoint.

          - *(string) --*

        - **AvailabilityZones** *(list) --*

          The availability zones for the Elasticsearch domain. Exists only if the domain was
          created with VPCOptions.

          - *(string) --*

        - **SecurityGroupIds** *(list) --*

          Specifies the security groups for VPC endpoint.

          - *(string) --*

      - **CognitoOptions** *(dict) --*

        The ``CognitoOptions`` for the specified domain. For more information, see `Amazon Cognito
        Authentication for Kibana
        <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-cognito-auth.html>`__
        .

        - **Enabled** *(boolean) --*

          Specifies the option to enable Cognito for Kibana authentication.

        - **UserPoolId** *(string) --*

          Specifies the Cognito user pool ID for Kibana authentication.

        - **IdentityPoolId** *(string) --*

          Specifies the Cognito identity pool ID for Kibana authentication.

        - **RoleArn** *(string) --*

          Specifies the role ARN that provides Elasticsearch permissions for accessing Cognito
          resources.

      - **EncryptionAtRestOptions** *(dict) --*

        Specifies the status of the ``EncryptionAtRestOptions`` .

        - **Enabled** *(boolean) --*

          Specifies the option to enable Encryption At Rest.

        - **KmsKeyId** *(string) --*

          Specifies the KMS Key ID for Encryption At Rest options.

      - **NodeToNodeEncryptionOptions** *(dict) --*

        Specifies the status of the ``NodeToNodeEncryptionOptions`` .

        - **Enabled** *(boolean) --*

          Specify true to enable node-to-node encryption.

      - **AdvancedOptions** *(dict) --*

        Specifies the status of the ``AdvancedOptions``

        - *(string) --*

          - *(string) --*

      - **LogPublishingOptions** *(dict) --*

        Log publishing options for the given domain.

        - *(string) --*

          Type of Log File, it can be one of the following:

          * INDEX_SLOW_LOGS: Index slow logs contain insert requests that took more time than
          configured index query log threshold to execute.

          * SEARCH_SLOW_LOGS: Search slow logs contain search queries that took more time than
          configured search query log threshold to execute.

          * ES_APPLICATION_LOGS: Elasticsearch application logs contain information about errors
          and warnings raised during the operation of the service and can be useful for
          troubleshooting.

          - *(dict) --*

            Log Publishing option that is set for given domain. Attributes and their details:

            * CloudWatchLogsLogGroupArn: ARN of the Cloudwatch log group to which log needs to be
            published.

            * Enabled: Whether the log publishing for given log type is enabled or not

            - **CloudWatchLogsLogGroupArn** *(string) --*

              ARN of the Cloudwatch log group to which log needs to be published.

            - **Enabled** *(boolean) --*

              Specifies whether given log publishing option is enabled or not.

      - **ServiceSoftwareOptions** *(dict) --*

        The current status of the Elasticsearch domain's service software.

        - **CurrentVersion** *(string) --*

          The current service software version that is present on the domain.

        - **NewVersion** *(string) --*

          The new service software version if one is available.

        - **UpdateAvailable** *(boolean) --*

          ``True`` if you are able to update you service software version. ``False`` if you are not
          able to update your service software version.

        - **Cancellable** *(boolean) --*

          ``True`` if you are able to cancel your service software version update. ``False`` if you
          are not able to cancel your service software version.

        - **UpdateStatus** *(string) --*

          The status of your service software update. This field can take the following values:
          ``ELIGIBLE`` , ``PENDING_UPDATE`` , ``IN_PROGRESS`` , ``COMPLETED`` , and
          ``NOT_ELIGIBLE`` .

        - **Description** *(string) --*

          The description of the ``UpdateStatus`` .

        - **AutomatedUpdateDate** *(datetime) --*

          Timestamp, in Epoch time, until which you can manually request a service software update.
          After this date, we automatically update your service software.

      - **DomainEndpointOptions** *(dict) --*

        The current status of the Elasticsearch domain's endpoint options.

        - **EnforceHTTPS** *(boolean) --*

          Specify if only HTTPS endpoint should be enabled for the Elasticsearch domain.

        - **TLSSecurityPolicy** *(string) --*

          Specify the TLS security policy that needs to be applied to the HTTPS endpoint of
          Elasticsearch domain. It can be one of the following values:

          * **Policy-Min-TLS-1-0-2019-07:** TLS security policy which supports TLSv1.0 and higher.

          * **Policy-Min-TLS-1-2-2019-07:** TLS security policy which supports only TLSv1.2
    """


_ClientDescribeElasticsearchDomainConfigResponseDomainConfigAccessPoliciesStatusTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainConfigResponseDomainConfigAccessPoliciesStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": str,
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientDescribeElasticsearchDomainConfigResponseDomainConfigAccessPoliciesStatusTypeDef(
    _ClientDescribeElasticsearchDomainConfigResponseDomainConfigAccessPoliciesStatusTypeDef
):
    """
    Type definition for `ClientDescribeElasticsearchDomainConfigResponseDomainConfigAccessPolicies` `Status`

    The status of the access policy for the Elasticsearch domain. See ``OptionStatus`` for
    the status information that's included.

    - **CreationDate** *(datetime) --*

      Timestamp which tells the creation date for the entity.

    - **UpdateDate** *(datetime) --*

      Timestamp which tells the last updated time for the entity.

    - **UpdateVersion** *(integer) --*

      Specifies the latest version for the entity.

    - **State** *(string) --*

      Provides the ``OptionState`` for the Elasticsearch domain.

    - **PendingDeletion** *(boolean) --*

      Indicates whether the Elasticsearch domain is being deleted.
    """


_ClientDescribeElasticsearchDomainConfigResponseDomainConfigAccessPoliciesTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainConfigResponseDomainConfigAccessPoliciesTypeDef",
    {
        "Options": str,
        "Status": ClientDescribeElasticsearchDomainConfigResponseDomainConfigAccessPoliciesStatusTypeDef,
    },
    total=False,
)


class ClientDescribeElasticsearchDomainConfigResponseDomainConfigAccessPoliciesTypeDef(
    _ClientDescribeElasticsearchDomainConfigResponseDomainConfigAccessPoliciesTypeDef
):
    """
    Type definition for `ClientDescribeElasticsearchDomainConfigResponseDomainConfig` `AccessPolicies`

    IAM access policy as a JSON-formatted string.

    - **Options** *(string) --*

      The access policy configured for the Elasticsearch domain. Access policies may be
      resource-based, IP-based, or IAM-based. See `Configuring Access Policies
      <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html#es-createdomain-configure-access-policies>`__
      for more information.

    - **Status** *(dict) --*

      The status of the access policy for the Elasticsearch domain. See ``OptionStatus`` for
      the status information that's included.

      - **CreationDate** *(datetime) --*

        Timestamp which tells the creation date for the entity.

      - **UpdateDate** *(datetime) --*

        Timestamp which tells the last updated time for the entity.

      - **UpdateVersion** *(integer) --*

        Specifies the latest version for the entity.

      - **State** *(string) --*

        Provides the ``OptionState`` for the Elasticsearch domain.

      - **PendingDeletion** *(boolean) --*

        Indicates whether the Elasticsearch domain is being deleted.
    """


_ClientDescribeElasticsearchDomainConfigResponseDomainConfigAdvancedOptionsStatusTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainConfigResponseDomainConfigAdvancedOptionsStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": str,
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientDescribeElasticsearchDomainConfigResponseDomainConfigAdvancedOptionsStatusTypeDef(
    _ClientDescribeElasticsearchDomainConfigResponseDomainConfigAdvancedOptionsStatusTypeDef
):
    """
    Type definition for `ClientDescribeElasticsearchDomainConfigResponseDomainConfigAdvancedOptions` `Status`

    Specifies the status of ``OptionStatus`` for advanced options for the specified
    Elasticsearch domain.

    - **CreationDate** *(datetime) --*

      Timestamp which tells the creation date for the entity.

    - **UpdateDate** *(datetime) --*

      Timestamp which tells the last updated time for the entity.

    - **UpdateVersion** *(integer) --*

      Specifies the latest version for the entity.

    - **State** *(string) --*

      Provides the ``OptionState`` for the Elasticsearch domain.

    - **PendingDeletion** *(boolean) --*

      Indicates whether the Elasticsearch domain is being deleted.
    """


_ClientDescribeElasticsearchDomainConfigResponseDomainConfigAdvancedOptionsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainConfigResponseDomainConfigAdvancedOptionsTypeDef",
    {
        "Options": Dict[str, str],
        "Status": ClientDescribeElasticsearchDomainConfigResponseDomainConfigAdvancedOptionsStatusTypeDef,
    },
    total=False,
)


class ClientDescribeElasticsearchDomainConfigResponseDomainConfigAdvancedOptionsTypeDef(
    _ClientDescribeElasticsearchDomainConfigResponseDomainConfigAdvancedOptionsTypeDef
):
    """
    Type definition for `ClientDescribeElasticsearchDomainConfigResponseDomainConfig` `AdvancedOptions`

    Specifies the ``AdvancedOptions`` for the domain. See `Configuring Advanced Options
    <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html#es-createdomain-configure-advanced-options>`__
    for more information.

    - **Options** *(dict) --*

      Specifies the status of advanced options for the specified Elasticsearch domain.

      - *(string) --*

        - *(string) --*

    - **Status** *(dict) --*

      Specifies the status of ``OptionStatus`` for advanced options for the specified
      Elasticsearch domain.

      - **CreationDate** *(datetime) --*

        Timestamp which tells the creation date for the entity.

      - **UpdateDate** *(datetime) --*

        Timestamp which tells the last updated time for the entity.

      - **UpdateVersion** *(integer) --*

        Specifies the latest version for the entity.

      - **State** *(string) --*

        Provides the ``OptionState`` for the Elasticsearch domain.

      - **PendingDeletion** *(boolean) --*

        Indicates whether the Elasticsearch domain is being deleted.
    """


_ClientDescribeElasticsearchDomainConfigResponseDomainConfigCognitoOptionsOptionsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainConfigResponseDomainConfigCognitoOptionsOptionsTypeDef",
    {"Enabled": bool, "UserPoolId": str, "IdentityPoolId": str, "RoleArn": str},
    total=False,
)


class ClientDescribeElasticsearchDomainConfigResponseDomainConfigCognitoOptionsOptionsTypeDef(
    _ClientDescribeElasticsearchDomainConfigResponseDomainConfigCognitoOptionsOptionsTypeDef
):
    """
    Type definition for `ClientDescribeElasticsearchDomainConfigResponseDomainConfigCognitoOptions` `Options`

    Specifies the Cognito options for the specified Elasticsearch domain.

    - **Enabled** *(boolean) --*

      Specifies the option to enable Cognito for Kibana authentication.

    - **UserPoolId** *(string) --*

      Specifies the Cognito user pool ID for Kibana authentication.

    - **IdentityPoolId** *(string) --*

      Specifies the Cognito identity pool ID for Kibana authentication.

    - **RoleArn** *(string) --*

      Specifies the role ARN that provides Elasticsearch permissions for accessing Cognito
      resources.
    """


_ClientDescribeElasticsearchDomainConfigResponseDomainConfigCognitoOptionsStatusTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainConfigResponseDomainConfigCognitoOptionsStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": str,
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientDescribeElasticsearchDomainConfigResponseDomainConfigCognitoOptionsStatusTypeDef(
    _ClientDescribeElasticsearchDomainConfigResponseDomainConfigCognitoOptionsStatusTypeDef
):
    """
    Type definition for `ClientDescribeElasticsearchDomainConfigResponseDomainConfigCognitoOptions` `Status`

    Specifies the status of the Cognito options for the specified Elasticsearch domain.

    - **CreationDate** *(datetime) --*

      Timestamp which tells the creation date for the entity.

    - **UpdateDate** *(datetime) --*

      Timestamp which tells the last updated time for the entity.

    - **UpdateVersion** *(integer) --*

      Specifies the latest version for the entity.

    - **State** *(string) --*

      Provides the ``OptionState`` for the Elasticsearch domain.

    - **PendingDeletion** *(boolean) --*

      Indicates whether the Elasticsearch domain is being deleted.
    """


_ClientDescribeElasticsearchDomainConfigResponseDomainConfigCognitoOptionsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainConfigResponseDomainConfigCognitoOptionsTypeDef",
    {
        "Options": ClientDescribeElasticsearchDomainConfigResponseDomainConfigCognitoOptionsOptionsTypeDef,
        "Status": ClientDescribeElasticsearchDomainConfigResponseDomainConfigCognitoOptionsStatusTypeDef,
    },
    total=False,
)


class ClientDescribeElasticsearchDomainConfigResponseDomainConfigCognitoOptionsTypeDef(
    _ClientDescribeElasticsearchDomainConfigResponseDomainConfigCognitoOptionsTypeDef
):
    """
    Type definition for `ClientDescribeElasticsearchDomainConfigResponseDomainConfig` `CognitoOptions`

    The ``CognitoOptions`` for the specified domain. For more information, see `Amazon Cognito
    Authentication for Kibana
    <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-cognito-auth.html>`__
    .

    - **Options** *(dict) --*

      Specifies the Cognito options for the specified Elasticsearch domain.

      - **Enabled** *(boolean) --*

        Specifies the option to enable Cognito for Kibana authentication.

      - **UserPoolId** *(string) --*

        Specifies the Cognito user pool ID for Kibana authentication.

      - **IdentityPoolId** *(string) --*

        Specifies the Cognito identity pool ID for Kibana authentication.

      - **RoleArn** *(string) --*

        Specifies the role ARN that provides Elasticsearch permissions for accessing Cognito
        resources.

    - **Status** *(dict) --*

      Specifies the status of the Cognito options for the specified Elasticsearch domain.

      - **CreationDate** *(datetime) --*

        Timestamp which tells the creation date for the entity.

      - **UpdateDate** *(datetime) --*

        Timestamp which tells the last updated time for the entity.

      - **UpdateVersion** *(integer) --*

        Specifies the latest version for the entity.

      - **State** *(string) --*

        Provides the ``OptionState`` for the Elasticsearch domain.

      - **PendingDeletion** *(boolean) --*

        Indicates whether the Elasticsearch domain is being deleted.
    """


_ClientDescribeElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsOptionsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsOptionsTypeDef",
    {"EnforceHTTPS": bool, "TLSSecurityPolicy": str},
    total=False,
)


class ClientDescribeElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsOptionsTypeDef(
    _ClientDescribeElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsOptionsTypeDef
):
    """
    Type definition for `ClientDescribeElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptions` `Options`

    Options to configure endpoint for the Elasticsearch domain.

    - **EnforceHTTPS** *(boolean) --*

      Specify if only HTTPS endpoint should be enabled for the Elasticsearch domain.

    - **TLSSecurityPolicy** *(string) --*

      Specify the TLS security policy that needs to be applied to the HTTPS endpoint of
      Elasticsearch domain. It can be one of the following values:

      * **Policy-Min-TLS-1-0-2019-07:** TLS security policy which supports TLSv1.0 and higher.

      * **Policy-Min-TLS-1-2-2019-07:** TLS security policy which supports only TLSv1.2
    """


_ClientDescribeElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsStatusTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": str,
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientDescribeElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsStatusTypeDef(
    _ClientDescribeElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsStatusTypeDef
):
    """
    Type definition for `ClientDescribeElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptions` `Status`

    The status of the endpoint options for the Elasticsearch domain. See ``OptionStatus`` for
    the status information that's included.

    - **CreationDate** *(datetime) --*

      Timestamp which tells the creation date for the entity.

    - **UpdateDate** *(datetime) --*

      Timestamp which tells the last updated time for the entity.

    - **UpdateVersion** *(integer) --*

      Specifies the latest version for the entity.

    - **State** *(string) --*

      Provides the ``OptionState`` for the Elasticsearch domain.

    - **PendingDeletion** *(boolean) --*

      Indicates whether the Elasticsearch domain is being deleted.
    """


_ClientDescribeElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsTypeDef",
    {
        "Options": ClientDescribeElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsOptionsTypeDef,
        "Status": ClientDescribeElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsStatusTypeDef,
    },
    total=False,
)


class ClientDescribeElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsTypeDef(
    _ClientDescribeElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsTypeDef
):
    """
    Type definition for `ClientDescribeElasticsearchDomainConfigResponseDomainConfig` `DomainEndpointOptions`

    Specifies the ``DomainEndpointOptions`` for the Elasticsearch domain.

    - **Options** *(dict) --*

      Options to configure endpoint for the Elasticsearch domain.

      - **EnforceHTTPS** *(boolean) --*

        Specify if only HTTPS endpoint should be enabled for the Elasticsearch domain.

      - **TLSSecurityPolicy** *(string) --*

        Specify the TLS security policy that needs to be applied to the HTTPS endpoint of
        Elasticsearch domain. It can be one of the following values:

        * **Policy-Min-TLS-1-0-2019-07:** TLS security policy which supports TLSv1.0 and higher.

        * **Policy-Min-TLS-1-2-2019-07:** TLS security policy which supports only TLSv1.2

    - **Status** *(dict) --*

      The status of the endpoint options for the Elasticsearch domain. See ``OptionStatus`` for
      the status information that's included.

      - **CreationDate** *(datetime) --*

        Timestamp which tells the creation date for the entity.

      - **UpdateDate** *(datetime) --*

        Timestamp which tells the last updated time for the entity.

      - **UpdateVersion** *(integer) --*

        Specifies the latest version for the entity.

      - **State** *(string) --*

        Provides the ``OptionState`` for the Elasticsearch domain.

      - **PendingDeletion** *(boolean) --*

        Indicates whether the Elasticsearch domain is being deleted.
    """


_ClientDescribeElasticsearchDomainConfigResponseDomainConfigEBSOptionsOptionsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainConfigResponseDomainConfigEBSOptionsOptionsTypeDef",
    {"EBSEnabled": bool, "VolumeType": str, "VolumeSize": int, "Iops": int},
    total=False,
)


class ClientDescribeElasticsearchDomainConfigResponseDomainConfigEBSOptionsOptionsTypeDef(
    _ClientDescribeElasticsearchDomainConfigResponseDomainConfigEBSOptionsOptionsTypeDef
):
    """
    Type definition for `ClientDescribeElasticsearchDomainConfigResponseDomainConfigEBSOptions` `Options`

    Specifies the EBS options for the specified Elasticsearch domain.

    - **EBSEnabled** *(boolean) --*

      Specifies whether EBS-based storage is enabled.

    - **VolumeType** *(string) --*

      Specifies the volume type for EBS-based storage.

    - **VolumeSize** *(integer) --*

      Integer to specify the size of an EBS volume.

    - **Iops** *(integer) --*

      Specifies the IOPD for a Provisioned IOPS EBS volume (SSD).
    """


_ClientDescribeElasticsearchDomainConfigResponseDomainConfigEBSOptionsStatusTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainConfigResponseDomainConfigEBSOptionsStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": str,
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientDescribeElasticsearchDomainConfigResponseDomainConfigEBSOptionsStatusTypeDef(
    _ClientDescribeElasticsearchDomainConfigResponseDomainConfigEBSOptionsStatusTypeDef
):
    """
    Type definition for `ClientDescribeElasticsearchDomainConfigResponseDomainConfigEBSOptions` `Status`

    Specifies the status of the EBS options for the specified Elasticsearch domain.

    - **CreationDate** *(datetime) --*

      Timestamp which tells the creation date for the entity.

    - **UpdateDate** *(datetime) --*

      Timestamp which tells the last updated time for the entity.

    - **UpdateVersion** *(integer) --*

      Specifies the latest version for the entity.

    - **State** *(string) --*

      Provides the ``OptionState`` for the Elasticsearch domain.

    - **PendingDeletion** *(boolean) --*

      Indicates whether the Elasticsearch domain is being deleted.
    """


_ClientDescribeElasticsearchDomainConfigResponseDomainConfigEBSOptionsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainConfigResponseDomainConfigEBSOptionsTypeDef",
    {
        "Options": ClientDescribeElasticsearchDomainConfigResponseDomainConfigEBSOptionsOptionsTypeDef,
        "Status": ClientDescribeElasticsearchDomainConfigResponseDomainConfigEBSOptionsStatusTypeDef,
    },
    total=False,
)


class ClientDescribeElasticsearchDomainConfigResponseDomainConfigEBSOptionsTypeDef(
    _ClientDescribeElasticsearchDomainConfigResponseDomainConfigEBSOptionsTypeDef
):
    """
    Type definition for `ClientDescribeElasticsearchDomainConfigResponseDomainConfig` `EBSOptions`

    Specifies the ``EBSOptions`` for the Elasticsearch domain.

    - **Options** *(dict) --*

      Specifies the EBS options for the specified Elasticsearch domain.

      - **EBSEnabled** *(boolean) --*

        Specifies whether EBS-based storage is enabled.

      - **VolumeType** *(string) --*

        Specifies the volume type for EBS-based storage.

      - **VolumeSize** *(integer) --*

        Integer to specify the size of an EBS volume.

      - **Iops** *(integer) --*

        Specifies the IOPD for a Provisioned IOPS EBS volume (SSD).

    - **Status** *(dict) --*

      Specifies the status of the EBS options for the specified Elasticsearch domain.

      - **CreationDate** *(datetime) --*

        Timestamp which tells the creation date for the entity.

      - **UpdateDate** *(datetime) --*

        Timestamp which tells the last updated time for the entity.

      - **UpdateVersion** *(integer) --*

        Specifies the latest version for the entity.

      - **State** *(string) --*

        Provides the ``OptionState`` for the Elasticsearch domain.

      - **PendingDeletion** *(boolean) --*

        Indicates whether the Elasticsearch domain is being deleted.
    """


_ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigOptionsZoneAwarenessConfigTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigOptionsZoneAwarenessConfigTypeDef",
    {"AvailabilityZoneCount": int},
    total=False,
)


class ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigOptionsZoneAwarenessConfigTypeDef(
    _ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigOptionsZoneAwarenessConfigTypeDef
):
    """
    Type definition for `ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigOptions` `ZoneAwarenessConfig`

    Specifies the zone awareness configuration for a domain when zone awareness is enabled.

    - **AvailabilityZoneCount** *(integer) --*

      An integer value to indicate the number of availability zones for a domain when zone
      awareness is enabled. This should be equal to number of subnets if VPC endpoints is
      enabled
    """


_ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigOptionsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigOptionsTypeDef",
    {
        "InstanceType": str,
        "InstanceCount": int,
        "DedicatedMasterEnabled": bool,
        "ZoneAwarenessEnabled": bool,
        "ZoneAwarenessConfig": ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigOptionsZoneAwarenessConfigTypeDef,
        "DedicatedMasterType": str,
        "DedicatedMasterCount": int,
    },
    total=False,
)


class ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigOptionsTypeDef(
    _ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigOptionsTypeDef
):
    """
    Type definition for `ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfig` `Options`

    Specifies the cluster configuration for the specified Elasticsearch domain.

    - **InstanceType** *(string) --*

      The instance type for an Elasticsearch cluster.

    - **InstanceCount** *(integer) --*

      The number of instances in the specified domain cluster.

    - **DedicatedMasterEnabled** *(boolean) --*

      A boolean value to indicate whether a dedicated master node is enabled. See `About
      Dedicated Master Nodes
      <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains.html#es-managedomains-dedicatedmasternodes>`__
      for more information.

    - **ZoneAwarenessEnabled** *(boolean) --*

      A boolean value to indicate whether zone awareness is enabled. See `About Zone
      Awareness
      <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains.html#es-managedomains-zoneawareness>`__
      for more information.

    - **ZoneAwarenessConfig** *(dict) --*

      Specifies the zone awareness configuration for a domain when zone awareness is enabled.

      - **AvailabilityZoneCount** *(integer) --*

        An integer value to indicate the number of availability zones for a domain when zone
        awareness is enabled. This should be equal to number of subnets if VPC endpoints is
        enabled

    - **DedicatedMasterType** *(string) --*

      The instance type for a dedicated master node.

    - **DedicatedMasterCount** *(integer) --*

      Total number of dedicated master nodes, active and on standby, for the cluster.
    """


_ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigStatusTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": str,
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigStatusTypeDef(
    _ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigStatusTypeDef
):
    """
    Type definition for `ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfig` `Status`

    Specifies the status of the configuration for the specified Elasticsearch domain.

    - **CreationDate** *(datetime) --*

      Timestamp which tells the creation date for the entity.

    - **UpdateDate** *(datetime) --*

      Timestamp which tells the last updated time for the entity.

    - **UpdateVersion** *(integer) --*

      Specifies the latest version for the entity.

    - **State** *(string) --*

      Provides the ``OptionState`` for the Elasticsearch domain.

    - **PendingDeletion** *(boolean) --*

      Indicates whether the Elasticsearch domain is being deleted.
    """


_ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigTypeDef",
    {
        "Options": ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigOptionsTypeDef,
        "Status": ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigStatusTypeDef,
    },
    total=False,
)


class ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigTypeDef(
    _ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigTypeDef
):
    """
    Type definition for `ClientDescribeElasticsearchDomainConfigResponseDomainConfig` `ElasticsearchClusterConfig`

    Specifies the ``ElasticsearchClusterConfig`` for the Elasticsearch domain.

    - **Options** *(dict) --*

      Specifies the cluster configuration for the specified Elasticsearch domain.

      - **InstanceType** *(string) --*

        The instance type for an Elasticsearch cluster.

      - **InstanceCount** *(integer) --*

        The number of instances in the specified domain cluster.

      - **DedicatedMasterEnabled** *(boolean) --*

        A boolean value to indicate whether a dedicated master node is enabled. See `About
        Dedicated Master Nodes
        <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains.html#es-managedomains-dedicatedmasternodes>`__
        for more information.

      - **ZoneAwarenessEnabled** *(boolean) --*

        A boolean value to indicate whether zone awareness is enabled. See `About Zone
        Awareness
        <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains.html#es-managedomains-zoneawareness>`__
        for more information.

      - **ZoneAwarenessConfig** *(dict) --*

        Specifies the zone awareness configuration for a domain when zone awareness is enabled.

        - **AvailabilityZoneCount** *(integer) --*

          An integer value to indicate the number of availability zones for a domain when zone
          awareness is enabled. This should be equal to number of subnets if VPC endpoints is
          enabled

      - **DedicatedMasterType** *(string) --*

        The instance type for a dedicated master node.

      - **DedicatedMasterCount** *(integer) --*

        Total number of dedicated master nodes, active and on standby, for the cluster.

    - **Status** *(dict) --*

      Specifies the status of the configuration for the specified Elasticsearch domain.

      - **CreationDate** *(datetime) --*

        Timestamp which tells the creation date for the entity.

      - **UpdateDate** *(datetime) --*

        Timestamp which tells the last updated time for the entity.

      - **UpdateVersion** *(integer) --*

        Specifies the latest version for the entity.

      - **State** *(string) --*

        Provides the ``OptionState`` for the Elasticsearch domain.

      - **PendingDeletion** *(boolean) --*

        Indicates whether the Elasticsearch domain is being deleted.
    """


_ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchVersionStatusTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchVersionStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": str,
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchVersionStatusTypeDef(
    _ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchVersionStatusTypeDef
):
    """
    Type definition for `ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchVersion` `Status`

    Specifies the status of the Elasticsearch version options for the specified Elasticsearch
    domain.

    - **CreationDate** *(datetime) --*

      Timestamp which tells the creation date for the entity.

    - **UpdateDate** *(datetime) --*

      Timestamp which tells the last updated time for the entity.

    - **UpdateVersion** *(integer) --*

      Specifies the latest version for the entity.

    - **State** *(string) --*

      Provides the ``OptionState`` for the Elasticsearch domain.

    - **PendingDeletion** *(boolean) --*

      Indicates whether the Elasticsearch domain is being deleted.
    """


_ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchVersionTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchVersionTypeDef",
    {
        "Options": str,
        "Status": ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchVersionStatusTypeDef,
    },
    total=False,
)


class ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchVersionTypeDef(
    _ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchVersionTypeDef
):
    """
    Type definition for `ClientDescribeElasticsearchDomainConfigResponseDomainConfig` `ElasticsearchVersion`

    String of format X.Y to specify version for the Elasticsearch domain.

    - **Options** *(string) --*

      Specifies the Elasticsearch version for the specified Elasticsearch domain.

    - **Status** *(dict) --*

      Specifies the status of the Elasticsearch version options for the specified Elasticsearch
      domain.

      - **CreationDate** *(datetime) --*

        Timestamp which tells the creation date for the entity.

      - **UpdateDate** *(datetime) --*

        Timestamp which tells the last updated time for the entity.

      - **UpdateVersion** *(integer) --*

        Specifies the latest version for the entity.

      - **State** *(string) --*

        Provides the ``OptionState`` for the Elasticsearch domain.

      - **PendingDeletion** *(boolean) --*

        Indicates whether the Elasticsearch domain is being deleted.
    """


_ClientDescribeElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsOptionsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsOptionsTypeDef",
    {"Enabled": bool, "KmsKeyId": str},
    total=False,
)


class ClientDescribeElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsOptionsTypeDef(
    _ClientDescribeElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsOptionsTypeDef
):
    """
    Type definition for `ClientDescribeElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptions` `Options`

    Specifies the Encryption At Rest options for the specified Elasticsearch domain.

    - **Enabled** *(boolean) --*

      Specifies the option to enable Encryption At Rest.

    - **KmsKeyId** *(string) --*

      Specifies the KMS Key ID for Encryption At Rest options.
    """


_ClientDescribeElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsStatusTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": str,
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientDescribeElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsStatusTypeDef(
    _ClientDescribeElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsStatusTypeDef
):
    """
    Type definition for `ClientDescribeElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptions` `Status`

    Specifies the status of the Encryption At Rest options for the specified Elasticsearch
    domain.

    - **CreationDate** *(datetime) --*

      Timestamp which tells the creation date for the entity.

    - **UpdateDate** *(datetime) --*

      Timestamp which tells the last updated time for the entity.

    - **UpdateVersion** *(integer) --*

      Specifies the latest version for the entity.

    - **State** *(string) --*

      Provides the ``OptionState`` for the Elasticsearch domain.

    - **PendingDeletion** *(boolean) --*

      Indicates whether the Elasticsearch domain is being deleted.
    """


_ClientDescribeElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsTypeDef",
    {
        "Options": ClientDescribeElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsOptionsTypeDef,
        "Status": ClientDescribeElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsStatusTypeDef,
    },
    total=False,
)


class ClientDescribeElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsTypeDef(
    _ClientDescribeElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsTypeDef
):
    """
    Type definition for `ClientDescribeElasticsearchDomainConfigResponseDomainConfig` `EncryptionAtRestOptions`

    Specifies the ``EncryptionAtRestOptions`` for the Elasticsearch domain.

    - **Options** *(dict) --*

      Specifies the Encryption At Rest options for the specified Elasticsearch domain.

      - **Enabled** *(boolean) --*

        Specifies the option to enable Encryption At Rest.

      - **KmsKeyId** *(string) --*

        Specifies the KMS Key ID for Encryption At Rest options.

    - **Status** *(dict) --*

      Specifies the status of the Encryption At Rest options for the specified Elasticsearch
      domain.

      - **CreationDate** *(datetime) --*

        Timestamp which tells the creation date for the entity.

      - **UpdateDate** *(datetime) --*

        Timestamp which tells the last updated time for the entity.

      - **UpdateVersion** *(integer) --*

        Specifies the latest version for the entity.

      - **State** *(string) --*

        Provides the ``OptionState`` for the Elasticsearch domain.

      - **PendingDeletion** *(boolean) --*

        Indicates whether the Elasticsearch domain is being deleted.
    """


_ClientDescribeElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsOptionsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsOptionsTypeDef",
    {"CloudWatchLogsLogGroupArn": str, "Enabled": bool},
    total=False,
)


class ClientDescribeElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsOptionsTypeDef(
    _ClientDescribeElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsOptionsTypeDef
):
    """
    Type definition for `ClientDescribeElasticsearchDomainConfigResponseDomainConfigLogPublishingOptions` `Options`

    Log Publishing option that is set for given domain. Attributes and their details:

    * CloudWatchLogsLogGroupArn: ARN of the Cloudwatch log group to which log needs to be
    published.

    * Enabled: Whether the log publishing for given log type is enabled or not

    - **CloudWatchLogsLogGroupArn** *(string) --*

      ARN of the Cloudwatch log group to which log needs to be published.

    - **Enabled** *(boolean) --*

      Specifies whether given log publishing option is enabled or not.
    """


_ClientDescribeElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsStatusTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": str,
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientDescribeElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsStatusTypeDef(
    _ClientDescribeElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsStatusTypeDef
):
    """
    Type definition for `ClientDescribeElasticsearchDomainConfigResponseDomainConfigLogPublishingOptions` `Status`

    The status of the log publishing options for the Elasticsearch domain. See
    ``OptionStatus`` for the status information that's included.

    - **CreationDate** *(datetime) --*

      Timestamp which tells the creation date for the entity.

    - **UpdateDate** *(datetime) --*

      Timestamp which tells the last updated time for the entity.

    - **UpdateVersion** *(integer) --*

      Specifies the latest version for the entity.

    - **State** *(string) --*

      Provides the ``OptionState`` for the Elasticsearch domain.

    - **PendingDeletion** *(boolean) --*

      Indicates whether the Elasticsearch domain is being deleted.
    """


_ClientDescribeElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsTypeDef",
    {
        "Options": Dict[
            str,
            ClientDescribeElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsOptionsTypeDef,
        ],
        "Status": ClientDescribeElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsStatusTypeDef,
    },
    total=False,
)


class ClientDescribeElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsTypeDef(
    _ClientDescribeElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsTypeDef
):
    """
    Type definition for `ClientDescribeElasticsearchDomainConfigResponseDomainConfig` `LogPublishingOptions`

    Log publishing options for the given domain.

    - **Options** *(dict) --*

      The log publishing options configured for the Elasticsearch domain.

      - *(string) --*

        Type of Log File, it can be one of the following:

        * INDEX_SLOW_LOGS: Index slow logs contain insert requests that took more time than
        configured index query log threshold to execute.

        * SEARCH_SLOW_LOGS: Search slow logs contain search queries that took more time than
        configured search query log threshold to execute.

        * ES_APPLICATION_LOGS: Elasticsearch application logs contain information about errors
        and warnings raised during the operation of the service and can be useful for
        troubleshooting.

        - *(dict) --*

          Log Publishing option that is set for given domain. Attributes and their details:

          * CloudWatchLogsLogGroupArn: ARN of the Cloudwatch log group to which log needs to be
          published.

          * Enabled: Whether the log publishing for given log type is enabled or not

          - **CloudWatchLogsLogGroupArn** *(string) --*

            ARN of the Cloudwatch log group to which log needs to be published.

          - **Enabled** *(boolean) --*

            Specifies whether given log publishing option is enabled or not.

    - **Status** *(dict) --*

      The status of the log publishing options for the Elasticsearch domain. See
      ``OptionStatus`` for the status information that's included.

      - **CreationDate** *(datetime) --*

        Timestamp which tells the creation date for the entity.

      - **UpdateDate** *(datetime) --*

        Timestamp which tells the last updated time for the entity.

      - **UpdateVersion** *(integer) --*

        Specifies the latest version for the entity.

      - **State** *(string) --*

        Provides the ``OptionState`` for the Elasticsearch domain.

      - **PendingDeletion** *(boolean) --*

        Indicates whether the Elasticsearch domain is being deleted.
    """


_ClientDescribeElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsOptionsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsOptionsTypeDef",
    {"Enabled": bool},
    total=False,
)


class ClientDescribeElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsOptionsTypeDef(
    _ClientDescribeElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsOptionsTypeDef
):
    """
    Type definition for `ClientDescribeElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptions` `Options`

    Specifies the node-to-node encryption options for the specified Elasticsearch domain.

    - **Enabled** *(boolean) --*

      Specify true to enable node-to-node encryption.
    """


_ClientDescribeElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsStatusTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": str,
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientDescribeElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsStatusTypeDef(
    _ClientDescribeElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsStatusTypeDef
):
    """
    Type definition for `ClientDescribeElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptions` `Status`

    Specifies the status of the node-to-node encryption options for the specified
    Elasticsearch domain.

    - **CreationDate** *(datetime) --*

      Timestamp which tells the creation date for the entity.

    - **UpdateDate** *(datetime) --*

      Timestamp which tells the last updated time for the entity.

    - **UpdateVersion** *(integer) --*

      Specifies the latest version for the entity.

    - **State** *(string) --*

      Provides the ``OptionState`` for the Elasticsearch domain.

    - **PendingDeletion** *(boolean) --*

      Indicates whether the Elasticsearch domain is being deleted.
    """


_ClientDescribeElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsTypeDef",
    {
        "Options": ClientDescribeElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsOptionsTypeDef,
        "Status": ClientDescribeElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsStatusTypeDef,
    },
    total=False,
)


class ClientDescribeElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsTypeDef(
    _ClientDescribeElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsTypeDef
):
    """
    Type definition for `ClientDescribeElasticsearchDomainConfigResponseDomainConfig` `NodeToNodeEncryptionOptions`

    Specifies the ``NodeToNodeEncryptionOptions`` for the Elasticsearch domain.

    - **Options** *(dict) --*

      Specifies the node-to-node encryption options for the specified Elasticsearch domain.

      - **Enabled** *(boolean) --*

        Specify true to enable node-to-node encryption.

    - **Status** *(dict) --*

      Specifies the status of the node-to-node encryption options for the specified
      Elasticsearch domain.

      - **CreationDate** *(datetime) --*

        Timestamp which tells the creation date for the entity.

      - **UpdateDate** *(datetime) --*

        Timestamp which tells the last updated time for the entity.

      - **UpdateVersion** *(integer) --*

        Specifies the latest version for the entity.

      - **State** *(string) --*

        Provides the ``OptionState`` for the Elasticsearch domain.

      - **PendingDeletion** *(boolean) --*

        Indicates whether the Elasticsearch domain is being deleted.
    """


_ClientDescribeElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsOptionsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsOptionsTypeDef",
    {"AutomatedSnapshotStartHour": int},
    total=False,
)


class ClientDescribeElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsOptionsTypeDef(
    _ClientDescribeElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsOptionsTypeDef
):
    """
    Type definition for `ClientDescribeElasticsearchDomainConfigResponseDomainConfigSnapshotOptions` `Options`

    Specifies the daily snapshot options specified for the Elasticsearch domain.

    - **AutomatedSnapshotStartHour** *(integer) --*

      Specifies the time, in UTC format, when the service takes a daily automated snapshot of
      the specified Elasticsearch domain. Default value is ``0`` hours.
    """


_ClientDescribeElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsStatusTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": str,
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientDescribeElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsStatusTypeDef(
    _ClientDescribeElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsStatusTypeDef
):
    """
    Type definition for `ClientDescribeElasticsearchDomainConfigResponseDomainConfigSnapshotOptions` `Status`

    Specifies the status of a daily automated snapshot.

    - **CreationDate** *(datetime) --*

      Timestamp which tells the creation date for the entity.

    - **UpdateDate** *(datetime) --*

      Timestamp which tells the last updated time for the entity.

    - **UpdateVersion** *(integer) --*

      Specifies the latest version for the entity.

    - **State** *(string) --*

      Provides the ``OptionState`` for the Elasticsearch domain.

    - **PendingDeletion** *(boolean) --*

      Indicates whether the Elasticsearch domain is being deleted.
    """


_ClientDescribeElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsTypeDef",
    {
        "Options": ClientDescribeElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsOptionsTypeDef,
        "Status": ClientDescribeElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsStatusTypeDef,
    },
    total=False,
)


class ClientDescribeElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsTypeDef(
    _ClientDescribeElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsTypeDef
):
    """
    Type definition for `ClientDescribeElasticsearchDomainConfigResponseDomainConfig` `SnapshotOptions`

    Specifies the ``SnapshotOptions`` for the Elasticsearch domain.

    - **Options** *(dict) --*

      Specifies the daily snapshot options specified for the Elasticsearch domain.

      - **AutomatedSnapshotStartHour** *(integer) --*

        Specifies the time, in UTC format, when the service takes a daily automated snapshot of
        the specified Elasticsearch domain. Default value is ``0`` hours.

    - **Status** *(dict) --*

      Specifies the status of a daily automated snapshot.

      - **CreationDate** *(datetime) --*

        Timestamp which tells the creation date for the entity.

      - **UpdateDate** *(datetime) --*

        Timestamp which tells the last updated time for the entity.

      - **UpdateVersion** *(integer) --*

        Specifies the latest version for the entity.

      - **State** *(string) --*

        Provides the ``OptionState`` for the Elasticsearch domain.

      - **PendingDeletion** *(boolean) --*

        Indicates whether the Elasticsearch domain is being deleted.
    """


_ClientDescribeElasticsearchDomainConfigResponseDomainConfigVPCOptionsOptionsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainConfigResponseDomainConfigVPCOptionsOptionsTypeDef",
    {
        "VPCId": str,
        "SubnetIds": List[str],
        "AvailabilityZones": List[str],
        "SecurityGroupIds": List[str],
    },
    total=False,
)


class ClientDescribeElasticsearchDomainConfigResponseDomainConfigVPCOptionsOptionsTypeDef(
    _ClientDescribeElasticsearchDomainConfigResponseDomainConfigVPCOptionsOptionsTypeDef
):
    """
    Type definition for `ClientDescribeElasticsearchDomainConfigResponseDomainConfigVPCOptions` `Options`

    Specifies the VPC options for the specified Elasticsearch domain.

    - **VPCId** *(string) --*

      The VPC Id for the Elasticsearch domain. Exists only if the domain was created with
      VPCOptions.

    - **SubnetIds** *(list) --*

      Specifies the subnets for VPC endpoint.

      - *(string) --*

    - **AvailabilityZones** *(list) --*

      The availability zones for the Elasticsearch domain. Exists only if the domain was
      created with VPCOptions.

      - *(string) --*

    - **SecurityGroupIds** *(list) --*

      Specifies the security groups for VPC endpoint.

      - *(string) --*
    """


_ClientDescribeElasticsearchDomainConfigResponseDomainConfigVPCOptionsStatusTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainConfigResponseDomainConfigVPCOptionsStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": str,
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientDescribeElasticsearchDomainConfigResponseDomainConfigVPCOptionsStatusTypeDef(
    _ClientDescribeElasticsearchDomainConfigResponseDomainConfigVPCOptionsStatusTypeDef
):
    """
    Type definition for `ClientDescribeElasticsearchDomainConfigResponseDomainConfigVPCOptions` `Status`

    Specifies the status of the VPC options for the specified Elasticsearch domain.

    - **CreationDate** *(datetime) --*

      Timestamp which tells the creation date for the entity.

    - **UpdateDate** *(datetime) --*

      Timestamp which tells the last updated time for the entity.

    - **UpdateVersion** *(integer) --*

      Specifies the latest version for the entity.

    - **State** *(string) --*

      Provides the ``OptionState`` for the Elasticsearch domain.

    - **PendingDeletion** *(boolean) --*

      Indicates whether the Elasticsearch domain is being deleted.
    """


_ClientDescribeElasticsearchDomainConfigResponseDomainConfigVPCOptionsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainConfigResponseDomainConfigVPCOptionsTypeDef",
    {
        "Options": ClientDescribeElasticsearchDomainConfigResponseDomainConfigVPCOptionsOptionsTypeDef,
        "Status": ClientDescribeElasticsearchDomainConfigResponseDomainConfigVPCOptionsStatusTypeDef,
    },
    total=False,
)


class ClientDescribeElasticsearchDomainConfigResponseDomainConfigVPCOptionsTypeDef(
    _ClientDescribeElasticsearchDomainConfigResponseDomainConfigVPCOptionsTypeDef
):
    """
    Type definition for `ClientDescribeElasticsearchDomainConfigResponseDomainConfig` `VPCOptions`

    The ``VPCOptions`` for the specified domain. For more information, see `VPC Endpoints for
    Amazon Elasticsearch Service Domains
    <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html>`__ .

    - **Options** *(dict) --*

      Specifies the VPC options for the specified Elasticsearch domain.

      - **VPCId** *(string) --*

        The VPC Id for the Elasticsearch domain. Exists only if the domain was created with
        VPCOptions.

      - **SubnetIds** *(list) --*

        Specifies the subnets for VPC endpoint.

        - *(string) --*

      - **AvailabilityZones** *(list) --*

        The availability zones for the Elasticsearch domain. Exists only if the domain was
        created with VPCOptions.

        - *(string) --*

      - **SecurityGroupIds** *(list) --*

        Specifies the security groups for VPC endpoint.

        - *(string) --*

    - **Status** *(dict) --*

      Specifies the status of the VPC options for the specified Elasticsearch domain.

      - **CreationDate** *(datetime) --*

        Timestamp which tells the creation date for the entity.

      - **UpdateDate** *(datetime) --*

        Timestamp which tells the last updated time for the entity.

      - **UpdateVersion** *(integer) --*

        Specifies the latest version for the entity.

      - **State** *(string) --*

        Provides the ``OptionState`` for the Elasticsearch domain.

      - **PendingDeletion** *(boolean) --*

        Indicates whether the Elasticsearch domain is being deleted.
    """


_ClientDescribeElasticsearchDomainConfigResponseDomainConfigTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainConfigResponseDomainConfigTypeDef",
    {
        "ElasticsearchVersion": ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchVersionTypeDef,
        "ElasticsearchClusterConfig": ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigTypeDef,
        "EBSOptions": ClientDescribeElasticsearchDomainConfigResponseDomainConfigEBSOptionsTypeDef,
        "AccessPolicies": ClientDescribeElasticsearchDomainConfigResponseDomainConfigAccessPoliciesTypeDef,
        "SnapshotOptions": ClientDescribeElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsTypeDef,
        "VPCOptions": ClientDescribeElasticsearchDomainConfigResponseDomainConfigVPCOptionsTypeDef,
        "CognitoOptions": ClientDescribeElasticsearchDomainConfigResponseDomainConfigCognitoOptionsTypeDef,
        "EncryptionAtRestOptions": ClientDescribeElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsTypeDef,
        "NodeToNodeEncryptionOptions": ClientDescribeElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsTypeDef,
        "AdvancedOptions": ClientDescribeElasticsearchDomainConfigResponseDomainConfigAdvancedOptionsTypeDef,
        "LogPublishingOptions": ClientDescribeElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsTypeDef,
        "DomainEndpointOptions": ClientDescribeElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsTypeDef,
    },
    total=False,
)


class ClientDescribeElasticsearchDomainConfigResponseDomainConfigTypeDef(
    _ClientDescribeElasticsearchDomainConfigResponseDomainConfigTypeDef
):
    """
    Type definition for `ClientDescribeElasticsearchDomainConfigResponse` `DomainConfig`

    The configuration information of the domain requested in the
    ``DescribeElasticsearchDomainConfig`` request.

    - **ElasticsearchVersion** *(dict) --*

      String of format X.Y to specify version for the Elasticsearch domain.

      - **Options** *(string) --*

        Specifies the Elasticsearch version for the specified Elasticsearch domain.

      - **Status** *(dict) --*

        Specifies the status of the Elasticsearch version options for the specified Elasticsearch
        domain.

        - **CreationDate** *(datetime) --*

          Timestamp which tells the creation date for the entity.

        - **UpdateDate** *(datetime) --*

          Timestamp which tells the last updated time for the entity.

        - **UpdateVersion** *(integer) --*

          Specifies the latest version for the entity.

        - **State** *(string) --*

          Provides the ``OptionState`` for the Elasticsearch domain.

        - **PendingDeletion** *(boolean) --*

          Indicates whether the Elasticsearch domain is being deleted.

    - **ElasticsearchClusterConfig** *(dict) --*

      Specifies the ``ElasticsearchClusterConfig`` for the Elasticsearch domain.

      - **Options** *(dict) --*

        Specifies the cluster configuration for the specified Elasticsearch domain.

        - **InstanceType** *(string) --*

          The instance type for an Elasticsearch cluster.

        - **InstanceCount** *(integer) --*

          The number of instances in the specified domain cluster.

        - **DedicatedMasterEnabled** *(boolean) --*

          A boolean value to indicate whether a dedicated master node is enabled. See `About
          Dedicated Master Nodes
          <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains.html#es-managedomains-dedicatedmasternodes>`__
          for more information.

        - **ZoneAwarenessEnabled** *(boolean) --*

          A boolean value to indicate whether zone awareness is enabled. See `About Zone
          Awareness
          <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains.html#es-managedomains-zoneawareness>`__
          for more information.

        - **ZoneAwarenessConfig** *(dict) --*

          Specifies the zone awareness configuration for a domain when zone awareness is enabled.

          - **AvailabilityZoneCount** *(integer) --*

            An integer value to indicate the number of availability zones for a domain when zone
            awareness is enabled. This should be equal to number of subnets if VPC endpoints is
            enabled

        - **DedicatedMasterType** *(string) --*

          The instance type for a dedicated master node.

        - **DedicatedMasterCount** *(integer) --*

          Total number of dedicated master nodes, active and on standby, for the cluster.

      - **Status** *(dict) --*

        Specifies the status of the configuration for the specified Elasticsearch domain.

        - **CreationDate** *(datetime) --*

          Timestamp which tells the creation date for the entity.

        - **UpdateDate** *(datetime) --*

          Timestamp which tells the last updated time for the entity.

        - **UpdateVersion** *(integer) --*

          Specifies the latest version for the entity.

        - **State** *(string) --*

          Provides the ``OptionState`` for the Elasticsearch domain.

        - **PendingDeletion** *(boolean) --*

          Indicates whether the Elasticsearch domain is being deleted.

    - **EBSOptions** *(dict) --*

      Specifies the ``EBSOptions`` for the Elasticsearch domain.

      - **Options** *(dict) --*

        Specifies the EBS options for the specified Elasticsearch domain.

        - **EBSEnabled** *(boolean) --*

          Specifies whether EBS-based storage is enabled.

        - **VolumeType** *(string) --*

          Specifies the volume type for EBS-based storage.

        - **VolumeSize** *(integer) --*

          Integer to specify the size of an EBS volume.

        - **Iops** *(integer) --*

          Specifies the IOPD for a Provisioned IOPS EBS volume (SSD).

      - **Status** *(dict) --*

        Specifies the status of the EBS options for the specified Elasticsearch domain.

        - **CreationDate** *(datetime) --*

          Timestamp which tells the creation date for the entity.

        - **UpdateDate** *(datetime) --*

          Timestamp which tells the last updated time for the entity.

        - **UpdateVersion** *(integer) --*

          Specifies the latest version for the entity.

        - **State** *(string) --*

          Provides the ``OptionState`` for the Elasticsearch domain.

        - **PendingDeletion** *(boolean) --*

          Indicates whether the Elasticsearch domain is being deleted.

    - **AccessPolicies** *(dict) --*

      IAM access policy as a JSON-formatted string.

      - **Options** *(string) --*

        The access policy configured for the Elasticsearch domain. Access policies may be
        resource-based, IP-based, or IAM-based. See `Configuring Access Policies
        <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html#es-createdomain-configure-access-policies>`__
        for more information.

      - **Status** *(dict) --*

        The status of the access policy for the Elasticsearch domain. See ``OptionStatus`` for
        the status information that's included.

        - **CreationDate** *(datetime) --*

          Timestamp which tells the creation date for the entity.

        - **UpdateDate** *(datetime) --*

          Timestamp which tells the last updated time for the entity.

        - **UpdateVersion** *(integer) --*

          Specifies the latest version for the entity.

        - **State** *(string) --*

          Provides the ``OptionState`` for the Elasticsearch domain.

        - **PendingDeletion** *(boolean) --*

          Indicates whether the Elasticsearch domain is being deleted.

    - **SnapshotOptions** *(dict) --*

      Specifies the ``SnapshotOptions`` for the Elasticsearch domain.

      - **Options** *(dict) --*

        Specifies the daily snapshot options specified for the Elasticsearch domain.

        - **AutomatedSnapshotStartHour** *(integer) --*

          Specifies the time, in UTC format, when the service takes a daily automated snapshot of
          the specified Elasticsearch domain. Default value is ``0`` hours.

      - **Status** *(dict) --*

        Specifies the status of a daily automated snapshot.

        - **CreationDate** *(datetime) --*

          Timestamp which tells the creation date for the entity.

        - **UpdateDate** *(datetime) --*

          Timestamp which tells the last updated time for the entity.

        - **UpdateVersion** *(integer) --*

          Specifies the latest version for the entity.

        - **State** *(string) --*

          Provides the ``OptionState`` for the Elasticsearch domain.

        - **PendingDeletion** *(boolean) --*

          Indicates whether the Elasticsearch domain is being deleted.

    - **VPCOptions** *(dict) --*

      The ``VPCOptions`` for the specified domain. For more information, see `VPC Endpoints for
      Amazon Elasticsearch Service Domains
      <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html>`__ .

      - **Options** *(dict) --*

        Specifies the VPC options for the specified Elasticsearch domain.

        - **VPCId** *(string) --*

          The VPC Id for the Elasticsearch domain. Exists only if the domain was created with
          VPCOptions.

        - **SubnetIds** *(list) --*

          Specifies the subnets for VPC endpoint.

          - *(string) --*

        - **AvailabilityZones** *(list) --*

          The availability zones for the Elasticsearch domain. Exists only if the domain was
          created with VPCOptions.

          - *(string) --*

        - **SecurityGroupIds** *(list) --*

          Specifies the security groups for VPC endpoint.

          - *(string) --*

      - **Status** *(dict) --*

        Specifies the status of the VPC options for the specified Elasticsearch domain.

        - **CreationDate** *(datetime) --*

          Timestamp which tells the creation date for the entity.

        - **UpdateDate** *(datetime) --*

          Timestamp which tells the last updated time for the entity.

        - **UpdateVersion** *(integer) --*

          Specifies the latest version for the entity.

        - **State** *(string) --*

          Provides the ``OptionState`` for the Elasticsearch domain.

        - **PendingDeletion** *(boolean) --*

          Indicates whether the Elasticsearch domain is being deleted.

    - **CognitoOptions** *(dict) --*

      The ``CognitoOptions`` for the specified domain. For more information, see `Amazon Cognito
      Authentication for Kibana
      <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-cognito-auth.html>`__
      .

      - **Options** *(dict) --*

        Specifies the Cognito options for the specified Elasticsearch domain.

        - **Enabled** *(boolean) --*

          Specifies the option to enable Cognito for Kibana authentication.

        - **UserPoolId** *(string) --*

          Specifies the Cognito user pool ID for Kibana authentication.

        - **IdentityPoolId** *(string) --*

          Specifies the Cognito identity pool ID for Kibana authentication.

        - **RoleArn** *(string) --*

          Specifies the role ARN that provides Elasticsearch permissions for accessing Cognito
          resources.

      - **Status** *(dict) --*

        Specifies the status of the Cognito options for the specified Elasticsearch domain.

        - **CreationDate** *(datetime) --*

          Timestamp which tells the creation date for the entity.

        - **UpdateDate** *(datetime) --*

          Timestamp which tells the last updated time for the entity.

        - **UpdateVersion** *(integer) --*

          Specifies the latest version for the entity.

        - **State** *(string) --*

          Provides the ``OptionState`` for the Elasticsearch domain.

        - **PendingDeletion** *(boolean) --*

          Indicates whether the Elasticsearch domain is being deleted.

    - **EncryptionAtRestOptions** *(dict) --*

      Specifies the ``EncryptionAtRestOptions`` for the Elasticsearch domain.

      - **Options** *(dict) --*

        Specifies the Encryption At Rest options for the specified Elasticsearch domain.

        - **Enabled** *(boolean) --*

          Specifies the option to enable Encryption At Rest.

        - **KmsKeyId** *(string) --*

          Specifies the KMS Key ID for Encryption At Rest options.

      - **Status** *(dict) --*

        Specifies the status of the Encryption At Rest options for the specified Elasticsearch
        domain.

        - **CreationDate** *(datetime) --*

          Timestamp which tells the creation date for the entity.

        - **UpdateDate** *(datetime) --*

          Timestamp which tells the last updated time for the entity.

        - **UpdateVersion** *(integer) --*

          Specifies the latest version for the entity.

        - **State** *(string) --*

          Provides the ``OptionState`` for the Elasticsearch domain.

        - **PendingDeletion** *(boolean) --*

          Indicates whether the Elasticsearch domain is being deleted.

    - **NodeToNodeEncryptionOptions** *(dict) --*

      Specifies the ``NodeToNodeEncryptionOptions`` for the Elasticsearch domain.

      - **Options** *(dict) --*

        Specifies the node-to-node encryption options for the specified Elasticsearch domain.

        - **Enabled** *(boolean) --*

          Specify true to enable node-to-node encryption.

      - **Status** *(dict) --*

        Specifies the status of the node-to-node encryption options for the specified
        Elasticsearch domain.

        - **CreationDate** *(datetime) --*

          Timestamp which tells the creation date for the entity.

        - **UpdateDate** *(datetime) --*

          Timestamp which tells the last updated time for the entity.

        - **UpdateVersion** *(integer) --*

          Specifies the latest version for the entity.

        - **State** *(string) --*

          Provides the ``OptionState`` for the Elasticsearch domain.

        - **PendingDeletion** *(boolean) --*

          Indicates whether the Elasticsearch domain is being deleted.

    - **AdvancedOptions** *(dict) --*

      Specifies the ``AdvancedOptions`` for the domain. See `Configuring Advanced Options
      <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html#es-createdomain-configure-advanced-options>`__
      for more information.

      - **Options** *(dict) --*

        Specifies the status of advanced options for the specified Elasticsearch domain.

        - *(string) --*

          - *(string) --*

      - **Status** *(dict) --*

        Specifies the status of ``OptionStatus`` for advanced options for the specified
        Elasticsearch domain.

        - **CreationDate** *(datetime) --*

          Timestamp which tells the creation date for the entity.

        - **UpdateDate** *(datetime) --*

          Timestamp which tells the last updated time for the entity.

        - **UpdateVersion** *(integer) --*

          Specifies the latest version for the entity.

        - **State** *(string) --*

          Provides the ``OptionState`` for the Elasticsearch domain.

        - **PendingDeletion** *(boolean) --*

          Indicates whether the Elasticsearch domain is being deleted.

    - **LogPublishingOptions** *(dict) --*

      Log publishing options for the given domain.

      - **Options** *(dict) --*

        The log publishing options configured for the Elasticsearch domain.

        - *(string) --*

          Type of Log File, it can be one of the following:

          * INDEX_SLOW_LOGS: Index slow logs contain insert requests that took more time than
          configured index query log threshold to execute.

          * SEARCH_SLOW_LOGS: Search slow logs contain search queries that took more time than
          configured search query log threshold to execute.

          * ES_APPLICATION_LOGS: Elasticsearch application logs contain information about errors
          and warnings raised during the operation of the service and can be useful for
          troubleshooting.

          - *(dict) --*

            Log Publishing option that is set for given domain. Attributes and their details:

            * CloudWatchLogsLogGroupArn: ARN of the Cloudwatch log group to which log needs to be
            published.

            * Enabled: Whether the log publishing for given log type is enabled or not

            - **CloudWatchLogsLogGroupArn** *(string) --*

              ARN of the Cloudwatch log group to which log needs to be published.

            - **Enabled** *(boolean) --*

              Specifies whether given log publishing option is enabled or not.

      - **Status** *(dict) --*

        The status of the log publishing options for the Elasticsearch domain. See
        ``OptionStatus`` for the status information that's included.

        - **CreationDate** *(datetime) --*

          Timestamp which tells the creation date for the entity.

        - **UpdateDate** *(datetime) --*

          Timestamp which tells the last updated time for the entity.

        - **UpdateVersion** *(integer) --*

          Specifies the latest version for the entity.

        - **State** *(string) --*

          Provides the ``OptionState`` for the Elasticsearch domain.

        - **PendingDeletion** *(boolean) --*

          Indicates whether the Elasticsearch domain is being deleted.

    - **DomainEndpointOptions** *(dict) --*

      Specifies the ``DomainEndpointOptions`` for the Elasticsearch domain.

      - **Options** *(dict) --*

        Options to configure endpoint for the Elasticsearch domain.

        - **EnforceHTTPS** *(boolean) --*

          Specify if only HTTPS endpoint should be enabled for the Elasticsearch domain.

        - **TLSSecurityPolicy** *(string) --*

          Specify the TLS security policy that needs to be applied to the HTTPS endpoint of
          Elasticsearch domain. It can be one of the following values:

          * **Policy-Min-TLS-1-0-2019-07:** TLS security policy which supports TLSv1.0 and higher.

          * **Policy-Min-TLS-1-2-2019-07:** TLS security policy which supports only TLSv1.2

      - **Status** *(dict) --*

        The status of the endpoint options for the Elasticsearch domain. See ``OptionStatus`` for
        the status information that's included.

        - **CreationDate** *(datetime) --*

          Timestamp which tells the creation date for the entity.

        - **UpdateDate** *(datetime) --*

          Timestamp which tells the last updated time for the entity.

        - **UpdateVersion** *(integer) --*

          Specifies the latest version for the entity.

        - **State** *(string) --*

          Provides the ``OptionState`` for the Elasticsearch domain.

        - **PendingDeletion** *(boolean) --*

          Indicates whether the Elasticsearch domain is being deleted.
    """


_ClientDescribeElasticsearchDomainConfigResponseTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainConfigResponseTypeDef",
    {
        "DomainConfig": ClientDescribeElasticsearchDomainConfigResponseDomainConfigTypeDef
    },
    total=False,
)


class ClientDescribeElasticsearchDomainConfigResponseTypeDef(
    _ClientDescribeElasticsearchDomainConfigResponseTypeDef
):
    """
    Type definition for `ClientDescribeElasticsearchDomainConfig` `Response`

    The result of a ``DescribeElasticsearchDomainConfig`` request. Contains the configuration
    information of the requested domain.

    - **DomainConfig** *(dict) --*

      The configuration information of the domain requested in the
      ``DescribeElasticsearchDomainConfig`` request.

      - **ElasticsearchVersion** *(dict) --*

        String of format X.Y to specify version for the Elasticsearch domain.

        - **Options** *(string) --*

          Specifies the Elasticsearch version for the specified Elasticsearch domain.

        - **Status** *(dict) --*

          Specifies the status of the Elasticsearch version options for the specified Elasticsearch
          domain.

          - **CreationDate** *(datetime) --*

            Timestamp which tells the creation date for the entity.

          - **UpdateDate** *(datetime) --*

            Timestamp which tells the last updated time for the entity.

          - **UpdateVersion** *(integer) --*

            Specifies the latest version for the entity.

          - **State** *(string) --*

            Provides the ``OptionState`` for the Elasticsearch domain.

          - **PendingDeletion** *(boolean) --*

            Indicates whether the Elasticsearch domain is being deleted.

      - **ElasticsearchClusterConfig** *(dict) --*

        Specifies the ``ElasticsearchClusterConfig`` for the Elasticsearch domain.

        - **Options** *(dict) --*

          Specifies the cluster configuration for the specified Elasticsearch domain.

          - **InstanceType** *(string) --*

            The instance type for an Elasticsearch cluster.

          - **InstanceCount** *(integer) --*

            The number of instances in the specified domain cluster.

          - **DedicatedMasterEnabled** *(boolean) --*

            A boolean value to indicate whether a dedicated master node is enabled. See `About
            Dedicated Master Nodes
            <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains.html#es-managedomains-dedicatedmasternodes>`__
            for more information.

          - **ZoneAwarenessEnabled** *(boolean) --*

            A boolean value to indicate whether zone awareness is enabled. See `About Zone
            Awareness
            <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains.html#es-managedomains-zoneawareness>`__
            for more information.

          - **ZoneAwarenessConfig** *(dict) --*

            Specifies the zone awareness configuration for a domain when zone awareness is enabled.

            - **AvailabilityZoneCount** *(integer) --*

              An integer value to indicate the number of availability zones for a domain when zone
              awareness is enabled. This should be equal to number of subnets if VPC endpoints is
              enabled

          - **DedicatedMasterType** *(string) --*

            The instance type for a dedicated master node.

          - **DedicatedMasterCount** *(integer) --*

            Total number of dedicated master nodes, active and on standby, for the cluster.

        - **Status** *(dict) --*

          Specifies the status of the configuration for the specified Elasticsearch domain.

          - **CreationDate** *(datetime) --*

            Timestamp which tells the creation date for the entity.

          - **UpdateDate** *(datetime) --*

            Timestamp which tells the last updated time for the entity.

          - **UpdateVersion** *(integer) --*

            Specifies the latest version for the entity.

          - **State** *(string) --*

            Provides the ``OptionState`` for the Elasticsearch domain.

          - **PendingDeletion** *(boolean) --*

            Indicates whether the Elasticsearch domain is being deleted.

      - **EBSOptions** *(dict) --*

        Specifies the ``EBSOptions`` for the Elasticsearch domain.

        - **Options** *(dict) --*

          Specifies the EBS options for the specified Elasticsearch domain.

          - **EBSEnabled** *(boolean) --*

            Specifies whether EBS-based storage is enabled.

          - **VolumeType** *(string) --*

            Specifies the volume type for EBS-based storage.

          - **VolumeSize** *(integer) --*

            Integer to specify the size of an EBS volume.

          - **Iops** *(integer) --*

            Specifies the IOPD for a Provisioned IOPS EBS volume (SSD).

        - **Status** *(dict) --*

          Specifies the status of the EBS options for the specified Elasticsearch domain.

          - **CreationDate** *(datetime) --*

            Timestamp which tells the creation date for the entity.

          - **UpdateDate** *(datetime) --*

            Timestamp which tells the last updated time for the entity.

          - **UpdateVersion** *(integer) --*

            Specifies the latest version for the entity.

          - **State** *(string) --*

            Provides the ``OptionState`` for the Elasticsearch domain.

          - **PendingDeletion** *(boolean) --*

            Indicates whether the Elasticsearch domain is being deleted.

      - **AccessPolicies** *(dict) --*

        IAM access policy as a JSON-formatted string.

        - **Options** *(string) --*

          The access policy configured for the Elasticsearch domain. Access policies may be
          resource-based, IP-based, or IAM-based. See `Configuring Access Policies
          <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html#es-createdomain-configure-access-policies>`__
          for more information.

        - **Status** *(dict) --*

          The status of the access policy for the Elasticsearch domain. See ``OptionStatus`` for
          the status information that's included.

          - **CreationDate** *(datetime) --*

            Timestamp which tells the creation date for the entity.

          - **UpdateDate** *(datetime) --*

            Timestamp which tells the last updated time for the entity.

          - **UpdateVersion** *(integer) --*

            Specifies the latest version for the entity.

          - **State** *(string) --*

            Provides the ``OptionState`` for the Elasticsearch domain.

          - **PendingDeletion** *(boolean) --*

            Indicates whether the Elasticsearch domain is being deleted.

      - **SnapshotOptions** *(dict) --*

        Specifies the ``SnapshotOptions`` for the Elasticsearch domain.

        - **Options** *(dict) --*

          Specifies the daily snapshot options specified for the Elasticsearch domain.

          - **AutomatedSnapshotStartHour** *(integer) --*

            Specifies the time, in UTC format, when the service takes a daily automated snapshot of
            the specified Elasticsearch domain. Default value is ``0`` hours.

        - **Status** *(dict) --*

          Specifies the status of a daily automated snapshot.

          - **CreationDate** *(datetime) --*

            Timestamp which tells the creation date for the entity.

          - **UpdateDate** *(datetime) --*

            Timestamp which tells the last updated time for the entity.

          - **UpdateVersion** *(integer) --*

            Specifies the latest version for the entity.

          - **State** *(string) --*

            Provides the ``OptionState`` for the Elasticsearch domain.

          - **PendingDeletion** *(boolean) --*

            Indicates whether the Elasticsearch domain is being deleted.

      - **VPCOptions** *(dict) --*

        The ``VPCOptions`` for the specified domain. For more information, see `VPC Endpoints for
        Amazon Elasticsearch Service Domains
        <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html>`__ .

        - **Options** *(dict) --*

          Specifies the VPC options for the specified Elasticsearch domain.

          - **VPCId** *(string) --*

            The VPC Id for the Elasticsearch domain. Exists only if the domain was created with
            VPCOptions.

          - **SubnetIds** *(list) --*

            Specifies the subnets for VPC endpoint.

            - *(string) --*

          - **AvailabilityZones** *(list) --*

            The availability zones for the Elasticsearch domain. Exists only if the domain was
            created with VPCOptions.

            - *(string) --*

          - **SecurityGroupIds** *(list) --*

            Specifies the security groups for VPC endpoint.

            - *(string) --*

        - **Status** *(dict) --*

          Specifies the status of the VPC options for the specified Elasticsearch domain.

          - **CreationDate** *(datetime) --*

            Timestamp which tells the creation date for the entity.

          - **UpdateDate** *(datetime) --*

            Timestamp which tells the last updated time for the entity.

          - **UpdateVersion** *(integer) --*

            Specifies the latest version for the entity.

          - **State** *(string) --*

            Provides the ``OptionState`` for the Elasticsearch domain.

          - **PendingDeletion** *(boolean) --*

            Indicates whether the Elasticsearch domain is being deleted.

      - **CognitoOptions** *(dict) --*

        The ``CognitoOptions`` for the specified domain. For more information, see `Amazon Cognito
        Authentication for Kibana
        <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-cognito-auth.html>`__
        .

        - **Options** *(dict) --*

          Specifies the Cognito options for the specified Elasticsearch domain.

          - **Enabled** *(boolean) --*

            Specifies the option to enable Cognito for Kibana authentication.

          - **UserPoolId** *(string) --*

            Specifies the Cognito user pool ID for Kibana authentication.

          - **IdentityPoolId** *(string) --*

            Specifies the Cognito identity pool ID for Kibana authentication.

          - **RoleArn** *(string) --*

            Specifies the role ARN that provides Elasticsearch permissions for accessing Cognito
            resources.

        - **Status** *(dict) --*

          Specifies the status of the Cognito options for the specified Elasticsearch domain.

          - **CreationDate** *(datetime) --*

            Timestamp which tells the creation date for the entity.

          - **UpdateDate** *(datetime) --*

            Timestamp which tells the last updated time for the entity.

          - **UpdateVersion** *(integer) --*

            Specifies the latest version for the entity.

          - **State** *(string) --*

            Provides the ``OptionState`` for the Elasticsearch domain.

          - **PendingDeletion** *(boolean) --*

            Indicates whether the Elasticsearch domain is being deleted.

      - **EncryptionAtRestOptions** *(dict) --*

        Specifies the ``EncryptionAtRestOptions`` for the Elasticsearch domain.

        - **Options** *(dict) --*

          Specifies the Encryption At Rest options for the specified Elasticsearch domain.

          - **Enabled** *(boolean) --*

            Specifies the option to enable Encryption At Rest.

          - **KmsKeyId** *(string) --*

            Specifies the KMS Key ID for Encryption At Rest options.

        - **Status** *(dict) --*

          Specifies the status of the Encryption At Rest options for the specified Elasticsearch
          domain.

          - **CreationDate** *(datetime) --*

            Timestamp which tells the creation date for the entity.

          - **UpdateDate** *(datetime) --*

            Timestamp which tells the last updated time for the entity.

          - **UpdateVersion** *(integer) --*

            Specifies the latest version for the entity.

          - **State** *(string) --*

            Provides the ``OptionState`` for the Elasticsearch domain.

          - **PendingDeletion** *(boolean) --*

            Indicates whether the Elasticsearch domain is being deleted.

      - **NodeToNodeEncryptionOptions** *(dict) --*

        Specifies the ``NodeToNodeEncryptionOptions`` for the Elasticsearch domain.

        - **Options** *(dict) --*

          Specifies the node-to-node encryption options for the specified Elasticsearch domain.

          - **Enabled** *(boolean) --*

            Specify true to enable node-to-node encryption.

        - **Status** *(dict) --*

          Specifies the status of the node-to-node encryption options for the specified
          Elasticsearch domain.

          - **CreationDate** *(datetime) --*

            Timestamp which tells the creation date for the entity.

          - **UpdateDate** *(datetime) --*

            Timestamp which tells the last updated time for the entity.

          - **UpdateVersion** *(integer) --*

            Specifies the latest version for the entity.

          - **State** *(string) --*

            Provides the ``OptionState`` for the Elasticsearch domain.

          - **PendingDeletion** *(boolean) --*

            Indicates whether the Elasticsearch domain is being deleted.

      - **AdvancedOptions** *(dict) --*

        Specifies the ``AdvancedOptions`` for the domain. See `Configuring Advanced Options
        <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html#es-createdomain-configure-advanced-options>`__
        for more information.

        - **Options** *(dict) --*

          Specifies the status of advanced options for the specified Elasticsearch domain.

          - *(string) --*

            - *(string) --*

        - **Status** *(dict) --*

          Specifies the status of ``OptionStatus`` for advanced options for the specified
          Elasticsearch domain.

          - **CreationDate** *(datetime) --*

            Timestamp which tells the creation date for the entity.

          - **UpdateDate** *(datetime) --*

            Timestamp which tells the last updated time for the entity.

          - **UpdateVersion** *(integer) --*

            Specifies the latest version for the entity.

          - **State** *(string) --*

            Provides the ``OptionState`` for the Elasticsearch domain.

          - **PendingDeletion** *(boolean) --*

            Indicates whether the Elasticsearch domain is being deleted.

      - **LogPublishingOptions** *(dict) --*

        Log publishing options for the given domain.

        - **Options** *(dict) --*

          The log publishing options configured for the Elasticsearch domain.

          - *(string) --*

            Type of Log File, it can be one of the following:

            * INDEX_SLOW_LOGS: Index slow logs contain insert requests that took more time than
            configured index query log threshold to execute.

            * SEARCH_SLOW_LOGS: Search slow logs contain search queries that took more time than
            configured search query log threshold to execute.

            * ES_APPLICATION_LOGS: Elasticsearch application logs contain information about errors
            and warnings raised during the operation of the service and can be useful for
            troubleshooting.

            - *(dict) --*

              Log Publishing option that is set for given domain. Attributes and their details:

              * CloudWatchLogsLogGroupArn: ARN of the Cloudwatch log group to which log needs to be
              published.

              * Enabled: Whether the log publishing for given log type is enabled or not

              - **CloudWatchLogsLogGroupArn** *(string) --*

                ARN of the Cloudwatch log group to which log needs to be published.

              - **Enabled** *(boolean) --*

                Specifies whether given log publishing option is enabled or not.

        - **Status** *(dict) --*

          The status of the log publishing options for the Elasticsearch domain. See
          ``OptionStatus`` for the status information that's included.

          - **CreationDate** *(datetime) --*

            Timestamp which tells the creation date for the entity.

          - **UpdateDate** *(datetime) --*

            Timestamp which tells the last updated time for the entity.

          - **UpdateVersion** *(integer) --*

            Specifies the latest version for the entity.

          - **State** *(string) --*

            Provides the ``OptionState`` for the Elasticsearch domain.

          - **PendingDeletion** *(boolean) --*

            Indicates whether the Elasticsearch domain is being deleted.

      - **DomainEndpointOptions** *(dict) --*

        Specifies the ``DomainEndpointOptions`` for the Elasticsearch domain.

        - **Options** *(dict) --*

          Options to configure endpoint for the Elasticsearch domain.

          - **EnforceHTTPS** *(boolean) --*

            Specify if only HTTPS endpoint should be enabled for the Elasticsearch domain.

          - **TLSSecurityPolicy** *(string) --*

            Specify the TLS security policy that needs to be applied to the HTTPS endpoint of
            Elasticsearch domain. It can be one of the following values:

            * **Policy-Min-TLS-1-0-2019-07:** TLS security policy which supports TLSv1.0 and higher.

            * **Policy-Min-TLS-1-2-2019-07:** TLS security policy which supports only TLSv1.2

        - **Status** *(dict) --*

          The status of the endpoint options for the Elasticsearch domain. See ``OptionStatus`` for
          the status information that's included.

          - **CreationDate** *(datetime) --*

            Timestamp which tells the creation date for the entity.

          - **UpdateDate** *(datetime) --*

            Timestamp which tells the last updated time for the entity.

          - **UpdateVersion** *(integer) --*

            Specifies the latest version for the entity.

          - **State** *(string) --*

            Provides the ``OptionState`` for the Elasticsearch domain.

          - **PendingDeletion** *(boolean) --*

            Indicates whether the Elasticsearch domain is being deleted.
    """


_ClientDescribeElasticsearchDomainResponseDomainStatusCognitoOptionsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainResponseDomainStatusCognitoOptionsTypeDef",
    {"Enabled": bool, "UserPoolId": str, "IdentityPoolId": str, "RoleArn": str},
    total=False,
)


class ClientDescribeElasticsearchDomainResponseDomainStatusCognitoOptionsTypeDef(
    _ClientDescribeElasticsearchDomainResponseDomainStatusCognitoOptionsTypeDef
):
    """
    Type definition for `ClientDescribeElasticsearchDomainResponseDomainStatus` `CognitoOptions`

    The ``CognitoOptions`` for the specified domain. For more information, see `Amazon Cognito
    Authentication for Kibana
    <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-cognito-auth.html>`__
    .

    - **Enabled** *(boolean) --*

      Specifies the option to enable Cognito for Kibana authentication.

    - **UserPoolId** *(string) --*

      Specifies the Cognito user pool ID for Kibana authentication.

    - **IdentityPoolId** *(string) --*

      Specifies the Cognito identity pool ID for Kibana authentication.

    - **RoleArn** *(string) --*

      Specifies the role ARN that provides Elasticsearch permissions for accessing Cognito
      resources.
    """


_ClientDescribeElasticsearchDomainResponseDomainStatusDomainEndpointOptionsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainResponseDomainStatusDomainEndpointOptionsTypeDef",
    {"EnforceHTTPS": bool, "TLSSecurityPolicy": str},
    total=False,
)


class ClientDescribeElasticsearchDomainResponseDomainStatusDomainEndpointOptionsTypeDef(
    _ClientDescribeElasticsearchDomainResponseDomainStatusDomainEndpointOptionsTypeDef
):
    """
    Type definition for `ClientDescribeElasticsearchDomainResponseDomainStatus` `DomainEndpointOptions`

    The current status of the Elasticsearch domain's endpoint options.

    - **EnforceHTTPS** *(boolean) --*

      Specify if only HTTPS endpoint should be enabled for the Elasticsearch domain.

    - **TLSSecurityPolicy** *(string) --*

      Specify the TLS security policy that needs to be applied to the HTTPS endpoint of
      Elasticsearch domain. It can be one of the following values:

      * **Policy-Min-TLS-1-0-2019-07:** TLS security policy which supports TLSv1.0 and higher.

      * **Policy-Min-TLS-1-2-2019-07:** TLS security policy which supports only TLSv1.2
    """


_ClientDescribeElasticsearchDomainResponseDomainStatusEBSOptionsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainResponseDomainStatusEBSOptionsTypeDef",
    {"EBSEnabled": bool, "VolumeType": str, "VolumeSize": int, "Iops": int},
    total=False,
)


class ClientDescribeElasticsearchDomainResponseDomainStatusEBSOptionsTypeDef(
    _ClientDescribeElasticsearchDomainResponseDomainStatusEBSOptionsTypeDef
):
    """
    Type definition for `ClientDescribeElasticsearchDomainResponseDomainStatus` `EBSOptions`

    The ``EBSOptions`` for the specified domain. See `Configuring EBS-based Storage
    <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html#es-createdomain-configure-ebs>`__
    for more information.

    - **EBSEnabled** *(boolean) --*

      Specifies whether EBS-based storage is enabled.

    - **VolumeType** *(string) --*

      Specifies the volume type for EBS-based storage.

    - **VolumeSize** *(integer) --*

      Integer to specify the size of an EBS volume.

    - **Iops** *(integer) --*

      Specifies the IOPD for a Provisioned IOPS EBS volume (SSD).
    """


_ClientDescribeElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigZoneAwarenessConfigTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigZoneAwarenessConfigTypeDef",
    {"AvailabilityZoneCount": int},
    total=False,
)


class ClientDescribeElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigZoneAwarenessConfigTypeDef(
    _ClientDescribeElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigZoneAwarenessConfigTypeDef
):
    """
    Type definition for `ClientDescribeElasticsearchDomainResponseDomainStatusElasticsearchClusterConfig` `ZoneAwarenessConfig`

    Specifies the zone awareness configuration for a domain when zone awareness is enabled.

    - **AvailabilityZoneCount** *(integer) --*

      An integer value to indicate the number of availability zones for a domain when zone
      awareness is enabled. This should be equal to number of subnets if VPC endpoints is
      enabled
    """


_ClientDescribeElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigTypeDef",
    {
        "InstanceType": str,
        "InstanceCount": int,
        "DedicatedMasterEnabled": bool,
        "ZoneAwarenessEnabled": bool,
        "ZoneAwarenessConfig": ClientDescribeElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigZoneAwarenessConfigTypeDef,
        "DedicatedMasterType": str,
        "DedicatedMasterCount": int,
    },
    total=False,
)


class ClientDescribeElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigTypeDef(
    _ClientDescribeElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigTypeDef
):
    """
    Type definition for `ClientDescribeElasticsearchDomainResponseDomainStatus` `ElasticsearchClusterConfig`

    The type and number of instances in the domain cluster.

    - **InstanceType** *(string) --*

      The instance type for an Elasticsearch cluster.

    - **InstanceCount** *(integer) --*

      The number of instances in the specified domain cluster.

    - **DedicatedMasterEnabled** *(boolean) --*

      A boolean value to indicate whether a dedicated master node is enabled. See `About
      Dedicated Master Nodes
      <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains.html#es-managedomains-dedicatedmasternodes>`__
      for more information.

    - **ZoneAwarenessEnabled** *(boolean) --*

      A boolean value to indicate whether zone awareness is enabled. See `About Zone Awareness
      <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains.html#es-managedomains-zoneawareness>`__
      for more information.

    - **ZoneAwarenessConfig** *(dict) --*

      Specifies the zone awareness configuration for a domain when zone awareness is enabled.

      - **AvailabilityZoneCount** *(integer) --*

        An integer value to indicate the number of availability zones for a domain when zone
        awareness is enabled. This should be equal to number of subnets if VPC endpoints is
        enabled

    - **DedicatedMasterType** *(string) --*

      The instance type for a dedicated master node.

    - **DedicatedMasterCount** *(integer) --*

      Total number of dedicated master nodes, active and on standby, for the cluster.
    """


_ClientDescribeElasticsearchDomainResponseDomainStatusEncryptionAtRestOptionsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainResponseDomainStatusEncryptionAtRestOptionsTypeDef",
    {"Enabled": bool, "KmsKeyId": str},
    total=False,
)


class ClientDescribeElasticsearchDomainResponseDomainStatusEncryptionAtRestOptionsTypeDef(
    _ClientDescribeElasticsearchDomainResponseDomainStatusEncryptionAtRestOptionsTypeDef
):
    """
    Type definition for `ClientDescribeElasticsearchDomainResponseDomainStatus` `EncryptionAtRestOptions`

    Specifies the status of the ``EncryptionAtRestOptions`` .

    - **Enabled** *(boolean) --*

      Specifies the option to enable Encryption At Rest.

    - **KmsKeyId** *(string) --*

      Specifies the KMS Key ID for Encryption At Rest options.
    """


_ClientDescribeElasticsearchDomainResponseDomainStatusLogPublishingOptionsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainResponseDomainStatusLogPublishingOptionsTypeDef",
    {"CloudWatchLogsLogGroupArn": str, "Enabled": bool},
    total=False,
)


class ClientDescribeElasticsearchDomainResponseDomainStatusLogPublishingOptionsTypeDef(
    _ClientDescribeElasticsearchDomainResponseDomainStatusLogPublishingOptionsTypeDef
):
    """
    Type definition for `ClientDescribeElasticsearchDomainResponseDomainStatus` `LogPublishingOptions`

    Log Publishing option that is set for given domain. Attributes and their details:

    * CloudWatchLogsLogGroupArn: ARN of the Cloudwatch log group to which log needs to be
    published.

    * Enabled: Whether the log publishing for given log type is enabled or not

    - **CloudWatchLogsLogGroupArn** *(string) --*

      ARN of the Cloudwatch log group to which log needs to be published.

    - **Enabled** *(boolean) --*

      Specifies whether given log publishing option is enabled or not.
    """


_ClientDescribeElasticsearchDomainResponseDomainStatusNodeToNodeEncryptionOptionsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainResponseDomainStatusNodeToNodeEncryptionOptionsTypeDef",
    {"Enabled": bool},
    total=False,
)


class ClientDescribeElasticsearchDomainResponseDomainStatusNodeToNodeEncryptionOptionsTypeDef(
    _ClientDescribeElasticsearchDomainResponseDomainStatusNodeToNodeEncryptionOptionsTypeDef
):
    """
    Type definition for `ClientDescribeElasticsearchDomainResponseDomainStatus` `NodeToNodeEncryptionOptions`

    Specifies the status of the ``NodeToNodeEncryptionOptions`` .

    - **Enabled** *(boolean) --*

      Specify true to enable node-to-node encryption.
    """


_ClientDescribeElasticsearchDomainResponseDomainStatusServiceSoftwareOptionsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainResponseDomainStatusServiceSoftwareOptionsTypeDef",
    {
        "CurrentVersion": str,
        "NewVersion": str,
        "UpdateAvailable": bool,
        "Cancellable": bool,
        "UpdateStatus": str,
        "Description": str,
        "AutomatedUpdateDate": datetime,
    },
    total=False,
)


class ClientDescribeElasticsearchDomainResponseDomainStatusServiceSoftwareOptionsTypeDef(
    _ClientDescribeElasticsearchDomainResponseDomainStatusServiceSoftwareOptionsTypeDef
):
    """
    Type definition for `ClientDescribeElasticsearchDomainResponseDomainStatus` `ServiceSoftwareOptions`

    The current status of the Elasticsearch domain's service software.

    - **CurrentVersion** *(string) --*

      The current service software version that is present on the domain.

    - **NewVersion** *(string) --*

      The new service software version if one is available.

    - **UpdateAvailable** *(boolean) --*

      ``True`` if you are able to update you service software version. ``False`` if you are not
      able to update your service software version.

    - **Cancellable** *(boolean) --*

      ``True`` if you are able to cancel your service software version update. ``False`` if you
      are not able to cancel your service software version.

    - **UpdateStatus** *(string) --*

      The status of your service software update. This field can take the following values:
      ``ELIGIBLE`` , ``PENDING_UPDATE`` , ``IN_PROGRESS`` , ``COMPLETED`` , and
      ``NOT_ELIGIBLE`` .

    - **Description** *(string) --*

      The description of the ``UpdateStatus`` .

    - **AutomatedUpdateDate** *(datetime) --*

      Timestamp, in Epoch time, until which you can manually request a service software update.
      After this date, we automatically update your service software.
    """


_ClientDescribeElasticsearchDomainResponseDomainStatusSnapshotOptionsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainResponseDomainStatusSnapshotOptionsTypeDef",
    {"AutomatedSnapshotStartHour": int},
    total=False,
)


class ClientDescribeElasticsearchDomainResponseDomainStatusSnapshotOptionsTypeDef(
    _ClientDescribeElasticsearchDomainResponseDomainStatusSnapshotOptionsTypeDef
):
    """
    Type definition for `ClientDescribeElasticsearchDomainResponseDomainStatus` `SnapshotOptions`

    Specifies the status of the ``SnapshotOptions``

    - **AutomatedSnapshotStartHour** *(integer) --*

      Specifies the time, in UTC format, when the service takes a daily automated snapshot of
      the specified Elasticsearch domain. Default value is ``0`` hours.
    """


_ClientDescribeElasticsearchDomainResponseDomainStatusVPCOptionsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainResponseDomainStatusVPCOptionsTypeDef",
    {
        "VPCId": str,
        "SubnetIds": List[str],
        "AvailabilityZones": List[str],
        "SecurityGroupIds": List[str],
    },
    total=False,
)


class ClientDescribeElasticsearchDomainResponseDomainStatusVPCOptionsTypeDef(
    _ClientDescribeElasticsearchDomainResponseDomainStatusVPCOptionsTypeDef
):
    """
    Type definition for `ClientDescribeElasticsearchDomainResponseDomainStatus` `VPCOptions`

    The ``VPCOptions`` for the specified domain. For more information, see `VPC Endpoints for
    Amazon Elasticsearch Service Domains
    <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html>`__ .

    - **VPCId** *(string) --*

      The VPC Id for the Elasticsearch domain. Exists only if the domain was created with
      VPCOptions.

    - **SubnetIds** *(list) --*

      Specifies the subnets for VPC endpoint.

      - *(string) --*

    - **AvailabilityZones** *(list) --*

      The availability zones for the Elasticsearch domain. Exists only if the domain was
      created with VPCOptions.

      - *(string) --*

    - **SecurityGroupIds** *(list) --*

      Specifies the security groups for VPC endpoint.

      - *(string) --*
    """


_ClientDescribeElasticsearchDomainResponseDomainStatusTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainResponseDomainStatusTypeDef",
    {
        "DomainId": str,
        "DomainName": str,
        "ARN": str,
        "Created": bool,
        "Deleted": bool,
        "Endpoint": str,
        "Endpoints": Dict[str, str],
        "Processing": bool,
        "UpgradeProcessing": bool,
        "ElasticsearchVersion": str,
        "ElasticsearchClusterConfig": ClientDescribeElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigTypeDef,
        "EBSOptions": ClientDescribeElasticsearchDomainResponseDomainStatusEBSOptionsTypeDef,
        "AccessPolicies": str,
        "SnapshotOptions": ClientDescribeElasticsearchDomainResponseDomainStatusSnapshotOptionsTypeDef,
        "VPCOptions": ClientDescribeElasticsearchDomainResponseDomainStatusVPCOptionsTypeDef,
        "CognitoOptions": ClientDescribeElasticsearchDomainResponseDomainStatusCognitoOptionsTypeDef,
        "EncryptionAtRestOptions": ClientDescribeElasticsearchDomainResponseDomainStatusEncryptionAtRestOptionsTypeDef,
        "NodeToNodeEncryptionOptions": ClientDescribeElasticsearchDomainResponseDomainStatusNodeToNodeEncryptionOptionsTypeDef,
        "AdvancedOptions": Dict[str, str],
        "LogPublishingOptions": Dict[
            str,
            ClientDescribeElasticsearchDomainResponseDomainStatusLogPublishingOptionsTypeDef,
        ],
        "ServiceSoftwareOptions": ClientDescribeElasticsearchDomainResponseDomainStatusServiceSoftwareOptionsTypeDef,
        "DomainEndpointOptions": ClientDescribeElasticsearchDomainResponseDomainStatusDomainEndpointOptionsTypeDef,
    },
    total=False,
)


class ClientDescribeElasticsearchDomainResponseDomainStatusTypeDef(
    _ClientDescribeElasticsearchDomainResponseDomainStatusTypeDef
):
    """
    Type definition for `ClientDescribeElasticsearchDomainResponse` `DomainStatus`

    The current status of the Elasticsearch domain.

    - **DomainId** *(string) --*

      The unique identifier for the specified Elasticsearch domain.

    - **DomainName** *(string) --*

      The name of an Elasticsearch domain. Domain names are unique across the domains owned by an
      account within an AWS region. Domain names start with a letter or number and can contain
      the following characters: a-z (lowercase), 0-9, and - (hyphen).

    - **ARN** *(string) --*

      The Amazon resource name (ARN) of an Elasticsearch domain. See `Identifiers for IAM
      Entities
      <http://docs.aws.amazon.com/IAM/latest/UserGuide/index.html?Using_Identifiers.html>`__ in
      *Using AWS Identity and Access Management* for more information.

    - **Created** *(boolean) --*

      The domain creation status. ``True`` if the creation of an Elasticsearch domain is
      complete. ``False`` if domain creation is still in progress.

    - **Deleted** *(boolean) --*

      The domain deletion status. ``True`` if a delete request has been received for the domain
      but resource cleanup is still in progress. ``False`` if the domain has not been deleted.
      Once domain deletion is complete, the status of the domain is no longer returned.

    - **Endpoint** *(string) --*

      The Elasticsearch domain endpoint that you use to submit index and search requests.

    - **Endpoints** *(dict) --*

      Map containing the Elasticsearch domain endpoints used to submit index and search requests.
      Example ``key, value`` :
      ``'vpc','vpc-endpoint-h2dsd34efgyghrtguk5gt6j2foh4.us-east-1.es.amazonaws.com'`` .

      - *(string) --*

        - *(string) --*

          The endpoint to which service requests are submitted. For example,
          ``search-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.es.amazonaws.com`` or
          ``doc-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.es.amazonaws.com`` .

    - **Processing** *(boolean) --*

      The status of the Elasticsearch domain configuration. ``True`` if Amazon Elasticsearch
      Service is processing configuration changes. ``False`` if the configuration is active.

    - **UpgradeProcessing** *(boolean) --*

      The status of an Elasticsearch domain version upgrade. ``True`` if Amazon Elasticsearch
      Service is undergoing a version upgrade. ``False`` if the configuration is active.

    - **ElasticsearchVersion** *(string) --*

    - **ElasticsearchClusterConfig** *(dict) --*

      The type and number of instances in the domain cluster.

      - **InstanceType** *(string) --*

        The instance type for an Elasticsearch cluster.

      - **InstanceCount** *(integer) --*

        The number of instances in the specified domain cluster.

      - **DedicatedMasterEnabled** *(boolean) --*

        A boolean value to indicate whether a dedicated master node is enabled. See `About
        Dedicated Master Nodes
        <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains.html#es-managedomains-dedicatedmasternodes>`__
        for more information.

      - **ZoneAwarenessEnabled** *(boolean) --*

        A boolean value to indicate whether zone awareness is enabled. See `About Zone Awareness
        <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains.html#es-managedomains-zoneawareness>`__
        for more information.

      - **ZoneAwarenessConfig** *(dict) --*

        Specifies the zone awareness configuration for a domain when zone awareness is enabled.

        - **AvailabilityZoneCount** *(integer) --*

          An integer value to indicate the number of availability zones for a domain when zone
          awareness is enabled. This should be equal to number of subnets if VPC endpoints is
          enabled

      - **DedicatedMasterType** *(string) --*

        The instance type for a dedicated master node.

      - **DedicatedMasterCount** *(integer) --*

        Total number of dedicated master nodes, active and on standby, for the cluster.

    - **EBSOptions** *(dict) --*

      The ``EBSOptions`` for the specified domain. See `Configuring EBS-based Storage
      <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html#es-createdomain-configure-ebs>`__
      for more information.

      - **EBSEnabled** *(boolean) --*

        Specifies whether EBS-based storage is enabled.

      - **VolumeType** *(string) --*

        Specifies the volume type for EBS-based storage.

      - **VolumeSize** *(integer) --*

        Integer to specify the size of an EBS volume.

      - **Iops** *(integer) --*

        Specifies the IOPD for a Provisioned IOPS EBS volume (SSD).

    - **AccessPolicies** *(string) --*

      IAM access policy as a JSON-formatted string.

    - **SnapshotOptions** *(dict) --*

      Specifies the status of the ``SnapshotOptions``

      - **AutomatedSnapshotStartHour** *(integer) --*

        Specifies the time, in UTC format, when the service takes a daily automated snapshot of
        the specified Elasticsearch domain. Default value is ``0`` hours.

    - **VPCOptions** *(dict) --*

      The ``VPCOptions`` for the specified domain. For more information, see `VPC Endpoints for
      Amazon Elasticsearch Service Domains
      <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html>`__ .

      - **VPCId** *(string) --*

        The VPC Id for the Elasticsearch domain. Exists only if the domain was created with
        VPCOptions.

      - **SubnetIds** *(list) --*

        Specifies the subnets for VPC endpoint.

        - *(string) --*

      - **AvailabilityZones** *(list) --*

        The availability zones for the Elasticsearch domain. Exists only if the domain was
        created with VPCOptions.

        - *(string) --*

      - **SecurityGroupIds** *(list) --*

        Specifies the security groups for VPC endpoint.

        - *(string) --*

    - **CognitoOptions** *(dict) --*

      The ``CognitoOptions`` for the specified domain. For more information, see `Amazon Cognito
      Authentication for Kibana
      <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-cognito-auth.html>`__
      .

      - **Enabled** *(boolean) --*

        Specifies the option to enable Cognito for Kibana authentication.

      - **UserPoolId** *(string) --*

        Specifies the Cognito user pool ID for Kibana authentication.

      - **IdentityPoolId** *(string) --*

        Specifies the Cognito identity pool ID for Kibana authentication.

      - **RoleArn** *(string) --*

        Specifies the role ARN that provides Elasticsearch permissions for accessing Cognito
        resources.

    - **EncryptionAtRestOptions** *(dict) --*

      Specifies the status of the ``EncryptionAtRestOptions`` .

      - **Enabled** *(boolean) --*

        Specifies the option to enable Encryption At Rest.

      - **KmsKeyId** *(string) --*

        Specifies the KMS Key ID for Encryption At Rest options.

    - **NodeToNodeEncryptionOptions** *(dict) --*

      Specifies the status of the ``NodeToNodeEncryptionOptions`` .

      - **Enabled** *(boolean) --*

        Specify true to enable node-to-node encryption.

    - **AdvancedOptions** *(dict) --*

      Specifies the status of the ``AdvancedOptions``

      - *(string) --*

        - *(string) --*

    - **LogPublishingOptions** *(dict) --*

      Log publishing options for the given domain.

      - *(string) --*

        Type of Log File, it can be one of the following:

        * INDEX_SLOW_LOGS: Index slow logs contain insert requests that took more time than
        configured index query log threshold to execute.

        * SEARCH_SLOW_LOGS: Search slow logs contain search queries that took more time than
        configured search query log threshold to execute.

        * ES_APPLICATION_LOGS: Elasticsearch application logs contain information about errors
        and warnings raised during the operation of the service and can be useful for
        troubleshooting.

        - *(dict) --*

          Log Publishing option that is set for given domain. Attributes and their details:

          * CloudWatchLogsLogGroupArn: ARN of the Cloudwatch log group to which log needs to be
          published.

          * Enabled: Whether the log publishing for given log type is enabled or not

          - **CloudWatchLogsLogGroupArn** *(string) --*

            ARN of the Cloudwatch log group to which log needs to be published.

          - **Enabled** *(boolean) --*

            Specifies whether given log publishing option is enabled or not.

    - **ServiceSoftwareOptions** *(dict) --*

      The current status of the Elasticsearch domain's service software.

      - **CurrentVersion** *(string) --*

        The current service software version that is present on the domain.

      - **NewVersion** *(string) --*

        The new service software version if one is available.

      - **UpdateAvailable** *(boolean) --*

        ``True`` if you are able to update you service software version. ``False`` if you are not
        able to update your service software version.

      - **Cancellable** *(boolean) --*

        ``True`` if you are able to cancel your service software version update. ``False`` if you
        are not able to cancel your service software version.

      - **UpdateStatus** *(string) --*

        The status of your service software update. This field can take the following values:
        ``ELIGIBLE`` , ``PENDING_UPDATE`` , ``IN_PROGRESS`` , ``COMPLETED`` , and
        ``NOT_ELIGIBLE`` .

      - **Description** *(string) --*

        The description of the ``UpdateStatus`` .

      - **AutomatedUpdateDate** *(datetime) --*

        Timestamp, in Epoch time, until which you can manually request a service software update.
        After this date, we automatically update your service software.

    - **DomainEndpointOptions** *(dict) --*

      The current status of the Elasticsearch domain's endpoint options.

      - **EnforceHTTPS** *(boolean) --*

        Specify if only HTTPS endpoint should be enabled for the Elasticsearch domain.

      - **TLSSecurityPolicy** *(string) --*

        Specify the TLS security policy that needs to be applied to the HTTPS endpoint of
        Elasticsearch domain. It can be one of the following values:

        * **Policy-Min-TLS-1-0-2019-07:** TLS security policy which supports TLSv1.0 and higher.

        * **Policy-Min-TLS-1-2-2019-07:** TLS security policy which supports only TLSv1.2
    """


_ClientDescribeElasticsearchDomainResponseTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainResponseTypeDef",
    {"DomainStatus": ClientDescribeElasticsearchDomainResponseDomainStatusTypeDef},
    total=False,
)


class ClientDescribeElasticsearchDomainResponseTypeDef(
    _ClientDescribeElasticsearchDomainResponseTypeDef
):
    """
    Type definition for `ClientDescribeElasticsearchDomain` `Response`

    The result of a ``DescribeElasticsearchDomain`` request. Contains the status of the domain
    specified in the request.

    - **DomainStatus** *(dict) --*

      The current status of the Elasticsearch domain.

      - **DomainId** *(string) --*

        The unique identifier for the specified Elasticsearch domain.

      - **DomainName** *(string) --*

        The name of an Elasticsearch domain. Domain names are unique across the domains owned by an
        account within an AWS region. Domain names start with a letter or number and can contain
        the following characters: a-z (lowercase), 0-9, and - (hyphen).

      - **ARN** *(string) --*

        The Amazon resource name (ARN) of an Elasticsearch domain. See `Identifiers for IAM
        Entities
        <http://docs.aws.amazon.com/IAM/latest/UserGuide/index.html?Using_Identifiers.html>`__ in
        *Using AWS Identity and Access Management* for more information.

      - **Created** *(boolean) --*

        The domain creation status. ``True`` if the creation of an Elasticsearch domain is
        complete. ``False`` if domain creation is still in progress.

      - **Deleted** *(boolean) --*

        The domain deletion status. ``True`` if a delete request has been received for the domain
        but resource cleanup is still in progress. ``False`` if the domain has not been deleted.
        Once domain deletion is complete, the status of the domain is no longer returned.

      - **Endpoint** *(string) --*

        The Elasticsearch domain endpoint that you use to submit index and search requests.

      - **Endpoints** *(dict) --*

        Map containing the Elasticsearch domain endpoints used to submit index and search requests.
        Example ``key, value`` :
        ``'vpc','vpc-endpoint-h2dsd34efgyghrtguk5gt6j2foh4.us-east-1.es.amazonaws.com'`` .

        - *(string) --*

          - *(string) --*

            The endpoint to which service requests are submitted. For example,
            ``search-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.es.amazonaws.com`` or
            ``doc-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.es.amazonaws.com`` .

      - **Processing** *(boolean) --*

        The status of the Elasticsearch domain configuration. ``True`` if Amazon Elasticsearch
        Service is processing configuration changes. ``False`` if the configuration is active.

      - **UpgradeProcessing** *(boolean) --*

        The status of an Elasticsearch domain version upgrade. ``True`` if Amazon Elasticsearch
        Service is undergoing a version upgrade. ``False`` if the configuration is active.

      - **ElasticsearchVersion** *(string) --*

      - **ElasticsearchClusterConfig** *(dict) --*

        The type and number of instances in the domain cluster.

        - **InstanceType** *(string) --*

          The instance type for an Elasticsearch cluster.

        - **InstanceCount** *(integer) --*

          The number of instances in the specified domain cluster.

        - **DedicatedMasterEnabled** *(boolean) --*

          A boolean value to indicate whether a dedicated master node is enabled. See `About
          Dedicated Master Nodes
          <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains.html#es-managedomains-dedicatedmasternodes>`__
          for more information.

        - **ZoneAwarenessEnabled** *(boolean) --*

          A boolean value to indicate whether zone awareness is enabled. See `About Zone Awareness
          <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains.html#es-managedomains-zoneawareness>`__
          for more information.

        - **ZoneAwarenessConfig** *(dict) --*

          Specifies the zone awareness configuration for a domain when zone awareness is enabled.

          - **AvailabilityZoneCount** *(integer) --*

            An integer value to indicate the number of availability zones for a domain when zone
            awareness is enabled. This should be equal to number of subnets if VPC endpoints is
            enabled

        - **DedicatedMasterType** *(string) --*

          The instance type for a dedicated master node.

        - **DedicatedMasterCount** *(integer) --*

          Total number of dedicated master nodes, active and on standby, for the cluster.

      - **EBSOptions** *(dict) --*

        The ``EBSOptions`` for the specified domain. See `Configuring EBS-based Storage
        <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html#es-createdomain-configure-ebs>`__
        for more information.

        - **EBSEnabled** *(boolean) --*

          Specifies whether EBS-based storage is enabled.

        - **VolumeType** *(string) --*

          Specifies the volume type for EBS-based storage.

        - **VolumeSize** *(integer) --*

          Integer to specify the size of an EBS volume.

        - **Iops** *(integer) --*

          Specifies the IOPD for a Provisioned IOPS EBS volume (SSD).

      - **AccessPolicies** *(string) --*

        IAM access policy as a JSON-formatted string.

      - **SnapshotOptions** *(dict) --*

        Specifies the status of the ``SnapshotOptions``

        - **AutomatedSnapshotStartHour** *(integer) --*

          Specifies the time, in UTC format, when the service takes a daily automated snapshot of
          the specified Elasticsearch domain. Default value is ``0`` hours.

      - **VPCOptions** *(dict) --*

        The ``VPCOptions`` for the specified domain. For more information, see `VPC Endpoints for
        Amazon Elasticsearch Service Domains
        <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html>`__ .

        - **VPCId** *(string) --*

          The VPC Id for the Elasticsearch domain. Exists only if the domain was created with
          VPCOptions.

        - **SubnetIds** *(list) --*

          Specifies the subnets for VPC endpoint.

          - *(string) --*

        - **AvailabilityZones** *(list) --*

          The availability zones for the Elasticsearch domain. Exists only if the domain was
          created with VPCOptions.

          - *(string) --*

        - **SecurityGroupIds** *(list) --*

          Specifies the security groups for VPC endpoint.

          - *(string) --*

      - **CognitoOptions** *(dict) --*

        The ``CognitoOptions`` for the specified domain. For more information, see `Amazon Cognito
        Authentication for Kibana
        <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-cognito-auth.html>`__
        .

        - **Enabled** *(boolean) --*

          Specifies the option to enable Cognito for Kibana authentication.

        - **UserPoolId** *(string) --*

          Specifies the Cognito user pool ID for Kibana authentication.

        - **IdentityPoolId** *(string) --*

          Specifies the Cognito identity pool ID for Kibana authentication.

        - **RoleArn** *(string) --*

          Specifies the role ARN that provides Elasticsearch permissions for accessing Cognito
          resources.

      - **EncryptionAtRestOptions** *(dict) --*

        Specifies the status of the ``EncryptionAtRestOptions`` .

        - **Enabled** *(boolean) --*

          Specifies the option to enable Encryption At Rest.

        - **KmsKeyId** *(string) --*

          Specifies the KMS Key ID for Encryption At Rest options.

      - **NodeToNodeEncryptionOptions** *(dict) --*

        Specifies the status of the ``NodeToNodeEncryptionOptions`` .

        - **Enabled** *(boolean) --*

          Specify true to enable node-to-node encryption.

      - **AdvancedOptions** *(dict) --*

        Specifies the status of the ``AdvancedOptions``

        - *(string) --*

          - *(string) --*

      - **LogPublishingOptions** *(dict) --*

        Log publishing options for the given domain.

        - *(string) --*

          Type of Log File, it can be one of the following:

          * INDEX_SLOW_LOGS: Index slow logs contain insert requests that took more time than
          configured index query log threshold to execute.

          * SEARCH_SLOW_LOGS: Search slow logs contain search queries that took more time than
          configured search query log threshold to execute.

          * ES_APPLICATION_LOGS: Elasticsearch application logs contain information about errors
          and warnings raised during the operation of the service and can be useful for
          troubleshooting.

          - *(dict) --*

            Log Publishing option that is set for given domain. Attributes and their details:

            * CloudWatchLogsLogGroupArn: ARN of the Cloudwatch log group to which log needs to be
            published.

            * Enabled: Whether the log publishing for given log type is enabled or not

            - **CloudWatchLogsLogGroupArn** *(string) --*

              ARN of the Cloudwatch log group to which log needs to be published.

            - **Enabled** *(boolean) --*

              Specifies whether given log publishing option is enabled or not.

      - **ServiceSoftwareOptions** *(dict) --*

        The current status of the Elasticsearch domain's service software.

        - **CurrentVersion** *(string) --*

          The current service software version that is present on the domain.

        - **NewVersion** *(string) --*

          The new service software version if one is available.

        - **UpdateAvailable** *(boolean) --*

          ``True`` if you are able to update you service software version. ``False`` if you are not
          able to update your service software version.

        - **Cancellable** *(boolean) --*

          ``True`` if you are able to cancel your service software version update. ``False`` if you
          are not able to cancel your service software version.

        - **UpdateStatus** *(string) --*

          The status of your service software update. This field can take the following values:
          ``ELIGIBLE`` , ``PENDING_UPDATE`` , ``IN_PROGRESS`` , ``COMPLETED`` , and
          ``NOT_ELIGIBLE`` .

        - **Description** *(string) --*

          The description of the ``UpdateStatus`` .

        - **AutomatedUpdateDate** *(datetime) --*

          Timestamp, in Epoch time, until which you can manually request a service software update.
          After this date, we automatically update your service software.

      - **DomainEndpointOptions** *(dict) --*

        The current status of the Elasticsearch domain's endpoint options.

        - **EnforceHTTPS** *(boolean) --*

          Specify if only HTTPS endpoint should be enabled for the Elasticsearch domain.

        - **TLSSecurityPolicy** *(string) --*

          Specify the TLS security policy that needs to be applied to the HTTPS endpoint of
          Elasticsearch domain. It can be one of the following values:

          * **Policy-Min-TLS-1-0-2019-07:** TLS security policy which supports TLSv1.0 and higher.

          * **Policy-Min-TLS-1-2-2019-07:** TLS security policy which supports only TLSv1.2
    """


_ClientDescribeElasticsearchDomainsResponseDomainStatusListCognitoOptionsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainsResponseDomainStatusListCognitoOptionsTypeDef",
    {"Enabled": bool, "UserPoolId": str, "IdentityPoolId": str, "RoleArn": str},
    total=False,
)


class ClientDescribeElasticsearchDomainsResponseDomainStatusListCognitoOptionsTypeDef(
    _ClientDescribeElasticsearchDomainsResponseDomainStatusListCognitoOptionsTypeDef
):
    """
    Type definition for `ClientDescribeElasticsearchDomainsResponseDomainStatusList` `CognitoOptions`

    The ``CognitoOptions`` for the specified domain. For more information, see `Amazon
    Cognito Authentication for Kibana
    <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-cognito-auth.html>`__
    .

    - **Enabled** *(boolean) --*

      Specifies the option to enable Cognito for Kibana authentication.

    - **UserPoolId** *(string) --*

      Specifies the Cognito user pool ID for Kibana authentication.

    - **IdentityPoolId** *(string) --*

      Specifies the Cognito identity pool ID for Kibana authentication.

    - **RoleArn** *(string) --*

      Specifies the role ARN that provides Elasticsearch permissions for accessing Cognito
      resources.
    """


_ClientDescribeElasticsearchDomainsResponseDomainStatusListDomainEndpointOptionsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainsResponseDomainStatusListDomainEndpointOptionsTypeDef",
    {"EnforceHTTPS": bool, "TLSSecurityPolicy": str},
    total=False,
)


class ClientDescribeElasticsearchDomainsResponseDomainStatusListDomainEndpointOptionsTypeDef(
    _ClientDescribeElasticsearchDomainsResponseDomainStatusListDomainEndpointOptionsTypeDef
):
    """
    Type definition for `ClientDescribeElasticsearchDomainsResponseDomainStatusList` `DomainEndpointOptions`

    The current status of the Elasticsearch domain's endpoint options.

    - **EnforceHTTPS** *(boolean) --*

      Specify if only HTTPS endpoint should be enabled for the Elasticsearch domain.

    - **TLSSecurityPolicy** *(string) --*

      Specify the TLS security policy that needs to be applied to the HTTPS endpoint of
      Elasticsearch domain. It can be one of the following values:

      * **Policy-Min-TLS-1-0-2019-07:** TLS security policy which supports TLSv1.0 and higher.

      * **Policy-Min-TLS-1-2-2019-07:** TLS security policy which supports only TLSv1.2
    """


_ClientDescribeElasticsearchDomainsResponseDomainStatusListEBSOptionsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainsResponseDomainStatusListEBSOptionsTypeDef",
    {"EBSEnabled": bool, "VolumeType": str, "VolumeSize": int, "Iops": int},
    total=False,
)


class ClientDescribeElasticsearchDomainsResponseDomainStatusListEBSOptionsTypeDef(
    _ClientDescribeElasticsearchDomainsResponseDomainStatusListEBSOptionsTypeDef
):
    """
    Type definition for `ClientDescribeElasticsearchDomainsResponseDomainStatusList` `EBSOptions`

    The ``EBSOptions`` for the specified domain. See `Configuring EBS-based Storage
    <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html#es-createdomain-configure-ebs>`__
    for more information.

    - **EBSEnabled** *(boolean) --*

      Specifies whether EBS-based storage is enabled.

    - **VolumeType** *(string) --*

      Specifies the volume type for EBS-based storage.

    - **VolumeSize** *(integer) --*

      Integer to specify the size of an EBS volume.

    - **Iops** *(integer) --*

      Specifies the IOPD for a Provisioned IOPS EBS volume (SSD).
    """


_ClientDescribeElasticsearchDomainsResponseDomainStatusListElasticsearchClusterConfigZoneAwarenessConfigTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainsResponseDomainStatusListElasticsearchClusterConfigZoneAwarenessConfigTypeDef",
    {"AvailabilityZoneCount": int},
    total=False,
)


class ClientDescribeElasticsearchDomainsResponseDomainStatusListElasticsearchClusterConfigZoneAwarenessConfigTypeDef(
    _ClientDescribeElasticsearchDomainsResponseDomainStatusListElasticsearchClusterConfigZoneAwarenessConfigTypeDef
):
    """
    Type definition for `ClientDescribeElasticsearchDomainsResponseDomainStatusListElasticsearchClusterConfig` `ZoneAwarenessConfig`

    Specifies the zone awareness configuration for a domain when zone awareness is enabled.

    - **AvailabilityZoneCount** *(integer) --*

      An integer value to indicate the number of availability zones for a domain when zone
      awareness is enabled. This should be equal to number of subnets if VPC endpoints is
      enabled
    """


_ClientDescribeElasticsearchDomainsResponseDomainStatusListElasticsearchClusterConfigTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainsResponseDomainStatusListElasticsearchClusterConfigTypeDef",
    {
        "InstanceType": str,
        "InstanceCount": int,
        "DedicatedMasterEnabled": bool,
        "ZoneAwarenessEnabled": bool,
        "ZoneAwarenessConfig": ClientDescribeElasticsearchDomainsResponseDomainStatusListElasticsearchClusterConfigZoneAwarenessConfigTypeDef,
        "DedicatedMasterType": str,
        "DedicatedMasterCount": int,
    },
    total=False,
)


class ClientDescribeElasticsearchDomainsResponseDomainStatusListElasticsearchClusterConfigTypeDef(
    _ClientDescribeElasticsearchDomainsResponseDomainStatusListElasticsearchClusterConfigTypeDef
):
    """
    Type definition for `ClientDescribeElasticsearchDomainsResponseDomainStatusList` `ElasticsearchClusterConfig`

    The type and number of instances in the domain cluster.

    - **InstanceType** *(string) --*

      The instance type for an Elasticsearch cluster.

    - **InstanceCount** *(integer) --*

      The number of instances in the specified domain cluster.

    - **DedicatedMasterEnabled** *(boolean) --*

      A boolean value to indicate whether a dedicated master node is enabled. See `About
      Dedicated Master Nodes
      <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains.html#es-managedomains-dedicatedmasternodes>`__
      for more information.

    - **ZoneAwarenessEnabled** *(boolean) --*

      A boolean value to indicate whether zone awareness is enabled. See `About Zone
      Awareness
      <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains.html#es-managedomains-zoneawareness>`__
      for more information.

    - **ZoneAwarenessConfig** *(dict) --*

      Specifies the zone awareness configuration for a domain when zone awareness is enabled.

      - **AvailabilityZoneCount** *(integer) --*

        An integer value to indicate the number of availability zones for a domain when zone
        awareness is enabled. This should be equal to number of subnets if VPC endpoints is
        enabled

    - **DedicatedMasterType** *(string) --*

      The instance type for a dedicated master node.

    - **DedicatedMasterCount** *(integer) --*

      Total number of dedicated master nodes, active and on standby, for the cluster.
    """


_ClientDescribeElasticsearchDomainsResponseDomainStatusListEncryptionAtRestOptionsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainsResponseDomainStatusListEncryptionAtRestOptionsTypeDef",
    {"Enabled": bool, "KmsKeyId": str},
    total=False,
)


class ClientDescribeElasticsearchDomainsResponseDomainStatusListEncryptionAtRestOptionsTypeDef(
    _ClientDescribeElasticsearchDomainsResponseDomainStatusListEncryptionAtRestOptionsTypeDef
):
    """
    Type definition for `ClientDescribeElasticsearchDomainsResponseDomainStatusList` `EncryptionAtRestOptions`

    Specifies the status of the ``EncryptionAtRestOptions`` .

    - **Enabled** *(boolean) --*

      Specifies the option to enable Encryption At Rest.

    - **KmsKeyId** *(string) --*

      Specifies the KMS Key ID for Encryption At Rest options.
    """


_ClientDescribeElasticsearchDomainsResponseDomainStatusListLogPublishingOptionsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainsResponseDomainStatusListLogPublishingOptionsTypeDef",
    {"CloudWatchLogsLogGroupArn": str, "Enabled": bool},
    total=False,
)


class ClientDescribeElasticsearchDomainsResponseDomainStatusListLogPublishingOptionsTypeDef(
    _ClientDescribeElasticsearchDomainsResponseDomainStatusListLogPublishingOptionsTypeDef
):
    """
    Type definition for `ClientDescribeElasticsearchDomainsResponseDomainStatusList` `LogPublishingOptions`

    Log Publishing option that is set for given domain. Attributes and their details:

    * CloudWatchLogsLogGroupArn: ARN of the Cloudwatch log group to which log needs to be
    published.

    * Enabled: Whether the log publishing for given log type is enabled or not

    - **CloudWatchLogsLogGroupArn** *(string) --*

      ARN of the Cloudwatch log group to which log needs to be published.

    - **Enabled** *(boolean) --*

      Specifies whether given log publishing option is enabled or not.
    """


_ClientDescribeElasticsearchDomainsResponseDomainStatusListNodeToNodeEncryptionOptionsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainsResponseDomainStatusListNodeToNodeEncryptionOptionsTypeDef",
    {"Enabled": bool},
    total=False,
)


class ClientDescribeElasticsearchDomainsResponseDomainStatusListNodeToNodeEncryptionOptionsTypeDef(
    _ClientDescribeElasticsearchDomainsResponseDomainStatusListNodeToNodeEncryptionOptionsTypeDef
):
    """
    Type definition for `ClientDescribeElasticsearchDomainsResponseDomainStatusList` `NodeToNodeEncryptionOptions`

    Specifies the status of the ``NodeToNodeEncryptionOptions`` .

    - **Enabled** *(boolean) --*

      Specify true to enable node-to-node encryption.
    """


_ClientDescribeElasticsearchDomainsResponseDomainStatusListServiceSoftwareOptionsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainsResponseDomainStatusListServiceSoftwareOptionsTypeDef",
    {
        "CurrentVersion": str,
        "NewVersion": str,
        "UpdateAvailable": bool,
        "Cancellable": bool,
        "UpdateStatus": str,
        "Description": str,
        "AutomatedUpdateDate": datetime,
    },
    total=False,
)


class ClientDescribeElasticsearchDomainsResponseDomainStatusListServiceSoftwareOptionsTypeDef(
    _ClientDescribeElasticsearchDomainsResponseDomainStatusListServiceSoftwareOptionsTypeDef
):
    """
    Type definition for `ClientDescribeElasticsearchDomainsResponseDomainStatusList` `ServiceSoftwareOptions`

    The current status of the Elasticsearch domain's service software.

    - **CurrentVersion** *(string) --*

      The current service software version that is present on the domain.

    - **NewVersion** *(string) --*

      The new service software version if one is available.

    - **UpdateAvailable** *(boolean) --*

      ``True`` if you are able to update you service software version. ``False`` if you are
      not able to update your service software version.

    - **Cancellable** *(boolean) --*

      ``True`` if you are able to cancel your service software version update. ``False`` if
      you are not able to cancel your service software version.

    - **UpdateStatus** *(string) --*

      The status of your service software update. This field can take the following values:
      ``ELIGIBLE`` , ``PENDING_UPDATE`` , ``IN_PROGRESS`` , ``COMPLETED`` , and
      ``NOT_ELIGIBLE`` .

    - **Description** *(string) --*

      The description of the ``UpdateStatus`` .

    - **AutomatedUpdateDate** *(datetime) --*

      Timestamp, in Epoch time, until which you can manually request a service software
      update. After this date, we automatically update your service software.
    """


_ClientDescribeElasticsearchDomainsResponseDomainStatusListSnapshotOptionsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainsResponseDomainStatusListSnapshotOptionsTypeDef",
    {"AutomatedSnapshotStartHour": int},
    total=False,
)


class ClientDescribeElasticsearchDomainsResponseDomainStatusListSnapshotOptionsTypeDef(
    _ClientDescribeElasticsearchDomainsResponseDomainStatusListSnapshotOptionsTypeDef
):
    """
    Type definition for `ClientDescribeElasticsearchDomainsResponseDomainStatusList` `SnapshotOptions`

    Specifies the status of the ``SnapshotOptions``

    - **AutomatedSnapshotStartHour** *(integer) --*

      Specifies the time, in UTC format, when the service takes a daily automated snapshot of
      the specified Elasticsearch domain. Default value is ``0`` hours.
    """


_ClientDescribeElasticsearchDomainsResponseDomainStatusListVPCOptionsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainsResponseDomainStatusListVPCOptionsTypeDef",
    {
        "VPCId": str,
        "SubnetIds": List[str],
        "AvailabilityZones": List[str],
        "SecurityGroupIds": List[str],
    },
    total=False,
)


class ClientDescribeElasticsearchDomainsResponseDomainStatusListVPCOptionsTypeDef(
    _ClientDescribeElasticsearchDomainsResponseDomainStatusListVPCOptionsTypeDef
):
    """
    Type definition for `ClientDescribeElasticsearchDomainsResponseDomainStatusList` `VPCOptions`

    The ``VPCOptions`` for the specified domain. For more information, see `VPC Endpoints for
    Amazon Elasticsearch Service Domains
    <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html>`__ .

    - **VPCId** *(string) --*

      The VPC Id for the Elasticsearch domain. Exists only if the domain was created with
      VPCOptions.

    - **SubnetIds** *(list) --*

      Specifies the subnets for VPC endpoint.

      - *(string) --*

    - **AvailabilityZones** *(list) --*

      The availability zones for the Elasticsearch domain. Exists only if the domain was
      created with VPCOptions.

      - *(string) --*

    - **SecurityGroupIds** *(list) --*

      Specifies the security groups for VPC endpoint.

      - *(string) --*
    """


_ClientDescribeElasticsearchDomainsResponseDomainStatusListTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainsResponseDomainStatusListTypeDef",
    {
        "DomainId": str,
        "DomainName": str,
        "ARN": str,
        "Created": bool,
        "Deleted": bool,
        "Endpoint": str,
        "Endpoints": Dict[str, str],
        "Processing": bool,
        "UpgradeProcessing": bool,
        "ElasticsearchVersion": str,
        "ElasticsearchClusterConfig": ClientDescribeElasticsearchDomainsResponseDomainStatusListElasticsearchClusterConfigTypeDef,
        "EBSOptions": ClientDescribeElasticsearchDomainsResponseDomainStatusListEBSOptionsTypeDef,
        "AccessPolicies": str,
        "SnapshotOptions": ClientDescribeElasticsearchDomainsResponseDomainStatusListSnapshotOptionsTypeDef,
        "VPCOptions": ClientDescribeElasticsearchDomainsResponseDomainStatusListVPCOptionsTypeDef,
        "CognitoOptions": ClientDescribeElasticsearchDomainsResponseDomainStatusListCognitoOptionsTypeDef,
        "EncryptionAtRestOptions": ClientDescribeElasticsearchDomainsResponseDomainStatusListEncryptionAtRestOptionsTypeDef,
        "NodeToNodeEncryptionOptions": ClientDescribeElasticsearchDomainsResponseDomainStatusListNodeToNodeEncryptionOptionsTypeDef,
        "AdvancedOptions": Dict[str, str],
        "LogPublishingOptions": Dict[
            str,
            ClientDescribeElasticsearchDomainsResponseDomainStatusListLogPublishingOptionsTypeDef,
        ],
        "ServiceSoftwareOptions": ClientDescribeElasticsearchDomainsResponseDomainStatusListServiceSoftwareOptionsTypeDef,
        "DomainEndpointOptions": ClientDescribeElasticsearchDomainsResponseDomainStatusListDomainEndpointOptionsTypeDef,
    },
    total=False,
)


class ClientDescribeElasticsearchDomainsResponseDomainStatusListTypeDef(
    _ClientDescribeElasticsearchDomainsResponseDomainStatusListTypeDef
):
    """
    Type definition for `ClientDescribeElasticsearchDomainsResponse` `DomainStatusList`

    The current status of an Elasticsearch domain.

    - **DomainId** *(string) --*

      The unique identifier for the specified Elasticsearch domain.

    - **DomainName** *(string) --*

      The name of an Elasticsearch domain. Domain names are unique across the domains owned by
      an account within an AWS region. Domain names start with a letter or number and can
      contain the following characters: a-z (lowercase), 0-9, and - (hyphen).

    - **ARN** *(string) --*

      The Amazon resource name (ARN) of an Elasticsearch domain. See `Identifiers for IAM
      Entities
      <http://docs.aws.amazon.com/IAM/latest/UserGuide/index.html?Using_Identifiers.html>`__ in
      *Using AWS Identity and Access Management* for more information.

    - **Created** *(boolean) --*

      The domain creation status. ``True`` if the creation of an Elasticsearch domain is
      complete. ``False`` if domain creation is still in progress.

    - **Deleted** *(boolean) --*

      The domain deletion status. ``True`` if a delete request has been received for the domain
      but resource cleanup is still in progress. ``False`` if the domain has not been deleted.
      Once domain deletion is complete, the status of the domain is no longer returned.

    - **Endpoint** *(string) --*

      The Elasticsearch domain endpoint that you use to submit index and search requests.

    - **Endpoints** *(dict) --*

      Map containing the Elasticsearch domain endpoints used to submit index and search
      requests. Example ``key, value`` :
      ``'vpc','vpc-endpoint-h2dsd34efgyghrtguk5gt6j2foh4.us-east-1.es.amazonaws.com'`` .

      - *(string) --*

        - *(string) --*

          The endpoint to which service requests are submitted. For example,
          ``search-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.es.amazonaws.com`` or
          ``doc-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.es.amazonaws.com`` .

    - **Processing** *(boolean) --*

      The status of the Elasticsearch domain configuration. ``True`` if Amazon Elasticsearch
      Service is processing configuration changes. ``False`` if the configuration is active.

    - **UpgradeProcessing** *(boolean) --*

      The status of an Elasticsearch domain version upgrade. ``True`` if Amazon Elasticsearch
      Service is undergoing a version upgrade. ``False`` if the configuration is active.

    - **ElasticsearchVersion** *(string) --*

    - **ElasticsearchClusterConfig** *(dict) --*

      The type and number of instances in the domain cluster.

      - **InstanceType** *(string) --*

        The instance type for an Elasticsearch cluster.

      - **InstanceCount** *(integer) --*

        The number of instances in the specified domain cluster.

      - **DedicatedMasterEnabled** *(boolean) --*

        A boolean value to indicate whether a dedicated master node is enabled. See `About
        Dedicated Master Nodes
        <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains.html#es-managedomains-dedicatedmasternodes>`__
        for more information.

      - **ZoneAwarenessEnabled** *(boolean) --*

        A boolean value to indicate whether zone awareness is enabled. See `About Zone
        Awareness
        <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains.html#es-managedomains-zoneawareness>`__
        for more information.

      - **ZoneAwarenessConfig** *(dict) --*

        Specifies the zone awareness configuration for a domain when zone awareness is enabled.

        - **AvailabilityZoneCount** *(integer) --*

          An integer value to indicate the number of availability zones for a domain when zone
          awareness is enabled. This should be equal to number of subnets if VPC endpoints is
          enabled

      - **DedicatedMasterType** *(string) --*

        The instance type for a dedicated master node.

      - **DedicatedMasterCount** *(integer) --*

        Total number of dedicated master nodes, active and on standby, for the cluster.

    - **EBSOptions** *(dict) --*

      The ``EBSOptions`` for the specified domain. See `Configuring EBS-based Storage
      <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html#es-createdomain-configure-ebs>`__
      for more information.

      - **EBSEnabled** *(boolean) --*

        Specifies whether EBS-based storage is enabled.

      - **VolumeType** *(string) --*

        Specifies the volume type for EBS-based storage.

      - **VolumeSize** *(integer) --*

        Integer to specify the size of an EBS volume.

      - **Iops** *(integer) --*

        Specifies the IOPD for a Provisioned IOPS EBS volume (SSD).

    - **AccessPolicies** *(string) --*

      IAM access policy as a JSON-formatted string.

    - **SnapshotOptions** *(dict) --*

      Specifies the status of the ``SnapshotOptions``

      - **AutomatedSnapshotStartHour** *(integer) --*

        Specifies the time, in UTC format, when the service takes a daily automated snapshot of
        the specified Elasticsearch domain. Default value is ``0`` hours.

    - **VPCOptions** *(dict) --*

      The ``VPCOptions`` for the specified domain. For more information, see `VPC Endpoints for
      Amazon Elasticsearch Service Domains
      <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html>`__ .

      - **VPCId** *(string) --*

        The VPC Id for the Elasticsearch domain. Exists only if the domain was created with
        VPCOptions.

      - **SubnetIds** *(list) --*

        Specifies the subnets for VPC endpoint.

        - *(string) --*

      - **AvailabilityZones** *(list) --*

        The availability zones for the Elasticsearch domain. Exists only if the domain was
        created with VPCOptions.

        - *(string) --*

      - **SecurityGroupIds** *(list) --*

        Specifies the security groups for VPC endpoint.

        - *(string) --*

    - **CognitoOptions** *(dict) --*

      The ``CognitoOptions`` for the specified domain. For more information, see `Amazon
      Cognito Authentication for Kibana
      <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-cognito-auth.html>`__
      .

      - **Enabled** *(boolean) --*

        Specifies the option to enable Cognito for Kibana authentication.

      - **UserPoolId** *(string) --*

        Specifies the Cognito user pool ID for Kibana authentication.

      - **IdentityPoolId** *(string) --*

        Specifies the Cognito identity pool ID for Kibana authentication.

      - **RoleArn** *(string) --*

        Specifies the role ARN that provides Elasticsearch permissions for accessing Cognito
        resources.

    - **EncryptionAtRestOptions** *(dict) --*

      Specifies the status of the ``EncryptionAtRestOptions`` .

      - **Enabled** *(boolean) --*

        Specifies the option to enable Encryption At Rest.

      - **KmsKeyId** *(string) --*

        Specifies the KMS Key ID for Encryption At Rest options.

    - **NodeToNodeEncryptionOptions** *(dict) --*

      Specifies the status of the ``NodeToNodeEncryptionOptions`` .

      - **Enabled** *(boolean) --*

        Specify true to enable node-to-node encryption.

    - **AdvancedOptions** *(dict) --*

      Specifies the status of the ``AdvancedOptions``

      - *(string) --*

        - *(string) --*

    - **LogPublishingOptions** *(dict) --*

      Log publishing options for the given domain.

      - *(string) --*

        Type of Log File, it can be one of the following:

        * INDEX_SLOW_LOGS: Index slow logs contain insert requests that took more time than
        configured index query log threshold to execute.

        * SEARCH_SLOW_LOGS: Search slow logs contain search queries that took more time than
        configured search query log threshold to execute.

        * ES_APPLICATION_LOGS: Elasticsearch application logs contain information about errors
        and warnings raised during the operation of the service and can be useful for
        troubleshooting.

        - *(dict) --*

          Log Publishing option that is set for given domain. Attributes and their details:

          * CloudWatchLogsLogGroupArn: ARN of the Cloudwatch log group to which log needs to be
          published.

          * Enabled: Whether the log publishing for given log type is enabled or not

          - **CloudWatchLogsLogGroupArn** *(string) --*

            ARN of the Cloudwatch log group to which log needs to be published.

          - **Enabled** *(boolean) --*

            Specifies whether given log publishing option is enabled or not.

    - **ServiceSoftwareOptions** *(dict) --*

      The current status of the Elasticsearch domain's service software.

      - **CurrentVersion** *(string) --*

        The current service software version that is present on the domain.

      - **NewVersion** *(string) --*

        The new service software version if one is available.

      - **UpdateAvailable** *(boolean) --*

        ``True`` if you are able to update you service software version. ``False`` if you are
        not able to update your service software version.

      - **Cancellable** *(boolean) --*

        ``True`` if you are able to cancel your service software version update. ``False`` if
        you are not able to cancel your service software version.

      - **UpdateStatus** *(string) --*

        The status of your service software update. This field can take the following values:
        ``ELIGIBLE`` , ``PENDING_UPDATE`` , ``IN_PROGRESS`` , ``COMPLETED`` , and
        ``NOT_ELIGIBLE`` .

      - **Description** *(string) --*

        The description of the ``UpdateStatus`` .

      - **AutomatedUpdateDate** *(datetime) --*

        Timestamp, in Epoch time, until which you can manually request a service software
        update. After this date, we automatically update your service software.

    - **DomainEndpointOptions** *(dict) --*

      The current status of the Elasticsearch domain's endpoint options.

      - **EnforceHTTPS** *(boolean) --*

        Specify if only HTTPS endpoint should be enabled for the Elasticsearch domain.

      - **TLSSecurityPolicy** *(string) --*

        Specify the TLS security policy that needs to be applied to the HTTPS endpoint of
        Elasticsearch domain. It can be one of the following values:

        * **Policy-Min-TLS-1-0-2019-07:** TLS security policy which supports TLSv1.0 and higher.

        * **Policy-Min-TLS-1-2-2019-07:** TLS security policy which supports only TLSv1.2
    """


_ClientDescribeElasticsearchDomainsResponseTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainsResponseTypeDef",
    {
        "DomainStatusList": List[
            ClientDescribeElasticsearchDomainsResponseDomainStatusListTypeDef
        ]
    },
    total=False,
)


class ClientDescribeElasticsearchDomainsResponseTypeDef(
    _ClientDescribeElasticsearchDomainsResponseTypeDef
):
    """
    Type definition for `ClientDescribeElasticsearchDomains` `Response`

    The result of a ``DescribeElasticsearchDomains`` request. Contains the status of the specified
    domains or all domains owned by the account.

    - **DomainStatusList** *(list) --*

      The status of the domains requested in the ``DescribeElasticsearchDomains`` request.

      - *(dict) --*

        The current status of an Elasticsearch domain.

        - **DomainId** *(string) --*

          The unique identifier for the specified Elasticsearch domain.

        - **DomainName** *(string) --*

          The name of an Elasticsearch domain. Domain names are unique across the domains owned by
          an account within an AWS region. Domain names start with a letter or number and can
          contain the following characters: a-z (lowercase), 0-9, and - (hyphen).

        - **ARN** *(string) --*

          The Amazon resource name (ARN) of an Elasticsearch domain. See `Identifiers for IAM
          Entities
          <http://docs.aws.amazon.com/IAM/latest/UserGuide/index.html?Using_Identifiers.html>`__ in
          *Using AWS Identity and Access Management* for more information.

        - **Created** *(boolean) --*

          The domain creation status. ``True`` if the creation of an Elasticsearch domain is
          complete. ``False`` if domain creation is still in progress.

        - **Deleted** *(boolean) --*

          The domain deletion status. ``True`` if a delete request has been received for the domain
          but resource cleanup is still in progress. ``False`` if the domain has not been deleted.
          Once domain deletion is complete, the status of the domain is no longer returned.

        - **Endpoint** *(string) --*

          The Elasticsearch domain endpoint that you use to submit index and search requests.

        - **Endpoints** *(dict) --*

          Map containing the Elasticsearch domain endpoints used to submit index and search
          requests. Example ``key, value`` :
          ``'vpc','vpc-endpoint-h2dsd34efgyghrtguk5gt6j2foh4.us-east-1.es.amazonaws.com'`` .

          - *(string) --*

            - *(string) --*

              The endpoint to which service requests are submitted. For example,
              ``search-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.es.amazonaws.com`` or
              ``doc-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.es.amazonaws.com`` .

        - **Processing** *(boolean) --*

          The status of the Elasticsearch domain configuration. ``True`` if Amazon Elasticsearch
          Service is processing configuration changes. ``False`` if the configuration is active.

        - **UpgradeProcessing** *(boolean) --*

          The status of an Elasticsearch domain version upgrade. ``True`` if Amazon Elasticsearch
          Service is undergoing a version upgrade. ``False`` if the configuration is active.

        - **ElasticsearchVersion** *(string) --*

        - **ElasticsearchClusterConfig** *(dict) --*

          The type and number of instances in the domain cluster.

          - **InstanceType** *(string) --*

            The instance type for an Elasticsearch cluster.

          - **InstanceCount** *(integer) --*

            The number of instances in the specified domain cluster.

          - **DedicatedMasterEnabled** *(boolean) --*

            A boolean value to indicate whether a dedicated master node is enabled. See `About
            Dedicated Master Nodes
            <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains.html#es-managedomains-dedicatedmasternodes>`__
            for more information.

          - **ZoneAwarenessEnabled** *(boolean) --*

            A boolean value to indicate whether zone awareness is enabled. See `About Zone
            Awareness
            <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains.html#es-managedomains-zoneawareness>`__
            for more information.

          - **ZoneAwarenessConfig** *(dict) --*

            Specifies the zone awareness configuration for a domain when zone awareness is enabled.

            - **AvailabilityZoneCount** *(integer) --*

              An integer value to indicate the number of availability zones for a domain when zone
              awareness is enabled. This should be equal to number of subnets if VPC endpoints is
              enabled

          - **DedicatedMasterType** *(string) --*

            The instance type for a dedicated master node.

          - **DedicatedMasterCount** *(integer) --*

            Total number of dedicated master nodes, active and on standby, for the cluster.

        - **EBSOptions** *(dict) --*

          The ``EBSOptions`` for the specified domain. See `Configuring EBS-based Storage
          <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html#es-createdomain-configure-ebs>`__
          for more information.

          - **EBSEnabled** *(boolean) --*

            Specifies whether EBS-based storage is enabled.

          - **VolumeType** *(string) --*

            Specifies the volume type for EBS-based storage.

          - **VolumeSize** *(integer) --*

            Integer to specify the size of an EBS volume.

          - **Iops** *(integer) --*

            Specifies the IOPD for a Provisioned IOPS EBS volume (SSD).

        - **AccessPolicies** *(string) --*

          IAM access policy as a JSON-formatted string.

        - **SnapshotOptions** *(dict) --*

          Specifies the status of the ``SnapshotOptions``

          - **AutomatedSnapshotStartHour** *(integer) --*

            Specifies the time, in UTC format, when the service takes a daily automated snapshot of
            the specified Elasticsearch domain. Default value is ``0`` hours.

        - **VPCOptions** *(dict) --*

          The ``VPCOptions`` for the specified domain. For more information, see `VPC Endpoints for
          Amazon Elasticsearch Service Domains
          <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html>`__ .

          - **VPCId** *(string) --*

            The VPC Id for the Elasticsearch domain. Exists only if the domain was created with
            VPCOptions.

          - **SubnetIds** *(list) --*

            Specifies the subnets for VPC endpoint.

            - *(string) --*

          - **AvailabilityZones** *(list) --*

            The availability zones for the Elasticsearch domain. Exists only if the domain was
            created with VPCOptions.

            - *(string) --*

          - **SecurityGroupIds** *(list) --*

            Specifies the security groups for VPC endpoint.

            - *(string) --*

        - **CognitoOptions** *(dict) --*

          The ``CognitoOptions`` for the specified domain. For more information, see `Amazon
          Cognito Authentication for Kibana
          <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-cognito-auth.html>`__
          .

          - **Enabled** *(boolean) --*

            Specifies the option to enable Cognito for Kibana authentication.

          - **UserPoolId** *(string) --*

            Specifies the Cognito user pool ID for Kibana authentication.

          - **IdentityPoolId** *(string) --*

            Specifies the Cognito identity pool ID for Kibana authentication.

          - **RoleArn** *(string) --*

            Specifies the role ARN that provides Elasticsearch permissions for accessing Cognito
            resources.

        - **EncryptionAtRestOptions** *(dict) --*

          Specifies the status of the ``EncryptionAtRestOptions`` .

          - **Enabled** *(boolean) --*

            Specifies the option to enable Encryption At Rest.

          - **KmsKeyId** *(string) --*

            Specifies the KMS Key ID for Encryption At Rest options.

        - **NodeToNodeEncryptionOptions** *(dict) --*

          Specifies the status of the ``NodeToNodeEncryptionOptions`` .

          - **Enabled** *(boolean) --*

            Specify true to enable node-to-node encryption.

        - **AdvancedOptions** *(dict) --*

          Specifies the status of the ``AdvancedOptions``

          - *(string) --*

            - *(string) --*

        - **LogPublishingOptions** *(dict) --*

          Log publishing options for the given domain.

          - *(string) --*

            Type of Log File, it can be one of the following:

            * INDEX_SLOW_LOGS: Index slow logs contain insert requests that took more time than
            configured index query log threshold to execute.

            * SEARCH_SLOW_LOGS: Search slow logs contain search queries that took more time than
            configured search query log threshold to execute.

            * ES_APPLICATION_LOGS: Elasticsearch application logs contain information about errors
            and warnings raised during the operation of the service and can be useful for
            troubleshooting.

            - *(dict) --*

              Log Publishing option that is set for given domain. Attributes and their details:

              * CloudWatchLogsLogGroupArn: ARN of the Cloudwatch log group to which log needs to be
              published.

              * Enabled: Whether the log publishing for given log type is enabled or not

              - **CloudWatchLogsLogGroupArn** *(string) --*

                ARN of the Cloudwatch log group to which log needs to be published.

              - **Enabled** *(boolean) --*

                Specifies whether given log publishing option is enabled or not.

        - **ServiceSoftwareOptions** *(dict) --*

          The current status of the Elasticsearch domain's service software.

          - **CurrentVersion** *(string) --*

            The current service software version that is present on the domain.

          - **NewVersion** *(string) --*

            The new service software version if one is available.

          - **UpdateAvailable** *(boolean) --*

            ``True`` if you are able to update you service software version. ``False`` if you are
            not able to update your service software version.

          - **Cancellable** *(boolean) --*

            ``True`` if you are able to cancel your service software version update. ``False`` if
            you are not able to cancel your service software version.

          - **UpdateStatus** *(string) --*

            The status of your service software update. This field can take the following values:
            ``ELIGIBLE`` , ``PENDING_UPDATE`` , ``IN_PROGRESS`` , ``COMPLETED`` , and
            ``NOT_ELIGIBLE`` .

          - **Description** *(string) --*

            The description of the ``UpdateStatus`` .

          - **AutomatedUpdateDate** *(datetime) --*

            Timestamp, in Epoch time, until which you can manually request a service software
            update. After this date, we automatically update your service software.

        - **DomainEndpointOptions** *(dict) --*

          The current status of the Elasticsearch domain's endpoint options.

          - **EnforceHTTPS** *(boolean) --*

            Specify if only HTTPS endpoint should be enabled for the Elasticsearch domain.

          - **TLSSecurityPolicy** *(string) --*

            Specify the TLS security policy that needs to be applied to the HTTPS endpoint of
            Elasticsearch domain. It can be one of the following values:

            * **Policy-Min-TLS-1-0-2019-07:** TLS security policy which supports TLSv1.0 and higher.

            * **Policy-Min-TLS-1-2-2019-07:** TLS security policy which supports only TLSv1.2
    """


_ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleAdditionalLimitsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleAdditionalLimitsTypeDef",
    {"LimitName": str, "LimitValues": List[str]},
    total=False,
)


class ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleAdditionalLimitsTypeDef(
    _ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleAdditionalLimitsTypeDef
):
    """
    Type definition for `ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRole` `AdditionalLimits`

    List of limits that are specific to a given InstanceType and for each of it's ``
    InstanceRole `` .

    - **LimitName** *(string) --*

      Name of Additional Limit is specific to a given InstanceType and for each of it's
      ``  InstanceRole `` etc. Attributes and their details:

      * MaximumNumberOfDataNodesSupported
      This attribute will be present in Master node only to specify how much data nodes
      upto which given ``  ESPartitionInstanceType `` can support as master node.
      * MaximumNumberOfDataNodesWithoutMasterNode
      This attribute will be present in Data node only to specify how much data nodes of
      given ``  ESPartitionInstanceType `` upto which you don't need any master nodes to
      govern them.

    - **LimitValues** *(list) --*

      Value for given ``  AdditionalLimit$LimitName `` .

      - *(string) --*
    """


_ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleInstanceLimitsInstanceCountLimitsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleInstanceLimitsInstanceCountLimitsTypeDef",
    {"MinimumInstanceCount": int, "MaximumInstanceCount": int},
    total=False,
)


class ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleInstanceLimitsInstanceCountLimitsTypeDef(
    _ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleInstanceLimitsInstanceCountLimitsTypeDef
):
    """
    Type definition for `ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleInstanceLimits` `InstanceCountLimits`

    InstanceCountLimits represents the limits on number of instances that be created in
    Amazon Elasticsearch for given InstanceType.

    - **MinimumInstanceCount** *(integer) --*

      Minimum number of Instances that can be instantiated for given InstanceType.

    - **MaximumInstanceCount** *(integer) --*

      Maximum number of Instances that can be instantiated for given InstanceType.
    """


_ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleInstanceLimitsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleInstanceLimitsTypeDef",
    {
        "InstanceCountLimits": ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleInstanceLimitsInstanceCountLimitsTypeDef
    },
    total=False,
)


class ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleInstanceLimitsTypeDef(
    _ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleInstanceLimitsTypeDef
):
    """
    Type definition for `ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRole` `InstanceLimits`

    InstanceLimits represents the list of instance related attributes that are available
    for given InstanceType.

    - **InstanceCountLimits** *(dict) --*

      InstanceCountLimits represents the limits on number of instances that be created in
      Amazon Elasticsearch for given InstanceType.

      - **MinimumInstanceCount** *(integer) --*

        Minimum number of Instances that can be instantiated for given InstanceType.

      - **MaximumInstanceCount** *(integer) --*

        Maximum number of Instances that can be instantiated for given InstanceType.
    """


_ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleStorageTypesStorageTypeLimitsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleStorageTypesStorageTypeLimitsTypeDef",
    {"LimitName": str, "LimitValues": List[str]},
    total=False,
)


class ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleStorageTypesStorageTypeLimitsTypeDef(
    _ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleStorageTypesStorageTypeLimitsTypeDef
):
    """
    Type definition for `ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleStorageTypes` `StorageTypeLimits`

    Limits that are applicable for given storage type.

    - **LimitName** *(string) --*

      Name of storage limits that are applicable for given storage type. If ``
      StorageType `` is ebs, following storage options are applicable

      * MinimumVolumeSize
      Minimum amount of volume size that is applicable for given storage type.It can
      be empty if it is not applicable.
      * MaximumVolumeSize
      Maximum amount of volume size that is applicable for given storage type.It can
      be empty if it is not applicable.
      * MaximumIops
      Maximum amount of Iops that is applicable for given storage type.It can be
      empty if it is not applicable.
      * MinimumIops
      Minimum amount of Iops that is applicable for given storage type.It can be
      empty if it is not applicable.

    - **LimitValues** *(list) --*

      Values for the ``  StorageTypeLimit$LimitName `` .

      - *(string) --*
    """


_ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleStorageTypesTypeDef = TypedDict(
    "_ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleStorageTypesTypeDef",
    {
        "StorageTypeName": str,
        "StorageSubTypeName": str,
        "StorageTypeLimits": List[
            ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleStorageTypesStorageTypeLimitsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleStorageTypesTypeDef(
    _ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleStorageTypesTypeDef
):
    """
    Type definition for `ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRole` `StorageTypes`

    StorageTypes represents the list of storage related types and their attributes that
    are available for given InstanceType.

    - **StorageTypeName** *(string) --*

      Type of the storage. List of available storage options:

      * instance
      Inbuilt storage available for the given Instance
      * ebs
      Elastic block storage that would be attached to the given Instance

    - **StorageSubTypeName** *(string) --*

      SubType of the given storage type. List of available sub-storage options: For
      "instance" storageType we wont have any storageSubType, in case of "ebs"
      storageType we will have following valid storageSubTypes

      * standard

      * gp2

      * io1

      Refer `` VolumeType`` for more information regarding above EBS storage options.

    - **StorageTypeLimits** *(list) --*

      List of limits that are applicable for given storage type.

      - *(dict) --*

        Limits that are applicable for given storage type.

        - **LimitName** *(string) --*

          Name of storage limits that are applicable for given storage type. If ``
          StorageType `` is ebs, following storage options are applicable

          * MinimumVolumeSize
          Minimum amount of volume size that is applicable for given storage type.It can
          be empty if it is not applicable.
          * MaximumVolumeSize
          Maximum amount of volume size that is applicable for given storage type.It can
          be empty if it is not applicable.
          * MaximumIops
          Maximum amount of Iops that is applicable for given storage type.It can be
          empty if it is not applicable.
          * MinimumIops
          Minimum amount of Iops that is applicable for given storage type.It can be
          empty if it is not applicable.

        - **LimitValues** *(list) --*

          Values for the ``  StorageTypeLimit$LimitName `` .

          - *(string) --*
    """


_ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleTypeDef = TypedDict(
    "_ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleTypeDef",
    {
        "StorageTypes": List[
            ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleStorageTypesTypeDef
        ],
        "InstanceLimits": ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleInstanceLimitsTypeDef,
        "AdditionalLimits": List[
            ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleAdditionalLimitsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleTypeDef(
    _ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleTypeDef
):
    """
    Type definition for `ClientDescribeElasticsearchInstanceTypeLimitsResponse` `LimitsByRole`

    Limits for given InstanceType and for each of it's role. Limits contains following ``
    StorageTypes, ``  ``  InstanceLimits `` and ``  AdditionalLimits ``

    - **StorageTypes** *(list) --*

      StorageType represents the list of storage related types and attributes that are
      available for given InstanceType.

      - *(dict) --*

        StorageTypes represents the list of storage related types and their attributes that
        are available for given InstanceType.

        - **StorageTypeName** *(string) --*

          Type of the storage. List of available storage options:

          * instance
          Inbuilt storage available for the given Instance
          * ebs
          Elastic block storage that would be attached to the given Instance

        - **StorageSubTypeName** *(string) --*

          SubType of the given storage type. List of available sub-storage options: For
          "instance" storageType we wont have any storageSubType, in case of "ebs"
          storageType we will have following valid storageSubTypes

          * standard

          * gp2

          * io1

          Refer `` VolumeType`` for more information regarding above EBS storage options.

        - **StorageTypeLimits** *(list) --*

          List of limits that are applicable for given storage type.

          - *(dict) --*

            Limits that are applicable for given storage type.

            - **LimitName** *(string) --*

              Name of storage limits that are applicable for given storage type. If ``
              StorageType `` is ebs, following storage options are applicable

              * MinimumVolumeSize
              Minimum amount of volume size that is applicable for given storage type.It can
              be empty if it is not applicable.
              * MaximumVolumeSize
              Maximum amount of volume size that is applicable for given storage type.It can
              be empty if it is not applicable.
              * MaximumIops
              Maximum amount of Iops that is applicable for given storage type.It can be
              empty if it is not applicable.
              * MinimumIops
              Minimum amount of Iops that is applicable for given storage type.It can be
              empty if it is not applicable.

            - **LimitValues** *(list) --*

              Values for the ``  StorageTypeLimit$LimitName `` .

              - *(string) --*

    - **InstanceLimits** *(dict) --*

      InstanceLimits represents the list of instance related attributes that are available
      for given InstanceType.

      - **InstanceCountLimits** *(dict) --*

        InstanceCountLimits represents the limits on number of instances that be created in
        Amazon Elasticsearch for given InstanceType.

        - **MinimumInstanceCount** *(integer) --*

          Minimum number of Instances that can be instantiated for given InstanceType.

        - **MaximumInstanceCount** *(integer) --*

          Maximum number of Instances that can be instantiated for given InstanceType.

    - **AdditionalLimits** *(list) --*

      List of additional limits that are specific to a given InstanceType and for each of
      it's ``  InstanceRole `` .

      - *(dict) --*

        List of limits that are specific to a given InstanceType and for each of it's ``
        InstanceRole `` .

        - **LimitName** *(string) --*

          Name of Additional Limit is specific to a given InstanceType and for each of it's
          ``  InstanceRole `` etc. Attributes and their details:

          * MaximumNumberOfDataNodesSupported
          This attribute will be present in Master node only to specify how much data nodes
          upto which given ``  ESPartitionInstanceType `` can support as master node.
          * MaximumNumberOfDataNodesWithoutMasterNode
          This attribute will be present in Data node only to specify how much data nodes of
          given ``  ESPartitionInstanceType `` upto which you don't need any master nodes to
          govern them.

        - **LimitValues** *(list) --*

          Value for given ``  AdditionalLimit$LimitName `` .

          - *(string) --*
    """


_ClientDescribeElasticsearchInstanceTypeLimitsResponseTypeDef = TypedDict(
    "_ClientDescribeElasticsearchInstanceTypeLimitsResponseTypeDef",
    {
        "LimitsByRole": Dict[
            str,
            ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleTypeDef,
        ]
    },
    total=False,
)


class ClientDescribeElasticsearchInstanceTypeLimitsResponseTypeDef(
    _ClientDescribeElasticsearchInstanceTypeLimitsResponseTypeDef
):
    """
    Type definition for `ClientDescribeElasticsearchInstanceTypeLimits` `Response`

    Container for the parameters received from ``  DescribeElasticsearchInstanceTypeLimits ``
    operation.

    - **LimitsByRole** *(dict) --*

      Map of Role of the Instance and Limits that are applicable. Role performed by given Instance
      in Elasticsearch can be one of the following:

      * Data: If the given InstanceType is used as Data node

      * Master: If the given InstanceType is used as Master node

      - *(string) --*

        - *(dict) --*

          Limits for given InstanceType and for each of it's role. Limits contains following ``
          StorageTypes, ``  ``  InstanceLimits `` and ``  AdditionalLimits ``

          - **StorageTypes** *(list) --*

            StorageType represents the list of storage related types and attributes that are
            available for given InstanceType.

            - *(dict) --*

              StorageTypes represents the list of storage related types and their attributes that
              are available for given InstanceType.

              - **StorageTypeName** *(string) --*

                Type of the storage. List of available storage options:

                * instance
                Inbuilt storage available for the given Instance
                * ebs
                Elastic block storage that would be attached to the given Instance

              - **StorageSubTypeName** *(string) --*

                SubType of the given storage type. List of available sub-storage options: For
                "instance" storageType we wont have any storageSubType, in case of "ebs"
                storageType we will have following valid storageSubTypes

                * standard

                * gp2

                * io1

                Refer `` VolumeType`` for more information regarding above EBS storage options.

              - **StorageTypeLimits** *(list) --*

                List of limits that are applicable for given storage type.

                - *(dict) --*

                  Limits that are applicable for given storage type.

                  - **LimitName** *(string) --*

                    Name of storage limits that are applicable for given storage type. If ``
                    StorageType `` is ebs, following storage options are applicable

                    * MinimumVolumeSize
                    Minimum amount of volume size that is applicable for given storage type.It can
                    be empty if it is not applicable.
                    * MaximumVolumeSize
                    Maximum amount of volume size that is applicable for given storage type.It can
                    be empty if it is not applicable.
                    * MaximumIops
                    Maximum amount of Iops that is applicable for given storage type.It can be
                    empty if it is not applicable.
                    * MinimumIops
                    Minimum amount of Iops that is applicable for given storage type.It can be
                    empty if it is not applicable.

                  - **LimitValues** *(list) --*

                    Values for the ``  StorageTypeLimit$LimitName `` .

                    - *(string) --*

          - **InstanceLimits** *(dict) --*

            InstanceLimits represents the list of instance related attributes that are available
            for given InstanceType.

            - **InstanceCountLimits** *(dict) --*

              InstanceCountLimits represents the limits on number of instances that be created in
              Amazon Elasticsearch for given InstanceType.

              - **MinimumInstanceCount** *(integer) --*

                Minimum number of Instances that can be instantiated for given InstanceType.

              - **MaximumInstanceCount** *(integer) --*

                Maximum number of Instances that can be instantiated for given InstanceType.

          - **AdditionalLimits** *(list) --*

            List of additional limits that are specific to a given InstanceType and for each of
            it's ``  InstanceRole `` .

            - *(dict) --*

              List of limits that are specific to a given InstanceType and for each of it's ``
              InstanceRole `` .

              - **LimitName** *(string) --*

                Name of Additional Limit is specific to a given InstanceType and for each of it's
                ``  InstanceRole `` etc. Attributes and their details:

                * MaximumNumberOfDataNodesSupported
                This attribute will be present in Master node only to specify how much data nodes
                upto which given ``  ESPartitionInstanceType `` can support as master node.
                * MaximumNumberOfDataNodesWithoutMasterNode
                This attribute will be present in Data node only to specify how much data nodes of
                given ``  ESPartitionInstanceType `` upto which you don't need any master nodes to
                govern them.

              - **LimitValues** *(list) --*

                Value for given ``  AdditionalLimit$LimitName `` .

                - *(string) --*
    """


_ClientDescribeReservedElasticsearchInstanceOfferingsResponseReservedElasticsearchInstanceOfferingsRecurringChargesTypeDef = TypedDict(
    "_ClientDescribeReservedElasticsearchInstanceOfferingsResponseReservedElasticsearchInstanceOfferingsRecurringChargesTypeDef",
    {"RecurringChargeAmount": float, "RecurringChargeFrequency": str},
    total=False,
)


class ClientDescribeReservedElasticsearchInstanceOfferingsResponseReservedElasticsearchInstanceOfferingsRecurringChargesTypeDef(
    _ClientDescribeReservedElasticsearchInstanceOfferingsResponseReservedElasticsearchInstanceOfferingsRecurringChargesTypeDef
):
    """
    Type definition for `ClientDescribeReservedElasticsearchInstanceOfferingsResponseReservedElasticsearchInstanceOfferings` `RecurringCharges`

    Contains the specific price and frequency of a recurring charges for a reserved
    Elasticsearch instance, or for a reserved Elasticsearch instance offering.

    - **RecurringChargeAmount** *(float) --*

      The monetary amount of the recurring charge.

    - **RecurringChargeFrequency** *(string) --*

      The frequency of the recurring charge.
    """


_ClientDescribeReservedElasticsearchInstanceOfferingsResponseReservedElasticsearchInstanceOfferingsTypeDef = TypedDict(
    "_ClientDescribeReservedElasticsearchInstanceOfferingsResponseReservedElasticsearchInstanceOfferingsTypeDef",
    {
        "ReservedElasticsearchInstanceOfferingId": str,
        "ElasticsearchInstanceType": str,
        "Duration": int,
        "FixedPrice": float,
        "UsagePrice": float,
        "CurrencyCode": str,
        "PaymentOption": str,
        "RecurringCharges": List[
            ClientDescribeReservedElasticsearchInstanceOfferingsResponseReservedElasticsearchInstanceOfferingsRecurringChargesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeReservedElasticsearchInstanceOfferingsResponseReservedElasticsearchInstanceOfferingsTypeDef(
    _ClientDescribeReservedElasticsearchInstanceOfferingsResponseReservedElasticsearchInstanceOfferingsTypeDef
):
    """
    Type definition for `ClientDescribeReservedElasticsearchInstanceOfferingsResponse` `ReservedElasticsearchInstanceOfferings`

    Details of a reserved Elasticsearch instance offering.

    - **ReservedElasticsearchInstanceOfferingId** *(string) --*

      The Elasticsearch reserved instance offering identifier.

    - **ElasticsearchInstanceType** *(string) --*

      The Elasticsearch instance type offered by the reserved instance offering.

    - **Duration** *(integer) --*

      The duration, in seconds, for which the offering will reserve the Elasticsearch instance.

    - **FixedPrice** *(float) --*

      The upfront fixed charge you will pay to purchase the specific reserved Elasticsearch
      instance offering.

    - **UsagePrice** *(float) --*

      The rate you are charged for each hour the domain that is using the offering is running.

    - **CurrencyCode** *(string) --*

      The currency code for the reserved Elasticsearch instance offering.

    - **PaymentOption** *(string) --*

      Payment option for the reserved Elasticsearch instance offering

    - **RecurringCharges** *(list) --*

      The charge to your account regardless of whether you are creating any domains using the
      instance offering.

      - *(dict) --*

        Contains the specific price and frequency of a recurring charges for a reserved
        Elasticsearch instance, or for a reserved Elasticsearch instance offering.

        - **RecurringChargeAmount** *(float) --*

          The monetary amount of the recurring charge.

        - **RecurringChargeFrequency** *(string) --*

          The frequency of the recurring charge.
    """


_ClientDescribeReservedElasticsearchInstanceOfferingsResponseTypeDef = TypedDict(
    "_ClientDescribeReservedElasticsearchInstanceOfferingsResponseTypeDef",
    {
        "NextToken": str,
        "ReservedElasticsearchInstanceOfferings": List[
            ClientDescribeReservedElasticsearchInstanceOfferingsResponseReservedElasticsearchInstanceOfferingsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeReservedElasticsearchInstanceOfferingsResponseTypeDef(
    _ClientDescribeReservedElasticsearchInstanceOfferingsResponseTypeDef
):
    """
    Type definition for `ClientDescribeReservedElasticsearchInstanceOfferings` `Response`

    Container for results from ``DescribeReservedElasticsearchInstanceOfferings``

    - **NextToken** *(string) --*

      Provides an identifier to allow retrieval of paginated results.

    - **ReservedElasticsearchInstanceOfferings** *(list) --*

      List of reserved Elasticsearch instance offerings

      - *(dict) --*

        Details of a reserved Elasticsearch instance offering.

        - **ReservedElasticsearchInstanceOfferingId** *(string) --*

          The Elasticsearch reserved instance offering identifier.

        - **ElasticsearchInstanceType** *(string) --*

          The Elasticsearch instance type offered by the reserved instance offering.

        - **Duration** *(integer) --*

          The duration, in seconds, for which the offering will reserve the Elasticsearch instance.

        - **FixedPrice** *(float) --*

          The upfront fixed charge you will pay to purchase the specific reserved Elasticsearch
          instance offering.

        - **UsagePrice** *(float) --*

          The rate you are charged for each hour the domain that is using the offering is running.

        - **CurrencyCode** *(string) --*

          The currency code for the reserved Elasticsearch instance offering.

        - **PaymentOption** *(string) --*

          Payment option for the reserved Elasticsearch instance offering

        - **RecurringCharges** *(list) --*

          The charge to your account regardless of whether you are creating any domains using the
          instance offering.

          - *(dict) --*

            Contains the specific price and frequency of a recurring charges for a reserved
            Elasticsearch instance, or for a reserved Elasticsearch instance offering.

            - **RecurringChargeAmount** *(float) --*

              The monetary amount of the recurring charge.

            - **RecurringChargeFrequency** *(string) --*

              The frequency of the recurring charge.
    """


_ClientDescribeReservedElasticsearchInstancesResponseReservedElasticsearchInstancesRecurringChargesTypeDef = TypedDict(
    "_ClientDescribeReservedElasticsearchInstancesResponseReservedElasticsearchInstancesRecurringChargesTypeDef",
    {"RecurringChargeAmount": float, "RecurringChargeFrequency": str},
    total=False,
)


class ClientDescribeReservedElasticsearchInstancesResponseReservedElasticsearchInstancesRecurringChargesTypeDef(
    _ClientDescribeReservedElasticsearchInstancesResponseReservedElasticsearchInstancesRecurringChargesTypeDef
):
    """
    Type definition for `ClientDescribeReservedElasticsearchInstancesResponseReservedElasticsearchInstances` `RecurringCharges`

    Contains the specific price and frequency of a recurring charges for a reserved
    Elasticsearch instance, or for a reserved Elasticsearch instance offering.

    - **RecurringChargeAmount** *(float) --*

      The monetary amount of the recurring charge.

    - **RecurringChargeFrequency** *(string) --*

      The frequency of the recurring charge.
    """


_ClientDescribeReservedElasticsearchInstancesResponseReservedElasticsearchInstancesTypeDef = TypedDict(
    "_ClientDescribeReservedElasticsearchInstancesResponseReservedElasticsearchInstancesTypeDef",
    {
        "ReservationName": str,
        "ReservedElasticsearchInstanceId": str,
        "ReservedElasticsearchInstanceOfferingId": str,
        "ElasticsearchInstanceType": str,
        "StartTime": datetime,
        "Duration": int,
        "FixedPrice": float,
        "UsagePrice": float,
        "CurrencyCode": str,
        "ElasticsearchInstanceCount": int,
        "State": str,
        "PaymentOption": str,
        "RecurringCharges": List[
            ClientDescribeReservedElasticsearchInstancesResponseReservedElasticsearchInstancesRecurringChargesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeReservedElasticsearchInstancesResponseReservedElasticsearchInstancesTypeDef(
    _ClientDescribeReservedElasticsearchInstancesResponseReservedElasticsearchInstancesTypeDef
):
    """
    Type definition for `ClientDescribeReservedElasticsearchInstancesResponse` `ReservedElasticsearchInstances`

    Details of a reserved Elasticsearch instance.

    - **ReservationName** *(string) --*

      The customer-specified identifier to track this reservation.

    - **ReservedElasticsearchInstanceId** *(string) --*

      The unique identifier for the reservation.

    - **ReservedElasticsearchInstanceOfferingId** *(string) --*

      The offering identifier.

    - **ElasticsearchInstanceType** *(string) --*

      The Elasticsearch instance type offered by the reserved instance offering.

    - **StartTime** *(datetime) --*

      The time the reservation started.

    - **Duration** *(integer) --*

      The duration, in seconds, for which the Elasticsearch instance is reserved.

    - **FixedPrice** *(float) --*

      The upfront fixed charge you will paid to purchase the specific reserved Elasticsearch
      instance offering.

    - **UsagePrice** *(float) --*

      The rate you are charged for each hour for the domain that is using this reserved
      instance.

    - **CurrencyCode** *(string) --*

      The currency code for the reserved Elasticsearch instance offering.

    - **ElasticsearchInstanceCount** *(integer) --*

      The number of Elasticsearch instances that have been reserved.

    - **State** *(string) --*

      The state of the reserved Elasticsearch instance.

    - **PaymentOption** *(string) --*

      The payment option as defined in the reserved Elasticsearch instance offering.

    - **RecurringCharges** *(list) --*

      The charge to your account regardless of whether you are creating any domains using the
      instance offering.

      - *(dict) --*

        Contains the specific price and frequency of a recurring charges for a reserved
        Elasticsearch instance, or for a reserved Elasticsearch instance offering.

        - **RecurringChargeAmount** *(float) --*

          The monetary amount of the recurring charge.

        - **RecurringChargeFrequency** *(string) --*

          The frequency of the recurring charge.
    """


_ClientDescribeReservedElasticsearchInstancesResponseTypeDef = TypedDict(
    "_ClientDescribeReservedElasticsearchInstancesResponseTypeDef",
    {
        "NextToken": str,
        "ReservedElasticsearchInstances": List[
            ClientDescribeReservedElasticsearchInstancesResponseReservedElasticsearchInstancesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeReservedElasticsearchInstancesResponseTypeDef(
    _ClientDescribeReservedElasticsearchInstancesResponseTypeDef
):
    """
    Type definition for `ClientDescribeReservedElasticsearchInstances` `Response`

    Container for results from ``DescribeReservedElasticsearchInstances``

    - **NextToken** *(string) --*

      Provides an identifier to allow retrieval of paginated results.

    - **ReservedElasticsearchInstances** *(list) --*

      List of reserved Elasticsearch instances.

      - *(dict) --*

        Details of a reserved Elasticsearch instance.

        - **ReservationName** *(string) --*

          The customer-specified identifier to track this reservation.

        - **ReservedElasticsearchInstanceId** *(string) --*

          The unique identifier for the reservation.

        - **ReservedElasticsearchInstanceOfferingId** *(string) --*

          The offering identifier.

        - **ElasticsearchInstanceType** *(string) --*

          The Elasticsearch instance type offered by the reserved instance offering.

        - **StartTime** *(datetime) --*

          The time the reservation started.

        - **Duration** *(integer) --*

          The duration, in seconds, for which the Elasticsearch instance is reserved.

        - **FixedPrice** *(float) --*

          The upfront fixed charge you will paid to purchase the specific reserved Elasticsearch
          instance offering.

        - **UsagePrice** *(float) --*

          The rate you are charged for each hour for the domain that is using this reserved
          instance.

        - **CurrencyCode** *(string) --*

          The currency code for the reserved Elasticsearch instance offering.

        - **ElasticsearchInstanceCount** *(integer) --*

          The number of Elasticsearch instances that have been reserved.

        - **State** *(string) --*

          The state of the reserved Elasticsearch instance.

        - **PaymentOption** *(string) --*

          The payment option as defined in the reserved Elasticsearch instance offering.

        - **RecurringCharges** *(list) --*

          The charge to your account regardless of whether you are creating any domains using the
          instance offering.

          - *(dict) --*

            Contains the specific price and frequency of a recurring charges for a reserved
            Elasticsearch instance, or for a reserved Elasticsearch instance offering.

            - **RecurringChargeAmount** *(float) --*

              The monetary amount of the recurring charge.

            - **RecurringChargeFrequency** *(string) --*

              The frequency of the recurring charge.
    """


_ClientGetCompatibleElasticsearchVersionsResponseCompatibleElasticsearchVersionsTypeDef = TypedDict(
    "_ClientGetCompatibleElasticsearchVersionsResponseCompatibleElasticsearchVersionsTypeDef",
    {"SourceVersion": str, "TargetVersions": List[str]},
    total=False,
)


class ClientGetCompatibleElasticsearchVersionsResponseCompatibleElasticsearchVersionsTypeDef(
    _ClientGetCompatibleElasticsearchVersionsResponseCompatibleElasticsearchVersionsTypeDef
):
    """
    Type definition for `ClientGetCompatibleElasticsearchVersionsResponse` `CompatibleElasticsearchVersions`

    A map from an ``  ElasticsearchVersion `` to a list of compatible ``  ElasticsearchVersion
    `` s to which the domain can be upgraded.

    - **SourceVersion** *(string) --*

      The current version of Elasticsearch on which a domain is.

    - **TargetVersions** *(list) --*

      List of supported elastic search versions.

      - *(string) --*
    """


_ClientGetCompatibleElasticsearchVersionsResponseTypeDef = TypedDict(
    "_ClientGetCompatibleElasticsearchVersionsResponseTypeDef",
    {
        "CompatibleElasticsearchVersions": List[
            ClientGetCompatibleElasticsearchVersionsResponseCompatibleElasticsearchVersionsTypeDef
        ]
    },
    total=False,
)


class ClientGetCompatibleElasticsearchVersionsResponseTypeDef(
    _ClientGetCompatibleElasticsearchVersionsResponseTypeDef
):
    """
    Type definition for `ClientGetCompatibleElasticsearchVersions` `Response`

    Container for response returned by ``  GetCompatibleElasticsearchVersions `` operation.

    - **CompatibleElasticsearchVersions** *(list) --*

      A map of compatible Elasticsearch versions returned as part of the ``
      GetCompatibleElasticsearchVersions `` operation.

      - *(dict) --*

        A map from an ``  ElasticsearchVersion `` to a list of compatible ``  ElasticsearchVersion
        `` s to which the domain can be upgraded.

        - **SourceVersion** *(string) --*

          The current version of Elasticsearch on which a domain is.

        - **TargetVersions** *(list) --*

          List of supported elastic search versions.

          - *(string) --*
    """


_ClientGetUpgradeHistoryResponseUpgradeHistoriesStepsListTypeDef = TypedDict(
    "_ClientGetUpgradeHistoryResponseUpgradeHistoriesStepsListTypeDef",
    {
        "UpgradeStep": str,
        "UpgradeStepStatus": str,
        "Issues": List[str],
        "ProgressPercent": float,
    },
    total=False,
)


class ClientGetUpgradeHistoryResponseUpgradeHistoriesStepsListTypeDef(
    _ClientGetUpgradeHistoryResponseUpgradeHistoriesStepsListTypeDef
):
    """
    Type definition for `ClientGetUpgradeHistoryResponseUpgradeHistories` `StepsList`

    Represents a single step of the Upgrade or Upgrade Eligibility Check workflow.

    - **UpgradeStep** *(string) --*

      Represents one of 3 steps that an Upgrade or Upgrade Eligibility Check does through:

      * PreUpgradeCheck

      * Snapshot

      * Upgrade

    - **UpgradeStepStatus** *(string) --*

      The status of a particular step during an upgrade. The status can take one of the
      following values:

      * In Progress

      * Succeeded

      * Succeeded with Issues

      * Failed

    - **Issues** *(list) --*

      A list of strings containing detailed information about the errors encountered in a
      particular step.

      - *(string) --*

    - **ProgressPercent** *(float) --*

      The Floating point value representing progress percentage of a particular step.
    """


_ClientGetUpgradeHistoryResponseUpgradeHistoriesTypeDef = TypedDict(
    "_ClientGetUpgradeHistoryResponseUpgradeHistoriesTypeDef",
    {
        "UpgradeName": str,
        "StartTimestamp": datetime,
        "UpgradeStatus": str,
        "StepsList": List[
            ClientGetUpgradeHistoryResponseUpgradeHistoriesStepsListTypeDef
        ],
    },
    total=False,
)


class ClientGetUpgradeHistoryResponseUpgradeHistoriesTypeDef(
    _ClientGetUpgradeHistoryResponseUpgradeHistoriesTypeDef
):
    """
    Type definition for `ClientGetUpgradeHistoryResponse` `UpgradeHistories`

    History of the last 10 Upgrades and Upgrade Eligibility Checks.

    - **UpgradeName** *(string) --*

      A string that describes the update briefly

    - **StartTimestamp** *(datetime) --*

      UTC Timestamp at which the Upgrade API call was made in "yyyy-MM-ddTHH:mm:ssZ" format.

    - **UpgradeStatus** *(string) --*

      The overall status of the update. The status can take one of the following values:

      * In Progress

      * Succeeded

      * Succeeded with Issues

      * Failed

    - **StepsList** *(list) --*

      A list of ``  UpgradeStepItem `` s representing information about each step performed as
      pard of a specific Upgrade or Upgrade Eligibility Check.

      - *(dict) --*

        Represents a single step of the Upgrade or Upgrade Eligibility Check workflow.

        - **UpgradeStep** *(string) --*

          Represents one of 3 steps that an Upgrade or Upgrade Eligibility Check does through:

          * PreUpgradeCheck

          * Snapshot

          * Upgrade

        - **UpgradeStepStatus** *(string) --*

          The status of a particular step during an upgrade. The status can take one of the
          following values:

          * In Progress

          * Succeeded

          * Succeeded with Issues

          * Failed

        - **Issues** *(list) --*

          A list of strings containing detailed information about the errors encountered in a
          particular step.

          - *(string) --*

        - **ProgressPercent** *(float) --*

          The Floating point value representing progress percentage of a particular step.
    """


_ClientGetUpgradeHistoryResponseTypeDef = TypedDict(
    "_ClientGetUpgradeHistoryResponseTypeDef",
    {
        "UpgradeHistories": List[
            ClientGetUpgradeHistoryResponseUpgradeHistoriesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientGetUpgradeHistoryResponseTypeDef(_ClientGetUpgradeHistoryResponseTypeDef):
    """
    Type definition for `ClientGetUpgradeHistory` `Response`

    Container for response returned by ``  GetUpgradeHistory `` operation.

    - **UpgradeHistories** *(list) --*

      A list of ``  UpgradeHistory `` objects corresponding to each Upgrade or Upgrade Eligibility
      Check performed on a domain returned as part of ``  GetUpgradeHistoryResponse `` object.

      - *(dict) --*

        History of the last 10 Upgrades and Upgrade Eligibility Checks.

        - **UpgradeName** *(string) --*

          A string that describes the update briefly

        - **StartTimestamp** *(datetime) --*

          UTC Timestamp at which the Upgrade API call was made in "yyyy-MM-ddTHH:mm:ssZ" format.

        - **UpgradeStatus** *(string) --*

          The overall status of the update. The status can take one of the following values:

          * In Progress

          * Succeeded

          * Succeeded with Issues

          * Failed

        - **StepsList** *(list) --*

          A list of ``  UpgradeStepItem `` s representing information about each step performed as
          pard of a specific Upgrade or Upgrade Eligibility Check.

          - *(dict) --*

            Represents a single step of the Upgrade or Upgrade Eligibility Check workflow.

            - **UpgradeStep** *(string) --*

              Represents one of 3 steps that an Upgrade or Upgrade Eligibility Check does through:

              * PreUpgradeCheck

              * Snapshot

              * Upgrade

            - **UpgradeStepStatus** *(string) --*

              The status of a particular step during an upgrade. The status can take one of the
              following values:

              * In Progress

              * Succeeded

              * Succeeded with Issues

              * Failed

            - **Issues** *(list) --*

              A list of strings containing detailed information about the errors encountered in a
              particular step.

              - *(string) --*

            - **ProgressPercent** *(float) --*

              The Floating point value representing progress percentage of a particular step.

    - **NextToken** *(string) --*

      Pagination token that needs to be supplied to the next call to get the next page of results
    """


_ClientGetUpgradeStatusResponseTypeDef = TypedDict(
    "_ClientGetUpgradeStatusResponseTypeDef",
    {"UpgradeStep": str, "StepStatus": str, "UpgradeName": str},
    total=False,
)


class ClientGetUpgradeStatusResponseTypeDef(_ClientGetUpgradeStatusResponseTypeDef):
    """
    Type definition for `ClientGetUpgradeStatus` `Response`

    Container for response returned by ``  GetUpgradeStatus `` operation.

    - **UpgradeStep** *(string) --*

      Represents one of 3 steps that an Upgrade or Upgrade Eligibility Check does through:

      * PreUpgradeCheck

      * Snapshot

      * Upgrade

    - **StepStatus** *(string) --*

      One of 4 statuses that a step can go through returned as part of the ``
      GetUpgradeStatusResponse `` object. The status can take one of the following values:

      * In Progress

      * Succeeded

      * Succeeded with Issues

      * Failed

    - **UpgradeName** *(string) --*

      A string that describes the update briefly
    """


_ClientListDomainNamesResponseDomainNamesTypeDef = TypedDict(
    "_ClientListDomainNamesResponseDomainNamesTypeDef", {"DomainName": str}, total=False
)


class ClientListDomainNamesResponseDomainNamesTypeDef(
    _ClientListDomainNamesResponseDomainNamesTypeDef
):
    """
    Type definition for `ClientListDomainNamesResponse` `DomainNames`

    - **DomainName** *(string) --*

      Specifies the ``DomainName`` .
    """


_ClientListDomainNamesResponseTypeDef = TypedDict(
    "_ClientListDomainNamesResponseTypeDef",
    {"DomainNames": List[ClientListDomainNamesResponseDomainNamesTypeDef]},
    total=False,
)


class ClientListDomainNamesResponseTypeDef(_ClientListDomainNamesResponseTypeDef):
    """
    Type definition for `ClientListDomainNames` `Response`

    The result of a ``ListDomainNames`` operation. Contains the names of all Elasticsearch domains
    owned by this account.

    - **DomainNames** *(list) --*

      List of Elasticsearch domain names.

      - *(dict) --*

        - **DomainName** *(string) --*

          Specifies the ``DomainName`` .
    """


_ClientListElasticsearchInstanceTypesResponseTypeDef = TypedDict(
    "_ClientListElasticsearchInstanceTypesResponseTypeDef",
    {"ElasticsearchInstanceTypes": List[str], "NextToken": str},
    total=False,
)


class ClientListElasticsearchInstanceTypesResponseTypeDef(
    _ClientListElasticsearchInstanceTypesResponseTypeDef
):
    """
    Type definition for `ClientListElasticsearchInstanceTypes` `Response`

    Container for the parameters returned by ``  ListElasticsearchInstanceTypes `` operation.

    - **ElasticsearchInstanceTypes** *(list) --*

      List of instance types supported by Amazon Elasticsearch service for given ``
      ElasticsearchVersion ``

      - *(string) --*

    - **NextToken** *(string) --*

      In case if there are more results available NextToken would be present, make further request
      to the same API with received NextToken to paginate remaining results.
    """


_ClientListElasticsearchVersionsResponseTypeDef = TypedDict(
    "_ClientListElasticsearchVersionsResponseTypeDef",
    {"ElasticsearchVersions": List[str], "NextToken": str},
    total=False,
)


class ClientListElasticsearchVersionsResponseTypeDef(
    _ClientListElasticsearchVersionsResponseTypeDef
):
    """
    Type definition for `ClientListElasticsearchVersions` `Response`

    Container for the parameters for response received from ``  ListElasticsearchVersions ``
    operation.

    - **ElasticsearchVersions** *(list) --*

      List of supported elastic search versions.

      - *(string) --*

    - **NextToken** *(string) --*

      Paginated APIs accepts NextToken input to returns next page results and provides a NextToken
      output in the response which can be used by the client to retrieve more results.
    """


_ClientListTagsResponseTagListTypeDef = TypedDict(
    "_ClientListTagsResponseTagListTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientListTagsResponseTagListTypeDef(_ClientListTagsResponseTagListTypeDef):
    """
    Type definition for `ClientListTagsResponse` `TagList`

    Specifies a key value pair for a resource tag.

    - **Key** *(string) --*

      Specifies the ``TagKey`` , the name of the tag. Tag keys must be unique for the
      Elasticsearch domain to which they are attached.

    - **Value** *(string) --*

      Specifies the ``TagValue`` , the value assigned to the corresponding tag key. Tag values
      can be null and do not have to be unique in a tag set. For example, you can have a key
      value pair in a tag set of ``project : Trinity`` and ``cost-center : Trinity``
    """


_ClientListTagsResponseTypeDef = TypedDict(
    "_ClientListTagsResponseTypeDef",
    {"TagList": List[ClientListTagsResponseTagListTypeDef]},
    total=False,
)


class ClientListTagsResponseTypeDef(_ClientListTagsResponseTypeDef):
    """
    Type definition for `ClientListTags` `Response`

    The result of a ``ListTags`` operation. Contains tags for all requested Elasticsearch domains.

    - **TagList** *(list) --*

      List of ``Tag`` for the requested Elasticsearch domain.

      - *(dict) --*

        Specifies a key value pair for a resource tag.

        - **Key** *(string) --*

          Specifies the ``TagKey`` , the name of the tag. Tag keys must be unique for the
          Elasticsearch domain to which they are attached.

        - **Value** *(string) --*

          Specifies the ``TagValue`` , the value assigned to the corresponding tag key. Tag values
          can be null and do not have to be unique in a tag set. For example, you can have a key
          value pair in a tag set of ``project : Trinity`` and ``cost-center : Trinity``
    """


_ClientPurchaseReservedElasticsearchInstanceOfferingResponseTypeDef = TypedDict(
    "_ClientPurchaseReservedElasticsearchInstanceOfferingResponseTypeDef",
    {"ReservedElasticsearchInstanceId": str, "ReservationName": str},
    total=False,
)


class ClientPurchaseReservedElasticsearchInstanceOfferingResponseTypeDef(
    _ClientPurchaseReservedElasticsearchInstanceOfferingResponseTypeDef
):
    """
    Type definition for `ClientPurchaseReservedElasticsearchInstanceOffering` `Response`

    Represents the output of a ``PurchaseReservedElasticsearchInstanceOffering`` operation.

    - **ReservedElasticsearchInstanceId** *(string) --*

      Details of the reserved Elasticsearch instance which was purchased.

    - **ReservationName** *(string) --*

      The customer-specified identifier used to track this reservation.
    """


_ClientStartElasticsearchServiceSoftwareUpdateResponseServiceSoftwareOptionsTypeDef = TypedDict(
    "_ClientStartElasticsearchServiceSoftwareUpdateResponseServiceSoftwareOptionsTypeDef",
    {
        "CurrentVersion": str,
        "NewVersion": str,
        "UpdateAvailable": bool,
        "Cancellable": bool,
        "UpdateStatus": str,
        "Description": str,
        "AutomatedUpdateDate": datetime,
    },
    total=False,
)


class ClientStartElasticsearchServiceSoftwareUpdateResponseServiceSoftwareOptionsTypeDef(
    _ClientStartElasticsearchServiceSoftwareUpdateResponseServiceSoftwareOptionsTypeDef
):
    """
    Type definition for `ClientStartElasticsearchServiceSoftwareUpdateResponse` `ServiceSoftwareOptions`

    The current status of the Elasticsearch service software update.

    - **CurrentVersion** *(string) --*

      The current service software version that is present on the domain.

    - **NewVersion** *(string) --*

      The new service software version if one is available.

    - **UpdateAvailable** *(boolean) --*

      ``True`` if you are able to update you service software version. ``False`` if you are not
      able to update your service software version.

    - **Cancellable** *(boolean) --*

      ``True`` if you are able to cancel your service software version update. ``False`` if you
      are not able to cancel your service software version.

    - **UpdateStatus** *(string) --*

      The status of your service software update. This field can take the following values:
      ``ELIGIBLE`` , ``PENDING_UPDATE`` , ``IN_PROGRESS`` , ``COMPLETED`` , and ``NOT_ELIGIBLE`` .

    - **Description** *(string) --*

      The description of the ``UpdateStatus`` .

    - **AutomatedUpdateDate** *(datetime) --*

      Timestamp, in Epoch time, until which you can manually request a service software update.
      After this date, we automatically update your service software.
    """


_ClientStartElasticsearchServiceSoftwareUpdateResponseTypeDef = TypedDict(
    "_ClientStartElasticsearchServiceSoftwareUpdateResponseTypeDef",
    {
        "ServiceSoftwareOptions": ClientStartElasticsearchServiceSoftwareUpdateResponseServiceSoftwareOptionsTypeDef
    },
    total=False,
)


class ClientStartElasticsearchServiceSoftwareUpdateResponseTypeDef(
    _ClientStartElasticsearchServiceSoftwareUpdateResponseTypeDef
):
    """
    Type definition for `ClientStartElasticsearchServiceSoftwareUpdate` `Response`

    The result of a ``StartElasticsearchServiceSoftwareUpdate`` operation. Contains the status of
    the update.

    - **ServiceSoftwareOptions** *(dict) --*

      The current status of the Elasticsearch service software update.

      - **CurrentVersion** *(string) --*

        The current service software version that is present on the domain.

      - **NewVersion** *(string) --*

        The new service software version if one is available.

      - **UpdateAvailable** *(boolean) --*

        ``True`` if you are able to update you service software version. ``False`` if you are not
        able to update your service software version.

      - **Cancellable** *(boolean) --*

        ``True`` if you are able to cancel your service software version update. ``False`` if you
        are not able to cancel your service software version.

      - **UpdateStatus** *(string) --*

        The status of your service software update. This field can take the following values:
        ``ELIGIBLE`` , ``PENDING_UPDATE`` , ``IN_PROGRESS`` , ``COMPLETED`` , and ``NOT_ELIGIBLE`` .

      - **Description** *(string) --*

        The description of the ``UpdateStatus`` .

      - **AutomatedUpdateDate** *(datetime) --*

        Timestamp, in Epoch time, until which you can manually request a service software update.
        After this date, we automatically update your service software.
    """


_ClientUpdateElasticsearchDomainConfigCognitoOptionsTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigCognitoOptionsTypeDef",
    {"Enabled": bool, "UserPoolId": str, "IdentityPoolId": str, "RoleArn": str},
    total=False,
)


class ClientUpdateElasticsearchDomainConfigCognitoOptionsTypeDef(
    _ClientUpdateElasticsearchDomainConfigCognitoOptionsTypeDef
):
    """
    Type definition for `ClientUpdateElasticsearchDomainConfig` `CognitoOptions`

    Options to specify the Cognito user and identity pools for Kibana authentication. For more
    information, see `Amazon Cognito Authentication for Kibana
    <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-cognito-auth.html>`__ .

    - **Enabled** *(boolean) --*

      Specifies the option to enable Cognito for Kibana authentication.

    - **UserPoolId** *(string) --*

      Specifies the Cognito user pool ID for Kibana authentication.

    - **IdentityPoolId** *(string) --*

      Specifies the Cognito identity pool ID for Kibana authentication.

    - **RoleArn** *(string) --*

      Specifies the role ARN that provides Elasticsearch permissions for accessing Cognito resources.
    """


_ClientUpdateElasticsearchDomainConfigDomainEndpointOptionsTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigDomainEndpointOptionsTypeDef",
    {"EnforceHTTPS": bool, "TLSSecurityPolicy": str},
    total=False,
)


class ClientUpdateElasticsearchDomainConfigDomainEndpointOptionsTypeDef(
    _ClientUpdateElasticsearchDomainConfigDomainEndpointOptionsTypeDef
):
    """
    Type definition for `ClientUpdateElasticsearchDomainConfig` `DomainEndpointOptions`

    Options to specify configuration that will be applied to the domain endpoint.

    - **EnforceHTTPS** *(boolean) --*

      Specify if only HTTPS endpoint should be enabled for the Elasticsearch domain.

    - **TLSSecurityPolicy** *(string) --*

      Specify the TLS security policy that needs to be applied to the HTTPS endpoint of Elasticsearch
      domain. It can be one of the following values:

      * **Policy-Min-TLS-1-0-2019-07:** TLS security policy which supports TLSv1.0 and higher.

      * **Policy-Min-TLS-1-2-2019-07:** TLS security policy which supports only TLSv1.2
    """


_ClientUpdateElasticsearchDomainConfigEBSOptionsTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigEBSOptionsTypeDef",
    {"EBSEnabled": bool, "VolumeType": str, "VolumeSize": int, "Iops": int},
    total=False,
)


class ClientUpdateElasticsearchDomainConfigEBSOptionsTypeDef(
    _ClientUpdateElasticsearchDomainConfigEBSOptionsTypeDef
):
    """
    Type definition for `ClientUpdateElasticsearchDomainConfig` `EBSOptions`

    Specify the type and size of the EBS volume that you want to use.

    - **EBSEnabled** *(boolean) --*

      Specifies whether EBS-based storage is enabled.

    - **VolumeType** *(string) --*

      Specifies the volume type for EBS-based storage.

    - **VolumeSize** *(integer) --*

      Integer to specify the size of an EBS volume.

    - **Iops** *(integer) --*

      Specifies the IOPD for a Provisioned IOPS EBS volume (SSD).
    """


_ClientUpdateElasticsearchDomainConfigElasticsearchClusterConfigZoneAwarenessConfigTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigElasticsearchClusterConfigZoneAwarenessConfigTypeDef",
    {"AvailabilityZoneCount": int},
    total=False,
)


class ClientUpdateElasticsearchDomainConfigElasticsearchClusterConfigZoneAwarenessConfigTypeDef(
    _ClientUpdateElasticsearchDomainConfigElasticsearchClusterConfigZoneAwarenessConfigTypeDef
):
    """
    Type definition for `ClientUpdateElasticsearchDomainConfigElasticsearchClusterConfig` `ZoneAwarenessConfig`

    Specifies the zone awareness configuration for a domain when zone awareness is enabled.

    - **AvailabilityZoneCount** *(integer) --*

      An integer value to indicate the number of availability zones for a domain when zone
      awareness is enabled. This should be equal to number of subnets if VPC endpoints is enabled
    """


_ClientUpdateElasticsearchDomainConfigElasticsearchClusterConfigTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigElasticsearchClusterConfigTypeDef",
    {
        "InstanceType": str,
        "InstanceCount": int,
        "DedicatedMasterEnabled": bool,
        "ZoneAwarenessEnabled": bool,
        "ZoneAwarenessConfig": ClientUpdateElasticsearchDomainConfigElasticsearchClusterConfigZoneAwarenessConfigTypeDef,
        "DedicatedMasterType": str,
        "DedicatedMasterCount": int,
    },
    total=False,
)


class ClientUpdateElasticsearchDomainConfigElasticsearchClusterConfigTypeDef(
    _ClientUpdateElasticsearchDomainConfigElasticsearchClusterConfigTypeDef
):
    """
    Type definition for `ClientUpdateElasticsearchDomainConfig` `ElasticsearchClusterConfig`

    The type and number of instances to instantiate for the domain cluster.

    - **InstanceType** *(string) --*

      The instance type for an Elasticsearch cluster.

    - **InstanceCount** *(integer) --*

      The number of instances in the specified domain cluster.

    - **DedicatedMasterEnabled** *(boolean) --*

      A boolean value to indicate whether a dedicated master node is enabled. See `About Dedicated
      Master Nodes
      <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains.html#es-managedomains-dedicatedmasternodes>`__
      for more information.

    - **ZoneAwarenessEnabled** *(boolean) --*

      A boolean value to indicate whether zone awareness is enabled. See `About Zone Awareness
      <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains.html#es-managedomains-zoneawareness>`__
      for more information.

    - **ZoneAwarenessConfig** *(dict) --*

      Specifies the zone awareness configuration for a domain when zone awareness is enabled.

      - **AvailabilityZoneCount** *(integer) --*

        An integer value to indicate the number of availability zones for a domain when zone
        awareness is enabled. This should be equal to number of subnets if VPC endpoints is enabled

    - **DedicatedMasterType** *(string) --*

      The instance type for a dedicated master node.

    - **DedicatedMasterCount** *(integer) --*

      Total number of dedicated master nodes, active and on standby, for the cluster.
    """


_ClientUpdateElasticsearchDomainConfigLogPublishingOptionsTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigLogPublishingOptionsTypeDef",
    {"CloudWatchLogsLogGroupArn": str, "Enabled": bool},
    total=False,
)


class ClientUpdateElasticsearchDomainConfigLogPublishingOptionsTypeDef(
    _ClientUpdateElasticsearchDomainConfigLogPublishingOptionsTypeDef
):
    """
    Type definition for `ClientUpdateElasticsearchDomainConfig` `LogPublishingOptions`

    Log Publishing option that is set for given domain. Attributes and their details:

    * CloudWatchLogsLogGroupArn: ARN of the Cloudwatch log group to which log needs to be
    published.

    * Enabled: Whether the log publishing for given log type is enabled or not

    - **CloudWatchLogsLogGroupArn** *(string) --*

      ARN of the Cloudwatch log group to which log needs to be published.

    - **Enabled** *(boolean) --*

      Specifies whether given log publishing option is enabled or not.
    """


_ClientUpdateElasticsearchDomainConfigResponseDomainConfigAccessPoliciesStatusTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigResponseDomainConfigAccessPoliciesStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": str,
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientUpdateElasticsearchDomainConfigResponseDomainConfigAccessPoliciesStatusTypeDef(
    _ClientUpdateElasticsearchDomainConfigResponseDomainConfigAccessPoliciesStatusTypeDef
):
    """
    Type definition for `ClientUpdateElasticsearchDomainConfigResponseDomainConfigAccessPolicies` `Status`

    The status of the access policy for the Elasticsearch domain. See ``OptionStatus`` for
    the status information that's included.

    - **CreationDate** *(datetime) --*

      Timestamp which tells the creation date for the entity.

    - **UpdateDate** *(datetime) --*

      Timestamp which tells the last updated time for the entity.

    - **UpdateVersion** *(integer) --*

      Specifies the latest version for the entity.

    - **State** *(string) --*

      Provides the ``OptionState`` for the Elasticsearch domain.

    - **PendingDeletion** *(boolean) --*

      Indicates whether the Elasticsearch domain is being deleted.
    """


_ClientUpdateElasticsearchDomainConfigResponseDomainConfigAccessPoliciesTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigResponseDomainConfigAccessPoliciesTypeDef",
    {
        "Options": str,
        "Status": ClientUpdateElasticsearchDomainConfigResponseDomainConfigAccessPoliciesStatusTypeDef,
    },
    total=False,
)


class ClientUpdateElasticsearchDomainConfigResponseDomainConfigAccessPoliciesTypeDef(
    _ClientUpdateElasticsearchDomainConfigResponseDomainConfigAccessPoliciesTypeDef
):
    """
    Type definition for `ClientUpdateElasticsearchDomainConfigResponseDomainConfig` `AccessPolicies`

    IAM access policy as a JSON-formatted string.

    - **Options** *(string) --*

      The access policy configured for the Elasticsearch domain. Access policies may be
      resource-based, IP-based, or IAM-based. See `Configuring Access Policies
      <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html#es-createdomain-configure-access-policies>`__
      for more information.

    - **Status** *(dict) --*

      The status of the access policy for the Elasticsearch domain. See ``OptionStatus`` for
      the status information that's included.

      - **CreationDate** *(datetime) --*

        Timestamp which tells the creation date for the entity.

      - **UpdateDate** *(datetime) --*

        Timestamp which tells the last updated time for the entity.

      - **UpdateVersion** *(integer) --*

        Specifies the latest version for the entity.

      - **State** *(string) --*

        Provides the ``OptionState`` for the Elasticsearch domain.

      - **PendingDeletion** *(boolean) --*

        Indicates whether the Elasticsearch domain is being deleted.
    """


_ClientUpdateElasticsearchDomainConfigResponseDomainConfigAdvancedOptionsStatusTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigResponseDomainConfigAdvancedOptionsStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": str,
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientUpdateElasticsearchDomainConfigResponseDomainConfigAdvancedOptionsStatusTypeDef(
    _ClientUpdateElasticsearchDomainConfigResponseDomainConfigAdvancedOptionsStatusTypeDef
):
    """
    Type definition for `ClientUpdateElasticsearchDomainConfigResponseDomainConfigAdvancedOptions` `Status`

    Specifies the status of ``OptionStatus`` for advanced options for the specified
    Elasticsearch domain.

    - **CreationDate** *(datetime) --*

      Timestamp which tells the creation date for the entity.

    - **UpdateDate** *(datetime) --*

      Timestamp which tells the last updated time for the entity.

    - **UpdateVersion** *(integer) --*

      Specifies the latest version for the entity.

    - **State** *(string) --*

      Provides the ``OptionState`` for the Elasticsearch domain.

    - **PendingDeletion** *(boolean) --*

      Indicates whether the Elasticsearch domain is being deleted.
    """


_ClientUpdateElasticsearchDomainConfigResponseDomainConfigAdvancedOptionsTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigResponseDomainConfigAdvancedOptionsTypeDef",
    {
        "Options": Dict[str, str],
        "Status": ClientUpdateElasticsearchDomainConfigResponseDomainConfigAdvancedOptionsStatusTypeDef,
    },
    total=False,
)


class ClientUpdateElasticsearchDomainConfigResponseDomainConfigAdvancedOptionsTypeDef(
    _ClientUpdateElasticsearchDomainConfigResponseDomainConfigAdvancedOptionsTypeDef
):
    """
    Type definition for `ClientUpdateElasticsearchDomainConfigResponseDomainConfig` `AdvancedOptions`

    Specifies the ``AdvancedOptions`` for the domain. See `Configuring Advanced Options
    <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html#es-createdomain-configure-advanced-options>`__
    for more information.

    - **Options** *(dict) --*

      Specifies the status of advanced options for the specified Elasticsearch domain.

      - *(string) --*

        - *(string) --*

    - **Status** *(dict) --*

      Specifies the status of ``OptionStatus`` for advanced options for the specified
      Elasticsearch domain.

      - **CreationDate** *(datetime) --*

        Timestamp which tells the creation date for the entity.

      - **UpdateDate** *(datetime) --*

        Timestamp which tells the last updated time for the entity.

      - **UpdateVersion** *(integer) --*

        Specifies the latest version for the entity.

      - **State** *(string) --*

        Provides the ``OptionState`` for the Elasticsearch domain.

      - **PendingDeletion** *(boolean) --*

        Indicates whether the Elasticsearch domain is being deleted.
    """


_ClientUpdateElasticsearchDomainConfigResponseDomainConfigCognitoOptionsOptionsTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigResponseDomainConfigCognitoOptionsOptionsTypeDef",
    {"Enabled": bool, "UserPoolId": str, "IdentityPoolId": str, "RoleArn": str},
    total=False,
)


class ClientUpdateElasticsearchDomainConfigResponseDomainConfigCognitoOptionsOptionsTypeDef(
    _ClientUpdateElasticsearchDomainConfigResponseDomainConfigCognitoOptionsOptionsTypeDef
):
    """
    Type definition for `ClientUpdateElasticsearchDomainConfigResponseDomainConfigCognitoOptions` `Options`

    Specifies the Cognito options for the specified Elasticsearch domain.

    - **Enabled** *(boolean) --*

      Specifies the option to enable Cognito for Kibana authentication.

    - **UserPoolId** *(string) --*

      Specifies the Cognito user pool ID for Kibana authentication.

    - **IdentityPoolId** *(string) --*

      Specifies the Cognito identity pool ID for Kibana authentication.

    - **RoleArn** *(string) --*

      Specifies the role ARN that provides Elasticsearch permissions for accessing Cognito
      resources.
    """


_ClientUpdateElasticsearchDomainConfigResponseDomainConfigCognitoOptionsStatusTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigResponseDomainConfigCognitoOptionsStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": str,
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientUpdateElasticsearchDomainConfigResponseDomainConfigCognitoOptionsStatusTypeDef(
    _ClientUpdateElasticsearchDomainConfigResponseDomainConfigCognitoOptionsStatusTypeDef
):
    """
    Type definition for `ClientUpdateElasticsearchDomainConfigResponseDomainConfigCognitoOptions` `Status`

    Specifies the status of the Cognito options for the specified Elasticsearch domain.

    - **CreationDate** *(datetime) --*

      Timestamp which tells the creation date for the entity.

    - **UpdateDate** *(datetime) --*

      Timestamp which tells the last updated time for the entity.

    - **UpdateVersion** *(integer) --*

      Specifies the latest version for the entity.

    - **State** *(string) --*

      Provides the ``OptionState`` for the Elasticsearch domain.

    - **PendingDeletion** *(boolean) --*

      Indicates whether the Elasticsearch domain is being deleted.
    """


_ClientUpdateElasticsearchDomainConfigResponseDomainConfigCognitoOptionsTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigResponseDomainConfigCognitoOptionsTypeDef",
    {
        "Options": ClientUpdateElasticsearchDomainConfigResponseDomainConfigCognitoOptionsOptionsTypeDef,
        "Status": ClientUpdateElasticsearchDomainConfigResponseDomainConfigCognitoOptionsStatusTypeDef,
    },
    total=False,
)


class ClientUpdateElasticsearchDomainConfigResponseDomainConfigCognitoOptionsTypeDef(
    _ClientUpdateElasticsearchDomainConfigResponseDomainConfigCognitoOptionsTypeDef
):
    """
    Type definition for `ClientUpdateElasticsearchDomainConfigResponseDomainConfig` `CognitoOptions`

    The ``CognitoOptions`` for the specified domain. For more information, see `Amazon Cognito
    Authentication for Kibana
    <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-cognito-auth.html>`__
    .

    - **Options** *(dict) --*

      Specifies the Cognito options for the specified Elasticsearch domain.

      - **Enabled** *(boolean) --*

        Specifies the option to enable Cognito for Kibana authentication.

      - **UserPoolId** *(string) --*

        Specifies the Cognito user pool ID for Kibana authentication.

      - **IdentityPoolId** *(string) --*

        Specifies the Cognito identity pool ID for Kibana authentication.

      - **RoleArn** *(string) --*

        Specifies the role ARN that provides Elasticsearch permissions for accessing Cognito
        resources.

    - **Status** *(dict) --*

      Specifies the status of the Cognito options for the specified Elasticsearch domain.

      - **CreationDate** *(datetime) --*

        Timestamp which tells the creation date for the entity.

      - **UpdateDate** *(datetime) --*

        Timestamp which tells the last updated time for the entity.

      - **UpdateVersion** *(integer) --*

        Specifies the latest version for the entity.

      - **State** *(string) --*

        Provides the ``OptionState`` for the Elasticsearch domain.

      - **PendingDeletion** *(boolean) --*

        Indicates whether the Elasticsearch domain is being deleted.
    """


_ClientUpdateElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsOptionsTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsOptionsTypeDef",
    {"EnforceHTTPS": bool, "TLSSecurityPolicy": str},
    total=False,
)


class ClientUpdateElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsOptionsTypeDef(
    _ClientUpdateElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsOptionsTypeDef
):
    """
    Type definition for `ClientUpdateElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptions` `Options`

    Options to configure endpoint for the Elasticsearch domain.

    - **EnforceHTTPS** *(boolean) --*

      Specify if only HTTPS endpoint should be enabled for the Elasticsearch domain.

    - **TLSSecurityPolicy** *(string) --*

      Specify the TLS security policy that needs to be applied to the HTTPS endpoint of
      Elasticsearch domain. It can be one of the following values:

      * **Policy-Min-TLS-1-0-2019-07:** TLS security policy which supports TLSv1.0 and higher.

      * **Policy-Min-TLS-1-2-2019-07:** TLS security policy which supports only TLSv1.2
    """


_ClientUpdateElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsStatusTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": str,
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientUpdateElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsStatusTypeDef(
    _ClientUpdateElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsStatusTypeDef
):
    """
    Type definition for `ClientUpdateElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptions` `Status`

    The status of the endpoint options for the Elasticsearch domain. See ``OptionStatus`` for
    the status information that's included.

    - **CreationDate** *(datetime) --*

      Timestamp which tells the creation date for the entity.

    - **UpdateDate** *(datetime) --*

      Timestamp which tells the last updated time for the entity.

    - **UpdateVersion** *(integer) --*

      Specifies the latest version for the entity.

    - **State** *(string) --*

      Provides the ``OptionState`` for the Elasticsearch domain.

    - **PendingDeletion** *(boolean) --*

      Indicates whether the Elasticsearch domain is being deleted.
    """


_ClientUpdateElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsTypeDef",
    {
        "Options": ClientUpdateElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsOptionsTypeDef,
        "Status": ClientUpdateElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsStatusTypeDef,
    },
    total=False,
)


class ClientUpdateElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsTypeDef(
    _ClientUpdateElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsTypeDef
):
    """
    Type definition for `ClientUpdateElasticsearchDomainConfigResponseDomainConfig` `DomainEndpointOptions`

    Specifies the ``DomainEndpointOptions`` for the Elasticsearch domain.

    - **Options** *(dict) --*

      Options to configure endpoint for the Elasticsearch domain.

      - **EnforceHTTPS** *(boolean) --*

        Specify if only HTTPS endpoint should be enabled for the Elasticsearch domain.

      - **TLSSecurityPolicy** *(string) --*

        Specify the TLS security policy that needs to be applied to the HTTPS endpoint of
        Elasticsearch domain. It can be one of the following values:

        * **Policy-Min-TLS-1-0-2019-07:** TLS security policy which supports TLSv1.0 and higher.

        * **Policy-Min-TLS-1-2-2019-07:** TLS security policy which supports only TLSv1.2

    - **Status** *(dict) --*

      The status of the endpoint options for the Elasticsearch domain. See ``OptionStatus`` for
      the status information that's included.

      - **CreationDate** *(datetime) --*

        Timestamp which tells the creation date for the entity.

      - **UpdateDate** *(datetime) --*

        Timestamp which tells the last updated time for the entity.

      - **UpdateVersion** *(integer) --*

        Specifies the latest version for the entity.

      - **State** *(string) --*

        Provides the ``OptionState`` for the Elasticsearch domain.

      - **PendingDeletion** *(boolean) --*

        Indicates whether the Elasticsearch domain is being deleted.
    """


_ClientUpdateElasticsearchDomainConfigResponseDomainConfigEBSOptionsOptionsTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigResponseDomainConfigEBSOptionsOptionsTypeDef",
    {"EBSEnabled": bool, "VolumeType": str, "VolumeSize": int, "Iops": int},
    total=False,
)


class ClientUpdateElasticsearchDomainConfigResponseDomainConfigEBSOptionsOptionsTypeDef(
    _ClientUpdateElasticsearchDomainConfigResponseDomainConfigEBSOptionsOptionsTypeDef
):
    """
    Type definition for `ClientUpdateElasticsearchDomainConfigResponseDomainConfigEBSOptions` `Options`

    Specifies the EBS options for the specified Elasticsearch domain.

    - **EBSEnabled** *(boolean) --*

      Specifies whether EBS-based storage is enabled.

    - **VolumeType** *(string) --*

      Specifies the volume type for EBS-based storage.

    - **VolumeSize** *(integer) --*

      Integer to specify the size of an EBS volume.

    - **Iops** *(integer) --*

      Specifies the IOPD for a Provisioned IOPS EBS volume (SSD).
    """


_ClientUpdateElasticsearchDomainConfigResponseDomainConfigEBSOptionsStatusTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigResponseDomainConfigEBSOptionsStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": str,
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientUpdateElasticsearchDomainConfigResponseDomainConfigEBSOptionsStatusTypeDef(
    _ClientUpdateElasticsearchDomainConfigResponseDomainConfigEBSOptionsStatusTypeDef
):
    """
    Type definition for `ClientUpdateElasticsearchDomainConfigResponseDomainConfigEBSOptions` `Status`

    Specifies the status of the EBS options for the specified Elasticsearch domain.

    - **CreationDate** *(datetime) --*

      Timestamp which tells the creation date for the entity.

    - **UpdateDate** *(datetime) --*

      Timestamp which tells the last updated time for the entity.

    - **UpdateVersion** *(integer) --*

      Specifies the latest version for the entity.

    - **State** *(string) --*

      Provides the ``OptionState`` for the Elasticsearch domain.

    - **PendingDeletion** *(boolean) --*

      Indicates whether the Elasticsearch domain is being deleted.
    """


_ClientUpdateElasticsearchDomainConfigResponseDomainConfigEBSOptionsTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigResponseDomainConfigEBSOptionsTypeDef",
    {
        "Options": ClientUpdateElasticsearchDomainConfigResponseDomainConfigEBSOptionsOptionsTypeDef,
        "Status": ClientUpdateElasticsearchDomainConfigResponseDomainConfigEBSOptionsStatusTypeDef,
    },
    total=False,
)


class ClientUpdateElasticsearchDomainConfigResponseDomainConfigEBSOptionsTypeDef(
    _ClientUpdateElasticsearchDomainConfigResponseDomainConfigEBSOptionsTypeDef
):
    """
    Type definition for `ClientUpdateElasticsearchDomainConfigResponseDomainConfig` `EBSOptions`

    Specifies the ``EBSOptions`` for the Elasticsearch domain.

    - **Options** *(dict) --*

      Specifies the EBS options for the specified Elasticsearch domain.

      - **EBSEnabled** *(boolean) --*

        Specifies whether EBS-based storage is enabled.

      - **VolumeType** *(string) --*

        Specifies the volume type for EBS-based storage.

      - **VolumeSize** *(integer) --*

        Integer to specify the size of an EBS volume.

      - **Iops** *(integer) --*

        Specifies the IOPD for a Provisioned IOPS EBS volume (SSD).

    - **Status** *(dict) --*

      Specifies the status of the EBS options for the specified Elasticsearch domain.

      - **CreationDate** *(datetime) --*

        Timestamp which tells the creation date for the entity.

      - **UpdateDate** *(datetime) --*

        Timestamp which tells the last updated time for the entity.

      - **UpdateVersion** *(integer) --*

        Specifies the latest version for the entity.

      - **State** *(string) --*

        Provides the ``OptionState`` for the Elasticsearch domain.

      - **PendingDeletion** *(boolean) --*

        Indicates whether the Elasticsearch domain is being deleted.
    """


_ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigOptionsZoneAwarenessConfigTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigOptionsZoneAwarenessConfigTypeDef",
    {"AvailabilityZoneCount": int},
    total=False,
)


class ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigOptionsZoneAwarenessConfigTypeDef(
    _ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigOptionsZoneAwarenessConfigTypeDef
):
    """
    Type definition for `ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigOptions` `ZoneAwarenessConfig`

    Specifies the zone awareness configuration for a domain when zone awareness is enabled.

    - **AvailabilityZoneCount** *(integer) --*

      An integer value to indicate the number of availability zones for a domain when zone
      awareness is enabled. This should be equal to number of subnets if VPC endpoints is
      enabled
    """


_ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigOptionsTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigOptionsTypeDef",
    {
        "InstanceType": str,
        "InstanceCount": int,
        "DedicatedMasterEnabled": bool,
        "ZoneAwarenessEnabled": bool,
        "ZoneAwarenessConfig": ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigOptionsZoneAwarenessConfigTypeDef,
        "DedicatedMasterType": str,
        "DedicatedMasterCount": int,
    },
    total=False,
)


class ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigOptionsTypeDef(
    _ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigOptionsTypeDef
):
    """
    Type definition for `ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfig` `Options`

    Specifies the cluster configuration for the specified Elasticsearch domain.

    - **InstanceType** *(string) --*

      The instance type for an Elasticsearch cluster.

    - **InstanceCount** *(integer) --*

      The number of instances in the specified domain cluster.

    - **DedicatedMasterEnabled** *(boolean) --*

      A boolean value to indicate whether a dedicated master node is enabled. See `About
      Dedicated Master Nodes
      <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains.html#es-managedomains-dedicatedmasternodes>`__
      for more information.

    - **ZoneAwarenessEnabled** *(boolean) --*

      A boolean value to indicate whether zone awareness is enabled. See `About Zone
      Awareness
      <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains.html#es-managedomains-zoneawareness>`__
      for more information.

    - **ZoneAwarenessConfig** *(dict) --*

      Specifies the zone awareness configuration for a domain when zone awareness is enabled.

      - **AvailabilityZoneCount** *(integer) --*

        An integer value to indicate the number of availability zones for a domain when zone
        awareness is enabled. This should be equal to number of subnets if VPC endpoints is
        enabled

    - **DedicatedMasterType** *(string) --*

      The instance type for a dedicated master node.

    - **DedicatedMasterCount** *(integer) --*

      Total number of dedicated master nodes, active and on standby, for the cluster.
    """


_ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigStatusTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": str,
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigStatusTypeDef(
    _ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigStatusTypeDef
):
    """
    Type definition for `ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfig` `Status`

    Specifies the status of the configuration for the specified Elasticsearch domain.

    - **CreationDate** *(datetime) --*

      Timestamp which tells the creation date for the entity.

    - **UpdateDate** *(datetime) --*

      Timestamp which tells the last updated time for the entity.

    - **UpdateVersion** *(integer) --*

      Specifies the latest version for the entity.

    - **State** *(string) --*

      Provides the ``OptionState`` for the Elasticsearch domain.

    - **PendingDeletion** *(boolean) --*

      Indicates whether the Elasticsearch domain is being deleted.
    """


_ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigTypeDef",
    {
        "Options": ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigOptionsTypeDef,
        "Status": ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigStatusTypeDef,
    },
    total=False,
)


class ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigTypeDef(
    _ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigTypeDef
):
    """
    Type definition for `ClientUpdateElasticsearchDomainConfigResponseDomainConfig` `ElasticsearchClusterConfig`

    Specifies the ``ElasticsearchClusterConfig`` for the Elasticsearch domain.

    - **Options** *(dict) --*

      Specifies the cluster configuration for the specified Elasticsearch domain.

      - **InstanceType** *(string) --*

        The instance type for an Elasticsearch cluster.

      - **InstanceCount** *(integer) --*

        The number of instances in the specified domain cluster.

      - **DedicatedMasterEnabled** *(boolean) --*

        A boolean value to indicate whether a dedicated master node is enabled. See `About
        Dedicated Master Nodes
        <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains.html#es-managedomains-dedicatedmasternodes>`__
        for more information.

      - **ZoneAwarenessEnabled** *(boolean) --*

        A boolean value to indicate whether zone awareness is enabled. See `About Zone
        Awareness
        <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains.html#es-managedomains-zoneawareness>`__
        for more information.

      - **ZoneAwarenessConfig** *(dict) --*

        Specifies the zone awareness configuration for a domain when zone awareness is enabled.

        - **AvailabilityZoneCount** *(integer) --*

          An integer value to indicate the number of availability zones for a domain when zone
          awareness is enabled. This should be equal to number of subnets if VPC endpoints is
          enabled

      - **DedicatedMasterType** *(string) --*

        The instance type for a dedicated master node.

      - **DedicatedMasterCount** *(integer) --*

        Total number of dedicated master nodes, active and on standby, for the cluster.

    - **Status** *(dict) --*

      Specifies the status of the configuration for the specified Elasticsearch domain.

      - **CreationDate** *(datetime) --*

        Timestamp which tells the creation date for the entity.

      - **UpdateDate** *(datetime) --*

        Timestamp which tells the last updated time for the entity.

      - **UpdateVersion** *(integer) --*

        Specifies the latest version for the entity.

      - **State** *(string) --*

        Provides the ``OptionState`` for the Elasticsearch domain.

      - **PendingDeletion** *(boolean) --*

        Indicates whether the Elasticsearch domain is being deleted.
    """


_ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchVersionStatusTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchVersionStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": str,
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchVersionStatusTypeDef(
    _ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchVersionStatusTypeDef
):
    """
    Type definition for `ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchVersion` `Status`

    Specifies the status of the Elasticsearch version options for the specified Elasticsearch
    domain.

    - **CreationDate** *(datetime) --*

      Timestamp which tells the creation date for the entity.

    - **UpdateDate** *(datetime) --*

      Timestamp which tells the last updated time for the entity.

    - **UpdateVersion** *(integer) --*

      Specifies the latest version for the entity.

    - **State** *(string) --*

      Provides the ``OptionState`` for the Elasticsearch domain.

    - **PendingDeletion** *(boolean) --*

      Indicates whether the Elasticsearch domain is being deleted.
    """


_ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchVersionTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchVersionTypeDef",
    {
        "Options": str,
        "Status": ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchVersionStatusTypeDef,
    },
    total=False,
)


class ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchVersionTypeDef(
    _ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchVersionTypeDef
):
    """
    Type definition for `ClientUpdateElasticsearchDomainConfigResponseDomainConfig` `ElasticsearchVersion`

    String of format X.Y to specify version for the Elasticsearch domain.

    - **Options** *(string) --*

      Specifies the Elasticsearch version for the specified Elasticsearch domain.

    - **Status** *(dict) --*

      Specifies the status of the Elasticsearch version options for the specified Elasticsearch
      domain.

      - **CreationDate** *(datetime) --*

        Timestamp which tells the creation date for the entity.

      - **UpdateDate** *(datetime) --*

        Timestamp which tells the last updated time for the entity.

      - **UpdateVersion** *(integer) --*

        Specifies the latest version for the entity.

      - **State** *(string) --*

        Provides the ``OptionState`` for the Elasticsearch domain.

      - **PendingDeletion** *(boolean) --*

        Indicates whether the Elasticsearch domain is being deleted.
    """


_ClientUpdateElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsOptionsTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsOptionsTypeDef",
    {"Enabled": bool, "KmsKeyId": str},
    total=False,
)


class ClientUpdateElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsOptionsTypeDef(
    _ClientUpdateElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsOptionsTypeDef
):
    """
    Type definition for `ClientUpdateElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptions` `Options`

    Specifies the Encryption At Rest options for the specified Elasticsearch domain.

    - **Enabled** *(boolean) --*

      Specifies the option to enable Encryption At Rest.

    - **KmsKeyId** *(string) --*

      Specifies the KMS Key ID for Encryption At Rest options.
    """


_ClientUpdateElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsStatusTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": str,
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientUpdateElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsStatusTypeDef(
    _ClientUpdateElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsStatusTypeDef
):
    """
    Type definition for `ClientUpdateElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptions` `Status`

    Specifies the status of the Encryption At Rest options for the specified Elasticsearch
    domain.

    - **CreationDate** *(datetime) --*

      Timestamp which tells the creation date for the entity.

    - **UpdateDate** *(datetime) --*

      Timestamp which tells the last updated time for the entity.

    - **UpdateVersion** *(integer) --*

      Specifies the latest version for the entity.

    - **State** *(string) --*

      Provides the ``OptionState`` for the Elasticsearch domain.

    - **PendingDeletion** *(boolean) --*

      Indicates whether the Elasticsearch domain is being deleted.
    """


_ClientUpdateElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsTypeDef",
    {
        "Options": ClientUpdateElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsOptionsTypeDef,
        "Status": ClientUpdateElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsStatusTypeDef,
    },
    total=False,
)


class ClientUpdateElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsTypeDef(
    _ClientUpdateElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsTypeDef
):
    """
    Type definition for `ClientUpdateElasticsearchDomainConfigResponseDomainConfig` `EncryptionAtRestOptions`

    Specifies the ``EncryptionAtRestOptions`` for the Elasticsearch domain.

    - **Options** *(dict) --*

      Specifies the Encryption At Rest options for the specified Elasticsearch domain.

      - **Enabled** *(boolean) --*

        Specifies the option to enable Encryption At Rest.

      - **KmsKeyId** *(string) --*

        Specifies the KMS Key ID for Encryption At Rest options.

    - **Status** *(dict) --*

      Specifies the status of the Encryption At Rest options for the specified Elasticsearch
      domain.

      - **CreationDate** *(datetime) --*

        Timestamp which tells the creation date for the entity.

      - **UpdateDate** *(datetime) --*

        Timestamp which tells the last updated time for the entity.

      - **UpdateVersion** *(integer) --*

        Specifies the latest version for the entity.

      - **State** *(string) --*

        Provides the ``OptionState`` for the Elasticsearch domain.

      - **PendingDeletion** *(boolean) --*

        Indicates whether the Elasticsearch domain is being deleted.
    """


_ClientUpdateElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsOptionsTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsOptionsTypeDef",
    {"CloudWatchLogsLogGroupArn": str, "Enabled": bool},
    total=False,
)


class ClientUpdateElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsOptionsTypeDef(
    _ClientUpdateElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsOptionsTypeDef
):
    """
    Type definition for `ClientUpdateElasticsearchDomainConfigResponseDomainConfigLogPublishingOptions` `Options`

    Log Publishing option that is set for given domain. Attributes and their details:

    * CloudWatchLogsLogGroupArn: ARN of the Cloudwatch log group to which log needs to be
    published.

    * Enabled: Whether the log publishing for given log type is enabled or not

    - **CloudWatchLogsLogGroupArn** *(string) --*

      ARN of the Cloudwatch log group to which log needs to be published.

    - **Enabled** *(boolean) --*

      Specifies whether given log publishing option is enabled or not.
    """


_ClientUpdateElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsStatusTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": str,
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientUpdateElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsStatusTypeDef(
    _ClientUpdateElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsStatusTypeDef
):
    """
    Type definition for `ClientUpdateElasticsearchDomainConfigResponseDomainConfigLogPublishingOptions` `Status`

    The status of the log publishing options for the Elasticsearch domain. See
    ``OptionStatus`` for the status information that's included.

    - **CreationDate** *(datetime) --*

      Timestamp which tells the creation date for the entity.

    - **UpdateDate** *(datetime) --*

      Timestamp which tells the last updated time for the entity.

    - **UpdateVersion** *(integer) --*

      Specifies the latest version for the entity.

    - **State** *(string) --*

      Provides the ``OptionState`` for the Elasticsearch domain.

    - **PendingDeletion** *(boolean) --*

      Indicates whether the Elasticsearch domain is being deleted.
    """


_ClientUpdateElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsTypeDef",
    {
        "Options": Dict[
            str,
            ClientUpdateElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsOptionsTypeDef,
        ],
        "Status": ClientUpdateElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsStatusTypeDef,
    },
    total=False,
)


class ClientUpdateElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsTypeDef(
    _ClientUpdateElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsTypeDef
):
    """
    Type definition for `ClientUpdateElasticsearchDomainConfigResponseDomainConfig` `LogPublishingOptions`

    Log publishing options for the given domain.

    - **Options** *(dict) --*

      The log publishing options configured for the Elasticsearch domain.

      - *(string) --*

        Type of Log File, it can be one of the following:

        * INDEX_SLOW_LOGS: Index slow logs contain insert requests that took more time than
        configured index query log threshold to execute.

        * SEARCH_SLOW_LOGS: Search slow logs contain search queries that took more time than
        configured search query log threshold to execute.

        * ES_APPLICATION_LOGS: Elasticsearch application logs contain information about errors
        and warnings raised during the operation of the service and can be useful for
        troubleshooting.

        - *(dict) --*

          Log Publishing option that is set for given domain. Attributes and their details:

          * CloudWatchLogsLogGroupArn: ARN of the Cloudwatch log group to which log needs to be
          published.

          * Enabled: Whether the log publishing for given log type is enabled or not

          - **CloudWatchLogsLogGroupArn** *(string) --*

            ARN of the Cloudwatch log group to which log needs to be published.

          - **Enabled** *(boolean) --*

            Specifies whether given log publishing option is enabled or not.

    - **Status** *(dict) --*

      The status of the log publishing options for the Elasticsearch domain. See
      ``OptionStatus`` for the status information that's included.

      - **CreationDate** *(datetime) --*

        Timestamp which tells the creation date for the entity.

      - **UpdateDate** *(datetime) --*

        Timestamp which tells the last updated time for the entity.

      - **UpdateVersion** *(integer) --*

        Specifies the latest version for the entity.

      - **State** *(string) --*

        Provides the ``OptionState`` for the Elasticsearch domain.

      - **PendingDeletion** *(boolean) --*

        Indicates whether the Elasticsearch domain is being deleted.
    """


_ClientUpdateElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsOptionsTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsOptionsTypeDef",
    {"Enabled": bool},
    total=False,
)


class ClientUpdateElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsOptionsTypeDef(
    _ClientUpdateElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsOptionsTypeDef
):
    """
    Type definition for `ClientUpdateElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptions` `Options`

    Specifies the node-to-node encryption options for the specified Elasticsearch domain.

    - **Enabled** *(boolean) --*

      Specify true to enable node-to-node encryption.
    """


_ClientUpdateElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsStatusTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": str,
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientUpdateElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsStatusTypeDef(
    _ClientUpdateElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsStatusTypeDef
):
    """
    Type definition for `ClientUpdateElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptions` `Status`

    Specifies the status of the node-to-node encryption options for the specified
    Elasticsearch domain.

    - **CreationDate** *(datetime) --*

      Timestamp which tells the creation date for the entity.

    - **UpdateDate** *(datetime) --*

      Timestamp which tells the last updated time for the entity.

    - **UpdateVersion** *(integer) --*

      Specifies the latest version for the entity.

    - **State** *(string) --*

      Provides the ``OptionState`` for the Elasticsearch domain.

    - **PendingDeletion** *(boolean) --*

      Indicates whether the Elasticsearch domain is being deleted.
    """


_ClientUpdateElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsTypeDef",
    {
        "Options": ClientUpdateElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsOptionsTypeDef,
        "Status": ClientUpdateElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsStatusTypeDef,
    },
    total=False,
)


class ClientUpdateElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsTypeDef(
    _ClientUpdateElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsTypeDef
):
    """
    Type definition for `ClientUpdateElasticsearchDomainConfigResponseDomainConfig` `NodeToNodeEncryptionOptions`

    Specifies the ``NodeToNodeEncryptionOptions`` for the Elasticsearch domain.

    - **Options** *(dict) --*

      Specifies the node-to-node encryption options for the specified Elasticsearch domain.

      - **Enabled** *(boolean) --*

        Specify true to enable node-to-node encryption.

    - **Status** *(dict) --*

      Specifies the status of the node-to-node encryption options for the specified
      Elasticsearch domain.

      - **CreationDate** *(datetime) --*

        Timestamp which tells the creation date for the entity.

      - **UpdateDate** *(datetime) --*

        Timestamp which tells the last updated time for the entity.

      - **UpdateVersion** *(integer) --*

        Specifies the latest version for the entity.

      - **State** *(string) --*

        Provides the ``OptionState`` for the Elasticsearch domain.

      - **PendingDeletion** *(boolean) --*

        Indicates whether the Elasticsearch domain is being deleted.
    """


_ClientUpdateElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsOptionsTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsOptionsTypeDef",
    {"AutomatedSnapshotStartHour": int},
    total=False,
)


class ClientUpdateElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsOptionsTypeDef(
    _ClientUpdateElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsOptionsTypeDef
):
    """
    Type definition for `ClientUpdateElasticsearchDomainConfigResponseDomainConfigSnapshotOptions` `Options`

    Specifies the daily snapshot options specified for the Elasticsearch domain.

    - **AutomatedSnapshotStartHour** *(integer) --*

      Specifies the time, in UTC format, when the service takes a daily automated snapshot of
      the specified Elasticsearch domain. Default value is ``0`` hours.
    """


_ClientUpdateElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsStatusTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": str,
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientUpdateElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsStatusTypeDef(
    _ClientUpdateElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsStatusTypeDef
):
    """
    Type definition for `ClientUpdateElasticsearchDomainConfigResponseDomainConfigSnapshotOptions` `Status`

    Specifies the status of a daily automated snapshot.

    - **CreationDate** *(datetime) --*

      Timestamp which tells the creation date for the entity.

    - **UpdateDate** *(datetime) --*

      Timestamp which tells the last updated time for the entity.

    - **UpdateVersion** *(integer) --*

      Specifies the latest version for the entity.

    - **State** *(string) --*

      Provides the ``OptionState`` for the Elasticsearch domain.

    - **PendingDeletion** *(boolean) --*

      Indicates whether the Elasticsearch domain is being deleted.
    """


_ClientUpdateElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsTypeDef",
    {
        "Options": ClientUpdateElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsOptionsTypeDef,
        "Status": ClientUpdateElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsStatusTypeDef,
    },
    total=False,
)


class ClientUpdateElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsTypeDef(
    _ClientUpdateElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsTypeDef
):
    """
    Type definition for `ClientUpdateElasticsearchDomainConfigResponseDomainConfig` `SnapshotOptions`

    Specifies the ``SnapshotOptions`` for the Elasticsearch domain.

    - **Options** *(dict) --*

      Specifies the daily snapshot options specified for the Elasticsearch domain.

      - **AutomatedSnapshotStartHour** *(integer) --*

        Specifies the time, in UTC format, when the service takes a daily automated snapshot of
        the specified Elasticsearch domain. Default value is ``0`` hours.

    - **Status** *(dict) --*

      Specifies the status of a daily automated snapshot.

      - **CreationDate** *(datetime) --*

        Timestamp which tells the creation date for the entity.

      - **UpdateDate** *(datetime) --*

        Timestamp which tells the last updated time for the entity.

      - **UpdateVersion** *(integer) --*

        Specifies the latest version for the entity.

      - **State** *(string) --*

        Provides the ``OptionState`` for the Elasticsearch domain.

      - **PendingDeletion** *(boolean) --*

        Indicates whether the Elasticsearch domain is being deleted.
    """


_ClientUpdateElasticsearchDomainConfigResponseDomainConfigVPCOptionsOptionsTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigResponseDomainConfigVPCOptionsOptionsTypeDef",
    {
        "VPCId": str,
        "SubnetIds": List[str],
        "AvailabilityZones": List[str],
        "SecurityGroupIds": List[str],
    },
    total=False,
)


class ClientUpdateElasticsearchDomainConfigResponseDomainConfigVPCOptionsOptionsTypeDef(
    _ClientUpdateElasticsearchDomainConfigResponseDomainConfigVPCOptionsOptionsTypeDef
):
    """
    Type definition for `ClientUpdateElasticsearchDomainConfigResponseDomainConfigVPCOptions` `Options`

    Specifies the VPC options for the specified Elasticsearch domain.

    - **VPCId** *(string) --*

      The VPC Id for the Elasticsearch domain. Exists only if the domain was created with
      VPCOptions.

    - **SubnetIds** *(list) --*

      Specifies the subnets for VPC endpoint.

      - *(string) --*

    - **AvailabilityZones** *(list) --*

      The availability zones for the Elasticsearch domain. Exists only if the domain was
      created with VPCOptions.

      - *(string) --*

    - **SecurityGroupIds** *(list) --*

      Specifies the security groups for VPC endpoint.

      - *(string) --*
    """


_ClientUpdateElasticsearchDomainConfigResponseDomainConfigVPCOptionsStatusTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigResponseDomainConfigVPCOptionsStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": str,
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientUpdateElasticsearchDomainConfigResponseDomainConfigVPCOptionsStatusTypeDef(
    _ClientUpdateElasticsearchDomainConfigResponseDomainConfigVPCOptionsStatusTypeDef
):
    """
    Type definition for `ClientUpdateElasticsearchDomainConfigResponseDomainConfigVPCOptions` `Status`

    Specifies the status of the VPC options for the specified Elasticsearch domain.

    - **CreationDate** *(datetime) --*

      Timestamp which tells the creation date for the entity.

    - **UpdateDate** *(datetime) --*

      Timestamp which tells the last updated time for the entity.

    - **UpdateVersion** *(integer) --*

      Specifies the latest version for the entity.

    - **State** *(string) --*

      Provides the ``OptionState`` for the Elasticsearch domain.

    - **PendingDeletion** *(boolean) --*

      Indicates whether the Elasticsearch domain is being deleted.
    """


_ClientUpdateElasticsearchDomainConfigResponseDomainConfigVPCOptionsTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigResponseDomainConfigVPCOptionsTypeDef",
    {
        "Options": ClientUpdateElasticsearchDomainConfigResponseDomainConfigVPCOptionsOptionsTypeDef,
        "Status": ClientUpdateElasticsearchDomainConfigResponseDomainConfigVPCOptionsStatusTypeDef,
    },
    total=False,
)


class ClientUpdateElasticsearchDomainConfigResponseDomainConfigVPCOptionsTypeDef(
    _ClientUpdateElasticsearchDomainConfigResponseDomainConfigVPCOptionsTypeDef
):
    """
    Type definition for `ClientUpdateElasticsearchDomainConfigResponseDomainConfig` `VPCOptions`

    The ``VPCOptions`` for the specified domain. For more information, see `VPC Endpoints for
    Amazon Elasticsearch Service Domains
    <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html>`__ .

    - **Options** *(dict) --*

      Specifies the VPC options for the specified Elasticsearch domain.

      - **VPCId** *(string) --*

        The VPC Id for the Elasticsearch domain. Exists only if the domain was created with
        VPCOptions.

      - **SubnetIds** *(list) --*

        Specifies the subnets for VPC endpoint.

        - *(string) --*

      - **AvailabilityZones** *(list) --*

        The availability zones for the Elasticsearch domain. Exists only if the domain was
        created with VPCOptions.

        - *(string) --*

      - **SecurityGroupIds** *(list) --*

        Specifies the security groups for VPC endpoint.

        - *(string) --*

    - **Status** *(dict) --*

      Specifies the status of the VPC options for the specified Elasticsearch domain.

      - **CreationDate** *(datetime) --*

        Timestamp which tells the creation date for the entity.

      - **UpdateDate** *(datetime) --*

        Timestamp which tells the last updated time for the entity.

      - **UpdateVersion** *(integer) --*

        Specifies the latest version for the entity.

      - **State** *(string) --*

        Provides the ``OptionState`` for the Elasticsearch domain.

      - **PendingDeletion** *(boolean) --*

        Indicates whether the Elasticsearch domain is being deleted.
    """


_ClientUpdateElasticsearchDomainConfigResponseDomainConfigTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigResponseDomainConfigTypeDef",
    {
        "ElasticsearchVersion": ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchVersionTypeDef,
        "ElasticsearchClusterConfig": ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigTypeDef,
        "EBSOptions": ClientUpdateElasticsearchDomainConfigResponseDomainConfigEBSOptionsTypeDef,
        "AccessPolicies": ClientUpdateElasticsearchDomainConfigResponseDomainConfigAccessPoliciesTypeDef,
        "SnapshotOptions": ClientUpdateElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsTypeDef,
        "VPCOptions": ClientUpdateElasticsearchDomainConfigResponseDomainConfigVPCOptionsTypeDef,
        "CognitoOptions": ClientUpdateElasticsearchDomainConfigResponseDomainConfigCognitoOptionsTypeDef,
        "EncryptionAtRestOptions": ClientUpdateElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsTypeDef,
        "NodeToNodeEncryptionOptions": ClientUpdateElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsTypeDef,
        "AdvancedOptions": ClientUpdateElasticsearchDomainConfigResponseDomainConfigAdvancedOptionsTypeDef,
        "LogPublishingOptions": ClientUpdateElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsTypeDef,
        "DomainEndpointOptions": ClientUpdateElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsTypeDef,
    },
    total=False,
)


class ClientUpdateElasticsearchDomainConfigResponseDomainConfigTypeDef(
    _ClientUpdateElasticsearchDomainConfigResponseDomainConfigTypeDef
):
    """
    Type definition for `ClientUpdateElasticsearchDomainConfigResponse` `DomainConfig`

    The status of the updated Elasticsearch domain.

    - **ElasticsearchVersion** *(dict) --*

      String of format X.Y to specify version for the Elasticsearch domain.

      - **Options** *(string) --*

        Specifies the Elasticsearch version for the specified Elasticsearch domain.

      - **Status** *(dict) --*

        Specifies the status of the Elasticsearch version options for the specified Elasticsearch
        domain.

        - **CreationDate** *(datetime) --*

          Timestamp which tells the creation date for the entity.

        - **UpdateDate** *(datetime) --*

          Timestamp which tells the last updated time for the entity.

        - **UpdateVersion** *(integer) --*

          Specifies the latest version for the entity.

        - **State** *(string) --*

          Provides the ``OptionState`` for the Elasticsearch domain.

        - **PendingDeletion** *(boolean) --*

          Indicates whether the Elasticsearch domain is being deleted.

    - **ElasticsearchClusterConfig** *(dict) --*

      Specifies the ``ElasticsearchClusterConfig`` for the Elasticsearch domain.

      - **Options** *(dict) --*

        Specifies the cluster configuration for the specified Elasticsearch domain.

        - **InstanceType** *(string) --*

          The instance type for an Elasticsearch cluster.

        - **InstanceCount** *(integer) --*

          The number of instances in the specified domain cluster.

        - **DedicatedMasterEnabled** *(boolean) --*

          A boolean value to indicate whether a dedicated master node is enabled. See `About
          Dedicated Master Nodes
          <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains.html#es-managedomains-dedicatedmasternodes>`__
          for more information.

        - **ZoneAwarenessEnabled** *(boolean) --*

          A boolean value to indicate whether zone awareness is enabled. See `About Zone
          Awareness
          <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains.html#es-managedomains-zoneawareness>`__
          for more information.

        - **ZoneAwarenessConfig** *(dict) --*

          Specifies the zone awareness configuration for a domain when zone awareness is enabled.

          - **AvailabilityZoneCount** *(integer) --*

            An integer value to indicate the number of availability zones for a domain when zone
            awareness is enabled. This should be equal to number of subnets if VPC endpoints is
            enabled

        - **DedicatedMasterType** *(string) --*

          The instance type for a dedicated master node.

        - **DedicatedMasterCount** *(integer) --*

          Total number of dedicated master nodes, active and on standby, for the cluster.

      - **Status** *(dict) --*

        Specifies the status of the configuration for the specified Elasticsearch domain.

        - **CreationDate** *(datetime) --*

          Timestamp which tells the creation date for the entity.

        - **UpdateDate** *(datetime) --*

          Timestamp which tells the last updated time for the entity.

        - **UpdateVersion** *(integer) --*

          Specifies the latest version for the entity.

        - **State** *(string) --*

          Provides the ``OptionState`` for the Elasticsearch domain.

        - **PendingDeletion** *(boolean) --*

          Indicates whether the Elasticsearch domain is being deleted.

    - **EBSOptions** *(dict) --*

      Specifies the ``EBSOptions`` for the Elasticsearch domain.

      - **Options** *(dict) --*

        Specifies the EBS options for the specified Elasticsearch domain.

        - **EBSEnabled** *(boolean) --*

          Specifies whether EBS-based storage is enabled.

        - **VolumeType** *(string) --*

          Specifies the volume type for EBS-based storage.

        - **VolumeSize** *(integer) --*

          Integer to specify the size of an EBS volume.

        - **Iops** *(integer) --*

          Specifies the IOPD for a Provisioned IOPS EBS volume (SSD).

      - **Status** *(dict) --*

        Specifies the status of the EBS options for the specified Elasticsearch domain.

        - **CreationDate** *(datetime) --*

          Timestamp which tells the creation date for the entity.

        - **UpdateDate** *(datetime) --*

          Timestamp which tells the last updated time for the entity.

        - **UpdateVersion** *(integer) --*

          Specifies the latest version for the entity.

        - **State** *(string) --*

          Provides the ``OptionState`` for the Elasticsearch domain.

        - **PendingDeletion** *(boolean) --*

          Indicates whether the Elasticsearch domain is being deleted.

    - **AccessPolicies** *(dict) --*

      IAM access policy as a JSON-formatted string.

      - **Options** *(string) --*

        The access policy configured for the Elasticsearch domain. Access policies may be
        resource-based, IP-based, or IAM-based. See `Configuring Access Policies
        <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html#es-createdomain-configure-access-policies>`__
        for more information.

      - **Status** *(dict) --*

        The status of the access policy for the Elasticsearch domain. See ``OptionStatus`` for
        the status information that's included.

        - **CreationDate** *(datetime) --*

          Timestamp which tells the creation date for the entity.

        - **UpdateDate** *(datetime) --*

          Timestamp which tells the last updated time for the entity.

        - **UpdateVersion** *(integer) --*

          Specifies the latest version for the entity.

        - **State** *(string) --*

          Provides the ``OptionState`` for the Elasticsearch domain.

        - **PendingDeletion** *(boolean) --*

          Indicates whether the Elasticsearch domain is being deleted.

    - **SnapshotOptions** *(dict) --*

      Specifies the ``SnapshotOptions`` for the Elasticsearch domain.

      - **Options** *(dict) --*

        Specifies the daily snapshot options specified for the Elasticsearch domain.

        - **AutomatedSnapshotStartHour** *(integer) --*

          Specifies the time, in UTC format, when the service takes a daily automated snapshot of
          the specified Elasticsearch domain. Default value is ``0`` hours.

      - **Status** *(dict) --*

        Specifies the status of a daily automated snapshot.

        - **CreationDate** *(datetime) --*

          Timestamp which tells the creation date for the entity.

        - **UpdateDate** *(datetime) --*

          Timestamp which tells the last updated time for the entity.

        - **UpdateVersion** *(integer) --*

          Specifies the latest version for the entity.

        - **State** *(string) --*

          Provides the ``OptionState`` for the Elasticsearch domain.

        - **PendingDeletion** *(boolean) --*

          Indicates whether the Elasticsearch domain is being deleted.

    - **VPCOptions** *(dict) --*

      The ``VPCOptions`` for the specified domain. For more information, see `VPC Endpoints for
      Amazon Elasticsearch Service Domains
      <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html>`__ .

      - **Options** *(dict) --*

        Specifies the VPC options for the specified Elasticsearch domain.

        - **VPCId** *(string) --*

          The VPC Id for the Elasticsearch domain. Exists only if the domain was created with
          VPCOptions.

        - **SubnetIds** *(list) --*

          Specifies the subnets for VPC endpoint.

          - *(string) --*

        - **AvailabilityZones** *(list) --*

          The availability zones for the Elasticsearch domain. Exists only if the domain was
          created with VPCOptions.

          - *(string) --*

        - **SecurityGroupIds** *(list) --*

          Specifies the security groups for VPC endpoint.

          - *(string) --*

      - **Status** *(dict) --*

        Specifies the status of the VPC options for the specified Elasticsearch domain.

        - **CreationDate** *(datetime) --*

          Timestamp which tells the creation date for the entity.

        - **UpdateDate** *(datetime) --*

          Timestamp which tells the last updated time for the entity.

        - **UpdateVersion** *(integer) --*

          Specifies the latest version for the entity.

        - **State** *(string) --*

          Provides the ``OptionState`` for the Elasticsearch domain.

        - **PendingDeletion** *(boolean) --*

          Indicates whether the Elasticsearch domain is being deleted.

    - **CognitoOptions** *(dict) --*

      The ``CognitoOptions`` for the specified domain. For more information, see `Amazon Cognito
      Authentication for Kibana
      <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-cognito-auth.html>`__
      .

      - **Options** *(dict) --*

        Specifies the Cognito options for the specified Elasticsearch domain.

        - **Enabled** *(boolean) --*

          Specifies the option to enable Cognito for Kibana authentication.

        - **UserPoolId** *(string) --*

          Specifies the Cognito user pool ID for Kibana authentication.

        - **IdentityPoolId** *(string) --*

          Specifies the Cognito identity pool ID for Kibana authentication.

        - **RoleArn** *(string) --*

          Specifies the role ARN that provides Elasticsearch permissions for accessing Cognito
          resources.

      - **Status** *(dict) --*

        Specifies the status of the Cognito options for the specified Elasticsearch domain.

        - **CreationDate** *(datetime) --*

          Timestamp which tells the creation date for the entity.

        - **UpdateDate** *(datetime) --*

          Timestamp which tells the last updated time for the entity.

        - **UpdateVersion** *(integer) --*

          Specifies the latest version for the entity.

        - **State** *(string) --*

          Provides the ``OptionState`` for the Elasticsearch domain.

        - **PendingDeletion** *(boolean) --*

          Indicates whether the Elasticsearch domain is being deleted.

    - **EncryptionAtRestOptions** *(dict) --*

      Specifies the ``EncryptionAtRestOptions`` for the Elasticsearch domain.

      - **Options** *(dict) --*

        Specifies the Encryption At Rest options for the specified Elasticsearch domain.

        - **Enabled** *(boolean) --*

          Specifies the option to enable Encryption At Rest.

        - **KmsKeyId** *(string) --*

          Specifies the KMS Key ID for Encryption At Rest options.

      - **Status** *(dict) --*

        Specifies the status of the Encryption At Rest options for the specified Elasticsearch
        domain.

        - **CreationDate** *(datetime) --*

          Timestamp which tells the creation date for the entity.

        - **UpdateDate** *(datetime) --*

          Timestamp which tells the last updated time for the entity.

        - **UpdateVersion** *(integer) --*

          Specifies the latest version for the entity.

        - **State** *(string) --*

          Provides the ``OptionState`` for the Elasticsearch domain.

        - **PendingDeletion** *(boolean) --*

          Indicates whether the Elasticsearch domain is being deleted.

    - **NodeToNodeEncryptionOptions** *(dict) --*

      Specifies the ``NodeToNodeEncryptionOptions`` for the Elasticsearch domain.

      - **Options** *(dict) --*

        Specifies the node-to-node encryption options for the specified Elasticsearch domain.

        - **Enabled** *(boolean) --*

          Specify true to enable node-to-node encryption.

      - **Status** *(dict) --*

        Specifies the status of the node-to-node encryption options for the specified
        Elasticsearch domain.

        - **CreationDate** *(datetime) --*

          Timestamp which tells the creation date for the entity.

        - **UpdateDate** *(datetime) --*

          Timestamp which tells the last updated time for the entity.

        - **UpdateVersion** *(integer) --*

          Specifies the latest version for the entity.

        - **State** *(string) --*

          Provides the ``OptionState`` for the Elasticsearch domain.

        - **PendingDeletion** *(boolean) --*

          Indicates whether the Elasticsearch domain is being deleted.

    - **AdvancedOptions** *(dict) --*

      Specifies the ``AdvancedOptions`` for the domain. See `Configuring Advanced Options
      <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html#es-createdomain-configure-advanced-options>`__
      for more information.

      - **Options** *(dict) --*

        Specifies the status of advanced options for the specified Elasticsearch domain.

        - *(string) --*

          - *(string) --*

      - **Status** *(dict) --*

        Specifies the status of ``OptionStatus`` for advanced options for the specified
        Elasticsearch domain.

        - **CreationDate** *(datetime) --*

          Timestamp which tells the creation date for the entity.

        - **UpdateDate** *(datetime) --*

          Timestamp which tells the last updated time for the entity.

        - **UpdateVersion** *(integer) --*

          Specifies the latest version for the entity.

        - **State** *(string) --*

          Provides the ``OptionState`` for the Elasticsearch domain.

        - **PendingDeletion** *(boolean) --*

          Indicates whether the Elasticsearch domain is being deleted.

    - **LogPublishingOptions** *(dict) --*

      Log publishing options for the given domain.

      - **Options** *(dict) --*

        The log publishing options configured for the Elasticsearch domain.

        - *(string) --*

          Type of Log File, it can be one of the following:

          * INDEX_SLOW_LOGS: Index slow logs contain insert requests that took more time than
          configured index query log threshold to execute.

          * SEARCH_SLOW_LOGS: Search slow logs contain search queries that took more time than
          configured search query log threshold to execute.

          * ES_APPLICATION_LOGS: Elasticsearch application logs contain information about errors
          and warnings raised during the operation of the service and can be useful for
          troubleshooting.

          - *(dict) --*

            Log Publishing option that is set for given domain. Attributes and their details:

            * CloudWatchLogsLogGroupArn: ARN of the Cloudwatch log group to which log needs to be
            published.

            * Enabled: Whether the log publishing for given log type is enabled or not

            - **CloudWatchLogsLogGroupArn** *(string) --*

              ARN of the Cloudwatch log group to which log needs to be published.

            - **Enabled** *(boolean) --*

              Specifies whether given log publishing option is enabled or not.

      - **Status** *(dict) --*

        The status of the log publishing options for the Elasticsearch domain. See
        ``OptionStatus`` for the status information that's included.

        - **CreationDate** *(datetime) --*

          Timestamp which tells the creation date for the entity.

        - **UpdateDate** *(datetime) --*

          Timestamp which tells the last updated time for the entity.

        - **UpdateVersion** *(integer) --*

          Specifies the latest version for the entity.

        - **State** *(string) --*

          Provides the ``OptionState`` for the Elasticsearch domain.

        - **PendingDeletion** *(boolean) --*

          Indicates whether the Elasticsearch domain is being deleted.

    - **DomainEndpointOptions** *(dict) --*

      Specifies the ``DomainEndpointOptions`` for the Elasticsearch domain.

      - **Options** *(dict) --*

        Options to configure endpoint for the Elasticsearch domain.

        - **EnforceHTTPS** *(boolean) --*

          Specify if only HTTPS endpoint should be enabled for the Elasticsearch domain.

        - **TLSSecurityPolicy** *(string) --*

          Specify the TLS security policy that needs to be applied to the HTTPS endpoint of
          Elasticsearch domain. It can be one of the following values:

          * **Policy-Min-TLS-1-0-2019-07:** TLS security policy which supports TLSv1.0 and higher.

          * **Policy-Min-TLS-1-2-2019-07:** TLS security policy which supports only TLSv1.2

      - **Status** *(dict) --*

        The status of the endpoint options for the Elasticsearch domain. See ``OptionStatus`` for
        the status information that's included.

        - **CreationDate** *(datetime) --*

          Timestamp which tells the creation date for the entity.

        - **UpdateDate** *(datetime) --*

          Timestamp which tells the last updated time for the entity.

        - **UpdateVersion** *(integer) --*

          Specifies the latest version for the entity.

        - **State** *(string) --*

          Provides the ``OptionState`` for the Elasticsearch domain.

        - **PendingDeletion** *(boolean) --*

          Indicates whether the Elasticsearch domain is being deleted.
    """


_ClientUpdateElasticsearchDomainConfigResponseTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigResponseTypeDef",
    {"DomainConfig": ClientUpdateElasticsearchDomainConfigResponseDomainConfigTypeDef},
    total=False,
)


class ClientUpdateElasticsearchDomainConfigResponseTypeDef(
    _ClientUpdateElasticsearchDomainConfigResponseTypeDef
):
    """
    Type definition for `ClientUpdateElasticsearchDomainConfig` `Response`

    The result of an ``UpdateElasticsearchDomain`` request. Contains the status of the
    Elasticsearch domain being updated.

    - **DomainConfig** *(dict) --*

      The status of the updated Elasticsearch domain.

      - **ElasticsearchVersion** *(dict) --*

        String of format X.Y to specify version for the Elasticsearch domain.

        - **Options** *(string) --*

          Specifies the Elasticsearch version for the specified Elasticsearch domain.

        - **Status** *(dict) --*

          Specifies the status of the Elasticsearch version options for the specified Elasticsearch
          domain.

          - **CreationDate** *(datetime) --*

            Timestamp which tells the creation date for the entity.

          - **UpdateDate** *(datetime) --*

            Timestamp which tells the last updated time for the entity.

          - **UpdateVersion** *(integer) --*

            Specifies the latest version for the entity.

          - **State** *(string) --*

            Provides the ``OptionState`` for the Elasticsearch domain.

          - **PendingDeletion** *(boolean) --*

            Indicates whether the Elasticsearch domain is being deleted.

      - **ElasticsearchClusterConfig** *(dict) --*

        Specifies the ``ElasticsearchClusterConfig`` for the Elasticsearch domain.

        - **Options** *(dict) --*

          Specifies the cluster configuration for the specified Elasticsearch domain.

          - **InstanceType** *(string) --*

            The instance type for an Elasticsearch cluster.

          - **InstanceCount** *(integer) --*

            The number of instances in the specified domain cluster.

          - **DedicatedMasterEnabled** *(boolean) --*

            A boolean value to indicate whether a dedicated master node is enabled. See `About
            Dedicated Master Nodes
            <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains.html#es-managedomains-dedicatedmasternodes>`__
            for more information.

          - **ZoneAwarenessEnabled** *(boolean) --*

            A boolean value to indicate whether zone awareness is enabled. See `About Zone
            Awareness
            <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains.html#es-managedomains-zoneawareness>`__
            for more information.

          - **ZoneAwarenessConfig** *(dict) --*

            Specifies the zone awareness configuration for a domain when zone awareness is enabled.

            - **AvailabilityZoneCount** *(integer) --*

              An integer value to indicate the number of availability zones for a domain when zone
              awareness is enabled. This should be equal to number of subnets if VPC endpoints is
              enabled

          - **DedicatedMasterType** *(string) --*

            The instance type for a dedicated master node.

          - **DedicatedMasterCount** *(integer) --*

            Total number of dedicated master nodes, active and on standby, for the cluster.

        - **Status** *(dict) --*

          Specifies the status of the configuration for the specified Elasticsearch domain.

          - **CreationDate** *(datetime) --*

            Timestamp which tells the creation date for the entity.

          - **UpdateDate** *(datetime) --*

            Timestamp which tells the last updated time for the entity.

          - **UpdateVersion** *(integer) --*

            Specifies the latest version for the entity.

          - **State** *(string) --*

            Provides the ``OptionState`` for the Elasticsearch domain.

          - **PendingDeletion** *(boolean) --*

            Indicates whether the Elasticsearch domain is being deleted.

      - **EBSOptions** *(dict) --*

        Specifies the ``EBSOptions`` for the Elasticsearch domain.

        - **Options** *(dict) --*

          Specifies the EBS options for the specified Elasticsearch domain.

          - **EBSEnabled** *(boolean) --*

            Specifies whether EBS-based storage is enabled.

          - **VolumeType** *(string) --*

            Specifies the volume type for EBS-based storage.

          - **VolumeSize** *(integer) --*

            Integer to specify the size of an EBS volume.

          - **Iops** *(integer) --*

            Specifies the IOPD for a Provisioned IOPS EBS volume (SSD).

        - **Status** *(dict) --*

          Specifies the status of the EBS options for the specified Elasticsearch domain.

          - **CreationDate** *(datetime) --*

            Timestamp which tells the creation date for the entity.

          - **UpdateDate** *(datetime) --*

            Timestamp which tells the last updated time for the entity.

          - **UpdateVersion** *(integer) --*

            Specifies the latest version for the entity.

          - **State** *(string) --*

            Provides the ``OptionState`` for the Elasticsearch domain.

          - **PendingDeletion** *(boolean) --*

            Indicates whether the Elasticsearch domain is being deleted.

      - **AccessPolicies** *(dict) --*

        IAM access policy as a JSON-formatted string.

        - **Options** *(string) --*

          The access policy configured for the Elasticsearch domain. Access policies may be
          resource-based, IP-based, or IAM-based. See `Configuring Access Policies
          <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html#es-createdomain-configure-access-policies>`__
          for more information.

        - **Status** *(dict) --*

          The status of the access policy for the Elasticsearch domain. See ``OptionStatus`` for
          the status information that's included.

          - **CreationDate** *(datetime) --*

            Timestamp which tells the creation date for the entity.

          - **UpdateDate** *(datetime) --*

            Timestamp which tells the last updated time for the entity.

          - **UpdateVersion** *(integer) --*

            Specifies the latest version for the entity.

          - **State** *(string) --*

            Provides the ``OptionState`` for the Elasticsearch domain.

          - **PendingDeletion** *(boolean) --*

            Indicates whether the Elasticsearch domain is being deleted.

      - **SnapshotOptions** *(dict) --*

        Specifies the ``SnapshotOptions`` for the Elasticsearch domain.

        - **Options** *(dict) --*

          Specifies the daily snapshot options specified for the Elasticsearch domain.

          - **AutomatedSnapshotStartHour** *(integer) --*

            Specifies the time, in UTC format, when the service takes a daily automated snapshot of
            the specified Elasticsearch domain. Default value is ``0`` hours.

        - **Status** *(dict) --*

          Specifies the status of a daily automated snapshot.

          - **CreationDate** *(datetime) --*

            Timestamp which tells the creation date for the entity.

          - **UpdateDate** *(datetime) --*

            Timestamp which tells the last updated time for the entity.

          - **UpdateVersion** *(integer) --*

            Specifies the latest version for the entity.

          - **State** *(string) --*

            Provides the ``OptionState`` for the Elasticsearch domain.

          - **PendingDeletion** *(boolean) --*

            Indicates whether the Elasticsearch domain is being deleted.

      - **VPCOptions** *(dict) --*

        The ``VPCOptions`` for the specified domain. For more information, see `VPC Endpoints for
        Amazon Elasticsearch Service Domains
        <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html>`__ .

        - **Options** *(dict) --*

          Specifies the VPC options for the specified Elasticsearch domain.

          - **VPCId** *(string) --*

            The VPC Id for the Elasticsearch domain. Exists only if the domain was created with
            VPCOptions.

          - **SubnetIds** *(list) --*

            Specifies the subnets for VPC endpoint.

            - *(string) --*

          - **AvailabilityZones** *(list) --*

            The availability zones for the Elasticsearch domain. Exists only if the domain was
            created with VPCOptions.

            - *(string) --*

          - **SecurityGroupIds** *(list) --*

            Specifies the security groups for VPC endpoint.

            - *(string) --*

        - **Status** *(dict) --*

          Specifies the status of the VPC options for the specified Elasticsearch domain.

          - **CreationDate** *(datetime) --*

            Timestamp which tells the creation date for the entity.

          - **UpdateDate** *(datetime) --*

            Timestamp which tells the last updated time for the entity.

          - **UpdateVersion** *(integer) --*

            Specifies the latest version for the entity.

          - **State** *(string) --*

            Provides the ``OptionState`` for the Elasticsearch domain.

          - **PendingDeletion** *(boolean) --*

            Indicates whether the Elasticsearch domain is being deleted.

      - **CognitoOptions** *(dict) --*

        The ``CognitoOptions`` for the specified domain. For more information, see `Amazon Cognito
        Authentication for Kibana
        <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-cognito-auth.html>`__
        .

        - **Options** *(dict) --*

          Specifies the Cognito options for the specified Elasticsearch domain.

          - **Enabled** *(boolean) --*

            Specifies the option to enable Cognito for Kibana authentication.

          - **UserPoolId** *(string) --*

            Specifies the Cognito user pool ID for Kibana authentication.

          - **IdentityPoolId** *(string) --*

            Specifies the Cognito identity pool ID for Kibana authentication.

          - **RoleArn** *(string) --*

            Specifies the role ARN that provides Elasticsearch permissions for accessing Cognito
            resources.

        - **Status** *(dict) --*

          Specifies the status of the Cognito options for the specified Elasticsearch domain.

          - **CreationDate** *(datetime) --*

            Timestamp which tells the creation date for the entity.

          - **UpdateDate** *(datetime) --*

            Timestamp which tells the last updated time for the entity.

          - **UpdateVersion** *(integer) --*

            Specifies the latest version for the entity.

          - **State** *(string) --*

            Provides the ``OptionState`` for the Elasticsearch domain.

          - **PendingDeletion** *(boolean) --*

            Indicates whether the Elasticsearch domain is being deleted.

      - **EncryptionAtRestOptions** *(dict) --*

        Specifies the ``EncryptionAtRestOptions`` for the Elasticsearch domain.

        - **Options** *(dict) --*

          Specifies the Encryption At Rest options for the specified Elasticsearch domain.

          - **Enabled** *(boolean) --*

            Specifies the option to enable Encryption At Rest.

          - **KmsKeyId** *(string) --*

            Specifies the KMS Key ID for Encryption At Rest options.

        - **Status** *(dict) --*

          Specifies the status of the Encryption At Rest options for the specified Elasticsearch
          domain.

          - **CreationDate** *(datetime) --*

            Timestamp which tells the creation date for the entity.

          - **UpdateDate** *(datetime) --*

            Timestamp which tells the last updated time for the entity.

          - **UpdateVersion** *(integer) --*

            Specifies the latest version for the entity.

          - **State** *(string) --*

            Provides the ``OptionState`` for the Elasticsearch domain.

          - **PendingDeletion** *(boolean) --*

            Indicates whether the Elasticsearch domain is being deleted.

      - **NodeToNodeEncryptionOptions** *(dict) --*

        Specifies the ``NodeToNodeEncryptionOptions`` for the Elasticsearch domain.

        - **Options** *(dict) --*

          Specifies the node-to-node encryption options for the specified Elasticsearch domain.

          - **Enabled** *(boolean) --*

            Specify true to enable node-to-node encryption.

        - **Status** *(dict) --*

          Specifies the status of the node-to-node encryption options for the specified
          Elasticsearch domain.

          - **CreationDate** *(datetime) --*

            Timestamp which tells the creation date for the entity.

          - **UpdateDate** *(datetime) --*

            Timestamp which tells the last updated time for the entity.

          - **UpdateVersion** *(integer) --*

            Specifies the latest version for the entity.

          - **State** *(string) --*

            Provides the ``OptionState`` for the Elasticsearch domain.

          - **PendingDeletion** *(boolean) --*

            Indicates whether the Elasticsearch domain is being deleted.

      - **AdvancedOptions** *(dict) --*

        Specifies the ``AdvancedOptions`` for the domain. See `Configuring Advanced Options
        <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html#es-createdomain-configure-advanced-options>`__
        for more information.

        - **Options** *(dict) --*

          Specifies the status of advanced options for the specified Elasticsearch domain.

          - *(string) --*

            - *(string) --*

        - **Status** *(dict) --*

          Specifies the status of ``OptionStatus`` for advanced options for the specified
          Elasticsearch domain.

          - **CreationDate** *(datetime) --*

            Timestamp which tells the creation date for the entity.

          - **UpdateDate** *(datetime) --*

            Timestamp which tells the last updated time for the entity.

          - **UpdateVersion** *(integer) --*

            Specifies the latest version for the entity.

          - **State** *(string) --*

            Provides the ``OptionState`` for the Elasticsearch domain.

          - **PendingDeletion** *(boolean) --*

            Indicates whether the Elasticsearch domain is being deleted.

      - **LogPublishingOptions** *(dict) --*

        Log publishing options for the given domain.

        - **Options** *(dict) --*

          The log publishing options configured for the Elasticsearch domain.

          - *(string) --*

            Type of Log File, it can be one of the following:

            * INDEX_SLOW_LOGS: Index slow logs contain insert requests that took more time than
            configured index query log threshold to execute.

            * SEARCH_SLOW_LOGS: Search slow logs contain search queries that took more time than
            configured search query log threshold to execute.

            * ES_APPLICATION_LOGS: Elasticsearch application logs contain information about errors
            and warnings raised during the operation of the service and can be useful for
            troubleshooting.

            - *(dict) --*

              Log Publishing option that is set for given domain. Attributes and their details:

              * CloudWatchLogsLogGroupArn: ARN of the Cloudwatch log group to which log needs to be
              published.

              * Enabled: Whether the log publishing for given log type is enabled or not

              - **CloudWatchLogsLogGroupArn** *(string) --*

                ARN of the Cloudwatch log group to which log needs to be published.

              - **Enabled** *(boolean) --*

                Specifies whether given log publishing option is enabled or not.

        - **Status** *(dict) --*

          The status of the log publishing options for the Elasticsearch domain. See
          ``OptionStatus`` for the status information that's included.

          - **CreationDate** *(datetime) --*

            Timestamp which tells the creation date for the entity.

          - **UpdateDate** *(datetime) --*

            Timestamp which tells the last updated time for the entity.

          - **UpdateVersion** *(integer) --*

            Specifies the latest version for the entity.

          - **State** *(string) --*

            Provides the ``OptionState`` for the Elasticsearch domain.

          - **PendingDeletion** *(boolean) --*

            Indicates whether the Elasticsearch domain is being deleted.

      - **DomainEndpointOptions** *(dict) --*

        Specifies the ``DomainEndpointOptions`` for the Elasticsearch domain.

        - **Options** *(dict) --*

          Options to configure endpoint for the Elasticsearch domain.

          - **EnforceHTTPS** *(boolean) --*

            Specify if only HTTPS endpoint should be enabled for the Elasticsearch domain.

          - **TLSSecurityPolicy** *(string) --*

            Specify the TLS security policy that needs to be applied to the HTTPS endpoint of
            Elasticsearch domain. It can be one of the following values:

            * **Policy-Min-TLS-1-0-2019-07:** TLS security policy which supports TLSv1.0 and higher.

            * **Policy-Min-TLS-1-2-2019-07:** TLS security policy which supports only TLSv1.2

        - **Status** *(dict) --*

          The status of the endpoint options for the Elasticsearch domain. See ``OptionStatus`` for
          the status information that's included.

          - **CreationDate** *(datetime) --*

            Timestamp which tells the creation date for the entity.

          - **UpdateDate** *(datetime) --*

            Timestamp which tells the last updated time for the entity.

          - **UpdateVersion** *(integer) --*

            Specifies the latest version for the entity.

          - **State** *(string) --*

            Provides the ``OptionState`` for the Elasticsearch domain.

          - **PendingDeletion** *(boolean) --*

            Indicates whether the Elasticsearch domain is being deleted.
    """


_ClientUpdateElasticsearchDomainConfigSnapshotOptionsTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigSnapshotOptionsTypeDef",
    {"AutomatedSnapshotStartHour": int},
    total=False,
)


class ClientUpdateElasticsearchDomainConfigSnapshotOptionsTypeDef(
    _ClientUpdateElasticsearchDomainConfigSnapshotOptionsTypeDef
):
    """
    Type definition for `ClientUpdateElasticsearchDomainConfig` `SnapshotOptions`

    Option to set the time, in UTC format, for the daily automated snapshot. Default value is ``0``
    hours.

    - **AutomatedSnapshotStartHour** *(integer) --*

      Specifies the time, in UTC format, when the service takes a daily automated snapshot of the
      specified Elasticsearch domain. Default value is ``0`` hours.
    """


_ClientUpdateElasticsearchDomainConfigVPCOptionsTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigVPCOptionsTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str]},
    total=False,
)


class ClientUpdateElasticsearchDomainConfigVPCOptionsTypeDef(
    _ClientUpdateElasticsearchDomainConfigVPCOptionsTypeDef
):
    """
    Type definition for `ClientUpdateElasticsearchDomainConfig` `VPCOptions`

    Options to specify the subnets and security groups for VPC endpoint. For more information, see
    `Creating a VPC
    <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html#es-creating-vpc>`__
    in *VPC Endpoints for Amazon Elasticsearch Service Domains*

    - **SubnetIds** *(list) --*

      Specifies the subnets for VPC endpoint.

      - *(string) --*

    - **SecurityGroupIds** *(list) --*

      Specifies the security groups for VPC endpoint.

      - *(string) --*
    """


_ClientUpgradeElasticsearchDomainResponseTypeDef = TypedDict(
    "_ClientUpgradeElasticsearchDomainResponseTypeDef",
    {"DomainName": str, "TargetVersion": str, "PerformCheckOnly": bool},
    total=False,
)


class ClientUpgradeElasticsearchDomainResponseTypeDef(
    _ClientUpgradeElasticsearchDomainResponseTypeDef
):
    """
    Type definition for `ClientUpgradeElasticsearchDomain` `Response`

    Container for response returned by ``  UpgradeElasticsearchDomain `` operation.

    - **DomainName** *(string) --*

      The name of an Elasticsearch domain. Domain names are unique across the domains owned by an
      account within an AWS region. Domain names start with a letter or number and can contain the
      following characters: a-z (lowercase), 0-9, and - (hyphen).

    - **TargetVersion** *(string) --*

      The version of Elasticsearch that you intend to upgrade the domain to.

    - **PerformCheckOnly** *(boolean) --*

      This flag, when set to True, indicates that an Upgrade Eligibility Check needs to be
      performed. This will not actually perform the Upgrade.
    """


_DescribeReservedElasticsearchInstanceOfferingsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeReservedElasticsearchInstanceOfferingsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeReservedElasticsearchInstanceOfferingsPaginatePaginationConfigTypeDef(
    _DescribeReservedElasticsearchInstanceOfferingsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeReservedElasticsearchInstanceOfferingsPaginate` `PaginationConfig`

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


_DescribeReservedElasticsearchInstanceOfferingsPaginateResponseReservedElasticsearchInstanceOfferingsRecurringChargesTypeDef = TypedDict(
    "_DescribeReservedElasticsearchInstanceOfferingsPaginateResponseReservedElasticsearchInstanceOfferingsRecurringChargesTypeDef",
    {"RecurringChargeAmount": float, "RecurringChargeFrequency": str},
    total=False,
)


class DescribeReservedElasticsearchInstanceOfferingsPaginateResponseReservedElasticsearchInstanceOfferingsRecurringChargesTypeDef(
    _DescribeReservedElasticsearchInstanceOfferingsPaginateResponseReservedElasticsearchInstanceOfferingsRecurringChargesTypeDef
):
    """
    Type definition for `DescribeReservedElasticsearchInstanceOfferingsPaginateResponseReservedElasticsearchInstanceOfferings` `RecurringCharges`

    Contains the specific price and frequency of a recurring charges for a reserved
    Elasticsearch instance, or for a reserved Elasticsearch instance offering.

    - **RecurringChargeAmount** *(float) --*

      The monetary amount of the recurring charge.

    - **RecurringChargeFrequency** *(string) --*

      The frequency of the recurring charge.
    """


_DescribeReservedElasticsearchInstanceOfferingsPaginateResponseReservedElasticsearchInstanceOfferingsTypeDef = TypedDict(
    "_DescribeReservedElasticsearchInstanceOfferingsPaginateResponseReservedElasticsearchInstanceOfferingsTypeDef",
    {
        "ReservedElasticsearchInstanceOfferingId": str,
        "ElasticsearchInstanceType": str,
        "Duration": int,
        "FixedPrice": float,
        "UsagePrice": float,
        "CurrencyCode": str,
        "PaymentOption": str,
        "RecurringCharges": List[
            DescribeReservedElasticsearchInstanceOfferingsPaginateResponseReservedElasticsearchInstanceOfferingsRecurringChargesTypeDef
        ],
    },
    total=False,
)


class DescribeReservedElasticsearchInstanceOfferingsPaginateResponseReservedElasticsearchInstanceOfferingsTypeDef(
    _DescribeReservedElasticsearchInstanceOfferingsPaginateResponseReservedElasticsearchInstanceOfferingsTypeDef
):
    """
    Type definition for `DescribeReservedElasticsearchInstanceOfferingsPaginateResponse` `ReservedElasticsearchInstanceOfferings`

    Details of a reserved Elasticsearch instance offering.

    - **ReservedElasticsearchInstanceOfferingId** *(string) --*

      The Elasticsearch reserved instance offering identifier.

    - **ElasticsearchInstanceType** *(string) --*

      The Elasticsearch instance type offered by the reserved instance offering.

    - **Duration** *(integer) --*

      The duration, in seconds, for which the offering will reserve the Elasticsearch instance.

    - **FixedPrice** *(float) --*

      The upfront fixed charge you will pay to purchase the specific reserved Elasticsearch
      instance offering.

    - **UsagePrice** *(float) --*

      The rate you are charged for each hour the domain that is using the offering is running.

    - **CurrencyCode** *(string) --*

      The currency code for the reserved Elasticsearch instance offering.

    - **PaymentOption** *(string) --*

      Payment option for the reserved Elasticsearch instance offering

    - **RecurringCharges** *(list) --*

      The charge to your account regardless of whether you are creating any domains using the
      instance offering.

      - *(dict) --*

        Contains the specific price and frequency of a recurring charges for a reserved
        Elasticsearch instance, or for a reserved Elasticsearch instance offering.

        - **RecurringChargeAmount** *(float) --*

          The monetary amount of the recurring charge.

        - **RecurringChargeFrequency** *(string) --*

          The frequency of the recurring charge.
    """


_DescribeReservedElasticsearchInstanceOfferingsPaginateResponseTypeDef = TypedDict(
    "_DescribeReservedElasticsearchInstanceOfferingsPaginateResponseTypeDef",
    {
        "ReservedElasticsearchInstanceOfferings": List[
            DescribeReservedElasticsearchInstanceOfferingsPaginateResponseReservedElasticsearchInstanceOfferingsTypeDef
        ]
    },
    total=False,
)


class DescribeReservedElasticsearchInstanceOfferingsPaginateResponseTypeDef(
    _DescribeReservedElasticsearchInstanceOfferingsPaginateResponseTypeDef
):
    """
    Type definition for `DescribeReservedElasticsearchInstanceOfferingsPaginate` `Response`

    Container for results from ``DescribeReservedElasticsearchInstanceOfferings``

    - **ReservedElasticsearchInstanceOfferings** *(list) --*

      List of reserved Elasticsearch instance offerings

      - *(dict) --*

        Details of a reserved Elasticsearch instance offering.

        - **ReservedElasticsearchInstanceOfferingId** *(string) --*

          The Elasticsearch reserved instance offering identifier.

        - **ElasticsearchInstanceType** *(string) --*

          The Elasticsearch instance type offered by the reserved instance offering.

        - **Duration** *(integer) --*

          The duration, in seconds, for which the offering will reserve the Elasticsearch instance.

        - **FixedPrice** *(float) --*

          The upfront fixed charge you will pay to purchase the specific reserved Elasticsearch
          instance offering.

        - **UsagePrice** *(float) --*

          The rate you are charged for each hour the domain that is using the offering is running.

        - **CurrencyCode** *(string) --*

          The currency code for the reserved Elasticsearch instance offering.

        - **PaymentOption** *(string) --*

          Payment option for the reserved Elasticsearch instance offering

        - **RecurringCharges** *(list) --*

          The charge to your account regardless of whether you are creating any domains using the
          instance offering.

          - *(dict) --*

            Contains the specific price and frequency of a recurring charges for a reserved
            Elasticsearch instance, or for a reserved Elasticsearch instance offering.

            - **RecurringChargeAmount** *(float) --*

              The monetary amount of the recurring charge.

            - **RecurringChargeFrequency** *(string) --*

              The frequency of the recurring charge.
    """


_DescribeReservedElasticsearchInstancesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeReservedElasticsearchInstancesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeReservedElasticsearchInstancesPaginatePaginationConfigTypeDef(
    _DescribeReservedElasticsearchInstancesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeReservedElasticsearchInstancesPaginate` `PaginationConfig`

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


_DescribeReservedElasticsearchInstancesPaginateResponseReservedElasticsearchInstancesRecurringChargesTypeDef = TypedDict(
    "_DescribeReservedElasticsearchInstancesPaginateResponseReservedElasticsearchInstancesRecurringChargesTypeDef",
    {"RecurringChargeAmount": float, "RecurringChargeFrequency": str},
    total=False,
)


class DescribeReservedElasticsearchInstancesPaginateResponseReservedElasticsearchInstancesRecurringChargesTypeDef(
    _DescribeReservedElasticsearchInstancesPaginateResponseReservedElasticsearchInstancesRecurringChargesTypeDef
):
    """
    Type definition for `DescribeReservedElasticsearchInstancesPaginateResponseReservedElasticsearchInstances` `RecurringCharges`

    Contains the specific price and frequency of a recurring charges for a reserved
    Elasticsearch instance, or for a reserved Elasticsearch instance offering.

    - **RecurringChargeAmount** *(float) --*

      The monetary amount of the recurring charge.

    - **RecurringChargeFrequency** *(string) --*

      The frequency of the recurring charge.
    """


_DescribeReservedElasticsearchInstancesPaginateResponseReservedElasticsearchInstancesTypeDef = TypedDict(
    "_DescribeReservedElasticsearchInstancesPaginateResponseReservedElasticsearchInstancesTypeDef",
    {
        "ReservationName": str,
        "ReservedElasticsearchInstanceId": str,
        "ReservedElasticsearchInstanceOfferingId": str,
        "ElasticsearchInstanceType": str,
        "StartTime": datetime,
        "Duration": int,
        "FixedPrice": float,
        "UsagePrice": float,
        "CurrencyCode": str,
        "ElasticsearchInstanceCount": int,
        "State": str,
        "PaymentOption": str,
        "RecurringCharges": List[
            DescribeReservedElasticsearchInstancesPaginateResponseReservedElasticsearchInstancesRecurringChargesTypeDef
        ],
    },
    total=False,
)


class DescribeReservedElasticsearchInstancesPaginateResponseReservedElasticsearchInstancesTypeDef(
    _DescribeReservedElasticsearchInstancesPaginateResponseReservedElasticsearchInstancesTypeDef
):
    """
    Type definition for `DescribeReservedElasticsearchInstancesPaginateResponse` `ReservedElasticsearchInstances`

    Details of a reserved Elasticsearch instance.

    - **ReservationName** *(string) --*

      The customer-specified identifier to track this reservation.

    - **ReservedElasticsearchInstanceId** *(string) --*

      The unique identifier for the reservation.

    - **ReservedElasticsearchInstanceOfferingId** *(string) --*

      The offering identifier.

    - **ElasticsearchInstanceType** *(string) --*

      The Elasticsearch instance type offered by the reserved instance offering.

    - **StartTime** *(datetime) --*

      The time the reservation started.

    - **Duration** *(integer) --*

      The duration, in seconds, for which the Elasticsearch instance is reserved.

    - **FixedPrice** *(float) --*

      The upfront fixed charge you will paid to purchase the specific reserved Elasticsearch
      instance offering.

    - **UsagePrice** *(float) --*

      The rate you are charged for each hour for the domain that is using this reserved
      instance.

    - **CurrencyCode** *(string) --*

      The currency code for the reserved Elasticsearch instance offering.

    - **ElasticsearchInstanceCount** *(integer) --*

      The number of Elasticsearch instances that have been reserved.

    - **State** *(string) --*

      The state of the reserved Elasticsearch instance.

    - **PaymentOption** *(string) --*

      The payment option as defined in the reserved Elasticsearch instance offering.

    - **RecurringCharges** *(list) --*

      The charge to your account regardless of whether you are creating any domains using the
      instance offering.

      - *(dict) --*

        Contains the specific price and frequency of a recurring charges for a reserved
        Elasticsearch instance, or for a reserved Elasticsearch instance offering.

        - **RecurringChargeAmount** *(float) --*

          The monetary amount of the recurring charge.

        - **RecurringChargeFrequency** *(string) --*

          The frequency of the recurring charge.
    """


_DescribeReservedElasticsearchInstancesPaginateResponseTypeDef = TypedDict(
    "_DescribeReservedElasticsearchInstancesPaginateResponseTypeDef",
    {
        "ReservedElasticsearchInstances": List[
            DescribeReservedElasticsearchInstancesPaginateResponseReservedElasticsearchInstancesTypeDef
        ]
    },
    total=False,
)


class DescribeReservedElasticsearchInstancesPaginateResponseTypeDef(
    _DescribeReservedElasticsearchInstancesPaginateResponseTypeDef
):
    """
    Type definition for `DescribeReservedElasticsearchInstancesPaginate` `Response`

    Container for results from ``DescribeReservedElasticsearchInstances``

    - **ReservedElasticsearchInstances** *(list) --*

      List of reserved Elasticsearch instances.

      - *(dict) --*

        Details of a reserved Elasticsearch instance.

        - **ReservationName** *(string) --*

          The customer-specified identifier to track this reservation.

        - **ReservedElasticsearchInstanceId** *(string) --*

          The unique identifier for the reservation.

        - **ReservedElasticsearchInstanceOfferingId** *(string) --*

          The offering identifier.

        - **ElasticsearchInstanceType** *(string) --*

          The Elasticsearch instance type offered by the reserved instance offering.

        - **StartTime** *(datetime) --*

          The time the reservation started.

        - **Duration** *(integer) --*

          The duration, in seconds, for which the Elasticsearch instance is reserved.

        - **FixedPrice** *(float) --*

          The upfront fixed charge you will paid to purchase the specific reserved Elasticsearch
          instance offering.

        - **UsagePrice** *(float) --*

          The rate you are charged for each hour for the domain that is using this reserved
          instance.

        - **CurrencyCode** *(string) --*

          The currency code for the reserved Elasticsearch instance offering.

        - **ElasticsearchInstanceCount** *(integer) --*

          The number of Elasticsearch instances that have been reserved.

        - **State** *(string) --*

          The state of the reserved Elasticsearch instance.

        - **PaymentOption** *(string) --*

          The payment option as defined in the reserved Elasticsearch instance offering.

        - **RecurringCharges** *(list) --*

          The charge to your account regardless of whether you are creating any domains using the
          instance offering.

          - *(dict) --*

            Contains the specific price and frequency of a recurring charges for a reserved
            Elasticsearch instance, or for a reserved Elasticsearch instance offering.

            - **RecurringChargeAmount** *(float) --*

              The monetary amount of the recurring charge.

            - **RecurringChargeFrequency** *(string) --*

              The frequency of the recurring charge.
    """


_GetUpgradeHistoryPaginatePaginationConfigTypeDef = TypedDict(
    "_GetUpgradeHistoryPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetUpgradeHistoryPaginatePaginationConfigTypeDef(
    _GetUpgradeHistoryPaginatePaginationConfigTypeDef
):
    """
    Type definition for `GetUpgradeHistoryPaginate` `PaginationConfig`

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


_GetUpgradeHistoryPaginateResponseUpgradeHistoriesStepsListTypeDef = TypedDict(
    "_GetUpgradeHistoryPaginateResponseUpgradeHistoriesStepsListTypeDef",
    {
        "UpgradeStep": str,
        "UpgradeStepStatus": str,
        "Issues": List[str],
        "ProgressPercent": float,
    },
    total=False,
)


class GetUpgradeHistoryPaginateResponseUpgradeHistoriesStepsListTypeDef(
    _GetUpgradeHistoryPaginateResponseUpgradeHistoriesStepsListTypeDef
):
    """
    Type definition for `GetUpgradeHistoryPaginateResponseUpgradeHistories` `StepsList`

    Represents a single step of the Upgrade or Upgrade Eligibility Check workflow.

    - **UpgradeStep** *(string) --*

      Represents one of 3 steps that an Upgrade or Upgrade Eligibility Check does through:

      * PreUpgradeCheck

      * Snapshot

      * Upgrade

    - **UpgradeStepStatus** *(string) --*

      The status of a particular step during an upgrade. The status can take one of the
      following values:

      * In Progress

      * Succeeded

      * Succeeded with Issues

      * Failed

    - **Issues** *(list) --*

      A list of strings containing detailed information about the errors encountered in a
      particular step.

      - *(string) --*

    - **ProgressPercent** *(float) --*

      The Floating point value representing progress percentage of a particular step.
    """


_GetUpgradeHistoryPaginateResponseUpgradeHistoriesTypeDef = TypedDict(
    "_GetUpgradeHistoryPaginateResponseUpgradeHistoriesTypeDef",
    {
        "UpgradeName": str,
        "StartTimestamp": datetime,
        "UpgradeStatus": str,
        "StepsList": List[
            GetUpgradeHistoryPaginateResponseUpgradeHistoriesStepsListTypeDef
        ],
    },
    total=False,
)


class GetUpgradeHistoryPaginateResponseUpgradeHistoriesTypeDef(
    _GetUpgradeHistoryPaginateResponseUpgradeHistoriesTypeDef
):
    """
    Type definition for `GetUpgradeHistoryPaginateResponse` `UpgradeHistories`

    History of the last 10 Upgrades and Upgrade Eligibility Checks.

    - **UpgradeName** *(string) --*

      A string that describes the update briefly

    - **StartTimestamp** *(datetime) --*

      UTC Timestamp at which the Upgrade API call was made in "yyyy-MM-ddTHH:mm:ssZ" format.

    - **UpgradeStatus** *(string) --*

      The overall status of the update. The status can take one of the following values:

      * In Progress

      * Succeeded

      * Succeeded with Issues

      * Failed

    - **StepsList** *(list) --*

      A list of ``  UpgradeStepItem `` s representing information about each step performed as
      pard of a specific Upgrade or Upgrade Eligibility Check.

      - *(dict) --*

        Represents a single step of the Upgrade or Upgrade Eligibility Check workflow.

        - **UpgradeStep** *(string) --*

          Represents one of 3 steps that an Upgrade or Upgrade Eligibility Check does through:

          * PreUpgradeCheck

          * Snapshot

          * Upgrade

        - **UpgradeStepStatus** *(string) --*

          The status of a particular step during an upgrade. The status can take one of the
          following values:

          * In Progress

          * Succeeded

          * Succeeded with Issues

          * Failed

        - **Issues** *(list) --*

          A list of strings containing detailed information about the errors encountered in a
          particular step.

          - *(string) --*

        - **ProgressPercent** *(float) --*

          The Floating point value representing progress percentage of a particular step.
    """


_GetUpgradeHistoryPaginateResponseTypeDef = TypedDict(
    "_GetUpgradeHistoryPaginateResponseTypeDef",
    {
        "UpgradeHistories": List[
            GetUpgradeHistoryPaginateResponseUpgradeHistoriesTypeDef
        ]
    },
    total=False,
)


class GetUpgradeHistoryPaginateResponseTypeDef(
    _GetUpgradeHistoryPaginateResponseTypeDef
):
    """
    Type definition for `GetUpgradeHistoryPaginate` `Response`

    Container for response returned by ``  GetUpgradeHistory `` operation.

    - **UpgradeHistories** *(list) --*

      A list of ``  UpgradeHistory `` objects corresponding to each Upgrade or Upgrade Eligibility
      Check performed on a domain returned as part of ``  GetUpgradeHistoryResponse `` object.

      - *(dict) --*

        History of the last 10 Upgrades and Upgrade Eligibility Checks.

        - **UpgradeName** *(string) --*

          A string that describes the update briefly

        - **StartTimestamp** *(datetime) --*

          UTC Timestamp at which the Upgrade API call was made in "yyyy-MM-ddTHH:mm:ssZ" format.

        - **UpgradeStatus** *(string) --*

          The overall status of the update. The status can take one of the following values:

          * In Progress

          * Succeeded

          * Succeeded with Issues

          * Failed

        - **StepsList** *(list) --*

          A list of ``  UpgradeStepItem `` s representing information about each step performed as
          pard of a specific Upgrade or Upgrade Eligibility Check.

          - *(dict) --*

            Represents a single step of the Upgrade or Upgrade Eligibility Check workflow.

            - **UpgradeStep** *(string) --*

              Represents one of 3 steps that an Upgrade or Upgrade Eligibility Check does through:

              * PreUpgradeCheck

              * Snapshot

              * Upgrade

            - **UpgradeStepStatus** *(string) --*

              The status of a particular step during an upgrade. The status can take one of the
              following values:

              * In Progress

              * Succeeded

              * Succeeded with Issues

              * Failed

            - **Issues** *(list) --*

              A list of strings containing detailed information about the errors encountered in a
              particular step.

              - *(string) --*

            - **ProgressPercent** *(float) --*

              The Floating point value representing progress percentage of a particular step.
    """


_ListElasticsearchInstanceTypesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListElasticsearchInstanceTypesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListElasticsearchInstanceTypesPaginatePaginationConfigTypeDef(
    _ListElasticsearchInstanceTypesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListElasticsearchInstanceTypesPaginate` `PaginationConfig`

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


_ListElasticsearchInstanceTypesPaginateResponseTypeDef = TypedDict(
    "_ListElasticsearchInstanceTypesPaginateResponseTypeDef",
    {"ElasticsearchInstanceTypes": List[str]},
    total=False,
)


class ListElasticsearchInstanceTypesPaginateResponseTypeDef(
    _ListElasticsearchInstanceTypesPaginateResponseTypeDef
):
    """
    Type definition for `ListElasticsearchInstanceTypesPaginate` `Response`

    Container for the parameters returned by ``  ListElasticsearchInstanceTypes `` operation.

    - **ElasticsearchInstanceTypes** *(list) --*

      List of instance types supported by Amazon Elasticsearch service for given ``
      ElasticsearchVersion ``

      - *(string) --*
    """


_ListElasticsearchVersionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListElasticsearchVersionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListElasticsearchVersionsPaginatePaginationConfigTypeDef(
    _ListElasticsearchVersionsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListElasticsearchVersionsPaginate` `PaginationConfig`

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


_ListElasticsearchVersionsPaginateResponseTypeDef = TypedDict(
    "_ListElasticsearchVersionsPaginateResponseTypeDef",
    {"ElasticsearchVersions": List[str]},
    total=False,
)


class ListElasticsearchVersionsPaginateResponseTypeDef(
    _ListElasticsearchVersionsPaginateResponseTypeDef
):
    """
    Type definition for `ListElasticsearchVersionsPaginate` `Response`

    Container for the parameters for response received from ``  ListElasticsearchVersions ``
    operation.

    - **ElasticsearchVersions** *(list) --*

      List of supported elastic search versions.

      - *(string) --*
    """
