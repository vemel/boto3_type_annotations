"Main interface for cloudformation Waiters"
from __future__ import annotations

from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_cloudformation.type_defs import (
    ChangeSetCreateCompleteWaitWaiterConfigTypeDef,
    StackCreateCompleteWaitWaiterConfigTypeDef,
    StackDeleteCompleteWaitWaiterConfigTypeDef,
    StackExistsWaitWaiterConfigTypeDef,
    StackImportCompleteWaitWaiterConfigTypeDef,
    StackUpdateCompleteWaitWaiterConfigTypeDef,
    TypeRegistrationCompleteWaitWaiterConfigTypeDef,
)


__all__ = (
    "ChangeSetCreateCompleteWaiter",
    "StackCreateCompleteWaiter",
    "StackDeleteCompleteWaiter",
    "StackExistsWaiter",
    "StackImportCompleteWaiter",
    "StackUpdateCompleteWaiter",
    "TypeRegistrationCompleteWaiter",
)


class ChangeSetCreateCompleteWaiter(Boto3Waiter):
    """
    Waiter for `change_set_create_complete` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        ChangeSetName: str,
        StackName: str = None,
        NextToken: str = None,
        WaiterConfig: ChangeSetCreateCompleteWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        Polls :py:meth:`CloudFormation.Client.describe_change_set` every 30 seconds until a successful
        state is reached. An error is returned after 120 failed checks.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/DescribeChangeSet>`_

        **Request Syntax**
        ::

          waiter.wait(
              ChangeSetName='string',
              StackName='string',
              NextToken='string',
              WaiterConfig={
                  'Delay': 123,
                  'MaxAttempts': 123
              }
          )
        :type ChangeSetName: string
        :param ChangeSetName: **[REQUIRED]**

          The name or Amazon Resource Name (ARN) of the change set that you want to describe.

        :type StackName: string
        :param StackName:

          If you specified the name of a change set, specify the stack name or ID (ARN) of the change set
          you want to describe.

        :type NextToken: string
        :param NextToken:

          A string (provided by the  DescribeChangeSet response output) that identifies the next page of
          information that you want to retrieve.

        :type WaiterConfig: dict
        :param WaiterConfig:

          A dictionary that provides parameters to control waiting behavior.

          - **Delay** *(integer) --*

            The amount of time in seconds to wait between attempts. Default: 30

          - **MaxAttempts** *(integer) --*

            The maximum number of attempts to be made. Default: 120

        :returns: None
        """


class StackCreateCompleteWaiter(Boto3Waiter):
    """
    Waiter for `stack_create_complete` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        StackName: str = None,
        NextToken: str = None,
        WaiterConfig: StackCreateCompleteWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        Polls :py:meth:`CloudFormation.Client.describe_stacks` every 30 seconds until a successful state is
        reached. An error is returned after 120 failed checks.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/DescribeStacks>`_

        **Request Syntax**
        ::

          waiter.wait(
              StackName='string',
              NextToken='string',
              WaiterConfig={
                  'Delay': 123,
                  'MaxAttempts': 123
              }
          )
        :type StackName: string
        :param StackName:

          The name or the unique stack ID that is associated with the stack, which are not always
          interchangeable:

          * Running stacks: You can specify either the stack's name or its unique stack ID.

          * Deleted stacks: You must specify the unique stack ID.

          Default: There is no default value.

        :type NextToken: string
        :param NextToken:

          A string that identifies the next page of stacks that you want to retrieve.

        :type WaiterConfig: dict
        :param WaiterConfig:

          A dictionary that provides parameters to control waiting behavior.

          - **Delay** *(integer) --*

            The amount of time in seconds to wait between attempts. Default: 30

          - **MaxAttempts** *(integer) --*

            The maximum number of attempts to be made. Default: 120

        :returns: None
        """


class StackDeleteCompleteWaiter(Boto3Waiter):
    """
    Waiter for `stack_delete_complete` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        StackName: str = None,
        NextToken: str = None,
        WaiterConfig: StackDeleteCompleteWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        Polls :py:meth:`CloudFormation.Client.describe_stacks` every 30 seconds until a successful state is
        reached. An error is returned after 120 failed checks.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/DescribeStacks>`_

        **Request Syntax**
        ::

          waiter.wait(
              StackName='string',
              NextToken='string',
              WaiterConfig={
                  'Delay': 123,
                  'MaxAttempts': 123
              }
          )
        :type StackName: string
        :param StackName:

          The name or the unique stack ID that is associated with the stack, which are not always
          interchangeable:

          * Running stacks: You can specify either the stack's name or its unique stack ID.

          * Deleted stacks: You must specify the unique stack ID.

          Default: There is no default value.

        :type NextToken: string
        :param NextToken:

          A string that identifies the next page of stacks that you want to retrieve.

        :type WaiterConfig: dict
        :param WaiterConfig:

          A dictionary that provides parameters to control waiting behavior.

          - **Delay** *(integer) --*

            The amount of time in seconds to wait between attempts. Default: 30

          - **MaxAttempts** *(integer) --*

            The maximum number of attempts to be made. Default: 120

        :returns: None
        """


