"Main interface for kafka type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientCreateClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfoTypeDef",
    "ClientCreateClusterBrokerNodeGroupInfoStorageInfoTypeDef",
    "ClientCreateClusterBrokerNodeGroupInfoTypeDef",
    "ClientCreateClusterClientAuthenticationTlsTypeDef",
    "ClientCreateClusterClientAuthenticationTypeDef",
    "ClientCreateClusterConfigurationInfoTypeDef",
    "ClientCreateClusterEncryptionInfoEncryptionAtRestTypeDef",
    "ClientCreateClusterEncryptionInfoEncryptionInTransitTypeDef",
    "ClientCreateClusterEncryptionInfoTypeDef",
    "ClientCreateClusterResponseTypeDef",
    "ClientCreateConfigurationResponseLatestRevisionTypeDef",
    "ClientCreateConfigurationResponseTypeDef",
    "ClientDeleteClusterResponseTypeDef",
    "ClientDescribeClusterOperationResponseClusterOperationInfoErrorInfoTypeDef",
    "ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoBrokerEBSVolumeInfoTypeDef",
    "ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoConfigurationInfoTypeDef",
    "ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoTypeDef",
    "ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoBrokerEBSVolumeInfoTypeDef",
    "ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoConfigurationInfoTypeDef",
    "ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoTypeDef",
    "ClientDescribeClusterOperationResponseClusterOperationInfoTypeDef",
    "ClientDescribeClusterOperationResponseTypeDef",
    "ClientDescribeClusterResponseClusterInfoBrokerNodeGroupInfoStorageInfoEbsStorageInfoTypeDef",
    "ClientDescribeClusterResponseClusterInfoBrokerNodeGroupInfoStorageInfoTypeDef",
    "ClientDescribeClusterResponseClusterInfoBrokerNodeGroupInfoTypeDef",
    "ClientDescribeClusterResponseClusterInfoClientAuthenticationTlsTypeDef",
    "ClientDescribeClusterResponseClusterInfoClientAuthenticationTypeDef",
    "ClientDescribeClusterResponseClusterInfoCurrentBrokerSoftwareInfoTypeDef",
    "ClientDescribeClusterResponseClusterInfoEncryptionInfoEncryptionAtRestTypeDef",
    "ClientDescribeClusterResponseClusterInfoEncryptionInfoEncryptionInTransitTypeDef",
    "ClientDescribeClusterResponseClusterInfoEncryptionInfoTypeDef",
    "ClientDescribeClusterResponseClusterInfoTypeDef",
    "ClientDescribeClusterResponseTypeDef",
    "ClientDescribeConfigurationResponseLatestRevisionTypeDef",
    "ClientDescribeConfigurationResponseTypeDef",
    "ClientDescribeConfigurationRevisionResponseTypeDef",
    "ClientGetBootstrapBrokersResponseTypeDef",
    "ClientListClusterOperationsResponseClusterOperationInfoListErrorInfoTypeDef",
    "ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoBrokerEBSVolumeInfoTypeDef",
    "ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoConfigurationInfoTypeDef",
    "ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoTypeDef",
    "ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoBrokerEBSVolumeInfoTypeDef",
    "ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoConfigurationInfoTypeDef",
    "ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoTypeDef",
    "ClientListClusterOperationsResponseClusterOperationInfoListTypeDef",
    "ClientListClusterOperationsResponseTypeDef",
    "ClientListClustersResponseClusterInfoListBrokerNodeGroupInfoStorageInfoEbsStorageInfoTypeDef",
    "ClientListClustersResponseClusterInfoListBrokerNodeGroupInfoStorageInfoTypeDef",
    "ClientListClustersResponseClusterInfoListBrokerNodeGroupInfoTypeDef",
    "ClientListClustersResponseClusterInfoListClientAuthenticationTlsTypeDef",
    "ClientListClustersResponseClusterInfoListClientAuthenticationTypeDef",
    "ClientListClustersResponseClusterInfoListCurrentBrokerSoftwareInfoTypeDef",
    "ClientListClustersResponseClusterInfoListEncryptionInfoEncryptionAtRestTypeDef",
    "ClientListClustersResponseClusterInfoListEncryptionInfoEncryptionInTransitTypeDef",
    "ClientListClustersResponseClusterInfoListEncryptionInfoTypeDef",
    "ClientListClustersResponseClusterInfoListTypeDef",
    "ClientListClustersResponseTypeDef",
    "ClientListConfigurationRevisionsResponseRevisionsTypeDef",
    "ClientListConfigurationRevisionsResponseTypeDef",
    "ClientListConfigurationsResponseConfigurationsLatestRevisionTypeDef",
    "ClientListConfigurationsResponseConfigurationsTypeDef",
    "ClientListConfigurationsResponseTypeDef",
    "ClientListNodesResponseNodeInfoListBrokerNodeInfoCurrentBrokerSoftwareInfoTypeDef",
    "ClientListNodesResponseNodeInfoListBrokerNodeInfoTypeDef",
    "ClientListNodesResponseNodeInfoListZookeeperNodeInfoTypeDef",
    "ClientListNodesResponseNodeInfoListTypeDef",
    "ClientListNodesResponseTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientUpdateBrokerCountResponseTypeDef",
    "ClientUpdateBrokerStorageResponseTypeDef",
    "ClientUpdateBrokerStorageTargetBrokerEBSVolumeInfoTypeDef",
    "ClientUpdateClusterConfigurationConfigurationInfoTypeDef",
    "ClientUpdateClusterConfigurationResponseTypeDef",
    "ListClusterOperationsPaginatePaginationConfigTypeDef",
    "ListClusterOperationsPaginateResponseClusterOperationInfoListErrorInfoTypeDef",
    "ListClusterOperationsPaginateResponseClusterOperationInfoListSourceClusterInfoBrokerEBSVolumeInfoTypeDef",
    "ListClusterOperationsPaginateResponseClusterOperationInfoListSourceClusterInfoConfigurationInfoTypeDef",
    "ListClusterOperationsPaginateResponseClusterOperationInfoListSourceClusterInfoTypeDef",
    "ListClusterOperationsPaginateResponseClusterOperationInfoListTargetClusterInfoBrokerEBSVolumeInfoTypeDef",
    "ListClusterOperationsPaginateResponseClusterOperationInfoListTargetClusterInfoConfigurationInfoTypeDef",
    "ListClusterOperationsPaginateResponseClusterOperationInfoListTargetClusterInfoTypeDef",
    "ListClusterOperationsPaginateResponseClusterOperationInfoListTypeDef",
    "ListClusterOperationsPaginateResponseTypeDef",
    "ListClustersPaginatePaginationConfigTypeDef",
    "ListClustersPaginateResponseClusterInfoListBrokerNodeGroupInfoStorageInfoEbsStorageInfoTypeDef",
    "ListClustersPaginateResponseClusterInfoListBrokerNodeGroupInfoStorageInfoTypeDef",
    "ListClustersPaginateResponseClusterInfoListBrokerNodeGroupInfoTypeDef",
    "ListClustersPaginateResponseClusterInfoListClientAuthenticationTlsTypeDef",
    "ListClustersPaginateResponseClusterInfoListClientAuthenticationTypeDef",
    "ListClustersPaginateResponseClusterInfoListCurrentBrokerSoftwareInfoTypeDef",
    "ListClustersPaginateResponseClusterInfoListEncryptionInfoEncryptionAtRestTypeDef",
    "ListClustersPaginateResponseClusterInfoListEncryptionInfoEncryptionInTransitTypeDef",
    "ListClustersPaginateResponseClusterInfoListEncryptionInfoTypeDef",
    "ListClustersPaginateResponseClusterInfoListTypeDef",
    "ListClustersPaginateResponseTypeDef",
    "ListConfigurationRevisionsPaginatePaginationConfigTypeDef",
    "ListConfigurationRevisionsPaginateResponseRevisionsTypeDef",
    "ListConfigurationRevisionsPaginateResponseTypeDef",
    "ListConfigurationsPaginatePaginationConfigTypeDef",
    "ListConfigurationsPaginateResponseConfigurationsLatestRevisionTypeDef",
    "ListConfigurationsPaginateResponseConfigurationsTypeDef",
    "ListConfigurationsPaginateResponseTypeDef",
    "ListNodesPaginatePaginationConfigTypeDef",
    "ListNodesPaginateResponseNodeInfoListBrokerNodeInfoCurrentBrokerSoftwareInfoTypeDef",
    "ListNodesPaginateResponseNodeInfoListBrokerNodeInfoTypeDef",
    "ListNodesPaginateResponseNodeInfoListZookeeperNodeInfoTypeDef",
    "ListNodesPaginateResponseNodeInfoListTypeDef",
    "ListNodesPaginateResponseTypeDef",
)


_ClientCreateClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfoTypeDef = TypedDict(
    "_ClientCreateClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfoTypeDef",
    {"VolumeSize": int},
    total=False,
)


class ClientCreateClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfoTypeDef(
    _ClientCreateClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfoTypeDef
):
    """
    Type definition for `ClientCreateClusterBrokerNodeGroupInfoStorageInfo` `EbsStorageInfo`

    EBS volume information.

    - **VolumeSize** *(integer) --*

      The size in GiB of the EBS volume for the data drive on each broker node.
    """


_ClientCreateClusterBrokerNodeGroupInfoStorageInfoTypeDef = TypedDict(
    "_ClientCreateClusterBrokerNodeGroupInfoStorageInfoTypeDef",
    {
        "EbsStorageInfo": ClientCreateClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfoTypeDef
    },
    total=False,
)


class ClientCreateClusterBrokerNodeGroupInfoStorageInfoTypeDef(
    _ClientCreateClusterBrokerNodeGroupInfoStorageInfoTypeDef
):
    """
    Type definition for `ClientCreateClusterBrokerNodeGroupInfo` `StorageInfo`

    Contains information about storage volumes attached to MSK broker nodes.

    - **EbsStorageInfo** *(dict) --*

      EBS volume information.

      - **VolumeSize** *(integer) --*

        The size in GiB of the EBS volume for the data drive on each broker node.
    """


_RequiredClientCreateClusterBrokerNodeGroupInfoTypeDef = TypedDict(
    "_RequiredClientCreateClusterBrokerNodeGroupInfoTypeDef",
    {"ClientSubnets": List[str], "InstanceType": str},
)
_OptionalClientCreateClusterBrokerNodeGroupInfoTypeDef = TypedDict(
    "_OptionalClientCreateClusterBrokerNodeGroupInfoTypeDef",
    {
        "BrokerAZDistribution": str,
        "SecurityGroups": List[str],
        "StorageInfo": ClientCreateClusterBrokerNodeGroupInfoStorageInfoTypeDef,
    },
    total=False,
)


class ClientCreateClusterBrokerNodeGroupInfoTypeDef(
    _RequiredClientCreateClusterBrokerNodeGroupInfoTypeDef,
    _OptionalClientCreateClusterBrokerNodeGroupInfoTypeDef,
):
    """
    Type definition for `ClientCreateCluster` `BrokerNodeGroupInfo`

    Information about the broker nodes in the cluster.

    - **BrokerAZDistribution** *(string) --*

      The distribution of broker nodes across Availability Zones. This is an optional parameter. If
      you don't specify it, Amazon MSK gives it the value DEFAULT. You can also explicitly set this
      parameter to the value DEFAULT. No other values are currently allowed.

      Amazon MSK distributes the broker nodes evenly across the Availability Zones that correspond to
      the subnets you provide when you create the cluster.

    - **ClientSubnets** *(list) --* **[REQUIRED]**

      The list of subnets to connect to in the client virtual private cloud (VPC). AWS creates
      elastic network interfaces inside these subnets. Client applications use elastic network
      interfaces to produce and consume data. Client subnets can't be in Availability Zone us-east-1e.

      - *(string) --*

    - **InstanceType** *(string) --* **[REQUIRED]**

      The type of Amazon EC2 instances to use for Kafka brokers. The following instance types are
      allowed: kafka.m5.large, kafka.m5.xlarge, kafka.m5.2xlarge, kafka.m5.4xlarge,
      kafka.m5.12xlarge, and kafka.m5.24xlarge.

    - **SecurityGroups** *(list) --*

      The AWS security groups to associate with the elastic network interfaces in order to specify
      who can connect to and communicate with the Amazon MSK cluster. If you don't specify a security
      group, Amazon MSK uses the default security group associated with the VPC.

      - *(string) --*

    - **StorageInfo** *(dict) --*

      Contains information about storage volumes attached to MSK broker nodes.

      - **EbsStorageInfo** *(dict) --*

        EBS volume information.

        - **VolumeSize** *(integer) --*

          The size in GiB of the EBS volume for the data drive on each broker node.
    """


_ClientCreateClusterClientAuthenticationTlsTypeDef = TypedDict(
    "_ClientCreateClusterClientAuthenticationTlsTypeDef",
    {"CertificateAuthorityArnList": List[str]},
    total=False,
)


class ClientCreateClusterClientAuthenticationTlsTypeDef(
    _ClientCreateClusterClientAuthenticationTlsTypeDef
):
    """
    Type definition for `ClientCreateClusterClientAuthentication` `Tls`

    Details for ClientAuthentication using TLS.

    - **CertificateAuthorityArnList** *(list) --*

      List of ACM Certificate Authority ARNs.

      - *(string) --*
    """


_ClientCreateClusterClientAuthenticationTypeDef = TypedDict(
    "_ClientCreateClusterClientAuthenticationTypeDef",
    {"Tls": ClientCreateClusterClientAuthenticationTlsTypeDef},
    total=False,
)


class ClientCreateClusterClientAuthenticationTypeDef(
    _ClientCreateClusterClientAuthenticationTypeDef
):
    """
    Type definition for `ClientCreateCluster` `ClientAuthentication`

    Includes all client authentication related information.

    - **Tls** *(dict) --*

      Details for ClientAuthentication using TLS.

      - **CertificateAuthorityArnList** *(list) --*

        List of ACM Certificate Authority ARNs.

        - *(string) --*
    """


_ClientCreateClusterConfigurationInfoTypeDef = TypedDict(
    "_ClientCreateClusterConfigurationInfoTypeDef", {"Arn": str, "Revision": int}
)


class ClientCreateClusterConfigurationInfoTypeDef(
    _ClientCreateClusterConfigurationInfoTypeDef
):
    """
    Type definition for `ClientCreateCluster` `ConfigurationInfo`

    Represents the configuration that you want MSK to use for the brokers in a cluster.

    - **Arn** *(string) --* **[REQUIRED]**

      ARN of the configuration to use.

    - **Revision** *(integer) --* **[REQUIRED]**

      The revision of the configuration to use.
    """


_ClientCreateClusterEncryptionInfoEncryptionAtRestTypeDef = TypedDict(
    "_ClientCreateClusterEncryptionInfoEncryptionAtRestTypeDef",
    {"DataVolumeKMSKeyId": str},
)


class ClientCreateClusterEncryptionInfoEncryptionAtRestTypeDef(
    _ClientCreateClusterEncryptionInfoEncryptionAtRestTypeDef
):
    """
    Type definition for `ClientCreateClusterEncryptionInfo` `EncryptionAtRest`

    The data-volume encryption details.

    - **DataVolumeKMSKeyId** *(string) --* **[REQUIRED]**

      The ARN of the AWS KMS key for encrypting data at rest. If you don't specify a KMS key, MSK
      creates one for you and uses it.
    """


_ClientCreateClusterEncryptionInfoEncryptionInTransitTypeDef = TypedDict(
    "_ClientCreateClusterEncryptionInfoEncryptionInTransitTypeDef",
    {"ClientBroker": str, "InCluster": bool},
    total=False,
)


class ClientCreateClusterEncryptionInfoEncryptionInTransitTypeDef(
    _ClientCreateClusterEncryptionInfoEncryptionInTransitTypeDef
):
    """
    Type definition for `ClientCreateClusterEncryptionInfo` `EncryptionInTransit`

    The details for encryption in transit.

    - **ClientBroker** *(string) --*

      Indicates the encryption setting for data in transit between clients and brokers. The
      following are the possible values.

      TLS means that client-broker communication is enabled with TLS only.

      TLS_PLAINTEXT means that client-broker communication is enabled for both TLS-encrypted, as
      well as plaintext data.

      PLAINTEXT means that client-broker communication is enabled in plaintext only.

      The default value is TLS_PLAINTEXT.

    - **InCluster** *(boolean) --*

      When set to true, it indicates that data communication among the broker nodes of the cluster
      is encrypted. When set to false, the communication happens in plaintext.

      The default value is true.
    """


_ClientCreateClusterEncryptionInfoTypeDef = TypedDict(
    "_ClientCreateClusterEncryptionInfoTypeDef",
    {
        "EncryptionAtRest": ClientCreateClusterEncryptionInfoEncryptionAtRestTypeDef,
        "EncryptionInTransit": ClientCreateClusterEncryptionInfoEncryptionInTransitTypeDef,
    },
    total=False,
)


class ClientCreateClusterEncryptionInfoTypeDef(
    _ClientCreateClusterEncryptionInfoTypeDef
):
    """
    Type definition for `ClientCreateCluster` `EncryptionInfo`

    Includes all encryption-related information.

    - **EncryptionAtRest** *(dict) --*

      The data-volume encryption details.

      - **DataVolumeKMSKeyId** *(string) --* **[REQUIRED]**

        The ARN of the AWS KMS key for encrypting data at rest. If you don't specify a KMS key, MSK
        creates one for you and uses it.

    - **EncryptionInTransit** *(dict) --*

      The details for encryption in transit.

      - **ClientBroker** *(string) --*

        Indicates the encryption setting for data in transit between clients and brokers. The
        following are the possible values.

        TLS means that client-broker communication is enabled with TLS only.

        TLS_PLAINTEXT means that client-broker communication is enabled for both TLS-encrypted, as
        well as plaintext data.

        PLAINTEXT means that client-broker communication is enabled in plaintext only.

        The default value is TLS_PLAINTEXT.

      - **InCluster** *(boolean) --*

        When set to true, it indicates that data communication among the broker nodes of the cluster
        is encrypted. When set to false, the communication happens in plaintext.

        The default value is true.
    """


_ClientCreateClusterResponseTypeDef = TypedDict(
    "_ClientCreateClusterResponseTypeDef",
    {"ClusterArn": str, "ClusterName": str, "State": str},
    total=False,
)


class ClientCreateClusterResponseTypeDef(_ClientCreateClusterResponseTypeDef):
    """
    Type definition for `ClientCreateCluster` `Response`

    - **ClusterArn** *(string) --*

      The Amazon Resource Name (ARN) of the cluster.

    - **ClusterName** *(string) --*

      The name of the MSK cluster.

    - **State** *(string) --*

      The state of the cluster. The possible states are CREATING, ACTIVE, and FAILED.
    """


_ClientCreateConfigurationResponseLatestRevisionTypeDef = TypedDict(
    "_ClientCreateConfigurationResponseLatestRevisionTypeDef",
    {"CreationTime": datetime, "Description": str, "Revision": int},
    total=False,
)


class ClientCreateConfigurationResponseLatestRevisionTypeDef(
    _ClientCreateConfigurationResponseLatestRevisionTypeDef
):
    """
    Type definition for `ClientCreateConfigurationResponse` `LatestRevision`

    Latest revision of the configuration.

    - **CreationTime** *(datetime) --*

      The time when the configuration revision was created.

    - **Description** *(string) --*

      The description of the configuration revision.

    - **Revision** *(integer) --*

      The revision number.
    """


_ClientCreateConfigurationResponseTypeDef = TypedDict(
    "_ClientCreateConfigurationResponseTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "LatestRevision": ClientCreateConfigurationResponseLatestRevisionTypeDef,
        "Name": str,
    },
    total=False,
)


class ClientCreateConfigurationResponseTypeDef(
    _ClientCreateConfigurationResponseTypeDef
):
    """
    Type definition for `ClientCreateConfiguration` `Response`

    200 response

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the configuration.

    - **CreationTime** *(datetime) --*

      The time when the configuration was created.

    - **LatestRevision** *(dict) --*

      Latest revision of the configuration.

      - **CreationTime** *(datetime) --*

        The time when the configuration revision was created.

      - **Description** *(string) --*

        The description of the configuration revision.

      - **Revision** *(integer) --*

        The revision number.

    - **Name** *(string) --*

      The name of the configuration.
    """


_ClientDeleteClusterResponseTypeDef = TypedDict(
    "_ClientDeleteClusterResponseTypeDef",
    {"ClusterArn": str, "State": str},
    total=False,
)


