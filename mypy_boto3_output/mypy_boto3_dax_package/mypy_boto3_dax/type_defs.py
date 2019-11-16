"Main interface for dax type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from typing_extensions import TypedDict


__all__ = (
    "ClientCreateClusterResponseClusterClusterDiscoveryEndpointTypeDef",
    "ClientCreateClusterResponseClusterNodesEndpointTypeDef",
    "ClientCreateClusterResponseClusterNodesTypeDef",
    "ClientCreateClusterResponseClusterNotificationConfigurationTypeDef",
    "ClientCreateClusterResponseClusterParameterGroupTypeDef",
    "ClientCreateClusterResponseClusterSSEDescriptionTypeDef",
    "ClientCreateClusterResponseClusterSecurityGroupsTypeDef",
    "ClientCreateClusterResponseClusterTypeDef",
    "ClientCreateClusterResponseTypeDef",
    "ClientCreateClusterSSESpecificationTypeDef",
    "ClientCreateClusterTagsTypeDef",
    "ClientCreateParameterGroupResponseParameterGroupTypeDef",
    "ClientCreateParameterGroupResponseTypeDef",
    "ClientCreateSubnetGroupResponseSubnetGroupSubnetsTypeDef",
    "ClientCreateSubnetGroupResponseSubnetGroupTypeDef",
    "ClientCreateSubnetGroupResponseTypeDef",
    "ClientDecreaseReplicationFactorResponseClusterClusterDiscoveryEndpointTypeDef",
    "ClientDecreaseReplicationFactorResponseClusterNodesEndpointTypeDef",
    "ClientDecreaseReplicationFactorResponseClusterNodesTypeDef",
    "ClientDecreaseReplicationFactorResponseClusterNotificationConfigurationTypeDef",
    "ClientDecreaseReplicationFactorResponseClusterParameterGroupTypeDef",
    "ClientDecreaseReplicationFactorResponseClusterSSEDescriptionTypeDef",
    "ClientDecreaseReplicationFactorResponseClusterSecurityGroupsTypeDef",
    "ClientDecreaseReplicationFactorResponseClusterTypeDef",
    "ClientDecreaseReplicationFactorResponseTypeDef",
    "ClientDeleteClusterResponseClusterClusterDiscoveryEndpointTypeDef",
    "ClientDeleteClusterResponseClusterNodesEndpointTypeDef",
    "ClientDeleteClusterResponseClusterNodesTypeDef",
    "ClientDeleteClusterResponseClusterNotificationConfigurationTypeDef",
    "ClientDeleteClusterResponseClusterParameterGroupTypeDef",
    "ClientDeleteClusterResponseClusterSSEDescriptionTypeDef",
    "ClientDeleteClusterResponseClusterSecurityGroupsTypeDef",
    "ClientDeleteClusterResponseClusterTypeDef",
    "ClientDeleteClusterResponseTypeDef",
    "ClientDeleteParameterGroupResponseTypeDef",
    "ClientDeleteSubnetGroupResponseTypeDef",
    "ClientDescribeClustersResponseClustersClusterDiscoveryEndpointTypeDef",
    "ClientDescribeClustersResponseClustersNodesEndpointTypeDef",
    "ClientDescribeClustersResponseClustersNodesTypeDef",
    "ClientDescribeClustersResponseClustersNotificationConfigurationTypeDef",
    "ClientDescribeClustersResponseClustersParameterGroupTypeDef",
    "ClientDescribeClustersResponseClustersSSEDescriptionTypeDef",
    "ClientDescribeClustersResponseClustersSecurityGroupsTypeDef",
    "ClientDescribeClustersResponseClustersTypeDef",
    "ClientDescribeClustersResponseTypeDef",
    "ClientDescribeDefaultParametersResponseParametersNodeTypeSpecificValuesTypeDef",
    "ClientDescribeDefaultParametersResponseParametersTypeDef",
    "ClientDescribeDefaultParametersResponseTypeDef",
    "ClientDescribeEventsResponseEventsTypeDef",
    "ClientDescribeEventsResponseTypeDef",
    "ClientDescribeParameterGroupsResponseParameterGroupsTypeDef",
    "ClientDescribeParameterGroupsResponseTypeDef",
    "ClientDescribeParametersResponseParametersNodeTypeSpecificValuesTypeDef",
    "ClientDescribeParametersResponseParametersTypeDef",
    "ClientDescribeParametersResponseTypeDef",
    "ClientDescribeSubnetGroupsResponseSubnetGroupsSubnetsTypeDef",
    "ClientDescribeSubnetGroupsResponseSubnetGroupsTypeDef",
    "ClientDescribeSubnetGroupsResponseTypeDef",
    "ClientIncreaseReplicationFactorResponseClusterClusterDiscoveryEndpointTypeDef",
    "ClientIncreaseReplicationFactorResponseClusterNodesEndpointTypeDef",
    "ClientIncreaseReplicationFactorResponseClusterNodesTypeDef",
    "ClientIncreaseReplicationFactorResponseClusterNotificationConfigurationTypeDef",
    "ClientIncreaseReplicationFactorResponseClusterParameterGroupTypeDef",
    "ClientIncreaseReplicationFactorResponseClusterSSEDescriptionTypeDef",
    "ClientIncreaseReplicationFactorResponseClusterSecurityGroupsTypeDef",
    "ClientIncreaseReplicationFactorResponseClusterTypeDef",
    "ClientIncreaseReplicationFactorResponseTypeDef",
    "ClientListTagsResponseTagsTypeDef",
    "ClientListTagsResponseTypeDef",
    "ClientRebootNodeResponseClusterClusterDiscoveryEndpointTypeDef",
    "ClientRebootNodeResponseClusterNodesEndpointTypeDef",
    "ClientRebootNodeResponseClusterNodesTypeDef",
    "ClientRebootNodeResponseClusterNotificationConfigurationTypeDef",
    "ClientRebootNodeResponseClusterParameterGroupTypeDef",
    "ClientRebootNodeResponseClusterSSEDescriptionTypeDef",
    "ClientRebootNodeResponseClusterSecurityGroupsTypeDef",
    "ClientRebootNodeResponseClusterTypeDef",
    "ClientRebootNodeResponseTypeDef",
    "ClientTagResourceResponseTagsTypeDef",
    "ClientTagResourceResponseTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientUntagResourceResponseTagsTypeDef",
    "ClientUntagResourceResponseTypeDef",
    "ClientUpdateClusterResponseClusterClusterDiscoveryEndpointTypeDef",
    "ClientUpdateClusterResponseClusterNodesEndpointTypeDef",
    "ClientUpdateClusterResponseClusterNodesTypeDef",
    "ClientUpdateClusterResponseClusterNotificationConfigurationTypeDef",
    "ClientUpdateClusterResponseClusterParameterGroupTypeDef",
    "ClientUpdateClusterResponseClusterSSEDescriptionTypeDef",
    "ClientUpdateClusterResponseClusterSecurityGroupsTypeDef",
    "ClientUpdateClusterResponseClusterTypeDef",
    "ClientUpdateClusterResponseTypeDef",
    "ClientUpdateParameterGroupParameterNameValuesTypeDef",
    "ClientUpdateParameterGroupResponseParameterGroupTypeDef",
    "ClientUpdateParameterGroupResponseTypeDef",
    "ClientUpdateSubnetGroupResponseSubnetGroupSubnetsTypeDef",
    "ClientUpdateSubnetGroupResponseSubnetGroupTypeDef",
    "ClientUpdateSubnetGroupResponseTypeDef",
    "DescribeClustersPaginatePaginationConfigTypeDef",
    "DescribeClustersPaginateResponseClustersClusterDiscoveryEndpointTypeDef",
    "DescribeClustersPaginateResponseClustersNodesEndpointTypeDef",
    "DescribeClustersPaginateResponseClustersNodesTypeDef",
    "DescribeClustersPaginateResponseClustersNotificationConfigurationTypeDef",
    "DescribeClustersPaginateResponseClustersParameterGroupTypeDef",
    "DescribeClustersPaginateResponseClustersSSEDescriptionTypeDef",
    "DescribeClustersPaginateResponseClustersSecurityGroupsTypeDef",
    "DescribeClustersPaginateResponseClustersTypeDef",
    "DescribeClustersPaginateResponseTypeDef",
    "DescribeDefaultParametersPaginatePaginationConfigTypeDef",
    "DescribeDefaultParametersPaginateResponseParametersNodeTypeSpecificValuesTypeDef",
    "DescribeDefaultParametersPaginateResponseParametersTypeDef",
    "DescribeDefaultParametersPaginateResponseTypeDef",
    "DescribeEventsPaginatePaginationConfigTypeDef",
    "DescribeEventsPaginateResponseEventsTypeDef",
    "DescribeEventsPaginateResponseTypeDef",
    "DescribeParameterGroupsPaginatePaginationConfigTypeDef",
    "DescribeParameterGroupsPaginateResponseParameterGroupsTypeDef",
    "DescribeParameterGroupsPaginateResponseTypeDef",
    "DescribeParametersPaginatePaginationConfigTypeDef",
    "DescribeParametersPaginateResponseParametersNodeTypeSpecificValuesTypeDef",
    "DescribeParametersPaginateResponseParametersTypeDef",
    "DescribeParametersPaginateResponseTypeDef",
    "DescribeSubnetGroupsPaginatePaginationConfigTypeDef",
    "DescribeSubnetGroupsPaginateResponseSubnetGroupsSubnetsTypeDef",
    "DescribeSubnetGroupsPaginateResponseSubnetGroupsTypeDef",
    "DescribeSubnetGroupsPaginateResponseTypeDef",
    "ListTagsPaginatePaginationConfigTypeDef",
    "ListTagsPaginateResponseTagsTypeDef",
    "ListTagsPaginateResponseTypeDef",
)


_ClientCreateClusterResponseClusterClusterDiscoveryEndpointTypeDef = TypedDict(
    "_ClientCreateClusterResponseClusterClusterDiscoveryEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientCreateClusterResponseClusterClusterDiscoveryEndpointTypeDef(
    _ClientCreateClusterResponseClusterClusterDiscoveryEndpointTypeDef
):
    """
    Type definition for `ClientCreateClusterResponseCluster` `ClusterDiscoveryEndpoint`

    The configuration endpoint for this DAX cluster, consisting of a DNS name and a port
    number. Client applications can specify this endpoint, rather than an individual node
    endpoint, and allow the DAX client software to intelligently route requests and responses
    to nodes in the DAX cluster.

    - **Address** *(string) --*

      The DNS hostname of the endpoint.

    - **Port** *(integer) --*

      The port number that applications should use to connect to the endpoint.
    """


_ClientCreateClusterResponseClusterNodesEndpointTypeDef = TypedDict(
    "_ClientCreateClusterResponseClusterNodesEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientCreateClusterResponseClusterNodesEndpointTypeDef(
    _ClientCreateClusterResponseClusterNodesEndpointTypeDef
):
    """
    Type definition for `ClientCreateClusterResponseClusterNodes` `Endpoint`

    The endpoint for the node, consisting of a DNS name and a port number. Client
    applications can connect directly to a node endpoint, if desired (as an alternative to
    allowing DAX client software to intelligently route requests and responses to nodes in
    the DAX cluster.

    - **Address** *(string) --*

      The DNS hostname of the endpoint.

    - **Port** *(integer) --*

      The port number that applications should use to connect to the endpoint.
    """


_ClientCreateClusterResponseClusterNodesTypeDef = TypedDict(
    "_ClientCreateClusterResponseClusterNodesTypeDef",
    {
        "NodeId": str,
        "Endpoint": ClientCreateClusterResponseClusterNodesEndpointTypeDef,
        "NodeCreateTime": datetime,
        "AvailabilityZone": str,
        "NodeStatus": str,
        "ParameterGroupStatus": str,
    },
    total=False,
)


class ClientCreateClusterResponseClusterNodesTypeDef(
    _ClientCreateClusterResponseClusterNodesTypeDef
):
    """
    Type definition for `ClientCreateClusterResponseCluster` `Nodes`

    Represents an individual node within a DAX cluster.

    - **NodeId** *(string) --*

      A system-generated identifier for the node.

    - **Endpoint** *(dict) --*

      The endpoint for the node, consisting of a DNS name and a port number. Client
      applications can connect directly to a node endpoint, if desired (as an alternative to
      allowing DAX client software to intelligently route requests and responses to nodes in
      the DAX cluster.

      - **Address** *(string) --*

        The DNS hostname of the endpoint.

      - **Port** *(integer) --*

        The port number that applications should use to connect to the endpoint.

    - **NodeCreateTime** *(datetime) --*

      The date and time (in UNIX epoch format) when the node was launched.

    - **AvailabilityZone** *(string) --*

      The Availability Zone (AZ) in which the node has been deployed.

    - **NodeStatus** *(string) --*

      The current status of the node. For example: ``available`` .

    - **ParameterGroupStatus** *(string) --*

      The status of the parameter group associated with this node. For example, ``in-sync`` .
    """


_ClientCreateClusterResponseClusterNotificationConfigurationTypeDef = TypedDict(
    "_ClientCreateClusterResponseClusterNotificationConfigurationTypeDef",
    {"TopicArn": str, "TopicStatus": str},
    total=False,
)


class ClientCreateClusterResponseClusterNotificationConfigurationTypeDef(
    _ClientCreateClusterResponseClusterNotificationConfigurationTypeDef
):
    """
    Type definition for `ClientCreateClusterResponseCluster` `NotificationConfiguration`

    Describes a notification topic and its status. Notification topics are used for publishing
    DAX events to subscribers using Amazon Simple Notification Service (SNS).

    - **TopicArn** *(string) --*

      The Amazon Resource Name (ARN) that identifies the topic.

    - **TopicStatus** *(string) --*

      The current state of the topic.
    """


_ClientCreateClusterResponseClusterParameterGroupTypeDef = TypedDict(
    "_ClientCreateClusterResponseClusterParameterGroupTypeDef",
    {
        "ParameterGroupName": str,
        "ParameterApplyStatus": str,
        "NodeIdsToReboot": List[str],
    },
    total=False,
)


class ClientCreateClusterResponseClusterParameterGroupTypeDef(
    _ClientCreateClusterResponseClusterParameterGroupTypeDef
):
    """
    Type definition for `ClientCreateClusterResponseCluster` `ParameterGroup`

    The parameter group being used by nodes in the cluster.

    - **ParameterGroupName** *(string) --*

      The name of the parameter group.

    - **ParameterApplyStatus** *(string) --*

      The status of parameter updates.

    - **NodeIdsToReboot** *(list) --*

      The node IDs of one or more nodes to be rebooted.

      - *(string) --*
    """


_ClientCreateClusterResponseClusterSSEDescriptionTypeDef = TypedDict(
    "_ClientCreateClusterResponseClusterSSEDescriptionTypeDef",
    {"Status": str},
    total=False,
)


class ClientCreateClusterResponseClusterSSEDescriptionTypeDef(
    _ClientCreateClusterResponseClusterSSEDescriptionTypeDef
):
    """
    Type definition for `ClientCreateClusterResponseCluster` `SSEDescription`

    The description of the server-side encryption status on the specified DAX cluster.

    - **Status** *(string) --*

      The current state of server-side encryption:

      * ``ENABLING`` - Server-side encryption is being enabled.

      * ``ENABLED`` - Server-side encryption is enabled.

      * ``DISABLING`` - Server-side encryption is being disabled.

      * ``DISABLED`` - Server-side encryption is disabled.
    """


_ClientCreateClusterResponseClusterSecurityGroupsTypeDef = TypedDict(
    "_ClientCreateClusterResponseClusterSecurityGroupsTypeDef",
    {"SecurityGroupIdentifier": str, "Status": str},
    total=False,
)


class ClientCreateClusterResponseClusterSecurityGroupsTypeDef(
    _ClientCreateClusterResponseClusterSecurityGroupsTypeDef
):
    """
    Type definition for `ClientCreateClusterResponseCluster` `SecurityGroups`

    An individual VPC security group and its status.

    - **SecurityGroupIdentifier** *(string) --*

      The unique ID for this security group.

    - **Status** *(string) --*

      The status of this security group.
    """


_ClientCreateClusterResponseClusterTypeDef = TypedDict(
    "_ClientCreateClusterResponseClusterTypeDef",
    {
        "ClusterName": str,
        "Description": str,
        "ClusterArn": str,
        "TotalNodes": int,
        "ActiveNodes": int,
        "NodeType": str,
        "Status": str,
        "ClusterDiscoveryEndpoint": ClientCreateClusterResponseClusterClusterDiscoveryEndpointTypeDef,
        "NodeIdsToRemove": List[str],
        "Nodes": List[ClientCreateClusterResponseClusterNodesTypeDef],
        "PreferredMaintenanceWindow": str,
        "NotificationConfiguration": ClientCreateClusterResponseClusterNotificationConfigurationTypeDef,
        "SubnetGroup": str,
        "SecurityGroups": List[ClientCreateClusterResponseClusterSecurityGroupsTypeDef],
        "IamRoleArn": str,
        "ParameterGroup": ClientCreateClusterResponseClusterParameterGroupTypeDef,
        "SSEDescription": ClientCreateClusterResponseClusterSSEDescriptionTypeDef,
    },
    total=False,
)


class ClientCreateClusterResponseClusterTypeDef(
    _ClientCreateClusterResponseClusterTypeDef
):
    """
    Type definition for `ClientCreateClusterResponse` `Cluster`

    A description of the DAX cluster that you have created.

    - **ClusterName** *(string) --*

      The name of the DAX cluster.

    - **Description** *(string) --*

      The description of the cluster.

    - **ClusterArn** *(string) --*

      The Amazon Resource Name (ARN) that uniquely identifies the cluster.

    - **TotalNodes** *(integer) --*

      The total number of nodes in the cluster.

    - **ActiveNodes** *(integer) --*

      The number of nodes in the cluster that are active (i.e., capable of serving requests).

    - **NodeType** *(string) --*

      The node type for the nodes in the cluster. (All nodes in a DAX cluster are of the same
      type.)

    - **Status** *(string) --*

      The current status of the cluster.

    - **ClusterDiscoveryEndpoint** *(dict) --*

      The configuration endpoint for this DAX cluster, consisting of a DNS name and a port
      number. Client applications can specify this endpoint, rather than an individual node
      endpoint, and allow the DAX client software to intelligently route requests and responses
      to nodes in the DAX cluster.

      - **Address** *(string) --*

        The DNS hostname of the endpoint.

      - **Port** *(integer) --*

        The port number that applications should use to connect to the endpoint.

    - **NodeIdsToRemove** *(list) --*

      A list of nodes to be removed from the cluster.

      - *(string) --*

    - **Nodes** *(list) --*

      A list of nodes that are currently in the cluster.

      - *(dict) --*

        Represents an individual node within a DAX cluster.

        - **NodeId** *(string) --*

          A system-generated identifier for the node.

        - **Endpoint** *(dict) --*

          The endpoint for the node, consisting of a DNS name and a port number. Client
          applications can connect directly to a node endpoint, if desired (as an alternative to
          allowing DAX client software to intelligently route requests and responses to nodes in
          the DAX cluster.

          - **Address** *(string) --*

            The DNS hostname of the endpoint.

          - **Port** *(integer) --*

            The port number that applications should use to connect to the endpoint.

        - **NodeCreateTime** *(datetime) --*

          The date and time (in UNIX epoch format) when the node was launched.

        - **AvailabilityZone** *(string) --*

          The Availability Zone (AZ) in which the node has been deployed.

        - **NodeStatus** *(string) --*

          The current status of the node. For example: ``available`` .

        - **ParameterGroupStatus** *(string) --*

          The status of the parameter group associated with this node. For example, ``in-sync`` .

    - **PreferredMaintenanceWindow** *(string) --*

      A range of time when maintenance of DAX cluster software will be performed. For example:
      ``sun:01:00-sun:09:00`` . Cluster maintenance normally takes less than 30 minutes, and is
      performed automatically within the maintenance window.

    - **NotificationConfiguration** *(dict) --*

      Describes a notification topic and its status. Notification topics are used for publishing
      DAX events to subscribers using Amazon Simple Notification Service (SNS).

      - **TopicArn** *(string) --*

        The Amazon Resource Name (ARN) that identifies the topic.

      - **TopicStatus** *(string) --*

        The current state of the topic.

    - **SubnetGroup** *(string) --*

      The subnet group where the DAX cluster is running.

    - **SecurityGroups** *(list) --*

      A list of security groups, and the status of each, for the nodes in the cluster.

      - *(dict) --*

        An individual VPC security group and its status.

        - **SecurityGroupIdentifier** *(string) --*

          The unique ID for this security group.

        - **Status** *(string) --*

          The status of this security group.

    - **IamRoleArn** *(string) --*

      A valid Amazon Resource Name (ARN) that identifies an IAM role. At runtime, DAX will assume
      this role and use the role's permissions to access DynamoDB on your behalf.

    - **ParameterGroup** *(dict) --*

      The parameter group being used by nodes in the cluster.

      - **ParameterGroupName** *(string) --*

        The name of the parameter group.

      - **ParameterApplyStatus** *(string) --*

        The status of parameter updates.

      - **NodeIdsToReboot** *(list) --*

        The node IDs of one or more nodes to be rebooted.

        - *(string) --*

    - **SSEDescription** *(dict) --*

      The description of the server-side encryption status on the specified DAX cluster.

      - **Status** *(string) --*

        The current state of server-side encryption:

        * ``ENABLING`` - Server-side encryption is being enabled.

        * ``ENABLED`` - Server-side encryption is enabled.

        * ``DISABLING`` - Server-side encryption is being disabled.

        * ``DISABLED`` - Server-side encryption is disabled.
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

      A description of the DAX cluster that you have created.

      - **ClusterName** *(string) --*

        The name of the DAX cluster.

      - **Description** *(string) --*

        The description of the cluster.

      - **ClusterArn** *(string) --*

        The Amazon Resource Name (ARN) that uniquely identifies the cluster.

      - **TotalNodes** *(integer) --*

        The total number of nodes in the cluster.

      - **ActiveNodes** *(integer) --*

        The number of nodes in the cluster that are active (i.e., capable of serving requests).

      - **NodeType** *(string) --*

        The node type for the nodes in the cluster. (All nodes in a DAX cluster are of the same
        type.)

      - **Status** *(string) --*

        The current status of the cluster.

      - **ClusterDiscoveryEndpoint** *(dict) --*

        The configuration endpoint for this DAX cluster, consisting of a DNS name and a port
        number. Client applications can specify this endpoint, rather than an individual node
        endpoint, and allow the DAX client software to intelligently route requests and responses
        to nodes in the DAX cluster.

        - **Address** *(string) --*

          The DNS hostname of the endpoint.

        - **Port** *(integer) --*

          The port number that applications should use to connect to the endpoint.

      - **NodeIdsToRemove** *(list) --*

        A list of nodes to be removed from the cluster.

        - *(string) --*

      - **Nodes** *(list) --*

        A list of nodes that are currently in the cluster.

        - *(dict) --*

          Represents an individual node within a DAX cluster.

          - **NodeId** *(string) --*

            A system-generated identifier for the node.

          - **Endpoint** *(dict) --*

            The endpoint for the node, consisting of a DNS name and a port number. Client
            applications can connect directly to a node endpoint, if desired (as an alternative to
            allowing DAX client software to intelligently route requests and responses to nodes in
            the DAX cluster.

            - **Address** *(string) --*

              The DNS hostname of the endpoint.

            - **Port** *(integer) --*

              The port number that applications should use to connect to the endpoint.

          - **NodeCreateTime** *(datetime) --*

            The date and time (in UNIX epoch format) when the node was launched.

          - **AvailabilityZone** *(string) --*

            The Availability Zone (AZ) in which the node has been deployed.

          - **NodeStatus** *(string) --*

            The current status of the node. For example: ``available`` .

          - **ParameterGroupStatus** *(string) --*

            The status of the parameter group associated with this node. For example, ``in-sync`` .

      - **PreferredMaintenanceWindow** *(string) --*

        A range of time when maintenance of DAX cluster software will be performed. For example:
        ``sun:01:00-sun:09:00`` . Cluster maintenance normally takes less than 30 minutes, and is
        performed automatically within the maintenance window.

      - **NotificationConfiguration** *(dict) --*

        Describes a notification topic and its status. Notification topics are used for publishing
        DAX events to subscribers using Amazon Simple Notification Service (SNS).

        - **TopicArn** *(string) --*

          The Amazon Resource Name (ARN) that identifies the topic.

        - **TopicStatus** *(string) --*

          The current state of the topic.

      - **SubnetGroup** *(string) --*

        The subnet group where the DAX cluster is running.

      - **SecurityGroups** *(list) --*

        A list of security groups, and the status of each, for the nodes in the cluster.

        - *(dict) --*

          An individual VPC security group and its status.

          - **SecurityGroupIdentifier** *(string) --*

            The unique ID for this security group.

          - **Status** *(string) --*

            The status of this security group.

      - **IamRoleArn** *(string) --*

        A valid Amazon Resource Name (ARN) that identifies an IAM role. At runtime, DAX will assume
        this role and use the role's permissions to access DynamoDB on your behalf.

      - **ParameterGroup** *(dict) --*

        The parameter group being used by nodes in the cluster.

        - **ParameterGroupName** *(string) --*

          The name of the parameter group.

        - **ParameterApplyStatus** *(string) --*

          The status of parameter updates.

        - **NodeIdsToReboot** *(list) --*

          The node IDs of one or more nodes to be rebooted.

          - *(string) --*

      - **SSEDescription** *(dict) --*

        The description of the server-side encryption status on the specified DAX cluster.

        - **Status** *(string) --*

          The current state of server-side encryption:

          * ``ENABLING`` - Server-side encryption is being enabled.

          * ``ENABLED`` - Server-side encryption is enabled.

          * ``DISABLING`` - Server-side encryption is being disabled.

          * ``DISABLED`` - Server-side encryption is disabled.
    """


