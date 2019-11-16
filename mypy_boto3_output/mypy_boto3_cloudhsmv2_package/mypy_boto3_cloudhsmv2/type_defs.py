"Main interface for cloudhsmv2 type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientCopyBackupToRegionResponseDestinationBackupTypeDef",
    "ClientCopyBackupToRegionResponseTypeDef",
    "ClientCreateClusterResponseClusterCertificatesTypeDef",
    "ClientCreateClusterResponseClusterHsmsTypeDef",
    "ClientCreateClusterResponseClusterTypeDef",
    "ClientCreateClusterResponseTypeDef",
    "ClientCreateHsmResponseHsmTypeDef",
    "ClientCreateHsmResponseTypeDef",
    "ClientDeleteBackupResponseBackupTypeDef",
    "ClientDeleteBackupResponseTypeDef",
    "ClientDeleteClusterResponseClusterCertificatesTypeDef",
    "ClientDeleteClusterResponseClusterHsmsTypeDef",
    "ClientDeleteClusterResponseClusterTypeDef",
    "ClientDeleteClusterResponseTypeDef",
    "ClientDeleteHsmResponseTypeDef",
    "ClientDescribeBackupsResponseBackupsTypeDef",
    "ClientDescribeBackupsResponseTypeDef",
    "ClientDescribeClustersResponseClustersCertificatesTypeDef",
    "ClientDescribeClustersResponseClustersHsmsTypeDef",
    "ClientDescribeClustersResponseClustersTypeDef",
    "ClientDescribeClustersResponseTypeDef",
    "ClientInitializeClusterResponseTypeDef",
    "ClientListTagsResponseTagListTypeDef",
    "ClientListTagsResponseTypeDef",
    "ClientRestoreBackupResponseBackupTypeDef",
    "ClientRestoreBackupResponseTypeDef",
    "ClientTagResourceTagListTypeDef",
    "DescribeBackupsPaginatePaginationConfigTypeDef",
    "DescribeBackupsPaginateResponseBackupsTypeDef",
    "DescribeBackupsPaginateResponseTypeDef",
    "DescribeClustersPaginatePaginationConfigTypeDef",
    "DescribeClustersPaginateResponseClustersCertificatesTypeDef",
    "DescribeClustersPaginateResponseClustersHsmsTypeDef",
    "DescribeClustersPaginateResponseClustersTypeDef",
    "DescribeClustersPaginateResponseTypeDef",
    "ListTagsPaginatePaginationConfigTypeDef",
    "ListTagsPaginateResponseTagListTypeDef",
    "ListTagsPaginateResponseTypeDef",
)


_ClientCopyBackupToRegionResponseDestinationBackupTypeDef = TypedDict(
    "_ClientCopyBackupToRegionResponseDestinationBackupTypeDef",
    {
        "CreateTimestamp": datetime,
        "SourceRegion": str,
        "SourceBackup": str,
        "SourceCluster": str,
    },
    total=False,
)


class ClientCopyBackupToRegionResponseDestinationBackupTypeDef(
    _ClientCopyBackupToRegionResponseDestinationBackupTypeDef
):
    """
    Type definition for `ClientCopyBackupToRegionResponse` `DestinationBackup`

    Information on the backup that will be copied to the destination region, including
    CreateTimestamp, SourceBackup, SourceCluster, and Source Region. CreateTimestamp of the
    destination backup will be the same as that of the source backup.

    You will need to use the ``sourceBackupID`` returned in this operation to use the
    DescribeBackups operation on the backup that will be copied to the destination region.

    - **CreateTimestamp** *(datetime) --*

    - **SourceRegion** *(string) --*

    - **SourceBackup** *(string) --*

    - **SourceCluster** *(string) --*
    """


_ClientCopyBackupToRegionResponseTypeDef = TypedDict(
    "_ClientCopyBackupToRegionResponseTypeDef",
    {"DestinationBackup": ClientCopyBackupToRegionResponseDestinationBackupTypeDef},
    total=False,
)


class ClientCopyBackupToRegionResponseTypeDef(_ClientCopyBackupToRegionResponseTypeDef):
    """
    Type definition for `ClientCopyBackupToRegion` `Response`

    - **DestinationBackup** *(dict) --*

      Information on the backup that will be copied to the destination region, including
      CreateTimestamp, SourceBackup, SourceCluster, and Source Region. CreateTimestamp of the
      destination backup will be the same as that of the source backup.

      You will need to use the ``sourceBackupID`` returned in this operation to use the
      DescribeBackups operation on the backup that will be copied to the destination region.

      - **CreateTimestamp** *(datetime) --*

      - **SourceRegion** *(string) --*

      - **SourceBackup** *(string) --*

      - **SourceCluster** *(string) --*
    """


_ClientCreateClusterResponseClusterCertificatesTypeDef = TypedDict(
    "_ClientCreateClusterResponseClusterCertificatesTypeDef",
    {
        "ClusterCsr": str,
        "HsmCertificate": str,
        "AwsHardwareCertificate": str,
        "ManufacturerHardwareCertificate": str,
        "ClusterCertificate": str,
    },
    total=False,
)


class ClientCreateClusterResponseClusterCertificatesTypeDef(
    _ClientCreateClusterResponseClusterCertificatesTypeDef
):
    """
    Type definition for `ClientCreateClusterResponseCluster` `Certificates`

    Contains one or more certificates or a certificate signing request (CSR).

    - **ClusterCsr** *(string) --*

      The cluster's certificate signing request (CSR). The CSR exists only when the cluster's
      state is ``UNINITIALIZED`` .

    - **HsmCertificate** *(string) --*

      The HSM certificate issued (signed) by the HSM hardware.

    - **AwsHardwareCertificate** *(string) --*

      The HSM hardware certificate issued (signed) by AWS CloudHSM.

    - **ManufacturerHardwareCertificate** *(string) --*

      The HSM hardware certificate issued (signed) by the hardware manufacturer.

    - **ClusterCertificate** *(string) --*

      The cluster certificate issued (signed) by the issuing certificate authority (CA) of the
      cluster's owner.
    """


_ClientCreateClusterResponseClusterHsmsTypeDef = TypedDict(
    "_ClientCreateClusterResponseClusterHsmsTypeDef",
    {
        "AvailabilityZone": str,
        "ClusterId": str,
        "SubnetId": str,
        "EniId": str,
        "EniIp": str,
        "HsmId": str,
        "State": str,
        "StateMessage": str,
    },
    total=False,
)


class ClientCreateClusterResponseClusterHsmsTypeDef(
    _ClientCreateClusterResponseClusterHsmsTypeDef
):
    """
    Type definition for `ClientCreateClusterResponseCluster` `Hsms`

    Contains information about a hardware security module (HSM) in an AWS CloudHSM cluster.

    - **AvailabilityZone** *(string) --*

      The Availability Zone that contains the HSM.

    - **ClusterId** *(string) --*

      The identifier (ID) of the cluster that contains the HSM.

    - **SubnetId** *(string) --*

      The subnet that contains the HSM's elastic network interface (ENI).

    - **EniId** *(string) --*

      The identifier (ID) of the HSM's elastic network interface (ENI).

    - **EniIp** *(string) --*

      The IP address of the HSM's elastic network interface (ENI).

    - **HsmId** *(string) --*

      The HSM's identifier (ID).

    - **State** *(string) --*

      The HSM's state.

    - **StateMessage** *(string) --*

      A description of the HSM's state.
    """


