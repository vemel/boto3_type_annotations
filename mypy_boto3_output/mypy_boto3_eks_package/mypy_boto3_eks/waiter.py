"Main interface for eks Waiters"
from __future__ import annotations

from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_eks.type_defs import (
    ClusterActiveWaitWaiterConfigTypeDef,
    ClusterDeletedWaitWaiterConfigTypeDef,
)


class ClusterActive(Boto3Waiter):
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


class ClusterDeleted(Boto3Waiter):
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
