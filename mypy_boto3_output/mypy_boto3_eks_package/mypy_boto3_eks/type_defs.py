"Main interface for eks type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from typing_extensions import TypedDict


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
      Each tag consists of a key and an optional value, both of which you define.

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
        Each tag consists of a key and an optional value, both of which you define.

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
      Each tag consists of a key and an optional value, both of which you define.

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
        Each tag consists of a key and an optional value, both of which you define.

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
      Each tag consists of a key and an optional value, both of which you define.

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
        Each tag consists of a key and an optional value, both of which you define.

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