_ClientCreateClusterResponseClusterTypeDef = TypedDict(
    "_ClientCreateClusterResponseClusterTypeDef",
    {
        "BackupPolicy": str,
        "ClusterId": str,
        "CreateTimestamp": datetime,
        "Hsms": List[ClientCreateClusterResponseClusterHsmsTypeDef],
        "HsmType": str,
        "PreCoPassword": str,
        "SecurityGroup": str,
        "SourceBackupId": str,
        "State": str,
        "StateMessage": str,
        "SubnetMapping": Dict[str, str],
        "VpcId": str,
        "Certificates": ClientCreateClusterResponseClusterCertificatesTypeDef,
    },
    total=False,
)


class ClientCreateClusterResponseClusterTypeDef(
    _ClientCreateClusterResponseClusterTypeDef
):
    """
    Type definition for `ClientCreateClusterResponse` `Cluster`

    Information about the cluster that was created.

    - **BackupPolicy** *(string) --*

      The cluster's backup policy.

    - **ClusterId** *(string) --*

      The cluster's identifier (ID).

    - **CreateTimestamp** *(datetime) --*

      The date and time when the cluster was created.

    - **Hsms** *(list) --*

      Contains information about the HSMs in the cluster.

      - *(dict) --*

        Contains information about a hardware security module (HSM) in an AWS CloudHSM cluster.

        - **AvailabilityZone** *(string) --*

          The Availability Zone that contains the HSM.

        - **ClusterId** *(string) --*

          The identifier (ID) of the cluster that contains the HSM.

        - **SubnetId** *(string) --*

          The subnet that contains the HSM's elastic network interface (ENI).

        - **EniId** *(string) --*

          The identifier (ID) of the HSM's elastic network interface (ENI).

        - **EniIp** *(string) --*

          The IP address of the HSM's elastic network interface (ENI).

        - **HsmId** *(string) --*

          The HSM's identifier (ID).

        - **State** *(string) --*

          The HSM's state.

        - **StateMessage** *(string) --*

          A description of the HSM's state.

    - **HsmType** *(string) --*

      The type of HSM that the cluster contains.

    - **PreCoPassword** *(string) --*

      The default password for the cluster's Pre-Crypto Officer (PRECO) user.

    - **SecurityGroup** *(string) --*

      The identifier (ID) of the cluster's security group.

    - **SourceBackupId** *(string) --*

      The identifier (ID) of the backup used to create the cluster. This value exists only when
      the cluster was created from a backup.

    - **State** *(string) --*

      The cluster's state.

    - **StateMessage** *(string) --*

      A description of the cluster's state.

    - **SubnetMapping** *(dict) --*

      A map of the cluster's subnets and their corresponding Availability Zones.

      - *(string) --*

        - *(string) --*

    - **VpcId** *(string) --*

      The identifier (ID) of the virtual private cloud (VPC) that contains the cluster.

    - **Certificates** *(dict) --*

      Contains one or more certificates or a certificate signing request (CSR).

      - **ClusterCsr** *(string) --*

        The cluster's certificate signing request (CSR). The CSR exists only when the cluster's
        state is ``UNINITIALIZED`` .

      - **HsmCertificate** *(string) --*

        The HSM certificate issued (signed) by the HSM hardware.

      - **AwsHardwareCertificate** *(string) --*

        The HSM hardware certificate issued (signed) by AWS CloudHSM.

      - **ManufacturerHardwareCertificate** *(string) --*

        The HSM hardware certificate issued (signed) by the hardware manufacturer.

      - **ClusterCertificate** *(string) --*

        The cluster certificate issued (signed) by the issuing certificate authority (CA) of the
        cluster's owner.
    """


_ClientCreateClusterResponseTypeDef = TypedDict(
    "_ClientCreateClusterResponseTypeDef",
    {"Cluster": ClientCreateClusterResponseClusterTypeDef},
    total=False,
)


class ClientCreateClusterResponseTypeDef(_ClientCreateClusterResponseTypeDef):
    """
    Type definition for `ClientCreateCluster` `Response`

    - **Cluster** *(dict) --*

      Information about the cluster that was created.

      - **BackupPolicy** *(string) --*

        The cluster's backup policy.

      - **ClusterId** *(string) --*

        The cluster's identifier (ID).

      - **CreateTimestamp** *(datetime) --*

        The date and time when the cluster was created.

      - **Hsms** *(list) --*

        Contains information about the HSMs in the cluster.

        - *(dict) --*

          Contains information about a hardware security module (HSM) in an AWS CloudHSM cluster.

          - **AvailabilityZone** *(string) --*

            The Availability Zone that contains the HSM.

          - **ClusterId** *(string) --*

            The identifier (ID) of the cluster that contains the HSM.

          - **SubnetId** *(string) --*

            The subnet that contains the HSM's elastic network interface (ENI).

          - **EniId** *(string) --*

            The identifier (ID) of the HSM's elastic network interface (ENI).

          - **EniIp** *(string) --*

            The IP address of the HSM's elastic network interface (ENI).

          - **HsmId** *(string) --*

            The HSM's identifier (ID).

          - **State** *(string) --*

            The HSM's state.

          - **StateMessage** *(string) --*

            A description of the HSM's state.

      - **HsmType** *(string) --*

        The type of HSM that the cluster contains.

      - **PreCoPassword** *(string) --*

        The default password for the cluster's Pre-Crypto Officer (PRECO) user.

      - **SecurityGroup** *(string) --*

        The identifier (ID) of the cluster's security group.

      - **SourceBackupId** *(string) --*

        The identifier (ID) of the backup used to create the cluster. This value exists only when
        the cluster was created from a backup.

      - **State** *(string) --*

        The cluster's state.

      - **StateMessage** *(string) --*

        A description of the cluster's state.

      - **SubnetMapping** *(dict) --*

        A map of the cluster's subnets and their corresponding Availability Zones.

        - *(string) --*

          - *(string) --*

      - **VpcId** *(string) --*

        The identifier (ID) of the virtual private cloud (VPC) that contains the cluster.

      - **Certificates** *(dict) --*

        Contains one or more certificates or a certificate signing request (CSR).

        - **ClusterCsr** *(string) --*

          The cluster's certificate signing request (CSR). The CSR exists only when the cluster's
          state is ``UNINITIALIZED`` .

        - **HsmCertificate** *(string) --*

          The HSM certificate issued (signed) by the HSM hardware.

        - **AwsHardwareCertificate** *(string) --*

          The HSM hardware certificate issued (signed) by AWS CloudHSM.

        - **ManufacturerHardwareCertificate** *(string) --*

          The HSM hardware certificate issued (signed) by the hardware manufacturer.

        - **ClusterCertificate** *(string) --*

          The cluster certificate issued (signed) by the issuing certificate authority (CA) of the
          cluster's owner.
    """


_ClientCreateHsmResponseHsmTypeDef = TypedDict(
    "_ClientCreateHsmResponseHsmTypeDef",
    {
        "AvailabilityZone": str,
        "ClusterId": str,
        "SubnetId": str,
        "EniId": str,
        "EniIp": str,
        "HsmId": str,
        "State": str,
        "StateMessage": str,
    },
    total=False,
)


