"Main interface for cloudfront Waiters"
from __future__ import annotations

from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_cloudfront.type_defs import (
    DistributionDeployedWaitWaiterConfigTypeDef,
    InvalidationCompletedWaitWaiterConfigTypeDef,
    StreamingDistributionDeployedWaitWaiterConfigTypeDef,
)


__all__ = (
    "DistributionDeployedWaiter",
    "InvalidationCompletedWaiter",
    "StreamingDistributionDeployedWaiter",
)


class DistributionDeployedWaiter(Boto3Waiter):
    """
    Waiter for `distribution_deployed` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self, Id: str, WaiterConfig: DistributionDeployedWaitWaiterConfigTypeDef = None
    ) -> None:
        """
        Polls :py:meth:`CloudFront.Client.get_distribution` every 60 seconds until a successful state is
        reached. An error is returned after 35 failed checks.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/cloudfront-2019-03-26/GetDistribution>`_

        **Request Syntax**
        ::

          waiter.wait(
              Id='string',
              WaiterConfig={
                  'Delay': 123,
                  'MaxAttempts': 123
              }
          )
        :type Id: string
        :param Id: **[REQUIRED]**

          The distribution's ID. If the ID is empty, an empty distribution configuration is returned.

        :type WaiterConfig: dict
        :param WaiterConfig:

          A dictionary that provides parameters to control waiting behavior.

          - **Delay** *(integer) --*

            The amount of time in seconds to wait between attempts. Default: 60

          - **MaxAttempts** *(integer) --*

            The maximum number of attempts to be made. Default: 35

        :returns: None
        """


class InvalidationCompletedWaiter(Boto3Waiter):
    """
    Waiter for `invalidation_completed` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        DistributionId: str,
        Id: str,
        WaiterConfig: InvalidationCompletedWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        Polls :py:meth:`CloudFront.Client.get_invalidation` every 20 seconds until a successful state is
        reached. An error is returned after 30 failed checks.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/cloudfront-2019-03-26/GetInvalidation>`_

        **Request Syntax**
        ::

          waiter.wait(
              DistributionId='string',
              Id='string',
              WaiterConfig={
                  'Delay': 123,
                  'MaxAttempts': 123
              }
          )
        :type DistributionId: string
        :param DistributionId: **[REQUIRED]**

          The distribution's ID.

        :type Id: string
        :param Id: **[REQUIRED]**

          The identifier for the invalidation request, for example, ``IDFDVBD632BHDS5`` .

        :type WaiterConfig: dict
        :param WaiterConfig:

          A dictionary that provides parameters to control waiting behavior.

          - **Delay** *(integer) --*

            The amount of time in seconds to wait between attempts. Default: 20

          - **MaxAttempts** *(integer) --*

            The maximum number of attempts to be made. Default: 30

        :returns: None
        """


class StreamingDistributionDeployedWaiter(Boto3Waiter):
    """
    Waiter for `streaming_distribution_deployed` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        Id: str,
        WaiterConfig: StreamingDistributionDeployedWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        Polls :py:meth:`CloudFront.Client.get_streaming_distribution` every 60 seconds until a successful
        state is reached. An error is returned after 25 failed checks.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/cloudfront-2019-03-26/GetStreamingDistribution>`_

        **Request Syntax**
        ::

          waiter.wait(
              Id='string',
              WaiterConfig={
                  'Delay': 123,
                  'MaxAttempts': 123
              }
          )
        :type Id: string
        :param Id: **[REQUIRED]**

          The streaming distribution's ID.

        :type WaiterConfig: dict
        :param WaiterConfig:

          A dictionary that provides parameters to control waiting behavior.

          - **Delay** *(integer) --*

            The amount of time in seconds to wait between attempts. Default: 60

          - **MaxAttempts** *(integer) --*

            The maximum number of attempts to be made. Default: 25

        :returns: None
        """
