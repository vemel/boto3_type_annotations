"Main interface for license-manager type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from typing_extensions import TypedDict


__all__ = (
    "ClientCreateLicenseConfigurationResponseTypeDef",
    "ClientCreateLicenseConfigurationTagsTypeDef",
    "ClientGetLicenseConfigurationResponseConsumedLicenseSummaryListTypeDef",
    "ClientGetLicenseConfigurationResponseManagedResourceSummaryListTypeDef",
    "ClientGetLicenseConfigurationResponseTagsTypeDef",
    "ClientGetLicenseConfigurationResponseTypeDef",
    "ClientGetServiceSettingsResponseOrganizationConfigurationTypeDef",
    "ClientGetServiceSettingsResponseTypeDef",
    "ClientListAssociationsForLicenseConfigurationResponseLicenseConfigurationAssociationsTypeDef",
    "ClientListAssociationsForLicenseConfigurationResponseTypeDef",
    "ClientListLicenseConfigurationsFiltersTypeDef",
    "ClientListLicenseConfigurationsResponseLicenseConfigurationsConsumedLicenseSummaryListTypeDef",
    "ClientListLicenseConfigurationsResponseLicenseConfigurationsManagedResourceSummaryListTypeDef",
    "ClientListLicenseConfigurationsResponseLicenseConfigurationsTypeDef",
    "ClientListLicenseConfigurationsResponseTypeDef",
    "ClientListLicenseSpecificationsForResourceResponseLicenseSpecificationsTypeDef",
    "ClientListLicenseSpecificationsForResourceResponseTypeDef",
    "ClientListResourceInventoryFiltersTypeDef",
    "ClientListResourceInventoryResponseResourceInventoryListTypeDef",
    "ClientListResourceInventoryResponseTypeDef",
    "ClientListTagsForResourceResponseTagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientListUsageForLicenseConfigurationFiltersTypeDef",
    "ClientListUsageForLicenseConfigurationResponseLicenseConfigurationUsageListTypeDef",
    "ClientListUsageForLicenseConfigurationResponseTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientUpdateLicenseSpecificationsForResourceAddLicenseSpecificationsTypeDef",
    "ClientUpdateLicenseSpecificationsForResourceRemoveLicenseSpecificationsTypeDef",
    "ClientUpdateServiceSettingsOrganizationConfigurationTypeDef",
    "ListAssociationsForLicenseConfigurationPaginatePaginationConfigTypeDef",
    "ListAssociationsForLicenseConfigurationPaginateResponseLicenseConfigurationAssociationsTypeDef",
    "ListAssociationsForLicenseConfigurationPaginateResponseTypeDef",
    "ListLicenseConfigurationsPaginateFiltersTypeDef",
    "ListLicenseConfigurationsPaginatePaginationConfigTypeDef",
    "ListLicenseConfigurationsPaginateResponseLicenseConfigurationsConsumedLicenseSummaryListTypeDef",
    "ListLicenseConfigurationsPaginateResponseLicenseConfigurationsManagedResourceSummaryListTypeDef",
    "ListLicenseConfigurationsPaginateResponseLicenseConfigurationsTypeDef",
    "ListLicenseConfigurationsPaginateResponseTypeDef",
    "ListLicenseSpecificationsForResourcePaginatePaginationConfigTypeDef",
    "ListLicenseSpecificationsForResourcePaginateResponseLicenseSpecificationsTypeDef",
    "ListLicenseSpecificationsForResourcePaginateResponseTypeDef",
    "ListResourceInventoryPaginateFiltersTypeDef",
    "ListResourceInventoryPaginatePaginationConfigTypeDef",
    "ListResourceInventoryPaginateResponseResourceInventoryListTypeDef",
    "ListResourceInventoryPaginateResponseTypeDef",
    "ListUsageForLicenseConfigurationPaginateFiltersTypeDef",
    "ListUsageForLicenseConfigurationPaginatePaginationConfigTypeDef",
    "ListUsageForLicenseConfigurationPaginateResponseLicenseConfigurationUsageListTypeDef",
    "ListUsageForLicenseConfigurationPaginateResponseTypeDef",
)


_ClientCreateLicenseConfigurationResponseTypeDef = TypedDict(
    "_ClientCreateLicenseConfigurationResponseTypeDef",
    {"LicenseConfigurationArn": str},
    total=False,
)


class ClientCreateLicenseConfigurationResponseTypeDef(
    _ClientCreateLicenseConfigurationResponseTypeDef
):
    """
    Type definition for `ClientCreateLicenseConfiguration` `Response`

    - **LicenseConfigurationArn** *(string) --*

      ARN of the license configuration object after its creation.
    """


_ClientCreateLicenseConfigurationTagsTypeDef = TypedDict(
    "_ClientCreateLicenseConfigurationTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientCreateLicenseConfigurationTagsTypeDef(
    _ClientCreateLicenseConfigurationTagsTypeDef
):
    """
    Type definition for `ClientCreateLicenseConfiguration` `Tags`

    Tag for a resource in a key-value format.

    - **Key** *(string) --*

      Key for the resource tag.

    - **Value** *(string) --*

      Value for the resource tag.
    """


_ClientGetLicenseConfigurationResponseConsumedLicenseSummaryListTypeDef = TypedDict(
    "_ClientGetLicenseConfigurationResponseConsumedLicenseSummaryListTypeDef",
    {"ResourceType": str, "ConsumedLicenses": int},
    total=False,
)


class ClientGetLicenseConfigurationResponseConsumedLicenseSummaryListTypeDef(
    _ClientGetLicenseConfigurationResponseConsumedLicenseSummaryListTypeDef
):
    """
    Type definition for `ClientGetLicenseConfigurationResponse` `ConsumedLicenseSummaryList`

    Details about license consumption.

    - **ResourceType** *(string) --*

      Resource type of the resource consuming a license (instance, host, or AMI).

    - **ConsumedLicenses** *(integer) --*

      Number of licenses consumed by a resource.
    """


_ClientGetLicenseConfigurationResponseManagedResourceSummaryListTypeDef = TypedDict(
    "_ClientGetLicenseConfigurationResponseManagedResourceSummaryListTypeDef",
    {"ResourceType": str, "AssociationCount": int},
    total=False,
)


class ClientGetLicenseConfigurationResponseManagedResourceSummaryListTypeDef(
    _ClientGetLicenseConfigurationResponseManagedResourceSummaryListTypeDef
):
    """
    Type definition for `ClientGetLicenseConfigurationResponse` `ManagedResourceSummaryList`

    Summary for a resource.

    - **ResourceType** *(string) --*

      Type of resource associated with a license (instance, host, or AMI).

    - **AssociationCount** *(integer) --*

      Number of resources associated with licenses.
    """


