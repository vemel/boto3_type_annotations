"Main interface for cloudhsm type defs"
from __future__ import annotations

from typing import List
from typing_extensions import TypedDict


__all__ = (
    "ClientAddTagsToResourceResponseTypeDef",
    "ClientAddTagsToResourceTagListTypeDef",
    "ClientCreateHapgResponseTypeDef",
    "ClientCreateHsmResponseTypeDef",
    "ClientCreateLunaClientResponseTypeDef",
    "ClientDeleteHapgResponseTypeDef",
    "ClientDeleteHsmResponseTypeDef",
    "ClientDeleteLunaClientResponseTypeDef",
    "ClientDescribeHapgResponseTypeDef",
    "ClientDescribeHsmResponseTypeDef",
    "ClientDescribeLunaClientResponseTypeDef",
    "ClientGetConfigResponseTypeDef",
    "ClientListAvailableZonesResponseTypeDef",
    "ClientListHapgsResponseTypeDef",
    "ClientListHsmsResponseTypeDef",
    "ClientListLunaClientsResponseTypeDef",
    "ClientListTagsForResourceResponseTagListTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientModifyHapgResponseTypeDef",
    "ClientModifyHsmResponseTypeDef",
    "ClientModifyLunaClientResponseTypeDef",
    "ClientRemoveTagsFromResourceResponseTypeDef",
    "ListHapgsPaginatePaginationConfigTypeDef",
    "ListHapgsPaginateResponseTypeDef",
    "ListHsmsPaginatePaginationConfigTypeDef",
    "ListHsmsPaginateResponseTypeDef",
    "ListLunaClientsPaginatePaginationConfigTypeDef",
    "ListLunaClientsPaginateResponseTypeDef",
)


_ClientAddTagsToResourceResponseTypeDef = TypedDict(
    "_ClientAddTagsToResourceResponseTypeDef", {"Status": str}, total=False
)


class ClientAddTagsToResourceResponseTypeDef(_ClientAddTagsToResourceResponseTypeDef):
    """
    Type definition for `ClientAddTagsToResource` `Response`

    - **Status** *(string) --*

      The status of the operation.
    """


_ClientAddTagsToResourceTagListTypeDef = TypedDict(
    "_ClientAddTagsToResourceTagListTypeDef", {"Key": str, "Value": str}
)


class ClientAddTagsToResourceTagListTypeDef(_ClientAddTagsToResourceTagListTypeDef):
    """
    Type definition for `ClientAddTagsToResource` `TagList`

    A key-value pair that identifies or specifies metadata about an AWS CloudHSM resource.

    - **Key** *(string) --* **[REQUIRED]**

      The key of the tag.

    - **Value** *(string) --* **[REQUIRED]**

      The value of the tag.
    """


_ClientCreateHapgResponseTypeDef = TypedDict(
    "_ClientCreateHapgResponseTypeDef", {"HapgArn": str}, total=False
)


class ClientCreateHapgResponseTypeDef(_ClientCreateHapgResponseTypeDef):
    """
    Type definition for `ClientCreateHapg` `Response`

    Contains the output of the  CreateHAPartitionGroup action.

    - **HapgArn** *(string) --*

      The ARN of the high-availability partition group.
    """


_ClientCreateHsmResponseTypeDef = TypedDict(
    "_ClientCreateHsmResponseTypeDef", {"HsmArn": str}, total=False
)


class ClientCreateHsmResponseTypeDef(_ClientCreateHsmResponseTypeDef):
    """
    Type definition for `ClientCreateHsm` `Response`

    Contains the output of the ``CreateHsm`` operation.

    - **HsmArn** *(string) --*

      The ARN of the HSM.
    """


_ClientCreateLunaClientResponseTypeDef = TypedDict(
    "_ClientCreateLunaClientResponseTypeDef", {"ClientArn": str}, total=False
)


class ClientCreateLunaClientResponseTypeDef(_ClientCreateLunaClientResponseTypeDef):
    """
    Type definition for `ClientCreateLunaClient` `Response`

    Contains the output of the  CreateLunaClient action.

    - **ClientArn** *(string) --*

      The ARN of the client.
    """


_ClientDeleteHapgResponseTypeDef = TypedDict(
    "_ClientDeleteHapgResponseTypeDef", {"Status": str}, total=False
)


class ClientDeleteHapgResponseTypeDef(_ClientDeleteHapgResponseTypeDef):
    """
    Type definition for `ClientDeleteHapg` `Response`

    Contains the output of the  DeleteHapg action.

    - **Status** *(string) --*

      The status of the action.
    """