class ClientDeleteClusterResponseTypeDef(_ClientDeleteClusterResponseTypeDef):
    """
    Type definition for `ClientDeleteCluster` `Response`

    Successful response.

    - **ClusterArn** *(string) --*

      The Amazon Resource Name (ARN) of the cluster.

    - **State** *(string) --*

      The state of the cluster. The possible states are CREATING, ACTIVE, and FAILED.
    """


_ClientDescribeClusterOperationResponseClusterOperationInfoErrorInfoTypeDef = TypedDict(
    "_ClientDescribeClusterOperationResponseClusterOperationInfoErrorInfoTypeDef",
    {"ErrorCode": str, "ErrorString": str},
    total=False,
)


class ClientDescribeClusterOperationResponseClusterOperationInfoErrorInfoTypeDef(
    _ClientDescribeClusterOperationResponseClusterOperationInfoErrorInfoTypeDef
):
    """
    Type definition for `ClientDescribeClusterOperationResponseClusterOperationInfo` `ErrorInfo`

    Describes the error if the operation fails.

    - **ErrorCode** *(string) --*

      A number describing the error programmatically.

    - **ErrorString** *(string) --*

      An optional field to provide more details about the error.
    """


_ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoBrokerEBSVolumeInfoTypeDef = TypedDict(
    "_ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoBrokerEBSVolumeInfoTypeDef",
    {"KafkaBrokerNodeId": str, "VolumeSizeGB": int},
    total=False,
)


class ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoBrokerEBSVolumeInfoTypeDef(
    _ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoBrokerEBSVolumeInfoTypeDef
):
    """
    Type definition for `ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfo` `BrokerEBSVolumeInfo`

    Specifies the EBS volume upgrade information. The broker identifier must be set to the
    keyword ALL. This means the changes apply to all the brokers in the cluster.

    - **KafkaBrokerNodeId** *(string) --*

      The ID of the broker to update.

    - **VolumeSizeGB** *(integer) --*

      Size of the EBS volume to update.
    """


_ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoConfigurationInfoTypeDef = TypedDict(
    "_ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoConfigurationInfoTypeDef",
    {"Arn": str, "Revision": int},
    total=False,
)


class ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoConfigurationInfoTypeDef(
    _ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoConfigurationInfoTypeDef
):
    """
    Type definition for `ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfo` `ConfigurationInfo`

    Information about the changes in the configuration of the brokers.

    - **Arn** *(string) --*

      ARN of the configuration to use.

    - **Revision** *(integer) --*

      The revision of the configuration to use.
    """


_ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoTypeDef = TypedDict(
    "_ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoTypeDef",
    {
        "BrokerEBSVolumeInfo": List[
            ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoBrokerEBSVolumeInfoTypeDef
        ],
        "ConfigurationInfo": ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoConfigurationInfoTypeDef,
        "NumberOfBrokerNodes": int,
    },
    total=False,
)


class ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoTypeDef(
    _ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoTypeDef
):
    """
    Type definition for `ClientDescribeClusterOperationResponseClusterOperationInfo` `SourceClusterInfo`

    Information about cluster attributes before a cluster is updated.

    - **BrokerEBSVolumeInfo** *(list) --*

      Specifies the size of the EBS volume and the ID of the associated broker.

      - *(dict) --*

        Specifies the EBS volume upgrade information. The broker identifier must be set to the
        keyword ALL. This means the changes apply to all the brokers in the cluster.

        - **KafkaBrokerNodeId** *(string) --*

          The ID of the broker to update.

        - **VolumeSizeGB** *(integer) --*

          Size of the EBS volume to update.

    - **ConfigurationInfo** *(dict) --*

      Information about the changes in the configuration of the brokers.

      - **Arn** *(string) --*

        ARN of the configuration to use.

      - **Revision** *(integer) --*

        The revision of the configuration to use.

    - **NumberOfBrokerNodes** *(integer) --*

      The number of broker nodes in the cluster.
    """


_ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoBrokerEBSVolumeInfoTypeDef = TypedDict(
    "_ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoBrokerEBSVolumeInfoTypeDef",
    {"KafkaBrokerNodeId": str, "VolumeSizeGB": int},
    total=False,
)


class ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoBrokerEBSVolumeInfoTypeDef(
    _ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoBrokerEBSVolumeInfoTypeDef
):
    """
    Type definition for `ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfo` `BrokerEBSVolumeInfo`

    Specifies the EBS volume upgrade information. The broker identifier must be set to the
    keyword ALL. This means the changes apply to all the brokers in the cluster.

    - **KafkaBrokerNodeId** *(string) --*

      The ID of the broker to update.

    - **VolumeSizeGB** *(integer) --*

      Size of the EBS volume to update.
    """


_ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoConfigurationInfoTypeDef = TypedDict(
    "_ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoConfigurationInfoTypeDef",
    {"Arn": str, "Revision": int},
    total=False,
)


class ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoConfigurationInfoTypeDef(
    _ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoConfigurationInfoTypeDef
):
    """
    Type definition for `ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfo` `ConfigurationInfo`

    Information about the changes in the configuration of the brokers.

    - **Arn** *(string) --*

      ARN of the configuration to use.

    - **Revision** *(integer) --*

      The revision of the configuration to use.
    """


_ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoTypeDef = TypedDict(
    "_ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoTypeDef",
    {
        "BrokerEBSVolumeInfo": List[
            ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoBrokerEBSVolumeInfoTypeDef
        ],
        "ConfigurationInfo": ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoConfigurationInfoTypeDef,
        "NumberOfBrokerNodes": int,
    },
    total=False,
)


class ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoTypeDef(
    _ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoTypeDef
):
    """
    Type definition for `ClientDescribeClusterOperationResponseClusterOperationInfo` `TargetClusterInfo`

    Information about cluster attributes after a cluster is updated.

    - **BrokerEBSVolumeInfo** *(list) --*

      Specifies the size of the EBS volume and the ID of the associated broker.

      - *(dict) --*

        Specifies the EBS volume upgrade information. The broker identifier must be set to the
        keyword ALL. This means the changes apply to all the brokers in the cluster.

        - **KafkaBrokerNodeId** *(string) --*

          The ID of the broker to update.

        - **VolumeSizeGB** *(integer) --*

          Size of the EBS volume to update.

    - **ConfigurationInfo** *(dict) --*

      Information about the changes in the configuration of the brokers.

      - **Arn** *(string) --*

        ARN of the configuration to use.

      - **Revision** *(integer) --*

        The revision of the configuration to use.

    - **NumberOfBrokerNodes** *(integer) --*

      The number of broker nodes in the cluster.
    """


_ClientDescribeClusterOperationResponseClusterOperationInfoTypeDef = TypedDict(
    "_ClientDescribeClusterOperationResponseClusterOperationInfoTypeDef",
    {
        "ClientRequestId": str,
        "ClusterArn": str,
        "CreationTime": datetime,
        "EndTime": datetime,
        "ErrorInfo": ClientDescribeClusterOperationResponseClusterOperationInfoErrorInfoTypeDef,
        "OperationArn": str,
        "OperationState": str,
        "OperationType": str,
        "SourceClusterInfo": ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoTypeDef,
        "TargetClusterInfo": ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoTypeDef,
    },
    total=False,
)


class ClientDescribeClusterOperationResponseClusterOperationInfoTypeDef(
    _ClientDescribeClusterOperationResponseClusterOperationInfoTypeDef
):
    """
    Type definition for `ClientDescribeClusterOperationResponse` `ClusterOperationInfo`

    Cluster operation information

    - **ClientRequestId** *(string) --*

      The ID of the API request that triggered this operation.

    - **ClusterArn** *(string) --*

      ARN of the cluster.

    - **CreationTime** *(datetime) --*

      The time that the operation was created.

    - **EndTime** *(datetime) --*

      The time at which the operation finished.

    - **ErrorInfo** *(dict) --*

      Describes the error if the operation fails.

      - **ErrorCode** *(string) --*

        A number describing the error programmatically.

      - **ErrorString** *(string) --*

        An optional field to provide more details about the error.

    - **OperationArn** *(string) --*

      ARN of the cluster operation.

    - **OperationState** *(string) --*

      State of the cluster operation.

    - **OperationType** *(string) --*

      Type of the cluster operation.

    - **SourceClusterInfo** *(dict) --*

      Information about cluster attributes before a cluster is updated.

      - **BrokerEBSVolumeInfo** *(list) --*

        Specifies the size of the EBS volume and the ID of the associated broker.

        - *(dict) --*

          Specifies the EBS volume upgrade information. The broker identifier must be set to the
          keyword ALL. This means the changes apply to all the brokers in the cluster.

          - **KafkaBrokerNodeId** *(string) --*

            The ID of the broker to update.

          - **VolumeSizeGB** *(integer) --*

            Size of the EBS volume to update.

      - **ConfigurationInfo** *(dict) --*

        Information about the changes in the configuration of the brokers.

        - **Arn** *(string) --*

          ARN of the configuration to use.

        - **Revision** *(integer) --*

          The revision of the configuration to use.

      - **NumberOfBrokerNodes** *(integer) --*

        The number of broker nodes in the cluster.

    - **TargetClusterInfo** *(dict) --*

      Information about cluster attributes after a cluster is updated.

      - **BrokerEBSVolumeInfo** *(list) --*

        Specifies the size of the EBS volume and the ID of the associated broker.

        - *(dict) --*

          Specifies the EBS volume upgrade information. The broker identifier must be set to the
          keyword ALL. This means the changes apply to all the brokers in the cluster.

          - **KafkaBrokerNodeId** *(string) --*

            The ID of the broker to update.

          - **VolumeSizeGB** *(integer) --*

            Size of the EBS volume to update.

      - **ConfigurationInfo** *(dict) --*

        Information about the changes in the configuration of the brokers.

        - **Arn** *(string) --*

          ARN of the configuration to use.

        - **Revision** *(integer) --*

          The revision of the configuration to use.

      - **NumberOfBrokerNodes** *(integer) --*

        The number of broker nodes in the cluster.
    """


_ClientDescribeClusterOperationResponseTypeDef = TypedDict(
    "_ClientDescribeClusterOperationResponseTypeDef",
    {
        "ClusterOperationInfo": ClientDescribeClusterOperationResponseClusterOperationInfoTypeDef
    },
    total=False,
)


class ClientDescribeClusterOperationResponseTypeDef(
    _ClientDescribeClusterOperationResponseTypeDef
):
    """
    Type definition for `ClientDescribeClusterOperation` `Response`

    200 response

    - **ClusterOperationInfo** *(dict) --*

      Cluster operation information

      - **ClientRequestId** *(string) --*

        The ID of the API request that triggered this operation.

      - **ClusterArn** *(string) --*

        ARN of the cluster.

      - **CreationTime** *(datetime) --*

        The time that the operation was created.

      - **EndTime** *(datetime) --*

        The time at which the operation finished.

      - **ErrorInfo** *(dict) --*

        Describes the error if the operation fails.

        - **ErrorCode** *(string) --*

          A number describing the error programmatically.

        - **ErrorString** *(string) --*

          An optional field to provide more details about the error.

      - **OperationArn** *(string) --*

        ARN of the cluster operation.

      - **OperationState** *(string) --*

        State of the cluster operation.

      - **OperationType** *(string) --*

        Type of the cluster operation.

      - **SourceClusterInfo** *(dict) --*

        Information about cluster attributes before a cluster is updated.

        - **BrokerEBSVolumeInfo** *(list) --*

          Specifies the size of the EBS volume and the ID of the associated broker.

          - *(dict) --*

            Specifies the EBS volume upgrade information. The broker identifier must be set to the
            keyword ALL. This means the changes apply to all the brokers in the cluster.

            - **KafkaBrokerNodeId** *(string) --*

              The ID of the broker to update.

            - **VolumeSizeGB** *(integer) --*

              Size of the EBS volume to update.

        - **ConfigurationInfo** *(dict) --*

          Information about the changes in the configuration of the brokers.

          - **Arn** *(string) --*

            ARN of the configuration to use.

          - **Revision** *(integer) --*

            The revision of the configuration to use.

        - **NumberOfBrokerNodes** *(integer) --*

          The number of broker nodes in the cluster.

      - **TargetClusterInfo** *(dict) --*

        Information about cluster attributes after a cluster is updated.

        - **BrokerEBSVolumeInfo** *(list) --*

          Specifies the size of the EBS volume and the ID of the associated broker.

          - *(dict) --*

            Specifies the EBS volume upgrade information. The broker identifier must be set to the
            keyword ALL. This means the changes apply to all the brokers in the cluster.

            - **KafkaBrokerNodeId** *(string) --*

              The ID of the broker to update.

            - **VolumeSizeGB** *(integer) --*

              Size of the EBS volume to update.

        - **ConfigurationInfo** *(dict) --*

          Information about the changes in the configuration of the brokers.

          - **Arn** *(string) --*

            ARN of the configuration to use.

          - **Revision** *(integer) --*

            The revision of the configuration to use.

        - **NumberOfBrokerNodes** *(integer) --*

          The number of broker nodes in the cluster.
    """


_ClientDescribeClusterResponseClusterInfoBrokerNodeGroupInfoStorageInfoEbsStorageInfoTypeDef = TypedDict(
    "_ClientDescribeClusterResponseClusterInfoBrokerNodeGroupInfoStorageInfoEbsStorageInfoTypeDef",
    {"VolumeSize": int},
    total=False,
)


class ClientDescribeClusterResponseClusterInfoBrokerNodeGroupInfoStorageInfoEbsStorageInfoTypeDef(
    _ClientDescribeClusterResponseClusterInfoBrokerNodeGroupInfoStorageInfoEbsStorageInfoTypeDef
):
    """
    Type definition for `ClientDescribeClusterResponseClusterInfoBrokerNodeGroupInfoStorageInfo` `EbsStorageInfo`

    EBS volume information.

    - **VolumeSize** *(integer) --*

      The size in GiB of the EBS volume for the data drive on each broker node.
    """


_ClientDescribeClusterResponseClusterInfoBrokerNodeGroupInfoStorageInfoTypeDef = TypedDict(
    "_ClientDescribeClusterResponseClusterInfoBrokerNodeGroupInfoStorageInfoTypeDef",
    {
        "EbsStorageInfo": ClientDescribeClusterResponseClusterInfoBrokerNodeGroupInfoStorageInfoEbsStorageInfoTypeDef
    },
    total=False,
)


class ClientDescribeClusterResponseClusterInfoBrokerNodeGroupInfoStorageInfoTypeDef(
    _ClientDescribeClusterResponseClusterInfoBrokerNodeGroupInfoStorageInfoTypeDef
):
    """
    Type definition for `ClientDescribeClusterResponseClusterInfoBrokerNodeGroupInfo` `StorageInfo`

    Contains information about storage volumes attached to MSK broker nodes.

    - **EbsStorageInfo** *(dict) --*

      EBS volume information.

      - **VolumeSize** *(integer) --*

        The size in GiB of the EBS volume for the data drive on each broker node.
    """


_ClientDescribeClusterResponseClusterInfoBrokerNodeGroupInfoTypeDef = TypedDict(
    "_ClientDescribeClusterResponseClusterInfoBrokerNodeGroupInfoTypeDef",
    {
        "BrokerAZDistribution": str,
        "ClientSubnets": List[str],
        "InstanceType": str,
        "SecurityGroups": List[str],
        "StorageInfo": ClientDescribeClusterResponseClusterInfoBrokerNodeGroupInfoStorageInfoTypeDef,
    },
    total=False,
)


class ClientDescribeClusterResponseClusterInfoBrokerNodeGroupInfoTypeDef(
    _ClientDescribeClusterResponseClusterInfoBrokerNodeGroupInfoTypeDef
):
    """
    Type definition for `ClientDescribeClusterResponseClusterInfo` `BrokerNodeGroupInfo`

    Information about the broker nodes.

    - **BrokerAZDistribution** *(string) --*

      The distribution of broker nodes across Availability Zones. This is an optional
      parameter. If you don't specify it, Amazon MSK gives it the value DEFAULT. You can also
      explicitly set this parameter to the value DEFAULT. No other values are currently allowed.

      Amazon MSK distributes the broker nodes evenly across the Availability Zones that
      correspond to the subnets you provide when you create the cluster.

    - **ClientSubnets** *(list) --*

      The list of subnets to connect to in the client virtual private cloud (VPC). AWS creates
      elastic network interfaces inside these subnets. Client applications use elastic network
      interfaces to produce and consume data. Client subnets can't be in Availability Zone
      us-east-1e.

      - *(string) --*

    - **InstanceType** *(string) --*

      The type of Amazon EC2 instances to use for Kafka brokers. The following instance types
      are allowed: kafka.m5.large, kafka.m5.xlarge, kafka.m5.2xlarge, kafka.m5.4xlarge,
      kafka.m5.12xlarge, and kafka.m5.24xlarge.

    - **SecurityGroups** *(list) --*

      The AWS security groups to associate with the elastic network interfaces in order to
      specify who can connect to and communicate with the Amazon MSK cluster. If you don't
      specify a security group, Amazon MSK uses the default security group associated with the
      VPC.

      - *(string) --*

    - **StorageInfo** *(dict) --*

      Contains information about storage volumes attached to MSK broker nodes.

      - **EbsStorageInfo** *(dict) --*

        EBS volume information.

        - **VolumeSize** *(integer) --*

          The size in GiB of the EBS volume for the data drive on each broker node.
    """


_ClientDescribeClusterResponseClusterInfoClientAuthenticationTlsTypeDef = TypedDict(
    "_ClientDescribeClusterResponseClusterInfoClientAuthenticationTlsTypeDef",
    {"CertificateAuthorityArnList": List[str]},
    total=False,
)


class ClientDescribeClusterResponseClusterInfoClientAuthenticationTlsTypeDef(
    _ClientDescribeClusterResponseClusterInfoClientAuthenticationTlsTypeDef
):
    """
    Type definition for `ClientDescribeClusterResponseClusterInfoClientAuthentication` `Tls`

    Details for ClientAuthentication using TLS.

    - **CertificateAuthorityArnList** *(list) --*

      List of ACM Certificate Authority ARNs.

      - *(string) --*
    """


_ClientDescribeClusterResponseClusterInfoClientAuthenticationTypeDef = TypedDict(
    "_ClientDescribeClusterResponseClusterInfoClientAuthenticationTypeDef",
    {"Tls": ClientDescribeClusterResponseClusterInfoClientAuthenticationTlsTypeDef},
    total=False,
)


class ClientDescribeClusterResponseClusterInfoClientAuthenticationTypeDef(
    _ClientDescribeClusterResponseClusterInfoClientAuthenticationTypeDef
):
    """
    Type definition for `ClientDescribeClusterResponseClusterInfo` `ClientAuthentication`

    Includes all client authentication information.

    - **Tls** *(dict) --*

      Details for ClientAuthentication using TLS.

      - **CertificateAuthorityArnList** *(list) --*

        List of ACM Certificate Authority ARNs.

        - *(string) --*
    """


_ClientDescribeClusterResponseClusterInfoCurrentBrokerSoftwareInfoTypeDef = TypedDict(
    "_ClientDescribeClusterResponseClusterInfoCurrentBrokerSoftwareInfoTypeDef",
    {"ConfigurationArn": str, "ConfigurationRevision": int, "KafkaVersion": str},
    total=False,
)


class ClientDescribeClusterResponseClusterInfoCurrentBrokerSoftwareInfoTypeDef(
    _ClientDescribeClusterResponseClusterInfoCurrentBrokerSoftwareInfoTypeDef
):
    """
    Type definition for `ClientDescribeClusterResponseClusterInfo` `CurrentBrokerSoftwareInfo`

    Information about the version of software currently deployed on the Kafka brokers in the
    cluster.

    - **ConfigurationArn** *(string) --*

      The Amazon Resource Name (ARN) of the configuration used for the cluster. This field
      isn't visible in this preview release.

    - **ConfigurationRevision** *(integer) --*

      The revision of the configuration to use. This field isn't visible in this preview
      release.

    - **KafkaVersion** *(string) --*

      The version of Apache Kafka.
    """


_ClientDescribeClusterResponseClusterInfoEncryptionInfoEncryptionAtRestTypeDef = TypedDict(
    "_ClientDescribeClusterResponseClusterInfoEncryptionInfoEncryptionAtRestTypeDef",
    {"DataVolumeKMSKeyId": str},
    total=False,
)


class ClientDescribeClusterResponseClusterInfoEncryptionInfoEncryptionAtRestTypeDef(
    _ClientDescribeClusterResponseClusterInfoEncryptionInfoEncryptionAtRestTypeDef
):
    """
    Type definition for `ClientDescribeClusterResponseClusterInfoEncryptionInfo` `EncryptionAtRest`

    The data-volume encryption details.

    - **DataVolumeKMSKeyId** *(string) --*

      The ARN of the AWS KMS key for encrypting data at rest. If you don't specify a KMS key,
      MSK creates one for you and uses it.
    """