class StackExistsWaiter(Boto3Waiter):
    """
    Waiter for `stack_exists` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        StackName: str = None,
        NextToken: str = None,
        WaiterConfig: StackExistsWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        Polls :py:meth:`CloudFormation.Client.describe_stacks` every 5 seconds until a successful state is
        reached. An error is returned after 20 failed checks.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/DescribeStacks>`_

        **Request Syntax**
        ::

          waiter.wait(
              StackName='string',
              NextToken='string',
              WaiterConfig={
                  'Delay': 123,
                  'MaxAttempts': 123
              }
          )
        :type StackName: string
        :param StackName:

          The name or the unique stack ID that is associated with the stack, which are not always
          interchangeable:

          * Running stacks: You can specify either the stack's name or its unique stack ID.

          * Deleted stacks: You must specify the unique stack ID.

          Default: There is no default value.

        :type NextToken: string
        :param NextToken:

          A string that identifies the next page of stacks that you want to retrieve.

        :type WaiterConfig: dict
        :param WaiterConfig:

          A dictionary that provides parameters to control waiting behavior.

          - **Delay** *(integer) --*

            The amount of time in seconds to wait between attempts. Default: 5

          - **MaxAttempts** *(integer) --*

            The maximum number of attempts to be made. Default: 20

        :returns: None
        """


class StackImportCompleteWaiter(Boto3Waiter):
    """
    Waiter for `stack_import_complete` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        StackName: str = None,
        NextToken: str = None,
        WaiterConfig: StackImportCompleteWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        Polls :py:meth:`CloudFormation.Client.describe_stacks` every 30 seconds until a successful state is
        reached. An error is returned after 120 failed checks.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/DescribeStacks>`_

        **Request Syntax**
        ::

          waiter.wait(
              StackName='string',
              NextToken='string',
              WaiterConfig={
                  'Delay': 123,
                  'MaxAttempts': 123
              }
          )
        :type StackName: string
        :param StackName:

          The name or the unique stack ID that is associated with the stack, which are not always
          interchangeable:

          * Running stacks: You can specify either the stack's name or its unique stack ID.

          * Deleted stacks: You must specify the unique stack ID.

          Default: There is no default value.

        :type NextToken: string
        :param NextToken:

          A string that identifies the next page of stacks that you want to retrieve.

        :type WaiterConfig: dict
        :param WaiterConfig:

          A dictionary that provides parameters to control waiting behavior.

          - **Delay** *(integer) --*

            The amount of time in seconds to wait between attempts. Default: 30

          - **MaxAttempts** *(integer) --*

            The maximum number of attempts to be made. Default: 120

        :returns: None
        """


class StackUpdateCompleteWaiter(Boto3Waiter):
    """
    Waiter for `stack_update_complete` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        StackName: str = None,
        NextToken: str = None,
        WaiterConfig: StackUpdateCompleteWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        Polls :py:meth:`CloudFormation.Client.describe_stacks` every 30 seconds until a successful state is
        reached. An error is returned after 120 failed checks.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/DescribeStacks>`_

        **Request Syntax**
        ::

          waiter.wait(
              StackName='string',
              NextToken='string',
              WaiterConfig={
                  'Delay': 123,
                  'MaxAttempts': 123
              }
          )
        :type StackName: string
        :param StackName:

          The name or the unique stack ID that is associated with the stack, which are not always
          interchangeable:

          * Running stacks: You can specify either the stack's name or its unique stack ID.

          * Deleted stacks: You must specify the unique stack ID.

          Default: There is no default value.

        :type NextToken: string
        :param NextToken:

          A string that identifies the next page of stacks that you want to retrieve.

        :type WaiterConfig: dict
        :param WaiterConfig:

          A dictionary that provides parameters to control waiting behavior.

          - **Delay** *(integer) --*

            The amount of time in seconds to wait between attempts. Default: 30

          - **MaxAttempts** *(integer) --*

            The maximum number of attempts to be made. Default: 120

        :returns: None
        """


class TypeRegistrationCompleteWaiter(Boto3Waiter):
    """
    Waiter for `type_registration_complete` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        RegistrationToken: str,
        WaiterConfig: TypeRegistrationCompleteWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        Polls :py:meth:`CloudFormation.Client.describe_type_registration` every 30 seconds until a
        successful state is reached. An error is returned after 120 failed checks.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/DescribeTypeRegistration>`_

        **Request Syntax**
        ::

          waiter.wait(
              RegistrationToken='string',
              WaiterConfig={
                  'Delay': 123,
                  'MaxAttempts': 123
              }
          )
        :type RegistrationToken: string
        :param RegistrationToken: **[REQUIRED]**

          The identifier for this registration request.

          This registration token is generated by CloudFormation when you initiate a registration request
          using ``  RegisterType `` .

        :type WaiterConfig: dict
        :param WaiterConfig:

          A dictionary that provides parameters to control waiting behavior.

          - **Delay** *(integer) --*

            The amount of time in seconds to wait between attempts. Default: 30

          - **MaxAttempts** *(integer) --*

            The maximum number of attempts to be made. Default: 120

        :returns: None
        """