_ClientDeleteHsmResponseTypeDef = TypedDict(
    "_ClientDeleteHsmResponseTypeDef", {"Status": str}, total=False
)


class ClientDeleteHsmResponseTypeDef(_ClientDeleteHsmResponseTypeDef):
    """
    Type definition for `ClientDeleteHsm` `Response`

    Contains the output of the  DeleteHsm operation.

    - **Status** *(string) --*

      The status of the operation.
    """


_ClientDeleteLunaClientResponseTypeDef = TypedDict(
    "_ClientDeleteLunaClientResponseTypeDef", {"Status": str}, total=False
)


class ClientDeleteLunaClientResponseTypeDef(_ClientDeleteLunaClientResponseTypeDef):
    """
    Type definition for `ClientDeleteLunaClient` `Response`

    - **Status** *(string) --*

      The status of the action.
    """


_ClientDescribeHapgResponseTypeDef = TypedDict(
    "_ClientDescribeHapgResponseTypeDef",
    {
        "HapgArn": str,
        "HapgSerial": str,
        "HsmsLastActionFailed": List[str],
        "HsmsPendingDeletion": List[str],
        "HsmsPendingRegistration": List[str],
        "Label": str,
        "LastModifiedTimestamp": str,
        "PartitionSerialList": List[str],
        "State": str,
    },
    total=False,
)


class ClientDescribeHapgResponseTypeDef(_ClientDescribeHapgResponseTypeDef):
    """
    Type definition for `ClientDescribeHapg` `Response`

    Contains the output of the  DescribeHapg action.

    - **HapgArn** *(string) --*

      The ARN of the high-availability partition group.

    - **HapgSerial** *(string) --*

      The serial number of the high-availability partition group.

    - **HsmsLastActionFailed** *(list) --*

      - *(string) --*

        An ARN that identifies an HSM.

    - **HsmsPendingDeletion** *(list) --*

      - *(string) --*

        An ARN that identifies an HSM.

    - **HsmsPendingRegistration** *(list) --*

      - *(string) --*

        An ARN that identifies an HSM.

    - **Label** *(string) --*

      The label for the high-availability partition group.

    - **LastModifiedTimestamp** *(string) --*

      The date and time the high-availability partition group was last modified.

    - **PartitionSerialList** *(list) --*

      The list of partition serial numbers that belong to the high-availability partition group.

      - *(string) --*

    - **State** *(string) --*

      The state of the high-availability partition group.
    """


_ClientDescribeHsmResponseTypeDef = TypedDict(
    "_ClientDescribeHsmResponseTypeDef",
    {
        "HsmArn": str,
        "Status": str,
        "StatusDetails": str,
        "AvailabilityZone": str,
        "EniId": str,
        "EniIp": str,
        "SubscriptionType": str,
        "SubscriptionStartDate": str,
        "SubscriptionEndDate": str,
        "VpcId": str,
        "SubnetId": str,
        "IamRoleArn": str,
        "SerialNumber": str,
        "VendorName": str,
        "HsmType": str,
        "SoftwareVersion": str,
        "SshPublicKey": str,
        "SshKeyLastUpdated": str,
        "ServerCertUri": str,
        "ServerCertLastUpdated": str,
        "Partitions": List[str],
    },
    total=False,
)


class ClientDescribeHsmResponseTypeDef(_ClientDescribeHsmResponseTypeDef):
    """
    Type definition for `ClientDescribeHsm` `Response`

    Contains the output of the  DescribeHsm operation.

    - **HsmArn** *(string) --*

      The ARN of the HSM.

    - **Status** *(string) --*

      The status of the HSM.

    - **StatusDetails** *(string) --*

      Contains additional information about the status of the HSM.

    - **AvailabilityZone** *(string) --*

      The Availability Zone that the HSM is in.

    - **EniId** *(string) --*

      The identifier of the elastic network interface (ENI) attached to the HSM.

    - **EniIp** *(string) --*

      The IP address assigned to the HSM's ENI.

    - **SubscriptionType** *(string) --*

      Specifies the type of subscription for the HSM.

      * **PRODUCTION** - The HSM is being used in a production environment.

      * **TRIAL** - The HSM is being used in a product trial.

    - **SubscriptionStartDate** *(string) --*

      The subscription start date.

    - **SubscriptionEndDate** *(string) --*

      The subscription end date.

    - **VpcId** *(string) --*

      The identifier of the VPC that the HSM is in.

    - **SubnetId** *(string) --*

      The identifier of the subnet that the HSM is in.

    - **IamRoleArn** *(string) --*

      The ARN of the IAM role assigned to the HSM.

    - **SerialNumber** *(string) --*

      The serial number of the HSM.

    - **VendorName** *(string) --*

      The name of the HSM vendor.

    - **HsmType** *(string) --*

      The HSM model type.

    - **SoftwareVersion** *(string) --*

      The HSM software version.

    - **SshPublicKey** *(string) --*

      The public SSH key.

    - **SshKeyLastUpdated** *(string) --*

      The date and time that the SSH key was last updated.

    - **ServerCertUri** *(string) --*

      The URI of the certificate server.

    - **ServerCertLastUpdated** *(string) --*

      The date and time that the server certificate was last updated.

    - **Partitions** *(list) --*

      The list of partitions on the HSM.

      - *(string) --*
    """