_ClientDescribeClusterResponseClusterInfoEncryptionInfoEncryptionInTransitTypeDef = TypedDict(
    "_ClientDescribeClusterResponseClusterInfoEncryptionInfoEncryptionInTransitTypeDef",
    {"ClientBroker": str, "InCluster": bool},
    total=False,
)


class ClientDescribeClusterResponseClusterInfoEncryptionInfoEncryptionInTransitTypeDef(
    _ClientDescribeClusterResponseClusterInfoEncryptionInfoEncryptionInTransitTypeDef
):
    """
    Type definition for `ClientDescribeClusterResponseClusterInfoEncryptionInfo` `EncryptionInTransit`

    The details for encryption in transit.

    - **ClientBroker** *(string) --*

      Indicates the encryption setting for data in transit between clients and brokers. The
      following are the possible values.

      TLS means that client-broker communication is enabled with TLS only.

      TLS_PLAINTEXT means that client-broker communication is enabled for both TLS-encrypted,
      as well as plaintext data.

      PLAINTEXT means that client-broker communication is enabled in plaintext only.

      The default value is TLS_PLAINTEXT.

    - **InCluster** *(boolean) --*

      When set to true, it indicates that data communication among the broker nodes of the
      cluster is encrypted. When set to false, the communication happens in plaintext.

      The default value is true.
    """


_ClientDescribeClusterResponseClusterInfoEncryptionInfoTypeDef = TypedDict(
    "_ClientDescribeClusterResponseClusterInfoEncryptionInfoTypeDef",
    {
        "EncryptionAtRest": ClientDescribeClusterResponseClusterInfoEncryptionInfoEncryptionAtRestTypeDef,
        "EncryptionInTransit": ClientDescribeClusterResponseClusterInfoEncryptionInfoEncryptionInTransitTypeDef,
    },
    total=False,
)


class ClientDescribeClusterResponseClusterInfoEncryptionInfoTypeDef(
    _ClientDescribeClusterResponseClusterInfoEncryptionInfoTypeDef
):
    """
    Type definition for `ClientDescribeClusterResponseClusterInfo` `EncryptionInfo`

    Includes all encryption-related information.

    - **EncryptionAtRest** *(dict) --*

      The data-volume encryption details.

      - **DataVolumeKMSKeyId** *(string) --*

        The ARN of the AWS KMS key for encrypting data at rest. If you don't specify a KMS key,
        MSK creates one for you and uses it.

    - **EncryptionInTransit** *(dict) --*

      The details for encryption in transit.

      - **ClientBroker** *(string) --*

        Indicates the encryption setting for data in transit between clients and brokers. The
        following are the possible values.

        TLS means that client-broker communication is enabled with TLS only.

        TLS_PLAINTEXT means that client-broker communication is enabled for both TLS-encrypted,
        as well as plaintext data.

        PLAINTEXT means that client-broker communication is enabled in plaintext only.

        The default value is TLS_PLAINTEXT.

      - **InCluster** *(boolean) --*

        When set to true, it indicates that data communication among the broker nodes of the
        cluster is encrypted. When set to false, the communication happens in plaintext.

        The default value is true.
    """


_ClientDescribeClusterResponseClusterInfoTypeDef = TypedDict(
    "_ClientDescribeClusterResponseClusterInfoTypeDef",
    {
        "ActiveOperationArn": str,
        "BrokerNodeGroupInfo": ClientDescribeClusterResponseClusterInfoBrokerNodeGroupInfoTypeDef,
        "ClientAuthentication": ClientDescribeClusterResponseClusterInfoClientAuthenticationTypeDef,
        "ClusterArn": str,
        "ClusterName": str,
        "CreationTime": datetime,
        "CurrentBrokerSoftwareInfo": ClientDescribeClusterResponseClusterInfoCurrentBrokerSoftwareInfoTypeDef,
        "CurrentVersion": str,
        "EncryptionInfo": ClientDescribeClusterResponseClusterInfoEncryptionInfoTypeDef,
        "EnhancedMonitoring": str,
        "NumberOfBrokerNodes": int,
        "State": str,
        "Tags": Dict[str, str],
        "ZookeeperConnectString": str,
    },
    total=False,
)


class ClientDescribeClusterResponseClusterInfoTypeDef(
    _ClientDescribeClusterResponseClusterInfoTypeDef
):
    """
    Type definition for `ClientDescribeClusterResponse` `ClusterInfo`

    The cluster information.

    - **ActiveOperationArn** *(string) --*

      Arn of active cluster operation.

    - **BrokerNodeGroupInfo** *(dict) --*

      Information about the broker nodes.

      - **BrokerAZDistribution** *(string) --*

        The distribution of broker nodes across Availability Zones. This is an optional
        parameter. If you don't specify it, Amazon MSK gives it the value DEFAULT. You can also
        explicitly set this parameter to the value DEFAULT. No other values are currently allowed.

        Amazon MSK distributes the broker nodes evenly across the Availability Zones that
        correspond to the subnets you provide when you create the cluster.

      - **ClientSubnets** *(list) --*

        The list of subnets to connect to in the client virtual private cloud (VPC). AWS creates
        elastic network interfaces inside these subnets. Client applications use elastic network
        interfaces to produce and consume data. Client subnets can't be in Availability Zone
        us-east-1e.

        - *(string) --*

      - **InstanceType** *(string) --*

        The type of Amazon EC2 instances to use for Kafka brokers. The following instance types
        are allowed: kafka.m5.large, kafka.m5.xlarge, kafka.m5.2xlarge, kafka.m5.4xlarge,
        kafka.m5.12xlarge, and kafka.m5.24xlarge.

      - **SecurityGroups** *(list) --*

        The AWS security groups to associate with the elastic network interfaces in order to
        specify who can connect to and communicate with the Amazon MSK cluster. If you don't
        specify a security group, Amazon MSK uses the default security group associated with the
        VPC.

        - *(string) --*

      - **StorageInfo** *(dict) --*

        Contains information about storage volumes attached to MSK broker nodes.

        - **EbsStorageInfo** *(dict) --*

          EBS volume information.

          - **VolumeSize** *(integer) --*

            The size in GiB of the EBS volume for the data drive on each broker node.

    - **ClientAuthentication** *(dict) --*

      Includes all client authentication information.

      - **Tls** *(dict) --*

        Details for ClientAuthentication using TLS.

        - **CertificateAuthorityArnList** *(list) --*

          List of ACM Certificate Authority ARNs.

          - *(string) --*

    - **ClusterArn** *(string) --*

      The Amazon Resource Name (ARN) that uniquely identifies the cluster.

    - **ClusterName** *(string) --*

      The name of the cluster.

    - **CreationTime** *(datetime) --*

      The time when the cluster was created.

    - **CurrentBrokerSoftwareInfo** *(dict) --*

      Information about the version of software currently deployed on the Kafka brokers in the
      cluster.

      - **ConfigurationArn** *(string) --*

        The Amazon Resource Name (ARN) of the configuration used for the cluster. This field
        isn't visible in this preview release.

      - **ConfigurationRevision** *(integer) --*

        The revision of the configuration to use. This field isn't visible in this preview
        release.

      - **KafkaVersion** *(string) --*

        The version of Apache Kafka.

    - **CurrentVersion** *(string) --*

      The current version of the MSK cluster.

    - **EncryptionInfo** *(dict) --*

      Includes all encryption-related information.

      - **EncryptionAtRest** *(dict) --*

        The data-volume encryption details.

        - **DataVolumeKMSKeyId** *(string) --*

          The ARN of the AWS KMS key for encrypting data at rest. If you don't specify a KMS key,
          MSK creates one for you and uses it.

      - **EncryptionInTransit** *(dict) --*

        The details for encryption in transit.

        - **ClientBroker** *(string) --*

          Indicates the encryption setting for data in transit between clients and brokers. The
          following are the possible values.

          TLS means that client-broker communication is enabled with TLS only.

          TLS_PLAINTEXT means that client-broker communication is enabled for both TLS-encrypted,
          as well as plaintext data.

          PLAINTEXT means that client-broker communication is enabled in plaintext only.

          The default value is TLS_PLAINTEXT.

        - **InCluster** *(boolean) --*

          When set to true, it indicates that data communication among the broker nodes of the
          cluster is encrypted. When set to false, the communication happens in plaintext.

          The default value is true.

    - **EnhancedMonitoring** *(string) --*

      Specifies which metrics are gathered for the MSK cluster. This property has three possible
      values: DEFAULT, PER_BROKER, and PER_TOPIC_PER_BROKER. For a list of the metrics associated
      with each of these three levels of monitoring, see `Monitoring
      <https://docs.aws.amazon.com/msk/latest/developerguide/monitoring.html>`__ .

    - **NumberOfBrokerNodes** *(integer) --*

      The number of broker nodes in the cluster.

    - **State** *(string) --*

      The state of the cluster. The possible states are CREATING, ACTIVE, and FAILED.

    - **Tags** *(dict) --*

      Tags attached to the cluster.

      - *(string) --*

        - *(string) --*

    - **ZookeeperConnectString** *(string) --*

      The connection string to use to connect to the Apache ZooKeeper cluster.
    """


_ClientDescribeClusterResponseTypeDef = TypedDict(
    "_ClientDescribeClusterResponseTypeDef",
    {"ClusterInfo": ClientDescribeClusterResponseClusterInfoTypeDef},
    total=False,
)


class ClientDescribeClusterResponseTypeDef(_ClientDescribeClusterResponseTypeDef):
    """
    Type definition for `ClientDescribeCluster` `Response`

    Successful response.

    - **ClusterInfo** *(dict) --*

      The cluster information.

      - **ActiveOperationArn** *(string) --*

        Arn of active cluster operation.

      - **BrokerNodeGroupInfo** *(dict) --*

        Information about the broker nodes.

        - **BrokerAZDistribution** *(string) --*

          The distribution of broker nodes across Availability Zones. This is an optional
          parameter. If you don't specify it, Amazon MSK gives it the value DEFAULT. You can also
          explicitly set this parameter to the value DEFAULT. No other values are currently allowed.

          Amazon MSK distributes the broker nodes evenly across the Availability Zones that
          correspond to the subnets you provide when you create the cluster.

        - **ClientSubnets** *(list) --*

          The list of subnets to connect to in the client virtual private cloud (VPC). AWS creates
          elastic network interfaces inside these subnets. Client applications use elastic network
          interfaces to produce and consume data. Client subnets can't be in Availability Zone
          us-east-1e.

          - *(string) --*

        - **InstanceType** *(string) --*

          The type of Amazon EC2 instances to use for Kafka brokers. The following instance types
          are allowed: kafka.m5.large, kafka.m5.xlarge, kafka.m5.2xlarge, kafka.m5.4xlarge,
          kafka.m5.12xlarge, and kafka.m5.24xlarge.

        - **SecurityGroups** *(list) --*

          The AWS security groups to associate with the elastic network interfaces in order to
          specify who can connect to and communicate with the Amazon MSK cluster. If you don't
          specify a security group, Amazon MSK uses the default security group associated with the
          VPC.

          - *(string) --*

        - **StorageInfo** *(dict) --*

          Contains information about storage volumes attached to MSK broker nodes.

          - **EbsStorageInfo** *(dict) --*

            EBS volume information.

            - **VolumeSize** *(integer) --*

              The size in GiB of the EBS volume for the data drive on each broker node.

      - **ClientAuthentication** *(dict) --*

        Includes all client authentication information.

        - **Tls** *(dict) --*

          Details for ClientAuthentication using TLS.

          - **CertificateAuthorityArnList** *(list) --*

            List of ACM Certificate Authority ARNs.

            - *(string) --*

      - **ClusterArn** *(string) --*

        The Amazon Resource Name (ARN) that uniquely identifies the cluster.

      - **ClusterName** *(string) --*

        The name of the cluster.

      - **CreationTime** *(datetime) --*

        The time when the cluster was created.

      - **CurrentBrokerSoftwareInfo** *(dict) --*

        Information about the version of software currently deployed on the Kafka brokers in the
        cluster.

        - **ConfigurationArn** *(string) --*

          The Amazon Resource Name (ARN) of the configuration used for the cluster. This field
          isn't visible in this preview release.

        - **ConfigurationRevision** *(integer) --*

          The revision of the configuration to use. This field isn't visible in this preview
          release.

        - **KafkaVersion** *(string) --*

          The version of Apache Kafka.

      - **CurrentVersion** *(string) --*

        The current version of the MSK cluster.

      - **EncryptionInfo** *(dict) --*

        Includes all encryption-related information.

        - **EncryptionAtRest** *(dict) --*

          The data-volume encryption details.

          - **DataVolumeKMSKeyId** *(string) --*

            The ARN of the AWS KMS key for encrypting data at rest. If you don't specify a KMS key,
            MSK creates one for you and uses it.

        - **EncryptionInTransit** *(dict) --*

          The details for encryption in transit.

          - **ClientBroker** *(string) --*

            Indicates the encryption setting for data in transit between clients and brokers. The
            following are the possible values.

            TLS means that client-broker communication is enabled with TLS only.

            TLS_PLAINTEXT means that client-broker communication is enabled for both TLS-encrypted,
            as well as plaintext data.

            PLAINTEXT means that client-broker communication is enabled in plaintext only.

            The default value is TLS_PLAINTEXT.

          - **InCluster** *(boolean) --*

            When set to true, it indicates that data communication among the broker nodes of the
            cluster is encrypted. When set to false, the communication happens in plaintext.

            The default value is true.

      - **EnhancedMonitoring** *(string) --*

        Specifies which metrics are gathered for the MSK cluster. This property has three possible
        values: DEFAULT, PER_BROKER, and PER_TOPIC_PER_BROKER. For a list of the metrics associated
        with each of these three levels of monitoring, see `Monitoring
        <https://docs.aws.amazon.com/msk/latest/developerguide/monitoring.html>`__ .

      - **NumberOfBrokerNodes** *(integer) --*

        The number of broker nodes in the cluster.

      - **State** *(string) --*

        The state of the cluster. The possible states are CREATING, ACTIVE, and FAILED.

      - **Tags** *(dict) --*

        Tags attached to the cluster.

        - *(string) --*

          - *(string) --*

      - **ZookeeperConnectString** *(string) --*

        The connection string to use to connect to the Apache ZooKeeper cluster.
    """


_ClientDescribeConfigurationResponseLatestRevisionTypeDef = TypedDict(
    "_ClientDescribeConfigurationResponseLatestRevisionTypeDef",
    {"CreationTime": datetime, "Description": str, "Revision": int},
    total=False,
)


class ClientDescribeConfigurationResponseLatestRevisionTypeDef(
    _ClientDescribeConfigurationResponseLatestRevisionTypeDef
):
    """
    Type definition for `ClientDescribeConfigurationResponse` `LatestRevision`

    Latest revision of the configuration.

    - **CreationTime** *(datetime) --*

      The time when the configuration revision was created.

    - **Description** *(string) --*

      The description of the configuration revision.

    - **Revision** *(integer) --*

      The revision number.
    """


_ClientDescribeConfigurationResponseTypeDef = TypedDict(
    "_ClientDescribeConfigurationResponseTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "Description": str,
        "KafkaVersions": List[str],
        "LatestRevision": ClientDescribeConfigurationResponseLatestRevisionTypeDef,
        "Name": str,
    },
    total=False,
)


class ClientDescribeConfigurationResponseTypeDef(
    _ClientDescribeConfigurationResponseTypeDef
):
    """
    Type definition for `ClientDescribeConfiguration` `Response`

    200 response

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the configuration.

    - **CreationTime** *(datetime) --*

      The time when the configuration was created.

    - **Description** *(string) --*

      The description of the configuration.

    - **KafkaVersions** *(list) --*

      The versions of Apache Kafka with which you can use this MSK configuration.

      - *(string) --*

    - **LatestRevision** *(dict) --*

      Latest revision of the configuration.

      - **CreationTime** *(datetime) --*

        The time when the configuration revision was created.

      - **Description** *(string) --*

        The description of the configuration revision.

      - **Revision** *(integer) --*

        The revision number.

    - **Name** *(string) --*

      The name of the configuration.
    """


_ClientDescribeConfigurationRevisionResponseTypeDef = TypedDict(
    "_ClientDescribeConfigurationRevisionResponseTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "Description": str,
        "Revision": int,
        "ServerProperties": bytes,
    },
    total=False,
)


class ClientDescribeConfigurationRevisionResponseTypeDef(
    _ClientDescribeConfigurationRevisionResponseTypeDef
):
    """
    Type definition for `ClientDescribeConfigurationRevision` `Response`

    200 response

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the configuration.

    - **CreationTime** *(datetime) --*

      The time when the configuration was created.

    - **Description** *(string) --*

      The description of the configuration.

    - **Revision** *(integer) --*

      The revision number.

    - **ServerProperties** *(bytes) --*

      Contents of the server.propertiesfile. When using the API, you must ensure that the contents
      of the file are base64 encoded. When using the AWS Management Console, the SDK, or the AWS
      CLI, the contents of server.propertiescan be in plaintext.
    """


_ClientGetBootstrapBrokersResponseTypeDef = TypedDict(
    "_ClientGetBootstrapBrokersResponseTypeDef",
    {"BootstrapBrokerString": str, "BootstrapBrokerStringTls": str},
    total=False,
)


class ClientGetBootstrapBrokersResponseTypeDef(
    _ClientGetBootstrapBrokersResponseTypeDef
):
    """
    Type definition for `ClientGetBootstrapBrokers` `Response`

    Successful response.

    - **BootstrapBrokerString** *(string) --*

      A string containing one or more hostname:port pairs.

    - **BootstrapBrokerStringTls** *(string) --*

      A string containing one or more DNS names (or IP) and TLS port pairs.
    """


_ClientListClusterOperationsResponseClusterOperationInfoListErrorInfoTypeDef = TypedDict(
    "_ClientListClusterOperationsResponseClusterOperationInfoListErrorInfoTypeDef",
    {"ErrorCode": str, "ErrorString": str},
    total=False,
)


class ClientListClusterOperationsResponseClusterOperationInfoListErrorInfoTypeDef(
    _ClientListClusterOperationsResponseClusterOperationInfoListErrorInfoTypeDef
):
    """
    Type definition for `ClientListClusterOperationsResponseClusterOperationInfoList` `ErrorInfo`

    Describes the error if the operation fails.

    - **ErrorCode** *(string) --*

      A number describing the error programmatically.

    - **ErrorString** *(string) --*

      An optional field to provide more details about the error.
    """


_ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoBrokerEBSVolumeInfoTypeDef = TypedDict(
    "_ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoBrokerEBSVolumeInfoTypeDef",
    {"KafkaBrokerNodeId": str, "VolumeSizeGB": int},
    total=False,
)


class ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoBrokerEBSVolumeInfoTypeDef(
    _ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoBrokerEBSVolumeInfoTypeDef
):
    """
    Type definition for `ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfo` `BrokerEBSVolumeInfo`

    Specifies the EBS volume upgrade information. The broker identifier must be set to
    the keyword ALL. This means the changes apply to all the brokers in the cluster.

    - **KafkaBrokerNodeId** *(string) --*

      The ID of the broker to update.

    - **VolumeSizeGB** *(integer) --*

      Size of the EBS volume to update.
    """


_ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoConfigurationInfoTypeDef = TypedDict(
    "_ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoConfigurationInfoTypeDef",
    {"Arn": str, "Revision": int},
    total=False,
)


class ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoConfigurationInfoTypeDef(
    _ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoConfigurationInfoTypeDef
):
    """
    Type definition for `ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfo` `ConfigurationInfo`

    Information about the changes in the configuration of the brokers.

    - **Arn** *(string) --*

      ARN of the configuration to use.

    - **Revision** *(integer) --*

      The revision of the configuration to use.
    """


_ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoTypeDef = TypedDict(
    "_ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoTypeDef",
    {
        "BrokerEBSVolumeInfo": List[
            ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoBrokerEBSVolumeInfoTypeDef
        ],
        "ConfigurationInfo": ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoConfigurationInfoTypeDef,
        "NumberOfBrokerNodes": int,
    },
    total=False,
)


class ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoTypeDef(
    _ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoTypeDef
):
    """
    Type definition for `ClientListClusterOperationsResponseClusterOperationInfoList` `SourceClusterInfo`

    Information about cluster attributes before a cluster is updated.

    - **BrokerEBSVolumeInfo** *(list) --*

      Specifies the size of the EBS volume and the ID of the associated broker.

      - *(dict) --*

        Specifies the EBS volume upgrade information. The broker identifier must be set to
        the keyword ALL. This means the changes apply to all the brokers in the cluster.

        - **KafkaBrokerNodeId** *(string) --*

          The ID of the broker to update.

        - **VolumeSizeGB** *(integer) --*

          Size of the EBS volume to update.

    - **ConfigurationInfo** *(dict) --*

      Information about the changes in the configuration of the brokers.

      - **Arn** *(string) --*

        ARN of the configuration to use.

      - **Revision** *(integer) --*

        The revision of the configuration to use.

    - **NumberOfBrokerNodes** *(integer) --*

      The number of broker nodes in the cluster.
    """


_ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoBrokerEBSVolumeInfoTypeDef = TypedDict(
    "_ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoBrokerEBSVolumeInfoTypeDef",
    {"KafkaBrokerNodeId": str, "VolumeSizeGB": int},
    total=False,
)


class ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoBrokerEBSVolumeInfoTypeDef(
    _ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoBrokerEBSVolumeInfoTypeDef
):
    """
    Type definition for `ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfo` `BrokerEBSVolumeInfo`

    Specifies the EBS volume upgrade information. The broker identifier must be set to
    the keyword ALL. This means the changes apply to all the brokers in the cluster.

    - **KafkaBrokerNodeId** *(string) --*

      The ID of the broker to update.

    - **VolumeSizeGB** *(integer) --*

      Size of the EBS volume to update.
    """


_ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoConfigurationInfoTypeDef = TypedDict(
    "_ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoConfigurationInfoTypeDef",
    {"Arn": str, "Revision": int},
    total=False,
)


class ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoConfigurationInfoTypeDef(
    _ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoConfigurationInfoTypeDef
):
    """
    Type definition for `ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfo` `ConfigurationInfo`

    Information about the changes in the configuration of the brokers.

    - **Arn** *(string) --*

      ARN of the configuration to use.

    - **Revision** *(integer) --*

      The revision of the configuration to use.
    """


_ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoTypeDef = TypedDict(
    "_ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoTypeDef",
    {
        "BrokerEBSVolumeInfo": List[
            ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoBrokerEBSVolumeInfoTypeDef
        ],
        "ConfigurationInfo": ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoConfigurationInfoTypeDef,
        "NumberOfBrokerNodes": int,
    },
    total=False,
)


class ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoTypeDef(
    _ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoTypeDef
):
    """
    Type definition for `ClientListClusterOperationsResponseClusterOperationInfoList` `TargetClusterInfo`

    Information about cluster attributes after a cluster is updated.

    - **BrokerEBSVolumeInfo** *(list) --*

      Specifies the size of the EBS volume and the ID of the associated broker.

      - *(dict) --*

        Specifies the EBS volume upgrade information. The broker identifier must be set to
        the keyword ALL. This means the changes apply to all the brokers in the cluster.

        - **KafkaBrokerNodeId** *(string) --*

          The ID of the broker to update.

        - **VolumeSizeGB** *(integer) --*

          Size of the EBS volume to update.

    - **ConfigurationInfo** *(dict) --*

      Information about the changes in the configuration of the brokers.

      - **Arn** *(string) --*

        ARN of the configuration to use.

      - **Revision** *(integer) --*

        The revision of the configuration to use.

    - **NumberOfBrokerNodes** *(integer) --*

      The number of broker nodes in the cluster.
    """


_ClientListClusterOperationsResponseClusterOperationInfoListTypeDef = TypedDict(
    "_ClientListClusterOperationsResponseClusterOperationInfoListTypeDef",
    {
        "ClientRequestId": str,
        "ClusterArn": str,
        "CreationTime": datetime,
        "EndTime": datetime,
        "ErrorInfo": ClientListClusterOperationsResponseClusterOperationInfoListErrorInfoTypeDef,
        "OperationArn": str,
        "OperationState": str,
        "OperationType": str,
        "SourceClusterInfo": ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoTypeDef,
        "TargetClusterInfo": ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoTypeDef,
    },
    total=False,
)


class ClientListClusterOperationsResponseClusterOperationInfoListTypeDef(
    _ClientListClusterOperationsResponseClusterOperationInfoListTypeDef
):
    """
    Type definition for `ClientListClusterOperationsResponse` `ClusterOperationInfoList`

    Returns information about a cluster operation.

    - **ClientRequestId** *(string) --*

      The ID of the API request that triggered this operation.

    - **ClusterArn** *(string) --*

      ARN of the cluster.

    - **CreationTime** *(datetime) --*

      The time that the operation was created.

    - **EndTime** *(datetime) --*

      The time at which the operation finished.

    - **ErrorInfo** *(dict) --*

      Describes the error if the operation fails.

      - **ErrorCode** *(string) --*

        A number describing the error programmatically.

      - **ErrorString** *(string) --*

        An optional field to provide more details about the error.

    - **OperationArn** *(string) --*

      ARN of the cluster operation.

    - **OperationState** *(string) --*

      State of the cluster operation.

    - **OperationType** *(string) --*

      Type of the cluster operation.

    - **SourceClusterInfo** *(dict) --*

      Information about cluster attributes before a cluster is updated.

      - **BrokerEBSVolumeInfo** *(list) --*

        Specifies the size of the EBS volume and the ID of the associated broker.

        - *(dict) --*

          Specifies the EBS volume upgrade information. The broker identifier must be set to
          the keyword ALL. This means the changes apply to all the brokers in the cluster.

          - **KafkaBrokerNodeId** *(string) --*

            The ID of the broker to update.

          - **VolumeSizeGB** *(integer) --*

            Size of the EBS volume to update.

      - **ConfigurationInfo** *(dict) --*

        Information about the changes in the configuration of the brokers.

        - **Arn** *(string) --*

          ARN of the configuration to use.

        - **Revision** *(integer) --*

          The revision of the configuration to use.

      - **NumberOfBrokerNodes** *(integer) --*

        The number of broker nodes in the cluster.

    - **TargetClusterInfo** *(dict) --*

      Information about cluster attributes after a cluster is updated.

      - **BrokerEBSVolumeInfo** *(list) --*

        Specifies the size of the EBS volume and the ID of the associated broker.

        - *(dict) --*

          Specifies the EBS volume upgrade information. The broker identifier must be set to
          the keyword ALL. This means the changes apply to all the brokers in the cluster.

          - **KafkaBrokerNodeId** *(string) --*

            The ID of the broker to update.

          - **VolumeSizeGB** *(integer) --*

            Size of the EBS volume to update.

      - **ConfigurationInfo** *(dict) --*

        Information about the changes in the configuration of the brokers.

        - **Arn** *(string) --*

          ARN of the configuration to use.

        - **Revision** *(integer) --*

          The revision of the configuration to use.

      - **NumberOfBrokerNodes** *(integer) --*

        The number of broker nodes in the cluster.
    """


