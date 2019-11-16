"Main interface for acm Waiters"
from __future__ import annotations

from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_acm.type_defs import CertificateValidatedWaitWaiterConfigTypeDef


__all__ = ("CertificateValidatedWaiter",)


class CertificateValidatedWaiter(Boto3Waiter):
    """
    Waiter for `certificate_validated` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        CertificateArn: str,
        WaiterConfig: CertificateValidatedWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        Polls :py:meth:`ACM.Client.describe_certificate` every 60 seconds until a successful state is
        reached. An error is returned after 40 failed checks.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/acm-2015-12-08/DescribeCertificate>`_

        **Request Syntax**
        ::

          waiter.wait(
              CertificateArn='string',
              WaiterConfig={
                  'Delay': 123,
                  'MaxAttempts': 123
              }
          )
        :type CertificateArn: string
        :param CertificateArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the ACM certificate. The ARN must have the following form:

           ``arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012``

          For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS Service Namespaces
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

        :type WaiterConfig: dict
        :param WaiterConfig:

          A dictionary that provides parameters to control waiting behavior.

          - **Delay** *(integer) --*

            The amount of time in seconds to wait between attempts. Default: 60

          - **MaxAttempts** *(integer) --*

            The maximum number of attempts to be made. Default: 40

        :returns: None
        """