class ClientCreateHsmResponseHsmTypeDef(_ClientCreateHsmResponseHsmTypeDef):
    """
    Type definition for `ClientCreateHsmResponse` `Hsm`

    Information about the HSM that was created.

    - **AvailabilityZone** *(string) --*

      The Availability Zone that contains the HSM.

    - **ClusterId** *(string) --*

      The identifier (ID) of the cluster that contains the HSM.

    - **SubnetId** *(string) --*

      The subnet that contains the HSM's elastic network interface (ENI).

    - **EniId** *(string) --*

      The identifier (ID) of the HSM's elastic network interface (ENI).

    - **EniIp** *(string) --*

      The IP address of the HSM's elastic network interface (ENI).

    - **HsmId** *(string) --*

      The HSM's identifier (ID).

    - **State** *(string) --*

      The HSM's state.

    - **StateMessage** *(string) --*

      A description of the HSM's state.
    """


_ClientCreateHsmResponseTypeDef = TypedDict(
    "_ClientCreateHsmResponseTypeDef",
    {"Hsm": ClientCreateHsmResponseHsmTypeDef},
    total=False,
)


class ClientCreateHsmResponseTypeDef(_ClientCreateHsmResponseTypeDef):
    """
    Type definition for `ClientCreateHsm` `Response`

    - **Hsm** *(dict) --*

      Information about the HSM that was created.

      - **AvailabilityZone** *(string) --*

        The Availability Zone that contains the HSM.

      - **ClusterId** *(string) --*

        The identifier (ID) of the cluster that contains the HSM.

      - **SubnetId** *(string) --*

        The subnet that contains the HSM's elastic network interface (ENI).

      - **EniId** *(string) --*

        The identifier (ID) of the HSM's elastic network interface (ENI).

      - **EniIp** *(string) --*

        The IP address of the HSM's elastic network interface (ENI).

      - **HsmId** *(string) --*

        The HSM's identifier (ID).

      - **State** *(string) --*

        The HSM's state.

      - **StateMessage** *(string) --*

        A description of the HSM's state.
    """


_ClientDeleteBackupResponseBackupTypeDef = TypedDict(
    "_ClientDeleteBackupResponseBackupTypeDef",
    {
        "BackupId": str,
        "BackupState": str,
        "ClusterId": str,
        "CreateTimestamp": datetime,
        "CopyTimestamp": datetime,
        "SourceRegion": str,
        "SourceBackup": str,
        "SourceCluster": str,
        "DeleteTimestamp": datetime,
    },
    total=False,
)


class ClientDeleteBackupResponseBackupTypeDef(_ClientDeleteBackupResponseBackupTypeDef):
    """
    Type definition for `ClientDeleteBackupResponse` `Backup`

    Information on the ``Backup`` object deleted.

    - **BackupId** *(string) --*

      The identifier (ID) of the backup.

    - **BackupState** *(string) --*

      The state of the backup.

    - **ClusterId** *(string) --*

      The identifier (ID) of the cluster that was backed up.

    - **CreateTimestamp** *(datetime) --*

      The date and time when the backup was created.

    - **CopyTimestamp** *(datetime) --*

    - **SourceRegion** *(string) --*

    - **SourceBackup** *(string) --*

    - **SourceCluster** *(string) --*

    - **DeleteTimestamp** *(datetime) --*

      The date and time when the backup will be permanently deleted.
    """


_ClientDeleteBackupResponseTypeDef = TypedDict(
    "_ClientDeleteBackupResponseTypeDef",
    {"Backup": ClientDeleteBackupResponseBackupTypeDef},
    total=False,
)


class ClientDeleteBackupResponseTypeDef(_ClientDeleteBackupResponseTypeDef):
    """
    Type definition for `ClientDeleteBackup` `Response`

    - **Backup** *(dict) --*

      Information on the ``Backup`` object deleted.

      - **BackupId** *(string) --*

        The identifier (ID) of the backup.

      - **BackupState** *(string) --*

        The state of the backup.

      - **ClusterId** *(string) --*

        The identifier (ID) of the cluster that was backed up.

      - **CreateTimestamp** *(datetime) --*

        The date and time when the backup was created.

      - **CopyTimestamp** *(datetime) --*

      - **SourceRegion** *(string) --*

      - **SourceBackup** *(string) --*

      - **SourceCluster** *(string) --*

      - **DeleteTimestamp** *(datetime) --*

        The date and time when the backup will be permanently deleted.
    """


_ClientDeleteClusterResponseClusterCertificatesTypeDef = TypedDict(
    "_ClientDeleteClusterResponseClusterCertificatesTypeDef",
    {
        "ClusterCsr": str,
        "HsmCertificate": str,
        "AwsHardwareCertificate": str,
        "ManufacturerHardwareCertificate": str,
        "ClusterCertificate": str,
    },
    total=False,
)


class ClientDeleteClusterResponseClusterCertificatesTypeDef(
    _ClientDeleteClusterResponseClusterCertificatesTypeDef
):
    """
    Type definition for `ClientDeleteClusterResponseCluster` `Certificates`

    Contains one or more certificates or a certificate signing request (CSR).

    - **ClusterCsr** *(string) --*

      The cluster's certificate signing request (CSR). The CSR exists only when the cluster's
      state is ``UNINITIALIZED`` .

    - **HsmCertificate** *(string) --*

      The HSM certificate issued (signed) by the HSM hardware.

    - **AwsHardwareCertificate** *(string) --*

      The HSM hardware certificate issued (signed) by AWS CloudHSM.

    - **ManufacturerHardwareCertificate** *(string) --*

      The HSM hardware certificate issued (signed) by the hardware manufacturer.

    - **ClusterCertificate** *(string) --*

      The cluster certificate issued (signed) by the issuing certificate authority (CA) of the
      cluster's owner.
    """


_ClientDeleteClusterResponseClusterHsmsTypeDef = TypedDict(
    "_ClientDeleteClusterResponseClusterHsmsTypeDef",
    {
        "AvailabilityZone": str,
        "ClusterId": str,
        "SubnetId": str,
        "EniId": str,
        "EniIp": str,
        "HsmId": str,
        "State": str,
        "StateMessage": str,
    },
    total=False,
)


class ClientDeleteClusterResponseClusterHsmsTypeDef(
    _ClientDeleteClusterResponseClusterHsmsTypeDef
):
    """
    Type definition for `ClientDeleteClusterResponseCluster` `Hsms`

    Contains information about a hardware security module (HSM) in an AWS CloudHSM cluster.

    - **AvailabilityZone** *(string) --*

      The Availability Zone that contains the HSM.

    - **ClusterId** *(string) --*

      The identifier (ID) of the cluster that contains the HSM.

    - **SubnetId** *(string) --*

      The subnet that contains the HSM's elastic network interface (ENI).

    - **EniId** *(string) --*

      The identifier (ID) of the HSM's elastic network interface (ENI).

    - **EniIp** *(string) --*

      The IP address of the HSM's elastic network interface (ENI).

    - **HsmId** *(string) --*

      The HSM's identifier (ID).

    - **State** *(string) --*

      The HSM's state.

    - **StateMessage** *(string) --*

      A description of the HSM's state.
    """


_ClientDeleteClusterResponseClusterTypeDef = TypedDict(
    "_ClientDeleteClusterResponseClusterTypeDef",
    {
        "BackupPolicy": str,
        "ClusterId": str,
        "CreateTimestamp": datetime,
        "Hsms": List[ClientDeleteClusterResponseClusterHsmsTypeDef],
        "HsmType": str,
        "PreCoPassword": str,
        "SecurityGroup": str,
        "SourceBackupId": str,
        "State": str,
        "StateMessage": str,
        "SubnetMapping": Dict[str, str],
        "VpcId": str,
        "Certificates": ClientDeleteClusterResponseClusterCertificatesTypeDef,
    },
    total=False,
)