_ClientDescribeLunaClientResponseTypeDef = TypedDict(
    "_ClientDescribeLunaClientResponseTypeDef",
    {
        "ClientArn": str,
        "Certificate": str,
        "CertificateFingerprint": str,
        "LastModifiedTimestamp": str,
        "Label": str,
    },
    total=False,
)


class ClientDescribeLunaClientResponseTypeDef(_ClientDescribeLunaClientResponseTypeDef):
    """
    Type definition for `ClientDescribeLunaClient` `Response`

    - **ClientArn** *(string) --*

      The ARN of the client.

    - **Certificate** *(string) --*

      The certificate installed on the HSMs used by this client.

    - **CertificateFingerprint** *(string) --*

      The certificate fingerprint.

    - **LastModifiedTimestamp** *(string) --*

      The date and time the client was last modified.

    - **Label** *(string) --*

      The label of the client.
    """


_ClientGetConfigResponseTypeDef = TypedDict(
    "_ClientGetConfigResponseTypeDef",
    {"ConfigType": str, "ConfigFile": str, "ConfigCred": str},
    total=False,
)


class ClientGetConfigResponseTypeDef(_ClientGetConfigResponseTypeDef):
    """
    Type definition for `ClientGetConfig` `Response`

    - **ConfigType** *(string) --*

      The type of credentials.

    - **ConfigFile** *(string) --*

      The chrystoki.conf configuration file.

    - **ConfigCred** *(string) --*

      The certificate file containing the server.pem files of the HSMs.
    """


_ClientListAvailableZonesResponseTypeDef = TypedDict(
    "_ClientListAvailableZonesResponseTypeDef", {"AZList": List[str]}, total=False
)


class ClientListAvailableZonesResponseTypeDef(_ClientListAvailableZonesResponseTypeDef):
    """
    Type definition for `ClientListAvailableZones` `Response`

    - **AZList** *(list) --*

      The list of Availability Zones that have available AWS CloudHSM capacity.

      - *(string) --*
    """


_ClientListHapgsResponseTypeDef = TypedDict(
    "_ClientListHapgsResponseTypeDef",
    {"HapgList": List[str], "NextToken": str},
    total=False,
)


class ClientListHapgsResponseTypeDef(_ClientListHapgsResponseTypeDef):
    """
    Type definition for `ClientListHapgs` `Response`

    - **HapgList** *(list) --*

      The list of high-availability partition groups.

      - *(string) --*

    - **NextToken** *(string) --*

      If not null, more results are available. Pass this value to ``ListHapgs`` to retrieve the
      next set of items.
    """


_ClientListHsmsResponseTypeDef = TypedDict(
    "_ClientListHsmsResponseTypeDef",
    {"HsmList": List[str], "NextToken": str},
    total=False,
)


class ClientListHsmsResponseTypeDef(_ClientListHsmsResponseTypeDef):
    """
    Type definition for `ClientListHsms` `Response`

    Contains the output of the ``ListHsms`` operation.

    - **HsmList** *(list) --*

      The list of ARNs that identify the HSMs.

      - *(string) --*

        An ARN that identifies an HSM.

    - **NextToken** *(string) --*

      If not null, more results are available. Pass this value to ``ListHsms`` to retrieve the next
      set of items.
    """


_ClientListLunaClientsResponseTypeDef = TypedDict(
    "_ClientListLunaClientsResponseTypeDef",
    {"ClientList": List[str], "NextToken": str},
    total=False,
)


