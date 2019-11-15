"Main interface for medialive Waiters"
from __future__ import annotations

from typing import Dict
from botocore.waiter import Waiter as Boto3Waiter


class ChannelCreated(Boto3Waiter):
    # pylint: disable=arguments-differ
    def wait(self, ChannelId: str, WaiterConfig: Dict = None) -> None:
        """
        Polls :py:meth:`MediaLive.Client.describe_channel` every 3 seconds until a successful state is
        reached. An error is returned after 5 failed checks.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/medialive-2017-10-14/DescribeChannel>`_

        **Request Syntax**
        ::

          waiter.wait(
              ChannelId='string',
              WaiterConfig={
                  'Delay': 123,
                  'MaxAttempts': 123
              }
          )
        :type ChannelId: string
        :param ChannelId: **[REQUIRED]** channel ID

        :type WaiterConfig: dict
        :param WaiterConfig:

          A dictionary that provides parameters to control waiting behavior.

          - **Delay** *(integer) --*

            The amount of time in seconds to wait between attempts. Default: 3

          - **MaxAttempts** *(integer) --*

            The maximum number of attempts to be made. Default: 5

        :returns: None
        """


class ChannelDeleted(Boto3Waiter):
    # pylint: disable=arguments-differ
    def wait(self, ChannelId: str, WaiterConfig: Dict = None) -> None:
        """
        Polls :py:meth:`MediaLive.Client.describe_channel` every 5 seconds until a successful state is
        reached. An error is returned after 20 failed checks.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/medialive-2017-10-14/DescribeChannel>`_

        **Request Syntax**
        ::

          waiter.wait(
              ChannelId='string',
              WaiterConfig={
                  'Delay': 123,
                  'MaxAttempts': 123
              }
          )
        :type ChannelId: string
        :param ChannelId: **[REQUIRED]** channel ID

        :type WaiterConfig: dict
        :param WaiterConfig:

          A dictionary that provides parameters to control waiting behavior.

          - **Delay** *(integer) --*

            The amount of time in seconds to wait between attempts. Default: 5

          - **MaxAttempts** *(integer) --*

            The maximum number of attempts to be made. Default: 20

        :returns: None
        """


class ChannelRunning(Boto3Waiter):
    # pylint: disable=arguments-differ
    def wait(self, ChannelId: str, WaiterConfig: Dict = None) -> None:
        """
        Polls :py:meth:`MediaLive.Client.describe_channel` every 5 seconds until a successful state is
        reached. An error is returned after 120 failed checks.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/medialive-2017-10-14/DescribeChannel>`_

        **Request Syntax**
        ::

          waiter.wait(
              ChannelId='string',
              WaiterConfig={
                  'Delay': 123,
                  'MaxAttempts': 123
              }
          )
        :type ChannelId: string
        :param ChannelId: **[REQUIRED]** channel ID

        :type WaiterConfig: dict
        :param WaiterConfig:

          A dictionary that provides parameters to control waiting behavior.

          - **Delay** *(integer) --*

            The amount of time in seconds to wait between attempts. Default: 5

          - **MaxAttempts** *(integer) --*

            The maximum number of attempts to be made. Default: 120

        :returns: None
        """


class ChannelStopped(Boto3Waiter):
    # pylint: disable=arguments-differ
    def wait(self, ChannelId: str, WaiterConfig: Dict = None) -> None:
        """
        Polls :py:meth:`MediaLive.Client.describe_channel` every 5 seconds until a successful state is
        reached. An error is returned after 28 failed checks.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/medialive-2017-10-14/DescribeChannel>`_

        **Request Syntax**
        ::

          waiter.wait(
              ChannelId='string',
              WaiterConfig={
                  'Delay': 123,
                  'MaxAttempts': 123
              }
          )
        :type ChannelId: string
        :param ChannelId: **[REQUIRED]** channel ID

        :type WaiterConfig: dict
        :param WaiterConfig:

          A dictionary that provides parameters to control waiting behavior.

          - **Delay** *(integer) --*

            The amount of time in seconds to wait between attempts. Default: 5

          - **MaxAttempts** *(integer) --*

            The maximum number of attempts to be made. Default: 28

        :returns: None
        """