class ClientDeleteClusterResponseClusterTypeDef(
    _ClientDeleteClusterResponseClusterTypeDef
):
    """
    Type definition for `ClientDeleteClusterResponse` `Cluster`

    Information about the cluster that was deleted.

    - **BackupPolicy** *(string) --*

      The cluster's backup policy.

    - **ClusterId** *(string) --*

      The cluster's identifier (ID).

    - **CreateTimestamp** *(datetime) --*

      The date and time when the cluster was created.

    - **Hsms** *(list) --*

      Contains information about the HSMs in the cluster.

      - *(dict) --*

        Contains information about a hardware security module (HSM) in an AWS CloudHSM cluster.

        - **AvailabilityZone** *(string) --*

          The Availability Zone that contains the HSM.

        - **ClusterId** *(string) --*

          The identifier (ID) of the cluster that contains the HSM.

        - **SubnetId** *(string) --*

          The subnet that contains the HSM's elastic network interface (ENI).

        - **EniId** *(string) --*

          The identifier (ID) of the HSM's elastic network interface (ENI).

        - **EniIp** *(string) --*

          The IP address of the HSM's elastic network interface (ENI).

        - **HsmId** *(string) --*

          The HSM's identifier (ID).

        - **State** *(string) --*

          The HSM's state.

        - **StateMessage** *(string) --*

          A description of the HSM's state.

    - **HsmType** *(string) --*

      The type of HSM that the cluster contains.

    - **PreCoPassword** *(string) --*

      The default password for the cluster's Pre-Crypto Officer (PRECO) user.

    - **SecurityGroup** *(string) --*

      The identifier (ID) of the cluster's security group.

    - **SourceBackupId** *(string) --*

      The identifier (ID) of the backup used to create the cluster. This value exists only when
      the cluster was created from a backup.

    - **State** *(string) --*

      The cluster's state.

    - **StateMessage** *(string) --*

      A description of the cluster's state.

    - **SubnetMapping** *(dict) --*

      A map of the cluster's subnets and their corresponding Availability Zones.

      - *(string) --*

        - *(string) --*

    - **VpcId** *(string) --*

      The identifier (ID) of the virtual private cloud (VPC) that contains the cluster.

    - **Certificates** *(dict) --*

      Contains one or more certificates or a certificate signing request (CSR).

      - **ClusterCsr** *(string) --*

        The cluster's certificate signing request (CSR). The CSR exists only when the cluster's
        state is ``UNINITIALIZED`` .

      - **HsmCertificate** *(string) --*

        The HSM certificate issued (signed) by the HSM hardware.

      - **AwsHardwareCertificate** *(string) --*

        The HSM hardware certificate issued (signed) by AWS CloudHSM.

      - **ManufacturerHardwareCertificate** *(string) --*

        The HSM hardware certificate issued (signed) by the hardware manufacturer.

      - **ClusterCertificate** *(string) --*

        The cluster certificate issued (signed) by the issuing certificate authority (CA) of the
        cluster's owner.
    """


_ClientDeleteClusterResponseTypeDef = TypedDict(
    "_ClientDeleteClusterResponseTypeDef",
    {"Cluster": ClientDeleteClusterResponseClusterTypeDef},
    total=False,
)


class ClientDeleteClusterResponseTypeDef(_ClientDeleteClusterResponseTypeDef):
    """
    Type definition for `ClientDeleteCluster` `Response`

    - **Cluster** *(dict) --*

      Information about the cluster that was deleted.

      - **BackupPolicy** *(string) --*

        The cluster's backup policy.

      - **ClusterId** *(string) --*

        The cluster's identifier (ID).

      - **CreateTimestamp** *(datetime) --*

        The date and time when the cluster was created.

      - **Hsms** *(list) --*

        Contains information about the HSMs in the cluster.

        - *(dict) --*

          Contains information about a hardware security module (HSM) in an AWS CloudHSM cluster.

          - **AvailabilityZone** *(string) --*

            The Availability Zone that contains the HSM.

          - **ClusterId** *(string) --*

            The identifier (ID) of the cluster that contains the HSM.

          - **SubnetId** *(string) --*

            The subnet that contains the HSM's elastic network interface (ENI).

          - **EniId** *(string) --*

            The identifier (ID) of the HSM's elastic network interface (ENI).

          - **EniIp** *(string) --*

            The IP address of the HSM's elastic network interface (ENI).

          - **HsmId** *(string) --*

            The HSM's identifier (ID).

          - **State** *(string) --*

            The HSM's state.

          - **StateMessage** *(string) --*

            A description of the HSM's state.

      - **HsmType** *(string) --*

        The type of HSM that the cluster contains.

      - **PreCoPassword** *(string) --*

        The default password for the cluster's Pre-Crypto Officer (PRECO) user.

      - **SecurityGroup** *(string) --*

        The identifier (ID) of the cluster's security group.

      - **SourceBackupId** *(string) --*

        The identifier (ID) of the backup used to create the cluster. This value exists only when
        the cluster was created from a backup.

      - **State** *(string) --*

        The cluster's state.

      - **StateMessage** *(string) --*

        A description of the cluster's state.

      - **SubnetMapping** *(dict) --*

        A map of the cluster's subnets and their corresponding Availability Zones.

        - *(string) --*

          - *(string) --*

      - **VpcId** *(string) --*

        The identifier (ID) of the virtual private cloud (VPC) that contains the cluster.

      - **Certificates** *(dict) --*

        Contains one or more certificates or a certificate signing request (CSR).

        - **ClusterCsr** *(string) --*

          The cluster's certificate signing request (CSR). The CSR exists only when the cluster's
          state is ``UNINITIALIZED`` .

        - **HsmCertificate** *(string) --*

          The HSM certificate issued (signed) by the HSM hardware.

        - **AwsHardwareCertificate** *(string) --*

          The HSM hardware certificate issued (signed) by AWS CloudHSM.

        - **ManufacturerHardwareCertificate** *(string) --*

          The HSM hardware certificate issued (signed) by the hardware manufacturer.

        - **ClusterCertificate** *(string) --*

          The cluster certificate issued (signed) by the issuing certificate authority (CA) of the
          cluster's owner.
    """


_ClientDeleteHsmResponseTypeDef = TypedDict(
    "_ClientDeleteHsmResponseTypeDef", {"HsmId": str}, total=False
)


class ClientDeleteHsmResponseTypeDef(_ClientDeleteHsmResponseTypeDef):
    """
    Type definition for `ClientDeleteHsm` `Response`

    - **HsmId** *(string) --*

      The identifier (ID) of the HSM that was deleted.
    """


_ClientDescribeBackupsResponseBackupsTypeDef = TypedDict(
    "_ClientDescribeBackupsResponseBackupsTypeDef",
    {
        "BackupId": str,
        "BackupState": str,
        "ClusterId": str,
        "CreateTimestamp": datetime,
        "CopyTimestamp": datetime,
        "SourceRegion": str,
        "SourceBackup": str,
        "SourceCluster": str,
        "DeleteTimestamp": datetime,
    },
    total=False,
)


class ClientDescribeBackupsResponseBackupsTypeDef(
    _ClientDescribeBackupsResponseBackupsTypeDef
):
    """
    Type definition for `ClientDescribeBackupsResponse` `Backups`

    Contains information about a backup of an AWS CloudHSM cluster.

    - **BackupId** *(string) --*

      The identifier (ID) of the backup.

    - **BackupState** *(string) --*

      The state of the backup.

    - **ClusterId** *(string) --*

      The identifier (ID) of the cluster that was backed up.

    - **CreateTimestamp** *(datetime) --*

      The date and time when the backup was created.

    - **CopyTimestamp** *(datetime) --*

    - **SourceRegion** *(string) --*

    - **SourceBackup** *(string) --*

    - **SourceCluster** *(string) --*

    - **DeleteTimestamp** *(datetime) --*

      The date and time when the backup will be permanently deleted.
    """


