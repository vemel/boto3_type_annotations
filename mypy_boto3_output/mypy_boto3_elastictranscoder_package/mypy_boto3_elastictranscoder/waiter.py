"Main interface for elastictranscoder Waiters"
from __future__ import annotations

from typing import Dict
from botocore.waiter import Waiter as Boto3Waiter


class JobComplete(Boto3Waiter):
    # pylint: disable=arguments-differ
    def wait(self, Id: str, WaiterConfig: Dict = None) -> None:
        """
        Polls :py:meth:`ElasticTranscoder.Client.read_job` every 30 seconds until a successful state is
        reached. An error is returned after 120 failed checks.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elastictranscoder-2012-09-25/ReadJob>`_

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

          The identifier of the job for which you want to get detailed information.

        :type WaiterConfig: dict
        :param WaiterConfig:

          A dictionary that provides parameters to control waiting behavior.

          - **Delay** *(integer) --*

            The amount of time in seconds to wait between attempts. Default: 30

          - **MaxAttempts** *(integer) --*

            The maximum number of attempts to be made. Default: 120

        :returns: None
        """
