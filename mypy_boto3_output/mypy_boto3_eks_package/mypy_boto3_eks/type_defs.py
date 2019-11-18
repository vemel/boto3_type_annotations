"Main interface for eks type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientCreateClusterResponseclustercertificateAuthorityTypeDef",
    "ClientCreateClusterResponseclusteridentityoidcTypeDef",
    "ClientCreateClusterResponseclusteridentityTypeDef",
    "ClientCreateClusterResponseclusterloggingclusterLoggingTypeDef",
    "ClientCreateClusterResponseclusterloggingTypeDef",
    "ClientCreateClusterResponseclusterresourcesVpcConfigTypeDef",
    "ClientCreateClusterResponseclusterTypeDef",
    "ClientCreateClusterResponseTypeDef",
    "ClientCreateClusterloggingclusterLoggingTypeDef",
    "ClientCreateClusterloggingTypeDef",
    "ClientCreateClusterresourcesVpcConfigTypeDef",
    "ClientCreateNodegroupResponsenodegrouphealthissuesTypeDef",
    "ClientCreateNodegroupResponsenodegrouphealthTypeDef",
    "ClientCreateNodegroupResponsenodegroupremoteAccessTypeDef",
    "ClientCreateNodegroupResponsenodegroupresourcesautoScalingGroupsTypeDef",
    "ClientCreateNodegroupResponsenodegroupresourcesTypeDef",
    "ClientCreateNodegroupResponsenodegroupscalingConfigTypeDef",
    "ClientCreateNodegroupResponsenodegroupTypeDef",
    "ClientCreateNodegroupResponseTypeDef",
    "ClientCreateNodegroupremoteAccessTypeDef",
    "ClientCreateNodegroupscalingConfigTypeDef",
    "ClientDeleteClusterResponseclustercertificateAuthorityTypeDef",
    "ClientDeleteClusterResponseclusteridentityoidcTypeDef",
    "ClientDeleteClusterResponseclusteridentityTypeDef",
    "ClientDeleteClusterResponseclusterloggingclusterLoggingTypeDef",
    "ClientDeleteClusterResponseclusterloggingTypeDef",
    "ClientDeleteClusterResponseclusterresourcesVpcConfigTypeDef",
    "ClientDeleteClusterResponseclusterTypeDef",
    "ClientDeleteClusterResponseTypeDef",
    "ClientDeleteNodegroupResponsenodegrouphealthissuesTypeDef",
    "ClientDeleteNodegroupResponsenodegrouphealthTypeDef",
    "ClientDeleteNodegroupResponsenodegroupremoteAccessTypeDef",
    "ClientDeleteNodegroupResponsenodegroupresourcesautoScalingGroupsTypeDef",
    "ClientDeleteNodegroupResponsenodegroupresourcesTypeDef",
    "ClientDeleteNodegroupResponsenodegroupscalingConfigTypeDef",
    "ClientDeleteNodegroupResponsenodegroupTypeDef",
    "ClientDeleteNodegroupResponseTypeDef",
    "ClientDescribeClusterResponseclustercertificateAuthorityTypeDef",
    "ClientDescribeClusterResponseclusteridentityoidcTypeDef",
    "ClientDescribeClusterResponseclusteridentityTypeDef",
    "ClientDescribeClusterResponseclusterloggingclusterLoggingTypeDef",
    "ClientDescribeClusterResponseclusterloggingTypeDef",
    "ClientDescribeClusterResponseclusterresourcesVpcConfigTypeDef",
    "ClientDescribeClusterResponseclusterTypeDef",
    "ClientDescribeClusterResponseTypeDef",
    "ClientDescribeNodegroupResponsenodegrouphealthissuesTypeDef",
    "ClientDescribeNodegroupResponsenodegrouphealthTypeDef",
    "ClientDescribeNodegroupResponsenodegroupremoteAccessTypeDef",
    "ClientDescribeNodegroupResponsenodegroupresourcesautoScalingGroupsTypeDef",
    "ClientDescribeNodegroupResponsenodegroupresourcesTypeDef",
    "ClientDescribeNodegroupResponsenodegroupscalingConfigTypeDef",
    "ClientDescribeNodegroupResponsenodegroupTypeDef",
    "ClientDescribeNodegroupResponseTypeDef",
    "ClientDescribeUpdateResponseupdateerrorsTypeDef",
    "ClientDescribeUpdateResponseupdateparamsTypeDef",
    "ClientDescribeUpdateResponseupdateTypeDef",
    "ClientDescribeUpdateResponseTypeDef",
    "ClientListClustersResponseTypeDef",
    "ClientListNodegroupsResponseTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientListUpdatesResponseTypeDef",
    "ClientUpdateClusterConfigResponseupdateerrorsTypeDef",
    "ClientUpdateClusterConfigResponseupdateparamsTypeDef",
    "ClientUpdateClusterConfigResponseupdateTypeDef",
    "ClientUpdateClusterConfigResponseTypeDef",
    "ClientUpdateClusterConfigloggingclusterLoggingTypeDef",
    "ClientUpdateClusterConfigloggingTypeDef",
    "ClientUpdateClusterConfigresourcesVpcConfigTypeDef",
    "ClientUpdateClusterVersionResponseupdateerrorsTypeDef",
    "ClientUpdateClusterVersionResponseupdateparamsTypeDef",
    "ClientUpdateClusterVersionResponseupdateTypeDef",
    "ClientUpdateClusterVersionResponseTypeDef",
    "ClientUpdateNodegroupConfigResponseupdateerrorsTypeDef",
    "ClientUpdateNodegroupConfigResponseupdateparamsTypeDef",
    "ClientUpdateNodegroupConfigResponseupdateTypeDef",
    "ClientUpdateNodegroupConfigResponseTypeDef",
    "ClientUpdateNodegroupConfiglabelsTypeDef",
    "ClientUpdateNodegroupConfigscalingConfigTypeDef",
    "ClientUpdateNodegroupVersionResponseupdateerrorsTypeDef",
    "ClientUpdateNodegroupVersionResponseupdateparamsTypeDef",
    "ClientUpdateNodegroupVersionResponseupdateTypeDef",
    "ClientUpdateNodegroupVersionResponseTypeDef",
    "ClusterActiveWaitWaiterConfigTypeDef",
    "ClusterDeletedWaitWaiterConfigTypeDef",
    "ListClustersPaginatePaginationConfigTypeDef",
    "ListClustersPaginateResponseTypeDef",
    "ListNodegroupsPaginatePaginationConfigTypeDef",
    "ListNodegroupsPaginateResponseTypeDef",
    "ListUpdatesPaginatePaginationConfigTypeDef",
    "ListUpdatesPaginateResponseTypeDef",
    "NodegroupActiveWaitWaiterConfigTypeDef",
    "NodegroupDeletedWaitWaiterConfigTypeDef",
)


_ClientCreateClusterResponseclustercertificateAuthorityTypeDef = TypedDict(
    "_ClientCreateClusterResponseclustercertificateAuthorityTypeDef",
    {"data": str},
    total=False,
)


class ClientCreateClusterResponseclustercertificateAuthorityTypeDef(
    _ClientCreateClusterResponseclustercertificateAuthorityTypeDef
):
    """
    Type definition for `ClientCreateClusterResponsecluster` `certificateAuthority`

    The ``certificate-authority-data`` for your cluster.

    - **data** *(string) --*

      The Base64-encoded certificate data required to communicate with your cluster. Add this
      to the ``certificate-authority-data`` section of the ``kubeconfig`` file for your cluster.
    """


_ClientCreateClusterResponseclusteridentityoidcTypeDef = TypedDict(
    "_ClientCreateClusterResponseclusteridentityoidcTypeDef",
    {"issuer": str},
    total=False,
)


class ClientCreateClusterResponseclusteridentityoidcTypeDef(
    _ClientCreateClusterResponseclusteridentityoidcTypeDef
):
    """
    Type definition for `ClientCreateClusterResponseclusteridentity` `oidc`

    The `OpenID Connect <https://openid.net/connect/>`__ identity provider information for
    the cluster.

    - **issuer** *(string) --*

      The issuer URL for the OpenID Connect identity provider.
    """


_ClientCreateClusterResponseclusteridentityTypeDef = TypedDict(
    "_ClientCreateClusterResponseclusteridentityTypeDef",
    {"oidc": ClientCreateClusterResponseclusteridentityoidcTypeDef},
    total=False,
)


class ClientCreateClusterResponseclusteridentityTypeDef(
    _ClientCreateClusterResponseclusteridentityTypeDef
):
    """
    Type definition for `ClientCreateClusterResponsecluster` `identity`

    The identity provider information for the cluster.

    - **oidc** *(dict) --*

      The `OpenID Connect <https://openid.net/connect/>`__ identity provider information for
      the cluster.

      - **issuer** *(string) --*

        The issuer URL for the OpenID Connect identity provider.
    """


_ClientCreateClusterResponseclusterloggingclusterLoggingTypeDef = TypedDict(
    "_ClientCreateClusterResponseclusterloggingclusterLoggingTypeDef",
    {"types": List[str], "enabled": bool},
    total=False,
)


class ClientCreateClusterResponseclusterloggingclusterLoggingTypeDef(
    _ClientCreateClusterResponseclusterloggingclusterLoggingTypeDef
):
    """
    Type definition for `ClientCreateClusterResponseclusterlogging` `clusterLogging`

    An object representing the enabled or disabled Kubernetes control plane logs for your
    cluster.

    - **types** *(list) --*

      The available cluster control plane log types.

      - *(string) --*

    - **enabled** *(boolean) --*

      If a log type is enabled, that log type exports its control plane logs to CloudWatch
      Logs. If a log type isn't enabled, that log type doesn't export its control plane
      logs. Each individual log type can be enabled or disabled independently.
    """


_ClientCreateClusterResponseclusterloggingTypeDef = TypedDict(
    "_ClientCreateClusterResponseclusterloggingTypeDef",
    {
        "clusterLogging": List[
            ClientCreateClusterResponseclusterloggingclusterLoggingTypeDef
        ]
    },
    total=False,
)


class ClientCreateClusterResponseclusterloggingTypeDef(
    _ClientCreateClusterResponseclusterloggingTypeDef
):
    """
    Type definition for `ClientCreateClusterResponsecluster` `logging`

    The logging configuration for your cluster.

    - **clusterLogging** *(list) --*

      The cluster control plane logging configuration for your cluster.

      - *(dict) --*

        An object representing the enabled or disabled Kubernetes control plane logs for your
        cluster.

        - **types** *(list) --*

          The available cluster control plane log types.

          - *(string) --*

        - **enabled** *(boolean) --*

          If a log type is enabled, that log type exports its control plane logs to CloudWatch
          Logs. If a log type isn't enabled, that log type doesn't export its control plane
          logs. Each individual log type can be enabled or disabled independently.
    """


_ClientCreateClusterResponseclusterresourcesVpcConfigTypeDef = TypedDict(
    "_ClientCreateClusterResponseclusterresourcesVpcConfigTypeDef",
    {
        "subnetIds": List[str],
        "securityGroupIds": List[str],
        "clusterSecurityGroupId": str,
        "vpcId": str,
        "endpointPublicAccess": bool,
        "endpointPrivateAccess": bool,
    },
    total=False,
)


class ClientCreateClusterResponseclusterresourcesVpcConfigTypeDef(
    _ClientCreateClusterResponseclusterresourcesVpcConfigTypeDef
):
    """
    Type definition for `ClientCreateClusterResponsecluster` `resourcesVpcConfig`

    The VPC configuration used by the cluster control plane. Amazon EKS VPC resources have
    specific requirements to work properly with Kubernetes. For more information, see `Cluster
    VPC Considerations <https://docs.aws.amazon.com/eks/latest/userguide/network_reqs.html>`__
    and `Cluster Security Group Considerations
    <https://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html>`__ in the *Amazon
    EKS User Guide* .

    - **subnetIds** *(list) --*

      The subnets associated with your cluster.

      - *(string) --*

    - **securityGroupIds** *(list) --*

      The security groups associated with the cross-account elastic network interfaces that are
      used to allow communication between your worker nodes and the Kubernetes control plane.

      - *(string) --*

    - **clusterSecurityGroupId** *(string) --*

      The cluster security group that was created by Amazon EKS for the cluster. Managed node
      groups use this security group for control plane to data plane communication.

    - **vpcId** *(string) --*

      The VPC associated with your cluster.

    - **endpointPublicAccess** *(boolean) --*

      This parameter indicates whether the Amazon EKS public API server endpoint is enabled. If
      the Amazon EKS public API server endpoint is disabled, your cluster's Kubernetes API
      server can receive only requests that originate from within the cluster VPC.

    - **endpointPrivateAccess** *(boolean) --*

      This parameter indicates whether the Amazon EKS private API server endpoint is enabled.
      If the Amazon EKS private API server endpoint is enabled, Kubernetes API requests that
      originate from within your cluster's VPC use the private VPC endpoint instead of
      traversing the internet.
    """


