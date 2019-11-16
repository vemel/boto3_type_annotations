"Main interface for signer Waiters"
from __future__ import annotations

from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_signer.type_defs import SuccessfulSigningJobWaitWaiterConfigTypeDef


__all__ = ("SuccessfulSigningJobWaiter",)


class SuccessfulSigningJobWaiter(Boto3Waiter):
    """
    Waiter for `successful_signing_job` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        jobId: str,
        WaiterConfig: SuccessfulSigningJobWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        Polls :py:meth:`signer.Client.describe_signing_job` every 20 seconds until a successful state is
        reached. An error is returned after 25 failed checks.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/signer-2017-08-25/DescribeSigningJob>`_

        **Request Syntax**
        ::

          waiter.wait(
              jobId='string',
              WaiterConfig={
                  'Delay': 123,
                  'MaxAttempts': 123
              }
          )
        :type jobId: string
        :param jobId: **[REQUIRED]**

          The ID of the signing job on input.

        :type WaiterConfig: dict
        :param WaiterConfig:

          A dictionary that provides parameters to control waiting behavior.

          - **Delay** *(integer) --*

            The amount of time in seconds to wait between attempts. Default: 20

          - **MaxAttempts** *(integer) --*

            The maximum number of attempts to be made. Default: 25

        :returns: None
        """
