"Main interface for elasticache Client"
from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List
from typing_extensions import Literal, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator
from botocore.waiter import Waiter as Boto3Waiter

# pylint: disable=import-self
import mypy_boto3_elasticache.client as client_scope

# pylint: disable=import-self
import mypy_boto3_elasticache.paginator as paginator_scope
from mypy_boto3_elasticache.type_defs import (
    ClientAddTagsToResourceResponseTypeDef,
    ClientAddTagsToResourceTagsTypeDef,
    ClientAuthorizeCacheSecurityGroupIngressResponseTypeDef,
    ClientBatchApplyUpdateActionResponseTypeDef,
    ClientBatchStopUpdateActionResponseTypeDef,
    ClientCompleteMigrationResponseTypeDef,
    ClientCopySnapshotResponseTypeDef,
    ClientCreateCacheClusterResponseTypeDef,
    ClientCreateCacheClusterTagsTypeDef,
    ClientCreateCacheParameterGroupResponseTypeDef,
    ClientCreateCacheSecurityGroupResponseTypeDef,
    ClientCreateCacheSubnetGroupResponseTypeDef,
    ClientCreateReplicationGroupNodeGroupConfigurationTypeDef,
    ClientCreateReplicationGroupResponseTypeDef,
    ClientCreateReplicationGroupTagsTypeDef,
    ClientCreateSnapshotResponseTypeDef,
    ClientDecreaseReplicaCountReplicaConfigurationTypeDef,
    ClientDecreaseReplicaCountResponseTypeDef,
    ClientDeleteCacheClusterResponseTypeDef,
    ClientDeleteReplicationGroupResponseTypeDef,
    ClientDeleteSnapshotResponseTypeDef,
    ClientDescribeCacheClustersResponseTypeDef,
    ClientDescribeCacheEngineVersionsResponseTypeDef,
    ClientDescribeCacheParameterGroupsResponseTypeDef,
    ClientDescribeCacheParametersResponseTypeDef,
    ClientDescribeCacheSecurityGroupsResponseTypeDef,
    ClientDescribeCacheSubnetGroupsResponseTypeDef,
    ClientDescribeEngineDefaultParametersResponseTypeDef,
    ClientDescribeEventsResponseTypeDef,
    ClientDescribeReplicationGroupsResponseTypeDef,
    ClientDescribeReservedCacheNodesOfferingsResponseTypeDef,
    ClientDescribeServiceUpdatesResponseTypeDef,
    ClientDescribeSnapshotsResponseTypeDef,
    ClientDescribeUpdateActionsResponseTypeDef,
    ClientDescribeUpdateActionsServiceUpdateTimeRangeTypeDef,
    ClientIncreaseReplicaCountReplicaConfigurationTypeDef,
    ClientIncreaseReplicaCountResponseTypeDef,
    ClientListAllowedNodeTypeModificationsResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientModifyCacheClusterResponseTypeDef,
    ClientModifyCacheParameterGroupParameterNameValuesTypeDef,
    ClientModifyCacheParameterGroupResponseTypeDef,
    ClientModifyCacheSubnetGroupResponseTypeDef,
    ClientModifyReplicationGroupResponseTypeDef,
    ClientModifyReplicationGroupShardConfigurationReshardingConfigurationTypeDef,
    ClientModifyReplicationGroupShardConfigurationResponseTypeDef,
    ClientPurchaseReservedCacheNodesOfferingResponseTypeDef,
    ClientRebootCacheClusterResponseTypeDef,
    ClientRemoveTagsFromResourceResponseTypeDef,
    ClientResetCacheParameterGroupParameterNameValuesTypeDef,
    ClientResetCacheParameterGroupResponseTypeDef,
    ClientRevokeCacheSecurityGroupIngressResponseTypeDef,
    ClientStartMigrationCustomerNodeEndpointListTypeDef,
    ClientStartMigrationResponseTypeDef,
    ClientTestFailoverResponseTypeDef,
)

# pylint: disable=import-self
import mypy_boto3_elasticache.waiter as waiter_scope


__all__ = ("Client",)


class Client(BaseClient):
    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def add_tags_to_resource(
        self, ResourceName: str, Tags: List[ClientAddTagsToResourceTagsTypeDef]
    ) -> ClientAddTagsToResourceResponseTypeDef:
        """
        Adds up to 50 cost allocation tags to the named resource. A cost allocation tag is a key-value pair
        where the key and value are case-sensitive. You can use cost allocation tags to categorize and
        track your AWS costs.

        When you apply tags to your ElastiCache resources, AWS generates a cost allocation report as a
        comma-separated value (CSV) file with your usage and costs aggregated by your tags. You can apply
        tags that represent business categories (such as cost centers, application names, or owners) to
        organize your costs across multiple services. For more information, see `Using Cost Allocation Tags
        in Amazon ElastiCache <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Tagging.html>`__
        in the *ElastiCache User Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/AddTagsToResource>`_

        **Request Syntax**
        ::

          response = client.add_tags_to_resource(
              ResourceName='string',
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        :type ResourceName: string
        :param ResourceName: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the resource to which the tags are to be added, for example
          ``arn:aws:elasticache:us-west-2:0123456789:cluster:myCluster`` or
          ``arn:aws:elasticache:us-west-2:0123456789:snapshot:mySnapshot`` . ElastiCache resources are
          *cluster* and *snapshot* .

          For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS Service Namespaces
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

        :type Tags: list
        :param Tags: **[REQUIRED]**

          A list of cost allocation tags to be added to this resource. A tag is a key-value pair. A tag key
          must be accompanied by a tag value.

          - *(dict) --*

            A cost allocation Tag that can be added to an ElastiCache cluster or replication group. Tags
            are composed of a Key/Value pair. A tag with a null Value is permitted.

            - **Key** *(string) --*

              The key for the tag. May not be null.

            - **Value** *(string) --*

              The tag's value. May be null.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'TagList': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            Represents the output from the ``AddTagsToResource`` , ``ListTagsForResource`` , and
            ``RemoveTagsFromResource`` operations.

            - **TagList** *(list) --*

              A list of cost allocation tags as key-value pairs.

              - *(dict) --*

                A cost allocation Tag that can be added to an ElastiCache cluster or replication group.
                Tags are composed of a Key/Value pair. A tag with a null Value is permitted.

                - **Key** *(string) --*

                  The key for the tag. May not be null.

                - **Value** *(string) --*

                  The tag's value. May be null.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def authorize_cache_security_group_ingress(
        self,
        CacheSecurityGroupName: str,
        EC2SecurityGroupName: str,
        EC2SecurityGroupOwnerId: str,
    ) -> ClientAuthorizeCacheSecurityGroupIngressResponseTypeDef:
        """
        Allows network ingress to a cache security group. Applications using ElastiCache must be running on
        Amazon EC2, and Amazon EC2 security groups are used as the authorization mechanism.

        .. note::

          You cannot authorize ingress from an Amazon EC2 security group in one region to an ElastiCache
          cluster in another region.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/AuthorizeCacheSecurityGroupIngress>`_
        <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/AuthorizeCacheSecurityGroupIngress>`_

        **Request Syntax**
        ::

          response = client.authorize_cache_security_group_ingress(
              CacheSecurityGroupName='string',
              EC2SecurityGroupName='string',
              EC2SecurityGroupOwnerId='string'
          )
        :type CacheSecurityGroupName: string
        :param CacheSecurityGroupName: **[REQUIRED]**

          The cache security group that allows network ingress.

        :type EC2SecurityGroupName: string
        :param EC2SecurityGroupName: **[REQUIRED]**

          The Amazon EC2 security group to be authorized for ingress to the cache security group.

        :type EC2SecurityGroupOwnerId: string
        :param EC2SecurityGroupOwnerId: **[REQUIRED]**

          The AWS account number of the Amazon EC2 security group owner. Note that this is not the same
          thing as an AWS access key ID - you must provide a valid AWS account number for this parameter.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'CacheSecurityGroup': {
                    'OwnerId': 'string',
                    'CacheSecurityGroupName': 'string',
                    'Description': 'string',
                    'EC2SecurityGroups': [
                        {
                            'Status': 'string',
                            'EC2SecurityGroupName': 'string',
                            'EC2SecurityGroupOwnerId': 'string'
                        },
                    ]
                }
            }
          **Response Structure**

          - *(dict) --*

            - **CacheSecurityGroup** *(dict) --*

              Represents the output of one of the following operations:

              * ``AuthorizeCacheSecurityGroupIngress``

              * ``CreateCacheSecurityGroup``

              * ``RevokeCacheSecurityGroupIngress``

              - **OwnerId** *(string) --*

                The AWS account ID of the cache security group owner.

              - **CacheSecurityGroupName** *(string) --*

                The name of the cache security group.

              - **Description** *(string) --*

                The description of the cache security group.

              - **EC2SecurityGroups** *(list) --*

                A list of Amazon EC2 security groups that are associated with this cache security group.

                - *(dict) --*

                  Provides ownership and status information for an Amazon EC2 security group.

                  - **Status** *(string) --*

                    The status of the Amazon EC2 security group.

                  - **EC2SecurityGroupName** *(string) --*

                    The name of the Amazon EC2 security group.

                  - **EC2SecurityGroupOwnerId** *(string) --*

                    The AWS account ID of the Amazon EC2 security group owner.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_apply_update_action(
        self,
        ServiceUpdateName: str,
        ReplicationGroupIds: List[str] = None,
        CacheClusterIds: List[str] = None,
    ) -> ClientBatchApplyUpdateActionResponseTypeDef:
        """
        Apply the service update. For more information on service updates and applying them, see `Applying
        Service Updates
        <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/applying-updates.html>`__ .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/BatchApplyUpdateAction>`_

        **Request Syntax**
        ::

          response = client.batch_apply_update_action(
              ReplicationGroupIds=[
                  'string',
              ],
              CacheClusterIds=[
                  'string',
              ],
              ServiceUpdateName='string'
          )
        :type ReplicationGroupIds: list
        :param ReplicationGroupIds:

          The replication group IDs

          - *(string) --*

        :type CacheClusterIds: list
        :param CacheClusterIds:

          The cache cluster IDs

          - *(string) --*

        :type ServiceUpdateName: string
        :param ServiceUpdateName: **[REQUIRED]**

          The unique ID of the service update

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ProcessedUpdateActions': [
                    {
                        'ReplicationGroupId': 'string',
                        'CacheClusterId': 'string',
                        'ServiceUpdateName': 'string',
                        'UpdateActionStatus':
                        'not-applied'|'waiting-to-start'|'in-progress'|'stopping'|'stopped'|'complete'
                    },
                ],
                'UnprocessedUpdateActions': [
                    {
                        'ReplicationGroupId': 'string',
                        'CacheClusterId': 'string',
                        'ServiceUpdateName': 'string',
                        'ErrorType': 'string',
                        'ErrorMessage': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **ProcessedUpdateActions** *(list) --*

              Update actions that have been processed successfully

              - *(dict) --*

                Update action that has been processed for the corresponding apply/stop request

                - **ReplicationGroupId** *(string) --*

                  The ID of the replication group

                - **CacheClusterId** *(string) --*

                  The ID of the cache cluster

                - **ServiceUpdateName** *(string) --*

                  The unique ID of the service update

                - **UpdateActionStatus** *(string) --*

                  The status of the update action on the Redis cluster

            - **UnprocessedUpdateActions** *(list) --*

              Update actions that haven't been processed successfully

              - *(dict) --*

                Update action that has failed to be processed for the corresponding apply/stop request

                - **ReplicationGroupId** *(string) --*

                  The replication group ID

                - **CacheClusterId** *(string) --*

                  The ID of the cache cluster

                - **ServiceUpdateName** *(string) --*

                  The unique ID of the service update

                - **ErrorType** *(string) --*

                  The error type for requests that are not processed

                - **ErrorMessage** *(string) --*

                  The error message that describes the reason the request was not processed

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_stop_update_action(
        self,
        ServiceUpdateName: str,
        ReplicationGroupIds: List[str] = None,
        CacheClusterIds: List[str] = None,
    ) -> ClientBatchStopUpdateActionResponseTypeDef:
        """
        Stop the service update. For more information on service updates and stopping them, see `Stopping
        Service Updates
        <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/stopping-self-service-updates.html>`__
        .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/BatchStopUpdateAction>`_

        **Request Syntax**
        ::

          response = client.batch_stop_update_action(
              ReplicationGroupIds=[
                  'string',
              ],
              CacheClusterIds=[
                  'string',
              ],
              ServiceUpdateName='string'
          )
        :type ReplicationGroupIds: list
        :param ReplicationGroupIds:

          The replication group IDs

          - *(string) --*

        :type CacheClusterIds: list
        :param CacheClusterIds:

          The cache cluster IDs

          - *(string) --*

        :type ServiceUpdateName: string
        :param ServiceUpdateName: **[REQUIRED]**

          The unique ID of the service update

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ProcessedUpdateActions': [
                    {
                        'ReplicationGroupId': 'string',
                        'CacheClusterId': 'string',
                        'ServiceUpdateName': 'string',
                        'UpdateActionStatus':
                        'not-applied'|'waiting-to-start'|'in-progress'|'stopping'|'stopped'|'complete'
                    },
                ],
                'UnprocessedUpdateActions': [
                    {
                        'ReplicationGroupId': 'string',
                        'CacheClusterId': 'string',
                        'ServiceUpdateName': 'string',
                        'ErrorType': 'string',
                        'ErrorMessage': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **ProcessedUpdateActions** *(list) --*

              Update actions that have been processed successfully

              - *(dict) --*

                Update action that has been processed for the corresponding apply/stop request

                - **ReplicationGroupId** *(string) --*

                  The ID of the replication group

                - **CacheClusterId** *(string) --*

                  The ID of the cache cluster

                - **ServiceUpdateName** *(string) --*

                  The unique ID of the service update

                - **UpdateActionStatus** *(string) --*

                  The status of the update action on the Redis cluster

            - **UnprocessedUpdateActions** *(list) --*

              Update actions that haven't been processed successfully

              - *(dict) --*

                Update action that has failed to be processed for the corresponding apply/stop request

                - **ReplicationGroupId** *(string) --*

                  The replication group ID

                - **CacheClusterId** *(string) --*

                  The ID of the cache cluster

                - **ServiceUpdateName** *(string) --*

                  The unique ID of the service update

                - **ErrorType** *(string) --*

                  The error type for requests that are not processed

                - **ErrorMessage** *(string) --*

                  The error message that describes the reason the request was not processed

        """

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
    def complete_migration(
        self, ReplicationGroupId: str, Force: bool = None
    ) -> ClientCompleteMigrationResponseTypeDef:
        """
        Complete the migration of data.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/CompleteMigration>`_

        **Request Syntax**
        ::

          response = client.complete_migration(
              ReplicationGroupId='string',
              Force=True|False
          )
        :type ReplicationGroupId: string
        :param ReplicationGroupId: **[REQUIRED]**

          The ID of the replication group to which data is being migrated.

        :type Force: boolean
        :param Force:

          Forces the migration to stop without ensuring that data is in sync. It is recommended to use this
          option only to abort the migration and not recommended when application wants to continue
          migration to ElastiCache.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ReplicationGroup': {
                    'ReplicationGroupId': 'string',
                    'Description': 'string',
                    'Status': 'string',
                    'PendingModifiedValues': {
                        'PrimaryClusterId': 'string',
                        'AutomaticFailoverStatus': 'enabled'|'disabled',
                        'Resharding': {
                            'SlotMigration': {
                                'ProgressPercentage': 123.0
                            }
                        },
                        'AuthTokenStatus': 'SETTING'|'ROTATING'
                    },
                    'MemberClusters': [
                        'string',
                    ],
                    'NodeGroups': [
                        {
                            'NodeGroupId': 'string',
                            'Status': 'string',
                            'PrimaryEndpoint': {
                                'Address': 'string',
                                'Port': 123
                            },
                            'ReaderEndpoint': {
                                'Address': 'string',
                                'Port': 123
                            },
                            'Slots': 'string',
                            'NodeGroupMembers': [
                                {
                                    'CacheClusterId': 'string',
                                    'CacheNodeId': 'string',
                                    'ReadEndpoint': {
                                        'Address': 'string',
                                        'Port': 123
                                    },
                                    'PreferredAvailabilityZone': 'string',
                                    'CurrentRole': 'string'
                                },
                            ]
                        },
                    ],
                    'SnapshottingClusterId': 'string',
                    'AutomaticFailover': 'enabled'|'disabled'|'enabling'|'disabling',
                    'ConfigurationEndpoint': {
                        'Address': 'string',
                        'Port': 123
                    },
                    'SnapshotRetentionLimit': 123,
                    'SnapshotWindow': 'string',
                    'ClusterEnabled': True|False,
                    'CacheNodeType': 'string',
                    'AuthTokenEnabled': True|False,
                    'AuthTokenLastModifiedDate': datetime(2015, 1, 1),
                    'TransitEncryptionEnabled': True|False,
                    'AtRestEncryptionEnabled': True|False,
                    'KmsKeyId': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **ReplicationGroup** *(dict) --*

              Contains all of the attributes of a specific Redis replication group.

              - **ReplicationGroupId** *(string) --*

                The identifier for the replication group.

              - **Description** *(string) --*

                The user supplied description of the replication group.

              - **Status** *(string) --*

                The current state of this replication group - ``creating`` , ``available`` , ``modifying``
                , ``deleting`` , ``create-failed`` , ``snapshotting`` .

              - **PendingModifiedValues** *(dict) --*

                A group of settings to be applied to the replication group, either immediately or during
                the next maintenance window.

                - **PrimaryClusterId** *(string) --*

                  The primary cluster ID that is applied immediately (if ``--apply-immediately`` was
                  specified), or during the next maintenance window.

                - **AutomaticFailoverStatus** *(string) --*

                  Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

                  Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

                  * Redis versions earlier than 2.8.6.

                  * Redis (cluster mode disabled): T1 node types.

                  * Redis (cluster mode enabled): T1 node types.

                - **Resharding** *(dict) --*

                  The status of an online resharding operation.

                  - **SlotMigration** *(dict) --*

                    Represents the progress of an online resharding operation.

                    - **ProgressPercentage** *(float) --*

                      The percentage of the slot migration that is complete.

                - **AuthTokenStatus** *(string) --*

                  The auth token status

              - **MemberClusters** *(list) --*

                The names of all the cache clusters that are part of this replication group.

                - *(string) --*

              - **NodeGroups** *(list) --*

                A list of node groups in this replication group. For Redis (cluster mode disabled)
                replication groups, this is a single-element list. For Redis (cluster mode enabled)
                replication groups, the list contains an entry for each node group (shard).

                - *(dict) --*

                  Represents a collection of cache nodes in a replication group. One node in the node group
                  is the read/write primary node. All the other nodes are read-only Replica nodes.

                  - **NodeGroupId** *(string) --*

                    The identifier for the node group (shard). A Redis (cluster mode disabled) replication
                    group contains only 1 node group; therefore, the node group ID is 0001. A Redis
                    (cluster mode enabled) replication group contains 1 to 90 node groups numbered 0001 to
                    0090. Optionally, the user can provide the id for a node group.

                  - **Status** *(string) --*

                    The current state of this replication group - ``creating`` , ``available`` , etc.

                  - **PrimaryEndpoint** *(dict) --*

                    The endpoint of the primary node in this node group (shard).

                    - **Address** *(string) --*

                      The DNS hostname of the cache node.

                    - **Port** *(integer) --*

                      The port number that the cache engine is listening on.

                  - **ReaderEndpoint** *(dict) --*

                    The endpoint of the replica nodes in this node group (shard).

                    - **Address** *(string) --*

                      The DNS hostname of the cache node.

                    - **Port** *(integer) --*

                      The port number that the cache engine is listening on.

                  - **Slots** *(string) --*

                    The keyspace for this node group (shard).

                  - **NodeGroupMembers** *(list) --*

                    A list containing information about individual nodes within the node group (shard).

                    - *(dict) --*

                      Represents a single node within a node group (shard).

                      - **CacheClusterId** *(string) --*

                        The ID of the cluster to which the node belongs.

                      - **CacheNodeId** *(string) --*

                        The ID of the node within its cluster. A node ID is a numeric identifier (0001,
                        0002, etc.).

                      - **ReadEndpoint** *(dict) --*

                        The information required for client programs to connect to a node for read
                        operations. The read endpoint is only applicable on Redis (cluster mode disabled)
                        clusters.

                        - **Address** *(string) --*

                          The DNS hostname of the cache node.

                        - **Port** *(integer) --*

                          The port number that the cache engine is listening on.

                      - **PreferredAvailabilityZone** *(string) --*

                        The name of the Availability Zone in which the node is located.

                      - **CurrentRole** *(string) --*

                        The role that is currently assigned to the node - ``primary`` or ``replica`` . This
                        member is only applicable for Redis (cluster mode disabled) replication groups.

              - **SnapshottingClusterId** *(string) --*

                The cluster ID that is used as the daily snapshot source for the replication group.

              - **AutomaticFailover** *(string) --*

                Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

                Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

                * Redis versions earlier than 2.8.6.

                * Redis (cluster mode disabled): T1 node types.

                * Redis (cluster mode enabled): T1 node types.

              - **ConfigurationEndpoint** *(dict) --*

                The configuration endpoint for this replication group. Use the configuration endpoint to
                connect to this replication group.

                - **Address** *(string) --*

                  The DNS hostname of the cache node.

                - **Port** *(integer) --*

                  The port number that the cache engine is listening on.

              - **SnapshotRetentionLimit** *(integer) --*

                The number of days for which ElastiCache retains automatic cluster snapshots before
                deleting them. For example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot that was
                taken today is retained for 5 days before being deleted.

                .. warning::

                  If the value of ``SnapshotRetentionLimit`` is set to zero (0), backups are turned off.

              - **SnapshotWindow** *(string) --*

                The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of
                your node group (shard).

                Example: ``05:00-09:00``

                If you do not specify this parameter, ElastiCache automatically chooses an appropriate time
                range.

                .. note::

                  This parameter is only valid if the ``Engine`` parameter is ``redis`` .

              - **ClusterEnabled** *(boolean) --*

                A flag indicating whether or not this replication group is cluster enabled; i.e., whether
                its data can be partitioned across multiple shards (API/CLI: node groups).

                Valid values: ``true`` | ``false``

              - **CacheNodeType** *(string) --*

                The name of the compute and memory capacity node type for each node in the replication
                group.

              - **AuthTokenEnabled** *(boolean) --*

                A flag that enables using an ``AuthToken`` (password) when issuing Redis commands.

                Default: ``false``

              - **AuthTokenLastModifiedDate** *(datetime) --*

                The date the auth token was last modified

              - **TransitEncryptionEnabled** *(boolean) --*

                A flag that enables in-transit encryption when set to ``true`` .

                You cannot modify the value of ``TransitEncryptionEnabled`` after the cluster is created.
                To enable in-transit encryption on a cluster you must set ``TransitEncryptionEnabled`` to
                ``true`` when you create a cluster.

                 **Required:** Only available when creating a replication group in an Amazon VPC using
                 redis version ``3.2.6`` , ``4.x`` or later.

                Default: ``false``

              - **AtRestEncryptionEnabled** *(boolean) --*

                A flag that enables encryption at-rest when set to ``true`` .

                You cannot modify the value of ``AtRestEncryptionEnabled`` after the cluster is created. To
                enable encryption at-rest on a cluster you must set ``AtRestEncryptionEnabled`` to ``true``
                when you create a cluster.

                 **Required:** Only available when creating a replication group in an Amazon VPC using
                 redis version ``3.2.6`` , ``4.x`` or later.

                Default: ``false``

              - **KmsKeyId** *(string) --*

                The ID of the KMS key used to encrypt the disk in the cluster.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def copy_snapshot(
        self,
        SourceSnapshotName: str,
        TargetSnapshotName: str,
        TargetBucket: str = None,
        KmsKeyId: str = None,
    ) -> ClientCopySnapshotResponseTypeDef:
        """
        Makes a copy of an existing snapshot.

        .. note::

          This operation is valid for Redis only.

        .. warning::

          Users or groups that have permissions to use the ``CopySnapshot`` operation can create their own
          Amazon S3 buckets and copy snapshots to it. To control access to your snapshots, use an IAM
          policy to control who has the ability to use the ``CopySnapshot`` operation. For more information
          about using IAM to control the use of ElastiCache operations, see `Exporting Snapshots
          <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/backups-exporting.html>`__ and
          `Authentication & Access Control
          <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/IAM.html>`__ .

        You could receive the following error messages.

         **Error Messages**

        * **Error Message:** The S3 bucket %s is outside of the region.  **Solution:** Create an Amazon S3
        bucket in the same region as your snapshot. For more information, see `Step 1\\: Create an Amazon
        S3 Bucket
        <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/backups-exporting.html#backups-exporting-create-s3-bucket>`__
        in the ElastiCache User Guide.

        * **Error Message:** The S3 bucket %s does not exist.  **Solution:** Create an Amazon S3 bucket in
        the same region as your snapshot. For more information, see `Step 1\\: Create an Amazon S3 Bucket
        <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/backups-exporting.html#backups-exporting-create-s3-bucket>`__
        in the ElastiCache User Guide.

        * **Error Message:** The S3 bucket %s is not owned by the authenticated user.  **Solution:** Create
        an Amazon S3 bucket in the same region as your snapshot. For more information, see `Step 1\\:
        Create an Amazon S3 Bucket
        <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/backups-exporting.html#backups-exporting-create-s3-bucket>`__
        in the ElastiCache User Guide.

        * **Error Message:** The authenticated user does not have sufficient permissions to perform the
        desired activity.  **Solution:** Contact your system administrator to get the needed permissions.

        * **Error Message:** The S3 bucket %s already contains an object with key %s.  **Solution:** Give
        the ``TargetSnapshotName`` a new and unique value. If exporting a snapshot, you could alternatively
        create a new Amazon S3 bucket and use this same value for ``TargetSnapshotName`` .

        * **Error Message:** ElastiCache has not been granted READ permissions %s on the S3 Bucket.
        **Solution:** Add List and Read permissions on the bucket. For more information, see `Step 2\\:
        Grant ElastiCache Access to Your Amazon S3 Bucket
        <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/backups-exporting.html#backups-exporting-grant-access>`__
        in the ElastiCache User Guide.

        * **Error Message:** ElastiCache has not been granted WRITE permissions %s on the S3 Bucket.
        **Solution:** Add Upload/Delete permissions on the bucket. For more information, see `Step 2\\:
        Grant ElastiCache Access to Your Amazon S3 Bucket
        <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/backups-exporting.html#backups-exporting-grant-access>`__
        in the ElastiCache User Guide.

        * **Error Message:** ElastiCache has not been granted READ_ACP permissions %s on the S3 Bucket.
        **Solution:** Add View Permissions on the bucket. For more information, see `Step 2\\: Grant
        ElastiCache Access to Your Amazon S3 Bucket
        <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/backups-exporting.html#backups-exporting-grant-access>`__
        in the ElastiCache User Guide.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/CopySnapshot>`_

        **Request Syntax**
        ::

          response = client.copy_snapshot(
              SourceSnapshotName='string',
              TargetSnapshotName='string',
              TargetBucket='string',
              KmsKeyId='string'
          )
        :type SourceSnapshotName: string
        :param SourceSnapshotName: **[REQUIRED]**

          The name of an existing snapshot from which to make a copy.

        :type TargetSnapshotName: string
        :param TargetSnapshotName: **[REQUIRED]**

          A name for the snapshot copy. ElastiCache does not permit overwriting a snapshot, therefore this
          name must be unique within its context - ElastiCache or an Amazon S3 bucket if exporting.

        :type TargetBucket: string
        :param TargetBucket:

          The Amazon S3 bucket to which the snapshot is exported. This parameter is used only when
          exporting a snapshot for external access.

          When using this parameter to export a snapshot, be sure Amazon ElastiCache has the needed
          permissions to this S3 bucket. For more information, see `Step 2\\: Grant ElastiCache Access to
          Your Amazon S3 Bucket
          <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/backups-exporting.html#backups-exporting-grant-access>`__
          in the *Amazon ElastiCache User Guide* .

          For more information, see `Exporting a Snapshot
          <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Snapshots.Exporting.html>`__ in the
          *Amazon ElastiCache User Guide* .

        :type KmsKeyId: string
        :param KmsKeyId:

          The ID of the KMS key used to encrypt the target snapshot.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Snapshot': {
                    'SnapshotName': 'string',
                    'ReplicationGroupId': 'string',
                    'ReplicationGroupDescription': 'string',
                    'CacheClusterId': 'string',
                    'SnapshotStatus': 'string',
                    'SnapshotSource': 'string',
                    'CacheNodeType': 'string',
                    'Engine': 'string',
                    'EngineVersion': 'string',
                    'NumCacheNodes': 123,
                    'PreferredAvailabilityZone': 'string',
                    'CacheClusterCreateTime': datetime(2015, 1, 1),
                    'PreferredMaintenanceWindow': 'string',
                    'TopicArn': 'string',
                    'Port': 123,
                    'CacheParameterGroupName': 'string',
                    'CacheSubnetGroupName': 'string',
                    'VpcId': 'string',
                    'AutoMinorVersionUpgrade': True|False,
                    'SnapshotRetentionLimit': 123,
                    'SnapshotWindow': 'string',
                    'NumNodeGroups': 123,
                    'AutomaticFailover': 'enabled'|'disabled'|'enabling'|'disabling',
                    'NodeSnapshots': [
                        {
                            'CacheClusterId': 'string',
                            'NodeGroupId': 'string',
                            'CacheNodeId': 'string',
                            'NodeGroupConfiguration': {
                                'NodeGroupId': 'string',
                                'Slots': 'string',
                                'ReplicaCount': 123,
                                'PrimaryAvailabilityZone': 'string',
                                'ReplicaAvailabilityZones': [
                                    'string',
                                ]
                            },
                            'CacheSize': 'string',
                            'CacheNodeCreateTime': datetime(2015, 1, 1),
                            'SnapshotCreateTime': datetime(2015, 1, 1)
                        },
                    ],
                    'KmsKeyId': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **Snapshot** *(dict) --*

              Represents a copy of an entire Redis cluster as of the time when the snapshot was taken.

              - **SnapshotName** *(string) --*

                The name of a snapshot. For an automatic snapshot, the name is system-generated. For a
                manual snapshot, this is the user-provided name.

              - **ReplicationGroupId** *(string) --*

                The unique identifier of the source replication group.

              - **ReplicationGroupDescription** *(string) --*

                A description of the source replication group.

              - **CacheClusterId** *(string) --*

                The user-supplied identifier of the source cluster.

              - **SnapshotStatus** *(string) --*

                The status of the snapshot. Valid values: ``creating`` | ``available`` | ``restoring`` |
                ``copying`` | ``deleting`` .

              - **SnapshotSource** *(string) --*

                Indicates whether the snapshot is from an automatic backup (``automated`` ) or was created
                manually (``manual`` ).

              - **CacheNodeType** *(string) --*

                The name of the compute and memory capacity node type for the source cluster.

                The following node types are supported by ElastiCache. Generally speaking, the current
                generation types provide more memory and computational power at lower cost when compared to
                their equivalent previous generation counterparts.

                * General purpose:

                  * Current generation:   **M5 node types:**  ``cache.m5.large`` , ``cache.m5.xlarge`` ,
                  ``cache.m5.2xlarge`` , ``cache.m5.4xlarge`` , ``cache.m5.12xlarge`` ,
                  ``cache.m5.24xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` ,
                  ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``    **T2 node types:**
                   ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``

                  * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``    **M1
                  node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` ,
                  ``cache.m1.xlarge``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` ,
                  ``cache.m3.xlarge`` , ``cache.m3.2xlarge``

                * Compute optimized:

                  * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``

                * Memory optimized:

                  * Current generation:   **R5 node types:**  ``cache.r5.large`` , ``cache.r5.xlarge`` ,
                  ``cache.r5.2xlarge`` , ``cache.r5.4xlarge`` , ``cache.r5.12xlarge`` ,
                  ``cache.r5.24xlarge``    **R4 node types:**  ``cache.r4.large`` , ``cache.r4.xlarge`` ,
                  ``cache.r4.2xlarge`` , ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` , ``cache.r4.16xlarge``

                  * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` ,
                  ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``    **R3 node types:**  ``cache.r3.large`` ,
                  ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``

                 **Additional node type info**

                * All current generation instance types are created in Amazon VPC by default.

                * Redis append-only files (AOF) are not supported for T1 or T2 instances.

                * Redis Multi-AZ with automatic failover is not supported on T1 instances.

                * Redis configuration variables ``appendonly`` and ``appendfsync`` are not supported on
                Redis version 2.8.22 and later.

              - **Engine** *(string) --*

                The name of the cache engine (``memcached`` or ``redis`` ) used by the source cluster.

              - **EngineVersion** *(string) --*

                The version of the cache engine version that is used by the source cluster.

              - **NumCacheNodes** *(integer) --*

                The number of cache nodes in the source cluster.

                For clusters running Redis, this value must be 1. For clusters running Memcached, this
                value must be between 1 and 20.

              - **PreferredAvailabilityZone** *(string) --*

                The name of the Availability Zone in which the source cluster is located.

              - **CacheClusterCreateTime** *(datetime) --*

                The date and time when the source cluster was created.

              - **PreferredMaintenanceWindow** *(string) --*

                Specifies the weekly time range during which maintenance on the cluster is performed. It is
                specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum
                maintenance window is a 60 minute period.

                Valid values for ``ddd`` are:

                * ``sun``

                * ``mon``

                * ``tue``

                * ``wed``

                * ``thu``

                * ``fri``

                * ``sat``

                Example: ``sun:23:00-mon:01:30``

              - **TopicArn** *(string) --*

                The Amazon Resource Name (ARN) for the topic used by the source cluster for publishing
                notifications.

              - **Port** *(integer) --*

                The port number used by each cache nodes in the source cluster.

              - **CacheParameterGroupName** *(string) --*

                The cache parameter group that is associated with the source cluster.

              - **CacheSubnetGroupName** *(string) --*

                The name of the cache subnet group associated with the source cluster.

              - **VpcId** *(string) --*

                The Amazon Virtual Private Cloud identifier (VPC ID) of the cache subnet group for the
                source cluster.

              - **AutoMinorVersionUpgrade** *(boolean) --*

                This parameter is currently disabled.

              - **SnapshotRetentionLimit** *(integer) --*

                For an automatic snapshot, the number of days for which ElastiCache retains the snapshot
                before deleting it.

                For manual snapshots, this field reflects the ``SnapshotRetentionLimit`` for the source
                cluster when the snapshot was created. This field is otherwise ignored: Manual snapshots do
                not expire, and can only be deleted using the ``DeleteSnapshot`` operation.

                 **Important** If the value of SnapshotRetentionLimit is set to zero (0), backups are
                 turned off.

              - **SnapshotWindow** *(string) --*

                The daily time range during which ElastiCache takes daily snapshots of the source cluster.

              - **NumNodeGroups** *(integer) --*

                The number of node groups (shards) in this snapshot. When restoring from a snapshot, the
                number of node groups (shards) in the snapshot and in the restored replication group must
                be the same.

              - **AutomaticFailover** *(string) --*

                Indicates the status of Multi-AZ with automatic failover for the source Redis replication
                group.

                Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

                * Redis versions earlier than 2.8.6.

                * Redis (cluster mode disabled): T1 node types.

                * Redis (cluster mode enabled): T1 node types.

              - **NodeSnapshots** *(list) --*

                A list of the cache nodes in the source cluster.

                - *(dict) --*

                  Represents an individual cache node in a snapshot of a cluster.

                  - **CacheClusterId** *(string) --*

                    A unique identifier for the source cluster.

                  - **NodeGroupId** *(string) --*

                    A unique identifier for the source node group (shard).

                  - **CacheNodeId** *(string) --*

                    The cache node identifier for the node in the source cluster.

                  - **NodeGroupConfiguration** *(dict) --*

                    The configuration for the source node group (shard).

                    - **NodeGroupId** *(string) --*

                      Either the ElastiCache for Redis supplied 4-digit id or a user supplied id for the
                      node group these configuration values apply to.

                    - **Slots** *(string) --*

                      A string that specifies the keyspace for a particular node group. Keyspaces range
                      from 0 to 16,383. The string is in the format ``startkey-endkey`` .

                      Example: ``"0-3999"``

                    - **ReplicaCount** *(integer) --*

                      The number of read replica nodes in this node group (shard).

                    - **PrimaryAvailabilityZone** *(string) --*

                      The Availability Zone where the primary node of this node group (shard) is launched.

                    - **ReplicaAvailabilityZones** *(list) --*

                      A list of Availability Zones to be used for the read replicas. The number of
                      Availability Zones in this list must match the value of ``ReplicaCount`` or
                      ``ReplicasPerNodeGroup`` if not specified.

                      - *(string) --*

                  - **CacheSize** *(string) --*

                    The size of the cache on the source cache node.

                  - **CacheNodeCreateTime** *(datetime) --*

                    The date and time when the cache node was created in the source cluster.

                  - **SnapshotCreateTime** *(datetime) --*

                    The date and time when the source node's metadata and cache data set was obtained for
                    the snapshot.

              - **KmsKeyId** *(string) --*

                The ID of the KMS key used to encrypt the snapshot.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_cache_cluster(
        self,
        CacheClusterId: str,
        ReplicationGroupId: str = None,
        AZMode: str = None,
        PreferredAvailabilityZone: str = None,
        PreferredAvailabilityZones: List[str] = None,
        NumCacheNodes: int = None,
        CacheNodeType: str = None,
        Engine: str = None,
        EngineVersion: str = None,
        CacheParameterGroupName: str = None,
        CacheSubnetGroupName: str = None,
        CacheSecurityGroupNames: List[str] = None,
        SecurityGroupIds: List[str] = None,
        Tags: List[ClientCreateCacheClusterTagsTypeDef] = None,
        SnapshotArns: List[str] = None,
        SnapshotName: str = None,
        PreferredMaintenanceWindow: str = None,
        Port: int = None,
        NotificationTopicArn: str = None,
        AutoMinorVersionUpgrade: bool = None,
        SnapshotRetentionLimit: int = None,
        SnapshotWindow: str = None,
        AuthToken: str = None,
    ) -> ClientCreateCacheClusterResponseTypeDef:
        """
        Creates a cluster. All nodes in the cluster run the same protocol-compliant cache engine software,
        either Memcached or Redis.

        This operation is not supported for Redis (cluster mode enabled) clusters.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/CreateCacheCluster>`_

        **Request Syntax**
        ::

          response = client.create_cache_cluster(
              CacheClusterId='string',
              ReplicationGroupId='string',
              AZMode='single-az'|'cross-az',
              PreferredAvailabilityZone='string',
              PreferredAvailabilityZones=[
                  'string',
              ],
              NumCacheNodes=123,
              CacheNodeType='string',
              Engine='string',
              EngineVersion='string',
              CacheParameterGroupName='string',
              CacheSubnetGroupName='string',
              CacheSecurityGroupNames=[
                  'string',
              ],
              SecurityGroupIds=[
                  'string',
              ],
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ],
              SnapshotArns=[
                  'string',
              ],
              SnapshotName='string',
              PreferredMaintenanceWindow='string',
              Port=123,
              NotificationTopicArn='string',
              AutoMinorVersionUpgrade=True|False,
              SnapshotRetentionLimit=123,
              SnapshotWindow='string',
              AuthToken='string'
          )
        :type CacheClusterId: string
        :param CacheClusterId: **[REQUIRED]**

          The node group (shard) identifier. This parameter is stored as a lowercase string.

           **Constraints:**

          * A name must contain from 1 to 50 alphanumeric characters or hyphens.

          * The first character must be a letter.

          * A name cannot end with a hyphen or contain two consecutive hyphens.

        :type ReplicationGroupId: string
        :param ReplicationGroupId:

          The ID of the replication group to which this cluster should belong. If this parameter is
          specified, the cluster is added to the specified replication group as a read replica; otherwise,
          the cluster is a standalone primary that is not part of any replication group.

          If the specified replication group is Multi-AZ enabled and the Availability Zone is not
          specified, the cluster is created in Availability Zones that provide the best spread of read
          replicas across Availability Zones.

          .. note::

            This parameter is only valid if the ``Engine`` parameter is ``redis`` .

        :type AZMode: string
        :param AZMode:

          Specifies whether the nodes in this Memcached cluster are created in a single Availability Zone
          or created across multiple Availability Zones in the cluster's region.

          This parameter is only supported for Memcached clusters.

          If the ``AZMode`` and ``PreferredAvailabilityZones`` are not specified, ElastiCache assumes
          ``single-az`` mode.

        :type PreferredAvailabilityZone: string
        :param PreferredAvailabilityZone:

          The EC2 Availability Zone in which the cluster is created.

          All nodes belonging to this Memcached cluster are placed in the preferred Availability Zone. If
          you want to create your nodes across multiple Availability Zones, use
          ``PreferredAvailabilityZones`` .

          Default: System chosen Availability Zone.

        :type PreferredAvailabilityZones: list
        :param PreferredAvailabilityZones:

          A list of the Availability Zones in which cache nodes are created. The order of the zones in the
          list is not important.

          This option is only supported on Memcached.

          .. note::

            If you are creating your cluster in an Amazon VPC (recommended) you can only locate nodes in
            Availability Zones that are associated with the subnets in the selected subnet group.

            The number of Availability Zones listed must equal the value of ``NumCacheNodes`` .

          If you want all the nodes in the same Availability Zone, use ``PreferredAvailabilityZone``
          instead, or repeat the Availability Zone multiple times in the list.

          Default: System chosen Availability Zones.

          - *(string) --*

        :type NumCacheNodes: integer
        :param NumCacheNodes:

          The initial number of cache nodes that the cluster has.

          For clusters running Redis, this value must be 1. For clusters running Memcached, this value must
          be between 1 and 20.

          If you need more than 20 nodes for your Memcached cluster, please fill out the ElastiCache Limit
          Increase Request form at `http\\://aws.amazon.com/contact-us/elasticache-node-limit-request/
          <http://aws.amazon.com/contact-us/elasticache-node-limit-request/>`__ .

        :type CacheNodeType: string
        :param CacheNodeType:

          The compute and memory capacity of the nodes in the node group (shard).

          The following node types are supported by ElastiCache. Generally speaking, the current generation
          types provide more memory and computational power at lower cost when compared to their equivalent
          previous generation counterparts.

          * General purpose:

            * Current generation:   **M5 node types:**  ``cache.m5.large`` , ``cache.m5.xlarge`` ,
            ``cache.m5.2xlarge`` , ``cache.m5.4xlarge`` , ``cache.m5.12xlarge`` , ``cache.m5.24xlarge``
            **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` , ``cache.m4.2xlarge`` ,
            ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``    **T2 node types:**  ``cache.t2.micro`` ,
            ``cache.t2.small`` , ``cache.t2.medium``

            * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``    **M1 node
            types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` , ``cache.m1.xlarge``
             **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` , ``cache.m3.xlarge`` ,
             ``cache.m3.2xlarge``

          * Compute optimized:

            * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``

          * Memory optimized:

            * Current generation:   **R5 node types:**  ``cache.r5.large`` , ``cache.r5.xlarge`` ,
            ``cache.r5.2xlarge`` , ``cache.r5.4xlarge`` , ``cache.r5.12xlarge`` , ``cache.r5.24xlarge``
            **R4 node types:**  ``cache.r4.large`` , ``cache.r4.xlarge`` , ``cache.r4.2xlarge`` ,
            ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` , ``cache.r4.16xlarge``

            * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` ,
            ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``    **R3 node types:**  ``cache.r3.large`` ,
            ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``

           **Additional node type info**

          * All current generation instance types are created in Amazon VPC by default.

          * Redis append-only files (AOF) are not supported for T1 or T2 instances.

          * Redis Multi-AZ with automatic failover is not supported on T1 instances.

          * Redis configuration variables ``appendonly`` and ``appendfsync`` are not supported on Redis
          version 2.8.22 and later.

        :type Engine: string
        :param Engine:

          The name of the cache engine to be used for this cluster.

          Valid values for this parameter are: ``memcached`` | ``redis``

        :type EngineVersion: string
        :param EngineVersion:

          The version number of the cache engine to be used for this cluster. To view the supported cache
          engine versions, use the DescribeCacheEngineVersions operation.

           **Important:** You can upgrade to a newer engine version (see `Selecting a Cache Engine and
           Version
           <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/SelectEngine.html#VersionManagement>`__
           ), but you cannot downgrade to an earlier engine version. If you want to use an earlier engine
           version, you must delete the existing cluster or replication group and create it anew with the
           earlier engine version.

        :type CacheParameterGroupName: string
        :param CacheParameterGroupName:

          The name of the parameter group to associate with this cluster. If this argument is omitted, the
          default parameter group for the specified engine is used. You cannot use any parameter group
          which has ``cluster-enabled='yes'`` when creating a cluster.

        :type CacheSubnetGroupName: string
        :param CacheSubnetGroupName:

          The name of the subnet group to be used for the cluster.

          Use this parameter only when you are creating a cluster in an Amazon Virtual Private Cloud
          (Amazon VPC).

          .. warning::

            If you're going to launch your cluster in an Amazon VPC, you need to create a subnet group
            before you start creating a cluster. For more information, see `Subnets and Subnet Groups
            <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/SubnetGroups.html>`__ .

        :type CacheSecurityGroupNames: list
        :param CacheSecurityGroupNames:

          A list of security group names to associate with this cluster.

          Use this parameter only when you are creating a cluster outside of an Amazon Virtual Private
          Cloud (Amazon VPC).

          - *(string) --*

        :type SecurityGroupIds: list
        :param SecurityGroupIds:

          One or more VPC security groups associated with the cluster.

          Use this parameter only when you are creating a cluster in an Amazon Virtual Private Cloud
          (Amazon VPC).

          - *(string) --*

        :type Tags: list
        :param Tags:

          A list of cost allocation tags to be added to this resource.

          - *(dict) --*

            A cost allocation Tag that can be added to an ElastiCache cluster or replication group. Tags
            are composed of a Key/Value pair. A tag with a null Value is permitted.

            - **Key** *(string) --*

              The key for the tag. May not be null.

            - **Value** *(string) --*

              The tag's value. May be null.

        :type SnapshotArns: list
        :param SnapshotArns:

          A single-element string list containing an Amazon Resource Name (ARN) that uniquely identifies a
          Redis RDB snapshot file stored in Amazon S3. The snapshot file is used to populate the node group
          (shard). The Amazon S3 object name in the ARN cannot contain any commas.

          .. note::

            This parameter is only valid if the ``Engine`` parameter is ``redis`` .

          Example of an Amazon S3 ARN: ``arn:aws:s3:::my_bucket/snapshot1.rdb``

          - *(string) --*

        :type SnapshotName: string
        :param SnapshotName:

          The name of a Redis snapshot from which to restore data into the new node group (shard). The
          snapshot status changes to ``restoring`` while the new node group (shard) is being created.

          .. note::

            This parameter is only valid if the ``Engine`` parameter is ``redis`` .

        :type PreferredMaintenanceWindow: string
        :param PreferredMaintenanceWindow:

          Specifies the weekly time range during which maintenance on the cluster is performed. It is
          specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum
          maintenance window is a 60 minute period. Valid values for ``ddd`` are:

          Specifies the weekly time range during which maintenance on the cluster is performed. It is
          specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum
          maintenance window is a 60 minute period.

          Valid values for ``ddd`` are:

          * ``sun``

          * ``mon``

          * ``tue``

          * ``wed``

          * ``thu``

          * ``fri``

          * ``sat``

          Example: ``sun:23:00-mon:01:30``

        :type Port: integer
        :param Port:

          The port number on which each of the cache nodes accepts connections.

        :type NotificationTopicArn: string
        :param NotificationTopicArn:

          The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) topic to which
          notifications are sent.

          .. note::

            The Amazon SNS topic owner must be the same as the cluster owner.

        :type AutoMinorVersionUpgrade: boolean
        :param AutoMinorVersionUpgrade:

          This parameter is currently disabled.

        :type SnapshotRetentionLimit: integer
        :param SnapshotRetentionLimit:

          The number of days for which ElastiCache retains automatic snapshots before deleting them. For
          example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot taken today is retained for 5
          days before being deleted.

          .. note::

            This parameter is only valid if the ``Engine`` parameter is ``redis`` .

          Default: 0 (i.e., automatic backups are disabled for this cache cluster).

        :type SnapshotWindow: string
        :param SnapshotWindow:

          The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your
          node group (shard).

          Example: ``05:00-09:00``

          If you do not specify this parameter, ElastiCache automatically chooses an appropriate time range.

          .. note::

            This parameter is only valid if the ``Engine`` parameter is ``redis`` .

        :type AuthToken: string
        :param AuthToken:

           **Reserved parameter.** The password used to access a password protected server.

          Password constraints:

          * Must be only printable ASCII characters.

          * Must be at least 16 characters and no more than 128 characters in length.

          * The only permitted printable special characters are !, &, #, $, ^, <, >, and -. Other printable
          special characters cannot be used in the AUTH token.

          For more information, see `AUTH password <http://redis.io/commands/AUTH>`__ at
          http://redis.io/commands/AUTH.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'CacheCluster': {
                    'CacheClusterId': 'string',
                    'ConfigurationEndpoint': {
                        'Address': 'string',
                        'Port': 123
                    },
                    'ClientDownloadLandingPage': 'string',
                    'CacheNodeType': 'string',
                    'Engine': 'string',
                    'EngineVersion': 'string',
                    'CacheClusterStatus': 'string',
                    'NumCacheNodes': 123,
                    'PreferredAvailabilityZone': 'string',
                    'CacheClusterCreateTime': datetime(2015, 1, 1),
                    'PreferredMaintenanceWindow': 'string',
                    'PendingModifiedValues': {
                        'NumCacheNodes': 123,
                        'CacheNodeIdsToRemove': [
                            'string',
                        ],
                        'EngineVersion': 'string',
                        'CacheNodeType': 'string',
                        'AuthTokenStatus': 'SETTING'|'ROTATING'
                    },
                    'NotificationConfiguration': {
                        'TopicArn': 'string',
                        'TopicStatus': 'string'
                    },
                    'CacheSecurityGroups': [
                        {
                            'CacheSecurityGroupName': 'string',
                            'Status': 'string'
                        },
                    ],
                    'CacheParameterGroup': {
                        'CacheParameterGroupName': 'string',
                        'ParameterApplyStatus': 'string',
                        'CacheNodeIdsToReboot': [
                            'string',
                        ]
                    },
                    'CacheSubnetGroupName': 'string',
                    'CacheNodes': [
                        {
                            'CacheNodeId': 'string',
                            'CacheNodeStatus': 'string',
                            'CacheNodeCreateTime': datetime(2015, 1, 1),
                            'Endpoint': {
                                'Address': 'string',
                                'Port': 123
                            },
                            'ParameterGroupStatus': 'string',
                            'SourceCacheNodeId': 'string',
                            'CustomerAvailabilityZone': 'string'
                        },
                    ],
                    'AutoMinorVersionUpgrade': True|False,
                    'SecurityGroups': [
                        {
                            'SecurityGroupId': 'string',
                            'Status': 'string'
                        },
                    ],
                    'ReplicationGroupId': 'string',
                    'SnapshotRetentionLimit': 123,
                    'SnapshotWindow': 'string',
                    'AuthTokenEnabled': True|False,
                    'AuthTokenLastModifiedDate': datetime(2015, 1, 1),
                    'TransitEncryptionEnabled': True|False,
                    'AtRestEncryptionEnabled': True|False
                }
            }
          **Response Structure**

          - *(dict) --*

            - **CacheCluster** *(dict) --*

              Contains all of the attributes of a specific cluster.

              - **CacheClusterId** *(string) --*

                The user-supplied identifier of the cluster. This identifier is a unique key that
                identifies a cluster.

              - **ConfigurationEndpoint** *(dict) --*

                Represents a Memcached cluster endpoint which, if Automatic Discovery is enabled on the
                cluster, can be used by an application to connect to any node in the cluster. The
                configuration endpoint will always have ``.cfg`` in it.

                Example: ``mem-3.9dvc4r.cfg.usw2.cache.amazonaws.com:11211``

                - **Address** *(string) --*

                  The DNS hostname of the cache node.

                - **Port** *(integer) --*

                  The port number that the cache engine is listening on.

              - **ClientDownloadLandingPage** *(string) --*

                The URL of the web page where you can download the latest ElastiCache client library.

              - **CacheNodeType** *(string) --*

                The name of the compute and memory capacity node type for the cluster.

                The following node types are supported by ElastiCache. Generally speaking, the current
                generation types provide more memory and computational power at lower cost when compared to
                their equivalent previous generation counterparts.

                * General purpose:

                  * Current generation:   **M5 node types:**  ``cache.m5.large`` , ``cache.m5.xlarge`` ,
                  ``cache.m5.2xlarge`` , ``cache.m5.4xlarge`` , ``cache.m5.12xlarge`` ,
                  ``cache.m5.24xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` ,
                  ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``    **T2 node types:**
                   ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``

                  * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``    **M1
                  node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` ,
                  ``cache.m1.xlarge``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` ,
                  ``cache.m3.xlarge`` , ``cache.m3.2xlarge``

                * Compute optimized:

                  * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``

                * Memory optimized:

                  * Current generation:   **R5 node types:**  ``cache.r5.large`` , ``cache.r5.xlarge`` ,
                  ``cache.r5.2xlarge`` , ``cache.r5.4xlarge`` , ``cache.r5.12xlarge`` ,
                  ``cache.r5.24xlarge``    **R4 node types:**  ``cache.r4.large`` , ``cache.r4.xlarge`` ,
                  ``cache.r4.2xlarge`` , ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` , ``cache.r4.16xlarge``

                  * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` ,
                  ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``    **R3 node types:**  ``cache.r3.large`` ,
                  ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``

                 **Additional node type info**

                * All current generation instance types are created in Amazon VPC by default.

                * Redis append-only files (AOF) are not supported for T1 or T2 instances.

                * Redis Multi-AZ with automatic failover is not supported on T1 instances.

                * Redis configuration variables ``appendonly`` and ``appendfsync`` are not supported on
                Redis version 2.8.22 and later.

              - **Engine** *(string) --*

                The name of the cache engine (``memcached`` or ``redis`` ) to be used for this cluster.

              - **EngineVersion** *(string) --*

                The version of the cache engine that is used in this cluster.

              - **CacheClusterStatus** *(string) --*

                The current state of this cluster, one of the following values: ``available`` ,
                ``creating`` , ``deleted`` , ``deleting`` , ``incompatible-network`` , ``modifying`` ,
                ``rebooting cluster nodes`` , ``restore-failed`` , or ``snapshotting`` .

              - **NumCacheNodes** *(integer) --*

                The number of cache nodes in the cluster.

                For clusters running Redis, this value must be 1. For clusters running Memcached, this
                value must be between 1 and 20.

              - **PreferredAvailabilityZone** *(string) --*

                The name of the Availability Zone in which the cluster is located or "Multiple" if the
                cache nodes are located in different Availability Zones.

              - **CacheClusterCreateTime** *(datetime) --*

                The date and time when the cluster was created.

              - **PreferredMaintenanceWindow** *(string) --*

                Specifies the weekly time range during which maintenance on the cluster is performed. It is
                specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum
                maintenance window is a 60 minute period.

                Valid values for ``ddd`` are:

                * ``sun``

                * ``mon``

                * ``tue``

                * ``wed``

                * ``thu``

                * ``fri``

                * ``sat``

                Example: ``sun:23:00-mon:01:30``

              - **PendingModifiedValues** *(dict) --*

                A group of settings that are applied to the cluster in the future, or that are currently
                being applied.

                - **NumCacheNodes** *(integer) --*

                  The new number of cache nodes for the cluster.

                  For clusters running Redis, this value must be 1. For clusters running Memcached, this
                  value must be between 1 and 20.

                - **CacheNodeIdsToRemove** *(list) --*

                  A list of cache node IDs that are being removed (or will be removed) from the cluster. A
                  node ID is a 4-digit numeric identifier (0001, 0002, etc.).

                  - *(string) --*

                - **EngineVersion** *(string) --*

                  The new cache engine version that the cluster runs.

                - **CacheNodeType** *(string) --*

                  The cache node type that this cluster or replication group is scaled to.

                - **AuthTokenStatus** *(string) --*

                  The auth token status

              - **NotificationConfiguration** *(dict) --*

                Describes a notification topic and its status. Notification topics are used for publishing
                ElastiCache events to subscribers using Amazon Simple Notification Service (SNS).

                - **TopicArn** *(string) --*

                  The Amazon Resource Name (ARN) that identifies the topic.

                - **TopicStatus** *(string) --*

                  The current state of the topic.

              - **CacheSecurityGroups** *(list) --*

                A list of cache security group elements, composed of name and status sub-elements.

                - *(dict) --*

                  Represents a cluster's status within a particular cache security group.

                  - **CacheSecurityGroupName** *(string) --*

                    The name of the cache security group.

                  - **Status** *(string) --*

                    The membership status in the cache security group. The status changes when a cache
                    security group is modified, or when the cache security groups assigned to a cluster are
                    modified.

              - **CacheParameterGroup** *(dict) --*

                Status of the cache parameter group.

                - **CacheParameterGroupName** *(string) --*

                  The name of the cache parameter group.

                - **ParameterApplyStatus** *(string) --*

                  The status of parameter updates.

                - **CacheNodeIdsToReboot** *(list) --*

                  A list of the cache node IDs which need to be rebooted for parameter changes to be
                  applied. A node ID is a numeric identifier (0001, 0002, etc.).

                  - *(string) --*

              - **CacheSubnetGroupName** *(string) --*

                The name of the cache subnet group associated with the cluster.

              - **CacheNodes** *(list) --*

                A list of cache nodes that are members of the cluster.

                - *(dict) --*

                  Represents an individual cache node within a cluster. Each cache node runs its own
                  instance of the cluster's protocol-compliant caching software - either Memcached or Redis.

                  The following node types are supported by ElastiCache. Generally speaking, the current
                  generation types provide more memory and computational power at lower cost when compared
                  to their equivalent previous generation counterparts.

                  * General purpose:

                    * Current generation:   **M5 node types:**  ``cache.m5.large`` , ``cache.m5.xlarge`` ,
                    ``cache.m5.2xlarge`` , ``cache.m5.4xlarge`` , ``cache.m5.12xlarge`` ,
                    ``cache.m5.24xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` ,
                    ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``    **T2 node
                    types:**  ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``

                    * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``
                    **M1 node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` ,
                    ``cache.m1.xlarge``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` ,
                    ``cache.m3.xlarge`` , ``cache.m3.2xlarge``

                  * Compute optimized:

                    * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``

                  * Memory optimized:

                    * Current generation:   **R5 node types:**  ``cache.r5.large`` , ``cache.r5.xlarge`` ,
                    ``cache.r5.2xlarge`` , ``cache.r5.4xlarge`` , ``cache.r5.12xlarge`` ,
                    ``cache.r5.24xlarge``    **R4 node types:**  ``cache.r4.large`` , ``cache.r4.xlarge`` ,
                    ``cache.r4.2xlarge`` , ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` ,
                    ``cache.r4.16xlarge``

                    * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` ,
                    ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``    **R3 node types:**  ``cache.r3.large`` ,
                    ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``

                   **Additional node type info**

                  * All current generation instance types are created in Amazon VPC by default.

                  * Redis append-only files (AOF) are not supported for T1 or T2 instances.

                  * Redis Multi-AZ with automatic failover is not supported on T1 instances.

                  * Redis configuration variables ``appendonly`` and ``appendfsync`` are not supported on
                  Redis version 2.8.22 and later.

                  - **CacheNodeId** *(string) --*

                    The cache node identifier. A node ID is a numeric identifier (0001, 0002, etc.). The
                    combination of cluster ID and node ID uniquely identifies every cache node used in a
                    customer's AWS account.

                  - **CacheNodeStatus** *(string) --*

                    The current state of this cache node.

                  - **CacheNodeCreateTime** *(datetime) --*

                    The date and time when the cache node was created.

                  - **Endpoint** *(dict) --*

                    The hostname for connecting to this cache node.

                    - **Address** *(string) --*

                      The DNS hostname of the cache node.

                    - **Port** *(integer) --*

                      The port number that the cache engine is listening on.

                  - **ParameterGroupStatus** *(string) --*

                    The status of the parameter group applied to this cache node.

                  - **SourceCacheNodeId** *(string) --*

                    The ID of the primary node to which this read replica node is synchronized. If this
                    field is empty, this node is not associated with a primary cluster.

                  - **CustomerAvailabilityZone** *(string) --*

                    The Availability Zone where this node was created and now resides.

              - **AutoMinorVersionUpgrade** *(boolean) --*

                This parameter is currently disabled.

              - **SecurityGroups** *(list) --*

                A list of VPC Security Groups associated with the cluster.

                - *(dict) --*

                  Represents a single cache security group and its status.

                  - **SecurityGroupId** *(string) --*

                    The identifier of the cache security group.

                  - **Status** *(string) --*

                    The status of the cache security group membership. The status changes whenever a cache
                    security group is modified, or when the cache security groups assigned to a cluster are
                    modified.

              - **ReplicationGroupId** *(string) --*

                The replication group to which this cluster belongs. If this field is empty, the cluster is
                not associated with any replication group.

              - **SnapshotRetentionLimit** *(integer) --*

                The number of days for which ElastiCache retains automatic cluster snapshots before
                deleting them. For example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot that was
                taken today is retained for 5 days before being deleted.

                .. warning::

                  If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.

              - **SnapshotWindow** *(string) --*

                The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of
                your cluster.

                Example: ``05:00-09:00``

              - **AuthTokenEnabled** *(boolean) --*

                A flag that enables using an ``AuthToken`` (password) when issuing Redis commands.

                Default: ``false``

              - **AuthTokenLastModifiedDate** *(datetime) --*

                The date the auth token was last modified

              - **TransitEncryptionEnabled** *(boolean) --*

                A flag that enables in-transit encryption when set to ``true`` .

                You cannot modify the value of ``TransitEncryptionEnabled`` after the cluster is created.
                To enable in-transit encryption on a cluster you must set ``TransitEncryptionEnabled`` to
                ``true`` when you create a cluster.

                 **Required:** Only available when creating a replication group in an Amazon VPC using
                 redis version ``3.2.6`` , ``4.x`` or later.

                Default: ``false``

              - **AtRestEncryptionEnabled** *(boolean) --*

                A flag that enables encryption at-rest when set to ``true`` .

                You cannot modify the value of ``AtRestEncryptionEnabled`` after the cluster is created. To
                enable at-rest encryption on a cluster you must set ``AtRestEncryptionEnabled`` to ``true``
                when you create a cluster.

                 **Required:** Only available when creating a replication group in an Amazon VPC using
                 redis version ``3.2.6`` , ``4.x`` or later.

                Default: ``false``

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_cache_parameter_group(
        self,
        CacheParameterGroupName: str,
        CacheParameterGroupFamily: str,
        Description: str,
    ) -> ClientCreateCacheParameterGroupResponseTypeDef:
        """
        Creates a new Amazon ElastiCache cache parameter group. An ElastiCache cache parameter group is a
        collection of parameters and their values that are applied to all of the nodes in any cluster or
        replication group using the CacheParameterGroup.

        A newly created CacheParameterGroup is an exact duplicate of the default parameter group for the
        CacheParameterGroupFamily. To customize the newly created CacheParameterGroup you can change the
        values of specific parameters. For more information, see:

        * `ModifyCacheParameterGroup
        <https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_ModifyCacheParameterGroup.html>`__
        in the ElastiCache API Reference.

        * `Parameters and Parameter Groups
        <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/ParameterGroups.html>`__ in the
        ElastiCache User Guide.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/CreateCacheParameterGroup>`_

        **Request Syntax**
        ::

          response = client.create_cache_parameter_group(
              CacheParameterGroupName='string',
              CacheParameterGroupFamily='string',
              Description='string'
          )
        :type CacheParameterGroupName: string
        :param CacheParameterGroupName: **[REQUIRED]**

          A user-specified name for the cache parameter group.

        :type CacheParameterGroupFamily: string
        :param CacheParameterGroupFamily: **[REQUIRED]**

          The name of the cache parameter group family that the cache parameter group can be used with.

          Valid values are: ``memcached1.4`` | ``memcached1.5`` | ``redis2.6`` | ``redis2.8`` |
          ``redis3.2`` | ``redis4.0`` | ``redis5.0`` |

        :type Description: string
        :param Description: **[REQUIRED]**

          A user-specified description for the cache parameter group.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'CacheParameterGroup': {
                    'CacheParameterGroupName': 'string',
                    'CacheParameterGroupFamily': 'string',
                    'Description': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **CacheParameterGroup** *(dict) --*

              Represents the output of a ``CreateCacheParameterGroup`` operation.

              - **CacheParameterGroupName** *(string) --*

                The name of the cache parameter group.

              - **CacheParameterGroupFamily** *(string) --*

                The name of the cache parameter group family that this cache parameter group is compatible
                with.

                Valid values are: ``memcached1.4`` | ``memcached1.5`` | ``redis2.6`` | ``redis2.8`` |
                ``redis3.2`` | ``redis4.0`` | ``redis5.0`` |

              - **Description** *(string) --*

                The description for this cache parameter group.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_cache_security_group(
        self, CacheSecurityGroupName: str, Description: str
    ) -> ClientCreateCacheSecurityGroupResponseTypeDef:
        """
        Creates a new cache security group. Use a cache security group to control access to one or more
        clusters.

        Cache security groups are only used when you are creating a cluster outside of an Amazon Virtual
        Private Cloud (Amazon VPC). If you are creating a cluster inside of a VPC, use a cache subnet group
        instead. For more information, see `CreateCacheSubnetGroup
        <https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_CreateCacheSubnetGroup.html>`__
        .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/CreateCacheSecurityGroup>`_

        **Request Syntax**
        ::

          response = client.create_cache_security_group(
              CacheSecurityGroupName='string',
              Description='string'
          )
        :type CacheSecurityGroupName: string
        :param CacheSecurityGroupName: **[REQUIRED]**

          A name for the cache security group. This value is stored as a lowercase string.

          Constraints: Must contain no more than 255 alphanumeric characters. Cannot be the word "Default".

          Example: ``mysecuritygroup``

        :type Description: string
        :param Description: **[REQUIRED]**

          A description for the cache security group.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'CacheSecurityGroup': {
                    'OwnerId': 'string',
                    'CacheSecurityGroupName': 'string',
                    'Description': 'string',
                    'EC2SecurityGroups': [
                        {
                            'Status': 'string',
                            'EC2SecurityGroupName': 'string',
                            'EC2SecurityGroupOwnerId': 'string'
                        },
                    ]
                }
            }
          **Response Structure**

          - *(dict) --*

            - **CacheSecurityGroup** *(dict) --*

              Represents the output of one of the following operations:

              * ``AuthorizeCacheSecurityGroupIngress``

              * ``CreateCacheSecurityGroup``

              * ``RevokeCacheSecurityGroupIngress``

              - **OwnerId** *(string) --*

                The AWS account ID of the cache security group owner.

              - **CacheSecurityGroupName** *(string) --*

                The name of the cache security group.

              - **Description** *(string) --*

                The description of the cache security group.

              - **EC2SecurityGroups** *(list) --*

                A list of Amazon EC2 security groups that are associated with this cache security group.

                - *(dict) --*

                  Provides ownership and status information for an Amazon EC2 security group.

                  - **Status** *(string) --*

                    The status of the Amazon EC2 security group.

                  - **EC2SecurityGroupName** *(string) --*

                    The name of the Amazon EC2 security group.

                  - **EC2SecurityGroupOwnerId** *(string) --*

                    The AWS account ID of the Amazon EC2 security group owner.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_cache_subnet_group(
        self,
        CacheSubnetGroupName: str,
        CacheSubnetGroupDescription: str,
        SubnetIds: List[str],
    ) -> ClientCreateCacheSubnetGroupResponseTypeDef:
        """
        Creates a new cache subnet group.

        Use this parameter only when you are creating a cluster in an Amazon Virtual Private Cloud (Amazon
        VPC).

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/CreateCacheSubnetGroup>`_

        **Request Syntax**
        ::

          response = client.create_cache_subnet_group(
              CacheSubnetGroupName='string',
              CacheSubnetGroupDescription='string',
              SubnetIds=[
                  'string',
              ]
          )
        :type CacheSubnetGroupName: string
        :param CacheSubnetGroupName: **[REQUIRED]**

          A name for the cache subnet group. This value is stored as a lowercase string.

          Constraints: Must contain no more than 255 alphanumeric characters or hyphens.

          Example: ``mysubnetgroup``

        :type CacheSubnetGroupDescription: string
        :param CacheSubnetGroupDescription: **[REQUIRED]**

          A description for the cache subnet group.

        :type SubnetIds: list
        :param SubnetIds: **[REQUIRED]**

          A list of VPC subnet IDs for the cache subnet group.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'CacheSubnetGroup': {
                    'CacheSubnetGroupName': 'string',
                    'CacheSubnetGroupDescription': 'string',
                    'VpcId': 'string',
                    'Subnets': [
                        {
                            'SubnetIdentifier': 'string',
                            'SubnetAvailabilityZone': {
                                'Name': 'string'
                            }
                        },
                    ]
                }
            }
          **Response Structure**

          - *(dict) --*

            - **CacheSubnetGroup** *(dict) --*

              Represents the output of one of the following operations:

              * ``CreateCacheSubnetGroup``

              * ``ModifyCacheSubnetGroup``

              - **CacheSubnetGroupName** *(string) --*

                The name of the cache subnet group.

              - **CacheSubnetGroupDescription** *(string) --*

                The description of the cache subnet group.

              - **VpcId** *(string) --*

                The Amazon Virtual Private Cloud identifier (VPC ID) of the cache subnet group.

              - **Subnets** *(list) --*

                A list of subnets associated with the cache subnet group.

                - *(dict) --*

                  Represents the subnet associated with a cluster. This parameter refers to subnets defined
                  in Amazon Virtual Private Cloud (Amazon VPC) and used with ElastiCache.

                  - **SubnetIdentifier** *(string) --*

                    The unique identifier for the subnet.

                  - **SubnetAvailabilityZone** *(dict) --*

                    The Availability Zone associated with the subnet.

                    - **Name** *(string) --*

                      The name of the Availability Zone.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_replication_group(
        self,
        ReplicationGroupId: str,
        ReplicationGroupDescription: str,
        PrimaryClusterId: str = None,
        AutomaticFailoverEnabled: bool = None,
        NumCacheClusters: int = None,
        PreferredCacheClusterAZs: List[str] = None,
        NumNodeGroups: int = None,
        ReplicasPerNodeGroup: int = None,
        NodeGroupConfiguration: List[
            ClientCreateReplicationGroupNodeGroupConfigurationTypeDef
        ] = None,
        CacheNodeType: str = None,
        Engine: str = None,
        EngineVersion: str = None,
        CacheParameterGroupName: str = None,
        CacheSubnetGroupName: str = None,
        CacheSecurityGroupNames: List[str] = None,
        SecurityGroupIds: List[str] = None,
        Tags: List[ClientCreateReplicationGroupTagsTypeDef] = None,
        SnapshotArns: List[str] = None,
        SnapshotName: str = None,
        PreferredMaintenanceWindow: str = None,
        Port: int = None,
        NotificationTopicArn: str = None,
        AutoMinorVersionUpgrade: bool = None,
        SnapshotRetentionLimit: int = None,
        SnapshotWindow: str = None,
        AuthToken: str = None,
        TransitEncryptionEnabled: bool = None,
        AtRestEncryptionEnabled: bool = None,
        KmsKeyId: str = None,
    ) -> ClientCreateReplicationGroupResponseTypeDef:
        """
        Creates a Redis (cluster mode disabled) or a Redis (cluster mode enabled) replication group.

        A Redis (cluster mode disabled) replication group is a collection of clusters, where one of the
        clusters is a read/write primary and the others are read-only replicas. Writes to the primary are
        asynchronously propagated to the replicas.

        A Redis (cluster mode enabled) replication group is a collection of 1 to 90 node groups (shards).
        Each node group (shard) has one read/write primary node and up to 5 read-only replica nodes. Writes
        to the primary are asynchronously propagated to the replicas. Redis (cluster mode enabled)
        replication groups partition the data across node groups (shards).

        When a Redis (cluster mode disabled) replication group has been successfully created, you can add
        one or more read replicas to it, up to a total of 5 read replicas. You cannot alter a Redis
        (cluster mode enabled) replication group after it has been created. However, if you need to
        increase or decrease the number of node groups (console: shards), you can avail yourself of
        ElastiCache for Redis' enhanced backup and restore. For more information, see `Restoring From a
        Backup with Cluster Resizing
        <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/backups-restoring.html>`__ in the
        *ElastiCache User Guide* .

        .. note::

          This operation is valid for Redis only.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/CreateReplicationGroup>`_

        **Request Syntax**
        ::

          response = client.create_replication_group(
              ReplicationGroupId='string',
              ReplicationGroupDescription='string',
              PrimaryClusterId='string',
              AutomaticFailoverEnabled=True|False,
              NumCacheClusters=123,
              PreferredCacheClusterAZs=[
                  'string',
              ],
              NumNodeGroups=123,
              ReplicasPerNodeGroup=123,
              NodeGroupConfiguration=[
                  {
                      'NodeGroupId': 'string',
                      'Slots': 'string',
                      'ReplicaCount': 123,
                      'PrimaryAvailabilityZone': 'string',
                      'ReplicaAvailabilityZones': [
                          'string',
                      ]
                  },
              ],
              CacheNodeType='string',
              Engine='string',
              EngineVersion='string',
              CacheParameterGroupName='string',
              CacheSubnetGroupName='string',
              CacheSecurityGroupNames=[
                  'string',
              ],
              SecurityGroupIds=[
                  'string',
              ],
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ],
              SnapshotArns=[
                  'string',
              ],
              SnapshotName='string',
              PreferredMaintenanceWindow='string',
              Port=123,
              NotificationTopicArn='string',
              AutoMinorVersionUpgrade=True|False,
              SnapshotRetentionLimit=123,
              SnapshotWindow='string',
              AuthToken='string',
              TransitEncryptionEnabled=True|False,
              AtRestEncryptionEnabled=True|False,
              KmsKeyId='string'
          )
        :type ReplicationGroupId: string
        :param ReplicationGroupId: **[REQUIRED]**

          The replication group identifier. This parameter is stored as a lowercase string.

          Constraints:

          * A name must contain from 1 to 40 alphanumeric characters or hyphens.

          * The first character must be a letter.

          * A name cannot end with a hyphen or contain two consecutive hyphens.

        :type ReplicationGroupDescription: string
        :param ReplicationGroupDescription: **[REQUIRED]**

          A user-created description for the replication group.

        :type PrimaryClusterId: string
        :param PrimaryClusterId:

          The identifier of the cluster that serves as the primary for this replication group. This cluster
          must already exist and have a status of ``available`` .

          This parameter is not required if ``NumCacheClusters`` , ``NumNodeGroups`` , or
          ``ReplicasPerNodeGroup`` is specified.

        :type AutomaticFailoverEnabled: boolean
        :param AutomaticFailoverEnabled:

          Specifies whether a read-only replica is automatically promoted to read/write primary if the
          existing primary fails.

          If ``true`` , Multi-AZ is enabled for this replication group. If ``false`` , Multi-AZ is disabled
          for this replication group.

           ``AutomaticFailoverEnabled`` must be enabled for Redis (cluster mode enabled) replication groups.

          Default: false

          Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

          * Redis versions earlier than 2.8.6.

          * Redis (cluster mode disabled): T1 node types.

          * Redis (cluster mode enabled): T1 node types.

        :type NumCacheClusters: integer
        :param NumCacheClusters:

          The number of clusters this replication group initially has.

          This parameter is not used if there is more than one node group (shard). You should use
          ``ReplicasPerNodeGroup`` instead.

          If ``AutomaticFailoverEnabled`` is ``true`` , the value of this parameter must be at least 2. If
          ``AutomaticFailoverEnabled`` is ``false`` you can omit this parameter (it will default to 1), or
          you can explicitly set it to a value between 2 and 6.

          The maximum permitted value for ``NumCacheClusters`` is 6 (1 primary plus 5 replicas).

        :type PreferredCacheClusterAZs: list
        :param PreferredCacheClusterAZs:

          A list of EC2 Availability Zones in which the replication group's clusters are created. The order
          of the Availability Zones in the list is the order in which clusters are allocated. The primary
          cluster is created in the first AZ in the list.

          This parameter is not used if there is more than one node group (shard). You should use
          ``NodeGroupConfiguration`` instead.

          .. note::

            If you are creating your replication group in an Amazon VPC (recommended), you can only locate
            clusters in Availability Zones associated with the subnets in the selected subnet group.

            The number of Availability Zones listed must equal the value of ``NumCacheClusters`` .

          Default: system chosen Availability Zones.

          - *(string) --*

        :type NumNodeGroups: integer
        :param NumNodeGroups:

          An optional parameter that specifies the number of node groups (shards) for this Redis (cluster
          mode enabled) replication group. For Redis (cluster mode disabled) either omit this parameter or
          set it to 1.

          Default: 1

        :type ReplicasPerNodeGroup: integer
        :param ReplicasPerNodeGroup:

          An optional parameter that specifies the number of replica nodes in each node group (shard).
          Valid values are 0 to 5.

        :type NodeGroupConfiguration: list
        :param NodeGroupConfiguration:

          A list of node group (shard) configuration options. Each node group (shard) configuration has the
          following members: ``PrimaryAvailabilityZone`` , ``ReplicaAvailabilityZones`` , ``ReplicaCount``
          , and ``Slots`` .

          If you're creating a Redis (cluster mode disabled) or a Redis (cluster mode enabled) replication
          group, you can use this parameter to individually configure each node group (shard), or you can
          omit this parameter. However, when seeding a Redis (cluster mode enabled) cluster from a S3 rdb
          file, you must configure each node group (shard) using this parameter because you must specify
          the slots for each node group.

          - *(dict) --*

            Node group (shard) configuration options. Each node group (shard) configuration has the
            following: ``Slots`` , ``PrimaryAvailabilityZone`` , ``ReplicaAvailabilityZones`` ,
            ``ReplicaCount`` .

            - **NodeGroupId** *(string) --*

              Either the ElastiCache for Redis supplied 4-digit id or a user supplied id for the node group
              these configuration values apply to.

            - **Slots** *(string) --*

              A string that specifies the keyspace for a particular node group. Keyspaces range from 0 to
              16,383. The string is in the format ``startkey-endkey`` .

              Example: ``"0-3999"``

            - **ReplicaCount** *(integer) --*

              The number of read replica nodes in this node group (shard).

            - **PrimaryAvailabilityZone** *(string) --*

              The Availability Zone where the primary node of this node group (shard) is launched.

            - **ReplicaAvailabilityZones** *(list) --*

              A list of Availability Zones to be used for the read replicas. The number of Availability
              Zones in this list must match the value of ``ReplicaCount`` or ``ReplicasPerNodeGroup`` if
              not specified.

              - *(string) --*

        :type CacheNodeType: string
        :param CacheNodeType:

          The compute and memory capacity of the nodes in the node group (shard).

          The following node types are supported by ElastiCache. Generally speaking, the current generation
          types provide more memory and computational power at lower cost when compared to their equivalent
          previous generation counterparts.

          * General purpose:

            * Current generation:   **M5 node types:**  ``cache.m5.large`` , ``cache.m5.xlarge`` ,
            ``cache.m5.2xlarge`` , ``cache.m5.4xlarge`` , ``cache.m5.12xlarge`` , ``cache.m5.24xlarge``
            **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` , ``cache.m4.2xlarge`` ,
            ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``    **T2 node types:**  ``cache.t2.micro`` ,
            ``cache.t2.small`` , ``cache.t2.medium``

            * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``    **M1 node
            types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` , ``cache.m1.xlarge``
             **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` , ``cache.m3.xlarge`` ,
             ``cache.m3.2xlarge``

          * Compute optimized:

            * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``

          * Memory optimized:

            * Current generation:   **R5 node types:**  ``cache.r5.large`` , ``cache.r5.xlarge`` ,
            ``cache.r5.2xlarge`` , ``cache.r5.4xlarge`` , ``cache.r5.12xlarge`` , ``cache.r5.24xlarge``
            **R4 node types:**  ``cache.r4.large`` , ``cache.r4.xlarge`` , ``cache.r4.2xlarge`` ,
            ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` , ``cache.r4.16xlarge``

            * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` ,
            ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``    **R3 node types:**  ``cache.r3.large`` ,
            ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``

           **Additional node type info**

          * All current generation instance types are created in Amazon VPC by default.

          * Redis append-only files (AOF) are not supported for T1 or T2 instances.

          * Redis Multi-AZ with automatic failover is not supported on T1 instances.

          * Redis configuration variables ``appendonly`` and ``appendfsync`` are not supported on Redis
          version 2.8.22 and later.

        :type Engine: string
        :param Engine:

          The name of the cache engine to be used for the clusters in this replication group.

        :type EngineVersion: string
        :param EngineVersion:

          The version number of the cache engine to be used for the clusters in this replication group. To
          view the supported cache engine versions, use the ``DescribeCacheEngineVersions`` operation.

           **Important:** You can upgrade to a newer engine version (see `Selecting a Cache Engine and
           Version
           <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/SelectEngine.html#VersionManagement>`__
           ) in the *ElastiCache User Guide* , but you cannot downgrade to an earlier engine version. If
           you want to use an earlier engine version, you must delete the existing cluster or replication
           group and create it anew with the earlier engine version.

        :type CacheParameterGroupName: string
        :param CacheParameterGroupName:

          The name of the parameter group to associate with this replication group. If this argument is
          omitted, the default cache parameter group for the specified engine is used.

          .. note::

            If you are restoring to an engine version that is different than the original, you must specify
            the default version of that version. For example, ``CacheParameterGroupName=default.redis4.0`` .

          If you are running Redis version 3.2.4 or later, only one node group (shard), and want to use a
          default parameter group, we recommend that you specify the parameter group by name.

          * To create a Redis (cluster mode disabled) replication group, use
          ``CacheParameterGroupName=default.redis3.2`` .

          * To create a Redis (cluster mode enabled) replication group, use
          ``CacheParameterGroupName=default.redis3.2.cluster.on`` .

        :type CacheSubnetGroupName: string
        :param CacheSubnetGroupName:

          The name of the cache subnet group to be used for the replication group.

          .. warning::

            If you're going to launch your cluster in an Amazon VPC, you need to create a subnet group
            before you start creating a cluster. For more information, see `Subnets and Subnet Groups
            <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/SubnetGroups.html>`__ .

        :type CacheSecurityGroupNames: list
        :param CacheSecurityGroupNames:

          A list of cache security group names to associate with this replication group.

          - *(string) --*

        :type SecurityGroupIds: list
        :param SecurityGroupIds:

          One or more Amazon VPC security groups associated with this replication group.

          Use this parameter only when you are creating a replication group in an Amazon Virtual Private
          Cloud (Amazon VPC).

          - *(string) --*

        :type Tags: list
        :param Tags:

          A list of cost allocation tags to be added to this resource. Tags are comma-separated key,value
          pairs (e.g. Key=``myKey`` , Value=``myKeyValue`` . You can include multiple tags as shown
          following: Key=``myKey`` , Value=``myKeyValue`` Key=``mySecondKey`` , Value=``mySecondKeyValue`` .

          - *(dict) --*

            A cost allocation Tag that can be added to an ElastiCache cluster or replication group. Tags
            are composed of a Key/Value pair. A tag with a null Value is permitted.

            - **Key** *(string) --*

              The key for the tag. May not be null.

            - **Value** *(string) --*

              The tag's value. May be null.

        :type SnapshotArns: list
        :param SnapshotArns:

          A list of Amazon Resource Names (ARN) that uniquely identify the Redis RDB snapshot files stored
          in Amazon S3. The snapshot files are used to populate the new replication group. The Amazon S3
          object name in the ARN cannot contain any commas. The new replication group will have the number
          of node groups (console: shards) specified by the parameter *NumNodeGroups* or the number of node
          groups configured by *NodeGroupConfiguration* regardless of the number of ARNs specified here.

          Example of an Amazon S3 ARN: ``arn:aws:s3:::my_bucket/snapshot1.rdb``

          - *(string) --*

        :type SnapshotName: string
        :param SnapshotName:

          The name of a snapshot from which to restore data into the new replication group. The snapshot
          status changes to ``restoring`` while the new replication group is being created.

        :type PreferredMaintenanceWindow: string
        :param PreferredMaintenanceWindow:

          Specifies the weekly time range during which maintenance on the cluster is performed. It is
          specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum
          maintenance window is a 60 minute period. Valid values for ``ddd`` are:

          Specifies the weekly time range during which maintenance on the cluster is performed. It is
          specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum
          maintenance window is a 60 minute period.

          Valid values for ``ddd`` are:

          * ``sun``

          * ``mon``

          * ``tue``

          * ``wed``

          * ``thu``

          * ``fri``

          * ``sat``

          Example: ``sun:23:00-mon:01:30``

        :type Port: integer
        :param Port:

          The port number on which each member of the replication group accepts connections.

        :type NotificationTopicArn: string
        :param NotificationTopicArn:

          The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) topic to which
          notifications are sent.

          .. note::

            The Amazon SNS topic owner must be the same as the cluster owner.

        :type AutoMinorVersionUpgrade: boolean
        :param AutoMinorVersionUpgrade:

          This parameter is currently disabled.

        :type SnapshotRetentionLimit: integer
        :param SnapshotRetentionLimit:

          The number of days for which ElastiCache retains automatic snapshots before deleting them. For
          example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot that was taken today is retained
          for 5 days before being deleted.

          Default: 0 (i.e., automatic backups are disabled for this cluster).

        :type SnapshotWindow: string
        :param SnapshotWindow:

          The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your
          node group (shard).

          Example: ``05:00-09:00``

          If you do not specify this parameter, ElastiCache automatically chooses an appropriate time range.

        :type AuthToken: string
        :param AuthToken:

           **Reserved parameter.** The password used to access a password protected server.

           ``AuthToken`` can be specified only on replication groups where ``TransitEncryptionEnabled`` is
           ``true`` .

          .. warning::

            For HIPAA compliance, you must specify ``TransitEncryptionEnabled`` as ``true`` , an
            ``AuthToken`` , and a ``CacheSubnetGroup`` .

          Password constraints:

          * Must be only printable ASCII characters.

          * Must be at least 16 characters and no more than 128 characters in length.

          * The only permitted printable special characters are !, &, #, $, ^, <, >, and -. Other printable
          special characters cannot be used in the AUTH token.

          For more information, see `AUTH password <http://redis.io/commands/AUTH>`__ at
          http://redis.io/commands/AUTH.

        :type TransitEncryptionEnabled: boolean
        :param TransitEncryptionEnabled:

          A flag that enables in-transit encryption when set to ``true`` .

          You cannot modify the value of ``TransitEncryptionEnabled`` after the cluster is created. To
          enable in-transit encryption on a cluster you must set ``TransitEncryptionEnabled`` to ``true``
          when you create a cluster.

          This parameter is valid only if the ``Engine`` parameter is ``redis`` , the ``EngineVersion``
          parameter is ``3.2.6`` , ``4.x`` or later, and the cluster is being created in an Amazon VPC.

          If you enable in-transit encryption, you must also specify a value for ``CacheSubnetGroup`` .

           **Required:** Only available when creating a replication group in an Amazon VPC using redis
           version ``3.2.6`` , ``4.x`` or later.

          Default: ``false``

          .. warning::

            For HIPAA compliance, you must specify ``TransitEncryptionEnabled`` as ``true`` , an
            ``AuthToken`` , and a ``CacheSubnetGroup`` .

        :type AtRestEncryptionEnabled: boolean
        :param AtRestEncryptionEnabled:

          A flag that enables encryption at rest when set to ``true`` .

          You cannot modify the value of ``AtRestEncryptionEnabled`` after the replication group is
          created. To enable encryption at rest on a replication group you must set
          ``AtRestEncryptionEnabled`` to ``true`` when you create the replication group.

           **Required:** Only available when creating a replication group in an Amazon VPC using redis
           version ``3.2.6`` , ``4.x`` or later.

          Default: ``false``

        :type KmsKeyId: string
        :param KmsKeyId:

          The ID of the KMS key used to encrypt the disk on the cluster.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ReplicationGroup': {
                    'ReplicationGroupId': 'string',
                    'Description': 'string',
                    'Status': 'string',
                    'PendingModifiedValues': {
                        'PrimaryClusterId': 'string',
                        'AutomaticFailoverStatus': 'enabled'|'disabled',
                        'Resharding': {
                            'SlotMigration': {
                                'ProgressPercentage': 123.0
                            }
                        },
                        'AuthTokenStatus': 'SETTING'|'ROTATING'
                    },
                    'MemberClusters': [
                        'string',
                    ],
                    'NodeGroups': [
                        {
                            'NodeGroupId': 'string',
                            'Status': 'string',
                            'PrimaryEndpoint': {
                                'Address': 'string',
                                'Port': 123
                            },
                            'ReaderEndpoint': {
                                'Address': 'string',
                                'Port': 123
                            },
                            'Slots': 'string',
                            'NodeGroupMembers': [
                                {
                                    'CacheClusterId': 'string',
                                    'CacheNodeId': 'string',
                                    'ReadEndpoint': {
                                        'Address': 'string',
                                        'Port': 123
                                    },
                                    'PreferredAvailabilityZone': 'string',
                                    'CurrentRole': 'string'
                                },
                            ]
                        },
                    ],
                    'SnapshottingClusterId': 'string',
                    'AutomaticFailover': 'enabled'|'disabled'|'enabling'|'disabling',
                    'ConfigurationEndpoint': {
                        'Address': 'string',
                        'Port': 123
                    },
                    'SnapshotRetentionLimit': 123,
                    'SnapshotWindow': 'string',
                    'ClusterEnabled': True|False,
                    'CacheNodeType': 'string',
                    'AuthTokenEnabled': True|False,
                    'AuthTokenLastModifiedDate': datetime(2015, 1, 1),
                    'TransitEncryptionEnabled': True|False,
                    'AtRestEncryptionEnabled': True|False,
                    'KmsKeyId': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **ReplicationGroup** *(dict) --*

              Contains all of the attributes of a specific Redis replication group.

              - **ReplicationGroupId** *(string) --*

                The identifier for the replication group.

              - **Description** *(string) --*

                The user supplied description of the replication group.

              - **Status** *(string) --*

                The current state of this replication group - ``creating`` , ``available`` , ``modifying``
                , ``deleting`` , ``create-failed`` , ``snapshotting`` .

              - **PendingModifiedValues** *(dict) --*

                A group of settings to be applied to the replication group, either immediately or during
                the next maintenance window.

                - **PrimaryClusterId** *(string) --*

                  The primary cluster ID that is applied immediately (if ``--apply-immediately`` was
                  specified), or during the next maintenance window.

                - **AutomaticFailoverStatus** *(string) --*

                  Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

                  Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

                  * Redis versions earlier than 2.8.6.

                  * Redis (cluster mode disabled): T1 node types.

                  * Redis (cluster mode enabled): T1 node types.

                - **Resharding** *(dict) --*

                  The status of an online resharding operation.

                  - **SlotMigration** *(dict) --*

                    Represents the progress of an online resharding operation.

                    - **ProgressPercentage** *(float) --*

                      The percentage of the slot migration that is complete.

                - **AuthTokenStatus** *(string) --*

                  The auth token status

              - **MemberClusters** *(list) --*

                The names of all the cache clusters that are part of this replication group.

                - *(string) --*

              - **NodeGroups** *(list) --*

                A list of node groups in this replication group. For Redis (cluster mode disabled)
                replication groups, this is a single-element list. For Redis (cluster mode enabled)
                replication groups, the list contains an entry for each node group (shard).

                - *(dict) --*

                  Represents a collection of cache nodes in a replication group. One node in the node group
                  is the read/write primary node. All the other nodes are read-only Replica nodes.

                  - **NodeGroupId** *(string) --*

                    The identifier for the node group (shard). A Redis (cluster mode disabled) replication
                    group contains only 1 node group; therefore, the node group ID is 0001. A Redis
                    (cluster mode enabled) replication group contains 1 to 90 node groups numbered 0001 to
                    0090. Optionally, the user can provide the id for a node group.

                  - **Status** *(string) --*

                    The current state of this replication group - ``creating`` , ``available`` , etc.

                  - **PrimaryEndpoint** *(dict) --*

                    The endpoint of the primary node in this node group (shard).

                    - **Address** *(string) --*

                      The DNS hostname of the cache node.

                    - **Port** *(integer) --*

                      The port number that the cache engine is listening on.

                  - **ReaderEndpoint** *(dict) --*

                    The endpoint of the replica nodes in this node group (shard).

                    - **Address** *(string) --*

                      The DNS hostname of the cache node.

                    - **Port** *(integer) --*

                      The port number that the cache engine is listening on.

                  - **Slots** *(string) --*

                    The keyspace for this node group (shard).

                  - **NodeGroupMembers** *(list) --*

                    A list containing information about individual nodes within the node group (shard).

                    - *(dict) --*

                      Represents a single node within a node group (shard).

                      - **CacheClusterId** *(string) --*

                        The ID of the cluster to which the node belongs.

                      - **CacheNodeId** *(string) --*

                        The ID of the node within its cluster. A node ID is a numeric identifier (0001,
                        0002, etc.).

                      - **ReadEndpoint** *(dict) --*

                        The information required for client programs to connect to a node for read
                        operations. The read endpoint is only applicable on Redis (cluster mode disabled)
                        clusters.

                        - **Address** *(string) --*

                          The DNS hostname of the cache node.

                        - **Port** *(integer) --*

                          The port number that the cache engine is listening on.

                      - **PreferredAvailabilityZone** *(string) --*

                        The name of the Availability Zone in which the node is located.

                      - **CurrentRole** *(string) --*

                        The role that is currently assigned to the node - ``primary`` or ``replica`` . This
                        member is only applicable for Redis (cluster mode disabled) replication groups.

              - **SnapshottingClusterId** *(string) --*

                The cluster ID that is used as the daily snapshot source for the replication group.

              - **AutomaticFailover** *(string) --*

                Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

                Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

                * Redis versions earlier than 2.8.6.

                * Redis (cluster mode disabled): T1 node types.

                * Redis (cluster mode enabled): T1 node types.

              - **ConfigurationEndpoint** *(dict) --*

                The configuration endpoint for this replication group. Use the configuration endpoint to
                connect to this replication group.

                - **Address** *(string) --*

                  The DNS hostname of the cache node.

                - **Port** *(integer) --*

                  The port number that the cache engine is listening on.

              - **SnapshotRetentionLimit** *(integer) --*

                The number of days for which ElastiCache retains automatic cluster snapshots before
                deleting them. For example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot that was
                taken today is retained for 5 days before being deleted.

                .. warning::

                  If the value of ``SnapshotRetentionLimit`` is set to zero (0), backups are turned off.

              - **SnapshotWindow** *(string) --*

                The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of
                your node group (shard).

                Example: ``05:00-09:00``

                If you do not specify this parameter, ElastiCache automatically chooses an appropriate time
                range.

                .. note::

                  This parameter is only valid if the ``Engine`` parameter is ``redis`` .

              - **ClusterEnabled** *(boolean) --*

                A flag indicating whether or not this replication group is cluster enabled; i.e., whether
                its data can be partitioned across multiple shards (API/CLI: node groups).

                Valid values: ``true`` | ``false``

              - **CacheNodeType** *(string) --*

                The name of the compute and memory capacity node type for each node in the replication
                group.

              - **AuthTokenEnabled** *(boolean) --*

                A flag that enables using an ``AuthToken`` (password) when issuing Redis commands.

                Default: ``false``

              - **AuthTokenLastModifiedDate** *(datetime) --*

                The date the auth token was last modified

              - **TransitEncryptionEnabled** *(boolean) --*

                A flag that enables in-transit encryption when set to ``true`` .

                You cannot modify the value of ``TransitEncryptionEnabled`` after the cluster is created.
                To enable in-transit encryption on a cluster you must set ``TransitEncryptionEnabled`` to
                ``true`` when you create a cluster.

                 **Required:** Only available when creating a replication group in an Amazon VPC using
                 redis version ``3.2.6`` , ``4.x`` or later.

                Default: ``false``

              - **AtRestEncryptionEnabled** *(boolean) --*

                A flag that enables encryption at-rest when set to ``true`` .

                You cannot modify the value of ``AtRestEncryptionEnabled`` after the cluster is created. To
                enable encryption at-rest on a cluster you must set ``AtRestEncryptionEnabled`` to ``true``
                when you create a cluster.

                 **Required:** Only available when creating a replication group in an Amazon VPC using
                 redis version ``3.2.6`` , ``4.x`` or later.

                Default: ``false``

              - **KmsKeyId** *(string) --*

                The ID of the KMS key used to encrypt the disk in the cluster.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_snapshot(
        self,
        SnapshotName: str,
        ReplicationGroupId: str = None,
        CacheClusterId: str = None,
        KmsKeyId: str = None,
    ) -> ClientCreateSnapshotResponseTypeDef:
        """
        Creates a copy of an entire cluster or replication group at a specific moment in time.

        .. note::

          This operation is valid for Redis only.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/CreateSnapshot>`_

        **Request Syntax**
        ::

          response = client.create_snapshot(
              ReplicationGroupId='string',
              CacheClusterId='string',
              SnapshotName='string',
              KmsKeyId='string'
          )
        :type ReplicationGroupId: string
        :param ReplicationGroupId:

          The identifier of an existing replication group. The snapshot is created from this replication
          group.

        :type CacheClusterId: string
        :param CacheClusterId:

          The identifier of an existing cluster. The snapshot is created from this cluster.

        :type SnapshotName: string
        :param SnapshotName: **[REQUIRED]**

          A name for the snapshot being created.

        :type KmsKeyId: string
        :param KmsKeyId:

          The ID of the KMS key used to encrypt the snapshot.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Snapshot': {
                    'SnapshotName': 'string',
                    'ReplicationGroupId': 'string',
                    'ReplicationGroupDescription': 'string',
                    'CacheClusterId': 'string',
                    'SnapshotStatus': 'string',
                    'SnapshotSource': 'string',
                    'CacheNodeType': 'string',
                    'Engine': 'string',
                    'EngineVersion': 'string',
                    'NumCacheNodes': 123,
                    'PreferredAvailabilityZone': 'string',
                    'CacheClusterCreateTime': datetime(2015, 1, 1),
                    'PreferredMaintenanceWindow': 'string',
                    'TopicArn': 'string',
                    'Port': 123,
                    'CacheParameterGroupName': 'string',
                    'CacheSubnetGroupName': 'string',
                    'VpcId': 'string',
                    'AutoMinorVersionUpgrade': True|False,
                    'SnapshotRetentionLimit': 123,
                    'SnapshotWindow': 'string',
                    'NumNodeGroups': 123,
                    'AutomaticFailover': 'enabled'|'disabled'|'enabling'|'disabling',
                    'NodeSnapshots': [
                        {
                            'CacheClusterId': 'string',
                            'NodeGroupId': 'string',
                            'CacheNodeId': 'string',
                            'NodeGroupConfiguration': {
                                'NodeGroupId': 'string',
                                'Slots': 'string',
                                'ReplicaCount': 123,
                                'PrimaryAvailabilityZone': 'string',
                                'ReplicaAvailabilityZones': [
                                    'string',
                                ]
                            },
                            'CacheSize': 'string',
                            'CacheNodeCreateTime': datetime(2015, 1, 1),
                            'SnapshotCreateTime': datetime(2015, 1, 1)
                        },
                    ],
                    'KmsKeyId': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **Snapshot** *(dict) --*

              Represents a copy of an entire Redis cluster as of the time when the snapshot was taken.

              - **SnapshotName** *(string) --*

                The name of a snapshot. For an automatic snapshot, the name is system-generated. For a
                manual snapshot, this is the user-provided name.

              - **ReplicationGroupId** *(string) --*

                The unique identifier of the source replication group.

              - **ReplicationGroupDescription** *(string) --*

                A description of the source replication group.

              - **CacheClusterId** *(string) --*

                The user-supplied identifier of the source cluster.

              - **SnapshotStatus** *(string) --*

                The status of the snapshot. Valid values: ``creating`` | ``available`` | ``restoring`` |
                ``copying`` | ``deleting`` .

              - **SnapshotSource** *(string) --*

                Indicates whether the snapshot is from an automatic backup (``automated`` ) or was created
                manually (``manual`` ).

              - **CacheNodeType** *(string) --*

                The name of the compute and memory capacity node type for the source cluster.

                The following node types are supported by ElastiCache. Generally speaking, the current
                generation types provide more memory and computational power at lower cost when compared to
                their equivalent previous generation counterparts.

                * General purpose:

                  * Current generation:   **M5 node types:**  ``cache.m5.large`` , ``cache.m5.xlarge`` ,
                  ``cache.m5.2xlarge`` , ``cache.m5.4xlarge`` , ``cache.m5.12xlarge`` ,
                  ``cache.m5.24xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` ,
                  ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``    **T2 node types:**
                   ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``

                  * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``    **M1
                  node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` ,
                  ``cache.m1.xlarge``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` ,
                  ``cache.m3.xlarge`` , ``cache.m3.2xlarge``

                * Compute optimized:

                  * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``

                * Memory optimized:

                  * Current generation:   **R5 node types:**  ``cache.r5.large`` , ``cache.r5.xlarge`` ,
                  ``cache.r5.2xlarge`` , ``cache.r5.4xlarge`` , ``cache.r5.12xlarge`` ,
                  ``cache.r5.24xlarge``    **R4 node types:**  ``cache.r4.large`` , ``cache.r4.xlarge`` ,
                  ``cache.r4.2xlarge`` , ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` , ``cache.r4.16xlarge``

                  * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` ,
                  ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``    **R3 node types:**  ``cache.r3.large`` ,
                  ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``

                 **Additional node type info**

                * All current generation instance types are created in Amazon VPC by default.

                * Redis append-only files (AOF) are not supported for T1 or T2 instances.

                * Redis Multi-AZ with automatic failover is not supported on T1 instances.

                * Redis configuration variables ``appendonly`` and ``appendfsync`` are not supported on
                Redis version 2.8.22 and later.

              - **Engine** *(string) --*

                The name of the cache engine (``memcached`` or ``redis`` ) used by the source cluster.

              - **EngineVersion** *(string) --*

                The version of the cache engine version that is used by the source cluster.

              - **NumCacheNodes** *(integer) --*

                The number of cache nodes in the source cluster.

                For clusters running Redis, this value must be 1. For clusters running Memcached, this
                value must be between 1 and 20.

              - **PreferredAvailabilityZone** *(string) --*

                The name of the Availability Zone in which the source cluster is located.

              - **CacheClusterCreateTime** *(datetime) --*

                The date and time when the source cluster was created.

              - **PreferredMaintenanceWindow** *(string) --*

                Specifies the weekly time range during which maintenance on the cluster is performed. It is
                specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum
                maintenance window is a 60 minute period.

                Valid values for ``ddd`` are:

                * ``sun``

                * ``mon``

                * ``tue``

                * ``wed``

                * ``thu``

                * ``fri``

                * ``sat``

                Example: ``sun:23:00-mon:01:30``

              - **TopicArn** *(string) --*

                The Amazon Resource Name (ARN) for the topic used by the source cluster for publishing
                notifications.

              - **Port** *(integer) --*

                The port number used by each cache nodes in the source cluster.

              - **CacheParameterGroupName** *(string) --*

                The cache parameter group that is associated with the source cluster.

              - **CacheSubnetGroupName** *(string) --*

                The name of the cache subnet group associated with the source cluster.

              - **VpcId** *(string) --*

                The Amazon Virtual Private Cloud identifier (VPC ID) of the cache subnet group for the
                source cluster.

              - **AutoMinorVersionUpgrade** *(boolean) --*

                This parameter is currently disabled.

              - **SnapshotRetentionLimit** *(integer) --*

                For an automatic snapshot, the number of days for which ElastiCache retains the snapshot
                before deleting it.

                For manual snapshots, this field reflects the ``SnapshotRetentionLimit`` for the source
                cluster when the snapshot was created. This field is otherwise ignored: Manual snapshots do
                not expire, and can only be deleted using the ``DeleteSnapshot`` operation.

                 **Important** If the value of SnapshotRetentionLimit is set to zero (0), backups are
                 turned off.

              - **SnapshotWindow** *(string) --*

                The daily time range during which ElastiCache takes daily snapshots of the source cluster.

              - **NumNodeGroups** *(integer) --*

                The number of node groups (shards) in this snapshot. When restoring from a snapshot, the
                number of node groups (shards) in the snapshot and in the restored replication group must
                be the same.

              - **AutomaticFailover** *(string) --*

                Indicates the status of Multi-AZ with automatic failover for the source Redis replication
                group.

                Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

                * Redis versions earlier than 2.8.6.

                * Redis (cluster mode disabled): T1 node types.

                * Redis (cluster mode enabled): T1 node types.

              - **NodeSnapshots** *(list) --*

                A list of the cache nodes in the source cluster.

                - *(dict) --*

                  Represents an individual cache node in a snapshot of a cluster.

                  - **CacheClusterId** *(string) --*

                    A unique identifier for the source cluster.

                  - **NodeGroupId** *(string) --*

                    A unique identifier for the source node group (shard).

                  - **CacheNodeId** *(string) --*

                    The cache node identifier for the node in the source cluster.

                  - **NodeGroupConfiguration** *(dict) --*

                    The configuration for the source node group (shard).

                    - **NodeGroupId** *(string) --*

                      Either the ElastiCache for Redis supplied 4-digit id or a user supplied id for the
                      node group these configuration values apply to.

                    - **Slots** *(string) --*

                      A string that specifies the keyspace for a particular node group. Keyspaces range
                      from 0 to 16,383. The string is in the format ``startkey-endkey`` .

                      Example: ``"0-3999"``

                    - **ReplicaCount** *(integer) --*

                      The number of read replica nodes in this node group (shard).

                    - **PrimaryAvailabilityZone** *(string) --*

                      The Availability Zone where the primary node of this node group (shard) is launched.

                    - **ReplicaAvailabilityZones** *(list) --*

                      A list of Availability Zones to be used for the read replicas. The number of
                      Availability Zones in this list must match the value of ``ReplicaCount`` or
                      ``ReplicasPerNodeGroup`` if not specified.

                      - *(string) --*

                  - **CacheSize** *(string) --*

                    The size of the cache on the source cache node.

                  - **CacheNodeCreateTime** *(datetime) --*

                    The date and time when the cache node was created in the source cluster.

                  - **SnapshotCreateTime** *(datetime) --*

                    The date and time when the source node's metadata and cache data set was obtained for
                    the snapshot.

              - **KmsKeyId** *(string) --*

                The ID of the KMS key used to encrypt the snapshot.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def decrease_replica_count(
        self,
        ReplicationGroupId: str,
        ApplyImmediately: bool,
        NewReplicaCount: int = None,
        ReplicaConfiguration: List[
            ClientDecreaseReplicaCountReplicaConfigurationTypeDef
        ] = None,
        ReplicasToRemove: List[str] = None,
    ) -> ClientDecreaseReplicaCountResponseTypeDef:
        """
        Dynamically decreases the number of replics in a Redis (cluster mode disabled) replication group or
        the number of replica nodes in one or more node groups (shards) of a Redis (cluster mode enabled)
        replication group. This operation is performed with no cluster down time.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/DecreaseReplicaCount>`_

        **Request Syntax**
        ::

          response = client.decrease_replica_count(
              ReplicationGroupId='string',
              NewReplicaCount=123,
              ReplicaConfiguration=[
                  {
                      'NodeGroupId': 'string',
                      'NewReplicaCount': 123,
                      'PreferredAvailabilityZones': [
                          'string',
                      ]
                  },
              ],
              ReplicasToRemove=[
                  'string',
              ],
              ApplyImmediately=True|False
          )
        :type ReplicationGroupId: string
        :param ReplicationGroupId: **[REQUIRED]**

          The id of the replication group from which you want to remove replica nodes.

        :type NewReplicaCount: integer
        :param NewReplicaCount:

          The number of read replica nodes you want at the completion of this operation. For Redis (cluster
          mode disabled) replication groups, this is the number of replica nodes in the replication group.
          For Redis (cluster mode enabled) replication groups, this is the number of replica nodes in each
          of the replication group's node groups.

          The minimum number of replicas in a shard or replication group is:

          * Redis (cluster mode disabled)

            * If Multi-AZ with Automatic Failover is enabled: 1

            * If Multi-AZ with Automatic Failover is not enabled: 0

          * Redis (cluster mode enabled): 0 (though you will not be able to failover to a replica if your
          primary node fails)

        :type ReplicaConfiguration: list
        :param ReplicaConfiguration:

          A list of ``ConfigureShard`` objects that can be used to configure each shard in a Redis (cluster
          mode enabled) replication group. The ``ConfigureShard`` has three members: ``NewReplicaCount`` ,
          ``NodeGroupId`` , and ``PreferredAvailabilityZones`` .

          - *(dict) --*

            Node group (shard) configuration options when adding or removing replicas. Each node group
            (shard) configuration has the following members: NodeGroupId, NewReplicaCount, and
            PreferredAvailabilityZones.

            - **NodeGroupId** *(string) --* **[REQUIRED]**

              The 4-digit id for the node group you are configuring. For Redis (cluster mode disabled)
              replication groups, the node group id is always 0001. To find a Redis (cluster mode
              enabled)'s node group's (shard's) id, see `Finding a Shard's Id
              <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/shard-find-id.html>`__ .

            - **NewReplicaCount** *(integer) --* **[REQUIRED]**

              The number of replicas you want in this node group at the end of this operation. The maximum
              value for ``NewReplicaCount`` is 5. The minimum value depends upon the type of Redis
              replication group you are working with.

              The minimum number of replicas in a shard or replication group is:

              * Redis (cluster mode disabled)

                * If Multi-AZ with Automatic Failover is enabled: 1

                * If Multi-AZ with Automatic Failover is not enable: 0

              * Redis (cluster mode enabled): 0 (though you will not be able to failover to a replica if
              your primary node fails)

            - **PreferredAvailabilityZones** *(list) --*

              A list of ``PreferredAvailabilityZone`` strings that specify which availability zones the
              replication group's nodes are to be in. The nummber of ``PreferredAvailabilityZone`` values
              must equal the value of ``NewReplicaCount`` plus 1 to account for the primary node. If this
              member of ``ReplicaConfiguration`` is omitted, ElastiCache for Redis selects the availability
              zone for each of the replicas.

              - *(string) --*

        :type ReplicasToRemove: list
        :param ReplicasToRemove:

          A list of the node ids to remove from the replication group or node group (shard).

          - *(string) --*

        :type ApplyImmediately: boolean
        :param ApplyImmediately: **[REQUIRED]**

          If ``True`` , the number of replica nodes is decreased immediately. ``ApplyImmediately=False`` is
          not currently supported.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ReplicationGroup': {
                    'ReplicationGroupId': 'string',
                    'Description': 'string',
                    'Status': 'string',
                    'PendingModifiedValues': {
                        'PrimaryClusterId': 'string',
                        'AutomaticFailoverStatus': 'enabled'|'disabled',
                        'Resharding': {
                            'SlotMigration': {
                                'ProgressPercentage': 123.0
                            }
                        },
                        'AuthTokenStatus': 'SETTING'|'ROTATING'
                    },
                    'MemberClusters': [
                        'string',
                    ],
                    'NodeGroups': [
                        {
                            'NodeGroupId': 'string',
                            'Status': 'string',
                            'PrimaryEndpoint': {
                                'Address': 'string',
                                'Port': 123
                            },
                            'ReaderEndpoint': {
                                'Address': 'string',
                                'Port': 123
                            },
                            'Slots': 'string',
                            'NodeGroupMembers': [
                                {
                                    'CacheClusterId': 'string',
                                    'CacheNodeId': 'string',
                                    'ReadEndpoint': {
                                        'Address': 'string',
                                        'Port': 123
                                    },
                                    'PreferredAvailabilityZone': 'string',
                                    'CurrentRole': 'string'
                                },
                            ]
                        },
                    ],
                    'SnapshottingClusterId': 'string',
                    'AutomaticFailover': 'enabled'|'disabled'|'enabling'|'disabling',
                    'ConfigurationEndpoint': {
                        'Address': 'string',
                        'Port': 123
                    },
                    'SnapshotRetentionLimit': 123,
                    'SnapshotWindow': 'string',
                    'ClusterEnabled': True|False,
                    'CacheNodeType': 'string',
                    'AuthTokenEnabled': True|False,
                    'AuthTokenLastModifiedDate': datetime(2015, 1, 1),
                    'TransitEncryptionEnabled': True|False,
                    'AtRestEncryptionEnabled': True|False,
                    'KmsKeyId': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **ReplicationGroup** *(dict) --*

              Contains all of the attributes of a specific Redis replication group.

              - **ReplicationGroupId** *(string) --*

                The identifier for the replication group.

              - **Description** *(string) --*

                The user supplied description of the replication group.

              - **Status** *(string) --*

                The current state of this replication group - ``creating`` , ``available`` , ``modifying``
                , ``deleting`` , ``create-failed`` , ``snapshotting`` .

              - **PendingModifiedValues** *(dict) --*

                A group of settings to be applied to the replication group, either immediately or during
                the next maintenance window.

                - **PrimaryClusterId** *(string) --*

                  The primary cluster ID that is applied immediately (if ``--apply-immediately`` was
                  specified), or during the next maintenance window.

                - **AutomaticFailoverStatus** *(string) --*

                  Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

                  Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

                  * Redis versions earlier than 2.8.6.

                  * Redis (cluster mode disabled): T1 node types.

                  * Redis (cluster mode enabled): T1 node types.

                - **Resharding** *(dict) --*

                  The status of an online resharding operation.

                  - **SlotMigration** *(dict) --*

                    Represents the progress of an online resharding operation.

                    - **ProgressPercentage** *(float) --*

                      The percentage of the slot migration that is complete.

                - **AuthTokenStatus** *(string) --*

                  The auth token status

              - **MemberClusters** *(list) --*

                The names of all the cache clusters that are part of this replication group.

                - *(string) --*

              - **NodeGroups** *(list) --*

                A list of node groups in this replication group. For Redis (cluster mode disabled)
                replication groups, this is a single-element list. For Redis (cluster mode enabled)
                replication groups, the list contains an entry for each node group (shard).

                - *(dict) --*

                  Represents a collection of cache nodes in a replication group. One node in the node group
                  is the read/write primary node. All the other nodes are read-only Replica nodes.

                  - **NodeGroupId** *(string) --*

                    The identifier for the node group (shard). A Redis (cluster mode disabled) replication
                    group contains only 1 node group; therefore, the node group ID is 0001. A Redis
                    (cluster mode enabled) replication group contains 1 to 90 node groups numbered 0001 to
                    0090. Optionally, the user can provide the id for a node group.

                  - **Status** *(string) --*

                    The current state of this replication group - ``creating`` , ``available`` , etc.

                  - **PrimaryEndpoint** *(dict) --*

                    The endpoint of the primary node in this node group (shard).

                    - **Address** *(string) --*

                      The DNS hostname of the cache node.

                    - **Port** *(integer) --*

                      The port number that the cache engine is listening on.

                  - **ReaderEndpoint** *(dict) --*

                    The endpoint of the replica nodes in this node group (shard).

                    - **Address** *(string) --*

                      The DNS hostname of the cache node.

                    - **Port** *(integer) --*

                      The port number that the cache engine is listening on.

                  - **Slots** *(string) --*

                    The keyspace for this node group (shard).

                  - **NodeGroupMembers** *(list) --*

                    A list containing information about individual nodes within the node group (shard).

                    - *(dict) --*

                      Represents a single node within a node group (shard).

                      - **CacheClusterId** *(string) --*

                        The ID of the cluster to which the node belongs.

                      - **CacheNodeId** *(string) --*

                        The ID of the node within its cluster. A node ID is a numeric identifier (0001,
                        0002, etc.).

                      - **ReadEndpoint** *(dict) --*

                        The information required for client programs to connect to a node for read
                        operations. The read endpoint is only applicable on Redis (cluster mode disabled)
                        clusters.

                        - **Address** *(string) --*

                          The DNS hostname of the cache node.

                        - **Port** *(integer) --*

                          The port number that the cache engine is listening on.

                      - **PreferredAvailabilityZone** *(string) --*

                        The name of the Availability Zone in which the node is located.

                      - **CurrentRole** *(string) --*

                        The role that is currently assigned to the node - ``primary`` or ``replica`` . This
                        member is only applicable for Redis (cluster mode disabled) replication groups.

              - **SnapshottingClusterId** *(string) --*

                The cluster ID that is used as the daily snapshot source for the replication group.

              - **AutomaticFailover** *(string) --*

                Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

                Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

                * Redis versions earlier than 2.8.6.

                * Redis (cluster mode disabled): T1 node types.

                * Redis (cluster mode enabled): T1 node types.

              - **ConfigurationEndpoint** *(dict) --*

                The configuration endpoint for this replication group. Use the configuration endpoint to
                connect to this replication group.

                - **Address** *(string) --*

                  The DNS hostname of the cache node.

                - **Port** *(integer) --*

                  The port number that the cache engine is listening on.

              - **SnapshotRetentionLimit** *(integer) --*

                The number of days for which ElastiCache retains automatic cluster snapshots before
                deleting them. For example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot that was
                taken today is retained for 5 days before being deleted.

                .. warning::

                  If the value of ``SnapshotRetentionLimit`` is set to zero (0), backups are turned off.

              - **SnapshotWindow** *(string) --*

                The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of
                your node group (shard).

                Example: ``05:00-09:00``

                If you do not specify this parameter, ElastiCache automatically chooses an appropriate time
                range.

                .. note::

                  This parameter is only valid if the ``Engine`` parameter is ``redis`` .

              - **ClusterEnabled** *(boolean) --*

                A flag indicating whether or not this replication group is cluster enabled; i.e., whether
                its data can be partitioned across multiple shards (API/CLI: node groups).

                Valid values: ``true`` | ``false``

              - **CacheNodeType** *(string) --*

                The name of the compute and memory capacity node type for each node in the replication
                group.

              - **AuthTokenEnabled** *(boolean) --*

                A flag that enables using an ``AuthToken`` (password) when issuing Redis commands.

                Default: ``false``

              - **AuthTokenLastModifiedDate** *(datetime) --*

                The date the auth token was last modified

              - **TransitEncryptionEnabled** *(boolean) --*

                A flag that enables in-transit encryption when set to ``true`` .

                You cannot modify the value of ``TransitEncryptionEnabled`` after the cluster is created.
                To enable in-transit encryption on a cluster you must set ``TransitEncryptionEnabled`` to
                ``true`` when you create a cluster.

                 **Required:** Only available when creating a replication group in an Amazon VPC using
                 redis version ``3.2.6`` , ``4.x`` or later.

                Default: ``false``

              - **AtRestEncryptionEnabled** *(boolean) --*

                A flag that enables encryption at-rest when set to ``true`` .

                You cannot modify the value of ``AtRestEncryptionEnabled`` after the cluster is created. To
                enable encryption at-rest on a cluster you must set ``AtRestEncryptionEnabled`` to ``true``
                when you create a cluster.

                 **Required:** Only available when creating a replication group in an Amazon VPC using
                 redis version ``3.2.6`` , ``4.x`` or later.

                Default: ``false``

              - **KmsKeyId** *(string) --*

                The ID of the KMS key used to encrypt the disk in the cluster.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_cache_cluster(
        self, CacheClusterId: str, FinalSnapshotIdentifier: str = None
    ) -> ClientDeleteCacheClusterResponseTypeDef:
        """
        Deletes a previously provisioned cluster. ``DeleteCacheCluster`` deletes all associated cache
        nodes, node endpoints and the cluster itself. When you receive a successful response from this
        operation, Amazon ElastiCache immediately begins deleting the cluster; you cannot cancel or revert
        this operation.

        This operation is not valid for:

        * Redis (cluster mode enabled) clusters

        * A cluster that is the last read replica of a replication group

        * A node group (shard) that has Multi-AZ mode enabled

        * A cluster from a Redis (cluster mode enabled) replication group

        * A cluster that is not in the ``available`` state

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/DeleteCacheCluster>`_

        **Request Syntax**
        ::

          response = client.delete_cache_cluster(
              CacheClusterId='string',
              FinalSnapshotIdentifier='string'
          )
        :type CacheClusterId: string
        :param CacheClusterId: **[REQUIRED]**

          The cluster identifier for the cluster to be deleted. This parameter is not case sensitive.

        :type FinalSnapshotIdentifier: string
        :param FinalSnapshotIdentifier:

          The user-supplied name of a final cluster snapshot. This is the unique name that identifies the
          snapshot. ElastiCache creates the snapshot, and then deletes the cluster immediately afterward.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'CacheCluster': {
                    'CacheClusterId': 'string',
                    'ConfigurationEndpoint': {
                        'Address': 'string',
                        'Port': 123
                    },
                    'ClientDownloadLandingPage': 'string',
                    'CacheNodeType': 'string',
                    'Engine': 'string',
                    'EngineVersion': 'string',
                    'CacheClusterStatus': 'string',
                    'NumCacheNodes': 123,
                    'PreferredAvailabilityZone': 'string',
                    'CacheClusterCreateTime': datetime(2015, 1, 1),
                    'PreferredMaintenanceWindow': 'string',
                    'PendingModifiedValues': {
                        'NumCacheNodes': 123,
                        'CacheNodeIdsToRemove': [
                            'string',
                        ],
                        'EngineVersion': 'string',
                        'CacheNodeType': 'string',
                        'AuthTokenStatus': 'SETTING'|'ROTATING'
                    },
                    'NotificationConfiguration': {
                        'TopicArn': 'string',
                        'TopicStatus': 'string'
                    },
                    'CacheSecurityGroups': [
                        {
                            'CacheSecurityGroupName': 'string',
                            'Status': 'string'
                        },
                    ],
                    'CacheParameterGroup': {
                        'CacheParameterGroupName': 'string',
                        'ParameterApplyStatus': 'string',
                        'CacheNodeIdsToReboot': [
                            'string',
                        ]
                    },
                    'CacheSubnetGroupName': 'string',
                    'CacheNodes': [
                        {
                            'CacheNodeId': 'string',
                            'CacheNodeStatus': 'string',
                            'CacheNodeCreateTime': datetime(2015, 1, 1),
                            'Endpoint': {
                                'Address': 'string',
                                'Port': 123
                            },
                            'ParameterGroupStatus': 'string',
                            'SourceCacheNodeId': 'string',
                            'CustomerAvailabilityZone': 'string'
                        },
                    ],
                    'AutoMinorVersionUpgrade': True|False,
                    'SecurityGroups': [
                        {
                            'SecurityGroupId': 'string',
                            'Status': 'string'
                        },
                    ],
                    'ReplicationGroupId': 'string',
                    'SnapshotRetentionLimit': 123,
                    'SnapshotWindow': 'string',
                    'AuthTokenEnabled': True|False,
                    'AuthTokenLastModifiedDate': datetime(2015, 1, 1),
                    'TransitEncryptionEnabled': True|False,
                    'AtRestEncryptionEnabled': True|False
                }
            }
          **Response Structure**

          - *(dict) --*

            - **CacheCluster** *(dict) --*

              Contains all of the attributes of a specific cluster.

              - **CacheClusterId** *(string) --*

                The user-supplied identifier of the cluster. This identifier is a unique key that
                identifies a cluster.

              - **ConfigurationEndpoint** *(dict) --*

                Represents a Memcached cluster endpoint which, if Automatic Discovery is enabled on the
                cluster, can be used by an application to connect to any node in the cluster. The
                configuration endpoint will always have ``.cfg`` in it.

                Example: ``mem-3.9dvc4r.cfg.usw2.cache.amazonaws.com:11211``

                - **Address** *(string) --*

                  The DNS hostname of the cache node.

                - **Port** *(integer) --*

                  The port number that the cache engine is listening on.

              - **ClientDownloadLandingPage** *(string) --*

                The URL of the web page where you can download the latest ElastiCache client library.

              - **CacheNodeType** *(string) --*

                The name of the compute and memory capacity node type for the cluster.

                The following node types are supported by ElastiCache. Generally speaking, the current
                generation types provide more memory and computational power at lower cost when compared to
                their equivalent previous generation counterparts.

                * General purpose:

                  * Current generation:   **M5 node types:**  ``cache.m5.large`` , ``cache.m5.xlarge`` ,
                  ``cache.m5.2xlarge`` , ``cache.m5.4xlarge`` , ``cache.m5.12xlarge`` ,
                  ``cache.m5.24xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` ,
                  ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``    **T2 node types:**
                   ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``

                  * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``    **M1
                  node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` ,
                  ``cache.m1.xlarge``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` ,
                  ``cache.m3.xlarge`` , ``cache.m3.2xlarge``

                * Compute optimized:

                  * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``

                * Memory optimized:

                  * Current generation:   **R5 node types:**  ``cache.r5.large`` , ``cache.r5.xlarge`` ,
                  ``cache.r5.2xlarge`` , ``cache.r5.4xlarge`` , ``cache.r5.12xlarge`` ,
                  ``cache.r5.24xlarge``    **R4 node types:**  ``cache.r4.large`` , ``cache.r4.xlarge`` ,
                  ``cache.r4.2xlarge`` , ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` , ``cache.r4.16xlarge``

                  * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` ,
                  ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``    **R3 node types:**  ``cache.r3.large`` ,
                  ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``

                 **Additional node type info**

                * All current generation instance types are created in Amazon VPC by default.

                * Redis append-only files (AOF) are not supported for T1 or T2 instances.

                * Redis Multi-AZ with automatic failover is not supported on T1 instances.

                * Redis configuration variables ``appendonly`` and ``appendfsync`` are not supported on
                Redis version 2.8.22 and later.

              - **Engine** *(string) --*

                The name of the cache engine (``memcached`` or ``redis`` ) to be used for this cluster.

              - **EngineVersion** *(string) --*

                The version of the cache engine that is used in this cluster.

              - **CacheClusterStatus** *(string) --*

                The current state of this cluster, one of the following values: ``available`` ,
                ``creating`` , ``deleted`` , ``deleting`` , ``incompatible-network`` , ``modifying`` ,
                ``rebooting cluster nodes`` , ``restore-failed`` , or ``snapshotting`` .

              - **NumCacheNodes** *(integer) --*

                The number of cache nodes in the cluster.

                For clusters running Redis, this value must be 1. For clusters running Memcached, this
                value must be between 1 and 20.

              - **PreferredAvailabilityZone** *(string) --*

                The name of the Availability Zone in which the cluster is located or "Multiple" if the
                cache nodes are located in different Availability Zones.

              - **CacheClusterCreateTime** *(datetime) --*

                The date and time when the cluster was created.

              - **PreferredMaintenanceWindow** *(string) --*

                Specifies the weekly time range during which maintenance on the cluster is performed. It is
                specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum
                maintenance window is a 60 minute period.

                Valid values for ``ddd`` are:

                * ``sun``

                * ``mon``

                * ``tue``

                * ``wed``

                * ``thu``

                * ``fri``

                * ``sat``

                Example: ``sun:23:00-mon:01:30``

              - **PendingModifiedValues** *(dict) --*

                A group of settings that are applied to the cluster in the future, or that are currently
                being applied.

                - **NumCacheNodes** *(integer) --*

                  The new number of cache nodes for the cluster.

                  For clusters running Redis, this value must be 1. For clusters running Memcached, this
                  value must be between 1 and 20.

                - **CacheNodeIdsToRemove** *(list) --*

                  A list of cache node IDs that are being removed (or will be removed) from the cluster. A
                  node ID is a 4-digit numeric identifier (0001, 0002, etc.).

                  - *(string) --*

                - **EngineVersion** *(string) --*

                  The new cache engine version that the cluster runs.

                - **CacheNodeType** *(string) --*

                  The cache node type that this cluster or replication group is scaled to.

                - **AuthTokenStatus** *(string) --*

                  The auth token status

              - **NotificationConfiguration** *(dict) --*

                Describes a notification topic and its status. Notification topics are used for publishing
                ElastiCache events to subscribers using Amazon Simple Notification Service (SNS).

                - **TopicArn** *(string) --*

                  The Amazon Resource Name (ARN) that identifies the topic.

                - **TopicStatus** *(string) --*

                  The current state of the topic.

              - **CacheSecurityGroups** *(list) --*

                A list of cache security group elements, composed of name and status sub-elements.

                - *(dict) --*

                  Represents a cluster's status within a particular cache security group.

                  - **CacheSecurityGroupName** *(string) --*

                    The name of the cache security group.

                  - **Status** *(string) --*

                    The membership status in the cache security group. The status changes when a cache
                    security group is modified, or when the cache security groups assigned to a cluster are
                    modified.

              - **CacheParameterGroup** *(dict) --*

                Status of the cache parameter group.

                - **CacheParameterGroupName** *(string) --*

                  The name of the cache parameter group.

                - **ParameterApplyStatus** *(string) --*

                  The status of parameter updates.

                - **CacheNodeIdsToReboot** *(list) --*

                  A list of the cache node IDs which need to be rebooted for parameter changes to be
                  applied. A node ID is a numeric identifier (0001, 0002, etc.).

                  - *(string) --*

              - **CacheSubnetGroupName** *(string) --*

                The name of the cache subnet group associated with the cluster.

              - **CacheNodes** *(list) --*

                A list of cache nodes that are members of the cluster.

                - *(dict) --*

                  Represents an individual cache node within a cluster. Each cache node runs its own
                  instance of the cluster's protocol-compliant caching software - either Memcached or Redis.

                  The following node types are supported by ElastiCache. Generally speaking, the current
                  generation types provide more memory and computational power at lower cost when compared
                  to their equivalent previous generation counterparts.

                  * General purpose:

                    * Current generation:   **M5 node types:**  ``cache.m5.large`` , ``cache.m5.xlarge`` ,
                    ``cache.m5.2xlarge`` , ``cache.m5.4xlarge`` , ``cache.m5.12xlarge`` ,
                    ``cache.m5.24xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` ,
                    ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``    **T2 node
                    types:**  ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``

                    * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``
                    **M1 node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` ,
                    ``cache.m1.xlarge``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` ,
                    ``cache.m3.xlarge`` , ``cache.m3.2xlarge``

                  * Compute optimized:

                    * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``

                  * Memory optimized:

                    * Current generation:   **R5 node types:**  ``cache.r5.large`` , ``cache.r5.xlarge`` ,
                    ``cache.r5.2xlarge`` , ``cache.r5.4xlarge`` , ``cache.r5.12xlarge`` ,
                    ``cache.r5.24xlarge``    **R4 node types:**  ``cache.r4.large`` , ``cache.r4.xlarge`` ,
                    ``cache.r4.2xlarge`` , ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` ,
                    ``cache.r4.16xlarge``

                    * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` ,
                    ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``    **R3 node types:**  ``cache.r3.large`` ,
                    ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``

                   **Additional node type info**

                  * All current generation instance types are created in Amazon VPC by default.

                  * Redis append-only files (AOF) are not supported for T1 or T2 instances.

                  * Redis Multi-AZ with automatic failover is not supported on T1 instances.

                  * Redis configuration variables ``appendonly`` and ``appendfsync`` are not supported on
                  Redis version 2.8.22 and later.

                  - **CacheNodeId** *(string) --*

                    The cache node identifier. A node ID is a numeric identifier (0001, 0002, etc.). The
                    combination of cluster ID and node ID uniquely identifies every cache node used in a
                    customer's AWS account.

                  - **CacheNodeStatus** *(string) --*

                    The current state of this cache node.

                  - **CacheNodeCreateTime** *(datetime) --*

                    The date and time when the cache node was created.

                  - **Endpoint** *(dict) --*

                    The hostname for connecting to this cache node.

                    - **Address** *(string) --*

                      The DNS hostname of the cache node.

                    - **Port** *(integer) --*

                      The port number that the cache engine is listening on.

                  - **ParameterGroupStatus** *(string) --*

                    The status of the parameter group applied to this cache node.

                  - **SourceCacheNodeId** *(string) --*

                    The ID of the primary node to which this read replica node is synchronized. If this
                    field is empty, this node is not associated with a primary cluster.

                  - **CustomerAvailabilityZone** *(string) --*

                    The Availability Zone where this node was created and now resides.

              - **AutoMinorVersionUpgrade** *(boolean) --*

                This parameter is currently disabled.

              - **SecurityGroups** *(list) --*

                A list of VPC Security Groups associated with the cluster.

                - *(dict) --*

                  Represents a single cache security group and its status.

                  - **SecurityGroupId** *(string) --*

                    The identifier of the cache security group.

                  - **Status** *(string) --*

                    The status of the cache security group membership. The status changes whenever a cache
                    security group is modified, or when the cache security groups assigned to a cluster are
                    modified.

              - **ReplicationGroupId** *(string) --*

                The replication group to which this cluster belongs. If this field is empty, the cluster is
                not associated with any replication group.

              - **SnapshotRetentionLimit** *(integer) --*

                The number of days for which ElastiCache retains automatic cluster snapshots before
                deleting them. For example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot that was
                taken today is retained for 5 days before being deleted.

                .. warning::

                  If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.

              - **SnapshotWindow** *(string) --*

                The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of
                your cluster.

                Example: ``05:00-09:00``

              - **AuthTokenEnabled** *(boolean) --*

                A flag that enables using an ``AuthToken`` (password) when issuing Redis commands.

                Default: ``false``

              - **AuthTokenLastModifiedDate** *(datetime) --*

                The date the auth token was last modified

              - **TransitEncryptionEnabled** *(boolean) --*

                A flag that enables in-transit encryption when set to ``true`` .

                You cannot modify the value of ``TransitEncryptionEnabled`` after the cluster is created.
                To enable in-transit encryption on a cluster you must set ``TransitEncryptionEnabled`` to
                ``true`` when you create a cluster.

                 **Required:** Only available when creating a replication group in an Amazon VPC using
                 redis version ``3.2.6`` , ``4.x`` or later.

                Default: ``false``

              - **AtRestEncryptionEnabled** *(boolean) --*

                A flag that enables encryption at-rest when set to ``true`` .

                You cannot modify the value of ``AtRestEncryptionEnabled`` after the cluster is created. To
                enable at-rest encryption on a cluster you must set ``AtRestEncryptionEnabled`` to ``true``
                when you create a cluster.

                 **Required:** Only available when creating a replication group in an Amazon VPC using
                 redis version ``3.2.6`` , ``4.x`` or later.

                Default: ``false``

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_cache_parameter_group(self, CacheParameterGroupName: str) -> None:
        """
        Deletes the specified cache parameter group. You cannot delete a cache parameter group if it is
        associated with any cache clusters.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/DeleteCacheParameterGroup>`_

        **Request Syntax**
        ::

          response = client.delete_cache_parameter_group(
              CacheParameterGroupName='string'
          )
        :type CacheParameterGroupName: string
        :param CacheParameterGroupName: **[REQUIRED]**

          The name of the cache parameter group to delete.

          .. note::

            The specified cache security group must not be associated with any clusters.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_cache_security_group(self, CacheSecurityGroupName: str) -> None:
        """
        Deletes a cache security group.

        .. note::

          You cannot delete a cache security group if it is associated with any clusters.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/DeleteCacheSecurityGroup>`_

        **Request Syntax**
        ::

          response = client.delete_cache_security_group(
              CacheSecurityGroupName='string'
          )
        :type CacheSecurityGroupName: string
        :param CacheSecurityGroupName: **[REQUIRED]**

          The name of the cache security group to delete.

          .. note::

            You cannot delete the default security group.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_cache_subnet_group(self, CacheSubnetGroupName: str) -> None:
        """
        Deletes a cache subnet group.

        .. note::

          You cannot delete a cache subnet group if it is associated with any clusters.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/DeleteCacheSubnetGroup>`_

        **Request Syntax**
        ::

          response = client.delete_cache_subnet_group(
              CacheSubnetGroupName='string'
          )
        :type CacheSubnetGroupName: string
        :param CacheSubnetGroupName: **[REQUIRED]**

          The name of the cache subnet group to delete.

          Constraints: Must contain no more than 255 alphanumeric characters or hyphens.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_replication_group(
        self,
        ReplicationGroupId: str,
        RetainPrimaryCluster: bool = None,
        FinalSnapshotIdentifier: str = None,
    ) -> ClientDeleteReplicationGroupResponseTypeDef:
        """
        Deletes an existing replication group. By default, this operation deletes the entire replication
        group, including the primary/primaries and all of the read replicas. If the replication group has
        only one primary, you can optionally delete only the read replicas, while retaining the primary by
        setting ``RetainPrimaryCluster=true`` .

        When you receive a successful response from this operation, Amazon ElastiCache immediately begins
        deleting the selected resources; you cannot cancel or revert this operation.

        .. note::

          This operation is valid for Redis only.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/DeleteReplicationGroup>`_

        **Request Syntax**
        ::

          response = client.delete_replication_group(
              ReplicationGroupId='string',
              RetainPrimaryCluster=True|False,
              FinalSnapshotIdentifier='string'
          )
        :type ReplicationGroupId: string
        :param ReplicationGroupId: **[REQUIRED]**

          The identifier for the cluster to be deleted. This parameter is not case sensitive.

        :type RetainPrimaryCluster: boolean
        :param RetainPrimaryCluster:

          If set to ``true`` , all of the read replicas are deleted, but the primary node is retained.

        :type FinalSnapshotIdentifier: string
        :param FinalSnapshotIdentifier:

          The name of a final node group (shard) snapshot. ElastiCache creates the snapshot from the
          primary node in the cluster, rather than one of the replicas; this is to ensure that it captures
          the freshest data. After the final snapshot is taken, the replication group is immediately
          deleted.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ReplicationGroup': {
                    'ReplicationGroupId': 'string',
                    'Description': 'string',
                    'Status': 'string',
                    'PendingModifiedValues': {
                        'PrimaryClusterId': 'string',
                        'AutomaticFailoverStatus': 'enabled'|'disabled',
                        'Resharding': {
                            'SlotMigration': {
                                'ProgressPercentage': 123.0
                            }
                        },
                        'AuthTokenStatus': 'SETTING'|'ROTATING'
                    },
                    'MemberClusters': [
                        'string',
                    ],
                    'NodeGroups': [
                        {
                            'NodeGroupId': 'string',
                            'Status': 'string',
                            'PrimaryEndpoint': {
                                'Address': 'string',
                                'Port': 123
                            },
                            'ReaderEndpoint': {
                                'Address': 'string',
                                'Port': 123
                            },
                            'Slots': 'string',
                            'NodeGroupMembers': [
                                {
                                    'CacheClusterId': 'string',
                                    'CacheNodeId': 'string',
                                    'ReadEndpoint': {
                                        'Address': 'string',
                                        'Port': 123
                                    },
                                    'PreferredAvailabilityZone': 'string',
                                    'CurrentRole': 'string'
                                },
                            ]
                        },
                    ],
                    'SnapshottingClusterId': 'string',
                    'AutomaticFailover': 'enabled'|'disabled'|'enabling'|'disabling',
                    'ConfigurationEndpoint': {
                        'Address': 'string',
                        'Port': 123
                    },
                    'SnapshotRetentionLimit': 123,
                    'SnapshotWindow': 'string',
                    'ClusterEnabled': True|False,
                    'CacheNodeType': 'string',
                    'AuthTokenEnabled': True|False,
                    'AuthTokenLastModifiedDate': datetime(2015, 1, 1),
                    'TransitEncryptionEnabled': True|False,
                    'AtRestEncryptionEnabled': True|False,
                    'KmsKeyId': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **ReplicationGroup** *(dict) --*

              Contains all of the attributes of a specific Redis replication group.

              - **ReplicationGroupId** *(string) --*

                The identifier for the replication group.

              - **Description** *(string) --*

                The user supplied description of the replication group.

              - **Status** *(string) --*

                The current state of this replication group - ``creating`` , ``available`` , ``modifying``
                , ``deleting`` , ``create-failed`` , ``snapshotting`` .

              - **PendingModifiedValues** *(dict) --*

                A group of settings to be applied to the replication group, either immediately or during
                the next maintenance window.

                - **PrimaryClusterId** *(string) --*

                  The primary cluster ID that is applied immediately (if ``--apply-immediately`` was
                  specified), or during the next maintenance window.

                - **AutomaticFailoverStatus** *(string) --*

                  Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

                  Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

                  * Redis versions earlier than 2.8.6.

                  * Redis (cluster mode disabled): T1 node types.

                  * Redis (cluster mode enabled): T1 node types.

                - **Resharding** *(dict) --*

                  The status of an online resharding operation.

                  - **SlotMigration** *(dict) --*

                    Represents the progress of an online resharding operation.

                    - **ProgressPercentage** *(float) --*

                      The percentage of the slot migration that is complete.

                - **AuthTokenStatus** *(string) --*

                  The auth token status

              - **MemberClusters** *(list) --*

                The names of all the cache clusters that are part of this replication group.

                - *(string) --*

              - **NodeGroups** *(list) --*

                A list of node groups in this replication group. For Redis (cluster mode disabled)
                replication groups, this is a single-element list. For Redis (cluster mode enabled)
                replication groups, the list contains an entry for each node group (shard).

                - *(dict) --*

                  Represents a collection of cache nodes in a replication group. One node in the node group
                  is the read/write primary node. All the other nodes are read-only Replica nodes.

                  - **NodeGroupId** *(string) --*

                    The identifier for the node group (shard). A Redis (cluster mode disabled) replication
                    group contains only 1 node group; therefore, the node group ID is 0001. A Redis
                    (cluster mode enabled) replication group contains 1 to 90 node groups numbered 0001 to
                    0090. Optionally, the user can provide the id for a node group.

                  - **Status** *(string) --*

                    The current state of this replication group - ``creating`` , ``available`` , etc.

                  - **PrimaryEndpoint** *(dict) --*

                    The endpoint of the primary node in this node group (shard).

                    - **Address** *(string) --*

                      The DNS hostname of the cache node.

                    - **Port** *(integer) --*

                      The port number that the cache engine is listening on.

                  - **ReaderEndpoint** *(dict) --*

                    The endpoint of the replica nodes in this node group (shard).

                    - **Address** *(string) --*

                      The DNS hostname of the cache node.

                    - **Port** *(integer) --*

                      The port number that the cache engine is listening on.

                  - **Slots** *(string) --*

                    The keyspace for this node group (shard).

                  - **NodeGroupMembers** *(list) --*

                    A list containing information about individual nodes within the node group (shard).

                    - *(dict) --*

                      Represents a single node within a node group (shard).

                      - **CacheClusterId** *(string) --*

                        The ID of the cluster to which the node belongs.

                      - **CacheNodeId** *(string) --*

                        The ID of the node within its cluster. A node ID is a numeric identifier (0001,
                        0002, etc.).

                      - **ReadEndpoint** *(dict) --*

                        The information required for client programs to connect to a node for read
                        operations. The read endpoint is only applicable on Redis (cluster mode disabled)
                        clusters.

                        - **Address** *(string) --*

                          The DNS hostname of the cache node.

                        - **Port** *(integer) --*

                          The port number that the cache engine is listening on.

                      - **PreferredAvailabilityZone** *(string) --*

                        The name of the Availability Zone in which the node is located.

                      - **CurrentRole** *(string) --*

                        The role that is currently assigned to the node - ``primary`` or ``replica`` . This
                        member is only applicable for Redis (cluster mode disabled) replication groups.

              - **SnapshottingClusterId** *(string) --*

                The cluster ID that is used as the daily snapshot source for the replication group.

              - **AutomaticFailover** *(string) --*

                Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

                Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

                * Redis versions earlier than 2.8.6.

                * Redis (cluster mode disabled): T1 node types.

                * Redis (cluster mode enabled): T1 node types.

              - **ConfigurationEndpoint** *(dict) --*

                The configuration endpoint for this replication group. Use the configuration endpoint to
                connect to this replication group.

                - **Address** *(string) --*

                  The DNS hostname of the cache node.

                - **Port** *(integer) --*

                  The port number that the cache engine is listening on.

              - **SnapshotRetentionLimit** *(integer) --*

                The number of days for which ElastiCache retains automatic cluster snapshots before
                deleting them. For example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot that was
                taken today is retained for 5 days before being deleted.

                .. warning::

                  If the value of ``SnapshotRetentionLimit`` is set to zero (0), backups are turned off.

              - **SnapshotWindow** *(string) --*

                The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of
                your node group (shard).

                Example: ``05:00-09:00``

                If you do not specify this parameter, ElastiCache automatically chooses an appropriate time
                range.

                .. note::

                  This parameter is only valid if the ``Engine`` parameter is ``redis`` .

              - **ClusterEnabled** *(boolean) --*

                A flag indicating whether or not this replication group is cluster enabled; i.e., whether
                its data can be partitioned across multiple shards (API/CLI: node groups).

                Valid values: ``true`` | ``false``

              - **CacheNodeType** *(string) --*

                The name of the compute and memory capacity node type for each node in the replication
                group.

              - **AuthTokenEnabled** *(boolean) --*

                A flag that enables using an ``AuthToken`` (password) when issuing Redis commands.

                Default: ``false``

              - **AuthTokenLastModifiedDate** *(datetime) --*

                The date the auth token was last modified

              - **TransitEncryptionEnabled** *(boolean) --*

                A flag that enables in-transit encryption when set to ``true`` .

                You cannot modify the value of ``TransitEncryptionEnabled`` after the cluster is created.
                To enable in-transit encryption on a cluster you must set ``TransitEncryptionEnabled`` to
                ``true`` when you create a cluster.

                 **Required:** Only available when creating a replication group in an Amazon VPC using
                 redis version ``3.2.6`` , ``4.x`` or later.

                Default: ``false``

              - **AtRestEncryptionEnabled** *(boolean) --*

                A flag that enables encryption at-rest when set to ``true`` .

                You cannot modify the value of ``AtRestEncryptionEnabled`` after the cluster is created. To
                enable encryption at-rest on a cluster you must set ``AtRestEncryptionEnabled`` to ``true``
                when you create a cluster.

                 **Required:** Only available when creating a replication group in an Amazon VPC using
                 redis version ``3.2.6`` , ``4.x`` or later.

                Default: ``false``

              - **KmsKeyId** *(string) --*

                The ID of the KMS key used to encrypt the disk in the cluster.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_snapshot(self, SnapshotName: str) -> ClientDeleteSnapshotResponseTypeDef:
        """
        Deletes an existing snapshot. When you receive a successful response from this operation,
        ElastiCache immediately begins deleting the snapshot; you cannot cancel or revert this operation.

        .. note::

          This operation is valid for Redis only.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/DeleteSnapshot>`_

        **Request Syntax**
        ::

          response = client.delete_snapshot(
              SnapshotName='string'
          )
        :type SnapshotName: string
        :param SnapshotName: **[REQUIRED]**

          The name of the snapshot to be deleted.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Snapshot': {
                    'SnapshotName': 'string',
                    'ReplicationGroupId': 'string',
                    'ReplicationGroupDescription': 'string',
                    'CacheClusterId': 'string',
                    'SnapshotStatus': 'string',
                    'SnapshotSource': 'string',
                    'CacheNodeType': 'string',
                    'Engine': 'string',
                    'EngineVersion': 'string',
                    'NumCacheNodes': 123,
                    'PreferredAvailabilityZone': 'string',
                    'CacheClusterCreateTime': datetime(2015, 1, 1),
                    'PreferredMaintenanceWindow': 'string',
                    'TopicArn': 'string',
                    'Port': 123,
                    'CacheParameterGroupName': 'string',
                    'CacheSubnetGroupName': 'string',
                    'VpcId': 'string',
                    'AutoMinorVersionUpgrade': True|False,
                    'SnapshotRetentionLimit': 123,
                    'SnapshotWindow': 'string',
                    'NumNodeGroups': 123,
                    'AutomaticFailover': 'enabled'|'disabled'|'enabling'|'disabling',
                    'NodeSnapshots': [
                        {
                            'CacheClusterId': 'string',
                            'NodeGroupId': 'string',
                            'CacheNodeId': 'string',
                            'NodeGroupConfiguration': {
                                'NodeGroupId': 'string',
                                'Slots': 'string',
                                'ReplicaCount': 123,
                                'PrimaryAvailabilityZone': 'string',
                                'ReplicaAvailabilityZones': [
                                    'string',
                                ]
                            },
                            'CacheSize': 'string',
                            'CacheNodeCreateTime': datetime(2015, 1, 1),
                            'SnapshotCreateTime': datetime(2015, 1, 1)
                        },
                    ],
                    'KmsKeyId': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **Snapshot** *(dict) --*

              Represents a copy of an entire Redis cluster as of the time when the snapshot was taken.

              - **SnapshotName** *(string) --*

                The name of a snapshot. For an automatic snapshot, the name is system-generated. For a
                manual snapshot, this is the user-provided name.

              - **ReplicationGroupId** *(string) --*

                The unique identifier of the source replication group.

              - **ReplicationGroupDescription** *(string) --*

                A description of the source replication group.

              - **CacheClusterId** *(string) --*

                The user-supplied identifier of the source cluster.

              - **SnapshotStatus** *(string) --*

                The status of the snapshot. Valid values: ``creating`` | ``available`` | ``restoring`` |
                ``copying`` | ``deleting`` .

              - **SnapshotSource** *(string) --*

                Indicates whether the snapshot is from an automatic backup (``automated`` ) or was created
                manually (``manual`` ).

              - **CacheNodeType** *(string) --*

                The name of the compute and memory capacity node type for the source cluster.

                The following node types are supported by ElastiCache. Generally speaking, the current
                generation types provide more memory and computational power at lower cost when compared to
                their equivalent previous generation counterparts.

                * General purpose:

                  * Current generation:   **M5 node types:**  ``cache.m5.large`` , ``cache.m5.xlarge`` ,
                  ``cache.m5.2xlarge`` , ``cache.m5.4xlarge`` , ``cache.m5.12xlarge`` ,
                  ``cache.m5.24xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` ,
                  ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``    **T2 node types:**
                   ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``

                  * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``    **M1
                  node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` ,
                  ``cache.m1.xlarge``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` ,
                  ``cache.m3.xlarge`` , ``cache.m3.2xlarge``

                * Compute optimized:

                  * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``

                * Memory optimized:

                  * Current generation:   **R5 node types:**  ``cache.r5.large`` , ``cache.r5.xlarge`` ,
                  ``cache.r5.2xlarge`` , ``cache.r5.4xlarge`` , ``cache.r5.12xlarge`` ,
                  ``cache.r5.24xlarge``    **R4 node types:**  ``cache.r4.large`` , ``cache.r4.xlarge`` ,
                  ``cache.r4.2xlarge`` , ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` , ``cache.r4.16xlarge``

                  * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` ,
                  ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``    **R3 node types:**  ``cache.r3.large`` ,
                  ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``

                 **Additional node type info**

                * All current generation instance types are created in Amazon VPC by default.

                * Redis append-only files (AOF) are not supported for T1 or T2 instances.

                * Redis Multi-AZ with automatic failover is not supported on T1 instances.

                * Redis configuration variables ``appendonly`` and ``appendfsync`` are not supported on
                Redis version 2.8.22 and later.

              - **Engine** *(string) --*

                The name of the cache engine (``memcached`` or ``redis`` ) used by the source cluster.

              - **EngineVersion** *(string) --*

                The version of the cache engine version that is used by the source cluster.

              - **NumCacheNodes** *(integer) --*

                The number of cache nodes in the source cluster.

                For clusters running Redis, this value must be 1. For clusters running Memcached, this
                value must be between 1 and 20.

              - **PreferredAvailabilityZone** *(string) --*

                The name of the Availability Zone in which the source cluster is located.

              - **CacheClusterCreateTime** *(datetime) --*

                The date and time when the source cluster was created.

              - **PreferredMaintenanceWindow** *(string) --*

                Specifies the weekly time range during which maintenance on the cluster is performed. It is
                specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum
                maintenance window is a 60 minute period.

                Valid values for ``ddd`` are:

                * ``sun``

                * ``mon``

                * ``tue``

                * ``wed``

                * ``thu``

                * ``fri``

                * ``sat``

                Example: ``sun:23:00-mon:01:30``

              - **TopicArn** *(string) --*

                The Amazon Resource Name (ARN) for the topic used by the source cluster for publishing
                notifications.

              - **Port** *(integer) --*

                The port number used by each cache nodes in the source cluster.

              - **CacheParameterGroupName** *(string) --*

                The cache parameter group that is associated with the source cluster.

              - **CacheSubnetGroupName** *(string) --*

                The name of the cache subnet group associated with the source cluster.

              - **VpcId** *(string) --*

                The Amazon Virtual Private Cloud identifier (VPC ID) of the cache subnet group for the
                source cluster.

              - **AutoMinorVersionUpgrade** *(boolean) --*

                This parameter is currently disabled.

              - **SnapshotRetentionLimit** *(integer) --*

                For an automatic snapshot, the number of days for which ElastiCache retains the snapshot
                before deleting it.

                For manual snapshots, this field reflects the ``SnapshotRetentionLimit`` for the source
                cluster when the snapshot was created. This field is otherwise ignored: Manual snapshots do
                not expire, and can only be deleted using the ``DeleteSnapshot`` operation.

                 **Important** If the value of SnapshotRetentionLimit is set to zero (0), backups are
                 turned off.

              - **SnapshotWindow** *(string) --*

                The daily time range during which ElastiCache takes daily snapshots of the source cluster.

              - **NumNodeGroups** *(integer) --*

                The number of node groups (shards) in this snapshot. When restoring from a snapshot, the
                number of node groups (shards) in the snapshot and in the restored replication group must
                be the same.

              - **AutomaticFailover** *(string) --*

                Indicates the status of Multi-AZ with automatic failover for the source Redis replication
                group.

                Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

                * Redis versions earlier than 2.8.6.

                * Redis (cluster mode disabled): T1 node types.

                * Redis (cluster mode enabled): T1 node types.

              - **NodeSnapshots** *(list) --*

                A list of the cache nodes in the source cluster.

                - *(dict) --*

                  Represents an individual cache node in a snapshot of a cluster.

                  - **CacheClusterId** *(string) --*

                    A unique identifier for the source cluster.

                  - **NodeGroupId** *(string) --*

                    A unique identifier for the source node group (shard).

                  - **CacheNodeId** *(string) --*

                    The cache node identifier for the node in the source cluster.

                  - **NodeGroupConfiguration** *(dict) --*

                    The configuration for the source node group (shard).

                    - **NodeGroupId** *(string) --*

                      Either the ElastiCache for Redis supplied 4-digit id or a user supplied id for the
                      node group these configuration values apply to.

                    - **Slots** *(string) --*

                      A string that specifies the keyspace for a particular node group. Keyspaces range
                      from 0 to 16,383. The string is in the format ``startkey-endkey`` .

                      Example: ``"0-3999"``

                    - **ReplicaCount** *(integer) --*

                      The number of read replica nodes in this node group (shard).

                    - **PrimaryAvailabilityZone** *(string) --*

                      The Availability Zone where the primary node of this node group (shard) is launched.

                    - **ReplicaAvailabilityZones** *(list) --*

                      A list of Availability Zones to be used for the read replicas. The number of
                      Availability Zones in this list must match the value of ``ReplicaCount`` or
                      ``ReplicasPerNodeGroup`` if not specified.

                      - *(string) --*

                  - **CacheSize** *(string) --*

                    The size of the cache on the source cache node.

                  - **CacheNodeCreateTime** *(datetime) --*

                    The date and time when the cache node was created in the source cluster.

                  - **SnapshotCreateTime** *(datetime) --*

                    The date and time when the source node's metadata and cache data set was obtained for
                    the snapshot.

              - **KmsKeyId** *(string) --*

                The ID of the KMS key used to encrypt the snapshot.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_cache_clusters(
        self,
        CacheClusterId: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        ShowCacheNodeInfo: bool = None,
        ShowCacheClustersNotInReplicationGroups: bool = None,
    ) -> ClientDescribeCacheClustersResponseTypeDef:
        """
        Returns information about all provisioned clusters if no cluster identifier is specified, or about
        a specific cache cluster if a cluster identifier is supplied.

        By default, abbreviated information about the clusters is returned. You can use the optional
        *ShowCacheNodeInfo* flag to retrieve detailed information about the cache nodes associated with the
        clusters. These details include the DNS address and port for the cache node endpoint.

        If the cluster is in the *creating* state, only cluster-level information is displayed until all of
        the nodes are successfully provisioned.

        If the cluster is in the *deleting* state, only cluster-level information is displayed.

        If cache nodes are currently being added to the cluster, node endpoint information and creation
        time for the additional nodes are not displayed until they are completely provisioned. When the
        cluster state is *available* , the cluster is ready for use.

        If cache nodes are currently being removed from the cluster, no endpoint information for the
        removed nodes is displayed.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/DescribeCacheClusters>`_

        **Request Syntax**
        ::

          response = client.describe_cache_clusters(
              CacheClusterId='string',
              MaxRecords=123,
              Marker='string',
              ShowCacheNodeInfo=True|False,
              ShowCacheClustersNotInReplicationGroups=True|False
          )
        :type CacheClusterId: string
        :param CacheClusterId:

          The user-supplied cluster identifier. If this parameter is specified, only information about that
          specific cluster is returned. This parameter isn't case sensitive.

        :type MaxRecords: integer
        :param MaxRecords:

          The maximum number of records to include in the response. If more records exist than the
          specified ``MaxRecords`` value, a marker is included in the response so that the remaining
          results can be retrieved.

          Default: 100

          Constraints: minimum 20; maximum 100.

        :type Marker: string
        :param Marker:

          An optional marker returned from a prior request. Use this marker for pagination of results from
          this operation. If this parameter is specified, the response includes only records beyond the
          marker, up to the value specified by ``MaxRecords`` .

        :type ShowCacheNodeInfo: boolean
        :param ShowCacheNodeInfo:

          An optional flag that can be included in the ``DescribeCacheCluster`` request to retrieve
          information about the individual cache nodes.

        :type ShowCacheClustersNotInReplicationGroups: boolean
        :param ShowCacheClustersNotInReplicationGroups:

          An optional flag that can be included in the ``DescribeCacheCluster`` request to show only nodes
          (API/CLI: clusters) that are not members of a replication group. In practice, this mean Memcached
          and single node Redis clusters.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Marker': 'string',
                'CacheClusters': [
                    {
                        'CacheClusterId': 'string',
                        'ConfigurationEndpoint': {
                            'Address': 'string',
                            'Port': 123
                        },
                        'ClientDownloadLandingPage': 'string',
                        'CacheNodeType': 'string',
                        'Engine': 'string',
                        'EngineVersion': 'string',
                        'CacheClusterStatus': 'string',
                        'NumCacheNodes': 123,
                        'PreferredAvailabilityZone': 'string',
                        'CacheClusterCreateTime': datetime(2015, 1, 1),
                        'PreferredMaintenanceWindow': 'string',
                        'PendingModifiedValues': {
                            'NumCacheNodes': 123,
                            'CacheNodeIdsToRemove': [
                                'string',
                            ],
                            'EngineVersion': 'string',
                            'CacheNodeType': 'string',
                            'AuthTokenStatus': 'SETTING'|'ROTATING'
                        },
                        'NotificationConfiguration': {
                            'TopicArn': 'string',
                            'TopicStatus': 'string'
                        },
                        'CacheSecurityGroups': [
                            {
                                'CacheSecurityGroupName': 'string',
                                'Status': 'string'
                            },
                        ],
                        'CacheParameterGroup': {
                            'CacheParameterGroupName': 'string',
                            'ParameterApplyStatus': 'string',
                            'CacheNodeIdsToReboot': [
                                'string',
                            ]
                        },
                        'CacheSubnetGroupName': 'string',
                        'CacheNodes': [
                            {
                                'CacheNodeId': 'string',
                                'CacheNodeStatus': 'string',
                                'CacheNodeCreateTime': datetime(2015, 1, 1),
                                'Endpoint': {
                                    'Address': 'string',
                                    'Port': 123
                                },
                                'ParameterGroupStatus': 'string',
                                'SourceCacheNodeId': 'string',
                                'CustomerAvailabilityZone': 'string'
                            },
                        ],
                        'AutoMinorVersionUpgrade': True|False,
                        'SecurityGroups': [
                            {
                                'SecurityGroupId': 'string',
                                'Status': 'string'
                            },
                        ],
                        'ReplicationGroupId': 'string',
                        'SnapshotRetentionLimit': 123,
                        'SnapshotWindow': 'string',
                        'AuthTokenEnabled': True|False,
                        'AuthTokenLastModifiedDate': datetime(2015, 1, 1),
                        'TransitEncryptionEnabled': True|False,
                        'AtRestEncryptionEnabled': True|False
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            Represents the output of a ``DescribeCacheClusters`` operation.

            - **Marker** *(string) --*

              Provides an identifier to allow retrieval of paginated results.

            - **CacheClusters** *(list) --*

              A list of clusters. Each item in the list contains detailed information about one cluster.

              - *(dict) --*

                Contains all of the attributes of a specific cluster.

                - **CacheClusterId** *(string) --*

                  The user-supplied identifier of the cluster. This identifier is a unique key that
                  identifies a cluster.

                - **ConfigurationEndpoint** *(dict) --*

                  Represents a Memcached cluster endpoint which, if Automatic Discovery is enabled on the
                  cluster, can be used by an application to connect to any node in the cluster. The
                  configuration endpoint will always have ``.cfg`` in it.

                  Example: ``mem-3.9dvc4r.cfg.usw2.cache.amazonaws.com:11211``

                  - **Address** *(string) --*

                    The DNS hostname of the cache node.

                  - **Port** *(integer) --*

                    The port number that the cache engine is listening on.

                - **ClientDownloadLandingPage** *(string) --*

                  The URL of the web page where you can download the latest ElastiCache client library.

                - **CacheNodeType** *(string) --*

                  The name of the compute and memory capacity node type for the cluster.

                  The following node types are supported by ElastiCache. Generally speaking, the current
                  generation types provide more memory and computational power at lower cost when compared
                  to their equivalent previous generation counterparts.

                  * General purpose:

                    * Current generation:   **M5 node types:**  ``cache.m5.large`` , ``cache.m5.xlarge`` ,
                    ``cache.m5.2xlarge`` , ``cache.m5.4xlarge`` , ``cache.m5.12xlarge`` ,
                    ``cache.m5.24xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` ,
                    ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``    **T2 node
                    types:**  ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``

                    * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``
                    **M1 node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` ,
                    ``cache.m1.xlarge``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` ,
                    ``cache.m3.xlarge`` , ``cache.m3.2xlarge``

                  * Compute optimized:

                    * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``

                  * Memory optimized:

                    * Current generation:   **R5 node types:**  ``cache.r5.large`` , ``cache.r5.xlarge`` ,
                    ``cache.r5.2xlarge`` , ``cache.r5.4xlarge`` , ``cache.r5.12xlarge`` ,
                    ``cache.r5.24xlarge``    **R4 node types:**  ``cache.r4.large`` , ``cache.r4.xlarge`` ,
                    ``cache.r4.2xlarge`` , ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` ,
                    ``cache.r4.16xlarge``

                    * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` ,
                    ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``    **R3 node types:**  ``cache.r3.large`` ,
                    ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``

                   **Additional node type info**

                  * All current generation instance types are created in Amazon VPC by default.

                  * Redis append-only files (AOF) are not supported for T1 or T2 instances.

                  * Redis Multi-AZ with automatic failover is not supported on T1 instances.

                  * Redis configuration variables ``appendonly`` and ``appendfsync`` are not supported on
                  Redis version 2.8.22 and later.

                - **Engine** *(string) --*

                  The name of the cache engine (``memcached`` or ``redis`` ) to be used for this cluster.

                - **EngineVersion** *(string) --*

                  The version of the cache engine that is used in this cluster.

                - **CacheClusterStatus** *(string) --*

                  The current state of this cluster, one of the following values: ``available`` ,
                  ``creating`` , ``deleted`` , ``deleting`` , ``incompatible-network`` , ``modifying`` ,
                  ``rebooting cluster nodes`` , ``restore-failed`` , or ``snapshotting`` .

                - **NumCacheNodes** *(integer) --*

                  The number of cache nodes in the cluster.

                  For clusters running Redis, this value must be 1. For clusters running Memcached, this
                  value must be between 1 and 20.

                - **PreferredAvailabilityZone** *(string) --*

                  The name of the Availability Zone in which the cluster is located or "Multiple" if the
                  cache nodes are located in different Availability Zones.

                - **CacheClusterCreateTime** *(datetime) --*

                  The date and time when the cluster was created.

                - **PreferredMaintenanceWindow** *(string) --*

                  Specifies the weekly time range during which maintenance on the cluster is performed. It
                  is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The
                  minimum maintenance window is a 60 minute period.

                  Valid values for ``ddd`` are:

                  * ``sun``

                  * ``mon``

                  * ``tue``

                  * ``wed``

                  * ``thu``

                  * ``fri``

                  * ``sat``

                  Example: ``sun:23:00-mon:01:30``

                - **PendingModifiedValues** *(dict) --*

                  A group of settings that are applied to the cluster in the future, or that are currently
                  being applied.

                  - **NumCacheNodes** *(integer) --*

                    The new number of cache nodes for the cluster.

                    For clusters running Redis, this value must be 1. For clusters running Memcached, this
                    value must be between 1 and 20.

                  - **CacheNodeIdsToRemove** *(list) --*

                    A list of cache node IDs that are being removed (or will be removed) from the cluster.
                    A node ID is a 4-digit numeric identifier (0001, 0002, etc.).

                    - *(string) --*

                  - **EngineVersion** *(string) --*

                    The new cache engine version that the cluster runs.

                  - **CacheNodeType** *(string) --*

                    The cache node type that this cluster or replication group is scaled to.

                  - **AuthTokenStatus** *(string) --*

                    The auth token status

                - **NotificationConfiguration** *(dict) --*

                  Describes a notification topic and its status. Notification topics are used for
                  publishing ElastiCache events to subscribers using Amazon Simple Notification Service
                  (SNS).

                  - **TopicArn** *(string) --*

                    The Amazon Resource Name (ARN) that identifies the topic.

                  - **TopicStatus** *(string) --*

                    The current state of the topic.

                - **CacheSecurityGroups** *(list) --*

                  A list of cache security group elements, composed of name and status sub-elements.

                  - *(dict) --*

                    Represents a cluster's status within a particular cache security group.

                    - **CacheSecurityGroupName** *(string) --*

                      The name of the cache security group.

                    - **Status** *(string) --*

                      The membership status in the cache security group. The status changes when a cache
                      security group is modified, or when the cache security groups assigned to a cluster
                      are modified.

                - **CacheParameterGroup** *(dict) --*

                  Status of the cache parameter group.

                  - **CacheParameterGroupName** *(string) --*

                    The name of the cache parameter group.

                  - **ParameterApplyStatus** *(string) --*

                    The status of parameter updates.

                  - **CacheNodeIdsToReboot** *(list) --*

                    A list of the cache node IDs which need to be rebooted for parameter changes to be
                    applied. A node ID is a numeric identifier (0001, 0002, etc.).

                    - *(string) --*

                - **CacheSubnetGroupName** *(string) --*

                  The name of the cache subnet group associated with the cluster.

                - **CacheNodes** *(list) --*

                  A list of cache nodes that are members of the cluster.

                  - *(dict) --*

                    Represents an individual cache node within a cluster. Each cache node runs its own
                    instance of the cluster's protocol-compliant caching software - either Memcached or
                    Redis.

                    The following node types are supported by ElastiCache. Generally speaking, the current
                    generation types provide more memory and computational power at lower cost when
                    compared to their equivalent previous generation counterparts.

                    * General purpose:

                      * Current generation:   **M5 node types:**  ``cache.m5.large`` , ``cache.m5.xlarge``
                      , ``cache.m5.2xlarge`` , ``cache.m5.4xlarge`` , ``cache.m5.12xlarge`` ,
                      ``cache.m5.24xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge``
                      , ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``    **T2 node
                      types:**  ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``

                      * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``
                      **M1 node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` ,
                      ``cache.m1.xlarge``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` ,
                      ``cache.m3.xlarge`` , ``cache.m3.2xlarge``

                    * Compute optimized:

                      * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``

                    * Memory optimized:

                      * Current generation:   **R5 node types:**  ``cache.r5.large`` , ``cache.r5.xlarge``
                      , ``cache.r5.2xlarge`` , ``cache.r5.4xlarge`` , ``cache.r5.12xlarge`` ,
                      ``cache.r5.24xlarge``    **R4 node types:**  ``cache.r4.large`` , ``cache.r4.xlarge``
                      , ``cache.r4.2xlarge`` , ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` ,
                      ``cache.r4.16xlarge``

                      * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` ,
                      ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``    **R3 node types:**  ``cache.r3.large``
                      , ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` ,
                      ``cache.r3.8xlarge``

                     **Additional node type info**

                    * All current generation instance types are created in Amazon VPC by default.

                    * Redis append-only files (AOF) are not supported for T1 or T2 instances.

                    * Redis Multi-AZ with automatic failover is not supported on T1 instances.

                    * Redis configuration variables ``appendonly`` and ``appendfsync`` are not supported on
                    Redis version 2.8.22 and later.

                    - **CacheNodeId** *(string) --*

                      The cache node identifier. A node ID is a numeric identifier (0001, 0002, etc.). The
                      combination of cluster ID and node ID uniquely identifies every cache node used in a
                      customer's AWS account.

                    - **CacheNodeStatus** *(string) --*

                      The current state of this cache node.

                    - **CacheNodeCreateTime** *(datetime) --*

                      The date and time when the cache node was created.

                    - **Endpoint** *(dict) --*

                      The hostname for connecting to this cache node.

                      - **Address** *(string) --*

                        The DNS hostname of the cache node.

                      - **Port** *(integer) --*

                        The port number that the cache engine is listening on.

                    - **ParameterGroupStatus** *(string) --*

                      The status of the parameter group applied to this cache node.

                    - **SourceCacheNodeId** *(string) --*

                      The ID of the primary node to which this read replica node is synchronized. If this
                      field is empty, this node is not associated with a primary cluster.

                    - **CustomerAvailabilityZone** *(string) --*

                      The Availability Zone where this node was created and now resides.

                - **AutoMinorVersionUpgrade** *(boolean) --*

                  This parameter is currently disabled.

                - **SecurityGroups** *(list) --*

                  A list of VPC Security Groups associated with the cluster.

                  - *(dict) --*

                    Represents a single cache security group and its status.

                    - **SecurityGroupId** *(string) --*

                      The identifier of the cache security group.

                    - **Status** *(string) --*

                      The status of the cache security group membership. The status changes whenever a
                      cache security group is modified, or when the cache security groups assigned to a
                      cluster are modified.

                - **ReplicationGroupId** *(string) --*

                  The replication group to which this cluster belongs. If this field is empty, the cluster
                  is not associated with any replication group.

                - **SnapshotRetentionLimit** *(integer) --*

                  The number of days for which ElastiCache retains automatic cluster snapshots before
                  deleting them. For example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot that
                  was taken today is retained for 5 days before being deleted.

                  .. warning::

                    If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.

                - **SnapshotWindow** *(string) --*

                  The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of
                  your cluster.

                  Example: ``05:00-09:00``

                - **AuthTokenEnabled** *(boolean) --*

                  A flag that enables using an ``AuthToken`` (password) when issuing Redis commands.

                  Default: ``false``

                - **AuthTokenLastModifiedDate** *(datetime) --*

                  The date the auth token was last modified

                - **TransitEncryptionEnabled** *(boolean) --*

                  A flag that enables in-transit encryption when set to ``true`` .

                  You cannot modify the value of ``TransitEncryptionEnabled`` after the cluster is created.
                  To enable in-transit encryption on a cluster you must set ``TransitEncryptionEnabled`` to
                  ``true`` when you create a cluster.

                   **Required:** Only available when creating a replication group in an Amazon VPC using
                   redis version ``3.2.6`` , ``4.x`` or later.

                  Default: ``false``

                - **AtRestEncryptionEnabled** *(boolean) --*

                  A flag that enables encryption at-rest when set to ``true`` .

                  You cannot modify the value of ``AtRestEncryptionEnabled`` after the cluster is created.
                  To enable at-rest encryption on a cluster you must set ``AtRestEncryptionEnabled`` to
                  ``true`` when you create a cluster.

                   **Required:** Only available when creating a replication group in an Amazon VPC using
                   redis version ``3.2.6`` , ``4.x`` or later.

                  Default: ``false``

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_cache_engine_versions(
        self,
        Engine: str = None,
        EngineVersion: str = None,
        CacheParameterGroupFamily: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        DefaultOnly: bool = None,
    ) -> ClientDescribeCacheEngineVersionsResponseTypeDef:
        """
        Returns a list of the available cache engines and their versions.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/DescribeCacheEngineVersions>`_

        **Request Syntax**
        ::

          response = client.describe_cache_engine_versions(
              Engine='string',
              EngineVersion='string',
              CacheParameterGroupFamily='string',
              MaxRecords=123,
              Marker='string',
              DefaultOnly=True|False
          )
        :type Engine: string
        :param Engine:

          The cache engine to return. Valid values: ``memcached`` | ``redis``

        :type EngineVersion: string
        :param EngineVersion:

          The cache engine version to return.

          Example: ``1.4.14``

        :type CacheParameterGroupFamily: string
        :param CacheParameterGroupFamily:

          The name of a specific cache parameter group family to return details for.

          Valid values are: ``memcached1.4`` | ``memcached1.5`` | ``redis2.6`` | ``redis2.8`` |
          ``redis3.2`` | ``redis4.0`` | ``redis5.0`` |

          Constraints:

          * Must be 1 to 255 alphanumeric characters

          * First character must be a letter

          * Cannot end with a hyphen or contain two consecutive hyphens

        :type MaxRecords: integer
        :param MaxRecords:

          The maximum number of records to include in the response. If more records exist than the
          specified ``MaxRecords`` value, a marker is included in the response so that the remaining
          results can be retrieved.

          Default: 100

          Constraints: minimum 20; maximum 100.

        :type Marker: string
        :param Marker:

          An optional marker returned from a prior request. Use this marker for pagination of results from
          this operation. If this parameter is specified, the response includes only records beyond the
          marker, up to the value specified by ``MaxRecords`` .

        :type DefaultOnly: boolean
        :param DefaultOnly:

          If ``true`` , specifies that only the default version of the specified engine or engine and major
          version combination is to be returned.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Marker': 'string',
                'CacheEngineVersions': [
                    {
                        'Engine': 'string',
                        'EngineVersion': 'string',
                        'CacheParameterGroupFamily': 'string',
                        'CacheEngineDescription': 'string',
                        'CacheEngineVersionDescription': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            Represents the output of a  DescribeCacheEngineVersions operation.

            - **Marker** *(string) --*

              Provides an identifier to allow retrieval of paginated results.

            - **CacheEngineVersions** *(list) --*

              A list of cache engine version details. Each element in the list contains detailed
              information about one cache engine version.

              - *(dict) --*

                Provides all of the details about a particular cache engine version.

                - **Engine** *(string) --*

                  The name of the cache engine.

                - **EngineVersion** *(string) --*

                  The version number of the cache engine.

                - **CacheParameterGroupFamily** *(string) --*

                  The name of the cache parameter group family associated with this cache engine.

                  Valid values are: ``memcached1.4`` | ``memcached1.5`` | ``redis2.6`` | ``redis2.8`` |
                  ``redis3.2`` | ``redis4.0`` | ``redis5.0`` |

                - **CacheEngineDescription** *(string) --*

                  The description of the cache engine.

                - **CacheEngineVersionDescription** *(string) --*

                  The description of the cache engine version.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_cache_parameter_groups(
        self,
        CacheParameterGroupName: str = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ClientDescribeCacheParameterGroupsResponseTypeDef:
        """
        Returns a list of cache parameter group descriptions. If a cache parameter group name is specified,
        the list contains only the descriptions for that group.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/DescribeCacheParameterGroups>`_

        **Request Syntax**
        ::

          response = client.describe_cache_parameter_groups(
              CacheParameterGroupName='string',
              MaxRecords=123,
              Marker='string'
          )
        :type CacheParameterGroupName: string
        :param CacheParameterGroupName:

          The name of a specific cache parameter group to return details for.

        :type MaxRecords: integer
        :param MaxRecords:

          The maximum number of records to include in the response. If more records exist than the
          specified ``MaxRecords`` value, a marker is included in the response so that the remaining
          results can be retrieved.

          Default: 100

          Constraints: minimum 20; maximum 100.

        :type Marker: string
        :param Marker:

          An optional marker returned from a prior request. Use this marker for pagination of results from
          this operation. If this parameter is specified, the response includes only records beyond the
          marker, up to the value specified by ``MaxRecords`` .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Marker': 'string',
                'CacheParameterGroups': [
                    {
                        'CacheParameterGroupName': 'string',
                        'CacheParameterGroupFamily': 'string',
                        'Description': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            Represents the output of a ``DescribeCacheParameterGroups`` operation.

            - **Marker** *(string) --*

              Provides an identifier to allow retrieval of paginated results.

            - **CacheParameterGroups** *(list) --*

              A list of cache parameter groups. Each element in the list contains detailed information
              about one cache parameter group.

              - *(dict) --*

                Represents the output of a ``CreateCacheParameterGroup`` operation.

                - **CacheParameterGroupName** *(string) --*

                  The name of the cache parameter group.

                - **CacheParameterGroupFamily** *(string) --*

                  The name of the cache parameter group family that this cache parameter group is
                  compatible with.

                  Valid values are: ``memcached1.4`` | ``memcached1.5`` | ``redis2.6`` | ``redis2.8`` |
                  ``redis3.2`` | ``redis4.0`` | ``redis5.0`` |

                - **Description** *(string) --*

                  The description for this cache parameter group.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_cache_parameters(
        self,
        CacheParameterGroupName: str,
        Source: str = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ClientDescribeCacheParametersResponseTypeDef:
        """
        Returns the detailed parameter list for a particular cache parameter group.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/DescribeCacheParameters>`_

        **Request Syntax**
        ::

          response = client.describe_cache_parameters(
              CacheParameterGroupName='string',
              Source='string',
              MaxRecords=123,
              Marker='string'
          )
        :type CacheParameterGroupName: string
        :param CacheParameterGroupName: **[REQUIRED]**

          The name of a specific cache parameter group to return details for.

        :type Source: string
        :param Source:

          The parameter types to return.

          Valid values: ``user`` | ``system`` | ``engine-default``

        :type MaxRecords: integer
        :param MaxRecords:

          The maximum number of records to include in the response. If more records exist than the
          specified ``MaxRecords`` value, a marker is included in the response so that the remaining
          results can be retrieved.

          Default: 100

          Constraints: minimum 20; maximum 100.

        :type Marker: string
        :param Marker:

          An optional marker returned from a prior request. Use this marker for pagination of results from
          this operation. If this parameter is specified, the response includes only records beyond the
          marker, up to the value specified by ``MaxRecords`` .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Marker': 'string',
                'Parameters': [
                    {
                        'ParameterName': 'string',
                        'ParameterValue': 'string',
                        'Description': 'string',
                        'Source': 'string',
                        'DataType': 'string',
                        'AllowedValues': 'string',
                        'IsModifiable': True|False,
                        'MinimumEngineVersion': 'string',
                        'ChangeType': 'immediate'|'requires-reboot'
                    },
                ],
                'CacheNodeTypeSpecificParameters': [
                    {
                        'ParameterName': 'string',
                        'Description': 'string',
                        'Source': 'string',
                        'DataType': 'string',
                        'AllowedValues': 'string',
                        'IsModifiable': True|False,
                        'MinimumEngineVersion': 'string',
                        'CacheNodeTypeSpecificValues': [
                            {
                                'CacheNodeType': 'string',
                                'Value': 'string'
                            },
                        ],
                        'ChangeType': 'immediate'|'requires-reboot'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            Represents the output of a ``DescribeCacheParameters`` operation.

            - **Marker** *(string) --*

              Provides an identifier to allow retrieval of paginated results.

            - **Parameters** *(list) --*

              A list of  Parameter instances.

              - *(dict) --*

                Describes an individual setting that controls some aspect of ElastiCache behavior.

                - **ParameterName** *(string) --*

                  The name of the parameter.

                - **ParameterValue** *(string) --*

                  The value of the parameter.

                - **Description** *(string) --*

                  A description of the parameter.

                - **Source** *(string) --*

                  The source of the parameter.

                - **DataType** *(string) --*

                  The valid data type for the parameter.

                - **AllowedValues** *(string) --*

                  The valid range of values for the parameter.

                - **IsModifiable** *(boolean) --*

                  Indicates whether (``true`` ) or not (``false`` ) the parameter can be modified. Some
                  parameters have security or operational implications that prevent them from being changed.

                - **MinimumEngineVersion** *(string) --*

                  The earliest cache engine version to which the parameter can apply.

                - **ChangeType** *(string) --*

                  Indicates whether a change to the parameter is applied immediately or requires a reboot
                  for the change to be applied. You can force a reboot or wait until the next maintenance
                  window's reboot. For more information, see `Rebooting a Cluster
                  <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Clusters.Rebooting.html>`__ .

            - **CacheNodeTypeSpecificParameters** *(list) --*

              A list of parameters specific to a particular cache node type. Each element in the list
              contains detailed information about one parameter.

              - *(dict) --*

                A parameter that has a different value for each cache node type it is applied to. For
                example, in a Redis cluster, a ``cache.m1.large`` cache node type would have a larger
                ``maxmemory`` value than a ``cache.m1.small`` type.

                - **ParameterName** *(string) --*

                  The name of the parameter.

                - **Description** *(string) --*

                  A description of the parameter.

                - **Source** *(string) --*

                  The source of the parameter value.

                - **DataType** *(string) --*

                  The valid data type for the parameter.

                - **AllowedValues** *(string) --*

                  The valid range of values for the parameter.

                - **IsModifiable** *(boolean) --*

                  Indicates whether (``true`` ) or not (``false`` ) the parameter can be modified. Some
                  parameters have security or operational implications that prevent them from being changed.

                - **MinimumEngineVersion** *(string) --*

                  The earliest cache engine version to which the parameter can apply.

                - **CacheNodeTypeSpecificValues** *(list) --*

                  A list of cache node types and their corresponding values for this parameter.

                  - *(dict) --*

                    A value that applies only to a certain cache node type.

                    - **CacheNodeType** *(string) --*

                      The cache node type for which this value applies.

                    - **Value** *(string) --*

                      The value for the cache node type.

                - **ChangeType** *(string) --*

                  Indicates whether a change to the parameter is applied immediately or requires a reboot
                  for the change to be applied. You can force a reboot or wait until the next maintenance
                  window's reboot. For more information, see `Rebooting a Cluster
                  <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Clusters.Rebooting.html>`__ .

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_cache_security_groups(
        self,
        CacheSecurityGroupName: str = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ClientDescribeCacheSecurityGroupsResponseTypeDef:
        """
        Returns a list of cache security group descriptions. If a cache security group name is specified,
        the list contains only the description of that group. This applicable only when you have
        ElastiCache in Classic setup

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/DescribeCacheSecurityGroups>`_

        **Request Syntax**
        ::

          response = client.describe_cache_security_groups(
              CacheSecurityGroupName='string',
              MaxRecords=123,
              Marker='string'
          )
        :type CacheSecurityGroupName: string
        :param CacheSecurityGroupName:

          The name of the cache security group to return details for.

        :type MaxRecords: integer
        :param MaxRecords:

          The maximum number of records to include in the response. If more records exist than the
          specified ``MaxRecords`` value, a marker is included in the response so that the remaining
          results can be retrieved.

          Default: 100

          Constraints: minimum 20; maximum 100.

        :type Marker: string
        :param Marker:

          An optional marker returned from a prior request. Use this marker for pagination of results from
          this operation. If this parameter is specified, the response includes only records beyond the
          marker, up to the value specified by ``MaxRecords`` .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Marker': 'string',
                'CacheSecurityGroups': [
                    {
                        'OwnerId': 'string',
                        'CacheSecurityGroupName': 'string',
                        'Description': 'string',
                        'EC2SecurityGroups': [
                            {
                                'Status': 'string',
                                'EC2SecurityGroupName': 'string',
                                'EC2SecurityGroupOwnerId': 'string'
                            },
                        ]
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            Represents the output of a ``DescribeCacheSecurityGroups`` operation.

            - **Marker** *(string) --*

              Provides an identifier to allow retrieval of paginated results.

            - **CacheSecurityGroups** *(list) --*

              A list of cache security groups. Each element in the list contains detailed information about
              one group.

              - *(dict) --*

                Represents the output of one of the following operations:

                * ``AuthorizeCacheSecurityGroupIngress``

                * ``CreateCacheSecurityGroup``

                * ``RevokeCacheSecurityGroupIngress``

                - **OwnerId** *(string) --*

                  The AWS account ID of the cache security group owner.

                - **CacheSecurityGroupName** *(string) --*

                  The name of the cache security group.

                - **Description** *(string) --*

                  The description of the cache security group.

                - **EC2SecurityGroups** *(list) --*

                  A list of Amazon EC2 security groups that are associated with this cache security group.

                  - *(dict) --*

                    Provides ownership and status information for an Amazon EC2 security group.

                    - **Status** *(string) --*

                      The status of the Amazon EC2 security group.

                    - **EC2SecurityGroupName** *(string) --*

                      The name of the Amazon EC2 security group.

                    - **EC2SecurityGroupOwnerId** *(string) --*

                      The AWS account ID of the Amazon EC2 security group owner.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_cache_subnet_groups(
        self,
        CacheSubnetGroupName: str = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ClientDescribeCacheSubnetGroupsResponseTypeDef:
        """
        Returns a list of cache subnet group descriptions. If a subnet group name is specified, the list
        contains only the description of that group. This is applicable only when you have ElastiCache in
        VPC setup. All ElastiCache clusters now launch in VPC by default.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/DescribeCacheSubnetGroups>`_

        **Request Syntax**
        ::

          response = client.describe_cache_subnet_groups(
              CacheSubnetGroupName='string',
              MaxRecords=123,
              Marker='string'
          )
        :type CacheSubnetGroupName: string
        :param CacheSubnetGroupName:

          The name of the cache subnet group to return details for.

        :type MaxRecords: integer
        :param MaxRecords:

          The maximum number of records to include in the response. If more records exist than the
          specified ``MaxRecords`` value, a marker is included in the response so that the remaining
          results can be retrieved.

          Default: 100

          Constraints: minimum 20; maximum 100.

        :type Marker: string
        :param Marker:

          An optional marker returned from a prior request. Use this marker for pagination of results from
          this operation. If this parameter is specified, the response includes only records beyond the
          marker, up to the value specified by ``MaxRecords`` .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Marker': 'string',
                'CacheSubnetGroups': [
                    {
                        'CacheSubnetGroupName': 'string',
                        'CacheSubnetGroupDescription': 'string',
                        'VpcId': 'string',
                        'Subnets': [
                            {
                                'SubnetIdentifier': 'string',
                                'SubnetAvailabilityZone': {
                                    'Name': 'string'
                                }
                            },
                        ]
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            Represents the output of a ``DescribeCacheSubnetGroups`` operation.

            - **Marker** *(string) --*

              Provides an identifier to allow retrieval of paginated results.

            - **CacheSubnetGroups** *(list) --*

              A list of cache subnet groups. Each element in the list contains detailed information about
              one group.

              - *(dict) --*

                Represents the output of one of the following operations:

                * ``CreateCacheSubnetGroup``

                * ``ModifyCacheSubnetGroup``

                - **CacheSubnetGroupName** *(string) --*

                  The name of the cache subnet group.

                - **CacheSubnetGroupDescription** *(string) --*

                  The description of the cache subnet group.

                - **VpcId** *(string) --*

                  The Amazon Virtual Private Cloud identifier (VPC ID) of the cache subnet group.

                - **Subnets** *(list) --*

                  A list of subnets associated with the cache subnet group.

                  - *(dict) --*

                    Represents the subnet associated with a cluster. This parameter refers to subnets
                    defined in Amazon Virtual Private Cloud (Amazon VPC) and used with ElastiCache.

                    - **SubnetIdentifier** *(string) --*

                      The unique identifier for the subnet.

                    - **SubnetAvailabilityZone** *(dict) --*

                      The Availability Zone associated with the subnet.

                      - **Name** *(string) --*

                        The name of the Availability Zone.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_engine_default_parameters(
        self, CacheParameterGroupFamily: str, MaxRecords: int = None, Marker: str = None
    ) -> ClientDescribeEngineDefaultParametersResponseTypeDef:
        """
        Returns the default engine and system parameter information for the specified cache engine.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/DescribeEngineDefaultParameters>`_

        **Request Syntax**
        ::

          response = client.describe_engine_default_parameters(
              CacheParameterGroupFamily='string',
              MaxRecords=123,
              Marker='string'
          )
        :type CacheParameterGroupFamily: string
        :param CacheParameterGroupFamily: **[REQUIRED]**

          The name of the cache parameter group family.

          Valid values are: ``memcached1.4`` | ``memcached1.5`` | ``redis2.6`` | ``redis2.8`` |
          ``redis3.2`` | ``redis4.0`` | ``redis5.0`` |

        :type MaxRecords: integer
        :param MaxRecords:

          The maximum number of records to include in the response. If more records exist than the
          specified ``MaxRecords`` value, a marker is included in the response so that the remaining
          results can be retrieved.

          Default: 100

          Constraints: minimum 20; maximum 100.

        :type Marker: string
        :param Marker:

          An optional marker returned from a prior request. Use this marker for pagination of results from
          this operation. If this parameter is specified, the response includes only records beyond the
          marker, up to the value specified by ``MaxRecords`` .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'EngineDefaults': {
                    'CacheParameterGroupFamily': 'string',
                    'Marker': 'string',
                    'Parameters': [
                        {
                            'ParameterName': 'string',
                            'ParameterValue': 'string',
                            'Description': 'string',
                            'Source': 'string',
                            'DataType': 'string',
                            'AllowedValues': 'string',
                            'IsModifiable': True|False,
                            'MinimumEngineVersion': 'string',
                            'ChangeType': 'immediate'|'requires-reboot'
                        },
                    ],
                    'CacheNodeTypeSpecificParameters': [
                        {
                            'ParameterName': 'string',
                            'Description': 'string',
                            'Source': 'string',
                            'DataType': 'string',
                            'AllowedValues': 'string',
                            'IsModifiable': True|False,
                            'MinimumEngineVersion': 'string',
                            'CacheNodeTypeSpecificValues': [
                                {
                                    'CacheNodeType': 'string',
                                    'Value': 'string'
                                },
                            ],
                            'ChangeType': 'immediate'|'requires-reboot'
                        },
                    ]
                }
            }
          **Response Structure**

          - *(dict) --*

            - **EngineDefaults** *(dict) --*

              Represents the output of a ``DescribeEngineDefaultParameters`` operation.

              - **CacheParameterGroupFamily** *(string) --*

                Specifies the name of the cache parameter group family to which the engine default
                parameters apply.

                Valid values are: ``memcached1.4`` | ``memcached1.5`` | ``redis2.6`` | ``redis2.8`` |
                ``redis3.2`` | ``redis4.0`` | ``redis5.0`` |

              - **Marker** *(string) --*

                Provides an identifier to allow retrieval of paginated results.

              - **Parameters** *(list) --*

                Contains a list of engine default parameters.

                - *(dict) --*

                  Describes an individual setting that controls some aspect of ElastiCache behavior.

                  - **ParameterName** *(string) --*

                    The name of the parameter.

                  - **ParameterValue** *(string) --*

                    The value of the parameter.

                  - **Description** *(string) --*

                    A description of the parameter.

                  - **Source** *(string) --*

                    The source of the parameter.

                  - **DataType** *(string) --*

                    The valid data type for the parameter.

                  - **AllowedValues** *(string) --*

                    The valid range of values for the parameter.

                  - **IsModifiable** *(boolean) --*

                    Indicates whether (``true`` ) or not (``false`` ) the parameter can be modified. Some
                    parameters have security or operational implications that prevent them from being
                    changed.

                  - **MinimumEngineVersion** *(string) --*

                    The earliest cache engine version to which the parameter can apply.

                  - **ChangeType** *(string) --*

                    Indicates whether a change to the parameter is applied immediately or requires a reboot
                    for the change to be applied. You can force a reboot or wait until the next maintenance
                    window's reboot. For more information, see `Rebooting a Cluster
                    <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Clusters.Rebooting.html>`__
                    .

              - **CacheNodeTypeSpecificParameters** *(list) --*

                A list of parameters specific to a particular cache node type. Each element in the list
                contains detailed information about one parameter.

                - *(dict) --*

                  A parameter that has a different value for each cache node type it is applied to. For
                  example, in a Redis cluster, a ``cache.m1.large`` cache node type would have a larger
                  ``maxmemory`` value than a ``cache.m1.small`` type.

                  - **ParameterName** *(string) --*

                    The name of the parameter.

                  - **Description** *(string) --*

                    A description of the parameter.

                  - **Source** *(string) --*

                    The source of the parameter value.

                  - **DataType** *(string) --*

                    The valid data type for the parameter.

                  - **AllowedValues** *(string) --*

                    The valid range of values for the parameter.

                  - **IsModifiable** *(boolean) --*

                    Indicates whether (``true`` ) or not (``false`` ) the parameter can be modified. Some
                    parameters have security or operational implications that prevent them from being
                    changed.

                  - **MinimumEngineVersion** *(string) --*

                    The earliest cache engine version to which the parameter can apply.

                  - **CacheNodeTypeSpecificValues** *(list) --*

                    A list of cache node types and their corresponding values for this parameter.

                    - *(dict) --*

                      A value that applies only to a certain cache node type.

                      - **CacheNodeType** *(string) --*

                        The cache node type for which this value applies.

                      - **Value** *(string) --*

                        The value for the cache node type.

                  - **ChangeType** *(string) --*

                    Indicates whether a change to the parameter is applied immediately or requires a reboot
                    for the change to be applied. You can force a reboot or wait until the next maintenance
                    window's reboot. For more information, see `Rebooting a Cluster
                    <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Clusters.Rebooting.html>`__
                    .

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_events(
        self,
        SourceIdentifier: str = None,
        SourceType: str = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        Duration: int = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ClientDescribeEventsResponseTypeDef:
        """
        Returns events related to clusters, cache security groups, and cache parameter groups. You can
        obtain events specific to a particular cluster, cache security group, or cache parameter group by
        providing the name as a parameter.

        By default, only the events occurring within the last hour are returned; however, you can retrieve
        up to 14 days' worth of events if necessary.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/DescribeEvents>`_

        **Request Syntax**
        ::

          response = client.describe_events(
              SourceIdentifier='string',
              SourceType=
                  'cache-cluster'|'cache-parameter-group'|'cache-security-group'|'cache-subnet-group'
                  |'replication-group',
              StartTime=datetime(2015, 1, 1),
              EndTime=datetime(2015, 1, 1),
              Duration=123,
              MaxRecords=123,
              Marker='string'
          )
        :type SourceIdentifier: string
        :param SourceIdentifier:

          The identifier of the event source for which events are returned. If not specified, all sources
          are included in the response.

        :type SourceType: string
        :param SourceType:

          The event source to retrieve events for. If no value is specified, all events are returned.

        :type StartTime: datetime
        :param StartTime:

          The beginning of the time interval to retrieve events for, specified in ISO 8601 format.

           **Example:** 2017-03-30T07:03:49.555Z

        :type EndTime: datetime
        :param EndTime:

          The end of the time interval for which to retrieve events, specified in ISO 8601 format.

           **Example:** 2017-03-30T07:03:49.555Z

        :type Duration: integer
        :param Duration:

          The number of minutes worth of events to retrieve.

        :type MaxRecords: integer
        :param MaxRecords:

          The maximum number of records to include in the response. If more records exist than the
          specified ``MaxRecords`` value, a marker is included in the response so that the remaining
          results can be retrieved.

          Default: 100

          Constraints: minimum 20; maximum 100.

        :type Marker: string
        :param Marker:

          An optional marker returned from a prior request. Use this marker for pagination of results from
          this operation. If this parameter is specified, the response includes only records beyond the
          marker, up to the value specified by ``MaxRecords`` .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Marker': 'string',
                'Events': [
                    {
                        'SourceIdentifier': 'string',
                        'SourceType':
                        'cache-cluster'|'cache-parameter-group'|'cache-security-group'|'cache-subnet-group'
                        |'replication-group',
                        'Message': 'string',
                        'Date': datetime(2015, 1, 1)
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            Represents the output of a ``DescribeEvents`` operation.

            - **Marker** *(string) --*

              Provides an identifier to allow retrieval of paginated results.

            - **Events** *(list) --*

              A list of events. Each element in the list contains detailed information about one event.

              - *(dict) --*

                Represents a single occurrence of something interesting within the system. Some examples of
                events are creating a cluster, adding or removing a cache node, or rebooting a node.

                - **SourceIdentifier** *(string) --*

                  The identifier for the source of the event. For example, if the event occurred at the
                  cluster level, the identifier would be the name of the cluster.

                - **SourceType** *(string) --*

                  Specifies the origin of this event - a cluster, a parameter group, a security group, etc.

                - **Message** *(string) --*

                  The text of the event.

                - **Date** *(datetime) --*

                  The date and time when the event occurred.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_replication_groups(
        self, ReplicationGroupId: str = None, MaxRecords: int = None, Marker: str = None
    ) -> ClientDescribeReplicationGroupsResponseTypeDef:
        """
        Returns information about a particular replication group. If no identifier is specified,
        ``DescribeReplicationGroups`` returns information about all replication groups.

        .. note::

          This operation is valid for Redis only.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/DescribeReplicationGroups>`_

        **Request Syntax**
        ::

          response = client.describe_replication_groups(
              ReplicationGroupId='string',
              MaxRecords=123,
              Marker='string'
          )
        :type ReplicationGroupId: string
        :param ReplicationGroupId:

          The identifier for the replication group to be described. This parameter is not case sensitive.

          If you do not specify this parameter, information about all replication groups is returned.

        :type MaxRecords: integer
        :param MaxRecords:

          The maximum number of records to include in the response. If more records exist than the
          specified ``MaxRecords`` value, a marker is included in the response so that the remaining
          results can be retrieved.

          Default: 100

          Constraints: minimum 20; maximum 100.

        :type Marker: string
        :param Marker:

          An optional marker returned from a prior request. Use this marker for pagination of results from
          this operation. If this parameter is specified, the response includes only records beyond the
          marker, up to the value specified by ``MaxRecords`` .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Marker': 'string',
                'ReplicationGroups': [
                    {
                        'ReplicationGroupId': 'string',
                        'Description': 'string',
                        'Status': 'string',
                        'PendingModifiedValues': {
                            'PrimaryClusterId': 'string',
                            'AutomaticFailoverStatus': 'enabled'|'disabled',
                            'Resharding': {
                                'SlotMigration': {
                                    'ProgressPercentage': 123.0
                                }
                            },
                            'AuthTokenStatus': 'SETTING'|'ROTATING'
                        },
                        'MemberClusters': [
                            'string',
                        ],
                        'NodeGroups': [
                            {
                                'NodeGroupId': 'string',
                                'Status': 'string',
                                'PrimaryEndpoint': {
                                    'Address': 'string',
                                    'Port': 123
                                },
                                'ReaderEndpoint': {
                                    'Address': 'string',
                                    'Port': 123
                                },
                                'Slots': 'string',
                                'NodeGroupMembers': [
                                    {
                                        'CacheClusterId': 'string',
                                        'CacheNodeId': 'string',
                                        'ReadEndpoint': {
                                            'Address': 'string',
                                            'Port': 123
                                        },
                                        'PreferredAvailabilityZone': 'string',
                                        'CurrentRole': 'string'
                                    },
                                ]
                            },
                        ],
                        'SnapshottingClusterId': 'string',
                        'AutomaticFailover': 'enabled'|'disabled'|'enabling'|'disabling',
                        'ConfigurationEndpoint': {
                            'Address': 'string',
                            'Port': 123
                        },
                        'SnapshotRetentionLimit': 123,
                        'SnapshotWindow': 'string',
                        'ClusterEnabled': True|False,
                        'CacheNodeType': 'string',
                        'AuthTokenEnabled': True|False,
                        'AuthTokenLastModifiedDate': datetime(2015, 1, 1),
                        'TransitEncryptionEnabled': True|False,
                        'AtRestEncryptionEnabled': True|False,
                        'KmsKeyId': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            Represents the output of a ``DescribeReplicationGroups`` operation.

            - **Marker** *(string) --*

              Provides an identifier to allow retrieval of paginated results.

            - **ReplicationGroups** *(list) --*

              A list of replication groups. Each item in the list contains detailed information about one
              replication group.

              - *(dict) --*

                Contains all of the attributes of a specific Redis replication group.

                - **ReplicationGroupId** *(string) --*

                  The identifier for the replication group.

                - **Description** *(string) --*

                  The user supplied description of the replication group.

                - **Status** *(string) --*

                  The current state of this replication group - ``creating`` , ``available`` ,
                  ``modifying`` , ``deleting`` , ``create-failed`` , ``snapshotting`` .

                - **PendingModifiedValues** *(dict) --*

                  A group of settings to be applied to the replication group, either immediately or during
                  the next maintenance window.

                  - **PrimaryClusterId** *(string) --*

                    The primary cluster ID that is applied immediately (if ``--apply-immediately`` was
                    specified), or during the next maintenance window.

                  - **AutomaticFailoverStatus** *(string) --*

                    Indicates the status of Multi-AZ with automatic failover for this Redis replication
                    group.

                    Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

                    * Redis versions earlier than 2.8.6.

                    * Redis (cluster mode disabled): T1 node types.

                    * Redis (cluster mode enabled): T1 node types.

                  - **Resharding** *(dict) --*

                    The status of an online resharding operation.

                    - **SlotMigration** *(dict) --*

                      Represents the progress of an online resharding operation.

                      - **ProgressPercentage** *(float) --*

                        The percentage of the slot migration that is complete.

                  - **AuthTokenStatus** *(string) --*

                    The auth token status

                - **MemberClusters** *(list) --*

                  The names of all the cache clusters that are part of this replication group.

                  - *(string) --*

                - **NodeGroups** *(list) --*

                  A list of node groups in this replication group. For Redis (cluster mode disabled)
                  replication groups, this is a single-element list. For Redis (cluster mode enabled)
                  replication groups, the list contains an entry for each node group (shard).

                  - *(dict) --*

                    Represents a collection of cache nodes in a replication group. One node in the node
                    group is the read/write primary node. All the other nodes are read-only Replica nodes.

                    - **NodeGroupId** *(string) --*

                      The identifier for the node group (shard). A Redis (cluster mode disabled)
                      replication group contains only 1 node group; therefore, the node group ID is 0001. A
                      Redis (cluster mode enabled) replication group contains 1 to 90 node groups numbered
                      0001 to 0090. Optionally, the user can provide the id for a node group.

                    - **Status** *(string) --*

                      The current state of this replication group - ``creating`` , ``available`` , etc.

                    - **PrimaryEndpoint** *(dict) --*

                      The endpoint of the primary node in this node group (shard).

                      - **Address** *(string) --*

                        The DNS hostname of the cache node.

                      - **Port** *(integer) --*

                        The port number that the cache engine is listening on.

                    - **ReaderEndpoint** *(dict) --*

                      The endpoint of the replica nodes in this node group (shard).

                      - **Address** *(string) --*

                        The DNS hostname of the cache node.

                      - **Port** *(integer) --*

                        The port number that the cache engine is listening on.

                    - **Slots** *(string) --*

                      The keyspace for this node group (shard).

                    - **NodeGroupMembers** *(list) --*

                      A list containing information about individual nodes within the node group (shard).

                      - *(dict) --*

                        Represents a single node within a node group (shard).

                        - **CacheClusterId** *(string) --*

                          The ID of the cluster to which the node belongs.

                        - **CacheNodeId** *(string) --*

                          The ID of the node within its cluster. A node ID is a numeric identifier (0001,
                          0002, etc.).

                        - **ReadEndpoint** *(dict) --*

                          The information required for client programs to connect to a node for read
                          operations. The read endpoint is only applicable on Redis (cluster mode disabled)
                          clusters.

                          - **Address** *(string) --*

                            The DNS hostname of the cache node.

                          - **Port** *(integer) --*

                            The port number that the cache engine is listening on.

                        - **PreferredAvailabilityZone** *(string) --*

                          The name of the Availability Zone in which the node is located.

                        - **CurrentRole** *(string) --*

                          The role that is currently assigned to the node - ``primary`` or ``replica`` .
                          This member is only applicable for Redis (cluster mode disabled) replication
                          groups.

                - **SnapshottingClusterId** *(string) --*

                  The cluster ID that is used as the daily snapshot source for the replication group.

                - **AutomaticFailover** *(string) --*

                  Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

                  Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

                  * Redis versions earlier than 2.8.6.

                  * Redis (cluster mode disabled): T1 node types.

                  * Redis (cluster mode enabled): T1 node types.

                - **ConfigurationEndpoint** *(dict) --*

                  The configuration endpoint for this replication group. Use the configuration endpoint to
                  connect to this replication group.

                  - **Address** *(string) --*

                    The DNS hostname of the cache node.

                  - **Port** *(integer) --*

                    The port number that the cache engine is listening on.

                - **SnapshotRetentionLimit** *(integer) --*

                  The number of days for which ElastiCache retains automatic cluster snapshots before
                  deleting them. For example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot that
                  was taken today is retained for 5 days before being deleted.

                  .. warning::

                    If the value of ``SnapshotRetentionLimit`` is set to zero (0), backups are turned off.

                - **SnapshotWindow** *(string) --*

                  The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of
                  your node group (shard).

                  Example: ``05:00-09:00``

                  If you do not specify this parameter, ElastiCache automatically chooses an appropriate
                  time range.

                  .. note::

                    This parameter is only valid if the ``Engine`` parameter is ``redis`` .

                - **ClusterEnabled** *(boolean) --*

                  A flag indicating whether or not this replication group is cluster enabled; i.e., whether
                  its data can be partitioned across multiple shards (API/CLI: node groups).

                  Valid values: ``true`` | ``false``

                - **CacheNodeType** *(string) --*

                  The name of the compute and memory capacity node type for each node in the replication
                  group.

                - **AuthTokenEnabled** *(boolean) --*

                  A flag that enables using an ``AuthToken`` (password) when issuing Redis commands.

                  Default: ``false``

                - **AuthTokenLastModifiedDate** *(datetime) --*

                  The date the auth token was last modified

                - **TransitEncryptionEnabled** *(boolean) --*

                  A flag that enables in-transit encryption when set to ``true`` .

                  You cannot modify the value of ``TransitEncryptionEnabled`` after the cluster is created.
                  To enable in-transit encryption on a cluster you must set ``TransitEncryptionEnabled`` to
                  ``true`` when you create a cluster.

                   **Required:** Only available when creating a replication group in an Amazon VPC using
                   redis version ``3.2.6`` , ``4.x`` or later.

                  Default: ``false``

                - **AtRestEncryptionEnabled** *(boolean) --*

                  A flag that enables encryption at-rest when set to ``true`` .

                  You cannot modify the value of ``AtRestEncryptionEnabled`` after the cluster is created.
                  To enable encryption at-rest on a cluster you must set ``AtRestEncryptionEnabled`` to
                  ``true`` when you create a cluster.

                   **Required:** Only available when creating a replication group in an Amazon VPC using
                   redis version ``3.2.6`` , ``4.x`` or later.

                  Default: ``false``

                - **KmsKeyId** *(string) --*

                  The ID of the KMS key used to encrypt the disk in the cluster.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_reserved_cache_nodes(
        self,
        ReservedCacheNodeId: str = None,
        ReservedCacheNodesOfferingId: str = None,
        CacheNodeType: str = None,
        Duration: str = None,
        ProductDescription: str = None,
        OfferingType: str = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> Dict[str, Any]:
        """
        Returns information about reserved cache nodes for this account, or about a specified reserved
        cache node.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/DescribeReservedCacheNodes>`_

        **Request Syntax**
        ::

          response = client.describe_reserved_cache_nodes(
              ReservedCacheNodeId='string',
              ReservedCacheNodesOfferingId='string',
              CacheNodeType='string',
              Duration='string',
              ProductDescription='string',
              OfferingType='string',
              MaxRecords=123,
              Marker='string'
          )
        :type ReservedCacheNodeId: string
        :param ReservedCacheNodeId:

          The reserved cache node identifier filter value. Use this parameter to show only the reservation
          that matches the specified reservation ID.

        :type ReservedCacheNodesOfferingId: string
        :param ReservedCacheNodesOfferingId:

          The offering identifier filter value. Use this parameter to show only purchased reservations
          matching the specified offering identifier.

        :type CacheNodeType: string
        :param CacheNodeType:

          The cache node type filter value. Use this parameter to show only those reservations matching the
          specified cache node type.

          The following node types are supported by ElastiCache. Generally speaking, the current generation
          types provide more memory and computational power at lower cost when compared to their equivalent
          previous generation counterparts.

          * General purpose:

            * Current generation:   **M5 node types:**  ``cache.m5.large`` , ``cache.m5.xlarge`` ,
            ``cache.m5.2xlarge`` , ``cache.m5.4xlarge`` , ``cache.m5.12xlarge`` , ``cache.m5.24xlarge``
            **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` , ``cache.m4.2xlarge`` ,
            ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``    **T2 node types:**  ``cache.t2.micro`` ,
            ``cache.t2.small`` , ``cache.t2.medium``

            * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``    **M1 node
            types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` , ``cache.m1.xlarge``
             **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` , ``cache.m3.xlarge`` ,
             ``cache.m3.2xlarge``

          * Compute optimized:

            * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``

          * Memory optimized:

            * Current generation:   **R5 node types:**  ``cache.r5.large`` , ``cache.r5.xlarge`` ,
            ``cache.r5.2xlarge`` , ``cache.r5.4xlarge`` , ``cache.r5.12xlarge`` , ``cache.r5.24xlarge``
            **R4 node types:**  ``cache.r4.large`` , ``cache.r4.xlarge`` , ``cache.r4.2xlarge`` ,
            ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` , ``cache.r4.16xlarge``

            * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` ,
            ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``    **R3 node types:**  ``cache.r3.large`` ,
            ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``

           **Additional node type info**

          * All current generation instance types are created in Amazon VPC by default.

          * Redis append-only files (AOF) are not supported for T1 or T2 instances.

          * Redis Multi-AZ with automatic failover is not supported on T1 instances.

          * Redis configuration variables ``appendonly`` and ``appendfsync`` are not supported on Redis
          version 2.8.22 and later.

        :type Duration: string
        :param Duration:

          The duration filter value, specified in years or seconds. Use this parameter to show only
          reservations for this duration.

          Valid Values: ``1 | 3 | 31536000 | 94608000``

        :type ProductDescription: string
        :param ProductDescription:

          The product description filter value. Use this parameter to show only those reservations matching
          the specified product description.

        :type OfferingType: string
        :param OfferingType:

          The offering type filter value. Use this parameter to show only the available offerings matching
          the specified offering type.

          Valid values: ``"Light Utilization"|"Medium Utilization"|"Heavy Utilization"``

        :type MaxRecords: integer
        :param MaxRecords:

          The maximum number of records to include in the response. If more records exist than the
          specified ``MaxRecords`` value, a marker is included in the response so that the remaining
          results can be retrieved.

          Default: 100

          Constraints: minimum 20; maximum 100.

        :type Marker: string
        :param Marker:

          An optional marker returned from a prior request. Use this marker for pagination of results from
          this operation. If this parameter is specified, the response includes only records beyond the
          marker, up to the value specified by ``MaxRecords`` .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Marker': 'string',
                'ReservedCacheNodes': [
                    {
                        'ReservedCacheNodeId': 'string',
                        'ReservedCacheNodesOfferingId': 'string',
                        'CacheNodeType': 'string',
                        'StartTime': datetime(2015, 1, 1),
                        'Duration': 123,
                        'FixedPrice': 123.0,
                        'UsagePrice': 123.0,
                        'CacheNodeCount': 123,
                        'ProductDescription': 'string',
                        'OfferingType': 'string',
                        'State': 'string',
                        'RecurringCharges': [
                            {
                                'RecurringChargeAmount': 123.0,
                                'RecurringChargeFrequency': 'string'
                            },
                        ],
                        'ReservationARN': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            Represents the output of a ``DescribeReservedCacheNodes`` operation.

            - **Marker** *(string) --*

              Provides an identifier to allow retrieval of paginated results.

            - **ReservedCacheNodes** *(list) --*

              A list of reserved cache nodes. Each element in the list contains detailed information about
              one node.

              - *(dict) --*

                Represents the output of a ``PurchaseReservedCacheNodesOffering`` operation.

                - **ReservedCacheNodeId** *(string) --*

                  The unique identifier for the reservation.

                - **ReservedCacheNodesOfferingId** *(string) --*

                  The offering identifier.

                - **CacheNodeType** *(string) --*

                  The cache node type for the reserved cache nodes.

                  The following node types are supported by ElastiCache. Generally speaking, the current
                  generation types provide more memory and computational power at lower cost when compared
                  to their equivalent previous generation counterparts.

                  * General purpose:

                    * Current generation:   **M5 node types:**  ``cache.m5.large`` , ``cache.m5.xlarge`` ,
                    ``cache.m5.2xlarge`` , ``cache.m5.4xlarge`` , ``cache.m5.12xlarge`` ,
                    ``cache.m5.24xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` ,
                    ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``    **T2 node
                    types:**  ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``

                    * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``
                    **M1 node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` ,
                    ``cache.m1.xlarge``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` ,
                    ``cache.m3.xlarge`` , ``cache.m3.2xlarge``

                  * Compute optimized:

                    * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``

                  * Memory optimized:

                    * Current generation:   **R5 node types:**  ``cache.r5.large`` , ``cache.r5.xlarge`` ,
                    ``cache.r5.2xlarge`` , ``cache.r5.4xlarge`` , ``cache.r5.12xlarge`` ,
                    ``cache.r5.24xlarge``    **R4 node types:**  ``cache.r4.large`` , ``cache.r4.xlarge`` ,
                    ``cache.r4.2xlarge`` , ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` ,
                    ``cache.r4.16xlarge``

                    * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` ,
                    ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``    **R3 node types:**  ``cache.r3.large`` ,
                    ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``

                   **Additional node type info**

                  * All current generation instance types are created in Amazon VPC by default.

                  * Redis append-only files (AOF) are not supported for T1 or T2 instances.

                  * Redis Multi-AZ with automatic failover is not supported on T1 instances.

                  * Redis configuration variables ``appendonly`` and ``appendfsync`` are not supported on
                  Redis version 2.8.22 and later.

                - **StartTime** *(datetime) --*

                  The time the reservation started.

                - **Duration** *(integer) --*

                  The duration of the reservation in seconds.

                - **FixedPrice** *(float) --*

                  The fixed price charged for this reserved cache node.

                - **UsagePrice** *(float) --*

                  The hourly price charged for this reserved cache node.

                - **CacheNodeCount** *(integer) --*

                  The number of cache nodes that have been reserved.

                - **ProductDescription** *(string) --*

                  The description of the reserved cache node.

                - **OfferingType** *(string) --*

                  The offering type of this reserved cache node.

                - **State** *(string) --*

                  The state of the reserved cache node.

                - **RecurringCharges** *(list) --*

                  The recurring price charged to run this reserved cache node.

                  - *(dict) --*

                    Contains the specific price and frequency of a recurring charges for a reserved cache
                    node, or for a reserved cache node offering.

                    - **RecurringChargeAmount** *(float) --*

                      The monetary amount of the recurring charge.

                    - **RecurringChargeFrequency** *(string) --*

                      The frequency of the recurring charge.

                - **ReservationARN** *(string) --*

                  The Amazon Resource Name (ARN) of the reserved cache node.

                  Example:
                  ``arn:aws:elasticache:us-east-1:123456789012:reserved-instance:ri-2017-03-27-08-33-25-582``
        ``arn:aws:elasticache:us-east-1:123456789012:reserved-instance:ri-2017-03-27-08-33-25-582``

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_reserved_cache_nodes_offerings(
        self,
        ReservedCacheNodesOfferingId: str = None,
        CacheNodeType: str = None,
        Duration: str = None,
        ProductDescription: str = None,
        OfferingType: str = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ClientDescribeReservedCacheNodesOfferingsResponseTypeDef:
        """
        Lists available reserved cache node offerings.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/DescribeReservedCacheNodesOfferings>`_
        <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/DescribeReservedCacheNodesOfferings>`_

        **Request Syntax**
        ::

          response = client.describe_reserved_cache_nodes_offerings(
              ReservedCacheNodesOfferingId='string',
              CacheNodeType='string',
              Duration='string',
              ProductDescription='string',
              OfferingType='string',
              MaxRecords=123,
              Marker='string'
          )
        :type ReservedCacheNodesOfferingId: string
        :param ReservedCacheNodesOfferingId:

          The offering identifier filter value. Use this parameter to show only the available offering that
          matches the specified reservation identifier.

          Example: ``438012d3-4052-4cc7-b2e3-8d3372e0e706``

        :type CacheNodeType: string
        :param CacheNodeType:

          The cache node type filter value. Use this parameter to show only the available offerings
          matching the specified cache node type.

          The following node types are supported by ElastiCache. Generally speaking, the current generation
          types provide more memory and computational power at lower cost when compared to their equivalent
          previous generation counterparts.

          * General purpose:

            * Current generation:   **M5 node types:**  ``cache.m5.large`` , ``cache.m5.xlarge`` ,
            ``cache.m5.2xlarge`` , ``cache.m5.4xlarge`` , ``cache.m5.12xlarge`` , ``cache.m5.24xlarge``
            **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` , ``cache.m4.2xlarge`` ,
            ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``    **T2 node types:**  ``cache.t2.micro`` ,
            ``cache.t2.small`` , ``cache.t2.medium``

            * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``    **M1 node
            types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` , ``cache.m1.xlarge``
             **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` , ``cache.m3.xlarge`` ,
             ``cache.m3.2xlarge``

          * Compute optimized:

            * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``

          * Memory optimized:

            * Current generation:   **R5 node types:**  ``cache.r5.large`` , ``cache.r5.xlarge`` ,
            ``cache.r5.2xlarge`` , ``cache.r5.4xlarge`` , ``cache.r5.12xlarge`` , ``cache.r5.24xlarge``
            **R4 node types:**  ``cache.r4.large`` , ``cache.r4.xlarge`` , ``cache.r4.2xlarge`` ,
            ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` , ``cache.r4.16xlarge``

            * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` ,
            ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``    **R3 node types:**  ``cache.r3.large`` ,
            ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``

           **Additional node type info**

          * All current generation instance types are created in Amazon VPC by default.

          * Redis append-only files (AOF) are not supported for T1 or T2 instances.

          * Redis Multi-AZ with automatic failover is not supported on T1 instances.

          * Redis configuration variables ``appendonly`` and ``appendfsync`` are not supported on Redis
          version 2.8.22 and later.

        :type Duration: string
        :param Duration:

          Duration filter value, specified in years or seconds. Use this parameter to show only
          reservations for a given duration.

          Valid Values: ``1 | 3 | 31536000 | 94608000``

        :type ProductDescription: string
        :param ProductDescription:

          The product description filter value. Use this parameter to show only the available offerings
          matching the specified product description.

        :type OfferingType: string
        :param OfferingType:

          The offering type filter value. Use this parameter to show only the available offerings matching
          the specified offering type.

          Valid Values: ``"Light Utilization"|"Medium Utilization"|"Heavy Utilization"``

        :type MaxRecords: integer
        :param MaxRecords:

          The maximum number of records to include in the response. If more records exist than the
          specified ``MaxRecords`` value, a marker is included in the response so that the remaining
          results can be retrieved.

          Default: 100

          Constraints: minimum 20; maximum 100.

        :type Marker: string
        :param Marker:

          An optional marker returned from a prior request. Use this marker for pagination of results from
          this operation. If this parameter is specified, the response includes only records beyond the
          marker, up to the value specified by ``MaxRecords`` .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Marker': 'string',
                'ReservedCacheNodesOfferings': [
                    {
                        'ReservedCacheNodesOfferingId': 'string',
                        'CacheNodeType': 'string',
                        'Duration': 123,
                        'FixedPrice': 123.0,
                        'UsagePrice': 123.0,
                        'ProductDescription': 'string',
                        'OfferingType': 'string',
                        'RecurringCharges': [
                            {
                                'RecurringChargeAmount': 123.0,
                                'RecurringChargeFrequency': 'string'
                            },
                        ]
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            Represents the output of a ``DescribeReservedCacheNodesOfferings`` operation.

            - **Marker** *(string) --*

              Provides an identifier to allow retrieval of paginated results.

            - **ReservedCacheNodesOfferings** *(list) --*

              A list of reserved cache node offerings. Each element in the list contains detailed
              information about one offering.

              - *(dict) --*

                Describes all of the attributes of a reserved cache node offering.

                - **ReservedCacheNodesOfferingId** *(string) --*

                  A unique identifier for the reserved cache node offering.

                - **CacheNodeType** *(string) --*

                  The cache node type for the reserved cache node.

                  The following node types are supported by ElastiCache. Generally speaking, the current
                  generation types provide more memory and computational power at lower cost when compared
                  to their equivalent previous generation counterparts.

                  * General purpose:

                    * Current generation:   **M5 node types:**  ``cache.m5.large`` , ``cache.m5.xlarge`` ,
                    ``cache.m5.2xlarge`` , ``cache.m5.4xlarge`` , ``cache.m5.12xlarge`` ,
                    ``cache.m5.24xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` ,
                    ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``    **T2 node
                    types:**  ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``

                    * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``
                    **M1 node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` ,
                    ``cache.m1.xlarge``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` ,
                    ``cache.m3.xlarge`` , ``cache.m3.2xlarge``

                  * Compute optimized:

                    * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``

                  * Memory optimized:

                    * Current generation:   **R5 node types:**  ``cache.r5.large`` , ``cache.r5.xlarge`` ,
                    ``cache.r5.2xlarge`` , ``cache.r5.4xlarge`` , ``cache.r5.12xlarge`` ,
                    ``cache.r5.24xlarge``    **R4 node types:**  ``cache.r4.large`` , ``cache.r4.xlarge`` ,
                    ``cache.r4.2xlarge`` , ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` ,
                    ``cache.r4.16xlarge``

                    * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` ,
                    ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``    **R3 node types:**  ``cache.r3.large`` ,
                    ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``

                   **Additional node type info**

                  * All current generation instance types are created in Amazon VPC by default.

                  * Redis append-only files (AOF) are not supported for T1 or T2 instances.

                  * Redis Multi-AZ with automatic failover is not supported on T1 instances.

                  * Redis configuration variables ``appendonly`` and ``appendfsync`` are not supported on
                  Redis version 2.8.22 and later.

                - **Duration** *(integer) --*

                  The duration of the offering. in seconds.

                - **FixedPrice** *(float) --*

                  The fixed price charged for this offering.

                - **UsagePrice** *(float) --*

                  The hourly price charged for this offering.

                - **ProductDescription** *(string) --*

                  The cache engine used by the offering.

                - **OfferingType** *(string) --*

                  The offering type.

                - **RecurringCharges** *(list) --*

                  The recurring price charged to run this reserved cache node.

                  - *(dict) --*

                    Contains the specific price and frequency of a recurring charges for a reserved cache
                    node, or for a reserved cache node offering.

                    - **RecurringChargeAmount** *(float) --*

                      The monetary amount of the recurring charge.

                    - **RecurringChargeFrequency** *(string) --*

                      The frequency of the recurring charge.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_service_updates(
        self,
        ServiceUpdateName: str = None,
        ServiceUpdateStatus: List[str] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ClientDescribeServiceUpdatesResponseTypeDef:
        """
        Returns details of the service updates

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/DescribeServiceUpdates>`_

        **Request Syntax**
        ::

          response = client.describe_service_updates(
              ServiceUpdateName='string',
              ServiceUpdateStatus=[
                  'available'|'cancelled'|'expired',
              ],
              MaxRecords=123,
              Marker='string'
          )
        :type ServiceUpdateName: string
        :param ServiceUpdateName:

          The unique ID of the service update

        :type ServiceUpdateStatus: list
        :param ServiceUpdateStatus:

          The status of the service update

          - *(string) --*

        :type MaxRecords: integer
        :param MaxRecords:

          The maximum number of records to include in the response

        :type Marker: string
        :param Marker:

          An optional marker returned from a prior request. Use this marker for pagination of results from
          this operation. If this parameter is specified, the response includes only records beyond the
          marker, up to the value specified by ``MaxRecords`` .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Marker': 'string',
                'ServiceUpdates': [
                    {
                        'ServiceUpdateName': 'string',
                        'ServiceUpdateReleaseDate': datetime(2015, 1, 1),
                        'ServiceUpdateEndDate': datetime(2015, 1, 1),
                        'ServiceUpdateSeverity': 'critical'|'important'|'medium'|'low',
                        'ServiceUpdateRecommendedApplyByDate': datetime(2015, 1, 1),
                        'ServiceUpdateStatus': 'available'|'cancelled'|'expired',
                        'ServiceUpdateDescription': 'string',
                        'ServiceUpdateType': 'security-update',
                        'Engine': 'string',
                        'EngineVersion': 'string',
                        'AutoUpdateAfterRecommendedApplyByDate': True|False,
                        'EstimatedUpdateTime': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **Marker** *(string) --*

              An optional marker returned from a prior request. Use this marker for pagination of results
              from this operation. If this parameter is specified, the response includes only records
              beyond the marker, up to the value specified by ``MaxRecords`` .

            - **ServiceUpdates** *(list) --*

              A list of service updates

              - *(dict) --*

                An update that you can apply to your Redis clusters.

                - **ServiceUpdateName** *(string) --*

                  The unique ID of the service update

                - **ServiceUpdateReleaseDate** *(datetime) --*

                  The date when the service update is initially available

                - **ServiceUpdateEndDate** *(datetime) --*

                  The date after which the service update is no longer available

                - **ServiceUpdateSeverity** *(string) --*

                  The severity of the service update

                - **ServiceUpdateRecommendedApplyByDate** *(datetime) --*

                  The recommendend date to apply the service update in order to ensure compliance. For
                  information on compliance, see `Self-Service Security Updates for Compliance
                  <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/elasticache-compliance.html#elasticache-compliance-self-service>`__
                  .

                - **ServiceUpdateStatus** *(string) --*

                  The status of the service update

                - **ServiceUpdateDescription** *(string) --*

                  Provides details of the service update

                - **ServiceUpdateType** *(string) --*

                  Reflects the nature of the service update

                - **Engine** *(string) --*

                  The Elasticache engine to which the update applies. Either Redis or Memcached

                - **EngineVersion** *(string) --*

                  The Elasticache engine version to which the update applies. Either Redis or Memcached
                  engine version

                - **AutoUpdateAfterRecommendedApplyByDate** *(boolean) --*

                  Indicates whether the service update will be automatically applied once the recommended
                  apply-by date has expired.

                - **EstimatedUpdateTime** *(string) --*

                  The estimated length of time the service update will take

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_snapshots(
        self,
        ReplicationGroupId: str = None,
        CacheClusterId: str = None,
        SnapshotName: str = None,
        SnapshotSource: str = None,
        Marker: str = None,
        MaxRecords: int = None,
        ShowNodeGroupConfig: bool = None,
    ) -> ClientDescribeSnapshotsResponseTypeDef:
        """
        Returns information about cluster or replication group snapshots. By default, ``DescribeSnapshots``
        lists all of your snapshots; it can optionally describe a single snapshot, or just the snapshots
        associated with a particular cache cluster.

        .. note::

          This operation is valid for Redis only.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/DescribeSnapshots>`_

        **Request Syntax**
        ::

          response = client.describe_snapshots(
              ReplicationGroupId='string',
              CacheClusterId='string',
              SnapshotName='string',
              SnapshotSource='string',
              Marker='string',
              MaxRecords=123,
              ShowNodeGroupConfig=True|False
          )
        :type ReplicationGroupId: string
        :param ReplicationGroupId:

          A user-supplied replication group identifier. If this parameter is specified, only snapshots
          associated with that specific replication group are described.

        :type CacheClusterId: string
        :param CacheClusterId:

          A user-supplied cluster identifier. If this parameter is specified, only snapshots associated
          with that specific cluster are described.

        :type SnapshotName: string
        :param SnapshotName:

          A user-supplied name of the snapshot. If this parameter is specified, only this snapshot are
          described.

        :type SnapshotSource: string
        :param SnapshotSource:

          If set to ``system`` , the output shows snapshots that were automatically created by ElastiCache.
          If set to ``user`` the output shows snapshots that were manually created. If omitted, the output
          shows both automatically and manually created snapshots.

        :type Marker: string
        :param Marker:

          An optional marker returned from a prior request. Use this marker for pagination of results from
          this operation. If this parameter is specified, the response includes only records beyond the
          marker, up to the value specified by ``MaxRecords`` .

        :type MaxRecords: integer
        :param MaxRecords:

          The maximum number of records to include in the response. If more records exist than the
          specified ``MaxRecords`` value, a marker is included in the response so that the remaining
          results can be retrieved.

          Default: 50

          Constraints: minimum 20; maximum 50.

        :type ShowNodeGroupConfig: boolean
        :param ShowNodeGroupConfig:

          A Boolean value which if true, the node group (shard) configuration is included in the snapshot
          description.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Marker': 'string',
                'Snapshots': [
                    {
                        'SnapshotName': 'string',
                        'ReplicationGroupId': 'string',
                        'ReplicationGroupDescription': 'string',
                        'CacheClusterId': 'string',
                        'SnapshotStatus': 'string',
                        'SnapshotSource': 'string',
                        'CacheNodeType': 'string',
                        'Engine': 'string',
                        'EngineVersion': 'string',
                        'NumCacheNodes': 123,
                        'PreferredAvailabilityZone': 'string',
                        'CacheClusterCreateTime': datetime(2015, 1, 1),
                        'PreferredMaintenanceWindow': 'string',
                        'TopicArn': 'string',
                        'Port': 123,
                        'CacheParameterGroupName': 'string',
                        'CacheSubnetGroupName': 'string',
                        'VpcId': 'string',
                        'AutoMinorVersionUpgrade': True|False,
                        'SnapshotRetentionLimit': 123,
                        'SnapshotWindow': 'string',
                        'NumNodeGroups': 123,
                        'AutomaticFailover': 'enabled'|'disabled'|'enabling'|'disabling',
                        'NodeSnapshots': [
                            {
                                'CacheClusterId': 'string',
                                'NodeGroupId': 'string',
                                'CacheNodeId': 'string',
                                'NodeGroupConfiguration': {
                                    'NodeGroupId': 'string',
                                    'Slots': 'string',
                                    'ReplicaCount': 123,
                                    'PrimaryAvailabilityZone': 'string',
                                    'ReplicaAvailabilityZones': [
                                        'string',
                                    ]
                                },
                                'CacheSize': 'string',
                                'CacheNodeCreateTime': datetime(2015, 1, 1),
                                'SnapshotCreateTime': datetime(2015, 1, 1)
                            },
                        ],
                        'KmsKeyId': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            Represents the output of a ``DescribeSnapshots`` operation.

            - **Marker** *(string) --*

              An optional marker returned from a prior request. Use this marker for pagination of results
              from this operation. If this parameter is specified, the response includes only records
              beyond the marker, up to the value specified by ``MaxRecords`` .

            - **Snapshots** *(list) --*

              A list of snapshots. Each item in the list contains detailed information about one snapshot.

              - *(dict) --*

                Represents a copy of an entire Redis cluster as of the time when the snapshot was taken.

                - **SnapshotName** *(string) --*

                  The name of a snapshot. For an automatic snapshot, the name is system-generated. For a
                  manual snapshot, this is the user-provided name.

                - **ReplicationGroupId** *(string) --*

                  The unique identifier of the source replication group.

                - **ReplicationGroupDescription** *(string) --*

                  A description of the source replication group.

                - **CacheClusterId** *(string) --*

                  The user-supplied identifier of the source cluster.

                - **SnapshotStatus** *(string) --*

                  The status of the snapshot. Valid values: ``creating`` | ``available`` | ``restoring`` |
                  ``copying`` | ``deleting`` .

                - **SnapshotSource** *(string) --*

                  Indicates whether the snapshot is from an automatic backup (``automated`` ) or was
                  created manually (``manual`` ).

                - **CacheNodeType** *(string) --*

                  The name of the compute and memory capacity node type for the source cluster.

                  The following node types are supported by ElastiCache. Generally speaking, the current
                  generation types provide more memory and computational power at lower cost when compared
                  to their equivalent previous generation counterparts.

                  * General purpose:

                    * Current generation:   **M5 node types:**  ``cache.m5.large`` , ``cache.m5.xlarge`` ,
                    ``cache.m5.2xlarge`` , ``cache.m5.4xlarge`` , ``cache.m5.12xlarge`` ,
                    ``cache.m5.24xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` ,
                    ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``    **T2 node
                    types:**  ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``

                    * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``
                    **M1 node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` ,
                    ``cache.m1.xlarge``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` ,
                    ``cache.m3.xlarge`` , ``cache.m3.2xlarge``

                  * Compute optimized:

                    * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``

                  * Memory optimized:

                    * Current generation:   **R5 node types:**  ``cache.r5.large`` , ``cache.r5.xlarge`` ,
                    ``cache.r5.2xlarge`` , ``cache.r5.4xlarge`` , ``cache.r5.12xlarge`` ,
                    ``cache.r5.24xlarge``    **R4 node types:**  ``cache.r4.large`` , ``cache.r4.xlarge`` ,
                    ``cache.r4.2xlarge`` , ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` ,
                    ``cache.r4.16xlarge``

                    * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` ,
                    ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``    **R3 node types:**  ``cache.r3.large`` ,
                    ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``

                   **Additional node type info**

                  * All current generation instance types are created in Amazon VPC by default.

                  * Redis append-only files (AOF) are not supported for T1 or T2 instances.

                  * Redis Multi-AZ with automatic failover is not supported on T1 instances.

                  * Redis configuration variables ``appendonly`` and ``appendfsync`` are not supported on
                  Redis version 2.8.22 and later.

                - **Engine** *(string) --*

                  The name of the cache engine (``memcached`` or ``redis`` ) used by the source cluster.

                - **EngineVersion** *(string) --*

                  The version of the cache engine version that is used by the source cluster.

                - **NumCacheNodes** *(integer) --*

                  The number of cache nodes in the source cluster.

                  For clusters running Redis, this value must be 1. For clusters running Memcached, this
                  value must be between 1 and 20.

                - **PreferredAvailabilityZone** *(string) --*

                  The name of the Availability Zone in which the source cluster is located.

                - **CacheClusterCreateTime** *(datetime) --*

                  The date and time when the source cluster was created.

                - **PreferredMaintenanceWindow** *(string) --*

                  Specifies the weekly time range during which maintenance on the cluster is performed. It
                  is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The
                  minimum maintenance window is a 60 minute period.

                  Valid values for ``ddd`` are:

                  * ``sun``

                  * ``mon``

                  * ``tue``

                  * ``wed``

                  * ``thu``

                  * ``fri``

                  * ``sat``

                  Example: ``sun:23:00-mon:01:30``

                - **TopicArn** *(string) --*

                  The Amazon Resource Name (ARN) for the topic used by the source cluster for publishing
                  notifications.

                - **Port** *(integer) --*

                  The port number used by each cache nodes in the source cluster.

                - **CacheParameterGroupName** *(string) --*

                  The cache parameter group that is associated with the source cluster.

                - **CacheSubnetGroupName** *(string) --*

                  The name of the cache subnet group associated with the source cluster.

                - **VpcId** *(string) --*

                  The Amazon Virtual Private Cloud identifier (VPC ID) of the cache subnet group for the
                  source cluster.

                - **AutoMinorVersionUpgrade** *(boolean) --*

                  This parameter is currently disabled.

                - **SnapshotRetentionLimit** *(integer) --*

                  For an automatic snapshot, the number of days for which ElastiCache retains the snapshot
                  before deleting it.

                  For manual snapshots, this field reflects the ``SnapshotRetentionLimit`` for the source
                  cluster when the snapshot was created. This field is otherwise ignored: Manual snapshots
                  do not expire, and can only be deleted using the ``DeleteSnapshot`` operation.

                   **Important** If the value of SnapshotRetentionLimit is set to zero (0), backups are
                   turned off.

                - **SnapshotWindow** *(string) --*

                  The daily time range during which ElastiCache takes daily snapshots of the source cluster.

                - **NumNodeGroups** *(integer) --*

                  The number of node groups (shards) in this snapshot. When restoring from a snapshot, the
                  number of node groups (shards) in the snapshot and in the restored replication group must
                  be the same.

                - **AutomaticFailover** *(string) --*

                  Indicates the status of Multi-AZ with automatic failover for the source Redis replication
                  group.

                  Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

                  * Redis versions earlier than 2.8.6.

                  * Redis (cluster mode disabled): T1 node types.

                  * Redis (cluster mode enabled): T1 node types.

                - **NodeSnapshots** *(list) --*

                  A list of the cache nodes in the source cluster.

                  - *(dict) --*

                    Represents an individual cache node in a snapshot of a cluster.

                    - **CacheClusterId** *(string) --*

                      A unique identifier for the source cluster.

                    - **NodeGroupId** *(string) --*

                      A unique identifier for the source node group (shard).

                    - **CacheNodeId** *(string) --*

                      The cache node identifier for the node in the source cluster.

                    - **NodeGroupConfiguration** *(dict) --*

                      The configuration for the source node group (shard).

                      - **NodeGroupId** *(string) --*

                        Either the ElastiCache for Redis supplied 4-digit id or a user supplied id for the
                        node group these configuration values apply to.

                      - **Slots** *(string) --*

                        A string that specifies the keyspace for a particular node group. Keyspaces range
                        from 0 to 16,383. The string is in the format ``startkey-endkey`` .

                        Example: ``"0-3999"``

                      - **ReplicaCount** *(integer) --*

                        The number of read replica nodes in this node group (shard).

                      - **PrimaryAvailabilityZone** *(string) --*

                        The Availability Zone where the primary node of this node group (shard) is launched.

                      - **ReplicaAvailabilityZones** *(list) --*

                        A list of Availability Zones to be used for the read replicas. The number of
                        Availability Zones in this list must match the value of ``ReplicaCount`` or
                        ``ReplicasPerNodeGroup`` if not specified.

                        - *(string) --*

                    - **CacheSize** *(string) --*

                      The size of the cache on the source cache node.

                    - **CacheNodeCreateTime** *(datetime) --*

                      The date and time when the cache node was created in the source cluster.

                    - **SnapshotCreateTime** *(datetime) --*

                      The date and time when the source node's metadata and cache data set was obtained for
                      the snapshot.

                - **KmsKeyId** *(string) --*

                  The ID of the KMS key used to encrypt the snapshot.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_update_actions(
        self,
        ServiceUpdateName: str = None,
        ReplicationGroupIds: List[str] = None,
        CacheClusterIds: List[str] = None,
        Engine: str = None,
        ServiceUpdateStatus: List[str] = None,
        ServiceUpdateTimeRange: ClientDescribeUpdateActionsServiceUpdateTimeRangeTypeDef = None,
        UpdateActionStatus: List[str] = None,
        ShowNodeLevelUpdateStatus: bool = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ClientDescribeUpdateActionsResponseTypeDef:
        """
        Returns details of the update actions

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/DescribeUpdateActions>`_

        **Request Syntax**
        ::

          response = client.describe_update_actions(
              ServiceUpdateName='string',
              ReplicationGroupIds=[
                  'string',
              ],
              CacheClusterIds=[
                  'string',
              ],
              Engine='string',
              ServiceUpdateStatus=[
                  'available'|'cancelled'|'expired',
              ],
              ServiceUpdateTimeRange={
                  'StartTime': datetime(2015, 1, 1),
                  'EndTime': datetime(2015, 1, 1)
              },
              UpdateActionStatus=[
                  'not-applied'|'waiting-to-start'|'in-progress'|'stopping'|'stopped'|'complete',
              ],
              ShowNodeLevelUpdateStatus=True|False,
              MaxRecords=123,
              Marker='string'
          )
        :type ServiceUpdateName: string
        :param ServiceUpdateName:

          The unique ID of the service update

        :type ReplicationGroupIds: list
        :param ReplicationGroupIds:

          The replication group IDs

          - *(string) --*

        :type CacheClusterIds: list
        :param CacheClusterIds:

          The cache cluster IDs

          - *(string) --*

        :type Engine: string
        :param Engine:

          The Elasticache engine to which the update applies. Either Redis or Memcached

        :type ServiceUpdateStatus: list
        :param ServiceUpdateStatus:

          The status of the service update

          - *(string) --*

        :type ServiceUpdateTimeRange: dict
        :param ServiceUpdateTimeRange:

          The range of time specified to search for service updates that are in available status

          - **StartTime** *(datetime) --*

            The start time of the time range filter

          - **EndTime** *(datetime) --*

            The end time of the time range filter

        :type UpdateActionStatus: list
        :param UpdateActionStatus:

          The status of the update action.

          - *(string) --*

        :type ShowNodeLevelUpdateStatus: boolean
        :param ShowNodeLevelUpdateStatus:

          Dictates whether to include node level update status in the response

        :type MaxRecords: integer
        :param MaxRecords:

          The maximum number of records to include in the response

        :type Marker: string
        :param Marker:

          An optional marker returned from a prior request. Use this marker for pagination of results from
          this operation. If this parameter is specified, the response includes only records beyond the
          marker, up to the value specified by ``MaxRecords`` .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Marker': 'string',
                'UpdateActions': [
                    {
                        'ReplicationGroupId': 'string',
                        'CacheClusterId': 'string',
                        'ServiceUpdateName': 'string',
                        'ServiceUpdateReleaseDate': datetime(2015, 1, 1),
                        'ServiceUpdateSeverity': 'critical'|'important'|'medium'|'low',
                        'ServiceUpdateStatus': 'available'|'cancelled'|'expired',
                        'ServiceUpdateRecommendedApplyByDate': datetime(2015, 1, 1),
                        'ServiceUpdateType': 'security-update',
                        'UpdateActionAvailableDate': datetime(2015, 1, 1),
                        'UpdateActionStatus':
                        'not-applied'|'waiting-to-start'|'in-progress'|'stopping'|'stopped'|'complete',
                        'NodesUpdated': 'string',
                        'UpdateActionStatusModifiedDate': datetime(2015, 1, 1),
                        'SlaMet': 'yes'|'no'|'n/a',
                        'NodeGroupUpdateStatus': [
                            {
                                'NodeGroupId': 'string',
                                'NodeGroupMemberUpdateStatus': [
                                    {
                                        'CacheClusterId': 'string',
                                        'CacheNodeId': 'string',
                                        'NodeUpdateStatus':
                                        'not-applied'|'waiting-to-start'|'in-progress'|'stopping'|'stopped'
                                        |'complete',
                                        'NodeDeletionDate': datetime(2015, 1, 1),
                                        'NodeUpdateStartDate': datetime(2015, 1, 1),
                                        'NodeUpdateEndDate': datetime(2015, 1, 1),
                                        'NodeUpdateInitiatedBy': 'system'|'customer',
                                        'NodeUpdateInitiatedDate': datetime(2015, 1, 1),
                                        'NodeUpdateStatusModifiedDate': datetime(2015, 1, 1)
                                    },
                                ]
                            },
                        ],
                        'CacheNodeUpdateStatus': [
                            {
                                'CacheNodeId': 'string',
                                'NodeUpdateStatus':
                                'not-applied'|'waiting-to-start'|'in-progress'|'stopping'|'stopped'
                                |'complete',
                                'NodeDeletionDate': datetime(2015, 1, 1),
                                'NodeUpdateStartDate': datetime(2015, 1, 1),
                                'NodeUpdateEndDate': datetime(2015, 1, 1),
                                'NodeUpdateInitiatedBy': 'system'|'customer',
                                'NodeUpdateInitiatedDate': datetime(2015, 1, 1),
                                'NodeUpdateStatusModifiedDate': datetime(2015, 1, 1)
                            },
                        ],
                        'EstimatedUpdateTime': 'string',
                        'Engine': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **Marker** *(string) --*

              An optional marker returned from a prior request. Use this marker for pagination of results
              from this operation. If this parameter is specified, the response includes only records
              beyond the marker, up to the value specified by ``MaxRecords`` .

            - **UpdateActions** *(list) --*

              Returns a list of update actions

              - *(dict) --*

                The status of the service update for a specific replication group

                - **ReplicationGroupId** *(string) --*

                  The ID of the replication group

                - **CacheClusterId** *(string) --*

                  The ID of the cache cluster

                - **ServiceUpdateName** *(string) --*

                  The unique ID of the service update

                - **ServiceUpdateReleaseDate** *(datetime) --*

                  The date the update is first available

                - **ServiceUpdateSeverity** *(string) --*

                  The severity of the service update

                - **ServiceUpdateStatus** *(string) --*

                  The status of the service update

                - **ServiceUpdateRecommendedApplyByDate** *(datetime) --*

                  The recommended date to apply the service update to ensure compliance. For information on
                  compliance, see `Self-Service Security Updates for Compliance
                  <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/elasticache-compliance.html#elasticache-compliance-self-service>`__
                  .

                - **ServiceUpdateType** *(string) --*

                  Reflects the nature of the service update

                - **UpdateActionAvailableDate** *(datetime) --*

                  The date that the service update is available to a replication group

                - **UpdateActionStatus** *(string) --*

                  The status of the update action

                - **NodesUpdated** *(string) --*

                  The progress of the service update on the replication group

                - **UpdateActionStatusModifiedDate** *(datetime) --*

                  The date when the UpdateActionStatus was last modified

                - **SlaMet** *(string) --*

                  If yes, all nodes in the replication group have been updated by the recommended apply-by
                  date. If no, at least one node in the replication group have not been updated by the
                  recommended apply-by date. If N/A, the replication group was created after the
                  recommended apply-by date.

                - **NodeGroupUpdateStatus** *(list) --*

                  The status of the service update on the node group

                  - *(dict) --*

                    The status of the service update on the node group

                    - **NodeGroupId** *(string) --*

                      The ID of the node group

                    - **NodeGroupMemberUpdateStatus** *(list) --*

                      The status of the service update on the node group member

                      - *(dict) --*

                        The status of the service update on the node group member

                        - **CacheClusterId** *(string) --*

                          The cache cluster ID

                        - **CacheNodeId** *(string) --*

                          The node ID of the cache cluster

                        - **NodeUpdateStatus** *(string) --*

                          The update status of the node

                        - **NodeDeletionDate** *(datetime) --*

                          The deletion date of the node

                        - **NodeUpdateStartDate** *(datetime) --*

                          The start date of the update for a node

                        - **NodeUpdateEndDate** *(datetime) --*

                          The end date of the update for a node

                        - **NodeUpdateInitiatedBy** *(string) --*

                          Reflects whether the update was initiated by the customer or automatically applied

                        - **NodeUpdateInitiatedDate** *(datetime) --*

                          The date when the update is triggered

                        - **NodeUpdateStatusModifiedDate** *(datetime) --*

                          The date when the NodeUpdateStatus was last modified

                - **CacheNodeUpdateStatus** *(list) --*

                  The status of the service update on the cache node

                  - *(dict) --*

                    The status of the service update on the cache node

                    - **CacheNodeId** *(string) --*

                      The node ID of the cache cluster

                    - **NodeUpdateStatus** *(string) --*

                      The update status of the node

                    - **NodeDeletionDate** *(datetime) --*

                      The deletion date of the node

                    - **NodeUpdateStartDate** *(datetime) --*

                      The start date of the update for a node

                    - **NodeUpdateEndDate** *(datetime) --*

                      The end date of the update for a node

                    - **NodeUpdateInitiatedBy** *(string) --*

                      Reflects whether the update was initiated by the customer or automatically applied

                    - **NodeUpdateInitiatedDate** *(datetime) --*

                      The date when the update is triggered

                    - **NodeUpdateStatusModifiedDate** *(datetime) --*

                      The date when the NodeUpdateStatus was last modified>

                - **EstimatedUpdateTime** *(string) --*

                  The estimated length of time for the update to complete

                - **Engine** *(string) --*

                  The Elasticache engine to which the update applies. Either Redis or Memcached

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
    def increase_replica_count(
        self,
        ReplicationGroupId: str,
        ApplyImmediately: bool,
        NewReplicaCount: int = None,
        ReplicaConfiguration: List[
            ClientIncreaseReplicaCountReplicaConfigurationTypeDef
        ] = None,
    ) -> ClientIncreaseReplicaCountResponseTypeDef:
        """
        Dynamically increases the number of replics in a Redis (cluster mode disabled) replication group or
        the number of replica nodes in one or more node groups (shards) of a Redis (cluster mode enabled)
        replication group. This operation is performed with no cluster down time.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/IncreaseReplicaCount>`_

        **Request Syntax**
        ::

          response = client.increase_replica_count(
              ReplicationGroupId='string',
              NewReplicaCount=123,
              ReplicaConfiguration=[
                  {
                      'NodeGroupId': 'string',
                      'NewReplicaCount': 123,
                      'PreferredAvailabilityZones': [
                          'string',
                      ]
                  },
              ],
              ApplyImmediately=True|False
          )
        :type ReplicationGroupId: string
        :param ReplicationGroupId: **[REQUIRED]**

          The id of the replication group to which you want to add replica nodes.

        :type NewReplicaCount: integer
        :param NewReplicaCount:

          The number of read replica nodes you want at the completion of this operation. For Redis (cluster
          mode disabled) replication groups, this is the number of replica nodes in the replication group.
          For Redis (cluster mode enabled) replication groups, this is the number of replica nodes in each
          of the replication group's node groups.

        :type ReplicaConfiguration: list
        :param ReplicaConfiguration:

          A list of ``ConfigureShard`` objects that can be used to configure each shard in a Redis (cluster
          mode enabled) replication group. The ``ConfigureShard`` has three members: ``NewReplicaCount`` ,
          ``NodeGroupId`` , and ``PreferredAvailabilityZones`` .

          - *(dict) --*

            Node group (shard) configuration options when adding or removing replicas. Each node group
            (shard) configuration has the following members: NodeGroupId, NewReplicaCount, and
            PreferredAvailabilityZones.

            - **NodeGroupId** *(string) --* **[REQUIRED]**

              The 4-digit id for the node group you are configuring. For Redis (cluster mode disabled)
              replication groups, the node group id is always 0001. To find a Redis (cluster mode
              enabled)'s node group's (shard's) id, see `Finding a Shard's Id
              <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/shard-find-id.html>`__ .

            - **NewReplicaCount** *(integer) --* **[REQUIRED]**

              The number of replicas you want in this node group at the end of this operation. The maximum
              value for ``NewReplicaCount`` is 5. The minimum value depends upon the type of Redis
              replication group you are working with.

              The minimum number of replicas in a shard or replication group is:

              * Redis (cluster mode disabled)

                * If Multi-AZ with Automatic Failover is enabled: 1

                * If Multi-AZ with Automatic Failover is not enable: 0

              * Redis (cluster mode enabled): 0 (though you will not be able to failover to a replica if
              your primary node fails)

            - **PreferredAvailabilityZones** *(list) --*

              A list of ``PreferredAvailabilityZone`` strings that specify which availability zones the
              replication group's nodes are to be in. The nummber of ``PreferredAvailabilityZone`` values
              must equal the value of ``NewReplicaCount`` plus 1 to account for the primary node. If this
              member of ``ReplicaConfiguration`` is omitted, ElastiCache for Redis selects the availability
              zone for each of the replicas.

              - *(string) --*

        :type ApplyImmediately: boolean
        :param ApplyImmediately: **[REQUIRED]**

          If ``True`` , the number of replica nodes is increased immediately. ``ApplyImmediately=False`` is
          not currently supported.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ReplicationGroup': {
                    'ReplicationGroupId': 'string',
                    'Description': 'string',
                    'Status': 'string',
                    'PendingModifiedValues': {
                        'PrimaryClusterId': 'string',
                        'AutomaticFailoverStatus': 'enabled'|'disabled',
                        'Resharding': {
                            'SlotMigration': {
                                'ProgressPercentage': 123.0
                            }
                        },
                        'AuthTokenStatus': 'SETTING'|'ROTATING'
                    },
                    'MemberClusters': [
                        'string',
                    ],
                    'NodeGroups': [
                        {
                            'NodeGroupId': 'string',
                            'Status': 'string',
                            'PrimaryEndpoint': {
                                'Address': 'string',
                                'Port': 123
                            },
                            'ReaderEndpoint': {
                                'Address': 'string',
                                'Port': 123
                            },
                            'Slots': 'string',
                            'NodeGroupMembers': [
                                {
                                    'CacheClusterId': 'string',
                                    'CacheNodeId': 'string',
                                    'ReadEndpoint': {
                                        'Address': 'string',
                                        'Port': 123
                                    },
                                    'PreferredAvailabilityZone': 'string',
                                    'CurrentRole': 'string'
                                },
                            ]
                        },
                    ],
                    'SnapshottingClusterId': 'string',
                    'AutomaticFailover': 'enabled'|'disabled'|'enabling'|'disabling',
                    'ConfigurationEndpoint': {
                        'Address': 'string',
                        'Port': 123
                    },
                    'SnapshotRetentionLimit': 123,
                    'SnapshotWindow': 'string',
                    'ClusterEnabled': True|False,
                    'CacheNodeType': 'string',
                    'AuthTokenEnabled': True|False,
                    'AuthTokenLastModifiedDate': datetime(2015, 1, 1),
                    'TransitEncryptionEnabled': True|False,
                    'AtRestEncryptionEnabled': True|False,
                    'KmsKeyId': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **ReplicationGroup** *(dict) --*

              Contains all of the attributes of a specific Redis replication group.

              - **ReplicationGroupId** *(string) --*

                The identifier for the replication group.

              - **Description** *(string) --*

                The user supplied description of the replication group.

              - **Status** *(string) --*

                The current state of this replication group - ``creating`` , ``available`` , ``modifying``
                , ``deleting`` , ``create-failed`` , ``snapshotting`` .

              - **PendingModifiedValues** *(dict) --*

                A group of settings to be applied to the replication group, either immediately or during
                the next maintenance window.

                - **PrimaryClusterId** *(string) --*

                  The primary cluster ID that is applied immediately (if ``--apply-immediately`` was
                  specified), or during the next maintenance window.

                - **AutomaticFailoverStatus** *(string) --*

                  Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

                  Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

                  * Redis versions earlier than 2.8.6.

                  * Redis (cluster mode disabled): T1 node types.

                  * Redis (cluster mode enabled): T1 node types.

                - **Resharding** *(dict) --*

                  The status of an online resharding operation.

                  - **SlotMigration** *(dict) --*

                    Represents the progress of an online resharding operation.

                    - **ProgressPercentage** *(float) --*

                      The percentage of the slot migration that is complete.

                - **AuthTokenStatus** *(string) --*

                  The auth token status

              - **MemberClusters** *(list) --*

                The names of all the cache clusters that are part of this replication group.

                - *(string) --*

              - **NodeGroups** *(list) --*

                A list of node groups in this replication group. For Redis (cluster mode disabled)
                replication groups, this is a single-element list. For Redis (cluster mode enabled)
                replication groups, the list contains an entry for each node group (shard).

                - *(dict) --*

                  Represents a collection of cache nodes in a replication group. One node in the node group
                  is the read/write primary node. All the other nodes are read-only Replica nodes.

                  - **NodeGroupId** *(string) --*

                    The identifier for the node group (shard). A Redis (cluster mode disabled) replication
                    group contains only 1 node group; therefore, the node group ID is 0001. A Redis
                    (cluster mode enabled) replication group contains 1 to 90 node groups numbered 0001 to
                    0090. Optionally, the user can provide the id for a node group.

                  - **Status** *(string) --*

                    The current state of this replication group - ``creating`` , ``available`` , etc.

                  - **PrimaryEndpoint** *(dict) --*

                    The endpoint of the primary node in this node group (shard).

                    - **Address** *(string) --*

                      The DNS hostname of the cache node.

                    - **Port** *(integer) --*

                      The port number that the cache engine is listening on.

                  - **ReaderEndpoint** *(dict) --*

                    The endpoint of the replica nodes in this node group (shard).

                    - **Address** *(string) --*

                      The DNS hostname of the cache node.

                    - **Port** *(integer) --*

                      The port number that the cache engine is listening on.

                  - **Slots** *(string) --*

                    The keyspace for this node group (shard).

                  - **NodeGroupMembers** *(list) --*

                    A list containing information about individual nodes within the node group (shard).

                    - *(dict) --*

                      Represents a single node within a node group (shard).

                      - **CacheClusterId** *(string) --*

                        The ID of the cluster to which the node belongs.

                      - **CacheNodeId** *(string) --*

                        The ID of the node within its cluster. A node ID is a numeric identifier (0001,
                        0002, etc.).

                      - **ReadEndpoint** *(dict) --*

                        The information required for client programs to connect to a node for read
                        operations. The read endpoint is only applicable on Redis (cluster mode disabled)
                        clusters.

                        - **Address** *(string) --*

                          The DNS hostname of the cache node.

                        - **Port** *(integer) --*

                          The port number that the cache engine is listening on.

                      - **PreferredAvailabilityZone** *(string) --*

                        The name of the Availability Zone in which the node is located.

                      - **CurrentRole** *(string) --*

                        The role that is currently assigned to the node - ``primary`` or ``replica`` . This
                        member is only applicable for Redis (cluster mode disabled) replication groups.

              - **SnapshottingClusterId** *(string) --*

                The cluster ID that is used as the daily snapshot source for the replication group.

              - **AutomaticFailover** *(string) --*

                Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

                Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

                * Redis versions earlier than 2.8.6.

                * Redis (cluster mode disabled): T1 node types.

                * Redis (cluster mode enabled): T1 node types.

              - **ConfigurationEndpoint** *(dict) --*

                The configuration endpoint for this replication group. Use the configuration endpoint to
                connect to this replication group.

                - **Address** *(string) --*

                  The DNS hostname of the cache node.

                - **Port** *(integer) --*

                  The port number that the cache engine is listening on.

              - **SnapshotRetentionLimit** *(integer) --*

                The number of days for which ElastiCache retains automatic cluster snapshots before
                deleting them. For example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot that was
                taken today is retained for 5 days before being deleted.

                .. warning::

                  If the value of ``SnapshotRetentionLimit`` is set to zero (0), backups are turned off.

              - **SnapshotWindow** *(string) --*

                The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of
                your node group (shard).

                Example: ``05:00-09:00``

                If you do not specify this parameter, ElastiCache automatically chooses an appropriate time
                range.

                .. note::

                  This parameter is only valid if the ``Engine`` parameter is ``redis`` .

              - **ClusterEnabled** *(boolean) --*

                A flag indicating whether or not this replication group is cluster enabled; i.e., whether
                its data can be partitioned across multiple shards (API/CLI: node groups).

                Valid values: ``true`` | ``false``

              - **CacheNodeType** *(string) --*

                The name of the compute and memory capacity node type for each node in the replication
                group.

              - **AuthTokenEnabled** *(boolean) --*

                A flag that enables using an ``AuthToken`` (password) when issuing Redis commands.

                Default: ``false``

              - **AuthTokenLastModifiedDate** *(datetime) --*

                The date the auth token was last modified

              - **TransitEncryptionEnabled** *(boolean) --*

                A flag that enables in-transit encryption when set to ``true`` .

                You cannot modify the value of ``TransitEncryptionEnabled`` after the cluster is created.
                To enable in-transit encryption on a cluster you must set ``TransitEncryptionEnabled`` to
                ``true`` when you create a cluster.

                 **Required:** Only available when creating a replication group in an Amazon VPC using
                 redis version ``3.2.6`` , ``4.x`` or later.

                Default: ``false``

              - **AtRestEncryptionEnabled** *(boolean) --*

                A flag that enables encryption at-rest when set to ``true`` .

                You cannot modify the value of ``AtRestEncryptionEnabled`` after the cluster is created. To
                enable encryption at-rest on a cluster you must set ``AtRestEncryptionEnabled`` to ``true``
                when you create a cluster.

                 **Required:** Only available when creating a replication group in an Amazon VPC using
                 redis version ``3.2.6`` , ``4.x`` or later.

                Default: ``false``

              - **KmsKeyId** *(string) --*

                The ID of the KMS key used to encrypt the disk in the cluster.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_allowed_node_type_modifications(
        self, CacheClusterId: str = None, ReplicationGroupId: str = None
    ) -> ClientListAllowedNodeTypeModificationsResponseTypeDef:
        """
        Lists all available node types that you can scale your Redis cluster's or replication group's
        current node type.

        When you use the ``ModifyCacheCluster`` or ``ModifyReplicationGroup`` operations to scale your
        cluster or replication group, the value of the ``CacheNodeType`` parameter must be one of the node
        types returned by this operation.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/ListAllowedNodeTypeModifications>`_

        **Request Syntax**
        ::

          response = client.list_allowed_node_type_modifications(
              CacheClusterId='string',
              ReplicationGroupId='string'
          )
        :type CacheClusterId: string
        :param CacheClusterId:

          The name of the cluster you want to scale up to a larger node instanced type. ElastiCache uses
          the cluster id to identify the current node type of this cluster and from that to create a list
          of node types you can scale up to.

          .. warning::

            You must provide a value for either the ``CacheClusterId`` or the ``ReplicationGroupId`` .

        :type ReplicationGroupId: string
        :param ReplicationGroupId:

          The name of the replication group want to scale up to a larger node type. ElastiCache uses the
          replication group id to identify the current node type being used by this replication group, and
          from that to create a list of node types you can scale up to.

          .. warning::

            You must provide a value for either the ``CacheClusterId`` or the ``ReplicationGroupId`` .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ScaleUpModifications': [
                    'string',
                ],
                'ScaleDownModifications': [
                    'string',
                ]
            }
          **Response Structure**

          - *(dict) --*

            Represents the allowed node types you can use to modify your cluster or replication group.

            - **ScaleUpModifications** *(list) --*

              A string list, each element of which specifies a cache node type which you can use to scale
              your cluster or replication group.

              When scaling up a Redis cluster or replication group using ``ModifyCacheCluster`` or
              ``ModifyReplicationGroup`` , use a value from this list for the ``CacheNodeType`` parameter.

              - *(string) --*

            - **ScaleDownModifications** *(list) --*

              A string list, each element of which specifies a cache node type which you can use to scale
              your cluster or replication group.

              When scaling down on a Redis cluster or replication group using ``ModifyCacheCluster`` or
              ``ModifyReplicationGroup`` , use a value from this list for the ``CacheNodeType`` parameter.

              - *(string) --*

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(
        self, ResourceName: str
    ) -> ClientListTagsForResourceResponseTypeDef:
        """
        Lists all cost allocation tags currently on the named resource. A ``cost allocation tag`` is a
        key-value pair where the key is case-sensitive and the value is optional. You can use cost
        allocation tags to categorize and track your AWS costs.

        If the cluster is not in the *available* state, ``ListTagsForResource`` returns an error.

        You can have a maximum of 50 cost allocation tags on an ElastiCache resource. For more information,
        see `Monitoring Costs with Tags
        <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Tagging.html>`__ .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/ListTagsForResource>`_

        **Request Syntax**
        ::

          response = client.list_tags_for_resource(
              ResourceName='string'
          )
        :type ResourceName: string
        :param ResourceName: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the resource for which you want the list of tags, for example
          ``arn:aws:elasticache:us-west-2:0123456789:cluster:myCluster`` or
          ``arn:aws:elasticache:us-west-2:0123456789:snapshot:mySnapshot`` .

          For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS Service Namespaces
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'TagList': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            Represents the output from the ``AddTagsToResource`` , ``ListTagsForResource`` , and
            ``RemoveTagsFromResource`` operations.

            - **TagList** *(list) --*

              A list of cost allocation tags as key-value pairs.

              - *(dict) --*

                A cost allocation Tag that can be added to an ElastiCache cluster or replication group.
                Tags are composed of a Key/Value pair. A tag with a null Value is permitted.

                - **Key** *(string) --*

                  The key for the tag. May not be null.

                - **Value** *(string) --*

                  The tag's value. May be null.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_cache_cluster(
        self,
        CacheClusterId: str,
        NumCacheNodes: int = None,
        CacheNodeIdsToRemove: List[str] = None,
        AZMode: str = None,
        NewAvailabilityZones: List[str] = None,
        CacheSecurityGroupNames: List[str] = None,
        SecurityGroupIds: List[str] = None,
        PreferredMaintenanceWindow: str = None,
        NotificationTopicArn: str = None,
        CacheParameterGroupName: str = None,
        NotificationTopicStatus: str = None,
        ApplyImmediately: bool = None,
        EngineVersion: str = None,
        AutoMinorVersionUpgrade: bool = None,
        SnapshotRetentionLimit: int = None,
        SnapshotWindow: str = None,
        CacheNodeType: str = None,
        AuthToken: str = None,
        AuthTokenUpdateStrategy: str = None,
    ) -> ClientModifyCacheClusterResponseTypeDef:
        """
        Modifies the settings for a cluster. You can use this operation to change one or more cluster
        configuration parameters by specifying the parameters and the new values.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/ModifyCacheCluster>`_

        **Request Syntax**
        ::

          response = client.modify_cache_cluster(
              CacheClusterId='string',
              NumCacheNodes=123,
              CacheNodeIdsToRemove=[
                  'string',
              ],
              AZMode='single-az'|'cross-az',
              NewAvailabilityZones=[
                  'string',
              ],
              CacheSecurityGroupNames=[
                  'string',
              ],
              SecurityGroupIds=[
                  'string',
              ],
              PreferredMaintenanceWindow='string',
              NotificationTopicArn='string',
              CacheParameterGroupName='string',
              NotificationTopicStatus='string',
              ApplyImmediately=True|False,
              EngineVersion='string',
              AutoMinorVersionUpgrade=True|False,
              SnapshotRetentionLimit=123,
              SnapshotWindow='string',
              CacheNodeType='string',
              AuthToken='string',
              AuthTokenUpdateStrategy='SET'|'ROTATE'
          )
        :type CacheClusterId: string
        :param CacheClusterId: **[REQUIRED]**

          The cluster identifier. This value is stored as a lowercase string.

        :type NumCacheNodes: integer
        :param NumCacheNodes:

          The number of cache nodes that the cluster should have. If the value for ``NumCacheNodes`` is
          greater than the sum of the number of current cache nodes and the number of cache nodes pending
          creation (which may be zero), more nodes are added. If the value is less than the number of
          existing cache nodes, nodes are removed. If the value is equal to the number of current cache
          nodes, any pending add or remove requests are canceled.

          If you are removing cache nodes, you must use the ``CacheNodeIdsToRemove`` parameter to provide
          the IDs of the specific cache nodes to remove.

          For clusters running Redis, this value must be 1. For clusters running Memcached, this value must
          be between 1 and 20.

          .. note::

            Adding or removing Memcached cache nodes can be applied immediately or as a pending operation
            (see ``ApplyImmediately`` ).

            A pending operation to modify the number of cache nodes in a cluster during its maintenance
            window, whether by adding or removing nodes in accordance with the scale out architecture, is
            not queued. The customer's latest request to add or remove nodes to the cluster overrides any
            previous pending operations to modify the number of cache nodes in the cluster. For example, a
            request to remove 2 nodes would override a previous pending operation to remove 3 nodes.
            Similarly, a request to add 2 nodes would override a previous pending operation to remove 3
            nodes and vice versa. As Memcached cache nodes may now be provisioned in different Availability
            Zones with flexible cache node placement, a request to add nodes does not automatically
            override a previous pending operation to add nodes. The customer can modify the previous
            pending operation to add more nodes or explicitly cancel the pending request and retry the new
            request. To cancel pending operations to modify the number of cache nodes in a cluster, use the
            ``ModifyCacheCluster`` request and set ``NumCacheNodes`` equal to the number of cache nodes
            currently in the cluster.

        :type CacheNodeIdsToRemove: list
        :param CacheNodeIdsToRemove:

          A list of cache node IDs to be removed. A node ID is a numeric identifier (0001, 0002, etc.).
          This parameter is only valid when ``NumCacheNodes`` is less than the existing number of cache
          nodes. The number of cache node IDs supplied in this parameter must match the difference between
          the existing number of cache nodes in the cluster or pending cache nodes, whichever is greater,
          and the value of ``NumCacheNodes`` in the request.

          For example: If you have 3 active cache nodes, 7 pending cache nodes, and the number of cache
          nodes in this ``ModifyCacheCluster`` call is 5, you must list 2 (7 - 5) cache node IDs to remove.

          - *(string) --*

        :type AZMode: string
        :param AZMode:

          Specifies whether the new nodes in this Memcached cluster are all created in a single
          Availability Zone or created across multiple Availability Zones.

          Valid values: ``single-az`` | ``cross-az`` .

          This option is only supported for Memcached clusters.

          .. note::

            You cannot specify ``single-az`` if the Memcached cluster already has cache nodes in different
            Availability Zones. If ``cross-az`` is specified, existing Memcached nodes remain in their
            current Availability Zone.

            Only newly created nodes are located in different Availability Zones.

        :type NewAvailabilityZones: list
        :param NewAvailabilityZones:

          The list of Availability Zones where the new Memcached cache nodes are created.

          This parameter is only valid when ``NumCacheNodes`` in the request is greater than the sum of the
          number of active cache nodes and the number of cache nodes pending creation (which may be zero).
          The number of Availability Zones supplied in this list must match the cache nodes being added in
          this request.

          This option is only supported on Memcached clusters.

          Scenarios:

          * **Scenario 1:** You have 3 active nodes and wish to add 2 nodes. Specify ``NumCacheNodes=5`` (3
          + 2) and optionally specify two Availability Zones for the two new nodes.

          * **Scenario 2:** You have 3 active nodes and 2 nodes pending creation (from the scenario 1 call)
          and want to add 1 more node. Specify ``NumCacheNodes=6`` ((3 + 2) + 1) and optionally specify an
          Availability Zone for the new node.

          * **Scenario 3:** You want to cancel all pending operations. Specify ``NumCacheNodes=3`` to
          cancel all pending operations.

          The Availability Zone placement of nodes pending creation cannot be modified. If you wish to
          cancel any nodes pending creation, add 0 nodes by setting ``NumCacheNodes`` to the number of
          current nodes.

          If ``cross-az`` is specified, existing Memcached nodes remain in their current Availability Zone.
          Only newly created nodes can be located in different Availability Zones. For guidance on how to
          move existing Memcached nodes to different Availability Zones, see the **Availability Zone
          Considerations** section of `Cache Node Considerations for Memcached
          <https://docs.aws.amazon.com/AmazonElastiCache/latest/mem-ug/CacheNodes.SupportedTypes.html>`__ .

           **Impact of new add/remove requests upon pending requests**

          * Scenario-1

            * Pending Action: Delete

            * New Request: Delete

            * Result: The new delete, pending or immediate, replaces the pending delete.

          * Scenario-2

            * Pending Action: Delete

            * New Request: Create

            * Result: The new create, pending or immediate, replaces the pending delete.

          * Scenario-3

            * Pending Action: Create

            * New Request: Delete

            * Result: The new delete, pending or immediate, replaces the pending create.

          * Scenario-4

            * Pending Action: Create

            * New Request: Create

            * Result: The new create is added to the pending create.

            .. warning::

                **Important:** If the new create request is **Apply Immediately - Yes** , all creates are
                performed immediately. If the new create request is **Apply Immediately - No** , all
                creates are pending.

          - *(string) --*

        :type CacheSecurityGroupNames: list
        :param CacheSecurityGroupNames:

          A list of cache security group names to authorize on this cluster. This change is asynchronously
          applied as soon as possible.

          You can use this parameter only with clusters that are created outside of an Amazon Virtual
          Private Cloud (Amazon VPC).

          Constraints: Must contain no more than 255 alphanumeric characters. Must not be "Default".

          - *(string) --*

        :type SecurityGroupIds: list
        :param SecurityGroupIds:

          Specifies the VPC Security Groups associated with the cluster.

          This parameter can be used only with clusters that are created in an Amazon Virtual Private Cloud
          (Amazon VPC).

          - *(string) --*

        :type PreferredMaintenanceWindow: string
        :param PreferredMaintenanceWindow:

          Specifies the weekly time range during which maintenance on the cluster is performed. It is
          specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum
          maintenance window is a 60 minute period.

          Valid values for ``ddd`` are:

          * ``sun``

          * ``mon``

          * ``tue``

          * ``wed``

          * ``thu``

          * ``fri``

          * ``sat``

          Example: ``sun:23:00-mon:01:30``

        :type NotificationTopicArn: string
        :param NotificationTopicArn:

          The Amazon Resource Name (ARN) of the Amazon SNS topic to which notifications are sent.

          .. note::

            The Amazon SNS topic owner must be same as the cluster owner.

        :type CacheParameterGroupName: string
        :param CacheParameterGroupName:

          The name of the cache parameter group to apply to this cluster. This change is asynchronously
          applied as soon as possible for parameters when the ``ApplyImmediately`` parameter is specified
          as ``true`` for this request.

        :type NotificationTopicStatus: string
        :param NotificationTopicStatus:

          The status of the Amazon SNS notification topic. Notifications are sent only if the status is
          ``active`` .

          Valid values: ``active`` | ``inactive``

        :type ApplyImmediately: boolean
        :param ApplyImmediately:

          If ``true`` , this parameter causes the modifications in this request and any pending
          modifications to be applied, asynchronously and as soon as possible, regardless of the
          ``PreferredMaintenanceWindow`` setting for the cluster.

          If ``false`` , changes to the cluster are applied on the next maintenance reboot, or the next
          failure reboot, whichever occurs first.

          .. warning::

            If you perform a ``ModifyCacheCluster`` before a pending modification is applied, the pending
            modification is replaced by the newer modification.

          Valid values: ``true`` | ``false``

          Default: ``false``

        :type EngineVersion: string
        :param EngineVersion:

          The upgraded version of the cache engine to be run on the cache nodes.

           **Important:** You can upgrade to a newer engine version (see `Selecting a Cache Engine and
           Version
           <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/SelectEngine.html#VersionManagement>`__
           ), but you cannot downgrade to an earlier engine version. If you want to use an earlier engine
           version, you must delete the existing cluster and create it anew with the earlier engine version.

        :type AutoMinorVersionUpgrade: boolean
        :param AutoMinorVersionUpgrade:

          This parameter is currently disabled.

        :type SnapshotRetentionLimit: integer
        :param SnapshotRetentionLimit:

          The number of days for which ElastiCache retains automatic cluster snapshots before deleting
          them. For example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot that was taken today is
          retained for 5 days before being deleted.

          .. note::

            If the value of ``SnapshotRetentionLimit`` is set to zero (0), backups are turned off.

        :type SnapshotWindow: string
        :param SnapshotWindow:

          The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your
          cluster.

        :type CacheNodeType: string
        :param CacheNodeType:

          A valid cache node type that you want to scale this cluster up to.

        :type AuthToken: string
        :param AuthToken:

          Reserved parameter. The password used to access a password protected server. This parameter must
          be specified with the ``auth-token-update`` parameter. Password constraints:

          * Must be only printable ASCII characters

          * Must be at least 16 characters and no more than 128 characters in length

          * Cannot contain any of the following characters: '/', '"', or '@', '%'

          For more information, see AUTH password at `AUTH <http://redis.io/commands/AUTH>`__ .

        :type AuthTokenUpdateStrategy: string
        :param AuthTokenUpdateStrategy:

          Specifies the strategy to use to update the AUTH token. This parameter must be specified with the
          ``auth-token`` parameter. Possible values:

          * Rotate

          * Set

          For more information, see `Authenticating Users with Redis AUTH
          <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/auth.html>`__

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'CacheCluster': {
                    'CacheClusterId': 'string',
                    'ConfigurationEndpoint': {
                        'Address': 'string',
                        'Port': 123
                    },
                    'ClientDownloadLandingPage': 'string',
                    'CacheNodeType': 'string',
                    'Engine': 'string',
                    'EngineVersion': 'string',
                    'CacheClusterStatus': 'string',
                    'NumCacheNodes': 123,
                    'PreferredAvailabilityZone': 'string',
                    'CacheClusterCreateTime': datetime(2015, 1, 1),
                    'PreferredMaintenanceWindow': 'string',
                    'PendingModifiedValues': {
                        'NumCacheNodes': 123,
                        'CacheNodeIdsToRemove': [
                            'string',
                        ],
                        'EngineVersion': 'string',
                        'CacheNodeType': 'string',
                        'AuthTokenStatus': 'SETTING'|'ROTATING'
                    },
                    'NotificationConfiguration': {
                        'TopicArn': 'string',
                        'TopicStatus': 'string'
                    },
                    'CacheSecurityGroups': [
                        {
                            'CacheSecurityGroupName': 'string',
                            'Status': 'string'
                        },
                    ],
                    'CacheParameterGroup': {
                        'CacheParameterGroupName': 'string',
                        'ParameterApplyStatus': 'string',
                        'CacheNodeIdsToReboot': [
                            'string',
                        ]
                    },
                    'CacheSubnetGroupName': 'string',
                    'CacheNodes': [
                        {
                            'CacheNodeId': 'string',
                            'CacheNodeStatus': 'string',
                            'CacheNodeCreateTime': datetime(2015, 1, 1),
                            'Endpoint': {
                                'Address': 'string',
                                'Port': 123
                            },
                            'ParameterGroupStatus': 'string',
                            'SourceCacheNodeId': 'string',
                            'CustomerAvailabilityZone': 'string'
                        },
                    ],
                    'AutoMinorVersionUpgrade': True|False,
                    'SecurityGroups': [
                        {
                            'SecurityGroupId': 'string',
                            'Status': 'string'
                        },
                    ],
                    'ReplicationGroupId': 'string',
                    'SnapshotRetentionLimit': 123,
                    'SnapshotWindow': 'string',
                    'AuthTokenEnabled': True|False,
                    'AuthTokenLastModifiedDate': datetime(2015, 1, 1),
                    'TransitEncryptionEnabled': True|False,
                    'AtRestEncryptionEnabled': True|False
                }
            }
          **Response Structure**

          - *(dict) --*

            - **CacheCluster** *(dict) --*

              Contains all of the attributes of a specific cluster.

              - **CacheClusterId** *(string) --*

                The user-supplied identifier of the cluster. This identifier is a unique key that
                identifies a cluster.

              - **ConfigurationEndpoint** *(dict) --*

                Represents a Memcached cluster endpoint which, if Automatic Discovery is enabled on the
                cluster, can be used by an application to connect to any node in the cluster. The
                configuration endpoint will always have ``.cfg`` in it.

                Example: ``mem-3.9dvc4r.cfg.usw2.cache.amazonaws.com:11211``

                - **Address** *(string) --*

                  The DNS hostname of the cache node.

                - **Port** *(integer) --*

                  The port number that the cache engine is listening on.

              - **ClientDownloadLandingPage** *(string) --*

                The URL of the web page where you can download the latest ElastiCache client library.

              - **CacheNodeType** *(string) --*

                The name of the compute and memory capacity node type for the cluster.

                The following node types are supported by ElastiCache. Generally speaking, the current
                generation types provide more memory and computational power at lower cost when compared to
                their equivalent previous generation counterparts.

                * General purpose:

                  * Current generation:   **M5 node types:**  ``cache.m5.large`` , ``cache.m5.xlarge`` ,
                  ``cache.m5.2xlarge`` , ``cache.m5.4xlarge`` , ``cache.m5.12xlarge`` ,
                  ``cache.m5.24xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` ,
                  ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``    **T2 node types:**
                   ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``

                  * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``    **M1
                  node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` ,
                  ``cache.m1.xlarge``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` ,
                  ``cache.m3.xlarge`` , ``cache.m3.2xlarge``

                * Compute optimized:

                  * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``

                * Memory optimized:

                  * Current generation:   **R5 node types:**  ``cache.r5.large`` , ``cache.r5.xlarge`` ,
                  ``cache.r5.2xlarge`` , ``cache.r5.4xlarge`` , ``cache.r5.12xlarge`` ,
                  ``cache.r5.24xlarge``    **R4 node types:**  ``cache.r4.large`` , ``cache.r4.xlarge`` ,
                  ``cache.r4.2xlarge`` , ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` , ``cache.r4.16xlarge``

                  * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` ,
                  ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``    **R3 node types:**  ``cache.r3.large`` ,
                  ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``

                 **Additional node type info**

                * All current generation instance types are created in Amazon VPC by default.

                * Redis append-only files (AOF) are not supported for T1 or T2 instances.

                * Redis Multi-AZ with automatic failover is not supported on T1 instances.

                * Redis configuration variables ``appendonly`` and ``appendfsync`` are not supported on
                Redis version 2.8.22 and later.

              - **Engine** *(string) --*

                The name of the cache engine (``memcached`` or ``redis`` ) to be used for this cluster.

              - **EngineVersion** *(string) --*

                The version of the cache engine that is used in this cluster.

              - **CacheClusterStatus** *(string) --*

                The current state of this cluster, one of the following values: ``available`` ,
                ``creating`` , ``deleted`` , ``deleting`` , ``incompatible-network`` , ``modifying`` ,
                ``rebooting cluster nodes`` , ``restore-failed`` , or ``snapshotting`` .

              - **NumCacheNodes** *(integer) --*

                The number of cache nodes in the cluster.

                For clusters running Redis, this value must be 1. For clusters running Memcached, this
                value must be between 1 and 20.

              - **PreferredAvailabilityZone** *(string) --*

                The name of the Availability Zone in which the cluster is located or "Multiple" if the
                cache nodes are located in different Availability Zones.

              - **CacheClusterCreateTime** *(datetime) --*

                The date and time when the cluster was created.

              - **PreferredMaintenanceWindow** *(string) --*

                Specifies the weekly time range during which maintenance on the cluster is performed. It is
                specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum
                maintenance window is a 60 minute period.

                Valid values for ``ddd`` are:

                * ``sun``

                * ``mon``

                * ``tue``

                * ``wed``

                * ``thu``

                * ``fri``

                * ``sat``

                Example: ``sun:23:00-mon:01:30``

              - **PendingModifiedValues** *(dict) --*

                A group of settings that are applied to the cluster in the future, or that are currently
                being applied.

                - **NumCacheNodes** *(integer) --*

                  The new number of cache nodes for the cluster.

                  For clusters running Redis, this value must be 1. For clusters running Memcached, this
                  value must be between 1 and 20.

                - **CacheNodeIdsToRemove** *(list) --*

                  A list of cache node IDs that are being removed (or will be removed) from the cluster. A
                  node ID is a 4-digit numeric identifier (0001, 0002, etc.).

                  - *(string) --*

                - **EngineVersion** *(string) --*

                  The new cache engine version that the cluster runs.

                - **CacheNodeType** *(string) --*

                  The cache node type that this cluster or replication group is scaled to.

                - **AuthTokenStatus** *(string) --*

                  The auth token status

              - **NotificationConfiguration** *(dict) --*

                Describes a notification topic and its status. Notification topics are used for publishing
                ElastiCache events to subscribers using Amazon Simple Notification Service (SNS).

                - **TopicArn** *(string) --*

                  The Amazon Resource Name (ARN) that identifies the topic.

                - **TopicStatus** *(string) --*

                  The current state of the topic.

              - **CacheSecurityGroups** *(list) --*

                A list of cache security group elements, composed of name and status sub-elements.

                - *(dict) --*

                  Represents a cluster's status within a particular cache security group.

                  - **CacheSecurityGroupName** *(string) --*

                    The name of the cache security group.

                  - **Status** *(string) --*

                    The membership status in the cache security group. The status changes when a cache
                    security group is modified, or when the cache security groups assigned to a cluster are
                    modified.

              - **CacheParameterGroup** *(dict) --*

                Status of the cache parameter group.

                - **CacheParameterGroupName** *(string) --*

                  The name of the cache parameter group.

                - **ParameterApplyStatus** *(string) --*

                  The status of parameter updates.

                - **CacheNodeIdsToReboot** *(list) --*

                  A list of the cache node IDs which need to be rebooted for parameter changes to be
                  applied. A node ID is a numeric identifier (0001, 0002, etc.).

                  - *(string) --*

              - **CacheSubnetGroupName** *(string) --*

                The name of the cache subnet group associated with the cluster.

              - **CacheNodes** *(list) --*

                A list of cache nodes that are members of the cluster.

                - *(dict) --*

                  Represents an individual cache node within a cluster. Each cache node runs its own
                  instance of the cluster's protocol-compliant caching software - either Memcached or Redis.

                  The following node types are supported by ElastiCache. Generally speaking, the current
                  generation types provide more memory and computational power at lower cost when compared
                  to their equivalent previous generation counterparts.

                  * General purpose:

                    * Current generation:   **M5 node types:**  ``cache.m5.large`` , ``cache.m5.xlarge`` ,
                    ``cache.m5.2xlarge`` , ``cache.m5.4xlarge`` , ``cache.m5.12xlarge`` ,
                    ``cache.m5.24xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` ,
                    ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``    **T2 node
                    types:**  ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``

                    * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``
                    **M1 node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` ,
                    ``cache.m1.xlarge``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` ,
                    ``cache.m3.xlarge`` , ``cache.m3.2xlarge``

                  * Compute optimized:

                    * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``

                  * Memory optimized:

                    * Current generation:   **R5 node types:**  ``cache.r5.large`` , ``cache.r5.xlarge`` ,
                    ``cache.r5.2xlarge`` , ``cache.r5.4xlarge`` , ``cache.r5.12xlarge`` ,
                    ``cache.r5.24xlarge``    **R4 node types:**  ``cache.r4.large`` , ``cache.r4.xlarge`` ,
                    ``cache.r4.2xlarge`` , ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` ,
                    ``cache.r4.16xlarge``

                    * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` ,
                    ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``    **R3 node types:**  ``cache.r3.large`` ,
                    ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``

                   **Additional node type info**

                  * All current generation instance types are created in Amazon VPC by default.

                  * Redis append-only files (AOF) are not supported for T1 or T2 instances.

                  * Redis Multi-AZ with automatic failover is not supported on T1 instances.

                  * Redis configuration variables ``appendonly`` and ``appendfsync`` are not supported on
                  Redis version 2.8.22 and later.

                  - **CacheNodeId** *(string) --*

                    The cache node identifier. A node ID is a numeric identifier (0001, 0002, etc.). The
                    combination of cluster ID and node ID uniquely identifies every cache node used in a
                    customer's AWS account.

                  - **CacheNodeStatus** *(string) --*

                    The current state of this cache node.

                  - **CacheNodeCreateTime** *(datetime) --*

                    The date and time when the cache node was created.

                  - **Endpoint** *(dict) --*

                    The hostname for connecting to this cache node.

                    - **Address** *(string) --*

                      The DNS hostname of the cache node.

                    - **Port** *(integer) --*

                      The port number that the cache engine is listening on.

                  - **ParameterGroupStatus** *(string) --*

                    The status of the parameter group applied to this cache node.

                  - **SourceCacheNodeId** *(string) --*

                    The ID of the primary node to which this read replica node is synchronized. If this
                    field is empty, this node is not associated with a primary cluster.

                  - **CustomerAvailabilityZone** *(string) --*

                    The Availability Zone where this node was created and now resides.

              - **AutoMinorVersionUpgrade** *(boolean) --*

                This parameter is currently disabled.

              - **SecurityGroups** *(list) --*

                A list of VPC Security Groups associated with the cluster.

                - *(dict) --*

                  Represents a single cache security group and its status.

                  - **SecurityGroupId** *(string) --*

                    The identifier of the cache security group.

                  - **Status** *(string) --*

                    The status of the cache security group membership. The status changes whenever a cache
                    security group is modified, or when the cache security groups assigned to a cluster are
                    modified.

              - **ReplicationGroupId** *(string) --*

                The replication group to which this cluster belongs. If this field is empty, the cluster is
                not associated with any replication group.

              - **SnapshotRetentionLimit** *(integer) --*

                The number of days for which ElastiCache retains automatic cluster snapshots before
                deleting them. For example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot that was
                taken today is retained for 5 days before being deleted.

                .. warning::

                  If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.

              - **SnapshotWindow** *(string) --*

                The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of
                your cluster.

                Example: ``05:00-09:00``

              - **AuthTokenEnabled** *(boolean) --*

                A flag that enables using an ``AuthToken`` (password) when issuing Redis commands.

                Default: ``false``

              - **AuthTokenLastModifiedDate** *(datetime) --*

                The date the auth token was last modified

              - **TransitEncryptionEnabled** *(boolean) --*

                A flag that enables in-transit encryption when set to ``true`` .

                You cannot modify the value of ``TransitEncryptionEnabled`` after the cluster is created.
                To enable in-transit encryption on a cluster you must set ``TransitEncryptionEnabled`` to
                ``true`` when you create a cluster.

                 **Required:** Only available when creating a replication group in an Amazon VPC using
                 redis version ``3.2.6`` , ``4.x`` or later.

                Default: ``false``

              - **AtRestEncryptionEnabled** *(boolean) --*

                A flag that enables encryption at-rest when set to ``true`` .

                You cannot modify the value of ``AtRestEncryptionEnabled`` after the cluster is created. To
                enable at-rest encryption on a cluster you must set ``AtRestEncryptionEnabled`` to ``true``
                when you create a cluster.

                 **Required:** Only available when creating a replication group in an Amazon VPC using
                 redis version ``3.2.6`` , ``4.x`` or later.

                Default: ``false``

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_cache_parameter_group(
        self,
        CacheParameterGroupName: str,
        ParameterNameValues: List[
            ClientModifyCacheParameterGroupParameterNameValuesTypeDef
        ],
    ) -> ClientModifyCacheParameterGroupResponseTypeDef:
        """
        Modifies the parameters of a cache parameter group. You can modify up to 20 parameters in a single
        request by submitting a list parameter name and value pairs.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/ModifyCacheParameterGroup>`_

        **Request Syntax**
        ::

          response = client.modify_cache_parameter_group(
              CacheParameterGroupName='string',
              ParameterNameValues=[
                  {
                      'ParameterName': 'string',
                      'ParameterValue': 'string'
                  },
              ]
          )
        :type CacheParameterGroupName: string
        :param CacheParameterGroupName: **[REQUIRED]**

          The name of the cache parameter group to modify.

        :type ParameterNameValues: list
        :param ParameterNameValues: **[REQUIRED]**

          An array of parameter names and values for the parameter update. You must supply at least one
          parameter name and value; subsequent arguments are optional. A maximum of 20 parameters may be
          modified per request.

          - *(dict) --*

            Describes a name-value pair that is used to update the value of a parameter.

            - **ParameterName** *(string) --*

              The name of the parameter.

            - **ParameterValue** *(string) --*

              The value of the parameter.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'CacheParameterGroupName': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Represents the output of one of the following operations:

            * ``ModifyCacheParameterGroup``

            * ``ResetCacheParameterGroup``

            - **CacheParameterGroupName** *(string) --*

              The name of the cache parameter group.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_cache_subnet_group(
        self,
        CacheSubnetGroupName: str,
        CacheSubnetGroupDescription: str = None,
        SubnetIds: List[str] = None,
    ) -> ClientModifyCacheSubnetGroupResponseTypeDef:
        """
        Modifies an existing cache subnet group.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/ModifyCacheSubnetGroup>`_

        **Request Syntax**
        ::

          response = client.modify_cache_subnet_group(
              CacheSubnetGroupName='string',
              CacheSubnetGroupDescription='string',
              SubnetIds=[
                  'string',
              ]
          )
        :type CacheSubnetGroupName: string
        :param CacheSubnetGroupName: **[REQUIRED]**

          The name for the cache subnet group. This value is stored as a lowercase string.

          Constraints: Must contain no more than 255 alphanumeric characters or hyphens.

          Example: ``mysubnetgroup``

        :type CacheSubnetGroupDescription: string
        :param CacheSubnetGroupDescription:

          A description of the cache subnet group.

        :type SubnetIds: list
        :param SubnetIds:

          The EC2 subnet IDs for the cache subnet group.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'CacheSubnetGroup': {
                    'CacheSubnetGroupName': 'string',
                    'CacheSubnetGroupDescription': 'string',
                    'VpcId': 'string',
                    'Subnets': [
                        {
                            'SubnetIdentifier': 'string',
                            'SubnetAvailabilityZone': {
                                'Name': 'string'
                            }
                        },
                    ]
                }
            }
          **Response Structure**

          - *(dict) --*

            - **CacheSubnetGroup** *(dict) --*

              Represents the output of one of the following operations:

              * ``CreateCacheSubnetGroup``

              * ``ModifyCacheSubnetGroup``

              - **CacheSubnetGroupName** *(string) --*

                The name of the cache subnet group.

              - **CacheSubnetGroupDescription** *(string) --*

                The description of the cache subnet group.

              - **VpcId** *(string) --*

                The Amazon Virtual Private Cloud identifier (VPC ID) of the cache subnet group.

              - **Subnets** *(list) --*

                A list of subnets associated with the cache subnet group.

                - *(dict) --*

                  Represents the subnet associated with a cluster. This parameter refers to subnets defined
                  in Amazon Virtual Private Cloud (Amazon VPC) and used with ElastiCache.

                  - **SubnetIdentifier** *(string) --*

                    The unique identifier for the subnet.

                  - **SubnetAvailabilityZone** *(dict) --*

                    The Availability Zone associated with the subnet.

                    - **Name** *(string) --*

                      The name of the Availability Zone.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_replication_group(
        self,
        ReplicationGroupId: str,
        ReplicationGroupDescription: str = None,
        PrimaryClusterId: str = None,
        SnapshottingClusterId: str = None,
        AutomaticFailoverEnabled: bool = None,
        NodeGroupId: str = None,
        CacheSecurityGroupNames: List[str] = None,
        SecurityGroupIds: List[str] = None,
        PreferredMaintenanceWindow: str = None,
        NotificationTopicArn: str = None,
        CacheParameterGroupName: str = None,
        NotificationTopicStatus: str = None,
        ApplyImmediately: bool = None,
        EngineVersion: str = None,
        AutoMinorVersionUpgrade: bool = None,
        SnapshotRetentionLimit: int = None,
        SnapshotWindow: str = None,
        CacheNodeType: str = None,
        AuthToken: str = None,
        AuthTokenUpdateStrategy: str = None,
    ) -> ClientModifyReplicationGroupResponseTypeDef:
        """
        Modifies the settings for a replication group.

        For Redis (cluster mode enabled) clusters, this operation cannot be used to change a cluster's node
        type or engine version. For more information, see:

        * `Scaling for Amazon ElastiCache for Redis (cluster mode enabled)
        <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/scaling-redis-cluster-mode-enabled.html>`__
        in the ElastiCache User Guide

        * `ModifyReplicationGroupShardConfiguration
        <https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_ModifyReplicationGroupShardConfiguration.html>`__
        in the ElastiCache API Reference

        .. note::

          This operation is valid for Redis only.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/ModifyReplicationGroup>`_

        **Request Syntax**
        ::

          response = client.modify_replication_group(
              ReplicationGroupId='string',
              ReplicationGroupDescription='string',
              PrimaryClusterId='string',
              SnapshottingClusterId='string',
              AutomaticFailoverEnabled=True|False,
              NodeGroupId='string',
              CacheSecurityGroupNames=[
                  'string',
              ],
              SecurityGroupIds=[
                  'string',
              ],
              PreferredMaintenanceWindow='string',
              NotificationTopicArn='string',
              CacheParameterGroupName='string',
              NotificationTopicStatus='string',
              ApplyImmediately=True|False,
              EngineVersion='string',
              AutoMinorVersionUpgrade=True|False,
              SnapshotRetentionLimit=123,
              SnapshotWindow='string',
              CacheNodeType='string',
              AuthToken='string',
              AuthTokenUpdateStrategy='SET'|'ROTATE'
          )
        :type ReplicationGroupId: string
        :param ReplicationGroupId: **[REQUIRED]**

          The identifier of the replication group to modify.

        :type ReplicationGroupDescription: string
        :param ReplicationGroupDescription:

          A description for the replication group. Maximum length is 255 characters.

        :type PrimaryClusterId: string
        :param PrimaryClusterId:

          For replication groups with a single primary, if this parameter is specified, ElastiCache
          promotes the specified cluster in the specified replication group to the primary role. The nodes
          of all other clusters in the replication group are read replicas.

        :type SnapshottingClusterId: string
        :param SnapshottingClusterId:

          The cluster ID that is used as the daily snapshot source for the replication group. This
          parameter cannot be set for Redis (cluster mode enabled) replication groups.

        :type AutomaticFailoverEnabled: boolean
        :param AutomaticFailoverEnabled:

          Determines whether a read replica is automatically promoted to read/write primary if the existing
          primary encounters a failure.

          Valid values: ``true`` | ``false``

          Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

          * Redis versions earlier than 2.8.6.

          * Redis (cluster mode disabled): T1 node types.

          * Redis (cluster mode enabled): T1 node types.

        :type NodeGroupId: string
        :param NodeGroupId:

          Deprecated. This parameter is not used.

        :type CacheSecurityGroupNames: list
        :param CacheSecurityGroupNames:

          A list of cache security group names to authorize for the clusters in this replication group.
          This change is asynchronously applied as soon as possible.

          This parameter can be used only with replication group containing clusters running outside of an
          Amazon Virtual Private Cloud (Amazon VPC).

          Constraints: Must contain no more than 255 alphanumeric characters. Must not be ``Default`` .

          - *(string) --*

        :type SecurityGroupIds: list
        :param SecurityGroupIds:

          Specifies the VPC Security Groups associated with the clusters in the replication group.

          This parameter can be used only with replication group containing clusters running in an Amazon
          Virtual Private Cloud (Amazon VPC).

          - *(string) --*

        :type PreferredMaintenanceWindow: string
        :param PreferredMaintenanceWindow:

          Specifies the weekly time range during which maintenance on the cluster is performed. It is
          specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum
          maintenance window is a 60 minute period.

          Valid values for ``ddd`` are:

          * ``sun``

          * ``mon``

          * ``tue``

          * ``wed``

          * ``thu``

          * ``fri``

          * ``sat``

          Example: ``sun:23:00-mon:01:30``

        :type NotificationTopicArn: string
        :param NotificationTopicArn:

          The Amazon Resource Name (ARN) of the Amazon SNS topic to which notifications are sent.

          .. note::

            The Amazon SNS topic owner must be same as the replication group owner.

        :type CacheParameterGroupName: string
        :param CacheParameterGroupName:

          The name of the cache parameter group to apply to all of the clusters in this replication group.
          This change is asynchronously applied as soon as possible for parameters when the
          ``ApplyImmediately`` parameter is specified as ``true`` for this request.

        :type NotificationTopicStatus: string
        :param NotificationTopicStatus:

          The status of the Amazon SNS notification topic for the replication group. Notifications are sent
          only if the status is ``active`` .

          Valid values: ``active`` | ``inactive``

        :type ApplyImmediately: boolean
        :param ApplyImmediately:

          If ``true`` , this parameter causes the modifications in this request and any pending
          modifications to be applied, asynchronously and as soon as possible, regardless of the
          ``PreferredMaintenanceWindow`` setting for the replication group.

          If ``false`` , changes to the nodes in the replication group are applied on the next maintenance
          reboot, or the next failure reboot, whichever occurs first.

          Valid values: ``true`` | ``false``

          Default: ``false``

        :type EngineVersion: string
        :param EngineVersion:

          The upgraded version of the cache engine to be run on the clusters in the replication group.

           **Important:** You can upgrade to a newer engine version (see `Selecting a Cache Engine and
           Version
           <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/SelectEngine.html#VersionManagement>`__
           ), but you cannot downgrade to an earlier engine version. If you want to use an earlier engine
           version, you must delete the existing replication group and create it anew with the earlier
           engine version.

        :type AutoMinorVersionUpgrade: boolean
        :param AutoMinorVersionUpgrade:

          This parameter is currently disabled.

        :type SnapshotRetentionLimit: integer
        :param SnapshotRetentionLimit:

          The number of days for which ElastiCache retains automatic node group (shard) snapshots before
          deleting them. For example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot that was taken
          today is retained for 5 days before being deleted.

           **Important** If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.

        :type SnapshotWindow: string
        :param SnapshotWindow:

          The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of the node
          group (shard) specified by ``SnapshottingClusterId`` .

          Example: ``05:00-09:00``

          If you do not specify this parameter, ElastiCache automatically chooses an appropriate time range.

        :type CacheNodeType: string
        :param CacheNodeType:

          A valid cache node type that you want to scale this replication group to.

        :type AuthToken: string
        :param AuthToken:

          Reserved parameter. The password used to access a password protected server. This parameter must
          be specified with the ``auth-token-update-strategy`` parameter. Password constraints:

          * Must be only printable ASCII characters

          * Must be at least 16 characters and no more than 128 characters in length

          * Cannot contain any of the following characters: '/', '"', or '@', '%'

          For more information, see AUTH password at `AUTH <http://redis.io/commands/AUTH>`__ .

        :type AuthTokenUpdateStrategy: string
        :param AuthTokenUpdateStrategy:

          Specifies the strategy to use to update the AUTH token. This parameter must be specified with the
          ``auth-token`` parameter. Possible values:

          * Rotate

          * Set

          For more information, see `Authenticating Users with Redis AUTH
          <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/auth.html>`__

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ReplicationGroup': {
                    'ReplicationGroupId': 'string',
                    'Description': 'string',
                    'Status': 'string',
                    'PendingModifiedValues': {
                        'PrimaryClusterId': 'string',
                        'AutomaticFailoverStatus': 'enabled'|'disabled',
                        'Resharding': {
                            'SlotMigration': {
                                'ProgressPercentage': 123.0
                            }
                        },
                        'AuthTokenStatus': 'SETTING'|'ROTATING'
                    },
                    'MemberClusters': [
                        'string',
                    ],
                    'NodeGroups': [
                        {
                            'NodeGroupId': 'string',
                            'Status': 'string',
                            'PrimaryEndpoint': {
                                'Address': 'string',
                                'Port': 123
                            },
                            'ReaderEndpoint': {
                                'Address': 'string',
                                'Port': 123
                            },
                            'Slots': 'string',
                            'NodeGroupMembers': [
                                {
                                    'CacheClusterId': 'string',
                                    'CacheNodeId': 'string',
                                    'ReadEndpoint': {
                                        'Address': 'string',
                                        'Port': 123
                                    },
                                    'PreferredAvailabilityZone': 'string',
                                    'CurrentRole': 'string'
                                },
                            ]
                        },
                    ],
                    'SnapshottingClusterId': 'string',
                    'AutomaticFailover': 'enabled'|'disabled'|'enabling'|'disabling',
                    'ConfigurationEndpoint': {
                        'Address': 'string',
                        'Port': 123
                    },
                    'SnapshotRetentionLimit': 123,
                    'SnapshotWindow': 'string',
                    'ClusterEnabled': True|False,
                    'CacheNodeType': 'string',
                    'AuthTokenEnabled': True|False,
                    'AuthTokenLastModifiedDate': datetime(2015, 1, 1),
                    'TransitEncryptionEnabled': True|False,
                    'AtRestEncryptionEnabled': True|False,
                    'KmsKeyId': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **ReplicationGroup** *(dict) --*

              Contains all of the attributes of a specific Redis replication group.

              - **ReplicationGroupId** *(string) --*

                The identifier for the replication group.

              - **Description** *(string) --*

                The user supplied description of the replication group.

              - **Status** *(string) --*

                The current state of this replication group - ``creating`` , ``available`` , ``modifying``
                , ``deleting`` , ``create-failed`` , ``snapshotting`` .

              - **PendingModifiedValues** *(dict) --*

                A group of settings to be applied to the replication group, either immediately or during
                the next maintenance window.

                - **PrimaryClusterId** *(string) --*

                  The primary cluster ID that is applied immediately (if ``--apply-immediately`` was
                  specified), or during the next maintenance window.

                - **AutomaticFailoverStatus** *(string) --*

                  Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

                  Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

                  * Redis versions earlier than 2.8.6.

                  * Redis (cluster mode disabled): T1 node types.

                  * Redis (cluster mode enabled): T1 node types.

                - **Resharding** *(dict) --*

                  The status of an online resharding operation.

                  - **SlotMigration** *(dict) --*

                    Represents the progress of an online resharding operation.

                    - **ProgressPercentage** *(float) --*

                      The percentage of the slot migration that is complete.

                - **AuthTokenStatus** *(string) --*

                  The auth token status

              - **MemberClusters** *(list) --*

                The names of all the cache clusters that are part of this replication group.

                - *(string) --*

              - **NodeGroups** *(list) --*

                A list of node groups in this replication group. For Redis (cluster mode disabled)
                replication groups, this is a single-element list. For Redis (cluster mode enabled)
                replication groups, the list contains an entry for each node group (shard).

                - *(dict) --*

                  Represents a collection of cache nodes in a replication group. One node in the node group
                  is the read/write primary node. All the other nodes are read-only Replica nodes.

                  - **NodeGroupId** *(string) --*

                    The identifier for the node group (shard). A Redis (cluster mode disabled) replication
                    group contains only 1 node group; therefore, the node group ID is 0001. A Redis
                    (cluster mode enabled) replication group contains 1 to 90 node groups numbered 0001 to
                    0090. Optionally, the user can provide the id for a node group.

                  - **Status** *(string) --*

                    The current state of this replication group - ``creating`` , ``available`` , etc.

                  - **PrimaryEndpoint** *(dict) --*

                    The endpoint of the primary node in this node group (shard).

                    - **Address** *(string) --*

                      The DNS hostname of the cache node.

                    - **Port** *(integer) --*

                      The port number that the cache engine is listening on.

                  - **ReaderEndpoint** *(dict) --*

                    The endpoint of the replica nodes in this node group (shard).

                    - **Address** *(string) --*

                      The DNS hostname of the cache node.

                    - **Port** *(integer) --*

                      The port number that the cache engine is listening on.

                  - **Slots** *(string) --*

                    The keyspace for this node group (shard).

                  - **NodeGroupMembers** *(list) --*

                    A list containing information about individual nodes within the node group (shard).

                    - *(dict) --*

                      Represents a single node within a node group (shard).

                      - **CacheClusterId** *(string) --*

                        The ID of the cluster to which the node belongs.

                      - **CacheNodeId** *(string) --*

                        The ID of the node within its cluster. A node ID is a numeric identifier (0001,
                        0002, etc.).

                      - **ReadEndpoint** *(dict) --*

                        The information required for client programs to connect to a node for read
                        operations. The read endpoint is only applicable on Redis (cluster mode disabled)
                        clusters.

                        - **Address** *(string) --*

                          The DNS hostname of the cache node.

                        - **Port** *(integer) --*

                          The port number that the cache engine is listening on.

                      - **PreferredAvailabilityZone** *(string) --*

                        The name of the Availability Zone in which the node is located.

                      - **CurrentRole** *(string) --*

                        The role that is currently assigned to the node - ``primary`` or ``replica`` . This
                        member is only applicable for Redis (cluster mode disabled) replication groups.

              - **SnapshottingClusterId** *(string) --*

                The cluster ID that is used as the daily snapshot source for the replication group.

              - **AutomaticFailover** *(string) --*

                Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

                Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

                * Redis versions earlier than 2.8.6.

                * Redis (cluster mode disabled): T1 node types.

                * Redis (cluster mode enabled): T1 node types.

              - **ConfigurationEndpoint** *(dict) --*

                The configuration endpoint for this replication group. Use the configuration endpoint to
                connect to this replication group.

                - **Address** *(string) --*

                  The DNS hostname of the cache node.

                - **Port** *(integer) --*

                  The port number that the cache engine is listening on.

              - **SnapshotRetentionLimit** *(integer) --*

                The number of days for which ElastiCache retains automatic cluster snapshots before
                deleting them. For example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot that was
                taken today is retained for 5 days before being deleted.

                .. warning::

                  If the value of ``SnapshotRetentionLimit`` is set to zero (0), backups are turned off.

              - **SnapshotWindow** *(string) --*

                The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of
                your node group (shard).

                Example: ``05:00-09:00``

                If you do not specify this parameter, ElastiCache automatically chooses an appropriate time
                range.

                .. note::

                  This parameter is only valid if the ``Engine`` parameter is ``redis`` .

              - **ClusterEnabled** *(boolean) --*

                A flag indicating whether or not this replication group is cluster enabled; i.e., whether
                its data can be partitioned across multiple shards (API/CLI: node groups).

                Valid values: ``true`` | ``false``

              - **CacheNodeType** *(string) --*

                The name of the compute and memory capacity node type for each node in the replication
                group.

              - **AuthTokenEnabled** *(boolean) --*

                A flag that enables using an ``AuthToken`` (password) when issuing Redis commands.

                Default: ``false``

              - **AuthTokenLastModifiedDate** *(datetime) --*

                The date the auth token was last modified

              - **TransitEncryptionEnabled** *(boolean) --*

                A flag that enables in-transit encryption when set to ``true`` .

                You cannot modify the value of ``TransitEncryptionEnabled`` after the cluster is created.
                To enable in-transit encryption on a cluster you must set ``TransitEncryptionEnabled`` to
                ``true`` when you create a cluster.

                 **Required:** Only available when creating a replication group in an Amazon VPC using
                 redis version ``3.2.6`` , ``4.x`` or later.

                Default: ``false``

              - **AtRestEncryptionEnabled** *(boolean) --*

                A flag that enables encryption at-rest when set to ``true`` .

                You cannot modify the value of ``AtRestEncryptionEnabled`` after the cluster is created. To
                enable encryption at-rest on a cluster you must set ``AtRestEncryptionEnabled`` to ``true``
                when you create a cluster.

                 **Required:** Only available when creating a replication group in an Amazon VPC using
                 redis version ``3.2.6`` , ``4.x`` or later.

                Default: ``false``

              - **KmsKeyId** *(string) --*

                The ID of the KMS key used to encrypt the disk in the cluster.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_replication_group_shard_configuration(
        self,
        ReplicationGroupId: str,
        NodeGroupCount: int,
        ApplyImmediately: bool,
        ReshardingConfiguration: List[
            ClientModifyReplicationGroupShardConfigurationReshardingConfigurationTypeDef
        ] = None,
        NodeGroupsToRemove: List[str] = None,
        NodeGroupsToRetain: List[str] = None,
    ) -> ClientModifyReplicationGroupShardConfigurationResponseTypeDef:
        """
        Modifies a replication group's shards (node groups) by allowing you to add shards, remove shards,
        or rebalance the keyspaces among exisiting shards.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/ModifyReplicationGroupShardConfiguration>`_
        <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/ModifyReplicationGroupShardConfiguration>`_

        **Request Syntax**
        ::

          response = client.modify_replication_group_shard_configuration(
              ReplicationGroupId='string',
              NodeGroupCount=123,
              ApplyImmediately=True|False,
              ReshardingConfiguration=[
                  {
                      'NodeGroupId': 'string',
                      'PreferredAvailabilityZones': [
                          'string',
                      ]
                  },
              ],
              NodeGroupsToRemove=[
                  'string',
              ],
              NodeGroupsToRetain=[
                  'string',
              ]
          )
        :type ReplicationGroupId: string
        :param ReplicationGroupId: **[REQUIRED]**

          The name of the Redis (cluster mode enabled) cluster (replication group) on which the shards are
          to be configured.

        :type NodeGroupCount: integer
        :param NodeGroupCount: **[REQUIRED]**

          The number of node groups (shards) that results from the modification of the shard configuration.

        :type ApplyImmediately: boolean
        :param ApplyImmediately: **[REQUIRED]**

          Indicates that the shard reconfiguration process begins immediately. At present, the only
          permitted value for this parameter is ``true`` .

          Value: true

        :type ReshardingConfiguration: list
        :param ReshardingConfiguration:

          Specifies the preferred availability zones for each node group in the cluster. If the value of
          ``NodeGroupCount`` is greater than the current number of node groups (shards), you can use this
          parameter to specify the preferred availability zones of the cluster's shards. If you omit this
          parameter ElastiCache selects availability zones for you.

          You can specify this parameter only if the value of ``NodeGroupCount`` is greater than the
          current number of node groups (shards).

          - *(dict) --*

            A list of ``PreferredAvailabilityZones`` objects that specifies the configuration of a node
            group in the resharded cluster.

            - **NodeGroupId** *(string) --*

              Either the ElastiCache for Redis supplied 4-digit id or a user supplied id for the node group
              these configuration values apply to.

            - **PreferredAvailabilityZones** *(list) --*

              A list of preferred availability zones for the nodes in this cluster.

              - *(string) --*

        :type NodeGroupsToRemove: list
        :param NodeGroupsToRemove:

          If the value of ``NodeGroupCount`` is less than the current number of node groups (shards), then
          either ``NodeGroupsToRemove`` or ``NodeGroupsToRetain`` is required. ``NodeGroupsToRemove`` is a
          list of ``NodeGroupId`` s to remove from the cluster.

          ElastiCache for Redis will attempt to remove all node groups listed by ``NodeGroupsToRemove``
          from the cluster.

          - *(string) --*

        :type NodeGroupsToRetain: list
        :param NodeGroupsToRetain:

          If the value of ``NodeGroupCount`` is less than the current number of node groups (shards), then
          either ``NodeGroupsToRemove`` or ``NodeGroupsToRetain`` is required. ``NodeGroupsToRetain`` is a
          list of ``NodeGroupId`` s to retain in the cluster.

          ElastiCache for Redis will attempt to remove all node groups except those listed by
          ``NodeGroupsToRetain`` from the cluster.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ReplicationGroup': {
                    'ReplicationGroupId': 'string',
                    'Description': 'string',
                    'Status': 'string',
                    'PendingModifiedValues': {
                        'PrimaryClusterId': 'string',
                        'AutomaticFailoverStatus': 'enabled'|'disabled',
                        'Resharding': {
                            'SlotMigration': {
                                'ProgressPercentage': 123.0
                            }
                        },
                        'AuthTokenStatus': 'SETTING'|'ROTATING'
                    },
                    'MemberClusters': [
                        'string',
                    ],
                    'NodeGroups': [
                        {
                            'NodeGroupId': 'string',
                            'Status': 'string',
                            'PrimaryEndpoint': {
                                'Address': 'string',
                                'Port': 123
                            },
                            'ReaderEndpoint': {
                                'Address': 'string',
                                'Port': 123
                            },
                            'Slots': 'string',
                            'NodeGroupMembers': [
                                {
                                    'CacheClusterId': 'string',
                                    'CacheNodeId': 'string',
                                    'ReadEndpoint': {
                                        'Address': 'string',
                                        'Port': 123
                                    },
                                    'PreferredAvailabilityZone': 'string',
                                    'CurrentRole': 'string'
                                },
                            ]
                        },
                    ],
                    'SnapshottingClusterId': 'string',
                    'AutomaticFailover': 'enabled'|'disabled'|'enabling'|'disabling',
                    'ConfigurationEndpoint': {
                        'Address': 'string',
                        'Port': 123
                    },
                    'SnapshotRetentionLimit': 123,
                    'SnapshotWindow': 'string',
                    'ClusterEnabled': True|False,
                    'CacheNodeType': 'string',
                    'AuthTokenEnabled': True|False,
                    'AuthTokenLastModifiedDate': datetime(2015, 1, 1),
                    'TransitEncryptionEnabled': True|False,
                    'AtRestEncryptionEnabled': True|False,
                    'KmsKeyId': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **ReplicationGroup** *(dict) --*

              Contains all of the attributes of a specific Redis replication group.

              - **ReplicationGroupId** *(string) --*

                The identifier for the replication group.

              - **Description** *(string) --*

                The user supplied description of the replication group.

              - **Status** *(string) --*

                The current state of this replication group - ``creating`` , ``available`` , ``modifying``
                , ``deleting`` , ``create-failed`` , ``snapshotting`` .

              - **PendingModifiedValues** *(dict) --*

                A group of settings to be applied to the replication group, either immediately or during
                the next maintenance window.

                - **PrimaryClusterId** *(string) --*

                  The primary cluster ID that is applied immediately (if ``--apply-immediately`` was
                  specified), or during the next maintenance window.

                - **AutomaticFailoverStatus** *(string) --*

                  Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

                  Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

                  * Redis versions earlier than 2.8.6.

                  * Redis (cluster mode disabled): T1 node types.

                  * Redis (cluster mode enabled): T1 node types.

                - **Resharding** *(dict) --*

                  The status of an online resharding operation.

                  - **SlotMigration** *(dict) --*

                    Represents the progress of an online resharding operation.

                    - **ProgressPercentage** *(float) --*

                      The percentage of the slot migration that is complete.

                - **AuthTokenStatus** *(string) --*

                  The auth token status

              - **MemberClusters** *(list) --*

                The names of all the cache clusters that are part of this replication group.

                - *(string) --*

              - **NodeGroups** *(list) --*

                A list of node groups in this replication group. For Redis (cluster mode disabled)
                replication groups, this is a single-element list. For Redis (cluster mode enabled)
                replication groups, the list contains an entry for each node group (shard).

                - *(dict) --*

                  Represents a collection of cache nodes in a replication group. One node in the node group
                  is the read/write primary node. All the other nodes are read-only Replica nodes.

                  - **NodeGroupId** *(string) --*

                    The identifier for the node group (shard). A Redis (cluster mode disabled) replication
                    group contains only 1 node group; therefore, the node group ID is 0001. A Redis
                    (cluster mode enabled) replication group contains 1 to 90 node groups numbered 0001 to
                    0090. Optionally, the user can provide the id for a node group.

                  - **Status** *(string) --*

                    The current state of this replication group - ``creating`` , ``available`` , etc.

                  - **PrimaryEndpoint** *(dict) --*

                    The endpoint of the primary node in this node group (shard).

                    - **Address** *(string) --*

                      The DNS hostname of the cache node.

                    - **Port** *(integer) --*

                      The port number that the cache engine is listening on.

                  - **ReaderEndpoint** *(dict) --*

                    The endpoint of the replica nodes in this node group (shard).

                    - **Address** *(string) --*

                      The DNS hostname of the cache node.

                    - **Port** *(integer) --*

                      The port number that the cache engine is listening on.

                  - **Slots** *(string) --*

                    The keyspace for this node group (shard).

                  - **NodeGroupMembers** *(list) --*

                    A list containing information about individual nodes within the node group (shard).

                    - *(dict) --*

                      Represents a single node within a node group (shard).

                      - **CacheClusterId** *(string) --*

                        The ID of the cluster to which the node belongs.

                      - **CacheNodeId** *(string) --*

                        The ID of the node within its cluster. A node ID is a numeric identifier (0001,
                        0002, etc.).

                      - **ReadEndpoint** *(dict) --*

                        The information required for client programs to connect to a node for read
                        operations. The read endpoint is only applicable on Redis (cluster mode disabled)
                        clusters.

                        - **Address** *(string) --*

                          The DNS hostname of the cache node.

                        - **Port** *(integer) --*

                          The port number that the cache engine is listening on.

                      - **PreferredAvailabilityZone** *(string) --*

                        The name of the Availability Zone in which the node is located.

                      - **CurrentRole** *(string) --*

                        The role that is currently assigned to the node - ``primary`` or ``replica`` . This
                        member is only applicable for Redis (cluster mode disabled) replication groups.

              - **SnapshottingClusterId** *(string) --*

                The cluster ID that is used as the daily snapshot source for the replication group.

              - **AutomaticFailover** *(string) --*

                Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

                Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

                * Redis versions earlier than 2.8.6.

                * Redis (cluster mode disabled): T1 node types.

                * Redis (cluster mode enabled): T1 node types.

              - **ConfigurationEndpoint** *(dict) --*

                The configuration endpoint for this replication group. Use the configuration endpoint to
                connect to this replication group.

                - **Address** *(string) --*

                  The DNS hostname of the cache node.

                - **Port** *(integer) --*

                  The port number that the cache engine is listening on.

              - **SnapshotRetentionLimit** *(integer) --*

                The number of days for which ElastiCache retains automatic cluster snapshots before
                deleting them. For example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot that was
                taken today is retained for 5 days before being deleted.

                .. warning::

                  If the value of ``SnapshotRetentionLimit`` is set to zero (0), backups are turned off.

              - **SnapshotWindow** *(string) --*

                The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of
                your node group (shard).

                Example: ``05:00-09:00``

                If you do not specify this parameter, ElastiCache automatically chooses an appropriate time
                range.

                .. note::

                  This parameter is only valid if the ``Engine`` parameter is ``redis`` .

              - **ClusterEnabled** *(boolean) --*

                A flag indicating whether or not this replication group is cluster enabled; i.e., whether
                its data can be partitioned across multiple shards (API/CLI: node groups).

                Valid values: ``true`` | ``false``

              - **CacheNodeType** *(string) --*

                The name of the compute and memory capacity node type for each node in the replication
                group.

              - **AuthTokenEnabled** *(boolean) --*

                A flag that enables using an ``AuthToken`` (password) when issuing Redis commands.

                Default: ``false``

              - **AuthTokenLastModifiedDate** *(datetime) --*

                The date the auth token was last modified

              - **TransitEncryptionEnabled** *(boolean) --*

                A flag that enables in-transit encryption when set to ``true`` .

                You cannot modify the value of ``TransitEncryptionEnabled`` after the cluster is created.
                To enable in-transit encryption on a cluster you must set ``TransitEncryptionEnabled`` to
                ``true`` when you create a cluster.

                 **Required:** Only available when creating a replication group in an Amazon VPC using
                 redis version ``3.2.6`` , ``4.x`` or later.

                Default: ``false``

              - **AtRestEncryptionEnabled** *(boolean) --*

                A flag that enables encryption at-rest when set to ``true`` .

                You cannot modify the value of ``AtRestEncryptionEnabled`` after the cluster is created. To
                enable encryption at-rest on a cluster you must set ``AtRestEncryptionEnabled`` to ``true``
                when you create a cluster.

                 **Required:** Only available when creating a replication group in an Amazon VPC using
                 redis version ``3.2.6`` , ``4.x`` or later.

                Default: ``false``

              - **KmsKeyId** *(string) --*

                The ID of the KMS key used to encrypt the disk in the cluster.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def purchase_reserved_cache_nodes_offering(
        self,
        ReservedCacheNodesOfferingId: str,
        ReservedCacheNodeId: str = None,
        CacheNodeCount: int = None,
    ) -> ClientPurchaseReservedCacheNodesOfferingResponseTypeDef:
        """
        Allows you to purchase a reserved cache node offering.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/PurchaseReservedCacheNodesOffering>`_
        <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/PurchaseReservedCacheNodesOffering>`_

        **Request Syntax**
        ::

          response = client.purchase_reserved_cache_nodes_offering(
              ReservedCacheNodesOfferingId='string',
              ReservedCacheNodeId='string',
              CacheNodeCount=123
          )
        :type ReservedCacheNodesOfferingId: string
        :param ReservedCacheNodesOfferingId: **[REQUIRED]**

          The ID of the reserved cache node offering to purchase.

          Example: ``438012d3-4052-4cc7-b2e3-8d3372e0e706``

        :type ReservedCacheNodeId: string
        :param ReservedCacheNodeId:

          A customer-specified identifier to track this reservation.

          .. note::

            The Reserved Cache Node ID is an unique customer-specified identifier to track this
            reservation. If this parameter is not specified, ElastiCache automatically generates an
            identifier for the reservation.

          Example: myreservationID

        :type CacheNodeCount: integer
        :param CacheNodeCount:

          The number of cache node instances to reserve.

          Default: ``1``

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ReservedCacheNode': {
                    'ReservedCacheNodeId': 'string',
                    'ReservedCacheNodesOfferingId': 'string',
                    'CacheNodeType': 'string',
                    'StartTime': datetime(2015, 1, 1),
                    'Duration': 123,
                    'FixedPrice': 123.0,
                    'UsagePrice': 123.0,
                    'CacheNodeCount': 123,
                    'ProductDescription': 'string',
                    'OfferingType': 'string',
                    'State': 'string',
                    'RecurringCharges': [
                        {
                            'RecurringChargeAmount': 123.0,
                            'RecurringChargeFrequency': 'string'
                        },
                    ],
                    'ReservationARN': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **ReservedCacheNode** *(dict) --*

              Represents the output of a ``PurchaseReservedCacheNodesOffering`` operation.

              - **ReservedCacheNodeId** *(string) --*

                The unique identifier for the reservation.

              - **ReservedCacheNodesOfferingId** *(string) --*

                The offering identifier.

              - **CacheNodeType** *(string) --*

                The cache node type for the reserved cache nodes.

                The following node types are supported by ElastiCache. Generally speaking, the current
                generation types provide more memory and computational power at lower cost when compared to
                their equivalent previous generation counterparts.

                * General purpose:

                  * Current generation:   **M5 node types:**  ``cache.m5.large`` , ``cache.m5.xlarge`` ,
                  ``cache.m5.2xlarge`` , ``cache.m5.4xlarge`` , ``cache.m5.12xlarge`` ,
                  ``cache.m5.24xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` ,
                  ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``    **T2 node types:**
                   ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``

                  * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``    **M1
                  node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` ,
                  ``cache.m1.xlarge``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` ,
                  ``cache.m3.xlarge`` , ``cache.m3.2xlarge``

                * Compute optimized:

                  * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``

                * Memory optimized:

                  * Current generation:   **R5 node types:**  ``cache.r5.large`` , ``cache.r5.xlarge`` ,
                  ``cache.r5.2xlarge`` , ``cache.r5.4xlarge`` , ``cache.r5.12xlarge`` ,
                  ``cache.r5.24xlarge``    **R4 node types:**  ``cache.r4.large`` , ``cache.r4.xlarge`` ,
                  ``cache.r4.2xlarge`` , ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` , ``cache.r4.16xlarge``

                  * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` ,
                  ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``    **R3 node types:**  ``cache.r3.large`` ,
                  ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``

                 **Additional node type info**

                * All current generation instance types are created in Amazon VPC by default.

                * Redis append-only files (AOF) are not supported for T1 or T2 instances.

                * Redis Multi-AZ with automatic failover is not supported on T1 instances.

                * Redis configuration variables ``appendonly`` and ``appendfsync`` are not supported on
                Redis version 2.8.22 and later.

              - **StartTime** *(datetime) --*

                The time the reservation started.

              - **Duration** *(integer) --*

                The duration of the reservation in seconds.

              - **FixedPrice** *(float) --*

                The fixed price charged for this reserved cache node.

              - **UsagePrice** *(float) --*

                The hourly price charged for this reserved cache node.

              - **CacheNodeCount** *(integer) --*

                The number of cache nodes that have been reserved.

              - **ProductDescription** *(string) --*

                The description of the reserved cache node.

              - **OfferingType** *(string) --*

                The offering type of this reserved cache node.

              - **State** *(string) --*

                The state of the reserved cache node.

              - **RecurringCharges** *(list) --*

                The recurring price charged to run this reserved cache node.

                - *(dict) --*

                  Contains the specific price and frequency of a recurring charges for a reserved cache
                  node, or for a reserved cache node offering.

                  - **RecurringChargeAmount** *(float) --*

                    The monetary amount of the recurring charge.

                  - **RecurringChargeFrequency** *(string) --*

                    The frequency of the recurring charge.

              - **ReservationARN** *(string) --*

                The Amazon Resource Name (ARN) of the reserved cache node.

                Example:
                ``arn:aws:elasticache:us-east-1:123456789012:reserved-instance:ri-2017-03-27-08-33-25-582``

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reboot_cache_cluster(
        self, CacheClusterId: str, CacheNodeIdsToReboot: List[str]
    ) -> ClientRebootCacheClusterResponseTypeDef:
        """
        Reboots some, or all, of the cache nodes within a provisioned cluster. This operation applies any
        modified cache parameter groups to the cluster. The reboot operation takes place as soon as
        possible, and results in a momentary outage to the cluster. During the reboot, the cluster status
        is set to REBOOTING.

        The reboot causes the contents of the cache (for each cache node being rebooted) to be lost.

        When the reboot is complete, a cluster event is created.

        Rebooting a cluster is currently supported on Memcached and Redis (cluster mode disabled) clusters.
        Rebooting is not supported on Redis (cluster mode enabled) clusters.

        If you make changes to parameters that require a Redis (cluster mode enabled) cluster reboot for
        the changes to be applied, see `Rebooting a Cluster
        <http://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Clusters.Rebooting.html>`__ for an
        alternate process.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/RebootCacheCluster>`_

        **Request Syntax**
        ::

          response = client.reboot_cache_cluster(
              CacheClusterId='string',
              CacheNodeIdsToReboot=[
                  'string',
              ]
          )
        :type CacheClusterId: string
        :param CacheClusterId: **[REQUIRED]**

          The cluster identifier. This parameter is stored as a lowercase string.

        :type CacheNodeIdsToReboot: list
        :param CacheNodeIdsToReboot: **[REQUIRED]**

          A list of cache node IDs to reboot. A node ID is a numeric identifier (0001, 0002, etc.). To
          reboot an entire cluster, specify all of the cache node IDs.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'CacheCluster': {
                    'CacheClusterId': 'string',
                    'ConfigurationEndpoint': {
                        'Address': 'string',
                        'Port': 123
                    },
                    'ClientDownloadLandingPage': 'string',
                    'CacheNodeType': 'string',
                    'Engine': 'string',
                    'EngineVersion': 'string',
                    'CacheClusterStatus': 'string',
                    'NumCacheNodes': 123,
                    'PreferredAvailabilityZone': 'string',
                    'CacheClusterCreateTime': datetime(2015, 1, 1),
                    'PreferredMaintenanceWindow': 'string',
                    'PendingModifiedValues': {
                        'NumCacheNodes': 123,
                        'CacheNodeIdsToRemove': [
                            'string',
                        ],
                        'EngineVersion': 'string',
                        'CacheNodeType': 'string',
                        'AuthTokenStatus': 'SETTING'|'ROTATING'
                    },
                    'NotificationConfiguration': {
                        'TopicArn': 'string',
                        'TopicStatus': 'string'
                    },
                    'CacheSecurityGroups': [
                        {
                            'CacheSecurityGroupName': 'string',
                            'Status': 'string'
                        },
                    ],
                    'CacheParameterGroup': {
                        'CacheParameterGroupName': 'string',
                        'ParameterApplyStatus': 'string',
                        'CacheNodeIdsToReboot': [
                            'string',
                        ]
                    },
                    'CacheSubnetGroupName': 'string',
                    'CacheNodes': [
                        {
                            'CacheNodeId': 'string',
                            'CacheNodeStatus': 'string',
                            'CacheNodeCreateTime': datetime(2015, 1, 1),
                            'Endpoint': {
                                'Address': 'string',
                                'Port': 123
                            },
                            'ParameterGroupStatus': 'string',
                            'SourceCacheNodeId': 'string',
                            'CustomerAvailabilityZone': 'string'
                        },
                    ],
                    'AutoMinorVersionUpgrade': True|False,
                    'SecurityGroups': [
                        {
                            'SecurityGroupId': 'string',
                            'Status': 'string'
                        },
                    ],
                    'ReplicationGroupId': 'string',
                    'SnapshotRetentionLimit': 123,
                    'SnapshotWindow': 'string',
                    'AuthTokenEnabled': True|False,
                    'AuthTokenLastModifiedDate': datetime(2015, 1, 1),
                    'TransitEncryptionEnabled': True|False,
                    'AtRestEncryptionEnabled': True|False
                }
            }
          **Response Structure**

          - *(dict) --*

            - **CacheCluster** *(dict) --*

              Contains all of the attributes of a specific cluster.

              - **CacheClusterId** *(string) --*

                The user-supplied identifier of the cluster. This identifier is a unique key that
                identifies a cluster.

              - **ConfigurationEndpoint** *(dict) --*

                Represents a Memcached cluster endpoint which, if Automatic Discovery is enabled on the
                cluster, can be used by an application to connect to any node in the cluster. The
                configuration endpoint will always have ``.cfg`` in it.

                Example: ``mem-3.9dvc4r.cfg.usw2.cache.amazonaws.com:11211``

                - **Address** *(string) --*

                  The DNS hostname of the cache node.

                - **Port** *(integer) --*

                  The port number that the cache engine is listening on.

              - **ClientDownloadLandingPage** *(string) --*

                The URL of the web page where you can download the latest ElastiCache client library.

              - **CacheNodeType** *(string) --*

                The name of the compute and memory capacity node type for the cluster.

                The following node types are supported by ElastiCache. Generally speaking, the current
                generation types provide more memory and computational power at lower cost when compared to
                their equivalent previous generation counterparts.

                * General purpose:

                  * Current generation:   **M5 node types:**  ``cache.m5.large`` , ``cache.m5.xlarge`` ,
                  ``cache.m5.2xlarge`` , ``cache.m5.4xlarge`` , ``cache.m5.12xlarge`` ,
                  ``cache.m5.24xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` ,
                  ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``    **T2 node types:**
                   ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``

                  * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``    **M1
                  node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` ,
                  ``cache.m1.xlarge``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` ,
                  ``cache.m3.xlarge`` , ``cache.m3.2xlarge``

                * Compute optimized:

                  * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``

                * Memory optimized:

                  * Current generation:   **R5 node types:**  ``cache.r5.large`` , ``cache.r5.xlarge`` ,
                  ``cache.r5.2xlarge`` , ``cache.r5.4xlarge`` , ``cache.r5.12xlarge`` ,
                  ``cache.r5.24xlarge``    **R4 node types:**  ``cache.r4.large`` , ``cache.r4.xlarge`` ,
                  ``cache.r4.2xlarge`` , ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` , ``cache.r4.16xlarge``

                  * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` ,
                  ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``    **R3 node types:**  ``cache.r3.large`` ,
                  ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``

                 **Additional node type info**

                * All current generation instance types are created in Amazon VPC by default.

                * Redis append-only files (AOF) are not supported for T1 or T2 instances.

                * Redis Multi-AZ with automatic failover is not supported on T1 instances.

                * Redis configuration variables ``appendonly`` and ``appendfsync`` are not supported on
                Redis version 2.8.22 and later.

              - **Engine** *(string) --*

                The name of the cache engine (``memcached`` or ``redis`` ) to be used for this cluster.

              - **EngineVersion** *(string) --*

                The version of the cache engine that is used in this cluster.

              - **CacheClusterStatus** *(string) --*

                The current state of this cluster, one of the following values: ``available`` ,
                ``creating`` , ``deleted`` , ``deleting`` , ``incompatible-network`` , ``modifying`` ,
                ``rebooting cluster nodes`` , ``restore-failed`` , or ``snapshotting`` .

              - **NumCacheNodes** *(integer) --*

                The number of cache nodes in the cluster.

                For clusters running Redis, this value must be 1. For clusters running Memcached, this
                value must be between 1 and 20.

              - **PreferredAvailabilityZone** *(string) --*

                The name of the Availability Zone in which the cluster is located or "Multiple" if the
                cache nodes are located in different Availability Zones.

              - **CacheClusterCreateTime** *(datetime) --*

                The date and time when the cluster was created.

              - **PreferredMaintenanceWindow** *(string) --*

                Specifies the weekly time range during which maintenance on the cluster is performed. It is
                specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum
                maintenance window is a 60 minute period.

                Valid values for ``ddd`` are:

                * ``sun``

                * ``mon``

                * ``tue``

                * ``wed``

                * ``thu``

                * ``fri``

                * ``sat``

                Example: ``sun:23:00-mon:01:30``

              - **PendingModifiedValues** *(dict) --*

                A group of settings that are applied to the cluster in the future, or that are currently
                being applied.

                - **NumCacheNodes** *(integer) --*

                  The new number of cache nodes for the cluster.

                  For clusters running Redis, this value must be 1. For clusters running Memcached, this
                  value must be between 1 and 20.

                - **CacheNodeIdsToRemove** *(list) --*

                  A list of cache node IDs that are being removed (or will be removed) from the cluster. A
                  node ID is a 4-digit numeric identifier (0001, 0002, etc.).

                  - *(string) --*

                - **EngineVersion** *(string) --*

                  The new cache engine version that the cluster runs.

                - **CacheNodeType** *(string) --*

                  The cache node type that this cluster or replication group is scaled to.

                - **AuthTokenStatus** *(string) --*

                  The auth token status

              - **NotificationConfiguration** *(dict) --*

                Describes a notification topic and its status. Notification topics are used for publishing
                ElastiCache events to subscribers using Amazon Simple Notification Service (SNS).

                - **TopicArn** *(string) --*

                  The Amazon Resource Name (ARN) that identifies the topic.

                - **TopicStatus** *(string) --*

                  The current state of the topic.

              - **CacheSecurityGroups** *(list) --*

                A list of cache security group elements, composed of name and status sub-elements.

                - *(dict) --*

                  Represents a cluster's status within a particular cache security group.

                  - **CacheSecurityGroupName** *(string) --*

                    The name of the cache security group.

                  - **Status** *(string) --*

                    The membership status in the cache security group. The status changes when a cache
                    security group is modified, or when the cache security groups assigned to a cluster are
                    modified.

              - **CacheParameterGroup** *(dict) --*

                Status of the cache parameter group.

                - **CacheParameterGroupName** *(string) --*

                  The name of the cache parameter group.

                - **ParameterApplyStatus** *(string) --*

                  The status of parameter updates.

                - **CacheNodeIdsToReboot** *(list) --*

                  A list of the cache node IDs which need to be rebooted for parameter changes to be
                  applied. A node ID is a numeric identifier (0001, 0002, etc.).

                  - *(string) --*

              - **CacheSubnetGroupName** *(string) --*

                The name of the cache subnet group associated with the cluster.

              - **CacheNodes** *(list) --*

                A list of cache nodes that are members of the cluster.

                - *(dict) --*

                  Represents an individual cache node within a cluster. Each cache node runs its own
                  instance of the cluster's protocol-compliant caching software - either Memcached or Redis.

                  The following node types are supported by ElastiCache. Generally speaking, the current
                  generation types provide more memory and computational power at lower cost when compared
                  to their equivalent previous generation counterparts.

                  * General purpose:

                    * Current generation:   **M5 node types:**  ``cache.m5.large`` , ``cache.m5.xlarge`` ,
                    ``cache.m5.2xlarge`` , ``cache.m5.4xlarge`` , ``cache.m5.12xlarge`` ,
                    ``cache.m5.24xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` ,
                    ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``    **T2 node
                    types:**  ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``

                    * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``
                    **M1 node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` ,
                    ``cache.m1.xlarge``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` ,
                    ``cache.m3.xlarge`` , ``cache.m3.2xlarge``

                  * Compute optimized:

                    * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``

                  * Memory optimized:

                    * Current generation:   **R5 node types:**  ``cache.r5.large`` , ``cache.r5.xlarge`` ,
                    ``cache.r5.2xlarge`` , ``cache.r5.4xlarge`` , ``cache.r5.12xlarge`` ,
                    ``cache.r5.24xlarge``    **R4 node types:**  ``cache.r4.large`` , ``cache.r4.xlarge`` ,
                    ``cache.r4.2xlarge`` , ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` ,
                    ``cache.r4.16xlarge``

                    * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` ,
                    ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``    **R3 node types:**  ``cache.r3.large`` ,
                    ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``

                   **Additional node type info**

                  * All current generation instance types are created in Amazon VPC by default.

                  * Redis append-only files (AOF) are not supported for T1 or T2 instances.

                  * Redis Multi-AZ with automatic failover is not supported on T1 instances.

                  * Redis configuration variables ``appendonly`` and ``appendfsync`` are not supported on
                  Redis version 2.8.22 and later.

                  - **CacheNodeId** *(string) --*

                    The cache node identifier. A node ID is a numeric identifier (0001, 0002, etc.). The
                    combination of cluster ID and node ID uniquely identifies every cache node used in a
                    customer's AWS account.

                  - **CacheNodeStatus** *(string) --*

                    The current state of this cache node.

                  - **CacheNodeCreateTime** *(datetime) --*

                    The date and time when the cache node was created.

                  - **Endpoint** *(dict) --*

                    The hostname for connecting to this cache node.

                    - **Address** *(string) --*

                      The DNS hostname of the cache node.

                    - **Port** *(integer) --*

                      The port number that the cache engine is listening on.

                  - **ParameterGroupStatus** *(string) --*

                    The status of the parameter group applied to this cache node.

                  - **SourceCacheNodeId** *(string) --*

                    The ID of the primary node to which this read replica node is synchronized. If this
                    field is empty, this node is not associated with a primary cluster.

                  - **CustomerAvailabilityZone** *(string) --*

                    The Availability Zone where this node was created and now resides.

              - **AutoMinorVersionUpgrade** *(boolean) --*

                This parameter is currently disabled.

              - **SecurityGroups** *(list) --*

                A list of VPC Security Groups associated with the cluster.

                - *(dict) --*

                  Represents a single cache security group and its status.

                  - **SecurityGroupId** *(string) --*

                    The identifier of the cache security group.

                  - **Status** *(string) --*

                    The status of the cache security group membership. The status changes whenever a cache
                    security group is modified, or when the cache security groups assigned to a cluster are
                    modified.

              - **ReplicationGroupId** *(string) --*

                The replication group to which this cluster belongs. If this field is empty, the cluster is
                not associated with any replication group.

              - **SnapshotRetentionLimit** *(integer) --*

                The number of days for which ElastiCache retains automatic cluster snapshots before
                deleting them. For example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot that was
                taken today is retained for 5 days before being deleted.

                .. warning::

                  If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.

              - **SnapshotWindow** *(string) --*

                The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of
                your cluster.

                Example: ``05:00-09:00``

              - **AuthTokenEnabled** *(boolean) --*

                A flag that enables using an ``AuthToken`` (password) when issuing Redis commands.

                Default: ``false``

              - **AuthTokenLastModifiedDate** *(datetime) --*

                The date the auth token was last modified

              - **TransitEncryptionEnabled** *(boolean) --*

                A flag that enables in-transit encryption when set to ``true`` .

                You cannot modify the value of ``TransitEncryptionEnabled`` after the cluster is created.
                To enable in-transit encryption on a cluster you must set ``TransitEncryptionEnabled`` to
                ``true`` when you create a cluster.

                 **Required:** Only available when creating a replication group in an Amazon VPC using
                 redis version ``3.2.6`` , ``4.x`` or later.

                Default: ``false``

              - **AtRestEncryptionEnabled** *(boolean) --*

                A flag that enables encryption at-rest when set to ``true`` .

                You cannot modify the value of ``AtRestEncryptionEnabled`` after the cluster is created. To
                enable at-rest encryption on a cluster you must set ``AtRestEncryptionEnabled`` to ``true``
                when you create a cluster.

                 **Required:** Only available when creating a replication group in an Amazon VPC using
                 redis version ``3.2.6`` , ``4.x`` or later.

                Default: ``false``

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def remove_tags_from_resource(
        self, ResourceName: str, TagKeys: List[str]
    ) -> ClientRemoveTagsFromResourceResponseTypeDef:
        """
        Removes the tags identified by the ``TagKeys`` list from the named resource.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/RemoveTagsFromResource>`_

        **Request Syntax**
        ::

          response = client.remove_tags_from_resource(
              ResourceName='string',
              TagKeys=[
                  'string',
              ]
          )
        :type ResourceName: string
        :param ResourceName: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the resource from which you want the tags removed, for example
          ``arn:aws:elasticache:us-west-2:0123456789:cluster:myCluster`` or
          ``arn:aws:elasticache:us-west-2:0123456789:snapshot:mySnapshot`` .

          For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS Service Namespaces
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

        :type TagKeys: list
        :param TagKeys: **[REQUIRED]**

          A list of ``TagKeys`` identifying the tags you want removed from the named resource.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'TagList': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            Represents the output from the ``AddTagsToResource`` , ``ListTagsForResource`` , and
            ``RemoveTagsFromResource`` operations.

            - **TagList** *(list) --*

              A list of cost allocation tags as key-value pairs.

              - *(dict) --*

                A cost allocation Tag that can be added to an ElastiCache cluster or replication group.
                Tags are composed of a Key/Value pair. A tag with a null Value is permitted.

                - **Key** *(string) --*

                  The key for the tag. May not be null.

                - **Value** *(string) --*

                  The tag's value. May be null.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reset_cache_parameter_group(
        self,
        CacheParameterGroupName: str,
        ResetAllParameters: bool = None,
        ParameterNameValues: List[
            ClientResetCacheParameterGroupParameterNameValuesTypeDef
        ] = None,
    ) -> ClientResetCacheParameterGroupResponseTypeDef:
        """
        Modifies the parameters of a cache parameter group to the engine or system default value. You can
        reset specific parameters by submitting a list of parameter names. To reset the entire cache
        parameter group, specify the ``ResetAllParameters`` and ``CacheParameterGroupName`` parameters.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/ResetCacheParameterGroup>`_

        **Request Syntax**
        ::

          response = client.reset_cache_parameter_group(
              CacheParameterGroupName='string',
              ResetAllParameters=True|False,
              ParameterNameValues=[
                  {
                      'ParameterName': 'string',
                      'ParameterValue': 'string'
                  },
              ]
          )
        :type CacheParameterGroupName: string
        :param CacheParameterGroupName: **[REQUIRED]**

          The name of the cache parameter group to reset.

        :type ResetAllParameters: boolean
        :param ResetAllParameters:

          If ``true`` , all parameters in the cache parameter group are reset to their default values. If
          ``false`` , only the parameters listed by ``ParameterNameValues`` are reset to their default
          values.

          Valid values: ``true`` | ``false``

        :type ParameterNameValues: list
        :param ParameterNameValues:

          An array of parameter names to reset to their default values. If ``ResetAllParameters`` is
          ``true`` , do not use ``ParameterNameValues`` . If ``ResetAllParameters`` is ``false`` , you must
          specify the name of at least one parameter to reset.

          - *(dict) --*

            Describes a name-value pair that is used to update the value of a parameter.

            - **ParameterName** *(string) --*

              The name of the parameter.

            - **ParameterValue** *(string) --*

              The value of the parameter.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'CacheParameterGroupName': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Represents the output of one of the following operations:

            * ``ModifyCacheParameterGroup``

            * ``ResetCacheParameterGroup``

            - **CacheParameterGroupName** *(string) --*

              The name of the cache parameter group.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def revoke_cache_security_group_ingress(
        self,
        CacheSecurityGroupName: str,
        EC2SecurityGroupName: str,
        EC2SecurityGroupOwnerId: str,
    ) -> ClientRevokeCacheSecurityGroupIngressResponseTypeDef:
        """
        Revokes ingress from a cache security group. Use this operation to disallow access from an Amazon
        EC2 security group that had been previously authorized.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/RevokeCacheSecurityGroupIngress>`_

        **Request Syntax**
        ::

          response = client.revoke_cache_security_group_ingress(
              CacheSecurityGroupName='string',
              EC2SecurityGroupName='string',
              EC2SecurityGroupOwnerId='string'
          )
        :type CacheSecurityGroupName: string
        :param CacheSecurityGroupName: **[REQUIRED]**

          The name of the cache security group to revoke ingress from.

        :type EC2SecurityGroupName: string
        :param EC2SecurityGroupName: **[REQUIRED]**

          The name of the Amazon EC2 security group to revoke access from.

        :type EC2SecurityGroupOwnerId: string
        :param EC2SecurityGroupOwnerId: **[REQUIRED]**

          The AWS account number of the Amazon EC2 security group owner. Note that this is not the same
          thing as an AWS access key ID - you must provide a valid AWS account number for this parameter.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'CacheSecurityGroup': {
                    'OwnerId': 'string',
                    'CacheSecurityGroupName': 'string',
                    'Description': 'string',
                    'EC2SecurityGroups': [
                        {
                            'Status': 'string',
                            'EC2SecurityGroupName': 'string',
                            'EC2SecurityGroupOwnerId': 'string'
                        },
                    ]
                }
            }
          **Response Structure**

          - *(dict) --*

            - **CacheSecurityGroup** *(dict) --*

              Represents the output of one of the following operations:

              * ``AuthorizeCacheSecurityGroupIngress``

              * ``CreateCacheSecurityGroup``

              * ``RevokeCacheSecurityGroupIngress``

              - **OwnerId** *(string) --*

                The AWS account ID of the cache security group owner.

              - **CacheSecurityGroupName** *(string) --*

                The name of the cache security group.

              - **Description** *(string) --*

                The description of the cache security group.

              - **EC2SecurityGroups** *(list) --*

                A list of Amazon EC2 security groups that are associated with this cache security group.

                - *(dict) --*

                  Provides ownership and status information for an Amazon EC2 security group.

                  - **Status** *(string) --*

                    The status of the Amazon EC2 security group.

                  - **EC2SecurityGroupName** *(string) --*

                    The name of the Amazon EC2 security group.

                  - **EC2SecurityGroupOwnerId** *(string) --*

                    The AWS account ID of the Amazon EC2 security group owner.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_migration(
        self,
        ReplicationGroupId: str,
        CustomerNodeEndpointList: List[
            ClientStartMigrationCustomerNodeEndpointListTypeDef
        ],
    ) -> ClientStartMigrationResponseTypeDef:
        """
        Start the migration of data.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/StartMigration>`_

        **Request Syntax**
        ::

          response = client.start_migration(
              ReplicationGroupId='string',
              CustomerNodeEndpointList=[
                  {
                      'Address': 'string',
                      'Port': 123
                  },
              ]
          )
        :type ReplicationGroupId: string
        :param ReplicationGroupId: **[REQUIRED]**

          The ID of the replication group to which data should be migrated.

        :type CustomerNodeEndpointList: list
        :param CustomerNodeEndpointList: **[REQUIRED]**

          List of endpoints from which data should be migrated. For Redis (cluster mode disabled), list
          should have only one element.

          - *(dict) --*

            The endpoint from which data should be migrated.

            - **Address** *(string) --*

              The address of the node endpoint

            - **Port** *(integer) --*

              The port of the node endpoint

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ReplicationGroup': {
                    'ReplicationGroupId': 'string',
                    'Description': 'string',
                    'Status': 'string',
                    'PendingModifiedValues': {
                        'PrimaryClusterId': 'string',
                        'AutomaticFailoverStatus': 'enabled'|'disabled',
                        'Resharding': {
                            'SlotMigration': {
                                'ProgressPercentage': 123.0
                            }
                        },
                        'AuthTokenStatus': 'SETTING'|'ROTATING'
                    },
                    'MemberClusters': [
                        'string',
                    ],
                    'NodeGroups': [
                        {
                            'NodeGroupId': 'string',
                            'Status': 'string',
                            'PrimaryEndpoint': {
                                'Address': 'string',
                                'Port': 123
                            },
                            'ReaderEndpoint': {
                                'Address': 'string',
                                'Port': 123
                            },
                            'Slots': 'string',
                            'NodeGroupMembers': [
                                {
                                    'CacheClusterId': 'string',
                                    'CacheNodeId': 'string',
                                    'ReadEndpoint': {
                                        'Address': 'string',
                                        'Port': 123
                                    },
                                    'PreferredAvailabilityZone': 'string',
                                    'CurrentRole': 'string'
                                },
                            ]
                        },
                    ],
                    'SnapshottingClusterId': 'string',
                    'AutomaticFailover': 'enabled'|'disabled'|'enabling'|'disabling',
                    'ConfigurationEndpoint': {
                        'Address': 'string',
                        'Port': 123
                    },
                    'SnapshotRetentionLimit': 123,
                    'SnapshotWindow': 'string',
                    'ClusterEnabled': True|False,
                    'CacheNodeType': 'string',
                    'AuthTokenEnabled': True|False,
                    'AuthTokenLastModifiedDate': datetime(2015, 1, 1),
                    'TransitEncryptionEnabled': True|False,
                    'AtRestEncryptionEnabled': True|False,
                    'KmsKeyId': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **ReplicationGroup** *(dict) --*

              Contains all of the attributes of a specific Redis replication group.

              - **ReplicationGroupId** *(string) --*

                The identifier for the replication group.

              - **Description** *(string) --*

                The user supplied description of the replication group.

              - **Status** *(string) --*

                The current state of this replication group - ``creating`` , ``available`` , ``modifying``
                , ``deleting`` , ``create-failed`` , ``snapshotting`` .

              - **PendingModifiedValues** *(dict) --*

                A group of settings to be applied to the replication group, either immediately or during
                the next maintenance window.

                - **PrimaryClusterId** *(string) --*

                  The primary cluster ID that is applied immediately (if ``--apply-immediately`` was
                  specified), or during the next maintenance window.

                - **AutomaticFailoverStatus** *(string) --*

                  Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

                  Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

                  * Redis versions earlier than 2.8.6.

                  * Redis (cluster mode disabled): T1 node types.

                  * Redis (cluster mode enabled): T1 node types.

                - **Resharding** *(dict) --*

                  The status of an online resharding operation.

                  - **SlotMigration** *(dict) --*

                    Represents the progress of an online resharding operation.

                    - **ProgressPercentage** *(float) --*

                      The percentage of the slot migration that is complete.

                - **AuthTokenStatus** *(string) --*

                  The auth token status

              - **MemberClusters** *(list) --*

                The names of all the cache clusters that are part of this replication group.

                - *(string) --*

              - **NodeGroups** *(list) --*

                A list of node groups in this replication group. For Redis (cluster mode disabled)
                replication groups, this is a single-element list. For Redis (cluster mode enabled)
                replication groups, the list contains an entry for each node group (shard).

                - *(dict) --*

                  Represents a collection of cache nodes in a replication group. One node in the node group
                  is the read/write primary node. All the other nodes are read-only Replica nodes.

                  - **NodeGroupId** *(string) --*

                    The identifier for the node group (shard). A Redis (cluster mode disabled) replication
                    group contains only 1 node group; therefore, the node group ID is 0001. A Redis
                    (cluster mode enabled) replication group contains 1 to 90 node groups numbered 0001 to
                    0090. Optionally, the user can provide the id for a node group.

                  - **Status** *(string) --*

                    The current state of this replication group - ``creating`` , ``available`` , etc.

                  - **PrimaryEndpoint** *(dict) --*

                    The endpoint of the primary node in this node group (shard).

                    - **Address** *(string) --*

                      The DNS hostname of the cache node.

                    - **Port** *(integer) --*

                      The port number that the cache engine is listening on.

                  - **ReaderEndpoint** *(dict) --*

                    The endpoint of the replica nodes in this node group (shard).

                    - **Address** *(string) --*

                      The DNS hostname of the cache node.

                    - **Port** *(integer) --*

                      The port number that the cache engine is listening on.

                  - **Slots** *(string) --*

                    The keyspace for this node group (shard).

                  - **NodeGroupMembers** *(list) --*

                    A list containing information about individual nodes within the node group (shard).

                    - *(dict) --*

                      Represents a single node within a node group (shard).

                      - **CacheClusterId** *(string) --*

                        The ID of the cluster to which the node belongs.

                      - **CacheNodeId** *(string) --*

                        The ID of the node within its cluster. A node ID is a numeric identifier (0001,
                        0002, etc.).

                      - **ReadEndpoint** *(dict) --*

                        The information required for client programs to connect to a node for read
                        operations. The read endpoint is only applicable on Redis (cluster mode disabled)
                        clusters.

                        - **Address** *(string) --*

                          The DNS hostname of the cache node.

                        - **Port** *(integer) --*

                          The port number that the cache engine is listening on.

                      - **PreferredAvailabilityZone** *(string) --*

                        The name of the Availability Zone in which the node is located.

                      - **CurrentRole** *(string) --*

                        The role that is currently assigned to the node - ``primary`` or ``replica`` . This
                        member is only applicable for Redis (cluster mode disabled) replication groups.

              - **SnapshottingClusterId** *(string) --*

                The cluster ID that is used as the daily snapshot source for the replication group.

              - **AutomaticFailover** *(string) --*

                Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

                Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

                * Redis versions earlier than 2.8.6.

                * Redis (cluster mode disabled): T1 node types.

                * Redis (cluster mode enabled): T1 node types.

              - **ConfigurationEndpoint** *(dict) --*

                The configuration endpoint for this replication group. Use the configuration endpoint to
                connect to this replication group.

                - **Address** *(string) --*

                  The DNS hostname of the cache node.

                - **Port** *(integer) --*

                  The port number that the cache engine is listening on.

              - **SnapshotRetentionLimit** *(integer) --*

                The number of days for which ElastiCache retains automatic cluster snapshots before
                deleting them. For example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot that was
                taken today is retained for 5 days before being deleted.

                .. warning::

                  If the value of ``SnapshotRetentionLimit`` is set to zero (0), backups are turned off.

              - **SnapshotWindow** *(string) --*

                The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of
                your node group (shard).

                Example: ``05:00-09:00``

                If you do not specify this parameter, ElastiCache automatically chooses an appropriate time
                range.

                .. note::

                  This parameter is only valid if the ``Engine`` parameter is ``redis`` .

              - **ClusterEnabled** *(boolean) --*

                A flag indicating whether or not this replication group is cluster enabled; i.e., whether
                its data can be partitioned across multiple shards (API/CLI: node groups).

                Valid values: ``true`` | ``false``

              - **CacheNodeType** *(string) --*

                The name of the compute and memory capacity node type for each node in the replication
                group.

              - **AuthTokenEnabled** *(boolean) --*

                A flag that enables using an ``AuthToken`` (password) when issuing Redis commands.

                Default: ``false``

              - **AuthTokenLastModifiedDate** *(datetime) --*

                The date the auth token was last modified

              - **TransitEncryptionEnabled** *(boolean) --*

                A flag that enables in-transit encryption when set to ``true`` .

                You cannot modify the value of ``TransitEncryptionEnabled`` after the cluster is created.
                To enable in-transit encryption on a cluster you must set ``TransitEncryptionEnabled`` to
                ``true`` when you create a cluster.

                 **Required:** Only available when creating a replication group in an Amazon VPC using
                 redis version ``3.2.6`` , ``4.x`` or later.

                Default: ``false``

              - **AtRestEncryptionEnabled** *(boolean) --*

                A flag that enables encryption at-rest when set to ``true`` .

                You cannot modify the value of ``AtRestEncryptionEnabled`` after the cluster is created. To
                enable encryption at-rest on a cluster you must set ``AtRestEncryptionEnabled`` to ``true``
                when you create a cluster.

                 **Required:** Only available when creating a replication group in an Amazon VPC using
                 redis version ``3.2.6`` , ``4.x`` or later.

                Default: ``false``

              - **KmsKeyId** *(string) --*

                The ID of the KMS key used to encrypt the disk in the cluster.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def test_failover(
        self, ReplicationGroupId: str, NodeGroupId: str
    ) -> ClientTestFailoverResponseTypeDef:
        """
        Represents the input of a ``TestFailover`` operation which test automatic failover on a specified
        node group (called shard in the console) in a replication group (called cluster in the console).

         **Note the following**

        * A customer can use this operation to test automatic failover on up to 5 shards (called node
        groups in the ElastiCache API and AWS CLI) in any rolling 24-hour period.

        * If calling this operation on shards in different clusters (called replication groups in the API
        and CLI), the calls can be made concurrently.

        * If calling this operation multiple times on different shards in the same Redis (cluster mode
        enabled) replication group, the first node replacement must complete before a subsequent call can
        be made.

        * To determine whether the node replacement is complete you can check Events using the Amazon
        ElastiCache console, the AWS CLI, or the ElastiCache API. Look for the following automatic failover
        related events, listed here in order of occurrance:

          * Replication group message: ``Test Failover API called for node group <node-group-id>``

          * Cache cluster message: ``Failover from master node <primary-node-id> to replica node <node-id>
          completed``

          * Replication group message: ``Failover from master node <primary-node-id> to replica node
          <node-id> completed``

          * Cache cluster message: ``Recovering cache nodes <node-id>``

          * Cache cluster message: ``Finished recovery for cache nodes <node-id>``

        For more information see:

          * `Viewing ElastiCache Events
          <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/ECEvents.Viewing.html>`__ in the
          *ElastiCache User Guide*

          * `DescribeEvents
          <https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_DescribeEvents.html>`__ in
          the ElastiCache API Reference

        Also see, `Testing Multi-AZ with Automatic Failover
        <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/AutoFailover.html#auto-failover-test>`__
        in the *ElastiCache User Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/TestFailover>`_

        **Request Syntax**
        ::

          response = client.test_failover(
              ReplicationGroupId='string',
              NodeGroupId='string'
          )
        :type ReplicationGroupId: string
        :param ReplicationGroupId: **[REQUIRED]**

          The name of the replication group (console: cluster) whose automatic failover is being tested by
          this operation.

        :type NodeGroupId: string
        :param NodeGroupId: **[REQUIRED]**

          The name of the node group (called shard in the console) in this replication group on which
          automatic failover is to be tested. You may test automatic failover on up to 5 node groups in any
          rolling 24-hour period.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ReplicationGroup': {
                    'ReplicationGroupId': 'string',
                    'Description': 'string',
                    'Status': 'string',
                    'PendingModifiedValues': {
                        'PrimaryClusterId': 'string',
                        'AutomaticFailoverStatus': 'enabled'|'disabled',
                        'Resharding': {
                            'SlotMigration': {
                                'ProgressPercentage': 123.0
                            }
                        },
                        'AuthTokenStatus': 'SETTING'|'ROTATING'
                    },
                    'MemberClusters': [
                        'string',
                    ],
                    'NodeGroups': [
                        {
                            'NodeGroupId': 'string',
                            'Status': 'string',
                            'PrimaryEndpoint': {
                                'Address': 'string',
                                'Port': 123
                            },
                            'ReaderEndpoint': {
                                'Address': 'string',
                                'Port': 123
                            },
                            'Slots': 'string',
                            'NodeGroupMembers': [
                                {
                                    'CacheClusterId': 'string',
                                    'CacheNodeId': 'string',
                                    'ReadEndpoint': {
                                        'Address': 'string',
                                        'Port': 123
                                    },
                                    'PreferredAvailabilityZone': 'string',
                                    'CurrentRole': 'string'
                                },
                            ]
                        },
                    ],
                    'SnapshottingClusterId': 'string',
                    'AutomaticFailover': 'enabled'|'disabled'|'enabling'|'disabling',
                    'ConfigurationEndpoint': {
                        'Address': 'string',
                        'Port': 123
                    },
                    'SnapshotRetentionLimit': 123,
                    'SnapshotWindow': 'string',
                    'ClusterEnabled': True|False,
                    'CacheNodeType': 'string',
                    'AuthTokenEnabled': True|False,
                    'AuthTokenLastModifiedDate': datetime(2015, 1, 1),
                    'TransitEncryptionEnabled': True|False,
                    'AtRestEncryptionEnabled': True|False,
                    'KmsKeyId': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **ReplicationGroup** *(dict) --*

              Contains all of the attributes of a specific Redis replication group.

              - **ReplicationGroupId** *(string) --*

                The identifier for the replication group.

              - **Description** *(string) --*

                The user supplied description of the replication group.

              - **Status** *(string) --*

                The current state of this replication group - ``creating`` , ``available`` , ``modifying``
                , ``deleting`` , ``create-failed`` , ``snapshotting`` .

              - **PendingModifiedValues** *(dict) --*

                A group of settings to be applied to the replication group, either immediately or during
                the next maintenance window.

                - **PrimaryClusterId** *(string) --*

                  The primary cluster ID that is applied immediately (if ``--apply-immediately`` was
                  specified), or during the next maintenance window.

                - **AutomaticFailoverStatus** *(string) --*

                  Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

                  Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

                  * Redis versions earlier than 2.8.6.

                  * Redis (cluster mode disabled): T1 node types.

                  * Redis (cluster mode enabled): T1 node types.

                - **Resharding** *(dict) --*

                  The status of an online resharding operation.

                  - **SlotMigration** *(dict) --*

                    Represents the progress of an online resharding operation.

                    - **ProgressPercentage** *(float) --*

                      The percentage of the slot migration that is complete.

                - **AuthTokenStatus** *(string) --*

                  The auth token status

              - **MemberClusters** *(list) --*

                The names of all the cache clusters that are part of this replication group.

                - *(string) --*

              - **NodeGroups** *(list) --*

                A list of node groups in this replication group. For Redis (cluster mode disabled)
                replication groups, this is a single-element list. For Redis (cluster mode enabled)
                replication groups, the list contains an entry for each node group (shard).

                - *(dict) --*

                  Represents a collection of cache nodes in a replication group. One node in the node group
                  is the read/write primary node. All the other nodes are read-only Replica nodes.

                  - **NodeGroupId** *(string) --*

                    The identifier for the node group (shard). A Redis (cluster mode disabled) replication
                    group contains only 1 node group; therefore, the node group ID is 0001. A Redis
                    (cluster mode enabled) replication group contains 1 to 90 node groups numbered 0001 to
                    0090. Optionally, the user can provide the id for a node group.

                  - **Status** *(string) --*

                    The current state of this replication group - ``creating`` , ``available`` , etc.

                  - **PrimaryEndpoint** *(dict) --*

                    The endpoint of the primary node in this node group (shard).

                    - **Address** *(string) --*

                      The DNS hostname of the cache node.

                    - **Port** *(integer) --*

                      The port number that the cache engine is listening on.

                  - **ReaderEndpoint** *(dict) --*

                    The endpoint of the replica nodes in this node group (shard).

                    - **Address** *(string) --*

                      The DNS hostname of the cache node.

                    - **Port** *(integer) --*

                      The port number that the cache engine is listening on.

                  - **Slots** *(string) --*

                    The keyspace for this node group (shard).

                  - **NodeGroupMembers** *(list) --*

                    A list containing information about individual nodes within the node group (shard).

                    - *(dict) --*

                      Represents a single node within a node group (shard).

                      - **CacheClusterId** *(string) --*

                        The ID of the cluster to which the node belongs.

                      - **CacheNodeId** *(string) --*

                        The ID of the node within its cluster. A node ID is a numeric identifier (0001,
                        0002, etc.).

                      - **ReadEndpoint** *(dict) --*

                        The information required for client programs to connect to a node for read
                        operations. The read endpoint is only applicable on Redis (cluster mode disabled)
                        clusters.

                        - **Address** *(string) --*

                          The DNS hostname of the cache node.

                        - **Port** *(integer) --*

                          The port number that the cache engine is listening on.

                      - **PreferredAvailabilityZone** *(string) --*

                        The name of the Availability Zone in which the node is located.

                      - **CurrentRole** *(string) --*

                        The role that is currently assigned to the node - ``primary`` or ``replica`` . This
                        member is only applicable for Redis (cluster mode disabled) replication groups.

              - **SnapshottingClusterId** *(string) --*

                The cluster ID that is used as the daily snapshot source for the replication group.

              - **AutomaticFailover** *(string) --*

                Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

                Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

                * Redis versions earlier than 2.8.6.

                * Redis (cluster mode disabled): T1 node types.

                * Redis (cluster mode enabled): T1 node types.

              - **ConfigurationEndpoint** *(dict) --*

                The configuration endpoint for this replication group. Use the configuration endpoint to
                connect to this replication group.

                - **Address** *(string) --*

                  The DNS hostname of the cache node.

                - **Port** *(integer) --*

                  The port number that the cache engine is listening on.

              - **SnapshotRetentionLimit** *(integer) --*

                The number of days for which ElastiCache retains automatic cluster snapshots before
                deleting them. For example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot that was
                taken today is retained for 5 days before being deleted.

                .. warning::

                  If the value of ``SnapshotRetentionLimit`` is set to zero (0), backups are turned off.

              - **SnapshotWindow** *(string) --*

                The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of
                your node group (shard).

                Example: ``05:00-09:00``

                If you do not specify this parameter, ElastiCache automatically chooses an appropriate time
                range.

                .. note::

                  This parameter is only valid if the ``Engine`` parameter is ``redis`` .

              - **ClusterEnabled** *(boolean) --*

                A flag indicating whether or not this replication group is cluster enabled; i.e., whether
                its data can be partitioned across multiple shards (API/CLI: node groups).

                Valid values: ``true`` | ``false``

              - **CacheNodeType** *(string) --*

                The name of the compute and memory capacity node type for each node in the replication
                group.

              - **AuthTokenEnabled** *(boolean) --*

                A flag that enables using an ``AuthToken`` (password) when issuing Redis commands.

                Default: ``false``

              - **AuthTokenLastModifiedDate** *(datetime) --*

                The date the auth token was last modified

              - **TransitEncryptionEnabled** *(boolean) --*

                A flag that enables in-transit encryption when set to ``true`` .

                You cannot modify the value of ``TransitEncryptionEnabled`` after the cluster is created.
                To enable in-transit encryption on a cluster you must set ``TransitEncryptionEnabled`` to
                ``true`` when you create a cluster.

                 **Required:** Only available when creating a replication group in an Amazon VPC using
                 redis version ``3.2.6`` , ``4.x`` or later.

                Default: ``false``

              - **AtRestEncryptionEnabled** *(boolean) --*

                A flag that enables encryption at-rest when set to ``true`` .

                You cannot modify the value of ``AtRestEncryptionEnabled`` after the cluster is created. To
                enable encryption at-rest on a cluster you must set ``AtRestEncryptionEnabled`` to ``true``
                when you create a cluster.

                 **Required:** Only available when creating a replication group in an Amazon VPC using
                 redis version ``3.2.6`` , ``4.x`` or later.

                Default: ``false``

              - **KmsKeyId** *(string) --*

                The ID of the KMS key used to encrypt the disk in the cluster.

        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_cache_clusters"]
    ) -> paginator_scope.DescribeCacheClustersPaginator:
        """
        Get Paginator for `describe_cache_clusters` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_cache_engine_versions"]
    ) -> paginator_scope.DescribeCacheEngineVersionsPaginator:
        """
        Get Paginator for `describe_cache_engine_versions` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_cache_parameter_groups"]
    ) -> paginator_scope.DescribeCacheParameterGroupsPaginator:
        """
        Get Paginator for `describe_cache_parameter_groups` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_cache_parameters"]
    ) -> paginator_scope.DescribeCacheParametersPaginator:
        """
        Get Paginator for `describe_cache_parameters` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_cache_security_groups"]
    ) -> paginator_scope.DescribeCacheSecurityGroupsPaginator:
        """
        Get Paginator for `describe_cache_security_groups` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_cache_subnet_groups"]
    ) -> paginator_scope.DescribeCacheSubnetGroupsPaginator:
        """
        Get Paginator for `describe_cache_subnet_groups` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_engine_default_parameters"]
    ) -> paginator_scope.DescribeEngineDefaultParametersPaginator:
        """
        Get Paginator for `describe_engine_default_parameters` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_events"]
    ) -> paginator_scope.DescribeEventsPaginator:
        """
        Get Paginator for `describe_events` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_replication_groups"]
    ) -> paginator_scope.DescribeReplicationGroupsPaginator:
        """
        Get Paginator for `describe_replication_groups` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_reserved_cache_nodes"]
    ) -> paginator_scope.DescribeReservedCacheNodesPaginator:
        """
        Get Paginator for `describe_reserved_cache_nodes` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_reserved_cache_nodes_offerings"]
    ) -> paginator_scope.DescribeReservedCacheNodesOfferingsPaginator:
        """
        Get Paginator for `describe_reserved_cache_nodes_offerings` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_service_updates"]
    ) -> paginator_scope.DescribeServiceUpdatesPaginator:
        """
        Get Paginator for `describe_service_updates` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_snapshots"]
    ) -> paginator_scope.DescribeSnapshotsPaginator:
        """
        Get Paginator for `describe_snapshots` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_update_actions"]
    ) -> paginator_scope.DescribeUpdateActionsPaginator:
        """
        Get Paginator for `describe_update_actions` operation.
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

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["cache_cluster_available"]
    ) -> waiter_scope.CacheClusterAvailableWaiter:
        """
        Get Waiter `cache_cluster_available`.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["cache_cluster_deleted"]
    ) -> waiter_scope.CacheClusterDeletedWaiter:
        """
        Get Waiter `cache_cluster_deleted`.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["replication_group_available"]
    ) -> waiter_scope.ReplicationGroupAvailableWaiter:
        """
        Get Waiter `replication_group_available`.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["replication_group_deleted"]
    ) -> waiter_scope.ReplicationGroupDeletedWaiter:
        """
        Get Waiter `replication_group_deleted`.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(self, waiter_name: str) -> Boto3Waiter:
        """
        Returns an object that can wait for some condition.

        :type waiter_name: str
        :param waiter_name: The name of the waiter to get. See the waiters
            section of the service docs for a list of available waiters.

        :returns: The specified waiter object.
        :rtype: botocore.waiter.Waiter
        """


class Exceptions:
    APICallRateForCustomerExceededFault: Boto3ClientError
    AuthorizationAlreadyExistsFault: Boto3ClientError
    AuthorizationNotFoundFault: Boto3ClientError
    CacheClusterAlreadyExistsFault: Boto3ClientError
    CacheClusterNotFoundFault: Boto3ClientError
    CacheParameterGroupAlreadyExistsFault: Boto3ClientError
    CacheParameterGroupNotFoundFault: Boto3ClientError
    CacheParameterGroupQuotaExceededFault: Boto3ClientError
    CacheSecurityGroupAlreadyExistsFault: Boto3ClientError
    CacheSecurityGroupNotFoundFault: Boto3ClientError
    CacheSecurityGroupQuotaExceededFault: Boto3ClientError
    CacheSubnetGroupAlreadyExistsFault: Boto3ClientError
    CacheSubnetGroupInUse: Boto3ClientError
    CacheSubnetGroupNotFoundFault: Boto3ClientError
    CacheSubnetGroupQuotaExceededFault: Boto3ClientError
    CacheSubnetQuotaExceededFault: Boto3ClientError
    ClientError: Boto3ClientError
    ClusterQuotaForCustomerExceededFault: Boto3ClientError
    InsufficientCacheClusterCapacityFault: Boto3ClientError
    InvalidARNFault: Boto3ClientError
    InvalidCacheClusterStateFault: Boto3ClientError
    InvalidCacheParameterGroupStateFault: Boto3ClientError
    InvalidCacheSecurityGroupStateFault: Boto3ClientError
    InvalidKMSKeyFault: Boto3ClientError
    InvalidParameterCombinationException: Boto3ClientError
    InvalidParameterValueException: Boto3ClientError
    InvalidReplicationGroupStateFault: Boto3ClientError
    InvalidSnapshotStateFault: Boto3ClientError
    InvalidSubnet: Boto3ClientError
    InvalidVPCNetworkStateFault: Boto3ClientError
    NoOperationFault: Boto3ClientError
    NodeGroupNotFoundFault: Boto3ClientError
    NodeGroupsPerReplicationGroupQuotaExceededFault: Boto3ClientError
    NodeQuotaForClusterExceededFault: Boto3ClientError
    NodeQuotaForCustomerExceededFault: Boto3ClientError
    ReplicationGroupAlreadyExistsFault: Boto3ClientError
    ReplicationGroupAlreadyUnderMigrationFault: Boto3ClientError
    ReplicationGroupNotFoundFault: Boto3ClientError
    ReplicationGroupNotUnderMigrationFault: Boto3ClientError
    ReservedCacheNodeAlreadyExistsFault: Boto3ClientError
    ReservedCacheNodeNotFoundFault: Boto3ClientError
    ReservedCacheNodeQuotaExceededFault: Boto3ClientError
    ReservedCacheNodesOfferingNotFoundFault: Boto3ClientError
    ServiceLinkedRoleNotFoundFault: Boto3ClientError
    ServiceUpdateNotFoundFault: Boto3ClientError
    SnapshotAlreadyExistsFault: Boto3ClientError
    SnapshotFeatureNotSupportedFault: Boto3ClientError
    SnapshotNotFoundFault: Boto3ClientError
    SnapshotQuotaExceededFault: Boto3ClientError
    SubnetInUse: Boto3ClientError
    TagNotFoundFault: Boto3ClientError
    TagQuotaPerResourceExceeded: Boto3ClientError
    TestFailoverNotAvailableFault: Boto3ClientError
