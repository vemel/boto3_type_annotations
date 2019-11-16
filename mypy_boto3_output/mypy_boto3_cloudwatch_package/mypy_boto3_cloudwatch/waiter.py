"Main interface for cloudwatch Waiters"
from __future__ import annotations

from typing import List
from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_cloudwatch.type_defs import AlarmExistsWaitWaiterConfigTypeDef


__all__ = ("AlarmExistsWaiter",)


class AlarmExistsWaiter(Boto3Waiter):
    """
    Waiter for `alarm_exists` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        AlarmNames: List[str] = None,
        AlarmNamePrefix: str = None,
        StateValue: str = None,
        ActionPrefix: str = None,
        MaxRecords: int = None,
        NextToken: str = None,
        WaiterConfig: AlarmExistsWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        Polls :py:meth:`CloudWatch.Client.describe_alarms` every 5 seconds until a successful state is
        reached. An error is returned after 40 failed checks.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/DescribeAlarms>`_

        **Request Syntax**
        ::

          waiter.wait(
              AlarmNames=[
                  'string',
              ],
              AlarmNamePrefix='string',
              StateValue='OK'|'ALARM'|'INSUFFICIENT_DATA',
              ActionPrefix='string',
              MaxRecords=123,
              NextToken='string',
              WaiterConfig={
                  'Delay': 123,
                  'MaxAttempts': 123
              }
          )
        :type AlarmNames: list
        :param AlarmNames:

          The names of the alarms.

          - *(string) --*

        :type AlarmNamePrefix: string
        :param AlarmNamePrefix:

          The alarm name prefix. If this parameter is specified, you cannot specify ``AlarmNames`` .

        :type StateValue: string
        :param StateValue:

          The state value to be used in matching alarms.

        :type ActionPrefix: string
        :param ActionPrefix:

          The action name prefix.

        :type MaxRecords: integer
        :param MaxRecords:

          The maximum number of alarm descriptions to retrieve.

        :type NextToken: string
        :param NextToken:

          The token returned by a previous call to indicate that there is more data available.

        :type WaiterConfig: dict
        :param WaiterConfig:

          A dictionary that provides parameters to control waiting behavior.

          - **Delay** *(integer) --*

            The amount of time in seconds to wait between attempts. Default: 5

          - **MaxAttempts** *(integer) --*

            The maximum number of attempts to be made. Default: 40

        :returns: None
        """
