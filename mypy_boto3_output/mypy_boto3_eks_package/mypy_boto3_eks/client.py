"Main interface for eks Client"
from __future__ import annotations

from typing import Any, Dict, List
from typing_extensions import Literal, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator
from botocore.waiter import Waiter as Boto3Waiter

# pylint: disable=import-self
import mypy_boto3_eks.client as client_scope

# pylint: disable=import-self
import mypy_boto3_eks.paginator as paginator_scope
from mypy_boto3_eks.type_defs import (
    ClientCreateClusterResponseTypeDef,
    ClientCreateClusterloggingTypeDef,
    ClientCreateClusterresourcesVpcConfigTypeDef,
    ClientCreateNodegroupResponseTypeDef,
    ClientCreateNodegroupremoteAccessTypeDef,
    ClientCreateNodegroupscalingConfigTypeDef,
    ClientDeleteClusterResponseTypeDef,
    ClientDeleteNodegroupResponseTypeDef,
    ClientDescribeClusterResponseTypeDef,
    ClientDescribeNodegroupResponseTypeDef,
    ClientDescribeUpdateResponseTypeDef,
    ClientListClustersResponseTypeDef,
    ClientListNodegroupsResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientListUpdatesResponseTypeDef,
    ClientUpdateClusterConfigResponseTypeDef,
    ClientUpdateClusterConfigloggingTypeDef,
    ClientUpdateClusterConfigresourcesVpcConfigTypeDef,
    ClientUpdateClusterVersionResponseTypeDef,
    ClientUpdateNodegroupConfigResponseTypeDef,
    ClientUpdateNodegroupConfiglabelsTypeDef,
    ClientUpdateNodegroupConfigscalingConfigTypeDef,
    ClientUpdateNodegroupVersionResponseTypeDef,
)

