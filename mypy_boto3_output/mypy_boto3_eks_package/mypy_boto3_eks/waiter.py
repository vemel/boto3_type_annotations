"Main interface for eks Waiters"
from __future__ import annotations

from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_eks.type_defs import (
    ClusterActiveWaitWaiterConfigTypeDef,
    ClusterDeletedWaitWaiterConfigTypeDef,
    NodegroupActiveWaitWaiterConfigTypeDef,
    NodegroupDeletedWaitWaiterConfigTypeDef,
)


__all__ = (
    "ClusterActiveWaiter",
    "ClusterDeletedWaiter",
    "NodegroupActiveWaiter",
    "NodegroupDeletedWaiter",
)


class ClusterActiveWaiter(Boto3Waiter):
    """
    Waiter for `cluster_active` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self, name: str, WaiterConfig: ClusterActiveWaitWaiterConfigTypeDef = None
    ) -> None:
        """
        Polls :py:meth:`EKS.Client.describe_cluster` every 30 seconds until a successful state is reached.
        An error is returned after 40 failed checks.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/eks-2017-11-01/DescribeCluster>`_

        **Request Syntax**
        ::

          waiter.wait(
              name='string',
              WaiterConfig={
                  'Delay': 123,
                  'MaxAttempts': 123
              }
          )
        :type name: string
        :param name: **[REQUIRED]**

          The name of the cluster to describe.

        :type WaiterConfig: dict
        :param WaiterConfig:

          A dictionary that provides parameters to control waiting behavior.

          - **Delay** *(integer) --*

            The amount of time in seconds to wait between attempts. Default: 30

          - **MaxAttempts** *(integer) --*

            The maximum number of attempts to be made. Default: 40

        :returns: None
        """


class ClusterDeletedWaiter(Boto3Waiter):
    """
    Waiter for `cluster_deleted` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self, name: str, WaiterConfig: ClusterDeletedWaitWaiterConfigTypeDef = None
    ) -> None:
        """
        Polls :py:meth:`EKS.Client.describe_cluster` every 30 seconds until a successful state is reached.
        An error is returned after 40 failed checks.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/eks-2017-11-01/DescribeCluster>`_

        **Request Syntax**
        ::

          waiter.wait(
              name='string',
              WaiterConfig={
                  'Delay': 123,
                  'MaxAttempts': 123
              }
          )
        :type name: string
        :param name: **[REQUIRED]**

          The name of the cluster to describe.

        :type WaiterConfig: dict
        :param WaiterConfig:

          A dictionary that provides parameters to control waiting behavior.

          - **Delay** *(integer) --*

            The amount of time in seconds to wait between attempts. Default: 30

          - **MaxAttempts** *(integer) --*

            The maximum number of attempts to be made. Default: 40

        :returns: None
        """


class NodegroupActiveWaiter(Boto3Waiter):
    """
    Waiter for `nodegroup_active` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        clusterName: str,
        nodegroupName: str,
        WaiterConfig: NodegroupActiveWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        Polls :py:meth:`EKS.Client.describe_nodegroup` every 30 seconds until a successful state is
        reached. An error is returned after 80 failed checks.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/eks-2017-11-01/DescribeNodegroup>`_

        **Request Syntax**
        ::

          waiter.wait(
              clusterName='string',
              nodegroupName='string',
              WaiterConfig={
                  'Delay': 123,
                  'MaxAttempts': 123
              }
          )
        :type clusterName: string
        :param clusterName: **[REQUIRED]**

          The name of the Amazon EKS cluster associated with the node group.

        :type nodegroupName: string
        :param nodegroupName: **[REQUIRED]**

          The name of the node group to describe.

        :type WaiterConfig: dict
        :param WaiterConfig:

          A dictionary that provides parameters to control waiting behavior.

          - **Delay** *(integer) --*

            The amount of time in seconds to wait between attempts. Default: 30

          - **MaxAttempts** *(integer) --*

            The maximum number of attempts to be made. Default: 80

        :returns: None
        """


class NodegroupDeletedWaiter(Boto3Waiter):
    """
    Waiter for `nodegroup_deleted` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        clusterName: str,
        nodegroupName: str,
        WaiterConfig: NodegroupDeletedWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        Polls :py:meth:`EKS.Client.describe_nodegroup` every 30 seconds until a successful state is
        reached. An error is returned after 40 failed checks.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/eks-2017-11-01/DescribeNodegroup>`_

        **Request Syntax**
        ::

          waiter.wait(
              clusterName='string',
              nodegroupName='string',
              WaiterConfig={
                  'Delay': 123,
                  'MaxAttempts': 123
              }
          )
        :type clusterName: string
        :param clusterName: **[REQUIRED]**

          The name of the Amazon EKS cluster associated with the node group.

        :type nodegroupName: string
        :param nodegroupName: **[REQUIRED]**

          The name of the node group to describe.

        :type WaiterConfig: dict
        :param WaiterConfig:

          A dictionary that provides parameters to control waiting behavior.

          - **Delay** *(integer) --*

            The amount of time in seconds to wait between attempts. Default: 30

          - **MaxAttempts** *(integer) --*

            The maximum number of attempts to be made. Default: 40

        :returns: None
        """
