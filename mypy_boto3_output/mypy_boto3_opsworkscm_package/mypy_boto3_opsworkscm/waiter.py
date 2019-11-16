"Main interface for opsworkscm Waiters"
from __future__ import annotations

from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_opsworkscm.type_defs import NodeAssociatedWaitWaiterConfigTypeDef


__all__ = ("NodeAssociatedWaiter",)


class NodeAssociatedWaiter(Boto3Waiter):
    """
    Waiter for `node_associated` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        NodeAssociationStatusToken: str,
        ServerName: str,
        WaiterConfig: NodeAssociatedWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        Polls :py:meth:`OpsWorksCM.Client.describe_node_association_status` every 15 seconds until a
        successful state is reached. An error is returned after 15 failed checks.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/opsworkscm-2016-11-01/DescribeNodeAssociationStatus>`_

        **Request Syntax**
        ::

          waiter.wait(
              NodeAssociationStatusToken='string',
              ServerName='string',
              WaiterConfig={
                  'Delay': 123,
                  'MaxAttempts': 123
              }
          )
        :type NodeAssociationStatusToken: string
        :param NodeAssociationStatusToken: **[REQUIRED]**

          The token returned in either the AssociateNodeResponse or the DisassociateNodeResponse.

        :type ServerName: string
        :param ServerName: **[REQUIRED]**

          The name of the server from which to disassociate the node.

        :type WaiterConfig: dict
        :param WaiterConfig:

          A dictionary that provides parameters to control waiting behavior.

          - **Delay** *(integer) --*

            The amount of time in seconds to wait between attempts. Default: 15

          - **MaxAttempts** *(integer) --*

            The maximum number of attempts to be made. Default: 15

        :returns: None
        """