_ClientListClusterOperationsResponseTypeDef = TypedDict(
    "_ClientListClusterOperationsResponseTypeDef",
    {
        "ClusterOperationInfoList": List[
            ClientListClusterOperationsResponseClusterOperationInfoListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListClusterOperationsResponseTypeDef(
    _ClientListClusterOperationsResponseTypeDef
):
    """
    Type definition for `ClientListClusterOperations` `Response`

    Successful response.

    - **ClusterOperationInfoList** *(list) --*

      An array of cluster operation information objects.

      - *(dict) --*

        Returns information about a cluster operation.

        - **ClientRequestId** *(string) --*

          The ID of the API request that triggered this operation.

        - **ClusterArn** *(string) --*

          ARN of the cluster.

        - **CreationTime** *(datetime) --*

          The time that the operation was created.

        - **EndTime** *(datetime) --*

          The time at which the operation finished.

        - **ErrorInfo** *(dict) --*

          Describes the error if the operation fails.

          - **ErrorCode** *(string) --*

            A number describing the error programmatically.

          - **ErrorString** *(string) --*

            An optional field to provide more details about the error.

        - **OperationArn** *(string) --*

          ARN of the cluster operation.

        - **OperationState** *(string) --*

          State of the cluster operation.

        - **OperationType** *(string) --*

          Type of the cluster operation.

        - **SourceClusterInfo** *(dict) --*

          Information about cluster attributes before a cluster is updated.

          - **BrokerEBSVolumeInfo** *(list) --*

            Specifies the size of the EBS volume and the ID of the associated broker.

            - *(dict) --*

              Specifies the EBS volume upgrade information. The broker identifier must be set to
              the keyword ALL. This means the changes apply to all the brokers in the cluster.

              - **KafkaBrokerNodeId** *(string) --*

                The ID of the broker to update.

              - **VolumeSizeGB** *(integer) --*

                Size of the EBS volume to update.

          - **ConfigurationInfo** *(dict) --*

            Information about the changes in the configuration of the brokers.

            - **Arn** *(string) --*

              ARN of the configuration to use.

            - **Revision** *(integer) --*

              The revision of the configuration to use.

          - **NumberOfBrokerNodes** *(integer) --*

            The number of broker nodes in the cluster.

        - **TargetClusterInfo** *(dict) --*

          Information about cluster attributes after a cluster is updated.

          - **BrokerEBSVolumeInfo** *(list) --*

            Specifies the size of the EBS volume and the ID of the associated broker.

            - *(dict) --*

              Specifies the EBS volume upgrade information. The broker identifier must be set to
              the keyword ALL. This means the changes apply to all the brokers in the cluster.

              - **KafkaBrokerNodeId** *(string) --*

                The ID of the broker to update.

              - **VolumeSizeGB** *(integer) --*

                Size of the EBS volume to update.

          - **ConfigurationInfo** *(dict) --*

            Information about the changes in the configuration of the brokers.

            - **Arn** *(string) --*

              ARN of the configuration to use.

            - **Revision** *(integer) --*

              The revision of the configuration to use.

          - **NumberOfBrokerNodes** *(integer) --*

            The number of broker nodes in the cluster.

    - **NextToken** *(string) --*

      If the response of ListClusterOperations is truncated, it returns a NextToken in the
      response. This Nexttoken should be sent in the subsequent request to ListClusterOperations.
    """


_ClientListClustersResponseClusterInfoListBrokerNodeGroupInfoStorageInfoEbsStorageInfoTypeDef = TypedDict(
    "_ClientListClustersResponseClusterInfoListBrokerNodeGroupInfoStorageInfoEbsStorageInfoTypeDef",
    {"VolumeSize": int},
    total=False,
)


class ClientListClustersResponseClusterInfoListBrokerNodeGroupInfoStorageInfoEbsStorageInfoTypeDef(
    _ClientListClustersResponseClusterInfoListBrokerNodeGroupInfoStorageInfoEbsStorageInfoTypeDef
):
    """
    Type definition for `ClientListClustersResponseClusterInfoListBrokerNodeGroupInfoStorageInfo` `EbsStorageInfo`

    EBS volume information.

    - **VolumeSize** *(integer) --*

      The size in GiB of the EBS volume for the data drive on each broker node.
    """


_ClientListClustersResponseClusterInfoListBrokerNodeGroupInfoStorageInfoTypeDef = TypedDict(
    "_ClientListClustersResponseClusterInfoListBrokerNodeGroupInfoStorageInfoTypeDef",
    {
        "EbsStorageInfo": ClientListClustersResponseClusterInfoListBrokerNodeGroupInfoStorageInfoEbsStorageInfoTypeDef
    },
    total=False,
)


class ClientListClustersResponseClusterInfoListBrokerNodeGroupInfoStorageInfoTypeDef(
    _ClientListClustersResponseClusterInfoListBrokerNodeGroupInfoStorageInfoTypeDef
):
    """
    Type definition for `ClientListClustersResponseClusterInfoListBrokerNodeGroupInfo` `StorageInfo`

    Contains information about storage volumes attached to MSK broker nodes.

    - **EbsStorageInfo** *(dict) --*

      EBS volume information.

      - **VolumeSize** *(integer) --*

        The size in GiB of the EBS volume for the data drive on each broker node.
    """


_ClientListClustersResponseClusterInfoListBrokerNodeGroupInfoTypeDef = TypedDict(
    "_ClientListClustersResponseClusterInfoListBrokerNodeGroupInfoTypeDef",
    {
        "BrokerAZDistribution": str,
        "ClientSubnets": List[str],
        "InstanceType": str,
        "SecurityGroups": List[str],
        "StorageInfo": ClientListClustersResponseClusterInfoListBrokerNodeGroupInfoStorageInfoTypeDef,
    },
    total=False,
)


class ClientListClustersResponseClusterInfoListBrokerNodeGroupInfoTypeDef(
    _ClientListClustersResponseClusterInfoListBrokerNodeGroupInfoTypeDef
):
    """
    Type definition for `ClientListClustersResponseClusterInfoList` `BrokerNodeGroupInfo`

    Information about the broker nodes.

    - **BrokerAZDistribution** *(string) --*

      The distribution of broker nodes across Availability Zones. This is an optional
      parameter. If you don't specify it, Amazon MSK gives it the value DEFAULT. You can also
      explicitly set this parameter to the value DEFAULT. No other values are currently
      allowed.

      Amazon MSK distributes the broker nodes evenly across the Availability Zones that
      correspond to the subnets you provide when you create the cluster.

    - **ClientSubnets** *(list) --*

      The list of subnets to connect to in the client virtual private cloud (VPC). AWS
      creates elastic network interfaces inside these subnets. Client applications use
      elastic network interfaces to produce and consume data. Client subnets can't be in
      Availability Zone us-east-1e.

      - *(string) --*

    - **InstanceType** *(string) --*

      The type of Amazon EC2 instances to use for Kafka brokers. The following instance types
      are allowed: kafka.m5.large, kafka.m5.xlarge, kafka.m5.2xlarge, kafka.m5.4xlarge,
      kafka.m5.12xlarge, and kafka.m5.24xlarge.

    - **SecurityGroups** *(list) --*

      The AWS security groups to associate with the elastic network interfaces in order to
      specify who can connect to and communicate with the Amazon MSK cluster. If you don't
      specify a security group, Amazon MSK uses the default security group associated with
      the VPC.

      - *(string) --*

    - **StorageInfo** *(dict) --*

      Contains information about storage volumes attached to MSK broker nodes.

      - **EbsStorageInfo** *(dict) --*

        EBS volume information.

        - **VolumeSize** *(integer) --*

          The size in GiB of the EBS volume for the data drive on each broker node.
    """


_ClientListClustersResponseClusterInfoListClientAuthenticationTlsTypeDef = TypedDict(
    "_ClientListClustersResponseClusterInfoListClientAuthenticationTlsTypeDef",
    {"CertificateAuthorityArnList": List[str]},
    total=False,
)


class ClientListClustersResponseClusterInfoListClientAuthenticationTlsTypeDef(
    _ClientListClustersResponseClusterInfoListClientAuthenticationTlsTypeDef
):
    """
    Type definition for `ClientListClustersResponseClusterInfoListClientAuthentication` `Tls`

    Details for ClientAuthentication using TLS.

    - **CertificateAuthorityArnList** *(list) --*

      List of ACM Certificate Authority ARNs.

      - *(string) --*
    """


_ClientListClustersResponseClusterInfoListClientAuthenticationTypeDef = TypedDict(
    "_ClientListClustersResponseClusterInfoListClientAuthenticationTypeDef",
    {"Tls": ClientListClustersResponseClusterInfoListClientAuthenticationTlsTypeDef},
    total=False,
)


class ClientListClustersResponseClusterInfoListClientAuthenticationTypeDef(
    _ClientListClustersResponseClusterInfoListClientAuthenticationTypeDef
):
    """
    Type definition for `ClientListClustersResponseClusterInfoList` `ClientAuthentication`

    Includes all client authentication information.

    - **Tls** *(dict) --*

      Details for ClientAuthentication using TLS.

      - **CertificateAuthorityArnList** *(list) --*

        List of ACM Certificate Authority ARNs.

        - *(string) --*
    """


_ClientListClustersResponseClusterInfoListCurrentBrokerSoftwareInfoTypeDef = TypedDict(
    "_ClientListClustersResponseClusterInfoListCurrentBrokerSoftwareInfoTypeDef",
    {"ConfigurationArn": str, "ConfigurationRevision": int, "KafkaVersion": str},
    total=False,
)


class ClientListClustersResponseClusterInfoListCurrentBrokerSoftwareInfoTypeDef(
    _ClientListClustersResponseClusterInfoListCurrentBrokerSoftwareInfoTypeDef
):
    """
    Type definition for `ClientListClustersResponseClusterInfoList` `CurrentBrokerSoftwareInfo`

    Information about the version of software currently deployed on the Kafka brokers in the
    cluster.

    - **ConfigurationArn** *(string) --*

      The Amazon Resource Name (ARN) of the configuration used for the cluster. This field
      isn't visible in this preview release.

    - **ConfigurationRevision** *(integer) --*

      The revision of the configuration to use. This field isn't visible in this preview
      release.

    - **KafkaVersion** *(string) --*

      The version of Apache Kafka.
    """


_ClientListClustersResponseClusterInfoListEncryptionInfoEncryptionAtRestTypeDef = TypedDict(
    "_ClientListClustersResponseClusterInfoListEncryptionInfoEncryptionAtRestTypeDef",
    {"DataVolumeKMSKeyId": str},
    total=False,
)


class ClientListClustersResponseClusterInfoListEncryptionInfoEncryptionAtRestTypeDef(
    _ClientListClustersResponseClusterInfoListEncryptionInfoEncryptionAtRestTypeDef
):
    """
    Type definition for `ClientListClustersResponseClusterInfoListEncryptionInfo` `EncryptionAtRest`

    The data-volume encryption details.

    - **DataVolumeKMSKeyId** *(string) --*

      The ARN of the AWS KMS key for encrypting data at rest. If you don't specify a KMS
      key, MSK creates one for you and uses it.
    """


_ClientListClustersResponseClusterInfoListEncryptionInfoEncryptionInTransitTypeDef = TypedDict(
    "_ClientListClustersResponseClusterInfoListEncryptionInfoEncryptionInTransitTypeDef",
    {"ClientBroker": str, "InCluster": bool},
    total=False,
)


class ClientListClustersResponseClusterInfoListEncryptionInfoEncryptionInTransitTypeDef(
    _ClientListClustersResponseClusterInfoListEncryptionInfoEncryptionInTransitTypeDef
):
    """
    Type definition for `ClientListClustersResponseClusterInfoListEncryptionInfo` `EncryptionInTransit`

    The details for encryption in transit.

    - **ClientBroker** *(string) --*

      Indicates the encryption setting for data in transit between clients and brokers. The
      following are the possible values.

      TLS means that client-broker communication is enabled with TLS only.

      TLS_PLAINTEXT means that client-broker communication is enabled for both
      TLS-encrypted, as well as plaintext data.

      PLAINTEXT means that client-broker communication is enabled in plaintext only.

      The default value is TLS_PLAINTEXT.

    - **InCluster** *(boolean) --*

      When set to true, it indicates that data communication among the broker nodes of the
      cluster is encrypted. When set to false, the communication happens in plaintext.

      The default value is true.
    """


_ClientListClustersResponseClusterInfoListEncryptionInfoTypeDef = TypedDict(
    "_ClientListClustersResponseClusterInfoListEncryptionInfoTypeDef",
    {
        "EncryptionAtRest": ClientListClustersResponseClusterInfoListEncryptionInfoEncryptionAtRestTypeDef,
        "EncryptionInTransit": ClientListClustersResponseClusterInfoListEncryptionInfoEncryptionInTransitTypeDef,
    },
    total=False,
)


class ClientListClustersResponseClusterInfoListEncryptionInfoTypeDef(
    _ClientListClustersResponseClusterInfoListEncryptionInfoTypeDef
):
    """
    Type definition for `ClientListClustersResponseClusterInfoList` `EncryptionInfo`

    Includes all encryption-related information.

    - **EncryptionAtRest** *(dict) --*

      The data-volume encryption details.

      - **DataVolumeKMSKeyId** *(string) --*

        The ARN of the AWS KMS key for encrypting data at rest. If you don't specify a KMS
        key, MSK creates one for you and uses it.

    - **EncryptionInTransit** *(dict) --*

      The details for encryption in transit.

      - **ClientBroker** *(string) --*

        Indicates the encryption setting for data in transit between clients and brokers. The
        following are the possible values.

        TLS means that client-broker communication is enabled with TLS only.

        TLS_PLAINTEXT means that client-broker communication is enabled for both
        TLS-encrypted, as well as plaintext data.

        PLAINTEXT means that client-broker communication is enabled in plaintext only.

        The default value is TLS_PLAINTEXT.

      - **InCluster** *(boolean) --*

        When set to true, it indicates that data communication among the broker nodes of the
        cluster is encrypted. When set to false, the communication happens in plaintext.

        The default value is true.
    """


_ClientListClustersResponseClusterInfoListTypeDef = TypedDict(
    "_ClientListClustersResponseClusterInfoListTypeDef",
    {
        "ActiveOperationArn": str,
        "BrokerNodeGroupInfo": ClientListClustersResponseClusterInfoListBrokerNodeGroupInfoTypeDef,
        "ClientAuthentication": ClientListClustersResponseClusterInfoListClientAuthenticationTypeDef,
        "ClusterArn": str,
        "ClusterName": str,
        "CreationTime": datetime,
        "CurrentBrokerSoftwareInfo": ClientListClustersResponseClusterInfoListCurrentBrokerSoftwareInfoTypeDef,
        "CurrentVersion": str,
        "EncryptionInfo": ClientListClustersResponseClusterInfoListEncryptionInfoTypeDef,
        "EnhancedMonitoring": str,
        "NumberOfBrokerNodes": int,
        "State": str,
        "Tags": Dict[str, str],
        "ZookeeperConnectString": str,
    },
    total=False,
)


class ClientListClustersResponseClusterInfoListTypeDef(
    _ClientListClustersResponseClusterInfoListTypeDef
):
    """
    Type definition for `ClientListClustersResponse` `ClusterInfoList`

    Returns information about a cluster.

    - **ActiveOperationArn** *(string) --*

      Arn of active cluster operation.

    - **BrokerNodeGroupInfo** *(dict) --*

      Information about the broker nodes.

      - **BrokerAZDistribution** *(string) --*

        The distribution of broker nodes across Availability Zones. This is an optional
        parameter. If you don't specify it, Amazon MSK gives it the value DEFAULT. You can also
        explicitly set this parameter to the value DEFAULT. No other values are currently
        allowed.

        Amazon MSK distributes the broker nodes evenly across the Availability Zones that
        correspond to the subnets you provide when you create the cluster.

      - **ClientSubnets** *(list) --*

        The list of subnets to connect to in the client virtual private cloud (VPC). AWS
        creates elastic network interfaces inside these subnets. Client applications use
        elastic network interfaces to produce and consume data. Client subnets can't be in
        Availability Zone us-east-1e.

        - *(string) --*

      - **InstanceType** *(string) --*

        The type of Amazon EC2 instances to use for Kafka brokers. The following instance types
        are allowed: kafka.m5.large, kafka.m5.xlarge, kafka.m5.2xlarge, kafka.m5.4xlarge,
        kafka.m5.12xlarge, and kafka.m5.24xlarge.

      - **SecurityGroups** *(list) --*

        The AWS security groups to associate with the elastic network interfaces in order to
        specify who can connect to and communicate with the Amazon MSK cluster. If you don't
        specify a security group, Amazon MSK uses the default security group associated with
        the VPC.

        - *(string) --*

      - **StorageInfo** *(dict) --*

        Contains information about storage volumes attached to MSK broker nodes.

        - **EbsStorageInfo** *(dict) --*

          EBS volume information.

          - **VolumeSize** *(integer) --*

            The size in GiB of the EBS volume for the data drive on each broker node.

    - **ClientAuthentication** *(dict) --*

      Includes all client authentication information.

      - **Tls** *(dict) --*

        Details for ClientAuthentication using TLS.

        - **CertificateAuthorityArnList** *(list) --*

          List of ACM Certificate Authority ARNs.

          - *(string) --*

    - **ClusterArn** *(string) --*

      The Amazon Resource Name (ARN) that uniquely identifies the cluster.

    - **ClusterName** *(string) --*

      The name of the cluster.

    - **CreationTime** *(datetime) --*

      The time when the cluster was created.

    - **CurrentBrokerSoftwareInfo** *(dict) --*

      Information about the version of software currently deployed on the Kafka brokers in the
      cluster.

      - **ConfigurationArn** *(string) --*

        The Amazon Resource Name (ARN) of the configuration used for the cluster. This field
        isn't visible in this preview release.

      - **ConfigurationRevision** *(integer) --*

        The revision of the configuration to use. This field isn't visible in this preview
        release.

      - **KafkaVersion** *(string) --*

        The version of Apache Kafka.

    - **CurrentVersion** *(string) --*

      The current version of the MSK cluster.

    - **EncryptionInfo** *(dict) --*

      Includes all encryption-related information.

      - **EncryptionAtRest** *(dict) --*

        The data-volume encryption details.

        - **DataVolumeKMSKeyId** *(string) --*

          The ARN of the AWS KMS key for encrypting data at rest. If you don't specify a KMS
          key, MSK creates one for you and uses it.

      - **EncryptionInTransit** *(dict) --*

        The details for encryption in transit.

        - **ClientBroker** *(string) --*

          Indicates the encryption setting for data in transit between clients and brokers. The
          following are the possible values.

          TLS means that client-broker communication is enabled with TLS only.

          TLS_PLAINTEXT means that client-broker communication is enabled for both
          TLS-encrypted, as well as plaintext data.

          PLAINTEXT means that client-broker communication is enabled in plaintext only.

          The default value is TLS_PLAINTEXT.

        - **InCluster** *(boolean) --*

          When set to true, it indicates that data communication among the broker nodes of the
          cluster is encrypted. When set to false, the communication happens in plaintext.

          The default value is true.

    - **EnhancedMonitoring** *(string) --*

      Specifies which metrics are gathered for the MSK cluster. This property has three
      possible values: DEFAULT, PER_BROKER, and PER_TOPIC_PER_BROKER. For a list of the metrics
      associated with each of these three levels of monitoring, see `Monitoring
      <https://docs.aws.amazon.com/msk/latest/developerguide/monitoring.html>`__ .

    - **NumberOfBrokerNodes** *(integer) --*

      The number of broker nodes in the cluster.

    - **State** *(string) --*

      The state of the cluster. The possible states are CREATING, ACTIVE, and FAILED.

    - **Tags** *(dict) --*

      Tags attached to the cluster.

      - *(string) --*

        - *(string) --*

    - **ZookeeperConnectString** *(string) --*

      The connection string to use to connect to the Apache ZooKeeper cluster.
    """


_ClientListClustersResponseTypeDef = TypedDict(
    "_ClientListClustersResponseTypeDef",
    {
        "ClusterInfoList": List[ClientListClustersResponseClusterInfoListTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListClustersResponseTypeDef(_ClientListClustersResponseTypeDef):
    """
    Type definition for `ClientListClusters` `Response`

    Successful response.

    - **ClusterInfoList** *(list) --*

      Information on each of the MSK clusters in the response.

      - *(dict) --*

        Returns information about a cluster.

        - **ActiveOperationArn** *(string) --*

          Arn of active cluster operation.

        - **BrokerNodeGroupInfo** *(dict) --*

          Information about the broker nodes.

          - **BrokerAZDistribution** *(string) --*

            The distribution of broker nodes across Availability Zones. This is an optional
            parameter. If you don't specify it, Amazon MSK gives it the value DEFAULT. You can also
            explicitly set this parameter to the value DEFAULT. No other values are currently
            allowed.

            Amazon MSK distributes the broker nodes evenly across the Availability Zones that
            correspond to the subnets you provide when you create the cluster.

          - **ClientSubnets** *(list) --*

            The list of subnets to connect to in the client virtual private cloud (VPC). AWS
            creates elastic network interfaces inside these subnets. Client applications use
            elastic network interfaces to produce and consume data. Client subnets can't be in
            Availability Zone us-east-1e.

            - *(string) --*

          - **InstanceType** *(string) --*

            The type of Amazon EC2 instances to use for Kafka brokers. The following instance types
            are allowed: kafka.m5.large, kafka.m5.xlarge, kafka.m5.2xlarge, kafka.m5.4xlarge,
            kafka.m5.12xlarge, and kafka.m5.24xlarge.

          - **SecurityGroups** *(list) --*

            The AWS security groups to associate with the elastic network interfaces in order to
            specify who can connect to and communicate with the Amazon MSK cluster. If you don't
            specify a security group, Amazon MSK uses the default security group associated with
            the VPC.

            - *(string) --*

          - **StorageInfo** *(dict) --*

            Contains information about storage volumes attached to MSK broker nodes.

            - **EbsStorageInfo** *(dict) --*

              EBS volume information.

              - **VolumeSize** *(integer) --*

                The size in GiB of the EBS volume for the data drive on each broker node.

        - **ClientAuthentication** *(dict) --*

          Includes all client authentication information.

          - **Tls** *(dict) --*

            Details for ClientAuthentication using TLS.

            - **CertificateAuthorityArnList** *(list) --*

              List of ACM Certificate Authority ARNs.

              - *(string) --*

        - **ClusterArn** *(string) --*

          The Amazon Resource Name (ARN) that uniquely identifies the cluster.

        - **ClusterName** *(string) --*

          The name of the cluster.

        - **CreationTime** *(datetime) --*

          The time when the cluster was created.

        - **CurrentBrokerSoftwareInfo** *(dict) --*

          Information about the version of software currently deployed on the Kafka brokers in the
          cluster.

          - **ConfigurationArn** *(string) --*

            The Amazon Resource Name (ARN) of the configuration used for the cluster. This field
            isn't visible in this preview release.

          - **ConfigurationRevision** *(integer) --*

            The revision of the configuration to use. This field isn't visible in this preview
            release.

          - **KafkaVersion** *(string) --*

            The version of Apache Kafka.

        - **CurrentVersion** *(string) --*

          The current version of the MSK cluster.

        - **EncryptionInfo** *(dict) --*

          Includes all encryption-related information.

          - **EncryptionAtRest** *(dict) --*

            The data-volume encryption details.

            - **DataVolumeKMSKeyId** *(string) --*

              The ARN of the AWS KMS key for encrypting data at rest. If you don't specify a KMS
              key, MSK creates one for you and uses it.

          - **EncryptionInTransit** *(dict) --*

            The details for encryption in transit.

            - **ClientBroker** *(string) --*

              Indicates the encryption setting for data in transit between clients and brokers. The
              following are the possible values.

              TLS means that client-broker communication is enabled with TLS only.

              TLS_PLAINTEXT means that client-broker communication is enabled for both
              TLS-encrypted, as well as plaintext data.

              PLAINTEXT means that client-broker communication is enabled in plaintext only.

              The default value is TLS_PLAINTEXT.

            - **InCluster** *(boolean) --*

              When set to true, it indicates that data communication among the broker nodes of the
              cluster is encrypted. When set to false, the communication happens in plaintext.

              The default value is true.

        - **EnhancedMonitoring** *(string) --*

          Specifies which metrics are gathered for the MSK cluster. This property has three
          possible values: DEFAULT, PER_BROKER, and PER_TOPIC_PER_BROKER. For a list of the metrics
          associated with each of these three levels of monitoring, see `Monitoring
          <https://docs.aws.amazon.com/msk/latest/developerguide/monitoring.html>`__ .

        - **NumberOfBrokerNodes** *(integer) --*

          The number of broker nodes in the cluster.

        - **State** *(string) --*

          The state of the cluster. The possible states are CREATING, ACTIVE, and FAILED.

        - **Tags** *(dict) --*

          Tags attached to the cluster.

          - *(string) --*

            - *(string) --*

        - **ZookeeperConnectString** *(string) --*

          The connection string to use to connect to the Apache ZooKeeper cluster.

    - **NextToken** *(string) --*

      The paginated results marker. When the result of a ListClusters operation is truncated, the
      call returns NextToken in the response. To get another batch of clusters, provide this token
      in your next request.
    """


_ClientListConfigurationRevisionsResponseRevisionsTypeDef = TypedDict(
    "_ClientListConfigurationRevisionsResponseRevisionsTypeDef",
    {"CreationTime": datetime, "Description": str, "Revision": int},
    total=False,
)


class ClientListConfigurationRevisionsResponseRevisionsTypeDef(
    _ClientListConfigurationRevisionsResponseRevisionsTypeDef
):
    """
    Type definition for `ClientListConfigurationRevisionsResponse` `Revisions`

    Describes a configuration revision.

    - **CreationTime** *(datetime) --*

      The time when the configuration revision was created.

    - **Description** *(string) --*

      The description of the configuration revision.

    - **Revision** *(integer) --*

      The revision number.
    """


_ClientListConfigurationRevisionsResponseTypeDef = TypedDict(
    "_ClientListConfigurationRevisionsResponseTypeDef",
    {
        "NextToken": str,
        "Revisions": List[ClientListConfigurationRevisionsResponseRevisionsTypeDef],
    },
    total=False,
)


class ClientListConfigurationRevisionsResponseTypeDef(
    _ClientListConfigurationRevisionsResponseTypeDef
):
    """
    Type definition for `ClientListConfigurationRevisions` `Response`

    200 response

    - **NextToken** *(string) --*

      Paginated results marker.

    - **Revisions** *(list) --*

      List of ConfigurationRevision objects.

      - *(dict) --*

        Describes a configuration revision.

        - **CreationTime** *(datetime) --*

          The time when the configuration revision was created.

        - **Description** *(string) --*

          The description of the configuration revision.

        - **Revision** *(integer) --*

          The revision number.
    """


_ClientListConfigurationsResponseConfigurationsLatestRevisionTypeDef = TypedDict(
    "_ClientListConfigurationsResponseConfigurationsLatestRevisionTypeDef",
    {"CreationTime": datetime, "Description": str, "Revision": int},
    total=False,
)


class ClientListConfigurationsResponseConfigurationsLatestRevisionTypeDef(
    _ClientListConfigurationsResponseConfigurationsLatestRevisionTypeDef
):
    """
    Type definition for `ClientListConfigurationsResponseConfigurations` `LatestRevision`

    Latest revision of the configuration.

    - **CreationTime** *(datetime) --*

      The time when the configuration revision was created.

    - **Description** *(string) --*

      The description of the configuration revision.

    - **Revision** *(integer) --*

      The revision number.
    """


_ClientListConfigurationsResponseConfigurationsTypeDef = TypedDict(
    "_ClientListConfigurationsResponseConfigurationsTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "Description": str,
        "KafkaVersions": List[str],
        "LatestRevision": ClientListConfigurationsResponseConfigurationsLatestRevisionTypeDef,
        "Name": str,
    },
    total=False,
)


class ClientListConfigurationsResponseConfigurationsTypeDef(
    _ClientListConfigurationsResponseConfigurationsTypeDef
):
    """
    Type definition for `ClientListConfigurationsResponse` `Configurations`

    Represents an MSK Configuration.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the configuration.

    - **CreationTime** *(datetime) --*

      The time when the configuration was created.

    - **Description** *(string) --*

      The description of the configuration.

    - **KafkaVersions** *(list) --*

      An array of the versions of Apache Kafka with which you can use this MSK configuration.
      You can use this configuration for an MSK cluster only if the Apache Kafka version
      specified for the cluster appears in this array.

      - *(string) --*

    - **LatestRevision** *(dict) --*

      Latest revision of the configuration.

      - **CreationTime** *(datetime) --*

        The time when the configuration revision was created.

      - **Description** *(string) --*

        The description of the configuration revision.

      - **Revision** *(integer) --*

        The revision number.

    - **Name** *(string) --*

      The name of the configuration.
    """


_ClientListConfigurationsResponseTypeDef = TypedDict(
    "_ClientListConfigurationsResponseTypeDef",
    {
        "Configurations": List[ClientListConfigurationsResponseConfigurationsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListConfigurationsResponseTypeDef(_ClientListConfigurationsResponseTypeDef):
    """
    Type definition for `ClientListConfigurations` `Response`

    200 response

    - **Configurations** *(list) --*

      An array of MSK configurations.

      - *(dict) --*

        Represents an MSK Configuration.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of the configuration.

        - **CreationTime** *(datetime) --*

          The time when the configuration was created.

        - **Description** *(string) --*

          The description of the configuration.

        - **KafkaVersions** *(list) --*

          An array of the versions of Apache Kafka with which you can use this MSK configuration.
          You can use this configuration for an MSK cluster only if the Apache Kafka version
          specified for the cluster appears in this array.

          - *(string) --*

        - **LatestRevision** *(dict) --*

          Latest revision of the configuration.

          - **CreationTime** *(datetime) --*

            The time when the configuration revision was created.

          - **Description** *(string) --*

            The description of the configuration revision.

          - **Revision** *(integer) --*

            The revision number.

        - **Name** *(string) --*

          The name of the configuration.

    - **NextToken** *(string) --*

      The paginated results marker. When the result of a ListConfigurations operation is truncated,
      the call returns NextToken in the response. To get another batch of configurations, provide
      this token in your next request.
    """


_ClientListNodesResponseNodeInfoListBrokerNodeInfoCurrentBrokerSoftwareInfoTypeDef = TypedDict(
    "_ClientListNodesResponseNodeInfoListBrokerNodeInfoCurrentBrokerSoftwareInfoTypeDef",
    {"ConfigurationArn": str, "ConfigurationRevision": int, "KafkaVersion": str},
    total=False,
)


class ClientListNodesResponseNodeInfoListBrokerNodeInfoCurrentBrokerSoftwareInfoTypeDef(
    _ClientListNodesResponseNodeInfoListBrokerNodeInfoCurrentBrokerSoftwareInfoTypeDef
):
    """
    Type definition for `ClientListNodesResponseNodeInfoListBrokerNodeInfo` `CurrentBrokerSoftwareInfo`

    Information about the version of software currently deployed on the Kafka brokers in
    the cluster.

    - **ConfigurationArn** *(string) --*

      The Amazon Resource Name (ARN) of the configuration used for the cluster. This field
      isn't visible in this preview release.

    - **ConfigurationRevision** *(integer) --*

      The revision of the configuration to use. This field isn't visible in this preview
      release.

    - **KafkaVersion** *(string) --*

      The version of Apache Kafka.
    """


_ClientListNodesResponseNodeInfoListBrokerNodeInfoTypeDef = TypedDict(
    "_ClientListNodesResponseNodeInfoListBrokerNodeInfoTypeDef",
    {
        "AttachedENIId": str,
        "BrokerId": float,
        "ClientSubnet": str,
        "ClientVpcIpAddress": str,
        "CurrentBrokerSoftwareInfo": ClientListNodesResponseNodeInfoListBrokerNodeInfoCurrentBrokerSoftwareInfoTypeDef,
        "Endpoints": List[str],
    },
    total=False,
)


class ClientListNodesResponseNodeInfoListBrokerNodeInfoTypeDef(
    _ClientListNodesResponseNodeInfoListBrokerNodeInfoTypeDef
):
    """
    Type definition for `ClientListNodesResponseNodeInfoList` `BrokerNodeInfo`

    The broker node info.

    - **AttachedENIId** *(string) --*

      The attached elastic network interface of the broker.

    - **BrokerId** *(float) --*

      The ID of the broker.

    - **ClientSubnet** *(string) --*

      The client subnet to which this broker node belongs.

    - **ClientVpcIpAddress** *(string) --*

      The virtual private cloud (VPC) of the client.

    - **CurrentBrokerSoftwareInfo** *(dict) --*

      Information about the version of software currently deployed on the Kafka brokers in
      the cluster.

      - **ConfigurationArn** *(string) --*

        The Amazon Resource Name (ARN) of the configuration used for the cluster. This field
        isn't visible in this preview release.

      - **ConfigurationRevision** *(integer) --*

        The revision of the configuration to use. This field isn't visible in this preview
        release.

      - **KafkaVersion** *(string) --*

        The version of Apache Kafka.

    - **Endpoints** *(list) --*

      Endpoints for accessing the broker.

      - *(string) --*
    """


_ClientListNodesResponseNodeInfoListZookeeperNodeInfoTypeDef = TypedDict(
    "_ClientListNodesResponseNodeInfoListZookeeperNodeInfoTypeDef",
    {
        "AttachedENIId": str,
        "ClientVpcIpAddress": str,
        "Endpoints": List[str],
        "ZookeeperId": float,
        "ZookeeperVersion": str,
    },
    total=False,
)


class ClientListNodesResponseNodeInfoListZookeeperNodeInfoTypeDef(
    _ClientListNodesResponseNodeInfoListZookeeperNodeInfoTypeDef
):
    """
    Type definition for `ClientListNodesResponseNodeInfoList` `ZookeeperNodeInfo`

    The ZookeeperNodeInfo.

    - **AttachedENIId** *(string) --*

      The attached elastic network interface of the broker.

    - **ClientVpcIpAddress** *(string) --*

      The virtual private cloud (VPC) IP address of the client.

    - **Endpoints** *(list) --*

      Endpoints for accessing the ZooKeeper.

      - *(string) --*

    - **ZookeeperId** *(float) --*

      The role-specific ID for Zookeeper.

    - **ZookeeperVersion** *(string) --*

      The version of Zookeeper.
    """


_ClientListNodesResponseNodeInfoListTypeDef = TypedDict(
    "_ClientListNodesResponseNodeInfoListTypeDef",
    {
        "AddedToClusterTime": str,
        "BrokerNodeInfo": ClientListNodesResponseNodeInfoListBrokerNodeInfoTypeDef,
        "InstanceType": str,
        "NodeARN": str,
        "NodeType": str,
        "ZookeeperNodeInfo": ClientListNodesResponseNodeInfoListZookeeperNodeInfoTypeDef,
    },
    total=False,
)


class ClientListNodesResponseNodeInfoListTypeDef(
    _ClientListNodesResponseNodeInfoListTypeDef
):
    """
    Type definition for `ClientListNodesResponse` `NodeInfoList`

    The node information object.

    - **AddedToClusterTime** *(string) --*

      The start time.

    - **BrokerNodeInfo** *(dict) --*

      The broker node info.

      - **AttachedENIId** *(string) --*

        The attached elastic network interface of the broker.

      - **BrokerId** *(float) --*

        The ID of the broker.

      - **ClientSubnet** *(string) --*

        The client subnet to which this broker node belongs.

      - **ClientVpcIpAddress** *(string) --*

        The virtual private cloud (VPC) of the client.

      - **CurrentBrokerSoftwareInfo** *(dict) --*

        Information about the version of software currently deployed on the Kafka brokers in
        the cluster.

        - **ConfigurationArn** *(string) --*

          The Amazon Resource Name (ARN) of the configuration used for the cluster. This field
          isn't visible in this preview release.

        - **ConfigurationRevision** *(integer) --*

          The revision of the configuration to use. This field isn't visible in this preview
          release.

        - **KafkaVersion** *(string) --*

          The version of Apache Kafka.

      - **Endpoints** *(list) --*

        Endpoints for accessing the broker.

        - *(string) --*

    - **InstanceType** *(string) --*

      The instance type.

    - **NodeARN** *(string) --*

      The Amazon Resource Name (ARN) of the node.

    - **NodeType** *(string) --*

      The node type.

    - **ZookeeperNodeInfo** *(dict) --*

      The ZookeeperNodeInfo.

      - **AttachedENIId** *(string) --*

        The attached elastic network interface of the broker.

      - **ClientVpcIpAddress** *(string) --*

        The virtual private cloud (VPC) IP address of the client.

      - **Endpoints** *(list) --*

        Endpoints for accessing the ZooKeeper.

        - *(string) --*

      - **ZookeeperId** *(float) --*

        The role-specific ID for Zookeeper.

      - **ZookeeperVersion** *(string) --*

        The version of Zookeeper.
    """


_ClientListNodesResponseTypeDef = TypedDict(
    "_ClientListNodesResponseTypeDef",
    {
        "NextToken": str,
        "NodeInfoList": List[ClientListNodesResponseNodeInfoListTypeDef],
    },
    total=False,
)


class ClientListNodesResponseTypeDef(_ClientListNodesResponseTypeDef):
    """
    Type definition for `ClientListNodes` `Response`

    Successful response.

    - **NextToken** *(string) --*

      The paginated results marker. When the result of a ListNodes operation is truncated, the call
      returns NextToken in the response. To get another batch of nodes, provide this token in your
      next request.

    - **NodeInfoList** *(list) --*

      List containing a NodeInfo object.

      - *(dict) --*

        The node information object.

        - **AddedToClusterTime** *(string) --*

          The start time.

        - **BrokerNodeInfo** *(dict) --*

          The broker node info.

          - **AttachedENIId** *(string) --*

            The attached elastic network interface of the broker.

          - **BrokerId** *(float) --*

            The ID of the broker.

          - **ClientSubnet** *(string) --*

            The client subnet to which this broker node belongs.

          - **ClientVpcIpAddress** *(string) --*

            The virtual private cloud (VPC) of the client.

          - **CurrentBrokerSoftwareInfo** *(dict) --*

            Information about the version of software currently deployed on the Kafka brokers in
            the cluster.

            - **ConfigurationArn** *(string) --*

              The Amazon Resource Name (ARN) of the configuration used for the cluster. This field
              isn't visible in this preview release.

            - **ConfigurationRevision** *(integer) --*

              The revision of the configuration to use. This field isn't visible in this preview
              release.

            - **KafkaVersion** *(string) --*

              The version of Apache Kafka.

          - **Endpoints** *(list) --*

            Endpoints for accessing the broker.

            - *(string) --*

        - **InstanceType** *(string) --*

          The instance type.

        - **NodeARN** *(string) --*

          The Amazon Resource Name (ARN) of the node.

        - **NodeType** *(string) --*

          The node type.

        - **ZookeeperNodeInfo** *(dict) --*

          The ZookeeperNodeInfo.

          - **AttachedENIId** *(string) --*

            The attached elastic network interface of the broker.

          - **ClientVpcIpAddress** *(string) --*

            The virtual private cloud (VPC) IP address of the client.

          - **Endpoints** *(list) --*

            Endpoints for accessing the ZooKeeper.

            - *(string) --*

          - **ZookeeperId** *(float) --*

            The role-specific ID for Zookeeper.

          - **ZookeeperVersion** *(string) --*

            The version of Zookeeper.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)


class ClientListTagsForResourceResponseTypeDef(
    _ClientListTagsForResourceResponseTypeDef
):
    """
    Type definition for `ClientListTagsForResource` `Response`

    Success response.

    - **Tags** *(dict) --*

      The key-value pair for the resource tag.

      - *(string) --*

        - *(string) --*
    """


_ClientUpdateBrokerCountResponseTypeDef = TypedDict(
    "_ClientUpdateBrokerCountResponseTypeDef",
    {"ClusterArn": str, "ClusterOperationArn": str},
    total=False,
)


class ClientUpdateBrokerCountResponseTypeDef(_ClientUpdateBrokerCountResponseTypeDef):
    """
    Type definition for `ClientUpdateBrokerCount` `Response`

    Successful response.

    - **ClusterArn** *(string) --*

      The Amazon Resource Name (ARN) of the cluster.

    - **ClusterOperationArn** *(string) --*

      The Amazon Resource Name (ARN) of the cluster operation.
    """


_ClientUpdateBrokerStorageResponseTypeDef = TypedDict(
    "_ClientUpdateBrokerStorageResponseTypeDef",
    {"ClusterArn": str, "ClusterOperationArn": str},
    total=False,
)


class ClientUpdateBrokerStorageResponseTypeDef(
    _ClientUpdateBrokerStorageResponseTypeDef
):
    """
    Type definition for `ClientUpdateBrokerStorage` `Response`

    Successful response.

    - **ClusterArn** *(string) --*

      The Amazon Resource Name (ARN) of the cluster.

    - **ClusterOperationArn** *(string) --*

      The Amazon Resource Name (ARN) of the cluster operation.
    """


_ClientUpdateBrokerStorageTargetBrokerEBSVolumeInfoTypeDef = TypedDict(
    "_ClientUpdateBrokerStorageTargetBrokerEBSVolumeInfoTypeDef",
    {"KafkaBrokerNodeId": str, "VolumeSizeGB": int},
)


class ClientUpdateBrokerStorageTargetBrokerEBSVolumeInfoTypeDef(
    _ClientUpdateBrokerStorageTargetBrokerEBSVolumeInfoTypeDef
):
    """
    Type definition for `ClientUpdateBrokerStorage` `TargetBrokerEBSVolumeInfo`

    Specifies the EBS volume upgrade information. The broker identifier must be set to the keyword
    ALL. This means the changes apply to all the brokers in the cluster.

    - **KafkaBrokerNodeId** *(string) --* **[REQUIRED]**

      The ID of the broker to update.

    - **VolumeSizeGB** *(integer) --* **[REQUIRED]**

      Size of the EBS volume to update.
    """


_ClientUpdateClusterConfigurationConfigurationInfoTypeDef = TypedDict(
    "_ClientUpdateClusterConfigurationConfigurationInfoTypeDef",
    {"Arn": str, "Revision": int},
)


class ClientUpdateClusterConfigurationConfigurationInfoTypeDef(
    _ClientUpdateClusterConfigurationConfigurationInfoTypeDef
):
    """
    Type definition for `ClientUpdateClusterConfiguration` `ConfigurationInfo`

    Represents the configuration that you want MSK to use for the brokers in a cluster.

    - **Arn** *(string) --* **[REQUIRED]**

      ARN of the configuration to use.

    - **Revision** *(integer) --* **[REQUIRED]**

      The revision of the configuration to use.
    """


_ClientUpdateClusterConfigurationResponseTypeDef = TypedDict(
    "_ClientUpdateClusterConfigurationResponseTypeDef",
    {"ClusterArn": str, "ClusterOperationArn": str},
    total=False,
)


class ClientUpdateClusterConfigurationResponseTypeDef(
    _ClientUpdateClusterConfigurationResponseTypeDef
):
    """
    Type definition for `ClientUpdateClusterConfiguration` `Response`

    Successful response.

    - **ClusterArn** *(string) --*

      The Amazon Resource Name (ARN) of the cluster.

    - **ClusterOperationArn** *(string) --*

      The Amazon Resource Name (ARN) of the cluster operation.
    """


_ListClusterOperationsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListClusterOperationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListClusterOperationsPaginatePaginationConfigTypeDef(
    _ListClusterOperationsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListClusterOperationsPaginate` `PaginationConfig`

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


_ListClusterOperationsPaginateResponseClusterOperationInfoListErrorInfoTypeDef = TypedDict(
    "_ListClusterOperationsPaginateResponseClusterOperationInfoListErrorInfoTypeDef",
    {"ErrorCode": str, "ErrorString": str},
    total=False,
)


class ListClusterOperationsPaginateResponseClusterOperationInfoListErrorInfoTypeDef(
    _ListClusterOperationsPaginateResponseClusterOperationInfoListErrorInfoTypeDef
):
    """
    Type definition for `ListClusterOperationsPaginateResponseClusterOperationInfoList` `ErrorInfo`

    Describes the error if the operation fails.

    - **ErrorCode** *(string) --*

      A number describing the error programmatically.

    - **ErrorString** *(string) --*

      An optional field to provide more details about the error.
    """


_ListClusterOperationsPaginateResponseClusterOperationInfoListSourceClusterInfoBrokerEBSVolumeInfoTypeDef = TypedDict(
    "_ListClusterOperationsPaginateResponseClusterOperationInfoListSourceClusterInfoBrokerEBSVolumeInfoTypeDef",
    {"KafkaBrokerNodeId": str, "VolumeSizeGB": int},
    total=False,
)


class ListClusterOperationsPaginateResponseClusterOperationInfoListSourceClusterInfoBrokerEBSVolumeInfoTypeDef(
    _ListClusterOperationsPaginateResponseClusterOperationInfoListSourceClusterInfoBrokerEBSVolumeInfoTypeDef
):
    """
    Type definition for `ListClusterOperationsPaginateResponseClusterOperationInfoListSourceClusterInfo` `BrokerEBSVolumeInfo`

    Specifies the EBS volume upgrade information. The broker identifier must be set to
    the keyword ALL. This means the changes apply to all the brokers in the cluster.

    - **KafkaBrokerNodeId** *(string) --*

      The ID of the broker to update.

    - **VolumeSizeGB** *(integer) --*

      Size of the EBS volume to update.
    """


_ListClusterOperationsPaginateResponseClusterOperationInfoListSourceClusterInfoConfigurationInfoTypeDef = TypedDict(
    "_ListClusterOperationsPaginateResponseClusterOperationInfoListSourceClusterInfoConfigurationInfoTypeDef",
    {"Arn": str, "Revision": int},
    total=False,
)


class ListClusterOperationsPaginateResponseClusterOperationInfoListSourceClusterInfoConfigurationInfoTypeDef(
    _ListClusterOperationsPaginateResponseClusterOperationInfoListSourceClusterInfoConfigurationInfoTypeDef
):
    """
    Type definition for `ListClusterOperationsPaginateResponseClusterOperationInfoListSourceClusterInfo` `ConfigurationInfo`

    Information about the changes in the configuration of the brokers.

    - **Arn** *(string) --*

      ARN of the configuration to use.

    - **Revision** *(integer) --*

      The revision of the configuration to use.
    """


_ListClusterOperationsPaginateResponseClusterOperationInfoListSourceClusterInfoTypeDef = TypedDict(
    "_ListClusterOperationsPaginateResponseClusterOperationInfoListSourceClusterInfoTypeDef",
    {
        "BrokerEBSVolumeInfo": List[
            ListClusterOperationsPaginateResponseClusterOperationInfoListSourceClusterInfoBrokerEBSVolumeInfoTypeDef
        ],
        "ConfigurationInfo": ListClusterOperationsPaginateResponseClusterOperationInfoListSourceClusterInfoConfigurationInfoTypeDef,
        "NumberOfBrokerNodes": int,
    },
    total=False,
)


class ListClusterOperationsPaginateResponseClusterOperationInfoListSourceClusterInfoTypeDef(
    _ListClusterOperationsPaginateResponseClusterOperationInfoListSourceClusterInfoTypeDef
):
    """
    Type definition for `ListClusterOperationsPaginateResponseClusterOperationInfoList` `SourceClusterInfo`

    Information about cluster attributes before a cluster is updated.

    - **BrokerEBSVolumeInfo** *(list) --*

      Specifies the size of the EBS volume and the ID of the associated broker.

      - *(dict) --*

        Specifies the EBS volume upgrade information. The broker identifier must be set to
        the keyword ALL. This means the changes apply to all the brokers in the cluster.

        - **KafkaBrokerNodeId** *(string) --*

          The ID of the broker to update.

        - **VolumeSizeGB** *(integer) --*

          Size of the EBS volume to update.

    - **ConfigurationInfo** *(dict) --*

      Information about the changes in the configuration of the brokers.

      - **Arn** *(string) --*

        ARN of the configuration to use.

      - **Revision** *(integer) --*

        The revision of the configuration to use.

    - **NumberOfBrokerNodes** *(integer) --*

      The number of broker nodes in the cluster.
    """


_ListClusterOperationsPaginateResponseClusterOperationInfoListTargetClusterInfoBrokerEBSVolumeInfoTypeDef = TypedDict(
    "_ListClusterOperationsPaginateResponseClusterOperationInfoListTargetClusterInfoBrokerEBSVolumeInfoTypeDef",
    {"KafkaBrokerNodeId": str, "VolumeSizeGB": int},
    total=False,
)


class ListClusterOperationsPaginateResponseClusterOperationInfoListTargetClusterInfoBrokerEBSVolumeInfoTypeDef(
    _ListClusterOperationsPaginateResponseClusterOperationInfoListTargetClusterInfoBrokerEBSVolumeInfoTypeDef
):
    """
    Type definition for `ListClusterOperationsPaginateResponseClusterOperationInfoListTargetClusterInfo` `BrokerEBSVolumeInfo`

    Specifies the EBS volume upgrade information. The broker identifier must be set to
    the keyword ALL. This means the changes apply to all the brokers in the cluster.

    - **KafkaBrokerNodeId** *(string) --*

      The ID of the broker to update.

    - **VolumeSizeGB** *(integer) --*

      Size of the EBS volume to update.
    """


_ListClusterOperationsPaginateResponseClusterOperationInfoListTargetClusterInfoConfigurationInfoTypeDef = TypedDict(
    "_ListClusterOperationsPaginateResponseClusterOperationInfoListTargetClusterInfoConfigurationInfoTypeDef",
    {"Arn": str, "Revision": int},
    total=False,
)


class ListClusterOperationsPaginateResponseClusterOperationInfoListTargetClusterInfoConfigurationInfoTypeDef(
    _ListClusterOperationsPaginateResponseClusterOperationInfoListTargetClusterInfoConfigurationInfoTypeDef
):
    """
    Type definition for `ListClusterOperationsPaginateResponseClusterOperationInfoListTargetClusterInfo` `ConfigurationInfo`

    Information about the changes in the configuration of the brokers.

    - **Arn** *(string) --*

      ARN of the configuration to use.

    - **Revision** *(integer) --*

      The revision of the configuration to use.
    """


_ListClusterOperationsPaginateResponseClusterOperationInfoListTargetClusterInfoTypeDef = TypedDict(
    "_ListClusterOperationsPaginateResponseClusterOperationInfoListTargetClusterInfoTypeDef",
    {
        "BrokerEBSVolumeInfo": List[
            ListClusterOperationsPaginateResponseClusterOperationInfoListTargetClusterInfoBrokerEBSVolumeInfoTypeDef
        ],
        "ConfigurationInfo": ListClusterOperationsPaginateResponseClusterOperationInfoListTargetClusterInfoConfigurationInfoTypeDef,
        "NumberOfBrokerNodes": int,
    },
    total=False,
)


class ListClusterOperationsPaginateResponseClusterOperationInfoListTargetClusterInfoTypeDef(
    _ListClusterOperationsPaginateResponseClusterOperationInfoListTargetClusterInfoTypeDef
):
    """
    Type definition for `ListClusterOperationsPaginateResponseClusterOperationInfoList` `TargetClusterInfo`

    Information about cluster attributes after a cluster is updated.

    - **BrokerEBSVolumeInfo** *(list) --*

      Specifies the size of the EBS volume and the ID of the associated broker.

      - *(dict) --*

        Specifies the EBS volume upgrade information. The broker identifier must be set to
        the keyword ALL. This means the changes apply to all the brokers in the cluster.

        - **KafkaBrokerNodeId** *(string) --*

          The ID of the broker to update.

        - **VolumeSizeGB** *(integer) --*

          Size of the EBS volume to update.

    - **ConfigurationInfo** *(dict) --*

      Information about the changes in the configuration of the brokers.

      - **Arn** *(string) --*

        ARN of the configuration to use.

      - **Revision** *(integer) --*

        The revision of the configuration to use.

    - **NumberOfBrokerNodes** *(integer) --*

      The number of broker nodes in the cluster.
    """


_ListClusterOperationsPaginateResponseClusterOperationInfoListTypeDef = TypedDict(
    "_ListClusterOperationsPaginateResponseClusterOperationInfoListTypeDef",
    {
        "ClientRequestId": str,
        "ClusterArn": str,
        "CreationTime": datetime,
        "EndTime": datetime,
        "ErrorInfo": ListClusterOperationsPaginateResponseClusterOperationInfoListErrorInfoTypeDef,
        "OperationArn": str,
        "OperationState": str,
        "OperationType": str,
        "SourceClusterInfo": ListClusterOperationsPaginateResponseClusterOperationInfoListSourceClusterInfoTypeDef,
        "TargetClusterInfo": ListClusterOperationsPaginateResponseClusterOperationInfoListTargetClusterInfoTypeDef,
    },
    total=False,
)


class ListClusterOperationsPaginateResponseClusterOperationInfoListTypeDef(
    _ListClusterOperationsPaginateResponseClusterOperationInfoListTypeDef
):
    """
    Type definition for `ListClusterOperationsPaginateResponse` `ClusterOperationInfoList`

    Returns information about a cluster operation.

    - **ClientRequestId** *(string) --*

      The ID of the API request that triggered this operation.

    - **ClusterArn** *(string) --*

      ARN of the cluster.

    - **CreationTime** *(datetime) --*

      The time that the operation was created.

    - **EndTime** *(datetime) --*

      The time at which the operation finished.

    - **ErrorInfo** *(dict) --*

      Describes the error if the operation fails.

      - **ErrorCode** *(string) --*

        A number describing the error programmatically.

      - **ErrorString** *(string) --*

        An optional field to provide more details about the error.

    - **OperationArn** *(string) --*

      ARN of the cluster operation.

    - **OperationState** *(string) --*

      State of the cluster operation.

    - **OperationType** *(string) --*

      Type of the cluster operation.

    - **SourceClusterInfo** *(dict) --*

      Information about cluster attributes before a cluster is updated.

      - **BrokerEBSVolumeInfo** *(list) --*

        Specifies the size of the EBS volume and the ID of the associated broker.

        - *(dict) --*

          Specifies the EBS volume upgrade information. The broker identifier must be set to
          the keyword ALL. This means the changes apply to all the brokers in the cluster.

          - **KafkaBrokerNodeId** *(string) --*

            The ID of the broker to update.

          - **VolumeSizeGB** *(integer) --*

            Size of the EBS volume to update.

      - **ConfigurationInfo** *(dict) --*

        Information about the changes in the configuration of the brokers.

        - **Arn** *(string) --*

          ARN of the configuration to use.

        - **Revision** *(integer) --*

          The revision of the configuration to use.

      - **NumberOfBrokerNodes** *(integer) --*

        The number of broker nodes in the cluster.

    - **TargetClusterInfo** *(dict) --*

      Information about cluster attributes after a cluster is updated.

      - **BrokerEBSVolumeInfo** *(list) --*

        Specifies the size of the EBS volume and the ID of the associated broker.

        - *(dict) --*

          Specifies the EBS volume upgrade information. The broker identifier must be set to
          the keyword ALL. This means the changes apply to all the brokers in the cluster.

          - **KafkaBrokerNodeId** *(string) --*

            The ID of the broker to update.

          - **VolumeSizeGB** *(integer) --*

            Size of the EBS volume to update.

      - **ConfigurationInfo** *(dict) --*

        Information about the changes in the configuration of the brokers.

        - **Arn** *(string) --*

          ARN of the configuration to use.

        - **Revision** *(integer) --*

          The revision of the configuration to use.

      - **NumberOfBrokerNodes** *(integer) --*

        The number of broker nodes in the cluster.
    """


_ListClusterOperationsPaginateResponseTypeDef = TypedDict(
    "_ListClusterOperationsPaginateResponseTypeDef",
    {
        "ClusterOperationInfoList": List[
            ListClusterOperationsPaginateResponseClusterOperationInfoListTypeDef
        ]
    },
    total=False,
)


class ListClusterOperationsPaginateResponseTypeDef(
    _ListClusterOperationsPaginateResponseTypeDef
):
    """
    Type definition for `ListClusterOperationsPaginate` `Response`

    Successful response.

    - **ClusterOperationInfoList** *(list) --*

      An array of cluster operation information objects.

      - *(dict) --*

        Returns information about a cluster operation.

        - **ClientRequestId** *(string) --*

          The ID of the API request that triggered this operation.

        - **ClusterArn** *(string) --*

          ARN of the cluster.

        - **CreationTime** *(datetime) --*

          The time that the operation was created.

        - **EndTime** *(datetime) --*

          The time at which the operation finished.

        - **ErrorInfo** *(dict) --*

          Describes the error if the operation fails.

          - **ErrorCode** *(string) --*

            A number describing the error programmatically.

          - **ErrorString** *(string) --*

            An optional field to provide more details about the error.

        - **OperationArn** *(string) --*

          ARN of the cluster operation.

        - **OperationState** *(string) --*

          State of the cluster operation.

        - **OperationType** *(string) --*

          Type of the cluster operation.

        - **SourceClusterInfo** *(dict) --*

          Information about cluster attributes before a cluster is updated.

          - **BrokerEBSVolumeInfo** *(list) --*

            Specifies the size of the EBS volume and the ID of the associated broker.

            - *(dict) --*

              Specifies the EBS volume upgrade information. The broker identifier must be set to
              the keyword ALL. This means the changes apply to all the brokers in the cluster.

              - **KafkaBrokerNodeId** *(string) --*

                The ID of the broker to update.

              - **VolumeSizeGB** *(integer) --*

                Size of the EBS volume to update.

          - **ConfigurationInfo** *(dict) --*

            Information about the changes in the configuration of the brokers.

            - **Arn** *(string) --*

              ARN of the configuration to use.

            - **Revision** *(integer) --*

              The revision of the configuration to use.

          - **NumberOfBrokerNodes** *(integer) --*

            The number of broker nodes in the cluster.

        - **TargetClusterInfo** *(dict) --*

          Information about cluster attributes after a cluster is updated.

          - **BrokerEBSVolumeInfo** *(list) --*

            Specifies the size of the EBS volume and the ID of the associated broker.

            - *(dict) --*

              Specifies the EBS volume upgrade information. The broker identifier must be set to
              the keyword ALL. This means the changes apply to all the brokers in the cluster.

              - **KafkaBrokerNodeId** *(string) --*

                The ID of the broker to update.

              - **VolumeSizeGB** *(integer) --*

                Size of the EBS volume to update.

          - **ConfigurationInfo** *(dict) --*

            Information about the changes in the configuration of the brokers.

            - **Arn** *(string) --*

              ARN of the configuration to use.

            - **Revision** *(integer) --*

              The revision of the configuration to use.

          - **NumberOfBrokerNodes** *(integer) --*

            The number of broker nodes in the cluster.
    """


_ListClustersPaginatePaginationConfigTypeDef = TypedDict(
    "_ListClustersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListClustersPaginatePaginationConfigTypeDef(
    _ListClustersPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListClustersPaginate` `PaginationConfig`

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


_ListClustersPaginateResponseClusterInfoListBrokerNodeGroupInfoStorageInfoEbsStorageInfoTypeDef = TypedDict(
    "_ListClustersPaginateResponseClusterInfoListBrokerNodeGroupInfoStorageInfoEbsStorageInfoTypeDef",
    {"VolumeSize": int},
    total=False,
)


class ListClustersPaginateResponseClusterInfoListBrokerNodeGroupInfoStorageInfoEbsStorageInfoTypeDef(
    _ListClustersPaginateResponseClusterInfoListBrokerNodeGroupInfoStorageInfoEbsStorageInfoTypeDef
):
    """
    Type definition for `ListClustersPaginateResponseClusterInfoListBrokerNodeGroupInfoStorageInfo` `EbsStorageInfo`

    EBS volume information.

    - **VolumeSize** *(integer) --*

      The size in GiB of the EBS volume for the data drive on each broker node.
    """


_ListClustersPaginateResponseClusterInfoListBrokerNodeGroupInfoStorageInfoTypeDef = TypedDict(
    "_ListClustersPaginateResponseClusterInfoListBrokerNodeGroupInfoStorageInfoTypeDef",
    {
        "EbsStorageInfo": ListClustersPaginateResponseClusterInfoListBrokerNodeGroupInfoStorageInfoEbsStorageInfoTypeDef
    },
    total=False,
)


class ListClustersPaginateResponseClusterInfoListBrokerNodeGroupInfoStorageInfoTypeDef(
    _ListClustersPaginateResponseClusterInfoListBrokerNodeGroupInfoStorageInfoTypeDef
):
    """
    Type definition for `ListClustersPaginateResponseClusterInfoListBrokerNodeGroupInfo` `StorageInfo`

    Contains information about storage volumes attached to MSK broker nodes.

    - **EbsStorageInfo** *(dict) --*

      EBS volume information.

      - **VolumeSize** *(integer) --*

        The size in GiB of the EBS volume for the data drive on each broker node.
    """


_ListClustersPaginateResponseClusterInfoListBrokerNodeGroupInfoTypeDef = TypedDict(
    "_ListClustersPaginateResponseClusterInfoListBrokerNodeGroupInfoTypeDef",
    {
        "BrokerAZDistribution": str,
        "ClientSubnets": List[str],
        "InstanceType": str,
        "SecurityGroups": List[str],
        "StorageInfo": ListClustersPaginateResponseClusterInfoListBrokerNodeGroupInfoStorageInfoTypeDef,
    },
    total=False,
)


class ListClustersPaginateResponseClusterInfoListBrokerNodeGroupInfoTypeDef(
    _ListClustersPaginateResponseClusterInfoListBrokerNodeGroupInfoTypeDef
):
    """
    Type definition for `ListClustersPaginateResponseClusterInfoList` `BrokerNodeGroupInfo`

    Information about the broker nodes.

    - **BrokerAZDistribution** *(string) --*

      The distribution of broker nodes across Availability Zones. This is an optional
      parameter. If you don't specify it, Amazon MSK gives it the value DEFAULT. You can also
      explicitly set this parameter to the value DEFAULT. No other values are currently
      allowed.

      Amazon MSK distributes the broker nodes evenly across the Availability Zones that
      correspond to the subnets you provide when you create the cluster.

    - **ClientSubnets** *(list) --*

      The list of subnets to connect to in the client virtual private cloud (VPC). AWS
      creates elastic network interfaces inside these subnets. Client applications use
      elastic network interfaces to produce and consume data. Client subnets can't be in
      Availability Zone us-east-1e.

      - *(string) --*

    - **InstanceType** *(string) --*

      The type of Amazon EC2 instances to use for Kafka brokers. The following instance types
      are allowed: kafka.m5.large, kafka.m5.xlarge, kafka.m5.2xlarge, kafka.m5.4xlarge,
      kafka.m5.12xlarge, and kafka.m5.24xlarge.

    - **SecurityGroups** *(list) --*

      The AWS security groups to associate with the elastic network interfaces in order to
      specify who can connect to and communicate with the Amazon MSK cluster. If you don't
      specify a security group, Amazon MSK uses the default security group associated with
      the VPC.

      - *(string) --*

    - **StorageInfo** *(dict) --*

      Contains information about storage volumes attached to MSK broker nodes.

      - **EbsStorageInfo** *(dict) --*

        EBS volume information.

        - **VolumeSize** *(integer) --*

          The size in GiB of the EBS volume for the data drive on each broker node.
    """


_ListClustersPaginateResponseClusterInfoListClientAuthenticationTlsTypeDef = TypedDict(
    "_ListClustersPaginateResponseClusterInfoListClientAuthenticationTlsTypeDef",
    {"CertificateAuthorityArnList": List[str]},
    total=False,
)


class ListClustersPaginateResponseClusterInfoListClientAuthenticationTlsTypeDef(
    _ListClustersPaginateResponseClusterInfoListClientAuthenticationTlsTypeDef
):
    """
    Type definition for `ListClustersPaginateResponseClusterInfoListClientAuthentication` `Tls`

    Details for ClientAuthentication using TLS.

    - **CertificateAuthorityArnList** *(list) --*

      List of ACM Certificate Authority ARNs.

      - *(string) --*
    """


_ListClustersPaginateResponseClusterInfoListClientAuthenticationTypeDef = TypedDict(
    "_ListClustersPaginateResponseClusterInfoListClientAuthenticationTypeDef",
    {"Tls": ListClustersPaginateResponseClusterInfoListClientAuthenticationTlsTypeDef},
    total=False,
)


class ListClustersPaginateResponseClusterInfoListClientAuthenticationTypeDef(
    _ListClustersPaginateResponseClusterInfoListClientAuthenticationTypeDef
):
    """
    Type definition for `ListClustersPaginateResponseClusterInfoList` `ClientAuthentication`

    Includes all client authentication information.

    - **Tls** *(dict) --*

      Details for ClientAuthentication using TLS.

      - **CertificateAuthorityArnList** *(list) --*

        List of ACM Certificate Authority ARNs.

        - *(string) --*
    """


_ListClustersPaginateResponseClusterInfoListCurrentBrokerSoftwareInfoTypeDef = TypedDict(
    "_ListClustersPaginateResponseClusterInfoListCurrentBrokerSoftwareInfoTypeDef",
    {"ConfigurationArn": str, "ConfigurationRevision": int, "KafkaVersion": str},
    total=False,
)


class ListClustersPaginateResponseClusterInfoListCurrentBrokerSoftwareInfoTypeDef(
    _ListClustersPaginateResponseClusterInfoListCurrentBrokerSoftwareInfoTypeDef
):
    """
    Type definition for `ListClustersPaginateResponseClusterInfoList` `CurrentBrokerSoftwareInfo`

    Information about the version of software currently deployed on the Kafka brokers in the
    cluster.

    - **ConfigurationArn** *(string) --*

      The Amazon Resource Name (ARN) of the configuration used for the cluster. This field
      isn't visible in this preview release.

    - **ConfigurationRevision** *(integer) --*

      The revision of the configuration to use. This field isn't visible in this preview
      release.

    - **KafkaVersion** *(string) --*

      The version of Apache Kafka.
    """


_ListClustersPaginateResponseClusterInfoListEncryptionInfoEncryptionAtRestTypeDef = TypedDict(
    "_ListClustersPaginateResponseClusterInfoListEncryptionInfoEncryptionAtRestTypeDef",
    {"DataVolumeKMSKeyId": str},
    total=False,
)


class ListClustersPaginateResponseClusterInfoListEncryptionInfoEncryptionAtRestTypeDef(
    _ListClustersPaginateResponseClusterInfoListEncryptionInfoEncryptionAtRestTypeDef
):
    """
    Type definition for `ListClustersPaginateResponseClusterInfoListEncryptionInfo` `EncryptionAtRest`

    The data-volume encryption details.

    - **DataVolumeKMSKeyId** *(string) --*

      The ARN of the AWS KMS key for encrypting data at rest. If you don't specify a KMS
      key, MSK creates one for you and uses it.
    """


_ListClustersPaginateResponseClusterInfoListEncryptionInfoEncryptionInTransitTypeDef = TypedDict(
    "_ListClustersPaginateResponseClusterInfoListEncryptionInfoEncryptionInTransitTypeDef",
    {"ClientBroker": str, "InCluster": bool},
    total=False,
)


class ListClustersPaginateResponseClusterInfoListEncryptionInfoEncryptionInTransitTypeDef(
    _ListClustersPaginateResponseClusterInfoListEncryptionInfoEncryptionInTransitTypeDef
):
    """
    Type definition for `ListClustersPaginateResponseClusterInfoListEncryptionInfo` `EncryptionInTransit`

    The details for encryption in transit.

    - **ClientBroker** *(string) --*

      Indicates the encryption setting for data in transit between clients and brokers. The
      following are the possible values.

      TLS means that client-broker communication is enabled with TLS only.

      TLS_PLAINTEXT means that client-broker communication is enabled for both
      TLS-encrypted, as well as plaintext data.

      PLAINTEXT means that client-broker communication is enabled in plaintext only.

      The default value is TLS_PLAINTEXT.

    - **InCluster** *(boolean) --*

      When set to true, it indicates that data communication among the broker nodes of the
      cluster is encrypted. When set to false, the communication happens in plaintext.

      The default value is true.
    """


_ListClustersPaginateResponseClusterInfoListEncryptionInfoTypeDef = TypedDict(
    "_ListClustersPaginateResponseClusterInfoListEncryptionInfoTypeDef",
    {
        "EncryptionAtRest": ListClustersPaginateResponseClusterInfoListEncryptionInfoEncryptionAtRestTypeDef,
        "EncryptionInTransit": ListClustersPaginateResponseClusterInfoListEncryptionInfoEncryptionInTransitTypeDef,
    },
    total=False,
)


class ListClustersPaginateResponseClusterInfoListEncryptionInfoTypeDef(
    _ListClustersPaginateResponseClusterInfoListEncryptionInfoTypeDef
):
    """
    Type definition for `ListClustersPaginateResponseClusterInfoList` `EncryptionInfo`

    Includes all encryption-related information.

    - **EncryptionAtRest** *(dict) --*

      The data-volume encryption details.

      - **DataVolumeKMSKeyId** *(string) --*

        The ARN of the AWS KMS key for encrypting data at rest. If you don't specify a KMS
        key, MSK creates one for you and uses it.

    - **EncryptionInTransit** *(dict) --*

      The details for encryption in transit.

      - **ClientBroker** *(string) --*

        Indicates the encryption setting for data in transit between clients and brokers. The
        following are the possible values.

        TLS means that client-broker communication is enabled with TLS only.

        TLS_PLAINTEXT means that client-broker communication is enabled for both
        TLS-encrypted, as well as plaintext data.

        PLAINTEXT means that client-broker communication is enabled in plaintext only.

        The default value is TLS_PLAINTEXT.

      - **InCluster** *(boolean) --*

        When set to true, it indicates that data communication among the broker nodes of the
        cluster is encrypted. When set to false, the communication happens in plaintext.

        The default value is true.
    """


_ListClustersPaginateResponseClusterInfoListTypeDef = TypedDict(
    "_ListClustersPaginateResponseClusterInfoListTypeDef",
    {
        "ActiveOperationArn": str,
        "BrokerNodeGroupInfo": ListClustersPaginateResponseClusterInfoListBrokerNodeGroupInfoTypeDef,
        "ClientAuthentication": ListClustersPaginateResponseClusterInfoListClientAuthenticationTypeDef,
        "ClusterArn": str,
        "ClusterName": str,
        "CreationTime": datetime,
        "CurrentBrokerSoftwareInfo": ListClustersPaginateResponseClusterInfoListCurrentBrokerSoftwareInfoTypeDef,
        "CurrentVersion": str,
        "EncryptionInfo": ListClustersPaginateResponseClusterInfoListEncryptionInfoTypeDef,
        "EnhancedMonitoring": str,
        "NumberOfBrokerNodes": int,
        "State": str,
        "Tags": Dict[str, str],
        "ZookeeperConnectString": str,
    },
    total=False,
)


class ListClustersPaginateResponseClusterInfoListTypeDef(
    _ListClustersPaginateResponseClusterInfoListTypeDef
):
    """
    Type definition for `ListClustersPaginateResponse` `ClusterInfoList`

    Returns information about a cluster.

    - **ActiveOperationArn** *(string) --*

      Arn of active cluster operation.

    - **BrokerNodeGroupInfo** *(dict) --*

      Information about the broker nodes.

      - **BrokerAZDistribution** *(string) --*

        The distribution of broker nodes across Availability Zones. This is an optional
        parameter. If you don't specify it, Amazon MSK gives it the value DEFAULT. You can also
        explicitly set this parameter to the value DEFAULT. No other values are currently
        allowed.

        Amazon MSK distributes the broker nodes evenly across the Availability Zones that
        correspond to the subnets you provide when you create the cluster.

      - **ClientSubnets** *(list) --*

        The list of subnets to connect to in the client virtual private cloud (VPC). AWS
        creates elastic network interfaces inside these subnets. Client applications use
        elastic network interfaces to produce and consume data. Client subnets can't be in
        Availability Zone us-east-1e.

        - *(string) --*

      - **InstanceType** *(string) --*

        The type of Amazon EC2 instances to use for Kafka brokers. The following instance types
        are allowed: kafka.m5.large, kafka.m5.xlarge, kafka.m5.2xlarge, kafka.m5.4xlarge,
        kafka.m5.12xlarge, and kafka.m5.24xlarge.

      - **SecurityGroups** *(list) --*

        The AWS security groups to associate with the elastic network interfaces in order to
        specify who can connect to and communicate with the Amazon MSK cluster. If you don't
        specify a security group, Amazon MSK uses the default security group associated with
        the VPC.

        - *(string) --*

      - **StorageInfo** *(dict) --*

        Contains information about storage volumes attached to MSK broker nodes.

        - **EbsStorageInfo** *(dict) --*

          EBS volume information.

          - **VolumeSize** *(integer) --*

            The size in GiB of the EBS volume for the data drive on each broker node.

    - **ClientAuthentication** *(dict) --*

      Includes all client authentication information.

      - **Tls** *(dict) --*

        Details for ClientAuthentication using TLS.

        - **CertificateAuthorityArnList** *(list) --*

          List of ACM Certificate Authority ARNs.

          - *(string) --*

    - **ClusterArn** *(string) --*

      The Amazon Resource Name (ARN) that uniquely identifies the cluster.

    - **ClusterName** *(string) --*

      The name of the cluster.

    - **CreationTime** *(datetime) --*

      The time when the cluster was created.

    - **CurrentBrokerSoftwareInfo** *(dict) --*

      Information about the version of software currently deployed on the Kafka brokers in the
      cluster.

      - **ConfigurationArn** *(string) --*

        The Amazon Resource Name (ARN) of the configuration used for the cluster. This field
        isn't visible in this preview release.

      - **ConfigurationRevision** *(integer) --*

        The revision of the configuration to use. This field isn't visible in this preview
        release.

      - **KafkaVersion** *(string) --*

        The version of Apache Kafka.

    - **CurrentVersion** *(string) --*

      The current version of the MSK cluster.

    - **EncryptionInfo** *(dict) --*

      Includes all encryption-related information.

      - **EncryptionAtRest** *(dict) --*

        The data-volume encryption details.

        - **DataVolumeKMSKeyId** *(string) --*

          The ARN of the AWS KMS key for encrypting data at rest. If you don't specify a KMS
          key, MSK creates one for you and uses it.

      - **EncryptionInTransit** *(dict) --*

        The details for encryption in transit.

        - **ClientBroker** *(string) --*

          Indicates the encryption setting for data in transit between clients and brokers. The
          following are the possible values.

          TLS means that client-broker communication is enabled with TLS only.

          TLS_PLAINTEXT means that client-broker communication is enabled for both
          TLS-encrypted, as well as plaintext data.

          PLAINTEXT means that client-broker communication is enabled in plaintext only.

          The default value is TLS_PLAINTEXT.

        - **InCluster** *(boolean) --*

          When set to true, it indicates that data communication among the broker nodes of the
          cluster is encrypted. When set to false, the communication happens in plaintext.

          The default value is true.

    - **EnhancedMonitoring** *(string) --*

      Specifies which metrics are gathered for the MSK cluster. This property has three
      possible values: DEFAULT, PER_BROKER, and PER_TOPIC_PER_BROKER. For a list of the metrics
      associated with each of these three levels of monitoring, see `Monitoring
      <https://docs.aws.amazon.com/msk/latest/developerguide/monitoring.html>`__ .

    - **NumberOfBrokerNodes** *(integer) --*

      The number of broker nodes in the cluster.

    - **State** *(string) --*

      The state of the cluster. The possible states are CREATING, ACTIVE, and FAILED.

    - **Tags** *(dict) --*

      Tags attached to the cluster.

      - *(string) --*

        - *(string) --*

    - **ZookeeperConnectString** *(string) --*

      The connection string to use to connect to the Apache ZooKeeper cluster.
    """


_ListClustersPaginateResponseTypeDef = TypedDict(
    "_ListClustersPaginateResponseTypeDef",
    {"ClusterInfoList": List[ListClustersPaginateResponseClusterInfoListTypeDef]},
    total=False,
)


class ListClustersPaginateResponseTypeDef(_ListClustersPaginateResponseTypeDef):
    """
    Type definition for `ListClustersPaginate` `Response`

    Successful response.

    - **ClusterInfoList** *(list) --*

      Information on each of the MSK clusters in the response.

      - *(dict) --*

        Returns information about a cluster.

        - **ActiveOperationArn** *(string) --*

          Arn of active cluster operation.

        - **BrokerNodeGroupInfo** *(dict) --*

          Information about the broker nodes.

          - **BrokerAZDistribution** *(string) --*

            The distribution of broker nodes across Availability Zones. This is an optional
            parameter. If you don't specify it, Amazon MSK gives it the value DEFAULT. You can also
            explicitly set this parameter to the value DEFAULT. No other values are currently
            allowed.

            Amazon MSK distributes the broker nodes evenly across the Availability Zones that
            correspond to the subnets you provide when you create the cluster.

          - **ClientSubnets** *(list) --*

            The list of subnets to connect to in the client virtual private cloud (VPC). AWS
            creates elastic network interfaces inside these subnets. Client applications use
            elastic network interfaces to produce and consume data. Client subnets can't be in
            Availability Zone us-east-1e.

            - *(string) --*

          - **InstanceType** *(string) --*

            The type of Amazon EC2 instances to use for Kafka brokers. The following instance types
            are allowed: kafka.m5.large, kafka.m5.xlarge, kafka.m5.2xlarge, kafka.m5.4xlarge,
            kafka.m5.12xlarge, and kafka.m5.24xlarge.

          - **SecurityGroups** *(list) --*

            The AWS security groups to associate with the elastic network interfaces in order to
            specify who can connect to and communicate with the Amazon MSK cluster. If you don't
            specify a security group, Amazon MSK uses the default security group associated with
            the VPC.

            - *(string) --*

          - **StorageInfo** *(dict) --*

            Contains information about storage volumes attached to MSK broker nodes.

            - **EbsStorageInfo** *(dict) --*

              EBS volume information.

              - **VolumeSize** *(integer) --*

                The size in GiB of the EBS volume for the data drive on each broker node.

        - **ClientAuthentication** *(dict) --*

          Includes all client authentication information.

          - **Tls** *(dict) --*

            Details for ClientAuthentication using TLS.

            - **CertificateAuthorityArnList** *(list) --*

              List of ACM Certificate Authority ARNs.

              - *(string) --*

        - **ClusterArn** *(string) --*

          The Amazon Resource Name (ARN) that uniquely identifies the cluster.

        - **ClusterName** *(string) --*

          The name of the cluster.

        - **CreationTime** *(datetime) --*

          The time when the cluster was created.

        - **CurrentBrokerSoftwareInfo** *(dict) --*

          Information about the version of software currently deployed on the Kafka brokers in the
          cluster.

          - **ConfigurationArn** *(string) --*

            The Amazon Resource Name (ARN) of the configuration used for the cluster. This field
            isn't visible in this preview release.

          - **ConfigurationRevision** *(integer) --*

            The revision of the configuration to use. This field isn't visible in this preview
            release.

          - **KafkaVersion** *(string) --*

            The version of Apache Kafka.

        - **CurrentVersion** *(string) --*

          The current version of the MSK cluster.

        - **EncryptionInfo** *(dict) --*

          Includes all encryption-related information.

          - **EncryptionAtRest** *(dict) --*

            The data-volume encryption details.

            - **DataVolumeKMSKeyId** *(string) --*

              The ARN of the AWS KMS key for encrypting data at rest. If you don't specify a KMS
              key, MSK creates one for you and uses it.

          - **EncryptionInTransit** *(dict) --*

            The details for encryption in transit.

            - **ClientBroker** *(string) --*

              Indicates the encryption setting for data in transit between clients and brokers. The
              following are the possible values.

              TLS means that client-broker communication is enabled with TLS only.

              TLS_PLAINTEXT means that client-broker communication is enabled for both
              TLS-encrypted, as well as plaintext data.

              PLAINTEXT means that client-broker communication is enabled in plaintext only.

              The default value is TLS_PLAINTEXT.

            - **InCluster** *(boolean) --*

              When set to true, it indicates that data communication among the broker nodes of the
              cluster is encrypted. When set to false, the communication happens in plaintext.

              The default value is true.

        - **EnhancedMonitoring** *(string) --*

          Specifies which metrics are gathered for the MSK cluster. This property has three
          possible values: DEFAULT, PER_BROKER, and PER_TOPIC_PER_BROKER. For a list of the metrics
          associated with each of these three levels of monitoring, see `Monitoring
          <https://docs.aws.amazon.com/msk/latest/developerguide/monitoring.html>`__ .

        - **NumberOfBrokerNodes** *(integer) --*

          The number of broker nodes in the cluster.

        - **State** *(string) --*

          The state of the cluster. The possible states are CREATING, ACTIVE, and FAILED.

        - **Tags** *(dict) --*

          Tags attached to the cluster.

          - *(string) --*

            - *(string) --*

        - **ZookeeperConnectString** *(string) --*

          The connection string to use to connect to the Apache ZooKeeper cluster.
    """


_ListConfigurationRevisionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListConfigurationRevisionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListConfigurationRevisionsPaginatePaginationConfigTypeDef(
    _ListConfigurationRevisionsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListConfigurationRevisionsPaginate` `PaginationConfig`

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


_ListConfigurationRevisionsPaginateResponseRevisionsTypeDef = TypedDict(
    "_ListConfigurationRevisionsPaginateResponseRevisionsTypeDef",
    {"CreationTime": datetime, "Description": str, "Revision": int},
    total=False,
)


class ListConfigurationRevisionsPaginateResponseRevisionsTypeDef(
    _ListConfigurationRevisionsPaginateResponseRevisionsTypeDef
):
    """
    Type definition for `ListConfigurationRevisionsPaginateResponse` `Revisions`

    Describes a configuration revision.

    - **CreationTime** *(datetime) --*

      The time when the configuration revision was created.

    - **Description** *(string) --*

      The description of the configuration revision.

    - **Revision** *(integer) --*

      The revision number.
    """


_ListConfigurationRevisionsPaginateResponseTypeDef = TypedDict(
    "_ListConfigurationRevisionsPaginateResponseTypeDef",
    {"Revisions": List[ListConfigurationRevisionsPaginateResponseRevisionsTypeDef]},
    total=False,
)


class ListConfigurationRevisionsPaginateResponseTypeDef(
    _ListConfigurationRevisionsPaginateResponseTypeDef
):
    """
    Type definition for `ListConfigurationRevisionsPaginate` `Response`

    200 response

    - **Revisions** *(list) --*

      List of ConfigurationRevision objects.

      - *(dict) --*

        Describes a configuration revision.

        - **CreationTime** *(datetime) --*

          The time when the configuration revision was created.

        - **Description** *(string) --*

          The description of the configuration revision.

        - **Revision** *(integer) --*

          The revision number.
    """


_ListConfigurationsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListConfigurationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListConfigurationsPaginatePaginationConfigTypeDef(
    _ListConfigurationsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListConfigurationsPaginate` `PaginationConfig`

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


_ListConfigurationsPaginateResponseConfigurationsLatestRevisionTypeDef = TypedDict(
    "_ListConfigurationsPaginateResponseConfigurationsLatestRevisionTypeDef",
    {"CreationTime": datetime, "Description": str, "Revision": int},
    total=False,
)


class ListConfigurationsPaginateResponseConfigurationsLatestRevisionTypeDef(
    _ListConfigurationsPaginateResponseConfigurationsLatestRevisionTypeDef
):
    """
    Type definition for `ListConfigurationsPaginateResponseConfigurations` `LatestRevision`

    Latest revision of the configuration.

    - **CreationTime** *(datetime) --*

      The time when the configuration revision was created.

    - **Description** *(string) --*

      The description of the configuration revision.

    - **Revision** *(integer) --*

      The revision number.
    """


_ListConfigurationsPaginateResponseConfigurationsTypeDef = TypedDict(
    "_ListConfigurationsPaginateResponseConfigurationsTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "Description": str,
        "KafkaVersions": List[str],
        "LatestRevision": ListConfigurationsPaginateResponseConfigurationsLatestRevisionTypeDef,
        "Name": str,
    },
    total=False,
)


class ListConfigurationsPaginateResponseConfigurationsTypeDef(
    _ListConfigurationsPaginateResponseConfigurationsTypeDef
):
    """
    Type definition for `ListConfigurationsPaginateResponse` `Configurations`

    Represents an MSK Configuration.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the configuration.

    - **CreationTime** *(datetime) --*

      The time when the configuration was created.

    - **Description** *(string) --*

      The description of the configuration.

    - **KafkaVersions** *(list) --*

      An array of the versions of Apache Kafka with which you can use this MSK configuration.
      You can use this configuration for an MSK cluster only if the Apache Kafka version
      specified for the cluster appears in this array.

      - *(string) --*

    - **LatestRevision** *(dict) --*

      Latest revision of the configuration.

      - **CreationTime** *(datetime) --*

        The time when the configuration revision was created.

      - **Description** *(string) --*

        The description of the configuration revision.

      - **Revision** *(integer) --*

        The revision number.

    - **Name** *(string) --*

      The name of the configuration.
    """


_ListConfigurationsPaginateResponseTypeDef = TypedDict(
    "_ListConfigurationsPaginateResponseTypeDef",
    {"Configurations": List[ListConfigurationsPaginateResponseConfigurationsTypeDef]},
    total=False,
)


class ListConfigurationsPaginateResponseTypeDef(
    _ListConfigurationsPaginateResponseTypeDef
):
    """
    Type definition for `ListConfigurationsPaginate` `Response`

    200 response

    - **Configurations** *(list) --*

      An array of MSK configurations.

      - *(dict) --*

        Represents an MSK Configuration.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of the configuration.

        - **CreationTime** *(datetime) --*

          The time when the configuration was created.

        - **Description** *(string) --*

          The description of the configuration.

        - **KafkaVersions** *(list) --*

          An array of the versions of Apache Kafka with which you can use this MSK configuration.
          You can use this configuration for an MSK cluster only if the Apache Kafka version
          specified for the cluster appears in this array.

          - *(string) --*

        - **LatestRevision** *(dict) --*

          Latest revision of the configuration.

          - **CreationTime** *(datetime) --*

            The time when the configuration revision was created.

          - **Description** *(string) --*

            The description of the configuration revision.

          - **Revision** *(integer) --*

            The revision number.

        - **Name** *(string) --*

          The name of the configuration.
    """


_ListNodesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListNodesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListNodesPaginatePaginationConfigTypeDef(
    _ListNodesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListNodesPaginate` `PaginationConfig`

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


_ListNodesPaginateResponseNodeInfoListBrokerNodeInfoCurrentBrokerSoftwareInfoTypeDef = TypedDict(
    "_ListNodesPaginateResponseNodeInfoListBrokerNodeInfoCurrentBrokerSoftwareInfoTypeDef",
    {"ConfigurationArn": str, "ConfigurationRevision": int, "KafkaVersion": str},
    total=False,
)


class ListNodesPaginateResponseNodeInfoListBrokerNodeInfoCurrentBrokerSoftwareInfoTypeDef(
    _ListNodesPaginateResponseNodeInfoListBrokerNodeInfoCurrentBrokerSoftwareInfoTypeDef
):
    """
    Type definition for `ListNodesPaginateResponseNodeInfoListBrokerNodeInfo` `CurrentBrokerSoftwareInfo`

    Information about the version of software currently deployed on the Kafka brokers in
    the cluster.

    - **ConfigurationArn** *(string) --*

      The Amazon Resource Name (ARN) of the configuration used for the cluster. This field
      isn't visible in this preview release.

    - **ConfigurationRevision** *(integer) --*

      The revision of the configuration to use. This field isn't visible in this preview
      release.

    - **KafkaVersion** *(string) --*

      The version of Apache Kafka.
    """


_ListNodesPaginateResponseNodeInfoListBrokerNodeInfoTypeDef = TypedDict(
    "_ListNodesPaginateResponseNodeInfoListBrokerNodeInfoTypeDef",
    {
        "AttachedENIId": str,
        "BrokerId": float,
        "ClientSubnet": str,
        "ClientVpcIpAddress": str,
        "CurrentBrokerSoftwareInfo": ListNodesPaginateResponseNodeInfoListBrokerNodeInfoCurrentBrokerSoftwareInfoTypeDef,
        "Endpoints": List[str],
    },
    total=False,
)


class ListNodesPaginateResponseNodeInfoListBrokerNodeInfoTypeDef(
    _ListNodesPaginateResponseNodeInfoListBrokerNodeInfoTypeDef
):
    """
    Type definition for `ListNodesPaginateResponseNodeInfoList` `BrokerNodeInfo`

    The broker node info.

    - **AttachedENIId** *(string) --*

      The attached elastic network interface of the broker.

    - **BrokerId** *(float) --*

      The ID of the broker.

    - **ClientSubnet** *(string) --*

      The client subnet to which this broker node belongs.

    - **ClientVpcIpAddress** *(string) --*

      The virtual private cloud (VPC) of the client.

    - **CurrentBrokerSoftwareInfo** *(dict) --*

      Information about the version of software currently deployed on the Kafka brokers in
      the cluster.

      - **ConfigurationArn** *(string) --*

        The Amazon Resource Name (ARN) of the configuration used for the cluster. This field
        isn't visible in this preview release.

      - **ConfigurationRevision** *(integer) --*

        The revision of the configuration to use. This field isn't visible in this preview
        release.

      - **KafkaVersion** *(string) --*

        The version of Apache Kafka.

    - **Endpoints** *(list) --*

      Endpoints for accessing the broker.

      - *(string) --*
    """


_ListNodesPaginateResponseNodeInfoListZookeeperNodeInfoTypeDef = TypedDict(
    "_ListNodesPaginateResponseNodeInfoListZookeeperNodeInfoTypeDef",
    {
        "AttachedENIId": str,
        "ClientVpcIpAddress": str,
        "Endpoints": List[str],
        "ZookeeperId": float,
        "ZookeeperVersion": str,
    },
    total=False,
)


class ListNodesPaginateResponseNodeInfoListZookeeperNodeInfoTypeDef(
    _ListNodesPaginateResponseNodeInfoListZookeeperNodeInfoTypeDef
):
    """
    Type definition for `ListNodesPaginateResponseNodeInfoList` `ZookeeperNodeInfo`

    The ZookeeperNodeInfo.

    - **AttachedENIId** *(string) --*

      The attached elastic network interface of the broker.

    - **ClientVpcIpAddress** *(string) --*

      The virtual private cloud (VPC) IP address of the client.

    - **Endpoints** *(list) --*

      Endpoints for accessing the ZooKeeper.

      - *(string) --*

    - **ZookeeperId** *(float) --*

      The role-specific ID for Zookeeper.

    - **ZookeeperVersion** *(string) --*

      The version of Zookeeper.
    """


_ListNodesPaginateResponseNodeInfoListTypeDef = TypedDict(
    "_ListNodesPaginateResponseNodeInfoListTypeDef",
    {
        "AddedToClusterTime": str,
        "BrokerNodeInfo": ListNodesPaginateResponseNodeInfoListBrokerNodeInfoTypeDef,
        "InstanceType": str,
        "NodeARN": str,
        "NodeType": str,
        "ZookeeperNodeInfo": ListNodesPaginateResponseNodeInfoListZookeeperNodeInfoTypeDef,
    },
    total=False,
)


class ListNodesPaginateResponseNodeInfoListTypeDef(
    _ListNodesPaginateResponseNodeInfoListTypeDef
):
    """
    Type definition for `ListNodesPaginateResponse` `NodeInfoList`

    The node information object.

    - **AddedToClusterTime** *(string) --*

      The start time.

    - **BrokerNodeInfo** *(dict) --*

      The broker node info.

      - **AttachedENIId** *(string) --*

        The attached elastic network interface of the broker.

      - **BrokerId** *(float) --*

        The ID of the broker.

      - **ClientSubnet** *(string) --*

        The client subnet to which this broker node belongs.

      - **ClientVpcIpAddress** *(string) --*

        The virtual private cloud (VPC) of the client.

      - **CurrentBrokerSoftwareInfo** *(dict) --*

        Information about the version of software currently deployed on the Kafka brokers in
        the cluster.

        - **ConfigurationArn** *(string) --*

          The Amazon Resource Name (ARN) of the configuration used for the cluster. This field
          isn't visible in this preview release.

        - **ConfigurationRevision** *(integer) --*

          The revision of the configuration to use. This field isn't visible in this preview
          release.

        - **KafkaVersion** *(string) --*

          The version of Apache Kafka.

      - **Endpoints** *(list) --*

        Endpoints for accessing the broker.

        - *(string) --*

    - **InstanceType** *(string) --*

      The instance type.

    - **NodeARN** *(string) --*

      The Amazon Resource Name (ARN) of the node.

    - **NodeType** *(string) --*

      The node type.

    - **ZookeeperNodeInfo** *(dict) --*

      The ZookeeperNodeInfo.

      - **AttachedENIId** *(string) --*

        The attached elastic network interface of the broker.

      - **ClientVpcIpAddress** *(string) --*

        The virtual private cloud (VPC) IP address of the client.

      - **Endpoints** *(list) --*

        Endpoints for accessing the ZooKeeper.

        - *(string) --*

      - **ZookeeperId** *(float) --*

        The role-specific ID for Zookeeper.

      - **ZookeeperVersion** *(string) --*

        The version of Zookeeper.
    """


_ListNodesPaginateResponseTypeDef = TypedDict(
    "_ListNodesPaginateResponseTypeDef",
    {"NodeInfoList": List[ListNodesPaginateResponseNodeInfoListTypeDef]},
    total=False,
)


class ListNodesPaginateResponseTypeDef(_ListNodesPaginateResponseTypeDef):
    """
    Type definition for `ListNodesPaginate` `Response`

    Successful response.

    - **NodeInfoList** *(list) --*

      List containing a NodeInfo object.

      - *(dict) --*

        The node information object.

        - **AddedToClusterTime** *(string) --*

          The start time.

        - **BrokerNodeInfo** *(dict) --*

          The broker node info.

          - **AttachedENIId** *(string) --*

            The attached elastic network interface of the broker.

          - **BrokerId** *(float) --*

            The ID of the broker.

          - **ClientSubnet** *(string) --*

            The client subnet to which this broker node belongs.

          - **ClientVpcIpAddress** *(string) --*

            The virtual private cloud (VPC) of the client.

          - **CurrentBrokerSoftwareInfo** *(dict) --*

            Information about the version of software currently deployed on the Kafka brokers in
            the cluster.

            - **ConfigurationArn** *(string) --*

              The Amazon Resource Name (ARN) of the configuration used for the cluster. This field
              isn't visible in this preview release.

            - **ConfigurationRevision** *(integer) --*

              The revision of the configuration to use. This field isn't visible in this preview
              release.

            - **KafkaVersion** *(string) --*

              The version of Apache Kafka.

          - **Endpoints** *(list) --*

            Endpoints for accessing the broker.

            - *(string) --*

        - **InstanceType** *(string) --*

          The instance type.

        - **NodeARN** *(string) --*

          The Amazon Resource Name (ARN) of the node.

        - **NodeType** *(string) --*

          The node type.

        - **ZookeeperNodeInfo** *(dict) --*

          The ZookeeperNodeInfo.

          - **AttachedENIId** *(string) --*

            The attached elastic network interface of the broker.

          - **ClientVpcIpAddress** *(string) --*

            The virtual private cloud (VPC) IP address of the client.

          - **Endpoints** *(list) --*

            Endpoints for accessing the ZooKeeper.

            - *(string) --*

          - **ZookeeperId** *(float) --*

            The role-specific ID for Zookeeper.

          - **ZookeeperVersion** *(string) --*

            The version of Zookeeper.
    """