_ClientCreateClusterResponseclusterTypeDef = TypedDict(
    "_ClientCreateClusterResponseclusterTypeDef",
    {
        "name": str,
        "arn": str,
        "createdAt": datetime,
        "version": str,
        "endpoint": str,
        "roleArn": str,
        "resourcesVpcConfig": ClientCreateClusterResponseclusterresourcesVpcConfigTypeDef,
        "logging": ClientCreateClusterResponseclusterloggingTypeDef,
        "identity": ClientCreateClusterResponseclusteridentityTypeDef,
        "status": str,
        "certificateAuthority": ClientCreateClusterResponseclustercertificateAuthorityTypeDef,
        "clientRequestToken": str,
        "platformVersion": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientCreateClusterResponseclusterTypeDef(
    _ClientCreateClusterResponseclusterTypeDef
):
    """
    Type definition for `ClientCreateClusterResponse` `cluster`

    The full description of your new cluster.

    - **name** *(string) --*

      The name of the cluster.

    - **arn** *(string) --*

      The Amazon Resource Name (ARN) of the cluster.

    - **createdAt** *(datetime) --*

      The Unix epoch timestamp in seconds for when the cluster was created.

    - **version** *(string) --*

      The Kubernetes server version for the cluster.

    - **endpoint** *(string) --*

      The endpoint for your Kubernetes API server.

    - **roleArn** *(string) --*

      The Amazon Resource Name (ARN) of the IAM role that provides permissions for the Kubernetes
      control plane to make calls to AWS API operations on your behalf.

    - **resourcesVpcConfig** *(dict) --*

      The VPC configuration used by the cluster control plane. Amazon EKS VPC resources have
      specific requirements to work properly with Kubernetes. For more information, see `Cluster
      VPC Considerations <https://docs.aws.amazon.com/eks/latest/userguide/network_reqs.html>`__
      and `Cluster Security Group Considerations
      <https://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html>`__ in the *Amazon
      EKS User Guide* .

      - **subnetIds** *(list) --*

        The subnets associated with your cluster.

        - *(string) --*

      - **securityGroupIds** *(list) --*

        The security groups associated with the cross-account elastic network interfaces that are
        used to allow communication between your worker nodes and the Kubernetes control plane.

        - *(string) --*

      - **clusterSecurityGroupId** *(string) --*

        The cluster security group that was created by Amazon EKS for the cluster. Managed node
        groups use this security group for control plane to data plane communication.

      - **vpcId** *(string) --*

        The VPC associated with your cluster.

      - **endpointPublicAccess** *(boolean) --*

        This parameter indicates whether the Amazon EKS public API server endpoint is enabled. If
        the Amazon EKS public API server endpoint is disabled, your cluster's Kubernetes API
        server can receive only requests that originate from within the cluster VPC.

      - **endpointPrivateAccess** *(boolean) --*

        This parameter indicates whether the Amazon EKS private API server endpoint is enabled.
        If the Amazon EKS private API server endpoint is enabled, Kubernetes API requests that
        originate from within your cluster's VPC use the private VPC endpoint instead of
        traversing the internet.

    - **logging** *(dict) --*

      The logging configuration for your cluster.

      - **clusterLogging** *(list) --*

        The cluster control plane logging configuration for your cluster.

        - *(dict) --*

          An object representing the enabled or disabled Kubernetes control plane logs for your
          cluster.

          - **types** *(list) --*

            The available cluster control plane log types.

            - *(string) --*

          - **enabled** *(boolean) --*

            If a log type is enabled, that log type exports its control plane logs to CloudWatch
            Logs. If a log type isn't enabled, that log type doesn't export its control plane
            logs. Each individual log type can be enabled or disabled independently.

    - **identity** *(dict) --*

      The identity provider information for the cluster.

      - **oidc** *(dict) --*

        The `OpenID Connect <https://openid.net/connect/>`__ identity provider information for
        the cluster.

        - **issuer** *(string) --*

          The issuer URL for the OpenID Connect identity provider.

    - **status** *(string) --*

      The current status of the cluster.

    - **certificateAuthority** *(dict) --*

      The ``certificate-authority-data`` for your cluster.

      - **data** *(string) --*

        The Base64-encoded certificate data required to communicate with your cluster. Add this
        to the ``certificate-authority-data`` section of the ``kubeconfig`` file for your cluster.

    - **clientRequestToken** *(string) --*

      Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

    - **platformVersion** *(string) --*

      The platform version of your Amazon EKS cluster. For more information, see `Platform
      Versions <https://docs.aws.amazon.com/eks/latest/userguide/platform-versions.html>`__ in
      the * *Amazon EKS User Guide* * .

    - **tags** *(dict) --*

      The metadata that you apply to the cluster to assist with categorization and organization.
      Each tag consists of a key and an optional value, both of which you define. Cluster tags do
      not propagate to any other resources associated with the cluster.

      - *(string) --*

        - *(string) --*
    """


_ClientCreateClusterResponseTypeDef = TypedDict(
    "_ClientCreateClusterResponseTypeDef",
    {"cluster": ClientCreateClusterResponseclusterTypeDef},
    total=False,
)


class ClientCreateClusterResponseTypeDef(_ClientCreateClusterResponseTypeDef):
    """
    Type definition for `ClientCreateCluster` `Response`

    - **cluster** *(dict) --*

      The full description of your new cluster.

      - **name** *(string) --*

        The name of the cluster.

      - **arn** *(string) --*

        The Amazon Resource Name (ARN) of the cluster.

      - **createdAt** *(datetime) --*

        The Unix epoch timestamp in seconds for when the cluster was created.

      - **version** *(string) --*

        The Kubernetes server version for the cluster.

      - **endpoint** *(string) --*

        The endpoint for your Kubernetes API server.

      - **roleArn** *(string) --*

        The Amazon Resource Name (ARN) of the IAM role that provides permissions for the Kubernetes
        control plane to make calls to AWS API operations on your behalf.

      - **resourcesVpcConfig** *(dict) --*

        The VPC configuration used by the cluster control plane. Amazon EKS VPC resources have
        specific requirements to work properly with Kubernetes. For more information, see `Cluster
        VPC Considerations <https://docs.aws.amazon.com/eks/latest/userguide/network_reqs.html>`__
        and `Cluster Security Group Considerations
        <https://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html>`__ in the *Amazon
        EKS User Guide* .

        - **subnetIds** *(list) --*

          The subnets associated with your cluster.

          - *(string) --*

        - **securityGroupIds** *(list) --*

          The security groups associated with the cross-account elastic network interfaces that are
          used to allow communication between your worker nodes and the Kubernetes control plane.

          - *(string) --*

        - **clusterSecurityGroupId** *(string) --*

          The cluster security group that was created by Amazon EKS for the cluster. Managed node
          groups use this security group for control plane to data plane communication.

        - **vpcId** *(string) --*

          The VPC associated with your cluster.

        - **endpointPublicAccess** *(boolean) --*

          This parameter indicates whether the Amazon EKS public API server endpoint is enabled. If
          the Amazon EKS public API server endpoint is disabled, your cluster's Kubernetes API
          server can receive only requests that originate from within the cluster VPC.

        - **endpointPrivateAccess** *(boolean) --*

          This parameter indicates whether the Amazon EKS private API server endpoint is enabled.
          If the Amazon EKS private API server endpoint is enabled, Kubernetes API requests that
          originate from within your cluster's VPC use the private VPC endpoint instead of
          traversing the internet.

      - **logging** *(dict) --*

        The logging configuration for your cluster.

        - **clusterLogging** *(list) --*

          The cluster control plane logging configuration for your cluster.

          - *(dict) --*

            An object representing the enabled or disabled Kubernetes control plane logs for your
            cluster.

            - **types** *(list) --*

              The available cluster control plane log types.

              - *(string) --*

            - **enabled** *(boolean) --*

              If a log type is enabled, that log type exports its control plane logs to CloudWatch
              Logs. If a log type isn't enabled, that log type doesn't export its control plane
              logs. Each individual log type can be enabled or disabled independently.

      - **identity** *(dict) --*

        The identity provider information for the cluster.

        - **oidc** *(dict) --*

          The `OpenID Connect <https://openid.net/connect/>`__ identity provider information for
          the cluster.

          - **issuer** *(string) --*

            The issuer URL for the OpenID Connect identity provider.

      - **status** *(string) --*

        The current status of the cluster.

      - **certificateAuthority** *(dict) --*

        The ``certificate-authority-data`` for your cluster.

        - **data** *(string) --*

          The Base64-encoded certificate data required to communicate with your cluster. Add this
          to the ``certificate-authority-data`` section of the ``kubeconfig`` file for your cluster.

      - **clientRequestToken** *(string) --*

        Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

      - **platformVersion** *(string) --*

        The platform version of your Amazon EKS cluster. For more information, see `Platform
        Versions <https://docs.aws.amazon.com/eks/latest/userguide/platform-versions.html>`__ in
        the * *Amazon EKS User Guide* * .

      - **tags** *(dict) --*

        The metadata that you apply to the cluster to assist with categorization and organization.
        Each tag consists of a key and an optional value, both of which you define. Cluster tags do
        not propagate to any other resources associated with the cluster.

        - *(string) --*

          - *(string) --*
    """


_ClientCreateClusterloggingclusterLoggingTypeDef = TypedDict(
    "_ClientCreateClusterloggingclusterLoggingTypeDef",
    {"types": List[str], "enabled": bool},
    total=False,
)


class ClientCreateClusterloggingclusterLoggingTypeDef(
    _ClientCreateClusterloggingclusterLoggingTypeDef
):
    """
    Type definition for `ClientCreateClusterlogging` `clusterLogging`

    An object representing the enabled or disabled Kubernetes control plane logs for your cluster.

    - **types** *(list) --*

      The available cluster control plane log types.

      - *(string) --*

    - **enabled** *(boolean) --*

      If a log type is enabled, that log type exports its control plane logs to CloudWatch Logs.
      If a log type isn't enabled, that log type doesn't export its control plane logs. Each
      individual log type can be enabled or disabled independently.
    """


_ClientCreateClusterloggingTypeDef = TypedDict(
    "_ClientCreateClusterloggingTypeDef",
    {"clusterLogging": List[ClientCreateClusterloggingclusterLoggingTypeDef]},
    total=False,
)


class ClientCreateClusterloggingTypeDef(_ClientCreateClusterloggingTypeDef):
    """
    Type definition for `ClientCreateCluster` `logging`

    Enable or disable exporting the Kubernetes control plane logs for your cluster to CloudWatch
    Logs. By default, cluster control plane logs aren't exported to CloudWatch Logs. For more
    information, see `Amazon EKS Cluster Control Plane Logs
    <https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html>`__ in the * *Amazon
    EKS User Guide* * .

    .. note::

      CloudWatch Logs ingestion, archive storage, and data scanning rates apply to exported control
      plane logs. For more information, see `Amazon CloudWatch Pricing
      <http://aws.amazon.com/cloudwatch/pricing/>`__ .

    - **clusterLogging** *(list) --*

      The cluster control plane logging configuration for your cluster.

      - *(dict) --*

        An object representing the enabled or disabled Kubernetes control plane logs for your cluster.

        - **types** *(list) --*

          The available cluster control plane log types.

          - *(string) --*

        - **enabled** *(boolean) --*

          If a log type is enabled, that log type exports its control plane logs to CloudWatch Logs.
          If a log type isn't enabled, that log type doesn't export its control plane logs. Each
          individual log type can be enabled or disabled independently.
    """


_ClientCreateClusterresourcesVpcConfigTypeDef = TypedDict(
    "_ClientCreateClusterresourcesVpcConfigTypeDef",
    {
        "subnetIds": List[str],
        "securityGroupIds": List[str],
        "endpointPublicAccess": bool,
        "endpointPrivateAccess": bool,
    },
    total=False,
)


class ClientCreateClusterresourcesVpcConfigTypeDef(
    _ClientCreateClusterresourcesVpcConfigTypeDef
):
    """
    Type definition for `ClientCreateCluster` `resourcesVpcConfig`

    The VPC configuration used by the cluster control plane. Amazon EKS VPC resources have specific
    requirements to work properly with Kubernetes. For more information, see `Cluster VPC
    Considerations <https://docs.aws.amazon.com/eks/latest/userguide/network_reqs.html>`__ and
    `Cluster Security Group Considerations
    <https://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html>`__ in the *Amazon EKS User
    Guide* . You must specify at least two subnets. You can specify up to five security groups, but
    we recommend that you use a dedicated security group for your cluster control plane.

    - **subnetIds** *(list) --*

      Specify subnets for your Amazon EKS worker nodes. Amazon EKS creates cross-account elastic
      network interfaces in these subnets to allow communication between your worker nodes and the
      Kubernetes control plane.

      - *(string) --*

    - **securityGroupIds** *(list) --*

      Specify one or more security groups for the cross-account elastic network interfaces that
      Amazon EKS creates to use to allow communication between your worker nodes and the Kubernetes
      control plane. If you don't specify a security group, the default security group for your VPC
      is used.

      - *(string) --*

    - **endpointPublicAccess** *(boolean) --*

      Set this value to ``false`` to disable public access for your cluster's Kubernetes API server
      endpoint. If you disable public access, your cluster's Kubernetes API server can receive only
      requests from within the cluster VPC. The default value for this parameter is ``true`` , which
      enables public access for your Kubernetes API server. For more information, see `Amazon EKS
      Cluster Endpoint Access Control
      <https://docs.aws.amazon.com/eks/latest/userguide/cluster-endpoint.html>`__ in the * *Amazon
      EKS User Guide* * .

    - **endpointPrivateAccess** *(boolean) --*

      Set this value to ``true`` to enable private access for your cluster's Kubernetes API server
      endpoint. If you enable private access, Kubernetes API requests from within your cluster's VPC
      use the private VPC endpoint. The default value for this parameter is ``false`` , which
      disables private access for your Kubernetes API server. For more information, see `Amazon EKS
      Cluster Endpoint Access Control
      <https://docs.aws.amazon.com/eks/latest/userguide/cluster-endpoint.html>`__ in the * *Amazon
      EKS User Guide* * .
    """


_ClientCreateNodegroupResponsenodegrouphealthissuesTypeDef = TypedDict(
    "_ClientCreateNodegroupResponsenodegrouphealthissuesTypeDef",
    {"code": str, "message": str, "resourceIds": List[str]},
    total=False,
)


class ClientCreateNodegroupResponsenodegrouphealthissuesTypeDef(
    _ClientCreateNodegroupResponsenodegrouphealthissuesTypeDef
):
    """
    Type definition for `ClientCreateNodegroupResponsenodegrouphealth` `issues`

    An object representing an issue with an Amazon EKS resource.

    - **code** *(string) --*

      A brief description of the error.

      * **AutoScalingGroupNotFound** : We couldn't find the Auto Scaling group associated
      with the managed node group. You may be able to recreate an Auto Scaling group with
      the same settings to recover.

      * **Ec2SecurityGroupNotFound** : We couldn't find the cluster security group for the
      cluster. You must recreate your cluster.

      * **Ec2SecurityGroupDeletionFailure** : We could not delete the remote access
      security group for your managed node group. Remove any dependencies from the security
      group.

      * **Ec2LaunchTemplateNotFound** : We couldn't find the Amazon EC2 launch template for
      your managed node group. You may be able to recreate a launch template with the same
      settings to recover.

      * **Ec2LaunchTemplateVersionMismatch** : The Amazon EC2 launch template version for
      your managed node group does not match the version that Amazon EKS created. You may
      be able to revert to the Amazon EKS-created version to recover.

      * **IamInstanceProfileNotFound** : We couldn't find the IAM instance profile for your
      managed node group. You may be able to recreate an instance profile with the same
      settings to recover.

      * **IamNodeRoleNotFound** : We couldn't find the IAM role for your managed node
      group. You may be able to recreate an IAM role with the same settings to recover.

      * **AsgInstanceLaunchFailures** : Your Auto Scaling group is experiencing failures
      while attempting to launch instances.

      * **InstanceLimitExceeded** : Your AWS account is unable to launch any more instances
      of the specified instance type. You may be able to request an Amazon EC2 instance
      limit increase to recover.

      * **InsufficientFreeAddresses** : One or more of the subnets associated with your
      managed node group does not have enough available IP addresses for new nodes.

      * **AccessDenied** : Amazon EKS and or one or more of your managed nodes is unable to
      communicate with your cluster API server.

      * **InternalFailure** : These errors are usually caused by an Amazon EKS server-side
      issue.

    - **message** *(string) --*

      The error message associated with the issue.

    - **resourceIds** *(list) --*

      The AWS resources that are afflicted by this issue.

      - *(string) --*
    """


_ClientCreateNodegroupResponsenodegrouphealthTypeDef = TypedDict(
    "_ClientCreateNodegroupResponsenodegrouphealthTypeDef",
    {"issues": List[ClientCreateNodegroupResponsenodegrouphealthissuesTypeDef]},
    total=False,
)


class ClientCreateNodegroupResponsenodegrouphealthTypeDef(
    _ClientCreateNodegroupResponsenodegrouphealthTypeDef
):
    """
    Type definition for `ClientCreateNodegroupResponsenodegroup` `health`

    The health status of the node group. If there are issues with your node group's health,
    they are listed here.

    - **issues** *(list) --*

      Any issues that are associated with the node group.

      - *(dict) --*

        An object representing an issue with an Amazon EKS resource.

        - **code** *(string) --*

          A brief description of the error.

          * **AutoScalingGroupNotFound** : We couldn't find the Auto Scaling group associated
          with the managed node group. You may be able to recreate an Auto Scaling group with
          the same settings to recover.

          * **Ec2SecurityGroupNotFound** : We couldn't find the cluster security group for the
          cluster. You must recreate your cluster.

          * **Ec2SecurityGroupDeletionFailure** : We could not delete the remote access
          security group for your managed node group. Remove any dependencies from the security
          group.

          * **Ec2LaunchTemplateNotFound** : We couldn't find the Amazon EC2 launch template for
          your managed node group. You may be able to recreate a launch template with the same
          settings to recover.

          * **Ec2LaunchTemplateVersionMismatch** : The Amazon EC2 launch template version for
          your managed node group does not match the version that Amazon EKS created. You may
          be able to revert to the Amazon EKS-created version to recover.

          * **IamInstanceProfileNotFound** : We couldn't find the IAM instance profile for your
          managed node group. You may be able to recreate an instance profile with the same
          settings to recover.

          * **IamNodeRoleNotFound** : We couldn't find the IAM role for your managed node
          group. You may be able to recreate an IAM role with the same settings to recover.

          * **AsgInstanceLaunchFailures** : Your Auto Scaling group is experiencing failures
          while attempting to launch instances.

          * **InstanceLimitExceeded** : Your AWS account is unable to launch any more instances
          of the specified instance type. You may be able to request an Amazon EC2 instance
          limit increase to recover.

          * **InsufficientFreeAddresses** : One or more of the subnets associated with your
          managed node group does not have enough available IP addresses for new nodes.

          * **AccessDenied** : Amazon EKS and or one or more of your managed nodes is unable to
          communicate with your cluster API server.

          * **InternalFailure** : These errors are usually caused by an Amazon EKS server-side
          issue.

        - **message** *(string) --*

          The error message associated with the issue.

        - **resourceIds** *(list) --*

          The AWS resources that are afflicted by this issue.

          - *(string) --*
    """


_ClientCreateNodegroupResponsenodegroupremoteAccessTypeDef = TypedDict(
    "_ClientCreateNodegroupResponsenodegroupremoteAccessTypeDef",
    {"ec2SshKey": str, "sourceSecurityGroups": List[str]},
    total=False,
)


class ClientCreateNodegroupResponsenodegroupremoteAccessTypeDef(
    _ClientCreateNodegroupResponsenodegroupremoteAccessTypeDef
):
    """
    Type definition for `ClientCreateNodegroupResponsenodegroup` `remoteAccess`

    The remote access (SSH) configuration that is associated with the node group.

    - **ec2SshKey** *(string) --*

      The Amazon EC2 SSH key that provides access for SSH communication with the worker nodes
      in the managed node group. For more information, see `Amazon EC2 Key Pairs
      <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html>`__ in the
      *Amazon Elastic Compute Cloud User Guide for Linux Instances* .

    - **sourceSecurityGroups** *(list) --*

      The security groups to allow SSH access (port 22) from on the worker nodes. If you
      specify an Amazon EC2 SSH key, but you do not specify a source security group when you
      create a managed node group, port 22 on the worker nodes is opened to the internet
      (0.0.0.0/0). For more information, see `Security Groups for Your VPC
      <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ in the
      *Amazon Virtual Private Cloud User Guide* .

      - *(string) --*
    """


_ClientCreateNodegroupResponsenodegroupresourcesautoScalingGroupsTypeDef = TypedDict(
    "_ClientCreateNodegroupResponsenodegroupresourcesautoScalingGroupsTypeDef",
    {"name": str},
    total=False,
)


class ClientCreateNodegroupResponsenodegroupresourcesautoScalingGroupsTypeDef(
    _ClientCreateNodegroupResponsenodegroupresourcesautoScalingGroupsTypeDef
):
    """
    Type definition for `ClientCreateNodegroupResponsenodegroupresources` `autoScalingGroups`

    An AutoScaling group that is associated with an Amazon EKS managed node group.

    - **name** *(string) --*

      The name of the AutoScaling group associated with an Amazon EKS managed node group.
    """


_ClientCreateNodegroupResponsenodegroupresourcesTypeDef = TypedDict(
    "_ClientCreateNodegroupResponsenodegroupresourcesTypeDef",
    {
        "autoScalingGroups": List[
            ClientCreateNodegroupResponsenodegroupresourcesautoScalingGroupsTypeDef
        ],
        "remoteAccessSecurityGroup": str,
    },
    total=False,
)


class ClientCreateNodegroupResponsenodegroupresourcesTypeDef(
    _ClientCreateNodegroupResponsenodegroupresourcesTypeDef
):
    """
    Type definition for `ClientCreateNodegroupResponsenodegroup` `resources`

    The resources associated with the nodegroup, such as AutoScaling groups and security groups
    for remote access.

    - **autoScalingGroups** *(list) --*

      The autoscaling groups associated with the node group.

      - *(dict) --*

        An AutoScaling group that is associated with an Amazon EKS managed node group.

        - **name** *(string) --*

          The name of the AutoScaling group associated with an Amazon EKS managed node group.

    - **remoteAccessSecurityGroup** *(string) --*

      The remote access security group associated with the node group. This security group
      controls SSH access to the worker nodes.
    """


_ClientCreateNodegroupResponsenodegroupscalingConfigTypeDef = TypedDict(
    "_ClientCreateNodegroupResponsenodegroupscalingConfigTypeDef",
    {"minSize": int, "maxSize": int, "desiredSize": int},
    total=False,
)


class ClientCreateNodegroupResponsenodegroupscalingConfigTypeDef(
    _ClientCreateNodegroupResponsenodegroupscalingConfigTypeDef
):
    """
    Type definition for `ClientCreateNodegroupResponsenodegroup` `scalingConfig`

    The scaling configuration details for the AutoScaling group that is associated with your
    node group.

    - **minSize** *(integer) --*

      The minimum number of worker nodes that the managed node group can scale in to. This
      number must be greater than zero.

    - **maxSize** *(integer) --*

      The maximum number of worker nodes that the managed node group can scale out to. Managed
      node groups can support up to 100 nodes by default.

    - **desiredSize** *(integer) --*

      The current number of worker nodes that the managed node group should maintain.
    """


_ClientCreateNodegroupResponsenodegroupTypeDef = TypedDict(
    "_ClientCreateNodegroupResponsenodegroupTypeDef",
    {
        "nodegroupName": str,
        "nodegroupArn": str,
        "clusterName": str,
        "version": str,
        "releaseVersion": str,
        "createdAt": datetime,
        "modifiedAt": datetime,
        "status": str,
        "scalingConfig": ClientCreateNodegroupResponsenodegroupscalingConfigTypeDef,
        "instanceTypes": List[str],
        "subnets": List[str],
        "remoteAccess": ClientCreateNodegroupResponsenodegroupremoteAccessTypeDef,
        "amiType": str,
        "nodeRole": str,
        "labels": Dict[str, str],
        "resources": ClientCreateNodegroupResponsenodegroupresourcesTypeDef,
        "diskSize": int,
        "health": ClientCreateNodegroupResponsenodegrouphealthTypeDef,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientCreateNodegroupResponsenodegroupTypeDef(
    _ClientCreateNodegroupResponsenodegroupTypeDef
):
    """
    Type definition for `ClientCreateNodegroupResponse` `nodegroup`

    The full description of your new node group.

    - **nodegroupName** *(string) --*

      The name associated with an Amazon EKS managed node group.

    - **nodegroupArn** *(string) --*

      The Amazon Resource Name (ARN) associated with the managed node group.

    - **clusterName** *(string) --*

      The name of the cluster that the managed node group resides in.

    - **version** *(string) --*

      The Kubernetes version of the managed node group.

    - **releaseVersion** *(string) --*

      The AMI version of the managed node group. For more information, see `Amazon EKS-Optimized
      Linux AMI Versions
      <https://docs.aws.amazon.com/eks/latest/userguide/eks-linux-ami-versions.html>`__ in the
      *Amazon EKS User Guide* .

    - **createdAt** *(datetime) --*

      The Unix epoch timestamp in seconds for when the managed node group was created.

    - **modifiedAt** *(datetime) --*

      The Unix epoch timestamp in seconds for when the managed node group was last modified.

    - **status** *(string) --*

      The current status of the managed node group.

    - **scalingConfig** *(dict) --*

      The scaling configuration details for the AutoScaling group that is associated with your
      node group.

      - **minSize** *(integer) --*

        The minimum number of worker nodes that the managed node group can scale in to. This
        number must be greater than zero.

      - **maxSize** *(integer) --*

        The maximum number of worker nodes that the managed node group can scale out to. Managed
        node groups can support up to 100 nodes by default.

      - **desiredSize** *(integer) --*

        The current number of worker nodes that the managed node group should maintain.

    - **instanceTypes** *(list) --*

      The instance types associated with your node group.

      - *(string) --*

    - **subnets** *(list) --*

      The subnets allowed for the AutoScaling group that is associated with your node group.
      These subnets must have the following tag: ``kubernetes.io/cluster/CLUSTER_NAME`` , where
      ``CLUSTER_NAME`` is replaced with the name of your cluster.

      - *(string) --*

    - **remoteAccess** *(dict) --*

      The remote access (SSH) configuration that is associated with the node group.

      - **ec2SshKey** *(string) --*

        The Amazon EC2 SSH key that provides access for SSH communication with the worker nodes
        in the managed node group. For more information, see `Amazon EC2 Key Pairs
        <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html>`__ in the
        *Amazon Elastic Compute Cloud User Guide for Linux Instances* .

      - **sourceSecurityGroups** *(list) --*

        The security groups to allow SSH access (port 22) from on the worker nodes. If you
        specify an Amazon EC2 SSH key, but you do not specify a source security group when you
        create a managed node group, port 22 on the worker nodes is opened to the internet
        (0.0.0.0/0). For more information, see `Security Groups for Your VPC
        <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ in the
        *Amazon Virtual Private Cloud User Guide* .

        - *(string) --*

    - **amiType** *(string) --*

      The AMI type associated with your node group. GPU instance types should use the
      ``AL2_x86_64_GPU`` AMI type, which uses the Amazon EKS-optimized Linux AMI with GPU
      support; non-GPU instances should use the ``AL2_x86_64`` AMI type, which uses the Amazon
      EKS-optimized Linux AMI.

    - **nodeRole** *(string) --*

      The IAM role associated with your node group. The Amazon EKS worker node ``kubelet`` daemon
      makes calls to AWS APIs on your behalf. Worker nodes receive permissions for these API
      calls through an IAM instance profile and associated policies. Before you can launch worker
      nodes and register them into a cluster, you must create an IAM role for those worker nodes
      to use when they are launched. For more information, see `Amazon EKS Worker Node IAM Role
      <https://docs.aws.amazon.com/eks/latest/userguide/worker_node_IAM_role.html>`__ in the *
      *Amazon EKS User Guide* * .

    - **labels** *(dict) --*

      The Kubernetes labels applied to the nodes in the node group.

      .. note::

        Only labels that are applied with the Amazon EKS API are shown here. There may be other
        Kubernetes labels applied to the nodes in this group.

      - *(string) --*

        - *(string) --*

    - **resources** *(dict) --*

      The resources associated with the nodegroup, such as AutoScaling groups and security groups
      for remote access.

      - **autoScalingGroups** *(list) --*

        The autoscaling groups associated with the node group.

        - *(dict) --*

          An AutoScaling group that is associated with an Amazon EKS managed node group.

          - **name** *(string) --*

            The name of the AutoScaling group associated with an Amazon EKS managed node group.

      - **remoteAccessSecurityGroup** *(string) --*

        The remote access security group associated with the node group. This security group
        controls SSH access to the worker nodes.

    - **diskSize** *(integer) --*

      The root device disk size (in GiB) for your node group instances. The default disk size is
      20 GiB.

    - **health** *(dict) --*

      The health status of the node group. If there are issues with your node group's health,
      they are listed here.

      - **issues** *(list) --*

        Any issues that are associated with the node group.

        - *(dict) --*

          An object representing an issue with an Amazon EKS resource.

          - **code** *(string) --*

            A brief description of the error.

            * **AutoScalingGroupNotFound** : We couldn't find the Auto Scaling group associated
            with the managed node group. You may be able to recreate an Auto Scaling group with
            the same settings to recover.

            * **Ec2SecurityGroupNotFound** : We couldn't find the cluster security group for the
            cluster. You must recreate your cluster.

            * **Ec2SecurityGroupDeletionFailure** : We could not delete the remote access
            security group for your managed node group. Remove any dependencies from the security
            group.

            * **Ec2LaunchTemplateNotFound** : We couldn't find the Amazon EC2 launch template for
            your managed node group. You may be able to recreate a launch template with the same
            settings to recover.

            * **Ec2LaunchTemplateVersionMismatch** : The Amazon EC2 launch template version for
            your managed node group does not match the version that Amazon EKS created. You may
            be able to revert to the Amazon EKS-created version to recover.

            * **IamInstanceProfileNotFound** : We couldn't find the IAM instance profile for your
            managed node group. You may be able to recreate an instance profile with the same
            settings to recover.

            * **IamNodeRoleNotFound** : We couldn't find the IAM role for your managed node
            group. You may be able to recreate an IAM role with the same settings to recover.

            * **AsgInstanceLaunchFailures** : Your Auto Scaling group is experiencing failures
            while attempting to launch instances.

            * **InstanceLimitExceeded** : Your AWS account is unable to launch any more instances
            of the specified instance type. You may be able to request an Amazon EC2 instance
            limit increase to recover.

            * **InsufficientFreeAddresses** : One or more of the subnets associated with your
            managed node group does not have enough available IP addresses for new nodes.

            * **AccessDenied** : Amazon EKS and or one or more of your managed nodes is unable to
            communicate with your cluster API server.

            * **InternalFailure** : These errors are usually caused by an Amazon EKS server-side
            issue.

          - **message** *(string) --*

            The error message associated with the issue.

          - **resourceIds** *(list) --*

            The AWS resources that are afflicted by this issue.

            - *(string) --*

    - **tags** *(dict) --*

      The metadata applied the node group to assist with categorization and organization. Each
      tag consists of a key and an optional value, both of which you define. Node group tags do
      not propagate to any other resources associated with the node group, such as the Amazon EC2
      instances or subnets.

      - *(string) --*

        - *(string) --*
    """


_ClientCreateNodegroupResponseTypeDef = TypedDict(
    "_ClientCreateNodegroupResponseTypeDef",
    {"nodegroup": ClientCreateNodegroupResponsenodegroupTypeDef},
    total=False,
)


class ClientCreateNodegroupResponseTypeDef(_ClientCreateNodegroupResponseTypeDef):
    """
    Type definition for `ClientCreateNodegroup` `Response`

    - **nodegroup** *(dict) --*

      The full description of your new node group.

      - **nodegroupName** *(string) --*

        The name associated with an Amazon EKS managed node group.

      - **nodegroupArn** *(string) --*

        The Amazon Resource Name (ARN) associated with the managed node group.

      - **clusterName** *(string) --*

        The name of the cluster that the managed node group resides in.

      - **version** *(string) --*

        The Kubernetes version of the managed node group.

      - **releaseVersion** *(string) --*

        The AMI version of the managed node group. For more information, see `Amazon EKS-Optimized
        Linux AMI Versions
        <https://docs.aws.amazon.com/eks/latest/userguide/eks-linux-ami-versions.html>`__ in the
        *Amazon EKS User Guide* .

      - **createdAt** *(datetime) --*

        The Unix epoch timestamp in seconds for when the managed node group was created.

      - **modifiedAt** *(datetime) --*

        The Unix epoch timestamp in seconds for when the managed node group was last modified.

      - **status** *(string) --*

        The current status of the managed node group.

      - **scalingConfig** *(dict) --*

        The scaling configuration details for the AutoScaling group that is associated with your
        node group.

        - **minSize** *(integer) --*

          The minimum number of worker nodes that the managed node group can scale in to. This
          number must be greater than zero.

        - **maxSize** *(integer) --*

          The maximum number of worker nodes that the managed node group can scale out to. Managed
          node groups can support up to 100 nodes by default.

        - **desiredSize** *(integer) --*

          The current number of worker nodes that the managed node group should maintain.

      - **instanceTypes** *(list) --*

        The instance types associated with your node group.

        - *(string) --*

      - **subnets** *(list) --*

        The subnets allowed for the AutoScaling group that is associated with your node group.
        These subnets must have the following tag: ``kubernetes.io/cluster/CLUSTER_NAME`` , where
        ``CLUSTER_NAME`` is replaced with the name of your cluster.

        - *(string) --*

      - **remoteAccess** *(dict) --*

        The remote access (SSH) configuration that is associated with the node group.

        - **ec2SshKey** *(string) --*

          The Amazon EC2 SSH key that provides access for SSH communication with the worker nodes
          in the managed node group. For more information, see `Amazon EC2 Key Pairs
          <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html>`__ in the
          *Amazon Elastic Compute Cloud User Guide for Linux Instances* .

        - **sourceSecurityGroups** *(list) --*

          The security groups to allow SSH access (port 22) from on the worker nodes. If you
          specify an Amazon EC2 SSH key, but you do not specify a source security group when you
          create a managed node group, port 22 on the worker nodes is opened to the internet
          (0.0.0.0/0). For more information, see `Security Groups for Your VPC
          <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ in the
          *Amazon Virtual Private Cloud User Guide* .

          - *(string) --*

      - **amiType** *(string) --*

        The AMI type associated with your node group. GPU instance types should use the
        ``AL2_x86_64_GPU`` AMI type, which uses the Amazon EKS-optimized Linux AMI with GPU
        support; non-GPU instances should use the ``AL2_x86_64`` AMI type, which uses the Amazon
        EKS-optimized Linux AMI.

      - **nodeRole** *(string) --*

        The IAM role associated with your node group. The Amazon EKS worker node ``kubelet`` daemon
        makes calls to AWS APIs on your behalf. Worker nodes receive permissions for these API
        calls through an IAM instance profile and associated policies. Before you can launch worker
        nodes and register them into a cluster, you must create an IAM role for those worker nodes
        to use when they are launched. For more information, see `Amazon EKS Worker Node IAM Role
        <https://docs.aws.amazon.com/eks/latest/userguide/worker_node_IAM_role.html>`__ in the *
        *Amazon EKS User Guide* * .

      - **labels** *(dict) --*

        The Kubernetes labels applied to the nodes in the node group.

        .. note::

          Only labels that are applied with the Amazon EKS API are shown here. There may be other
          Kubernetes labels applied to the nodes in this group.

        - *(string) --*

          - *(string) --*

      - **resources** *(dict) --*

        The resources associated with the nodegroup, such as AutoScaling groups and security groups
        for remote access.

        - **autoScalingGroups** *(list) --*

          The autoscaling groups associated with the node group.

          - *(dict) --*

            An AutoScaling group that is associated with an Amazon EKS managed node group.

            - **name** *(string) --*

              The name of the AutoScaling group associated with an Amazon EKS managed node group.

        - **remoteAccessSecurityGroup** *(string) --*

          The remote access security group associated with the node group. This security group
          controls SSH access to the worker nodes.

      - **diskSize** *(integer) --*

        The root device disk size (in GiB) for your node group instances. The default disk size is
        20 GiB.

      - **health** *(dict) --*

        The health status of the node group. If there are issues with your node group's health,
        they are listed here.

        - **issues** *(list) --*

          Any issues that are associated with the node group.

          - *(dict) --*

            An object representing an issue with an Amazon EKS resource.

            - **code** *(string) --*

              A brief description of the error.

              * **AutoScalingGroupNotFound** : We couldn't find the Auto Scaling group associated
              with the managed node group. You may be able to recreate an Auto Scaling group with
              the same settings to recover.

              * **Ec2SecurityGroupNotFound** : We couldn't find the cluster security group for the
              cluster. You must recreate your cluster.

              * **Ec2SecurityGroupDeletionFailure** : We could not delete the remote access
              security group for your managed node group. Remove any dependencies from the security
              group.

              * **Ec2LaunchTemplateNotFound** : We couldn't find the Amazon EC2 launch template for
              your managed node group. You may be able to recreate a launch template with the same
              settings to recover.

              * **Ec2LaunchTemplateVersionMismatch** : The Amazon EC2 launch template version for
              your managed node group does not match the version that Amazon EKS created. You may
              be able to revert to the Amazon EKS-created version to recover.

              * **IamInstanceProfileNotFound** : We couldn't find the IAM instance profile for your
              managed node group. You may be able to recreate an instance profile with the same
              settings to recover.

              * **IamNodeRoleNotFound** : We couldn't find the IAM role for your managed node
              group. You may be able to recreate an IAM role with the same settings to recover.

              * **AsgInstanceLaunchFailures** : Your Auto Scaling group is experiencing failures
              while attempting to launch instances.

              * **InstanceLimitExceeded** : Your AWS account is unable to launch any more instances
              of the specified instance type. You may be able to request an Amazon EC2 instance
              limit increase to recover.

              * **InsufficientFreeAddresses** : One or more of the subnets associated with your
              managed node group does not have enough available IP addresses for new nodes.

              * **AccessDenied** : Amazon EKS and or one or more of your managed nodes is unable to
              communicate with your cluster API server.

              * **InternalFailure** : These errors are usually caused by an Amazon EKS server-side
              issue.

            - **message** *(string) --*

              The error message associated with the issue.

            - **resourceIds** *(list) --*

              The AWS resources that are afflicted by this issue.

              - *(string) --*

      - **tags** *(dict) --*

        The metadata applied the node group to assist with categorization and organization. Each
        tag consists of a key and an optional value, both of which you define. Node group tags do
        not propagate to any other resources associated with the node group, such as the Amazon EC2
        instances or subnets.

        - *(string) --*

          - *(string) --*
    """


_ClientCreateNodegroupremoteAccessTypeDef = TypedDict(
    "_ClientCreateNodegroupremoteAccessTypeDef",
    {"ec2SshKey": str, "sourceSecurityGroups": List[str]},
    total=False,
)


class ClientCreateNodegroupremoteAccessTypeDef(
    _ClientCreateNodegroupremoteAccessTypeDef
):
    """
    Type definition for `ClientCreateNodegroup` `remoteAccess`

    The remote access (SSH) configuration to use with your node group.

    - **ec2SshKey** *(string) --*

      The Amazon EC2 SSH key that provides access for SSH communication with the worker nodes in the
      managed node group. For more information, see `Amazon EC2 Key Pairs
      <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html>`__ in the *Amazon
      Elastic Compute Cloud User Guide for Linux Instances* .

    - **sourceSecurityGroups** *(list) --*

      The security groups to allow SSH access (port 22) from on the worker nodes. If you specify an
      Amazon EC2 SSH key, but you do not specify a source security group when you create a managed
      node group, port 22 on the worker nodes is opened to the internet (0.0.0.0/0). For more
      information, see `Security Groups for Your VPC
      <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ in the *Amazon
      Virtual Private Cloud User Guide* .

      - *(string) --*
    """


_ClientCreateNodegroupscalingConfigTypeDef = TypedDict(
    "_ClientCreateNodegroupscalingConfigTypeDef",
    {"minSize": int, "maxSize": int, "desiredSize": int},
    total=False,
)


class ClientCreateNodegroupscalingConfigTypeDef(
    _ClientCreateNodegroupscalingConfigTypeDef
):
    """
    Type definition for `ClientCreateNodegroup` `scalingConfig`

    The scaling configuration details for the AutoScaling group that is created for your node group.

    - **minSize** *(integer) --*

      The minimum number of worker nodes that the managed node group can scale in to. This number
      must be greater than zero.

    - **maxSize** *(integer) --*

      The maximum number of worker nodes that the managed node group can scale out to. Managed node
      groups can support up to 100 nodes by default.

    - **desiredSize** *(integer) --*

      The current number of worker nodes that the managed node group should maintain.
    """


_ClientDeleteClusterResponseclustercertificateAuthorityTypeDef = TypedDict(
    "_ClientDeleteClusterResponseclustercertificateAuthorityTypeDef",
    {"data": str},
    total=False,
)


class ClientDeleteClusterResponseclustercertificateAuthorityTypeDef(
    _ClientDeleteClusterResponseclustercertificateAuthorityTypeDef
):
    """
    Type definition for `ClientDeleteClusterResponsecluster` `certificateAuthority`

    The ``certificate-authority-data`` for your cluster.

    - **data** *(string) --*

      The Base64-encoded certificate data required to communicate with your cluster. Add this
      to the ``certificate-authority-data`` section of the ``kubeconfig`` file for your cluster.
    """


_ClientDeleteClusterResponseclusteridentityoidcTypeDef = TypedDict(
    "_ClientDeleteClusterResponseclusteridentityoidcTypeDef",
    {"issuer": str},
    total=False,
)


class ClientDeleteClusterResponseclusteridentityoidcTypeDef(
    _ClientDeleteClusterResponseclusteridentityoidcTypeDef
):
    """
    Type definition for `ClientDeleteClusterResponseclusteridentity` `oidc`

    The `OpenID Connect <https://openid.net/connect/>`__ identity provider information for
    the cluster.

    - **issuer** *(string) --*

      The issuer URL for the OpenID Connect identity provider.
    """


_ClientDeleteClusterResponseclusteridentityTypeDef = TypedDict(
    "_ClientDeleteClusterResponseclusteridentityTypeDef",
    {"oidc": ClientDeleteClusterResponseclusteridentityoidcTypeDef},
    total=False,
)


class ClientDeleteClusterResponseclusteridentityTypeDef(
    _ClientDeleteClusterResponseclusteridentityTypeDef
):
    """
    Type definition for `ClientDeleteClusterResponsecluster` `identity`

    The identity provider information for the cluster.

    - **oidc** *(dict) --*

      The `OpenID Connect <https://openid.net/connect/>`__ identity provider information for
      the cluster.

      - **issuer** *(string) --*

        The issuer URL for the OpenID Connect identity provider.
    """


_ClientDeleteClusterResponseclusterloggingclusterLoggingTypeDef = TypedDict(
    "_ClientDeleteClusterResponseclusterloggingclusterLoggingTypeDef",
    {"types": List[str], "enabled": bool},
    total=False,
)


class ClientDeleteClusterResponseclusterloggingclusterLoggingTypeDef(
    _ClientDeleteClusterResponseclusterloggingclusterLoggingTypeDef
):
    """
    Type definition for `ClientDeleteClusterResponseclusterlogging` `clusterLogging`

    An object representing the enabled or disabled Kubernetes control plane logs for your
    cluster.

    - **types** *(list) --*

      The available cluster control plane log types.

      - *(string) --*

    - **enabled** *(boolean) --*

      If a log type is enabled, that log type exports its control plane logs to CloudWatch
      Logs. If a log type isn't enabled, that log type doesn't export its control plane
      logs. Each individual log type can be enabled or disabled independently.
    """


_ClientDeleteClusterResponseclusterloggingTypeDef = TypedDict(
    "_ClientDeleteClusterResponseclusterloggingTypeDef",
    {
        "clusterLogging": List[
            ClientDeleteClusterResponseclusterloggingclusterLoggingTypeDef
        ]
    },
    total=False,
)


class ClientDeleteClusterResponseclusterloggingTypeDef(
    _ClientDeleteClusterResponseclusterloggingTypeDef
):
    """
    Type definition for `ClientDeleteClusterResponsecluster` `logging`

    The logging configuration for your cluster.

    - **clusterLogging** *(list) --*

      The cluster control plane logging configuration for your cluster.

      - *(dict) --*

        An object representing the enabled or disabled Kubernetes control plane logs for your
        cluster.

        - **types** *(list) --*

          The available cluster control plane log types.

          - *(string) --*

        - **enabled** *(boolean) --*

          If a log type is enabled, that log type exports its control plane logs to CloudWatch
          Logs. If a log type isn't enabled, that log type doesn't export its control plane
          logs. Each individual log type can be enabled or disabled independently.
    """


_ClientDeleteClusterResponseclusterresourcesVpcConfigTypeDef = TypedDict(
    "_ClientDeleteClusterResponseclusterresourcesVpcConfigTypeDef",
    {
        "subnetIds": List[str],
        "securityGroupIds": List[str],
        "clusterSecurityGroupId": str,
        "vpcId": str,
        "endpointPublicAccess": bool,
        "endpointPrivateAccess": bool,
    },
    total=False,
)


class ClientDeleteClusterResponseclusterresourcesVpcConfigTypeDef(
    _ClientDeleteClusterResponseclusterresourcesVpcConfigTypeDef
):
    """
    Type definition for `ClientDeleteClusterResponsecluster` `resourcesVpcConfig`

    The VPC configuration used by the cluster control plane. Amazon EKS VPC resources have
    specific requirements to work properly with Kubernetes. For more information, see `Cluster
    VPC Considerations <https://docs.aws.amazon.com/eks/latest/userguide/network_reqs.html>`__
    and `Cluster Security Group Considerations
    <https://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html>`__ in the *Amazon
    EKS User Guide* .

    - **subnetIds** *(list) --*

      The subnets associated with your cluster.

      - *(string) --*

    - **securityGroupIds** *(list) --*

      The security groups associated with the cross-account elastic network interfaces that are
      used to allow communication between your worker nodes and the Kubernetes control plane.

      - *(string) --*

    - **clusterSecurityGroupId** *(string) --*

      The cluster security group that was created by Amazon EKS for the cluster. Managed node
      groups use this security group for control plane to data plane communication.

    - **vpcId** *(string) --*

      The VPC associated with your cluster.

    - **endpointPublicAccess** *(boolean) --*

      This parameter indicates whether the Amazon EKS public API server endpoint is enabled. If
      the Amazon EKS public API server endpoint is disabled, your cluster's Kubernetes API
      server can receive only requests that originate from within the cluster VPC.

    - **endpointPrivateAccess** *(boolean) --*

      This parameter indicates whether the Amazon EKS private API server endpoint is enabled.
      If the Amazon EKS private API server endpoint is enabled, Kubernetes API requests that
      originate from within your cluster's VPC use the private VPC endpoint instead of
      traversing the internet.
    """


_ClientDeleteClusterResponseclusterTypeDef = TypedDict(
    "_ClientDeleteClusterResponseclusterTypeDef",
    {
        "name": str,
        "arn": str,
        "createdAt": datetime,
        "version": str,
        "endpoint": str,
        "roleArn": str,
        "resourcesVpcConfig": ClientDeleteClusterResponseclusterresourcesVpcConfigTypeDef,
        "logging": ClientDeleteClusterResponseclusterloggingTypeDef,
        "identity": ClientDeleteClusterResponseclusteridentityTypeDef,
        "status": str,
        "certificateAuthority": ClientDeleteClusterResponseclustercertificateAuthorityTypeDef,
        "clientRequestToken": str,
        "platformVersion": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientDeleteClusterResponseclusterTypeDef(
    _ClientDeleteClusterResponseclusterTypeDef
):
    """
    Type definition for `ClientDeleteClusterResponse` `cluster`

    The full description of the cluster to delete.

    - **name** *(string) --*

      The name of the cluster.

    - **arn** *(string) --*

      The Amazon Resource Name (ARN) of the cluster.

    - **createdAt** *(datetime) --*

      The Unix epoch timestamp in seconds for when the cluster was created.

    - **version** *(string) --*

      The Kubernetes server version for the cluster.

    - **endpoint** *(string) --*

      The endpoint for your Kubernetes API server.

    - **roleArn** *(string) --*

      The Amazon Resource Name (ARN) of the IAM role that provides permissions for the Kubernetes
      control plane to make calls to AWS API operations on your behalf.

    - **resourcesVpcConfig** *(dict) --*

      The VPC configuration used by the cluster control plane. Amazon EKS VPC resources have
      specific requirements to work properly with Kubernetes. For more information, see `Cluster
      VPC Considerations <https://docs.aws.amazon.com/eks/latest/userguide/network_reqs.html>`__
      and `Cluster Security Group Considerations
      <https://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html>`__ in the *Amazon
      EKS User Guide* .

      - **subnetIds** *(list) --*

        The subnets associated with your cluster.

        - *(string) --*

      - **securityGroupIds** *(list) --*

        The security groups associated with the cross-account elastic network interfaces that are
        used to allow communication between your worker nodes and the Kubernetes control plane.

        - *(string) --*

      - **clusterSecurityGroupId** *(string) --*

        The cluster security group that was created by Amazon EKS for the cluster. Managed node
        groups use this security group for control plane to data plane communication.

      - **vpcId** *(string) --*

        The VPC associated with your cluster.

      - **endpointPublicAccess** *(boolean) --*

        This parameter indicates whether the Amazon EKS public API server endpoint is enabled. If
        the Amazon EKS public API server endpoint is disabled, your cluster's Kubernetes API
        server can receive only requests that originate from within the cluster VPC.

      - **endpointPrivateAccess** *(boolean) --*

        This parameter indicates whether the Amazon EKS private API server endpoint is enabled.
        If the Amazon EKS private API server endpoint is enabled, Kubernetes API requests that
        originate from within your cluster's VPC use the private VPC endpoint instead of
        traversing the internet.

    - **logging** *(dict) --*

      The logging configuration for your cluster.

      - **clusterLogging** *(list) --*

        The cluster control plane logging configuration for your cluster.

        - *(dict) --*

          An object representing the enabled or disabled Kubernetes control plane logs for your
          cluster.

          - **types** *(list) --*

            The available cluster control plane log types.

            - *(string) --*

          - **enabled** *(boolean) --*

            If a log type is enabled, that log type exports its control plane logs to CloudWatch
            Logs. If a log type isn't enabled, that log type doesn't export its control plane
            logs. Each individual log type can be enabled or disabled independently.

    - **identity** *(dict) --*

      The identity provider information for the cluster.

      - **oidc** *(dict) --*

        The `OpenID Connect <https://openid.net/connect/>`__ identity provider information for
        the cluster.

        - **issuer** *(string) --*

          The issuer URL for the OpenID Connect identity provider.

    - **status** *(string) --*

      The current status of the cluster.

    - **certificateAuthority** *(dict) --*

      The ``certificate-authority-data`` for your cluster.

      - **data** *(string) --*

        The Base64-encoded certificate data required to communicate with your cluster. Add this
        to the ``certificate-authority-data`` section of the ``kubeconfig`` file for your cluster.

    - **clientRequestToken** *(string) --*

      Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

    - **platformVersion** *(string) --*

      The platform version of your Amazon EKS cluster. For more information, see `Platform
      Versions <https://docs.aws.amazon.com/eks/latest/userguide/platform-versions.html>`__ in
      the * *Amazon EKS User Guide* * .

    - **tags** *(dict) --*

      The metadata that you apply to the cluster to assist with categorization and organization.
      Each tag consists of a key and an optional value, both of which you define. Cluster tags do
      not propagate to any other resources associated with the cluster.

      - *(string) --*

        - *(string) --*
    """


_ClientDeleteClusterResponseTypeDef = TypedDict(
    "_ClientDeleteClusterResponseTypeDef",
    {"cluster": ClientDeleteClusterResponseclusterTypeDef},
    total=False,
)


class ClientDeleteClusterResponseTypeDef(_ClientDeleteClusterResponseTypeDef):
    """
    Type definition for `ClientDeleteCluster` `Response`

    - **cluster** *(dict) --*

      The full description of the cluster to delete.

      - **name** *(string) --*

        The name of the cluster.

      - **arn** *(string) --*

        The Amazon Resource Name (ARN) of the cluster.

      - **createdAt** *(datetime) --*

        The Unix epoch timestamp in seconds for when the cluster was created.

      - **version** *(string) --*

        The Kubernetes server version for the cluster.

      - **endpoint** *(string) --*

        The endpoint for your Kubernetes API server.

      - **roleArn** *(string) --*

        The Amazon Resource Name (ARN) of the IAM role that provides permissions for the Kubernetes
        control plane to make calls to AWS API operations on your behalf.

      - **resourcesVpcConfig** *(dict) --*

        The VPC configuration used by the cluster control plane. Amazon EKS VPC resources have
        specific requirements to work properly with Kubernetes. For more information, see `Cluster
        VPC Considerations <https://docs.aws.amazon.com/eks/latest/userguide/network_reqs.html>`__
        and `Cluster Security Group Considerations
        <https://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html>`__ in the *Amazon
        EKS User Guide* .

        - **subnetIds** *(list) --*

          The subnets associated with your cluster.

          - *(string) --*

        - **securityGroupIds** *(list) --*

          The security groups associated with the cross-account elastic network interfaces that are
          used to allow communication between your worker nodes and the Kubernetes control plane.

          - *(string) --*

        - **clusterSecurityGroupId** *(string) --*

          The cluster security group that was created by Amazon EKS for the cluster. Managed node
          groups use this security group for control plane to data plane communication.

        - **vpcId** *(string) --*

          The VPC associated with your cluster.

        - **endpointPublicAccess** *(boolean) --*

          This parameter indicates whether the Amazon EKS public API server endpoint is enabled. If
          the Amazon EKS public API server endpoint is disabled, your cluster's Kubernetes API
          server can receive only requests that originate from within the cluster VPC.

        - **endpointPrivateAccess** *(boolean) --*

          This parameter indicates whether the Amazon EKS private API server endpoint is enabled.
          If the Amazon EKS private API server endpoint is enabled, Kubernetes API requests that
          originate from within your cluster's VPC use the private VPC endpoint instead of
          traversing the internet.

      - **logging** *(dict) --*

        The logging configuration for your cluster.

        - **clusterLogging** *(list) --*

          The cluster control plane logging configuration for your cluster.

          - *(dict) --*

            An object representing the enabled or disabled Kubernetes control plane logs for your
            cluster.

            - **types** *(list) --*

              The available cluster control plane log types.

              - *(string) --*

            - **enabled** *(boolean) --*

              If a log type is enabled, that log type exports its control plane logs to CloudWatch
              Logs. If a log type isn't enabled, that log type doesn't export its control plane
              logs. Each individual log type can be enabled or disabled independently.

      - **identity** *(dict) --*

        The identity provider information for the cluster.

        - **oidc** *(dict) --*

          The `OpenID Connect <https://openid.net/connect/>`__ identity provider information for
          the cluster.

          - **issuer** *(string) --*

            The issuer URL for the OpenID Connect identity provider.

      - **status** *(string) --*

        The current status of the cluster.

      - **certificateAuthority** *(dict) --*

        The ``certificate-authority-data`` for your cluster.

        - **data** *(string) --*

          The Base64-encoded certificate data required to communicate with your cluster. Add this
          to the ``certificate-authority-data`` section of the ``kubeconfig`` file for your cluster.

      - **clientRequestToken** *(string) --*

        Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

      - **platformVersion** *(string) --*

        The platform version of your Amazon EKS cluster. For more information, see `Platform
        Versions <https://docs.aws.amazon.com/eks/latest/userguide/platform-versions.html>`__ in
        the * *Amazon EKS User Guide* * .

      - **tags** *(dict) --*

        The metadata that you apply to the cluster to assist with categorization and organization.
        Each tag consists of a key and an optional value, both of which you define. Cluster tags do
        not propagate to any other resources associated with the cluster.

        - *(string) --*

          - *(string) --*
    """


_ClientDeleteNodegroupResponsenodegrouphealthissuesTypeDef = TypedDict(
    "_ClientDeleteNodegroupResponsenodegrouphealthissuesTypeDef",
    {"code": str, "message": str, "resourceIds": List[str]},
    total=False,
)


class ClientDeleteNodegroupResponsenodegrouphealthissuesTypeDef(
    _ClientDeleteNodegroupResponsenodegrouphealthissuesTypeDef
):
    """
    Type definition for `ClientDeleteNodegroupResponsenodegrouphealth` `issues`

    An object representing an issue with an Amazon EKS resource.

    - **code** *(string) --*

      A brief description of the error.

      * **AutoScalingGroupNotFound** : We couldn't find the Auto Scaling group associated
      with the managed node group. You may be able to recreate an Auto Scaling group with
      the same settings to recover.

      * **Ec2SecurityGroupNotFound** : We couldn't find the cluster security group for the
      cluster. You must recreate your cluster.

      * **Ec2SecurityGroupDeletionFailure** : We could not delete the remote access
      security group for your managed node group. Remove any dependencies from the security
      group.

      * **Ec2LaunchTemplateNotFound** : We couldn't find the Amazon EC2 launch template for
      your managed node group. You may be able to recreate a launch template with the same
      settings to recover.

      * **Ec2LaunchTemplateVersionMismatch** : The Amazon EC2 launch template version for
      your managed node group does not match the version that Amazon EKS created. You may
      be able to revert to the Amazon EKS-created version to recover.

      * **IamInstanceProfileNotFound** : We couldn't find the IAM instance profile for your
      managed node group. You may be able to recreate an instance profile with the same
      settings to recover.

      * **IamNodeRoleNotFound** : We couldn't find the IAM role for your managed node
      group. You may be able to recreate an IAM role with the same settings to recover.

      * **AsgInstanceLaunchFailures** : Your Auto Scaling group is experiencing failures
      while attempting to launch instances.

      * **InstanceLimitExceeded** : Your AWS account is unable to launch any more instances
      of the specified instance type. You may be able to request an Amazon EC2 instance
      limit increase to recover.

      * **InsufficientFreeAddresses** : One or more of the subnets associated with your
      managed node group does not have enough available IP addresses for new nodes.

      * **AccessDenied** : Amazon EKS and or one or more of your managed nodes is unable to
      communicate with your cluster API server.

      * **InternalFailure** : These errors are usually caused by an Amazon EKS server-side
      issue.

    - **message** *(string) --*

      The error message associated with the issue.

    - **resourceIds** *(list) --*

      The AWS resources that are afflicted by this issue.

      - *(string) --*
    """


_ClientDeleteNodegroupResponsenodegrouphealthTypeDef = TypedDict(
    "_ClientDeleteNodegroupResponsenodegrouphealthTypeDef",
    {"issues": List[ClientDeleteNodegroupResponsenodegrouphealthissuesTypeDef]},
    total=False,
)


class ClientDeleteNodegroupResponsenodegrouphealthTypeDef(
    _ClientDeleteNodegroupResponsenodegrouphealthTypeDef
):
    """
    Type definition for `ClientDeleteNodegroupResponsenodegroup` `health`

    The health status of the node group. If there are issues with your node group's health,
    they are listed here.

    - **issues** *(list) --*

      Any issues that are associated with the node group.

      - *(dict) --*

        An object representing an issue with an Amazon EKS resource.

        - **code** *(string) --*

          A brief description of the error.

          * **AutoScalingGroupNotFound** : We couldn't find the Auto Scaling group associated
          with the managed node group. You may be able to recreate an Auto Scaling group with
          the same settings to recover.

          * **Ec2SecurityGroupNotFound** : We couldn't find the cluster security group for the
          cluster. You must recreate your cluster.

          * **Ec2SecurityGroupDeletionFailure** : We could not delete the remote access
          security group for your managed node group. Remove any dependencies from the security
          group.

          * **Ec2LaunchTemplateNotFound** : We couldn't find the Amazon EC2 launch template for
          your managed node group. You may be able to recreate a launch template with the same
          settings to recover.

          * **Ec2LaunchTemplateVersionMismatch** : The Amazon EC2 launch template version for
          your managed node group does not match the version that Amazon EKS created. You may
          be able to revert to the Amazon EKS-created version to recover.

          * **IamInstanceProfileNotFound** : We couldn't find the IAM instance profile for your
          managed node group. You may be able to recreate an instance profile with the same
          settings to recover.

          * **IamNodeRoleNotFound** : We couldn't find the IAM role for your managed node
          group. You may be able to recreate an IAM role with the same settings to recover.

          * **AsgInstanceLaunchFailures** : Your Auto Scaling group is experiencing failures
          while attempting to launch instances.

          * **InstanceLimitExceeded** : Your AWS account is unable to launch any more instances
          of the specified instance type. You may be able to request an Amazon EC2 instance
          limit increase to recover.

          * **InsufficientFreeAddresses** : One or more of the subnets associated with your
          managed node group does not have enough available IP addresses for new nodes.

          * **AccessDenied** : Amazon EKS and or one or more of your managed nodes is unable to
          communicate with your cluster API server.

          * **InternalFailure** : These errors are usually caused by an Amazon EKS server-side
          issue.

        - **message** *(string) --*

          The error message associated with the issue.

        - **resourceIds** *(list) --*

          The AWS resources that are afflicted by this issue.

          - *(string) --*
    """


_ClientDeleteNodegroupResponsenodegroupremoteAccessTypeDef = TypedDict(
    "_ClientDeleteNodegroupResponsenodegroupremoteAccessTypeDef",
    {"ec2SshKey": str, "sourceSecurityGroups": List[str]},
    total=False,
)


class ClientDeleteNodegroupResponsenodegroupremoteAccessTypeDef(
    _ClientDeleteNodegroupResponsenodegroupremoteAccessTypeDef
):
    """
    Type definition for `ClientDeleteNodegroupResponsenodegroup` `remoteAccess`

    The remote access (SSH) configuration that is associated with the node group.

    - **ec2SshKey** *(string) --*

      The Amazon EC2 SSH key that provides access for SSH communication with the worker nodes
      in the managed node group. For more information, see `Amazon EC2 Key Pairs
      <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html>`__ in the
      *Amazon Elastic Compute Cloud User Guide for Linux Instances* .

    - **sourceSecurityGroups** *(list) --*

      The security groups to allow SSH access (port 22) from on the worker nodes. If you
      specify an Amazon EC2 SSH key, but you do not specify a source security group when you
      create a managed node group, port 22 on the worker nodes is opened to the internet
      (0.0.0.0/0). For more information, see `Security Groups for Your VPC
      <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ in the
      *Amazon Virtual Private Cloud User Guide* .

      - *(string) --*
    """


_ClientDeleteNodegroupResponsenodegroupresourcesautoScalingGroupsTypeDef = TypedDict(
    "_ClientDeleteNodegroupResponsenodegroupresourcesautoScalingGroupsTypeDef",
    {"name": str},
    total=False,
)


class ClientDeleteNodegroupResponsenodegroupresourcesautoScalingGroupsTypeDef(
    _ClientDeleteNodegroupResponsenodegroupresourcesautoScalingGroupsTypeDef
):
    """
    Type definition for `ClientDeleteNodegroupResponsenodegroupresources` `autoScalingGroups`

    An AutoScaling group that is associated with an Amazon EKS managed node group.

    - **name** *(string) --*

      The name of the AutoScaling group associated with an Amazon EKS managed node group.
    """


_ClientDeleteNodegroupResponsenodegroupresourcesTypeDef = TypedDict(
    "_ClientDeleteNodegroupResponsenodegroupresourcesTypeDef",
    {
        "autoScalingGroups": List[
            ClientDeleteNodegroupResponsenodegroupresourcesautoScalingGroupsTypeDef
        ],
        "remoteAccessSecurityGroup": str,
    },
    total=False,
)


class ClientDeleteNodegroupResponsenodegroupresourcesTypeDef(
    _ClientDeleteNodegroupResponsenodegroupresourcesTypeDef
):
    """
    Type definition for `ClientDeleteNodegroupResponsenodegroup` `resources`

    The resources associated with the nodegroup, such as AutoScaling groups and security groups
    for remote access.

    - **autoScalingGroups** *(list) --*

      The autoscaling groups associated with the node group.

      - *(dict) --*

        An AutoScaling group that is associated with an Amazon EKS managed node group.

        - **name** *(string) --*

          The name of the AutoScaling group associated with an Amazon EKS managed node group.

    - **remoteAccessSecurityGroup** *(string) --*

      The remote access security group associated with the node group. This security group
      controls SSH access to the worker nodes.
    """


_ClientDeleteNodegroupResponsenodegroupscalingConfigTypeDef = TypedDict(
    "_ClientDeleteNodegroupResponsenodegroupscalingConfigTypeDef",
    {"minSize": int, "maxSize": int, "desiredSize": int},
    total=False,
)


class ClientDeleteNodegroupResponsenodegroupscalingConfigTypeDef(
    _ClientDeleteNodegroupResponsenodegroupscalingConfigTypeDef
):
    """
    Type definition for `ClientDeleteNodegroupResponsenodegroup` `scalingConfig`

    The scaling configuration details for the AutoScaling group that is associated with your
    node group.

    - **minSize** *(integer) --*

      The minimum number of worker nodes that the managed node group can scale in to. This
      number must be greater than zero.

    - **maxSize** *(integer) --*

      The maximum number of worker nodes that the managed node group can scale out to. Managed
      node groups can support up to 100 nodes by default.

    - **desiredSize** *(integer) --*

      The current number of worker nodes that the managed node group should maintain.
    """


_ClientDeleteNodegroupResponsenodegroupTypeDef = TypedDict(
    "_ClientDeleteNodegroupResponsenodegroupTypeDef",
    {
        "nodegroupName": str,
        "nodegroupArn": str,
        "clusterName": str,
        "version": str,
        "releaseVersion": str,
        "createdAt": datetime,
        "modifiedAt": datetime,
        "status": str,
        "scalingConfig": ClientDeleteNodegroupResponsenodegroupscalingConfigTypeDef,
        "instanceTypes": List[str],
        "subnets": List[str],
        "remoteAccess": ClientDeleteNodegroupResponsenodegroupremoteAccessTypeDef,
        "amiType": str,
        "nodeRole": str,
        "labels": Dict[str, str],
        "resources": ClientDeleteNodegroupResponsenodegroupresourcesTypeDef,
        "diskSize": int,
        "health": ClientDeleteNodegroupResponsenodegrouphealthTypeDef,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientDeleteNodegroupResponsenodegroupTypeDef(
    _ClientDeleteNodegroupResponsenodegroupTypeDef
):
    """
    Type definition for `ClientDeleteNodegroupResponse` `nodegroup`

    The full description of your deleted node group.

    - **nodegroupName** *(string) --*

      The name associated with an Amazon EKS managed node group.

    - **nodegroupArn** *(string) --*

      The Amazon Resource Name (ARN) associated with the managed node group.

    - **clusterName** *(string) --*

      The name of the cluster that the managed node group resides in.

    - **version** *(string) --*

      The Kubernetes version of the managed node group.

    - **releaseVersion** *(string) --*

      The AMI version of the managed node group. For more information, see `Amazon EKS-Optimized
      Linux AMI Versions
      <https://docs.aws.amazon.com/eks/latest/userguide/eks-linux-ami-versions.html>`__ in the
      *Amazon EKS User Guide* .

    - **createdAt** *(datetime) --*

      The Unix epoch timestamp in seconds for when the managed node group was created.

    - **modifiedAt** *(datetime) --*

      The Unix epoch timestamp in seconds for when the managed node group was last modified.

    - **status** *(string) --*

      The current status of the managed node group.

    - **scalingConfig** *(dict) --*

      The scaling configuration details for the AutoScaling group that is associated with your
      node group.

      - **minSize** *(integer) --*

        The minimum number of worker nodes that the managed node group can scale in to. This
        number must be greater than zero.

      - **maxSize** *(integer) --*

        The maximum number of worker nodes that the managed node group can scale out to. Managed
        node groups can support up to 100 nodes by default.

      - **desiredSize** *(integer) --*

        The current number of worker nodes that the managed node group should maintain.

    - **instanceTypes** *(list) --*

      The instance types associated with your node group.

      - *(string) --*

    - **subnets** *(list) --*

      The subnets allowed for the AutoScaling group that is associated with your node group.
      These subnets must have the following tag: ``kubernetes.io/cluster/CLUSTER_NAME`` , where
      ``CLUSTER_NAME`` is replaced with the name of your cluster.

      - *(string) --*

    - **remoteAccess** *(dict) --*

      The remote access (SSH) configuration that is associated with the node group.

      - **ec2SshKey** *(string) --*

        The Amazon EC2 SSH key that provides access for SSH communication with the worker nodes
        in the managed node group. For more information, see `Amazon EC2 Key Pairs
        <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html>`__ in the
        *Amazon Elastic Compute Cloud User Guide for Linux Instances* .

      - **sourceSecurityGroups** *(list) --*

        The security groups to allow SSH access (port 22) from on the worker nodes. If you
        specify an Amazon EC2 SSH key, but you do not specify a source security group when you
        create a managed node group, port 22 on the worker nodes is opened to the internet
        (0.0.0.0/0). For more information, see `Security Groups for Your VPC
        <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ in the
        *Amazon Virtual Private Cloud User Guide* .

        - *(string) --*

    - **amiType** *(string) --*

      The AMI type associated with your node group. GPU instance types should use the
      ``AL2_x86_64_GPU`` AMI type, which uses the Amazon EKS-optimized Linux AMI with GPU
      support; non-GPU instances should use the ``AL2_x86_64`` AMI type, which uses the Amazon
      EKS-optimized Linux AMI.

    - **nodeRole** *(string) --*

      The IAM role associated with your node group. The Amazon EKS worker node ``kubelet`` daemon
      makes calls to AWS APIs on your behalf. Worker nodes receive permissions for these API
      calls through an IAM instance profile and associated policies. Before you can launch worker
      nodes and register them into a cluster, you must create an IAM role for those worker nodes
      to use when they are launched. For more information, see `Amazon EKS Worker Node IAM Role
      <https://docs.aws.amazon.com/eks/latest/userguide/worker_node_IAM_role.html>`__ in the *
      *Amazon EKS User Guide* * .

    - **labels** *(dict) --*

      The Kubernetes labels applied to the nodes in the node group.

      .. note::

        Only labels that are applied with the Amazon EKS API are shown here. There may be other
        Kubernetes labels applied to the nodes in this group.

      - *(string) --*

        - *(string) --*

    - **resources** *(dict) --*

      The resources associated with the nodegroup, such as AutoScaling groups and security groups
      for remote access.

      - **autoScalingGroups** *(list) --*

        The autoscaling groups associated with the node group.

        - *(dict) --*

          An AutoScaling group that is associated with an Amazon EKS managed node group.

          - **name** *(string) --*

            The name of the AutoScaling group associated with an Amazon EKS managed node group.

      - **remoteAccessSecurityGroup** *(string) --*

        The remote access security group associated with the node group. This security group
        controls SSH access to the worker nodes.

    - **diskSize** *(integer) --*

      The root device disk size (in GiB) for your node group instances. The default disk size is
      20 GiB.

    - **health** *(dict) --*

      The health status of the node group. If there are issues with your node group's health,
      they are listed here.

      - **issues** *(list) --*

        Any issues that are associated with the node group.

        - *(dict) --*

          An object representing an issue with an Amazon EKS resource.

          - **code** *(string) --*

            A brief description of the error.

            * **AutoScalingGroupNotFound** : We couldn't find the Auto Scaling group associated
            with the managed node group. You may be able to recreate an Auto Scaling group with
            the same settings to recover.

            * **Ec2SecurityGroupNotFound** : We couldn't find the cluster security group for the
            cluster. You must recreate your cluster.

            * **Ec2SecurityGroupDeletionFailure** : We could not delete the remote access
            security group for your managed node group. Remove any dependencies from the security
            group.

            * **Ec2LaunchTemplateNotFound** : We couldn't find the Amazon EC2 launch template for
            your managed node group. You may be able to recreate a launch template with the same
            settings to recover.

            * **Ec2LaunchTemplateVersionMismatch** : The Amazon EC2 launch template version for
            your managed node group does not match the version that Amazon EKS created. You may
            be able to revert to the Amazon EKS-created version to recover.

            * **IamInstanceProfileNotFound** : We couldn't find the IAM instance profile for your
            managed node group. You may be able to recreate an instance profile with the same
            settings to recover.

            * **IamNodeRoleNotFound** : We couldn't find the IAM role for your managed node
            group. You may be able to recreate an IAM role with the same settings to recover.

            * **AsgInstanceLaunchFailures** : Your Auto Scaling group is experiencing failures
            while attempting to launch instances.

            * **InstanceLimitExceeded** : Your AWS account is unable to launch any more instances
            of the specified instance type. You may be able to request an Amazon EC2 instance
            limit increase to recover.

            * **InsufficientFreeAddresses** : One or more of the subnets associated with your
            managed node group does not have enough available IP addresses for new nodes.

            * **AccessDenied** : Amazon EKS and or one or more of your managed nodes is unable to
            communicate with your cluster API server.

            * **InternalFailure** : These errors are usually caused by an Amazon EKS server-side
            issue.

          - **message** *(string) --*

            The error message associated with the issue.

          - **resourceIds** *(list) --*

            The AWS resources that are afflicted by this issue.

            - *(string) --*

    - **tags** *(dict) --*

      The metadata applied the node group to assist with categorization and organization. Each
      tag consists of a key and an optional value, both of which you define. Node group tags do
      not propagate to any other resources associated with the node group, such as the Amazon EC2
      instances or subnets.

      - *(string) --*

        - *(string) --*
    """


_ClientDeleteNodegroupResponseTypeDef = TypedDict(
    "_ClientDeleteNodegroupResponseTypeDef",
    {"nodegroup": ClientDeleteNodegroupResponsenodegroupTypeDef},
    total=False,
)


class ClientDeleteNodegroupResponseTypeDef(_ClientDeleteNodegroupResponseTypeDef):
    """
    Type definition for `ClientDeleteNodegroup` `Response`

    - **nodegroup** *(dict) --*

      The full description of your deleted node group.

      - **nodegroupName** *(string) --*

        The name associated with an Amazon EKS managed node group.

      - **nodegroupArn** *(string) --*

        The Amazon Resource Name (ARN) associated with the managed node group.

      - **clusterName** *(string) --*

        The name of the cluster that the managed node group resides in.

      - **version** *(string) --*

        The Kubernetes version of the managed node group.

      - **releaseVersion** *(string) --*

        The AMI version of the managed node group. For more information, see `Amazon EKS-Optimized
        Linux AMI Versions
        <https://docs.aws.amazon.com/eks/latest/userguide/eks-linux-ami-versions.html>`__ in the
        *Amazon EKS User Guide* .

      - **createdAt** *(datetime) --*

        The Unix epoch timestamp in seconds for when the managed node group was created.

      - **modifiedAt** *(datetime) --*

        The Unix epoch timestamp in seconds for when the managed node group was last modified.

      - **status** *(string) --*

        The current status of the managed node group.

      - **scalingConfig** *(dict) --*

        The scaling configuration details for the AutoScaling group that is associated with your
        node group.

        - **minSize** *(integer) --*

          The minimum number of worker nodes that the managed node group can scale in to. This
          number must be greater than zero.

        - **maxSize** *(integer) --*

          The maximum number of worker nodes that the managed node group can scale out to. Managed
          node groups can support up to 100 nodes by default.

        - **desiredSize** *(integer) --*

          The current number of worker nodes that the managed node group should maintain.

      - **instanceTypes** *(list) --*

        The instance types associated with your node group.

        - *(string) --*

      - **subnets** *(list) --*

        The subnets allowed for the AutoScaling group that is associated with your node group.
        These subnets must have the following tag: ``kubernetes.io/cluster/CLUSTER_NAME`` , where
        ``CLUSTER_NAME`` is replaced with the name of your cluster.

        - *(string) --*

      - **remoteAccess** *(dict) --*

        The remote access (SSH) configuration that is associated with the node group.

        - **ec2SshKey** *(string) --*

          The Amazon EC2 SSH key that provides access for SSH communication with the worker nodes
          in the managed node group. For more information, see `Amazon EC2 Key Pairs
          <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html>`__ in the
          *Amazon Elastic Compute Cloud User Guide for Linux Instances* .

        - **sourceSecurityGroups** *(list) --*

          The security groups to allow SSH access (port 22) from on the worker nodes. If you
          specify an Amazon EC2 SSH key, but you do not specify a source security group when you
          create a managed node group, port 22 on the worker nodes is opened to the internet
          (0.0.0.0/0). For more information, see `Security Groups for Your VPC
          <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ in the
          *Amazon Virtual Private Cloud User Guide* .

          - *(string) --*

      - **amiType** *(string) --*

        The AMI type associated with your node group. GPU instance types should use the
        ``AL2_x86_64_GPU`` AMI type, which uses the Amazon EKS-optimized Linux AMI with GPU
        support; non-GPU instances should use the ``AL2_x86_64`` AMI type, which uses the Amazon
        EKS-optimized Linux AMI.

      - **nodeRole** *(string) --*

        The IAM role associated with your node group. The Amazon EKS worker node ``kubelet`` daemon
        makes calls to AWS APIs on your behalf. Worker nodes receive permissions for these API
        calls through an IAM instance profile and associated policies. Before you can launch worker
        nodes and register them into a cluster, you must create an IAM role for those worker nodes
        to use when they are launched. For more information, see `Amazon EKS Worker Node IAM Role
        <https://docs.aws.amazon.com/eks/latest/userguide/worker_node_IAM_role.html>`__ in the *
        *Amazon EKS User Guide* * .

      - **labels** *(dict) --*

        The Kubernetes labels applied to the nodes in the node group.

        .. note::

          Only labels that are applied with the Amazon EKS API are shown here. There may be other
          Kubernetes labels applied to the nodes in this group.

        - *(string) --*

          - *(string) --*

      - **resources** *(dict) --*

        The resources associated with the nodegroup, such as AutoScaling groups and security groups
        for remote access.

        - **autoScalingGroups** *(list) --*

          The autoscaling groups associated with the node group.

          - *(dict) --*

            An AutoScaling group that is associated with an Amazon EKS managed node group.

            - **name** *(string) --*

              The name of the AutoScaling group associated with an Amazon EKS managed node group.

        - **remoteAccessSecurityGroup** *(string) --*

          The remote access security group associated with the node group. This security group
          controls SSH access to the worker nodes.

      - **diskSize** *(integer) --*

        The root device disk size (in GiB) for your node group instances. The default disk size is
        20 GiB.

      - **health** *(dict) --*

        The health status of the node group. If there are issues with your node group's health,
        they are listed here.

        - **issues** *(list) --*

          Any issues that are associated with the node group.

          - *(dict) --*

            An object representing an issue with an Amazon EKS resource.

            - **code** *(string) --*

              A brief description of the error.

              * **AutoScalingGroupNotFound** : We couldn't find the Auto Scaling group associated
              with the managed node group. You may be able to recreate an Auto Scaling group with
              the same settings to recover.

              * **Ec2SecurityGroupNotFound** : We couldn't find the cluster security group for the
              cluster. You must recreate your cluster.

              * **Ec2SecurityGroupDeletionFailure** : We could not delete the remote access
              security group for your managed node group. Remove any dependencies from the security
              group.

              * **Ec2LaunchTemplateNotFound** : We couldn't find the Amazon EC2 launch template for
              your managed node group. You may be able to recreate a launch template with the same
              settings to recover.

              * **Ec2LaunchTemplateVersionMismatch** : The Amazon EC2 launch template version for
              your managed node group does not match the version that Amazon EKS created. You may
              be able to revert to the Amazon EKS-created version to recover.

              * **IamInstanceProfileNotFound** : We couldn't find the IAM instance profile for your
              managed node group. You may be able to recreate an instance profile with the same
              settings to recover.

              * **IamNodeRoleNotFound** : We couldn't find the IAM role for your managed node
              group. You may be able to recreate an IAM role with the same settings to recover.

              * **AsgInstanceLaunchFailures** : Your Auto Scaling group is experiencing failures
              while attempting to launch instances.

              * **InstanceLimitExceeded** : Your AWS account is unable to launch any more instances
              of the specified instance type. You may be able to request an Amazon EC2 instance
              limit increase to recover.

              * **InsufficientFreeAddresses** : One or more of the subnets associated with your
              managed node group does not have enough available IP addresses for new nodes.

              * **AccessDenied** : Amazon EKS and or one or more of your managed nodes is unable to
              communicate with your cluster API server.

              * **InternalFailure** : These errors are usually caused by an Amazon EKS server-side
              issue.

            - **message** *(string) --*

              The error message associated with the issue.

            - **resourceIds** *(list) --*

              The AWS resources that are afflicted by this issue.

              - *(string) --*

      - **tags** *(dict) --*

        The metadata applied the node group to assist with categorization and organization. Each
        tag consists of a key and an optional value, both of which you define. Node group tags do
        not propagate to any other resources associated with the node group, such as the Amazon EC2
        instances or subnets.

        - *(string) --*

          - *(string) --*
    """


_ClientDescribeClusterResponseclustercertificateAuthorityTypeDef = TypedDict(
    "_ClientDescribeClusterResponseclustercertificateAuthorityTypeDef",
    {"data": str},
    total=False,
)


class ClientDescribeClusterResponseclustercertificateAuthorityTypeDef(
    _ClientDescribeClusterResponseclustercertificateAuthorityTypeDef
):
    """
    Type definition for `ClientDescribeClusterResponsecluster` `certificateAuthority`

    The ``certificate-authority-data`` for your cluster.

    - **data** *(string) --*

      The Base64-encoded certificate data required to communicate with your cluster. Add this
      to the ``certificate-authority-data`` section of the ``kubeconfig`` file for your cluster.
    """


_ClientDescribeClusterResponseclusteridentityoidcTypeDef = TypedDict(
    "_ClientDescribeClusterResponseclusteridentityoidcTypeDef",
    {"issuer": str},
    total=False,
)


class ClientDescribeClusterResponseclusteridentityoidcTypeDef(
    _ClientDescribeClusterResponseclusteridentityoidcTypeDef
):
    """
    Type definition for `ClientDescribeClusterResponseclusteridentity` `oidc`

    The `OpenID Connect <https://openid.net/connect/>`__ identity provider information for
    the cluster.

    - **issuer** *(string) --*

      The issuer URL for the OpenID Connect identity provider.
    """


_ClientDescribeClusterResponseclusteridentityTypeDef = TypedDict(
    "_ClientDescribeClusterResponseclusteridentityTypeDef",
    {"oidc": ClientDescribeClusterResponseclusteridentityoidcTypeDef},
    total=False,
)


class ClientDescribeClusterResponseclusteridentityTypeDef(
    _ClientDescribeClusterResponseclusteridentityTypeDef
):
    """
    Type definition for `ClientDescribeClusterResponsecluster` `identity`

    The identity provider information for the cluster.

    - **oidc** *(dict) --*

      The `OpenID Connect <https://openid.net/connect/>`__ identity provider information for
      the cluster.

      - **issuer** *(string) --*

        The issuer URL for the OpenID Connect identity provider.
    """


_ClientDescribeClusterResponseclusterloggingclusterLoggingTypeDef = TypedDict(
    "_ClientDescribeClusterResponseclusterloggingclusterLoggingTypeDef",
    {"types": List[str], "enabled": bool},
    total=False,
)


class ClientDescribeClusterResponseclusterloggingclusterLoggingTypeDef(
    _ClientDescribeClusterResponseclusterloggingclusterLoggingTypeDef
):
    """
    Type definition for `ClientDescribeClusterResponseclusterlogging` `clusterLogging`

    An object representing the enabled or disabled Kubernetes control plane logs for your
    cluster.

    - **types** *(list) --*

      The available cluster control plane log types.

      - *(string) --*

    - **enabled** *(boolean) --*

      If a log type is enabled, that log type exports its control plane logs to CloudWatch
      Logs. If a log type isn't enabled, that log type doesn't export its control plane
      logs. Each individual log type can be enabled or disabled independently.
    """


_ClientDescribeClusterResponseclusterloggingTypeDef = TypedDict(
    "_ClientDescribeClusterResponseclusterloggingTypeDef",
    {
        "clusterLogging": List[
            ClientDescribeClusterResponseclusterloggingclusterLoggingTypeDef
        ]
    },
    total=False,
)


class ClientDescribeClusterResponseclusterloggingTypeDef(
    _ClientDescribeClusterResponseclusterloggingTypeDef
):
    """
    Type definition for `ClientDescribeClusterResponsecluster` `logging`

    The logging configuration for your cluster.

    - **clusterLogging** *(list) --*

      The cluster control plane logging configuration for your cluster.

      - *(dict) --*

        An object representing the enabled or disabled Kubernetes control plane logs for your
        cluster.

        - **types** *(list) --*

          The available cluster control plane log types.

          - *(string) --*

        - **enabled** *(boolean) --*

          If a log type is enabled, that log type exports its control plane logs to CloudWatch
          Logs. If a log type isn't enabled, that log type doesn't export its control plane
          logs. Each individual log type can be enabled or disabled independently.
    """


_ClientDescribeClusterResponseclusterresourcesVpcConfigTypeDef = TypedDict(
    "_ClientDescribeClusterResponseclusterresourcesVpcConfigTypeDef",
    {
        "subnetIds": List[str],
        "securityGroupIds": List[str],
        "clusterSecurityGroupId": str,
        "vpcId": str,
        "endpointPublicAccess": bool,
        "endpointPrivateAccess": bool,
    },
    total=False,
)


class ClientDescribeClusterResponseclusterresourcesVpcConfigTypeDef(
    _ClientDescribeClusterResponseclusterresourcesVpcConfigTypeDef
):
    """
    Type definition for `ClientDescribeClusterResponsecluster` `resourcesVpcConfig`

    The VPC configuration used by the cluster control plane. Amazon EKS VPC resources have
    specific requirements to work properly with Kubernetes. For more information, see `Cluster
    VPC Considerations <https://docs.aws.amazon.com/eks/latest/userguide/network_reqs.html>`__
    and `Cluster Security Group Considerations
    <https://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html>`__ in the *Amazon
    EKS User Guide* .

    - **subnetIds** *(list) --*

      The subnets associated with your cluster.

      - *(string) --*

    - **securityGroupIds** *(list) --*

      The security groups associated with the cross-account elastic network interfaces that are
      used to allow communication between your worker nodes and the Kubernetes control plane.

      - *(string) --*

    - **clusterSecurityGroupId** *(string) --*

      The cluster security group that was created by Amazon EKS for the cluster. Managed node
      groups use this security group for control plane to data plane communication.

    - **vpcId** *(string) --*

      The VPC associated with your cluster.

    - **endpointPublicAccess** *(boolean) --*

      This parameter indicates whether the Amazon EKS public API server endpoint is enabled. If
      the Amazon EKS public API server endpoint is disabled, your cluster's Kubernetes API
      server can receive only requests that originate from within the cluster VPC.

    - **endpointPrivateAccess** *(boolean) --*

      This parameter indicates whether the Amazon EKS private API server endpoint is enabled.
      If the Amazon EKS private API server endpoint is enabled, Kubernetes API requests that
      originate from within your cluster's VPC use the private VPC endpoint instead of
      traversing the internet.
    """


_ClientDescribeClusterResponseclusterTypeDef = TypedDict(
    "_ClientDescribeClusterResponseclusterTypeDef",
    {
        "name": str,
        "arn": str,
        "createdAt": datetime,
        "version": str,
        "endpoint": str,
        "roleArn": str,
        "resourcesVpcConfig": ClientDescribeClusterResponseclusterresourcesVpcConfigTypeDef,
        "logging": ClientDescribeClusterResponseclusterloggingTypeDef,
        "identity": ClientDescribeClusterResponseclusteridentityTypeDef,
        "status": str,
        "certificateAuthority": ClientDescribeClusterResponseclustercertificateAuthorityTypeDef,
        "clientRequestToken": str,
        "platformVersion": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientDescribeClusterResponseclusterTypeDef(
    _ClientDescribeClusterResponseclusterTypeDef
):
    """
    Type definition for `ClientDescribeClusterResponse` `cluster`

    The full description of your specified cluster.

    - **name** *(string) --*

      The name of the cluster.

    - **arn** *(string) --*

      The Amazon Resource Name (ARN) of the cluster.

    - **createdAt** *(datetime) --*

      The Unix epoch timestamp in seconds for when the cluster was created.

    - **version** *(string) --*

      The Kubernetes server version for the cluster.

    - **endpoint** *(string) --*

      The endpoint for your Kubernetes API server.

    - **roleArn** *(string) --*

      The Amazon Resource Name (ARN) of the IAM role that provides permissions for the Kubernetes
      control plane to make calls to AWS API operations on your behalf.

    - **resourcesVpcConfig** *(dict) --*

      The VPC configuration used by the cluster control plane. Amazon EKS VPC resources have
      specific requirements to work properly with Kubernetes. For more information, see `Cluster
      VPC Considerations <https://docs.aws.amazon.com/eks/latest/userguide/network_reqs.html>`__
      and `Cluster Security Group Considerations
      <https://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html>`__ in the *Amazon
      EKS User Guide* .

      - **subnetIds** *(list) --*

        The subnets associated with your cluster.

        - *(string) --*

      - **securityGroupIds** *(list) --*

        The security groups associated with the cross-account elastic network interfaces that are
        used to allow communication between your worker nodes and the Kubernetes control plane.

        - *(string) --*

      - **clusterSecurityGroupId** *(string) --*

        The cluster security group that was created by Amazon EKS for the cluster. Managed node
        groups use this security group for control plane to data plane communication.

      - **vpcId** *(string) --*

        The VPC associated with your cluster.

      - **endpointPublicAccess** *(boolean) --*

        This parameter indicates whether the Amazon EKS public API server endpoint is enabled. If
        the Amazon EKS public API server endpoint is disabled, your cluster's Kubernetes API
        server can receive only requests that originate from within the cluster VPC.

      - **endpointPrivateAccess** *(boolean) --*

        This parameter indicates whether the Amazon EKS private API server endpoint is enabled.
        If the Amazon EKS private API server endpoint is enabled, Kubernetes API requests that
        originate from within your cluster's VPC use the private VPC endpoint instead of
        traversing the internet.

    - **logging** *(dict) --*

      The logging configuration for your cluster.

      - **clusterLogging** *(list) --*

        The cluster control plane logging configuration for your cluster.

        - *(dict) --*

          An object representing the enabled or disabled Kubernetes control plane logs for your
          cluster.

          - **types** *(list) --*

            The available cluster control plane log types.

            - *(string) --*

          - **enabled** *(boolean) --*

            If a log type is enabled, that log type exports its control plane logs to CloudWatch
            Logs. If a log type isn't enabled, that log type doesn't export its control plane
            logs. Each individual log type can be enabled or disabled independently.

    - **identity** *(dict) --*

      The identity provider information for the cluster.

      - **oidc** *(dict) --*

        The `OpenID Connect <https://openid.net/connect/>`__ identity provider information for
        the cluster.

        - **issuer** *(string) --*

          The issuer URL for the OpenID Connect identity provider.

    - **status** *(string) --*

      The current status of the cluster.

    - **certificateAuthority** *(dict) --*

      The ``certificate-authority-data`` for your cluster.

      - **data** *(string) --*

        The Base64-encoded certificate data required to communicate with your cluster. Add this
        to the ``certificate-authority-data`` section of the ``kubeconfig`` file for your cluster.

    - **clientRequestToken** *(string) --*

      Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

    - **platformVersion** *(string) --*

      The platform version of your Amazon EKS cluster. For more information, see `Platform
      Versions <https://docs.aws.amazon.com/eks/latest/userguide/platform-versions.html>`__ in
      the * *Amazon EKS User Guide* * .

    - **tags** *(dict) --*

      The metadata that you apply to the cluster to assist with categorization and organization.
      Each tag consists of a key and an optional value, both of which you define. Cluster tags do
      not propagate to any other resources associated with the cluster.

      - *(string) --*

        - *(string) --*
    """


_ClientDescribeClusterResponseTypeDef = TypedDict(
    "_ClientDescribeClusterResponseTypeDef",
    {"cluster": ClientDescribeClusterResponseclusterTypeDef},
    total=False,
)


class ClientDescribeClusterResponseTypeDef(_ClientDescribeClusterResponseTypeDef):
    """
    Type definition for `ClientDescribeCluster` `Response`

    - **cluster** *(dict) --*

      The full description of your specified cluster.

      - **name** *(string) --*

        The name of the cluster.

      - **arn** *(string) --*

        The Amazon Resource Name (ARN) of the cluster.

      - **createdAt** *(datetime) --*

        The Unix epoch timestamp in seconds for when the cluster was created.

      - **version** *(string) --*

        The Kubernetes server version for the cluster.

      - **endpoint** *(string) --*

        The endpoint for your Kubernetes API server.

      - **roleArn** *(string) --*

        The Amazon Resource Name (ARN) of the IAM role that provides permissions for the Kubernetes
        control plane to make calls to AWS API operations on your behalf.

      - **resourcesVpcConfig** *(dict) --*

        The VPC configuration used by the cluster control plane. Amazon EKS VPC resources have
        specific requirements to work properly with Kubernetes. For more information, see `Cluster
        VPC Considerations <https://docs.aws.amazon.com/eks/latest/userguide/network_reqs.html>`__
        and `Cluster Security Group Considerations
        <https://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html>`__ in the *Amazon
        EKS User Guide* .

        - **subnetIds** *(list) --*

          The subnets associated with your cluster.

          - *(string) --*

        - **securityGroupIds** *(list) --*

          The security groups associated with the cross-account elastic network interfaces that are
          used to allow communication between your worker nodes and the Kubernetes control plane.

          - *(string) --*

        - **clusterSecurityGroupId** *(string) --*

          The cluster security group that was created by Amazon EKS for the cluster. Managed node
          groups use this security group for control plane to data plane communication.

        - **vpcId** *(string) --*

          The VPC associated with your cluster.

        - **endpointPublicAccess** *(boolean) --*

          This parameter indicates whether the Amazon EKS public API server endpoint is enabled. If
          the Amazon EKS public API server endpoint is disabled, your cluster's Kubernetes API
          server can receive only requests that originate from within the cluster VPC.

        - **endpointPrivateAccess** *(boolean) --*

          This parameter indicates whether the Amazon EKS private API server endpoint is enabled.
          If the Amazon EKS private API server endpoint is enabled, Kubernetes API requests that
          originate from within your cluster's VPC use the private VPC endpoint instead of
          traversing the internet.

      - **logging** *(dict) --*

        The logging configuration for your cluster.

        - **clusterLogging** *(list) --*

          The cluster control plane logging configuration for your cluster.

          - *(dict) --*

            An object representing the enabled or disabled Kubernetes control plane logs for your
            cluster.

            - **types** *(list) --*

              The available cluster control plane log types.

              - *(string) --*

            - **enabled** *(boolean) --*

              If a log type is enabled, that log type exports its control plane logs to CloudWatch
              Logs. If a log type isn't enabled, that log type doesn't export its control plane
              logs. Each individual log type can be enabled or disabled independently.

      - **identity** *(dict) --*

        The identity provider information for the cluster.

        - **oidc** *(dict) --*

          The `OpenID Connect <https://openid.net/connect/>`__ identity provider information for
          the cluster.

          - **issuer** *(string) --*

            The issuer URL for the OpenID Connect identity provider.

      - **status** *(string) --*

        The current status of the cluster.

      - **certificateAuthority** *(dict) --*

        The ``certificate-authority-data`` for your cluster.

        - **data** *(string) --*

          The Base64-encoded certificate data required to communicate with your cluster. Add this
          to the ``certificate-authority-data`` section of the ``kubeconfig`` file for your cluster.

      - **clientRequestToken** *(string) --*

        Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

      - **platformVersion** *(string) --*

        The platform version of your Amazon EKS cluster. For more information, see `Platform
        Versions <https://docs.aws.amazon.com/eks/latest/userguide/platform-versions.html>`__ in
        the * *Amazon EKS User Guide* * .

      - **tags** *(dict) --*

        The metadata that you apply to the cluster to assist with categorization and organization.
        Each tag consists of a key and an optional value, both of which you define. Cluster tags do
        not propagate to any other resources associated with the cluster.

        - *(string) --*

          - *(string) --*
    """


_ClientDescribeNodegroupResponsenodegrouphealthissuesTypeDef = TypedDict(
    "_ClientDescribeNodegroupResponsenodegrouphealthissuesTypeDef",
    {"code": str, "message": str, "resourceIds": List[str]},
    total=False,
)


class ClientDescribeNodegroupResponsenodegrouphealthissuesTypeDef(
    _ClientDescribeNodegroupResponsenodegrouphealthissuesTypeDef
):
    """
    Type definition for `ClientDescribeNodegroupResponsenodegrouphealth` `issues`

    An object representing an issue with an Amazon EKS resource.

    - **code** *(string) --*

      A brief description of the error.

      * **AutoScalingGroupNotFound** : We couldn't find the Auto Scaling group associated
      with the managed node group. You may be able to recreate an Auto Scaling group with
      the same settings to recover.

      * **Ec2SecurityGroupNotFound** : We couldn't find the cluster security group for the
      cluster. You must recreate your cluster.

      * **Ec2SecurityGroupDeletionFailure** : We could not delete the remote access
      security group for your managed node group. Remove any dependencies from the security
      group.

      * **Ec2LaunchTemplateNotFound** : We couldn't find the Amazon EC2 launch template for
      your managed node group. You may be able to recreate a launch template with the same
      settings to recover.

      * **Ec2LaunchTemplateVersionMismatch** : The Amazon EC2 launch template version for
      your managed node group does not match the version that Amazon EKS created. You may
      be able to revert to the Amazon EKS-created version to recover.

      * **IamInstanceProfileNotFound** : We couldn't find the IAM instance profile for your
      managed node group. You may be able to recreate an instance profile with the same
      settings to recover.

      * **IamNodeRoleNotFound** : We couldn't find the IAM role for your managed node
      group. You may be able to recreate an IAM role with the same settings to recover.

      * **AsgInstanceLaunchFailures** : Your Auto Scaling group is experiencing failures
      while attempting to launch instances.

      * **InstanceLimitExceeded** : Your AWS account is unable to launch any more instances
      of the specified instance type. You may be able to request an Amazon EC2 instance
      limit increase to recover.

      * **InsufficientFreeAddresses** : One or more of the subnets associated with your
      managed node group does not have enough available IP addresses for new nodes.

      * **AccessDenied** : Amazon EKS and or one or more of your managed nodes is unable to
      communicate with your cluster API server.

      * **InternalFailure** : These errors are usually caused by an Amazon EKS server-side
      issue.

    - **message** *(string) --*

      The error message associated with the issue.

    - **resourceIds** *(list) --*

      The AWS resources that are afflicted by this issue.

      - *(string) --*
    """


_ClientDescribeNodegroupResponsenodegrouphealthTypeDef = TypedDict(
    "_ClientDescribeNodegroupResponsenodegrouphealthTypeDef",
    {"issues": List[ClientDescribeNodegroupResponsenodegrouphealthissuesTypeDef]},
    total=False,
)


class ClientDescribeNodegroupResponsenodegrouphealthTypeDef(
    _ClientDescribeNodegroupResponsenodegrouphealthTypeDef
):
    """
    Type definition for `ClientDescribeNodegroupResponsenodegroup` `health`

    The health status of the node group. If there are issues with your node group's health,
    they are listed here.

    - **issues** *(list) --*

      Any issues that are associated with the node group.

      - *(dict) --*

        An object representing an issue with an Amazon EKS resource.

        - **code** *(string) --*

          A brief description of the error.

          * **AutoScalingGroupNotFound** : We couldn't find the Auto Scaling group associated
          with the managed node group. You may be able to recreate an Auto Scaling group with
          the same settings to recover.

          * **Ec2SecurityGroupNotFound** : We couldn't find the cluster security group for the
          cluster. You must recreate your cluster.

          * **Ec2SecurityGroupDeletionFailure** : We could not delete the remote access
          security group for your managed node group. Remove any dependencies from the security
          group.

          * **Ec2LaunchTemplateNotFound** : We couldn't find the Amazon EC2 launch template for
          your managed node group. You may be able to recreate a launch template with the same
          settings to recover.

          * **Ec2LaunchTemplateVersionMismatch** : The Amazon EC2 launch template version for
          your managed node group does not match the version that Amazon EKS created. You may
          be able to revert to the Amazon EKS-created version to recover.

          * **IamInstanceProfileNotFound** : We couldn't find the IAM instance profile for your
          managed node group. You may be able to recreate an instance profile with the same
          settings to recover.

          * **IamNodeRoleNotFound** : We couldn't find the IAM role for your managed node
          group. You may be able to recreate an IAM role with the same settings to recover.

          * **AsgInstanceLaunchFailures** : Your Auto Scaling group is experiencing failures
          while attempting to launch instances.

          * **InstanceLimitExceeded** : Your AWS account is unable to launch any more instances
          of the specified instance type. You may be able to request an Amazon EC2 instance
          limit increase to recover.

          * **InsufficientFreeAddresses** : One or more of the subnets associated with your
          managed node group does not have enough available IP addresses for new nodes.

          * **AccessDenied** : Amazon EKS and or one or more of your managed nodes is unable to
          communicate with your cluster API server.

          * **InternalFailure** : These errors are usually caused by an Amazon EKS server-side
          issue.

        - **message** *(string) --*

          The error message associated with the issue.

        - **resourceIds** *(list) --*

          The AWS resources that are afflicted by this issue.

          - *(string) --*
    """


_ClientDescribeNodegroupResponsenodegroupremoteAccessTypeDef = TypedDict(
    "_ClientDescribeNodegroupResponsenodegroupremoteAccessTypeDef",
    {"ec2SshKey": str, "sourceSecurityGroups": List[str]},
    total=False,
)


class ClientDescribeNodegroupResponsenodegroupremoteAccessTypeDef(
    _ClientDescribeNodegroupResponsenodegroupremoteAccessTypeDef
):
    """
    Type definition for `ClientDescribeNodegroupResponsenodegroup` `remoteAccess`

    The remote access (SSH) configuration that is associated with the node group.

    - **ec2SshKey** *(string) --*

      The Amazon EC2 SSH key that provides access for SSH communication with the worker nodes
      in the managed node group. For more information, see `Amazon EC2 Key Pairs
      <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html>`__ in the
      *Amazon Elastic Compute Cloud User Guide for Linux Instances* .

    - **sourceSecurityGroups** *(list) --*

      The security groups to allow SSH access (port 22) from on the worker nodes. If you
      specify an Amazon EC2 SSH key, but you do not specify a source security group when you
      create a managed node group, port 22 on the worker nodes is opened to the internet
      (0.0.0.0/0). For more information, see `Security Groups for Your VPC
      <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ in the
      *Amazon Virtual Private Cloud User Guide* .

      - *(string) --*
    """


_ClientDescribeNodegroupResponsenodegroupresourcesautoScalingGroupsTypeDef = TypedDict(
    "_ClientDescribeNodegroupResponsenodegroupresourcesautoScalingGroupsTypeDef",
    {"name": str},
    total=False,
)


class ClientDescribeNodegroupResponsenodegroupresourcesautoScalingGroupsTypeDef(
    _ClientDescribeNodegroupResponsenodegroupresourcesautoScalingGroupsTypeDef
):
    """
    Type definition for `ClientDescribeNodegroupResponsenodegroupresources` `autoScalingGroups`

    An AutoScaling group that is associated with an Amazon EKS managed node group.

    - **name** *(string) --*

      The name of the AutoScaling group associated with an Amazon EKS managed node group.
    """


_ClientDescribeNodegroupResponsenodegroupresourcesTypeDef = TypedDict(
    "_ClientDescribeNodegroupResponsenodegroupresourcesTypeDef",
    {
        "autoScalingGroups": List[
            ClientDescribeNodegroupResponsenodegroupresourcesautoScalingGroupsTypeDef
        ],
        "remoteAccessSecurityGroup": str,
    },
    total=False,
)


class ClientDescribeNodegroupResponsenodegroupresourcesTypeDef(
    _ClientDescribeNodegroupResponsenodegroupresourcesTypeDef
):
    """
    Type definition for `ClientDescribeNodegroupResponsenodegroup` `resources`

    The resources associated with the nodegroup, such as AutoScaling groups and security groups
    for remote access.

    - **autoScalingGroups** *(list) --*

      The autoscaling groups associated with the node group.

      - *(dict) --*

        An AutoScaling group that is associated with an Amazon EKS managed node group.

        - **name** *(string) --*

          The name of the AutoScaling group associated with an Amazon EKS managed node group.

    - **remoteAccessSecurityGroup** *(string) --*

      The remote access security group associated with the node group. This security group
      controls SSH access to the worker nodes.
    """


_ClientDescribeNodegroupResponsenodegroupscalingConfigTypeDef = TypedDict(
    "_ClientDescribeNodegroupResponsenodegroupscalingConfigTypeDef",
    {"minSize": int, "maxSize": int, "desiredSize": int},
    total=False,
)


class ClientDescribeNodegroupResponsenodegroupscalingConfigTypeDef(
    _ClientDescribeNodegroupResponsenodegroupscalingConfigTypeDef
):
    """
    Type definition for `ClientDescribeNodegroupResponsenodegroup` `scalingConfig`

    The scaling configuration details for the AutoScaling group that is associated with your
    node group.

    - **minSize** *(integer) --*

      The minimum number of worker nodes that the managed node group can scale in to. This
      number must be greater than zero.

    - **maxSize** *(integer) --*

      The maximum number of worker nodes that the managed node group can scale out to. Managed
      node groups can support up to 100 nodes by default.

    - **desiredSize** *(integer) --*

      The current number of worker nodes that the managed node group should maintain.
    """


_ClientDescribeNodegroupResponsenodegroupTypeDef = TypedDict(
    "_ClientDescribeNodegroupResponsenodegroupTypeDef",
    {
        "nodegroupName": str,
        "nodegroupArn": str,
        "clusterName": str,
        "version": str,
        "releaseVersion": str,
        "createdAt": datetime,
        "modifiedAt": datetime,
        "status": str,
        "scalingConfig": ClientDescribeNodegroupResponsenodegroupscalingConfigTypeDef,
        "instanceTypes": List[str],
        "subnets": List[str],
        "remoteAccess": ClientDescribeNodegroupResponsenodegroupremoteAccessTypeDef,
        "amiType": str,
        "nodeRole": str,
        "labels": Dict[str, str],
        "resources": ClientDescribeNodegroupResponsenodegroupresourcesTypeDef,
        "diskSize": int,
        "health": ClientDescribeNodegroupResponsenodegrouphealthTypeDef,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientDescribeNodegroupResponsenodegroupTypeDef(
    _ClientDescribeNodegroupResponsenodegroupTypeDef
):
    """
    Type definition for `ClientDescribeNodegroupResponse` `nodegroup`

    The full description of your node group.

    - **nodegroupName** *(string) --*

      The name associated with an Amazon EKS managed node group.

    - **nodegroupArn** *(string) --*

      The Amazon Resource Name (ARN) associated with the managed node group.

    - **clusterName** *(string) --*

      The name of the cluster that the managed node group resides in.

    - **version** *(string) --*

      The Kubernetes version of the managed node group.

    - **releaseVersion** *(string) --*

      The AMI version of the managed node group. For more information, see `Amazon EKS-Optimized
      Linux AMI Versions
      <https://docs.aws.amazon.com/eks/latest/userguide/eks-linux-ami-versions.html>`__ in the
      *Amazon EKS User Guide* .

    - **createdAt** *(datetime) --*

      The Unix epoch timestamp in seconds for when the managed node group was created.

    - **modifiedAt** *(datetime) --*

      The Unix epoch timestamp in seconds for when the managed node group was last modified.

    - **status** *(string) --*

      The current status of the managed node group.

    - **scalingConfig** *(dict) --*

      The scaling configuration details for the AutoScaling group that is associated with your
      node group.

      - **minSize** *(integer) --*

        The minimum number of worker nodes that the managed node group can scale in to. This
        number must be greater than zero.

      - **maxSize** *(integer) --*

        The maximum number of worker nodes that the managed node group can scale out to. Managed
        node groups can support up to 100 nodes by default.

      - **desiredSize** *(integer) --*

        The current number of worker nodes that the managed node group should maintain.

    - **instanceTypes** *(list) --*

      The instance types associated with your node group.

      - *(string) --*

    - **subnets** *(list) --*

      The subnets allowed for the AutoScaling group that is associated with your node group.
      These subnets must have the following tag: ``kubernetes.io/cluster/CLUSTER_NAME`` , where
      ``CLUSTER_NAME`` is replaced with the name of your cluster.

      - *(string) --*

    - **remoteAccess** *(dict) --*

      The remote access (SSH) configuration that is associated with the node group.

      - **ec2SshKey** *(string) --*

        The Amazon EC2 SSH key that provides access for SSH communication with the worker nodes
        in the managed node group. For more information, see `Amazon EC2 Key Pairs
        <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html>`__ in the
        *Amazon Elastic Compute Cloud User Guide for Linux Instances* .

      - **sourceSecurityGroups** *(list) --*

        The security groups to allow SSH access (port 22) from on the worker nodes. If you
        specify an Amazon EC2 SSH key, but you do not specify a source security group when you
        create a managed node group, port 22 on the worker nodes is opened to the internet
        (0.0.0.0/0). For more information, see `Security Groups for Your VPC
        <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ in the
        *Amazon Virtual Private Cloud User Guide* .

        - *(string) --*

    - **amiType** *(string) --*

      The AMI type associated with your node group. GPU instance types should use the
      ``AL2_x86_64_GPU`` AMI type, which uses the Amazon EKS-optimized Linux AMI with GPU
      support; non-GPU instances should use the ``AL2_x86_64`` AMI type, which uses the Amazon
      EKS-optimized Linux AMI.

    - **nodeRole** *(string) --*

      The IAM role associated with your node group. The Amazon EKS worker node ``kubelet`` daemon
      makes calls to AWS APIs on your behalf. Worker nodes receive permissions for these API
      calls through an IAM instance profile and associated policies. Before you can launch worker
      nodes and register them into a cluster, you must create an IAM role for those worker nodes
      to use when they are launched. For more information, see `Amazon EKS Worker Node IAM Role
      <https://docs.aws.amazon.com/eks/latest/userguide/worker_node_IAM_role.html>`__ in the *
      *Amazon EKS User Guide* * .

    - **labels** *(dict) --*

      The Kubernetes labels applied to the nodes in the node group.

      .. note::

        Only labels that are applied with the Amazon EKS API are shown here. There may be other
        Kubernetes labels applied to the nodes in this group.

      - *(string) --*

        - *(string) --*

    - **resources** *(dict) --*

      The resources associated with the nodegroup, such as AutoScaling groups and security groups
      for remote access.

      - **autoScalingGroups** *(list) --*

        The autoscaling groups associated with the node group.

        - *(dict) --*

          An AutoScaling group that is associated with an Amazon EKS managed node group.

          - **name** *(string) --*

            The name of the AutoScaling group associated with an Amazon EKS managed node group.

      - **remoteAccessSecurityGroup** *(string) --*

        The remote access security group associated with the node group. This security group
        controls SSH access to the worker nodes.

    - **diskSize** *(integer) --*

      The root device disk size (in GiB) for your node group instances. The default disk size is
      20 GiB.

    - **health** *(dict) --*

      The health status of the node group. If there are issues with your node group's health,
      they are listed here.

      - **issues** *(list) --*

        Any issues that are associated with the node group.

        - *(dict) --*

          An object representing an issue with an Amazon EKS resource.

          - **code** *(string) --*

            A brief description of the error.

            * **AutoScalingGroupNotFound** : We couldn't find the Auto Scaling group associated
            with the managed node group. You may be able to recreate an Auto Scaling group with
            the same settings to recover.

            * **Ec2SecurityGroupNotFound** : We couldn't find the cluster security group for the
            cluster. You must recreate your cluster.

            * **Ec2SecurityGroupDeletionFailure** : We could not delete the remote access
            security group for your managed node group. Remove any dependencies from the security
            group.

            * **Ec2LaunchTemplateNotFound** : We couldn't find the Amazon EC2 launch template for
            your managed node group. You may be able to recreate a launch template with the same
            settings to recover.

            * **Ec2LaunchTemplateVersionMismatch** : The Amazon EC2 launch template version for
            your managed node group does not match the version that Amazon EKS created. You may
            be able to revert to the Amazon EKS-created version to recover.

            * **IamInstanceProfileNotFound** : We couldn't find the IAM instance profile for your
            managed node group. You may be able to recreate an instance profile with the same
            settings to recover.

            * **IamNodeRoleNotFound** : We couldn't find the IAM role for your managed node
            group. You may be able to recreate an IAM role with the same settings to recover.

            * **AsgInstanceLaunchFailures** : Your Auto Scaling group is experiencing failures
            while attempting to launch instances.

            * **InstanceLimitExceeded** : Your AWS account is unable to launch any more instances
            of the specified instance type. You may be able to request an Amazon EC2 instance
            limit increase to recover.

            * **InsufficientFreeAddresses** : One or more of the subnets associated with your
            managed node group does not have enough available IP addresses for new nodes.

            * **AccessDenied** : Amazon EKS and or one or more of your managed nodes is unable to
            communicate with your cluster API server.

            * **InternalFailure** : These errors are usually caused by an Amazon EKS server-side
            issue.

          - **message** *(string) --*

            The error message associated with the issue.

          - **resourceIds** *(list) --*

            The AWS resources that are afflicted by this issue.

            - *(string) --*

    - **tags** *(dict) --*

      The metadata applied the node group to assist with categorization and organization. Each
      tag consists of a key and an optional value, both of which you define. Node group tags do
      not propagate to any other resources associated with the node group, such as the Amazon EC2
      instances or subnets.

      - *(string) --*

        - *(string) --*
    """


_ClientDescribeNodegroupResponseTypeDef = TypedDict(
    "_ClientDescribeNodegroupResponseTypeDef",
    {"nodegroup": ClientDescribeNodegroupResponsenodegroupTypeDef},
    total=False,
)


class ClientDescribeNodegroupResponseTypeDef(_ClientDescribeNodegroupResponseTypeDef):
    """
    Type definition for `ClientDescribeNodegroup` `Response`

    - **nodegroup** *(dict) --*

      The full description of your node group.

      - **nodegroupName** *(string) --*

        The name associated with an Amazon EKS managed node group.

      - **nodegroupArn** *(string) --*

        The Amazon Resource Name (ARN) associated with the managed node group.

      - **clusterName** *(string) --*

        The name of the cluster that the managed node group resides in.

      - **version** *(string) --*

        The Kubernetes version of the managed node group.

      - **releaseVersion** *(string) --*

        The AMI version of the managed node group. For more information, see `Amazon EKS-Optimized
        Linux AMI Versions
        <https://docs.aws.amazon.com/eks/latest/userguide/eks-linux-ami-versions.html>`__ in the
        *Amazon EKS User Guide* .

      - **createdAt** *(datetime) --*

        The Unix epoch timestamp in seconds for when the managed node group was created.

      - **modifiedAt** *(datetime) --*

        The Unix epoch timestamp in seconds for when the managed node group was last modified.

      - **status** *(string) --*

        The current status of the managed node group.

      - **scalingConfig** *(dict) --*

        The scaling configuration details for the AutoScaling group that is associated with your
        node group.

        - **minSize** *(integer) --*

          The minimum number of worker nodes that the managed node group can scale in to. This
          number must be greater than zero.

        - **maxSize** *(integer) --*

          The maximum number of worker nodes that the managed node group can scale out to. Managed
          node groups can support up to 100 nodes by default.

        - **desiredSize** *(integer) --*

          The current number of worker nodes that the managed node group should maintain.

      - **instanceTypes** *(list) --*

        The instance types associated with your node group.

        - *(string) --*

      - **subnets** *(list) --*

        The subnets allowed for the AutoScaling group that is associated with your node group.
        These subnets must have the following tag: ``kubernetes.io/cluster/CLUSTER_NAME`` , where
        ``CLUSTER_NAME`` is replaced with the name of your cluster.

        - *(string) --*

      - **remoteAccess** *(dict) --*

        The remote access (SSH) configuration that is associated with the node group.

        - **ec2SshKey** *(string) --*

          The Amazon EC2 SSH key that provides access for SSH communication with the worker nodes
          in the managed node group. For more information, see `Amazon EC2 Key Pairs
          <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html>`__ in the
          *Amazon Elastic Compute Cloud User Guide for Linux Instances* .

        - **sourceSecurityGroups** *(list) --*

          The security groups to allow SSH access (port 22) from on the worker nodes. If you
          specify an Amazon EC2 SSH key, but you do not specify a source security group when you
          create a managed node group, port 22 on the worker nodes is opened to the internet
          (0.0.0.0/0). For more information, see `Security Groups for Your VPC
          <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ in the
          *Amazon Virtual Private Cloud User Guide* .

          - *(string) --*

      - **amiType** *(string) --*

        The AMI type associated with your node group. GPU instance types should use the
        ``AL2_x86_64_GPU`` AMI type, which uses the Amazon EKS-optimized Linux AMI with GPU
        support; non-GPU instances should use the ``AL2_x86_64`` AMI type, which uses the Amazon
        EKS-optimized Linux AMI.

      - **nodeRole** *(string) --*

        The IAM role associated with your node group. The Amazon EKS worker node ``kubelet`` daemon
        makes calls to AWS APIs on your behalf. Worker nodes receive permissions for these API
        calls through an IAM instance profile and associated policies. Before you can launch worker
        nodes and register them into a cluster, you must create an IAM role for those worker nodes
        to use when they are launched. For more information, see `Amazon EKS Worker Node IAM Role
        <https://docs.aws.amazon.com/eks/latest/userguide/worker_node_IAM_role.html>`__ in the *
        *Amazon EKS User Guide* * .

      - **labels** *(dict) --*

        The Kubernetes labels applied to the nodes in the node group.

        .. note::

          Only labels that are applied with the Amazon EKS API are shown here. There may be other
          Kubernetes labels applied to the nodes in this group.

        - *(string) --*

          - *(string) --*

      - **resources** *(dict) --*

        The resources associated with the nodegroup, such as AutoScaling groups and security groups
        for remote access.

        - **autoScalingGroups** *(list) --*

          The autoscaling groups associated with the node group.

          - *(dict) --*

            An AutoScaling group that is associated with an Amazon EKS managed node group.

            - **name** *(string) --*

              The name of the AutoScaling group associated with an Amazon EKS managed node group.

        - **remoteAccessSecurityGroup** *(string) --*

          The remote access security group associated with the node group. This security group
          controls SSH access to the worker nodes.

      - **diskSize** *(integer) --*

        The root device disk size (in GiB) for your node group instances. The default disk size is
        20 GiB.

      - **health** *(dict) --*

        The health status of the node group. If there are issues with your node group's health,
        they are listed here.

        - **issues** *(list) --*

          Any issues that are associated with the node group.

          - *(dict) --*

            An object representing an issue with an Amazon EKS resource.

            - **code** *(string) --*

              A brief description of the error.

              * **AutoScalingGroupNotFound** : We couldn't find the Auto Scaling group associated
              with the managed node group. You may be able to recreate an Auto Scaling group with
              the same settings to recover.

              * **Ec2SecurityGroupNotFound** : We couldn't find the cluster security group for the
              cluster. You must recreate your cluster.

              * **Ec2SecurityGroupDeletionFailure** : We could not delete the remote access
              security group for your managed node group. Remove any dependencies from the security
              group.

              * **Ec2LaunchTemplateNotFound** : We couldn't find the Amazon EC2 launch template for
              your managed node group. You may be able to recreate a launch template with the same
              settings to recover.

              * **Ec2LaunchTemplateVersionMismatch** : The Amazon EC2 launch template version for
              your managed node group does not match the version that Amazon EKS created. You may
              be able to revert to the Amazon EKS-created version to recover.

              * **IamInstanceProfileNotFound** : We couldn't find the IAM instance profile for your
              managed node group. You may be able to recreate an instance profile with the same
              settings to recover.

              * **IamNodeRoleNotFound** : We couldn't find the IAM role for your managed node
              group. You may be able to recreate an IAM role with the same settings to recover.

              * **AsgInstanceLaunchFailures** : Your Auto Scaling group is experiencing failures
              while attempting to launch instances.

              * **InstanceLimitExceeded** : Your AWS account is unable to launch any more instances
              of the specified instance type. You may be able to request an Amazon EC2 instance
              limit increase to recover.

              * **InsufficientFreeAddresses** : One or more of the subnets associated with your
              managed node group does not have enough available IP addresses for new nodes.

              * **AccessDenied** : Amazon EKS and or one or more of your managed nodes is unable to
              communicate with your cluster API server.

              * **InternalFailure** : These errors are usually caused by an Amazon EKS server-side
              issue.

            - **message** *(string) --*

              The error message associated with the issue.

            - **resourceIds** *(list) --*

              The AWS resources that are afflicted by this issue.

              - *(string) --*

      - **tags** *(dict) --*

        The metadata applied the node group to assist with categorization and organization. Each
        tag consists of a key and an optional value, both of which you define. Node group tags do
        not propagate to any other resources associated with the node group, such as the Amazon EC2
        instances or subnets.

        - *(string) --*

          - *(string) --*
    """


_ClientDescribeUpdateResponseupdateerrorsTypeDef = TypedDict(
    "_ClientDescribeUpdateResponseupdateerrorsTypeDef",
    {"errorCode": str, "errorMessage": str, "resourceIds": List[str]},
    total=False,
)


class ClientDescribeUpdateResponseupdateerrorsTypeDef(
    _ClientDescribeUpdateResponseupdateerrorsTypeDef
):
    """
    Type definition for `ClientDescribeUpdateResponseupdate` `errors`

    An object representing an error when an asynchronous operation fails.

    - **errorCode** *(string) --*

      A brief description of the error.

      * **SubnetNotFound** : We couldn't find one of the subnets associated with the cluster.

      * **SecurityGroupNotFound** : We couldn't find one of the security groups associated
      with the cluster.

      * **EniLimitReached** : You have reached the elastic network interface limit for your
      account.

      * **IpNotAvailable** : A subnet associated with the cluster doesn't have any free IP
      addresses.

      * **AccessDenied** : You don't have permissions to perform the specified operation.

      * **OperationNotPermitted** : The service role associated with the cluster doesn't have
      the required access permissions for Amazon EKS.

      * **VpcIdNotFound** : We couldn't find the VPC associated with the cluster.

    - **errorMessage** *(string) --*

      A more complete description of the error.

    - **resourceIds** *(list) --*

      An optional field that contains the resource IDs associated with the error.

      - *(string) --*
    """


_ClientDescribeUpdateResponseupdateparamsTypeDef = TypedDict(
    "_ClientDescribeUpdateResponseupdateparamsTypeDef",
    {"type": str, "value": str},
    total=False,
)


class ClientDescribeUpdateResponseupdateparamsTypeDef(
    _ClientDescribeUpdateResponseupdateparamsTypeDef
):
    """
    Type definition for `ClientDescribeUpdateResponseupdate` `params`

    An object representing the details of an update request.

    - **type** *(string) --*

      The keys associated with an update request.

    - **value** *(string) --*

      The value of the keys submitted as part of an update request.
    """


_ClientDescribeUpdateResponseupdateTypeDef = TypedDict(
    "_ClientDescribeUpdateResponseupdateTypeDef",
    {
        "id": str,
        "status": str,
        "type": str,
        "params": List[ClientDescribeUpdateResponseupdateparamsTypeDef],
        "createdAt": datetime,
        "errors": List[ClientDescribeUpdateResponseupdateerrorsTypeDef],
    },
    total=False,
)


class ClientDescribeUpdateResponseupdateTypeDef(
    _ClientDescribeUpdateResponseupdateTypeDef
):
    """
    Type definition for `ClientDescribeUpdateResponse` `update`

    The full description of the specified update.

    - **id** *(string) --*

      A UUID that is used to track the update.

    - **status** *(string) --*

      The current status of the update.

    - **type** *(string) --*

      The type of the update.

    - **params** *(list) --*

      A key-value map that contains the parameters associated with the update.

      - *(dict) --*

        An object representing the details of an update request.

        - **type** *(string) --*

          The keys associated with an update request.

        - **value** *(string) --*

          The value of the keys submitted as part of an update request.

    - **createdAt** *(datetime) --*

      The Unix epoch timestamp in seconds for when the update was created.

    - **errors** *(list) --*

      Any errors associated with a ``Failed`` update.

      - *(dict) --*

        An object representing an error when an asynchronous operation fails.

        - **errorCode** *(string) --*

          A brief description of the error.

          * **SubnetNotFound** : We couldn't find one of the subnets associated with the cluster.

          * **SecurityGroupNotFound** : We couldn't find one of the security groups associated
          with the cluster.

          * **EniLimitReached** : You have reached the elastic network interface limit for your
          account.

          * **IpNotAvailable** : A subnet associated with the cluster doesn't have any free IP
          addresses.

          * **AccessDenied** : You don't have permissions to perform the specified operation.

          * **OperationNotPermitted** : The service role associated with the cluster doesn't have
          the required access permissions for Amazon EKS.

          * **VpcIdNotFound** : We couldn't find the VPC associated with the cluster.

        - **errorMessage** *(string) --*

          A more complete description of the error.

        - **resourceIds** *(list) --*

          An optional field that contains the resource IDs associated with the error.

          - *(string) --*
    """


_ClientDescribeUpdateResponseTypeDef = TypedDict(
    "_ClientDescribeUpdateResponseTypeDef",
    {"update": ClientDescribeUpdateResponseupdateTypeDef},
    total=False,
)


class ClientDescribeUpdateResponseTypeDef(_ClientDescribeUpdateResponseTypeDef):
    """
    Type definition for `ClientDescribeUpdate` `Response`

    - **update** *(dict) --*

      The full description of the specified update.

      - **id** *(string) --*

        A UUID that is used to track the update.

      - **status** *(string) --*

        The current status of the update.

      - **type** *(string) --*

        The type of the update.

      - **params** *(list) --*

        A key-value map that contains the parameters associated with the update.

        - *(dict) --*

          An object representing the details of an update request.

          - **type** *(string) --*

            The keys associated with an update request.

          - **value** *(string) --*

            The value of the keys submitted as part of an update request.

      - **createdAt** *(datetime) --*

        The Unix epoch timestamp in seconds for when the update was created.

      - **errors** *(list) --*

        Any errors associated with a ``Failed`` update.

        - *(dict) --*

          An object representing an error when an asynchronous operation fails.

          - **errorCode** *(string) --*

            A brief description of the error.

            * **SubnetNotFound** : We couldn't find one of the subnets associated with the cluster.

            * **SecurityGroupNotFound** : We couldn't find one of the security groups associated
            with the cluster.

            * **EniLimitReached** : You have reached the elastic network interface limit for your
            account.

            * **IpNotAvailable** : A subnet associated with the cluster doesn't have any free IP
            addresses.

            * **AccessDenied** : You don't have permissions to perform the specified operation.

            * **OperationNotPermitted** : The service role associated with the cluster doesn't have
            the required access permissions for Amazon EKS.

            * **VpcIdNotFound** : We couldn't find the VPC associated with the cluster.

          - **errorMessage** *(string) --*

            A more complete description of the error.

          - **resourceIds** *(list) --*

            An optional field that contains the resource IDs associated with the error.

            - *(string) --*
    """


_ClientListClustersResponseTypeDef = TypedDict(
    "_ClientListClustersResponseTypeDef",
    {"clusters": List[str], "nextToken": str},
    total=False,
)


class ClientListClustersResponseTypeDef(_ClientListClustersResponseTypeDef):
    """
    Type definition for `ClientListClusters` `Response`

    - **clusters** *(list) --*

      A list of all of the clusters for your account in the specified Region.

      - *(string) --*

    - **nextToken** *(string) --*

      The ``nextToken`` value to include in a future ``ListClusters`` request. When the results of
      a ``ListClusters`` request exceed ``maxResults`` , you can use this value to retrieve the
      next page of results. This value is ``null`` when there are no more results to return.
    """


_ClientListNodegroupsResponseTypeDef = TypedDict(
    "_ClientListNodegroupsResponseTypeDef",
    {"nodegroups": List[str], "nextToken": str},
    total=False,
)


class ClientListNodegroupsResponseTypeDef(_ClientListNodegroupsResponseTypeDef):
    """
    Type definition for `ClientListNodegroups` `Response`

    - **nodegroups** *(list) --*

      A list of all of the node groups associated with the specified cluster.

      - *(string) --*

    - **nextToken** *(string) --*

      The ``nextToken`` value to include in a future ``ListNodegroups`` request. When the results
      of a ``ListNodegroups`` request exceed ``maxResults`` , you can use this value to retrieve
      the next page of results. This value is ``null`` when there are no more results to return.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef", {"tags": Dict[str, str]}, total=False
)


class ClientListTagsForResourceResponseTypeDef(
    _ClientListTagsForResourceResponseTypeDef
):
    """
    Type definition for `ClientListTagsForResource` `Response`

    - **tags** *(dict) --*

      The tags for the resource.

      - *(string) --*

        - *(string) --*
    """


_ClientListUpdatesResponseTypeDef = TypedDict(
    "_ClientListUpdatesResponseTypeDef",
    {"updateIds": List[str], "nextToken": str},
    total=False,
)


class ClientListUpdatesResponseTypeDef(_ClientListUpdatesResponseTypeDef):
    """
    Type definition for `ClientListUpdates` `Response`

    - **updateIds** *(list) --*

      A list of all the updates for the specified cluster and Region.

      - *(string) --*

    - **nextToken** *(string) --*

      The ``nextToken`` value to include in a future ``ListUpdates`` request. When the results of a
      ``ListUpdates`` request exceed ``maxResults`` , you can use this value to retrieve the next
      page of results. This value is ``null`` when there are no more results to return.
    """


_ClientUpdateClusterConfigResponseupdateerrorsTypeDef = TypedDict(
    "_ClientUpdateClusterConfigResponseupdateerrorsTypeDef",
    {"errorCode": str, "errorMessage": str, "resourceIds": List[str]},
    total=False,
)


class ClientUpdateClusterConfigResponseupdateerrorsTypeDef(
    _ClientUpdateClusterConfigResponseupdateerrorsTypeDef
):
    """
    Type definition for `ClientUpdateClusterConfigResponseupdate` `errors`

    An object representing an error when an asynchronous operation fails.

    - **errorCode** *(string) --*

      A brief description of the error.

      * **SubnetNotFound** : We couldn't find one of the subnets associated with the cluster.

      * **SecurityGroupNotFound** : We couldn't find one of the security groups associated
      with the cluster.

      * **EniLimitReached** : You have reached the elastic network interface limit for your
      account.

      * **IpNotAvailable** : A subnet associated with the cluster doesn't have any free IP
      addresses.

      * **AccessDenied** : You don't have permissions to perform the specified operation.

      * **OperationNotPermitted** : The service role associated with the cluster doesn't have
      the required access permissions for Amazon EKS.

      * **VpcIdNotFound** : We couldn't find the VPC associated with the cluster.

    - **errorMessage** *(string) --*

      A more complete description of the error.

    - **resourceIds** *(list) --*

      An optional field that contains the resource IDs associated with the error.

      - *(string) --*
    """


_ClientUpdateClusterConfigResponseupdateparamsTypeDef = TypedDict(
    "_ClientUpdateClusterConfigResponseupdateparamsTypeDef",
    {"type": str, "value": str},
    total=False,
)


class ClientUpdateClusterConfigResponseupdateparamsTypeDef(
    _ClientUpdateClusterConfigResponseupdateparamsTypeDef
):
    """
    Type definition for `ClientUpdateClusterConfigResponseupdate` `params`

    An object representing the details of an update request.

    - **type** *(string) --*

      The keys associated with an update request.

    - **value** *(string) --*

      The value of the keys submitted as part of an update request.
    """


_ClientUpdateClusterConfigResponseupdateTypeDef = TypedDict(
    "_ClientUpdateClusterConfigResponseupdateTypeDef",
    {
        "id": str,
        "status": str,
        "type": str,
        "params": List[ClientUpdateClusterConfigResponseupdateparamsTypeDef],
        "createdAt": datetime,
        "errors": List[ClientUpdateClusterConfigResponseupdateerrorsTypeDef],
    },
    total=False,
)


class ClientUpdateClusterConfigResponseupdateTypeDef(
    _ClientUpdateClusterConfigResponseupdateTypeDef
):
    """
    Type definition for `ClientUpdateClusterConfigResponse` `update`

    An object representing an asynchronous update.

    - **id** *(string) --*

      A UUID that is used to track the update.

    - **status** *(string) --*

      The current status of the update.

    - **type** *(string) --*

      The type of the update.

    - **params** *(list) --*

      A key-value map that contains the parameters associated with the update.

      - *(dict) --*

        An object representing the details of an update request.

        - **type** *(string) --*

          The keys associated with an update request.

        - **value** *(string) --*

          The value of the keys submitted as part of an update request.

    - **createdAt** *(datetime) --*

      The Unix epoch timestamp in seconds for when the update was created.

    - **errors** *(list) --*

      Any errors associated with a ``Failed`` update.

      - *(dict) --*

        An object representing an error when an asynchronous operation fails.

        - **errorCode** *(string) --*

          A brief description of the error.

          * **SubnetNotFound** : We couldn't find one of the subnets associated with the cluster.

          * **SecurityGroupNotFound** : We couldn't find one of the security groups associated
          with the cluster.

          * **EniLimitReached** : You have reached the elastic network interface limit for your
          account.

          * **IpNotAvailable** : A subnet associated with the cluster doesn't have any free IP
          addresses.

          * **AccessDenied** : You don't have permissions to perform the specified operation.

          * **OperationNotPermitted** : The service role associated with the cluster doesn't have
          the required access permissions for Amazon EKS.

          * **VpcIdNotFound** : We couldn't find the VPC associated with the cluster.

        - **errorMessage** *(string) --*

          A more complete description of the error.

        - **resourceIds** *(list) --*

          An optional field that contains the resource IDs associated with the error.

          - *(string) --*
    """


_ClientUpdateClusterConfigResponseTypeDef = TypedDict(
    "_ClientUpdateClusterConfigResponseTypeDef",
    {"update": ClientUpdateClusterConfigResponseupdateTypeDef},
    total=False,
)


class ClientUpdateClusterConfigResponseTypeDef(
    _ClientUpdateClusterConfigResponseTypeDef
):
    """
    Type definition for `ClientUpdateClusterConfig` `Response`

    - **update** *(dict) --*

      An object representing an asynchronous update.

      - **id** *(string) --*

        A UUID that is used to track the update.

      - **status** *(string) --*

        The current status of the update.

      - **type** *(string) --*

        The type of the update.

      - **params** *(list) --*

        A key-value map that contains the parameters associated with the update.

        - *(dict) --*

          An object representing the details of an update request.

          - **type** *(string) --*

            The keys associated with an update request.

          - **value** *(string) --*

            The value of the keys submitted as part of an update request.

      - **createdAt** *(datetime) --*

        The Unix epoch timestamp in seconds for when the update was created.

      - **errors** *(list) --*

        Any errors associated with a ``Failed`` update.

        - *(dict) --*

          An object representing an error when an asynchronous operation fails.

          - **errorCode** *(string) --*

            A brief description of the error.

            * **SubnetNotFound** : We couldn't find one of the subnets associated with the cluster.

            * **SecurityGroupNotFound** : We couldn't find one of the security groups associated
            with the cluster.

            * **EniLimitReached** : You have reached the elastic network interface limit for your
            account.

            * **IpNotAvailable** : A subnet associated with the cluster doesn't have any free IP
            addresses.

            * **AccessDenied** : You don't have permissions to perform the specified operation.

            * **OperationNotPermitted** : The service role associated with the cluster doesn't have
            the required access permissions for Amazon EKS.

            * **VpcIdNotFound** : We couldn't find the VPC associated with the cluster.

          - **errorMessage** *(string) --*

            A more complete description of the error.

          - **resourceIds** *(list) --*

            An optional field that contains the resource IDs associated with the error.

            - *(string) --*
    """


_ClientUpdateClusterConfigloggingclusterLoggingTypeDef = TypedDict(
    "_ClientUpdateClusterConfigloggingclusterLoggingTypeDef",
    {"types": List[str], "enabled": bool},
    total=False,
)


class ClientUpdateClusterConfigloggingclusterLoggingTypeDef(
    _ClientUpdateClusterConfigloggingclusterLoggingTypeDef
):
    """
    Type definition for `ClientUpdateClusterConfiglogging` `clusterLogging`

    An object representing the enabled or disabled Kubernetes control plane logs for your cluster.

    - **types** *(list) --*

      The available cluster control plane log types.

      - *(string) --*

    - **enabled** *(boolean) --*

      If a log type is enabled, that log type exports its control plane logs to CloudWatch Logs.
      If a log type isn't enabled, that log type doesn't export its control plane logs. Each
      individual log type can be enabled or disabled independently.
    """


_ClientUpdateClusterConfigloggingTypeDef = TypedDict(
    "_ClientUpdateClusterConfigloggingTypeDef",
    {"clusterLogging": List[ClientUpdateClusterConfigloggingclusterLoggingTypeDef]},
    total=False,
)


class ClientUpdateClusterConfigloggingTypeDef(_ClientUpdateClusterConfigloggingTypeDef):
    """
    Type definition for `ClientUpdateClusterConfig` `logging`

    Enable or disable exporting the Kubernetes control plane logs for your cluster to CloudWatch
    Logs. By default, cluster control plane logs aren't exported to CloudWatch Logs. For more
    information, see `Amazon EKS Cluster Control Plane Logs
    <https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html>`__ in the * *Amazon
    EKS User Guide* * .

    .. note::

      CloudWatch Logs ingestion, archive storage, and data scanning rates apply to exported control
      plane logs. For more information, see `Amazon CloudWatch Pricing
      <http://aws.amazon.com/cloudwatch/pricing/>`__ .

    - **clusterLogging** *(list) --*

      The cluster control plane logging configuration for your cluster.

      - *(dict) --*

        An object representing the enabled or disabled Kubernetes control plane logs for your cluster.

        - **types** *(list) --*

          The available cluster control plane log types.

          - *(string) --*

        - **enabled** *(boolean) --*

          If a log type is enabled, that log type exports its control plane logs to CloudWatch Logs.
          If a log type isn't enabled, that log type doesn't export its control plane logs. Each
          individual log type can be enabled or disabled independently.
    """


_ClientUpdateClusterConfigresourcesVpcConfigTypeDef = TypedDict(
    "_ClientUpdateClusterConfigresourcesVpcConfigTypeDef",
    {
        "subnetIds": List[str],
        "securityGroupIds": List[str],
        "endpointPublicAccess": bool,
        "endpointPrivateAccess": bool,
    },
    total=False,
)


class ClientUpdateClusterConfigresourcesVpcConfigTypeDef(
    _ClientUpdateClusterConfigresourcesVpcConfigTypeDef
):
    """
    Type definition for `ClientUpdateClusterConfig` `resourcesVpcConfig`

    An object representing the VPC configuration to use for an Amazon EKS cluster.

    - **subnetIds** *(list) --*

      Specify subnets for your Amazon EKS worker nodes. Amazon EKS creates cross-account elastic
      network interfaces in these subnets to allow communication between your worker nodes and the
      Kubernetes control plane.

      - *(string) --*

    - **securityGroupIds** *(list) --*

      Specify one or more security groups for the cross-account elastic network interfaces that
      Amazon EKS creates to use to allow communication between your worker nodes and the Kubernetes
      control plane. If you don't specify a security group, the default security group for your VPC
      is used.

      - *(string) --*

    - **endpointPublicAccess** *(boolean) --*

      Set this value to ``false`` to disable public access for your cluster's Kubernetes API server
      endpoint. If you disable public access, your cluster's Kubernetes API server can receive only
      requests from within the cluster VPC. The default value for this parameter is ``true`` , which
      enables public access for your Kubernetes API server. For more information, see `Amazon EKS
      Cluster Endpoint Access Control
      <https://docs.aws.amazon.com/eks/latest/userguide/cluster-endpoint.html>`__ in the * *Amazon
      EKS User Guide* * .

    - **endpointPrivateAccess** *(boolean) --*

      Set this value to ``true`` to enable private access for your cluster's Kubernetes API server
      endpoint. If you enable private access, Kubernetes API requests from within your cluster's VPC
      use the private VPC endpoint. The default value for this parameter is ``false`` , which
      disables private access for your Kubernetes API server. For more information, see `Amazon EKS
      Cluster Endpoint Access Control
      <https://docs.aws.amazon.com/eks/latest/userguide/cluster-endpoint.html>`__ in the * *Amazon
      EKS User Guide* * .
    """


_ClientUpdateClusterVersionResponseupdateerrorsTypeDef = TypedDict(
    "_ClientUpdateClusterVersionResponseupdateerrorsTypeDef",
    {"errorCode": str, "errorMessage": str, "resourceIds": List[str]},
    total=False,
)


class ClientUpdateClusterVersionResponseupdateerrorsTypeDef(
    _ClientUpdateClusterVersionResponseupdateerrorsTypeDef
):
    """
    Type definition for `ClientUpdateClusterVersionResponseupdate` `errors`

    An object representing an error when an asynchronous operation fails.

    - **errorCode** *(string) --*

      A brief description of the error.

      * **SubnetNotFound** : We couldn't find one of the subnets associated with the cluster.

      * **SecurityGroupNotFound** : We couldn't find one of the security groups associated
      with the cluster.

      * **EniLimitReached** : You have reached the elastic network interface limit for your
      account.

      * **IpNotAvailable** : A subnet associated with the cluster doesn't have any free IP
      addresses.

      * **AccessDenied** : You don't have permissions to perform the specified operation.

      * **OperationNotPermitted** : The service role associated with the cluster doesn't have
      the required access permissions for Amazon EKS.

      * **VpcIdNotFound** : We couldn't find the VPC associated with the cluster.

    - **errorMessage** *(string) --*

      A more complete description of the error.

    - **resourceIds** *(list) --*

      An optional field that contains the resource IDs associated with the error.

      - *(string) --*
    """


_ClientUpdateClusterVersionResponseupdateparamsTypeDef = TypedDict(
    "_ClientUpdateClusterVersionResponseupdateparamsTypeDef",
    {"type": str, "value": str},
    total=False,
)


class ClientUpdateClusterVersionResponseupdateparamsTypeDef(
    _ClientUpdateClusterVersionResponseupdateparamsTypeDef
):
    """
    Type definition for `ClientUpdateClusterVersionResponseupdate` `params`

    An object representing the details of an update request.

    - **type** *(string) --*

      The keys associated with an update request.

    - **value** *(string) --*

      The value of the keys submitted as part of an update request.
    """


_ClientUpdateClusterVersionResponseupdateTypeDef = TypedDict(
    "_ClientUpdateClusterVersionResponseupdateTypeDef",
    {
        "id": str,
        "status": str,
        "type": str,
        "params": List[ClientUpdateClusterVersionResponseupdateparamsTypeDef],
        "createdAt": datetime,
        "errors": List[ClientUpdateClusterVersionResponseupdateerrorsTypeDef],
    },
    total=False,
)


class ClientUpdateClusterVersionResponseupdateTypeDef(
    _ClientUpdateClusterVersionResponseupdateTypeDef
):
    """
    Type definition for `ClientUpdateClusterVersionResponse` `update`

    The full description of the specified update

    - **id** *(string) --*

      A UUID that is used to track the update.

    - **status** *(string) --*

      The current status of the update.

    - **type** *(string) --*

      The type of the update.

    - **params** *(list) --*

      A key-value map that contains the parameters associated with the update.

      - *(dict) --*

        An object representing the details of an update request.

        - **type** *(string) --*

          The keys associated with an update request.

        - **value** *(string) --*

          The value of the keys submitted as part of an update request.

    - **createdAt** *(datetime) --*

      The Unix epoch timestamp in seconds for when the update was created.

    - **errors** *(list) --*

      Any errors associated with a ``Failed`` update.

      - *(dict) --*

        An object representing an error when an asynchronous operation fails.

        - **errorCode** *(string) --*

          A brief description of the error.

          * **SubnetNotFound** : We couldn't find one of the subnets associated with the cluster.

          * **SecurityGroupNotFound** : We couldn't find one of the security groups associated
          with the cluster.

          * **EniLimitReached** : You have reached the elastic network interface limit for your
          account.

          * **IpNotAvailable** : A subnet associated with the cluster doesn't have any free IP
          addresses.

          * **AccessDenied** : You don't have permissions to perform the specified operation.

          * **OperationNotPermitted** : The service role associated with the cluster doesn't have
          the required access permissions for Amazon EKS.

          * **VpcIdNotFound** : We couldn't find the VPC associated with the cluster.

        - **errorMessage** *(string) --*

          A more complete description of the error.

        - **resourceIds** *(list) --*

          An optional field that contains the resource IDs associated with the error.

          - *(string) --*
    """


_ClientUpdateClusterVersionResponseTypeDef = TypedDict(
    "_ClientUpdateClusterVersionResponseTypeDef",
    {"update": ClientUpdateClusterVersionResponseupdateTypeDef},
    total=False,
)


class ClientUpdateClusterVersionResponseTypeDef(
    _ClientUpdateClusterVersionResponseTypeDef
):
    """
    Type definition for `ClientUpdateClusterVersion` `Response`

    - **update** *(dict) --*

      The full description of the specified update

      - **id** *(string) --*

        A UUID that is used to track the update.

      - **status** *(string) --*

        The current status of the update.

      - **type** *(string) --*

        The type of the update.

      - **params** *(list) --*

        A key-value map that contains the parameters associated with the update.

        - *(dict) --*

          An object representing the details of an update request.

          - **type** *(string) --*

            The keys associated with an update request.

          - **value** *(string) --*

            The value of the keys submitted as part of an update request.

      - **createdAt** *(datetime) --*

        The Unix epoch timestamp in seconds for when the update was created.

      - **errors** *(list) --*

        Any errors associated with a ``Failed`` update.

        - *(dict) --*

          An object representing an error when an asynchronous operation fails.

          - **errorCode** *(string) --*

            A brief description of the error.

            * **SubnetNotFound** : We couldn't find one of the subnets associated with the cluster.

            * **SecurityGroupNotFound** : We couldn't find one of the security groups associated
            with the cluster.

            * **EniLimitReached** : You have reached the elastic network interface limit for your
            account.

            * **IpNotAvailable** : A subnet associated with the cluster doesn't have any free IP
            addresses.

            * **AccessDenied** : You don't have permissions to perform the specified operation.

            * **OperationNotPermitted** : The service role associated with the cluster doesn't have
            the required access permissions for Amazon EKS.

            * **VpcIdNotFound** : We couldn't find the VPC associated with the cluster.

          - **errorMessage** *(string) --*

            A more complete description of the error.

          - **resourceIds** *(list) --*

            An optional field that contains the resource IDs associated with the error.

            - *(string) --*
    """


_ClientUpdateNodegroupConfigResponseupdateerrorsTypeDef = TypedDict(
    "_ClientUpdateNodegroupConfigResponseupdateerrorsTypeDef",
    {"errorCode": str, "errorMessage": str, "resourceIds": List[str]},
    total=False,
)


class ClientUpdateNodegroupConfigResponseupdateerrorsTypeDef(
    _ClientUpdateNodegroupConfigResponseupdateerrorsTypeDef
):
    """
    Type definition for `ClientUpdateNodegroupConfigResponseupdate` `errors`

    An object representing an error when an asynchronous operation fails.

    - **errorCode** *(string) --*

      A brief description of the error.

      * **SubnetNotFound** : We couldn't find one of the subnets associated with the cluster.

      * **SecurityGroupNotFound** : We couldn't find one of the security groups associated
      with the cluster.

      * **EniLimitReached** : You have reached the elastic network interface limit for your
      account.

      * **IpNotAvailable** : A subnet associated with the cluster doesn't have any free IP
      addresses.

      * **AccessDenied** : You don't have permissions to perform the specified operation.

      * **OperationNotPermitted** : The service role associated with the cluster doesn't have
      the required access permissions for Amazon EKS.

      * **VpcIdNotFound** : We couldn't find the VPC associated with the cluster.

    - **errorMessage** *(string) --*

      A more complete description of the error.

    - **resourceIds** *(list) --*

      An optional field that contains the resource IDs associated with the error.

      - *(string) --*
    """


_ClientUpdateNodegroupConfigResponseupdateparamsTypeDef = TypedDict(
    "_ClientUpdateNodegroupConfigResponseupdateparamsTypeDef",
    {"type": str, "value": str},
    total=False,
)


class ClientUpdateNodegroupConfigResponseupdateparamsTypeDef(
    _ClientUpdateNodegroupConfigResponseupdateparamsTypeDef
):
    """
    Type definition for `ClientUpdateNodegroupConfigResponseupdate` `params`

    An object representing the details of an update request.

    - **type** *(string) --*

      The keys associated with an update request.

    - **value** *(string) --*

      The value of the keys submitted as part of an update request.
    """


_ClientUpdateNodegroupConfigResponseupdateTypeDef = TypedDict(
    "_ClientUpdateNodegroupConfigResponseupdateTypeDef",
    {
        "id": str,
        "status": str,
        "type": str,
        "params": List[ClientUpdateNodegroupConfigResponseupdateparamsTypeDef],
        "createdAt": datetime,
        "errors": List[ClientUpdateNodegroupConfigResponseupdateerrorsTypeDef],
    },
    total=False,
)


class ClientUpdateNodegroupConfigResponseupdateTypeDef(
    _ClientUpdateNodegroupConfigResponseupdateTypeDef
):
    """
    Type definition for `ClientUpdateNodegroupConfigResponse` `update`

    An object representing an asynchronous update.

    - **id** *(string) --*

      A UUID that is used to track the update.

    - **status** *(string) --*

      The current status of the update.

    - **type** *(string) --*

      The type of the update.

    - **params** *(list) --*

      A key-value map that contains the parameters associated with the update.

      - *(dict) --*

        An object representing the details of an update request.

        - **type** *(string) --*

          The keys associated with an update request.

        - **value** *(string) --*

          The value of the keys submitted as part of an update request.

    - **createdAt** *(datetime) --*

      The Unix epoch timestamp in seconds for when the update was created.

    - **errors** *(list) --*

      Any errors associated with a ``Failed`` update.

      - *(dict) --*

        An object representing an error when an asynchronous operation fails.

        - **errorCode** *(string) --*

          A brief description of the error.

          * **SubnetNotFound** : We couldn't find one of the subnets associated with the cluster.

          * **SecurityGroupNotFound** : We couldn't find one of the security groups associated
          with the cluster.

          * **EniLimitReached** : You have reached the elastic network interface limit for your
          account.

          * **IpNotAvailable** : A subnet associated with the cluster doesn't have any free IP
          addresses.

          * **AccessDenied** : You don't have permissions to perform the specified operation.

          * **OperationNotPermitted** : The service role associated with the cluster doesn't have
          the required access permissions for Amazon EKS.

          * **VpcIdNotFound** : We couldn't find the VPC associated with the cluster.

        - **errorMessage** *(string) --*

          A more complete description of the error.

        - **resourceIds** *(list) --*

          An optional field that contains the resource IDs associated with the error.

          - *(string) --*
    """


_ClientUpdateNodegroupConfigResponseTypeDef = TypedDict(
    "_ClientUpdateNodegroupConfigResponseTypeDef",
    {"update": ClientUpdateNodegroupConfigResponseupdateTypeDef},
    total=False,
)


class ClientUpdateNodegroupConfigResponseTypeDef(
    _ClientUpdateNodegroupConfigResponseTypeDef
):
    """
    Type definition for `ClientUpdateNodegroupConfig` `Response`

    - **update** *(dict) --*

      An object representing an asynchronous update.

      - **id** *(string) --*

        A UUID that is used to track the update.

      - **status** *(string) --*

        The current status of the update.

      - **type** *(string) --*

        The type of the update.

      - **params** *(list) --*

        A key-value map that contains the parameters associated with the update.

        - *(dict) --*

          An object representing the details of an update request.

          - **type** *(string) --*

            The keys associated with an update request.

          - **value** *(string) --*

            The value of the keys submitted as part of an update request.

      - **createdAt** *(datetime) --*

        The Unix epoch timestamp in seconds for when the update was created.

      - **errors** *(list) --*

        Any errors associated with a ``Failed`` update.

        - *(dict) --*

          An object representing an error when an asynchronous operation fails.

          - **errorCode** *(string) --*

            A brief description of the error.

            * **SubnetNotFound** : We couldn't find one of the subnets associated with the cluster.

            * **SecurityGroupNotFound** : We couldn't find one of the security groups associated
            with the cluster.

            * **EniLimitReached** : You have reached the elastic network interface limit for your
            account.

            * **IpNotAvailable** : A subnet associated with the cluster doesn't have any free IP
            addresses.

            * **AccessDenied** : You don't have permissions to perform the specified operation.

            * **OperationNotPermitted** : The service role associated with the cluster doesn't have
            the required access permissions for Amazon EKS.

            * **VpcIdNotFound** : We couldn't find the VPC associated with the cluster.

          - **errorMessage** *(string) --*

            A more complete description of the error.

          - **resourceIds** *(list) --*

            An optional field that contains the resource IDs associated with the error.

            - *(string) --*
    """


_ClientUpdateNodegroupConfiglabelsTypeDef = TypedDict(
    "_ClientUpdateNodegroupConfiglabelsTypeDef",
    {"addOrUpdateLabels": Dict[str, str], "removeLabels": List[str]},
    total=False,
)


class ClientUpdateNodegroupConfiglabelsTypeDef(
    _ClientUpdateNodegroupConfiglabelsTypeDef
):
    """
    Type definition for `ClientUpdateNodegroupConfig` `labels`

    The Kubernetes labels to be applied to the nodes in the node group after the update.

    - **addOrUpdateLabels** *(dict) --*

      Kubernetes labels to be added or updated.

      - *(string) --*

        - *(string) --*

    - **removeLabels** *(list) --*

      Kubernetes labels to be removed.

      - *(string) --*
    """


_ClientUpdateNodegroupConfigscalingConfigTypeDef = TypedDict(
    "_ClientUpdateNodegroupConfigscalingConfigTypeDef",
    {"minSize": int, "maxSize": int, "desiredSize": int},
    total=False,
)


class ClientUpdateNodegroupConfigscalingConfigTypeDef(
    _ClientUpdateNodegroupConfigscalingConfigTypeDef
):
    """
    Type definition for `ClientUpdateNodegroupConfig` `scalingConfig`

    The scaling configuration details for the AutoScaling group after the update.

    - **minSize** *(integer) --*

      The minimum number of worker nodes that the managed node group can scale in to. This number
      must be greater than zero.

    - **maxSize** *(integer) --*

      The maximum number of worker nodes that the managed node group can scale out to. Managed node
      groups can support up to 100 nodes by default.

    - **desiredSize** *(integer) --*

      The current number of worker nodes that the managed node group should maintain.
    """


_ClientUpdateNodegroupVersionResponseupdateerrorsTypeDef = TypedDict(
    "_ClientUpdateNodegroupVersionResponseupdateerrorsTypeDef",
    {"errorCode": str, "errorMessage": str, "resourceIds": List[str]},
    total=False,
)


class ClientUpdateNodegroupVersionResponseupdateerrorsTypeDef(
    _ClientUpdateNodegroupVersionResponseupdateerrorsTypeDef
):
    """
    Type definition for `ClientUpdateNodegroupVersionResponseupdate` `errors`

    An object representing an error when an asynchronous operation fails.

    - **errorCode** *(string) --*

      A brief description of the error.

      * **SubnetNotFound** : We couldn't find one of the subnets associated with the cluster.

      * **SecurityGroupNotFound** : We couldn't find one of the security groups associated
      with the cluster.

      * **EniLimitReached** : You have reached the elastic network interface limit for your
      account.

      * **IpNotAvailable** : A subnet associated with the cluster doesn't have any free IP
      addresses.

      * **AccessDenied** : You don't have permissions to perform the specified operation.

      * **OperationNotPermitted** : The service role associated with the cluster doesn't have
      the required access permissions for Amazon EKS.

      * **VpcIdNotFound** : We couldn't find the VPC associated with the cluster.

    - **errorMessage** *(string) --*

      A more complete description of the error.

    - **resourceIds** *(list) --*

      An optional field that contains the resource IDs associated with the error.

      - *(string) --*
    """


_ClientUpdateNodegroupVersionResponseupdateparamsTypeDef = TypedDict(
    "_ClientUpdateNodegroupVersionResponseupdateparamsTypeDef",
    {"type": str, "value": str},
    total=False,
)


class ClientUpdateNodegroupVersionResponseupdateparamsTypeDef(
    _ClientUpdateNodegroupVersionResponseupdateparamsTypeDef
):
    """
    Type definition for `ClientUpdateNodegroupVersionResponseupdate` `params`

    An object representing the details of an update request.

    - **type** *(string) --*

      The keys associated with an update request.

    - **value** *(string) --*

      The value of the keys submitted as part of an update request.
    """


_ClientUpdateNodegroupVersionResponseupdateTypeDef = TypedDict(
    "_ClientUpdateNodegroupVersionResponseupdateTypeDef",
    {
        "id": str,
        "status": str,
        "type": str,
        "params": List[ClientUpdateNodegroupVersionResponseupdateparamsTypeDef],
        "createdAt": datetime,
        "errors": List[ClientUpdateNodegroupVersionResponseupdateerrorsTypeDef],
    },
    total=False,
)


class ClientUpdateNodegroupVersionResponseupdateTypeDef(
    _ClientUpdateNodegroupVersionResponseupdateTypeDef
):
    """
    Type definition for `ClientUpdateNodegroupVersionResponse` `update`

    An object representing an asynchronous update.

    - **id** *(string) --*

      A UUID that is used to track the update.

    - **status** *(string) --*

      The current status of the update.

    - **type** *(string) --*

      The type of the update.

    - **params** *(list) --*

      A key-value map that contains the parameters associated with the update.

      - *(dict) --*

        An object representing the details of an update request.

        - **type** *(string) --*

          The keys associated with an update request.

        - **value** *(string) --*

          The value of the keys submitted as part of an update request.

    - **createdAt** *(datetime) --*

      The Unix epoch timestamp in seconds for when the update was created.

    - **errors** *(list) --*

      Any errors associated with a ``Failed`` update.

      - *(dict) --*

        An object representing an error when an asynchronous operation fails.

        - **errorCode** *(string) --*

          A brief description of the error.

          * **SubnetNotFound** : We couldn't find one of the subnets associated with the cluster.

          * **SecurityGroupNotFound** : We couldn't find one of the security groups associated
          with the cluster.

          * **EniLimitReached** : You have reached the elastic network interface limit for your
          account.

          * **IpNotAvailable** : A subnet associated with the cluster doesn't have any free IP
          addresses.

          * **AccessDenied** : You don't have permissions to perform the specified operation.

          * **OperationNotPermitted** : The service role associated with the cluster doesn't have
          the required access permissions for Amazon EKS.

          * **VpcIdNotFound** : We couldn't find the VPC associated with the cluster.

        - **errorMessage** *(string) --*

          A more complete description of the error.

        - **resourceIds** *(list) --*

          An optional field that contains the resource IDs associated with the error.

          - *(string) --*
    """


_ClientUpdateNodegroupVersionResponseTypeDef = TypedDict(
    "_ClientUpdateNodegroupVersionResponseTypeDef",
    {"update": ClientUpdateNodegroupVersionResponseupdateTypeDef},
    total=False,
)


class ClientUpdateNodegroupVersionResponseTypeDef(
    _ClientUpdateNodegroupVersionResponseTypeDef
):
    """
    Type definition for `ClientUpdateNodegroupVersion` `Response`

    - **update** *(dict) --*

      An object representing an asynchronous update.

      - **id** *(string) --*

        A UUID that is used to track the update.

      - **status** *(string) --*

        The current status of the update.

      - **type** *(string) --*

        The type of the update.

      - **params** *(list) --*

        A key-value map that contains the parameters associated with the update.

        - *(dict) --*

          An object representing the details of an update request.

          - **type** *(string) --*

            The keys associated with an update request.

          - **value** *(string) --*

            The value of the keys submitted as part of an update request.

      - **createdAt** *(datetime) --*

        The Unix epoch timestamp in seconds for when the update was created.

      - **errors** *(list) --*

        Any errors associated with a ``Failed`` update.

        - *(dict) --*

          An object representing an error when an asynchronous operation fails.

          - **errorCode** *(string) --*

            A brief description of the error.

            * **SubnetNotFound** : We couldn't find one of the subnets associated with the cluster.

            * **SecurityGroupNotFound** : We couldn't find one of the security groups associated
            with the cluster.

            * **EniLimitReached** : You have reached the elastic network interface limit for your
            account.

            * **IpNotAvailable** : A subnet associated with the cluster doesn't have any free IP
            addresses.

            * **AccessDenied** : You don't have permissions to perform the specified operation.

            * **OperationNotPermitted** : The service role associated with the cluster doesn't have
            the required access permissions for Amazon EKS.

            * **VpcIdNotFound** : We couldn't find the VPC associated with the cluster.

          - **errorMessage** *(string) --*

            A more complete description of the error.

          - **resourceIds** *(list) --*

            An optional field that contains the resource IDs associated with the error.

            - *(string) --*
    """


_ClusterActiveWaitWaiterConfigTypeDef = TypedDict(
    "_ClusterActiveWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class ClusterActiveWaitWaiterConfigTypeDef(_ClusterActiveWaitWaiterConfigTypeDef):
    """
    Type definition for `ClusterActiveWait` `WaiterConfig`

    A dictionary that provides parameters to control waiting behavior.

    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 30

    - **MaxAttempts** *(integer) --*

      The maximum number of attempts to be made. Default: 40
    """


_ClusterDeletedWaitWaiterConfigTypeDef = TypedDict(
    "_ClusterDeletedWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class ClusterDeletedWaitWaiterConfigTypeDef(_ClusterDeletedWaitWaiterConfigTypeDef):
    """
    Type definition for `ClusterDeletedWait` `WaiterConfig`

    A dictionary that provides parameters to control waiting behavior.

    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 30

    - **MaxAttempts** *(integer) --*

      The maximum number of attempts to be made. Default: 40
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


_ListClustersPaginateResponseTypeDef = TypedDict(
    "_ListClustersPaginateResponseTypeDef",
    {"clusters": List[str], "NextToken": str},
    total=False,
)


class ListClustersPaginateResponseTypeDef(_ListClustersPaginateResponseTypeDef):
    """
    Type definition for `ListClustersPaginate` `Response`

    - **clusters** *(list) --*

      A list of all of the clusters for your account in the specified Region.

      - *(string) --*

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListNodegroupsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListNodegroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListNodegroupsPaginatePaginationConfigTypeDef(
    _ListNodegroupsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListNodegroupsPaginate` `PaginationConfig`

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


_ListNodegroupsPaginateResponseTypeDef = TypedDict(
    "_ListNodegroupsPaginateResponseTypeDef",
    {"nodegroups": List[str], "NextToken": str},
    total=False,
)


class ListNodegroupsPaginateResponseTypeDef(_ListNodegroupsPaginateResponseTypeDef):
    """
    Type definition for `ListNodegroupsPaginate` `Response`

    - **nodegroups** *(list) --*

      A list of all of the node groups associated with the specified cluster.

      - *(string) --*

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListUpdatesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListUpdatesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListUpdatesPaginatePaginationConfigTypeDef(
    _ListUpdatesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListUpdatesPaginate` `PaginationConfig`

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


_ListUpdatesPaginateResponseTypeDef = TypedDict(
    "_ListUpdatesPaginateResponseTypeDef",
    {"updateIds": List[str], "NextToken": str},
    total=False,
)


class ListUpdatesPaginateResponseTypeDef(_ListUpdatesPaginateResponseTypeDef):
    """
    Type definition for `ListUpdatesPaginate` `Response`

    - **updateIds** *(list) --*

      A list of all the updates for the specified cluster and Region.

      - *(string) --*

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_NodegroupActiveWaitWaiterConfigTypeDef = TypedDict(
    "_NodegroupActiveWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class NodegroupActiveWaitWaiterConfigTypeDef(_NodegroupActiveWaitWaiterConfigTypeDef):
    """
    Type definition for `NodegroupActiveWait` `WaiterConfig`

    A dictionary that provides parameters to control waiting behavior.

    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 30

    - **MaxAttempts** *(integer) --*

      The maximum number of attempts to be made. Default: 80
    """


_NodegroupDeletedWaitWaiterConfigTypeDef = TypedDict(
    "_NodegroupDeletedWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class NodegroupDeletedWaitWaiterConfigTypeDef(_NodegroupDeletedWaitWaiterConfigTypeDef):
    """
    Type definition for `NodegroupDeletedWait` `WaiterConfig`

    A dictionary that provides parameters to control waiting behavior.

    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 30

    - **MaxAttempts** *(integer) --*

      The maximum number of attempts to be made. Default: 40
    """
