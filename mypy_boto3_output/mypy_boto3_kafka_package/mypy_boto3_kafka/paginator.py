"Main interface for kafka Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_kafka.type_defs import (
    ListClusterOperationsPaginatePaginationConfigTypeDef,
    ListClusterOperationsPaginateResponseTypeDef,
    ListClustersPaginatePaginationConfigTypeDef,
    ListClustersPaginateResponseTypeDef,
    ListConfigurationRevisionsPaginatePaginationConfigTypeDef,
    ListConfigurationRevisionsPaginateResponseTypeDef,
    ListConfigurationsPaginatePaginationConfigTypeDef,
    ListConfigurationsPaginateResponseTypeDef,
    ListNodesPaginatePaginationConfigTypeDef,
    ListNodesPaginateResponseTypeDef,
)


__all__ = (
    "ListClusterOperationsPaginator",
    "ListClustersPaginator",
    "ListConfigurationRevisionsPaginator",
    "ListConfigurationsPaginator",
    "ListNodesPaginator",
)


class ListClusterOperationsPaginator(Boto3Paginator):
    """
    Paginator for `list_cluster_operations`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ClusterArn: str,
        PaginationConfig: ListClusterOperationsPaginatePaginationConfigTypeDef = None,
    ) -> ListClusterOperationsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`Kafka.Client.list_cluster_operations`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kafka-2018-11-14/ListClusterOperations>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              ClusterArn='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type ClusterArn: string
        :param ClusterArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) that uniquely identifies the cluster.

        :type PaginationConfig: dict
        :param PaginationConfig:

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

        """


class ListClustersPaginator(Boto3Paginator):
    """
    Paginator for `list_clusters`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ClusterNameFilter: str = None,
        PaginationConfig: ListClustersPaginatePaginationConfigTypeDef = None,
    ) -> ListClustersPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Kafka.Client.list_clusters`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kafka-2018-11-14/ListClusters>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              ClusterNameFilter='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type ClusterNameFilter: string
        :param ClusterNameFilter:

          Specify a prefix of the name of the clusters that you want to list. The service lists all the
          clusters whose names start with this prefix.

        :type PaginationConfig: dict
        :param PaginationConfig:

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

        """


class ListConfigurationRevisionsPaginator(Boto3Paginator):
    """
    Paginator for `list_configuration_revisions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Arn: str,
        PaginationConfig: ListConfigurationRevisionsPaginatePaginationConfigTypeDef = None,
    ) -> ListConfigurationRevisionsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`Kafka.Client.list_configuration_revisions`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kafka-2018-11-14/ListConfigurationRevisions>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              Arn='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type Arn: string
        :param Arn: **[REQUIRED]**

          The Amazon Resource Name (ARN) that uniquely identifies an MSK configuration and all of its
          revisions.

        :type PaginationConfig: dict
        :param PaginationConfig:

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

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
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


class ListConfigurationsPaginator(Boto3Paginator):
    """
    Paginator for `list_configurations`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListConfigurationsPaginatePaginationConfigTypeDef = None
    ) -> ListConfigurationsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`Kafka.Client.list_configurations`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kafka-2018-11-14/ListConfigurations>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type PaginationConfig: dict
        :param PaginationConfig:

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

        """


class ListNodesPaginator(Boto3Paginator):
    """
    Paginator for `list_nodes`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ClusterArn: str,
        PaginationConfig: ListNodesPaginatePaginationConfigTypeDef = None,
    ) -> ListNodesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Kafka.Client.list_nodes`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kafka-2018-11-14/ListNodes>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              ClusterArn='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type ClusterArn: string
        :param ClusterArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) that uniquely identifies the cluster.

        :type PaginationConfig: dict
        :param PaginationConfig:

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

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
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
