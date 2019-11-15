"Main interface for glacier Waiters"
from __future__ import annotations

from typing import Dict
from botocore.waiter import Waiter as Boto3Waiter


class VaultExists(Boto3Waiter):
    # pylint: disable=arguments-differ
    def wait(
        self, vaultName: str, accountId: str = None, WaiterConfig: Dict = None
    ) -> None:
        """
        Polls :py:meth:`Glacier.Client.describe_vault` every 3 seconds until a successful state is reached.
        An error is returned after 15 failed checks.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/DescribeVault>`_

        **Request Syntax**
        ::

          waiter.wait(
              vaultName='string',
              WaiterConfig={
                  'Delay': 123,
                  'MaxAttempts': 123
              }
          )
        :type accountId: string
        :param accountId:

          The ``AccountId`` value is the AWS account ID of the account that owns the vault. You can either
          specify an AWS account ID or optionally a single '``-`` ' (hyphen), in which case Amazon S3
          Glacier uses the AWS account ID associated with the credentials used to sign the request. If you
          use an account ID, do not include any hyphens ('-') in the ID.

            Note: this parameter is set to "-" bydefault if no value is not specified.

        :type vaultName: string
        :param vaultName: **[REQUIRED]**

          The name of the vault.

        :type WaiterConfig: dict
        :param WaiterConfig:

          A dictionary that provides parameters to control waiting behavior.

          - **Delay** *(integer) --*

            The amount of time in seconds to wait between attempts. Default: 3

          - **MaxAttempts** *(integer) --*

            The maximum number of attempts to be made. Default: 15

        :returns: None
        """


class VaultNotExists(Boto3Waiter):
    # pylint: disable=arguments-differ
    def wait(
        self, vaultName: str, accountId: str = None, WaiterConfig: Dict = None
    ) -> None:
        """
        Polls :py:meth:`Glacier.Client.describe_vault` every 3 seconds until a successful state is reached.
        An error is returned after 15 failed checks.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/DescribeVault>`_

        **Request Syntax**
        ::

          waiter.wait(
              vaultName='string',
              WaiterConfig={
                  'Delay': 123,
                  'MaxAttempts': 123
              }
          )
        :type accountId: string
        :param accountId:

          The ``AccountId`` value is the AWS account ID of the account that owns the vault. You can either
          specify an AWS account ID or optionally a single '``-`` ' (hyphen), in which case Amazon S3
          Glacier uses the AWS account ID associated with the credentials used to sign the request. If you
          use an account ID, do not include any hyphens ('-') in the ID.

            Note: this parameter is set to "-" bydefault if no value is not specified.

        :type vaultName: string
        :param vaultName: **[REQUIRED]**

          The name of the vault.

        :type WaiterConfig: dict
        :param WaiterConfig:

          A dictionary that provides parameters to control waiting behavior.

          - **Delay** *(integer) --*

            The amount of time in seconds to wait between attempts. Default: 3

          - **MaxAttempts** *(integer) --*

            The maximum number of attempts to be made. Default: 15

        :returns: None
        """