_ClientCreateClusterSSESpecificationTypeDef = TypedDict(
    "_ClientCreateClusterSSESpecificationTypeDef", {"Enabled": bool}
)


class ClientCreateClusterSSESpecificationTypeDef(
    _ClientCreateClusterSSESpecificationTypeDef
):
    """
    Type definition for `ClientCreateCluster` `SSESpecification`

    Represents the settings used to enable server-side encryption on the cluster.

    - **Enabled** *(boolean) --* **[REQUIRED]**

      Indicates whether server-side encryption is enabled (true) or disabled (false) on the cluster.
    """


_ClientCreateClusterTagsTypeDef = TypedDict(
    "_ClientCreateClusterTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateClusterTagsTypeDef(_ClientCreateClusterTagsTypeDef):
    """
    Type definition for `ClientCreateCluster` `Tags`

    A description of a tag. Every tag is a key-value pair. You can add up to 50 tags to a single
    DAX cluster.

    AWS-assigned tag names and values are automatically assigned the ``aws:`` prefix, which the
    user cannot assign. AWS-assigned tag names do not count towards the tag limit of 50.
    User-assigned tag names have the prefix ``user:`` .

    You cannot backdate the application of a tag.

    - **Key** *(string) --*

      The key for the tag. Tag keys are case sensitive. Every DAX cluster can only have one tag
      with the same key. If you try to add an existing tag (same key), the existing tag value will
      be updated to the new value.

    - **Value** *(string) --*

      The value of the tag. Tag values are case-sensitive and can be null.
    """


_ClientCreateParameterGroupResponseParameterGroupTypeDef = TypedDict(
    "_ClientCreateParameterGroupResponseParameterGroupTypeDef",
    {"ParameterGroupName": str, "Description": str},
    total=False,
)


class ClientCreateParameterGroupResponseParameterGroupTypeDef(
    _ClientCreateParameterGroupResponseParameterGroupTypeDef
):
    """
    Type definition for `ClientCreateParameterGroupResponse` `ParameterGroup`

    Represents the output of a *CreateParameterGroup* action.

    - **ParameterGroupName** *(string) --*

      The name of the parameter group.

    - **Description** *(string) --*

      A description of the parameter group.
    """


_ClientCreateParameterGroupResponseTypeDef = TypedDict(
    "_ClientCreateParameterGroupResponseTypeDef",
    {"ParameterGroup": ClientCreateParameterGroupResponseParameterGroupTypeDef},
    total=False,
)


class ClientCreateParameterGroupResponseTypeDef(
    _ClientCreateParameterGroupResponseTypeDef
):
    """
    Type definition for `ClientCreateParameterGroup` `Response`

    - **ParameterGroup** *(dict) --*

      Represents the output of a *CreateParameterGroup* action.

      - **ParameterGroupName** *(string) --*

        The name of the parameter group.

      - **Description** *(string) --*

        A description of the parameter group.
    """


_ClientCreateSubnetGroupResponseSubnetGroupSubnetsTypeDef = TypedDict(
    "_ClientCreateSubnetGroupResponseSubnetGroupSubnetsTypeDef",
    {"SubnetIdentifier": str, "SubnetAvailabilityZone": str},
    total=False,
)


class ClientCreateSubnetGroupResponseSubnetGroupSubnetsTypeDef(
    _ClientCreateSubnetGroupResponseSubnetGroupSubnetsTypeDef
):
    """
    Type definition for `ClientCreateSubnetGroupResponseSubnetGroup` `Subnets`

    Represents the subnet associated with a DAX cluster. This parameter refers to subnets
    defined in Amazon Virtual Private Cloud (Amazon VPC) and used with DAX.

    - **SubnetIdentifier** *(string) --*

      The system-assigned identifier for the subnet.

    - **SubnetAvailabilityZone** *(string) --*

      The Availability Zone (AZ) for the subnet.
    """


_ClientCreateSubnetGroupResponseSubnetGroupTypeDef = TypedDict(
    "_ClientCreateSubnetGroupResponseSubnetGroupTypeDef",
    {
        "SubnetGroupName": str,
        "Description": str,
        "VpcId": str,
        "Subnets": List[ClientCreateSubnetGroupResponseSubnetGroupSubnetsTypeDef],
    },
    total=False,
)


class ClientCreateSubnetGroupResponseSubnetGroupTypeDef(
    _ClientCreateSubnetGroupResponseSubnetGroupTypeDef
):
    """
    Type definition for `ClientCreateSubnetGroupResponse` `SubnetGroup`

    Represents the output of a *CreateSubnetGroup* operation.

    - **SubnetGroupName** *(string) --*

      The name of the subnet group.

    - **Description** *(string) --*

      The description of the subnet group.

    - **VpcId** *(string) --*

      The Amazon Virtual Private Cloud identifier (VPC ID) of the subnet group.

    - **Subnets** *(list) --*

      A list of subnets associated with the subnet group.

      - *(dict) --*

        Represents the subnet associated with a DAX cluster. This parameter refers to subnets
        defined in Amazon Virtual Private Cloud (Amazon VPC) and used with DAX.

        - **SubnetIdentifier** *(string) --*

          The system-assigned identifier for the subnet.

        - **SubnetAvailabilityZone** *(string) --*

          The Availability Zone (AZ) for the subnet.
    """


_ClientCreateSubnetGroupResponseTypeDef = TypedDict(
    "_ClientCreateSubnetGroupResponseTypeDef",
    {"SubnetGroup": ClientCreateSubnetGroupResponseSubnetGroupTypeDef},
    total=False,
)


class ClientCreateSubnetGroupResponseTypeDef(_ClientCreateSubnetGroupResponseTypeDef):
    """
    Type definition for `ClientCreateSubnetGroup` `Response`

    - **SubnetGroup** *(dict) --*

      Represents the output of a *CreateSubnetGroup* operation.

      - **SubnetGroupName** *(string) --*

        The name of the subnet group.

      - **Description** *(string) --*

        The description of the subnet group.

      - **VpcId** *(string) --*

        The Amazon Virtual Private Cloud identifier (VPC ID) of the subnet group.

      - **Subnets** *(list) --*

        A list of subnets associated with the subnet group.

        - *(dict) --*

          Represents the subnet associated with a DAX cluster. This parameter refers to subnets
          defined in Amazon Virtual Private Cloud (Amazon VPC) and used with DAX.

          - **SubnetIdentifier** *(string) --*

            The system-assigned identifier for the subnet.

          - **SubnetAvailabilityZone** *(string) --*

            The Availability Zone (AZ) for the subnet.
    """


_ClientDecreaseReplicationFactorResponseClusterClusterDiscoveryEndpointTypeDef = TypedDict(
    "_ClientDecreaseReplicationFactorResponseClusterClusterDiscoveryEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientDecreaseReplicationFactorResponseClusterClusterDiscoveryEndpointTypeDef(
    _ClientDecreaseReplicationFactorResponseClusterClusterDiscoveryEndpointTypeDef
):
    """
    Type definition for `ClientDecreaseReplicationFactorResponseCluster` `ClusterDiscoveryEndpoint`

    The configuration endpoint for this DAX cluster, consisting of a DNS name and a port
    number. Client applications can specify this endpoint, rather than an individual node
    endpoint, and allow the DAX client software to intelligently route requests and responses
    to nodes in the DAX cluster.

    - **Address** *(string) --*

      The DNS hostname of the endpoint.

    - **Port** *(integer) --*

      The port number that applications should use to connect to the endpoint.
    """


_ClientDecreaseReplicationFactorResponseClusterNodesEndpointTypeDef = TypedDict(
    "_ClientDecreaseReplicationFactorResponseClusterNodesEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientDecreaseReplicationFactorResponseClusterNodesEndpointTypeDef(
    _ClientDecreaseReplicationFactorResponseClusterNodesEndpointTypeDef
):
    """
    Type definition for `ClientDecreaseReplicationFactorResponseClusterNodes` `Endpoint`

    The endpoint for the node, consisting of a DNS name and a port number. Client
    applications can connect directly to a node endpoint, if desired (as an alternative to
    allowing DAX client software to intelligently route requests and responses to nodes in
    the DAX cluster.

    - **Address** *(string) --*

      The DNS hostname of the endpoint.

    - **Port** *(integer) --*

      The port number that applications should use to connect to the endpoint.
    """


_ClientDecreaseReplicationFactorResponseClusterNodesTypeDef = TypedDict(
    "_ClientDecreaseReplicationFactorResponseClusterNodesTypeDef",
    {
        "NodeId": str,
        "Endpoint": ClientDecreaseReplicationFactorResponseClusterNodesEndpointTypeDef,
        "NodeCreateTime": datetime,
        "AvailabilityZone": str,
        "NodeStatus": str,
        "ParameterGroupStatus": str,
    },
    total=False,
)


class ClientDecreaseReplicationFactorResponseClusterNodesTypeDef(
    _ClientDecreaseReplicationFactorResponseClusterNodesTypeDef
):
    """
    Type definition for `ClientDecreaseReplicationFactorResponseCluster` `Nodes`

    Represents an individual node within a DAX cluster.

    - **NodeId** *(string) --*

      A system-generated identifier for the node.

    - **Endpoint** *(dict) --*

      The endpoint for the node, consisting of a DNS name and a port number. Client
      applications can connect directly to a node endpoint, if desired (as an alternative to
      allowing DAX client software to intelligently route requests and responses to nodes in
      the DAX cluster.

      - **Address** *(string) --*

        The DNS hostname of the endpoint.

      - **Port** *(integer) --*

        The port number that applications should use to connect to the endpoint.

    - **NodeCreateTime** *(datetime) --*

      The date and time (in UNIX epoch format) when the node was launched.

    - **AvailabilityZone** *(string) --*

      The Availability Zone (AZ) in which the node has been deployed.

    - **NodeStatus** *(string) --*

      The current status of the node. For example: ``available`` .

    - **ParameterGroupStatus** *(string) --*

      The status of the parameter group associated with this node. For example, ``in-sync`` .
    """


_ClientDecreaseReplicationFactorResponseClusterNotificationConfigurationTypeDef = TypedDict(
    "_ClientDecreaseReplicationFactorResponseClusterNotificationConfigurationTypeDef",
    {"TopicArn": str, "TopicStatus": str},
    total=False,
)


class ClientDecreaseReplicationFactorResponseClusterNotificationConfigurationTypeDef(
    _ClientDecreaseReplicationFactorResponseClusterNotificationConfigurationTypeDef
):
    """
    Type definition for `ClientDecreaseReplicationFactorResponseCluster` `NotificationConfiguration`

    Describes a notification topic and its status. Notification topics are used for publishing
    DAX events to subscribers using Amazon Simple Notification Service (SNS).

    - **TopicArn** *(string) --*

      The Amazon Resource Name (ARN) that identifies the topic.

    - **TopicStatus** *(string) --*

      The current state of the topic.
    """


_ClientDecreaseReplicationFactorResponseClusterParameterGroupTypeDef = TypedDict(
    "_ClientDecreaseReplicationFactorResponseClusterParameterGroupTypeDef",
    {
        "ParameterGroupName": str,
        "ParameterApplyStatus": str,
        "NodeIdsToReboot": List[str],
    },
    total=False,
)


class ClientDecreaseReplicationFactorResponseClusterParameterGroupTypeDef(
    _ClientDecreaseReplicationFactorResponseClusterParameterGroupTypeDef
):
    """
    Type definition for `ClientDecreaseReplicationFactorResponseCluster` `ParameterGroup`

    The parameter group being used by nodes in the cluster.

    - **ParameterGroupName** *(string) --*

      The name of the parameter group.

    - **ParameterApplyStatus** *(string) --*

      The status of parameter updates.

    - **NodeIdsToReboot** *(list) --*

      The node IDs of one or more nodes to be rebooted.

      - *(string) --*
    """


_ClientDecreaseReplicationFactorResponseClusterSSEDescriptionTypeDef = TypedDict(
    "_ClientDecreaseReplicationFactorResponseClusterSSEDescriptionTypeDef",
    {"Status": str},
    total=False,
)


class ClientDecreaseReplicationFactorResponseClusterSSEDescriptionTypeDef(
    _ClientDecreaseReplicationFactorResponseClusterSSEDescriptionTypeDef
):
    """
    Type definition for `ClientDecreaseReplicationFactorResponseCluster` `SSEDescription`

    The description of the server-side encryption status on the specified DAX cluster.

    - **Status** *(string) --*

      The current state of server-side encryption:

      * ``ENABLING`` - Server-side encryption is being enabled.

      * ``ENABLED`` - Server-side encryption is enabled.

      * ``DISABLING`` - Server-side encryption is being disabled.

      * ``DISABLED`` - Server-side encryption is disabled.
    """


_ClientDecreaseReplicationFactorResponseClusterSecurityGroupsTypeDef = TypedDict(
    "_ClientDecreaseReplicationFactorResponseClusterSecurityGroupsTypeDef",
    {"SecurityGroupIdentifier": str, "Status": str},
    total=False,
)


class ClientDecreaseReplicationFactorResponseClusterSecurityGroupsTypeDef(
    _ClientDecreaseReplicationFactorResponseClusterSecurityGroupsTypeDef
):
    """
    Type definition for `ClientDecreaseReplicationFactorResponseCluster` `SecurityGroups`

    An individual VPC security group and its status.

    - **SecurityGroupIdentifier** *(string) --*

      The unique ID for this security group.

    - **Status** *(string) --*

      The status of this security group.
    """


_ClientDecreaseReplicationFactorResponseClusterTypeDef = TypedDict(
    "_ClientDecreaseReplicationFactorResponseClusterTypeDef",
    {
        "ClusterName": str,
        "Description": str,
        "ClusterArn": str,
        "TotalNodes": int,
        "ActiveNodes": int,
        "NodeType": str,
        "Status": str,
        "ClusterDiscoveryEndpoint": ClientDecreaseReplicationFactorResponseClusterClusterDiscoveryEndpointTypeDef,
        "NodeIdsToRemove": List[str],
        "Nodes": List[ClientDecreaseReplicationFactorResponseClusterNodesTypeDef],
        "PreferredMaintenanceWindow": str,
        "NotificationConfiguration": ClientDecreaseReplicationFactorResponseClusterNotificationConfigurationTypeDef,
        "SubnetGroup": str,
        "SecurityGroups": List[
            ClientDecreaseReplicationFactorResponseClusterSecurityGroupsTypeDef
        ],
        "IamRoleArn": str,
        "ParameterGroup": ClientDecreaseReplicationFactorResponseClusterParameterGroupTypeDef,
        "SSEDescription": ClientDecreaseReplicationFactorResponseClusterSSEDescriptionTypeDef,
    },
    total=False,
)


class ClientDecreaseReplicationFactorResponseClusterTypeDef(
    _ClientDecreaseReplicationFactorResponseClusterTypeDef
):
    """
    Type definition for `ClientDecreaseReplicationFactorResponse` `Cluster`

    A description of the DAX cluster, after you have decreased its replication factor.

    - **ClusterName** *(string) --*

      The name of the DAX cluster.

    - **Description** *(string) --*

      The description of the cluster.

    - **ClusterArn** *(string) --*

      The Amazon Resource Name (ARN) that uniquely identifies the cluster.

    - **TotalNodes** *(integer) --*

      The total number of nodes in the cluster.

    - **ActiveNodes** *(integer) --*

      The number of nodes in the cluster that are active (i.e., capable of serving requests).

    - **NodeType** *(string) --*

      The node type for the nodes in the cluster. (All nodes in a DAX cluster are of the same
      type.)

    - **Status** *(string) --*

      The current status of the cluster.

    - **ClusterDiscoveryEndpoint** *(dict) --*

      The configuration endpoint for this DAX cluster, consisting of a DNS name and a port
      number. Client applications can specify this endpoint, rather than an individual node
      endpoint, and allow the DAX client software to intelligently route requests and responses
      to nodes in the DAX cluster.

      - **Address** *(string) --*

        The DNS hostname of the endpoint.

      - **Port** *(integer) --*

        The port number that applications should use to connect to the endpoint.

    - **NodeIdsToRemove** *(list) --*

      A list of nodes to be removed from the cluster.

      - *(string) --*

    - **Nodes** *(list) --*

      A list of nodes that are currently in the cluster.

      - *(dict) --*

        Represents an individual node within a DAX cluster.

        - **NodeId** *(string) --*

          A system-generated identifier for the node.

        - **Endpoint** *(dict) --*

          The endpoint for the node, consisting of a DNS name and a port number. Client
          applications can connect directly to a node endpoint, if desired (as an alternative to
          allowing DAX client software to intelligently route requests and responses to nodes in
          the DAX cluster.

          - **Address** *(string) --*

            The DNS hostname of the endpoint.

          - **Port** *(integer) --*

            The port number that applications should use to connect to the endpoint.

        - **NodeCreateTime** *(datetime) --*

          The date and time (in UNIX epoch format) when the node was launched.

        - **AvailabilityZone** *(string) --*

          The Availability Zone (AZ) in which the node has been deployed.

        - **NodeStatus** *(string) --*

          The current status of the node. For example: ``available`` .

        - **ParameterGroupStatus** *(string) --*

          The status of the parameter group associated with this node. For example, ``in-sync`` .

    - **PreferredMaintenanceWindow** *(string) --*

      A range of time when maintenance of DAX cluster software will be performed. For example:
      ``sun:01:00-sun:09:00`` . Cluster maintenance normally takes less than 30 minutes, and is
      performed automatically within the maintenance window.

    - **NotificationConfiguration** *(dict) --*

      Describes a notification topic and its status. Notification topics are used for publishing
      DAX events to subscribers using Amazon Simple Notification Service (SNS).

      - **TopicArn** *(string) --*

        The Amazon Resource Name (ARN) that identifies the topic.

      - **TopicStatus** *(string) --*

        The current state of the topic.

    - **SubnetGroup** *(string) --*

      The subnet group where the DAX cluster is running.

    - **SecurityGroups** *(list) --*

      A list of security groups, and the status of each, for the nodes in the cluster.

      - *(dict) --*

        An individual VPC security group and its status.

        - **SecurityGroupIdentifier** *(string) --*

          The unique ID for this security group.

        - **Status** *(string) --*

          The status of this security group.

    - **IamRoleArn** *(string) --*

      A valid Amazon Resource Name (ARN) that identifies an IAM role. At runtime, DAX will assume
      this role and use the role's permissions to access DynamoDB on your behalf.

    - **ParameterGroup** *(dict) --*

      The parameter group being used by nodes in the cluster.

      - **ParameterGroupName** *(string) --*

        The name of the parameter group.

      - **ParameterApplyStatus** *(string) --*

        The status of parameter updates.

      - **NodeIdsToReboot** *(list) --*

        The node IDs of one or more nodes to be rebooted.

        - *(string) --*

    - **SSEDescription** *(dict) --*

      The description of the server-side encryption status on the specified DAX cluster.

      - **Status** *(string) --*

        The current state of server-side encryption:

        * ``ENABLING`` - Server-side encryption is being enabled.

        * ``ENABLED`` - Server-side encryption is enabled.

        * ``DISABLING`` - Server-side encryption is being disabled.

        * ``DISABLED`` - Server-side encryption is disabled.
    """


_ClientDecreaseReplicationFactorResponseTypeDef = TypedDict(
    "_ClientDecreaseReplicationFactorResponseTypeDef",
    {"Cluster": ClientDecreaseReplicationFactorResponseClusterTypeDef},
    total=False,
)


class ClientDecreaseReplicationFactorResponseTypeDef(
    _ClientDecreaseReplicationFactorResponseTypeDef
):
    """
    Type definition for `ClientDecreaseReplicationFactor` `Response`

    - **Cluster** *(dict) --*

      A description of the DAX cluster, after you have decreased its replication factor.

      - **ClusterName** *(string) --*

        The name of the DAX cluster.

      - **Description** *(string) --*

        The description of the cluster.

      - **ClusterArn** *(string) --*

        The Amazon Resource Name (ARN) that uniquely identifies the cluster.

      - **TotalNodes** *(integer) --*

        The total number of nodes in the cluster.

      - **ActiveNodes** *(integer) --*

        The number of nodes in the cluster that are active (i.e., capable of serving requests).

      - **NodeType** *(string) --*

        The node type for the nodes in the cluster. (All nodes in a DAX cluster are of the same
        type.)

      - **Status** *(string) --*

        The current status of the cluster.

      - **ClusterDiscoveryEndpoint** *(dict) --*

        The configuration endpoint for this DAX cluster, consisting of a DNS name and a port
        number. Client applications can specify this endpoint, rather than an individual node
        endpoint, and allow the DAX client software to intelligently route requests and responses
        to nodes in the DAX cluster.

        - **Address** *(string) --*

          The DNS hostname of the endpoint.

        - **Port** *(integer) --*

          The port number that applications should use to connect to the endpoint.

      - **NodeIdsToRemove** *(list) --*

        A list of nodes to be removed from the cluster.

        - *(string) --*

      - **Nodes** *(list) --*

        A list of nodes that are currently in the cluster.

        - *(dict) --*

          Represents an individual node within a DAX cluster.

          - **NodeId** *(string) --*

            A system-generated identifier for the node.

          - **Endpoint** *(dict) --*

            The endpoint for the node, consisting of a DNS name and a port number. Client
            applications can connect directly to a node endpoint, if desired (as an alternative to
            allowing DAX client software to intelligently route requests and responses to nodes in
            the DAX cluster.

            - **Address** *(string) --*

              The DNS hostname of the endpoint.

            - **Port** *(integer) --*

              The port number that applications should use to connect to the endpoint.

          - **NodeCreateTime** *(datetime) --*

            The date and time (in UNIX epoch format) when the node was launched.

          - **AvailabilityZone** *(string) --*

            The Availability Zone (AZ) in which the node has been deployed.

          - **NodeStatus** *(string) --*

            The current status of the node. For example: ``available`` .

          - **ParameterGroupStatus** *(string) --*

            The status of the parameter group associated with this node. For example, ``in-sync`` .

      - **PreferredMaintenanceWindow** *(string) --*

        A range of time when maintenance of DAX cluster software will be performed. For example:
        ``sun:01:00-sun:09:00`` . Cluster maintenance normally takes less than 30 minutes, and is
        performed automatically within the maintenance window.

      - **NotificationConfiguration** *(dict) --*

        Describes a notification topic and its status. Notification topics are used for publishing
        DAX events to subscribers using Amazon Simple Notification Service (SNS).

        - **TopicArn** *(string) --*

          The Amazon Resource Name (ARN) that identifies the topic.

        - **TopicStatus** *(string) --*

          The current state of the topic.

      - **SubnetGroup** *(string) --*

        The subnet group where the DAX cluster is running.

      - **SecurityGroups** *(list) --*

        A list of security groups, and the status of each, for the nodes in the cluster.

        - *(dict) --*

          An individual VPC security group and its status.

          - **SecurityGroupIdentifier** *(string) --*

            The unique ID for this security group.

          - **Status** *(string) --*

            The status of this security group.

      - **IamRoleArn** *(string) --*

        A valid Amazon Resource Name (ARN) that identifies an IAM role. At runtime, DAX will assume
        this role and use the role's permissions to access DynamoDB on your behalf.

      - **ParameterGroup** *(dict) --*

        The parameter group being used by nodes in the cluster.

        - **ParameterGroupName** *(string) --*

          The name of the parameter group.

        - **ParameterApplyStatus** *(string) --*

          The status of parameter updates.

        - **NodeIdsToReboot** *(list) --*

          The node IDs of one or more nodes to be rebooted.

          - *(string) --*

      - **SSEDescription** *(dict) --*

        The description of the server-side encryption status on the specified DAX cluster.

        - **Status** *(string) --*

          The current state of server-side encryption:

          * ``ENABLING`` - Server-side encryption is being enabled.

          * ``ENABLED`` - Server-side encryption is enabled.

          * ``DISABLING`` - Server-side encryption is being disabled.

          * ``DISABLED`` - Server-side encryption is disabled.
    """


_ClientDeleteClusterResponseClusterClusterDiscoveryEndpointTypeDef = TypedDict(
    "_ClientDeleteClusterResponseClusterClusterDiscoveryEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientDeleteClusterResponseClusterClusterDiscoveryEndpointTypeDef(
    _ClientDeleteClusterResponseClusterClusterDiscoveryEndpointTypeDef
):
    """
    Type definition for `ClientDeleteClusterResponseCluster` `ClusterDiscoveryEndpoint`

    The configuration endpoint for this DAX cluster, consisting of a DNS name and a port
    number. Client applications can specify this endpoint, rather than an individual node
    endpoint, and allow the DAX client software to intelligently route requests and responses
    to nodes in the DAX cluster.

    - **Address** *(string) --*

      The DNS hostname of the endpoint.

    - **Port** *(integer) --*

      The port number that applications should use to connect to the endpoint.
    """


_ClientDeleteClusterResponseClusterNodesEndpointTypeDef = TypedDict(
    "_ClientDeleteClusterResponseClusterNodesEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientDeleteClusterResponseClusterNodesEndpointTypeDef(
    _ClientDeleteClusterResponseClusterNodesEndpointTypeDef
):
    """
    Type definition for `ClientDeleteClusterResponseClusterNodes` `Endpoint`

    The endpoint for the node, consisting of a DNS name and a port number. Client
    applications can connect directly to a node endpoint, if desired (as an alternative to
    allowing DAX client software to intelligently route requests and responses to nodes in
    the DAX cluster.

    - **Address** *(string) --*

      The DNS hostname of the endpoint.

    - **Port** *(integer) --*

      The port number that applications should use to connect to the endpoint.
    """


_ClientDeleteClusterResponseClusterNodesTypeDef = TypedDict(
    "_ClientDeleteClusterResponseClusterNodesTypeDef",
    {
        "NodeId": str,
        "Endpoint": ClientDeleteClusterResponseClusterNodesEndpointTypeDef,
        "NodeCreateTime": datetime,
        "AvailabilityZone": str,
        "NodeStatus": str,
        "ParameterGroupStatus": str,
    },
    total=False,
)


class ClientDeleteClusterResponseClusterNodesTypeDef(
    _ClientDeleteClusterResponseClusterNodesTypeDef
):
    """
    Type definition for `ClientDeleteClusterResponseCluster` `Nodes`

    Represents an individual node within a DAX cluster.

    - **NodeId** *(string) --*

      A system-generated identifier for the node.

    - **Endpoint** *(dict) --*

      The endpoint for the node, consisting of a DNS name and a port number. Client
      applications can connect directly to a node endpoint, if desired (as an alternative to
      allowing DAX client software to intelligently route requests and responses to nodes in
      the DAX cluster.

      - **Address** *(string) --*

        The DNS hostname of the endpoint.

      - **Port** *(integer) --*

        The port number that applications should use to connect to the endpoint.

    - **NodeCreateTime** *(datetime) --*

      The date and time (in UNIX epoch format) when the node was launched.

    - **AvailabilityZone** *(string) --*

      The Availability Zone (AZ) in which the node has been deployed.

    - **NodeStatus** *(string) --*

      The current status of the node. For example: ``available`` .

    - **ParameterGroupStatus** *(string) --*

      The status of the parameter group associated with this node. For example, ``in-sync`` .
    """


_ClientDeleteClusterResponseClusterNotificationConfigurationTypeDef = TypedDict(
    "_ClientDeleteClusterResponseClusterNotificationConfigurationTypeDef",
    {"TopicArn": str, "TopicStatus": str},
    total=False,
)


class ClientDeleteClusterResponseClusterNotificationConfigurationTypeDef(
    _ClientDeleteClusterResponseClusterNotificationConfigurationTypeDef
):
    """
    Type definition for `ClientDeleteClusterResponseCluster` `NotificationConfiguration`

    Describes a notification topic and its status. Notification topics are used for publishing
    DAX events to subscribers using Amazon Simple Notification Service (SNS).

    - **TopicArn** *(string) --*

      The Amazon Resource Name (ARN) that identifies the topic.

    - **TopicStatus** *(string) --*

      The current state of the topic.
    """


_ClientDeleteClusterResponseClusterParameterGroupTypeDef = TypedDict(
    "_ClientDeleteClusterResponseClusterParameterGroupTypeDef",
    {
        "ParameterGroupName": str,
        "ParameterApplyStatus": str,
        "NodeIdsToReboot": List[str],
    },
    total=False,
)


class ClientDeleteClusterResponseClusterParameterGroupTypeDef(
    _ClientDeleteClusterResponseClusterParameterGroupTypeDef
):
    """
    Type definition for `ClientDeleteClusterResponseCluster` `ParameterGroup`

    The parameter group being used by nodes in the cluster.

    - **ParameterGroupName** *(string) --*

      The name of the parameter group.

    - **ParameterApplyStatus** *(string) --*

      The status of parameter updates.

    - **NodeIdsToReboot** *(list) --*

      The node IDs of one or more nodes to be rebooted.

      - *(string) --*
    """


_ClientDeleteClusterResponseClusterSSEDescriptionTypeDef = TypedDict(
    "_ClientDeleteClusterResponseClusterSSEDescriptionTypeDef",
    {"Status": str},
    total=False,
)


class ClientDeleteClusterResponseClusterSSEDescriptionTypeDef(
    _ClientDeleteClusterResponseClusterSSEDescriptionTypeDef
):
    """
    Type definition for `ClientDeleteClusterResponseCluster` `SSEDescription`

    The description of the server-side encryption status on the specified DAX cluster.

    - **Status** *(string) --*

      The current state of server-side encryption:

      * ``ENABLING`` - Server-side encryption is being enabled.

      * ``ENABLED`` - Server-side encryption is enabled.

      * ``DISABLING`` - Server-side encryption is being disabled.

      * ``DISABLED`` - Server-side encryption is disabled.
    """


_ClientDeleteClusterResponseClusterSecurityGroupsTypeDef = TypedDict(
    "_ClientDeleteClusterResponseClusterSecurityGroupsTypeDef",
    {"SecurityGroupIdentifier": str, "Status": str},
    total=False,
)


class ClientDeleteClusterResponseClusterSecurityGroupsTypeDef(
    _ClientDeleteClusterResponseClusterSecurityGroupsTypeDef
):
    """
    Type definition for `ClientDeleteClusterResponseCluster` `SecurityGroups`

    An individual VPC security group and its status.

    - **SecurityGroupIdentifier** *(string) --*

      The unique ID for this security group.

    - **Status** *(string) --*

      The status of this security group.
    """


_ClientDeleteClusterResponseClusterTypeDef = TypedDict(
    "_ClientDeleteClusterResponseClusterTypeDef",
    {
        "ClusterName": str,
        "Description": str,
        "ClusterArn": str,
        "TotalNodes": int,
        "ActiveNodes": int,
        "NodeType": str,
        "Status": str,
        "ClusterDiscoveryEndpoint": ClientDeleteClusterResponseClusterClusterDiscoveryEndpointTypeDef,
        "NodeIdsToRemove": List[str],
        "Nodes": List[ClientDeleteClusterResponseClusterNodesTypeDef],
        "PreferredMaintenanceWindow": str,
        "NotificationConfiguration": ClientDeleteClusterResponseClusterNotificationConfigurationTypeDef,
        "SubnetGroup": str,
        "SecurityGroups": List[ClientDeleteClusterResponseClusterSecurityGroupsTypeDef],
        "IamRoleArn": str,
        "ParameterGroup": ClientDeleteClusterResponseClusterParameterGroupTypeDef,
        "SSEDescription": ClientDeleteClusterResponseClusterSSEDescriptionTypeDef,
    },
    total=False,
)


class ClientDeleteClusterResponseClusterTypeDef(
    _ClientDeleteClusterResponseClusterTypeDef
):
    """
    Type definition for `ClientDeleteClusterResponse` `Cluster`

    A description of the DAX cluster that is being deleted.

    - **ClusterName** *(string) --*

      The name of the DAX cluster.

    - **Description** *(string) --*

      The description of the cluster.

    - **ClusterArn** *(string) --*

      The Amazon Resource Name (ARN) that uniquely identifies the cluster.

    - **TotalNodes** *(integer) --*

      The total number of nodes in the cluster.

    - **ActiveNodes** *(integer) --*

      The number of nodes in the cluster that are active (i.e., capable of serving requests).

    - **NodeType** *(string) --*

      The node type for the nodes in the cluster. (All nodes in a DAX cluster are of the same
      type.)

    - **Status** *(string) --*

      The current status of the cluster.

    - **ClusterDiscoveryEndpoint** *(dict) --*

      The configuration endpoint for this DAX cluster, consisting of a DNS name and a port
      number. Client applications can specify this endpoint, rather than an individual node
      endpoint, and allow the DAX client software to intelligently route requests and responses
      to nodes in the DAX cluster.

      - **Address** *(string) --*

        The DNS hostname of the endpoint.

      - **Port** *(integer) --*

        The port number that applications should use to connect to the endpoint.

    - **NodeIdsToRemove** *(list) --*

      A list of nodes to be removed from the cluster.

      - *(string) --*

    - **Nodes** *(list) --*

      A list of nodes that are currently in the cluster.

      - *(dict) --*

        Represents an individual node within a DAX cluster.

        - **NodeId** *(string) --*

          A system-generated identifier for the node.

        - **Endpoint** *(dict) --*

          The endpoint for the node, consisting of a DNS name and a port number. Client
          applications can connect directly to a node endpoint, if desired (as an alternative to
          allowing DAX client software to intelligently route requests and responses to nodes in
          the DAX cluster.

          - **Address** *(string) --*

            The DNS hostname of the endpoint.

          - **Port** *(integer) --*

            The port number that applications should use to connect to the endpoint.

        - **NodeCreateTime** *(datetime) --*

          The date and time (in UNIX epoch format) when the node was launched.

        - **AvailabilityZone** *(string) --*

          The Availability Zone (AZ) in which the node has been deployed.

        - **NodeStatus** *(string) --*

          The current status of the node. For example: ``available`` .

        - **ParameterGroupStatus** *(string) --*

          The status of the parameter group associated with this node. For example, ``in-sync`` .

    - **PreferredMaintenanceWindow** *(string) --*

      A range of time when maintenance of DAX cluster software will be performed. For example:
      ``sun:01:00-sun:09:00`` . Cluster maintenance normally takes less than 30 minutes, and is
      performed automatically within the maintenance window.

    - **NotificationConfiguration** *(dict) --*

      Describes a notification topic and its status. Notification topics are used for publishing
      DAX events to subscribers using Amazon Simple Notification Service (SNS).

      - **TopicArn** *(string) --*

        The Amazon Resource Name (ARN) that identifies the topic.

      - **TopicStatus** *(string) --*

        The current state of the topic.

    - **SubnetGroup** *(string) --*

      The subnet group where the DAX cluster is running.

    - **SecurityGroups** *(list) --*

      A list of security groups, and the status of each, for the nodes in the cluster.

      - *(dict) --*

        An individual VPC security group and its status.

        - **SecurityGroupIdentifier** *(string) --*

          The unique ID for this security group.

        - **Status** *(string) --*

          The status of this security group.

    - **IamRoleArn** *(string) --*

      A valid Amazon Resource Name (ARN) that identifies an IAM role. At runtime, DAX will assume
      this role and use the role's permissions to access DynamoDB on your behalf.

    - **ParameterGroup** *(dict) --*

      The parameter group being used by nodes in the cluster.

      - **ParameterGroupName** *(string) --*

        The name of the parameter group.

      - **ParameterApplyStatus** *(string) --*

        The status of parameter updates.

      - **NodeIdsToReboot** *(list) --*

        The node IDs of one or more nodes to be rebooted.

        - *(string) --*

    - **SSEDescription** *(dict) --*

      The description of the server-side encryption status on the specified DAX cluster.

      - **Status** *(string) --*

        The current state of server-side encryption:

        * ``ENABLING`` - Server-side encryption is being enabled.

        * ``ENABLED`` - Server-side encryption is enabled.

        * ``DISABLING`` - Server-side encryption is being disabled.

        * ``DISABLED`` - Server-side encryption is disabled.
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

      A description of the DAX cluster that is being deleted.

      - **ClusterName** *(string) --*

        The name of the DAX cluster.

      - **Description** *(string) --*

        The description of the cluster.

      - **ClusterArn** *(string) --*

        The Amazon Resource Name (ARN) that uniquely identifies the cluster.

      - **TotalNodes** *(integer) --*

        The total number of nodes in the cluster.

      - **ActiveNodes** *(integer) --*

        The number of nodes in the cluster that are active (i.e., capable of serving requests).

      - **NodeType** *(string) --*

        The node type for the nodes in the cluster. (All nodes in a DAX cluster are of the same
        type.)

      - **Status** *(string) --*

        The current status of the cluster.

      - **ClusterDiscoveryEndpoint** *(dict) --*

        The configuration endpoint for this DAX cluster, consisting of a DNS name and a port
        number. Client applications can specify this endpoint, rather than an individual node
        endpoint, and allow the DAX client software to intelligently route requests and responses
        to nodes in the DAX cluster.

        - **Address** *(string) --*

          The DNS hostname of the endpoint.

        - **Port** *(integer) --*

          The port number that applications should use to connect to the endpoint.

      - **NodeIdsToRemove** *(list) --*

        A list of nodes to be removed from the cluster.

        - *(string) --*

      - **Nodes** *(list) --*

        A list of nodes that are currently in the cluster.

        - *(dict) --*

          Represents an individual node within a DAX cluster.

          - **NodeId** *(string) --*

            A system-generated identifier for the node.

          - **Endpoint** *(dict) --*

            The endpoint for the node, consisting of a DNS name and a port number. Client
            applications can connect directly to a node endpoint, if desired (as an alternative to
            allowing DAX client software to intelligently route requests and responses to nodes in
            the DAX cluster.

            - **Address** *(string) --*

              The DNS hostname of the endpoint.

            - **Port** *(integer) --*

              The port number that applications should use to connect to the endpoint.

          - **NodeCreateTime** *(datetime) --*

            The date and time (in UNIX epoch format) when the node was launched.

          - **AvailabilityZone** *(string) --*

            The Availability Zone (AZ) in which the node has been deployed.

          - **NodeStatus** *(string) --*

            The current status of the node. For example: ``available`` .

          - **ParameterGroupStatus** *(string) --*

            The status of the parameter group associated with this node. For example, ``in-sync`` .

      - **PreferredMaintenanceWindow** *(string) --*

        A range of time when maintenance of DAX cluster software will be performed. For example:
        ``sun:01:00-sun:09:00`` . Cluster maintenance normally takes less than 30 minutes, and is
        performed automatically within the maintenance window.

      - **NotificationConfiguration** *(dict) --*

        Describes a notification topic and its status. Notification topics are used for publishing
        DAX events to subscribers using Amazon Simple Notification Service (SNS).

        - **TopicArn** *(string) --*

          The Amazon Resource Name (ARN) that identifies the topic.

        - **TopicStatus** *(string) --*

          The current state of the topic.

      - **SubnetGroup** *(string) --*

        The subnet group where the DAX cluster is running.

      - **SecurityGroups** *(list) --*

        A list of security groups, and the status of each, for the nodes in the cluster.

        - *(dict) --*

          An individual VPC security group and its status.

          - **SecurityGroupIdentifier** *(string) --*

            The unique ID for this security group.

          - **Status** *(string) --*

            The status of this security group.

      - **IamRoleArn** *(string) --*

        A valid Amazon Resource Name (ARN) that identifies an IAM role. At runtime, DAX will assume
        this role and use the role's permissions to access DynamoDB on your behalf.

      - **ParameterGroup** *(dict) --*

        The parameter group being used by nodes in the cluster.

        - **ParameterGroupName** *(string) --*

          The name of the parameter group.

        - **ParameterApplyStatus** *(string) --*

          The status of parameter updates.

        - **NodeIdsToReboot** *(list) --*

          The node IDs of one or more nodes to be rebooted.

          - *(string) --*

      - **SSEDescription** *(dict) --*

        The description of the server-side encryption status on the specified DAX cluster.

        - **Status** *(string) --*

          The current state of server-side encryption:

          * ``ENABLING`` - Server-side encryption is being enabled.

          * ``ENABLED`` - Server-side encryption is enabled.

          * ``DISABLING`` - Server-side encryption is being disabled.

          * ``DISABLED`` - Server-side encryption is disabled.
    """


_ClientDeleteParameterGroupResponseTypeDef = TypedDict(
    "_ClientDeleteParameterGroupResponseTypeDef", {"DeletionMessage": str}, total=False
)


class ClientDeleteParameterGroupResponseTypeDef(
    _ClientDeleteParameterGroupResponseTypeDef
):
    """
    Type definition for `ClientDeleteParameterGroup` `Response`

    - **DeletionMessage** *(string) --*

      A user-specified message for this action (i.e., a reason for deleting the parameter group).
    """


_ClientDeleteSubnetGroupResponseTypeDef = TypedDict(
    "_ClientDeleteSubnetGroupResponseTypeDef", {"DeletionMessage": str}, total=False
)


class ClientDeleteSubnetGroupResponseTypeDef(_ClientDeleteSubnetGroupResponseTypeDef):
    """
    Type definition for `ClientDeleteSubnetGroup` `Response`

    - **DeletionMessage** *(string) --*

      A user-specified message for this action (i.e., a reason for deleting the subnet group).
    """


_ClientDescribeClustersResponseClustersClusterDiscoveryEndpointTypeDef = TypedDict(
    "_ClientDescribeClustersResponseClustersClusterDiscoveryEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientDescribeClustersResponseClustersClusterDiscoveryEndpointTypeDef(
    _ClientDescribeClustersResponseClustersClusterDiscoveryEndpointTypeDef
):
    """
    Type definition for `ClientDescribeClustersResponseClusters` `ClusterDiscoveryEndpoint`

    The configuration endpoint for this DAX cluster, consisting of a DNS name and a port
    number. Client applications can specify this endpoint, rather than an individual node
    endpoint, and allow the DAX client software to intelligently route requests and responses
    to nodes in the DAX cluster.

    - **Address** *(string) --*

      The DNS hostname of the endpoint.

    - **Port** *(integer) --*

      The port number that applications should use to connect to the endpoint.
    """


_ClientDescribeClustersResponseClustersNodesEndpointTypeDef = TypedDict(
    "_ClientDescribeClustersResponseClustersNodesEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientDescribeClustersResponseClustersNodesEndpointTypeDef(
    _ClientDescribeClustersResponseClustersNodesEndpointTypeDef
):
    """
    Type definition for `ClientDescribeClustersResponseClustersNodes` `Endpoint`

    The endpoint for the node, consisting of a DNS name and a port number. Client
    applications can connect directly to a node endpoint, if desired (as an alternative
    to allowing DAX client software to intelligently route requests and responses to
    nodes in the DAX cluster.

    - **Address** *(string) --*

      The DNS hostname of the endpoint.

    - **Port** *(integer) --*

      The port number that applications should use to connect to the endpoint.
    """


_ClientDescribeClustersResponseClustersNodesTypeDef = TypedDict(
    "_ClientDescribeClustersResponseClustersNodesTypeDef",
    {
        "NodeId": str,
        "Endpoint": ClientDescribeClustersResponseClustersNodesEndpointTypeDef,
        "NodeCreateTime": datetime,
        "AvailabilityZone": str,
        "NodeStatus": str,
        "ParameterGroupStatus": str,
    },
    total=False,
)


class ClientDescribeClustersResponseClustersNodesTypeDef(
    _ClientDescribeClustersResponseClustersNodesTypeDef
):
    """
    Type definition for `ClientDescribeClustersResponseClusters` `Nodes`

    Represents an individual node within a DAX cluster.

    - **NodeId** *(string) --*

      A system-generated identifier for the node.

    - **Endpoint** *(dict) --*

      The endpoint for the node, consisting of a DNS name and a port number. Client
      applications can connect directly to a node endpoint, if desired (as an alternative
      to allowing DAX client software to intelligently route requests and responses to
      nodes in the DAX cluster.

      - **Address** *(string) --*

        The DNS hostname of the endpoint.

      - **Port** *(integer) --*

        The port number that applications should use to connect to the endpoint.

    - **NodeCreateTime** *(datetime) --*

      The date and time (in UNIX epoch format) when the node was launched.

    - **AvailabilityZone** *(string) --*

      The Availability Zone (AZ) in which the node has been deployed.

    - **NodeStatus** *(string) --*

      The current status of the node. For example: ``available`` .

    - **ParameterGroupStatus** *(string) --*

      The status of the parameter group associated with this node. For example, ``in-sync``
      .
    """


_ClientDescribeClustersResponseClustersNotificationConfigurationTypeDef = TypedDict(
    "_ClientDescribeClustersResponseClustersNotificationConfigurationTypeDef",
    {"TopicArn": str, "TopicStatus": str},
    total=False,
)


class ClientDescribeClustersResponseClustersNotificationConfigurationTypeDef(
    _ClientDescribeClustersResponseClustersNotificationConfigurationTypeDef
):
    """
    Type definition for `ClientDescribeClustersResponseClusters` `NotificationConfiguration`

    Describes a notification topic and its status. Notification topics are used for
    publishing DAX events to subscribers using Amazon Simple Notification Service (SNS).

    - **TopicArn** *(string) --*

      The Amazon Resource Name (ARN) that identifies the topic.

    - **TopicStatus** *(string) --*

      The current state of the topic.
    """


_ClientDescribeClustersResponseClustersParameterGroupTypeDef = TypedDict(
    "_ClientDescribeClustersResponseClustersParameterGroupTypeDef",
    {
        "ParameterGroupName": str,
        "ParameterApplyStatus": str,
        "NodeIdsToReboot": List[str],
    },
    total=False,
)


class ClientDescribeClustersResponseClustersParameterGroupTypeDef(
    _ClientDescribeClustersResponseClustersParameterGroupTypeDef
):
    """
    Type definition for `ClientDescribeClustersResponseClusters` `ParameterGroup`

    The parameter group being used by nodes in the cluster.

    - **ParameterGroupName** *(string) --*

      The name of the parameter group.

    - **ParameterApplyStatus** *(string) --*

      The status of parameter updates.

    - **NodeIdsToReboot** *(list) --*

      The node IDs of one or more nodes to be rebooted.

      - *(string) --*
    """


_ClientDescribeClustersResponseClustersSSEDescriptionTypeDef = TypedDict(
    "_ClientDescribeClustersResponseClustersSSEDescriptionTypeDef",
    {"Status": str},
    total=False,
)


class ClientDescribeClustersResponseClustersSSEDescriptionTypeDef(
    _ClientDescribeClustersResponseClustersSSEDescriptionTypeDef
):
    """
    Type definition for `ClientDescribeClustersResponseClusters` `SSEDescription`

    The description of the server-side encryption status on the specified DAX cluster.

    - **Status** *(string) --*

      The current state of server-side encryption:

      * ``ENABLING`` - Server-side encryption is being enabled.

      * ``ENABLED`` - Server-side encryption is enabled.

      * ``DISABLING`` - Server-side encryption is being disabled.

      * ``DISABLED`` - Server-side encryption is disabled.
    """


_ClientDescribeClustersResponseClustersSecurityGroupsTypeDef = TypedDict(
    "_ClientDescribeClustersResponseClustersSecurityGroupsTypeDef",
    {"SecurityGroupIdentifier": str, "Status": str},
    total=False,
)


class ClientDescribeClustersResponseClustersSecurityGroupsTypeDef(
    _ClientDescribeClustersResponseClustersSecurityGroupsTypeDef
):
    """
    Type definition for `ClientDescribeClustersResponseClusters` `SecurityGroups`

    An individual VPC security group and its status.

    - **SecurityGroupIdentifier** *(string) --*

      The unique ID for this security group.

    - **Status** *(string) --*

      The status of this security group.
    """


_ClientDescribeClustersResponseClustersTypeDef = TypedDict(
    "_ClientDescribeClustersResponseClustersTypeDef",
    {
        "ClusterName": str,
        "Description": str,
        "ClusterArn": str,
        "TotalNodes": int,
        "ActiveNodes": int,
        "NodeType": str,
        "Status": str,
        "ClusterDiscoveryEndpoint": ClientDescribeClustersResponseClustersClusterDiscoveryEndpointTypeDef,
        "NodeIdsToRemove": List[str],
        "Nodes": List[ClientDescribeClustersResponseClustersNodesTypeDef],
        "PreferredMaintenanceWindow": str,
        "NotificationConfiguration": ClientDescribeClustersResponseClustersNotificationConfigurationTypeDef,
        "SubnetGroup": str,
        "SecurityGroups": List[
            ClientDescribeClustersResponseClustersSecurityGroupsTypeDef
        ],
        "IamRoleArn": str,
        "ParameterGroup": ClientDescribeClustersResponseClustersParameterGroupTypeDef,
        "SSEDescription": ClientDescribeClustersResponseClustersSSEDescriptionTypeDef,
    },
    total=False,
)


class ClientDescribeClustersResponseClustersTypeDef(
    _ClientDescribeClustersResponseClustersTypeDef
):
    """
    Type definition for `ClientDescribeClustersResponse` `Clusters`

    Contains all of the attributes of a specific DAX cluster.

    - **ClusterName** *(string) --*

      The name of the DAX cluster.

    - **Description** *(string) --*

      The description of the cluster.

    - **ClusterArn** *(string) --*

      The Amazon Resource Name (ARN) that uniquely identifies the cluster.

    - **TotalNodes** *(integer) --*

      The total number of nodes in the cluster.

    - **ActiveNodes** *(integer) --*

      The number of nodes in the cluster that are active (i.e., capable of serving requests).

    - **NodeType** *(string) --*

      The node type for the nodes in the cluster. (All nodes in a DAX cluster are of the same
      type.)

    - **Status** *(string) --*

      The current status of the cluster.

    - **ClusterDiscoveryEndpoint** *(dict) --*

      The configuration endpoint for this DAX cluster, consisting of a DNS name and a port
      number. Client applications can specify this endpoint, rather than an individual node
      endpoint, and allow the DAX client software to intelligently route requests and responses
      to nodes in the DAX cluster.

      - **Address** *(string) --*

        The DNS hostname of the endpoint.

      - **Port** *(integer) --*

        The port number that applications should use to connect to the endpoint.

    - **NodeIdsToRemove** *(list) --*

      A list of nodes to be removed from the cluster.

      - *(string) --*

    - **Nodes** *(list) --*

      A list of nodes that are currently in the cluster.

      - *(dict) --*

        Represents an individual node within a DAX cluster.

        - **NodeId** *(string) --*

          A system-generated identifier for the node.

        - **Endpoint** *(dict) --*

          The endpoint for the node, consisting of a DNS name and a port number. Client
          applications can connect directly to a node endpoint, if desired (as an alternative
          to allowing DAX client software to intelligently route requests and responses to
          nodes in the DAX cluster.

          - **Address** *(string) --*

            The DNS hostname of the endpoint.

          - **Port** *(integer) --*

            The port number that applications should use to connect to the endpoint.

        - **NodeCreateTime** *(datetime) --*

          The date and time (in UNIX epoch format) when the node was launched.

        - **AvailabilityZone** *(string) --*

          The Availability Zone (AZ) in which the node has been deployed.

        - **NodeStatus** *(string) --*

          The current status of the node. For example: ``available`` .

        - **ParameterGroupStatus** *(string) --*

          The status of the parameter group associated with this node. For example, ``in-sync``
          .

    - **PreferredMaintenanceWindow** *(string) --*

      A range of time when maintenance of DAX cluster software will be performed. For example:
      ``sun:01:00-sun:09:00`` . Cluster maintenance normally takes less than 30 minutes, and is
      performed automatically within the maintenance window.

    - **NotificationConfiguration** *(dict) --*

      Describes a notification topic and its status. Notification topics are used for
      publishing DAX events to subscribers using Amazon Simple Notification Service (SNS).

      - **TopicArn** *(string) --*

        The Amazon Resource Name (ARN) that identifies the topic.

      - **TopicStatus** *(string) --*

        The current state of the topic.

    - **SubnetGroup** *(string) --*

      The subnet group where the DAX cluster is running.

    - **SecurityGroups** *(list) --*

      A list of security groups, and the status of each, for the nodes in the cluster.

      - *(dict) --*

        An individual VPC security group and its status.

        - **SecurityGroupIdentifier** *(string) --*

          The unique ID for this security group.

        - **Status** *(string) --*

          The status of this security group.

    - **IamRoleArn** *(string) --*

      A valid Amazon Resource Name (ARN) that identifies an IAM role. At runtime, DAX will
      assume this role and use the role's permissions to access DynamoDB on your behalf.

    - **ParameterGroup** *(dict) --*

      The parameter group being used by nodes in the cluster.

      - **ParameterGroupName** *(string) --*

        The name of the parameter group.

      - **ParameterApplyStatus** *(string) --*

        The status of parameter updates.

      - **NodeIdsToReboot** *(list) --*

        The node IDs of one or more nodes to be rebooted.

        - *(string) --*

    - **SSEDescription** *(dict) --*

      The description of the server-side encryption status on the specified DAX cluster.

      - **Status** *(string) --*

        The current state of server-side encryption:

        * ``ENABLING`` - Server-side encryption is being enabled.

        * ``ENABLED`` - Server-side encryption is enabled.

        * ``DISABLING`` - Server-side encryption is being disabled.

        * ``DISABLED`` - Server-side encryption is disabled.
    """


_ClientDescribeClustersResponseTypeDef = TypedDict(
    "_ClientDescribeClustersResponseTypeDef",
    {"NextToken": str, "Clusters": List[ClientDescribeClustersResponseClustersTypeDef]},
    total=False,
)


class ClientDescribeClustersResponseTypeDef(_ClientDescribeClustersResponseTypeDef):
    """
    Type definition for `ClientDescribeClusters` `Response`

    - **NextToken** *(string) --*

      Provides an identifier to allow retrieval of paginated results.

    - **Clusters** *(list) --*

      The descriptions of your DAX clusters, in response to a *DescribeClusters* request.

      - *(dict) --*

        Contains all of the attributes of a specific DAX cluster.

        - **ClusterName** *(string) --*

          The name of the DAX cluster.

        - **Description** *(string) --*

          The description of the cluster.

        - **ClusterArn** *(string) --*

          The Amazon Resource Name (ARN) that uniquely identifies the cluster.

        - **TotalNodes** *(integer) --*

          The total number of nodes in the cluster.

        - **ActiveNodes** *(integer) --*

          The number of nodes in the cluster that are active (i.e., capable of serving requests).

        - **NodeType** *(string) --*

          The node type for the nodes in the cluster. (All nodes in a DAX cluster are of the same
          type.)

        - **Status** *(string) --*

          The current status of the cluster.

        - **ClusterDiscoveryEndpoint** *(dict) --*

          The configuration endpoint for this DAX cluster, consisting of a DNS name and a port
          number. Client applications can specify this endpoint, rather than an individual node
          endpoint, and allow the DAX client software to intelligently route requests and responses
          to nodes in the DAX cluster.

          - **Address** *(string) --*

            The DNS hostname of the endpoint.

          - **Port** *(integer) --*

            The port number that applications should use to connect to the endpoint.

        - **NodeIdsToRemove** *(list) --*

          A list of nodes to be removed from the cluster.

          - *(string) --*

        - **Nodes** *(list) --*

          A list of nodes that are currently in the cluster.

          - *(dict) --*

            Represents an individual node within a DAX cluster.

            - **NodeId** *(string) --*

              A system-generated identifier for the node.

            - **Endpoint** *(dict) --*

              The endpoint for the node, consisting of a DNS name and a port number. Client
              applications can connect directly to a node endpoint, if desired (as an alternative
              to allowing DAX client software to intelligently route requests and responses to
              nodes in the DAX cluster.

              - **Address** *(string) --*

                The DNS hostname of the endpoint.

              - **Port** *(integer) --*

                The port number that applications should use to connect to the endpoint.

            - **NodeCreateTime** *(datetime) --*

              The date and time (in UNIX epoch format) when the node was launched.

            - **AvailabilityZone** *(string) --*

              The Availability Zone (AZ) in which the node has been deployed.

            - **NodeStatus** *(string) --*

              The current status of the node. For example: ``available`` .

            - **ParameterGroupStatus** *(string) --*

              The status of the parameter group associated with this node. For example, ``in-sync``
              .

        - **PreferredMaintenanceWindow** *(string) --*

          A range of time when maintenance of DAX cluster software will be performed. For example:
          ``sun:01:00-sun:09:00`` . Cluster maintenance normally takes less than 30 minutes, and is
          performed automatically within the maintenance window.

        - **NotificationConfiguration** *(dict) --*

          Describes a notification topic and its status. Notification topics are used for
          publishing DAX events to subscribers using Amazon Simple Notification Service (SNS).

          - **TopicArn** *(string) --*

            The Amazon Resource Name (ARN) that identifies the topic.

          - **TopicStatus** *(string) --*

            The current state of the topic.

        - **SubnetGroup** *(string) --*

          The subnet group where the DAX cluster is running.

        - **SecurityGroups** *(list) --*

          A list of security groups, and the status of each, for the nodes in the cluster.

          - *(dict) --*

            An individual VPC security group and its status.

            - **SecurityGroupIdentifier** *(string) --*

              The unique ID for this security group.

            - **Status** *(string) --*

              The status of this security group.

        - **IamRoleArn** *(string) --*

          A valid Amazon Resource Name (ARN) that identifies an IAM role. At runtime, DAX will
          assume this role and use the role's permissions to access DynamoDB on your behalf.

        - **ParameterGroup** *(dict) --*

          The parameter group being used by nodes in the cluster.

          - **ParameterGroupName** *(string) --*

            The name of the parameter group.

          - **ParameterApplyStatus** *(string) --*

            The status of parameter updates.

          - **NodeIdsToReboot** *(list) --*

            The node IDs of one or more nodes to be rebooted.

            - *(string) --*

        - **SSEDescription** *(dict) --*

          The description of the server-side encryption status on the specified DAX cluster.

          - **Status** *(string) --*

            The current state of server-side encryption:

            * ``ENABLING`` - Server-side encryption is being enabled.

            * ``ENABLED`` - Server-side encryption is enabled.

            * ``DISABLING`` - Server-side encryption is being disabled.

            * ``DISABLED`` - Server-side encryption is disabled.
    """


_ClientDescribeDefaultParametersResponseParametersNodeTypeSpecificValuesTypeDef = TypedDict(
    "_ClientDescribeDefaultParametersResponseParametersNodeTypeSpecificValuesTypeDef",
    {"NodeType": str, "Value": str},
    total=False,
)


class ClientDescribeDefaultParametersResponseParametersNodeTypeSpecificValuesTypeDef(
    _ClientDescribeDefaultParametersResponseParametersNodeTypeSpecificValuesTypeDef
):
    """
    Type definition for `ClientDescribeDefaultParametersResponseParameters` `NodeTypeSpecificValues`

    Represents a parameter value that is applicable to a particular node type.

    - **NodeType** *(string) --*

      A node type to which the parameter value applies.

    - **Value** *(string) --*

      The parameter value for this node type.
    """


_ClientDescribeDefaultParametersResponseParametersTypeDef = TypedDict(
    "_ClientDescribeDefaultParametersResponseParametersTypeDef",
    {
        "ParameterName": str,
        "ParameterType": str,
        "ParameterValue": str,
        "NodeTypeSpecificValues": List[
            ClientDescribeDefaultParametersResponseParametersNodeTypeSpecificValuesTypeDef
        ],
        "Description": str,
        "Source": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": str,
        "ChangeType": str,
    },
    total=False,
)


class ClientDescribeDefaultParametersResponseParametersTypeDef(
    _ClientDescribeDefaultParametersResponseParametersTypeDef
):
    """
    Type definition for `ClientDescribeDefaultParametersResponse` `Parameters`

    Describes an individual setting that controls some aspect of DAX behavior.

    - **ParameterName** *(string) --*

      The name of the parameter.

    - **ParameterType** *(string) --*

      Determines whether the parameter can be applied to any nodes, or only nodes of a
      particular type.

    - **ParameterValue** *(string) --*

      The value for the parameter.

    - **NodeTypeSpecificValues** *(list) --*

      A list of node types, and specific parameter values for each node.

      - *(dict) --*

        Represents a parameter value that is applicable to a particular node type.

        - **NodeType** *(string) --*

          A node type to which the parameter value applies.

        - **Value** *(string) --*

          The parameter value for this node type.

    - **Description** *(string) --*

      A description of the parameter

    - **Source** *(string) --*

      How the parameter is defined. For example, ``system`` denotes a system-defined parameter.

    - **DataType** *(string) --*

      The data type of the parameter. For example, ``integer`` :

    - **AllowedValues** *(string) --*

      A range of values within which the parameter can be set.

    - **IsModifiable** *(string) --*

      Whether the customer is allowed to modify the parameter.

    - **ChangeType** *(string) --*

      The conditions under which changes to this parameter can be applied. For example,
      ``requires-reboot`` indicates that a new value for this parameter will only take effect
      if a node is rebooted.
    """


_ClientDescribeDefaultParametersResponseTypeDef = TypedDict(
    "_ClientDescribeDefaultParametersResponseTypeDef",
    {
        "NextToken": str,
        "Parameters": List[ClientDescribeDefaultParametersResponseParametersTypeDef],
    },
    total=False,
)


class ClientDescribeDefaultParametersResponseTypeDef(
    _ClientDescribeDefaultParametersResponseTypeDef
):
    """
    Type definition for `ClientDescribeDefaultParameters` `Response`

    - **NextToken** *(string) --*

      Provides an identifier to allow retrieval of paginated results.

    - **Parameters** *(list) --*

      A list of parameters. Each element in the list represents one parameter.

      - *(dict) --*

        Describes an individual setting that controls some aspect of DAX behavior.

        - **ParameterName** *(string) --*

          The name of the parameter.

        - **ParameterType** *(string) --*

          Determines whether the parameter can be applied to any nodes, or only nodes of a
          particular type.

        - **ParameterValue** *(string) --*

          The value for the parameter.

        - **NodeTypeSpecificValues** *(list) --*

          A list of node types, and specific parameter values for each node.

          - *(dict) --*

            Represents a parameter value that is applicable to a particular node type.

            - **NodeType** *(string) --*

              A node type to which the parameter value applies.

            - **Value** *(string) --*

              The parameter value for this node type.

        - **Description** *(string) --*

          A description of the parameter

        - **Source** *(string) --*

          How the parameter is defined. For example, ``system`` denotes a system-defined parameter.

        - **DataType** *(string) --*

          The data type of the parameter. For example, ``integer`` :

        - **AllowedValues** *(string) --*

          A range of values within which the parameter can be set.

        - **IsModifiable** *(string) --*

          Whether the customer is allowed to modify the parameter.

        - **ChangeType** *(string) --*

          The conditions under which changes to this parameter can be applied. For example,
          ``requires-reboot`` indicates that a new value for this parameter will only take effect
          if a node is rebooted.
    """


_ClientDescribeEventsResponseEventsTypeDef = TypedDict(
    "_ClientDescribeEventsResponseEventsTypeDef",
    {"SourceName": str, "SourceType": str, "Message": str, "Date": datetime},
    total=False,
)


class ClientDescribeEventsResponseEventsTypeDef(
    _ClientDescribeEventsResponseEventsTypeDef
):
    """
    Type definition for `ClientDescribeEventsResponse` `Events`

    Represents a single occurrence of something interesting within the system. Some examples of
    events are creating a DAX cluster, adding or removing a node, or rebooting a node.

    - **SourceName** *(string) --*

      The source of the event. For example, if the event occurred at the node level, the source
      would be the node ID.

    - **SourceType** *(string) --*

      Specifies the origin of this event - a cluster, a parameter group, a node ID, etc.

    - **Message** *(string) --*

      A user-defined message associated with the event.

    - **Date** *(datetime) --*

      The date and time when the event occurred.
    """


_ClientDescribeEventsResponseTypeDef = TypedDict(
    "_ClientDescribeEventsResponseTypeDef",
    {"NextToken": str, "Events": List[ClientDescribeEventsResponseEventsTypeDef]},
    total=False,
)


class ClientDescribeEventsResponseTypeDef(_ClientDescribeEventsResponseTypeDef):
    """
    Type definition for `ClientDescribeEvents` `Response`

    - **NextToken** *(string) --*

      Provides an identifier to allow retrieval of paginated results.

    - **Events** *(list) --*

      An array of events. Each element in the array represents one event.

      - *(dict) --*

        Represents a single occurrence of something interesting within the system. Some examples of
        events are creating a DAX cluster, adding or removing a node, or rebooting a node.

        - **SourceName** *(string) --*

          The source of the event. For example, if the event occurred at the node level, the source
          would be the node ID.

        - **SourceType** *(string) --*

          Specifies the origin of this event - a cluster, a parameter group, a node ID, etc.

        - **Message** *(string) --*

          A user-defined message associated with the event.

        - **Date** *(datetime) --*

          The date and time when the event occurred.
    """


_ClientDescribeParameterGroupsResponseParameterGroupsTypeDef = TypedDict(
    "_ClientDescribeParameterGroupsResponseParameterGroupsTypeDef",
    {"ParameterGroupName": str, "Description": str},
    total=False,
)


class ClientDescribeParameterGroupsResponseParameterGroupsTypeDef(
    _ClientDescribeParameterGroupsResponseParameterGroupsTypeDef
):
    """
    Type definition for `ClientDescribeParameterGroupsResponse` `ParameterGroups`

    A named set of parameters that are applied to all of the nodes in a DAX cluster.

    - **ParameterGroupName** *(string) --*

      The name of the parameter group.

    - **Description** *(string) --*

      A description of the parameter group.
    """


_ClientDescribeParameterGroupsResponseTypeDef = TypedDict(
    "_ClientDescribeParameterGroupsResponseTypeDef",
    {
        "NextToken": str,
        "ParameterGroups": List[
            ClientDescribeParameterGroupsResponseParameterGroupsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeParameterGroupsResponseTypeDef(
    _ClientDescribeParameterGroupsResponseTypeDef
):
    """
    Type definition for `ClientDescribeParameterGroups` `Response`

    - **NextToken** *(string) --*

      Provides an identifier to allow retrieval of paginated results.

    - **ParameterGroups** *(list) --*

      An array of parameter groups. Each element in the array represents one parameter group.

      - *(dict) --*

        A named set of parameters that are applied to all of the nodes in a DAX cluster.

        - **ParameterGroupName** *(string) --*

          The name of the parameter group.

        - **Description** *(string) --*

          A description of the parameter group.
    """


_ClientDescribeParametersResponseParametersNodeTypeSpecificValuesTypeDef = TypedDict(
    "_ClientDescribeParametersResponseParametersNodeTypeSpecificValuesTypeDef",
    {"NodeType": str, "Value": str},
    total=False,
)


class ClientDescribeParametersResponseParametersNodeTypeSpecificValuesTypeDef(
    _ClientDescribeParametersResponseParametersNodeTypeSpecificValuesTypeDef
):
    """
    Type definition for `ClientDescribeParametersResponseParameters` `NodeTypeSpecificValues`

    Represents a parameter value that is applicable to a particular node type.

    - **NodeType** *(string) --*

      A node type to which the parameter value applies.

    - **Value** *(string) --*

      The parameter value for this node type.
    """


_ClientDescribeParametersResponseParametersTypeDef = TypedDict(
    "_ClientDescribeParametersResponseParametersTypeDef",
    {
        "ParameterName": str,
        "ParameterType": str,
        "ParameterValue": str,
        "NodeTypeSpecificValues": List[
            ClientDescribeParametersResponseParametersNodeTypeSpecificValuesTypeDef
        ],
        "Description": str,
        "Source": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": str,
        "ChangeType": str,
    },
    total=False,
)


class ClientDescribeParametersResponseParametersTypeDef(
    _ClientDescribeParametersResponseParametersTypeDef
):
    """
    Type definition for `ClientDescribeParametersResponse` `Parameters`

    Describes an individual setting that controls some aspect of DAX behavior.

    - **ParameterName** *(string) --*

      The name of the parameter.

    - **ParameterType** *(string) --*

      Determines whether the parameter can be applied to any nodes, or only nodes of a
      particular type.

    - **ParameterValue** *(string) --*

      The value for the parameter.

    - **NodeTypeSpecificValues** *(list) --*

      A list of node types, and specific parameter values for each node.

      - *(dict) --*

        Represents a parameter value that is applicable to a particular node type.

        - **NodeType** *(string) --*

          A node type to which the parameter value applies.

        - **Value** *(string) --*

          The parameter value for this node type.

    - **Description** *(string) --*

      A description of the parameter

    - **Source** *(string) --*

      How the parameter is defined. For example, ``system`` denotes a system-defined parameter.

    - **DataType** *(string) --*

      The data type of the parameter. For example, ``integer`` :

    - **AllowedValues** *(string) --*

      A range of values within which the parameter can be set.

    - **IsModifiable** *(string) --*

      Whether the customer is allowed to modify the parameter.

    - **ChangeType** *(string) --*

      The conditions under which changes to this parameter can be applied. For example,
      ``requires-reboot`` indicates that a new value for this parameter will only take effect
      if a node is rebooted.
    """


_ClientDescribeParametersResponseTypeDef = TypedDict(
    "_ClientDescribeParametersResponseTypeDef",
    {
        "NextToken": str,
        "Parameters": List[ClientDescribeParametersResponseParametersTypeDef],
    },
    total=False,
)


class ClientDescribeParametersResponseTypeDef(_ClientDescribeParametersResponseTypeDef):
    """
    Type definition for `ClientDescribeParameters` `Response`

    - **NextToken** *(string) --*

      Provides an identifier to allow retrieval of paginated results.

    - **Parameters** *(list) --*

      A list of parameters within a parameter group. Each element in the list represents one
      parameter.

      - *(dict) --*

        Describes an individual setting that controls some aspect of DAX behavior.

        - **ParameterName** *(string) --*

          The name of the parameter.

        - **ParameterType** *(string) --*

          Determines whether the parameter can be applied to any nodes, or only nodes of a
          particular type.

        - **ParameterValue** *(string) --*

          The value for the parameter.

        - **NodeTypeSpecificValues** *(list) --*

          A list of node types, and specific parameter values for each node.

          - *(dict) --*

            Represents a parameter value that is applicable to a particular node type.

            - **NodeType** *(string) --*

              A node type to which the parameter value applies.

            - **Value** *(string) --*

              The parameter value for this node type.

        - **Description** *(string) --*

          A description of the parameter

        - **Source** *(string) --*

          How the parameter is defined. For example, ``system`` denotes a system-defined parameter.

        - **DataType** *(string) --*

          The data type of the parameter. For example, ``integer`` :

        - **AllowedValues** *(string) --*

          A range of values within which the parameter can be set.

        - **IsModifiable** *(string) --*

          Whether the customer is allowed to modify the parameter.

        - **ChangeType** *(string) --*

          The conditions under which changes to this parameter can be applied. For example,
          ``requires-reboot`` indicates that a new value for this parameter will only take effect
          if a node is rebooted.
    """


_ClientDescribeSubnetGroupsResponseSubnetGroupsSubnetsTypeDef = TypedDict(
    "_ClientDescribeSubnetGroupsResponseSubnetGroupsSubnetsTypeDef",
    {"SubnetIdentifier": str, "SubnetAvailabilityZone": str},
    total=False,
)


class ClientDescribeSubnetGroupsResponseSubnetGroupsSubnetsTypeDef(
    _ClientDescribeSubnetGroupsResponseSubnetGroupsSubnetsTypeDef
):
    """
    Type definition for `ClientDescribeSubnetGroupsResponseSubnetGroups` `Subnets`

    Represents the subnet associated with a DAX cluster. This parameter refers to subnets
    defined in Amazon Virtual Private Cloud (Amazon VPC) and used with DAX.

    - **SubnetIdentifier** *(string) --*

      The system-assigned identifier for the subnet.

    - **SubnetAvailabilityZone** *(string) --*

      The Availability Zone (AZ) for the subnet.
    """


_ClientDescribeSubnetGroupsResponseSubnetGroupsTypeDef = TypedDict(
    "_ClientDescribeSubnetGroupsResponseSubnetGroupsTypeDef",
    {
        "SubnetGroupName": str,
        "Description": str,
        "VpcId": str,
        "Subnets": List[ClientDescribeSubnetGroupsResponseSubnetGroupsSubnetsTypeDef],
    },
    total=False,
)


class ClientDescribeSubnetGroupsResponseSubnetGroupsTypeDef(
    _ClientDescribeSubnetGroupsResponseSubnetGroupsTypeDef
):
    """
    Type definition for `ClientDescribeSubnetGroupsResponse` `SubnetGroups`

    Represents the output of one of the following actions:

    * *CreateSubnetGroup*

    * *ModifySubnetGroup*

    - **SubnetGroupName** *(string) --*

      The name of the subnet group.

    - **Description** *(string) --*

      The description of the subnet group.

    - **VpcId** *(string) --*

      The Amazon Virtual Private Cloud identifier (VPC ID) of the subnet group.

    - **Subnets** *(list) --*

      A list of subnets associated with the subnet group.

      - *(dict) --*

        Represents the subnet associated with a DAX cluster. This parameter refers to subnets
        defined in Amazon Virtual Private Cloud (Amazon VPC) and used with DAX.

        - **SubnetIdentifier** *(string) --*

          The system-assigned identifier for the subnet.

        - **SubnetAvailabilityZone** *(string) --*

          The Availability Zone (AZ) for the subnet.
    """


_ClientDescribeSubnetGroupsResponseTypeDef = TypedDict(
    "_ClientDescribeSubnetGroupsResponseTypeDef",
    {
        "NextToken": str,
        "SubnetGroups": List[ClientDescribeSubnetGroupsResponseSubnetGroupsTypeDef],
    },
    total=False,
)


class ClientDescribeSubnetGroupsResponseTypeDef(
    _ClientDescribeSubnetGroupsResponseTypeDef
):
    """
    Type definition for `ClientDescribeSubnetGroups` `Response`

    - **NextToken** *(string) --*

      Provides an identifier to allow retrieval of paginated results.

    - **SubnetGroups** *(list) --*

      An array of subnet groups. Each element in the array represents a single subnet group.

      - *(dict) --*

        Represents the output of one of the following actions:

        * *CreateSubnetGroup*

        * *ModifySubnetGroup*

        - **SubnetGroupName** *(string) --*

          The name of the subnet group.

        - **Description** *(string) --*

          The description of the subnet group.

        - **VpcId** *(string) --*

          The Amazon Virtual Private Cloud identifier (VPC ID) of the subnet group.

        - **Subnets** *(list) --*

          A list of subnets associated with the subnet group.

          - *(dict) --*

            Represents the subnet associated with a DAX cluster. This parameter refers to subnets
            defined in Amazon Virtual Private Cloud (Amazon VPC) and used with DAX.

            - **SubnetIdentifier** *(string) --*

              The system-assigned identifier for the subnet.

            - **SubnetAvailabilityZone** *(string) --*

              The Availability Zone (AZ) for the subnet.
    """


_ClientIncreaseReplicationFactorResponseClusterClusterDiscoveryEndpointTypeDef = TypedDict(
    "_ClientIncreaseReplicationFactorResponseClusterClusterDiscoveryEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientIncreaseReplicationFactorResponseClusterClusterDiscoveryEndpointTypeDef(
    _ClientIncreaseReplicationFactorResponseClusterClusterDiscoveryEndpointTypeDef
):
    """
    Type definition for `ClientIncreaseReplicationFactorResponseCluster` `ClusterDiscoveryEndpoint`

    The configuration endpoint for this DAX cluster, consisting of a DNS name and a port
    number. Client applications can specify this endpoint, rather than an individual node
    endpoint, and allow the DAX client software to intelligently route requests and responses
    to nodes in the DAX cluster.

    - **Address** *(string) --*

      The DNS hostname of the endpoint.

    - **Port** *(integer) --*

      The port number that applications should use to connect to the endpoint.
    """


_ClientIncreaseReplicationFactorResponseClusterNodesEndpointTypeDef = TypedDict(
    "_ClientIncreaseReplicationFactorResponseClusterNodesEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientIncreaseReplicationFactorResponseClusterNodesEndpointTypeDef(
    _ClientIncreaseReplicationFactorResponseClusterNodesEndpointTypeDef
):
    """
    Type definition for `ClientIncreaseReplicationFactorResponseClusterNodes` `Endpoint`

    The endpoint for the node, consisting of a DNS name and a port number. Client
    applications can connect directly to a node endpoint, if desired (as an alternative to
    allowing DAX client software to intelligently route requests and responses to nodes in
    the DAX cluster.

    - **Address** *(string) --*

      The DNS hostname of the endpoint.

    - **Port** *(integer) --*

      The port number that applications should use to connect to the endpoint.
    """


_ClientIncreaseReplicationFactorResponseClusterNodesTypeDef = TypedDict(
    "_ClientIncreaseReplicationFactorResponseClusterNodesTypeDef",
    {
        "NodeId": str,
        "Endpoint": ClientIncreaseReplicationFactorResponseClusterNodesEndpointTypeDef,
        "NodeCreateTime": datetime,
        "AvailabilityZone": str,
        "NodeStatus": str,
        "ParameterGroupStatus": str,
    },
    total=False,
)


class ClientIncreaseReplicationFactorResponseClusterNodesTypeDef(
    _ClientIncreaseReplicationFactorResponseClusterNodesTypeDef
):
    """
    Type definition for `ClientIncreaseReplicationFactorResponseCluster` `Nodes`

    Represents an individual node within a DAX cluster.

    - **NodeId** *(string) --*

      A system-generated identifier for the node.

    - **Endpoint** *(dict) --*

      The endpoint for the node, consisting of a DNS name and a port number. Client
      applications can connect directly to a node endpoint, if desired (as an alternative to
      allowing DAX client software to intelligently route requests and responses to nodes in
      the DAX cluster.

      - **Address** *(string) --*

        The DNS hostname of the endpoint.

      - **Port** *(integer) --*

        The port number that applications should use to connect to the endpoint.

    - **NodeCreateTime** *(datetime) --*

      The date and time (in UNIX epoch format) when the node was launched.

    - **AvailabilityZone** *(string) --*

      The Availability Zone (AZ) in which the node has been deployed.

    - **NodeStatus** *(string) --*

      The current status of the node. For example: ``available`` .

    - **ParameterGroupStatus** *(string) --*

      The status of the parameter group associated with this node. For example, ``in-sync`` .
    """


_ClientIncreaseReplicationFactorResponseClusterNotificationConfigurationTypeDef = TypedDict(
    "_ClientIncreaseReplicationFactorResponseClusterNotificationConfigurationTypeDef",
    {"TopicArn": str, "TopicStatus": str},
    total=False,
)


class ClientIncreaseReplicationFactorResponseClusterNotificationConfigurationTypeDef(
    _ClientIncreaseReplicationFactorResponseClusterNotificationConfigurationTypeDef
):
    """
    Type definition for `ClientIncreaseReplicationFactorResponseCluster` `NotificationConfiguration`

    Describes a notification topic and its status. Notification topics are used for publishing
    DAX events to subscribers using Amazon Simple Notification Service (SNS).

    - **TopicArn** *(string) --*

      The Amazon Resource Name (ARN) that identifies the topic.

    - **TopicStatus** *(string) --*

      The current state of the topic.
    """


_ClientIncreaseReplicationFactorResponseClusterParameterGroupTypeDef = TypedDict(
    "_ClientIncreaseReplicationFactorResponseClusterParameterGroupTypeDef",
    {
        "ParameterGroupName": str,
        "ParameterApplyStatus": str,
        "NodeIdsToReboot": List[str],
    },
    total=False,
)


class ClientIncreaseReplicationFactorResponseClusterParameterGroupTypeDef(
    _ClientIncreaseReplicationFactorResponseClusterParameterGroupTypeDef
):
    """
    Type definition for `ClientIncreaseReplicationFactorResponseCluster` `ParameterGroup`

    The parameter group being used by nodes in the cluster.

    - **ParameterGroupName** *(string) --*

      The name of the parameter group.

    - **ParameterApplyStatus** *(string) --*

      The status of parameter updates.

    - **NodeIdsToReboot** *(list) --*

      The node IDs of one or more nodes to be rebooted.

      - *(string) --*
    """


_ClientIncreaseReplicationFactorResponseClusterSSEDescriptionTypeDef = TypedDict(
    "_ClientIncreaseReplicationFactorResponseClusterSSEDescriptionTypeDef",
    {"Status": str},
    total=False,
)


class ClientIncreaseReplicationFactorResponseClusterSSEDescriptionTypeDef(
    _ClientIncreaseReplicationFactorResponseClusterSSEDescriptionTypeDef
):
    """
    Type definition for `ClientIncreaseReplicationFactorResponseCluster` `SSEDescription`

    The description of the server-side encryption status on the specified DAX cluster.

    - **Status** *(string) --*

      The current state of server-side encryption:

      * ``ENABLING`` - Server-side encryption is being enabled.

      * ``ENABLED`` - Server-side encryption is enabled.

      * ``DISABLING`` - Server-side encryption is being disabled.

      * ``DISABLED`` - Server-side encryption is disabled.
    """


_ClientIncreaseReplicationFactorResponseClusterSecurityGroupsTypeDef = TypedDict(
    "_ClientIncreaseReplicationFactorResponseClusterSecurityGroupsTypeDef",
    {"SecurityGroupIdentifier": str, "Status": str},
    total=False,
)


class ClientIncreaseReplicationFactorResponseClusterSecurityGroupsTypeDef(
    _ClientIncreaseReplicationFactorResponseClusterSecurityGroupsTypeDef
):
    """
    Type definition for `ClientIncreaseReplicationFactorResponseCluster` `SecurityGroups`

    An individual VPC security group and its status.

    - **SecurityGroupIdentifier** *(string) --*

      The unique ID for this security group.

    - **Status** *(string) --*

      The status of this security group.
    """


_ClientIncreaseReplicationFactorResponseClusterTypeDef = TypedDict(
    "_ClientIncreaseReplicationFactorResponseClusterTypeDef",
    {
        "ClusterName": str,
        "Description": str,
        "ClusterArn": str,
        "TotalNodes": int,
        "ActiveNodes": int,
        "NodeType": str,
        "Status": str,
        "ClusterDiscoveryEndpoint": ClientIncreaseReplicationFactorResponseClusterClusterDiscoveryEndpointTypeDef,
        "NodeIdsToRemove": List[str],
        "Nodes": List[ClientIncreaseReplicationFactorResponseClusterNodesTypeDef],
        "PreferredMaintenanceWindow": str,
        "NotificationConfiguration": ClientIncreaseReplicationFactorResponseClusterNotificationConfigurationTypeDef,
        "SubnetGroup": str,
        "SecurityGroups": List[
            ClientIncreaseReplicationFactorResponseClusterSecurityGroupsTypeDef
        ],
        "IamRoleArn": str,
        "ParameterGroup": ClientIncreaseReplicationFactorResponseClusterParameterGroupTypeDef,
        "SSEDescription": ClientIncreaseReplicationFactorResponseClusterSSEDescriptionTypeDef,
    },
    total=False,
)


class ClientIncreaseReplicationFactorResponseClusterTypeDef(
    _ClientIncreaseReplicationFactorResponseClusterTypeDef
):
    """
    Type definition for `ClientIncreaseReplicationFactorResponse` `Cluster`

    A description of the DAX cluster. with its new replication factor.

    - **ClusterName** *(string) --*

      The name of the DAX cluster.

    - **Description** *(string) --*

      The description of the cluster.

    - **ClusterArn** *(string) --*

      The Amazon Resource Name (ARN) that uniquely identifies the cluster.

    - **TotalNodes** *(integer) --*

      The total number of nodes in the cluster.

    - **ActiveNodes** *(integer) --*

      The number of nodes in the cluster that are active (i.e., capable of serving requests).

    - **NodeType** *(string) --*

      The node type for the nodes in the cluster. (All nodes in a DAX cluster are of the same
      type.)

    - **Status** *(string) --*

      The current status of the cluster.

    - **ClusterDiscoveryEndpoint** *(dict) --*

      The configuration endpoint for this DAX cluster, consisting of a DNS name and a port
      number. Client applications can specify this endpoint, rather than an individual node
      endpoint, and allow the DAX client software to intelligently route requests and responses
      to nodes in the DAX cluster.

      - **Address** *(string) --*

        The DNS hostname of the endpoint.

      - **Port** *(integer) --*

        The port number that applications should use to connect to the endpoint.

    - **NodeIdsToRemove** *(list) --*

      A list of nodes to be removed from the cluster.

      - *(string) --*

    - **Nodes** *(list) --*

      A list of nodes that are currently in the cluster.

      - *(dict) --*

        Represents an individual node within a DAX cluster.

        - **NodeId** *(string) --*

          A system-generated identifier for the node.

        - **Endpoint** *(dict) --*

          The endpoint for the node, consisting of a DNS name and a port number. Client
          applications can connect directly to a node endpoint, if desired (as an alternative to
          allowing DAX client software to intelligently route requests and responses to nodes in
          the DAX cluster.

          - **Address** *(string) --*

            The DNS hostname of the endpoint.

          - **Port** *(integer) --*

            The port number that applications should use to connect to the endpoint.

        - **NodeCreateTime** *(datetime) --*

          The date and time (in UNIX epoch format) when the node was launched.

        - **AvailabilityZone** *(string) --*

          The Availability Zone (AZ) in which the node has been deployed.

        - **NodeStatus** *(string) --*

          The current status of the node. For example: ``available`` .

        - **ParameterGroupStatus** *(string) --*

          The status of the parameter group associated with this node. For example, ``in-sync`` .

    - **PreferredMaintenanceWindow** *(string) --*

      A range of time when maintenance of DAX cluster software will be performed. For example:
      ``sun:01:00-sun:09:00`` . Cluster maintenance normally takes less than 30 minutes, and is
      performed automatically within the maintenance window.

    - **NotificationConfiguration** *(dict) --*

      Describes a notification topic and its status. Notification topics are used for publishing
      DAX events to subscribers using Amazon Simple Notification Service (SNS).

      - **TopicArn** *(string) --*

        The Amazon Resource Name (ARN) that identifies the topic.

      - **TopicStatus** *(string) --*

        The current state of the topic.

    - **SubnetGroup** *(string) --*

      The subnet group where the DAX cluster is running.

    - **SecurityGroups** *(list) --*

      A list of security groups, and the status of each, for the nodes in the cluster.

      - *(dict) --*

        An individual VPC security group and its status.

        - **SecurityGroupIdentifier** *(string) --*

          The unique ID for this security group.

        - **Status** *(string) --*

          The status of this security group.

    - **IamRoleArn** *(string) --*

      A valid Amazon Resource Name (ARN) that identifies an IAM role. At runtime, DAX will assume
      this role and use the role's permissions to access DynamoDB on your behalf.

    - **ParameterGroup** *(dict) --*

      The parameter group being used by nodes in the cluster.

      - **ParameterGroupName** *(string) --*

        The name of the parameter group.

      - **ParameterApplyStatus** *(string) --*

        The status of parameter updates.

      - **NodeIdsToReboot** *(list) --*

        The node IDs of one or more nodes to be rebooted.

        - *(string) --*

    - **SSEDescription** *(dict) --*

      The description of the server-side encryption status on the specified DAX cluster.

      - **Status** *(string) --*

        The current state of server-side encryption:

        * ``ENABLING`` - Server-side encryption is being enabled.

        * ``ENABLED`` - Server-side encryption is enabled.

        * ``DISABLING`` - Server-side encryption is being disabled.

        * ``DISABLED`` - Server-side encryption is disabled.
    """


_ClientIncreaseReplicationFactorResponseTypeDef = TypedDict(
    "_ClientIncreaseReplicationFactorResponseTypeDef",
    {"Cluster": ClientIncreaseReplicationFactorResponseClusterTypeDef},
    total=False,
)


class ClientIncreaseReplicationFactorResponseTypeDef(
    _ClientIncreaseReplicationFactorResponseTypeDef
):
    """
    Type definition for `ClientIncreaseReplicationFactor` `Response`

    - **Cluster** *(dict) --*

      A description of the DAX cluster. with its new replication factor.

      - **ClusterName** *(string) --*

        The name of the DAX cluster.

      - **Description** *(string) --*

        The description of the cluster.

      - **ClusterArn** *(string) --*

        The Amazon Resource Name (ARN) that uniquely identifies the cluster.

      - **TotalNodes** *(integer) --*

        The total number of nodes in the cluster.

      - **ActiveNodes** *(integer) --*

        The number of nodes in the cluster that are active (i.e., capable of serving requests).

      - **NodeType** *(string) --*

        The node type for the nodes in the cluster. (All nodes in a DAX cluster are of the same
        type.)

      - **Status** *(string) --*

        The current status of the cluster.

      - **ClusterDiscoveryEndpoint** *(dict) --*

        The configuration endpoint for this DAX cluster, consisting of a DNS name and a port
        number. Client applications can specify this endpoint, rather than an individual node
        endpoint, and allow the DAX client software to intelligently route requests and responses
        to nodes in the DAX cluster.

        - **Address** *(string) --*

          The DNS hostname of the endpoint.

        - **Port** *(integer) --*

          The port number that applications should use to connect to the endpoint.

      - **NodeIdsToRemove** *(list) --*

        A list of nodes to be removed from the cluster.

        - *(string) --*

      - **Nodes** *(list) --*

        A list of nodes that are currently in the cluster.

        - *(dict) --*

          Represents an individual node within a DAX cluster.

          - **NodeId** *(string) --*

            A system-generated identifier for the node.

          - **Endpoint** *(dict) --*

            The endpoint for the node, consisting of a DNS name and a port number. Client
            applications can connect directly to a node endpoint, if desired (as an alternative to
            allowing DAX client software to intelligently route requests and responses to nodes in
            the DAX cluster.

            - **Address** *(string) --*

              The DNS hostname of the endpoint.

            - **Port** *(integer) --*

              The port number that applications should use to connect to the endpoint.

          - **NodeCreateTime** *(datetime) --*

            The date and time (in UNIX epoch format) when the node was launched.

          - **AvailabilityZone** *(string) --*

            The Availability Zone (AZ) in which the node has been deployed.

          - **NodeStatus** *(string) --*

            The current status of the node. For example: ``available`` .

          - **ParameterGroupStatus** *(string) --*

            The status of the parameter group associated with this node. For example, ``in-sync`` .

      - **PreferredMaintenanceWindow** *(string) --*

        A range of time when maintenance of DAX cluster software will be performed. For example:
        ``sun:01:00-sun:09:00`` . Cluster maintenance normally takes less than 30 minutes, and is
        performed automatically within the maintenance window.

      - **NotificationConfiguration** *(dict) --*

        Describes a notification topic and its status. Notification topics are used for publishing
        DAX events to subscribers using Amazon Simple Notification Service (SNS).

        - **TopicArn** *(string) --*

          The Amazon Resource Name (ARN) that identifies the topic.

        - **TopicStatus** *(string) --*

          The current state of the topic.

      - **SubnetGroup** *(string) --*

        The subnet group where the DAX cluster is running.

      - **SecurityGroups** *(list) --*

        A list of security groups, and the status of each, for the nodes in the cluster.

        - *(dict) --*

          An individual VPC security group and its status.

          - **SecurityGroupIdentifier** *(string) --*

            The unique ID for this security group.

          - **Status** *(string) --*

            The status of this security group.

      - **IamRoleArn** *(string) --*

        A valid Amazon Resource Name (ARN) that identifies an IAM role. At runtime, DAX will assume
        this role and use the role's permissions to access DynamoDB on your behalf.

      - **ParameterGroup** *(dict) --*

        The parameter group being used by nodes in the cluster.

        - **ParameterGroupName** *(string) --*

          The name of the parameter group.

        - **ParameterApplyStatus** *(string) --*

          The status of parameter updates.

        - **NodeIdsToReboot** *(list) --*

          The node IDs of one or more nodes to be rebooted.

          - *(string) --*

      - **SSEDescription** *(dict) --*

        The description of the server-side encryption status on the specified DAX cluster.

        - **Status** *(string) --*

          The current state of server-side encryption:

          * ``ENABLING`` - Server-side encryption is being enabled.

          * ``ENABLED`` - Server-side encryption is enabled.

          * ``DISABLING`` - Server-side encryption is being disabled.

          * ``DISABLED`` - Server-side encryption is disabled.
    """


_ClientListTagsResponseTagsTypeDef = TypedDict(
    "_ClientListTagsResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientListTagsResponseTagsTypeDef(_ClientListTagsResponseTagsTypeDef):
    """
    Type definition for `ClientListTagsResponse` `Tags`

    A description of a tag. Every tag is a key-value pair. You can add up to 50 tags to a
    single DAX cluster.

    AWS-assigned tag names and values are automatically assigned the ``aws:`` prefix, which the
    user cannot assign. AWS-assigned tag names do not count towards the tag limit of 50.
    User-assigned tag names have the prefix ``user:`` .

    You cannot backdate the application of a tag.

    - **Key** *(string) --*

      The key for the tag. Tag keys are case sensitive. Every DAX cluster can only have one tag
      with the same key. If you try to add an existing tag (same key), the existing tag value
      will be updated to the new value.

    - **Value** *(string) --*

      The value of the tag. Tag values are case-sensitive and can be null.
    """


_ClientListTagsResponseTypeDef = TypedDict(
    "_ClientListTagsResponseTypeDef",
    {"Tags": List[ClientListTagsResponseTagsTypeDef], "NextToken": str},
    total=False,
)


class ClientListTagsResponseTypeDef(_ClientListTagsResponseTypeDef):
    """
    Type definition for `ClientListTags` `Response`

    - **Tags** *(list) --*

      A list of tags currently associated with the DAX cluster.

      - *(dict) --*

        A description of a tag. Every tag is a key-value pair. You can add up to 50 tags to a
        single DAX cluster.

        AWS-assigned tag names and values are automatically assigned the ``aws:`` prefix, which the
        user cannot assign. AWS-assigned tag names do not count towards the tag limit of 50.
        User-assigned tag names have the prefix ``user:`` .

        You cannot backdate the application of a tag.

        - **Key** *(string) --*

          The key for the tag. Tag keys are case sensitive. Every DAX cluster can only have one tag
          with the same key. If you try to add an existing tag (same key), the existing tag value
          will be updated to the new value.

        - **Value** *(string) --*

          The value of the tag. Tag values are case-sensitive and can be null.

    - **NextToken** *(string) --*

      If this value is present, there are additional results to be displayed. To retrieve them,
      call ``ListTags`` again, with ``NextToken`` set to this value.
    """


_ClientRebootNodeResponseClusterClusterDiscoveryEndpointTypeDef = TypedDict(
    "_ClientRebootNodeResponseClusterClusterDiscoveryEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientRebootNodeResponseClusterClusterDiscoveryEndpointTypeDef(
    _ClientRebootNodeResponseClusterClusterDiscoveryEndpointTypeDef
):
    """
    Type definition for `ClientRebootNodeResponseCluster` `ClusterDiscoveryEndpoint`

    The configuration endpoint for this DAX cluster, consisting of a DNS name and a port
    number. Client applications can specify this endpoint, rather than an individual node
    endpoint, and allow the DAX client software to intelligently route requests and responses
    to nodes in the DAX cluster.

    - **Address** *(string) --*

      The DNS hostname of the endpoint.

    - **Port** *(integer) --*

      The port number that applications should use to connect to the endpoint.
    """


_ClientRebootNodeResponseClusterNodesEndpointTypeDef = TypedDict(
    "_ClientRebootNodeResponseClusterNodesEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientRebootNodeResponseClusterNodesEndpointTypeDef(
    _ClientRebootNodeResponseClusterNodesEndpointTypeDef
):
    """
    Type definition for `ClientRebootNodeResponseClusterNodes` `Endpoint`

    The endpoint for the node, consisting of a DNS name and a port number. Client
    applications can connect directly to a node endpoint, if desired (as an alternative to
    allowing DAX client software to intelligently route requests and responses to nodes in
    the DAX cluster.

    - **Address** *(string) --*

      The DNS hostname of the endpoint.

    - **Port** *(integer) --*

      The port number that applications should use to connect to the endpoint.
    """


_ClientRebootNodeResponseClusterNodesTypeDef = TypedDict(
    "_ClientRebootNodeResponseClusterNodesTypeDef",
    {
        "NodeId": str,
        "Endpoint": ClientRebootNodeResponseClusterNodesEndpointTypeDef,
        "NodeCreateTime": datetime,
        "AvailabilityZone": str,
        "NodeStatus": str,
        "ParameterGroupStatus": str,
    },
    total=False,
)


class ClientRebootNodeResponseClusterNodesTypeDef(
    _ClientRebootNodeResponseClusterNodesTypeDef
):
    """
    Type definition for `ClientRebootNodeResponseCluster` `Nodes`

    Represents an individual node within a DAX cluster.

    - **NodeId** *(string) --*

      A system-generated identifier for the node.

    - **Endpoint** *(dict) --*

      The endpoint for the node, consisting of a DNS name and a port number. Client
      applications can connect directly to a node endpoint, if desired (as an alternative to
      allowing DAX client software to intelligently route requests and responses to nodes in
      the DAX cluster.

      - **Address** *(string) --*

        The DNS hostname of the endpoint.

      - **Port** *(integer) --*

        The port number that applications should use to connect to the endpoint.

    - **NodeCreateTime** *(datetime) --*

      The date and time (in UNIX epoch format) when the node was launched.

    - **AvailabilityZone** *(string) --*

      The Availability Zone (AZ) in which the node has been deployed.

    - **NodeStatus** *(string) --*

      The current status of the node. For example: ``available`` .

    - **ParameterGroupStatus** *(string) --*

      The status of the parameter group associated with this node. For example, ``in-sync`` .
    """


_ClientRebootNodeResponseClusterNotificationConfigurationTypeDef = TypedDict(
    "_ClientRebootNodeResponseClusterNotificationConfigurationTypeDef",
    {"TopicArn": str, "TopicStatus": str},
    total=False,
)


class ClientRebootNodeResponseClusterNotificationConfigurationTypeDef(
    _ClientRebootNodeResponseClusterNotificationConfigurationTypeDef
):
    """
    Type definition for `ClientRebootNodeResponseCluster` `NotificationConfiguration`

    Describes a notification topic and its status. Notification topics are used for publishing
    DAX events to subscribers using Amazon Simple Notification Service (SNS).

    - **TopicArn** *(string) --*

      The Amazon Resource Name (ARN) that identifies the topic.

    - **TopicStatus** *(string) --*

      The current state of the topic.
    """


_ClientRebootNodeResponseClusterParameterGroupTypeDef = TypedDict(
    "_ClientRebootNodeResponseClusterParameterGroupTypeDef",
    {
        "ParameterGroupName": str,
        "ParameterApplyStatus": str,
        "NodeIdsToReboot": List[str],
    },
    total=False,
)


class ClientRebootNodeResponseClusterParameterGroupTypeDef(
    _ClientRebootNodeResponseClusterParameterGroupTypeDef
):
    """
    Type definition for `ClientRebootNodeResponseCluster` `ParameterGroup`

    The parameter group being used by nodes in the cluster.

    - **ParameterGroupName** *(string) --*

      The name of the parameter group.

    - **ParameterApplyStatus** *(string) --*

      The status of parameter updates.

    - **NodeIdsToReboot** *(list) --*

      The node IDs of one or more nodes to be rebooted.

      - *(string) --*
    """


_ClientRebootNodeResponseClusterSSEDescriptionTypeDef = TypedDict(
    "_ClientRebootNodeResponseClusterSSEDescriptionTypeDef",
    {"Status": str},
    total=False,
)


class ClientRebootNodeResponseClusterSSEDescriptionTypeDef(
    _ClientRebootNodeResponseClusterSSEDescriptionTypeDef
):
    """
    Type definition for `ClientRebootNodeResponseCluster` `SSEDescription`

    The description of the server-side encryption status on the specified DAX cluster.

    - **Status** *(string) --*

      The current state of server-side encryption:

      * ``ENABLING`` - Server-side encryption is being enabled.

      * ``ENABLED`` - Server-side encryption is enabled.

      * ``DISABLING`` - Server-side encryption is being disabled.

      * ``DISABLED`` - Server-side encryption is disabled.
    """


_ClientRebootNodeResponseClusterSecurityGroupsTypeDef = TypedDict(
    "_ClientRebootNodeResponseClusterSecurityGroupsTypeDef",
    {"SecurityGroupIdentifier": str, "Status": str},
    total=False,
)


class ClientRebootNodeResponseClusterSecurityGroupsTypeDef(
    _ClientRebootNodeResponseClusterSecurityGroupsTypeDef
):
    """
    Type definition for `ClientRebootNodeResponseCluster` `SecurityGroups`

    An individual VPC security group and its status.

    - **SecurityGroupIdentifier** *(string) --*

      The unique ID for this security group.

    - **Status** *(string) --*

      The status of this security group.
    """


_ClientRebootNodeResponseClusterTypeDef = TypedDict(
    "_ClientRebootNodeResponseClusterTypeDef",
    {
        "ClusterName": str,
        "Description": str,
        "ClusterArn": str,
        "TotalNodes": int,
        "ActiveNodes": int,
        "NodeType": str,
        "Status": str,
        "ClusterDiscoveryEndpoint": ClientRebootNodeResponseClusterClusterDiscoveryEndpointTypeDef,
        "NodeIdsToRemove": List[str],
        "Nodes": List[ClientRebootNodeResponseClusterNodesTypeDef],
        "PreferredMaintenanceWindow": str,
        "NotificationConfiguration": ClientRebootNodeResponseClusterNotificationConfigurationTypeDef,
        "SubnetGroup": str,
        "SecurityGroups": List[ClientRebootNodeResponseClusterSecurityGroupsTypeDef],
        "IamRoleArn": str,
        "ParameterGroup": ClientRebootNodeResponseClusterParameterGroupTypeDef,
        "SSEDescription": ClientRebootNodeResponseClusterSSEDescriptionTypeDef,
    },
    total=False,
)


class ClientRebootNodeResponseClusterTypeDef(_ClientRebootNodeResponseClusterTypeDef):
    """
    Type definition for `ClientRebootNodeResponse` `Cluster`

    A description of the DAX cluster after a node has been rebooted.

    - **ClusterName** *(string) --*

      The name of the DAX cluster.

    - **Description** *(string) --*

      The description of the cluster.

    - **ClusterArn** *(string) --*

      The Amazon Resource Name (ARN) that uniquely identifies the cluster.

    - **TotalNodes** *(integer) --*

      The total number of nodes in the cluster.

    - **ActiveNodes** *(integer) --*

      The number of nodes in the cluster that are active (i.e., capable of serving requests).

    - **NodeType** *(string) --*

      The node type for the nodes in the cluster. (All nodes in a DAX cluster are of the same
      type.)

    - **Status** *(string) --*

      The current status of the cluster.

    - **ClusterDiscoveryEndpoint** *(dict) --*

      The configuration endpoint for this DAX cluster, consisting of a DNS name and a port
      number. Client applications can specify this endpoint, rather than an individual node
      endpoint, and allow the DAX client software to intelligently route requests and responses
      to nodes in the DAX cluster.

      - **Address** *(string) --*

        The DNS hostname of the endpoint.

      - **Port** *(integer) --*

        The port number that applications should use to connect to the endpoint.

    - **NodeIdsToRemove** *(list) --*

      A list of nodes to be removed from the cluster.

      - *(string) --*

    - **Nodes** *(list) --*

      A list of nodes that are currently in the cluster.

      - *(dict) --*

        Represents an individual node within a DAX cluster.

        - **NodeId** *(string) --*

          A system-generated identifier for the node.

        - **Endpoint** *(dict) --*

          The endpoint for the node, consisting of a DNS name and a port number. Client
          applications can connect directly to a node endpoint, if desired (as an alternative to
          allowing DAX client software to intelligently route requests and responses to nodes in
          the DAX cluster.

          - **Address** *(string) --*

            The DNS hostname of the endpoint.

          - **Port** *(integer) --*

            The port number that applications should use to connect to the endpoint.

        - **NodeCreateTime** *(datetime) --*

          The date and time (in UNIX epoch format) when the node was launched.

        - **AvailabilityZone** *(string) --*

          The Availability Zone (AZ) in which the node has been deployed.

        - **NodeStatus** *(string) --*

          The current status of the node. For example: ``available`` .

        - **ParameterGroupStatus** *(string) --*

          The status of the parameter group associated with this node. For example, ``in-sync`` .

    - **PreferredMaintenanceWindow** *(string) --*

      A range of time when maintenance of DAX cluster software will be performed. For example:
      ``sun:01:00-sun:09:00`` . Cluster maintenance normally takes less than 30 minutes, and is
      performed automatically within the maintenance window.

    - **NotificationConfiguration** *(dict) --*

      Describes a notification topic and its status. Notification topics are used for publishing
      DAX events to subscribers using Amazon Simple Notification Service (SNS).

      - **TopicArn** *(string) --*

        The Amazon Resource Name (ARN) that identifies the topic.

      - **TopicStatus** *(string) --*

        The current state of the topic.

    - **SubnetGroup** *(string) --*

      The subnet group where the DAX cluster is running.

    - **SecurityGroups** *(list) --*

      A list of security groups, and the status of each, for the nodes in the cluster.

      - *(dict) --*

        An individual VPC security group and its status.

        - **SecurityGroupIdentifier** *(string) --*

          The unique ID for this security group.

        - **Status** *(string) --*

          The status of this security group.

    - **IamRoleArn** *(string) --*

      A valid Amazon Resource Name (ARN) that identifies an IAM role. At runtime, DAX will assume
      this role and use the role's permissions to access DynamoDB on your behalf.

    - **ParameterGroup** *(dict) --*

      The parameter group being used by nodes in the cluster.

      - **ParameterGroupName** *(string) --*

        The name of the parameter group.

      - **ParameterApplyStatus** *(string) --*

        The status of parameter updates.

      - **NodeIdsToReboot** *(list) --*

        The node IDs of one or more nodes to be rebooted.

        - *(string) --*

    - **SSEDescription** *(dict) --*

      The description of the server-side encryption status on the specified DAX cluster.

      - **Status** *(string) --*

        The current state of server-side encryption:

        * ``ENABLING`` - Server-side encryption is being enabled.

        * ``ENABLED`` - Server-side encryption is enabled.

        * ``DISABLING`` - Server-side encryption is being disabled.

        * ``DISABLED`` - Server-side encryption is disabled.
    """


_ClientRebootNodeResponseTypeDef = TypedDict(
    "_ClientRebootNodeResponseTypeDef",
    {"Cluster": ClientRebootNodeResponseClusterTypeDef},
    total=False,
)


class ClientRebootNodeResponseTypeDef(_ClientRebootNodeResponseTypeDef):
    """
    Type definition for `ClientRebootNode` `Response`

    - **Cluster** *(dict) --*

      A description of the DAX cluster after a node has been rebooted.

      - **ClusterName** *(string) --*

        The name of the DAX cluster.

      - **Description** *(string) --*

        The description of the cluster.

      - **ClusterArn** *(string) --*

        The Amazon Resource Name (ARN) that uniquely identifies the cluster.

      - **TotalNodes** *(integer) --*

        The total number of nodes in the cluster.

      - **ActiveNodes** *(integer) --*

        The number of nodes in the cluster that are active (i.e., capable of serving requests).

      - **NodeType** *(string) --*

        The node type for the nodes in the cluster. (All nodes in a DAX cluster are of the same
        type.)

      - **Status** *(string) --*

        The current status of the cluster.

      - **ClusterDiscoveryEndpoint** *(dict) --*

        The configuration endpoint for this DAX cluster, consisting of a DNS name and a port
        number. Client applications can specify this endpoint, rather than an individual node
        endpoint, and allow the DAX client software to intelligently route requests and responses
        to nodes in the DAX cluster.

        - **Address** *(string) --*

          The DNS hostname of the endpoint.

        - **Port** *(integer) --*

          The port number that applications should use to connect to the endpoint.

      - **NodeIdsToRemove** *(list) --*

        A list of nodes to be removed from the cluster.

        - *(string) --*

      - **Nodes** *(list) --*

        A list of nodes that are currently in the cluster.

        - *(dict) --*

          Represents an individual node within a DAX cluster.

          - **NodeId** *(string) --*

            A system-generated identifier for the node.

          - **Endpoint** *(dict) --*

            The endpoint for the node, consisting of a DNS name and a port number. Client
            applications can connect directly to a node endpoint, if desired (as an alternative to
            allowing DAX client software to intelligently route requests and responses to nodes in
            the DAX cluster.

            - **Address** *(string) --*

              The DNS hostname of the endpoint.

            - **Port** *(integer) --*

              The port number that applications should use to connect to the endpoint.

          - **NodeCreateTime** *(datetime) --*

            The date and time (in UNIX epoch format) when the node was launched.

          - **AvailabilityZone** *(string) --*

            The Availability Zone (AZ) in which the node has been deployed.

          - **NodeStatus** *(string) --*

            The current status of the node. For example: ``available`` .

          - **ParameterGroupStatus** *(string) --*

            The status of the parameter group associated with this node. For example, ``in-sync`` .

      - **PreferredMaintenanceWindow** *(string) --*

        A range of time when maintenance of DAX cluster software will be performed. For example:
        ``sun:01:00-sun:09:00`` . Cluster maintenance normally takes less than 30 minutes, and is
        performed automatically within the maintenance window.

      - **NotificationConfiguration** *(dict) --*

        Describes a notification topic and its status. Notification topics are used for publishing
        DAX events to subscribers using Amazon Simple Notification Service (SNS).

        - **TopicArn** *(string) --*

          The Amazon Resource Name (ARN) that identifies the topic.

        - **TopicStatus** *(string) --*

          The current state of the topic.

      - **SubnetGroup** *(string) --*

        The subnet group where the DAX cluster is running.

      - **SecurityGroups** *(list) --*

        A list of security groups, and the status of each, for the nodes in the cluster.

        - *(dict) --*

          An individual VPC security group and its status.

          - **SecurityGroupIdentifier** *(string) --*

            The unique ID for this security group.

          - **Status** *(string) --*

            The status of this security group.

      - **IamRoleArn** *(string) --*

        A valid Amazon Resource Name (ARN) that identifies an IAM role. At runtime, DAX will assume
        this role and use the role's permissions to access DynamoDB on your behalf.

      - **ParameterGroup** *(dict) --*

        The parameter group being used by nodes in the cluster.

        - **ParameterGroupName** *(string) --*

          The name of the parameter group.

        - **ParameterApplyStatus** *(string) --*

          The status of parameter updates.

        - **NodeIdsToReboot** *(list) --*

          The node IDs of one or more nodes to be rebooted.

          - *(string) --*

      - **SSEDescription** *(dict) --*

        The description of the server-side encryption status on the specified DAX cluster.

        - **Status** *(string) --*

          The current state of server-side encryption:

          * ``ENABLING`` - Server-side encryption is being enabled.

          * ``ENABLED`` - Server-side encryption is enabled.

          * ``DISABLING`` - Server-side encryption is being disabled.

          * ``DISABLED`` - Server-side encryption is disabled.
    """


_ClientTagResourceResponseTagsTypeDef = TypedDict(
    "_ClientTagResourceResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientTagResourceResponseTagsTypeDef(_ClientTagResourceResponseTagsTypeDef):
    """
    Type definition for `ClientTagResourceResponse` `Tags`

    A description of a tag. Every tag is a key-value pair. You can add up to 50 tags to a
    single DAX cluster.

    AWS-assigned tag names and values are automatically assigned the ``aws:`` prefix, which the
    user cannot assign. AWS-assigned tag names do not count towards the tag limit of 50.
    User-assigned tag names have the prefix ``user:`` .

    You cannot backdate the application of a tag.

    - **Key** *(string) --*

      The key for the tag. Tag keys are case sensitive. Every DAX cluster can only have one tag
      with the same key. If you try to add an existing tag (same key), the existing tag value
      will be updated to the new value.

    - **Value** *(string) --*

      The value of the tag. Tag values are case-sensitive and can be null.
    """


_ClientTagResourceResponseTypeDef = TypedDict(
    "_ClientTagResourceResponseTypeDef",
    {"Tags": List[ClientTagResourceResponseTagsTypeDef]},
    total=False,
)


class ClientTagResourceResponseTypeDef(_ClientTagResourceResponseTypeDef):
    """
    Type definition for `ClientTagResource` `Response`

    - **Tags** *(list) --*

      The list of tags that are associated with the DAX resource.

      - *(dict) --*

        A description of a tag. Every tag is a key-value pair. You can add up to 50 tags to a
        single DAX cluster.

        AWS-assigned tag names and values are automatically assigned the ``aws:`` prefix, which the
        user cannot assign. AWS-assigned tag names do not count towards the tag limit of 50.
        User-assigned tag names have the prefix ``user:`` .

        You cannot backdate the application of a tag.

        - **Key** *(string) --*

          The key for the tag. Tag keys are case sensitive. Every DAX cluster can only have one tag
          with the same key. If you try to add an existing tag (same key), the existing tag value
          will be updated to the new value.

        - **Value** *(string) --*

          The value of the tag. Tag values are case-sensitive and can be null.
    """


_ClientTagResourceTagsTypeDef = TypedDict(
    "_ClientTagResourceTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientTagResourceTagsTypeDef(_ClientTagResourceTagsTypeDef):
    """
    Type definition for `ClientTagResource` `Tags`

    A description of a tag. Every tag is a key-value pair. You can add up to 50 tags to a single
    DAX cluster.

    AWS-assigned tag names and values are automatically assigned the ``aws:`` prefix, which the
    user cannot assign. AWS-assigned tag names do not count towards the tag limit of 50.
    User-assigned tag names have the prefix ``user:`` .

    You cannot backdate the application of a tag.

    - **Key** *(string) --*

      The key for the tag. Tag keys are case sensitive. Every DAX cluster can only have one tag
      with the same key. If you try to add an existing tag (same key), the existing tag value will
      be updated to the new value.

    - **Value** *(string) --*

      The value of the tag. Tag values are case-sensitive and can be null.
    """


_ClientUntagResourceResponseTagsTypeDef = TypedDict(
    "_ClientUntagResourceResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientUntagResourceResponseTagsTypeDef(_ClientUntagResourceResponseTagsTypeDef):
    """
    Type definition for `ClientUntagResourceResponse` `Tags`

    A description of a tag. Every tag is a key-value pair. You can add up to 50 tags to a
    single DAX cluster.

    AWS-assigned tag names and values are automatically assigned the ``aws:`` prefix, which the
    user cannot assign. AWS-assigned tag names do not count towards the tag limit of 50.
    User-assigned tag names have the prefix ``user:`` .

    You cannot backdate the application of a tag.

    - **Key** *(string) --*

      The key for the tag. Tag keys are case sensitive. Every DAX cluster can only have one tag
      with the same key. If you try to add an existing tag (same key), the existing tag value
      will be updated to the new value.

    - **Value** *(string) --*

      The value of the tag. Tag values are case-sensitive and can be null.
    """


_ClientUntagResourceResponseTypeDef = TypedDict(
    "_ClientUntagResourceResponseTypeDef",
    {"Tags": List[ClientUntagResourceResponseTagsTypeDef]},
    total=False,
)


class ClientUntagResourceResponseTypeDef(_ClientUntagResourceResponseTypeDef):
    """
    Type definition for `ClientUntagResource` `Response`

    - **Tags** *(list) --*

      The tag keys that have been removed from the cluster.

      - *(dict) --*

        A description of a tag. Every tag is a key-value pair. You can add up to 50 tags to a
        single DAX cluster.

        AWS-assigned tag names and values are automatically assigned the ``aws:`` prefix, which the
        user cannot assign. AWS-assigned tag names do not count towards the tag limit of 50.
        User-assigned tag names have the prefix ``user:`` .

        You cannot backdate the application of a tag.

        - **Key** *(string) --*

          The key for the tag. Tag keys are case sensitive. Every DAX cluster can only have one tag
          with the same key. If you try to add an existing tag (same key), the existing tag value
          will be updated to the new value.

        - **Value** *(string) --*

          The value of the tag. Tag values are case-sensitive and can be null.
    """


_ClientUpdateClusterResponseClusterClusterDiscoveryEndpointTypeDef = TypedDict(
    "_ClientUpdateClusterResponseClusterClusterDiscoveryEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientUpdateClusterResponseClusterClusterDiscoveryEndpointTypeDef(
    _ClientUpdateClusterResponseClusterClusterDiscoveryEndpointTypeDef
):
    """
    Type definition for `ClientUpdateClusterResponseCluster` `ClusterDiscoveryEndpoint`

    The configuration endpoint for this DAX cluster, consisting of a DNS name and a port
    number. Client applications can specify this endpoint, rather than an individual node
    endpoint, and allow the DAX client software to intelligently route requests and responses
    to nodes in the DAX cluster.

    - **Address** *(string) --*

      The DNS hostname of the endpoint.

    - **Port** *(integer) --*

      The port number that applications should use to connect to the endpoint.
    """


_ClientUpdateClusterResponseClusterNodesEndpointTypeDef = TypedDict(
    "_ClientUpdateClusterResponseClusterNodesEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientUpdateClusterResponseClusterNodesEndpointTypeDef(
    _ClientUpdateClusterResponseClusterNodesEndpointTypeDef
):
    """
    Type definition for `ClientUpdateClusterResponseClusterNodes` `Endpoint`

    The endpoint for the node, consisting of a DNS name and a port number. Client
    applications can connect directly to a node endpoint, if desired (as an alternative to
    allowing DAX client software to intelligently route requests and responses to nodes in
    the DAX cluster.

    - **Address** *(string) --*

      The DNS hostname of the endpoint.

    - **Port** *(integer) --*

      The port number that applications should use to connect to the endpoint.
    """


_ClientUpdateClusterResponseClusterNodesTypeDef = TypedDict(
    "_ClientUpdateClusterResponseClusterNodesTypeDef",
    {
        "NodeId": str,
        "Endpoint": ClientUpdateClusterResponseClusterNodesEndpointTypeDef,
        "NodeCreateTime": datetime,
        "AvailabilityZone": str,
        "NodeStatus": str,
        "ParameterGroupStatus": str,
    },
    total=False,
)


class ClientUpdateClusterResponseClusterNodesTypeDef(
    _ClientUpdateClusterResponseClusterNodesTypeDef
):
    """
    Type definition for `ClientUpdateClusterResponseCluster` `Nodes`

    Represents an individual node within a DAX cluster.

    - **NodeId** *(string) --*

      A system-generated identifier for the node.

    - **Endpoint** *(dict) --*

      The endpoint for the node, consisting of a DNS name and a port number. Client
      applications can connect directly to a node endpoint, if desired (as an alternative to
      allowing DAX client software to intelligently route requests and responses to nodes in
      the DAX cluster.

      - **Address** *(string) --*

        The DNS hostname of the endpoint.

      - **Port** *(integer) --*

        The port number that applications should use to connect to the endpoint.

    - **NodeCreateTime** *(datetime) --*

      The date and time (in UNIX epoch format) when the node was launched.

    - **AvailabilityZone** *(string) --*

      The Availability Zone (AZ) in which the node has been deployed.

    - **NodeStatus** *(string) --*

      The current status of the node. For example: ``available`` .

    - **ParameterGroupStatus** *(string) --*

      The status of the parameter group associated with this node. For example, ``in-sync`` .
    """


_ClientUpdateClusterResponseClusterNotificationConfigurationTypeDef = TypedDict(
    "_ClientUpdateClusterResponseClusterNotificationConfigurationTypeDef",
    {"TopicArn": str, "TopicStatus": str},
    total=False,
)


class ClientUpdateClusterResponseClusterNotificationConfigurationTypeDef(
    _ClientUpdateClusterResponseClusterNotificationConfigurationTypeDef
):
    """
    Type definition for `ClientUpdateClusterResponseCluster` `NotificationConfiguration`

    Describes a notification topic and its status. Notification topics are used for publishing
    DAX events to subscribers using Amazon Simple Notification Service (SNS).

    - **TopicArn** *(string) --*

      The Amazon Resource Name (ARN) that identifies the topic.

    - **TopicStatus** *(string) --*

      The current state of the topic.
    """


_ClientUpdateClusterResponseClusterParameterGroupTypeDef = TypedDict(
    "_ClientUpdateClusterResponseClusterParameterGroupTypeDef",
    {
        "ParameterGroupName": str,
        "ParameterApplyStatus": str,
        "NodeIdsToReboot": List[str],
    },
    total=False,
)


class ClientUpdateClusterResponseClusterParameterGroupTypeDef(
    _ClientUpdateClusterResponseClusterParameterGroupTypeDef
):
    """
    Type definition for `ClientUpdateClusterResponseCluster` `ParameterGroup`

    The parameter group being used by nodes in the cluster.

    - **ParameterGroupName** *(string) --*

      The name of the parameter group.

    - **ParameterApplyStatus** *(string) --*

      The status of parameter updates.

    - **NodeIdsToReboot** *(list) --*

      The node IDs of one or more nodes to be rebooted.

      - *(string) --*
    """


_ClientUpdateClusterResponseClusterSSEDescriptionTypeDef = TypedDict(
    "_ClientUpdateClusterResponseClusterSSEDescriptionTypeDef",
    {"Status": str},
    total=False,
)


class ClientUpdateClusterResponseClusterSSEDescriptionTypeDef(
    _ClientUpdateClusterResponseClusterSSEDescriptionTypeDef
):
    """
    Type definition for `ClientUpdateClusterResponseCluster` `SSEDescription`

    The description of the server-side encryption status on the specified DAX cluster.

    - **Status** *(string) --*

      The current state of server-side encryption:

      * ``ENABLING`` - Server-side encryption is being enabled.

      * ``ENABLED`` - Server-side encryption is enabled.

      * ``DISABLING`` - Server-side encryption is being disabled.

      * ``DISABLED`` - Server-side encryption is disabled.
    """


_ClientUpdateClusterResponseClusterSecurityGroupsTypeDef = TypedDict(
    "_ClientUpdateClusterResponseClusterSecurityGroupsTypeDef",
    {"SecurityGroupIdentifier": str, "Status": str},
    total=False,
)


class ClientUpdateClusterResponseClusterSecurityGroupsTypeDef(
    _ClientUpdateClusterResponseClusterSecurityGroupsTypeDef
):
    """
    Type definition for `ClientUpdateClusterResponseCluster` `SecurityGroups`

    An individual VPC security group and its status.

    - **SecurityGroupIdentifier** *(string) --*

      The unique ID for this security group.

    - **Status** *(string) --*

      The status of this security group.
    """


_ClientUpdateClusterResponseClusterTypeDef = TypedDict(
    "_ClientUpdateClusterResponseClusterTypeDef",
    {
        "ClusterName": str,
        "Description": str,
        "ClusterArn": str,
        "TotalNodes": int,
        "ActiveNodes": int,
        "NodeType": str,
        "Status": str,
        "ClusterDiscoveryEndpoint": ClientUpdateClusterResponseClusterClusterDiscoveryEndpointTypeDef,
        "NodeIdsToRemove": List[str],
        "Nodes": List[ClientUpdateClusterResponseClusterNodesTypeDef],
        "PreferredMaintenanceWindow": str,
        "NotificationConfiguration": ClientUpdateClusterResponseClusterNotificationConfigurationTypeDef,
        "SubnetGroup": str,
        "SecurityGroups": List[ClientUpdateClusterResponseClusterSecurityGroupsTypeDef],
        "IamRoleArn": str,
        "ParameterGroup": ClientUpdateClusterResponseClusterParameterGroupTypeDef,
        "SSEDescription": ClientUpdateClusterResponseClusterSSEDescriptionTypeDef,
    },
    total=False,
)


class ClientUpdateClusterResponseClusterTypeDef(
    _ClientUpdateClusterResponseClusterTypeDef
):
    """
    Type definition for `ClientUpdateClusterResponse` `Cluster`

    A description of the DAX cluster, after it has been modified.

    - **ClusterName** *(string) --*

      The name of the DAX cluster.

    - **Description** *(string) --*

      The description of the cluster.

    - **ClusterArn** *(string) --*

      The Amazon Resource Name (ARN) that uniquely identifies the cluster.

    - **TotalNodes** *(integer) --*

      The total number of nodes in the cluster.

    - **ActiveNodes** *(integer) --*

      The number of nodes in the cluster that are active (i.e., capable of serving requests).

    - **NodeType** *(string) --*

      The node type for the nodes in the cluster. (All nodes in a DAX cluster are of the same
      type.)

    - **Status** *(string) --*

      The current status of the cluster.

    - **ClusterDiscoveryEndpoint** *(dict) --*

      The configuration endpoint for this DAX cluster, consisting of a DNS name and a port
      number. Client applications can specify this endpoint, rather than an individual node
      endpoint, and allow the DAX client software to intelligently route requests and responses
      to nodes in the DAX cluster.

      - **Address** *(string) --*

        The DNS hostname of the endpoint.

      - **Port** *(integer) --*

        The port number that applications should use to connect to the endpoint.

    - **NodeIdsToRemove** *(list) --*

      A list of nodes to be removed from the cluster.

      - *(string) --*

    - **Nodes** *(list) --*

      A list of nodes that are currently in the cluster.

      - *(dict) --*

        Represents an individual node within a DAX cluster.

        - **NodeId** *(string) --*

          A system-generated identifier for the node.

        - **Endpoint** *(dict) --*

          The endpoint for the node, consisting of a DNS name and a port number. Client
          applications can connect directly to a node endpoint, if desired (as an alternative to
          allowing DAX client software to intelligently route requests and responses to nodes in
          the DAX cluster.

          - **Address** *(string) --*

            The DNS hostname of the endpoint.

          - **Port** *(integer) --*

            The port number that applications should use to connect to the endpoint.

        - **NodeCreateTime** *(datetime) --*

          The date and time (in UNIX epoch format) when the node was launched.

        - **AvailabilityZone** *(string) --*

          The Availability Zone (AZ) in which the node has been deployed.

        - **NodeStatus** *(string) --*

          The current status of the node. For example: ``available`` .

        - **ParameterGroupStatus** *(string) --*

          The status of the parameter group associated with this node. For example, ``in-sync`` .

    - **PreferredMaintenanceWindow** *(string) --*

      A range of time when maintenance of DAX cluster software will be performed. For example:
      ``sun:01:00-sun:09:00`` . Cluster maintenance normally takes less than 30 minutes, and is
      performed automatically within the maintenance window.

    - **NotificationConfiguration** *(dict) --*

      Describes a notification topic and its status. Notification topics are used for publishing
      DAX events to subscribers using Amazon Simple Notification Service (SNS).

      - **TopicArn** *(string) --*

        The Amazon Resource Name (ARN) that identifies the topic.

      - **TopicStatus** *(string) --*

        The current state of the topic.

    - **SubnetGroup** *(string) --*

      The subnet group where the DAX cluster is running.

    - **SecurityGroups** *(list) --*

      A list of security groups, and the status of each, for the nodes in the cluster.

      - *(dict) --*

        An individual VPC security group and its status.

        - **SecurityGroupIdentifier** *(string) --*

          The unique ID for this security group.

        - **Status** *(string) --*

          The status of this security group.

    - **IamRoleArn** *(string) --*

      A valid Amazon Resource Name (ARN) that identifies an IAM role. At runtime, DAX will assume
      this role and use the role's permissions to access DynamoDB on your behalf.

    - **ParameterGroup** *(dict) --*

      The parameter group being used by nodes in the cluster.

      - **ParameterGroupName** *(string) --*

        The name of the parameter group.

      - **ParameterApplyStatus** *(string) --*

        The status of parameter updates.

      - **NodeIdsToReboot** *(list) --*

        The node IDs of one or more nodes to be rebooted.

        - *(string) --*

    - **SSEDescription** *(dict) --*

      The description of the server-side encryption status on the specified DAX cluster.

      - **Status** *(string) --*

        The current state of server-side encryption:

        * ``ENABLING`` - Server-side encryption is being enabled.

        * ``ENABLED`` - Server-side encryption is enabled.

        * ``DISABLING`` - Server-side encryption is being disabled.

        * ``DISABLED`` - Server-side encryption is disabled.
    """


_ClientUpdateClusterResponseTypeDef = TypedDict(
    "_ClientUpdateClusterResponseTypeDef",
    {"Cluster": ClientUpdateClusterResponseClusterTypeDef},
    total=False,
)


class ClientUpdateClusterResponseTypeDef(_ClientUpdateClusterResponseTypeDef):
    """
    Type definition for `ClientUpdateCluster` `Response`

    - **Cluster** *(dict) --*

      A description of the DAX cluster, after it has been modified.

      - **ClusterName** *(string) --*

        The name of the DAX cluster.

      - **Description** *(string) --*

        The description of the cluster.

      - **ClusterArn** *(string) --*

        The Amazon Resource Name (ARN) that uniquely identifies the cluster.

      - **TotalNodes** *(integer) --*

        The total number of nodes in the cluster.

      - **ActiveNodes** *(integer) --*

        The number of nodes in the cluster that are active (i.e., capable of serving requests).

      - **NodeType** *(string) --*

        The node type for the nodes in the cluster. (All nodes in a DAX cluster are of the same
        type.)

      - **Status** *(string) --*

        The current status of the cluster.

      - **ClusterDiscoveryEndpoint** *(dict) --*

        The configuration endpoint for this DAX cluster, consisting of a DNS name and a port
        number. Client applications can specify this endpoint, rather than an individual node
        endpoint, and allow the DAX client software to intelligently route requests and responses
        to nodes in the DAX cluster.

        - **Address** *(string) --*

          The DNS hostname of the endpoint.

        - **Port** *(integer) --*

          The port number that applications should use to connect to the endpoint.

      - **NodeIdsToRemove** *(list) --*

        A list of nodes to be removed from the cluster.

        - *(string) --*

      - **Nodes** *(list) --*

        A list of nodes that are currently in the cluster.

        - *(dict) --*

          Represents an individual node within a DAX cluster.

          - **NodeId** *(string) --*

            A system-generated identifier for the node.

          - **Endpoint** *(dict) --*

            The endpoint for the node, consisting of a DNS name and a port number. Client
            applications can connect directly to a node endpoint, if desired (as an alternative to
            allowing DAX client software to intelligently route requests and responses to nodes in
            the DAX cluster.

            - **Address** *(string) --*

              The DNS hostname of the endpoint.

            - **Port** *(integer) --*

              The port number that applications should use to connect to the endpoint.

          - **NodeCreateTime** *(datetime) --*

            The date and time (in UNIX epoch format) when the node was launched.

          - **AvailabilityZone** *(string) --*

            The Availability Zone (AZ) in which the node has been deployed.

          - **NodeStatus** *(string) --*

            The current status of the node. For example: ``available`` .

          - **ParameterGroupStatus** *(string) --*

            The status of the parameter group associated with this node. For example, ``in-sync`` .

      - **PreferredMaintenanceWindow** *(string) --*

        A range of time when maintenance of DAX cluster software will be performed. For example:
        ``sun:01:00-sun:09:00`` . Cluster maintenance normally takes less than 30 minutes, and is
        performed automatically within the maintenance window.

      - **NotificationConfiguration** *(dict) --*

        Describes a notification topic and its status. Notification topics are used for publishing
        DAX events to subscribers using Amazon Simple Notification Service (SNS).

        - **TopicArn** *(string) --*

          The Amazon Resource Name (ARN) that identifies the topic.

        - **TopicStatus** *(string) --*

          The current state of the topic.

      - **SubnetGroup** *(string) --*

        The subnet group where the DAX cluster is running.

      - **SecurityGroups** *(list) --*

        A list of security groups, and the status of each, for the nodes in the cluster.

        - *(dict) --*

          An individual VPC security group and its status.

          - **SecurityGroupIdentifier** *(string) --*

            The unique ID for this security group.

          - **Status** *(string) --*

            The status of this security group.

      - **IamRoleArn** *(string) --*

        A valid Amazon Resource Name (ARN) that identifies an IAM role. At runtime, DAX will assume
        this role and use the role's permissions to access DynamoDB on your behalf.

      - **ParameterGroup** *(dict) --*

        The parameter group being used by nodes in the cluster.

        - **ParameterGroupName** *(string) --*

          The name of the parameter group.

        - **ParameterApplyStatus** *(string) --*

          The status of parameter updates.

        - **NodeIdsToReboot** *(list) --*

          The node IDs of one or more nodes to be rebooted.

          - *(string) --*

      - **SSEDescription** *(dict) --*

        The description of the server-side encryption status on the specified DAX cluster.

        - **Status** *(string) --*

          The current state of server-side encryption:

          * ``ENABLING`` - Server-side encryption is being enabled.

          * ``ENABLED`` - Server-side encryption is enabled.

          * ``DISABLING`` - Server-side encryption is being disabled.

          * ``DISABLED`` - Server-side encryption is disabled.
    """


_ClientUpdateParameterGroupParameterNameValuesTypeDef = TypedDict(
    "_ClientUpdateParameterGroupParameterNameValuesTypeDef",
    {"ParameterName": str, "ParameterValue": str},
    total=False,
)


class ClientUpdateParameterGroupParameterNameValuesTypeDef(
    _ClientUpdateParameterGroupParameterNameValuesTypeDef
):
    """
    Type definition for `ClientUpdateParameterGroup` `ParameterNameValues`

    An individual DAX parameter.

    - **ParameterName** *(string) --*

      The name of the parameter.

    - **ParameterValue** *(string) --*

      The value of the parameter.
    """


_ClientUpdateParameterGroupResponseParameterGroupTypeDef = TypedDict(
    "_ClientUpdateParameterGroupResponseParameterGroupTypeDef",
    {"ParameterGroupName": str, "Description": str},
    total=False,
)


class ClientUpdateParameterGroupResponseParameterGroupTypeDef(
    _ClientUpdateParameterGroupResponseParameterGroupTypeDef
):
    """
    Type definition for `ClientUpdateParameterGroupResponse` `ParameterGroup`

    The parameter group that has been modified.

    - **ParameterGroupName** *(string) --*

      The name of the parameter group.

    - **Description** *(string) --*

      A description of the parameter group.
    """


_ClientUpdateParameterGroupResponseTypeDef = TypedDict(
    "_ClientUpdateParameterGroupResponseTypeDef",
    {"ParameterGroup": ClientUpdateParameterGroupResponseParameterGroupTypeDef},
    total=False,
)


class ClientUpdateParameterGroupResponseTypeDef(
    _ClientUpdateParameterGroupResponseTypeDef
):
    """
    Type definition for `ClientUpdateParameterGroup` `Response`

    - **ParameterGroup** *(dict) --*

      The parameter group that has been modified.

      - **ParameterGroupName** *(string) --*

        The name of the parameter group.

      - **Description** *(string) --*

        A description of the parameter group.
    """


_ClientUpdateSubnetGroupResponseSubnetGroupSubnetsTypeDef = TypedDict(
    "_ClientUpdateSubnetGroupResponseSubnetGroupSubnetsTypeDef",
    {"SubnetIdentifier": str, "SubnetAvailabilityZone": str},
    total=False,
)


class ClientUpdateSubnetGroupResponseSubnetGroupSubnetsTypeDef(
    _ClientUpdateSubnetGroupResponseSubnetGroupSubnetsTypeDef
):
    """
    Type definition for `ClientUpdateSubnetGroupResponseSubnetGroup` `Subnets`

    Represents the subnet associated with a DAX cluster. This parameter refers to subnets
    defined in Amazon Virtual Private Cloud (Amazon VPC) and used with DAX.

    - **SubnetIdentifier** *(string) --*

      The system-assigned identifier for the subnet.

    - **SubnetAvailabilityZone** *(string) --*

      The Availability Zone (AZ) for the subnet.
    """


_ClientUpdateSubnetGroupResponseSubnetGroupTypeDef = TypedDict(
    "_ClientUpdateSubnetGroupResponseSubnetGroupTypeDef",
    {
        "SubnetGroupName": str,
        "Description": str,
        "VpcId": str,
        "Subnets": List[ClientUpdateSubnetGroupResponseSubnetGroupSubnetsTypeDef],
    },
    total=False,
)


class ClientUpdateSubnetGroupResponseSubnetGroupTypeDef(
    _ClientUpdateSubnetGroupResponseSubnetGroupTypeDef
):
    """
    Type definition for `ClientUpdateSubnetGroupResponse` `SubnetGroup`

    The subnet group that has been modified.

    - **SubnetGroupName** *(string) --*

      The name of the subnet group.

    - **Description** *(string) --*

      The description of the subnet group.

    - **VpcId** *(string) --*

      The Amazon Virtual Private Cloud identifier (VPC ID) of the subnet group.

    - **Subnets** *(list) --*

      A list of subnets associated with the subnet group.

      - *(dict) --*

        Represents the subnet associated with a DAX cluster. This parameter refers to subnets
        defined in Amazon Virtual Private Cloud (Amazon VPC) and used with DAX.

        - **SubnetIdentifier** *(string) --*

          The system-assigned identifier for the subnet.

        - **SubnetAvailabilityZone** *(string) --*

          The Availability Zone (AZ) for the subnet.
    """


_ClientUpdateSubnetGroupResponseTypeDef = TypedDict(
    "_ClientUpdateSubnetGroupResponseTypeDef",
    {"SubnetGroup": ClientUpdateSubnetGroupResponseSubnetGroupTypeDef},
    total=False,
)


class ClientUpdateSubnetGroupResponseTypeDef(_ClientUpdateSubnetGroupResponseTypeDef):
    """
    Type definition for `ClientUpdateSubnetGroup` `Response`

    - **SubnetGroup** *(dict) --*

      The subnet group that has been modified.

      - **SubnetGroupName** *(string) --*

        The name of the subnet group.

      - **Description** *(string) --*

        The description of the subnet group.

      - **VpcId** *(string) --*

        The Amazon Virtual Private Cloud identifier (VPC ID) of the subnet group.

      - **Subnets** *(list) --*

        A list of subnets associated with the subnet group.

        - *(dict) --*

          Represents the subnet associated with a DAX cluster. This parameter refers to subnets
          defined in Amazon Virtual Private Cloud (Amazon VPC) and used with DAX.

          - **SubnetIdentifier** *(string) --*

            The system-assigned identifier for the subnet.

          - **SubnetAvailabilityZone** *(string) --*

            The Availability Zone (AZ) for the subnet.
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


_DescribeClustersPaginateResponseClustersClusterDiscoveryEndpointTypeDef = TypedDict(
    "_DescribeClustersPaginateResponseClustersClusterDiscoveryEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class DescribeClustersPaginateResponseClustersClusterDiscoveryEndpointTypeDef(
    _DescribeClustersPaginateResponseClustersClusterDiscoveryEndpointTypeDef
):
    """
    Type definition for `DescribeClustersPaginateResponseClusters` `ClusterDiscoveryEndpoint`

    The configuration endpoint for this DAX cluster, consisting of a DNS name and a port
    number. Client applications can specify this endpoint, rather than an individual node
    endpoint, and allow the DAX client software to intelligently route requests and responses
    to nodes in the DAX cluster.

    - **Address** *(string) --*

      The DNS hostname of the endpoint.

    - **Port** *(integer) --*

      The port number that applications should use to connect to the endpoint.
    """


_DescribeClustersPaginateResponseClustersNodesEndpointTypeDef = TypedDict(
    "_DescribeClustersPaginateResponseClustersNodesEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class DescribeClustersPaginateResponseClustersNodesEndpointTypeDef(
    _DescribeClustersPaginateResponseClustersNodesEndpointTypeDef
):
    """
    Type definition for `DescribeClustersPaginateResponseClustersNodes` `Endpoint`

    The endpoint for the node, consisting of a DNS name and a port number. Client
    applications can connect directly to a node endpoint, if desired (as an alternative
    to allowing DAX client software to intelligently route requests and responses to
    nodes in the DAX cluster.

    - **Address** *(string) --*

      The DNS hostname of the endpoint.

    - **Port** *(integer) --*

      The port number that applications should use to connect to the endpoint.
    """


_DescribeClustersPaginateResponseClustersNodesTypeDef = TypedDict(
    "_DescribeClustersPaginateResponseClustersNodesTypeDef",
    {
        "NodeId": str,
        "Endpoint": DescribeClustersPaginateResponseClustersNodesEndpointTypeDef,
        "NodeCreateTime": datetime,
        "AvailabilityZone": str,
        "NodeStatus": str,
        "ParameterGroupStatus": str,
    },
    total=False,
)


class DescribeClustersPaginateResponseClustersNodesTypeDef(
    _DescribeClustersPaginateResponseClustersNodesTypeDef
):
    """
    Type definition for `DescribeClustersPaginateResponseClusters` `Nodes`

    Represents an individual node within a DAX cluster.

    - **NodeId** *(string) --*

      A system-generated identifier for the node.

    - **Endpoint** *(dict) --*

      The endpoint for the node, consisting of a DNS name and a port number. Client
      applications can connect directly to a node endpoint, if desired (as an alternative
      to allowing DAX client software to intelligently route requests and responses to
      nodes in the DAX cluster.

      - **Address** *(string) --*

        The DNS hostname of the endpoint.

      - **Port** *(integer) --*

        The port number that applications should use to connect to the endpoint.

    - **NodeCreateTime** *(datetime) --*

      The date and time (in UNIX epoch format) when the node was launched.

    - **AvailabilityZone** *(string) --*

      The Availability Zone (AZ) in which the node has been deployed.

    - **NodeStatus** *(string) --*

      The current status of the node. For example: ``available`` .

    - **ParameterGroupStatus** *(string) --*

      The status of the parameter group associated with this node. For example, ``in-sync``
      .
    """


_DescribeClustersPaginateResponseClustersNotificationConfigurationTypeDef = TypedDict(
    "_DescribeClustersPaginateResponseClustersNotificationConfigurationTypeDef",
    {"TopicArn": str, "TopicStatus": str},
    total=False,
)


class DescribeClustersPaginateResponseClustersNotificationConfigurationTypeDef(
    _DescribeClustersPaginateResponseClustersNotificationConfigurationTypeDef
):
    """
    Type definition for `DescribeClustersPaginateResponseClusters` `NotificationConfiguration`

    Describes a notification topic and its status. Notification topics are used for
    publishing DAX events to subscribers using Amazon Simple Notification Service (SNS).

    - **TopicArn** *(string) --*

      The Amazon Resource Name (ARN) that identifies the topic.

    - **TopicStatus** *(string) --*

      The current state of the topic.
    """


_DescribeClustersPaginateResponseClustersParameterGroupTypeDef = TypedDict(
    "_DescribeClustersPaginateResponseClustersParameterGroupTypeDef",
    {
        "ParameterGroupName": str,
        "ParameterApplyStatus": str,
        "NodeIdsToReboot": List[str],
    },
    total=False,
)


class DescribeClustersPaginateResponseClustersParameterGroupTypeDef(
    _DescribeClustersPaginateResponseClustersParameterGroupTypeDef
):
    """
    Type definition for `DescribeClustersPaginateResponseClusters` `ParameterGroup`

    The parameter group being used by nodes in the cluster.

    - **ParameterGroupName** *(string) --*

      The name of the parameter group.

    - **ParameterApplyStatus** *(string) --*

      The status of parameter updates.

    - **NodeIdsToReboot** *(list) --*

      The node IDs of one or more nodes to be rebooted.

      - *(string) --*
    """


_DescribeClustersPaginateResponseClustersSSEDescriptionTypeDef = TypedDict(
    "_DescribeClustersPaginateResponseClustersSSEDescriptionTypeDef",
    {"Status": str},
    total=False,
)


class DescribeClustersPaginateResponseClustersSSEDescriptionTypeDef(
    _DescribeClustersPaginateResponseClustersSSEDescriptionTypeDef
):
    """
    Type definition for `DescribeClustersPaginateResponseClusters` `SSEDescription`

    The description of the server-side encryption status on the specified DAX cluster.

    - **Status** *(string) --*

      The current state of server-side encryption:

      * ``ENABLING`` - Server-side encryption is being enabled.

      * ``ENABLED`` - Server-side encryption is enabled.

      * ``DISABLING`` - Server-side encryption is being disabled.

      * ``DISABLED`` - Server-side encryption is disabled.
    """


_DescribeClustersPaginateResponseClustersSecurityGroupsTypeDef = TypedDict(
    "_DescribeClustersPaginateResponseClustersSecurityGroupsTypeDef",
    {"SecurityGroupIdentifier": str, "Status": str},
    total=False,
)


class DescribeClustersPaginateResponseClustersSecurityGroupsTypeDef(
    _DescribeClustersPaginateResponseClustersSecurityGroupsTypeDef
):
    """
    Type definition for `DescribeClustersPaginateResponseClusters` `SecurityGroups`

    An individual VPC security group and its status.

    - **SecurityGroupIdentifier** *(string) --*

      The unique ID for this security group.

    - **Status** *(string) --*

      The status of this security group.
    """


_DescribeClustersPaginateResponseClustersTypeDef = TypedDict(
    "_DescribeClustersPaginateResponseClustersTypeDef",
    {
        "ClusterName": str,
        "Description": str,
        "ClusterArn": str,
        "TotalNodes": int,
        "ActiveNodes": int,
        "NodeType": str,
        "Status": str,
        "ClusterDiscoveryEndpoint": DescribeClustersPaginateResponseClustersClusterDiscoveryEndpointTypeDef,
        "NodeIdsToRemove": List[str],
        "Nodes": List[DescribeClustersPaginateResponseClustersNodesTypeDef],
        "PreferredMaintenanceWindow": str,
        "NotificationConfiguration": DescribeClustersPaginateResponseClustersNotificationConfigurationTypeDef,
        "SubnetGroup": str,
        "SecurityGroups": List[
            DescribeClustersPaginateResponseClustersSecurityGroupsTypeDef
        ],
        "IamRoleArn": str,
        "ParameterGroup": DescribeClustersPaginateResponseClustersParameterGroupTypeDef,
        "SSEDescription": DescribeClustersPaginateResponseClustersSSEDescriptionTypeDef,
    },
    total=False,
)


class DescribeClustersPaginateResponseClustersTypeDef(
    _DescribeClustersPaginateResponseClustersTypeDef
):
    """
    Type definition for `DescribeClustersPaginateResponse` `Clusters`

    Contains all of the attributes of a specific DAX cluster.

    - **ClusterName** *(string) --*

      The name of the DAX cluster.

    - **Description** *(string) --*

      The description of the cluster.

    - **ClusterArn** *(string) --*

      The Amazon Resource Name (ARN) that uniquely identifies the cluster.

    - **TotalNodes** *(integer) --*

      The total number of nodes in the cluster.

    - **ActiveNodes** *(integer) --*

      The number of nodes in the cluster that are active (i.e., capable of serving requests).

    - **NodeType** *(string) --*

      The node type for the nodes in the cluster. (All nodes in a DAX cluster are of the same
      type.)

    - **Status** *(string) --*

      The current status of the cluster.

    - **ClusterDiscoveryEndpoint** *(dict) --*

      The configuration endpoint for this DAX cluster, consisting of a DNS name and a port
      number. Client applications can specify this endpoint, rather than an individual node
      endpoint, and allow the DAX client software to intelligently route requests and responses
      to nodes in the DAX cluster.

      - **Address** *(string) --*

        The DNS hostname of the endpoint.

      - **Port** *(integer) --*

        The port number that applications should use to connect to the endpoint.

    - **NodeIdsToRemove** *(list) --*

      A list of nodes to be removed from the cluster.

      - *(string) --*

    - **Nodes** *(list) --*

      A list of nodes that are currently in the cluster.

      - *(dict) --*

        Represents an individual node within a DAX cluster.

        - **NodeId** *(string) --*

          A system-generated identifier for the node.

        - **Endpoint** *(dict) --*

          The endpoint for the node, consisting of a DNS name and a port number. Client
          applications can connect directly to a node endpoint, if desired (as an alternative
          to allowing DAX client software to intelligently route requests and responses to
          nodes in the DAX cluster.

          - **Address** *(string) --*

            The DNS hostname of the endpoint.

          - **Port** *(integer) --*

            The port number that applications should use to connect to the endpoint.

        - **NodeCreateTime** *(datetime) --*

          The date and time (in UNIX epoch format) when the node was launched.

        - **AvailabilityZone** *(string) --*

          The Availability Zone (AZ) in which the node has been deployed.

        - **NodeStatus** *(string) --*

          The current status of the node. For example: ``available`` .

        - **ParameterGroupStatus** *(string) --*

          The status of the parameter group associated with this node. For example, ``in-sync``
          .

    - **PreferredMaintenanceWindow** *(string) --*

      A range of time when maintenance of DAX cluster software will be performed. For example:
      ``sun:01:00-sun:09:00`` . Cluster maintenance normally takes less than 30 minutes, and is
      performed automatically within the maintenance window.

    - **NotificationConfiguration** *(dict) --*

      Describes a notification topic and its status. Notification topics are used for
      publishing DAX events to subscribers using Amazon Simple Notification Service (SNS).

      - **TopicArn** *(string) --*

        The Amazon Resource Name (ARN) that identifies the topic.

      - **TopicStatus** *(string) --*

        The current state of the topic.

    - **SubnetGroup** *(string) --*

      The subnet group where the DAX cluster is running.

    - **SecurityGroups** *(list) --*

      A list of security groups, and the status of each, for the nodes in the cluster.

      - *(dict) --*

        An individual VPC security group and its status.

        - **SecurityGroupIdentifier** *(string) --*

          The unique ID for this security group.

        - **Status** *(string) --*

          The status of this security group.

    - **IamRoleArn** *(string) --*

      A valid Amazon Resource Name (ARN) that identifies an IAM role. At runtime, DAX will
      assume this role and use the role's permissions to access DynamoDB on your behalf.

    - **ParameterGroup** *(dict) --*

      The parameter group being used by nodes in the cluster.

      - **ParameterGroupName** *(string) --*

        The name of the parameter group.

      - **ParameterApplyStatus** *(string) --*

        The status of parameter updates.

      - **NodeIdsToReboot** *(list) --*

        The node IDs of one or more nodes to be rebooted.

        - *(string) --*

    - **SSEDescription** *(dict) --*

      The description of the server-side encryption status on the specified DAX cluster.

      - **Status** *(string) --*

        The current state of server-side encryption:

        * ``ENABLING`` - Server-side encryption is being enabled.

        * ``ENABLED`` - Server-side encryption is enabled.

        * ``DISABLING`` - Server-side encryption is being disabled.

        * ``DISABLED`` - Server-side encryption is disabled.
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

      The descriptions of your DAX clusters, in response to a *DescribeClusters* request.

      - *(dict) --*

        Contains all of the attributes of a specific DAX cluster.

        - **ClusterName** *(string) --*

          The name of the DAX cluster.

        - **Description** *(string) --*

          The description of the cluster.

        - **ClusterArn** *(string) --*

          The Amazon Resource Name (ARN) that uniquely identifies the cluster.

        - **TotalNodes** *(integer) --*

          The total number of nodes in the cluster.

        - **ActiveNodes** *(integer) --*

          The number of nodes in the cluster that are active (i.e., capable of serving requests).

        - **NodeType** *(string) --*

          The node type for the nodes in the cluster. (All nodes in a DAX cluster are of the same
          type.)

        - **Status** *(string) --*

          The current status of the cluster.

        - **ClusterDiscoveryEndpoint** *(dict) --*

          The configuration endpoint for this DAX cluster, consisting of a DNS name and a port
          number. Client applications can specify this endpoint, rather than an individual node
          endpoint, and allow the DAX client software to intelligently route requests and responses
          to nodes in the DAX cluster.

          - **Address** *(string) --*

            The DNS hostname of the endpoint.

          - **Port** *(integer) --*

            The port number that applications should use to connect to the endpoint.

        - **NodeIdsToRemove** *(list) --*

          A list of nodes to be removed from the cluster.

          - *(string) --*

        - **Nodes** *(list) --*

          A list of nodes that are currently in the cluster.

          - *(dict) --*

            Represents an individual node within a DAX cluster.

            - **NodeId** *(string) --*

              A system-generated identifier for the node.

            - **Endpoint** *(dict) --*

              The endpoint for the node, consisting of a DNS name and a port number. Client
              applications can connect directly to a node endpoint, if desired (as an alternative
              to allowing DAX client software to intelligently route requests and responses to
              nodes in the DAX cluster.

              - **Address** *(string) --*

                The DNS hostname of the endpoint.

              - **Port** *(integer) --*

                The port number that applications should use to connect to the endpoint.

            - **NodeCreateTime** *(datetime) --*

              The date and time (in UNIX epoch format) when the node was launched.

            - **AvailabilityZone** *(string) --*

              The Availability Zone (AZ) in which the node has been deployed.

            - **NodeStatus** *(string) --*

              The current status of the node. For example: ``available`` .

            - **ParameterGroupStatus** *(string) --*

              The status of the parameter group associated with this node. For example, ``in-sync``
              .

        - **PreferredMaintenanceWindow** *(string) --*

          A range of time when maintenance of DAX cluster software will be performed. For example:
          ``sun:01:00-sun:09:00`` . Cluster maintenance normally takes less than 30 minutes, and is
          performed automatically within the maintenance window.

        - **NotificationConfiguration** *(dict) --*

          Describes a notification topic and its status. Notification topics are used for
          publishing DAX events to subscribers using Amazon Simple Notification Service (SNS).

          - **TopicArn** *(string) --*

            The Amazon Resource Name (ARN) that identifies the topic.

          - **TopicStatus** *(string) --*

            The current state of the topic.

        - **SubnetGroup** *(string) --*

          The subnet group where the DAX cluster is running.

        - **SecurityGroups** *(list) --*

          A list of security groups, and the status of each, for the nodes in the cluster.

          - *(dict) --*

            An individual VPC security group and its status.

            - **SecurityGroupIdentifier** *(string) --*

              The unique ID for this security group.

            - **Status** *(string) --*

              The status of this security group.

        - **IamRoleArn** *(string) --*

          A valid Amazon Resource Name (ARN) that identifies an IAM role. At runtime, DAX will
          assume this role and use the role's permissions to access DynamoDB on your behalf.

        - **ParameterGroup** *(dict) --*

          The parameter group being used by nodes in the cluster.

          - **ParameterGroupName** *(string) --*

            The name of the parameter group.

          - **ParameterApplyStatus** *(string) --*

            The status of parameter updates.

          - **NodeIdsToReboot** *(list) --*

            The node IDs of one or more nodes to be rebooted.

            - *(string) --*

        - **SSEDescription** *(dict) --*

          The description of the server-side encryption status on the specified DAX cluster.

          - **Status** *(string) --*

            The current state of server-side encryption:

            * ``ENABLING`` - Server-side encryption is being enabled.

            * ``ENABLED`` - Server-side encryption is enabled.

            * ``DISABLING`` - Server-side encryption is being disabled.

            * ``DISABLED`` - Server-side encryption is disabled.
    """


_DescribeDefaultParametersPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeDefaultParametersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeDefaultParametersPaginatePaginationConfigTypeDef(
    _DescribeDefaultParametersPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeDefaultParametersPaginate` `PaginationConfig`

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


_DescribeDefaultParametersPaginateResponseParametersNodeTypeSpecificValuesTypeDef = TypedDict(
    "_DescribeDefaultParametersPaginateResponseParametersNodeTypeSpecificValuesTypeDef",
    {"NodeType": str, "Value": str},
    total=False,
)


class DescribeDefaultParametersPaginateResponseParametersNodeTypeSpecificValuesTypeDef(
    _DescribeDefaultParametersPaginateResponseParametersNodeTypeSpecificValuesTypeDef
):
    """
    Type definition for `DescribeDefaultParametersPaginateResponseParameters` `NodeTypeSpecificValues`

    Represents a parameter value that is applicable to a particular node type.

    - **NodeType** *(string) --*

      A node type to which the parameter value applies.

    - **Value** *(string) --*

      The parameter value for this node type.
    """


_DescribeDefaultParametersPaginateResponseParametersTypeDef = TypedDict(
    "_DescribeDefaultParametersPaginateResponseParametersTypeDef",
    {
        "ParameterName": str,
        "ParameterType": str,
        "ParameterValue": str,
        "NodeTypeSpecificValues": List[
            DescribeDefaultParametersPaginateResponseParametersNodeTypeSpecificValuesTypeDef
        ],
        "Description": str,
        "Source": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": str,
        "ChangeType": str,
    },
    total=False,
)


class DescribeDefaultParametersPaginateResponseParametersTypeDef(
    _DescribeDefaultParametersPaginateResponseParametersTypeDef
):
    """
    Type definition for `DescribeDefaultParametersPaginateResponse` `Parameters`

    Describes an individual setting that controls some aspect of DAX behavior.

    - **ParameterName** *(string) --*

      The name of the parameter.

    - **ParameterType** *(string) --*

      Determines whether the parameter can be applied to any nodes, or only nodes of a
      particular type.

    - **ParameterValue** *(string) --*

      The value for the parameter.

    - **NodeTypeSpecificValues** *(list) --*

      A list of node types, and specific parameter values for each node.

      - *(dict) --*

        Represents a parameter value that is applicable to a particular node type.

        - **NodeType** *(string) --*

          A node type to which the parameter value applies.

        - **Value** *(string) --*

          The parameter value for this node type.

    - **Description** *(string) --*

      A description of the parameter

    - **Source** *(string) --*

      How the parameter is defined. For example, ``system`` denotes a system-defined parameter.

    - **DataType** *(string) --*

      The data type of the parameter. For example, ``integer`` :

    - **AllowedValues** *(string) --*

      A range of values within which the parameter can be set.

    - **IsModifiable** *(string) --*

      Whether the customer is allowed to modify the parameter.

    - **ChangeType** *(string) --*

      The conditions under which changes to this parameter can be applied. For example,
      ``requires-reboot`` indicates that a new value for this parameter will only take effect
      if a node is rebooted.
    """


_DescribeDefaultParametersPaginateResponseTypeDef = TypedDict(
    "_DescribeDefaultParametersPaginateResponseTypeDef",
    {"Parameters": List[DescribeDefaultParametersPaginateResponseParametersTypeDef]},
    total=False,
)


class DescribeDefaultParametersPaginateResponseTypeDef(
    _DescribeDefaultParametersPaginateResponseTypeDef
):
    """
    Type definition for `DescribeDefaultParametersPaginate` `Response`

    - **Parameters** *(list) --*

      A list of parameters. Each element in the list represents one parameter.

      - *(dict) --*

        Describes an individual setting that controls some aspect of DAX behavior.

        - **ParameterName** *(string) --*

          The name of the parameter.

        - **ParameterType** *(string) --*

          Determines whether the parameter can be applied to any nodes, or only nodes of a
          particular type.

        - **ParameterValue** *(string) --*

          The value for the parameter.

        - **NodeTypeSpecificValues** *(list) --*

          A list of node types, and specific parameter values for each node.

          - *(dict) --*

            Represents a parameter value that is applicable to a particular node type.

            - **NodeType** *(string) --*

              A node type to which the parameter value applies.

            - **Value** *(string) --*

              The parameter value for this node type.

        - **Description** *(string) --*

          A description of the parameter

        - **Source** *(string) --*

          How the parameter is defined. For example, ``system`` denotes a system-defined parameter.

        - **DataType** *(string) --*

          The data type of the parameter. For example, ``integer`` :

        - **AllowedValues** *(string) --*

          A range of values within which the parameter can be set.

        - **IsModifiable** *(string) --*

          Whether the customer is allowed to modify the parameter.

        - **ChangeType** *(string) --*

          The conditions under which changes to this parameter can be applied. For example,
          ``requires-reboot`` indicates that a new value for this parameter will only take effect
          if a node is rebooted.
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
    {"SourceName": str, "SourceType": str, "Message": str, "Date": datetime},
    total=False,
)


class DescribeEventsPaginateResponseEventsTypeDef(
    _DescribeEventsPaginateResponseEventsTypeDef
):
    """
    Type definition for `DescribeEventsPaginateResponse` `Events`

    Represents a single occurrence of something interesting within the system. Some examples of
    events are creating a DAX cluster, adding or removing a node, or rebooting a node.

    - **SourceName** *(string) --*

      The source of the event. For example, if the event occurred at the node level, the source
      would be the node ID.

    - **SourceType** *(string) --*

      Specifies the origin of this event - a cluster, a parameter group, a node ID, etc.

    - **Message** *(string) --*

      A user-defined message associated with the event.

    - **Date** *(datetime) --*

      The date and time when the event occurred.
    """


_DescribeEventsPaginateResponseTypeDef = TypedDict(
    "_DescribeEventsPaginateResponseTypeDef",
    {"Events": List[DescribeEventsPaginateResponseEventsTypeDef]},
    total=False,
)


class DescribeEventsPaginateResponseTypeDef(_DescribeEventsPaginateResponseTypeDef):
    """
    Type definition for `DescribeEventsPaginate` `Response`

    - **Events** *(list) --*

      An array of events. Each element in the array represents one event.

      - *(dict) --*

        Represents a single occurrence of something interesting within the system. Some examples of
        events are creating a DAX cluster, adding or removing a node, or rebooting a node.

        - **SourceName** *(string) --*

          The source of the event. For example, if the event occurred at the node level, the source
          would be the node ID.

        - **SourceType** *(string) --*

          Specifies the origin of this event - a cluster, a parameter group, a node ID, etc.

        - **Message** *(string) --*

          A user-defined message associated with the event.

        - **Date** *(datetime) --*

          The date and time when the event occurred.
    """


_DescribeParameterGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeParameterGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeParameterGroupsPaginatePaginationConfigTypeDef(
    _DescribeParameterGroupsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeParameterGroupsPaginate` `PaginationConfig`

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


_DescribeParameterGroupsPaginateResponseParameterGroupsTypeDef = TypedDict(
    "_DescribeParameterGroupsPaginateResponseParameterGroupsTypeDef",
    {"ParameterGroupName": str, "Description": str},
    total=False,
)


class DescribeParameterGroupsPaginateResponseParameterGroupsTypeDef(
    _DescribeParameterGroupsPaginateResponseParameterGroupsTypeDef
):
    """
    Type definition for `DescribeParameterGroupsPaginateResponse` `ParameterGroups`

    A named set of parameters that are applied to all of the nodes in a DAX cluster.

    - **ParameterGroupName** *(string) --*

      The name of the parameter group.

    - **Description** *(string) --*

      A description of the parameter group.
    """


_DescribeParameterGroupsPaginateResponseTypeDef = TypedDict(
    "_DescribeParameterGroupsPaginateResponseTypeDef",
    {
        "ParameterGroups": List[
            DescribeParameterGroupsPaginateResponseParameterGroupsTypeDef
        ]
    },
    total=False,
)


class DescribeParameterGroupsPaginateResponseTypeDef(
    _DescribeParameterGroupsPaginateResponseTypeDef
):
    """
    Type definition for `DescribeParameterGroupsPaginate` `Response`

    - **ParameterGroups** *(list) --*

      An array of parameter groups. Each element in the array represents one parameter group.

      - *(dict) --*

        A named set of parameters that are applied to all of the nodes in a DAX cluster.

        - **ParameterGroupName** *(string) --*

          The name of the parameter group.

        - **Description** *(string) --*

          A description of the parameter group.
    """


_DescribeParametersPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeParametersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeParametersPaginatePaginationConfigTypeDef(
    _DescribeParametersPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeParametersPaginate` `PaginationConfig`

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


_DescribeParametersPaginateResponseParametersNodeTypeSpecificValuesTypeDef = TypedDict(
    "_DescribeParametersPaginateResponseParametersNodeTypeSpecificValuesTypeDef",
    {"NodeType": str, "Value": str},
    total=False,
)


class DescribeParametersPaginateResponseParametersNodeTypeSpecificValuesTypeDef(
    _DescribeParametersPaginateResponseParametersNodeTypeSpecificValuesTypeDef
):
    """
    Type definition for `DescribeParametersPaginateResponseParameters` `NodeTypeSpecificValues`

    Represents a parameter value that is applicable to a particular node type.

    - **NodeType** *(string) --*

      A node type to which the parameter value applies.

    - **Value** *(string) --*

      The parameter value for this node type.
    """


_DescribeParametersPaginateResponseParametersTypeDef = TypedDict(
    "_DescribeParametersPaginateResponseParametersTypeDef",
    {
        "ParameterName": str,
        "ParameterType": str,
        "ParameterValue": str,
        "NodeTypeSpecificValues": List[
            DescribeParametersPaginateResponseParametersNodeTypeSpecificValuesTypeDef
        ],
        "Description": str,
        "Source": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": str,
        "ChangeType": str,
    },
    total=False,
)


class DescribeParametersPaginateResponseParametersTypeDef(
    _DescribeParametersPaginateResponseParametersTypeDef
):
    """
    Type definition for `DescribeParametersPaginateResponse` `Parameters`

    Describes an individual setting that controls some aspect of DAX behavior.

    - **ParameterName** *(string) --*

      The name of the parameter.

    - **ParameterType** *(string) --*

      Determines whether the parameter can be applied to any nodes, or only nodes of a
      particular type.

    - **ParameterValue** *(string) --*

      The value for the parameter.

    - **NodeTypeSpecificValues** *(list) --*

      A list of node types, and specific parameter values for each node.

      - *(dict) --*

        Represents a parameter value that is applicable to a particular node type.

        - **NodeType** *(string) --*

          A node type to which the parameter value applies.

        - **Value** *(string) --*

          The parameter value for this node type.

    - **Description** *(string) --*

      A description of the parameter

    - **Source** *(string) --*

      How the parameter is defined. For example, ``system`` denotes a system-defined parameter.

    - **DataType** *(string) --*

      The data type of the parameter. For example, ``integer`` :

    - **AllowedValues** *(string) --*

      A range of values within which the parameter can be set.

    - **IsModifiable** *(string) --*

      Whether the customer is allowed to modify the parameter.

    - **ChangeType** *(string) --*

      The conditions under which changes to this parameter can be applied. For example,
      ``requires-reboot`` indicates that a new value for this parameter will only take effect
      if a node is rebooted.
    """


_DescribeParametersPaginateResponseTypeDef = TypedDict(
    "_DescribeParametersPaginateResponseTypeDef",
    {"Parameters": List[DescribeParametersPaginateResponseParametersTypeDef]},
    total=False,
)


class DescribeParametersPaginateResponseTypeDef(
    _DescribeParametersPaginateResponseTypeDef
):
    """
    Type definition for `DescribeParametersPaginate` `Response`

    - **Parameters** *(list) --*

      A list of parameters within a parameter group. Each element in the list represents one
      parameter.

      - *(dict) --*

        Describes an individual setting that controls some aspect of DAX behavior.

        - **ParameterName** *(string) --*

          The name of the parameter.

        - **ParameterType** *(string) --*

          Determines whether the parameter can be applied to any nodes, or only nodes of a
          particular type.

        - **ParameterValue** *(string) --*

          The value for the parameter.

        - **NodeTypeSpecificValues** *(list) --*

          A list of node types, and specific parameter values for each node.

          - *(dict) --*

            Represents a parameter value that is applicable to a particular node type.

            - **NodeType** *(string) --*

              A node type to which the parameter value applies.

            - **Value** *(string) --*

              The parameter value for this node type.

        - **Description** *(string) --*

          A description of the parameter

        - **Source** *(string) --*

          How the parameter is defined. For example, ``system`` denotes a system-defined parameter.

        - **DataType** *(string) --*

          The data type of the parameter. For example, ``integer`` :

        - **AllowedValues** *(string) --*

          A range of values within which the parameter can be set.

        - **IsModifiable** *(string) --*

          Whether the customer is allowed to modify the parameter.

        - **ChangeType** *(string) --*

          The conditions under which changes to this parameter can be applied. For example,
          ``requires-reboot`` indicates that a new value for this parameter will only take effect
          if a node is rebooted.
    """


_DescribeSubnetGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeSubnetGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeSubnetGroupsPaginatePaginationConfigTypeDef(
    _DescribeSubnetGroupsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeSubnetGroupsPaginate` `PaginationConfig`

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


_DescribeSubnetGroupsPaginateResponseSubnetGroupsSubnetsTypeDef = TypedDict(
    "_DescribeSubnetGroupsPaginateResponseSubnetGroupsSubnetsTypeDef",
    {"SubnetIdentifier": str, "SubnetAvailabilityZone": str},
    total=False,
)


class DescribeSubnetGroupsPaginateResponseSubnetGroupsSubnetsTypeDef(
    _DescribeSubnetGroupsPaginateResponseSubnetGroupsSubnetsTypeDef
):
    """
    Type definition for `DescribeSubnetGroupsPaginateResponseSubnetGroups` `Subnets`

    Represents the subnet associated with a DAX cluster. This parameter refers to subnets
    defined in Amazon Virtual Private Cloud (Amazon VPC) and used with DAX.

    - **SubnetIdentifier** *(string) --*

      The system-assigned identifier for the subnet.

    - **SubnetAvailabilityZone** *(string) --*

      The Availability Zone (AZ) for the subnet.
    """


_DescribeSubnetGroupsPaginateResponseSubnetGroupsTypeDef = TypedDict(
    "_DescribeSubnetGroupsPaginateResponseSubnetGroupsTypeDef",
    {
        "SubnetGroupName": str,
        "Description": str,
        "VpcId": str,
        "Subnets": List[DescribeSubnetGroupsPaginateResponseSubnetGroupsSubnetsTypeDef],
    },
    total=False,
)


class DescribeSubnetGroupsPaginateResponseSubnetGroupsTypeDef(
    _DescribeSubnetGroupsPaginateResponseSubnetGroupsTypeDef
):
    """
    Type definition for `DescribeSubnetGroupsPaginateResponse` `SubnetGroups`

    Represents the output of one of the following actions:

    * *CreateSubnetGroup*

    * *ModifySubnetGroup*

    - **SubnetGroupName** *(string) --*

      The name of the subnet group.

    - **Description** *(string) --*

      The description of the subnet group.

    - **VpcId** *(string) --*

      The Amazon Virtual Private Cloud identifier (VPC ID) of the subnet group.

    - **Subnets** *(list) --*

      A list of subnets associated with the subnet group.

      - *(dict) --*

        Represents the subnet associated with a DAX cluster. This parameter refers to subnets
        defined in Amazon Virtual Private Cloud (Amazon VPC) and used with DAX.

        - **SubnetIdentifier** *(string) --*

          The system-assigned identifier for the subnet.

        - **SubnetAvailabilityZone** *(string) --*

          The Availability Zone (AZ) for the subnet.
    """


_DescribeSubnetGroupsPaginateResponseTypeDef = TypedDict(
    "_DescribeSubnetGroupsPaginateResponseTypeDef",
    {"SubnetGroups": List[DescribeSubnetGroupsPaginateResponseSubnetGroupsTypeDef]},
    total=False,
)


class DescribeSubnetGroupsPaginateResponseTypeDef(
    _DescribeSubnetGroupsPaginateResponseTypeDef
):
    """
    Type definition for `DescribeSubnetGroupsPaginate` `Response`

    - **SubnetGroups** *(list) --*

      An array of subnet groups. Each element in the array represents a single subnet group.

      - *(dict) --*

        Represents the output of one of the following actions:

        * *CreateSubnetGroup*

        * *ModifySubnetGroup*

        - **SubnetGroupName** *(string) --*

          The name of the subnet group.

        - **Description** *(string) --*

          The description of the subnet group.

        - **VpcId** *(string) --*

          The Amazon Virtual Private Cloud identifier (VPC ID) of the subnet group.

        - **Subnets** *(list) --*

          A list of subnets associated with the subnet group.

          - *(dict) --*

            Represents the subnet associated with a DAX cluster. This parameter refers to subnets
            defined in Amazon Virtual Private Cloud (Amazon VPC) and used with DAX.

            - **SubnetIdentifier** *(string) --*

              The system-assigned identifier for the subnet.

            - **SubnetAvailabilityZone** *(string) --*

              The Availability Zone (AZ) for the subnet.
    """


_ListTagsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListTagsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
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

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListTagsPaginateResponseTagsTypeDef = TypedDict(
    "_ListTagsPaginateResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ListTagsPaginateResponseTagsTypeDef(_ListTagsPaginateResponseTagsTypeDef):
    """
    Type definition for `ListTagsPaginateResponse` `Tags`

    A description of a tag. Every tag is a key-value pair. You can add up to 50 tags to a
    single DAX cluster.

    AWS-assigned tag names and values are automatically assigned the ``aws:`` prefix, which the
    user cannot assign. AWS-assigned tag names do not count towards the tag limit of 50.
    User-assigned tag names have the prefix ``user:`` .

    You cannot backdate the application of a tag.

    - **Key** *(string) --*

      The key for the tag. Tag keys are case sensitive. Every DAX cluster can only have one tag
      with the same key. If you try to add an existing tag (same key), the existing tag value
      will be updated to the new value.

    - **Value** *(string) --*

      The value of the tag. Tag values are case-sensitive and can be null.
    """


_ListTagsPaginateResponseTypeDef = TypedDict(
    "_ListTagsPaginateResponseTypeDef",
    {"Tags": List[ListTagsPaginateResponseTagsTypeDef]},
    total=False,
)


class ListTagsPaginateResponseTypeDef(_ListTagsPaginateResponseTypeDef):
    """
    Type definition for `ListTagsPaginate` `Response`

    - **Tags** *(list) --*

      A list of tags currently associated with the DAX cluster.

      - *(dict) --*

        A description of a tag. Every tag is a key-value pair. You can add up to 50 tags to a
        single DAX cluster.

        AWS-assigned tag names and values are automatically assigned the ``aws:`` prefix, which the
        user cannot assign. AWS-assigned tag names do not count towards the tag limit of 50.
        User-assigned tag names have the prefix ``user:`` .

        You cannot backdate the application of a tag.

        - **Key** *(string) --*

          The key for the tag. Tag keys are case sensitive. Every DAX cluster can only have one tag
          with the same key. If you try to add an existing tag (same key), the existing tag value
          will be updated to the new value.

        - **Value** *(string) --*

          The value of the tag. Tag values are case-sensitive and can be null.
    """
