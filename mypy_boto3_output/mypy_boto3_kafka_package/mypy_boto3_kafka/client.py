"Main interface for kafka Client"
from __future__ import annotations

from typing import Dict, List
from typing_extensions import Literal, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator

# pylint: disable=import-self
import mypy_boto3_kafka.client as client_scope

# pylint: disable=import-self
import mypy_boto3_kafka.paginator as paginator_scope
from mypy_boto3_kafka.type_defs import (
    ClientCreateClusterBrokerNodeGroupInfoTypeDef,
    ClientCreateClusterClientAuthenticationTypeDef,
    ClientCreateClusterConfigurationInfoTypeDef,
    ClientCreateClusterEncryptionInfoTypeDef,
    ClientCreateClusterResponseTypeDef,
    ClientCreateConfigurationResponseTypeDef,
    ClientDeleteClusterResponseTypeDef,
    ClientDescribeClusterOperationResponseTypeDef,
    ClientDescribeClusterResponseTypeDef,
    ClientDescribeConfigurationResponseTypeDef,
    ClientDescribeConfigurationRevisionResponseTypeDef,
    ClientGetBootstrapBrokersResponseTypeDef,
    ClientListClusterOperationsResponseTypeDef,
    ClientListClustersResponseTypeDef,
    ClientListConfigurationRevisionsResponseTypeDef,
    ClientListConfigurationsResponseTypeDef,
    ClientListNodesResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientUpdateBrokerCountResponseTypeDef,
    ClientUpdateBrokerStorageResponseTypeDef,
    ClientUpdateBrokerStorageTargetBrokerEBSVolumeInfoTypeDef,
    ClientUpdateClusterConfigurationConfigurationInfoTypeDef,
    ClientUpdateClusterConfigurationResponseTypeDef,
)


__all__ = ("Client",)