# pylint: disable=import-self
import mypy_boto3_eks.waiter as waiter_scope


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
        name: str,
        roleArn: str,
        resourcesVpcConfig: ClientCreateClusterresourcesVpcConfigTypeDef,
        version: str = None,
        logging: ClientCreateClusterloggingTypeDef = None,
        clientRequestToken: str = None,
        tags: Dict[str, str] = None,
    ) -> ClientCreateClusterResponseTypeDef:
        """
        Creates an Amazon EKS control plane.

        The Amazon EKS control plane consists of control plane instances that run the Kubernetes software,
        such as ``etcd`` and the API server. The control plane runs in an account managed by AWS, and the
        Kubernetes API is exposed via the Amazon EKS API server endpoint. Each Amazon EKS cluster control
        plane is single-tenant and unique and runs on its own set of Amazon EC2 instances.

        The cluster control plane is provisioned across multiple Availability Zones and fronted by an
        Elastic Load Balancing Network Load Balancer. Amazon EKS also provisions elastic network interfaces
        in your VPC subnets to provide connectivity from the control plane instances to the worker nodes
        (for example, to support ``kubectl exec`` , ``logs`` , and ``proxy`` data flows).

        Amazon EKS worker nodes run in your AWS account and connect to your cluster's control plane via the
        Kubernetes API server endpoint and a certificate file that is created for your cluster.

        You can use the ``endpointPublicAccess`` and ``endpointPrivateAccess`` parameters to enable or
        disable public and private access to your cluster's Kubernetes API server endpoint. By default,
        public access is enabled, and private access is disabled. For more information, see `Amazon EKS
        Cluster Endpoint Access Control
        <https://docs.aws.amazon.com/eks/latest/userguide/cluster-endpoint.html>`__ in the * *Amazon EKS
        User Guide* * .

        You can use the ``logging`` parameter to enable or disable exporting the Kubernetes control plane
        logs for your cluster to CloudWatch Logs. By default, cluster control plane logs aren't exported to
        CloudWatch Logs. For more information, see `Amazon EKS Cluster Control Plane Logs
        <https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html>`__ in the * *Amazon EKS
        User Guide* * .

        .. note::

          CloudWatch Logs ingestion, archive storage, and data scanning rates apply to exported control
          plane logs. For more information, see `Amazon CloudWatch Pricing
          <http://aws.amazon.com/cloudwatch/pricing/>`__ .

        Cluster creation typically takes between 10 and 15 minutes. After you create an Amazon EKS cluster,
        you must configure your Kubernetes tooling to communicate with the API server and launch worker
        nodes into your cluster. For more information, see `Managing Cluster Authentication
        <https://docs.aws.amazon.com/eks/latest/userguide/managing-auth.html>`__ and `Launching Amazon EKS
        Worker Nodes <https://docs.aws.amazon.com/eks/latest/userguide/launch-workers.html>`__ in the
        *Amazon EKS User Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/eks-2017-11-01/CreateCluster>`_

        **Request Syntax**
        ::

          response = client.create_cluster(
              name='string',
              version='string',
              roleArn='string',
              resourcesVpcConfig={
                  'subnetIds': [
                      'string',
                  ],
                  'securityGroupIds': [
                      'string',
                  ],
                  'endpointPublicAccess': True|False,
                  'endpointPrivateAccess': True|False
              },
              logging={
                  'clusterLogging': [
                      {
                          'types': [
                              'api'|'audit'|'authenticator'|'controllerManager'|'scheduler',
                          ],
                          'enabled': True|False
                      },
                  ]
              },
              clientRequestToken='string',
              tags={
                  'string': 'string'
              }
          )
        :type name: string
        :param name: **[REQUIRED]**

          The unique name to give to your cluster.

        :type version: string
        :param version:

          The desired Kubernetes version for your cluster. If you don't specify a value here, the latest
          version available in Amazon EKS is used.

        :type roleArn: string
        :param roleArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the IAM role that provides permissions for Amazon EKS to make
          calls to other AWS API operations on your behalf. For more information, see `Amazon EKS Service
          IAM Role <https://docs.aws.amazon.com/eks/latest/userguide/service_IAM_role.html>`__ in the *
          *Amazon EKS User Guide* * .

        :type resourcesVpcConfig: dict
        :param resourcesVpcConfig: **[REQUIRED]**

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

        :type logging: dict
        :param logging:

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

        :type clientRequestToken: string
        :param clientRequestToken:

          Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

          This field is autopopulated if not provided.

        :type tags: dict
        :param tags:

          The metadata to apply to the cluster to assist with categorization and organization. Each tag
          consists of a key and an optional value, both of which you define.

          - *(string) --*

            - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'cluster': {
                    'name': 'string',
                    'arn': 'string',
                    'createdAt': datetime(2015, 1, 1),
                    'version': 'string',
                    'endpoint': 'string',
                    'roleArn': 'string',
                    'resourcesVpcConfig': {
                        'subnetIds': [
                            'string',
                        ],
                        'securityGroupIds': [
                            'string',
                        ],
                        'clusterSecurityGroupId': 'string',
                        'vpcId': 'string',
                        'endpointPublicAccess': True|False,
                        'endpointPrivateAccess': True|False
                    },
                    'logging': {
                        'clusterLogging': [
                            {
                                'types': [
                                    'api'|'audit'|'authenticator'|'controllerManager'|'scheduler',
                                ],
                                'enabled': True|False
                            },
                        ]
                    },
                    'identity': {
                        'oidc': {
                            'issuer': 'string'
                        }
                    },
                    'status': 'CREATING'|'ACTIVE'|'DELETING'|'FAILED'|'UPDATING',
                    'certificateAuthority': {
                        'data': 'string'
                    },
                    'clientRequestToken': 'string',
                    'platformVersion': 'string',
                    'tags': {
                        'string': 'string'
                    }
                }
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_nodegroup(
        self,
        clusterName: str,
        nodegroupName: str,
        subnets: List[str],
        nodeRole: str,
        scalingConfig: ClientCreateNodegroupscalingConfigTypeDef = None,
        diskSize: int = None,
        instanceTypes: List[str] = None,
        amiType: str = None,
        remoteAccess: ClientCreateNodegroupremoteAccessTypeDef = None,
        labels: Dict[str, str] = None,
        tags: Dict[str, str] = None,
        clientRequestToken: str = None,
        version: str = None,
        releaseVersion: str = None,
    ) -> ClientCreateNodegroupResponseTypeDef:
        """
        Creates a managed worker node group for an Amazon EKS cluster. You can only create a node group for
        your cluster that is equal to the current Kubernetes version for the cluster. All node groups are
        created with the latest AMI release version for the respective minor Kubernetes version of the
        cluster.

        An Amazon EKS managed node group is an Amazon EC2 Auto Scaling group and associated Amazon EC2
        instances that are managed by AWS for an Amazon EKS cluster. Each node group uses a version of the
        Amazon EKS-optimized Amazon Linux 2 AMI. For more information, see `Managed Node Groups
        <https://docs.aws.amazon.com/eks/latest/userguide/managed-node-groups.html>`__ in the *Amazon EKS
        User Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/eks-2017-11-01/CreateNodegroup>`_

        **Request Syntax**
        ::

          response = client.create_nodegroup(
              clusterName='string',
              nodegroupName='string',
              scalingConfig={
                  'minSize': 123,
                  'maxSize': 123,
                  'desiredSize': 123
              },
              diskSize=123,
              subnets=[
                  'string',
              ],
              instanceTypes=[
                  'string',
              ],
              amiType='AL2_x86_64'|'AL2_x86_64_GPU',
              remoteAccess={
                  'ec2SshKey': 'string',
                  'sourceSecurityGroups': [
                      'string',
                  ]
              },
              nodeRole='string',
              labels={
                  'string': 'string'
              },
              tags={
                  'string': 'string'
              },
              clientRequestToken='string',
              version='string',
              releaseVersion='string'
          )
        :type clusterName: string
        :param clusterName: **[REQUIRED]**

          The name of the cluster to create the node group in.

        :type nodegroupName: string
        :param nodegroupName: **[REQUIRED]**

          The unique name to give your node group.

        :type scalingConfig: dict
        :param scalingConfig:

          The scaling configuration details for the AutoScaling group that is created for your node group.

          - **minSize** *(integer) --*

            The minimum number of worker nodes that the managed node group can scale in to. This number
            must be greater than zero.

          - **maxSize** *(integer) --*

            The maximum number of worker nodes that the managed node group can scale out to. Managed node
            groups can support up to 100 nodes by default.

          - **desiredSize** *(integer) --*

            The current number of worker nodes that the managed node group should maintain.

        :type diskSize: integer
        :param diskSize:

          The root device disk size (in GiB) for your node group instances. The default disk size is 20 GiB.

        :type subnets: list
        :param subnets: **[REQUIRED]**

          The subnets to use for the AutoScaling group that is created for your node group. These subnets
          must have the tag key ``kubernetes.io/cluster/CLUSTER_NAME`` with a value of ``shared`` , where
          ``CLUSTER_NAME`` is replaced with the name of your cluster.

          - *(string) --*

        :type instanceTypes: list
        :param instanceTypes:

          The instance type to use for your node group. Currently, you can specify a single instance type
          for a node group. The default value for this parameter is ``t3.medium`` . If you choose a GPU
          instance type, be sure to specify the ``AL2_x86_64_GPU`` with the ``amiType`` parameter.

          - *(string) --*

        :type amiType: string
        :param amiType:

          The AMI type for your node group. GPU instance types should use the ``AL2_x86_64_GPU`` AMI type,
          which uses the Amazon EKS-optimized Linux AMI with GPU support; non-GPU instances should use the
          ``AL2_x86_64`` AMI type, which uses the Amazon EKS-optimized Linux AMI.

        :type remoteAccess: dict
        :param remoteAccess:

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

        :type nodeRole: string
        :param nodeRole: **[REQUIRED]**

          The IAM role associated with your node group. The Amazon EKS worker node ``kubelet`` daemon makes
          calls to AWS APIs on your behalf. Worker nodes receive permissions for these API calls through an
          IAM instance profile and associated policies. Before you can launch worker nodes and register
          them into a cluster, you must create an IAM role for those worker nodes to use when they are
          launched. For more information, see `Amazon EKS Worker Node IAM Role
          <https://docs.aws.amazon.com/eks/latest/userguide/worker_node_IAM_role.html>`__ in the * *Amazon
          EKS User Guide* * .

        :type labels: dict
        :param labels:

          The Kubernetes labels to be applied to the nodes in the node group when they are created.

          - *(string) --*

            - *(string) --*

        :type tags: dict
        :param tags:

          The metadata to apply to the node group to assist with categorization and organization. Each tag
          consists of a key and an optional value, both of which you define. Node group tags do not
          propagate to any other resources associated with the node group, such as the Amazon EC2 instances
          or subnets.

          - *(string) --*

            - *(string) --*

        :type clientRequestToken: string
        :param clientRequestToken:

          Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

          This field is autopopulated if not provided.

        :type version: string
        :param version:

          The Kubernetes version to use for your managed nodes. By default, the Kubernetes version of the
          cluster is used, and this is the only accepted specified value.

        :type releaseVersion: string
        :param releaseVersion:

          The AMI version of the Amazon EKS-optimized AMI to use with your node group. By default, the
          latest available AMI version for the node group's current Kubernetes version is used. For more
          information, see `Amazon EKS-Optimized Linux AMI Versions
          <https://docs.aws.amazon.com/eks/latest/userguide/eks-linux-ami-versions.html>`__ in the *Amazon
          EKS User Guide* .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'nodegroup': {
                    'nodegroupName': 'string',
                    'nodegroupArn': 'string',
                    'clusterName': 'string',
                    'version': 'string',
                    'releaseVersion': 'string',
                    'createdAt': datetime(2015, 1, 1),
                    'modifiedAt': datetime(2015, 1, 1),
                    'status':
                    'CREATING'|'ACTIVE'|'UPDATING'|'DELETING'|'CREATE_FAILED'|'DELETE_FAILED'|'DEGRADED',
                    'scalingConfig': {
                        'minSize': 123,
                        'maxSize': 123,
                        'desiredSize': 123
                    },
                    'instanceTypes': [
                        'string',
                    ],
                    'subnets': [
                        'string',
                    ],
                    'remoteAccess': {
                        'ec2SshKey': 'string',
                        'sourceSecurityGroups': [
                            'string',
                        ]
                    },
                    'amiType': 'AL2_x86_64'|'AL2_x86_64_GPU',
                    'nodeRole': 'string',
                    'labels': {
                        'string': 'string'
                    },
                    'resources': {
                        'autoScalingGroups': [
                            {
                                'name': 'string'
                            },
                        ],
                        'remoteAccessSecurityGroup': 'string'
                    },
                    'diskSize': 123,
                    'health': {
                        'issues': [
                            {
                                'code':
                                'AutoScalingGroupNotFound'|'Ec2SecurityGroupNotFound'
                                |'Ec2SecurityGroupDeletionFailure'|'Ec2LaunchTemplateNotFound'
                                |'Ec2LaunchTemplateVersionMismatch'|'IamInstanceProfileNotFound'
                                |'IamNodeRoleNotFound'|'AsgInstanceLaunchFailures'|'InstanceLimitExceeded'
                                |'InsufficientFreeAddresses'|'AccessDenied'|'InternalFailure',
                                'message': 'string',
                                'resourceIds': [
                                    'string',
                                ]
                            },
                        ]
                    },
                    'tags': {
                        'string': 'string'
                    }
                }
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_cluster(self, name: str) -> ClientDeleteClusterResponseTypeDef:
        """
        Deletes the Amazon EKS cluster control plane.

        If you have active services in your cluster that are associated with a load balancer, you must
        delete those services before deleting the cluster so that the load balancers are deleted properly.
        Otherwise, you can have orphaned resources in your VPC that prevent you from being able to delete
        the VPC. For more information, see `Deleting a Cluster
        <https://docs.aws.amazon.com/eks/latest/userguide/delete-cluster.html>`__ in the *Amazon EKS User
        Guide* .

        If you have managed node groups attached to the cluster, you must delete them first. For more
        information, see  DeleteNodegroup .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/eks-2017-11-01/DeleteCluster>`_

        **Request Syntax**
        ::

          response = client.delete_cluster(
              name='string'
          )
        :type name: string
        :param name: **[REQUIRED]**

          The name of the cluster to delete.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'cluster': {
                    'name': 'string',
                    'arn': 'string',
                    'createdAt': datetime(2015, 1, 1),
                    'version': 'string',
                    'endpoint': 'string',
                    'roleArn': 'string',
                    'resourcesVpcConfig': {
                        'subnetIds': [
                            'string',
                        ],
                        'securityGroupIds': [
                            'string',
                        ],
                        'clusterSecurityGroupId': 'string',
                        'vpcId': 'string',
                        'endpointPublicAccess': True|False,
                        'endpointPrivateAccess': True|False
                    },
                    'logging': {
                        'clusterLogging': [
                            {
                                'types': [
                                    'api'|'audit'|'authenticator'|'controllerManager'|'scheduler',
                                ],
                                'enabled': True|False
                            },
                        ]
                    },
                    'identity': {
                        'oidc': {
                            'issuer': 'string'
                        }
                    },
                    'status': 'CREATING'|'ACTIVE'|'DELETING'|'FAILED'|'UPDATING',
                    'certificateAuthority': {
                        'data': 'string'
                    },
                    'clientRequestToken': 'string',
                    'platformVersion': 'string',
                    'tags': {
                        'string': 'string'
                    }
                }
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_nodegroup(
        self, clusterName: str, nodegroupName: str
    ) -> ClientDeleteNodegroupResponseTypeDef:
        """
        Deletes an Amazon EKS node group for a cluster.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/eks-2017-11-01/DeleteNodegroup>`_

        **Request Syntax**
        ::

          response = client.delete_nodegroup(
              clusterName='string',
              nodegroupName='string'
          )
        :type clusterName: string
        :param clusterName: **[REQUIRED]**

          The name of the Amazon EKS cluster that is associated with your node group.

        :type nodegroupName: string
        :param nodegroupName: **[REQUIRED]**

          The name of the node group to delete.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'nodegroup': {
                    'nodegroupName': 'string',
                    'nodegroupArn': 'string',
                    'clusterName': 'string',
                    'version': 'string',
                    'releaseVersion': 'string',
                    'createdAt': datetime(2015, 1, 1),
                    'modifiedAt': datetime(2015, 1, 1),
                    'status':
                    'CREATING'|'ACTIVE'|'UPDATING'|'DELETING'|'CREATE_FAILED'|'DELETE_FAILED'|'DEGRADED',
                    'scalingConfig': {
                        'minSize': 123,
                        'maxSize': 123,
                        'desiredSize': 123
                    },
                    'instanceTypes': [
                        'string',
                    ],
                    'subnets': [
                        'string',
                    ],
                    'remoteAccess': {
                        'ec2SshKey': 'string',
                        'sourceSecurityGroups': [
                            'string',
                        ]
                    },
                    'amiType': 'AL2_x86_64'|'AL2_x86_64_GPU',
                    'nodeRole': 'string',
                    'labels': {
                        'string': 'string'
                    },
                    'resources': {
                        'autoScalingGroups': [
                            {
                                'name': 'string'
                            },
                        ],
                        'remoteAccessSecurityGroup': 'string'
                    },
                    'diskSize': 123,
                    'health': {
                        'issues': [
                            {
                                'code':
                                'AutoScalingGroupNotFound'|'Ec2SecurityGroupNotFound'
                                |'Ec2SecurityGroupDeletionFailure'|'Ec2LaunchTemplateNotFound'
                                |'Ec2LaunchTemplateVersionMismatch'|'IamInstanceProfileNotFound'
                                |'IamNodeRoleNotFound'|'AsgInstanceLaunchFailures'|'InstanceLimitExceeded'
                                |'InsufficientFreeAddresses'|'AccessDenied'|'InternalFailure',
                                'message': 'string',
                                'resourceIds': [
                                    'string',
                                ]
                            },
                        ]
                    },
                    'tags': {
                        'string': 'string'
                    }
                }
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_cluster(self, name: str) -> ClientDescribeClusterResponseTypeDef:
        """
        Returns descriptive information about an Amazon EKS cluster.

        The API server endpoint and certificate authority data returned by this operation are required for
        ``kubelet`` and ``kubectl`` to communicate with your Kubernetes API server. For more information,
        see `Create a kubeconfig for Amazon EKS
        <https://docs.aws.amazon.com/eks/latest/userguide/create-kubeconfig.html>`__ .

        .. note::

          The API server endpoint and certificate authority data aren't available until the cluster reaches
          the ``ACTIVE`` state.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/eks-2017-11-01/DescribeCluster>`_

        **Request Syntax**
        ::

          response = client.describe_cluster(
              name='string'
          )
        :type name: string
        :param name: **[REQUIRED]**

          The name of the cluster to describe.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'cluster': {
                    'name': 'string',
                    'arn': 'string',
                    'createdAt': datetime(2015, 1, 1),
                    'version': 'string',
                    'endpoint': 'string',
                    'roleArn': 'string',
                    'resourcesVpcConfig': {
                        'subnetIds': [
                            'string',
                        ],
                        'securityGroupIds': [
                            'string',
                        ],
                        'clusterSecurityGroupId': 'string',
                        'vpcId': 'string',
                        'endpointPublicAccess': True|False,
                        'endpointPrivateAccess': True|False
                    },
                    'logging': {
                        'clusterLogging': [
                            {
                                'types': [
                                    'api'|'audit'|'authenticator'|'controllerManager'|'scheduler',
                                ],
                                'enabled': True|False
                            },
                        ]
                    },
                    'identity': {
                        'oidc': {
                            'issuer': 'string'
                        }
                    },
                    'status': 'CREATING'|'ACTIVE'|'DELETING'|'FAILED'|'UPDATING',
                    'certificateAuthority': {
                        'data': 'string'
                    },
                    'clientRequestToken': 'string',
                    'platformVersion': 'string',
                    'tags': {
                        'string': 'string'
                    }
                }
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_nodegroup(
        self, clusterName: str, nodegroupName: str
    ) -> ClientDescribeNodegroupResponseTypeDef:
        """
        Returns descriptive information about an Amazon EKS node group.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/eks-2017-11-01/DescribeNodegroup>`_

        **Request Syntax**
        ::

          response = client.describe_nodegroup(
              clusterName='string',
              nodegroupName='string'
          )
        :type clusterName: string
        :param clusterName: **[REQUIRED]**

          The name of the Amazon EKS cluster associated with the node group.

        :type nodegroupName: string
        :param nodegroupName: **[REQUIRED]**

          The name of the node group to describe.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'nodegroup': {
                    'nodegroupName': 'string',
                    'nodegroupArn': 'string',
                    'clusterName': 'string',
                    'version': 'string',
                    'releaseVersion': 'string',
                    'createdAt': datetime(2015, 1, 1),
                    'modifiedAt': datetime(2015, 1, 1),
                    'status':
                    'CREATING'|'ACTIVE'|'UPDATING'|'DELETING'|'CREATE_FAILED'|'DELETE_FAILED'|'DEGRADED',
                    'scalingConfig': {
                        'minSize': 123,
                        'maxSize': 123,
                        'desiredSize': 123
                    },
                    'instanceTypes': [
                        'string',
                    ],
                    'subnets': [
                        'string',
                    ],
                    'remoteAccess': {
                        'ec2SshKey': 'string',
                        'sourceSecurityGroups': [
                            'string',
                        ]
                    },
                    'amiType': 'AL2_x86_64'|'AL2_x86_64_GPU',
                    'nodeRole': 'string',
                    'labels': {
                        'string': 'string'
                    },
                    'resources': {
                        'autoScalingGroups': [
                            {
                                'name': 'string'
                            },
                        ],
                        'remoteAccessSecurityGroup': 'string'
                    },
                    'diskSize': 123,
                    'health': {
                        'issues': [
                            {
                                'code':
                                'AutoScalingGroupNotFound'|'Ec2SecurityGroupNotFound'
                                |'Ec2SecurityGroupDeletionFailure'|'Ec2LaunchTemplateNotFound'
                                |'Ec2LaunchTemplateVersionMismatch'|'IamInstanceProfileNotFound'
                                |'IamNodeRoleNotFound'|'AsgInstanceLaunchFailures'|'InstanceLimitExceeded'
                                |'InsufficientFreeAddresses'|'AccessDenied'|'InternalFailure',
                                'message': 'string',
                                'resourceIds': [
                                    'string',
                                ]
                            },
                        ]
                    },
                    'tags': {
                        'string': 'string'
                    }
                }
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_update(
        self, name: str, updateId: str, nodegroupName: str = None
    ) -> ClientDescribeUpdateResponseTypeDef:
        """
        Returns descriptive information about an update against your Amazon EKS cluster or associated
        managed node group.

        When the status of the update is ``Succeeded`` , the update is complete. If an update fails, the
        status is ``Failed`` , and an error detail explains the reason for the failure.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/eks-2017-11-01/DescribeUpdate>`_

        **Request Syntax**
        ::

          response = client.describe_update(
              name='string',
              updateId='string',
              nodegroupName='string'
          )
        :type name: string
        :param name: **[REQUIRED]**

          The name of the Amazon EKS cluster associated with the update.

        :type updateId: string
        :param updateId: **[REQUIRED]**

          The ID of the update to describe.

        :type nodegroupName: string
        :param nodegroupName:

          The name of the Amazon EKS node group associated with the update.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'update': {
                    'id': 'string',
                    'status': 'InProgress'|'Failed'|'Cancelled'|'Successful',
                    'type': 'VersionUpdate'|'EndpointAccessUpdate'|'LoggingUpdate'|'ConfigUpdate',
                    'params': [
                        {
                            'type':
                            'Version'|'PlatformVersion'|'EndpointPrivateAccess'|'EndpointPublicAccess'
                            |'ClusterLogging'|'DesiredSize'|'LabelsToAdd'|'LabelsToRemove'|'MaxSize'
                            |'MinSize'|'ReleaseVersion',
                            'value': 'string'
                        },
                    ],
                    'createdAt': datetime(2015, 1, 1),
                    'errors': [
                        {
                            'errorCode':
                            'SubnetNotFound'|'SecurityGroupNotFound'|'EniLimitReached'|'IpNotAvailable'
                            |'AccessDenied'|'OperationNotPermitted'|'VpcIdNotFound'|'Unknown'
                            |'NodeCreationFailure'|'PodEvictionFailure'|'InsufficientFreeAddresses',
                            'errorMessage': 'string',
                            'resourceIds': [
                                'string',
                            ]
                        },
                    ]
                }
            }
          **Response Structure**

          - *(dict) --*

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
    def list_clusters(
        self, maxResults: int = None, nextToken: str = None
    ) -> ClientListClustersResponseTypeDef:
        """
        Lists the Amazon EKS clusters in your AWS account in the specified Region.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/eks-2017-11-01/ListClusters>`_

        **Request Syntax**
        ::

          response = client.list_clusters(
              maxResults=123,
              nextToken='string'
          )
        :type maxResults: integer
        :param maxResults:

          The maximum number of cluster results returned by ``ListClusters`` in paginated output. When you
          use this parameter, ``ListClusters`` returns only ``maxResults`` results in a single page along
          with a ``nextToken`` response element. You can see the remaining results of the initial request
          by sending another ``ListClusters`` request with the returned ``nextToken`` value. This value can
          be between 1 and 100. If you don't use this parameter, ``ListClusters`` returns up to 100 results
          and a ``nextToken`` value if applicable.

        :type nextToken: string
        :param nextToken:

          The ``nextToken`` value returned from a previous paginated ``ListClusters`` request where
          ``maxResults`` was used and the results exceeded the value of that parameter. Pagination
          continues from the end of the previous results that returned the ``nextToken`` value.

          .. note::

            This token should be treated as an opaque identifier that is used only to retrieve the next
            items in a list and not for other programmatic purposes.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'clusters': [
                    'string',
                ],
                'nextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **clusters** *(list) --*

              A list of all of the clusters for your account in the specified Region.

              - *(string) --*

            - **nextToken** *(string) --*

              The ``nextToken`` value to include in a future ``ListClusters`` request. When the results of
              a ``ListClusters`` request exceed ``maxResults`` , you can use this value to retrieve the
              next page of results. This value is ``null`` when there are no more results to return.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_nodegroups(
        self, clusterName: str, maxResults: int = None, nextToken: str = None
    ) -> ClientListNodegroupsResponseTypeDef:
        """
        Lists the Amazon EKS node groups associated with the specified cluster in your AWS account in the
        specified Region.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/eks-2017-11-01/ListNodegroups>`_

        **Request Syntax**
        ::

          response = client.list_nodegroups(
              clusterName='string',
              maxResults=123,
              nextToken='string'
          )
        :type clusterName: string
        :param clusterName: **[REQUIRED]**

          The name of the Amazon EKS cluster that you would like to list node groups in.

        :type maxResults: integer
        :param maxResults:

          The maximum number of node group results returned by ``ListNodegroups`` in paginated output. When
          you use this parameter, ``ListNodegroups`` returns only ``maxResults`` results in a single page
          along with a ``nextToken`` response element. You can see the remaining results of the initial
          request by sending another ``ListNodegroups`` request with the returned ``nextToken`` value. This
          value can be between 1 and 100. If you don't use this parameter, ``ListNodegroups`` returns up to
          100 results and a ``nextToken`` value if applicable.

        :type nextToken: string
        :param nextToken:

          The ``nextToken`` value returned from a previous paginated ``ListNodegroups`` request where
          ``maxResults`` was used and the results exceeded the value of that parameter. Pagination
          continues from the end of the previous results that returned the ``nextToken`` value.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'nodegroups': [
                    'string',
                ],
                'nextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **nodegroups** *(list) --*

              A list of all of the node groups associated with the specified cluster.

              - *(string) --*

            - **nextToken** *(string) --*

              The ``nextToken`` value to include in a future ``ListNodegroups`` request. When the results
              of a ``ListNodegroups`` request exceed ``maxResults`` , you can use this value to retrieve
              the next page of results. This value is ``null`` when there are no more results to return.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(
        self, resourceArn: str
    ) -> ClientListTagsForResourceResponseTypeDef:
        """
        List the tags for an Amazon EKS resource.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/eks-2017-11-01/ListTagsForResource>`_

        **Request Syntax**
        ::

          response = client.list_tags_for_resource(
              resourceArn='string'
          )
        :type resourceArn: string
        :param resourceArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) that identifies the resource for which to list the tags.
          Currently, the supported resources are Amazon EKS clusters and managed node groups.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'tags': {
                    'string': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **tags** *(dict) --*

              The tags for the resource.

              - *(string) --*

                - *(string) --*

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_updates(
        self,
        name: str,
        nodegroupName: str = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ClientListUpdatesResponseTypeDef:
        """
        Lists the updates associated with an Amazon EKS cluster or managed node group in your AWS account,
        in the specified Region.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/eks-2017-11-01/ListUpdates>`_

        **Request Syntax**
        ::

          response = client.list_updates(
              name='string',
              nodegroupName='string',
              nextToken='string',
              maxResults=123
          )
        :type name: string
        :param name: **[REQUIRED]**

          The name of the Amazon EKS cluster to list updates for.

        :type nodegroupName: string
        :param nodegroupName:

          The name of the Amazon EKS managed node group to list updates for.

        :type nextToken: string
        :param nextToken:

          The ``nextToken`` value returned from a previous paginated ``ListUpdates`` request where
          ``maxResults`` was used and the results exceeded the value of that parameter. Pagination
          continues from the end of the previous results that returned the ``nextToken`` value.

        :type maxResults: integer
        :param maxResults:

          The maximum number of update results returned by ``ListUpdates`` in paginated output. When you
          use this parameter, ``ListUpdates`` returns only ``maxResults`` results in a single page along
          with a ``nextToken`` response element. You can see the remaining results of the initial request
          by sending another ``ListUpdates`` request with the returned ``nextToken`` value. This value can
          be between 1 and 100. If you don't use this parameter, ``ListUpdates`` returns up to 100 results
          and a ``nextToken`` value if applicable.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'updateIds': [
                    'string',
                ],
                'nextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **updateIds** *(list) --*

              A list of all the updates for the specified cluster and Region.

              - *(string) --*

            - **nextToken** *(string) --*

              The ``nextToken`` value to include in a future ``ListUpdates`` request. When the results of a
              ``ListUpdates`` request exceed ``maxResults`` , you can use this value to retrieve the next
              page of results. This value is ``null`` when there are no more results to return.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(self, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Associates the specified tags to a resource with the specified ``resourceArn`` . If existing tags
        on a resource are not specified in the request parameters, they are not changed. When a resource is
        deleted, the tags associated with that resource are deleted as well. Tags that you create for
        Amazon EKS resources do not propagate to any other resources associated with the cluster. For
        example, if you tag a cluster with this operation, that tag does not automatically propagate to the
        subnets and worker nodes associated with the cluster.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/eks-2017-11-01/TagResource>`_

        **Request Syntax**
        ::

          response = client.tag_resource(
              resourceArn='string',
              tags={
                  'string': 'string'
              }
          )
        :type resourceArn: string
        :param resourceArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the resource to which to add tags. Currently, the supported
          resources are Amazon EKS clusters and managed node groups.

        :type tags: dict
        :param tags: **[REQUIRED]**

          The tags to add to the resource. A tag is an array of key-value pairs.

          - *(string) --*

            - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Deletes specified tags from a resource.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/eks-2017-11-01/UntagResource>`_

        **Request Syntax**
        ::

          response = client.untag_resource(
              resourceArn='string',
              tagKeys=[
                  'string',
              ]
          )
        :type resourceArn: string
        :param resourceArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the resource from which to delete tags. Currently, the
          supported resources are Amazon EKS clusters and managed node groups.

        :type tagKeys: list
        :param tagKeys: **[REQUIRED]**

          The keys of the tags to be removed.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_cluster_config(
        self,
        name: str,
        resourcesVpcConfig: ClientUpdateClusterConfigresourcesVpcConfigTypeDef = None,
        logging: ClientUpdateClusterConfigloggingTypeDef = None,
        clientRequestToken: str = None,
    ) -> ClientUpdateClusterConfigResponseTypeDef:
        """
        Updates an Amazon EKS cluster configuration. Your cluster continues to function during the update.
        The response output includes an update ID that you can use to track the status of your cluster
        update with the  DescribeUpdate API operation.

        You can use this API operation to enable or disable exporting the Kubernetes control plane logs for
        your cluster to CloudWatch Logs. By default, cluster control plane logs aren't exported to
        CloudWatch Logs. For more information, see `Amazon EKS Cluster Control Plane Logs
        <https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html>`__ in the * *Amazon EKS
        User Guide* * .

        .. note::

          CloudWatch Logs ingestion, archive storage, and data scanning rates apply to exported control
          plane logs. For more information, see `Amazon CloudWatch Pricing
          <http://aws.amazon.com/cloudwatch/pricing/>`__ .

        You can also use this API operation to enable or disable public and private access to your
        cluster's Kubernetes API server endpoint. By default, public access is enabled, and private access
        is disabled. For more information, see `Amazon EKS Cluster Endpoint Access Control
        <https://docs.aws.amazon.com/eks/latest/userguide/cluster-endpoint.html>`__ in the * *Amazon EKS
        User Guide* * .

        .. warning::

          At this time, you can not update the subnets or security group IDs for an existing cluster.

        Cluster updates are asynchronous, and they should finish within a few minutes. During an update,
        the cluster status moves to ``UPDATING`` (this status transition is eventually consistent). When
        the update is complete (either ``Failed`` or ``Successful`` ), the cluster status moves to
        ``Active`` .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/eks-2017-11-01/UpdateClusterConfig>`_

        **Request Syntax**
        ::

          response = client.update_cluster_config(
              name='string',
              resourcesVpcConfig={
                  'subnetIds': [
                      'string',
                  ],
                  'securityGroupIds': [
                      'string',
                  ],
                  'endpointPublicAccess': True|False,
                  'endpointPrivateAccess': True|False
              },
              logging={
                  'clusterLogging': [
                      {
                          'types': [
                              'api'|'audit'|'authenticator'|'controllerManager'|'scheduler',
                          ],
                          'enabled': True|False
                      },
                  ]
              },
              clientRequestToken='string'
          )
        :type name: string
        :param name: **[REQUIRED]**

          The name of the Amazon EKS cluster to update.

        :type resourcesVpcConfig: dict
        :param resourcesVpcConfig:

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

        :type logging: dict
        :param logging:

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

        :type clientRequestToken: string
        :param clientRequestToken:

          Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

          This field is autopopulated if not provided.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'update': {
                    'id': 'string',
                    'status': 'InProgress'|'Failed'|'Cancelled'|'Successful',
                    'type': 'VersionUpdate'|'EndpointAccessUpdate'|'LoggingUpdate'|'ConfigUpdate',
                    'params': [
                        {
                            'type':
                            'Version'|'PlatformVersion'|'EndpointPrivateAccess'|'EndpointPublicAccess'
                            |'ClusterLogging'|'DesiredSize'|'LabelsToAdd'|'LabelsToRemove'|'MaxSize'
                            |'MinSize'|'ReleaseVersion',
                            'value': 'string'
                        },
                    ],
                    'createdAt': datetime(2015, 1, 1),
                    'errors': [
                        {
                            'errorCode':
                            'SubnetNotFound'|'SecurityGroupNotFound'|'EniLimitReached'|'IpNotAvailable'
                            |'AccessDenied'|'OperationNotPermitted'|'VpcIdNotFound'|'Unknown'
                            |'NodeCreationFailure'|'PodEvictionFailure'|'InsufficientFreeAddresses',
                            'errorMessage': 'string',
                            'resourceIds': [
                                'string',
                            ]
                        },
                    ]
                }
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_cluster_version(
        self, name: str, version: str, clientRequestToken: str = None
    ) -> ClientUpdateClusterVersionResponseTypeDef:
        """
        Updates an Amazon EKS cluster to the specified Kubernetes version. Your cluster continues to
        function during the update. The response output includes an update ID that you can use to track the
        status of your cluster update with the  DescribeUpdate API operation.

        Cluster updates are asynchronous, and they should finish within a few minutes. During an update,
        the cluster status moves to ``UPDATING`` (this status transition is eventually consistent). When
        the update is complete (either ``Failed`` or ``Successful`` ), the cluster status moves to
        ``Active`` .

        If your cluster has managed node groups attached to it, all of your node groups’ Kubernetes
        versions must match the cluster’s Kubernetes version in order to update the cluster to a new
        Kubernetes version.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/eks-2017-11-01/UpdateClusterVersion>`_

        **Request Syntax**
        ::

          response = client.update_cluster_version(
              name='string',
              version='string',
              clientRequestToken='string'
          )
        :type name: string
        :param name: **[REQUIRED]**

          The name of the Amazon EKS cluster to update.

        :type version: string
        :param version: **[REQUIRED]**

          The desired Kubernetes version following a successful update.

        :type clientRequestToken: string
        :param clientRequestToken:

          Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

          This field is autopopulated if not provided.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'update': {
                    'id': 'string',
                    'status': 'InProgress'|'Failed'|'Cancelled'|'Successful',
                    'type': 'VersionUpdate'|'EndpointAccessUpdate'|'LoggingUpdate'|'ConfigUpdate',
                    'params': [
                        {
                            'type':
                            'Version'|'PlatformVersion'|'EndpointPrivateAccess'|'EndpointPublicAccess'
                            |'ClusterLogging'|'DesiredSize'|'LabelsToAdd'|'LabelsToRemove'|'MaxSize'
                            |'MinSize'|'ReleaseVersion',
                            'value': 'string'
                        },
                    ],
                    'createdAt': datetime(2015, 1, 1),
                    'errors': [
                        {
                            'errorCode':
                            'SubnetNotFound'|'SecurityGroupNotFound'|'EniLimitReached'|'IpNotAvailable'
                            |'AccessDenied'|'OperationNotPermitted'|'VpcIdNotFound'|'Unknown'
                            |'NodeCreationFailure'|'PodEvictionFailure'|'InsufficientFreeAddresses',
                            'errorMessage': 'string',
                            'resourceIds': [
                                'string',
                            ]
                        },
                    ]
                }
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_nodegroup_config(
        self,
        clusterName: str,
        nodegroupName: str,
        labels: ClientUpdateNodegroupConfiglabelsTypeDef = None,
        scalingConfig: ClientUpdateNodegroupConfigscalingConfigTypeDef = None,
        clientRequestToken: str = None,
    ) -> ClientUpdateNodegroupConfigResponseTypeDef:
        """
        Updates an Amazon EKS managed node group configuration. Your node group continues to function
        during the update. The response output includes an update ID that you can use to track the status
        of your node group update with the  DescribeUpdate API operation. Currently you can update the
        Kubernetes labels for a node group or the scaling configuration.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/eks-2017-11-01/UpdateNodegroupConfig>`_

        **Request Syntax**
        ::

          response = client.update_nodegroup_config(
              clusterName='string',
              nodegroupName='string',
              labels={
                  'addOrUpdateLabels': {
                      'string': 'string'
                  },
                  'removeLabels': [
                      'string',
                  ]
              },
              scalingConfig={
                  'minSize': 123,
                  'maxSize': 123,
                  'desiredSize': 123
              },
              clientRequestToken='string'
          )
        :type clusterName: string
        :param clusterName: **[REQUIRED]**

          The name of the Amazon EKS cluster that the managed node group resides in.

        :type nodegroupName: string
        :param nodegroupName: **[REQUIRED]**

          The name of the managed node group to update.

        :type labels: dict
        :param labels:

          The Kubernetes labels to be applied to the nodes in the node group after the update.

          - **addOrUpdateLabels** *(dict) --*

            Kubernetes labels to be added or updated.

            - *(string) --*

              - *(string) --*

          - **removeLabels** *(list) --*

            Kubernetes labels to be removed.

            - *(string) --*

        :type scalingConfig: dict
        :param scalingConfig:

          The scaling configuration details for the AutoScaling group after the update.

          - **minSize** *(integer) --*

            The minimum number of worker nodes that the managed node group can scale in to. This number
            must be greater than zero.

          - **maxSize** *(integer) --*

            The maximum number of worker nodes that the managed node group can scale out to. Managed node
            groups can support up to 100 nodes by default.

          - **desiredSize** *(integer) --*

            The current number of worker nodes that the managed node group should maintain.

        :type clientRequestToken: string
        :param clientRequestToken:

          Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

          This field is autopopulated if not provided.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'update': {
                    'id': 'string',
                    'status': 'InProgress'|'Failed'|'Cancelled'|'Successful',
                    'type': 'VersionUpdate'|'EndpointAccessUpdate'|'LoggingUpdate'|'ConfigUpdate',
                    'params': [
                        {
                            'type':
                            'Version'|'PlatformVersion'|'EndpointPrivateAccess'|'EndpointPublicAccess'
                            |'ClusterLogging'|'DesiredSize'|'LabelsToAdd'|'LabelsToRemove'|'MaxSize'
                            |'MinSize'|'ReleaseVersion',
                            'value': 'string'
                        },
                    ],
                    'createdAt': datetime(2015, 1, 1),
                    'errors': [
                        {
                            'errorCode':
                            'SubnetNotFound'|'SecurityGroupNotFound'|'EniLimitReached'|'IpNotAvailable'
                            |'AccessDenied'|'OperationNotPermitted'|'VpcIdNotFound'|'Unknown'
                            |'NodeCreationFailure'|'PodEvictionFailure'|'InsufficientFreeAddresses',
                            'errorMessage': 'string',
                            'resourceIds': [
                                'string',
                            ]
                        },
                    ]
                }
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_nodegroup_version(
        self,
        clusterName: str,
        nodegroupName: str,
        version: str = None,
        releaseVersion: str = None,
        force: bool = None,
        clientRequestToken: str = None,
    ) -> ClientUpdateNodegroupVersionResponseTypeDef:
        """
        Updates the Kubernetes version or AMI version of an Amazon EKS managed node group.

        You can update to the latest available AMI version of a node group's current Kubernetes version by
        not specifying a Kubernetes version in the request. You can update to the latest AMI version of
        your cluster's current Kubernetes version by specifying your cluster's Kubernetes version in the
        request. For more information, see `Amazon EKS-Optimized Linux AMI Versions
        <https://docs.aws.amazon.com/eks/latest/userguide/eks-linux-ami-versions.html>`__ in the *Amazon
        EKS User Guide* .

        You cannot roll back a node group to an earlier Kubernetes version or AMI version.

        When a node in a managed node group is terminated due to a scaling action or update, the pods in
        that node are drained first. Amazon EKS attempts to drain the nodes gracefully and will fail if it
        is unable to do so. You can ``force`` the update if Amazon EKS is unable to drain the nodes as a
        result of a pod disruption budget issue.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/eks-2017-11-01/UpdateNodegroupVersion>`_

        **Request Syntax**
        ::

          response = client.update_nodegroup_version(
              clusterName='string',
              nodegroupName='string',
              version='string',
              releaseVersion='string',
              force=True|False,
              clientRequestToken='string'
          )
        :type clusterName: string
        :param clusterName: **[REQUIRED]**

          The name of the Amazon EKS cluster that is associated with the managed node group to update.

        :type nodegroupName: string
        :param nodegroupName: **[REQUIRED]**

          The name of the managed node group to update.

        :type version: string
        :param version:

          The Kubernetes version to update to. If no version is specified, then the Kubernetes version of
          the node group does not change. You can specify the Kubernetes version of the cluster to update
          the node group to the latest AMI version of the cluster's Kubernetes version.

        :type releaseVersion: string
        :param releaseVersion:

          The AMI version of the Amazon EKS-optimized AMI to use for the update. By default, the latest
          available AMI version for the node group's Kubernetes version is used. For more information, see
          `Amazon EKS-Optimized Linux AMI Versions
          <https://docs.aws.amazon.com/eks/latest/userguide/eks-linux-ami-versions.html>`__ in the *Amazon
          EKS User Guide* .

        :type force: boolean
        :param force:

          Force the update if the existing node group's pods are unable to be drained due to a pod
          disruption budget issue. If a previous update fails because pods could not be drained, you can
          force the update after it fails to terminate the old node regardless of whether or not any pods
          are running on the node.

        :type clientRequestToken: string
        :param clientRequestToken:

          Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

          This field is autopopulated if not provided.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'update': {
                    'id': 'string',
                    'status': 'InProgress'|'Failed'|'Cancelled'|'Successful',
                    'type': 'VersionUpdate'|'EndpointAccessUpdate'|'LoggingUpdate'|'ConfigUpdate',
                    'params': [
                        {
                            'type':
                            'Version'|'PlatformVersion'|'EndpointPrivateAccess'|'EndpointPublicAccess'
                            |'ClusterLogging'|'DesiredSize'|'LabelsToAdd'|'LabelsToRemove'|'MaxSize'
                            |'MinSize'|'ReleaseVersion',
                            'value': 'string'
                        },
                    ],
                    'createdAt': datetime(2015, 1, 1),
                    'errors': [
                        {
                            'errorCode':
                            'SubnetNotFound'|'SecurityGroupNotFound'|'EniLimitReached'|'IpNotAvailable'
                            |'AccessDenied'|'OperationNotPermitted'|'VpcIdNotFound'|'Unknown'
                            |'NodeCreationFailure'|'PodEvictionFailure'|'InsufficientFreeAddresses',
                            'errorMessage': 'string',
                            'resourceIds': [
                                'string',
                            ]
                        },
                    ]
                }
            }
          **Response Structure**

          - *(dict) --*

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
        self, operation_name: Literal["list_nodegroups"]
    ) -> paginator_scope.ListNodegroupsPaginator:
        """
        Get Paginator for `list_nodegroups` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_updates"]
    ) -> paginator_scope.ListUpdatesPaginator:
        """
        Get Paginator for `list_updates` operation.
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
        self, waiter_name: Literal["cluster_active"]
    ) -> waiter_scope.ClusterActiveWaiter:
        """
        Get Waiter `cluster_active`.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["cluster_deleted"]
    ) -> waiter_scope.ClusterDeletedWaiter:
        """
        Get Waiter `cluster_deleted`.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["nodegroup_active"]
    ) -> waiter_scope.NodegroupActiveWaiter:
        """
        Get Waiter `nodegroup_active`.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["nodegroup_deleted"]
    ) -> waiter_scope.NodegroupDeletedWaiter:
        """
        Get Waiter `nodegroup_deleted`.
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
    BadRequestException: Boto3ClientError
    ClientError: Boto3ClientError
    ClientException: Boto3ClientError
    InvalidParameterException: Boto3ClientError
    InvalidRequestException: Boto3ClientError
    NotFoundException: Boto3ClientError
    ResourceInUseException: Boto3ClientError
    ResourceLimitExceededException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ServerException: Boto3ClientError
    ServiceUnavailableException: Boto3ClientError
    UnsupportedAvailabilityZoneException: Boto3ClientError