_ClientDescribeBackupsResponseTypeDef = TypedDict(
    "_ClientDescribeBackupsResponseTypeDef",
    {"Backups": List[ClientDescribeBackupsResponseBackupsTypeDef], "NextToken": str},
    total=False,
)


class ClientDescribeBackupsResponseTypeDef(_ClientDescribeBackupsResponseTypeDef):
    """
    Type definition for `ClientDescribeBackups` `Response`

    - **Backups** *(list) --*

      A list of backups.

      - *(dict) --*

        Contains information about a backup of an AWS CloudHSM cluster.

        - **BackupId** *(string) --*

          The identifier (ID) of the backup.

        - **BackupState** *(string) --*

          The state of the backup.

        - **ClusterId** *(string) --*

          The identifier (ID) of the cluster that was backed up.

        - **CreateTimestamp** *(datetime) --*

          The date and time when the backup was created.

        - **CopyTimestamp** *(datetime) --*

        - **SourceRegion** *(string) --*

        - **SourceBackup** *(string) --*

        - **SourceCluster** *(string) --*

        - **DeleteTimestamp** *(datetime) --*

          The date and time when the backup will be permanently deleted.

    - **NextToken** *(string) --*

      An opaque string that indicates that the response contains only a subset of backups. Use this
      value in a subsequent ``DescribeBackups`` request to get more backups.
    """


_ClientDescribeClustersResponseClustersCertificatesTypeDef = TypedDict(
    "_ClientDescribeClustersResponseClustersCertificatesTypeDef",
    {
        "ClusterCsr": str,
        "HsmCertificate": str,
        "AwsHardwareCertificate": str,
        "ManufacturerHardwareCertificate": str,
        "ClusterCertificate": str,
    },
    total=False,
)


class ClientDescribeClustersResponseClustersCertificatesTypeDef(
    _ClientDescribeClustersResponseClustersCertificatesTypeDef
):
    """
    Type definition for `ClientDescribeClustersResponseClusters` `Certificates`

    Contains one or more certificates or a certificate signing request (CSR).

    - **ClusterCsr** *(string) --*

      The cluster's certificate signing request (CSR). The CSR exists only when the cluster's
      state is ``UNINITIALIZED`` .

    - **HsmCertificate** *(string) --*

      The HSM certificate issued (signed) by the HSM hardware.

    - **AwsHardwareCertificate** *(string) --*

      The HSM hardware certificate issued (signed) by AWS CloudHSM.

    - **ManufacturerHardwareCertificate** *(string) --*

      The HSM hardware certificate issued (signed) by the hardware manufacturer.

    - **ClusterCertificate** *(string) --*

      The cluster certificate issued (signed) by the issuing certificate authority (CA) of
      the cluster's owner.
    """


_ClientDescribeClustersResponseClustersHsmsTypeDef = TypedDict(
    "_ClientDescribeClustersResponseClustersHsmsTypeDef",
    {
        "AvailabilityZone": str,
        "ClusterId": str,
        "SubnetId": str,
        "EniId": str,
        "EniIp": str,
        "HsmId": str,
        "State": str,
        "StateMessage": str,
    },
    total=False,
)


class ClientDescribeClustersResponseClustersHsmsTypeDef(
    _ClientDescribeClustersResponseClustersHsmsTypeDef
):
    """
    Type definition for `ClientDescribeClustersResponseClusters` `Hsms`

    Contains information about a hardware security module (HSM) in an AWS CloudHSM cluster.

    - **AvailabilityZone** *(string) --*

      The Availability Zone that contains the HSM.

    - **ClusterId** *(string) --*

      The identifier (ID) of the cluster that contains the HSM.

    - **SubnetId** *(string) --*

      The subnet that contains the HSM's elastic network interface (ENI).

    - **EniId** *(string) --*

      The identifier (ID) of the HSM's elastic network interface (ENI).

    - **EniIp** *(string) --*

      The IP address of the HSM's elastic network interface (ENI).

    - **HsmId** *(string) --*

      The HSM's identifier (ID).

    - **State** *(string) --*

      The HSM's state.

    - **StateMessage** *(string) --*

      A description of the HSM's state.
    """


_ClientDescribeClustersResponseClustersTypeDef = TypedDict(
    "_ClientDescribeClustersResponseClustersTypeDef",
    {
        "BackupPolicy": str,
        "ClusterId": str,
        "CreateTimestamp": datetime,
        "Hsms": List[ClientDescribeClustersResponseClustersHsmsTypeDef],
        "HsmType": str,
        "PreCoPassword": str,
        "SecurityGroup": str,
        "SourceBackupId": str,
        "State": str,
        "StateMessage": str,
        "SubnetMapping": Dict[str, str],
        "VpcId": str,
        "Certificates": ClientDescribeClustersResponseClustersCertificatesTypeDef,
    },
    total=False,
)


class ClientDescribeClustersResponseClustersTypeDef(
    _ClientDescribeClustersResponseClustersTypeDef
):
    """
    Type definition for `ClientDescribeClustersResponse` `Clusters`

    Contains information about an AWS CloudHSM cluster.

    - **BackupPolicy** *(string) --*

      The cluster's backup policy.

    - **ClusterId** *(string) --*

      The cluster's identifier (ID).

    - **CreateTimestamp** *(datetime) --*

      The date and time when the cluster was created.

    - **Hsms** *(list) --*

      Contains information about the HSMs in the cluster.

      - *(dict) --*

        Contains information about a hardware security module (HSM) in an AWS CloudHSM cluster.

        - **AvailabilityZone** *(string) --*

          The Availability Zone that contains the HSM.

        - **ClusterId** *(string) --*

          The identifier (ID) of the cluster that contains the HSM.

        - **SubnetId** *(string) --*

          The subnet that contains the HSM's elastic network interface (ENI).

        - **EniId** *(string) --*

          The identifier (ID) of the HSM's elastic network interface (ENI).

        - **EniIp** *(string) --*

          The IP address of the HSM's elastic network interface (ENI).

        - **HsmId** *(string) --*

          The HSM's identifier (ID).

        - **State** *(string) --*

          The HSM's state.

        - **StateMessage** *(string) --*

          A description of the HSM's state.

    - **HsmType** *(string) --*

      The type of HSM that the cluster contains.

    - **PreCoPassword** *(string) --*

      The default password for the cluster's Pre-Crypto Officer (PRECO) user.

    - **SecurityGroup** *(string) --*

      The identifier (ID) of the cluster's security group.

    - **SourceBackupId** *(string) --*

      The identifier (ID) of the backup used to create the cluster. This value exists only when
      the cluster was created from a backup.

    - **State** *(string) --*

      The cluster's state.

    - **StateMessage** *(string) --*

      A description of the cluster's state.

    - **SubnetMapping** *(dict) --*

      A map of the cluster's subnets and their corresponding Availability Zones.

      - *(string) --*

        - *(string) --*

    - **VpcId** *(string) --*

      The identifier (ID) of the virtual private cloud (VPC) that contains the cluster.

    - **Certificates** *(dict) --*

      Contains one or more certificates or a certificate signing request (CSR).

      - **ClusterCsr** *(string) --*

        The cluster's certificate signing request (CSR). The CSR exists only when the cluster's
        state is ``UNINITIALIZED`` .

      - **HsmCertificate** *(string) --*

        The HSM certificate issued (signed) by the HSM hardware.

      - **AwsHardwareCertificate** *(string) --*

        The HSM hardware certificate issued (signed) by AWS CloudHSM.

      - **ManufacturerHardwareCertificate** *(string) --*

        The HSM hardware certificate issued (signed) by the hardware manufacturer.

      - **ClusterCertificate** *(string) --*

        The cluster certificate issued (signed) by the issuing certificate authority (CA) of
        the cluster's owner.
    """