class Client(BaseClient):
    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> None:
        """
        Check if an operation can be paginated.

        :type operation_name: string
        :param operation_name: The operation name.  This is the same name
            as the method name on the client.  For example, if the
            method name is ``create_foo``, and you'd normally invoke the
            operation as ``client.create_foo(**kwargs)``, if the
            ``create_foo`` operation can be paginated, you can use the
            call ``client.get_paginator("create_foo")``.

        :return: ``True`` if the operation can be paginated,
            ``False`` otherwise.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_cluster(
        self,
        BrokerNodeGroupInfo: ClientCreateClusterBrokerNodeGroupInfoTypeDef,
        ClusterName: str,
        KafkaVersion: str,
        NumberOfBrokerNodes: int,
        ClientAuthentication: ClientCreateClusterClientAuthenticationTypeDef = None,
        ConfigurationInfo: ClientCreateClusterConfigurationInfoTypeDef = None,
        EncryptionInfo: ClientCreateClusterEncryptionInfoTypeDef = None,
        EnhancedMonitoring: str = None,
        Tags: List[str] = None,
    ) -> ClientCreateClusterResponseTypeDef:
        """
        Creates a new MSK cluster.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kafka-2018-11-14/CreateCluster>`_

        **Request Syntax**
        ::

          response = client.create_cluster(
              BrokerNodeGroupInfo={
                  'BrokerAZDistribution': 'DEFAULT',
                  'ClientSubnets': [
                      'string',
                  ],
                  'InstanceType': 'string',
                  'SecurityGroups': [
                      'string',
                  ],
                  'StorageInfo': {
                      'EbsStorageInfo': {
                          'VolumeSize': 123
                      }
                  }
              },
              ClientAuthentication={
                  'Tls': {
                      'CertificateAuthorityArnList': [
                          'string',
                      ]
                  }
              },
              ClusterName='string',
              ConfigurationInfo={
                  'Arn': 'string',
                  'Revision': 123
              },
              EncryptionInfo={
                  'EncryptionAtRest': {
                      'DataVolumeKMSKeyId': 'string'
                  },
                  'EncryptionInTransit': {
                      'ClientBroker': 'TLS'|'TLS_PLAINTEXT'|'PLAINTEXT',
                      'InCluster': True|False
                  }
              },
              EnhancedMonitoring='DEFAULT'|'PER_BROKER'|'PER_TOPIC_PER_BROKER',
              KafkaVersion='string',
              NumberOfBrokerNodes=123,
              Tags={
                  'string': 'string'
              }
          )
        :type BrokerNodeGroupInfo: dict
        :param BrokerNodeGroupInfo: **[REQUIRED]**

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

        :type ClientAuthentication: dict
        :param ClientAuthentication:

          Includes all client authentication related information.

          - **Tls** *(dict) --*

            Details for ClientAuthentication using TLS.

            - **CertificateAuthorityArnList** *(list) --*

              List of ACM Certificate Authority ARNs.

              - *(string) --*

        :type ClusterName: string
        :param ClusterName: **[REQUIRED]**

          The name of the cluster.

        :type ConfigurationInfo: dict
        :param ConfigurationInfo:

          Represents the configuration that you want MSK to use for the brokers in a cluster.

          - **Arn** *(string) --* **[REQUIRED]**

            ARN of the configuration to use.

          - **Revision** *(integer) --* **[REQUIRED]**

            The revision of the configuration to use.

        :type EncryptionInfo: dict
        :param EncryptionInfo:

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

        :type EnhancedMonitoring: string
        :param EnhancedMonitoring:

          Specifies the level of monitoring for the MSK cluster. The possible values are DEFAULT,
          PER_BROKER, and PER_TOPIC_PER_BROKER.

        :type KafkaVersion: string
        :param KafkaVersion: **[REQUIRED]**

          The version of Apache Kafka.

        :type NumberOfBrokerNodes: integer
        :param NumberOfBrokerNodes: **[REQUIRED]**

          The number of broker nodes in the cluster.

        :type Tags: dict
        :param Tags:

          Create tags when creating the cluster.

          - *(string) --*

            - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ClusterArn': 'string',
                'ClusterName': 'string',
                'State': 'ACTIVE'|'CREATING'|'UPDATING'|'DELETING'|'FAILED'
            }
          **Response Structure**

          - *(dict) --*

            - **ClusterArn** *(string) --*

              The Amazon Resource Name (ARN) of the cluster.

            - **ClusterName** *(string) --*

              The name of the MSK cluster.

            - **State** *(string) --*

              The state of the cluster. The possible states are CREATING, ACTIVE, and FAILED.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_configuration(
        self,
        KafkaVersions: List[str],
        Name: str,
        ServerProperties: bytes,
        Description: str = None,
    ) -> ClientCreateConfigurationResponseTypeDef:
        """
        Creates a new MSK configuration.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kafka-2018-11-14/CreateConfiguration>`_

        **Request Syntax**
        ::

          response = client.create_configuration(
              Description='string',
              KafkaVersions=[
                  'string',
              ],
              Name='string',
              ServerProperties=b'bytes'
          )
        :type Description: string
        :param Description:

          The description of the configuration.

        :type KafkaVersions: list
        :param KafkaVersions: **[REQUIRED]**

          The versions of Apache Kafka with which you can use this MSK configuration.

          - *(string) --*

        :type Name: string
        :param Name: **[REQUIRED]**

          The name of the configuration.

        :type ServerProperties: bytes
        :param ServerProperties: **[REQUIRED]**

          Contents of the server.propertiesfile. When using the API, you must ensure that the contents of
          the file are base64 encoded. When using the AWS Management Console, the SDK, or the AWS CLI, the
          contents of server.propertiescan be in plaintext.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Arn': 'string',
                'CreationTime': datetime(2015, 1, 1),
                'LatestRevision': {
                    'CreationTime': datetime(2015, 1, 1),
                    'Description': 'string',
                    'Revision': 123
                },
                'Name': 'string'
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_cluster(
        self, ClusterArn: str, CurrentVersion: str = None
    ) -> ClientDeleteClusterResponseTypeDef:
        """
        Deletes the MSK cluster specified by the Amazon Resource Name (ARN) in the request.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kafka-2018-11-14/DeleteCluster>`_

        **Request Syntax**
        ::

          response = client.delete_cluster(
              ClusterArn='string',
              CurrentVersion='string'
          )
        :type ClusterArn: string
        :param ClusterArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) that uniquely identifies the cluster.

        :type CurrentVersion: string
        :param CurrentVersion:

          The current version of the MSK cluster.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ClusterArn': 'string',
                'State': 'ACTIVE'|'CREATING'|'UPDATING'|'DELETING'|'FAILED'
            }
          **Response Structure**

          - *(dict) --*

            Successful response.

            - **ClusterArn** *(string) --*

              The Amazon Resource Name (ARN) of the cluster.

            - **State** *(string) --*

              The state of the cluster. The possible states are CREATING, ACTIVE, and FAILED.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_cluster(self, ClusterArn: str) -> ClientDescribeClusterResponseTypeDef:
        """
        Returns a description of the MSK cluster whose Amazon Resource Name (ARN) is specified in the
        request.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kafka-2018-11-14/DescribeCluster>`_

        **Request Syntax**
        ::

          response = client.describe_cluster(
              ClusterArn='string'
          )
        :type ClusterArn: string
        :param ClusterArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) that uniquely identifies the cluster.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ClusterInfo': {
                    'ActiveOperationArn': 'string',
                    'BrokerNodeGroupInfo': {
                        'BrokerAZDistribution': 'DEFAULT',
                        'ClientSubnets': [
                            'string',
                        ],
                        'InstanceType': 'string',
                        'SecurityGroups': [
                            'string',
                        ],
                        'StorageInfo': {
                            'EbsStorageInfo': {
                                'VolumeSize': 123
                            }
                        }
                    },
                    'ClientAuthentication': {
                        'Tls': {
                            'CertificateAuthorityArnList': [
                                'string',
                            ]
                        }
                    },
                    'ClusterArn': 'string',
                    'ClusterName': 'string',
                    'CreationTime': datetime(2015, 1, 1),
                    'CurrentBrokerSoftwareInfo': {
                        'ConfigurationArn': 'string',
                        'ConfigurationRevision': 123,
                        'KafkaVersion': 'string'
                    },
                    'CurrentVersion': 'string',
                    'EncryptionInfo': {
                        'EncryptionAtRest': {
                            'DataVolumeKMSKeyId': 'string'
                        },
                        'EncryptionInTransit': {
                            'ClientBroker': 'TLS'|'TLS_PLAINTEXT'|'PLAINTEXT',
                            'InCluster': True|False
                        }
                    },
                    'EnhancedMonitoring': 'DEFAULT'|'PER_BROKER'|'PER_TOPIC_PER_BROKER',
                    'NumberOfBrokerNodes': 123,
                    'State': 'ACTIVE'|'CREATING'|'UPDATING'|'DELETING'|'FAILED',
                    'Tags': {
                        'string': 'string'
                    },
                    'ZookeeperConnectString': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_cluster_operation(
        self, ClusterOperationArn: str
    ) -> ClientDescribeClusterOperationResponseTypeDef:
        """
        Returns a description of the cluster operation specified by the ARN.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kafka-2018-11-14/DescribeClusterOperation>`_

        **Request Syntax**
        ::

          response = client.describe_cluster_operation(
              ClusterOperationArn='string'
          )
        :type ClusterOperationArn: string
        :param ClusterOperationArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) that uniquely identifies the MSK cluster operation.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ClusterOperationInfo': {
                    'ClientRequestId': 'string',
                    'ClusterArn': 'string',
                    'CreationTime': datetime(2015, 1, 1),
                    'EndTime': datetime(2015, 1, 1),
                    'ErrorInfo': {
                        'ErrorCode': 'string',
                        'ErrorString': 'string'
                    },
                    'OperationArn': 'string',
                    'OperationState': 'string',
                    'OperationType': 'string',
                    'SourceClusterInfo': {
                        'BrokerEBSVolumeInfo': [
                            {
                                'KafkaBrokerNodeId': 'string',
                                'VolumeSizeGB': 123
                            },
                        ],
                        'ConfigurationInfo': {
                            'Arn': 'string',
                            'Revision': 123
                        },
                        'NumberOfBrokerNodes': 123
                    },
                    'TargetClusterInfo': {
                        'BrokerEBSVolumeInfo': [
                            {
                                'KafkaBrokerNodeId': 'string',
                                'VolumeSizeGB': 123
                            },
                        ],
                        'ConfigurationInfo': {
                            'Arn': 'string',
                            'Revision': 123
                        },
                        'NumberOfBrokerNodes': 123
                    }
                }
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_configuration(
        self, Arn: str
    ) -> ClientDescribeConfigurationResponseTypeDef:
        """
        Returns a description of this MSK configuration.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kafka-2018-11-14/DescribeConfiguration>`_

        **Request Syntax**
        ::

          response = client.describe_configuration(
              Arn='string'
          )
        :type Arn: string
        :param Arn: **[REQUIRED]**

          The Amazon Resource Name (ARN) that uniquely identifies an MSK configuration and all of its
          revisions.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Arn': 'string',
                'CreationTime': datetime(2015, 1, 1),
                'Description': 'string',
                'KafkaVersions': [
                    'string',
                ],
                'LatestRevision': {
                    'CreationTime': datetime(2015, 1, 1),
                    'Description': 'string',
                    'Revision': 123
                },
                'Name': 'string'
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_configuration_revision(
        self, Arn: str, Revision: int
    ) -> ClientDescribeConfigurationRevisionResponseTypeDef:
        """
        Returns a description of this revision of the configuration.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kafka-2018-11-14/DescribeConfigurationRevision>`_

        **Request Syntax**
        ::

          response = client.describe_configuration_revision(
              Arn='string',
              Revision=123
          )
        :type Arn: string
        :param Arn: **[REQUIRED]**

          The Amazon Resource Name (ARN) that uniquely identifies an MSK configuration and all of its
          revisions.

        :type Revision: integer
        :param Revision: **[REQUIRED]**

          A string that uniquely identifies a revision of an MSK configuration.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Arn': 'string',
                'CreationTime': datetime(2015, 1, 1),
                'Description': 'string',
                'Revision': 123,
                'ServerProperties': b'bytes'
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        Generate a presigned url given a client, its method, and arguments

        :type ClientMethod: string
        :param ClientMethod: The client method to presign for

        :type Params: dict
        :param Params: The parameters normally passed to
            ``ClientMethod``.

        :type ExpiresIn: int
        :param ExpiresIn: The number of seconds the presigned url is valid
            for. By default it expires in an hour (3600 seconds)

        :type HttpMethod: string
        :param HttpMethod: The http method to use on the generated url. By
            default, the http method is whatever is used in the method's model.

        :returns: The presigned url
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_bootstrap_brokers(
        self, ClusterArn: str
    ) -> ClientGetBootstrapBrokersResponseTypeDef:
        """
        A list of brokers that a client application can use to bootstrap.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kafka-2018-11-14/GetBootstrapBrokers>`_

        **Request Syntax**
        ::

          response = client.get_bootstrap_brokers(
              ClusterArn='string'
          )
        :type ClusterArn: string
        :param ClusterArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) that uniquely identifies the cluster.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'BootstrapBrokerString': 'string',
                'BootstrapBrokerStringTls': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Successful response.

            - **BootstrapBrokerString** *(string) --*

              A string containing one or more hostname:port pairs.

            - **BootstrapBrokerStringTls** *(string) --*

              A string containing one or more DNS names (or IP) and TLS port pairs.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_cluster_operations(
        self, ClusterArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ClientListClusterOperationsResponseTypeDef:
        """
        Returns a list of all the operations that have been performed on the specified MSK cluster.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kafka-2018-11-14/ListClusterOperations>`_

        **Request Syntax**
        ::

          response = client.list_cluster_operations(
              ClusterArn='string',
              MaxResults=123,
              NextToken='string'
          )
        :type ClusterArn: string
        :param ClusterArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) that uniquely identifies the cluster.

        :type MaxResults: integer
        :param MaxResults:

          The maximum number of results to return in the response. If there are more results, the response
          includes a NextToken parameter.

        :type NextToken: string
        :param NextToken:

          The paginated results marker. When the result of the operation is truncated, the call returns
          NextToken in the response. To get the next batch, provide this token in your next request.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ClusterOperationInfoList': [
                    {
                        'ClientRequestId': 'string',
                        'ClusterArn': 'string',
                        'CreationTime': datetime(2015, 1, 1),
                        'EndTime': datetime(2015, 1, 1),
                        'ErrorInfo': {
                            'ErrorCode': 'string',
                            'ErrorString': 'string'
                        },
                        'OperationArn': 'string',
                        'OperationState': 'string',
                        'OperationType': 'string',
                        'SourceClusterInfo': {
                            'BrokerEBSVolumeInfo': [
                                {
                                    'KafkaBrokerNodeId': 'string',
                                    'VolumeSizeGB': 123
                                },
                            ],
                            'ConfigurationInfo': {
                                'Arn': 'string',
                                'Revision': 123
                            },
                            'NumberOfBrokerNodes': 123
                        },
                        'TargetClusterInfo': {
                            'BrokerEBSVolumeInfo': [
                                {
                                    'KafkaBrokerNodeId': 'string',
                                    'VolumeSizeGB': 123
                                },
                            ],
                            'ConfigurationInfo': {
                                'Arn': 'string',
                                'Revision': 123
                            },
                            'NumberOfBrokerNodes': 123
                        }
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_clusters(
        self,
        ClusterNameFilter: str = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientListClustersResponseTypeDef:
        """
        Returns a list of all the MSK clusters in the current Region.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kafka-2018-11-14/ListClusters>`_

        **Request Syntax**
        ::

          response = client.list_clusters(
              ClusterNameFilter='string',
              MaxResults=123,
              NextToken='string'
          )
        :type ClusterNameFilter: string
        :param ClusterNameFilter:

          Specify a prefix of the name of the clusters that you want to list. The service lists all the
          clusters whose names start with this prefix.

        :type MaxResults: integer
        :param MaxResults:

          The maximum number of results to return in the response. If there are more results, the response
          includes a NextToken parameter.

        :type NextToken: string
        :param NextToken:

          The paginated results marker. When the result of the operation is truncated, the call returns
          NextToken in the response. To get the next batch, provide this token in your next request.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ClusterInfoList': [
                    {
                        'ActiveOperationArn': 'string',
                        'BrokerNodeGroupInfo': {
                            'BrokerAZDistribution': 'DEFAULT',
                            'ClientSubnets': [
                                'string',
                            ],
                            'InstanceType': 'string',
                            'SecurityGroups': [
                                'string',
                            ],
                            'StorageInfo': {
                                'EbsStorageInfo': {
                                    'VolumeSize': 123
                                }
                            }
                        },
                        'ClientAuthentication': {
                            'Tls': {
                                'CertificateAuthorityArnList': [
                                    'string',
                                ]
                            }
                        },
                        'ClusterArn': 'string',
                        'ClusterName': 'string',
                        'CreationTime': datetime(2015, 1, 1),
                        'CurrentBrokerSoftwareInfo': {
                            'ConfigurationArn': 'string',
                            'ConfigurationRevision': 123,
                            'KafkaVersion': 'string'
                        },
                        'CurrentVersion': 'string',
                        'EncryptionInfo': {
                            'EncryptionAtRest': {
                                'DataVolumeKMSKeyId': 'string'
                            },
                            'EncryptionInTransit': {
                                'ClientBroker': 'TLS'|'TLS_PLAINTEXT'|'PLAINTEXT',
                                'InCluster': True|False
                            }
                        },
                        'EnhancedMonitoring': 'DEFAULT'|'PER_BROKER'|'PER_TOPIC_PER_BROKER',
                        'NumberOfBrokerNodes': 123,
                        'State': 'ACTIVE'|'CREATING'|'UPDATING'|'DELETING'|'FAILED',
                        'Tags': {
                            'string': 'string'
                        },
                        'ZookeeperConnectString': 'string'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_configuration_revisions(
        self, Arn: str, MaxResults: int = None, NextToken: str = None
    ) -> ClientListConfigurationRevisionsResponseTypeDef:
        """
        Returns a list of all the MSK configurations in this Region.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kafka-2018-11-14/ListConfigurationRevisions>`_

        **Request Syntax**
        ::

          response = client.list_configuration_revisions(
              Arn='string',
              MaxResults=123,
              NextToken='string'
          )
        :type Arn: string
        :param Arn: **[REQUIRED]**

          The Amazon Resource Name (ARN) that uniquely identifies an MSK configuration and all of its
          revisions.

        :type MaxResults: integer
        :param MaxResults:

          The maximum number of results to return in the response. If there are more results, the response
          includes a NextToken parameter.

        :type NextToken: string
        :param NextToken:

          The paginated results marker. When the result of the operation is truncated, the call returns
          NextToken in the response. To get the next batch, provide this token in your next request.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'NextToken': 'string',
                'Revisions': [
                    {
                        'CreationTime': datetime(2015, 1, 1),
                        'Description': 'string',
                        'Revision': 123
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_configurations(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ClientListConfigurationsResponseTypeDef:
        """
        Returns a list of all the MSK configurations in this Region.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kafka-2018-11-14/ListConfigurations>`_

        **Request Syntax**
        ::

          response = client.list_configurations(
              MaxResults=123,
              NextToken='string'
          )
        :type MaxResults: integer
        :param MaxResults:

          The maximum number of results to return in the response. If there are more results, the response
          includes a NextToken parameter.

        :type NextToken: string
        :param NextToken:

          The paginated results marker. When the result of the operation is truncated, the call returns
          NextToken in the response. To get the next batch, provide this token in your next request.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Configurations': [
                    {
                        'Arn': 'string',
                        'CreationTime': datetime(2015, 1, 1),
                        'Description': 'string',
                        'KafkaVersions': [
                            'string',
                        ],
                        'LatestRevision': {
                            'CreationTime': datetime(2015, 1, 1),
                            'Description': 'string',
                            'Revision': 123
                        },
                        'Name': 'string'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_nodes(
        self, ClusterArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ClientListNodesResponseTypeDef:
        """
        Returns a list of the broker nodes in the cluster.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kafka-2018-11-14/ListNodes>`_

        **Request Syntax**
        ::

          response = client.list_nodes(
              ClusterArn='string',
              MaxResults=123,
              NextToken='string'
          )
        :type ClusterArn: string
        :param ClusterArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) that uniquely identifies the cluster.

        :type MaxResults: integer
        :param MaxResults:

          The maximum number of results to return in the response. If there are more results, the response
          includes a NextToken parameter.

        :type NextToken: string
        :param NextToken:

          The paginated results marker. When the result of the operation is truncated, the call returns
          NextToken in the response. To get the next batch, provide this token in your next request.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'NextToken': 'string',
                'NodeInfoList': [
                    {
                        'AddedToClusterTime': 'string',
                        'BrokerNodeInfo': {
                            'AttachedENIId': 'string',
                            'BrokerId': 123.0,
                            'ClientSubnet': 'string',
                            'ClientVpcIpAddress': 'string',
                            'CurrentBrokerSoftwareInfo': {
                                'ConfigurationArn': 'string',
                                'ConfigurationRevision': 123,
                                'KafkaVersion': 'string'
                            },
                            'Endpoints': [
                                'string',
                            ]
                        },
                        'InstanceType': 'string',
                        'NodeARN': 'string',
                        'NodeType': 'BROKER',
                        'ZookeeperNodeInfo': {
                            'AttachedENIId': 'string',
                            'ClientVpcIpAddress': 'string',
                            'Endpoints': [
                                'string',
                            ],
                            'ZookeeperId': 123.0,
                            'ZookeeperVersion': 'string'
                        }
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(
        self, ResourceArn: str
    ) -> ClientListTagsForResourceResponseTypeDef:
        """
        Returns a list of the tags associated with the specified resource.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kafka-2018-11-14/ListTagsForResource>`_

        **Request Syntax**
        ::

          response = client.list_tags_for_resource(
              ResourceArn='string'
          )
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) that uniquely identifies the resource that's associated with the
          tags.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Tags': {
                    'string': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            Success response.

            - **Tags** *(dict) --*

              The key-value pair for the resource tag.

              - *(string) --*

                - *(string) --*

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(self, ResourceArn: str, Tags: List[str]) -> None:
        """
        Adds tags to the specified MSK resource.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kafka-2018-11-14/TagResource>`_

        **Request Syntax**
        ::

          response = client.tag_resource(
              ResourceArn='string',
              Tags={
                  'string': 'string'
              }
          )
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) that uniquely identifies the resource that's associated with the
          tags.

        :type Tags: dict
        :param Tags: **[REQUIRED]**

          The key-value pair for the resource tag.

          - *(string) --*

            - *(string) --*

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> None:
        """
        Removes the tags associated with the keys that are provided in the query.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kafka-2018-11-14/UntagResource>`_

        **Request Syntax**
        ::

          response = client.untag_resource(
              ResourceArn='string',
              TagKeys=[
                  'string',
              ]
          )
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) that uniquely identifies the resource that's associated with the
          tags.

        :type TagKeys: list
        :param TagKeys: **[REQUIRED]**

          Tag keys must be unique for a given cluster. In addition, the following restrictions apply:

          * Each tag key must be unique. If you add a tag with a key that's already in use, your new tag
          overwrites the existing key-value pair.

          * You can't start a tag key with aws: because this prefix is reserved for use by AWS. AWS creates
          tags that begin with this prefix on your behalf, but you can't edit or delete them.

          * Tag keys must be between 1 and 128 Unicode characters in length.

          * Tag keys must consist of the following characters: Unicode letters, digits, white space, and
          the following special characters: _ . / = + - @.

          - *(string) --*

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_broker_count(
        self, ClusterArn: str, CurrentVersion: str, TargetNumberOfBrokerNodes: int
    ) -> ClientUpdateBrokerCountResponseTypeDef:
        """
        Updates the number of broker nodes in the cluster.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kafka-2018-11-14/UpdateBrokerCount>`_

        **Request Syntax**
        ::

          response = client.update_broker_count(
              ClusterArn='string',
              CurrentVersion='string',
              TargetNumberOfBrokerNodes=123
          )
        :type ClusterArn: string
        :param ClusterArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) that uniquely identifies the cluster.

        :type CurrentVersion: string
        :param CurrentVersion: **[REQUIRED]**

          The version of cluster to update from. A successful operation will then generate a new version.

        :type TargetNumberOfBrokerNodes: integer
        :param TargetNumberOfBrokerNodes: **[REQUIRED]**

          The number of broker nodes that you want the cluster to have after this operation completes
          successfully.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ClusterArn': 'string',
                'ClusterOperationArn': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Successful response.

            - **ClusterArn** *(string) --*

              The Amazon Resource Name (ARN) of the cluster.

            - **ClusterOperationArn** *(string) --*

              The Amazon Resource Name (ARN) of the cluster operation.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_broker_storage(
        self,
        ClusterArn: str,
        CurrentVersion: str,
        TargetBrokerEBSVolumeInfo: List[
            ClientUpdateBrokerStorageTargetBrokerEBSVolumeInfoTypeDef
        ],
    ) -> ClientUpdateBrokerStorageResponseTypeDef:
        """
        Updates the EBS storage associated with MSK brokers.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kafka-2018-11-14/UpdateBrokerStorage>`_

        **Request Syntax**
        ::

          response = client.update_broker_storage(
              ClusterArn='string',
              CurrentVersion='string',
              TargetBrokerEBSVolumeInfo=[
                  {
                      'KafkaBrokerNodeId': 'string',
                      'VolumeSizeGB': 123
                  },
              ]
          )
        :type ClusterArn: string
        :param ClusterArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) that uniquely identifies the cluster.

        :type CurrentVersion: string
        :param CurrentVersion: **[REQUIRED]**

          The version of cluster to update from. A successful operation will then generate a new version.

        :type TargetBrokerEBSVolumeInfo: list
        :param TargetBrokerEBSVolumeInfo: **[REQUIRED]**

          Describes the target volume size and the ID of the broker to apply the update to.

          - *(dict) --*

            Specifies the EBS volume upgrade information. The broker identifier must be set to the keyword
            ALL. This means the changes apply to all the brokers in the cluster.

            - **KafkaBrokerNodeId** *(string) --* **[REQUIRED]**

              The ID of the broker to update.

            - **VolumeSizeGB** *(integer) --* **[REQUIRED]**

              Size of the EBS volume to update.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ClusterArn': 'string',
                'ClusterOperationArn': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Successful response.

            - **ClusterArn** *(string) --*

              The Amazon Resource Name (ARN) of the cluster.

            - **ClusterOperationArn** *(string) --*

              The Amazon Resource Name (ARN) of the cluster operation.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_cluster_configuration(
        self,
        ClusterArn: str,
        ConfigurationInfo: ClientUpdateClusterConfigurationConfigurationInfoTypeDef,
        CurrentVersion: str,
    ) -> ClientUpdateClusterConfigurationResponseTypeDef:
        """
        Updates the cluster with the configuration that is specified in the request body.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kafka-2018-11-14/UpdateClusterConfiguration>`_

        **Request Syntax**
        ::

          response = client.update_cluster_configuration(
              ClusterArn='string',
              ConfigurationInfo={
                  'Arn': 'string',
                  'Revision': 123
              },
              CurrentVersion='string'
          )
        :type ClusterArn: string
        :param ClusterArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) that uniquely identifies the cluster.

        :type ConfigurationInfo: dict
        :param ConfigurationInfo: **[REQUIRED]**

          Represents the configuration that you want MSK to use for the brokers in a cluster.

          - **Arn** *(string) --* **[REQUIRED]**

            ARN of the configuration to use.

          - **Revision** *(integer) --* **[REQUIRED]**

            The revision of the configuration to use.

        :type CurrentVersion: string
        :param CurrentVersion: **[REQUIRED]**

          The version of the cluster that needs to be updated.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ClusterArn': 'string',
                'ClusterOperationArn': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Successful response.

            - **ClusterArn** *(string) --*

              The Amazon Resource Name (ARN) of the cluster.

            - **ClusterOperationArn** *(string) --*

              The Amazon Resource Name (ARN) of the cluster operation.

        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_cluster_operations"]
    ) -> paginator_scope.ListClusterOperationsPaginator:
        """
        Get Paginator for `list_cluster_operations` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_clusters"]
    ) -> paginator_scope.ListClustersPaginator:
        """
        Get Paginator for `list_clusters` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_configuration_revisions"]
    ) -> paginator_scope.ListConfigurationRevisionsPaginator:
        """
        Get Paginator for `list_configuration_revisions` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_configurations"]
    ) -> paginator_scope.ListConfigurationsPaginator:
        """
        Get Paginator for `list_configurations` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_nodes"]
    ) -> paginator_scope.ListNodesPaginator:
        """
        Get Paginator for `list_nodes` operation.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(self, operation_name: str) -> Boto3Paginator:
        """
        Create a paginator for an operation.

        :type operation_name: string
        :param operation_name: The operation name.  This is the same name
            as the method name on the client.  For example, if the
            method name is ``create_foo``, and you'd normally invoke the
            operation as ``client.create_foo(**kwargs)``, if the
            ``create_foo`` operation can be paginated, you can use the
            call ``client.get_paginator("create_foo")``.

        :raise OperationNotPageableError: Raised if the operation is not
            pageable.  You can use the ``client.can_paginate`` method to
            check if an operation is pageable.

        :rtype: L{botocore.paginate.Paginator}
        :return: A paginator object.
        """


class Exceptions:
    BadRequestException: Boto3ClientError
    ClientError: Boto3ClientError
    ConflictException: Boto3ClientError
    ForbiddenException: Boto3ClientError
    InternalServerErrorException: Boto3ClientError
    NotFoundException: Boto3ClientError
    ServiceUnavailableException: Boto3ClientError
    TooManyRequestsException: Boto3ClientError
    UnauthorizedException: Boto3ClientError