_ClientGetLicenseConfigurationResponseTagsTypeDef = TypedDict(
    "_ClientGetLicenseConfigurationResponseTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientGetLicenseConfigurationResponseTagsTypeDef(
    _ClientGetLicenseConfigurationResponseTagsTypeDef
):
    """
    Type definition for `ClientGetLicenseConfigurationResponse` `Tags`

    Tag for a resource in a key-value format.

    - **Key** *(string) --*

      Key for the resource tag.

    - **Value** *(string) --*

      Value for the resource tag.
    """


_ClientGetLicenseConfigurationResponseTypeDef = TypedDict(
    "_ClientGetLicenseConfigurationResponseTypeDef",
    {
        "LicenseConfigurationId": str,
        "LicenseConfigurationArn": str,
        "Name": str,
        "Description": str,
        "LicenseCountingType": str,
        "LicenseRules": List[str],
        "LicenseCount": int,
        "LicenseCountHardLimit": bool,
        "ConsumedLicenses": int,
        "Status": str,
        "OwnerAccountId": str,
        "ConsumedLicenseSummaryList": List[
            ClientGetLicenseConfigurationResponseConsumedLicenseSummaryListTypeDef
        ],
        "ManagedResourceSummaryList": List[
            ClientGetLicenseConfigurationResponseManagedResourceSummaryListTypeDef
        ],
        "Tags": List[ClientGetLicenseConfigurationResponseTagsTypeDef],
    },
    total=False,
)


class ClientGetLicenseConfigurationResponseTypeDef(
    _ClientGetLicenseConfigurationResponseTypeDef
):
    """
    Type definition for `ClientGetLicenseConfiguration` `Response`

    - **LicenseConfigurationId** *(string) --*

      Unique ID for the license configuration.

    - **LicenseConfigurationArn** *(string) --*

      ARN of the license configuration requested.

    - **Name** *(string) --*

      Name of the license configuration.

    - **Description** *(string) --*

      Description of the license configuration.

    - **LicenseCountingType** *(string) --*

      Dimension on which the licenses are counted (for example, instances, cores, sockets, or
      VCPUs).

    - **LicenseRules** *(list) --*

      List of flexible text strings designating license rules.

      - *(string) --*

    - **LicenseCount** *(integer) --*

      Number of available licenses.

    - **LicenseCountHardLimit** *(boolean) --*

      Sets the number of available licenses as a hard limit.

    - **ConsumedLicenses** *(integer) --*

      Number of licenses assigned to resources.

    - **Status** *(string) --*

      License configuration status (active, etc.).

    - **OwnerAccountId** *(string) --*

      Owner account ID for the license configuration.

    - **ConsumedLicenseSummaryList** *(list) --*

      List of summaries for consumed licenses used by various resources.

      - *(dict) --*

        Details about license consumption.

        - **ResourceType** *(string) --*

          Resource type of the resource consuming a license (instance, host, or AMI).

        - **ConsumedLicenses** *(integer) --*

          Number of licenses consumed by a resource.

    - **ManagedResourceSummaryList** *(list) --*

      List of summaries of managed resources.

      - *(dict) --*

        Summary for a resource.

        - **ResourceType** *(string) --*

          Type of resource associated with a license (instance, host, or AMI).

        - **AssociationCount** *(integer) --*

          Number of resources associated with licenses.

    - **Tags** *(list) --*

      List of tags attached to the license configuration.

      - *(dict) --*

        Tag for a resource in a key-value format.

        - **Key** *(string) --*

          Key for the resource tag.

        - **Value** *(string) --*

          Value for the resource tag.
    """


_ClientGetServiceSettingsResponseOrganizationConfigurationTypeDef = TypedDict(
    "_ClientGetServiceSettingsResponseOrganizationConfigurationTypeDef",
    {"EnableIntegration": bool},
    total=False,
)


class ClientGetServiceSettingsResponseOrganizationConfigurationTypeDef(
    _ClientGetServiceSettingsResponseOrganizationConfigurationTypeDef
):
    """
    Type definition for `ClientGetServiceSettingsResponse` `OrganizationConfiguration`

    Indicates whether AWS Organizations has been integrated with License Manager for
    cross-account discovery.

    - **EnableIntegration** *(boolean) --*

      Flag to activate AWS Organization integration.
    """


_ClientGetServiceSettingsResponseTypeDef = TypedDict(
    "_ClientGetServiceSettingsResponseTypeDef",
    {
        "S3BucketArn": str,
        "SnsTopicArn": str,
        "OrganizationConfiguration": ClientGetServiceSettingsResponseOrganizationConfigurationTypeDef,
        "EnableCrossAccountsDiscovery": bool,
    },
    total=False,
)


class ClientGetServiceSettingsResponseTypeDef(_ClientGetServiceSettingsResponseTypeDef):
    """
    Type definition for `ClientGetServiceSettings` `Response`

    - **S3BucketArn** *(string) --*

      Regional S3 bucket path for storing reports, license trail event data, discovery data, etc.

    - **SnsTopicArn** *(string) --*

      SNS topic configured to receive notifications from License Manager.

    - **OrganizationConfiguration** *(dict) --*

      Indicates whether AWS Organizations has been integrated with License Manager for
      cross-account discovery.

      - **EnableIntegration** *(boolean) --*

        Flag to activate AWS Organization integration.

    - **EnableCrossAccountsDiscovery** *(boolean) --*

      Indicates whether cross-account discovery has been enabled.
    """


_ClientListAssociationsForLicenseConfigurationResponseLicenseConfigurationAssociationsTypeDef = TypedDict(
    "_ClientListAssociationsForLicenseConfigurationResponseLicenseConfigurationAssociationsTypeDef",
    {
        "ResourceArn": str,
        "ResourceType": str,
        "ResourceOwnerId": str,
        "AssociationTime": datetime,
    },
    total=False,
)


class ClientListAssociationsForLicenseConfigurationResponseLicenseConfigurationAssociationsTypeDef(
    _ClientListAssociationsForLicenseConfigurationResponseLicenseConfigurationAssociationsTypeDef
):
    """
    Type definition for `ClientListAssociationsForLicenseConfigurationResponse` `LicenseConfigurationAssociations`

    Describes a server resource that is associated with a license configuration.

    - **ResourceArn** *(string) --*

      ARN of the resource associated with the license configuration.

    - **ResourceType** *(string) --*

      Type of server resource.

    - **ResourceOwnerId** *(string) --*

      ID of the AWS account that owns the resource consuming licenses.

    - **AssociationTime** *(datetime) --*

      Time when the license configuration was associated with the resource.
    """