_ClientDescribeClustersResponseTypeDef = TypedDict(
    "_ClientDescribeClustersResponseTypeDef",
    {"Clusters": List[ClientDescribeClustersResponseClustersTypeDef], "NextToken": str},
    total=False,
)


class ClientDescribeClustersResponseTypeDef(_ClientDescribeClustersResponseTypeDef):
    """
    Type definition for `ClientDescribeClusters` `Response`

    - **Clusters** *(list) --*

      A list of clusters.

      - *(dict) --*

        Contains information about an AWS CloudHSM cluster.

        - **BackupPolicy** *(string) --*

          The cluster's backup policy.

        - **ClusterId** *(string) --*

          The cluster's identifier (ID).

        - **CreateTimestamp** *(datetime) --*

          The date and time when the cluster was created.

        - **Hsms** *(list) --*

          Contains information about the HSMs in the cluster.

          - *(dict) --*

            Contains information about a hardware security module (HSM) in an AWS CloudHSM cluster.

            - **AvailabilityZone** *(string) --*

              The Availability Zone that contains the HSM.

            - **ClusterId** *(string) --*

              The identifier (ID) of the cluster that contains the HSM.

            - **SubnetId** *(string) --*

              The subnet that contains the HSM's elastic network interface (ENI).

            - **EniId** *(string) --*

              The identifier (ID) of the HSM's elastic network interface (ENI).

            - **EniIp** *(string) --*

              The IP address of the HSM's elastic network interface (ENI).

            - **HsmId** *(string) --*

              The HSM's identifier (ID).

            - **State** *(string) --*

              The HSM's state.

            - **StateMessage** *(string) --*

              A description of the HSM's state.

        - **HsmType** *(string) --*

          The type of HSM that the cluster contains.

        - **PreCoPassword** *(string) --*

          The default password for the cluster's Pre-Crypto Officer (PRECO) user.

        - **SecurityGroup** *(string) --*

          The identifier (ID) of the cluster's security group.

        - **SourceBackupId** *(string) --*

          The identifier (ID) of the backup used to create the cluster. This value exists only when
          the cluster was created from a backup.

        - **State** *(string) --*

          The cluster's state.

        - **StateMessage** *(string) --*

          A description of the cluster's state.

        - **SubnetMapping** *(dict) --*

          A map of the cluster's subnets and their corresponding Availability Zones.

          - *(string) --*

            - *(string) --*

        - **VpcId** *(string) --*

          The identifier (ID) of the virtual private cloud (VPC) that contains the cluster.

        - **Certificates** *(dict) --*

          Contains one or more certificates or a certificate signing request (CSR).

          - **ClusterCsr** *(string) --*

            The cluster's certificate signing request (CSR). The CSR exists only when the cluster's
            state is ``UNINITIALIZED`` .

          - **HsmCertificate** *(string) --*

            The HSM certificate issued (signed) by the HSM hardware.

          - **AwsHardwareCertificate** *(string) --*

            The HSM hardware certificate issued (signed) by AWS CloudHSM.

          - **ManufacturerHardwareCertificate** *(string) --*

            The HSM hardware certificate issued (signed) by the hardware manufacturer.

          - **ClusterCertificate** *(string) --*

            The cluster certificate issued (signed) by the issuing certificate authority (CA) of
            the cluster's owner.

    - **NextToken** *(string) --*

      An opaque string that indicates that the response contains only a subset of clusters. Use
      this value in a subsequent ``DescribeClusters`` request to get more clusters.
    """


_ClientInitializeClusterResponseTypeDef = TypedDict(
    "_ClientInitializeClusterResponseTypeDef",
    {"State": str, "StateMessage": str},
    total=False,
)


class ClientInitializeClusterResponseTypeDef(_ClientInitializeClusterResponseTypeDef):
    """
    Type definition for `ClientInitializeCluster` `Response`

    - **State** *(string) --*

      The cluster's state.

    - **StateMessage** *(string) --*

      A description of the cluster's state.
    """