class ClientListLunaClientsResponseTypeDef(_ClientListLunaClientsResponseTypeDef):
    """
    Type definition for `ClientListLunaClients` `Response`

    - **ClientList** *(list) --*

      The list of clients.

      - *(string) --*

    - **NextToken** *(string) --*

      If not null, more results are available. Pass this to ``ListLunaClients`` to retrieve the
      next set of items.
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

    A key-value pair that identifies or specifies metadata about an AWS CloudHSM resource.

    - **Key** *(string) --*

      The key of the tag.

    - **Value** *(string) --*

      The value of the tag.
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

      One or more tags.

      - *(dict) --*

        A key-value pair that identifies or specifies metadata about an AWS CloudHSM resource.

        - **Key** *(string) --*

          The key of the tag.

        - **Value** *(string) --*

          The value of the tag.
    """


_ClientModifyHapgResponseTypeDef = TypedDict(
    "_ClientModifyHapgResponseTypeDef", {"HapgArn": str}, total=False
)


class ClientModifyHapgResponseTypeDef(_ClientModifyHapgResponseTypeDef):
    """
    Type definition for `ClientModifyHapg` `Response`

    - **HapgArn** *(string) --*

      The ARN of the high-availability partition group.
    """


_ClientModifyHsmResponseTypeDef = TypedDict(
    "_ClientModifyHsmResponseTypeDef", {"HsmArn": str}, total=False
)


class ClientModifyHsmResponseTypeDef(_ClientModifyHsmResponseTypeDef):
    """
    Type definition for `ClientModifyHsm` `Response`

    Contains the output of the  ModifyHsm operation.

    - **HsmArn** *(string) --*

      The ARN of the HSM.
    """


_ClientModifyLunaClientResponseTypeDef = TypedDict(
    "_ClientModifyLunaClientResponseTypeDef", {"ClientArn": str}, total=False
)


class ClientModifyLunaClientResponseTypeDef(_ClientModifyLunaClientResponseTypeDef):
    """
    Type definition for `ClientModifyLunaClient` `Response`

    - **ClientArn** *(string) --*

      The ARN of the client.
    """


_ClientRemoveTagsFromResourceResponseTypeDef = TypedDict(
    "_ClientRemoveTagsFromResourceResponseTypeDef", {"Status": str}, total=False
)


class ClientRemoveTagsFromResourceResponseTypeDef(
    _ClientRemoveTagsFromResourceResponseTypeDef
):
    """
    Type definition for `ClientRemoveTagsFromResource` `Response`

    - **Status** *(string) --*

      The status of the operation.
    """


_ListHapgsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListHapgsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListHapgsPaginatePaginationConfigTypeDef(
    _ListHapgsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListHapgsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListHapgsPaginateResponseTypeDef = TypedDict(
    "_ListHapgsPaginateResponseTypeDef", {"HapgList": List[str]}, total=False
)


class ListHapgsPaginateResponseTypeDef(_ListHapgsPaginateResponseTypeDef):
    """
    Type definition for `ListHapgsPaginate` `Response`

    - **HapgList** *(list) --*

      The list of high-availability partition groups.

      - *(string) --*
    """


_ListHsmsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListHsmsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListHsmsPaginatePaginationConfigTypeDef(_ListHsmsPaginatePaginationConfigTypeDef):
    """
    Type definition for `ListHsmsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListHsmsPaginateResponseTypeDef = TypedDict(
    "_ListHsmsPaginateResponseTypeDef", {"HsmList": List[str]}, total=False
)


class ListHsmsPaginateResponseTypeDef(_ListHsmsPaginateResponseTypeDef):
    """
    Type definition for `ListHsmsPaginate` `Response`

    Contains the output of the ``ListHsms`` operation.

    - **HsmList** *(list) --*

      The list of ARNs that identify the HSMs.

      - *(string) --*

        An ARN that identifies an HSM.
    """


_ListLunaClientsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListLunaClientsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListLunaClientsPaginatePaginationConfigTypeDef(
    _ListLunaClientsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListLunaClientsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListLunaClientsPaginateResponseTypeDef = TypedDict(
    "_ListLunaClientsPaginateResponseTypeDef", {"ClientList": List[str]}, total=False
)


class ListLunaClientsPaginateResponseTypeDef(_ListLunaClientsPaginateResponseTypeDef):
    """
    Type definition for `ListLunaClientsPaginate` `Response`

    - **ClientList** *(list) --*

      The list of clients.

      - *(string) --*
    """