_ClientListAssociationsForLicenseConfigurationResponseTypeDef = TypedDict(
    "_ClientListAssociationsForLicenseConfigurationResponseTypeDef",
    {
        "LicenseConfigurationAssociations": List[
            ClientListAssociationsForLicenseConfigurationResponseLicenseConfigurationAssociationsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListAssociationsForLicenseConfigurationResponseTypeDef(
    _ClientListAssociationsForLicenseConfigurationResponseTypeDef
):
    """
    Type definition for `ClientListAssociationsForLicenseConfiguration` `Response`

    - **LicenseConfigurationAssociations** *(list) --*

      Lists association objects for the license configuration, each containing the association
      time, number of consumed licenses, resource ARN, resource ID, account ID that owns the
      resource, resource size, and resource type.

      - *(dict) --*

        Describes a server resource that is associated with a license configuration.

        - **ResourceArn** *(string) --*

          ARN of the resource associated with the license configuration.

        - **ResourceType** *(string) --*

          Type of server resource.

        - **ResourceOwnerId** *(string) --*

          ID of the AWS account that owns the resource consuming licenses.

        - **AssociationTime** *(datetime) --*

          Time when the license configuration was associated with the resource.

    - **NextToken** *(string) --*

      Token for the next set of results.
    """


_ClientListLicenseConfigurationsFiltersTypeDef = TypedDict(
    "_ClientListLicenseConfigurationsFiltersTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)


class ClientListLicenseConfigurationsFiltersTypeDef(
    _ClientListLicenseConfigurationsFiltersTypeDef
):
    """
    Type definition for `ClientListLicenseConfigurations` `Filters`

    A filter name and value pair that is used to return a more specific list of results from a
    describe operation. Filters can be used to match a set of resources by specific criteria, such
    as tags, attributes, or IDs. The filters supported by a ``Describe`` operation are documented
    with the ``Describe`` operation.

    - **Name** *(string) --*

      Name of the filter. Filter names are case-sensitive.

    - **Values** *(list) --*

      One or more filter values. Filter values are case-sensitive.

      - *(string) --*
    """


_ClientListLicenseConfigurationsResponseLicenseConfigurationsConsumedLicenseSummaryListTypeDef = TypedDict(
    "_ClientListLicenseConfigurationsResponseLicenseConfigurationsConsumedLicenseSummaryListTypeDef",
    {"ResourceType": str, "ConsumedLicenses": int},
    total=False,
)


class ClientListLicenseConfigurationsResponseLicenseConfigurationsConsumedLicenseSummaryListTypeDef(
    _ClientListLicenseConfigurationsResponseLicenseConfigurationsConsumedLicenseSummaryListTypeDef
):
    """
    Type definition for `ClientListLicenseConfigurationsResponseLicenseConfigurations` `ConsumedLicenseSummaryList`

    Details about license consumption.

    - **ResourceType** *(string) --*

      Resource type of the resource consuming a license (instance, host, or AMI).

    - **ConsumedLicenses** *(integer) --*

      Number of licenses consumed by a resource.
    """


_ClientListLicenseConfigurationsResponseLicenseConfigurationsManagedResourceSummaryListTypeDef = TypedDict(
    "_ClientListLicenseConfigurationsResponseLicenseConfigurationsManagedResourceSummaryListTypeDef",
    {"ResourceType": str, "AssociationCount": int},
    total=False,
)


class ClientListLicenseConfigurationsResponseLicenseConfigurationsManagedResourceSummaryListTypeDef(
    _ClientListLicenseConfigurationsResponseLicenseConfigurationsManagedResourceSummaryListTypeDef
):
    """
    Type definition for `ClientListLicenseConfigurationsResponseLicenseConfigurations` `ManagedResourceSummaryList`

    Summary for a resource.

    - **ResourceType** *(string) --*

      Type of resource associated with a license (instance, host, or AMI).

    - **AssociationCount** *(integer) --*

      Number of resources associated with licenses.
    """


_ClientListLicenseConfigurationsResponseLicenseConfigurationsTypeDef = TypedDict(
    "_ClientListLicenseConfigurationsResponseLicenseConfigurationsTypeDef",
    {
        "LicenseConfigurationId": str,
        "LicenseConfigurationArn": str,
        "Name": str,
        "Description": str,
        "LicenseCountingType": str,
        "LicenseRules": List[str],
        "LicenseCount": int,
        "LicenseCountHardLimit": bool,
        "ConsumedLicenses": int,
        "Status": str,
        "OwnerAccountId": str,
        "ConsumedLicenseSummaryList": List[
            ClientListLicenseConfigurationsResponseLicenseConfigurationsConsumedLicenseSummaryListTypeDef
        ],
        "ManagedResourceSummaryList": List[
            ClientListLicenseConfigurationsResponseLicenseConfigurationsManagedResourceSummaryListTypeDef
        ],
    },
    total=False,
)


class ClientListLicenseConfigurationsResponseLicenseConfigurationsTypeDef(
    _ClientListLicenseConfigurationsResponseLicenseConfigurationsTypeDef
):
    """
    Type definition for `ClientListLicenseConfigurationsResponse` `LicenseConfigurations`

    A license configuration is an abstraction of a customer license agreement that can be
    consumed and enforced by License Manager. Components include specifications for the license
    type (licensing by instance, socket, CPU, or VCPU), tenancy (shared tenancy, Amazon EC2
    Dedicated Instance, Amazon EC2 Dedicated Host, or any of these), host affinity (how long a
    VM must be associated with a host), the number of licenses purchased and used.

    - **LicenseConfigurationId** *(string) --*

      Unique ID of the ``LicenseConfiguration`` object.

    - **LicenseConfigurationArn** *(string) --*

      ARN of the ``LicenseConfiguration`` object.

    - **Name** *(string) --*

      Name of the license configuration.

    - **Description** *(string) --*

      Description of the license configuration.

    - **LicenseCountingType** *(string) --*

      Dimension to use to track license inventory.

    - **LicenseRules** *(list) --*

      Array of configured License Manager rules.

      - *(string) --*

    - **LicenseCount** *(integer) --*

      Number of licenses managed by the license configuration.

    - **LicenseCountHardLimit** *(boolean) --*

      Sets the number of available licenses as a hard limit.

    - **ConsumedLicenses** *(integer) --*

      Number of licenses consumed.

    - **Status** *(string) --*

      Status of the license configuration.

    - **OwnerAccountId** *(string) --*

      Account ID of the license configuration's owner.

    - **ConsumedLicenseSummaryList** *(list) --*

      List of summaries for licenses consumed by various resources.

      - *(dict) --*

        Details about license consumption.

        - **ResourceType** *(string) --*

          Resource type of the resource consuming a license (instance, host, or AMI).

        - **ConsumedLicenses** *(integer) --*

          Number of licenses consumed by a resource.

    - **ManagedResourceSummaryList** *(list) --*

      List of summaries for managed resources.

      - *(dict) --*

        Summary for a resource.

        - **ResourceType** *(string) --*

          Type of resource associated with a license (instance, host, or AMI).

        - **AssociationCount** *(integer) --*

          Number of resources associated with licenses.
    """


_ClientListLicenseConfigurationsResponseTypeDef = TypedDict(
    "_ClientListLicenseConfigurationsResponseTypeDef",
    {
        "LicenseConfigurations": List[
            ClientListLicenseConfigurationsResponseLicenseConfigurationsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListLicenseConfigurationsResponseTypeDef(
    _ClientListLicenseConfigurationsResponseTypeDef
):
    """
    Type definition for `ClientListLicenseConfigurations` `Response`

    - **LicenseConfigurations** *(list) --*

      Array of license configuration objects.

      - *(dict) --*

        A license configuration is an abstraction of a customer license agreement that can be
        consumed and enforced by License Manager. Components include specifications for the license
        type (licensing by instance, socket, CPU, or VCPU), tenancy (shared tenancy, Amazon EC2
        Dedicated Instance, Amazon EC2 Dedicated Host, or any of these), host affinity (how long a
        VM must be associated with a host), the number of licenses purchased and used.

        - **LicenseConfigurationId** *(string) --*

          Unique ID of the ``LicenseConfiguration`` object.

        - **LicenseConfigurationArn** *(string) --*

          ARN of the ``LicenseConfiguration`` object.

        - **Name** *(string) --*

          Name of the license configuration.

        - **Description** *(string) --*

          Description of the license configuration.

        - **LicenseCountingType** *(string) --*

          Dimension to use to track license inventory.

        - **LicenseRules** *(list) --*

          Array of configured License Manager rules.

          - *(string) --*

        - **LicenseCount** *(integer) --*

          Number of licenses managed by the license configuration.

        - **LicenseCountHardLimit** *(boolean) --*

          Sets the number of available licenses as a hard limit.

        - **ConsumedLicenses** *(integer) --*

          Number of licenses consumed.

        - **Status** *(string) --*

          Status of the license configuration.

        - **OwnerAccountId** *(string) --*

          Account ID of the license configuration's owner.

        - **ConsumedLicenseSummaryList** *(list) --*

          List of summaries for licenses consumed by various resources.

          - *(dict) --*

            Details about license consumption.

            - **ResourceType** *(string) --*

              Resource type of the resource consuming a license (instance, host, or AMI).

            - **ConsumedLicenses** *(integer) --*

              Number of licenses consumed by a resource.

        - **ManagedResourceSummaryList** *(list) --*

          List of summaries for managed resources.

          - *(dict) --*

            Summary for a resource.

            - **ResourceType** *(string) --*

              Type of resource associated with a license (instance, host, or AMI).

            - **AssociationCount** *(integer) --*

              Number of resources associated with licenses.

    - **NextToken** *(string) --*

      Token for the next set of results.
    """


_ClientListLicenseSpecificationsForResourceResponseLicenseSpecificationsTypeDef = TypedDict(
    "_ClientListLicenseSpecificationsForResourceResponseLicenseSpecificationsTypeDef",
    {"LicenseConfigurationArn": str},
    total=False,
)


class ClientListLicenseSpecificationsForResourceResponseLicenseSpecificationsTypeDef(
    _ClientListLicenseSpecificationsForResourceResponseLicenseSpecificationsTypeDef
):
    """
    Type definition for `ClientListLicenseSpecificationsForResourceResponse` `LicenseSpecifications`

    Object used for associating a license configuration with a resource.

    - **LicenseConfigurationArn** *(string) --*

      ARN of the ``LicenseConfiguration`` object.
    """


_ClientListLicenseSpecificationsForResourceResponseTypeDef = TypedDict(
    "_ClientListLicenseSpecificationsForResourceResponseTypeDef",
    {
        "LicenseSpecifications": List[
            ClientListLicenseSpecificationsForResourceResponseLicenseSpecificationsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListLicenseSpecificationsForResourceResponseTypeDef(
    _ClientListLicenseSpecificationsForResourceResponseTypeDef
):
    """
    Type definition for `ClientListLicenseSpecificationsForResource` `Response`

    - **LicenseSpecifications** *(list) --*

      License configurations associated with a resource.

      - *(dict) --*

        Object used for associating a license configuration with a resource.

        - **LicenseConfigurationArn** *(string) --*

          ARN of the ``LicenseConfiguration`` object.

    - **NextToken** *(string) --*

      Token for the next set of results.
    """


_RequiredClientListResourceInventoryFiltersTypeDef = TypedDict(
    "_RequiredClientListResourceInventoryFiltersTypeDef",
    {"Name": str, "Condition": str},
)
_OptionalClientListResourceInventoryFiltersTypeDef = TypedDict(
    "_OptionalClientListResourceInventoryFiltersTypeDef", {"Value": str}, total=False
)


class ClientListResourceInventoryFiltersTypeDef(
    _RequiredClientListResourceInventoryFiltersTypeDef,
    _OptionalClientListResourceInventoryFiltersTypeDef,
):
    """
    Type definition for `ClientListResourceInventory` `Filters`

    An inventory filter object.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the filter.

    - **Condition** *(string) --* **[REQUIRED]**

      The condition of the filter.

    - **Value** *(string) --*

      Value of the filter.
    """


_ClientListResourceInventoryResponseResourceInventoryListTypeDef = TypedDict(
    "_ClientListResourceInventoryResponseResourceInventoryListTypeDef",
    {
        "ResourceId": str,
        "ResourceType": str,
        "ResourceArn": str,
        "Platform": str,
        "PlatformVersion": str,
        "ResourceOwningAccountId": str,
    },
    total=False,
)


class ClientListResourceInventoryResponseResourceInventoryListTypeDef(
    _ClientListResourceInventoryResponseResourceInventoryListTypeDef
):
    """
    Type definition for `ClientListResourceInventoryResponse` `ResourceInventoryList`

    A set of attributes that describe a resource.

    - **ResourceId** *(string) --*

      Unique ID of the resource.

    - **ResourceType** *(string) --*

      The type of resource.

    - **ResourceArn** *(string) --*

      The ARN of the resource.

    - **Platform** *(string) --*

      The platform of the resource.

    - **PlatformVersion** *(string) --*

      Platform version of the resource in the inventory.

    - **ResourceOwningAccountId** *(string) --*

      Unique ID of the account that owns the resource.
    """


_ClientListResourceInventoryResponseTypeDef = TypedDict(
    "_ClientListResourceInventoryResponseTypeDef",
    {
        "ResourceInventoryList": List[
            ClientListResourceInventoryResponseResourceInventoryListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListResourceInventoryResponseTypeDef(
    _ClientListResourceInventoryResponseTypeDef
):
    """
    Type definition for `ClientListResourceInventory` `Response`

    - **ResourceInventoryList** *(list) --*

      The detailed list of resources.

      - *(dict) --*

        A set of attributes that describe a resource.

        - **ResourceId** *(string) --*

          Unique ID of the resource.

        - **ResourceType** *(string) --*

          The type of resource.

        - **ResourceArn** *(string) --*

          The ARN of the resource.

        - **Platform** *(string) --*

          The platform of the resource.

        - **PlatformVersion** *(string) --*

          Platform version of the resource in the inventory.

        - **ResourceOwningAccountId** *(string) --*

          Unique ID of the account that owns the resource.

    - **NextToken** *(string) --*

      Token for the next set of results.
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

    Tag for a resource in a key-value format.

    - **Key** *(string) --*

      Key for the resource tag.

    - **Value** *(string) --*

      Value for the resource tag.
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

      List of tags attached to the resource.

      - *(dict) --*

        Tag for a resource in a key-value format.

        - **Key** *(string) --*

          Key for the resource tag.

        - **Value** *(string) --*

          Value for the resource tag.
    """


_ClientListUsageForLicenseConfigurationFiltersTypeDef = TypedDict(
    "_ClientListUsageForLicenseConfigurationFiltersTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)


class ClientListUsageForLicenseConfigurationFiltersTypeDef(
    _ClientListUsageForLicenseConfigurationFiltersTypeDef
):
    """
    Type definition for `ClientListUsageForLicenseConfiguration` `Filters`

    A filter name and value pair that is used to return a more specific list of results from a
    describe operation. Filters can be used to match a set of resources by specific criteria, such
    as tags, attributes, or IDs. The filters supported by a ``Describe`` operation are documented
    with the ``Describe`` operation.

    - **Name** *(string) --*

      Name of the filter. Filter names are case-sensitive.

    - **Values** *(list) --*

      One or more filter values. Filter values are case-sensitive.

      - *(string) --*
    """


_ClientListUsageForLicenseConfigurationResponseLicenseConfigurationUsageListTypeDef = TypedDict(
    "_ClientListUsageForLicenseConfigurationResponseLicenseConfigurationUsageListTypeDef",
    {
        "ResourceArn": str,
        "ResourceType": str,
        "ResourceStatus": str,
        "ResourceOwnerId": str,
        "AssociationTime": datetime,
        "ConsumedLicenses": int,
    },
    total=False,
)


class ClientListUsageForLicenseConfigurationResponseLicenseConfigurationUsageListTypeDef(
    _ClientListUsageForLicenseConfigurationResponseLicenseConfigurationUsageListTypeDef
):
    """
    Type definition for `ClientListUsageForLicenseConfigurationResponse` `LicenseConfigurationUsageList`

    Contains details of the usage of each resource from the license pool.

    - **ResourceArn** *(string) --*

      ARN of the resource associated with a license configuration.

    - **ResourceType** *(string) --*

      Type of resource associated with athe license configuration.

    - **ResourceStatus** *(string) --*

      Status of a resource associated with the license configuration.

    - **ResourceOwnerId** *(string) --*

      ID of the account that owns a resource that is associated with the license configuration.

    - **AssociationTime** *(datetime) --*

      Time when the license configuration was initially associated with a resource.

    - **ConsumedLicenses** *(integer) --*

      Number of licenses consumed out of the total provisioned in the license configuration.
    """


_ClientListUsageForLicenseConfigurationResponseTypeDef = TypedDict(
    "_ClientListUsageForLicenseConfigurationResponseTypeDef",
    {
        "LicenseConfigurationUsageList": List[
            ClientListUsageForLicenseConfigurationResponseLicenseConfigurationUsageListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListUsageForLicenseConfigurationResponseTypeDef(
    _ClientListUsageForLicenseConfigurationResponseTypeDef
):
    """
    Type definition for `ClientListUsageForLicenseConfiguration` `Response`

    - **LicenseConfigurationUsageList** *(list) --*

      An array of ``LicenseConfigurationUsage`` objects.

      - *(dict) --*

        Contains details of the usage of each resource from the license pool.

        - **ResourceArn** *(string) --*

          ARN of the resource associated with a license configuration.

        - **ResourceType** *(string) --*

          Type of resource associated with athe license configuration.

        - **ResourceStatus** *(string) --*

          Status of a resource associated with the license configuration.

        - **ResourceOwnerId** *(string) --*

          ID of the account that owns a resource that is associated with the license configuration.

        - **AssociationTime** *(datetime) --*

          Time when the license configuration was initially associated with a resource.

        - **ConsumedLicenses** *(integer) --*

          Number of licenses consumed out of the total provisioned in the license configuration.

    - **NextToken** *(string) --*

      Token for the next set of results.
    """


_ClientTagResourceTagsTypeDef = TypedDict(
    "_ClientTagResourceTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientTagResourceTagsTypeDef(_ClientTagResourceTagsTypeDef):
    """
    Type definition for `ClientTagResource` `Tags`

    Tag for a resource in a key-value format.

    - **Key** *(string) --*

      Key for the resource tag.

    - **Value** *(string) --*

      Value for the resource tag.
    """


_ClientUpdateLicenseSpecificationsForResourceAddLicenseSpecificationsTypeDef = TypedDict(
    "_ClientUpdateLicenseSpecificationsForResourceAddLicenseSpecificationsTypeDef",
    {"LicenseConfigurationArn": str},
)


class ClientUpdateLicenseSpecificationsForResourceAddLicenseSpecificationsTypeDef(
    _ClientUpdateLicenseSpecificationsForResourceAddLicenseSpecificationsTypeDef
):
    """
    Type definition for `ClientUpdateLicenseSpecificationsForResource` `AddLicenseSpecifications`

    Object used for associating a license configuration with a resource.

    - **LicenseConfigurationArn** *(string) --* **[REQUIRED]**

      ARN of the ``LicenseConfiguration`` object.
    """


_ClientUpdateLicenseSpecificationsForResourceRemoveLicenseSpecificationsTypeDef = TypedDict(
    "_ClientUpdateLicenseSpecificationsForResourceRemoveLicenseSpecificationsTypeDef",
    {"LicenseConfigurationArn": str},
)


class ClientUpdateLicenseSpecificationsForResourceRemoveLicenseSpecificationsTypeDef(
    _ClientUpdateLicenseSpecificationsForResourceRemoveLicenseSpecificationsTypeDef
):
    """
    Type definition for `ClientUpdateLicenseSpecificationsForResource` `RemoveLicenseSpecifications`

    Object used for associating a license configuration with a resource.

    - **LicenseConfigurationArn** *(string) --* **[REQUIRED]**

      ARN of the ``LicenseConfiguration`` object.
    """


_ClientUpdateServiceSettingsOrganizationConfigurationTypeDef = TypedDict(
    "_ClientUpdateServiceSettingsOrganizationConfigurationTypeDef",
    {"EnableIntegration": bool},
)


class ClientUpdateServiceSettingsOrganizationConfigurationTypeDef(
    _ClientUpdateServiceSettingsOrganizationConfigurationTypeDef
):
    """
    Type definition for `ClientUpdateServiceSettings` `OrganizationConfiguration`

    Integrates AWS Organizations with License Manager for cross-account discovery.

    - **EnableIntegration** *(boolean) --* **[REQUIRED]**

      Flag to activate AWS Organization integration.
    """


_ListAssociationsForLicenseConfigurationPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAssociationsForLicenseConfigurationPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListAssociationsForLicenseConfigurationPaginatePaginationConfigTypeDef(
    _ListAssociationsForLicenseConfigurationPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListAssociationsForLicenseConfigurationPaginate` `PaginationConfig`

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


_ListAssociationsForLicenseConfigurationPaginateResponseLicenseConfigurationAssociationsTypeDef = TypedDict(
    "_ListAssociationsForLicenseConfigurationPaginateResponseLicenseConfigurationAssociationsTypeDef",
    {
        "ResourceArn": str,
        "ResourceType": str,
        "ResourceOwnerId": str,
        "AssociationTime": datetime,
    },
    total=False,
)


class ListAssociationsForLicenseConfigurationPaginateResponseLicenseConfigurationAssociationsTypeDef(
    _ListAssociationsForLicenseConfigurationPaginateResponseLicenseConfigurationAssociationsTypeDef
):
    """
    Type definition for `ListAssociationsForLicenseConfigurationPaginateResponse` `LicenseConfigurationAssociations`

    Describes a server resource that is associated with a license configuration.

    - **ResourceArn** *(string) --*

      ARN of the resource associated with the license configuration.

    - **ResourceType** *(string) --*

      Type of server resource.

    - **ResourceOwnerId** *(string) --*

      ID of the AWS account that owns the resource consuming licenses.

    - **AssociationTime** *(datetime) --*

      Time when the license configuration was associated with the resource.
    """


_ListAssociationsForLicenseConfigurationPaginateResponseTypeDef = TypedDict(
    "_ListAssociationsForLicenseConfigurationPaginateResponseTypeDef",
    {
        "LicenseConfigurationAssociations": List[
            ListAssociationsForLicenseConfigurationPaginateResponseLicenseConfigurationAssociationsTypeDef
        ]
    },
    total=False,
)


class ListAssociationsForLicenseConfigurationPaginateResponseTypeDef(
    _ListAssociationsForLicenseConfigurationPaginateResponseTypeDef
):
    """
    Type definition for `ListAssociationsForLicenseConfigurationPaginate` `Response`

    - **LicenseConfigurationAssociations** *(list) --*

      Lists association objects for the license configuration, each containing the association
      time, number of consumed licenses, resource ARN, resource ID, account ID that owns the
      resource, resource size, and resource type.

      - *(dict) --*

        Describes a server resource that is associated with a license configuration.

        - **ResourceArn** *(string) --*

          ARN of the resource associated with the license configuration.

        - **ResourceType** *(string) --*

          Type of server resource.

        - **ResourceOwnerId** *(string) --*

          ID of the AWS account that owns the resource consuming licenses.

        - **AssociationTime** *(datetime) --*

          Time when the license configuration was associated with the resource.
    """


_ListLicenseConfigurationsPaginateFiltersTypeDef = TypedDict(
    "_ListLicenseConfigurationsPaginateFiltersTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)


class ListLicenseConfigurationsPaginateFiltersTypeDef(
    _ListLicenseConfigurationsPaginateFiltersTypeDef
):
    """
    Type definition for `ListLicenseConfigurationsPaginate` `Filters`

    A filter name and value pair that is used to return a more specific list of results from a
    describe operation. Filters can be used to match a set of resources by specific criteria, such
    as tags, attributes, or IDs. The filters supported by a ``Describe`` operation are documented
    with the ``Describe`` operation.

    - **Name** *(string) --*

      Name of the filter. Filter names are case-sensitive.

    - **Values** *(list) --*

      One or more filter values. Filter values are case-sensitive.

      - *(string) --*
    """


_ListLicenseConfigurationsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListLicenseConfigurationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListLicenseConfigurationsPaginatePaginationConfigTypeDef(
    _ListLicenseConfigurationsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListLicenseConfigurationsPaginate` `PaginationConfig`

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


_ListLicenseConfigurationsPaginateResponseLicenseConfigurationsConsumedLicenseSummaryListTypeDef = TypedDict(
    "_ListLicenseConfigurationsPaginateResponseLicenseConfigurationsConsumedLicenseSummaryListTypeDef",
    {"ResourceType": str, "ConsumedLicenses": int},
    total=False,
)


class ListLicenseConfigurationsPaginateResponseLicenseConfigurationsConsumedLicenseSummaryListTypeDef(
    _ListLicenseConfigurationsPaginateResponseLicenseConfigurationsConsumedLicenseSummaryListTypeDef
):
    """
    Type definition for `ListLicenseConfigurationsPaginateResponseLicenseConfigurations` `ConsumedLicenseSummaryList`

    Details about license consumption.

    - **ResourceType** *(string) --*

      Resource type of the resource consuming a license (instance, host, or AMI).

    - **ConsumedLicenses** *(integer) --*

      Number of licenses consumed by a resource.
    """


_ListLicenseConfigurationsPaginateResponseLicenseConfigurationsManagedResourceSummaryListTypeDef = TypedDict(
    "_ListLicenseConfigurationsPaginateResponseLicenseConfigurationsManagedResourceSummaryListTypeDef",
    {"ResourceType": str, "AssociationCount": int},
    total=False,
)


class ListLicenseConfigurationsPaginateResponseLicenseConfigurationsManagedResourceSummaryListTypeDef(
    _ListLicenseConfigurationsPaginateResponseLicenseConfigurationsManagedResourceSummaryListTypeDef
):
    """
    Type definition for `ListLicenseConfigurationsPaginateResponseLicenseConfigurations` `ManagedResourceSummaryList`

    Summary for a resource.

    - **ResourceType** *(string) --*

      Type of resource associated with a license (instance, host, or AMI).

    - **AssociationCount** *(integer) --*

      Number of resources associated with licenses.
    """


_ListLicenseConfigurationsPaginateResponseLicenseConfigurationsTypeDef = TypedDict(
    "_ListLicenseConfigurationsPaginateResponseLicenseConfigurationsTypeDef",
    {
        "LicenseConfigurationId": str,
        "LicenseConfigurationArn": str,
        "Name": str,
        "Description": str,
        "LicenseCountingType": str,
        "LicenseRules": List[str],
        "LicenseCount": int,
        "LicenseCountHardLimit": bool,
        "ConsumedLicenses": int,
        "Status": str,
        "OwnerAccountId": str,
        "ConsumedLicenseSummaryList": List[
            ListLicenseConfigurationsPaginateResponseLicenseConfigurationsConsumedLicenseSummaryListTypeDef
        ],
        "ManagedResourceSummaryList": List[
            ListLicenseConfigurationsPaginateResponseLicenseConfigurationsManagedResourceSummaryListTypeDef
        ],
    },
    total=False,
)


class ListLicenseConfigurationsPaginateResponseLicenseConfigurationsTypeDef(
    _ListLicenseConfigurationsPaginateResponseLicenseConfigurationsTypeDef
):
    """
    Type definition for `ListLicenseConfigurationsPaginateResponse` `LicenseConfigurations`

    A license configuration is an abstraction of a customer license agreement that can be
    consumed and enforced by License Manager. Components include specifications for the license
    type (licensing by instance, socket, CPU, or VCPU), tenancy (shared tenancy, Amazon EC2
    Dedicated Instance, Amazon EC2 Dedicated Host, or any of these), host affinity (how long a
    VM must be associated with a host), the number of licenses purchased and used.

    - **LicenseConfigurationId** *(string) --*

      Unique ID of the ``LicenseConfiguration`` object.

    - **LicenseConfigurationArn** *(string) --*

      ARN of the ``LicenseConfiguration`` object.

    - **Name** *(string) --*

      Name of the license configuration.

    - **Description** *(string) --*

      Description of the license configuration.

    - **LicenseCountingType** *(string) --*

      Dimension to use to track license inventory.

    - **LicenseRules** *(list) --*

      Array of configured License Manager rules.

      - *(string) --*

    - **LicenseCount** *(integer) --*

      Number of licenses managed by the license configuration.

    - **LicenseCountHardLimit** *(boolean) --*

      Sets the number of available licenses as a hard limit.

    - **ConsumedLicenses** *(integer) --*

      Number of licenses consumed.

    - **Status** *(string) --*

      Status of the license configuration.

    - **OwnerAccountId** *(string) --*

      Account ID of the license configuration's owner.

    - **ConsumedLicenseSummaryList** *(list) --*

      List of summaries for licenses consumed by various resources.

      - *(dict) --*

        Details about license consumption.

        - **ResourceType** *(string) --*

          Resource type of the resource consuming a license (instance, host, or AMI).

        - **ConsumedLicenses** *(integer) --*

          Number of licenses consumed by a resource.

    - **ManagedResourceSummaryList** *(list) --*

      List of summaries for managed resources.

      - *(dict) --*

        Summary for a resource.

        - **ResourceType** *(string) --*

          Type of resource associated with a license (instance, host, or AMI).

        - **AssociationCount** *(integer) --*

          Number of resources associated with licenses.
    """


_ListLicenseConfigurationsPaginateResponseTypeDef = TypedDict(
    "_ListLicenseConfigurationsPaginateResponseTypeDef",
    {
        "LicenseConfigurations": List[
            ListLicenseConfigurationsPaginateResponseLicenseConfigurationsTypeDef
        ]
    },
    total=False,
)


class ListLicenseConfigurationsPaginateResponseTypeDef(
    _ListLicenseConfigurationsPaginateResponseTypeDef
):
    """
    Type definition for `ListLicenseConfigurationsPaginate` `Response`

    - **LicenseConfigurations** *(list) --*

      Array of license configuration objects.

      - *(dict) --*

        A license configuration is an abstraction of a customer license agreement that can be
        consumed and enforced by License Manager. Components include specifications for the license
        type (licensing by instance, socket, CPU, or VCPU), tenancy (shared tenancy, Amazon EC2
        Dedicated Instance, Amazon EC2 Dedicated Host, or any of these), host affinity (how long a
        VM must be associated with a host), the number of licenses purchased and used.

        - **LicenseConfigurationId** *(string) --*

          Unique ID of the ``LicenseConfiguration`` object.

        - **LicenseConfigurationArn** *(string) --*

          ARN of the ``LicenseConfiguration`` object.

        - **Name** *(string) --*

          Name of the license configuration.

        - **Description** *(string) --*

          Description of the license configuration.

        - **LicenseCountingType** *(string) --*

          Dimension to use to track license inventory.

        - **LicenseRules** *(list) --*

          Array of configured License Manager rules.

          - *(string) --*

        - **LicenseCount** *(integer) --*

          Number of licenses managed by the license configuration.

        - **LicenseCountHardLimit** *(boolean) --*

          Sets the number of available licenses as a hard limit.

        - **ConsumedLicenses** *(integer) --*

          Number of licenses consumed.

        - **Status** *(string) --*

          Status of the license configuration.

        - **OwnerAccountId** *(string) --*

          Account ID of the license configuration's owner.

        - **ConsumedLicenseSummaryList** *(list) --*

          List of summaries for licenses consumed by various resources.

          - *(dict) --*

            Details about license consumption.

            - **ResourceType** *(string) --*

              Resource type of the resource consuming a license (instance, host, or AMI).

            - **ConsumedLicenses** *(integer) --*

              Number of licenses consumed by a resource.

        - **ManagedResourceSummaryList** *(list) --*

          List of summaries for managed resources.

          - *(dict) --*

            Summary for a resource.

            - **ResourceType** *(string) --*

              Type of resource associated with a license (instance, host, or AMI).

            - **AssociationCount** *(integer) --*

              Number of resources associated with licenses.
    """


_ListLicenseSpecificationsForResourcePaginatePaginationConfigTypeDef = TypedDict(
    "_ListLicenseSpecificationsForResourcePaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListLicenseSpecificationsForResourcePaginatePaginationConfigTypeDef(
    _ListLicenseSpecificationsForResourcePaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListLicenseSpecificationsForResourcePaginate` `PaginationConfig`

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


_ListLicenseSpecificationsForResourcePaginateResponseLicenseSpecificationsTypeDef = TypedDict(
    "_ListLicenseSpecificationsForResourcePaginateResponseLicenseSpecificationsTypeDef",
    {"LicenseConfigurationArn": str},
    total=False,
)


class ListLicenseSpecificationsForResourcePaginateResponseLicenseSpecificationsTypeDef(
    _ListLicenseSpecificationsForResourcePaginateResponseLicenseSpecificationsTypeDef
):
    """
    Type definition for `ListLicenseSpecificationsForResourcePaginateResponse` `LicenseSpecifications`

    Object used for associating a license configuration with a resource.

    - **LicenseConfigurationArn** *(string) --*

      ARN of the ``LicenseConfiguration`` object.
    """


_ListLicenseSpecificationsForResourcePaginateResponseTypeDef = TypedDict(
    "_ListLicenseSpecificationsForResourcePaginateResponseTypeDef",
    {
        "LicenseSpecifications": List[
            ListLicenseSpecificationsForResourcePaginateResponseLicenseSpecificationsTypeDef
        ]
    },
    total=False,
)


class ListLicenseSpecificationsForResourcePaginateResponseTypeDef(
    _ListLicenseSpecificationsForResourcePaginateResponseTypeDef
):
    """
    Type definition for `ListLicenseSpecificationsForResourcePaginate` `Response`

    - **LicenseSpecifications** *(list) --*

      License configurations associated with a resource.

      - *(dict) --*

        Object used for associating a license configuration with a resource.

        - **LicenseConfigurationArn** *(string) --*

          ARN of the ``LicenseConfiguration`` object.
    """


_RequiredListResourceInventoryPaginateFiltersTypeDef = TypedDict(
    "_RequiredListResourceInventoryPaginateFiltersTypeDef",
    {"Name": str, "Condition": str},
)
_OptionalListResourceInventoryPaginateFiltersTypeDef = TypedDict(
    "_OptionalListResourceInventoryPaginateFiltersTypeDef", {"Value": str}, total=False
)


class ListResourceInventoryPaginateFiltersTypeDef(
    _RequiredListResourceInventoryPaginateFiltersTypeDef,
    _OptionalListResourceInventoryPaginateFiltersTypeDef,
):
    """
    Type definition for `ListResourceInventoryPaginate` `Filters`

    An inventory filter object.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the filter.

    - **Condition** *(string) --* **[REQUIRED]**

      The condition of the filter.

    - **Value** *(string) --*

      Value of the filter.
    """


_ListResourceInventoryPaginatePaginationConfigTypeDef = TypedDict(
    "_ListResourceInventoryPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListResourceInventoryPaginatePaginationConfigTypeDef(
    _ListResourceInventoryPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListResourceInventoryPaginate` `PaginationConfig`

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


_ListResourceInventoryPaginateResponseResourceInventoryListTypeDef = TypedDict(
    "_ListResourceInventoryPaginateResponseResourceInventoryListTypeDef",
    {
        "ResourceId": str,
        "ResourceType": str,
        "ResourceArn": str,
        "Platform": str,
        "PlatformVersion": str,
        "ResourceOwningAccountId": str,
    },
    total=False,
)


class ListResourceInventoryPaginateResponseResourceInventoryListTypeDef(
    _ListResourceInventoryPaginateResponseResourceInventoryListTypeDef
):
    """
    Type definition for `ListResourceInventoryPaginateResponse` `ResourceInventoryList`

    A set of attributes that describe a resource.

    - **ResourceId** *(string) --*

      Unique ID of the resource.

    - **ResourceType** *(string) --*

      The type of resource.

    - **ResourceArn** *(string) --*

      The ARN of the resource.

    - **Platform** *(string) --*

      The platform of the resource.

    - **PlatformVersion** *(string) --*

      Platform version of the resource in the inventory.

    - **ResourceOwningAccountId** *(string) --*

      Unique ID of the account that owns the resource.
    """


_ListResourceInventoryPaginateResponseTypeDef = TypedDict(
    "_ListResourceInventoryPaginateResponseTypeDef",
    {
        "ResourceInventoryList": List[
            ListResourceInventoryPaginateResponseResourceInventoryListTypeDef
        ]
    },
    total=False,
)


class ListResourceInventoryPaginateResponseTypeDef(
    _ListResourceInventoryPaginateResponseTypeDef
):
    """
    Type definition for `ListResourceInventoryPaginate` `Response`

    - **ResourceInventoryList** *(list) --*

      The detailed list of resources.

      - *(dict) --*

        A set of attributes that describe a resource.

        - **ResourceId** *(string) --*

          Unique ID of the resource.

        - **ResourceType** *(string) --*

          The type of resource.

        - **ResourceArn** *(string) --*

          The ARN of the resource.

        - **Platform** *(string) --*

          The platform of the resource.

        - **PlatformVersion** *(string) --*

          Platform version of the resource in the inventory.

        - **ResourceOwningAccountId** *(string) --*

          Unique ID of the account that owns the resource.
    """


_ListUsageForLicenseConfigurationPaginateFiltersTypeDef = TypedDict(
    "_ListUsageForLicenseConfigurationPaginateFiltersTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)


class ListUsageForLicenseConfigurationPaginateFiltersTypeDef(
    _ListUsageForLicenseConfigurationPaginateFiltersTypeDef
):
    """
    Type definition for `ListUsageForLicenseConfigurationPaginate` `Filters`

    A filter name and value pair that is used to return a more specific list of results from a
    describe operation. Filters can be used to match a set of resources by specific criteria, such
    as tags, attributes, or IDs. The filters supported by a ``Describe`` operation are documented
    with the ``Describe`` operation.

    - **Name** *(string) --*

      Name of the filter. Filter names are case-sensitive.

    - **Values** *(list) --*

      One or more filter values. Filter values are case-sensitive.

      - *(string) --*
    """


_ListUsageForLicenseConfigurationPaginatePaginationConfigTypeDef = TypedDict(
    "_ListUsageForLicenseConfigurationPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListUsageForLicenseConfigurationPaginatePaginationConfigTypeDef(
    _ListUsageForLicenseConfigurationPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListUsageForLicenseConfigurationPaginate` `PaginationConfig`

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


_ListUsageForLicenseConfigurationPaginateResponseLicenseConfigurationUsageListTypeDef = TypedDict(
    "_ListUsageForLicenseConfigurationPaginateResponseLicenseConfigurationUsageListTypeDef",
    {
        "ResourceArn": str,
        "ResourceType": str,
        "ResourceStatus": str,
        "ResourceOwnerId": str,
        "AssociationTime": datetime,
        "ConsumedLicenses": int,
    },
    total=False,
)


class ListUsageForLicenseConfigurationPaginateResponseLicenseConfigurationUsageListTypeDef(
    _ListUsageForLicenseConfigurationPaginateResponseLicenseConfigurationUsageListTypeDef
):
    """
    Type definition for `ListUsageForLicenseConfigurationPaginateResponse` `LicenseConfigurationUsageList`

    Contains details of the usage of each resource from the license pool.

    - **ResourceArn** *(string) --*

      ARN of the resource associated with a license configuration.

    - **ResourceType** *(string) --*

      Type of resource associated with athe license configuration.

    - **ResourceStatus** *(string) --*

      Status of a resource associated with the license configuration.

    - **ResourceOwnerId** *(string) --*

      ID of the account that owns a resource that is associated with the license configuration.

    - **AssociationTime** *(datetime) --*

      Time when the license configuration was initially associated with a resource.

    - **ConsumedLicenses** *(integer) --*

      Number of licenses consumed out of the total provisioned in the license configuration.
    """


_ListUsageForLicenseConfigurationPaginateResponseTypeDef = TypedDict(
    "_ListUsageForLicenseConfigurationPaginateResponseTypeDef",
    {
        "LicenseConfigurationUsageList": List[
            ListUsageForLicenseConfigurationPaginateResponseLicenseConfigurationUsageListTypeDef
        ]
    },
    total=False,
)


class ListUsageForLicenseConfigurationPaginateResponseTypeDef(
    _ListUsageForLicenseConfigurationPaginateResponseTypeDef
):
    """
    Type definition for `ListUsageForLicenseConfigurationPaginate` `Response`

    - **LicenseConfigurationUsageList** *(list) --*

      An array of ``LicenseConfigurationUsage`` objects.

      - *(dict) --*

        Contains details of the usage of each resource from the license pool.

        - **ResourceArn** *(string) --*

          ARN of the resource associated with a license configuration.

        - **ResourceType** *(string) --*

          Type of resource associated with athe license configuration.

        - **ResourceStatus** *(string) --*

          Status of a resource associated with the license configuration.

        - **ResourceOwnerId** *(string) --*

          ID of the account that owns a resource that is associated with the license configuration.

        - **AssociationTime** *(datetime) --*

          Time when the license configuration was initially associated with a resource.

        - **ConsumedLicenses** *(integer) --*

          Number of licenses consumed out of the total provisioned in the license configuration.
    """
