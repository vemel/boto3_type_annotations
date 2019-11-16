"Main interface for codedeploy Waiters"
from __future__ import annotations

from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_codedeploy.type_defs import DeploymentSuccessfulWaitWaiterConfigTypeDef


__all__ = ("DeploymentSuccessfulWaiter",)


class DeploymentSuccessfulWaiter(Boto3Waiter):
    """
    Waiter for `deployment_successful` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        deploymentId: str,
        WaiterConfig: DeploymentSuccessfulWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        Polls :py:meth:`CodeDeploy.Client.get_deployment` every 15 seconds until a successful state is
        reached. An error is returned after 120 failed checks.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/GetDeployment>`_

        **Request Syntax**
        ::

          waiter.wait(
              deploymentId='string',
              WaiterConfig={
                  'Delay': 123,
                  'MaxAttempts': 123
              }
          )
        :type deploymentId: string
        :param deploymentId: **[REQUIRED]**

          The unique ID of a deployment associated with the IAM user or AWS account.

        :type WaiterConfig: dict
        :param WaiterConfig:

          A dictionary that provides parameters to control waiting behavior.

          - **Delay** *(integer) --*

            The amount of time in seconds to wait between attempts. Default: 15

          - **MaxAttempts** *(integer) --*

            The maximum number of attempts to be made. Default: 120

        :returns: None
        """