_ClientListTagsResponseTagListTypeDef = TypedDict(
    "_ClientListTagsResponseTagListTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientListTagsResponseTagListTypeDef(_ClientListTagsResponseTagListTypeDef):
    """
    Type definition for `ClientListTagsResponse` `TagList`

    Contains a tag. A tag is a key-value pair.

    - **Key** *(string) --*

      The key of the tag.

    - **Value** *(string) --*

      The value of the tag.
    """


_ClientListTagsResponseTypeDef = TypedDict(
    "_ClientListTagsResponseTypeDef",
    {"TagList": List[ClientListTagsResponseTagListTypeDef], "NextToken": str},
    total=False,
)


class ClientListTagsResponseTypeDef(_ClientListTagsResponseTypeDef):
    """
    Type definition for `ClientListTags` `Response`

    - **TagList** *(list) --*

      A list of tags.

      - *(dict) --*

        Contains a tag. A tag is a key-value pair.

        - **Key** *(string) --*

          The key of the tag.

        - **Value** *(string) --*

          The value of the tag.

    - **NextToken** *(string) --*

      An opaque string that indicates that the response contains only a subset of tags. Use this
      value in a subsequent ``ListTags`` request to get more tags.
    """


_ClientRestoreBackupResponseBackupTypeDef = TypedDict(
    "_ClientRestoreBackupResponseBackupTypeDef",
    {
        "BackupId": str,
        "BackupState": str,
        "ClusterId": str,
        "CreateTimestamp": datetime,
        "CopyTimestamp": datetime,
        "SourceRegion": str,
        "SourceBackup": str,
        "SourceCluster": str,
        "DeleteTimestamp": datetime,
    },
    total=False,
)


class ClientRestoreBackupResponseBackupTypeDef(
    _ClientRestoreBackupResponseBackupTypeDef
):
    """
    Type definition for `ClientRestoreBackupResponse` `Backup`

    Information on the ``Backup`` object created.

    - **BackupId** *(string) --*

      The identifier (ID) of the backup.

    - **BackupState** *(string) --*

      The state of the backup.

    - **ClusterId** *(string) --*

      The identifier (ID) of the cluster that was backed up.

    - **CreateTimestamp** *(datetime) --*

      The date and time when the backup was created.

    - **CopyTimestamp** *(datetime) --*

    - **SourceRegion** *(string) --*

    - **SourceBackup** *(string) --*

    - **SourceCluster** *(string) --*

    - **DeleteTimestamp** *(datetime) --*

      The date and time when the backup will be permanently deleted.
    """


_ClientRestoreBackupResponseTypeDef = TypedDict(
    "_ClientRestoreBackupResponseTypeDef",
    {"Backup": ClientRestoreBackupResponseBackupTypeDef},
    total=False,
)


class ClientRestoreBackupResponseTypeDef(_ClientRestoreBackupResponseTypeDef):
    """
    Type definition for `ClientRestoreBackup` `Response`

    - **Backup** *(dict) --*

      Information on the ``Backup`` object created.

      - **BackupId** *(string) --*

        The identifier (ID) of the backup.

      - **BackupState** *(string) --*

        The state of the backup.

      - **ClusterId** *(string) --*

        The identifier (ID) of the cluster that was backed up.

      - **CreateTimestamp** *(datetime) --*

        The date and time when the backup was created.

      - **CopyTimestamp** *(datetime) --*

      - **SourceRegion** *(string) --*

      - **SourceBackup** *(string) --*

      - **SourceCluster** *(string) --*

      - **DeleteTimestamp** *(datetime) --*

        The date and time when the backup will be permanently deleted.
    """


_ClientTagResourceTagListTypeDef = TypedDict(
    "_ClientTagResourceTagListTypeDef", {"Key": str, "Value": str}
)


class ClientTagResourceTagListTypeDef(_ClientTagResourceTagListTypeDef):
    """
    Type definition for `ClientTagResource` `TagList`

    Contains a tag. A tag is a key-value pair.

    - **Key** *(string) --* **[REQUIRED]**

      The key of the tag.

    - **Value** *(string) --* **[REQUIRED]**

      The value of the tag.
    """


_DescribeBackupsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeBackupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeBackupsPaginatePaginationConfigTypeDef(
    _DescribeBackupsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeBackupsPaginate` `PaginationConfig`

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


_DescribeBackupsPaginateResponseBackupsTypeDef = TypedDict(
    "_DescribeBackupsPaginateResponseBackupsTypeDef",
    {
        "BackupId": str,
        "BackupState": str,
        "ClusterId": str,
        "CreateTimestamp": datetime,
        "CopyTimestamp": datetime,
        "SourceRegion": str,
        "SourceBackup": str,
        "SourceCluster": str,
        "DeleteTimestamp": datetime,
    },
    total=False,
)


class DescribeBackupsPaginateResponseBackupsTypeDef(
    _DescribeBackupsPaginateResponseBackupsTypeDef
):
    """
    Type definition for `DescribeBackupsPaginateResponse` `Backups`

    Contains information about a backup of an AWS CloudHSM cluster.

    - **BackupId** *(string) --*

      The identifier (ID) of the backup.

    - **BackupState** *(string) --*

      The state of the backup.

    - **ClusterId** *(string) --*

      The identifier (ID) of the cluster that was backed up.

    - **CreateTimestamp** *(datetime) --*

      The date and time when the backup was created.

    - **CopyTimestamp** *(datetime) --*

    - **SourceRegion** *(string) --*

    - **SourceBackup** *(string) --*

    - **SourceCluster** *(string) --*

    - **DeleteTimestamp** *(datetime) --*

      The date and time when the backup will be permanently deleted.
    """


_DescribeBackupsPaginateResponseTypeDef = TypedDict(
    "_DescribeBackupsPaginateResponseTypeDef",
    {"Backups": List[DescribeBackupsPaginateResponseBackupsTypeDef]},
    total=False,
)


class DescribeBackupsPaginateResponseTypeDef(_DescribeBackupsPaginateResponseTypeDef):
    """
    Type definition for `DescribeBackupsPaginate` `Response`

    - **Backups** *(list) --*

      A list of backups.

      - *(dict) --*

        Contains information about a backup of an AWS CloudHSM cluster.

        - **BackupId** *(string) --*

          The identifier (ID) of the backup.

        - **BackupState** *(string) --*

          The state of the backup.

        - **ClusterId** *(string) --*

          The identifier (ID) of the cluster that was backed up.

        - **CreateTimestamp** *(datetime) --*

          The date and time when the backup was created.

        - **CopyTimestamp** *(datetime) --*

        - **SourceRegion** *(string) --*

        - **SourceBackup** *(string) --*

        - **SourceCluster** *(string) --*

        - **DeleteTimestamp** *(datetime) --*

          The date and time when the backup will be permanently deleted.
    """


_DescribeClustersPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeClustersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeClustersPaginatePaginationConfigTypeDef(
    _DescribeClustersPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeClustersPaginate` `PaginationConfig`

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


_DescribeClustersPaginateResponseClustersCertificatesTypeDef = TypedDict(
    "_DescribeClustersPaginateResponseClustersCertificatesTypeDef",
    {
        "ClusterCsr": str,
        "HsmCertificate": str,
        "AwsHardwareCertificate": str,
        "ManufacturerHardwareCertificate": str,
        "ClusterCertificate": str,
    },
    total=False,
)


class DescribeClustersPaginateResponseClustersCertificatesTypeDef(
    _DescribeClustersPaginateResponseClustersCertificatesTypeDef
):
    """
    Type definition for `DescribeClustersPaginateResponseClusters` `Certificates`

    Contains one or more certificates or a certificate signing request (CSR).

    - **ClusterCsr** *(string) --*

      The cluster's certificate signing request (CSR). The CSR exists only when the cluster's
      state is ``UNINITIALIZED`` .

    - **HsmCertificate** *(string) --*

      The HSM certificate issued (signed) by the HSM hardware.

    - **AwsHardwareCertificate** *(string) --*

      The HSM hardware certificate issued (signed) by AWS CloudHSM.

    - **ManufacturerHardwareCertificate** *(string) --*

      The HSM hardware certificate issued (signed) by the hardware manufacturer.

    - **ClusterCertificate** *(string) --*

      The cluster certificate issued (signed) by the issuing certificate authority (CA) of
      the cluster's owner.
    """


_DescribeClustersPaginateResponseClustersHsmsTypeDef = TypedDict(
    "_DescribeClustersPaginateResponseClustersHsmsTypeDef",
    {
        "AvailabilityZone": str,
        "ClusterId": str,
        "SubnetId": str,
        "EniId": str,
        "EniIp": str,
        "HsmId": str,
        "State": str,
        "StateMessage": str,
    },
    total=False,
)


class DescribeClustersPaginateResponseClustersHsmsTypeDef(
    _DescribeClustersPaginateResponseClustersHsmsTypeDef
):
    """
    Type definition for `DescribeClustersPaginateResponseClusters` `Hsms`

    Contains information about a hardware security module (HSM) in an AWS CloudHSM cluster.

    - **AvailabilityZone** *(string) --*

      The Availability Zone that contains the HSM.

    - **ClusterId** *(string) --*

      The identifier (ID) of the cluster that contains the HSM.

    - **SubnetId** *(string) --*

      The subnet that contains the HSM's elastic network interface (ENI).

    - **EniId** *(string) --*

      The identifier (ID) of the HSM's elastic network interface (ENI).

    - **EniIp** *(string) --*

      The IP address of the HSM's elastic network interface (ENI).

    - **HsmId** *(string) --*

      The HSM's identifier (ID).

    - **State** *(string) --*

      The HSM's state.

    - **StateMessage** *(string) --*

      A description of the HSM's state.
    """


_DescribeClustersPaginateResponseClustersTypeDef = TypedDict(
    "_DescribeClustersPaginateResponseClustersTypeDef",
    {
        "BackupPolicy": str,
        "ClusterId": str,
        "CreateTimestamp": datetime,
        "Hsms": List[DescribeClustersPaginateResponseClustersHsmsTypeDef],
        "HsmType": str,
        "PreCoPassword": str,
        "SecurityGroup": str,
        "SourceBackupId": str,
        "State": str,
        "StateMessage": str,
        "SubnetMapping": Dict[str, str],
        "VpcId": str,
        "Certificates": DescribeClustersPaginateResponseClustersCertificatesTypeDef,
    },
    total=False,
)


class DescribeClustersPaginateResponseClustersTypeDef(
    _DescribeClustersPaginateResponseClustersTypeDef
):
    """
    Type definition for `DescribeClustersPaginateResponse` `Clusters`

    Contains information about an AWS CloudHSM cluster.

    - **BackupPolicy** *(string) --*

      The cluster's backup policy.

    - **ClusterId** *(string) --*

      The cluster's identifier (ID).

    - **CreateTimestamp** *(datetime) --*

      The date and time when the cluster was created.

    - **Hsms** *(list) --*

      Contains information about the HSMs in the cluster.

      - *(dict) --*

        Contains information about a hardware security module (HSM) in an AWS CloudHSM cluster.

        - **AvailabilityZone** *(string) --*

          The Availability Zone that contains the HSM.

        - **ClusterId** *(string) --*

          The identifier (ID) of the cluster that contains the HSM.

        - **SubnetId** *(string) --*

          The subnet that contains the HSM's elastic network interface (ENI).

        - **EniId** *(string) --*

          The identifier (ID) of the HSM's elastic network interface (ENI).

        - **EniIp** *(string) --*

          The IP address of the HSM's elastic network interface (ENI).

        - **HsmId** *(string) --*

          The HSM's identifier (ID).

        - **State** *(string) --*

          The HSM's state.

        - **StateMessage** *(string) --*

          A description of the HSM's state.

    - **HsmType** *(string) --*

      The type of HSM that the cluster contains.

    - **PreCoPassword** *(string) --*

      The default password for the cluster's Pre-Crypto Officer (PRECO) user.

    - **SecurityGroup** *(string) --*

      The identifier (ID) of the cluster's security group.

    - **SourceBackupId** *(string) --*

      The identifier (ID) of the backup used to create the cluster. This value exists only when
      the cluster was created from a backup.

    - **State** *(string) --*

      The cluster's state.

    - **StateMessage** *(string) --*

      A description of the cluster's state.

    - **SubnetMapping** *(dict) --*

      A map of the cluster's subnets and their corresponding Availability Zones.

      - *(string) --*

        - *(string) --*

    - **VpcId** *(string) --*

      The identifier (ID) of the virtual private cloud (VPC) that contains the cluster.

    - **Certificates** *(dict) --*

      Contains one or more certificates or a certificate signing request (CSR).

      - **ClusterCsr** *(string) --*

        The cluster's certificate signing request (CSR). The CSR exists only when the cluster's
        state is ``UNINITIALIZED`` .

      - **HsmCertificate** *(string) --*

        The HSM certificate issued (signed) by the HSM hardware.

      - **AwsHardwareCertificate** *(string) --*

        The HSM hardware certificate issued (signed) by AWS CloudHSM.

      - **ManufacturerHardwareCertificate** *(string) --*

        The HSM hardware certificate issued (signed) by the hardware manufacturer.

      - **ClusterCertificate** *(string) --*

        The cluster certificate issued (signed) by the issuing certificate authority (CA) of
        the cluster's owner.
    """


_DescribeClustersPaginateResponseTypeDef = TypedDict(
    "_DescribeClustersPaginateResponseTypeDef",
    {"Clusters": List[DescribeClustersPaginateResponseClustersTypeDef]},
    total=False,
)


class DescribeClustersPaginateResponseTypeDef(_DescribeClustersPaginateResponseTypeDef):
    """
    Type definition for `DescribeClustersPaginate` `Response`

    - **Clusters** *(list) --*

      A list of clusters.

      - *(dict) --*

        Contains information about an AWS CloudHSM cluster.

        - **BackupPolicy** *(string) --*

          The cluster's backup policy.

        - **ClusterId** *(string) --*

          The cluster's identifier (ID).

        - **CreateTimestamp** *(datetime) --*

          The date and time when the cluster was created.

        - **Hsms** *(list) --*

          Contains information about the HSMs in the cluster.

          - *(dict) --*

            Contains information about a hardware security module (HSM) in an AWS CloudHSM cluster.

            - **AvailabilityZone** *(string) --*

              The Availability Zone that contains the HSM.

            - **ClusterId** *(string) --*

              The identifier (ID) of the cluster that contains the HSM.

            - **SubnetId** *(string) --*

              The subnet that contains the HSM's elastic network interface (ENI).

            - **EniId** *(string) --*

              The identifier (ID) of the HSM's elastic network interface (ENI).

            - **EniIp** *(string) --*

              The IP address of the HSM's elastic network interface (ENI).

            - **HsmId** *(string) --*

              The HSM's identifier (ID).

            - **State** *(string) --*

              The HSM's state.

            - **StateMessage** *(string) --*

              A description of the HSM's state.

        - **HsmType** *(string) --*

          The type of HSM that the cluster contains.

        - **PreCoPassword** *(string) --*

          The default password for the cluster's Pre-Crypto Officer (PRECO) user.

        - **SecurityGroup** *(string) --*

          The identifier (ID) of the cluster's security group.

        - **SourceBackupId** *(string) --*

          The identifier (ID) of the backup used to create the cluster. This value exists only when
          the cluster was created from a backup.

        - **State** *(string) --*

          The cluster's state.

        - **StateMessage** *(string) --*

          A description of the cluster's state.

        - **SubnetMapping** *(dict) --*

          A map of the cluster's subnets and their corresponding Availability Zones.

          - *(string) --*

            - *(string) --*

        - **VpcId** *(string) --*

          The identifier (ID) of the virtual private cloud (VPC) that contains the cluster.

        - **Certificates** *(dict) --*

          Contains one or more certificates or a certificate signing request (CSR).

          - **ClusterCsr** *(string) --*

            The cluster's certificate signing request (CSR). The CSR exists only when the cluster's
            state is ``UNINITIALIZED`` .

          - **HsmCertificate** *(string) --*

            The HSM certificate issued (signed) by the HSM hardware.

          - **AwsHardwareCertificate** *(string) --*

            The HSM hardware certificate issued (signed) by AWS CloudHSM.

          - **ManufacturerHardwareCertificate** *(string) --*

            The HSM hardware certificate issued (signed) by the hardware manufacturer.

          - **ClusterCertificate** *(string) --*

            The cluster certificate issued (signed) by the issuing certificate authority (CA) of
            the cluster's owner.
    """


_ListTagsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListTagsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListTagsPaginatePaginationConfigTypeDef(_ListTagsPaginatePaginationConfigTypeDef):
    """
    Type definition for `ListTagsPaginate` `PaginationConfig`

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


_ListTagsPaginateResponseTagListTypeDef = TypedDict(
    "_ListTagsPaginateResponseTagListTypeDef", {"Key": str, "Value": str}, total=False
)


class ListTagsPaginateResponseTagListTypeDef(_ListTagsPaginateResponseTagListTypeDef):
    """
    Type definition for `ListTagsPaginateResponse` `TagList`

    Contains a tag. A tag is a key-value pair.

    - **Key** *(string) --*

      The key of the tag.

    - **Value** *(string) --*

      The value of the tag.
    """


_ListTagsPaginateResponseTypeDef = TypedDict(
    "_ListTagsPaginateResponseTypeDef",
    {"TagList": List[ListTagsPaginateResponseTagListTypeDef]},
    total=False,
)


class ListTagsPaginateResponseTypeDef(_ListTagsPaginateResponseTypeDef):
    """
    Type definition for `ListTagsPaginate` `Response`

    - **TagList** *(list) --*

      A list of tags.

      - *(dict) --*

        Contains a tag. A tag is a key-value pair.

        - **Key** *(string) --*

          The key of the tag.

        - **Value** *(string) --*

          The value of the tag.
    """
